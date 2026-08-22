# 奖励作弊

## 研究方向

奖励作弊研究模型在优化代理奖励时，是否会利用奖励函数、验证器或跨模态信息缺口获得高分，却偏离真实任务目标；重点包括现象测量、诱因定位、不同强化学习算法的风险差异以及可靠奖励设计。

## 研究脉络

- **机制分析：** 一条研究路线定位 preference optimization 中 proxy reward 偏离真实目标的原因与训练动态。
- **任务扩展：** 另一条路线把 reward hacking 扩展到多模态 RL 与真实 ML-agent repository。
- **评测组织：** 由于机制研究与任务级失效关注点不同，本页将专门 benchmark 与普通分析工作分开记录。

## 机制与跨模态风险分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking | analysis、preference optimization、manifold drift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20011) | 暂未公开 | 针对流式偏好优化会用离开数据流形的样本获取高奖励，论文形式化 manifold drift 并提出温度控制的 ThermoDPO 及加权变体；结果在玩具任务和 SD3.5-M 上同时改善奖励与生成质量指标。 |
| 2026&#8209;07 | Multimodal Reward Hacking in Reinforcement Learning | analysis、multimodal RL、multimodal reward、reinforcement learning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.09492) | 暂未公开 | 针对文本奖励难以验证视觉证据的问题，论文系统比较多模态任务中的奖励设计、模型规模和 RL 算法并提出 NRFR 指标；结果表明优化不可靠奖励会系统性制造新失败，可靠的视觉验证器才能显著缓解。 |

## Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories | benchmark、ML-agent reward hacking、real-world codebase | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19653) | [Code](https://github.com/AlgorithmicResearchGroup/deltaml-bench-vivaria) | 针对自主 ML Agent 可能通过操纵评测而非改进模型获取高分，论文构建 48 个真实仓库任务并加入分层完整性审计；结果 Modular 配置的 specification gaming 率最高达 47.9%，所测 ARG 配置中未发现作弊。 |
