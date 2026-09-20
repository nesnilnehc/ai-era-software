# -*- coding: utf-8 -*-
"""由 catalog.py 生成 README.md、index.tsv 与 fetch.sh。

改条目只改 catalog.py，然后跑 `python3 meta/build.py`。
"""
import io
import os
import csv
from collections import namedtuple
from catalog import ITEMS, TAGS, GENRES, ORG_KINDS, NO_REDISTRIBUTION, ARXIV_NOTE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# 具名字段：条目元组这轮已经改过三次形状，用位置下标统计必然悄悄算错
Item = namedtuple("Item", "first updated title org genre org_kind topics tags url key")

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

TOPICS = ["界面与接入", "应用内部", "构造方式", "安全与攻防", "运行与问责",
          "协议与生态", "商业与组织"]


def sha_map():
    """从 fetched.tsv 读取每个原件的 sha256、体积与最后核对日期。"""
    out = {}
    path = os.path.join(HERE, "fetched.tsv")
    if not os.path.exists(path):
        return out
    with io.open(path, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[row["名称"]] = (row["sha256"], row["原始字节"], row["抓取日期"])
    return out


def sort_key(item):
    """按首发日期倒序；只精确到月的补 -00，排在当月之后。"""
    d = item[0]
    return (d + "-00") if len(d) == 7 else d


def main():
    shas = sha_map()
    items = [Item(*t) for t in sorted(ITEMS, key=sort_key, reverse=True)]

    # ── index.tsv：机器可读 ──
    with io.open(os.path.join(ROOT, "index.tsv"), "w", encoding="utf-8", newline="") as fh:
        # lineterminator 必须显式指定：csv 默认写 \r\n，
        # 会让 fetch.sh 用 read -r 切出来的最后一个字段带上游离的 \r
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["首发日期", "最后更新", "标题", "出品方", "体裁", "出品方类型",
                    "主题", "标签", "出处", "原件sha256", "原件字节"])
        for i in items:
            sha, size, _ = shas.get(i.key, ("", "", ""))
            # 中间列不许为空：制表符是 IFS 空白字符，连续两个会被 shell 的 read 当成
            # 一个分隔符吞掉，后面所有列左移一位，fetch.sh 就会拿错 url 去下载。
            # 末尾的 sha/size 可以为空，read 会把尾部空字段一并剥掉，不影响前面的列。
            w.writerow([i.first, i.updated, i.title, i.org, i.genre, i.org_kind,
                        "|".join(i.topics), "|".join(with_alias(i.tags)), i.url, sha, size])

    # ── README.md：给人读 ──
    L = []
    L.append("# AI 时代的软件重构 · 材料清单\n")
    L.append("收集「软件本身因 AI 被怎样改写」的一手材料：论文、厂商文档与公告、标准文件、"
             "分析与投资机构的公开报告、社区维护的清单。\n")
    L.append("**本仓只做三件事：收集、打标签、按发布时间排序。不做解读，不写评价。**\n")
    L.append("机器可读版在 [`index.tsv`](index.tsv)。\n")
    dates = sorted({v[2] for v in shas.values() if v[2]})
    got = sum(1 for i in items if shas.get(i.key, ("", "", ""))[0])
    L.append("**本清单最后核对：%s**——那天按清单取回 %d／%d 份原件并留下 sha256。"
             "核对是整份清单的属性，不是每行的：这 %d 条是同一天抓的。"
             "跑 [`fetch.sh`](fetch.sh) 会拿当下的原件和记录的 sha256 比对，"
             "不一致就说明原文自那天起改过。\n"
             % (dates[-1] if dates else "尚未核对", got, len(items), len(items)))

    L.append("## 关于原文副本\n")
    L.append("**本仓不分发原文副本**，只给标题、链接、发布日期、标签，以及"
             "**每份原件的 sha256**（供核对你取回的是不是同一份）。原因：\n")
    L.append("- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——"
             "作者授权 arXiv 分发，**未授权第三方转载**\n")
    L.append("- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载\n")
    L.append("\n要原文，跑 [`fetch.sh`](fetch.sh)，它按清单把原件下载到本地 `originals/`（已在 .gitignore 里）。\n")

    L.append("## 怎么分类\n")
    L.append("四根轴互相独立，各答一个问题，**不叠在一起**：体裁问这份材料是什么形态，"
             "出品方类型问谁出的，主题问什么在被重构，标签是横切主题的检索词。\n")

    L.append("**体裁**：六选一，互斥。\n")
    L.append(" ｜ ".join("`%s`（%d）" % (g, sum(1 for i in items if i.genre == g)) for g in GENRES) + "\n")
    L.append("`论文` 发在 arXiv、会议、期刊上的｜`规范` 约束他人的规范文本，"
             "协议规范、风险框架、监管文件、行业基线、API 政策｜`文档` 出品方自家的说明，"
             "开发者文档、官网说明页、产品页、定价页｜`清单` 第三方汇编的清单、时间线、评分表｜"
             "`报告` 有方法有数据的调研或评估出版物｜`文章` 单篇观点、公告、工程博客。\n")

    L.append("**出品方类型**：八选一，互斥。\n")
    L.append(" ｜ ".join("`%s`（%d）" % (k, sum(1 for i in items if i.org_kind == k)) for k in ORG_KINDS) + "\n")
    L.append("先看有没有混：同时含大学院所与公司归 `产学合作`，只含其一归 `学界` 或 `厂商`。"
             "标准化机构与协议项目归 `标准组织`，非营利组织与独立研究组织归 `社区与非营利`，"
             "个人署名或原文未署机构归 `个人`。\n")
    L.append("体裁和出品方类型是两个问题，别混成一根轴——厂商能发论文，公司能维护清单，"
             "非营利组织能出规范。混成一根就得靠没写下来的优先级维持互斥，"
             "下一个人加条目时必然走样。\n")

    multi = sum(1 for i in items if len(i.topics) > 1)
    L.append("**主题**：什么在被重构，分七个区，每条至少一个。**可以多挂，不互斥**"
             "——一条材料同时谈两件事就挂两个区，%d 条里有 %d 条是这样，"
             "同一条出现在两个区不是重复收录。\n" % (len(items), multi))
    for t in TOPICS:
        L.append("- `%s`（%d 条）" % (t, sum(1 for i in items if t in i.topics)))
    L.append("\n`安全与攻防` 与 `运行与问责` 的分界：材料谈的是**怎么被攻破、怎么防住**"
             "（威胁、漏洞、越权、隔离、安全普查），还是**跑起来之后谁管、按什么规矩管、"
             "出事谁负责**（法规、风险框架、可观测、管控面、责任边界）。\n")

    L.append("**标签**：材料谈的具体对象或取证方式，一条可带多个，供跨主题检索。**英文是正名，中文是别名**，同一条两个都列出来，按哪种写法搜都找得到。"
             "它横着穿过主题，不在主题之下——`MCP` 一个词就落在 5 个主题里。\n")
    L.append(" ｜ ".join(
        "`%s`%s（%d）" % (en, ("／`%s`" % zh) if zh else "",
                        sum(1 for i in items if en in i.tags))
        for en, zh in TAGS) + "\n")
    L.append("加新标签有一条规矩：**它若和某个主题圈住的是同一堆材料，就不要它**"
             "——主题已经承担了，两个名字指一件事，用的人不知道该按哪个找。\n")

    L.append("## 清单（按发布时间倒序）\n")
    L.append("| 首发 | 最后更新 | 标题 | 出品方 | 体裁 | 出品方类型 | 主题 | 标签 |")
    L.append("|---|---|---|---|---|---|---|---|")
    for i in items:
        mark = " ⚠" if i.key in NO_REDISTRIBUTION else ""
        L.append("| %s | %s | [%s](%s)%s | %s | %s | %s | %s | %s |"
                 % (i.first, i.updated, i.title.replace("|", "\\|"), i.url, mark,
                    i.org, i.genre, i.org_kind,
                    " ".join("`%s`" % t for t in i.topics),
                    " ".join("`%s`" % t for t in with_alias(i.tags))))
    L.append("")
    filled = sum(1 for i in items if i.updated != "-")
    L.append("**首发**是原文第一次出现的日子：论文取 arXiv v1 的投稿日，代码仓取仓库创建日，"
             "网页取互联网档案馆最早快照——快照是**下界**，只能证明该 URL 至少此时已存在。\n")
    L.append("**最后更新**默认是 `-`，**只有实际采集到明确信号才填日期**：论文有修订版的取修订日，"
             "代码仓取最后推送。未修订的论文、一次性的文章与公告都不拿首发日回填——那是推断，"
             "不是采集。52 条里实填 %d 条。\n" % filled)
    L.append("**出品方**按原文署名的机构填写。arXiv 摘要页不带机构信息，这一列取自正文首页"
             "（HTML 版的作者块，或 PDF 第 1 页）；原文通篇未署机构的，直接写明"
             "「原文未署机构」并附作者名。\n")
    L.append("⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 "
             "`NO_REDISTRIBUTION`。\n")

    L.append("## 怎么加一条\n")
    L.append("改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`，跑 `python3 meta/build.py` 重新生成。"
             "**只填事实字段，不要写评价**——评价一旦进来，这份清单就变成了某个人的观点集，"
             "别人就没法直接拿去用。\n")
    L.append("## 许可\n")
    L.append("**许可只覆盖本仓自有的那部分**：条目的挑选与标签、`index.tsv`、"
             "`meta/` 下的脚本、以及本文的说明文字——以 [CC0 1.0](LICENSE) 置于公有领域，"
             "拿去用不必署名、不必告知。\n")
    L.append("\n**被收录材料的版权归各自权利人**，本仓一份副本都不分发，"
             "链接一律指向其原始出处。**CC0 不适用于它们**——"
             "把某篇论文或某份标准转发出去之前，看它自己的许可。\n")

    io.open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(L))

    # ── fetch.sh ──
    lines = ["#!/usr/bin/env bash",
             "# 按 index.tsv 把原件下载到 originals/。原件不入库，见 README「关于原文副本」。",
             "set -euo pipefail",
             'cd "$(dirname "$0")"',
             "mkdir -p originals",
             'tail -n +2 index.tsv | while IFS=$\'\\t\' read -r d checked title org genre okind topics tags url sha size; do',
             '  [ -z "$sha" ] && continue',
             '  name=$(printf "%s" "$url" | tr -c "A-Za-z0-9._-" "_" | cut -c1-90)',
             '  out="originals/$name"',
             '  if [ -s "$out" ]; then echo "已有 $name"; continue; fi',
             '  echo "取 $title"',
             '  # arXiv 的出处列指向 abs 页（给人读），原件与 sha256 记的是 PDF，',
             '  # 这里要把地址换成 PDF，否则下回来的是网页，校验必然假报不一致。',
             '  src=$(printf "%s" "$url" | sed "s#/abs/#/pdf/#")',
             '  curl -sSL --max-time 60 -A "Mozilla/5.0" -o "$out" "$src" || echo "  取不到：$src"',
             '  got=$(shasum -a 256 "$out" 2>/dev/null | cut -d" " -f1 || true)',
             '  [ "$got" = "$sha" ] && echo "  校验一致" || echo "  ⚠ 与清单记录的 sha256 不一致（页面可能已改版）"',
             "done"]
    p = os.path.join(ROOT, "fetch.sh")
    io.open(p, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    os.chmod(p, 0o755)

    print("生成完毕：%d 条；README.md、index.tsv、fetch.sh" % len(items))
    print("提示：", ARXIV_NOTE)


if __name__ == "__main__":
    main()
