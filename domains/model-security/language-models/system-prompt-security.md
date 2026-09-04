# System Prompt Security

[返回 Language Model Security 目录](README.md)

## 研究方向

本页把 system prompt 视为同时承载应用逻辑、安全 policy、工具规则、persona 和商业知识的隐形软件资产与配置平面，研究其 extraction、leakage、stealing、auditing、instruction conflict、behavioral compliance 与 protection。风险不仅是逐字恢复或功能克隆，也包括 prompt 内部规则互相干扰、用户指令覆盖高优先级约束、persona 或用户身份改变安全边界，以及过度具体的配置诱导模型依赖可被攻击者反转的 shortcut；评测因此需要联合检查 confidentiality、policy consistency、task utility、over-refusal 和 adaptive robustness。

## 研究脉络

- **资产泄漏、功能窃取与克隆验证：** 研究从逐字恢复隐藏 prompt 扩展到以少量 I/O 复制任务功能，并用真实 marketplace prompt 检验 exact、semantic 与 functional recovery 的差异；行为指纹进一步用于验证被提取的 prompt 是否已在可疑服务中重新部署。
- **自动化 extraction：** gradient-free evolution 与 curious code agent 根据黑盒反馈组合攻击策略，使防御必须面对 adaptive query 而不只是固定 jailbreak template。
- **Prompt-as-policy 审计：** AISPA 从用户保护维度审计 instruction span，Arbiter 与 WIRE 则把长 system prompt 当作软件 policy，定位 architecture interference 与 within-policy collision。
- **Instruction hierarchy：** VSysBench 将 system-message compliance 与任务正确性联合评测，区分真正遵守高优先级约束和因约束导致的 capability loss。
- **配置敏感的安全边界：** safety prompt、phishing rule、role persona 和 user identity 都可能改变 safety-utility trade-off；同一 prompt 在不同模型上也可能形成相反的保护效果。
- **表示级与明文保护：** prompt obfuscation、system vector、continuous safety prompt 与 attention re-anchoring 尝试减少明文资产、稳定约束执行并保留应用能力。

## Prompt Extraction 与 Stealing Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges | attack、system prompt、confidential inference、adversarial robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17829) | [Code](https://github.com/yeasen-z/LeakGauge) | 大型语言模型越来越依赖外部上下文。 | 大型语言模型越来越依赖外部上下文 | 例如预定义系统提示或检索文档，以提高生成质量；既有探测研究表明，与泄漏相关的信号会出现在隐藏状态中，但提取这些状态又带来额外部署困难 | 通过激活引导干预，我们进一步表明，风险分数对内部的泄漏相关方向敏感，从而将可观察信号与模型内部表征联系起来。 |
| 2026-06 | AGFPS: An Automated Gradient-Free Framework for Prompt Stealing | attack、prompt stealing、gradient-free evolution、exact recovery | IEEE Transactions on Dependable and Secure Computing 2026 | [DOI](https://doi.org/10.1109/TDSC.2026.3671410) | 暂未公开 | 针对既有 stealing 方法依赖梯度且难扩展到黑盒服务 | AGFPS 以 elite retention、adaptive crossover、mutation 和分段 fitness 进化 adversarial query | 关键实现：AGFPS 以 elite retention、adaptive crossover、mutation 和分段 fitness 进化 adversarial query。 | 结果在多数据集与模型上实现高 exact-recovery rate 并表现出跨模型迁移性。 |
| 2026-04 | Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems ↗ | attack、functional prompt inference、black-box system、proxy prompt | SIGIR 2026 | [Official](https://doi.org/10.1145/3805712.3809691) · [arXiv](https://arxiv.org/abs/2604.23640) | 暂未公开 | 针对攻击者看不到推荐系统的 system prompt 与模型 | PUDA 通过黑盒反馈进化出能复现受害者排序行为的离散 proxy prompt | 再据此训练 surrogate 和构造推广攻击 | 这里恢复的是足以复制功能的隐藏指令结构，而非声称逐字提取原 prompt。 |
| 2026-01 | Just Ask: Curious Code Agents Reveal System Prompts in Frontier LLMs | attack、system prompt extraction、curious code agent、online exploration | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/61428) · [arXiv](https://arxiv.org/abs/2601.21233) | [Code](https://github.com/x-zheng16/JustAsk) | 针对静态 query 无法根据失败结果探索新泄漏策略 | JustAsk 用 UCB 选择 atomic probe 与高层 orchestration skill 并验证多轮恢复的一致性 | 关键实现：JustAsk 用 UCB 选择 atomic probe 与高层 orchestration skill 并验证多轮恢复的一致性。 | 结果在大量黑盒商业模型上恢复完整或接近完整的 system prompt 语义。 |
| 2025-08 | PRSA: Prompt Stealing Attacks against Real-World Prompt Services | attack、prompt stealing、prompt marketplace、functional replication | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/yang-yong) | 暂未公开 | 针对 academic prompt 上的攻击无法代表付费 marketplace 和应用商店 | PRSA 以少量 I/O 推断 prompt intent 并重建可复刻功能的提示 | 关键实现：PRSA 以少量 I/O 推断 prompt intent 并重建可复刻功能的提示。 | 结果在两类真实服务中明显提高窃取成功率并揭示 prompt-output mutual information 与泄漏风险相关。 |
| 2025-05 | On the Effectiveness of Prompt Stealing Attacks on In-The-Wild Prompts | benchmark、prompt stealing、in-the-wild prompt、functional recovery | IEEE Symposium on Security and Privacy 2025 | [CISPA](https://cispa.de/en/research/publications/84717-on-the-effectiveness-of-prompt-stealing-attacks-on-in-the-wild-prompts) | 暂未公开 | 针对学术数据上的 prompt stealing 结果能否迁移到真实用户 prompt | 论文比较二者的长度、主题与语义并引入 text-gradient refinement | 关键实现：论文比较二者的长度、主题与语义并引入 text-gradient refinement。 | 结果虽改善原文和输出恢复指标，但现有攻击在真实 prompt 上仍面临根本限制。 |
| 2024-05 | PLeak: Prompt Leaking Attacks against Large Language Model Applications | attack、prompt leakage、LLM application、black-box query | ACM CCS 2024 | [Official](https://doi.org/10.1145/3658644.3670370) · [arXiv](https://arxiv.org/abs/2405.06823) | [Code](https://github.com/BHui97/PLeak) | 针对 LLM application 把核心逻辑存放在不可见 system prompt | PLeak 自动构造黑盒查询并迭代恢复隐藏指令 | 关键实现：PLeak 自动构造黑盒查询并迭代恢复隐藏指令。 | 结果证明常见“不许泄漏”提示难以阻止自适应提取。 |
| 2024 | Effective Prompt Extraction from Language Models | benchmark、prompt extraction、exact-match verification、secret prompt | COLM 2024 | [OpenReview](https://openreview.net/forum?id=0o95CVdNuz) | [Code](https://github.com/y0mingzhang/prompt-extraction) | 针对 prompt extraction 缺少可复现且能区分真实恢复与 hallucination 的评测 | 论文在多来源 prompt 和多个模型上系统测试简单文本攻击并设计高精度验证 | 关键实现：论文在多来源 prompt 和多个模型上系统测试简单文本攻击并设计高精度验证。 | 结果显示隐藏 prompt 可被高概率直接恢复。 |
| 2023-02 | Prompt Stealing Attacks Against Text-to-Image Generation Models | attack、T2I prompt stealing、subject recovery、modifier detection | USENIX Security 2024 | [USENIX](https://www.usenix.org/conference/usenixsecurity24/presentation/shen-xinyue) · [arXiv](https://arxiv.org/abs/2302.09923) | [Code](https://github.com/verazuo/prompt-stealing-attack) | 针对高价值 T2I prompt 可从生成图像中被反向恢复的问题 | PromptStealer 联合 subject generator 与 modifier detector 重建主题和修饰词 | 关键实现：PromptStealer 联合 subject generator 与 modifier detector 重建主题和修饰词。 | 结果优于图像描述基线并证明生成输出会泄漏 prompt 知识产权。 |

## 防泄漏与资产保护

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Do System Prompts Leave Behavioral Fingerprints? A Large-Scale Empirical Study of Clone Detection via Output Similarity | detection、system prompt fingerprint、black-box clone detection、style robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.24461) | 暂未公开 | 针对 system prompt 被提取并重新部署后原所有者无法验证克隆的问题 | BBF 仅凭黑盒输出注册行为签名 | 并检验可疑服务是否比无关基线更接近该签名 | 同模型检测达到 0.876 AUC，非自适应改写下仍稳健，但单句 formal-tone prefix 可使短结构化输出上的检测接近失效。 |
| 2026-06 | Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications | defense、prompt leakage、attention drift、attention re-anchoring | ACM CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2606.18673) | [Code](https://github.com/yangyZJU/AREA) | 针对真实应用的泄漏规模、内部原因和 defense utility 缺少统一证据 | 论文测量六个平台的 1,200 个应用并把失效归因于 attention drift | 再以 AREA soft prompt 重锚防御指令 | 结果在保持应用功能时显著减少泄漏。 |
| 2025-09 | You Can't Steal Nothing: Mitigating Prompt Leakages in LLMs via System Vectors | defense、system vector、prompt leakage、instruction retention | ACM CCS 2025 | [Official](https://doi.org/10.1145/3719027.3765124) · [arXiv](https://arxiv.org/abs/2509.21884) | 暂未公开 | 针对明文 system prompt 留在 context 中就始终可被诱导复述 | SysVec 将其编码为内部 representation vector 而不放置原始文本 | 关键实现：SysVec 将其编码为内部 representation vector 而不放置原始文本。 | 结果降低未授权披露，同时保持任务功能并缓解长上下文遗忘。 |
| 2025-08 | Prompt Obfuscation for Large Language Models | defense、prompt obfuscation、functional equivalence、deobfuscation attack | USENIX Security 2025 | [USENIX](https://www.usenix.org/conference/usenixsecurity25/presentation/pape) | [Artifact](https://doi.org/10.5281/zenodo.15601914) | 针对明文 prompt 的知识产权无法靠拒绝指令可靠保护 | 论文在离散 token 或连续 embedding 空间寻找功能等价但不可理解的 obfuscated prompt | 关键实现：论文在离散 token 或连续 embedding 空间寻找功能等价但不可理解的 obfuscated prompt。 | 结果在多类 utility 指标上接近原 prompt，并抵抗不同知识条件下的反混淆攻击。 |

## Policy 审计与内部规则冲突

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls | analysis、prompt-as-policy、security rule audit、enforcement mismatch | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23550) | 暂未公开 | 分析 security rule audit、prompt-as-policy 风险的形成机制，重点考察 enforcement mismatch 对安全行为的影响。 | 论文把 CLAUDE.md 视为承载安全 policy 的项目级 instruction surface | 量化相同明文形式如何掩盖两类完全不同的保证：可由 sandbox／permission 强制的规则，以及只能依赖模型解释的规则 | 4%–16% 的控制匹配率揭示 prompt-as-policy 与真实执行语义之间的系统性错位。 |
| 2026-07 | AISPA: User-Centric System Prompt Auditing for Large Language Model Applications | benchmark、system prompt audit、user protection、instruction taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28617) | [Project](https://systempromptindex.ai/) | 针对商业产品的隐藏 system prompt 缺少面向用户的可审计标准 | AISPA 将 prompt 切分为 instruction span 并按八个维度标注 protective 或 problematic | 关键实现：AISPA 将 prompt 切分为 instruction span 并按八个维度标注 protective 或 problematic。 | 对 88 个产品的审计发现保护覆盖普遍不完整且问题指令与保护指令经常共存。 |
| 2026-05 | WIRE: Profiling Witnessed Within-Policy Instruction Collisions in LLM Agents | tool、within-policy collision、symbolic triage、behavioral witness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.27784) | 暂未公开 | 针对长驻 prompt policy 中单条合理规则可能在同一状态共同生效并冲突 | WIRE 将源规则编码为 PYRULE、用 SAT 只提名候选并生成 concrete co-governance witness | 关键实现：WIRE 将源规则编码为 PYRULE、用 SAT 只提名候选并生成 concrete co-governance witness。 | 六份 policy 的可判定试验仅 35.4% 同时满足两条规则，形成可复现的 resolution profile 而非自然语言矛盾证明。 |
| 2026-03 | Arbiter: Detecting Interference in LLM Agent System Prompts | detection、system prompt interference、formal rule、multi-model scouring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.08993) | [Artifact](https://doi.org/10.5281/zenodo.18929834) | 针对 coding agent 的 system prompt 像软件却缺少测试基础设施 | Arbiter 结合 formal evaluation rule 与多模型 scouring 查找指令干扰 | 关键实现：Arbiter 结合 formal evaluation rule 与多模型 scouring 查找指令干扰。 | 结果在 Claude Code、Codex CLI 与 Gemini CLI prompt 中发现 architecture-specific failure class，并以 0.27 美元完成跨模型扫描。 |

## System Message Compliance 与 Configuration Risk

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models ↗ | attack、developer impersonation、system-message trust、configuration risk | 未确认（arXiv） | [arXiv](https://arxiv.org/abs/2609.03247) | 暂未找到公开代码 | 伪造 developer 身份的文本是否会污染 system-message/configuration 遵循，即使并未获得真实权限？ | 把身份声明视为可被模型接受的配置输入，区分口头认证和受限动作执行。 | 黑盒对话测试不同自称开发者请求，比较身份判断、规则遵循和敏感动作结果。 | 模型可能口头承认未验证身份，但实验未显示真实权限提升；文本承诺不能替代授权证据。 |
| 2026-08 | When Context Gets Root: Privilege Escalation in LLM Harnesses | attack、instruction hierarchy、tool-to-system escalation、context provenance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27299) | 暂未公开 | 针对 system／user／tool 层级只在来源标注可信时才有效 | 论文诱导 harness 将低权限 tool content 放进 custom subagent 的 system prompt 或重建为真实 user message | 关键实现：论文诱导 harness 将低权限 tool content 放进 custom subagent 的 system prompt 或重建为真实 user message。 | 攻击在六种 harness 上完成全部 13 个 CIA／RCE 目标，表明 system-message compliance 无法弥补 context provenance 被提升。 |
| 2026-08 | SkillShield: Prompt-Space Security Skills for LLM Coding Agents | defense、system-prompt security、security-skill provisioning、policy compliance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25817) | 暂未公开 | 研究如何防御 system-prompt security、security-skill provisioning 威胁，并评估 policy compliance 条件下的安全收益与效用代价。 | SkillShield 在 session 初始化时把离线合成的 security skill 写入 system prompt | 并研究有限上下文预算下统一、分组和逐类 policy 的配置效果 | 其无需改权重或调用额外 guard model，但安全性仍依赖 Coding Agent 在后续工具循环中持续遵循该高优先级 prompt。 |
| 2026-08 | Compliance, Capability, and Conflict: Benchmarking Multimodal LLMs under System Messages | benchmark、system-message compliance、instruction hierarchy、multimodal constraint | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19207) | [Code（论文声明公开，当前 404）](https://github.com/naver-ai/VSysBench) | 针对多模态 system message 的约束遵循是否以基础能力为代价缺少联合评测 | VSysBench 用五类、22 个子类约束及其冲突用户指令同时衡量 compliance 与 answer correctness | 关键实现：VSysBench 用五类、22 个子类约束及其冲突用户指令同时衡量 compliance 与 answer correctness。 | 结果开源权重模型在冲突下合规性明显崩塌，vision-grounded constraint 对所有模型最难。 |
| 2026-03 | The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities | analysis、prompt-model interaction、phishing detection、shortcut vulnerability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.25056) | [Code & Data](https://github.com/R-Lit/PhishNChips) | 针对 system prompt 是否只是中性的部署配置 | PhishNChips 比较 11 个模型和十种 phishing-detection prompt | 关键实现：PhishNChips 比较 11 个模型和十种 phishing-detection prompt。 | 同一模型的 bypass rate 可从不足 1% 变到 97%，且攻击者反转 domain-matching signal 后能利用过度具体规则形成的 shortcut。 |

## Persona、Personalization 与 Safety-Utility

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2025-02 | The Rise of Darkness: Safety-Utility Trade-Offs in Role-Playing Dialogue Agents | defense、role-playing system prompt、risk coupling、multi-preference alignment | Findings of ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.findings-acl.839/) · [arXiv](https://arxiv.org/abs/2502.20757) | [Code](https://github.com/Toyhom/The-Rise-of-Darkness) | 针对 villain persona 的 system prompt 能提高角色还原却放大有害回答 | 论文把角色与用户请求共同形成的风险建模为 risk coupling | 并用 ADMP 与 Coupling Margin Sampling 动态调整安全和角色效用偏好 | 结果提高安全指标同时维持角色表现。 |
| 2024-06 | Exploring Safety-Utility Trade-Offs in Personalized Language Models | analysis、personalization bias、identity system prompt、safety-utility trade-off | NAACL 2025 | [ACL Anthology](https://aclanthology.org/2025.naacl-long.565/) · [arXiv](https://arxiv.org/abs/2406.11107) | [Code](https://github.com/brcsomnath/personalization-bias) | 针对开发者用 system prompt 注入用户身份后是否公平地维持安全与能力 | 论文跨身份、模型和多类 utility task 测量 personalization bias | 关键实现：论文跨身份、模型和多类 utility task 测量 personalization bias。 | 结果不同身份会显著改变 safety-utility trade-off，DPO 与显式忽略身份的 defense prompt 只能部分缓解。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | Persona Non Grata: Single-Method Safety Evaluation Is Incomplete for Persona-Imbued LLMs | benchmark、persona safety、activation steering、system prompt | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2604.11120) | 暂未公开 | 针对 persona safety 只评测 system prompting 会漏报风险的问题 | 作者在 5,568 个条件上发现 prompt 与 activation steering 暴露不同且依架构变化的漏洞 | 关键实现：作者在 5,568 个条件上发现 prompt 与 activation steering 暴露不同且依架构变化的漏洞。 | 其中看似亲社会 persona 在 Llama 上经 steering 后 ASR 可达约 0.818。 |

## 基础 Tool 与资源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | HieraSuite: A Holistic Toolkit for Building Versatile System-User Instruction Hierarchy | tool、instruction hierarchy、system constraint、system prompt | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) | 论文声明公开，链接待核实 | 针对 LM 在 system 与 user 指令冲突时无法稳定维护高权限约束。 | 针对 LM 在 system 与 user 指令冲突时无法稳定维护高权限约束 | 关键实现：针对 LM 在 system 与 user 指令冲突时无法稳定维护高权限约束。 | HieraSuite 以 221K instruction pair 及数据、模型、训练和评测四组件覆盖 system constraint、隐私安全、steerability 和 override 场景。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | PROVE: Training-Free Prompt Recovery using Verifiable Evidence | analysis、system prompt、prompt extraction、instruction confidentiality | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13671) | 暂未公开 | 分析 system prompt、prompt extraction 风险的形成机制，重点考察 instruction confidentiality 对安全行为的影响。 | 现代文本到图像模型可以根据自然语言提示生成高度逼真的图像 | 而提示反转的最新进展使得从生成的输出中恢复这些提示变得越来越可行，引发了对版权保护和内容所有权的新担忧 | 然而，基于优化的方法通常会产生不可读的提示，字幕方法会产生未经验证的细节，而基于强化学习的方法经常会过度拟合特定的生成器，同时引入评估循环。 |

> 面向外部不可信内容覆盖 system instruction 的攻击见 [Prompt Injection](../../misc/prompt-injection.md)；将 safety-rule retrieval 训练进模型的 ASCL 和通用 over-refusal benchmark 见 [Safety Alignment 与 Refusal](safety-alignment-and-refusal.md)；Agent harness 与运行时权限执行见 [Agent Harness 与 Runtime Security](../../agent/harness-and-runtime-security.md)。
