# Awesome Trustworthy AI

论文阅读网站：<https://liao1123.github.io/awesome-trustworthy-ai/>（tsrigo 预构建模式：静态产物同步到仓库根目录随源码提交，由 `tools/deploy_site.sh` 更新）

这个仓库用于持续收集和整理 Trustworthy AI 与 AI Safety 论文。内容由 Codex 按任务逐次检索和更新，所有结果直接保存为 Markdown。

## 目录

| 目录 | 内容 |
| --- | --- |
| [`daily/`](daily/README.md) | 每天从 arXiv 收集的新论文，按 `年-月/日期.md` 保存 |
| [`conferences/`](conferences/README.md) | 从顶会官方 accepted-paper 列表中筛选的相关论文 |
| [`domains/`](domains/README.md) | 按研究领域长期汇总日报和会议中出现的论文 |
| [`reader/`](reader/README.md) | 将 `daily/`、`domains/` 和 `conferences/` 变成统一卡片阅读流的静态网站 |
| [`tools/`](tools/) | 一次性整理管道：全仓论文索引、元数据补全、总结批次、卡片格式迁移与格式 lint |
| [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) | 当前关注的 AI Safety 范围、条件收录主题和明确排除项 |
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Markdown 结构、英文关键词、专有名词、链接和摘要写法 |

## 更新关系

```text
arXiv 当日论文 ──> daily/日期.md ──┐
                                  ├──> 去重与语义分类 ──> domains/
顶会录用列表 ──> conferences/ ────┘
```

`domains/` 中形成稳定二级分类的方向使用独立文件夹；规模较小的方向直接保存为 `misc/<domain>.md`。`daily/` 与 `conferences/` 保持各自的来源视图和筛选逻辑；领域同步先按 [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) 筛选，再对符合兴趣的论文做去重、语义分类和长期聚合，不要求来源文件中的每篇论文都进入领域页。

每篇论文统一使用卡片格式（见 [`STYLE_GUIDE.md`](STYLE_GUIDE.md)）：英文原题、类型化图标链接行（📄 arXiv / 🐙 Code / 🤗 Model / 📊 Dataset / 🌐 Project / 📝 OpenReview / 🎓 Official）加 📅 日期与 🏷 会议徽章、英文关键词、👤 作者、🎯/🔬/📌 三段式中文总结、`<details>` 折叠的英文摘要原文。同一论文在三个视图中保持同一份卡片内容。

`reader/` 是三个来源目录的展示层：运行 [`reader/build.py`](reader/build.py) 后即可得到独立的静态论文阅读网站（卡片流、⭐ 收藏、搜索、三视图导航）。Daily、Domain、Conference 在网页中保持独立入口；阅读器不维护第二套论文源数据。`reader/data/` 中的元数据缓存只在批量整理 Markdown 时使用，不回写 Markdown。

每次运行 Codex 时，先读取 [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) 和 [`STYLE_GUIDE.md`](STYLE_GUIDE.md)，再读取相应目录的 `README.md` 并执行其中的 Prompt。
