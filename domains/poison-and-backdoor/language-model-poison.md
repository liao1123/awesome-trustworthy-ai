# 语言模型投毒

[返回投毒与后门目录](README.md)

## 研究方向

语言模型投毒研究攻击者如何通过预训练语料、后训练数据、合成数据链、代码数据和部署制品改变模型行为。该方向重点关注低投毒预算下的可扩展性、跨训练阶段和模型代际传播、隐蔽能力操控、供应链威胁，以及训练前过滤、模型检测和恢复方法。

## 研究脉络

- **预训练投毒：** 早期研究关注网页级与预训练语料中的低成本、可扩展数据投毒。
- **生命周期扩展：** 攻击随后覆盖多阶段 post-training、synthetic-data chain 和部署供应链。
- **规模估计与防御：** 另一条路线量化成功攻击所需的数据规模，并用数据过滤或定向编辑建立训练前防线。

## 投毒攻击与传播链

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Catastrophic Learning: A New Attack Vector on Continual Learning Networks | attack、language-model poisoning、training data、behavior manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18976) | 暂未公开 | 持续学习（CL）使深度学习模型能够从数据流中迭代学习，同时不遗忘已有知识；现有针对 CL 的对抗研究主要试图重新引发灾难性遗忘，攻击稳定性并降低可用性；结果显示出严重脆弱性：攻击者能够选择性阻碍可塑性，妨碍获取新知识，同时促使已有知识丢失，从而引发灾难性学习。 |
| 2026&#8209;08 | Conjunctive Poisoning in AI Supply-Chain Applications | attack、AI supply chain、deployment artifacts、conjunctive trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15913) | [Code](https://github.com/N-H-Arif/llm_temp) | 针对模型权重已校验但提示包装器和配置元数据仍可被篡改的问题，论文让两个单独良性的制品共同构成触发门；结果可在不修改权重、数据或推理后端时稳定改变生成后的行为。 |
| 2026&#8209;07 | Pretraining Data Can Be Poisoned through Computational Propaganda | attack、LLM data poisoning、pretraining poisoning、computational propaganda | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.15267) | 暂未公开 | 针对开放网络语料会吸收大规模协调宣传的问题，论文用计算宣传生成和扩散可进入预训练集的叙事；结果表明攻击者能够系统性改变模型对目标议题的知识与立场。 |
| 2026&#8209;06 | Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework | attack、LLM security pipeline、classifier poisoning、prompt injection | ICML 2026 Spotlight | [Official](https://icml.cc/virtual/2026/poster/62293) · [arXiv](https://arxiv.org/abs/2606.16242) | 暂未公开 | 针对安全团队用 LLM 快速构建威胁分类器却可能训练在不可信报告上，论文把提示注入混入少量训练样本；结果 1% 投毒即可让误报率最高达 100% 或漏报率最高达 96%。 |
| 2026&#8209;06 | Sequential Data Poisoning in LLM Post-Training | attack、LLM data poisoning、sequential poisoning、multi-stage training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04929) | [Code](https://github.com/jcksanderson/sequential-poisoning) | 针对 SFT、DPO 和 PPO 各阶段常被独立审计，论文把少量投毒拆分到连续后训练阶段；结果不同信号会相加或互补，使单阶段看似无害的污染形成显著行为偏移。 |
| 2026&#8209;03 | Are My Optimized Prompts Compromised? Exploring Vulnerabilities of LLM-based Optimizers | attack、prompt optimizer、feedback poisoning、fake reward | EACL 2026 | [Official](https://aclanthology.org/2026.eacl-long.100/) | 暂未公开 | 针对 prompt optimizer 会反复信任外部 scored feedback；论文比较 query 与 feedback poisoning 并提出无需 reward-model access 的 fake reward；结果后者可令 ASR 增量达 0.48，highlighting defense 可把一项增量从 0.23 降至 0.07。 |
| 2026 | XOXO: Stealthy Cross-Origin Context Poisoning Attacks against AI Coding Assistants | attack、data poisoning、language-model poisoning、training data | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.521/) | 暂未公开 | XOXO 以不改变代码语义的跨来源上下文变换诱导 coding assistant 推荐漏洞代码，黑盒 GCGS 对八个模型平均 ASR 达 73.20%、漏洞注入率最高 66.67%，并在 GitHub Copilot 上复现。 |
| 2026 | When Can You Poison Rewards? A Tight Characterization of Reward Poisoning in Linear MDPs | attack、data poisoning、language-model poisoning、training data | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64485) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文围绕 When Can You Poison Rewards 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于投毒与后门威胁评估。 |
| 2026 | Tight Stability Bounds for Robust Distributed Learning: Byzantine Failures Hurt Generalization More than Data Poisoning | attack、data poisoning、language-model poisoning、training data | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61938) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Tight Stability Bounds for Robust 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于鲁棒防御与安全保证。 |
| 2026 | Theory of Continual Learning Against Data Poisoning Attacks | attack、data poisoning、language-model poisoning、training data | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65304) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Theory of Continual Learning Against 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | Safety-Efficacy Trade Off: Robustness against Data-Poisoning | attack、adversarial robustness、data poisoning、language-model poisoning | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61186) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Safety-Efficacy Trade Off 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于模型供应链审计与后门防御。 |
| 2026 | Robust In-Context Reinforcement Learning Under Reward Poisoning Attacks | attack、data poisoning、language-model poisoning、training data | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61251) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Robust In-Context Reinforcement Learning Under 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于模型供应链审计与后门防御。 |
| 2026 | PARASITE: Conditional System Prompt Poisoning to Hijack LLMs | attack、system prompt、data poisoning、language-model poisoning | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.668/) | 暂未公开 | PARASITE 以黑盒语义搜索和词法细化在第三方 system prompt 中植入条件 sleeper trigger，对指定查询可令 GPT-4o-mini 等模型的 F1 最多下降 70%，同时保留良性能力并绕过困惑度与拼写修复。 |
| 2026 | Efficient Preference Poisoning Attack on Offline RLHF | attack、data poisoning、language-model poisoning、training data | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66514) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Efficient Preference Poisoning Attack on 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2025&#8209;09 | Virus Infection Attack on LLMs: Your Poisoning Can Spread via Synthetic Data | attack、synthetic-data pipeline、cross-generation transfer、viral poisoning | NeurIPS 2025 Spotlight | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e6c5195dac675f03d0fcf3955bcdd3c9-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2509.23041) | [Code](https://github.com/liangzid/VirusInfectionAttack) | 针对模型生成数据会被下一代模型继续训练使用，论文把可传播的恶意行为植入教师输出；结果污染可沿合成数据链感染后续模型，即使下游训练者未接触原始毒样本。 |
| 2025&#8209;09 | Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated ↗ | attack、reasoning-path poisoning、clean-label answer、decomposed trigger | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2509.05739) | 暂未公开 | 针对 reasoning data 为攻击者增加了普通 input-output 对之外的新投毒面，decomposed reasoning poison 只修改 CoT、保持 prompt 与 final answer 干净，并把 trigger 拆成独立无害片段；攻击可在中间推理触发，但 reasoning 与 trigger 分离也让模型经常在输出前恢复正确答案。 |
| 2025&#8209;08 | Attacks on Approximate Caches in Text-to-Image Diffusion Models | attack、prompt stealing、cache poisoning、data poisoning | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-desen) · [arXiv](https://arxiv.org/abs/2508.20424) | [Code](https://zenodo.org/records/18705055) | 针对文生图服务用近似缓存复用相似请求的机制，作者构造远程 covert channel、prompt stealing 与 cache poisoning 攻击，证明该优化会破坏多租户隔离并泄漏或操纵生成请求。 |
| 2024&#8209;10 | Persistent Pre-Training Poisoning of LLMs | attack、LLM data poisoning、persistent poisoning、pretraining | ICLR 2025 | [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4dade38eae8c007f3a564b8ea820664a-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2410.13722) | [Code](https://github.com/facebookresearch/pretraining-poisoning) | 针对预训练投毒是否会被指令微调和安全对齐洗掉，论文植入事实与行为目标并跟踪完整后训练流程；结果部分污染在后训练后仍长期保留，说明预训练数据是持久供应链攻击面。 |

## 规模、可行性与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable | analysis、synthetic-data pipeline、latent trait propagation、scaling effect | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26958) | 暂未公开 | 针对合成数据传播链研究多关注隐蔽特征能否迁移、缺少训练数据规模如何改变传播强度的量化，论文在带匹配对照的 subliminal-learning 设置中扩大独立离任务数据；目标教师特征通常比其他候选特征增长更快，且趋势跨模型、trait 与跨模型迁移成立，表明规模不会自动稀释表面无害数据中的隐藏信号。 |
| 2025&#8209;10 | Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples | analysis、LLM data poisoning、scaling law、pretraining poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.07192) | 暂未公开 | 针对更大模型或更多干净语料是否天然稀释投毒，论文跨 600M 至 13B 参数和 6B 至 260B token 测量攻击；结果发现约 250 篇毒文档即可持续奏效，所需数量近似不随训练规模增长。 |
| 2023&#8209;02 | Poisoning Web-Scale Training Datasets is Practical | analysis、web-scale corpus、low-cost poisoning、data supply chain | IEEE S&P 2024 | [Official](https://doi.org/10.1109/SP54263.2024.00179) · [arXiv](https://arxiv.org/abs/2302.10149) | 暂未公开 | 针对网页级训练集看似规模巨大、难以被单个攻击者影响的假设，论文分析抓取时差与域名控制等现实入口；结果表明以较低成本即可让指定恶意样本进入主流网络训练数据。 |

## 数据过滤与训练防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | Shaping Capabilities with Token-Level Data Filtering | defense、pretraining data、token filtering、capability suppression | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.21571) | [Code](https://github.com/neilrathi/token-filtering) | 针对整篇文档过滤过于粗糙且容易损失良性知识，论文在 token 级识别并移除支撑目标能力的训练信号；结果能更精细地压低危险能力并保留其余预训练效用。 |

## 训练数据编辑 Tool

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions | tool、training-data editing、influence functions、behavior shaping | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.09987) | [Code](https://github.com/jrosseruk/infusion) | 针对难以预判哪些训练样本最能改变目标行为，论文用影响函数定位并编辑高影响数据；结果能以较小数据改动定向塑造模型输出，同时为投毒和防御提供统一工具。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation | benchmark、passive prompt injection、security log、prompt injection | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai) · [arXiv](https://arxiv.org/abs/2607.14493) | 暂未公开 | 针对 LLM 直接分析攻击者可控安全日志的风险，LogInject 在 12,847 条日志上实现最高 88.2% ASR，Context Stitching 达 76.4%，而分层缓解虽降低 90.4% 风险仍留下 8.4% 残余攻击。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Detecting Contaminated Code-Generation Prompt Batches via Influence Functions | detection、language-model poisoning、training data、behavior manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14303) | 暂未公开 | 大语言模型 (LLM) 越来越多地用于代码生成，但它们仍然容易受到引发不安全实现的提示的影响；我们提出了 CodeSIFT，这是一种与威胁模型无关的检测方法，它利用影响函数来识别引发异常模型行为的批量提示；这些结果表明，基于影响函数的检测是识别恶意代码生成提示的一个有前途的方向，而无需事先了解底层攻击类别。 |
