#!/usr/bin/env bash
# 按 index.tsv 把原件下载到 originals/。原件不入库，见 README「关于原文副本」。
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p originals
tail -n +2 index.tsv | while IFS=$'\t' read -r d checked title org genre okind topics tags url sha size; do
  [ -z "$sha" ] && continue
  name=$(printf "%s" "$url" | tr -c "A-Za-z0-9._-" "_" | cut -c1-90)
  out="originals/$name"
  if [ -s "$out" ]; then echo "已有 $name"; continue; fi
  echo "取 $title"
  # arXiv 的出处列指向 abs 页（给人读），原件与 sha256 记的是 PDF，
  # 这里要把地址换成 PDF，否则下回来的是网页，校验必然假报不一致。
  src=$(printf "%s" "$url" | sed "s#/abs/#/pdf/#")
  curl -sSL --max-time 60 -A "Mozilla/5.0" -o "$out" "$src" || echo "  取不到：$src"
  got=$(shasum -a 256 "$out" 2>/dev/null | cut -d" " -f1 || true)
  [ "$got" = "$sha" ] && echo "  校验一致" || echo "  ⚠ 与清单记录的 sha256 不一致（页面可能已改版）"
done
