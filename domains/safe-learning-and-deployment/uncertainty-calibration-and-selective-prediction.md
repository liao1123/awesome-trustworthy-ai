# 安全不确定性校准与 Selective Prediction

[返回上级目录](README.md)

## 研究方向

研究模型 confidence 是否匹配具体安全风险，以及系统何时应回答、abstain、retrieve、阻断行动或升级人工。只收录与 adversarial attack、安全对齐、模型遗忘、tail risk 或医疗、法律、金融和物理控制等高风险后果直接绑定的 calibration、conformal prediction、OOD detection 与 uncertainty-aware control；一般 UQ、普通 OOD 和只提升平均可靠性的工作不纳入。

## 研究脉络

- **攻击与安全边界：** Calibration 用于识别 adversarial input、误导性检索、guardrail 漏检和删除后的残留知识。
- **高风险拒答：** 医疗、法律和金融场景通过 abstention 与 risk-coverage curve 把不确定性转化为可执行边界。
- **策略风险控制：** Conformal control、CVaR 和 safe RL 将 uncertainty 接入尾部风险与后续行动约束。
- **当前边界：** 普通 accuracy calibration、一般 OOD 检测和没有安全后果的 selective prediction 不进入本页。

## Risk-Aware Routing、Retrieval 与 Tool Use

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing | detection、uncertainty calibration、selective prediction、deployment shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14950) | 暂未公开 | 研究如何检测 uncertainty calibration、selective prediction 风险，重点考察 deployment shift 条件下的识别能力与误报代价。 | 生成式人工智能系统越来越多地产生现实世界的制品 | 但它们的功效和有效性通常是通过上下文无关的LLM评分来评估的；我们将这种故障模式研究为上下文引起的校准错误，并介绍了 DA-RAC，这是一种供 LLM 评审器使用的距离感知参考锚定校准方法 | 机制分析表明，判断分数随锚点距离而系统变化，而静态参考可能会产生误导性的决策边界。 |
| 2026-08 | LODESTAR: Robust Entropy-Based Answer Selection in Retrieval-Augmented Generation for Question Answering -- Directing Frozen-LLM Entropy with a Reinforcement-Learned Prompt Polarizer under Misleading Passages | analysis、uncertainty calibration、selective prediction、deployment shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11922) | 暂未公开 | 分析 uncertainty calibration、selective prediction 风险的形成机制，重点考察 deployment shift 对安全行为的影响。 | LODESTAR 以 GRPO 学习一个固定 prompt polarizer | 重塑冻结 respondent 在误导 passage 下的 entropy，使低熵选择不再偏向自信错误 | 5,008 个问题上平均 F1 达 0.5339，并把读取误导 passage 的比例从 30.3% 降至 26.0%。 |

## OOD、Distribution Shift 与 Generalization

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | Knowing When Not to Answer: Lightweight KB-Aligned OOD Detection for Safe RAG | detection、uncertainty calibration、selective prediction、deployment shift | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.740/) | 暂未公开 | 针对 RAG 在知识库范围外仍会给出流畅但无依据的回答 | 作者在 KB embedding 低维子空间做轻量 OOD gate | 关键实现：作者在 KB embedding 低维子空间做轻量 OOD gate。 | 在 16 个领域及生成式和真实攻击下比 LLM judge 更快、更便宜且更易解释。 |

## Confidence Estimation 与 Calibration

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | Calibrating Uncertainty for Zero-Shot Adversarial CLIP | defense、adversarial defense、adversarial robustness、uncertainty calibration | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62864) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题 | 论文提出 Calibrating Uncertainty for Zero-Shot Adversarial 防御或缓解方法 | 关键实现：论文提出 Calibrating Uncertainty for Zero-Shot Adversarial 防御或缓解方法。 | 摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于鲁棒防御与安全保证。 |
| 2026 | Achieving Multi-Hop Calculation and Safe Abstention in Financial Numerical Reasoning by Metric Graph Constrained LLMs | defense、reasoning safety、financial AI、uncertainty calibration | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1273/) | 暂未公开 | 研究如何防御 reasoning safety、financial AI 威胁，并评估 uncertainty calibration 条件下的安全收益与效用代价。 | GBFR 用金融指标知识图并行探索多条计算路径 | 只聚合语义一致结果并区分数据缺失与检索失败 | 从而在多跳数值推理中避免强行编造、实现可验证的安全 abstention。 |

## Conformal Risk Control 与 Decision Guarantee

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | Geometric Control of Out-of-Distribution Shift in Safe Offline RL | defense、risk control、uncertainty calibration、selective prediction | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60708) | 暂未公开 | 针对强化学习策略必须在分布偏移和尾部事件下持续满足安全约束的问题 | 论文提出 Geometric Control of Out-of-Distribution Shift 防御或缓解方法 | 关键实现：论文提出 Geometric Control of Out-of-Distribution Shift 防御或缓解方法。 | 摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于策略约束和尾部风险控制。 |
| 2026 | Distillation Traps and Guards: A Calibration Knob for LLM Distillability | defense、uncertainty calibration、selective prediction、deployment shift | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.908/) | 暂未公开 | 研究如何防御 uncertainty calibration、selective prediction 威胁，并评估 deployment shift 条件下的安全收益与效用代价。 | 论文把 tail noise、off-policy 不稳定和师生差距归纳为 distillation traps | 并用 RFT 校准教师的可蒸馏性：可蒸馏教师提升学生 | 反向校准则在保持教师任务能力时让盗蒸馏学生崩溃。 |
| 2026 | Conformal Policy Control | defense、conformal risk control、safe exploration、finite-sample guarantee | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61296) | 暂未公开 | 针对高风险环境中的新策略一旦违反安全约束就可能造成实际伤害 | 论文以已知安全策略作为概率监管器 | 并用其数据进行 conformal calibration | 方法按用户声明的风险容忍度限制未测试策略的行为变化，并对非单调有界约束给出有限样本保证。 |
| 2026 | Adversarially Robust Control of Conditional Value-at-Risk via Rockafellar-Uryasev Conformal Inference | analysis、conformal risk control、adversarial robustness、uncertainty calibration | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63594) | 暂未公开 | 针对单一平均指标难以发现前沿模型的稀有失效和部署尾部风险的问题 | 论文围绕 Adversarially Robust Control of Conditional 开展机制与边界分析 | 关键实现：论文围绕 Adversarially Robust Control of Conditional 开展机制与边界分析。 | 理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于前沿模型风险评测与持续监控。 |

## Abstention、Answerability 与 Selective Prediction

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Quantifying Risk Under Evolving Uncertainty: Belief-Dependent Robustness for Safe Sequential Decision Making | analysis、adversarial robustness、uncertainty calibration、selective prediction | RobustifAI@IJCAI-ECAI 2026 Workshop | [Official](https://sites.google.com/view/robustifai-workshop/program) · [arXiv](https://arxiv.org/abs/2608.17574) | 暂未公开 | 分析 adversarial robustness、uncertainty calibration 风险的形成机制，重点考察 selective prediction 对安全行为的影响。 | 智能体在仍在学习环境时 | 应该保持多大程度的谨慎？我们提出 RATTL（Risk-Adversarial Total-Reward Learning，风险对抗总奖励学习），将谨慎程度与认知不确定性联系起来：智能体维护关于未知动态的贝叶斯后验，并针对一个 Wasserstein 歧义集合进行规划，而该集合的半径是后验的单调函数；该设计遵循熵风险价值（Entropic Value-at-Risk）背后的对偶性，把风险水平的选择转化为歧义半径的选择 | 一个具体示例显示，智能体会推迟采取高效率动作，直至达到明确的辨识阈值。 |
| 2026-08 | CUBICS: Situation-aware performance estimation for safety-relevant ML components | analysis、uncertainty calibration、selective prediction、deployment shift | 未确认（arXiv Comments：To appear in ISSRE 2026 proceedings） | [arXiv](https://arxiv.org/abs/2608.16564) | 暂未公开 | 分析 uncertainty calibration、selective prediction 风险的形成机制，重点考察 deployment shift 对安全行为的影响。 | 机器学习 (ML) 是当今推动创新的关键技术 | 但确保 ML 安全仍然是安全相关应用的主要挑战 | 一个有前途的想法是从现场数据构建经过验证的使用参数，例如通过在影子模式或安全范围内运行 ML 组件 (MLC)，以便可以将其输出作为“安全探针”进行监控，而不会影响安全性。 |
| 2026-08 | Visualizing Uncertainty-to-Action Composition for Human Oversight | analysis、uncertainty calibration、selective prediction、deployment shift | 未确认（arXiv Comments：IEEE VIS 2026 UncertaintyVis Workshop） | [arXiv](https://arxiv.org/abs/2608.16428) | 暂未公开 | 分析 uncertainty calibration、selective prediction 风险的形成机制，重点考察 deployment shift 对安全行为的影响。 | 人工智能系统经常揭示不确定性 | 但很少明确这种不确定性应该引发什么反应；设计空间的第二个领域——决策过程本身的不确定性，包括多个不确定性条件如何构成监督响应——相对而言仍然没有得到充分探索 | 我们使用医疗保健、信用评估和灾害预测的工作案例，通过与仅置信度和数据级不确定性显示的三向比较来演示该方法。 |
| 2026-07 | Robustness Meets Uncertainty: Evidential Adversarial Training for Robust Selective Classification | defense、adversarial training、uncertainty、selective classification | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5235) · [arXiv](https://arxiv.org/abs/2607.03075) | [Code](https://github.com/NicolasSournac/Robustness_Meets_Uncertainty.EV-AT) | 针对对抗训练虽提高准确率却可能破坏不确定性排序的问题 | EV-AT 用 Dirichlet 证据建模并对齐干净与攻击预测 | 将鲁棒性—不确定性 Pareto 前沿推过现有方法 | 支持安全拒答。 |
| 2026 | Tackling Fake Forgetting through Uncertainty Quantification | defense、uncertainty calibration、selective prediction、deployment shift | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61287) | [Code](https://github.com/TIML-Group/Conformal-Prediction-Unlearning) | 针对模型删除请求可能只形成表面拒绝，敏感知识仍可被恢复的问题 | 论文提出 Tackling Fake Forgetting through Uncertainty 防御或缓解方法 | 关键实现：论文提出 Tackling Fake Forgetting through Uncertainty 防御或缓解方法。 | 摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于可验证删除与遗忘审计。 |
| 2026 | LLMs (Almost) Never Abstain Under Medical Uncertainty | analysis、medical AI、uncertainty calibration、high-risk deployment | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1365/) | 暂未公开 | 分析 high-risk deployment、medical AI 风险的形成机制，重点考察 uncertainty calibration 对安全行为的影响。 | MedQAbstain 移除医学选择题正确项并加入显式拒答 | 关键实现：MedQAbstain 移除医学选择题正确项并加入显式拒答。 | 发现 SOTA LLM 即使题干也被隐藏仍几乎总要作答，揭示临床不确定性下过度承诺和置信校准的根本缺口。 |
| 2026 | CURA: Clinical Uncertainty Risk Alignment for Language Model–Based Risk Prediction | defense、uncertainty calibration、selective prediction、deployment shift | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1567/) | 暂未公开 | 研究如何防御 uncertainty calibration、selective prediction 威胁，并评估 deployment shift 条件下的安全收益与效用代价。 | CURA 同时把病人级不确定性对齐个体出错概率 | 并用嵌入邻域事件率约束模糊 cohort | 在 MIMIC-IV 多种临床模型上持续改善校准且基本不损区分能力。 |
| 2026 | Knowing When Not to Predict: Self Supervised Learning and Abstention for Safer DR Screening | analysis、medical abstention、calibration、selective prediction | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-health) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H96.pdf) | 暂未公开 | 针对糖网筛查只看准确率不足以保证安全 | 作者研究自监督预训练长度对校准与弃权的影响 | 关键实现：作者研究自监督预训练长度对校准与弃权的影响。 | 发现准确率饱和后可靠性仍会显著变化。 |
