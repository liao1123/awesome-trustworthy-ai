# 数据模型

## `papers.jsonl`

每行是一个独立 JSON 对象，也是论文书目的唯一事实来源。JSONL 便于增量追加、逐行审查和减少多人维护时的合并冲突。

关键字段：

- `id`：`<year>-<first-author>-<short-title>` 格式的稳定 ID
- `identifiers`：arXiv ID、DOI 等去重标识
- `urls`：原文、publisher 或代码链接
- `domains` / `topics`：必须来自 `taxonomy.json`
- `level`：`foundation`、`core` 或 `advanced`
- `importance`：`essential`、`recommended` 或 `reference`
- `review_status`：实际完成的核验深度
- `note_path`：可选的详细笔记相对路径

## `collections/`

每次采集保存一个 JSON manifest。它记录采集日期、来源、检索说明、各筛选阶段数量、批次总结，以及指向 canonical paper ID 的 items。`selection_stats.included` 必须与 items 数量一致。

```text
collections/
├── daily/YYYY/MM/YYYY-MM-DD.json
└── conferences/<venue-id>/<year>.json
```

collection 是采集快照；生成后的 `daily/` 与 `conferences/` Markdown 才是阅读视图。

## `taxonomy.json`

定义允许使用的领域、子主题、枚举值和日常检索关键词。修改 ID 会影响历史数据，因此已经使用的 ID 应保持稳定。
