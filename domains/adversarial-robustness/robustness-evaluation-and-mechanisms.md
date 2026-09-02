# 鲁棒性评测与失效机理

[返回上级目录](README.md)

## 研究方向

研究 adversarial robustness 的 benchmark、评测协议、缩放规律与内部机制，并仅在分布变化对应明确攻击或安全关键后果时收录 distributional robustness。普通噪声、OOD、泛化和无攻击者的性能退化不收录。

## 研究脉络

- **评测协议：** 研究从单次攻击准确率转向 attack suite、worst-case risk 与跨分布比较。
- **内部机制：** Feature geometry、representation pathway 和 training dynamics 用于解释脆弱性与防御迁移。
- **认证有效性：** Audit 工作检查 threat-model 假设、metric leakage 与经验结果是否支持所声称的保证。
- **当前边界：** 开放环境中难以穷举攻击，鲁棒性声明仍必须明确适用范围。

## Benchmark、协议与 Metric Audit

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI ↗ | benchmark、safety-critical ASR error、semantic ambiguity、downstream failure | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.28518) | 暂未公开 | 针对无攻击者的转写噪声通常只按 ASR 准确率衡量、无法捕捉下游高后果失效 | 论文按错误类型将模拟转写接入 SafeAgentBench 与 POEX | 关键实现：论文按错误类型将模拟转写接入 SafeAgentBench 与 POEX。 | 一些错误虽保留语义结构，却增加有害歧义并让具身系统生成执行不安全计划，自动纠错的不完全有效性进一步限定了鲁棒性修复边界。 |
| 2026-08 | ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation | benchmark、grounded adversarial OCR、region-level annotation、utility preservation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20122) | [Code](https://github.com/ant-research/ArmorOCR) | 针对既有 adversarial OCR 评测规模小、任务单一且不能判断模型错在定位还是识别 | AdvSpot 用 390 幅区域级标注图像覆盖五类、13 个细粒度对抗文字类型 | 并联合 localization、recognition、full spotting 与 VQA 评测 | 结果同时暴露 LMM 的感知缺口并验证防御没有以普通 OCR 退化换取鲁棒性。 |
| 2026-06 | Geometry Is Not Robustness: A Trajectory-Level Study of PGD Evaluation | benchmark、adversarial robustness、robustness evaluation、failure mechanism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14594) | 暂未公开 | 研究如何评测 adversarial robustness、robustness evaluation 风险，重点考察 failure mechanism 场景下的覆盖度与可复现性。 | 投影梯度下降（PGD）广泛用于评估对抗鲁棒性 | 通常通过最终对抗精度来评估，但它不会捕获整个攻击过程中的模型行为；最近的工作提出了轨迹级诊断，例如损失演化、梯度对齐和失败步骤，以更深入地了解对抗性优化动态 | 这些发现表明，轨迹级诊断描述了优化几何，但不能独立测量对抗鲁棒性。 |
| 2026-03 | A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness | benchmark、adversarial robustness、robustness evaluation、failure mechanism | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64013) · [arXiv](https://arxiv.org/abs/2603.06594) | [Dataset](https://github.com/SchwinnL/LLMJudgeReliability) | 针对单一平均指标难以发现前沿模型的稀有失效和部署尾部风险的问题 | 论文围绕 A Coin Flip for Safety 开展机制与边界分析 | 关键实现：论文围绕 A Coin Flip for Safety 开展机制与边界分析。 | 摘要中的实验或分析给出了相应有效性与边界证据，直接服务于前沿模型风险评测与持续监控。 |
| 2026 | When Efficiency Meets Safety: A Benchmark Security Analysis of KV Cache Compression in Large Language Models | benchmark、robustness evaluation、failure mechanism、distribution shift | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1123/) | 暂未公开 | 针对 KV-cache 压缩可能同时破坏攻击和安全机制 | 作者揭示 semantic eviction、gradient mismatch 与浅层 head collapse 的双刃效应 | 关键实现：作者揭示 semantic eviction、gradient mismatch 与浅层 head collapse 的双刃效应。 | 并以 Safe-CAM 在低开销下恢复到 0% ASR 且改善良性任务。 |
| 2026 | On Evaluating the Robustness of Large Vision-Language Models via Untargeted Modality Alignment Breaking Adversarial Attack | benchmark、vision-language model、modality alignment、adversarial robustness | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-zhichao) | 暂未公开 | 针对 LVLM adversarial robustness 评测过度依赖定向目标的问题 | MABA 以 untargeted modality-alignment breaking 构造可迁移黑盒攻击 | 关键实现：MABA 以 untargeted modality-alignment breaking 构造可迁移黑盒攻击。 | 使多种模型输出语义相似度平均下降 58.37%。 |
| 2026 | RobustBlack: Challenging Black-Box Adversarial Attacks on State-of-the-Art Defenses | benchmark、black-box attack、robust defense、transferability | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) | 暂未公开 | 针对黑盒攻击往往只在弱防御上得出过强结论的问题 | 作者让 13 种攻击对抗八种 ImageNet 防御 | 关键实现：作者让 13 种攻击对抗八种 ImageNet 防御。 | 发现强白盒鲁棒模型也明显压低黑盒攻击成功率且 surrogate–target 鲁棒性匹配至关重要。 |
| 2025-12 | Read or Ignore? A Unified Benchmark for Typographic-Attack Robustness and Text Recognition in Vision-Language Models | benchmark、typographic attack、adversarial robustness、VLM safety | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4589) · [arXiv](https://arxiv.org/abs/2512.11899) | 暂未公开 | 针对防御排版攻击常靠忽略全部图中文字而损害真实任务的问题 | RIO-Bench 用同场景反事实问题同时测“该读”与“该忽略” | 关键实现：RIO-Bench 用同场景反事实问题同时测“该读”与“该忽略”。 | 并给出兼顾两种能力的数据驱动防御基线。 |

## 机制、理论与 Generalization Analysis

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models | analysis、shared encoder geometry、adaptation transfer、zero-query threat | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16931) | 暂未公开 | 论文把“公开 foundation encoder 是否让不可见 downstream model 继承同一攻击面”拆解到 task geometry 与适配方式：shrinkage-whitened prototype 能从少量标签恢复决策结构。 | 论文把“公开 foundation encoder 是否让不可见 downstream model 继承同一攻击面”拆解到 task geometry 与适配方式：shrinkage-whitened prototype 能从少量标签恢复决策结构 | 且攻击跨四种 encoder、linear probing／full fine-tuning、cross-subject／within-subject 仍迁移 | 这一结果说明公开表征的可复用性会形成跨部署边界共享的 adversarial failure mechanism。 |
| 2026 | Diverge to Converge: Mutual Heterogeneous Learning for Robust Pruning | defense、robust pruning、adversarial perturbation、heterogeneous learning | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6722.pdf) | 暂未公开 | 针对高稀疏率同时削弱对抗与腐蚀鲁棒性 | MHL 训练具有不同平滑和 margin 目标的专家再互蒸馏 | 关键实现：MHL 训练具有不同平滑和 margin 目标的专家再互蒸馏。 | 得到单模型部署的鲁棒剪枝结果。 |
| 2026 | Generalization Analysis for Adversarial Vision Transformer | analysis、vision transformer、adversarial generalization、robustness bound | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2754.pdf) | 暂未公开 | 针对 ViT 对抗泛化缺少理论解释 | 作者用 Rademacher complexity 分析深层扰动累积并给出高概率界 | 关键实现：作者用 Rademacher complexity 分析深层扰动累积并给出高概率界。 | 刻画范数与注意力正则的防御作用。 |
| 2025-12 | The Eminence in Shadow: Exploiting Feature Boundary Ambiguity for Robust Backdoor Attacks ↗ | analysis、feature-boundary geometry、influence function、attack durability | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3780322) · [arXiv](https://arxiv.org/abs/2512.10402) | 暂未公开 | 针对低投毒率后门在再训练和数据扰动下为何仍能泛化的问题 | 论文以 influence-function 理论刻画 feature-boundary ambiguity | 并据此选择高杠杆毒样本 | 低于 0.1% 的投毒仍取得超过 90% ASR，给出后门耐久性的几何解释。 |
