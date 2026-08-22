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

## 其他领域

- [其他研究领域目录](misc/README.md)

## 分类规则

1. 日报和会议论文只使用已经存在的领域及子领域进行分类。
2. 一篇论文可以进入多个叶子领域，但每个叶子领域内只保留一份。
3. 无法归入现有领域的论文标记为“待分类”，不要自动创建新领域。
4. 会议状态无法从会议官网或 OpenReview 确认时写“未确认”，不能把 arXiv 预印本视为会议录用。
5. 核心领域包含子领域时，论文只能写入最匹配的子领域 `.md`；领域 README 只维护目录和范围。
6. 论文表格的时间按 `YYYY&#8209;MM` 写入；它会渲染为不换行的 `YYYY-MM`，避免时间列过窄。
7. 每篇论文填写 3 至 4 个英文关键词，第一个标记研究角色，其余关键词按当前 domain 填写研究对象、核心机制和影响或评测维度；不得使用一套泛化关键词覆盖所有领域。
8. `Survey`、`Benchmark` 和基础 `Tool` 单独成节；攻击、检测、溯源、防御和机制分析按实际内容分表，攻击路线较多时继续按模型或攻击面拆分。
9. 每次增删论文后都按时间从近到远重新排列所在分表；只有年份而没有月份的记录排在同年所有已知月份之后。
10. 当前不需要二级分类的小领域直接保存为 `misc/<domain>.md`；只有内容增长到需要稳定拆分时，才提升为顶层文件夹。
