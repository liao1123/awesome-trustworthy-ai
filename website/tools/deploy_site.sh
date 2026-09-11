#!/usr/bin/env bash
# 公开站部署：构建阅读站数据并把静态产物同步到 website/public/，
# 由 .github/workflows/pages.yml 通过 GitHub Actions 发布到 Pages。
# 站点地址：https://liao1123.github.io/awesome-trustworthy-ai/
#
# 产物（提交进仓库）：
#   website/public/index.html  app.js  style.css  data/papers.js
# 源文件仍维护在 website/reader/，本脚本负责构建 + 同步 + 暂存。
#
# 用法（在更新论文之后）：
#   tools/deploy_site.sh          # 构建 + 同步 + 暂存（随你的内容提交一起 push）
#   tools/deploy_site.sh --commit # 构建 + 同步 + 暂存 + 立即单独提交
#   tools/deploy_site.sh --push   # 构建 + 同步 + 提交 + 推送（需要 git 凭证或 GITHUB_TOKEN）

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "==> [1/3] 构建阅读站数据"
python3 website/reader/build.py

echo "==> [2/3] 同步静态产物到 website/public/"
mkdir -p "$ROOT/website/public/data"
cp website/reader/index.html website/reader/app.js website/reader/style.css "$ROOT/website/public/"
cp website/reader/data/papers.js "$ROOT/website/public/data/"
git add website/public

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
  echo "==> 产物已暂存于 website/public/，请随本次内容改动一起 commit / push（或用 --commit / --push）"
fi
