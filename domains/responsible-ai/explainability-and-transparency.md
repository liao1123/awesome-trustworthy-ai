# 可解释性与 Transparency

[返回上级目录](README.md)

## 研究方向

研究 explanation、feature attribution、mechanistic interpretation、transparency artifact 和 auditability，重点检查解释是否忠实、稳定、可操作，并避免把可读叙述误当作因果证据。

## 研究脉络

- **事后解释：** Saliency、attribution 和 example-based explanation 为单次输出提供局部说明。
- **机制解释：** Representation、circuit 和 causal intervention 尝试验证内部成因。
- **解释审计：** Robustness、faithfulness 和 demographic consistency benchmark 检查解释本身是否可靠。
- **部署透明度：** Model card、trace 和 evidence artifact 将可解释性连接到外部问责。

## Attribution、Transparency 与 Auditability

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Multimodal Model Diffing for Feature Discovery and Control | analysis、VLM safety、explainability、model transparency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.09928) | 暂未公开 | MMDiff 对 base LM 与多模态适配模型的 SAE 做 feature diff，定位并因果操纵视觉能力与安全特征；移除对应特征可使多模态攻击 ASR 平均下降 24% 且不损害 VQA，说明 feature interface 可同时用于审计和安全 steering。 |
| 2026&#8209;06 | Explainability-aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors | detection、LiDAR、explainability、model transparency | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5021) · [arXiv](https://arxiv.org/abs/2606.29963) | 论文声明公开，链接待核实 | 针对三维检测器空间依赖不透明的问题，SALL 先生成通用显著性图再由 EFA 攻击关键视锥，以少 25%–50% 的扰动视锥令检测召回下降超过 15 个百分点，揭示感知安全脆弱性。 |
| 2026 | Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection | detection、AI-generated content、explainability、model transparency | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61817) | 暂未公开 | 针对快速演进的生成器使深度伪造与 AI 生成内容检测难以跨域泛化的问题，论文提出 Hermes 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于合成媒体取证。 |
| 2026 | Beyond External Monitors: Enhancing Transparency of Large Language Models for Easier Monitoring | detection、explainability、model transparency、auditability | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65911) | 暂未公开 | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文提出 Beyond External Monitors 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026 | BanHADEX: Towards Explainable HAte Speech Detection in Bangla Using Human Annotated EXplanation | detection、explainability、model transparency、auditability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2022/) | 暂未公开 | 针对 Bangla hate speech 只有分类、缺少文化化解释，BanHADEX 为 19,203 条评论标注七类危害、七类目标和人工解释，explanation-guided LoRA 同时提升分类与解释质量。 |
| 2026 | At the Edge of Understanding: Sparse Autoencoders Trace The Limits of Transformer Generalization | detection、sparse autoencoder、explainability、model transparency | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65535) | 暂未公开 | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文围绕 At the Edge of Understanding 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于对齐保持与有害行为缓解。 |

## Mechanistic Interpretability 与 Causal Analysis

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Explanation Multiplicity: Circuit-Level Interpretability Evidence Does Not Survive Defensible Analytic Variation | analysis、explainability、model transparency、auditability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13754) | 暂未公开 | 欧盟人工智能法案要求高风险系统的提供商提交技术文件，描述系统如何做出决策；我们询问这些证据是否能够在其所依赖的条件下继续存在：两个有能力的分析师、相同的系统、相同的工具、不同的防御设置；我们将可归档性标准作为独立协议给出，并且我们报告七个记录的发现目标之一根本不执行图书馆自己的规范任务。 |
| 2026 | Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI | detection、explainability、model transparency、auditability | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2018/) | 暂未公开 | EAVAE 以对比预训练和分离的 style/content encoder 解耦作者风格与主题，再让判别器同时分类并生成解释，在多个作者归因集达 SOTA、M4 的少样本 AI 文本检测也表现突出。 |

## Explanation Benchmark 与 Faithfulness Audit

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents | benchmark、explainability、model transparency、auditability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17524) | 暂未公开 | 这篇初步论文概述了一个计划用于评估可解释强化学习（XRL）方法的基准；我们建议根据 XRL 方法所生成的解释，在多大程度上能帮助诊断并修复发生故障的强化学习（RL）智能体来评估这些方法。 |
| 2026&#8209;08 | Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments | benchmark、explainability、model transparency、auditability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16747) | [Code](https://github.com/adamkarvonen/chive) | 人工智能研究的许多领域，例如语言模型的可解释性和思维链的可信度，都试图解释模型的行为；但什么才是“好的”解释呢？在这项工作中，我们通过反事实可模拟性的角度来评估解释——该解释是否有助于预测相关反事实输入的模型行为；总的来说，CHIVE 自动发现自然发生的 LLM 行为的解释，使我们能够评估和改进解释 LLM 行为的方法。 |
