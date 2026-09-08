# Paper Reader

这是 `awesome-trustworthy-ai` 的独立论文阅读器。它把 `daily/`、`domains/` 和 `conferences/` 中的卡片格式 Markdown 转成统一的卡片阅读流；三个入口彼此独立，Markdown 仍然是论文清单、归属和阅读笔记的唯一源数据，不要直接编辑 `data/` 下的生成文件。

## 构建数据

在仓库根目录执行：

```bash
python3 reader/build.py
```

脚本会完成以下工作：

- 解析三个来源目录中所有卡片格式论文条目（图标链接行、关键词、作者、三段式总结、`<details>` 折叠摘要）；
- 按 arXiv ID（缺失时用规范化英文标题）合并交叉收录的同一论文，链接取并集、字段取最优；
- 输出 `reader/data/papers.js`（页面直接加载的浏览器数据）。

## 页面功能

- **三个视图**：日报（按日期）、领域（按核心领域分组）、会议（按会议与年份），左侧折叠导航；
- **卡片**：标题直达 arXiv、类型徽章（arXiv/Code/Model/Dataset/Project/OpenReview/Official）、📅 日期与 🏷 会议徽章、关键词 pill（点击即搜索）、👤 作者、🎯/🔬/📌 三段式总结、可展开英文摘要；
- **⭐ 收藏**：卡片右上角星标（整卡高亮），保存在浏览器 `localStorage`（沿用旧的 `trustworthy-ai-paper-reader:` 前缀，历史收藏状态保留），顶栏“只看收藏”一键筛选；
- **搜索**：标题/作者/关键词/总结实时过滤；
- **懒加载**：滚动增量渲染，3,000+ 卡片不卡顿；明暗主题切换；回到顶部。

## 本地预览

```bash
python3 -m http.server 8000
```

打开 <http://127.0.0.1:8000/>（仓库根目录即站点；也可开 `/reader/` 源文件副本）。

## GitHub Pages

采用 tsrigo/ICML2026-Guide-CN 的预构建模式：**静态产物同步到仓库根目录并随源码提交**（`index.html`、`app.js`、`style.css`、`data/papers.js`），Pages 用 Deploy from a branch（`main` / root）服务，无 CI 依赖。

更新论文后运行：

```bash
tools/deploy_site.sh            # 构建 + 同步到根目录 + 暂存，随内容一起 commit/push
tools/deploy_site.sh --commit   # 构建 + 同步 + 单独提交
tools/deploy_site.sh --push     # 构建 + 同步 + 提交 + 推送（可设 GITHUB_TOKEN）
```

站点地址：<https://liao1123.github.io/awesome-trustworthy-ai/>

## 元数据缓存

`reader/data/arxiv_metadata.json` 缓存 arXiv 元数据（标题、作者、摘要、提交日期），由 `tools/collect_index.py` → `tools/join_metadata.py` → `tools/fetch_missing.py` 管道维护，用于卡片作者与摘要补全。构建时 Markdown 已携带全部卡片字段，该缓存只在批量修复 Markdown 时使用。
