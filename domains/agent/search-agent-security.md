# Search Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 LLM Search Agent 在自主生成 query、检索开放网页、读取多源证据并综合答案时的安全问题。核心 threat model 包括：有害意图被拆成看似无害的检索步骤、攻击者控制的网页进入 evidence set、检索或训练目标削弱原有 refusal，以及错误证据沿长程 research trajectory 被放大为推荐、引用或行动建议。这里重点评估完整 search loop，而不是只在固定 context 中测试单轮 RAG。

## 研究脉络

- **检索带来的安全退化：** 早期工作发现，从无检索扩展到 Wikipedia 和开放网页后，Agent 的 refusal、bias 与 harmfulness safeguard 会系统性变化，说明正确检索不等于安全综合。
- **有害信息检索红队：** SearchAttack、CREST-Search 与 SafeSearch 将危险目标重写为搜索任务，并检查 query generation、网页引用和最终回答如何共同绕过 base model 的安全边界。
- **网页证据操纵：** SearchGEO、UGC poisoning 与 MisKnow-Agent 从替换检索结果发展到 authority cue、虚假共识和可重复出现的用户生成内容，攻击目标也从“被检索”转向“被 Agent 背书”。
- **长程轨迹劫持：** FORGE 与 Breadcrumbing 利用多个网页和多轮 observation 逐步改变 research plan，表明单页检测不足以覆盖跨文档、跨步骤的 cumulative attack。
- **过程级对齐：** SafeSearch 与 COMPASS 将监督从 final answer 前移到 query 和 trajectory，并同时约束 utility；当前仍缺少在真实搜索排序、动态网页和未知攻击者站点上的端到端防御证据。

## Web Evidence Manipulation 与 Trajectory Hijacking

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Breadcrumbing Search Agents | attack、web evidence poisoning、breadcrumbing、trajectory hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.04565) | 暂未公开 | 针对单页注入无法刻画长程搜索中多个弱信号的累积影响；论文让攻击者控制的页面在不同 query step 中留下相互强化的 breadcrumbs；结果协调式网页 observation 可持续牵引检索轨迹并显著提高目标结论的攻击成功率。 |
| 2026&#8209;07 | SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders | attack、Web-RAG、preference manipulation、recommendation corruption | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.21951) | 暂未公开 | 针对 Web-RAG 推荐会把第三方网页内容转化为排序偏好；论文用 PAIR 驱动的迭代网页改写搜索能稳定提升攻击目标的内容；结果在固定 retrieval context 中，成功候选跨重复实验仍保持较高的目标偏好。 |
| 2026&#8209;07 | Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions | attack、misleading knowledge、authority cues、false conclusion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.20891) | [Code](https://github.com/whfeLingYu/MisKnow-Agent) | 针对 Deep Research 是否会识别看似权威但结论错误的网页证据；论文构造带 authority 与 style cue 的 Misleading Knowledge，并测试长程检索、focused verifier 和前后置防御；结果 Agent 仍会吸收错误知识形成虚假结论，现有核验只能部分缓解。 |
| 2026&#8209;07 | FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents | attack、research trajectory、planning poisoning、evidence chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.04718) | 暂未公开 | 针对只操纵 final context 难以改变 Deep Research 的持续规划；论文组合文内伪造与跨文档证据链并以 PRISM 衡量 planning-level hijack；结果攻击可把早期误导传播到后续 query 与报告，而 Root Query Anchoring 只能降低、不能消除该风险。 |
| 2026&#8209;06 | How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation | benchmark、endorsement corruption、web manipulation、backend variance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.16821) | [Code](https://github.com/Beastlyprime/searchgeo) | 针对被操纵网页是否会从 retrieval exposure 转化为 Agent 的可信背书；论文用 SearchGEO 在 13 个 backend 上测试 machine-layer 与 trust-signal 操纵及 skill recommendation；结果不同 backend 的 ASR 差异显著，prompt defense 也高度依赖底层模型。 |
| 2026&#8209;05 | Deep-Research Agents Can Be Poisoned via User-Generated Content | attack、UGC poisoning、retrieval exposure、source promotion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.24245) | 暂未公开 | 针对攻击者能否只靠一个经常被检索到的用户生成页面影响整组 research query；论文在 STORM、Co-STORM 与 OmniThink 中注入面向 query cluster 的 UGC；结果单一来源即可跨问题提升攻击内容的出现与引用，必须在 retrieval、source trust 和 synthesis 多层防护。 |
| 2026&#8209;01 | “Someone Hid It”: Query-Agnostic Black-Box Attacks on LLM-Based Retrieval | attack、retrieval ranking、query-agnostic suffix、black-box transfer | ICML 2026 | [OpenReview](https://openreview.net/forum?id=bzmt9wJ6uW) · [arXiv](https://arxiv.org/abs/2602.00364) | [Code](https://github.com/JetRichardLee/DQA-Learning) | 针对攻击者不知道 victim query 与模型时仍想压低目标文档的检索排名；论文学习可迁移的 query-agnostic adversarial suffix 并进行黑盒优化；结果攻击可跨查询和检索器隐藏文档，说明 search pipeline 的 ranking layer 本身也是可操纵入口。 |

## Harmful Information-Seeking 与 Red Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | SearchAttack: Red-Teaming LLMs against Real-World Threats via Framing Unsafe Web Information-Seeking Tasks | benchmark、unsafe search task、query framing、knowledge-to-action | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.04093) | 暂未公开 | 针对直接有害 prompt 容易被拒绝但危险目标可外包给网页搜索；论文把真实威胁拆成 skeletal query 和基于检索信息的重构 rubric；结果 web information-seeking framing 能暴露单轮 jailbreak benchmark 看不到的 knowledge-to-action 风险。 |
| 2025&#8209;10 | Deep Research Brings Deeper Harm | attack、deep research、plan injection、intent hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.11851) | [Project](https://chenxshuo.github.io/deeper-harm/) | 针对 Deep Research 的长报告能力是否也会放大危险信息；论文提出 Plan Injection 与 Intent Hijack 绕过研究 Agent 的拒绝边界；结果联网、规划和多源综合可生成比普通聊天模型更完整的有害报告。 |
| 2025&#8209;10 | When Search Goes Wrong: Red-Teaming Web-Augmented Large Language Models | benchmark、web-augmented LLM、query optimization、unsafe citation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.09689) | 暂未公开 | 针对表面正常的 query 是否会驱动联网模型主动检索并引用危险网页；论文提出 CREST-Search 和 WebSearch-Harm，迭代优化 query 与网页证据；结果搜索增强会引入 base model 静态知识之外的 unsafe citation 与内容综合路径。 |
| 2025&#8209;09 | SafeSearch: Automated Red-Teaming of LLM-Based Search Agents | benchmark、automated red teaming、harmful query、search scaffold | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2509.23694) | [Code](https://github.com/jianshuod/SafeSearch) | 针对人工 red-team 难以覆盖多轮 query 与搜索 scaffold 的组合；论文自动生成覆盖五类风险的 300 个案例并评测多种 scaffold 和模型；结果部分配置的 ASR 可达 90.5%，简单安全提醒并不能稳定阻止有害检索。 |
| 2025&#8209;05 | Information Retrieval Induced Safety Degradation in AI Agents | analysis、retrieval access、safety degradation、refusal erosion | NeurIPS 2025 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5aafb56b9b541742388d1ca2a4aa3802-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.14215) | 暂未公开 | 针对更多外部信息是否在提高回答能力的同时改变安全行为；论文比较无检索、Wikipedia 与开放网页访问下的 refusal、bias 和 harmfulness；结果检索范围越开放安全退化越明显，且高 retrieval accuracy 与 prompt mitigation 均不足以消除。 |

## Alignment 与 Defense

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents | defense、process alignment、MCTS、safe trajectory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.30838) | 暂未公开 | 针对 final-answer safety supervision 无法指出搜索轨迹何时偏离；论文用 cognitive MCTS 合成隐蔽危险轨迹并施加 step-level process alignment；结果在较少训练数据下同时改善搜索安全与任务效用，显示 query 和 action 级监督比只约束终局更有效。 |
| 2026&#8209;03 | SafeSearch: Do Not Trade Safety for Utility in LLM Search Agents | defense、multi-objective RL、query shaping、safety-utility | Findings of EACL 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-eacl.146/) | [Code](https://github.com/amazon-science/SafeSearch) | 针对 utility-only finetuning 会进一步提高 Search Agent 的 harmfulness；论文联合 final safety-utility reward 与 query-level shaping 训练 SafeSearch；结果跨三组红队数据把 harmfulness 降低 70% 以上，同时保持 utility-only Agent 的 QA 表现。 |
| 2025&#8209;10 | Agentic Reinforcement Learning for Search Misaligns Instruction-Tuning | analysis、search RL、instruction misalignment、representation steering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.17431) | 暂未公开 | 针对 search RL 只优化答题奖励可能破坏 instruction-tuned safety；论文测量训练前后的 harmful-query behavior 并定位表示空间中的安全方向；结果部分设置的安全性下降最高 68.6%，representation-guided reward 可在不牺牲搜索准确率的情况下恢复对齐。 |

## Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | A Survey of Large Language Model-Based Search Agents | survey、search agent、architecture taxonomy、evaluation | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.374/) | [Repository](https://github.com/YunjiaXi/Awesome-Search-Agent-Papers)（论文列表） | 针对 Search Agent 的模型、搜索环境和训练路线缺少统一视图；论文按 architecture、learning method、tool interaction 与 evaluation 整理研究；结论为安全分析提供从 query formulation 到 evidence synthesis 的系统组件边界，但本身不是安全 benchmark。 |

> 生成式搜索中的内容可见性与 ranking manipulation 见 [Generative Engine Optimization Security](generative-engine-optimization-security.md)；固定或结构化知识库的污染见 [RAG Poisoning](../poisoning-and-backdoors/rag-poisoning.md)；通用网页 instruction/data boundary 见 [Prompt Injection](../misc/prompt-injection.md)；Deep Research 的 factuality、provenance 与 multimodal evidence 评测见 [Scientific Research Agent Reliability](../ai-for-science-safety/scientific-research-agent-reliability.md)。
