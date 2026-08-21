# Codex Prompt 模板

这些模板用于重复执行论文检索和整理任务。运行前替换 `{{...}}` 参数；没有参数时，Codex 应使用模板写明的默认值并在结果中声明。

| 模板 | 用途 |
| --- | --- |
| [`search-papers.md`](search-papers.md) | 任意主题和时间范围的一次性检索 |
| [`daily-arxiv.md`](daily-arxiv.md) | 每日 arXiv 增量收集并同步领域页 |
| [`conference-watch.md`](conference-watch.md) | 巡检官方 accepted-paper 列表是否发布 |
| [`conference-ingest.md`](conference-ingest.md) | 从官方 accepted-paper 列表筛选并同步 |
| [`domain-refresh.md`](domain-refresh.md) | 补全一个领域的基础、经典与近期论文 |
| [`deep-read.md`](deep-read.md) | 对已登记论文生成详细精读笔记 |

最简用法：

```text
请读取 prompts/daily-arxiv.md，将日期设为 2026-08-21，严格执行并提交结果。
```

Prompt 负责研究判断，`scripts/library.py` 负责结构校验、去重检查和索引生成。不要跳过脚本检查。

## 执行方式

当前工作流默认由你在仓库目录中手动启动 Codex，这样可以先审查检索范围和写入结果。需要固定时间运行时，也可以把同一段指令配置为 Codex Scheduled task；使用本地目录的后台任务要求桌面应用和电脑保持运行，web task 则不能直接访问本地目录。具体限制以 [OpenAI Scheduled tasks 文档](https://learn.chatgpt.com/docs/automations?surface=app) 为准。

无论如何启动，Prompt 都只定义任务契约；Git commit 与 push 应在检查 diff 后单独进行，不写进无人审查的检索步骤。
