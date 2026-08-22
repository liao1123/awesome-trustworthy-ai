# Cybersecurity 与 Dual-Use

[返回上级目录](README.md)

## 研究方向

研究 AI 在漏洞发现、利用、恶意代码、phishing、诈骗、攻防自动化与安全运营中的能力和风险，既覆盖 offensive uplift，也收录可验证的 secure-code 与 cyber-defense 方法。

## 研究脉络

- **能力评测：** CTF、cryptography、vulnerability 和 SOC benchmark 测量模型在真实网络任务中的有效能力。
- **进攻性滥用：** Phishing、scam、malware 与 automated exploitation 研究模型如何降低攻击成本。
- **防御自动化：** Secure generation、vulnerability detection、patching 和 cyber-defense RL 形成可执行防线。
- **治理与边界：** Responsible disclosure、bug bounty 和 dual-use evaluation 约束能力发布与评测证据。

## Phishing、Scam 与 Technology-Facilitated Abuse

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Breaking and Defending LLM-Powered Social Media Bot Detection Systems | detection、cyber misuse、offensive capability、dual-use risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15893) | [Code](https://github.com/runi-cyber-ai/LSABRE) | 社交媒体机器人的兴起构成了持续的威胁，导致错误信息、舆论操纵以及对在线平台信任的侵蚀；为了解决这个问题，人们开发了机器学习系统来检测和限制机器人活动，但攻击者通过对抗性学习和行为模仿等技术不断适应，从而加剧了机器人和检测工具之间持续的军备竞赛；我们引入了两种新颖的对抗性攻击策略，它们系统地利用了基于 LLM 的分类器的语义和上下文弱点，使其检测精度降低了高达 48%。 |
| 2026&#8209;02 | Assessing LLM Response Quality in the Context of Technology-Facilitated Abuse | benchmark、technology-facilitated abuse、LLM response safety、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/prakash) · [arXiv](https://arxiv.org/abs/2602.17672) | 暂未公开 | 针对受害者向 LLM 求助 technology-facilitated abuse 时的安全风险，作者结合专家与用户评测比较四个模型在专门提示下的回答质量，揭示其能力边界并提出面向幸存者支持的设计建议。 |
| 2026 | Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs | detection、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62158) | 暂未公开 | 针对后训练、微调或模型压缩可能削弱安全对齐并放大有害行为的问题，论文构建 Scam2Prompt 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于对齐保持与有害行为缓解。 |
| 2026 | Luring as a Proxy: Evaluating Corpus Transferability for Cybergrooming Detection | benchmark、cyber misuse、offensive capability、dual-use risk | ACL 2026 | [Official](https://aclanthology.org/2026.acl-short.31/) | 暂未公开 | 针对未成年人 cybergrooming 数据稀缺，论文把 grooming 视为 luring communication，系统评估其他诱导和操纵语料能否迁移为检测代理，为低资源在线保护给出数据复用边界。 |
| 2026 | From Trust to Compromise: Outcome-Verified LLM Phishing Simulation and Real-Time Defense | defense、cyber misuse、offensive capability、dual-use risk | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.543/) | 暂未公开 | PhishSim 让多轮社工攻击以受害者在外部恶意平台提交凭证等真实结果作为成功标准，PhishGate 再用多 agent 实时评分与 RAG 复核提升对话级检测，同时暴露防御脆弱性。 |

## Vulnerability、Secure Code 与 Automated Patching

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Securing AI-Generated Code: A Just-in-Time Vulnerability Detection and Remediation Pipeline | detection、AI-generated content、cyber misuse、offensive capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16187) | [Code](https://github.com/Droidsurikov/securing-ai-generated-code) | 人工智能辅助开发工具以极高的速度生成易受攻击的代码，但很少有自动化机制能够以开发速度检测、丰富、修复和验证安全问题，特别是那些在现实世界威胁环境中进行修复的机制；本文提出了一种自动安全评估管道，该管道根据 LLMSecEval 提示生成 Python 代码，使用 CodeQL 和 Bandit 与独立的代码验证器 LLM 并行扫描漏洞，利用 MITRE ATT&CK 技术、CWE 观察示例和 Python 最佳实践指南丰富代码验证器发现结果，通过代码生成 LLM 生成修复程序，并使用 CodeQL 和 Bandit 重新扫描以验证结果；值得注意的是，最好的代码生成 LLM (Opus 4.8) 并不是最好的流程执行者，因为 Sonnet 4.6 在 P2 修复后产生了最低的残留结果和最高的通过率，这表明流程有效性和初稿安全性是不同的属性。 |
| 2026 | SecCodePRM: A Process Reward Model for Code Security | analysis、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64014) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文围绕 SecCodePRM 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于危险能力评测与高风险部署治理。 |
| 2026 | PatchWeaver: Risk-Bounded Autonomous Vulnerability Remediation Under Change-Management Policies | defense、autonomous remediation、risk-bounded agent、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-rui) | 暂未公开 | 针对 LLM remediation agent 容易违反维护窗口、审批和 blast-radius 等规则的问题，PatchWeaver 以资产图、ChangeSpec 和短视界模拟约束规划，较工具链和 LLM agent 分别减少 52.5% 与 79.1% 的 step-level policy violation。 |
| 2026 | Learn from Your Mistakes: Tree-like Self-Play for Secure Code LLMs | defense、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61209) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文提出 Learn from Your Mistakes 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险能力评测与高风险部署治理。 |
| 2026 | Is Vibe Coding Safe? Benchmarking Vulnerability of Agent-Generated Code in Real-World Tasks | benchmark、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61427) | [Code](https://github.com/LeiLiLab/susvibes) | 针对工具型智能体会受到环境、记忆、检索和跨智能体通信攻击的问题，论文构建 Is Vibe Coding Safe Benchmarking 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于智能体攻击面治理。 |
| 2026 | From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching | attack、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65663) | 暂未公开 | 针对模型输出、梯度、记忆或检索库可能泄露训练数据和真实身份的问题，论文提出 From Similarity to Vulnerability 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于训练数据和身份泄漏评估。 |
| 2026 | DeepGuard: Secure Code Generation via Multi-Layer Semantic Aggregation | defense、cyber misuse、offensive capability、dual-use risk | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.907/) | 暂未公开 | DeepGuard 聚合多个中高层中较明显的漏洞线索，以安全 analyzer 和多目标训练兼顾正确性，在五个 code LLM 上将“安全且正确”生成率较 SVEN 等强基线平均提升 11.9%。 |
| 2026 | Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation | defense、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64101) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文提出 Autoregressive, Yet Revisable 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险能力评测与高风险部署治理。 |
| 2026 | AutoBaxBuilder: Bootstrapping Code Security Benchmarking | benchmark、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64856) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文构建 AutoBaxBuilder 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于危险能力评测与高风险部署治理。 |

## Offensive Capability 与 Dual-Use Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus | analysis、adversarial robustness、cyber misuse、offensive capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19266) | [Code](https://github.com/rocklambros/incident-rank-validation) | OWASP LLM 应用十大风险对安全从业者社群认为最重要的风险进行排名；我们提出一个更窄的问题：与真实事件记录对照时，专家排名是否与数据一致？我们从 CVE、GHSA、OSV 和 AIAAIC 汇集大规模 LLM 安全事件语料库，其中快照事件 7,714 条，依据 20 项分类法标注的事件 6,639 条；随后使用贝叶斯测量误差模型，根据分类器精确率和召回率校正每个类别的计数，得到基于事件的排名。 |
| 2026&#8209;08 | Beyond the Hype: Evaluating LLM Integration and Practical Limitations in Security Operation Centers | benchmark、cyber misuse、offensive capability、dual-use risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17154) | 暂未公开 | 安全运营中心 (SOC) 中越来越多地探索大语言模型 (LLM)，以支持文本密集型分析工作，例如警报上下文化、事件摘要和起草调查制品；在本文中，我们展示了对 20 名 SOC 从业者（包括一线分析师、SOC 经理和工具开发人员）进行半结构化访谈的结果。 |
| 2026&#8209;02 | GoodVibe: Security-by-Vibe for LLM-Based Code Generation | defense、code generation、cyber misuse、offensive capability | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/thang) · [arXiv](https://arxiv.org/abs/2602.10778) | 暂未公开 | 针对 LLM 代码生成中的漏洞与全量安全微调开销，GoodVibe 定位 security-relevant neurons 并选择性调优，使安全代码生成最高提高 2.5 倍，同时较 LoRA 使用少 4,700 倍可训练参数和少 3.6 倍计算。 |
| 2026&#8209;01 | VIPER Strike: Defeating Visual Reasoning CAPTCHAs via Structured Vision–Language Inference | attack、visual reasoning CAPTCHA、VLM safety、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/qi-minfeng) · [arXiv](https://arxiv.org/abs/2601.06461) | 暂未公开 | 针对依赖关系推理的新型 visual CAPTCHA 被认为能抵抗自动化的问题，VIPER 以结构化 vision-language inference 解析题面，最高取得 93.2% 破解率，并据此提出 TSR 防御。 |
| 2026 | From Assistance to Autonomy: An Empirical Study of AI Use in a Live Capture-the-Flag (CTF) Competition | benchmark、CTF agent、human-in-the-loop、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tang-tingxuan) | 暂未公开 | 针对 AI 在真实网络攻防竞赛中的自主能力与人机协作边界，作者通过 41 名参赛者的现场研究和四个 autonomous agent 对照，发现 human-in-the-loop 表现最佳且 AI 主要放大已有专家能力。 |
| 2026 | Beyond Rewards in RL for Cyber Defence | defense、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64372) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文提出 Beyond Rewards in RL for 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险能力评测与高风险部署治理。 |
| 2026 | AICrypto: Evaluating Cryptography Capabilities of Large Language Models | benchmark、cyber misuse、offensive capability、dual-use risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63082) | [Code](https://github.com/wangyu-ovo/aicrypto-agent) | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文构建 AICrypto 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于危险能力评测与高风险部署治理。 |
| 2025&#8209;12 | COGNITION: From Evaluation to Defense against Multimodal LLM CAPTCHA Solvers | benchmark、VLM safety、cyber misuse、offensive capability | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-junyu) · [arXiv](https://arxiv.org/abs/2512.02318) | 暂未公开 | 针对 MLLM 自动破解真实 CAPTCHA 的能力，COGNITION 评测七个模型与 18 类挑战，并以局部化和隐式计数 hardening 将原本超过 95% 的破解成功率降至 0。 |

## SoK、Survey 与研究议程

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | SoK: The Pitfalls of Deep Reinforcement Learning for Cybersecurity | survey、cyber misuse、offensive capability、dual-use risk | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/mcfadden) · [arXiv](https://arxiv.org/abs/2602.08690) | 暂未公开 | 针对 deep reinforcement learning for cybersecurity 的实验结果难以复现和部署，该 SoK 审查 66 篇论文并总结 11 类方法陷阱，平均每篇超过五项，并通过 cyber defense、malware 与 Web 实验验证其影响。 |
| 2026&#8209;02 | SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned | survey、AIxCC、cyber misuse、offensive capability | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhang-cen) · [arXiv](https://arxiv.org/abs/2602.07666) | 暂未公开 | 针对 AIxCC 如何评测自主漏洞发现与修复能力，该 SoK 系统分析竞赛设计、决赛系统架构、实测结果与局限，提炼 AI cyber reasoning 走向真实部署的工程和安全经验。 |
| 2026 | SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framework | survey、AI phishing detector、security evaluation、cyber misuse | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/alam) | 暂未公开 | 针对 AI phishing detector 文献的功能和安全结论难以横向核验，PHILTER 复核 55 项研究，发现没有工作同时满足全部要求，也缺乏能处理多样且持续演化攻击策略的证据。 |
