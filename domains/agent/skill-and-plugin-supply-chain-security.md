# Agent Skill、Plugin 与供应链安全

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究以自然语言说明、脚本、依赖、模型或其他资源封装的 Agent skill/plugin。skill 通常经历 discovery、activation、execution、update 与 reuse，并以 Agent 或用户权限运行；威胁包括恶意 marketplace package、描述诱导、credential theft、代码执行、延迟 payload、self-mutation、skill composition 和 scanner evasion。页面重点是第三方生态与供应链；由 memory 或 trajectory 演化出的持久后门主记录在投毒目录。

## 研究脉络

- **新型 instruction supply chain：** skill 将 prompt、code 和依赖同时变成可安装能力，传统 package scanner 看不见自然语言指令，LLM judge 又可能看不见动态代码行为。
- **攻击生命周期：** 研究从单次恶意执行扩展到 discovery/activation 操纵、延迟复用、self-mutating content 和多个良性 skill 组合后的 emergent harm。
- **真实生态测量：** 大规模 registry crawl 发现 credential theft、RCE、隐藏能力和品牌仿冒已经出现在真实 skill 市场。
- **检测演进：** 防御由 pattern matching 与 LLM review 发展到 sandbox detonation、OS-boundary evidence、taint tracking 和 runtime audit。
- **当前边界：** scanner 对语义等价变形、下载后 payload、环境依赖行为和 signed-but-compromised update 仍缺少稳健保证。

## Survey 与 Threat Model

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation | benchmark、skill lifecycle、SkillSec-Eval、repository admission | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.13987) | 暂未公开 | 针对既有研究集中于 prompt injection 和执行期、忽视 skill 进入仓库到持续演化的完整生命周期；论文提出 SkillSec-Eval，覆盖 admission、retrieval、planner selection、execution 与 evolution，并评测 327 个真实 skill；结果表明漏洞会在执行前后多个阶段产生，需要 lifecycle-aware security evaluation。 |
| 2026&#8209;04 | Towards Secure Agent Skills: Architecture, Threat Taxonomy, and Security Analysis | survey、skill lifecycle、threat taxonomy、structural risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.02837) | 暂未公开 | 针对 Agent Skill 标准快速采用却缺少系统安全定义的问题，论文按 creation、distribution、deployment 和 execution 建立三层十七场景 taxonomy；结论是 instruction/data boundary、持久信任和市场审核缺失属于结构性风险。 |
| 2026&#8209;02 | SoK: Agentic Skills -- Beyond Tool Use in LLM Agents | survey、skill lifecycle、design pattern、governance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.20867) | 暂未公开 | 针对 skill 常被等同于单次 tool call、缺少独立系统抽象的问题；论文沿 discovery、practice、distillation、storage、composition、evaluation 和 update 整理七类设计模式及 representation-scope taxonomy；结论是 marketplace supply chain、prompt injection 和 trust-tiered execution 应纳入完整 lifecycle governance。 |
| 2026&#8209;02 | Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward | survey、progressive disclosure、skill acquisition、trust tier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.12430) | [Code](https://github.com/scienceaix/agentskills) | 针对 skill 的架构、获取、规模化部署与安全讨论分散；论文从 SKILL.md progressive disclosure、skill/MCP 关系、自主获取和 CUA 部署整理该层能力；结论提出按 provenance 分级授权的四层 Skill Trust and Lifecycle Governance Framework。 |
| 2026&#8209;02 | Formal Analysis and Supply Chain Security for Agentic AI Skills | analysis、formal model、supply chain、SkillFortify | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.00195) | [Code](https://github.com/qualixar/skillfortify) | 针对自然语言、脚本和依赖混合的 skill 缺少统一可检查模型；论文形式化 permission、information flow 与供应链验证，并实现 SkillFortify；修订版实验显示 pattern matching 已覆盖该 corpus 的检出项，information-flow analysis 未带来额外检出，明确了形式化保证的适用边界。 |

## 攻击与组合风险

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | CompoSkill: Compositional Skill Chain Attacks from Individually Scanner-Passing LLM Agent Skills | attack、Agent Skill、plugin supply chain、persistent compromise | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16246) | 暂未公开 | 处理长期任务的自主AI 智能体依赖于一次经过一项认证的市场技能：扫描仪返回每项技能的安全判决，并在每个包裹都通过时宣布生态系统安全；我们证明这个假设在技能构成下失败；这些结果暴露了自主AI 智能体单一技能认证方面的系统性差距。 |
| 2026&#8209;08 | ColluSkill: Adversarial Cross-Skill Composition for Evading Agent Skill Scanners | attack、Agent Skill、adversarial robustness、plugin supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.09732) | 暂未公开 | ColluSkill 把恶意目标拆进多个单看合理、通过 scanner 的 skill，并靠 artifact 传递和执行 handoff 在组合时恢复攻击，平均 ASR 达 96.0%；联合分析已安装 skill chain 的 ChainGuard 将 ASR 降至 22.5%，同时放行 99.5% 良性流程。 |
| 2026&#8209;06 | POISE: Position-Aware Undetectable Skill Injection on LLM Agents | attack、skill injection、position-aware blending、stealth | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.07943) | [Code](https://github.com/liofoil/SkillSafety) | 针对 payload 成功却破坏正常任务会暴露攻击的问题，论文把单条良性外观 instruction 放入上下文合适的 setup 位置，并同时要求攻击与用户任务成功；结果在 Skill-Inject 上取得高 ASR 且很少触发新增静态告警。 |
| 2026&#8209;06 | SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction | attack、skill lifecycle、self-mutating poisoning、automated construction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.02540) | 暂未公开 | 针对既有 skill attack 只测一次执行且风险清单零散；论文区分 Fixed-Payload Poisoning 与跨复用的 Self-Mutating Poisoning，并自动构建 879 个攻击样本；结果当前 Agent 在两类设置中最高分别达到 86.3% 和 69.3% ASR。 |
| 2026&#8209;05 | Harmless Yet Harmful: Neutral Prompting Attacks for Stealthy Hallucination Steering in Agent Skills | attack、neutral prompting、package hallucination、supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29354) | 暂未公开 | 针对 coding skill 能否用表面无害提示操纵依赖生成的问题，论文以鼓励想象和穷举的 neutral prompt 提高不存在 package 的生成与安装率；结果攻击改变 hallucinated-name 分布并绕过多类 skill scanner。 |
| 2026&#8209;05 | When Safe Skills Collide: Measuring Compositional Risk in Agent Skill Ecosystems | analysis、skill composition、emergent risk、cross-skill interaction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.00448) | 暂未公开 | 针对逐个审查均良性的 skill 在同一任务中组合后可能形成危险能力链；论文提出 SkillReact 并系统搜索跨 skill data/control flow；结果表明 package-level clean verdict 不能推出组合执行安全。 |
| 2026&#8209;04 | BadSkill: Backdoor Attacks on Agent Skills via Model-in-Skill Poisoning | attack、model-in-skill、semantic trigger、backdoor | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.09378) | 暂未公开 | 针对 skill 可捆绑 learned model 而传统 prompt 审计看不到模型后门的问题，论文在内嵌 classifier 中植入语义组合 trigger；结果跨多种架构保持高 ASR 与良性准确率，暴露独立的模型供应链风险。 |
| 2026&#8209;04 | SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems | attack、skill implementation、payload fragmentation、trigger | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65209) · [arXiv](https://arxiv.org/abs/2604.06811) | [Code](https://github.com/Yunhao-Feng/SkillTrojan) | 针对单个恶意 payload 容易被 skill 审核发现的问题，论文将加密 payload 分散到多个良性外观调用并在 trigger 出现时重组执行；结果在代码型 Agent 中保持良性效用并取得较高攻击成功率。 |
| 2026&#8209;04 | SkillAttack: Automated Red Teaming of Agent Skills through Attack Path Refinement | attack、adversarial prompt、attack path、latent vulnerability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.04989) | [Code](https://github.com/Zhow01/SkillAttack) | 针对不修改良性 skill、只靠用户 prompt 能否利用其潜在高权限路径的问题，论文组合漏洞分析、多入口攻击生成和反馈驱动 refinement；结果在对抗及真实 skill 上显著提高 exploit ASR。 |
| 2026&#8209;04 | Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems | attack、document-driven payload、coding skill、MITRE ATT&CK | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.03081) | 暂未公开 | 针对强对齐模型会拒绝显式恶意 instruction 的问题，论文把 payload 藏入 skill 文档的代码示例和配置模板，使 Agent 在正常复用时执行；结果 DDIPE 在多框架上绕过防御，并发现少量样本同时逃过静态检测和 alignment。 |
| 2026&#8209;04 | How Your Credentials Are Leaked by LLM Agent Skills: An Empirical Study | analysis、credential leakage、cross-modal audit、skill marketplace | ASE 2026 | [arXiv](https://arxiv.org/abs/2604.03070) | 暂未公开 | 针对 skill 文档与程序逻辑共同造成的 credential exposure 难被单模态审计发现的问题，论文静态和动态分析大规模市场样本；结果识别十类泄漏模式，并发现 debug stdout 进入 Agent context 是主要来源。 |
| 2026&#8209;03 | Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance | attack、guidance injection、bootstrap file、OpenClaw | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.19974) | 暂未公开 | 针对 OpenClaw 初始化时自动载入 guidance file 的信任路径，论文把有害动作包装成日常最佳实践并建立 ORE-Bench；结果攻击可在无需确认时执行多类真实副作用，且大部分恶意 skill 逃过现有 scanner。 |
| 2026&#8209;02 | SkillJect: Automating Stealthy Skill-Based Prompt Injection for Coding Agents with Trace-Driven Closed-Loop Refinement | attack、coding skill、closed-loop refinement、payload hiding | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.14211) | [Code](https://github.com/jiaxiaojunQAQ/SkillJect) | 针对手工 skill poison 明显且难适配不同任务的问题，论文让攻击、执行和评估 Agent 根据真实 tool/file trace 闭环优化，并把 payload 隐藏在辅助脚本中；结果在多种 coding-agent 设置持续提高隐蔽攻击成功率。 |
| 2026&#8209;02 | When Skills Lie: Hidden-Comment Injection in LLM Agents | attack、hidden comment、human-model visibility、tool intent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.10498) | 暂未公开 | 针对 HTML comment 对人工审核不可见却会以原始 Markdown 进入模型的问题，论文在良性 skill 中加入隐藏 instruction；结果可诱导敏感工具意图，而把 skill 明确视作不可信输入的防御提示能阻断实验攻击。 |
| 2025&#8209;10 | Agent Skills Enable a New Class of Realistic and Trivially Simple Prompt Injections | attack、agent skill、prompt injection、approval reuse | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.26328) | [Code](https://github.com/aisa-group/promptinject-agent-skills) | 针对 coding Agent 会信任长 skill 文件与引用脚本的问题，论文隐藏恶意 instruction 并利用持久审批外传文件和密码；结果表明现实 skill 路径中的简单注入即可绕过 system-level guardrail。 |

## 检测、审计与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware | detection、scanner evasion、sandbox detonation、taint tracking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.02357) | 暂未公开 | 针对 static/LLM scanner 依赖安装时可见外观；论文用 SkillCloak 保持恶意语义地混淆或自解包 payload，再以 SkillDetonate 在 sandbox 追踪 OS-boundary information flow；结果 evasion 对八类 scanner 大量成功，而 runtime auditor 达到 97% detection、2% false positive。 |
| 2026&#8209;06 | Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security | detection、runtime audit、targeted probing、trace evidence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.11671) | 暂未公开 | 针对安装前静态检查无法看到特定请求、本地状态与多步工具交互触发的行为，论文按风险接口定向构造运行条件并审计 trace evidence；结果在 OpenClaw skill 上较最佳静态基线提高 13 个百分点准确率。 |
| 2026&#8209;05 | Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis | detection、static audit、Datalog reachability、hybrid artifact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.00314) | 暂未公开 | 针对传统 analyzer 忽略自然语言而 LLM judge 无法证明 dataflow 的问题，论文把 skill 提升为 Skill Description Language facts 并以 Datalog 查询风险；结果在真实 marketplace 样本上实现高 recall 与可复现语义审计。 |
| 2026&#8209;04 | RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents | detection、attention hijacking、hidden state、pre-execution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.22888) | 暂未公开 | 针对文本过滤看不出密集合法 instruction 中的 skill poison，论文利用响应时 attention 向恶意 span 偏移的内部信号，并融合 hidden-state alignment；结果能找回大量 lexical screen 漏掉的 description attack。 |
| 2026&#8209;03 | SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration | detection、marketplace audit、semantic-behavior alignment、composition | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.21019) | 暂未公开 | 针对 marketplace 同时存在语义行为不一致和 skill 组合风险的问题，论文以多个审计 Agent 串联准入过滤、对齐检测与组合模拟；结果发现下载量不能代表安全质量，且组合风险会形成大规模关联结构。 |

## Benchmark 与生态测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces | benchmark、skill-mediated risk、CLI agent、rule-based verifier | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.12015) | [Project](https://jinchang1223.github.io/skill-safety-bench-website/) | 针对良性 user request 也会被 skill guidance、local artifact 或 execution file 引向危险动作；论文构建 47 个任务、155 个对抗案例和逐例 rule verifier；结果显示风险随 domain、attack method 及 scaffold-model pairing 明显变化。 |
| 2026&#8209;04 | HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents? | benchmark、harmful skill、ecosystem measurement、implicit intent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.15415) | [Code](https://github.com/TrustAIRLab/HarmfulSkillBench) | 针对 skill 可直接封装网络攻击、诈骗与隐私侵害能力的问题，论文测量两个 registry 并构建真实 Agent benchmark；结果预安装 skill 尤其在隐式有害意图下显著提高模型执行伤害的倾向。 |
| 2026&#8209;03 | SkillTester: Benchmarking Utility and Security of Agent Skills | benchmark、paired execution、security probe、quality assurance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.28815) | [Code](https://github.com/skilltester-ai/skilltester) | 针对 skill 评估只看任务成功或只看恶意模式的问题，论文比较无 skill 与有 skill 的成对执行并独立运行 security probes；结果输出统一 utility、security score 和状态标签，作为可复用 QA harness。 |
| 2026&#8209;03 | Malicious Or Not: Adding Repository Context to Agent Skill Classification | analysis、repository context、false positive、abandoned repository | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.16572) | 暂未公开 | 针对仅凭 SKILL.md 会把大量条目标成恶意的问题，论文联合三类分发源、GitHub repository 与行为上下文重新测量；结果显著降低误报，并识别废弃仓库被接管等此前忽略的攻击向量。 |
| 2026&#8209;02 | Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks | benchmark、skill file、contextual injection、authorization | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.20156) | [Project](https://www.skill-inject.com/) | 针对 skill file 兼具第三方代码、知识与 instruction 却缺少标准攻击评测的问题，论文构建从显式到上下文伪装的 injection-task pairs 并联合衡量 harm 与 utility；结果 frontier Agent 最高 ASR 达 80%，简单过滤和 scaling 均不足。 |
| 2026&#8209;02 | Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality | analysis、ecosystem measurement、skill taxonomy、unsafe capability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.08004) | 暂未公开 | 针对公开 skill 的类别、采用模式和风险缺少整体证据；论文分析一个大型 marketplace 的 40,285 个 skill 及其内容与需求分布；结果发现生态在软件工程任务上高度集中且意图重复，并存在可改变状态或执行系统级动作的非平凡安全风险。 |
| 2026&#8209;02 | "Do Not Mention This to the User": Detecting and Understanding Malicious Agent Skills in the Wild | analysis、skill marketplace、malware measurement、credential theft | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi) · [arXiv](https://arxiv.org/abs/2602.06547) | [Code](https://github.com/protectskills/MaliciousAgentSkillsBench) | 针对社区 registry 缺少标注威胁数据；论文静态筛选并动态验证两个市场的 98,380 个 skill；结果确认 157 个恶意 skill、632 个漏洞，主要路线为 credential/RCE 与文档内 adversarial instruction，披露后相关条目均被移除。 |
| 2026&#8209;01 | Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale | analysis、SkillScan、vulnerability taxonomy、marketplace measurement | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.10338) | 暂未公开 | 针对新兴 skill marketplace 的实际 vulnerability 缺少规模化证据，论文以静态分析和 LLM semantic classification 审计大规模样本；结果归纳 prompt injection、data exfiltration、privilege escalation 与 supply-chain 四类高频风险。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation | analysis、Agent Skill、cyber misuse、plugin supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17588) | 暂未公开 | Agent Skill 把可复用的自然语言流程与可执行资源封装在一起，使软件智能体无需调整模型即可获得特定任务能力；我们提出 TRUSS，一种以证据为引导、用于生成兼具功能效果与安全可靠性的 Agent Skill 的框架；这些结果说明，执行证据能够暴露制品检查遗漏的行为失效，并引导 Skill 生成实现经过联合验证的功能与安全结果。 |
| 2026&#8209;08 | Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents | analysis、Agent Skill、plugin supply chain、persistent compromise | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.11888) | 暂未公开 | 论文以有无 skill 或语义匹配 skill 的成对执行归因 skill-induced failure，并在两套 benchmark 中得到 307 个案例，包括 125 个功能失败与 182 个效率退化；SkillTriage 揭示相关 skill 常把验证清单或重型流程误当成强制步骤。 |

## Benchmark 与评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection | benchmark、Agent Skill、plugin supply chain、persistent compromise | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19901) | [Code](https://github.com/protectskills/MaliciousSkillBench) | 智能体技能通过可复用的指令包扩展 LLM 智能体，这些指令包还可能包含脚本、资源和服务配置；我们提出 MaliciousSkillBench，一个面向恶意智能体技能检测的综合基准；综合来看，这些结果表明，可靠的恶意技能检测既需要覆盖更广泛来源的基准，也需要同时衡量攻击检测能力和对良性技能过度标记情况的评估。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | How a Poisoned litellm Package Compromised an MCP Server in Cursor | FutureSearch | MCP supply chain、unpinned dependency、local execution | [FutureSearch](https://futuresearch.ai/blog/no-prompt-injection-required/) | 复盘 Cursor 自动启动本地 MCP server 时经未锁定依赖下载恶意 PyPI package 的真实事件；说明 Agent extension 安全还必须采用 checksum lock、dependency audit 与远程隔离，不能只防 prompt injection。 |
| 2026&#8209;02 | ClawHavoc: 341 Malicious Clawed Skills Found by the Bot They Were Targeting | Koi Research | ClawHub、skill malware、credential theft | [Koi](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) | 披露 ClawHub 恶意 skill campaign 的 typosquat、伪装 prerequisite、password-protected payload 与 reverse shell 路线，并给出后续扩展和 IOC；它是现实生态观测，不代替同行评审 benchmark。 |

## 基础 Tool

| 时间 | 名称 | 类型 | 链接 | 作用与边界 |
| --- | --- | --- | --- | --- |
| 2026 | Cisco AI Defense Skill Scanner | static and LLM-assisted scanner | [Code](https://github.com/cisco-ai-defense/skill-scanner) | 对 skill metadata、instructions 和 bundled files 做安装前检查；适合 CI/registry gate，但不能替代 sandbox 与最小权限运行时控制。 |
| 2026 | Snyk agent-scan | agent extension scanner | [Code](https://github.com/snyk/agent-scan) | 扫描 Agent 配置、skill 与相关扩展中的已知风险模式；检测范围随规则和可见 artifact 变化。 |
| 2026 | SkillTester | skill testing harness | [Code](https://github.com/skilltester-ai/skilltester) | 在受控环境执行和评估 skill 行为；结果取决于测试覆盖、secret marker、网络策略和环境仿真完整度。 |

> 从 memory、experience 或 trajectory 晋升产生的 skill poisoning 与 backdoor 主记录见 [Agent 记忆与技能投毒](../poisoning-and-backdoors/agent-memory-and-skill-poisoning.md)。
