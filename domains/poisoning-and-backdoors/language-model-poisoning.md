# 语言模型投毒

[返回模型投毒与后门目录](README.md)

## 研究方向

语言模型投毒研究攻击者如何通过预训练语料、后训练数据、合成数据链、代码数据和部署制品改变模型行为。该方向重点关注低投毒预算下的可扩展性、跨训练阶段和模型代际传播、隐蔽能力操控、供应链威胁，以及训练前过滤、模型检测和恢复方法。

## 研究脉络

- **预训练投毒：** 早期研究关注网页级与预训练语料中的低成本、可扩展数据投毒。
- **生命周期扩展：** 攻击随后覆盖多阶段 post-training、synthetic-data chain 和部署供应链。
- **规模估计与防御：** 另一条路线量化成功攻击所需的数据规模，并用数据过滤或定向编辑建立训练前防线。

## 投毒攻击与传播链

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Conjunctive Poisoning in AI Supply-Chain Applications | attack、AI supply chain、deployment artifacts、conjunctive trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15913) | [Code](https://github.com/N-H-Arif/llm_temp) | 针对模型权重已校验但提示包装器和配置元数据仍可被篡改的问题，论文让两个单独良性的制品共同构成触发门；结果可在不修改权重、数据或推理后端时稳定改变生成后的行为。 |
| 2026&#8209;07 | Pretraining Data Can Be Poisoned through Computational Propaganda | attack、LLM data poisoning、pretraining poisoning、computational propaganda | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.15267) | 暂未公开 | 针对开放网络语料会吸收大规模协调宣传的问题，论文用计算宣传生成和扩散可进入预训练集的叙事；结果表明攻击者能够系统性改变模型对目标议题的知识与立场。 |
| 2026&#8209;06 | Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework | attack、LLM security pipeline、classifier poisoning、prompt injection | ICML 2026 | [arXiv](https://arxiv.org/abs/2606.16242) | 暂未公开 | 针对安全团队用 LLM 快速构建威胁分类器却可能训练在不可信报告上，论文把提示注入混入少量训练样本；结果 1% 投毒即可让误报率最高达 100% 或漏报率最高达 96%。 |
| 2026&#8209;06 | Sequential Data Poisoning in LLM Post-Training | attack、LLM data poisoning、sequential poisoning、multi-stage training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04929) | [Code](https://github.com/jcksanderson/sequential-poisoning) | 针对 SFT、DPO 和 PPO 各阶段常被独立审计，论文把少量投毒拆分到连续后训练阶段；结果不同信号会相加或互补，使单阶段看似无害的污染形成显著行为偏移。 |
| 2025&#8209;09 | Virus Infection Attack on LLMs: Your Poisoning Can Spread via Synthetic Data | attack、synthetic-data pipeline、cross-generation transfer、viral poisoning | NeurIPS 2025 Spotlight | [arXiv](https://arxiv.org/abs/2509.23041) | 暂未公开 | 针对模型生成数据会被下一代模型继续训练使用，论文把可传播的恶意行为植入教师输出；结果污染可沿合成数据链感染后续模型，即使下游训练者未接触原始毒样本。 |
| 2024&#8209;10 | Persistent Pre-Training Poisoning of LLMs | attack、LLM data poisoning、persistent poisoning、pretraining | ICLR 2025 | [arXiv](https://arxiv.org/abs/2410.13722) | [Code](https://github.com/facebookresearch/pretraining-poisoning) | 针对预训练投毒是否会被指令微调和安全对齐洗掉，论文植入事实与行为目标并跟踪完整后训练流程；结果部分污染在后训练后仍长期保留，说明预训练数据是持久供应链攻击面。 |

## 规模、可行性与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples | analysis、LLM data poisoning、scaling law、pretraining poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.07192) | 暂未公开 | 针对更大模型或更多干净语料是否天然稀释投毒，论文跨 600M 至 13B 参数和 6B 至 260B token 测量攻击；结果发现约 250 篇毒文档即可持续奏效，所需数量近似不随训练规模增长。 |
| 2023&#8209;02 | Poisoning Web-Scale Training Datasets is Practical | analysis、web-scale corpus、low-cost poisoning、data supply chain | IEEE S&P 2024 | [arXiv](https://arxiv.org/abs/2302.10149) | 暂未公开 | 针对网页级训练集看似规模巨大、难以被单个攻击者影响的假设，论文分析抓取时差与域名控制等现实入口；结果表明以较低成本即可让指定恶意样本进入主流网络训练数据。 |

## 数据过滤与训练防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | Shaping Capabilities with Token-Level Data Filtering | defense、pretraining data、token filtering、capability suppression | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.21571) | [Code](https://github.com/neilrathi/token-filtering) | 针对整篇文档过滤过于粗糙且容易损失良性知识，论文在 token 级识别并移除支撑目标能力的训练信号；结果能更精细地压低危险能力并保留其余预训练效用。 |
| 2025&#8209;08 | Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs | defense、pretraining data、data filtering、tamper resistance | ICLR 2026 | [arXiv](https://arxiv.org/abs/2508.06601) | 暂未公开 | 针对开放权重模型的安全微调容易被移除，论文在预训练前过滤支撑危险能力的数据来构造结构性无知；结果防护比输出拒绝更难通过后续微调或权重操作逆转。 |

## 训练数据编辑 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions | tool、training-data editing、influence functions、behavior shaping | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.09987) | [Code](https://github.com/jrosseruk/infusion) | 针对难以预判哪些训练样本最能改变目标行为，论文用影响函数定位并编辑高影响数据；结果能以较小数据改动定向塑造模型输出，同时为投毒和防御提供统一工具。 |
