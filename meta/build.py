# -*- coding: utf-8 -*-
"""由 catalog.py 生成 README.md、index.tsv 与 fetch.sh。

改条目只改 catalog.py，然后跑 `python3 meta/build.py`。
"""
import io
import os
import csv
from catalog import ITEMS, NO_REDISTRIBUTION, ARXIV_NOTE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TOPICS = ["界面与接入", "应用内部", "构造方式", "运行与治理", "协议与生态", "商业与组织"]
KINDS = ["论文", "厂商", "标准", "分析", "投资", "社区"]


def sha_map():
    """从 fetched.tsv 读取每个原件的 sha256 与体积。"""
    out = {}
    path = os.path.join(HERE, "fetched.tsv")
    if not os.path.exists(path):
        return out
    with io.open(path, encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[row["名称"]] = (row["sha256"], row["原始字节"], row["原始类型"])
    return out


def sort_key(item):
    """按发布日期倒序；只精确到月的补 -00，排在当月之后。"""
    d = item[0]
    return (d + "-00") if len(d) == 7 else d


def main():
    shas = sha_map()
    items = sorted(ITEMS, key=sort_key, reverse=True)

    # ── index.tsv：机器可读 ──
    with io.open(os.path.join(ROOT, "index.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["发布日期", "标题", "出品方", "类型", "主题标签", "出处", "原件sha256", "原件字节"])
        for d, title, org, kind, topics, url, key in items:
            sha, size, _ = shas.get(key, ("", "", ""))
            w.writerow([d, title, org, kind, "|".join(topics), url, sha, size])

    # ── README.md：给人读 ──
    L = []
    L.append("# AI 时代的软件重构 · 材料清单\n")
    L.append("收集「软件本身因 AI 被怎样改写」的一手材料：论文、厂商文档与公告、标准文件、"
             "分析与投资机构的公开报告、社区维护的清单。\n")
    L.append("**本仓只做三件事：收集、打标签、按发布时间排序。不做解读，不写评价。**\n")
    L.append("机器可读版在 [`index.tsv`](index.tsv)。\n")

    L.append("## 关于原文副本\n")
    L.append("**本仓不分发原文副本**，只给标题、链接、发布日期、标签，以及"
             "**每份原件的 sha256**（供核对你取回的是不是同一份）。原因：\n")
    L.append("- 收录的 arXiv 论文，许可为 `nonexclusive-distrib/1.0`——"
             "作者授权 arXiv 分发，**未授权第三方转载**\n")
    L.append("- 厂商页面与部分标准文件另有版权声明，其中一份明文禁止转载\n")
    L.append("\n要原文，跑 [`fetch.sh`](fetch.sh)，它按清单把原件下载到本地 `originals/`（已在 .gitignore 里）。\n")

    L.append("## 标签\n")
    L.append("**主题**按「什么在被重构」分六类，不按角色分：\n")
    for t in TOPICS:
        n = sum(1 for i in items if t in i[4])
        L.append("- `%s`（%d 条）" % (t, n))
    L.append("\n**类型**：" + " ｜ ".join("`%s`（%d）" % (k, sum(1 for i in items if i[3] == k)) for k in KINDS) + "\n")

    L.append("## 清单（按发布时间倒序）\n")
    L.append("| 发布 | 标题 | 出品方 | 类型 | 主题 |")
    L.append("|---|---|---|---|---|")
    for d, title, org, kind, topics, url, key in items:
        mark = " ⚠" if key in NO_REDISTRIBUTION else ""
        L.append("| %s | [%s](%s)%s | %s | %s | %s |"
                 % (d, title.replace("|", "\\|"), url, mark, org, kind,
                    " ".join("`%s`" % t for t in topics)))
    L.append("")
    L.append("⚠ 标记的条目连原件也不要自行转发，理由见 [`meta/catalog.py`](meta/catalog.py) 的 "
             "`NO_REDISTRIBUTION`。\n")

    L.append("## 怎么加一条\n")
    L.append("改 [`meta/catalog.py`](meta/catalog.py) 里的 `ITEMS`，跑 `python3 meta/build.py` 重新生成。"
             "**只填事实字段，不要写评价**——评价一旦进来，这份清单就变成了某个人的观点集，"
             "别人就没法直接拿去用。\n")
    L.append("## 许可\n")
    L.append("本仓自有内容（清单、标签、脚本）以 CC0 发布，随便用。"
             "**所收录材料的版权归各自权利人**，链接指向其原始出处。\n")

    io.open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write("\n".join(L))

    # ── fetch.sh ──
    lines = ["#!/usr/bin/env bash",
             "# 按 index.tsv 把原件下载到 originals/。原件不入库，见 README「关于原文副本」。",
             "set -euo pipefail",
             'cd "$(dirname "$0")"',
             "mkdir -p originals",
             'tail -n +2 index.tsv | while IFS=$\'\\t\' read -r d title org kind topics url sha size; do',
             '  [ -z "$sha" ] && continue',
             '  name=$(printf "%s" "$url" | tr -c "A-Za-z0-9._-" "_" | cut -c1-90)',
             '  out="originals/$name"',
             '  if [ -s "$out" ]; then echo "已有 $name"; continue; fi',
             '  echo "取 $title"',
             '  curl -sSL --max-time 60 -A "Mozilla/5.0" -o "$out" "$url" || echo "  取不到：$url"',
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
