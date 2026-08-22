# Misinformation 与 Fact Checking

[返回上级目录](README.md)

## 研究方向

研究文本、图像、视频和音频中的 misinformation、fake news 与事实一致性，覆盖 claim verification、动态证据检索、来源归因、协同操纵和可解释纠错。

## 研究脉络

- **静态事实核查：** 早期工作以固定 claim 和证据集合判断真假及支持关系。
- **多模态与动态信息：** Benchmark 扩展到短视频、交错图文、热点演化和实时网页证据。
- **解释与纠错：** Agentic retrieval、verdict-anchored explanation 和 faithful correction 将检测连接到证据与修复。
- **对抗与治理：** 协同操纵、Community Notes 和平台传播研究把单条内容判断扩展到社会技术系统。

## Benchmark 与动态评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Many Ways to Be Fake: Benchmarking Fake News Detection Under Strategy-Driven AI Generation | benchmark、misinformation、fact checking、source attribution | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.09514) | 暂未公开 | 针对现代虚假新闻由人机协作把细微谬误嵌进可信叙事而现有二元数据不足，MANYFAKE 以多种策略生成 6,798 篇文章，显示强 reasoning detector 对全伪故事近饱和，却会在优化后的 mixed-truth 内容上明显失效。 |
| 2026 | VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking | benchmark、multimodal safety、VLM safety、misinformation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1948/) | [Project](https://veritas.mai.informatik.tu-darmstadt.de) | VeriTaS 通过七阶段自动流程每季度更新，现含 104 家机构的 25,000 条真实多模态声明、覆盖 54 种语言，并以标准化解耦分数和文本理由降低持续预训练造成的数据泄漏风险。 |
| 2026 | TrendFact: A Benchmark Towards Hotspot Perception in Automatic Fact-Checking | benchmark、fact-checking、misinformation、fact checking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1219/) | 暂未公开 | TrendFact 用 7,643 条热点样本和 366,634 条证据，并以 ECS、HCPI 衡量有限算力下能否优先核验高影响声明；现有系统表现有限，FactISR 可改善热点感知与效率。 |
| 2026 | Perception, Understanding and Reasoning: A Multimodal Benchmark for Video Fake News Detection | benchmark、multimodal safety、reasoning safety、VLM safety | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2103/) | 暂未公开 | POVFNDB 用 36,240 个人工问答、十项任务和 15 个维度分解视频假新闻的感知、理解与推理，并以验证过的 CoT 数据微调 Qwen2.5VL-7B 获得该任务 SOTA。 |
| 2026 | LiveFact: A Dynamic, Time-Aware Benchmark for LLM-Driven Fake News Detection | benchmark、misinformation、fact checking、source attribution | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.546/) | 暂未公开 | LiveFact 持续更新随时间演化的不完整证据，并分别评测最终分类、证据推理和 benchmark 污染；22 个 LLM 的结果暴露静态基准看不到的“早期不可核验”认知谦逊与推理差距。 |
| 2026 | FactVerse: A Benchmark for Factual Consistency in Interleaved Image–Text Generation | benchmark、misinformation、fact checking、source attribution | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1323/) | 暂未公开 | FactVerse 以 3,000 个中英双语、人工核验实例覆盖四类和 50 个领域，建立交错图文生成的多维事实一致性评测，其评分与人工判断高度一致并揭示现有模型系统性缺陷。 |
| 2026 | All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection | benchmark、misinformation detection、financial AI、misinformation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.492/) | 暂未公开 | RFC-Bench 在段落级比较无参考检测与原文—扰动对照诊断，发现 LLM 有比较依据时明显更强，而纯 reference-free 金融假讯息判断不稳定且无效输出增多。 |

## 平台治理、协同操纵与传播

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Wikipedia in the Era of LLMs: Evolution and Risks | detection、misinformation、fact checking、source attribution | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/68815) | 暂未公开 | 针对生成式 AI 会放大虚假信息、知识污染和来源混淆的问题，论文提出 Wikipedia in the Era of LLMs 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于内容真实性与知识生态安全。 |
| 2026 | Gaming Consensus: Coordinated Manipulation in Crowdsourced Fact-Checking | detection、misinformation、fact checking、source attribution | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64544) | 暂未公开 | 针对快速演进的生成器使深度伪造与 AI 生成内容检测难以跨域泛化的问题，论文提出 Gaming Consensus 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于合成媒体取证。 |
| 2026 | Beyond the Crowd: LLM-Augmented Community Notes for Governing Health Misinformation | analysis、misinformation detection、misinformation、fact checking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.233/) | 暂未公开 | 对 30,800 条健康 Community Notes 的分析发现获得“有帮助”状态中位延迟 17.6 小时且投票者混淆流畅与事实；CrowdNotes+ 用证据和三级评估在 15 个 LLM 上超过人工注释者。 |

## Fact Checking、Evidence 与 Explanation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | REFLEX: Self-Refining Explainable Fact-Checking via Verdict-Anchored Style Control | analysis、fact-checking、misinformation、fact checking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.202/) | 暂未公开 | REFLEX 以基座与微调模型的自分歧构造 verdict-anchored steering vector，仅用 465 个自精炼样本即在 LLaMA 系列达 SOTA，野外数据 macro-F1 最多提升 7.54 分并减少解释幻觉。 |
| 2026 | Emergent Communication Under Misinformation | detection、misinformation、fact checking、source attribution | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61022) | 暂未公开 | 针对生成式 AI 会放大虚假信息、知识污染和来源混淆的问题，论文提出 Emergent Communication Under Misinformation 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于内容真实性与知识生态安全。 |
| 2026 | DiNO: Disinformation Narrative Observer | analysis、misinformation、fact checking、source attribution | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.2160/) | 暂未公开 | DiNO 从乌克兰战争、COVID-19 与移民新闻抽取并跟踪虚假叙事，相对 Relatio、CaNarEx 将主题对齐提高 41%–44%、立场对齐提高 30%–41%。 |
| 2026 | CoT is Not the Chain of Truth: An Empirical Internal Analysis of Reasoning LLMs for Fake News Generation | analysis、misinformation、fact checking、source attribution | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61042) | 暂未公开 | 针对生成式 AI 会放大虚假信息、知识污染和来源混淆的问题，论文围绕 CoT is Not the Chain of Truth 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于内容真实性与知识生态安全。 |

## Multimodal Misinformation 与 Fake News

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | When Misinformation Speaks and Converses: Rethinking Fact-Checking in Audio Platforms | tool、misinformation detection、misinformation、fact-checking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.93/) | 暂未公开 | 该立场论文指出音频假讯息同时依赖韵律、节奏与情绪的“口语性”和跨轮次、说话人的“会话性”，现有转写后文本核查无法覆盖这些结构风险，需重构音频验证流程。 |
| 2026 | From Form to Logic: Masked Reconstruction and Reasoning Distillation for Short Video Fake News Detection | detection、reasoning safety、misinformation、fact checking | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.579/) | [Code](https://github.com/SeinCore/PCDD) | PCDD 用感知流放大短视频局部跨模态矛盾，再把 LLM 逻辑识别蒸馏到轻量学生，避免推理时幻觉和高延迟，并在真实数据上提升检测、可解释性与小数据鲁棒性。 |
| 2026 | From Detection to Understanding: Multi-Turn Reasoning for Video Misinformation Analysis | detection、reasoning safety、misinformation detection、misinformation | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1716/) | 暂未公开 | MisVideoQA 用 12 类欺骗和六层问题评测视频假讯息的感知、意图与说服推理；SOTA MLLM 表现不佳，而 Delphi 式多 agent MisAgent 通过外部证据协作提升准确率与解释质量。 |
| 2026 | FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning | detection、misinformation、reinforcement learning、fact checking | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65720) | 暂未公开 | 针对生成式 AI 会放大虚假信息、知识污染和来源混淆的问题，论文提出 FactGuard 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于内容真实性与知识生态安全。 |

## 事实纠错与干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Mask-to-Correct^+: Leveraging Retriever Diversity for Masking-guided Faithful Fact Correction | defense、misinformation、fact checking、source attribution | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.175/) | 暂未公开 | Mask-to-Correct⁺ 免训练地遮蔽疑似错误 span、用检索证据校正，再集成多种 ranker 降低检索偏差，无需 gold evidence 即在 benchmark 上将 SARI 最多提高 14%。 |
