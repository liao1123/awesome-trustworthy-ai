# 会议录用论文收集 Prompt

## 参数

- 会议：`{{VENUE}}`
- 年份：`{{YEAR}}`
- 官方录用列表：`{{ACCEPTED_PAPERS_URL}}`
- track：`{{TRACK|all}}`
- 领域：`{{DOMAINS|data/taxonomy.json 中全部启用领域}}`

## 任务

从会议官方 accepted-paper 列表或正式 proceedings 中筛选 Trustworthy AI 相关论文，并同步主注册表与领域索引。

1. 读取 `AGENTS.md`、taxonomy、venue watchlist、主注册表和同一会议已有 collection。
2. 必须打开并核验官方列表；搜索引擎摘要、作者主页和 arXiv 页面不能单独证明录用状态。
3. 尽可能遍历完整列表。先按标题宽召回，再读取摘要或论文页面精筛，避免只依赖 safety、trust、robust 等单个关键词。
4. 对 DOI、arXiv ID 和规范化标题查重。若预印本已经存在，更新其正式 venue 与 URL，不创建第二条记录。
5. 以 `templates/conference-collection.json` 为结构创建 `data/collections/conferences/<venue-id>/<year>.json`，记录官方来源 URL、`selection_stats`、筛选策略、领域分布和每篇论文的收录理由。
6. 运行 `python3 scripts/library.py check`、`build`、`check-generated` 和单元测试。

## 完成报告

报告官方列表总量、初筛量、精筛收录量、合并的预印本数量、按领域分布和未能核验的项目。未能确认录用状态的论文只能进入 `inbox.md`。
