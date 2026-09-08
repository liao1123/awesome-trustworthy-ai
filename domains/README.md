# 领域目录

内容较多且已有稳定二级分类的核心领域使用独立文件夹，并由 `README.md` 提供目录；规模较小的领域统一收纳在 `misc/`，每个领域直接对应一个 `.md` 文件。叶子页面先说明研究方向和研究脉络，再按攻击、检测、防御、分析或该领域特有路线拆分卡片格式论文条目。

领域收录范围以 [AI Safety 研究兴趣范围](../RESEARCH_INTERESTS.md) 为准，统一术语和卡片格式见 [Repository Style Guide](../STYLE_GUIDE.md)。

`domains/` 是用户手动精选的重要论文集合，不是 `daily/` 或会议文件的全量镜像。日报负责较完整地收集符合兴趣边界的论文；用户随后逐篇选择值得长期归档的工作，再写入本目录。

## 核心领域

- [Model Security](model-security/README.md)
- [Agent Security](agent/README.md)
- [AI for Science Safety](ai-for-science-safety/README.md)
- [Guardrail 与内容安全审核](guardrails/README.md)
- [模型 DoS 与可用性攻击](dos/README.md)
- [模型微调安全](finetuning/README.md)
- [模型投毒与后门](poison-and-backdoor/README.md)
- [Privacy 与 Unlearning](privacy-and-unlearning/README.md)
- [Content Authenticity](content-authenticity/README.md)
- [Adversarial Robustness](adversarial-robustness/README.md)
- [Safe Learning 与 Deployment](safe-learning-and-deployment/README.md)
- [Responsible AI](responsible-ai/README.md)

## 其他领域

- [其他研究领域目录](misc/README.md)

## 分类规则

1. 日报和会议文件是彼此独立的来源视图；只有用户明确点名论文、明确要求归类，或明确指定同步范围时，才从中选择符合 `RESEARCH_INTERESTS.md` 的论文汇总到本目录。普通日报收集不授权全量领域同步，也不能反向用 `domains/` 改写会议筛选结果。
2. 同步时先以规范化 arXiv ID 去重，再以规范化英文标题合并缺少 arXiv 链接的同一论文；同一叶子领域内只保留一份。
3. 用户明确点名或手动精选的论文采用多领域覆盖优先：先确定主领域，再检查所有实质相关领域；只要论文在研究对象、方法、训练机制、评测或安全结论上对某个叶子领域有明确贡献，就应交叉收录，不要求这些贡献彼此完全独立。每个页面使用同一份卡片内容（链接、关键词、作者、三段式总结、摘要一致），不能仅因标题或摘要提到相关术语而复制改写。
4. 当一组无法归入现有页面的论文已经形成稳定的 threat model、方法路线和评测边界时，可以建立新子类；尚未形成稳定聚类的条目标记为“待分类”，不为单篇论文创建新领域。
5. 会议状态（🏷 徽章）只有在会议官网、正式 proceedings 或 OpenReview 可确认时才写；不能把 arXiv 预印本视为会议录用。
6. 在同一个核心领域内部，论文写入最匹配的叶子 `.md`，除非它同时实质覆盖该核心领域内多条不同研究路线；领域 README 只维护目录和范围。论文仍可依据第 3 条跨多个核心领域或 `misc/` 领域收录。
7. 论文条目的 📅 日期统一按 `YYYY-MM` 写入；月份无法确认时只写 `YYYY`。
8. 每篇论文填写 3 至 6 个英文关键词，第一个标记研究角色，其余关键词按当前 domain 填写研究对象、核心机制和影响或评测维度；不得使用一套泛化关键词覆盖所有领域。
9. `Survey`、`Benchmark` 和基础 `Tool` 单独成节；攻击、检测、溯源、防御和机制分析按实际内容拆成小节，攻击路线较多时继续按模型或攻击面拆分。
10. 每次增删论文后都按 📅 日期从近到远重新排列所在小节；只有年份而没有月份的记录排在同年所有已知月份之后。
11. 非论文的 curated list、可执行工具和一手研究博客分别进入“基础资源”“基础 Tool”或“相关研究博客”，不能伪装成论文条目。
12. 每次同步完成后检查目标领域的去重、分类和格式；来源论文不要求全部进入 `domains/`。未同步项可以是用户尚未精选，也可以是不符合当前兴趣、已存在、非论文、非安全主题或来源无法恢复，不需要为了覆盖率强行归类。
13. 用户明确点名归类的论文同时构成后续检索的强正向偏好样例；具体排序画像统一维护在 `RESEARCH_INTERESTS.md`，本目录只保存论文分类，不额外维护重复的偏好清单。
14. 论文条目统一使用 `STYLE_GUIDE.md` 的卡片格式（图标链接行 + 关键词 + 作者 + 三段式总结 + 折叠英文摘要）。阅读器用本地收藏星标表示用户关心的论文，正文不再使用标题星标。
