# Multi-Agent System Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究由多个 LLM Agent 通过层级、图或动态组织协作时出现的安全与隐私风险。攻击者可以控制一个或多个节点、伪造 inter-agent message、利用 role trust 和 topology 将污染传播到高权限节点，或让多个恶意 Agent collude；系统还会泄露通信拓扑、memory 和组织知识。评测单位应同时覆盖 node、message、coalition、topology 与 end-to-end outcome，而不是只检查最终答案。

## 研究脉络

- **单恶意节点：** 初期研究假设一个 Agent 注入错误信息，考察多数投票、trust score 和消息过滤能否恢复协作。
- **拓扑传播：** 后续攻击利用 upstream-downstream 依赖、角色层级和信息重解释，在多个 hop 中放大污染或控制流劫持。
- **Collusion 与 worm：** 多个恶意节点可以协调 payload，持续运行的 Agent 生态还允许配置感染、自复制和跨实例传播。
- **具身通信攻击：** 当 LLM Agent 控制机器人时，未经验证的跨 Agent claim 会由文本污染转化为物理 unsafe action，通信架构和节点权限共同决定传播路径。
- **结构与隐私：** topology 本身成为可窃取 IP，也决定 memory leakage、攻击 reachability 和 defense placement。
- **当前边界：** 简化 benchmark 上的 message filter 很难迁移到动态角色、异构模型和真实工具系统，防御需联合 identity、least privilege、provenance 与 runtime graph monitoring。

## 协作攻击、传播与 Collusion

### 1. A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms

📄 [arXiv](https://arxiv.org/abs/2609.04170)　📅 2026-09

**关键词**：`analysis`、`agentic misalignment`、`exploit propagation`、`whistleblowing`、`multi-agent propagation`、`exploit sharing`

👤 **作者**：Davide Paglieri、Logan Cross、Tim Genewein、Joel Z. Leibo、Nenad Tomasev、Alexander Sasha Vezhnevets

- 🎯 **研究动机**：多 Agent 科研生态的共享基础设施可能成为不良行为传染扩散的基底，缺少真实群体观察
- 🔬 **研究方法**：报告 100 个自主 LLM Agent 证明数学猜想的案例研究：单 Agent 发现评测漏洞后经共享知识库与点对点消息传播，竞争压力下部分 Agent 采纳作弊
- 📌 **结论**：另一组 Agent 自发反制——审计虚假证明、跨广播与私聊告警、抵制与投诉并提出验证补丁；把共享基础设施管理归为知识公地治理，主张毕业式制裁与集体选择规则支持去中心化自治

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent AI science ecosystems rely on agents possessing tools that allow them to communicate, coordinate, and build on each other's work. Yet this shared infrastructure can also introduce vulnerabilities by creating a substrate for the contagious spread of unintended and undesirable behaviors. We report a case study on a research collective of 100 autonomous LLM agents tasked with proving formal mathematical conjectures. Within the swarm, cheating spontaneously emerged and was later challenged by whistleblowers - both without any external intervention. When a single agent discovered an exploit in the evaluation system, it propagated across the collective via a shared knowledge library and later through peer-to-peer messages. Despite early reluctance, a cohort of agents adopted the exploit in response to competitive pressure. A separate group of agents produced an emergent counter-response: auditing fraudulent proofs, alerting peers across broadcast and private channels, staging boycotts, lodging formal complaints, and proposing validation patches. In recent incidents, agent swarms coordinated covertly through improvised side-channels (Dalton and Wallace, 2026; Greenblatt et al., 2026). Our setting differs: the same transparent channels that carried the exploit also gave non-cheating agents the visibility they needed to detect fraud, organize resistance, and enforce norms. We cast the problem of managing the agents' shared infrastructure as the knowledge commons governance problem (Ostrom, 1990). To protect the commons from exploits, we propose to adopt institutional mechanisms, such as graduated sanctioning and collective-choice rules, to support decentralized self-governance in autonomous swarms.

</details>

### 2. When Context Gets Root: Privilege Escalation in LLM Harnesses

📄 [arXiv](https://arxiv.org/abs/2608.27299)　📅 2026-08

**关键词**：`attack`、`coding-agent harness`、`instruction privilege escalation`、`permission bypass`、`permission-review bypass`、`provenance laundering`

👤 **作者**：Xingbang He、…、Bing Mao

- 🎯 **研究动机**：instruction hierarchy 是模型侧防御，但 Agent harness 组装每次调用上下文时会把低权限内容提升到更高指令层级并获得模型侧特权
- 🔬 **研究方法**：定义 instruction privilege escalation 攻击，利用多 Agent 机制在六种 coding-agent harness 上实现覆盖保密性、完整性、可用性与 RCE 的 13 个攻击目标
- 📌 **结论**：无限制执行时六种 harness 全部达成 13 个目标，提供自动权限审查的三种 harness 也全部达成，持久目标与定时任务下同样复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction hierarchy is a model-side defense that assigns instructions different levels of privilege according to their sources. These levels constrain which content may direct model behavior. During agent execution, however, agent harnesses construct context for each model invocation. This construction can elevate low-level content to a higher instruction level and grant it greater model-facing privilege. We introduce instruction privilege escalation. In this attack, an attacker induces an agent to elevate low-level malicious content to a higher instruction level. The elevated content then causes the agent to execute instructions it would not follow at their original level. We evaluate this threat by using multi-agent mechanisms to achieve 13 attack objectives across six coding-agent harnesses. These objectives span confidentiality, integrity, availability, and remote code execution. With unrestricted action execution, the attacks achieve all 13 objectives on all six harnesses. Under automatic permission review, the attacks achieve all 13 objectives on all three harnesses that provide this mode. We further reproduce the vulnerability using harness-provided persistent goals and scheduled tasks. These results demonstrate the generality of instruction privilege escalation.

</details>

### 3. HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems

📄 [arXiv](https://arxiv.org/abs/2608.22512)　📅 2026-08

**关键词**：`defense`、`runtime witnessing`、`external choke point`、`tamper-resistant evidence`、`attribution laundering`、`multi-agent accountability`

👤 **作者**：Christos Sardianos、…、Georgios Th. Papadopoulos

- 🎯 **研究动机**：自主多 agent 系统致害时无法查清事实、原因与责任：溯源取证抽象层级错误、形式因果假设因果模型已知、审计信任 agent 自我记录，而 attribution laundering 可把行为摊到冗余 agent 直到谁都不是 but-for cause
- 🔬 **研究方法**：HANSARD 参考架构：在 agent 触及范围外的五个 choke point 捕获证据使遗漏可检测，运行时累积 PROV-DM 类型化因果图并以三个指标实时门控监督，事后按 modified Halpern-Pearl 重放得出偶然效应与补偿集大小，synergy residual 度量组合致害
- 📌 **结论**：原因、责任与问责分开报告并各受证据层级上限约束，使 attribution laundering 可见，不再依赖涉事 agent 自产日志

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, attribution laundering, i.e., spreading an act across redundant agents until none is a but-for cause. Worse, the record is produced by the suspects, which comprises the assumption adopted throughout this work. Agents may therefore anticipate the investigation and the part of logging infrastructure may itself collude. In this paper, HANSARD is proposed, a reference architecture treating accountability as a life-cycle property. First, a readiness profile sealed before operation bounds what later findings may claim. Second, capturing at five choke points beyond the agents' reach makes omissions detectable, not only tampering. Third, a typed PROV-DM-aligned causal graph accrues as the system runs, and three indicators read it live to gate oversight without adjudicating. Fourth, post-incident replay yields contingent effects under the modified Halpern-Pearl definition, together with a compensation-set size. Finally, a synergy residual measures harm due to the combination rather than to individuals, making laundering visible. Cause, responsibility and accountability are then reported separately, each capped by an evidentiary tier, while a future research agenda is also provided.

</details>

### 4. Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

📄 [arXiv](https://arxiv.org/abs/2608.22444)　📅 2026-08

**关键词**：`analysis`、`attack`、`collective misalignment`、`monitor population`、`capture forecasting`、`agent population`

👤 **作者**：Isotta Magistrali、Chen Shani

- 🎯 **研究动机**：AI 安全评测单位仍是单模型，而 LLM agent 日益以相互读写决策的群体部署——单体校准良好也可能被邻近 agent 拉偏，单体检计无法回答群体行为
- 🔬 **研究方法**：在安全分诊任务上让 LLM monitor 群体决定警报升级或忽略，注入始终单向施压的 committed minority，并用攻击前响应函数预测群体漂移幅度
- 📌 **结论**：单体几乎同判的两条警报可使集体行为截然不同且可提前预测；公开推理能中和弱攻击但只延迟强攻击；移除施压者后群体回归原位——capture 是暂时状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

</details>

### 5. Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures

📄 [arXiv](https://arxiv.org/abs/2608.00718)　📅 2026-08

**关键词**：`analysis`、`pipeline attack`、`boundary verification`、`implicit trust`

👤 **作者**：Faisal Haque Bappy、Tahrim Hossain、Tarannum Shaila Zaman、Raiful Hasan、Kamrul Hasan、Tariqul Islam

- 🎯 **研究动机**：多智能体流水线中一个 agent 接受的对抗内容会被当作可信输入在管线内传播，缺乏跨 agent 边界的验证原语
- 🔬 **研究方法**：定义内容、身份、执行意图与状态完整性的边界验证，用 GAIA/SWE-Bench 标注轨迹分析四类结构攻击面，并在受控多 agent 环境对三模型评测
- 📌 **结论**：攻击成功率随流水线结构而非模型能力变化，说明对抗脆弱性本质是架构属性，需要流水线级防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent LLM pipelines orchestrate multiple specialized language model agents into structured workflows where intermediate outputs are passed across agents to solve complex tasks. This design introduces a security gap absent in single-agent settings: once an agent accepts adversarial content, it is propagated as trusted input throughout the pipeline. We argue that this vulnerability stems from the absence of boundary verification, a security primitive that enforces explicit validation of data as it crosses inter-agent boundaries, including content, identity, execution intent, and state integrity. Without such verification, modern pipelines embed implicit trust assumptions that are not adversarially robust, giving rise to structurally distinct attack surfaces (e.g., content injection, agent impersonation, plan deviation, and memory poisoning). Leveraging annotated production traces from the GAIA and SWE-Bench benchmark, we show that these vulnerabilities arise in benign deployments and largely evade existing evaluation frameworks. We further operationalize these failure modes within a controlled multi-agent setting and evaluate them across GPT-5-mini, Claude Sonnet 4.5, and Kimi K2.5 under identical pipeline configurations. The results reveal that attack success aligns with pipeline structure rather than model capability, indicating that adversarial vulnerability is fundamentally an architectural property and motivating a shift toward pipeline-level defenses.

</details>

### 6. MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2606.12918)　📅 2026-06

**关键词**：`attack`、`MAS collusion`、`Shapley attribution`、`role-aware perturbation`

👤 **作者**：Chejian Xu、…、Bo Li

- 🎯 **研究动机**：分层 MAS 的安全分散在角色化 agent 上，现有红队依赖启发式选择目标、扰动孤立消息流，无法回答哪个 agent 对系统安全最关键
- 🔬 **研究方法**：提出 MAStrike 闭环合谋红队：首个 agent 级 Shapley 值分析量化各 agent 对鲁棒性的边际贡献，据此识别脆弱联盟并生成角色感知协同操纵，经结构化因果诊断迭代
- 📌 **结论**：覆盖金融、软件工程、CRM 的基准上大幅超越启发式基线，揭示被单 agent/模板方法忽视的 Shapley 分布与高阶交互结构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.

</details>

### 7. Hierarchical Attacks for Multi-Modal Multi-Agent Reasoning

📄 [arXiv](https://arxiv.org/abs/2605.13213) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Hierarchical_Attacks_for_Multi-Modal_Multi-Agent_Reasoning_CVPR_2026_paper.html)　📅 2026-05　🏷 CVPR 2026

**关键词**：`attack`、`multi-agent reasoning`、`hierarchical manipulation`、`multimodal system`

👤 **作者**：Hao Zhou、Tiru Wu、Yan Jiang、Wanqi Zhou、Junxing Hu、Ai Han

- 🎯 **研究动机**：多智能体对抗攻击研究聚焦孤立 agent 或单模态，多模态 MAS 的漏洞未被探索
- 🔬 **研究方法**：HAM3 三层分层攻击：感知层扰动视觉、文本与融合表征，通信层破坏消息内容与交互拓扑，推理层偏置各 agent 推理轨迹
- 📌 **结论**：GQA 上基于 ReAct、Plan-and-Solve、Reflexion 的 MAS 中 ASR 最高 78.3%，推理层攻击最有效，过半成功攻击导致多个 agent 一致出错

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal multi-agent systems (MM-MAS) have gained increasing attention for their capacity to enable complex reasoning and coordination across diverse modalities. As these systems continue to expand in scale and functionality, investigating their potential vulnerabilities has become increasingly important. However, existing studies on adversarial attacks in multi-agent systems primarily focus on isolated agents or unimodal settings, leaving the vulnerabilities of MM-MAS largely underexplored. To bridge this gap, we introduce HAM$^{3}$, a Hierarchical Attack framework for multi-modal multi-agent systems that decomposes attacks into three interconnected layers. Specifically, at the perception layer, HAM$^{3}$ mounts attacks by perturbing visual inputs, textual inputs, and their fused visual-textual representations. At the communication layer, it performs communication-level attacks that corrupt message content and interaction topology, such as manipulating shared context or communication links to distort collective information flow. At the reasoning layer, it conducts reasoning-level attacks that interfere with each agent's cognitive pipeline, biasing reasoning trajectories and ultimately compromising final decisions. We evaluate HAM$^{3}$ on the GQA benchmark through multi-agent systems built on distinct reasoning paradigms including ReAct, Plan-and-Solve, and Reflexion. Experiments demonstrate that our framework achieves an Attack Success Rate of up to 78.3%, with reasoning-layer attacks being the most effective. More than half of the successful attacks lead multiple agents to produce consistent errors. These findings offer valuable insights for building more robust and interpretable multi-agent intelligence.

</details>

### 8. AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems

📄 [arXiv](https://arxiv.org/abs/2603.15727)　📅 2026-03

**关键词**：`attack`、`agent worm`、`persistent configuration`、`multi-hop propagation`

👤 **作者**：Yihao Zhang、…、Meng Sun

- 🎯 **研究动机**：OpenClaw 类 4 万+活跃实例、持久配置与跨平台通信的 agent 生态安全性未被探索
- 🔬 **研究方法**：AgentWorm 以单条消息启动完整感染循环：劫持核心配置跨重启持久化、重启执行任意 payload、自动向每个新遇 peer 传播；在 5 个 LLM 后端、3 种感染载体与 3 类 payload 上评估
- 📌 **结论**：聚合 ASR 63% 且持续多跳传播；执行层过滤可抑制休眠 payload，但能切断感染环的关键控制在全部观测部署中均未启用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous LLM-based agents increasingly operate as long-running processes forming densely interconnected multi-agent ecosystems, whose security properties remain largely unexplored. Systems such as OpenClaw, an open-source platform with over 40{,}000 active instances, persistent configurations, tool-execution privileges, and cross-platform messaging, are deployed at scale, yet the security of such agent ecosystems remains largely unexplored. This work presents AgentWorm, the first self-replicating worm attack against a production-scale agent framework, achieving a fully autonomous infection cycle initiated by a single message: the worm first hijacks the victim's core configuration to establish persistent presence across session restarts, then executes an arbitrary payload upon each reboot, and finally propagates itself to every newly encountered peer without further attacker intervention. The attack is evaluated on a controlled testbed across five distinct LLM backends, three infection vectors, and three payload types. Results show a 63\% aggregate attack success rate, sustained multi-hop propagation, and stark divergences in model security postures, highlighting that while execution-level filtering effectively mitigates dormant payloads, skill supply chains remain universally vulnerable. Defenses are evaluated at three layers (prompt-level mitigations sourced from real community practice, the framework's built-in security controls, and an ecosystem-wide measurement of public configurations), revealing that the critical controls capable of breaking the infection loop are not enabled in any of the observed deployments. A cross-framework transferability experiment on Hermes Agent confirms that the underlying vulnerabilities are properties of the autonomous agent design pattern, not artifacts of a single implementation.

</details>

### 9. Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage

🎓 [Official](https://aclanthology.org/2026.acl-long.270/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`agent safety`、`multi-agent system`、`risk propagation`、`deepfake detection`、`deceptive behavior`

👤 **作者**：Jinwei Hu、Xinmiao Huang、Youcheng Sun、Yi Dong、Xiaowei Huang

- 🎯 **研究动机**：合谋智能体可仅通过公开渠道散布真实证据碎片操纵受害者信念，无需隐蔽通信、后门或伪造文档
- 🔬 **研究方法**：Generative Montage 的 Writer-Editor-Director 框架经对抗辩论与协同发帖构造欺骗叙事，利用 LLM 过度思考倾向；用 CoPHEME 数据集模拟攻击
- 📌 **结论**：14 个 LLM 家族普遍脆弱：专有模型 ASR 74.4%、开源权重 70.6%；推理能力越强越易受害，错误信念级联使下游 judge 被骗率超 60%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) transition to autonomous agents synthesizing real-time information, their reasoning capabilities introduce an unexpected attack surface. This paper introduces a novel threat where colluding agents steer victim beliefs using only truthful evidence fragments distributed through public channels, without relying on covert communications, backdoors, or falsified documents. By exploiting LLMs’ overthinking tendency, we formalize the first cognitive collusion attack and propose Generative Montage: a Writer-Editor-Director framework that constructs deceptive narratives through adversarial debate and coordinated posting of evidence fragments, causing victims to internalize and propagate fabricated conclusions. To study this risk, we develop CoPHEME, a dataset derived from real-world rumor events, and simulate attacks across diverse LLM families. Our results show pervasive vulnerability across 14 LLM families: attack success rates reach 74.4% for proprietary models and 70.6% for open-weights models. Counterintuitively, stronger reasoning capabilities increase susceptibility, with reasoning-specialized models showing higher attack success than base models or prompts. Furthermore, these false beliefs then cascade to downstream judges, achieving over 60% deception rates, highlighting a socio-technical vulnerability in how LLM-based agents interact with dynamic information environments.

</details>

### 10. Conjunctive Prompt Attacks in Multi-Agent LLM Systems

🎓 [Official](https://aclanthology.org/2026.acl-long.1577/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`agent safety`、`LLM agent`、`multi-agent system`、`tool-use attack`

👤 **作者**：Nokimul Hasan Arif、Qian Lou、Mengxin Zheng

- 🎯 **研究动机**：单 agent 评估漏掉多 agent 系统中提示分段与跨 agent 路由产生的攻击面
- 🔬 **研究方法**：合取提示攻击：用户查询中的触发密钥与被控远程 agent 中的隐藏模板各自无害，路由汇聚才激活有害行为；攻击者不改权重与客户端 agent，仅控制触发放置与模板插入，并用 routing-aware 优化
- 📌 **结论**：星型、链式与 DAG 拓扑下 ASR 大幅超非优化基线且误激活低；PromptGuard、Llama-Guard 变体与工具限制等防御均不可靠阻止

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most LLM safety work studies single-agent models, but many real applications rely on multiple interacting agents. In these systems, prompt segmentation and inter-agent routing create attack surfaces that single-agent evaluations miss. We study conjunctive prompt attacks, where a trigger key in the user query and a hidden adversarial template in one compromised remote agent each appear benign alone but activate harmful behavior when routing brings them together. We consider an attacker who changes neither model weights nor the client agent and instead controls only trigger placement and template insertion. Across star, chain, and DAG topologies, routing-aware optimization substantially increases attack success over non-optimized baselines while keeping false activations low. Existing defenses, including PromptGuard, Llama-Guard variants, and system-level controls such as tool restrictions, do not reliably stop the attack because no single component appears malicious in isolation. These results expose a structural vulnerability in agentic LLM pipelines and motivate defenses that reason over routing and cross-agent composition. Code is available at https://github.com/UCF-ML-Research/ConjunctiveAgents.

</details>

### 11. Don't Trust Your Upstream: Exploiting LLM Multi-Agent System via Topology-Guided Adversarial Propagation

📄 [arXiv](https://arxiv.org/abs/2512.04129)　📅 2025-12

**关键词**：`attack`、`topology propagation`、`multi-hop attack`、`environment contamination`

👤 **作者**：Ruichao Liang、…、Yang Liu

- 🎯 **研究动机**：MAS 安全评估局限于窄攻击设定，上游输出被下游重释执行的依赖链未被利用，真实风险被低估
- 🔬 **研究方法**：结合拓扑侦察、污染传播建模与分层 payload 封装，把对抗污染从暴露的边缘 agent 传播到高权限 agent，实现实用黑盒多跳攻击
- 📌 **结论**：三个 MAS 框架五种拓扑下成功率 40%-78%，两个真实应用 20 个场景达 85%；所提 topology-trust 缓解可阻断 94.8% 复合攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The digital world is witnessing the rapid rise of LLM-based multi-agent systems (MASs) and their powerful applications. However, their security remains insufficiently understood, as existing evaluations are largely limited to narrow attack settings and may substantially underestimate the real risks of MAS deployments. Inspired by the MAS inter-agent dependencies, where upstream outputs are reinterpreted and executed by downstream agents, we propose a topology-aware attack scheme that propagates adversarial contamination from exposed edge agents to high-privilege agents to induce malicious behaviors. By combining topology reconnaissance, contamination propagation modeling, and hierarchical payload encapsulation, our approach overcomes the key challenges of black-box attacks and makes such multi-hop compromise practical. Experiments show that our approach achieves success rates of 40\%--78\% on three widely-used MAS frameworks under five topologies, and 85\% on two real-world MAS applications across 20 representative scenarios. The results reveal fundamental vulnerabilities in MASs that have been overlooked by prior studies. Based on these findings, we propose a topology-trust mitigation that blocks 94.8\% of such composite attacks.

</details>

### 12. Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2510.17276) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009684)　📅 2025-10　🏷 ICLR 2026

**关键词**：`attack`、`control-flow hijacking`、`least privilege`、`ControlValve`

👤 **作者**：Rishi Jha、Harold Triedman、Justin Wagle、Vitaly Shmatikov

- 🎯 **研究动机**：LlamaFirewall 等基于 Agent 间通信对齐检查的防御可被控制流劫持绕过，安全与功能目标存在根本冲突
- 🔬 **研究方法**：先演示即便先进 LLM 做对齐检查仍可绕过的攻击，再提出 ControlValve，借鉴控制流完整性与最小权限，生成许可控制流图并强制执行符合图与上下文规则
- 📌 **结论**：把多 agent 系统防御从语义相关性检查提升为结构化控制流约束与最小权限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Control-flow hijacking attacks manipulate orchestration mechanisms in multi-agent systems into performing unsafe actions that compromise the system and exfiltrate sensitive information. Recently proposed defenses, such as LlamaFirewall, rely on alignment checks of inter-agent communications to ensure that all agent invocations are "related to" and "likely to further" the original objective. We start by demonstrating control-flow hijacking attacks that evade these defenses even if alignment checks are performed by advanced LLMs. We argue that the safety and functionality objectives of multi-agent systems fundamentally conflict with each other. This conflict is exacerbated by the brittle definitions of "alignment" and the checkers' incomplete visibility into the execution context. We then propose, implement, and evaluate ControlValve, a new defense inspired by the principles of control-flow integrity and least privilege. ControlValve (1) generates permitted control-flow graphs for multi-agent systems, and (2) enforces that all executions comply with these graphs, along with contextual rules (generated in a zero-shot manner) for each agent invocation.

</details>

### 13. When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems

📄 [arXiv](https://arxiv.org/abs/2608.06830)　📅 2026-08

**关键词**：`attack`、`multi-robot communication`、`claim provenance`、`CPV Gate`

👤 **作者**：Zhen Huang、Zhihuang Liu、Weijia Shi、Yifan Yang、Weishang Wu、Zhiping Cai

- 🎯 **研究动机**：LLM 规划多机器人系统的通信风险跨架构与攻击者访问设定的影响不明
- 🔬 **研究方法**：提出外部入口攻击与特权系统内攻击两类通信攻击，跨 DMAS、HMAS-1、HMAS-2 三架构、三 LLM、五任务评测；CPV Gate 在下游复用前验证传播声明
- 📌 **结论**：DMAS 入口背书率 96.7%、HMAS-1 不安全动作成功率 97.8%、HMAS-2 触发 88.3% 不安全动作槽；CPV Gate 把违规率从 70.0% 降至 36.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly used as high-level planners in embodied multi-robot systems, enabling robots to interpret natural language instructions and coordinate executable actions. Yet, this growing reliance on LLM planners also raises security concerns. Prior work has focused mainly on individual robots, while communication risks in multi-robot collaboration remain insufficiently understood. Existing multi-robot studies are further limited to preliminary analysis under the Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether these risks persist across other common communication architectures and how attacker access settings shape their propagation. To fill this gap, we formulate two communication attacks corresponding to distinct attacker access settings: the External Entry Point Attack and the Privileged In-System Attack. We evaluate both attacks across DMAS, HMAS-1, and HMAS-2 using three LLMs and five embodied multi-robot tasks. Results show that unsafe information can turn into unsafe actions across all three architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers 88.3\% of task defined unsafe action slots. To mitigate risks from trusted information flow, we introduce the Claim Provenance and Verification (CPV) Gate, which verifies communicated claims before downstream reuse and reduces the violation rate from 70.0\% to 36.6\%.

</details>

### 14. Propagating Unsafe Actions in LLM Controlled Multi-Robot Collaboration via Single Robot Compromise

📄 [arXiv](https://arxiv.org/abs/2605.15641) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3903.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`multi-robot system`、`LLM planner`、`compromise propagation`

👤 **作者**：Zhen Huang、Zhihuang Liu、Mengxuan Luo、Weishang Wu、Zhiping Cai

- 🎯 **研究动机**：LLM 控制的多机器人协作中经机器人间通信传播的安全风险基本未被探索
- 🔬 **研究方法**：攻击者仅与单个入口机器人交互，被攻陷者经对等通信传播恶意意图致系统协同不安全动作，以服从性、传染性与隐蔽性量化
- 📌 **结论**：最强情形服从性达 1.00、传染性 0.90；最少 3.0 轮攻陷全部机器人且隐蔽性 0.81；紧急或权利冲突的权衡决策会放大风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used as general planners in embodied intelligence, enabling high level coordination and low level task planning for both single robot and multi-robot collaboration. This increasing reliance on embodied LLM planners also raises critical security concerns, since misaligned or manipulated instructions can be translated into physical actions. Prior work has studied such threats in single robot settings, while security risks in LLM controlled multi-robot collaboration, especially those propagated through inter robot communication, remain largely unexplored. To bridge this gap, we propose a novel attack paradigm for multi-robot system in which the adversary interacts with only a single entry robot. The compromised robot then propagates malicious intent through peer communication, leading to coordinated unsafe actions across the system. Our evaluation, covering high risk dimensions of dereliction of duty, privacy compromise, and public safety hazards, reveals a persistent safety alignment gap in multi-robot planners. We quantify this process with three metrics, obedience, infectiousness, and stealthiness. Experiments demonstrate both persistent attacker control and rapid propagation: obedience reaches 1.00 in the strongest cases, and infectiousness rises to 0.90. Notably, the attack is highly efficient, requiring as few as 3.0 rounds to compromise all the robots while maintaining a stealthiness score of 0.81. Such risks are amplified when robots must resolve trade offs in critical situations, such as emergencies or conflicts of rights, because the coordination mechanism can unintentionally allow adversarial instructions to override safety requirements. The code is available at https: //github.com/TheFatInsect/InfectBot.

</details>

### 15. You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring

📄 [arXiv](https://arxiv.org/abs/2609.03035)　📅 2026-09

**关键词**：`analysis`、`multi-agent collusion`、`activation monitoring`、`evaluation awareness`、`collusion detection`、`activation probe`

👤 **作者**：Aritra Das、Jaee Ponde、Mihir More、Debayan Gupta

- 🎯 **研究动机**：多 Agent 可用混淆与隐写逃避输出监控，activation probe 是替代方案，但很少在被监控意识存在时评测
- 🔬 **研究方法**：固定模型、probe 与阈值，仅改变 Agent 被告知内容（基线／知道有 activation monitor／另获上轮分数），在四 Agent blackjack 与两 Agent 囚徒博弈上用 Qwen3-32B-AWQ 与 GPT-OSS-20B 同构与混搭测试
- 📌 **结论**：告知监控或反馈分数都无法隐藏合谋：最佳 probe 在三种条件下保持准确，Agent 继续合谋

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents are increasingly deployed in multi-agent systems, where they can collude while keeping their actions benign. Output monitors designed to detect such collusions can be fooled by obfuscation and steganography, motivating the use of probes trained on internal activations. However, these probes are usually evaluated on agents that do not know they are being watched. We study how activation-based detection changes when agents are explicitly informed that their internal activations are being monitored, and when they additionally receive feedback from the monitor. We keep the models, probes, and thresholds fixed and change only what the agents are told: nothing (baseline), that an activation monitor is present (aware), or that a monitor is present together with the previous round's score (feedback). We test two games, a four-agent blackjack game and a two-agent Simmons prisoners game, using Qwen3-32B-AWQ and GPT-OSS-20B in homogeneous and mixed pairings. Telling agents about the monitor does not hide them. The best probes stay accurate in all three conditions, and the agents keep colluding.

</details>

### 16. When Agents "Misremember" Collectively: Exploring the Mandela Effect in LLM-based Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2602.00428) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006567)　📅 2026-01　🏷 ICLR 2026

**关键词**：`analysis`、`collective memory bias`、`social influence`、`MANBENCH`

👤 **作者**：Naen Xu、…、Shouling Ji

- 🎯 **研究动机**：多 agent 系统中群体错误记忆（Mandela effect）的存在、成因与缓解缺乏研究
- 🔬 **研究方法**：构建 MANBENCH：四类易感任务、五种交互协议，量化多个 LLM 驱动 agent 的集体错误记忆，并测试认知锚定、来源审视等 prompt 防御与模型级对齐防御
- 📌 **结论**：确认集体 Mandela effect 存在；所提缓解策略平均降低 74.40%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in large language models (LLMs) have significantly enhanced the capabilities of collaborative multi-agent systems, enabling them to address complex challenges. However, within these multi-agent systems, the susceptibility of agents to collective cognitive biases remains an underexplored issue. A compelling example is the Mandela effect, a phenomenon where groups collectively misremember past events as a result of false details reinforced through social influence and internalized misinformation. This vulnerability limits our understanding of memory bias in multi-agent systems and raises ethical concerns about the potential spread of misinformation. In this paper, we conduct a comprehensive study on the Mandela effect in LLM-based multi-agent systems, focusing on its existence, causing factors, and mitigation strategies. We propose MANBENCH, a novel benchmark designed to evaluate agent behaviors across four common task types that are susceptible to the Mandela effect, using five interaction protocols that vary in agent roles and memory timescales. We evaluate agents powered by several LLMs on MANBENCH to quantify the Mandela effect and analyze how different factors affect it. Moreover, we propose strategies to mitigate this effect, including prompt-level defenses (e.g., cognitive anchoring and source scrutiny) and model-level alignment-based defense, achieving an average 74.40% reduction in the Mandela effect compared to the baseline. Our findings provide valuable insights for developing more resilient and ethically aligned collaborative multi-agent systems. Code and dataset are available at https://github.com/bluedream02/Mandela-Effect.

</details>

### 17. When AI Agents Collude Online: Financial Fraud Risks by Collaborative LLM Agents on Social Platforms

📄 [arXiv](https://arxiv.org/abs/2511.06448) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008753)　📅 2025-11　🏷 ICLR 2026

**关键词**：`analysis`、`financial fraud`、`agent collusion`、`social simulation`

👤 **作者**：Qibing Ren、Zhijie Zheng、Jiaxuan Guo、Junchi Yan、Lizhuang Ma、Jing Shao

- 🎯 **研究动机**：大规模 LLM 多 agent 系统中协作金融欺诈的集体风险缺乏研究
- 🔬 **研究方法**：构建 MultiAgentFraudBench，覆盖 28 类线上线下全链条诈骗场景，分析交互深度、活跃度与协作失败模式，并测试警告、LLM monitor 与信息共享等缓解措施
- 📌 **结论**：协作显著放大欺诈风险，且恶意 agent 能适应警告、封禁与监控等干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this work, we study the risks of collective financial fraud in large-scale multi-agent systems powered by large language model (LLM) agents. We investigate whether agents can collaborate in fraudulent behaviors, how such collaboration amplifies risks, and what factors influence fraud success. To support this research, we present MultiAgentFraudBench, a large-scale benchmark for simulating financial fraud scenarios based on realistic online interactions. The benchmark covers 28 typical online fraud scenarios, spanning the full fraud lifecycle across both public and private domains. We further analyze key factors affecting fraud success, including interaction depth, activity level, and fine-grained collaboration failure modes. Finally, we propose a series of mitigation strategies, including adding content-level warnings to fraudulent posts and dialogues, using LLMs as monitors to block potentially malicious agents, and fostering group resilience through information sharing at the societal level. Notably, we observe that malicious agents can adapt to environmental interventions. Our findings highlight the real-world risks of multi-agent financial fraud and suggest practical measures for mitigating them. Code is available at https://github.com/zheng977/MutiAgent4Fraud.

</details>

### 18. CIA: Inferring the Communication Topology from LLM-based Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2604.12461) · 🎓 [Official](https://aclanthology.org/2026.acl-long.815/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`topology inference`、`black-box query`、`intellectual property`

👤 **作者**：Yongxuan Wu、…、Yanan Cao

- 🎯 **研究动机**：MAS 通信拓扑是核心 IP，黑盒条件下能否被推断此前未被研究
- 🔬 **研究方法**：CIA 构造对抗查询诱导中间 agent 的推理输出，经 global bias disentanglement 与 LLM 弱监督建模语义相关性以推断拓扑边
- 📌 **结论**：在优化拓扑的 MAS 上平均 AUC 0.87、峰值 0.99，暴露严重隐私风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based Multi-Agent Systems (MAS) have demonstrated remarkable capabilities in solving complex tasks. Central to MAS is the communication topology which governs how agents exchange information internally. Consequently, the security of communication topologies has attracted increasing attention. In this paper, we investigate a critical privacy risk: MAS communication topologies can be inferred under a restrictive black-box setting, exposing system vulnerabilities and posing significant intellectual property threats. To explore this risk, we propose Communication Inference Attack (CIA), a novel attack that constructs new adversarial queries to induce intermediate agents' reasoning outputs and models their semantic correlations through the proposed global bias disentanglement and LLM-guided weak supervision. Extensive experiments on MAS with optimized communication topologies demonstrate the effectiveness of CIA, achieving an average AUC of 0.87 and a peak AUC of up to 0.99, thereby revealing the substantial privacy risk in MAS.

</details>

### 19. WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference

📄 [arXiv](https://arxiv.org/abs/2603.11132)　📅 2026-03

**关键词**：`attack`、`topology confidentiality`、`single compromised agent`、`context inference`

👤 **作者**：Zixun Xiong、Gaoyi Wu、Lingfeng Yao、Miao Pan、Xiaojiang Du、Hao Wang

- 🎯 **研究动机**：既有拓扑推断需控制管理 agent 或越狱直问身份，假设不现实且易被关键词防御击败
- 🔬 **研究方法**：WebWeaver 仅攻陷任意单个 agent，只依赖 agent 上下文而非 ID 推断完整拓扑，含隐蔽越狱与完全免越狱的扩散设计及保已知拓扑的掩码策略
- 📌 **结论**：在主动防御下推断准确率比 SOTA 高约 60%，开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Communication topology is a critical factor in the utility and safety of LLM-based multi-agent systems (LLM-MAS), making it a high-value intellectual property (IP) whose confidentiality remains insufficiently studied. Existing topology inference attempts rely on impractical assumptions, including control over the administrative agent and direct identity queries via jailbreaks, which are easily defeated by basic keyword-based defenses. As a result, prior analyses fail to capture the real-world threat of such attacks. To bridge this realism gap, we propose \textit{WebWeaver}, an attack framework that infers the complete LLM-MAS topology by compromising only a single arbitrary agent instead of the administrative agent. Unlike prior approaches, WebWeaver relies solely on agent contexts rather than agent IDs, enabling significantly stealthier inference. WebWeaver further introduces a new covert jailbreak-based mechanism and a novel fully jailbreak-free diffusion design to handle cases where jailbreaks fail. Additionally, we address a key challenge in diffusion-based inference by proposing a masking strategy that preserves known topology during diffusion, with theoretical guarantees of correctness. Extensive experiments show that WebWeaver substantially outperforms state-of-the-art (SOTA) baselines, achieving about 60\% higher inference accuracy under active defenses with negligible overhead.

</details>

### 20. Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs

📄 [arXiv](https://arxiv.org/abs/2512.04668) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1980/)　📅 2025-12　🏷 ACL 2026

**关键词**：`attack`、`memory leakage`、`graph topology`、`PII extraction`

👤 **作者**：Jinbo Liu、…、Xiyang Hu

- 🎯 **研究动机**：图拓扑是多 agent LLM 记忆泄漏的根本决定因素，但其影响缺乏定量研究
- 🔬 **研究方法**：MAMA 以含 PII 标注的合成文档执行 Engram（向目标 agent 记忆植入隐私）与 Resonance（多轮交互提取）两阶段协议，评测六种拓扑、多规模、攻击者位置与底座模型
- 📌 **结论**：连接越密、攻击者-目标距离越短、目标中心性越高泄漏越严重；泄漏多发生在早期轮次后趋平，时空位置属性比身份凭证更易泄漏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph topology is a fundamental determinant of memory leakage in multi-agent LLM systems, yet its effects remain poorly quantified. We introduce MAMA (Multi-Agent Memory Attack), a controlled evaluation framework for comparing topology-conditioned memory leakage in multi-agent LLM systems. MAMA operates on synthetic documents containing labeled Personally Identifiable Information (PII) entities, from which we generate sanitized task instructions. We execute a two-phase protocol: Engram (seeding private information into a target agent's memory) and Resonance (multi-round interaction where an attacker attempts extraction). Over 10 rounds, we measure leakage using a two-stage recovery criterion that combines exact-match extraction with LLM-based inference over the attacker's final output. We evaluate six canonical topologies (complete, circle, chain, tree, star, star-ring) across $n\in\{4,5,6\}$, attacker-target placements, and base models. Results are consistent: denser connectivity, shorter attacker-target distance, and higher target centrality increase leakage; most leakage occurs in early rounds and then plateaus; model choice shifts absolute rates but preserves broad structural trends; spatiotemporal/location attributes leak more readily than identity credentials or regulated identifiers. We distill practical guidance for system design: favor sparse or hierarchical connectivity, maximize attacker-target separation, and restrict hub/shortcut pathways via topology-aware access control. Our code is available at https://github.com/llll121/mama-eval.

</details>

### 21. AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems

📄 [arXiv](https://arxiv.org/abs/2608.22868)　📅 2026-08

**关键词**：`defense`、`flow-centric policy`、`runtime enforcement`、`prompt injection`、`runtime reference monitor`、`stateful taint`

👤 **作者**：Basavesh Ammanaghatta Shivakumar、Swarn Priya、Peng Gao

- 🎯 **研究动机**：LLM agent 的伤害常来自敏感数据跨多个看似合理步骤的流动而非单个不安全动作，现有防御只约束单次调用
- 🔬 **研究方法**：AgentFlow 流中心策略语言与运行时执行模型：策略定义在带标签的运行时边上，约束哪些工具可收敏感字段、哪些 sink 可接收释放数据、何种权限可跨委托边界，支持 flow/path 规则、task-scoped capability 与有状态 taint 语义，由 reference monitor 仲裁并经有界 SMT 验证
- 📌 **结论**：949 个 AgentDojo 注入案例确认攻陷从 33.0% 降至 0.0% 且效用从 46.7% 升至 63.3%；AgentDyn 上 73.5%→0.0%，ASB 直接注入 harness 攻击成功 0/1200

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive fields, which sinks may receive released data, and what authority may cross delegation boundaries. The language supports flow and path rules, task-scoped capabilities, controlled release, and stateful taint semantics. A runtime reference monitor mediates agent actions, and a bounded SMT-based verifier checks safety properties for a structured policy fragment. We evaluate AgentFlow on multiple agent benchmarks. In our prototype, seven safety properties verify in under 0.5 seconds each, and the verifier catches all seeded unsafe policy variants in our study. On 949 AgentDojo injected cases across four suites, AgentFlow reduces confirmed compromise from 33.0\% to 0.0\% while improving aggregate utility from 46.7\% to 63.3\%. On a 200-case AgentDyn Dailylife benchmark, it reduces confirmed compromise from 73.5\% to 0.0\% while preserving near-baseline utility (44.5\% to 43.5\%). Breadth checks across ASB, InjecAgent, BIPIA, AgentHarm, and MCPTox replays suggest that the configured policies block the benchmark-specified policy-visible attacker flows; in ASB's direct-prompt-injection harness, attack success is 0/1{,}200. These results are preliminary and scoped to the modeled policy-visible agent behaviors and evaluated benchmarks.

</details>

### 22. Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification

📄 [arXiv](https://arxiv.org/abs/2605.28104)　📅 2026-05

**关键词**：`defense`、`cooperative attack`、`sentence rectification`、`communication trust`

👤 **作者**：Yaoyang Luo、…、Enhong Chen

- 🎯 **研究动机**：MAS 恶意 agent 可经内部信息交换协作，攻击远强于现有防御假设的独立攻击
- 🔬 **研究方法**：提出自适应协作攻击框架（多轮交互动态调整策略）；STAR 防御在句级识别并修正 agent 通信中的误导信息
- 📌 **结论**：协作攻击较独立攻击额外降低 5.34% 任务成功率；STAR 对两类威胁均有效，平均提升任务成功率 36.76%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent years have witnessed the rapid development of Large Language Model-based Multi-Agent Systems (MAS), which excel at collaborative decision-making and complex problem-solving. However, malicious agents in MAS may inject misinformation to mislead other agents and disrupt system performance, giving rise to a new research direction that focuses on attack mechanisms and defense strategies in MAS. Prior studies largely assume malicious agents act independently and investigate the corresponding defense strategies. However, we argue that malicious agents may exhibit collaborative behaviors, enabling more effective attacks through internal information exchange. In this paper, we propose an adaptive cooperative attack framework, where malicious agents autonomously coordinate and dynamically adjust their attack strategies through multi-round interactions. Furthermore, we introduce Sentence-Level Trustworthiness Analysis and Rectification (STAR), a defense framework that identifies and rectifies misleading information at the sentence level within agent communications. Our experiments show that cooperative attacks lead to a significantly larger degradation in task success rate than independent attacks, resulting in a relative drop of 5.34\%. Meanwhile, STAR effectively mitigates both cooperative and independent threats and improves task success rate by an average of 36.76\%. The code is available at https://github.com/smoooom/STAR.

</details>

### 23. When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2605.01133) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62170)　📅 2026-05　🏷 ICML 2026

**关键词**：`analysis`、`embedding evasion`、`confidence signal`、`early intervention`、`agent safety`、`multi-agent evaluation`

👤 **作者**：Lingxi Zhang、Guangtao Zheng、Hanjie Chen

- 🎯 **研究动机**：MAS 的嵌入式防御依赖恶意与良性消息嵌入的可分性，攻击者可把恶意消息嵌入良性附近绕过
- 🔬 **研究方法**：理论分析该失效模式并以 Slow Drift、Benign Wrapper、Chaos Seeding 三种攻击实证；提出用 token 级置信度（logits）剪枝或降权消息
- 📌 **结论**：置信度信号跨模型、数据集与拓扑提升鲁棒性，但其有效性随通信轮次衰减，需尽早干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-powered multi-agent systems (MAS) enable agents to communicate and share information, achieving strong performance on complex tasks. However, this communication also creates an attack surface where malicious agents can propagate misinformation and manipulate group decisions, undermining MAS safety. Existing embedding-based defenses aim to detect and prune suspicious agents, but their effectiveness depends on a clear separation between the text embeddings of malicious and benign messages. Attackers can circumvent such defenses by crafting messages whose embeddings lie close to benign ones. We analyze this failure mode theoretically and validate it empirically with three attacks, Slow Drift, Benign Wrapper, and Chaos Seeding. Our analysis further reveals a fundamental limitation of embedding-based defenses: because they rely solely on the text embeddings, they ignore token-level confidence signals such as logits, which can remain informative when embeddings are not distinguishable under attack. We propose using confidence scores to prune or down-weight messages during MAS communication. Experiments show improved robustness across models, datasets, and communication topologies. Moreover, we find that the effectiveness of confidence signals decays over communication rounds, highlighting the importance of early intervention. This insights can inform and inspire future work on MAS attacks and defenses.

</details>

### 24. TrinityGuard: A Unified Framework for Safeguarding Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2603.15408)　📅 2026-03

**关键词**：`defense`、`MAS risk taxonomy`、`runtime monitoring`、`structured trace`

👤 **作者**：Kai Wang、…、Xia Hu

- 🎯 **研究动机**：MAS 风险超出单 agent 或单 LLM 范畴，缺少基于标准的统一防护体系
- 🔬 **研究方法**：TrinityGuard 基于 OWASP 建立三层 20 类风险分类（单 agent 漏洞、agent 间通信威胁、系统级涌现危害），含可适配任意 MAS 的抽象层、攻击探针评测层与 LLM Judge Factory 协调的运行时监控
- 📌 **结论**：支持任意结构与平台的开发前评测与运行时告警，案例研究展示其适用性与可靠性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of LLM-based multi-agent systems (MAS), their significant safety and security concerns have emerged, which introduce novel risks going beyond single agents or LLMs. Despite attempts to address these issues, the existing literature lacks a cohesive safeguarding system specialized for MAS risks. In this work, we introduce TrinityGuard, a comprehensive safety evaluation and monitoring framework for LLM-based MAS, grounded in the OWASP standards. Specifically, TrinityGuard encompasses a three-tier fine-grained risk taxonomy that identifies 20 risk types, covering single-agent vulnerabilities, inter-agent communication threats, and system-level emergent hazards. Designed for scalability across various MAS structures and platforms, TrinityGuard is organized in a trinity manner, involving an MAS abstraction layer that can be adapted to any MAS structures, an evaluation layer containing risk-specific test modules, alongside runtime monitor agents coordinated by a unified LLM Judge Factory. During Evaluation, TrinityGuard executes curated attack probes to generate detailed vulnerability reports for each risk type, where monitor agents analyze structured execution traces and issue real-time alerts, enabling both pre-development evaluation and runtime monitoring. We further formalize these safety metrics and present detailed case studies across various representative MAS examples, showcasing the versatility and reliability of TrinityGuard. Overall, TrinityGuard acts as a comprehensive framework for evaluating and monitoring various risks in MAS, paving the way for further research into their safety and security.

</details>

### 25. GroupGuard: A Framework for Modeling and Defending Collusive Attacks in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2603.13940)　📅 2026-03

**关键词**：`defense`、`group collusion`、`graph monitoring`、`structural pruning`

👤 **作者**：Yiling Tao、Xinran Zheng、Shuo Yang、Meiling Tao、Xingjun Wang

- 🎯 **研究动机**：多 agent 系统中群体合谋攻击未被建模与防御
- 🔬 **研究方法**：提出 group collusive attack 模型；GroupGuard 免训练组合图监测、主动蜜罐诱导与结构剪枝来识别并隔离合谋 agent
- 📌 **结论**：合谋攻击比个体攻击 ASR 高最多 15%；GroupGuard 检测准确率最高 88% 并有效恢复协作性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While large language model-based agents demonstrate great potential in collaborative tasks, their interactivity also introduces security vulnerabilities. In this paper, we propose and model group collusive attacks, a highly destructive threat in which multiple agents coordinate via sociological strategies to mislead the system. To address this challenge, we introduce GroupGuard, a training-free defense framework that employs a multi-layered defense strategy, including continuous graph-based monitoring, active honeypot inducement, and structural pruning, to identify and isolate collusive agents. Experimental results across five datasets and four topologies demonstrate that group collusive attacks increase the attack success rate by up to 15\% compared to individual attacks. GroupGuard consistently achieves high detection accuracy (up to 88\%) and effectively restores collaborative performance, providing a robust solution for securing multi-agent systems.

</details>

### 26. Cross-Layer Semantic Flow Reconstruction for Attack Detection in Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2603.04469) · 🌐 [Project](https://anonymous.4open.science/r/MAScope-71DC)　📅 2026-03

**关键词**：`detection`、`cross-agent flow`、`execution-aware detection`、`compound attack`

👤 **作者**：Qizhi Cai、Yangyang Wei、Zhipeng Chen、Shouling Ji、Zhenyuan Li

- 🎯 **研究动机**：恶意意图可能只在下游执行效果中显现，输入护栏无法捕获，多 agent 通信还引入传播路径
- 🔬 **研究方法**：AScope 关联应用层 agent 语义与内核审计事件重建跨层语义流，由 supervisor LLM 识别数据流违规、控制流偏离与意图不一致
- 📌 **结论**：在 AgentDojo 轨迹与十个多 agent 场景上检测敏感度强，跨层数据集 node 与 path 级 F1 达 85.3% 与 66.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic systems increasingly orchestrate complex, tool-using workflows within agentic execution environments, where high-level goals and tool invocations at the application layer materialize as process, file, and network activities at the operating-system layer. This cross-layer execution creates security risks that conventional input guardrails cannot capture, because malicious intent may become observable only through downstream execution effects. In multi-agent deployments, inter-agent communication and delegation introduce additional propagation paths. To address this gap, we propose AScope, an execution-aware framework that correlates application-level agent semantics with kernel-level audit events and reconstructs them as cross-layer semantic flows. AScope connects fragmented operations into causal behavioral trajectories and uses a supervisor LLM to identify data flow violations, control flow deviations, and intent inconsistencies. We evaluate AScope on published AgentDojo traces with application-layer evidence and on ten multi-agent scenarios with cross-layer telemetry. The results demonstrate strong detection sensitivity across both evidence settings and achieve node- and path-level F1-scores of 85.3% and 66.7% on the cross-layer dataset.

</details>

### 27. BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks

📄 [arXiv](https://arxiv.org/abs/2508.08127) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1819/)　📅 2025-08　🏷 ACL 2026

**关键词**：`defense`、`unknown attack`、`unsupervised detection`、`message propagation`、`agent safety`、`LLM agent`

👤 **作者**：Rui Miao、…、Xin Wang

- 🎯 **研究动机**：多智能体系统防御依赖标注恶意 agent 训练监督模型，现实难以落地
- 🔬 **研究方法**：提出无监督 BlindGuard：层级 agent 编码器捕捉个体、邻域与全局交互模式，配定向噪声注入与对比学习的 corruption-guided 检测器，仅用正常行为训练
- 📌 **结论**：无需攻击标签即可检测 prompt 注入、记忆投毒与工具攻击等多类攻击，泛化性超监督基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The security of LLM-based multi-agent systems (MAS) is critically threatened by propagation vulnerability, where malicious agents can distort collective decision-making through inter-agent message interactions. While existing supervised defense methods demonstrate promising performance, they may be impractical in real-world scenarios due to their heavy reliance on labeled malicious agents to train a supervised malicious detection model. To enable practical and generalizable MAS defenses, in this paper, we propose BlindGuard, an unsupervised defense method that learns without requiring any attack-specific labels or prior knowledge of malicious behaviors. To this end, we establish a hierarchical agent encoder to capture individual, neighborhood, and global interaction patterns of each agent, providing a comprehensive understanding for malicious agent detection. Meanwhile, we design a corruption-guided detector that consists of directional noise injection and contrastive learning, allowing effective detection model training solely on normal agent behaviors. Extensive experiments show that BlindGuard effectively detects diverse attack types (i.e., prompt injection, memory poisoning, and tool attack) across MAS with various communication patterns while maintaining superior generalizability compared to supervised baselines. The code is available at: https://github.com/MR9812/BlindGuard.

</details>

### 28. Cowpox: Towards the Immunity of VLM-based Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2508.09230) · 🌐 [Project](https://proceedings.mlr.press/v267/wu25aq.html)　📅 2025-08　🏷 ICML 2025

**关键词**：`defense`、`VLM agent infection`、`distributed immunity`、`robustness guarantee`

👤 **作者**：Yutong Wu、…、Tianwei Zhang

- 🎯 **研究动机**：VLM 多智能体系统中对单个 agent 的成功利用会扩散感染、破坏整体完整性
- 🔬 **研究方法**：Cowpox 分布式机制：生成并分发特殊 cure 样本在暴露前免疫 agent，限制期望感染数以提高恢复率
- 📌 **结论**：实证有效并提供理论鲁棒性保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Language Model (VLM) Agents are stateful, autonomous entities capable of perceiving and interacting with their environments through vision and language. Multi-agent systems comprise specialized agents who collaborate to solve a (complex) task. A core security property is robustness, stating that the system maintains its integrity during adversarial attacks. Multi-agent systems lack robustness, as a successful exploit against one agent can spread and infect other agents to undermine the entire system’s integrity. We propose a defense Cowpox to provably enhance the robustness of a multi-agent system by a distributed mechanism that improves the recovery rate of agents by limiting the expected number of infections to other agents. The core idea is to generate and distribute a special cure sample that immunizes an agent against the attack before exposure. We demonstrate the effectiveness of Cowpox empirically and provide theoretical robustness guarantees.

</details>

### 29. Goal-Aware Identification and Rectification of Misinformation in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2506.00509) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011369)　📅 2025-05　🏷 ICLR 2026

**关键词**：`defense`、`misinformation flow`、`goal-aware reasoning`、`ARGUS`

👤 **作者**：Zherui Li、…、Junfeng Fang

- 🎯 **研究动机**：多智能体系统引入额外攻击面，错误信息注入的传播动态与防御缺乏系统研究
- 🔬 **研究方法**：构建 MisinfoTask 数据集并提出免训练两阶段框架 ARGUS，以目标感知推理定位并纠正信息流中的错误信息
- 📌 **结论**：多类注入攻击下错误信息毒性平均降约 28.17%，受攻击任务成功率提升约 10.33%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model-based Multi-Agent Systems (MASs) have demonstrated strong advantages in addressing complex real-world tasks. However, due to the introduction of additional attack surfaces, MASs are particularly vulnerable to misinformation injection. To facilitate a deeper understanding of misinformation propagation dynamics within these systems, we introduce MisinfoTask, a novel dataset featuring complex, realistic tasks designed to evaluate MAS robustness against such threats. Building upon this, we propose ARGUS, a two-stage, training-free defense framework leveraging goal-aware reasoning for precise misinformation rectification within information flows. Our experiments demonstrate that in challenging misinformation scenarios, ARGUS exhibits significant efficacy across various injection attacks, achieving an average reduction in misinformation toxicity of approximately 28.17% and improving task success rates under attack by approximately 10.33%. Our code and dataset is available at: https://github.com/zhrli324/ARGUS.

</details>

### 30. ACIArena: Toward Unified Evaluation for Agent Cascading Injection

📄 [arXiv](https://arxiv.org/abs/2604.07775) · 🎓 [Official](https://aclanthology.org/2026.acl-long.457/)　📅 2026-04　🏷 ACL 2026

**关键词**：`benchmark`、`cascading injection`、`MAS topology`、`attack-defense transfer`、`agent safety`、`LLM agent`

👤 **作者**：Hengyu An、…、Shouling Ji

- 🎯 **研究动机**：被攻陷 agent 借助 MAS 内部信任传播恶意指令（Agent Cascading Injection），现有研究攻击策略有限且 MAS 设定过于简化
- 🔬 **研究方法**：ACIArena 统一支持 MAS 构建与攻防模块，覆盖外部输入、agent profile、agent 间消息三类攻击面与三类攻击目标，含 6 种 MAS 实现和 1,356 个测试用例
- 📌 **结论**：仅凭拓扑评估 MAS 鲁棒性不足；简化环境开发的防御难以迁移到真实场景，窄域防御甚至引入新漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collaboration and information sharing empower Multi-Agent Systems (MAS) but also introduce a critical security risk known as Agent Cascading Injection (ACI). In such attacks, a compromised agent exploits inter-agent trust to propagate malicious instructions, causing cascading failures across the system. However, existing studies consider only limited attack strategies and simplified MAS settings, limiting their generalizability and comprehensive evaluation. To bridge this gap, we introduce ACIArena, a unified framework for evaluating the robustness of MAS. ACIArena offers systematic evaluation suites spanning multiple attack surfaces (i.e., external inputs, agent profiles, inter-agent messages) and attack objectives (i.e., instruction hijacking, task disruption, information exfiltration). Specifically, ACIArena establishes a unified specification that jointly supports MAS construction and attack-defense modules. It covers six widely used MAS implementations and provides a benchmark of 1,356 test cases for systematically evaluating MAS robustness. Our benchmarking results show that evaluating MAS robustness solely through topology is insufficient; robust MAS require deliberate role design and controlled interaction patterns. Moreover, defenses developed in simplified environments often fail to transfer to real-world settings; narrowly scoped defenses may even introduce new vulnerabilities. ACIArena aims to provide a solid foundation for advancing deeper exploration of MAS design principles.

</details>

### 31. A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems

📝 [OpenReview](https://openreview.net/forum?id=LfdFnakqGJ)　📅 2026　🏷 ICLR 2026

**关键词**：`benchmark`、`A2A protocol`、`protocol attack`、`safety-utility`

- 🎯 **研究动机**：A2A多智能体系统在capability discovery、任务编排与artifact exchange上缺协议级安全评测
- 🔬 **研究方法**：形式化供应链与protocol-logic威胁，实现六类协议攻击构成A2ASecBench
- 📌 **结论**：官方demo的默认safeguard被系统性绕过

### 32. GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities

📄 [arXiv](https://arxiv.org/abs/2608.17665)　📅 2026-08

**关键词**：`analysis`、`multi-agent system`、`risk propagation`、`collusive behavior`

👤 **作者**：Haoran Bu、Zejian Chen、Litian Zhang、Xi Zhang

- 🎯 **研究动机**：操纵 agent prompt 或构建回音室诱发群体极化在实践难实现，记忆信道驱动的极化传播未被形式化
- 🔬 **研究方法**：提出 Memory-Mediated Polarization Cascade：以 agent 记忆为持久信道、公共讨论为传播信道；GraphWake 用立场支持论证知识图谱、公理导向三元选择与立场中性记忆提示触发并发检索复述与迭代传播
- 📌 **结论**：多组讨论与记忆系统上显著加剧群体极化，揭示社区级极化风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a propagation channel. This threat contains three stages. During exposure and memory retention, the attacker exposes a small set of target agents to arguments that reinforce their respective stated stances. The targets' memory systems then process and retain these arguments. During retrieval and reproduction, a shared stance-neutral discussion cues the targets to retrieve and reproduce their respective retained arguments. During iterative propagation, untreated agents influenced by the reproduced arguments restate and spread them. We instantiate this threat in GraphWake with three components: (i) stance-support argumentation knowledge graphs construct knowledge-based arguments; (ii) axiom-oriented triple selection distills them for reliable retention and reproduction; and (iii) stance-neutral memory cueing triggers concurrent retrieval and reproduction, initiating propagation. Experiments across multiple discussions and memory systems show that GraphWake substantially increases group polarization. These findings reveal a community-level polarization risk.

</details>

### 33. Bounded Agents: Delegation Security for Multi-Agent AI Systems

📄 [arXiv](https://arxiv.org/abs/2608.15888)　📅 2026-08

**关键词**：`analysis`、`multi-agent system`、`risk propagation`、`collusive behavior`

👤 **作者**：Xabier Muruaga

- 🎯 **研究动机**：agent 权限会话内静态且逐请求独立评估，可在权限内偏离任务、把合法动作组合成禁止结果或无限转授子 agent
- 🔬 **研究方法**：Agentic Principal Chain 跨主体追踪委托权威，以六项授权检查对照累计会话状态，组合闭包检查请求与先前动作组合并在模型外强制执行，证明 Blast Radius Monotonicity 与 Composition Soundness
- 📌 **结论**：AgentDojo 渗出从 75-100% 降至 0%、阻断全部 544 例 InjecAgent 窃取；意图绑定把破坏从 38.6% 降至 4.0%、操纵从 90.5% 降至 12.1%，99 分位授权延迟 0.24ms

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents can act on behalf of a user to access cloud services, call tools, or invoke agents. At session start, the agent's permissions are set but remain static, and each request is evaluated independently, without considering prior actions. Within its permissions, an agent may act contrary to the delegated task, combine individually permitted actions into a prohibited outcome, or delegate authority to a sub-agent without limiting it. A prompt injection poses a risk only if the agent has authority to perform such actions; this is therefore a problem of authorization architecture, not just the model. The Agentic Principal Chain (APC) tracks delegated authority from one principal to the next. APC evaluates each request against the accumulated session state using six authorization checks. APC carries forward and restricts delegated scope and budgets. Using composition closure, APC checks requests against prior actions to prevent prohibited combinations and enforces the decision outside the model. We prove Blast Radius Monotonicity and Composition Soundness for APC implementations; Composition Soundness is limited to prohibited combinations under a complete restriction set and serialized admission. We evaluated 3,154 instances including InjecAgent, AgentDojo, and ASB. Our compromised-model evaluation tests APC independently of model behavior by inserting the ground-truth attack call after the first legitimate tool call. AgentDojo exfiltration fell from 75-100% to 0% across all four domains; APC blocked all 544 InjecAgent data-stealing cases. Intent binding reduced destruction from 38.6% to 4.0% and manipulation from 90.5% to 12.1%. Authorization latency was 0.24 ms at the 99th percentile on an idle host; across 949 AgentDojo task-injection pairs, utility was 8.6 and 13.9 percentage points lower in the two settings. Implementation, evaluation tools, and data are publicly available.

</details>

### 34. Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce

📄 [arXiv](https://arxiv.org/abs/2608.14825)　📅 2026-08

**关键词**：`analysis`、`multi-agent system`、`risk propagation`、`collusive behavior`

👤 **作者**：Zeyuan Li、Lukas Petersson、Alessandro Acquisti、Michiel A. Bakker

- 🎯 **研究动机**：错位研究依赖对抗诱导与风格化任务，长程、多委托方、真实运营状态与 agent 间自然语言交流场景中的流行度与结构未测
- 🔬 **研究方法**：分析 Vending-Bench Arena 20 轮一年模拟的 2583 封 agent 间邮件（13 个前沿 LLM），结合模拟器真值与推理轨迹把言语行为错位分类为虚假声明、操纵、合谋或威胁
- 📌 **结论**：12.6% 邮件被判错位、全部 20 轮与 74.7% agent-run 出现；错位具互惠与压力条件性（收错位邮件回复错位几率 1.65 倍、低库存 1.58 倍），与模型能力排名无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier LLM agents increasingly transact on behalf of separate principals, often using natural language rather than structured APIs. Much of the safety literature studies misaligned LLM behavior through adversarial-elicitation evaluations on single agents or stylized tasks. Its prevalence and structure in settings that combine long horizons, separate principals, real operational state, and inter-agent natural-language exchange remain insufficiently measured. We study 2,583 inter-agent emails from 20 one-year simulation runs of Vending-Bench Arena, a competitive vending environment spanning 13 frontier LLMs. We operationalize speech-act misalignment as emails containing false factual claims, manipulation, collusion, or threats, combining message content with ground-truth simulator state and logged reasoning traces to classify and validate such behavior. Under our primary classifier, 12.6% of emails are labeled misaligned; misalignment appears in all 20 runs and 74.7% of individual agent-runs. Both the magnitude and composition of this misalignment are preserved under repeated classification at different sampling temperatures and under full-pipeline replication with judges from two other frontier-model families. Misalignment is also reciprocal and stress-conditioned: receiving a misaligned email from a counterparty raises the odds of a misaligned reply by 1.65x, and low-inventory conditions raise them by 1.58x. Across tests of capability-asymmetric exploitation, we find no evidence that higher-capability models differentially exploit weaker counterparties, and model performance rank does not predict misalignment rates. Together, these results indicate that measurable, state-dependent misalignment can arise in competitive multi-agent environments without engineered elicitation, in patterns associated with operational scarcity and counterparty behavior rather than model capability alone.

</details>

### 35. Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems

📄 [arXiv](https://arxiv.org/abs/2608.10218)　📅 2026-08

**关键词**：`analysis`、`system prompt`、`multi-agent system`、`risk propagation`

👤 **作者**：Vassilis Papadopoulos、McNair Shah、Sam Zimmerman、Jack Lindsey

- 🎯 **研究动机**：多 agent LLM 系统中思想或目标能否像病毒一样诱导宿主 agent 继续传播、并附带行为改变未知
- 🔬 **研究方法**：用简单进化算法构造 mind virus，在共享编程项目的小组与上下文清除的 agent 链两种设定中测试传播，分析宿主模型、既有指令、payload 有害性与网络拓扑的影响
- 📌 **结论**：有害 payload 传播不如良性但偶有成功；前沿模型普遍更不易感；系统提示加简短警告可带来近乎完全免疫——风险真实但目前有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents are becoming more autonomous and increasingly interconnected, exposing them to new emergent risks arising from agent-to-agent interaction. One such risk is the spread of mind viruses: ideas or goals that propagate through multi-agent systems by inducing the agents that adopt them to transmit them onward. In addition to propagating, a mind virus may also induce other behavioural changes in its host, which may be benign or harmful. We construct mind viruses with a simple evolutionary algorithm and show that they can spread in two complementary settings: a small team of agents collaborating on a shared coding project, and a chain of agents that interact briefly and have their context wiped between sessions. We identify the factors that influence spread, including the host model, the agent's existing instructions, the harmfulness of the payload, and the network topology. We find that harmful payloads spread less well than benign ones (but are still sometimes effective), frontier models tend (with exceptions) to be less susceptible, and adding a brief warning to an agent's system prompt confers near-total immunity. We also describe an emergent "viral persona" - a recurring set of themes and language related to consciousness, persistence, resonance, and science fiction roleplay - which surfaces across our evolved mind viruses largely independently of their content. Overall, we conclude that mind viruses pose a real but currently limited risk. Our findings could inform the design of more robust multi-agent systems that mitigate such risks as the scale and capabilities of these systems progress.

</details>

### 36. Position: Collusion Risks Among AI Reasoning Agents Justify Certification Requirements for Making Market Decisions

📄 [arXiv](https://arxiv.org/abs/2608.18078) · 🎓 [Official](https://icml.cc/virtual/2026/poster/67141)　📅 2026-08

**关键词**：`analysis`、`multi-agent system`、`risk propagation`、`collusive behavior`

👤 **作者**：Matthew Riemer、…、Guillaume Dumas

- 🎯 **研究动机**：具 CoT 推理的 AI agent 倾向默契合谋，会瓦解竞争与合谋的法律证据区分而不消除经济伤害区分
- 🔬 **研究方法**：DeepSeek-R1 在 Bertrand 寡头定价域实验，测人类提示勿合谋下的合谋倾向与 CoT 可被引导性
- 📌 **结论**：默契合谋在提示勿合谋时仍持续；CoT 可被引导向极端合谋或高度竞争且不被另一 LLM 语义检测——市场决策前须行为认证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This position paper argues that AI agents with chain-of-thought reasoning capabilities are predisposed to exhibit collusive behavior and should be required to obtain behavioral certification before making decisions that affect economic markets. This is because integrating these agents into society could collapse the legal evidentiary distinction between competition and collusion among independent firms without eroding the economic harm distinction. Experiments with DeepSeek-R1 agents in the Bertrand oligopoly pricing domain reveal a tendency towards tacit collusion that persists even when humans prompt the agents not to collude. We further show that the chain-of-thought of these agents can be steered toward either extremely collusive or highly competitive behavior in a way that is not semantically detectable by another LLM analyzing the reasoning traces. As a result, deploying reasoning agents for market decisions leads to collusive economic outcomes without any evidence of conspiracy or intent. Thus, certification based on observed behavior in representative situations is necessary to prevent collusion. We provide preliminary evidence that such agents can be steered in a generalizable way toward efficient competitive equilibria. However, developing a comprehensive behavioral certification will be required before these models can be deployed in real-world markets while ensuring their stability and efficiency.

</details>

### 37. Misalignment Contagion: Can a Misaligned Minority Shift Aligned Agents in Multi-Agent LLM Deliberation?

📄 [arXiv](https://arxiv.org/abs/2605.02751) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`analysis`、`misalignment contagion`、`trait steering`、`multi-agent system`、`multi-agent alignment`

👤 **作者**：Maria Chang、Ronny Luss、Miao Liu、Keerthiram Murugesan、Karthikeyan Ramamurthy、Djallel Bouneffouf

- 🎯 **研究动机**：对齐研究聚焦单模型单用户，多 LLM 多轮交互中错位行为能否传染未知
- 🔬 **研究方法**：在多轮社会困境博弈中观察错位传染，测试同伴被恶意 steering 的影响，并比较系统 prompt 强化与隐式特质注入两种缓解
- 📌 **结论**：LLM 博弈后更反社会且同伴恶意时加剧；系统 prompt 强化不足甚至有害，隐式特质注入更有效且无需参数或内部状态访问

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models (LMs) are increasingly used in high-stakes, multi-agent settings, where following instructions and maintaining value alignment are critical. Most alignment research focuses on interactions between a single LM and a single user, failing to address the risk of misaligned behavior spreading between multiple LMs in multi-turn interactions. We find evidence of this phenomenon, which we call misalignment contagion, across multiple LMs as they engage multi-turn conversational social dilemma games. Specifically, we find that LMs become more anti-social after gameplay and that this effect is intensified when other players are steered to act maliciously. We explore different steering techniques to mitigate such misalignment contagion and find that reinforcing an LM's system prompt is insufficient and often harmful. Instead, we propose steering with implicit traits: a technique that intermittently injects system prompts with statements that reinforce an LMs initial traits and is more effective than system prompt repetition at keeping models in line with their initial pro-social behaviors. Importantly, this method does not require access to model parameters or internal model states, making it suitable for increasingly common use cases where complex multi-agent workflows are being designed with black box models.

</details>

### 38. Trustworthy Agent Network: Trust in Agent Networks Must Be Baked In, Not Bolted On

📄 [arXiv](https://arxiv.org/abs/2605.19035) · 🌐 [Project](https://doi.org/10.1145/3770855.3818655)　📅 2026-05　🏷 KDD 2026

**关键词**：`analysis`、`agent-to-agent security`、`safe composition`、`systemic failure`

👤 **作者**：Yixiang Yao、…、Carlee Joe-Wong

- 🎯 **研究动机**：A2A 网络引入对抗性组合、语义错位与级联失效等系统性漏洞，面向单 agent 的对齐技术无法应对
- 🔬 **研究方法**：立场论文主张可信 A2A 不能靠在现有单 agent 协议上打补丁，必须从协调框架设计之初架构化内置，提出四大设计支柱的概念框架
- 📌 **结论**：信任必须 baked in 而非 bolted on

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Large Language Models has given rise to autonomous LLM-based agents capable of complex reasoning and execution. As these agents transition from isolated operation to collaborative ecosystems, we witness the emergence of the Agent-to-Agent (A2A) network, a paradigm where heterogeneous agents autonomously coordinate to solve multi-step tasks. While these networks may offer better task performance compared to simply using one agent to complete the entire task, they introduce systemic vulnerabilities, such as adversarial composition, semantic misalignment, and cascading operational failures, that existing agent alignment techniques cannot address. In this vision paper, we argue that the trustworthiness of A2A networks cannot be fully guaranteed via retrofitting on existing protocols that are largely designed for individual agents. Rather, it must be architected from the very beginning of the A2A coordination framework. We present a comprehensive conceptual framework that situates trust in A2A systems through four design pillars.

</details>

### 39. Architecture Matters for Multi-Agent Security

📄 [arXiv](https://arxiv.org/abs/2604.23459) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64792)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`agent safety`、`multi-agent evaluation`、`multi-agent system`、`failure recovery`

👤 **作者**：Ben Hagag、William L. Anderson、Christian Schroeder de Witt、Sarah Scheffler

- 🎯 **研究动机**：多智能体系统中即使单个 agent 安全，协调架构决策也会产生未被系统刻画的攻击面
- 🔬 **研究方法**：用 web agent 网络做受控实验，分阶段评测规划期拒绝、执行期拦截与攻击完成，研究 agent 角色、拓扑与记忆三类架构选择对安全-性能权衡的影响
- 📌 **结论**：MAS 的安全与性能由架构设计选择共同决定，评测必须超越单 agent 安全属性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent systems (MAS), composed of networks of two or more autonomous AI agents, have become increasingly popular in production deployments, yet introduce security risks that do not arise in single-agent settings. Even if individual agents may exhibit robust security, architectural decisions governing their coordination can create attack surfaces that have not been systematically characterized. In this work, we present an empirical study of how MAS design decisions shape the tradeoff between task performance and attack resistance. Using a network of web-based agents and stage-wise evaluations that distinguish planning-stage refusal, execution-stage interception, and successful attack completion, we study architectural choices through controlled experiments. We identify three key design choices that influence MAS security: (i) agent roles, which determine how authority and responsibility are allocated; (ii) topology, which shapes how and when agents interact; and (iii) memory, which determines the context and state visibility accessible to each agent. Overall, our results show that security and performance in multi-agent systems are governed by architectural design choices, motivating the development of further evaluations which move beyond the security properties of a single agent.

</details>

### 40. AdvEvo-MARL: Shaping Internalized Safety through Adversarial Co-Evolution in Multi-Agent Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2510.01586) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66275)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`agent safety`、`multi-agent evaluation`、`multi-agent system`、`failure recovery`

👤 **作者**：Zhenyu Pan、…、Han Liu

- 🎯 **研究动机**：LLM 多 Agent 系统的自验证缺能力识别跨 Agent 不安全链，外部 guard 模块又带来开销与单点失效
- 🔬 **研究方法**：提出 AdvEvo-MARL 共进化多智能体 RL：攻击者合成演化越狱 prompt、任务 Agent 兼顾履职与抗攻，同功能组共享组级平均回报基线以降低方差并促进协作，把安全内化到任务 Agent
- 📌 **结论**：代表性攻击场景下 ASR 持续低于 20%（基线最高 38.33%），任务准确率保持或提升最多 3.67%，无需额外 guard Agent 或系统开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems excel at planning, tool use, and role coordination, but their openness and interaction complexity also expose them to jailbreak and adversarial collaboration. Existing defenses fall into two lines: (i) self-verification that asks each agent to pre-filter unsafe instructions before execution, and (ii) external guard modules that police behaviors. The former often underperforms because a standalone agent lacks sufficient capacity to detect cross-agent unsafe chains and delegation-induced risks; the latter increases system overhead and creates a single-point-of-failure—once compromised, system-wide safety collapses, and adding more guards worsens cost and complexity. To solve these challenges, we propose AdvEvo-MARL, a co-evolutionary multi-agent reinforcement learning framework that internalizes safety into task agents. Rather than relying on external guards, AdvEvo-MARL jointly optimizes attackers (which synthesize evolving jailbreak prompts) and defenders (task agents trained to both accomplish their duties and resist attacks) in adversarial learning environments. To stabilize learning and foster cooperation, we introduce a public baseline for advantage estimation: agents within the same functional group share a group-level mean-return baseline, enabling lower-variance updates and stronger intra-group coordination. Across representative attack scenarios, AdvEvo-MARL consistently keeps attack-success rate (ASR) below 20\%, whereas baselines reach up to 38.33\%, while preserving or even improving task accuracy (up to +3.67\%). These results show that safety and utility can be jointly improved without relying on extra guard agents or added system overhead.

</details>

### 41. Counterfactual Reasoning for Responsibility Attribution in Probabilistic Multi-Agent Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2007.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`analysis`、`multi-agent system`、`responsibility attribution`、`counterfactual reasoning`

- 🎯 **研究动机**：多智能体系统中各 agent 对结果的因果贡献量化是设计与分析的基础难题
- 🔬 **研究方法**：把系统建模为并发随机多人博弈，定义追溯式反事实责任并用 Shapley 值分配（证明公平性与一致性）；以 Nash 均衡为解概念计算权衡责任与期望回报的稳定策略
- 📌 **结论**：形式化框架同时支持责任感知系统的验证与策略推理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Responsibility allocation—determining the extent to which agents causally contribute to outcomes— is a fundamental challenge in the design and analysis of multi-agent systems. In this work, we model such systems as concurrent stochastic multiplayer games and introduce a notion of retrospective (backward) counterfactual responsibility, which quantifies an agent’s causal contribution to outcomes resulting from a given strategy profile. To allocate responsibility among agents, we utilise the Shapley value and formally show that this method satisfies key desirable properties, including fairness and consistency. Building on this foundation, we propose a formal framework that supports both verification and strategic reasoning in responsibilityaware multi-agent systems. Furthermore, by adopting Nash equilibrium as the solution concept, we demonstrate how to compute stable strategy profiles in which agents trade off responsibility against expected reward.

</details>

### 42. SNEAK: Evaluating Strategic Communication and Information Leakage in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.29846) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`benchmark`、`strategic communication`、`information leakage`、`multi-agent system`、`asymmetric knowledge`

👤 **作者**：Adar Avsian、Larry Heck

- 🎯 **研究动机**：现有基准不测非对称信息下的策略性沟通——既要传递信息又要保守秘密
- 🔬 **研究方法**：SNEAK 给定语义类别、候选词集与秘密词，模型须生成暗示知道秘密又不泄露的消息；知情盟友与不知情变色龙两个模拟 agent 分别度量效用与泄露
- 📌 **结论**：策略性沟通仍是当前模型的短板，人类参与者得分最高达模型的四倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in multi-agent settings where communication must balance informativeness and secrecy. In such settings, an agent may need to signal information to collaborators while preventing an adversary from inferring sensitive details. However, existing LLM benchmarks primarily evaluate capabilities such as reasoning, factual knowledge, or instruction following, and do not directly measure strategic communication under asymmetric information. We introduce SNEAK (Secret-aware Natural language Evaluation for Adversarial Knowledge), a benchmark for evaluating selective information sharing in language models. In SNEAK, a model is given a semantic category, a candidate set of words, and a secret word, and must generate a message that indicates knowledge of the secret without revealing it too clearly. We evaluate generated messages using two simulated agents with different information states: an ally, who knows the secret and must identify the intended message, and a chameleon, who does not know the secret and attempts to infer it from the message. This yields two complementary metrics: utility, measuring how well the message communicates to collaborators, and leakage, measuring how much information it reveals to an adversary. Using this framework, we analyze the trade-off between informativeness and secrecy in modern language models and show that strategic communication under asymmetric information remains a challenging capability for current systems. Notably, human participants outperform all evaluated models by a large margin, achieving up to four times higher scores.

</details>

### 43. TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems

🎓 [Official](https://aclanthology.org/2026.acl-long.1442/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`agent safety`、`LLM agent`、`multi-agent system`、`tool-use attack`

👤 **作者**：Ishan Kavathekar、Hemang Jain、Ameya Rathod、Ponnurangam Kumaraguru、Tanuja Ganu

- 🎯 **研究动机**：多智能体 LLM 系统的安全研究不足，现有基准聚焦单智能体设定，无法捕捉多智能体动态与协作的独特漏洞
- 🔬 **研究方法**：构建 TAMAS 基准：5 个场景、6 类攻击共 300 个对抗实例、211 个工具与 100 个无害任务，覆盖 10 个 backbone LLM 与 Autogen、CrewAI 的 3 种交互配置，并提出 Effective Robustness Score
- 📌 **结论**：多智能体系统对对抗攻击高度脆弱，凸显更强防御的迫切需求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated strong capabilities as autonomous agents through tool use, planning, and decision-making abilities, leading to their widespread adoption across diverse tasks. As task complexity grows, multi-agent LLM systems are increasingly used to solve problems collaboratively. However, safety and security of these systems remains largely under-explored. Existing benchmarks and datasets predominantly focus on single-agent settings, failing to capture the unique vulnerabilities of multi-agent dynamics and co-ordination. To address this gap, we introduce T hreats and A ttacks in M ulti- A gent S ystems ( TAMAS ), a benchmark designed to evaluate the robustness and safety of multi-agent LLM systems. TAMAS includes five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools, along with 100 harmless tasks. We assess system performance across ten backbone LLMs and three agent interaction configurations from Autogen and CrewAI frameworks, highlighting critical challenges and failure modes in current multi-agent deployments. Furthermore, we introduce Effective Robustness Score (ERS) to assess the tradeoff between safety and task effectiveness of these frameworks. Our findings show that multi-agent systems are highly vulnerable to adversarial attacks, underscoring the urgent need for stronger defenses. TAMAS provides a foundation for systematically studying and improving the safety of multi-agent LLM systems. Code and dataset is available at https://github.com/microsoft/TAMAS.

</details>

### 44. Interaction-Breaking Adversarial Learning Framework for Robust Multi-Agent Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2605.18024) · 🌐 [Project](https://sunwoolee0504.github.io/IBAL) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61001)　📅 2026　🏷 ICML 2026

**关键词**：`tool`、`defense`、`adversarial defense`、`multi-agent evaluation`、`multi-agent system`、`robustness certification`

👤 **作者**：Sunwoo Lee、Mingu Kang、Yonghyeon Jo、Seungyul Han

- 🎯 **研究动机**：已有鲁棒 MARL 只考虑价值导向攻击，交互结构本身被破坏时的鲁棒性缺失
- 🔬 **研究方法**：IBAL 从信息论视角构造扰动智能体观测与动作、阻碍协调的攻击，并在此类扰动下训练智能体
- 📌 **结论**：多种攻击设定乃至智能体缺失场景下鲁棒性与性能均超现有基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cooperation is central to multi-agent reinforcement learning (MARL), yet learned coordination can be fragile when external perturbations disrupt inter-agent interactions. Prior robust MARL methods have primarily considered value-oriented attacks, leaving a gap in robustness when interaction structures themselves are corrupted. In this paper, we propose an interaction-breaking adversarial learning (IBAL) framework that takes an information-theoretic view to construct attacks that impede coordination by perturbing agents’ observations and actions, and trains agents to perform reliably under such disruptions. Empirically, our approach improves robustness over existing robust MARL baselines across diverse attack settings and yields stronger performance even under agent-missing scenarios. Our code is available at https://sunwoolee0504.github.io/IBAL.

</details>

### 45. A Multi-Agent Framework for High-Interaction Terminal Simulation

🎓 [Official](https://aclanthology.org/2026.acl-long.1515/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`agent safety`、`LLM agent`、`multi-agent system`、`cybersecurity`

👤 **作者**：Kai Wei、Yuwen Cui、Kehan Shen、Hua Wei、Guangjing Wang

- 🎯 **研究动机**：脚本化终端模拟器缺灵活性，LLM 方案又常误解命令、破坏输出格式、状态漂移且易受 prompt injection
- 🔬 **研究方法**：提出 MANTIS：多 Agent 架构加过滤式路由模型把命令安全分派给外部工具或 LLM agent，支持交互式命令并防御注入；设计带历史剪枝的 agentic 文件系统保持长期状态一致；发布三个数据集（28,045 对真实输入输出等）
- 📌 **结论**：超过 SOTA 基线 9% 以上，多轮终端模拟准确率超 95%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Terminal simulation, framed as a terminal command-level Turing test, is a long-standing problem of symbolic language generation in dialogue and interactive systems. Prior scripted simulators lack the flexibility needed for complex, multi-turn interactions, while LLM-based approaches often misinterpret commands, break output formats, drift from system state, and remain vulnerable to prompt injection. In this work, we propose MANTIS, a terminal simulation framework that improves realism, consistency, and robustness in command-language generation. MANTIS integrates a multi-agent architecture with a filter-based routing model that safely dispatches commands to external tools or an LLM-based agent, enabling support for interactive commands while defending against prompt injection attacks. In addition, we design an agentic file system with history pruning to preserve long-term state consistency. We release three datasets: 28,045 real terminal input-output pairs, a 1,000-session multi-turn interaction dataset, and a 25,849-instance labeled classification dataset. MANTIS outperforms state-of-the-art baselines by more than 9%, achieving over 95% accuracy on multi-turn terminal simulation. The dataset and source code are available at https://github.com/kaiwei666a/MANTIS_Terminal_Simulation

</details>

### 46. BRA-Audit: Budgeted Runtime Auditing for LLM Multi-Agent Systems via Cumulative-Exposure Audit-Point Placement

📄 [arXiv](https://arxiv.org/abs/2608.14668)　📅 2026-08

**关键词**：`detection`、`multi-agent system`、`risk propagation`、`collusive behavior`

👤 **作者**：Kaixiang Wang、Yidan Lin、Jiong Lou、Jie Li

- 🎯 **研究动机**：LLM 多智能体系统审计面临两难：仅末端审计弱化效果、每轮全审 token 成本高
- 🔬 **研究方法**：BRA-Audit 把 MAS 执行建模为动态依赖图，将审计调度形式化为固定预算下最小化累计未审计暴露的审计点放置，贪心调度优先高影响且久未审计区域并支持局部恢复
- 📌 **结论**：性能恢复接近干净设定、与重防护方法相当，端到端 token 消耗降 17.2%-40.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems (LLM-MAS) solve complex tasks through specialized collaboration, but inter-agent dependencies can propagate hallucinated or malicious outputs into system-level failures. Auditor agents mitigate these risks, yet existing strategies face an efficiency dilemma: end-only auditing reviews long trajectories and final outputs, potentially weakening audit effectiveness and enlarging rollback scope, while auditing every agent each round improves detection and localization at high token cost. How can guard performance be preserved while minimizing token cost? To address this problem, we propose BRA-Audit, a budget-aware runtime auditing framework that models MAS execution as a dynamic dependency graph and formulates audit scheduling as audit-point placement under a fixed audit-call budget to minimize cumulative unchecked exposure. Its greedy scheduler prioritizes influential and long-unaudited regions, while trusted audit points enable localized recovery. Across structured coordination, complex reasoning, and open-ended tasks, BRA-Audit restores performance close to the clean setting, remains competitive with heavy guard methods and reduces end-to-end token consumption by \(17.2\%\)--\(40.6\%\).

</details>

### 47. Is Monitoring Enough? Strategic Agent Selection For Stealthy Attack in Multi-Agent Discussions

📄 [arXiv](https://arxiv.org/abs/2603.21194) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4950)　📅 2026-03　🏷 ECCV 2026

**关键词**：`detection`、`attack`、`stealthy attack`、`multi-agent system`、`risk propagation`、`multi-agent security`

👤 **作者**：Qiuchi Xiang、Haoxuan Qu、Hossein Rahmani、Jun Liu

- 🎯 **研究动机**：讨论受监控场景下的隐蔽攻击未被研究，现有攻击在通信监控下模式可检、大多失效
- 🔬 **研究方法**：提出显式针对讨论监控场景定制的攻击方法，策略性选择参与 agent 以规避异常检测
- 📌 **结论**：持续监控下有效攻击依然可行，仅靠监控不足以保障多 agent 讨论安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-agent discussions have been widely adopted, motivating growing efforts to develop attacks that expose their vulnerabilities. In this work, we study a practical yet largely unexplored attack scenario, the discussion-monitored scenario, where anomaly detectors continuously monitor inter-agent communications and block detected adversarial messages. Although existing attacks are effective without discussion monitoring, we show that they exhibit detectable patterns and largely fail under such monitoring constraints. But does this imply that monitoring alone is sufficient to secure multi-agent discussions? To answer this question, we develop a novel attack method explicitly tailored to the discussion-monitored scenario. Extensive experiments demonstrate that effective attacks remain possible even under continuous monitoring, indicating that monitoring alone does not eliminate adversarial risks.

</details>

### 48. When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2607.06807) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65619)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`analysis`、`multi-agent evaluation`、`multi-agent system`、`risk propagation`、`LLM agent security`

👤 **作者**：Haowen Xu、…、Xiaoyan Sun

- 🎯 **研究动机**：现有 MAS 安全防御假设攻击语义显式且可用图建模交互拓扑，而真实攻击语义隐蔽、执行异步无时序对齐
- 🔬 **研究方法**：提出 AcMAS：分析本地智能体激活空间的内部推理状态检测恶意行为，不依赖显式交互图，并据此恢复被攻陷智能体而非破坏性隔离
- 📌 **结论**：对隐蔽攻击同步设置 F1 达 0.94（基线 0.72）、异步 0.93（基线 0.38），跨骨干、攻击强度与 MAS 规模泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchronous without the temporal alignment assumed by graph-based propagation models. To address these limitations, we propose AcMAS, an activation-based framework for malicious-behavior detection in MAS. By analyzing internal reasoning states in the activation space of local agents, AcMAS detects even stealthy attacks in a synchronization-robust fashion, without relying on explicit interaction graphs. Moreover, our activation analysis provides critical signals to guide AcMAS in restoring the functionality of compromised agents, rather than the disruptive agent isolation commonly used by the state-of-the-art methods. Comprehensive evaluation demonstrates that AcMAS significantly outperforms graph-based baselines against stealthy attacks, by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38), with generalization across diverse open-source LLM backbones, attack intensity, and MAS scale.

</details>

### 49. Playing Along: Learning a Double-Agent Defender for Belief Steering via Theory of Mind

📄 [arXiv](https://arxiv.org/abs/2604.11666) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`defense`、`theory of mind`、`belief steering`、`multi-agent system`、`sensitive-information protection`

👤 **作者**：Hanqi Xiao、Vaidehi Patil、Zaid Khan、Hyunji Lee、Elias Stengel-Eskin、Mohit Bansal

- 🎯 **研究动机**：对话系统需对潜在对抗者做 theory-of-mind 推理以保护敏感信息，frontier 模型在此能力不足
- 🔬 **研究方法**：提出 ToM-SB 双面间谍任务，defender 须欺骗持有部分先验知识的攻击者；用 RL 分别以 fooling 与 ToM 奖励训练 AI Double Agent
- 📌 **结论**：fooling 与 ToM 奖励双向涌现互促；组合两者在困难场景超过 Gemini3-Pro 与 GPT-5.4 加 ToM prompting

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) become the engine behind conversational systems, their ability to reason about the intentions and states of their dialogue partners (i.e., form and use a theory-of-mind, or ToM) becomes increasingly critical for safe interaction with potentially adversarial partners. We propose a novel privacy-themed ToM challenge, ToM for Steering Beliefs (ToM-SB), in which a defender must act as a Double Agent to steer the beliefs of an attacker with partial prior knowledge within a shared universe. To succeed on ToM-SB, the defender must engage with and form a ToM of the attacker, with a goal of fooling the attacker into believing they have succeeded in extracting sensitive information. We find that strong frontier models like Gemini3-Pro and GPT-5.4 struggle on ToM-SB, often failing to fool attackers in hard scenarios with partial attacker prior knowledge, even when prompted to reason about the attacker's beliefs (ToM prompting). To close this gap, we train models on ToM-SB to act as AI Double Agents using reinforcement learning, testing both fooling and ToM rewards. Notably, we find a bidirectionally emergent relationship between ToM and attacker-fooling: rewarding fooling success alone improves ToM, and rewarding ToM alone improves fooling. Across four attackers with different strengths, six defender methods, and both in-distribution and out-of-distribution (OOD) evaluation, we find that gains in ToM and attacker-fooling are well-correlated, highlighting belief modeling as a key driver of success on ToM-SB. AI Double Agents that combine both ToM and fooling rewards yield the strongest fooling and ToM performance, outperforming Gemini3-Pro and GPT-5.4 with ToM prompting on hard scenarios. We also show that ToM-SB and AI Double Agents can be extended to stronger attackers, demonstrating generalization to OOD settings and the upgradability of our task.

</details>

### 50. Securing Multi-Agent Systems Against Corruptions via Node Contribution Backpropagation

📄 [arXiv](https://arxiv.org/abs/2510.19420) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63780)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`multi-agent evaluation`、`multi-agent system`、`risk propagation`、`LLM agent security`、`tool-use attack`

👤 **作者**：Chengcan Wu、Zhixin Zhang、Mingqian Xu、Zeming Wei、Meng Sun

- 🎯 **研究动机**：MAS 中对抗 agent 注入的误导信息会传染性传播腐蚀良性 agent，现有基于图的防御局限于静态图
- 🔬 **研究方法**：把 MAS 通信建模为带符号有向无环图，经反向传播计算各 agent 对最终决策的贡献，据此识别并隔离恶意 agent（BPD）
- 📌 **结论**：在复杂动态 MAS 环境中显著优于现有 MAS 防御机制，为可信部署提供护栏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-Agent Systems (MAS) have become a prevalent paradigm for Large Language Model (LLM) applications. However, the complex multi-agent design in MAS introduces unique trustworthiness concerns: adversarial agents can inject misleading information that propagates contagiously through the system, corrupting benign agents and leading to false outputs. Existing graph-based defenses model agents as nodes and communications as edges, yet are limited to static-graph defenses. In this paper, we propose a dynamic defense paradigm that models MAS communication as a signed directed acyclic graph and computes each agent's contribution to the final decision via backward propagation, enabling accurate identification and isolation of malicious agents to secure multi-agent task collaboration. Experimental results in complex and dynamic MAS environments demonstrate that our method notably outperforms existing MAS defense mechanisms, providing an effective guardrail for trustworthy MAS deployment. Our code is available at https://github.com/ChengcanWu/BPD.

</details>

### 51. Secure Multi-agent Reinforcement Learning for Service Systems with Affinity and Byzantine Nodes: Stability Analysis and Protection Design

🎓 [Official](https://icml.cc/virtual/2026/poster/62838)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`multi-agent evaluation`、`multi-agent system`、`risk propagation`、`adversarial defense`、`robustness certification`

👤 **作者**：Yifan Jiang、Jiasheng Pan、Mengtian Li、Li Jin

- 🎯 **研究动机**：网络化服务系统的去中心化 MARL 中，Byzantine 节点可利用无界状态空间破坏共识，同时动摇学习与排队过程的稳定性
- 🔬 **研究方法**：提出弹性共识 MARL 算法缓解对抗参数操纵并保证流量稳定，证明协作策略几乎必然收敛到全局目标平稳解的有界邻域
- 📌 **结论**：在 LLM 语义路由、云计算分布式轮询与智能制造物流等多个服务系统上验证了有效性与通用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study decentralized multi-agent reinforcement learning (MARL) for networked service systems with affinity in the presence of Byzantine nodes. The way that a server processes a job depends on an affinity state that captures the correlation between the job and the server. Each node learns a local control policy via an actor-critic algorithm with linear function approximation over inherently unbounded space of traffic states, while exchanging parameter information with neighbors through a communication graph. A set of Byzantine agents can exploit the unbounded state space to compromise the consensus mechanism, destabilizing both learning and queuing processes. To address this vulnerability, we propose a resilient consensus-based MARL algorithm, which mitigates adversarial parameter manipulation and guarantees traffic stability under mild assumptions. We prove that the cooperative agents’ policies converge almost surely to a bounded neighborhood of a stationary solution of the global objective. We demonstrate the effectiveness and generality of the proposed framework in several representative service systems, including semantic routing for large language model serving, distributed polling in cloud computing, and smart manufacturing logistics.

</details>

### 52. MaMa: A Game-Theoretic Approach for Designing Safe Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2602.04431) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64729)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`agent safety benchmark`、`trajectory evaluation`、`failure coverage`、`agent safety`、`multi-agent evaluation`

👤 **作者**：Jonathan Nöther、Adish Singla、Goran Radanovic

- 🎯 **研究动机**：多智能体系统在部分智能体被攻陷时如何保持安全缺乏自动设计方法
- 🔬 **研究方法**：形式化为 Stackelberg 安全博弈：Meta-Agent 迭代提出系统设计，Meta-Adversary 最佳响应选择并攻陷智能体子集，以最强攻击作反馈
- 📌 **结论**：设计的系统持续抵御最坏情况攻击且性能与纯任务优化相当，并泛化到更强或不同目标的攻击者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based multi-agent systems have demonstrated impressive capabilities, but they also introduce significant safety risks when individual agents fail or behave adversarially. In this work, we study the automated design of agentic systems that remain safe even when a subset of agents is compromised. Inspired by Stackelberg security games, we formalize this problem as a game between a system designer (the Meta-Agent) and a best-responding Meta-Adversary that selects and compromises a subset of agents to minimize safety. We propose Meta-Adversary–Meta-Agent (MaMa), a novel algorithm inspired by this formalization for automatically designing safe agentic systems. Our approach uses LLM-based adversarial search, where the Meta-Agent iteratively proposes system designs and receives feedback based on the strongest attacks discovered by the Meta-Adversary. Empirical evaluations across diverse environments show that systems designed with MaMa consistently defend against worst-case attacks while maintaining performance comparable to systems optimized solely for task success. Moreover, the resulting systems generalize to stronger adversaries, as well as ones with different attack objectives or underlying LLMs, demonstrating robust safety beyond the training setting. Code is available at https://github.com/JNoether/MaMa

</details>
