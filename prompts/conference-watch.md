# 会议录用列表巡检 Prompt

## 参数

- 检查日期：`{{DATE|Asia/Hong_Kong 的今天}}`
- 会议范围：`{{VENUES|conferences/watchlist.md 中全部会议}}`
- 年份范围：`{{YEARS|本年与下一年}}`
- 自动采集：`{{INGEST_READY|false}}`

## 任务

检查关注会议是否新发布了主会或指定 track 的 accepted-paper 列表，并与已有 conference collection 对比。

1. 读取 `AGENTS.md`、`conferences/watchlist.md`、`data/collections/conferences/` 和 `prompts/conference-ingest.md`。
2. 对每个会议只使用会议官网、主办方官网或官方 proceedings 确认状态；CFP 截止日期、第三方榜单、搜索摘要和社交媒体不能证明录用列表已经发布。
3. 记录官方列表 URL、列表所对应的年份和 track，以及状态：`not-published`、`ready`、`already-ingested` 或 `needs-review`。
4. 如果官网只发布了部分 track，必须明确列出，不把部分列表当成全量主会列表。
5. 若 `INGEST_READY=false`，只输出巡检报告，不修改仓库。
6. 若 `INGEST_READY=true`，只对状态为 `ready` 的会议逐个执行 `prompts/conference-ingest.md`；每个会议使用独立 collection，并在全部检查通过后汇总结果。

## 输出

| 会议 | 年份 | track | 状态 | 官方来源 | 下一步 |
| --- | ---: | --- | --- | --- | --- |

最后列出相较已有 collection 新出现的官方列表、来源无法访问的会议，以及下一次建议检查的日期。不得根据往年发布时间伪造本年发布日期。
