#!/usr/bin/env bash
# 本文件由 meta/build.py 生成，改这里会在下次构建时被覆盖。
# 按 index.tsv 把原件下载到 originals/。原件不入库，见 README「关于原文副本」。
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p originals
tail -n +2 index.tsv | while IFS=$'\t' read -r first updated title org genre okind topics tags url summary rationale org_context; do
  # 文件名末尾拼 URL 的短哈希：只截前 80 字符会让长 URL 撞名并静默互相覆盖。
  slug=$(printf "%s" "$url" | tr -c "A-Za-z0-9._-" "_" | cut -c1-80)
  h=$(printf "%s" "$url" | shasum -a 256 | cut -c1-8)
  out="originals/${slug}-${h}"
  if [ -s "$out" ]; then echo "已有 $title"; continue; fi
  echo "取 $title"
  # arXiv 的出处列指向 abs 页（给人读），原件要的是 PDF。
  src=$(printf "%s" "$url" | sed "s#/abs/#/pdf/#")
  # -f 不可省：没有它 curl 遇到 403/404 照样退出 0，会把错误页当原件存下来，
  # 下次运行再当成「已有」跳过，垃圾就永久留在 originals/ 里。
  if ! curl -fsSL --max-time 60 -A "Mozilla/5.0" -o "$out" "$src"; then
    # 失败要删残留：留着零字节或半截文件，下次运行会当成「已有」跳过。
    rm -f "$out"; echo "  取不到：$src"
  fi
done
