# Awesome Trustworthy AI

这个仓库用于持续收集和整理 Trustworthy AI 与 AI Safety 论文。内容由 Codex 按任务逐次检索和更新，所有结果直接保存为 Markdown。

## 目录

| 目录 | 内容 |
| --- | --- |
| [`daily/`](daily/README.md) | 每天从 arXiv 收集的新论文，按 `年-月/日期.md` 保存 |
| [`conferences/`](conferences/README.md) | 从顶会官方 accepted-paper 列表中筛选的相关论文 |
| [`domains/`](domains/README.md) | 按研究领域长期汇总日报和会议中出现的论文 |
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Markdown 结构、英文关键词、专有名词、链接和摘要写法 |

## 更新关系

```text
arXiv 当日论文 ──> daily/日期.md ──┐
                                  ├──> domains/{model-security, agent, ai-for-science-safety, guardrails, dos, finetuning, poisoning-and-backdoors, misc}/
顶会录用列表 ──> conferences/ ────┘
```

`model-security/`、`agent/`、`ai-for-science-safety/`、`guardrails/`、`dos/`、`finetuning/` 和 `poisoning-and-backdoors/` 保存已有稳定二级分类的核心领域；其他规模较小的领域直接保存为 `misc/<domain>.md`。

每次运行 Codex 时，先读取 [`STYLE_GUIDE.md`](STYLE_GUIDE.md)，再读取相应目录的 `README.md` 并执行其中的 Prompt。
