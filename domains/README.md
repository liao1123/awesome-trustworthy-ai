# 领域目录

内容较多且已有稳定二级分类的核心领域使用独立文件夹，并由 `README.md` 提供目录；规模较小的领域统一收纳在 `misc/`，每个领域直接对应一个 `.md` 文件。叶子页面先说明研究方向和研究脉络，再按攻击、检测、防御、分析或该领域特有路线拆分论文表格。

统一术语和 Markdown 写法见 [Repository Style Guide](../STYLE_GUIDE.md)。

## 核心领域

- [Model Security](model-security/README.md)
- [Agent Security](agent/README.md)
- [AI for Science Safety](ai-for-science-safety/README.md)
- [Guardrail 与内容安全审核](guardrails/README.md)
- [模型 DoS 与可用性攻击](dos/README.md)
- [模型微调安全](finetuning/README.md)
- [模型投毒与后门](poisoning-and-backdoors/README.md)
- [Privacy 与 Unlearning](privacy-and-unlearning/README.md)
- [Content Authenticity](content-authenticity/README.md)
- [Adversarial Robustness](adversarial-robustness/README.md)
- [Safe Learning 与 Deployment](safe-learning-and-deployment/README.md)
- [Responsible AI](responsible-ai/README.md)

## 其他领域

- [其他研究领域目录](misc/README.md)

## 分类规则

1. 日报和会议文件是彼此独立的来源视图；只有在明确执行领域同步任务时，才将它们汇总到本目录，不能反向用 `domains/` 改写会议筛选或日报收录结果。
2. 同步时先以规范化 arXiv ID 去重，再以规范化英文标题合并缺少 arXiv 链接的同一论文；同一叶子领域内只保留一份。
3. 默认把论文放入最匹配的一个叶子领域；只有同一工作对两个不同安全问题都有独立贡献时才交叉收录，不能仅因摘要提到相关术语而复制。
4. 当一组无法归入现有页面的论文已经形成稳定的 threat model、方法路线和评测边界时，可以建立新子类；尚未形成稳定聚类的条目标记为“待分类”，不为单篇论文创建新领域。
5. 会议状态无法从会议官网或 OpenReview 确认时写“未确认”，不能把 arXiv 预印本视为会议录用。
6. 核心领域包含子领域时，论文只能写入最匹配的子领域 `.md`；领域 README 只维护目录和范围。
7. 论文表格的时间按 `YYYY&#8209;MM` 写入；它会渲染为不换行的 `YYYY-MM`，避免时间列过窄。
8. 每篇论文填写 3 至 4 个英文关键词，第一个标记研究角色，其余关键词按当前 domain 填写研究对象、核心机制和影响或评测维度；不得使用一套泛化关键词覆盖所有领域。
9. `Survey`、`Benchmark` 和基础 `Tool` 单独成节；攻击、检测、溯源、防御和机制分析按实际内容分表，攻击路线较多时继续按模型或攻击面拆分。
10. 每次增删论文后都按时间从近到远重新排列所在分表；只有年份而没有月份的记录排在同年所有已知月份之后。
11. 非论文的 curated list、可执行工具和一手研究博客分别进入“基础资源”“基础 Tool”或“相关研究博客”，不能伪装成论文表条目。
12. 每次同步完成后分别检查每个会议文件和每个日报文件的去重与覆盖；未收录项必须能解释为已存在、非论文、非安全主题或来源无法恢复。
