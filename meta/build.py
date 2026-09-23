# -*- coding: utf-8 -*-
"""由 catalog.py 生成 README.md、index.tsv 与 fetch.sh。

改条目只改 catalog.py，然后跑 `python3 meta/build.py`。
"""
import io
import os
import csv
import sys
import tempfile
import check
from catalog import (Item, ITEMS, TAGS, TOPICS, GENRES, ORG_KINDS,
                     NO_REDISTRIBUTION, ARXIV_NOTE)
from policy import (TITLE, SCOPE, OUT_OF_SCOPE, FIRST_DATE_RULE,
                    UPDATED_DATE_RULE, ORG_RULE, AXES_INTRO, GENRE_RULE,
                    ORG_KIND_RULE, TOPIC_BOUNDARY_RULE, TAG_RULE,
                    CONTRIBUTION_RULE, AXIS_WARNINGS)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TAG_ZH = dict(TAGS)          # 英文正名 -> 中文别名（无别名为 None）
TAG_EN = [en for en, _ in TAGS]


def with_alias(tags):
    """条目只存英文正名，展示与导出时带出中文别名，两种语言都搜得到。"""
    out = []
    for t in tags:
        out.append(t)
        if TAG_ZH.get(t):
            out.append(TAG_ZH[t])
    return out

TSV_COLUMNS = ["首发日期", "最后更新", "标题", "出品方", "体裁", "出品方类型",
               "主题", "标签", "出处"]


def widest_tag(items):
    """横跨主题最多的那个标签，用来举例说明标签不是主题的下级。

    写死成「MCP 落在 5 个主题里」会随条目增减悄悄失真——本轮那句
    「52 条里实填 70 条」就是这么来的，所以凡是会漂的数字一律算出来。
    """
    span = lambda en: len({t for i in items if en in i.tags for t in i.topics})
    best = max(TAG_EN, key=span)
    return best, span(best)


def fetch_map():
    """从 fetched.tsv 读取每个原件的抓取日期——本仓哪天确认过这个地址取得回来。"""
    out = {}
    path = os.path.join(HERE, "fetched.tsv")
    if not os.path.exists(path):
        return out
    with io.open(path, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[row["名称"]] = row["抓取日期"]
    return out


def sort_key(item):
    """按首发日期倒序；只精确到月的补 -00，排在当月之后。"""
    d = item.first
    return (d + "-00") if len(d) == 7 else d


def md(text):
    """表格单元格里的管道符要转义，否则会把 Markdown 的列打乱。"""
    return text.replace("|", "\\|")


def die(problems):
    print("校验不通过，%d 处，未生成任何文件：" % len(problems))
    for p in problems:
        print("  ✗", p)
    raise SystemExit(1)


def render_outputs():
    """在内存中生成全部文件；调用方校验通过后再一次性落盘。"""
    fetched = fetch_map()
    items = sorted((Item(*t) for t in ITEMS), key=sort_key, reverse=True)

    # ── index.tsv：机器可读 ──
    index_out = io.StringIO(newline="")
    # lineterminator 必须显式指定：csv 默认写 \r\n，
    # 会让 fetch.sh 用 read -r 切出来的最后一个字段带上游离的 \r
    w = csv.writer(index_out, delimiter="\t", lineterminator="\n")
    w.writerow(TSV_COLUMNS)
    for i in items:
        # 任何一列都不许为空：制表符是 IFS 空白字符，连续两个会被 shell 的 read
        # 当成一个分隔符吞掉，后面所有列左移一位，fetch.sh 就会拿错 url 去下载。
        w.writerow([i.first, i.updated, i.title, i.org, i.genre, i.org_kind,
                    "|".join(i.topics), "|".join(with_alias(i.tags)), i.url])
    index_text = index_out.getvalue()

    # ── README.md：给人读 ──
    # 排布按「30 秒内看到产品」：标题 → 入口点 → 清单表 → 判据（参考）→ 约束 → 许可。
    # 判据是查阅材料，放表下面；入口点在最上面，因为 doc 型仓的首要问题是「东西在哪」。
    L = []
    L.append("<!-- 本文件由 meta/build.py 生成，改这里会在下次构建时被覆盖。"
             "怎么改见下方「怎么加一条」。 -->\n")
    L.append("# %s\n" % TITLE)
    L.append(SCOPE + "\n")
    L.append(OUT_OF_SCOPE + "\n")

    L.append("## 怎么用\n")
    L.append("- **要数据**：[`index.tsv`](index.tsv)，%d 条 × %d 列，制表符分隔。列为 %s；"
             "主题与标签列内用 `|` 分隔多值，标签同时含英文正名与中文别名，两种写法都能 grep。\n"
             % (len(items), len(TSV_COLUMNS), "／".join(TSV_COLUMNS)))
    L.append("- **要翻看**：本页下方的[清单表](#清单按发布时间倒序)，按首发时间倒序。\n")
    L.append("- **要原文**：跑 [`fetch.sh`](fetch.sh)，按清单把原件下载到本地 `originals/`"
             "（已在 .gitignore 里）。取不到的会逐条报出来。\n")
    L.append("- **要加条目**：改 [`meta/catalog.py`](meta/catalog.py)；**要改判据**：改 "
             "[`meta/policy.py`](meta/policy.py)。完成后跑 `python3 meta/build.py`。\n")
    L.append("[清单](#清单按发布时间倒序) · [分类口径](#怎么分类) · "
             "[原文副本](#关于原文副本) · [添加条目](#怎么加一条) · [许可](#许可)\n")
    L.append("常用检索：\n\n```sh\nrg 'MCP' index.tsv\nrg '商业与组织' index.tsv\n```\n")
    dates = sorted({d for d in fetched.values() if d})
    got = sum(1 for i in items if fetched.get(i.key))
    L.append("**抓取记录最近更新：%s**——%d／%d 条有与当前出处一致的抓取记录，"
             "其余 %d 条只给链接。各条的实际抓取日期见 [`meta/fetched.tsv`](meta/fetched.tsv)。\n"
             % (dates[-1] if dates else "尚未核对", got, len(items), len(items) - got))

    L.append("## 清单（按发布时间倒序）\n")
    # README 只保留三列，避免窄屏把标题挤成竖条；完整九列见 index.tsv。
    # 主题与标签只在展示层合并，机器可读数据仍是两个字段。
    L.append("| 日期 | 材料 | 分类 |")
    L.append("|---|---|---|")
    for i in items:
        mark = " ⚠" if i.key in NO_REDISTRIBUTION else ""
        # 相同也不画箭头：首发当天之后没改过，写两遍等于噪声
        same = i.updated in ("-", i.first)
        when = i.first if same else "%s → %s" % (i.first, i.updated)
        material = "[%s](%s)%s<br>%s · %s · %s" % (
            md(i.title), md(i.url), mark, md(i.org), i.genre, i.org_kind)
        classification = "**主题** %s<br>**标签** %s" % (
            " ".join("`%s`" % t for t in i.topics),
            " ".join("`%s`" % t for t in with_alias(i.tags)))
        L.append("| %s | %s | %s |" % (when, material, classification))
    L.append("")
    filled = sum(1 for i in items if i.updated != "-")
    L.append("**日期列**写的是「首发 → 最后更新」，原文自首发后没改过、或改没改采集不到的，"
             "只写首发一个日期。\n")
    L.append(FIRST_DATE_RULE + "\n")
    L.append(UPDATED_DATE_RULE + "%d 条里实填 %d 条。\n" % (len(items), filled))
    L.append(ORG_RULE + "\n")
    L.append("⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 "
             "`NO_REDISTRIBUTION`。\n")

    L.append("## 怎么分类\n")
    L.append(AXES_INTRO + "\n")

    L.append("**体裁**：%d 选一，互斥。\n" % len(GENRES))
    L.append(" ｜ ".join("`%s`（%d）" % (g, sum(1 for i in items if i.genre == g)) for g in GENRES) + "\n")
    L.append(GENRE_RULE + "\n")

    L.append("**出品方类型**：%d 选一，互斥。\n" % len(ORG_KINDS))
    L.append(" ｜ ".join("`%s`（%d）" % (k, sum(1 for i in items if i.org_kind == k)) for k in ORG_KINDS) + "\n")
    L.append(ORG_KIND_RULE + "\n")

    multi = sum(1 for i in items if len(i.topics) > 1)
    L.append("**主题**：什么在被重构，分 %d 个区，每条至少一个。**可以多挂，不互斥**"
             "——一条材料同时谈两件事就挂两个区，%d 条里有 %d 条是这样，"
             "同一条出现在两个区不是重复收录。\n" % (len(TOPICS), len(items), multi))
    for t in TOPICS:
        L.append("- `%s`（%d 条）" % (t, sum(1 for i in items if t in i.topics)))
    L.append("\n" + TOPIC_BOUNDARY_RULE + "\n")

    L.append(TAG_RULE + "例如，`%s` 一个词就落在 %d 个主题里。\n" % widest_tag(items))
    L.append("| 英文标签 | 中文别名 | 条目数 |")
    L.append("|---|---|---:|")
    for en, zh in TAGS:
        L.append("| `%s` | %s | %d |" % (
            en, ("`%s`" % zh) if zh else "—",
            sum(1 for i in items if en in i.tags)))
    L.append("")

    L.append("## 关于原文副本\n")
    L.append("**本仓不分发原文副本**，只给标题、链接、日期与标签。原因：\n")
    L.append("- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——"
             "作者授权 arXiv 分发，**未授权第三方转载**\n")
    L.append("- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载\n")
    L.append("**本仓也不记原件指纹**：收录的条目多数是持续更新的网页，GitHub 页面还内嵌 "
             "csrf 令牌与实时星数，同一秒抓两次校验值都不同——记了也核对不了，"
             "只会一直假报不一致。取原件的办法见上方「怎么用」。\n")

    L.append("## 怎么加一条\n")
    L.append("改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`；分类判据在 "
             "[`meta/policy.py`](meta/policy.py)。完成后跑 `python3 meta/build.py` 重新生成。"
             + CONTRIBUTION_RULE + "\n")
    L.append("生成前会先跑 [`meta/check.py`](meta/check.py)：日期是否真实存在、"
             "最后更新不得早于首发、四轴取值是否在词表内、同一行标题与出品方是否同语言、"
             "出处与原件键是否重复、标签是否与某个主题圈了同一堆材料。"
             "**任一项不过就不生成任何文件**，错在哪会逐条打出来。\n")
    L.append("本地回归测试：`python3 -m unittest discover -s meta -p 'test_*.py'`。\n")
    L.append("定轴时两条别踩：\n")
    for warning in AXIS_WARNINGS:
        L.append("- %s" % warning)
    L.append("")
    L.append("## 许可\n")
    L.append("**许可只覆盖本仓自有的那部分**：条目的挑选与标签、`index.tsv`、"
             "`meta/` 下的脚本、以及本文的说明文字——以 [CC0 1.0](LICENSE) 置于公有领域，"
             "拿去用不必署名、不必告知。\n")
    L.append("**被收录材料的版权归各自权利人**，本仓一份副本都不分发，"
             "链接一律指向其原始出处。**CC0 不适用于它们**——"
             "把某篇论文或某份标准转发出去之前，看它自己的许可。\n")

    readme_text = "\n".join(L)

    # ── fetch.sh ──
    lines = ["#!/usr/bin/env bash",
             "# 本文件由 meta/build.py 生成，改这里会在下次构建时被覆盖。",
             "# 按 index.tsv 把原件下载到 originals/。原件不入库，见 README「关于原文副本」。",
             "set -euo pipefail",
             'cd "$(dirname "$0")"',
             "mkdir -p originals",
             'tail -n +2 index.tsv | while IFS=$\'\\t\' read -r first updated title org genre okind topics tags url; do',
             '  # 文件名末尾拼 URL 的短哈希：只截前 80 字符会让长 URL 撞名并静默互相覆盖。',
             '  slug=$(printf "%s" "$url" | tr -c "A-Za-z0-9._-" "_" | cut -c1-80)',
             '  h=$(printf "%s" "$url" | shasum -a 256 | cut -c1-8)',
             '  out="originals/${slug}-${h}"',
             '  if [ -s "$out" ]; then echo "已有 $title"; continue; fi',
             '  echo "取 $title"',
             '  # arXiv 的出处列指向 abs 页（给人读），原件要的是 PDF。',
             '  src=$(printf "%s" "$url" | sed "s#/abs/#/pdf/#")',
             '  # -f 不可省：没有它 curl 遇到 403/404 照样退出 0，会把错误页当原件存下来，',
             '  # 下次运行再当成「已有」跳过，垃圾就永久留在 originals/ 里。',
             '  if ! curl -fsSL --max-time 60 -A "Mozilla/5.0" -o "$out" "$src"; then',
             '    # 失败要删残留：留着零字节或半截文件，下次运行会当成「已有」跳过。',
             '    rm -f "$out"; echo "  取不到：$src"',
             '  fi',
             "done"]
    fetch_text = "\n".join(lines) + "\n"

    return items, {
        "README.md": readme_text,
        "index.tsv": index_text,
        "fetch.sh": fetch_text,
    }


def write_outputs(outputs):
    """全部内容校验后，以同目录临时文件逐个原子替换目标。"""
    pending = []
    try:
        for name, content in outputs.items():
            fd, tmp = tempfile.mkstemp(prefix=".%s." % name, dir=ROOT, text=True)
            pending.append((tmp, os.path.join(ROOT, name)))
            with io.open(fd, "w", encoding="utf-8", newline="") as fh:
                fh.write(content)
                fh.flush()
                os.fsync(fh.fileno())
            os.chmod(tmp, 0o755 if name == "fetch.sh" else 0o644)
        for tmp, target in pending:
            os.replace(tmp, target)
        pending = []
    finally:
        for tmp, _ in pending:
            try:
                os.unlink(tmp)
            except FileNotFoundError:
                pass


def check_written_outputs(outputs):
    """逐字比较已落盘文件与内存渲染结果。"""
    bad = []
    for name, content in outputs.items():
        path = os.path.join(ROOT, name)
        if not os.path.exists(path):
            bad.append("%s 还没生成" % name)
            continue
        with io.open(path, encoding="utf-8", newline="") as fh:
            if fh.read() != content:
                bad.append("%s 与生成源不一致；请运行 python3 meta/build.py" % name)
    fetch = os.path.join(ROOT, "fetch.sh")
    if os.path.exists(fetch) and not os.access(fetch, os.X_OK):
        bad.append("fetch.sh 缺少可执行权限；请运行 python3 meta/build.py")
    return bad


def check_generated():
    """供 check.py 调用的只读生成物一致性检查。"""
    try:
        _, outputs = render_outputs()
        bad = check_written_outputs(outputs)
    except (KeyError, TypeError, ValueError) as error:
        bad = ["无法渲染生成物：%s；请先运行 python3 meta/check.py 修复数据" % error]
    if bad:
        for problem in bad:
            print(problem)
        return 1
    return 0


def main():
    # 先在内存中生成并校验，任何校验失败都不会碰现有生成物。
    bad = check.run("数据")
    if bad:
        die(bad)
    items, outputs = render_outputs()
    bad = check.check_index_text(outputs["index.tsv"])
    if bad:
        die(bad)
    write_outputs(outputs)

    print("生成完毕：%d 条；README.md、index.tsv、fetch.sh（校验通过）" % len(items))
    print("提示：", ARXIV_NOTE)


if __name__ == "__main__":
    if sys.argv[1:] == ["--check-generated"]:
        raise SystemExit(check_generated())
    if sys.argv[1:]:
        print("用法：python3 meta/build.py [--check-generated]")
        raise SystemExit(2)
    main()
