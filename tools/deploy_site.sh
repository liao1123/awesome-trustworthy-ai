#!/usr/bin/env bash
# tsrigo 模式部署：本地构建阅读站，把静态产物同步到仓库根目录并提交，
# GitHub Pages（Deploy from branch: main / root）直接服务仓库内容。
# 站点地址：https://liao1123.github.io/awesome-trustworthy-ai/
#
# 产物（提交进仓库）：
#   index.html  app.js  style.css  data/papers.js
# 源文件仍维护在 reader/，本脚本负责构建 + 同步。
#
# 用法（在更新论文之后）：
#   tools/deploy_site.sh          # 构建 + 同步 + 暂存（随你的内容提交一起 push）
#   tools/deploy_site.sh --commit # 构建 + 同步 + 暂存 + 立即单独提交
#   tools/deploy_site.sh --push   # 构建 + 同步 + 提交 + 推送（需要 git 凭证或 GITHUB_TOKEN）

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> [1/3] 构建阅读站数据"
python3 reader/build.py

echo "==> [2/3] 同步静态产物到仓库根目录"
cp reader/index.html reader/app.js reader/style.css "$ROOT/"
mkdir -p "$ROOT/data"
cp reader/data/papers.js "$ROOT/data/"
git add index.html app.js style.css data/papers.js

MODE="${1:-}"
case "$MODE" in
  --commit|--push)
    STAMP="$(TZ='Asia/Shanghai' date '+%Y-%m-%d %H:%M:%S CST')"
    git commit -m "$STAMP - 更新阅读站静态产物" 1>&2
    echo "==> 已提交：$STAMP - 更新阅读站静态产物"
    ;;
esac

if [[ "$MODE" == "--push" ]]; then
  echo "==> [3/3] 推送"
  if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    PUSH_URL="https://x-access-token:${GITHUB_TOKEN}@github.com/liao1123/awesome-trustworthy-ai.git"
    git push "$PUSH_URL" HEAD:main 1>&2
  else
    git push origin HEAD 1>&2
  fi
  echo "==> 完成：https://liao1123.github.io/awesome-trustworthy-ai/"
else
  echo "==> 产物已暂存于仓库根目录，请随本次内容改动一起 commit / push（或用 --commit / --push）"
fi
