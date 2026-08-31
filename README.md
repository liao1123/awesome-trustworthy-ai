# Awesome Trustworthy AI

这个仓库用于持续收集和整理 Trustworthy AI 与 AI Safety 论文。内容由 Codex 按任务逐次检索和更新，所有结果直接保存为 Markdown。

## 目录

| 目录 | 内容 |
| --- | --- |
| [`daily/`](daily/README.md) | 每天从 arXiv 收集的新论文，按 `年-月/日期.md` 保存 |
| [`conferences/`](conferences/README.md) | 从顶会官方 accepted-paper 列表中筛选的相关论文 |
| [`domains/`](domains/README.md) | 按研究领域长期汇总日报和会议中出现的论文 |
| [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) | 当前关注的 AI Safety 范围、条件收录主题和明确排除项 |
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Markdown 结构、英文关键词、专有名词、链接和摘要写法 |

## 更新关系

```text
arXiv 当日论文 ──> daily/日期.md ──┐
                                  ├──> 去重与语义分类 ──> domains/
顶会录用列表 ──> conferences/ ────┘
```

`domains/` 中形成稳定二级分类的方向使用独立文件夹；规模较小的方向直接保存为 `misc/<domain>.md`。`daily/` 与 `conferences/` 保持各自的来源视图和筛选逻辑；领域同步先按 [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) 筛选，再对符合兴趣的论文做去重、语义分类和长期聚合，不要求来源文件中的每篇论文都进入领域页。

每次运行 Codex 时，先读取 [`RESEARCH_INTERESTS.md`](RESEARCH_INTERESTS.md) 和 [`STYLE_GUIDE.md`](STYLE_GUIDE.md)，再读取相应目录的 `README.md` 并执行其中的 Prompt。
