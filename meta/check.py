# -*- coding: utf-8 -*-
"""条目与生成物的不变量校验。

`build.py` 生成前后各调用一次；也可单独跑：`python3 meta/check.py`。

这些检查以前只存在于一次性的 shell 命令里，出过三次事：写死的条目数、位置下标
静默算错标签计数、TSV 中间列为空导致 shell 读取时整行错位。固化在这里，改完
catalog.py 跑一次就知道坏没坏。
"""
import io
import os
import re
import csv
import datetime
from catalog import ITEMS, TAGS, TOPICS, GENRES, ORG_KINDS, NO_REDISTRIBUTION

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def valid_date(text):
    """精确到月或到日都算合法，但必须是真实存在的日期。

    只用正则验形状不够：`^\\d{4}-\\d{2}(-\\d{2})?$` 会放过 2026-13-99，
    13 当月份、99 当日期照样匹配。必须真解析一次。
    """
    # 先卡补零的形状：strptime 会接受 2026-1-1，而那种写法按字符串排序会排错位置
    if not re.match(r"^\d{4}-\d{2}(-\d{2})?$", text):
        return False
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            datetime.datetime.strptime(text, fmt)
            return True
        except ValueError:
            pass
    return False

CJK = re.compile(r"[一-鿿]")
FIELDS = "first updated title org genre org_kind topics tags url key"
TAG_EN = [en for en, _ in TAGS]
TAG_ZH = dict(TAGS)
# 标签与主题重合到这个比例以上，说明两个名字圈的是同一堆材料，留一个就够
OVERLAP_MAX = 0.7


def _rows():
    """把 ITEMS 转成 dict，避免位置下标——元组形状改过三次，下标必然算错。"""
    names = FIELDS.split()
    return [dict(zip(names, t)) for t in ITEMS]


def check_data():
    """校验 catalog.py 本身。返回问题列表，空列表表示全部通过。"""
    bad = []
    rows = _rows()

    def fail(row, msg):
        bad.append("%s ｜ %s" % (row["title"][:46], msg))

    for r in rows:
        if not valid_date(r["first"]):
            fail(r, "首发日期格式不对：%s" % r["first"])
        if r["updated"] != "-":
            if not valid_date(r["updated"]):
                fail(r, "最后更新格式不对：%s" % r["updated"])
            elif r["updated"] < r["first"]:
                fail(r, "最后更新早于首发：%s < %s" % (r["updated"], r["first"]))
        if r["genre"] not in GENRES:
            fail(r, "体裁不在词表内：%s" % r["genre"])
        if r["org_kind"] not in ORG_KINDS:
            fail(r, "出品方类型不在词表内：%s" % r["org_kind"])
        if not r["topics"]:
            fail(r, "没有主题")
        for t in r["topics"]:
            if t not in TOPICS:
                fail(r, "主题不在词表内：%s" % t)
        if not r["tags"]:
            fail(r, "没有标签")
        for t in r["tags"]:
            if t not in TAG_EN:
                fail(r, "标签不在词表内：%s" % t)
            if CJK.search(t):
                fail(r, "条目里混进了中文标签：%s（只存英文正名，中文由 TAGS 带出）" % t)
        # 同一行的标题与出品方必须同语言：中文原文的条目两列都中文，英文的都英文
        if bool(CJK.search(r["title"])) != bool(CJK.search(r["org"])):
            fail(r, "标题与出品方语言不一致：%s ／ %s" % (r["title"][:24], r["org"][:24]))
        if not r["url"].startswith("http"):
            fail(r, "出处不是网址：%s" % r["url"])

    for name, seq in (("出处", [r["url"] for r in rows]),
                      ("原件键", [r["key"] for r in rows if r["key"]])):
        dup = sorted({x for x in seq if seq.count(x) > 1})
        if dup:
            bad.append("%s 重复：%s" % (name, "、".join(dup)))

    missing = sorted(set(NO_REDISTRIBUTION) - {r["key"] for r in rows if r["key"]})
    if missing:
        bad.append("NO_REDISTRIBUTION 指向不存在的条目：%s" % "、".join(missing))

    alias = [z for z in TAG_ZH.values() if z]
    clash = sorted(set(alias) & (set(TOPICS) | set(GENRES) | set(ORG_KINDS)))
    if clash:
        bad.append("标签别名与其他轴撞名：%s" % "、".join(clash))
    dup_alias = sorted({a for a in alias if alias.count(a) > 1})
    if dup_alias:
        bad.append("标签别名重复：%s" % "、".join(dup_alias))

    unused = [en for en in TAG_EN if not any(en in r["tags"] for r in rows)]
    if unused:
        bad.append("词表里有没被任何条目用到的标签：%s" % "、".join(unused))

    for en in TAG_EN:
        a = {r["url"] for r in rows if en in r["tags"]}
        for tp in TOPICS:
            b = {r["url"] for r in rows if tp in r["topics"]}
            if a and b and len(a & b) / len(a | b) >= OVERLAP_MAX:
                bad.append("标签 `%s` 与主题 `%s` 圈的是同一堆材料（重合 %.0f%%），留一个就够"
                           % (en, tp, 100.0 * len(a & b) / len(a | b)))
    return bad


def check_fetched():
    """校验 fetched.tsv 与 catalog.py 对得上。"""
    bad = []
    path = os.path.join(HERE, "fetched.tsv")
    if not os.path.exists(path):
        return bad
    with io.open(path, encoding="utf-8") as fh:
        rec = {r["名称"] for r in csv.DictReader(fh, delimiter="\t")}
    keys = {r["key"] for r in _rows() if r["key"]}
    orphan = sorted(rec - keys)
    if orphan:
        bad.append("fetched.tsv 有孤儿记录，catalog.py 已不引用：%s" % "、".join(orphan))
    dangling = sorted(keys - rec)
    if dangling:
        bad.append("catalog.py 引用了 fetched.tsv 里没有的键：%s" % "、".join(dangling))
    return bad


def check_index_tsv():
    """校验生成出来的 index.tsv：列数一致，且没有空列。

    制表符是 IFS 空白字符，连续两个会被 shell 的 read 当成一个分隔符吞掉，
    后面所有列左移一位，fetch.sh 就会拿错 url 去下载。所以一列都不许为空。
    """
    bad = []
    path = os.path.join(ROOT, "index.tsv")
    if not os.path.exists(path):
        return ["index.tsv 还没生成"]
    with io.open(path, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    if "\r" in raw:
        bad.append("index.tsv 含 \\r：行尾必须是 LF，否则 shell 切出的末列会带游离字符")
    rows = list(csv.reader(io.StringIO(raw), delimiter="\t"))
    width = len(rows[0])
    for n, r in enumerate(rows[1:], start=2):
        if len(r) != width:
            bad.append("index.tsv 第 %d 行有 %d 列，表头是 %d 列" % (n, len(r), width))
        for k, c in enumerate(r):
            if not c:
                bad.append("index.tsv 第 %d 行第 %d 列为空（%s）" % (n, k + 1, rows[0][k]))
    return bad


def run(stage="全部"):
    bad = []
    if stage in ("全部", "数据"):
        bad += check_data() + check_fetched()
    if stage in ("全部", "生成物"):
        bad += check_index_tsv()
    return bad


if __name__ == "__main__":
    import sys
    problems = run()
    if problems:
        print("校验不通过，%d 处：" % len(problems))
        for p in problems:
            print("  ✗", p)
        sys.exit(1)
    print("校验通过：%d 条条目，%d 个标签，%d 个主题" % (len(ITEMS), len(TAGS), len(TOPICS)))
