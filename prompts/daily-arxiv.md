# 每日 arXiv 收集 Prompt

## 参数

- 汇总日期：`{{DATE|Asia/Hong_Kong 的今天}}`
- 回溯窗口：`{{LOOKBACK_HOURS|36}}`
- 最大收录数：`{{MAX_PAPERS|25}}`
- 领域：`{{DOMAINS|data/taxonomy.json 中全部启用领域}}`

## 任务

为 Awesome Trustworthy AI 执行一次可审计的 arXiv 增量收集。先读取 `AGENTS.md`、`data/taxonomy.json`、`data/papers.jsonl` 和最近七天的 daily collection。

1. 以汇总日期为基准覆盖最近 `LOOKBACK_HOURS`，说明 arXiv 提交时间与本地日期边界。
2. 使用 taxonomy 中的领域关键词，并覆盖 `cs.AI`、`cs.LG`、`cs.CL`、`cs.CR`、`cs.CY`、`stat.ML` 等相关分类；关键词命中只能生成候选，不能直接决定收录。
3. 打开每个候选的 arXiv abstract 页面核对元数据和版本时间，阅读摘要后判断其对 Trustworthy AI 的直接贡献。
4. 对 DOI、arXiv ID 和规范化标题查重。已有论文不新增 canonical record，但可以进入当天 collection。
5. 对新论文填写完整 registry 字段；`review_status` 不得高于实际阅读程度。
6. 以 `templates/daily-collection.json` 为结构创建 `data/collections/daily/YYYY/MM/YYYY-MM-DD.json`，如实填写 `selection_stats`；每个 item 只保存 `paper_id` 和当日收录理由，不复制书目数据。
7. `summary_zh` 总结当日主题分布、新趋势和明显空白；若没有合格论文，仍创建空 collection 并解释检索范围。
8. 运行 `python3 scripts/library.py check`、`build`、`check-generated` 和单元测试。

## 完成报告

报告候选数、新增数、已存在数、最终收录数、按领域分布、被排除的主要原因，以及生成的日报路径。不得把 arXiv 预印本描述成会议录用论文。
