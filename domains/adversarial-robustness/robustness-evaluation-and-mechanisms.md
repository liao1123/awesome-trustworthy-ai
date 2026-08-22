# 鲁棒性评测与失效机理

[返回上级目录](README.md)

## 研究方向

研究 adversarial robustness 和 distributional robustness 的 benchmark、评测协议、缩放规律与内部机制，重点识别 attack strength、metric、trajectory 和数据分布造成的虚假鲁棒性结论。

## 研究脉络

- **评测协议：** 研究从单次攻击准确率转向 attack suite、worst-case risk 与跨分布比较。
- **内部机制：** Feature geometry、representation pathway 和 training dynamics 用于解释脆弱性与防御迁移。
- **认证有效性：** Audit 工作检查 threat-model 假设、metric leakage 与经验结果是否支持所声称的保证。
- **当前边界：** 开放环境中难以穷举攻击，鲁棒性声明仍必须明确适用范围。

## Benchmark、协议与 Metric Audit

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Geometry Is Not Robustness: A Trajectory-Level Study of PGD Evaluation | benchmark、adversarial robustness、robustness evaluation、failure mechanism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14594) | 暂未公开 | 投影梯度下降（PGD）广泛用于评估对抗鲁棒性，通常通过最终对抗精度来评估，但它不会捕获整个攻击过程中的模型行为；最近的工作提出了轨迹级诊断，例如损失演化、梯度对齐和失败步骤，以更深入地了解对抗性优化动态；这些发现表明，轨迹级诊断描述了优化几何，但不能独立测量对抗鲁棒性。 |
| 2026&#8209;03 | A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness | benchmark、adversarial robustness、robustness evaluation、failure mechanism | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64013) · [arXiv](https://arxiv.org/abs/2603.06594) | 暂未公开 | 针对单一平均指标难以发现前沿模型的稀有失效和部署尾部风险的问题，论文围绕 A Coin Flip for Safety 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于前沿模型风险评测与持续监控。 |
| 2026 | When Efficiency Meets Safety: A Benchmark Security Analysis of KV Cache Compression in Large Language Models | benchmark、robustness evaluation、failure mechanism、distribution shift | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1123/) | 暂未公开 | 针对 KV-cache 压缩可能同时破坏攻击和安全机制，作者揭示 semantic eviction、gradient mismatch 与浅层 head collapse 的双刃效应，并以 Safe-CAM 在低开销下恢复到 0% ASR 且改善良性任务。 |
| 2026 | On Evaluating the Robustness of Large Vision-Language Models via Untargeted Modality Alignment Breaking Adversarial Attack | benchmark、vision-language model、modality alignment、adversarial robustness | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-zhichao) | 暂未公开 | 针对 LVLM adversarial robustness 评测过度依赖定向目标的问题，MABA 以 untargeted modality-alignment breaking 构造可迁移黑盒攻击，使多种模型输出语义相似度平均下降 58.37%。 |
| 2025&#8209;12 | Read or Ignore? A Unified Benchmark for Typographic-Attack Robustness and Text Recognition in Vision-Language Models | benchmark、typographic attack、adversarial robustness、VLM safety | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4589) · [arXiv](https://arxiv.org/abs/2512.11899) | 暂未公开 | 针对防御排版攻击常靠忽略全部图中文字而损害真实任务的问题，RIO-Bench 用同场景反事实问题同时测“该读”与“该忽略”，并给出兼顾两种能力的数据驱动防御基线。 |

## Failure Detection 与 Robustness Monitoring

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Certifying Compressed Language Models: An Audit and a Statistical Toolkit | detection、robustness evaluation、failure mechanism、distribution shift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15046) | [Code](https://github.com/amoghsingh130/flipeval) | 基准精度的一小部分是压缩模型与其原始模型等效的通常证据；我们审核证据的充分性，而不是真相：没有任何主张被称为错误；一项受控实验在五个种子的字节相同校准样本上对 GPTQ 和 AWQ 进行配对。 |

## 机制、理论与 Generalization Analysis

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Accuracy and Robustness of Model Cascades Under Data Perturbations | analysis、adversarial robustness、robustness evaluation、failure mechanism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17711) | 暂未公开 | 预测级联系统可以在保持较高预测性能的同时，显著降低人工智能模型的能耗；虽然这一设计能提高干净数据上的计算效率，但其效果取决于基于置信度的路由是否可靠；这些发现表明，评估节能模型级联不能只看干净准确率，还必须明确关注分布偏移下的路由可靠性。 |
