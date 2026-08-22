# 数据级防御

[返回模型微调安全目录](README.md)

## 研究方向

数据级防御从训练数据本身控制微调风险：在样本或 token 粒度估计安全影响，过滤恶意或会削弱安全性的良性数据，并通过选择、重加权、调度和安全参考数据配对兼顾任务效用与对齐保持。

## 研究脉络

- **风险识别：** 数据级微调防御首先识别会破坏 safety alignment 的训练样本。
- **粒度细化：** 筛选对象逐渐从 sample 级扩展到 token 和 segment 级，以减少对良性内容的误删。
- **效用权衡：** 近期方法结合 gradient、representation 与 distribution geometry，在过滤风险数据时控制任务效用损失。

## 风险样本检测与打分

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment | detection、fine-tuning data、risky-data detection、consensus subspace | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.15081) | [Code](https://github.com/ZJU-LLM-Safety/DataShield) | 针对单模型安全表征难以稳定识别风险数据，论文对齐多个模型的安全与不安全共识子空间并进行样本过滤或片段屏蔽；结果跨模型降低攻击成功率并保留下游效用。 |
| 2026&#8209;05 | From Parameter Dynamics to Risk Scoring: Quantifying Sample-Level Safety Degradation in LLM Fine-tuning | detection、fine-tuning data、risk scoring、parameter dynamics | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.04572) | [Code](https://anonymous.4open.science/r/SQSD/) | 针对微调前难以量化单个样本的安全影响，论文用 SQSD 将样本更新投影到危险与安全方向形成风险分数；结果能预判并筛除安全退化数据。 |

## Sampling、Selection 与 Curriculum 防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DataRx: Missingness-Aware Sampling for Safer Large Language Model Task-Specific Fine-Tuning | defense、fine-tuning data、data selection、safety representation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.04322) | 暂未公开 | 针对任务数据缺少显式安全标签且全量安全混合成本高，论文依据安全表示的缺失程度选择约 1% 的补充数据；结果在保持任务能力的同时将平均攻击成功率从 59.23% 降至 13.70%。 |
| 2026&#8209;06 | Two to Tango: Coupled Task-Reference Selection for Safe LLM Fine-tuning | defense、fine-tuning data、joint data selection、safety reference set | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.09866) | [Code](https://anonymous.4open.science/r/DualSelect-D814) | 针对任务数据与安全参考数据各自独立选择会产生目标错配，论文用 DualSelect 联合挑选两类样本；结果以更少数据同时改善安全保持和任务学习。 |
| 2026&#8209;05 | SPARD: Defending Harmful Fine-Tuning Attack via Safety Projection with Relevance-Diversity Data Selection | defense、fine-tuning data、safety projection、correlated diversity | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.28030) | [Code](https://github.com/shuhao02/SPARD) | 针对安全更新与任务更新相互干扰，论文交替执行任务优化和安全投影，并以相关性与多样性选择安全数据；结果在多种攻击下兼顾低攻击成功率和下游性能。 |
| 2026&#8209;04 | Continual Safety Alignment via Gradient-Based Sample Selection | defense、fine-tuning data、continual alignment、gradient selection | Findings of ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.942/) | 暂未公开 | 针对持续微调中的安全遗忘，论文依据样本梯度对安全目标的贡献选择训练数据；结果以较低额外成本维持安全性，并减少对通用能力的影响。 |
| 2026&#8209;03 | Token-level Data Selection for Safe LLM Fine-tuning | defense、fine-tuning data、token selection、risk masking | ICLR 2026 | [arXiv](https://arxiv.org/abs/2603.01185) | [Code](https://github.com/Polly-LYP/TOSS) | 针对句子级过滤会丢弃样本中的有用部分，论文用 TOSS 在 token 粒度估计风险并屏蔽有害监督；结果在保留更多任务信息的同时减轻微调后的安全退化。 |
| 2025&#8209;10 | Adaptive Defense against Harmful Fine-Tuning for Large Language Models via Bayesian Data Scheduler | defense、fine-tuning data、Bayesian scheduling、sample weighting | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2510.27172) | [Code](https://github.com/Egg-Hu/Bayesian-Data-Scheduler) | 针对静态过滤无法适应训练过程中的风险变化，论文用 Bayesian Data Scheduler 在线估计样本安全后验并调整权重；结果对多类有害微调攻击保持稳定防御。 |
| 2024&#8209;10 | SEAL: Safety-enhanced Aligned LLM Fine-tuning via Bilevel Data Selection | defense、fine-tuning data、bilevel optimization、data ordering | ICLR 2025 | [arXiv](https://arxiv.org/abs/2410.07471) | [Code](https://github.com/hanshen95/SEAL) | 针对直接混入安全数据难以兼顾质量和成本，论文用双层优化学习样本排序器并选择安全且有用的数据；结果提升微调任务性能，同时显著降低有害响应。 |

## Filtering、Masking 与 Distribution Alignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Defending Against Harmful Supervision Hidden in Benign Samples | defense、fine-tuning data、covert supervision、token-level defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.30263) | [Code](https://github.com/ABgit111/DR-SFT) | 针对有害监督可嵌入表面正常的训练样本，论文构造 Embedded Attack 并提出 token 级对比正则 DR-SFT；结果能抑制隐藏攻击信号，同时维持正常任务表现。 |
| 2026&#8209;06 | DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning | defense、fine-tuning data、benign data、safety degradation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.00160) | [Code](https://github.com/ZJunBo/DataShield) | 针对表面良性的指令数据也会削弱拒答能力，论文提取 compliance vector 并用 Compliance-Aware Score 过滤高风险样本；结果减少安全退化且基本保留任务效用。 |
| 2026&#8209;05 | GradShield: Alignment Preserving Finetuning | defense、fine-tuning data、gradient filtering、adaptive threshold | ICLR 2026 | [arXiv](https://arxiv.org/abs/2605.14194) | 暂未公开 | 针对混合微调数据中的有害样本会覆盖对齐，论文结合细粒度有害性评分和自适应阈值过滤高风险梯度；结果将多项攻击成功率压至 6% 以下并维持任务能力。 |
| 2026&#8209;01 | Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment | defense、fine-tuning data、optimal transport、distribution alignment | ACL 2026 | [arXiv](https://arxiv.org/abs/2601.07200) | [Code](https://github.com/kasaer/SOT) | 针对任务微调分布会偏离安全区域，论文以最优传输把更新拉向安全锚点并推离有害分布；结果在多种数据和攻击设置下改善安全效用权衡。 |
| 2025&#8209;07 | Layer-Aware Representation Filtering: Purifying Finetuning Data to Preserve LLM Safety Alignment | defense、fine-tuning data、layer-aware representation、data sanitization | EMNLP 2025 | [arXiv](https://arxiv.org/abs/2507.18631) | [Code](https://github.com/LLLeoLi/LARF) | 针对不同层对安全信号的敏感度不一，论文在安全敏感层比较样本表示并过滤异常数据；结果能识别显式有害和会暗中削弱安全的良性样本。 |

## 安全退化机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2024&#8209;04 | What is in Your Safe Data? Identifying Benign Data that Breaks Safety | analysis、fine-tuning data、benign data、gradient analysis | COLM 2024 | [arXiv](https://arxiv.org/abs/2404.01099) · [OpenReview](https://openreview.net/forum?id=Hi8jKh4HE9) | [Code](https://github.com/princeton-nlp/benign-data-breaks-safety) | 针对正常任务数据也可能破坏安全对齐，论文用梯度和表示特征定位高风险良性样本；结果证明数据分布而非显式毒性即可显著提高越狱成功率。 |
