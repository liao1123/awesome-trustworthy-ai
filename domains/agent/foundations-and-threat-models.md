# Agent Security 基础框架、Survey 与 Threat Model

[返回 Agent Security 目录](README.md)

## 研究方向

本页整理能够解释整个 Agent security landscape 的基础框架。核心不是再列一组攻击名称，而是明确 security property、资产与主体、instruction/data provenance、delegated authority、persistent state、跨层传播和时间尺度，从而判断一个 action 在具体任务上下文中为何违规，以及防御和 benchmark 实际覆盖了哪一段生命周期。

## 研究脉络

- **组件枚举：** 早期 survey 从 brain、memory、tool 和 environment 等组件归纳 prompt injection、privacy、backdoor 与 unsafe action。
- **攻击面分层：** 后续 taxonomy 按 foundation、cognitive、memory、tool execution、MAS、ecosystem 和 governance 定位漏洞来源，并增加 session persistence 等时间维度。
- **上下文安全属性：** formal framework 将 task alignment、action alignment、source authorization 和 data isolation 作为可检查属性，避免脱离授权上下文判断动作。
- **系统生命周期：** 新近综述围绕 information flow、delegated authority 与 persistent state 串联 ingestion、planning、execution、persistence 和 monitoring。
- **Agent-human interaction：** 产业系统主要依赖 policy specification、runtime approval 与 scope configuration，学术研究则更偏向 intent anchoring 和 trust labeling；两者之间仍存在明显部署鸿沟。
- **当前边界：** 现有防御仍缺少跨层组合保证，benchmark 对长期状态、真实权限和部署配置的覆盖也不充分。

## Survey 与 Taxonomy

### 1. Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions

📄 [arXiv](https://arxiv.org/abs/2607.12406)　📅 2026-09

**关键词**：`survey`、`agent isolation`、`boundary taxonomy`、`cross-boundary propagation`

👤 **作者**：Huihao Jing、…、Yangqiu Song

- 🎯 **研究动机**：agent 安全文献碎片化，prompt injection、工具滥用、记忆投毒等失败共享相同结构成因却缺乏统一解释框架
- 🔬 **研究方法**：把隔离（用户输入、工具访问、执行通道、agent 间通信与环境上下文的分离）作为一等原则，用五边界分类法（用户-agent、agent-工具、agent-执行、agent-agent、系统-环境）组织文献并总结跨边界失败路径
- 📌 **结论**：该视角可定位隔离丧失首发点、危害跨边界传播路径与各接口最相关防御，提出 isolation-by-construction 研究议程

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share the same structural cause, and how they spread through an agent workflow. In this survey, we treat isolation as a first-class principle for LLM-agent system safety. By isolation, we refer to the separation of user inputs, tool access, execution channels, inter-agent communication, and environment-originated context. We organize the literature with a boundary-centric taxonomy of five boundaries: user-agent, agent-tool, agent-execution, agent-agent, and system-environment. This view helps identify where the loss of isolation first occurs, how compromise propagates across boundaries, and which defenses are most relevant at each interface. We also summarize cross-boundary failure paths, discuss open challenges, and outline a research agenda for isolation-by-construction in future agent systems.

</details>

### 2. Toward Safe LLM Agents: A Survey of Specification, Verification, and Enforcement

📄 [arXiv](https://arxiv.org/abs/2608.14590)　📅 2026-08

**关键词**：`survey`、`agent security`、`threat model`、`attack taxonomy`

👤 **作者**：Pierre Dantas、Lucas Cordeiro、Ehsan Nowroozi、Tihanyi Norbert

- 🎯 **研究动机**：LLM agent 执行数据库更新、API 调用等不可逆动作，但无系统提供任务级形式安全保证，规范/验证/执行研究割裂
- 🔬 **研究方法**：PRISMA 系统综述 38 项研究（2022-2026），提出三级分类法、比较分析与十问题研究议程
- 📌 **结论**：自然语言到形式化翻译仅 24-35% 语义正确是首要瓶颈；运行时监控最成熟（降不安全动作 40-65%）但无完整保证；verifier tax——拦 94% 不安全动作仍留不足 5% 安全任务完成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly perform irreversible real-world actions, including database updates, API calls, file operations, and autonomous use of tools. However, no existing system provides formally grounded, task-level safety guarantees for the plans these agents generate. Research remains fragmented across specification, verification, and enforcement, limiting understanding of the strengths and limitations of existing approaches. To address this gap, we conducted a PRISMA 2020 systematic review of 38 studies published between 2022 and 2026 and retrieved from six academic databases. Our analysis reveals four key findings. First, the specification bottleneck remains the primary challenge: natural-language-to-formal translation achieves only 24% to 35% semantic correctness, undermining downstream verification. Second, runtime monitoring is the most mature enforcement strategy, reducing unsafe actions by 40% to 65% in controlled settings, but it does not provide complete safety guarantees. Third, the verifier tax shows that blocking 94% of unsafe actions can still result in less than 5% safe task completion because agents exploit alternative unsafe paths. Finally, no existing approach simultaneously achieves soundness, scalability, semantic correctness, and task-level safety preservation. We contribute a three-level taxonomy, a comparative analysis of existing techniques, a synthesis of evidence on the verifier tax, and a ten-problem research agenda for trustworthy agentic AI.

</details>

### 3. Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation

📄 [arXiv](https://arxiv.org/abs/2606.10749)　📅 2026-06

**关键词**：`survey`、`agent lifecycle`、`delegated authority`、`persistent state`

👤 **作者**：Yuchen Ling、Shengcheng Yu、Zhenyu Chen、Chunrong Fang

- 🎯 **研究动机**：LLM agent 安全面向工具、记忆与外部环境，攻击族、防御层与评估设定分散，缺乏系统综合
- 🔬 **研究方法**：以生命周期与系统视角综合 247 篇论文，用信息流、委托权限与持久状态的交互建模 agent 安全，围绕威胁模型、攻击族、防御与评估四问组织文献
- 📌 **结论**：prompt injection 与工具介导控制流劫持仍占主导，持久状态污染与多 agent 传播成为新兴焦点；防御组合性弱，基准低估长时序有状态风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings, failures are no longer limited to unsafe text generation. Untrusted content may redirect control flow, misuse tool privileges, corrupt persistent state, leak sensitive information, or trigger harmful external actions. At the same time, research on LLM agent security is expanding quickly but remains fragmented across attack families, defense layers, application domains, and evaluation settings. This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework that models agent security around the interaction of information flow, delegated authority, and persistent state. We organize the literature around four questions: how LLM agent security should be modeled, which threat surfaces and attack families dominate, what defenses have been proposed and with what tradeoffs, and how security claims are evaluated. We find that prompt injection and tool-mediated control-flow hijacking still dominate the field, while persistent state corruption and multi-agent propagation are becoming central emerging concerns. We further find that current defenses provide useful building blocks but remain weakly compositional, and that existing benchmarks still underrepresent long-horizon, stateful, and deployment-sensitive risks. We argue that secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings.

</details>

### 4. Security Attack and Defense Strategies for Autonomous Agent Frameworks: A Layered Review with OpenClaw as a Case Study

📄 [arXiv](https://arxiv.org/abs/2604.27464)　📅 2026-04

**关键词**：`survey`、`autonomous framework`、`cross-layer propagation`、`OpenClaw`

👤 **作者**：Luyao Xu、Xiang Chen

- 🎯 **研究动机**：Agent 框架演进为工具集成、持续运行的系统，风险超出传统 prompt 级漏洞，缺分层综述
- 🔬 **研究方法**：以 OpenClaw 为案例，按 context/instruction、tool/action、state/persistence、ecosystem/automation 四层梳理风险与防御
- 📌 **结论**：威胁可跨层传播——从输入操纵到不安全动作、持久状态污染再到生态级影响；指出层间研究失衡、长时程评测缺失与信任模型薄弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous agent frameworks built upon large language models (LLMs) are evolving into complex, tool-integrated, and continuously operating systems, introducing security risks beyond traditional prompt-level vulnerabilities. As this paradigm is still at an early stage of development, a timely and systematic understanding of its security implications is increasingly important. Although a growing body of work has examined different attack surfaces and defense problems in agent systems, existing studies remain scattered across individual aspects of agent security, and there is still a lack of a layered review on this topic. To address this gap, this survey presents a layered review of security risks and defense strategies in autonomous agent frameworks, with OpenClaw as a case study. We organize the analysis into four security-relevant layers: the context and instruction layer, the tool and action layer, the state and persistence layer, and the ecosystem and automation layer. For each layer, we summarize its functional role, representative security risks, and corresponding defense strategies. Based on this layered analysis, we further identify that threats in autonomous agent frameworks may propagate across layers, from manipulated inputs to unsafe actions, persistent state contamination, and broader ecosystem-level impact. Finally, we highlight potential key challenges, including research imbalance across layers, the lack of long-horizon evaluation, and weak ecosystem trust models, and outline future directions toward more systematic and integrated defenses.

</details>

### 5. A Systematic Survey of Security Threats and Defenses in LLM-Based AI Agents: A Layered Attack Surface Framework

📄 [arXiv](https://arxiv.org/abs/2604.23338)　📅 2026-04

**关键词**：`survey`、`layered attack surface`、`threat temporality`、`defense gap`

👤 **作者**：Kexin Chu

- 🎯 **研究动机**：现有安全 taxonomy 按攻击类型组织威胁，掩盖其在 agent 栈内的位置与时间尺度
- 🔬 **研究方法**：LASM 将 agent 栈分为七层并叠加四类时间性轴，以 7×4 框架分析 116 篇 2021-2026 论文
- 📌 **结论**：栈上层（尤其长时程与跨栈传播威胁）探索严重不足，多个攻击区无对应防御，基准不覆盖跨 session 失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI systems introduce a security surface that is qualitatively different from that of stateless LLMs. They persist memory, invoke external tools, coordinate with peer agents, and operate across sessions, allowing attacks to emerge not only at the prompt interface but also through architectural state, delegated authority, and long-horizon interactions. Existing security taxonomies, however, primarily organize threats by attack type, such as prompt injection or jailbreaking, and therefore obscure where in the agentic stack a threat arises and over what timescale it manifests. We propose the Layered Attack Surface Model (\lasm), a structural taxonomy for agentic AI security. \lasm decomposes the agentic stack into seven layers -- Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, and Governance -- and augments them with a four-class temporality axis covering instantaneous, session-persistent, cross-session cumulative, and sub-session-stack threats. We use this 7$\times$4 framework to analyze 116 papers from 2021--2026. The resulting map reveals that the upper layers of the agentic stack remain sharply under-explored, especially for long-horizon and stack-propagating threats; multiple documented attack regions have no corresponding defenses; and current benchmarks provide no coverage for cross-session or sub-session-stack failure modes. We further derive a cross-layer defense taxonomy, defense recipes for canonical attack classes, and a dependency DAG that separates near-term engineering gaps from fundamental research challenges. We release the per-paper coding, robustness scripts, and a reference Agent Bill of Materials schema to support reproducible analysis.

</details>

### 6. Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats

📄 [arXiv](https://arxiv.org/abs/2603.11619)　📅 2026-03

**关键词**：`analysis`、`autonomous agent`、`OpenClaw`、`security mitigation`

👤 **作者**：Xinhao Deng、…、Qi Li

- 🎯 **研究动机**：OpenClaw 类即时通讯交互加高权限执行的自主 agent 大幅扩张系统攻击面
- 🔬 **研究方法**：提出初始化、输入、推理、决策、执行五层生命周期安全框架，系统检验间接注入、skill 供应链污染、记忆投毒与意图漂移等复合威胁
- 📌 **结论**：揭示单点防御应对跨时期、多阶段系统性风险的局限，需覆盖全生命周期的整体安全架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous Large Language Model (LLM) agents, exemplified by OpenClaw, demonstrate remarkable capabilities in executing complex, long-horizon tasks. However, their tightly coupled instant-messaging interaction paradigm and high-privilege execution capabilities substantially expand the system attack surface. In this paper, we present a comprehensive security threat analysis of OpenClaw. To structure our analysis, we introduce a five-layer lifecycle-oriented security framework that captures key stages of agent operation, i.e., initialization, input, inference, decision, and execution, and systematically examine compound threats across the agent's operational lifecycle, including indirect prompt injection, skill supply chain contamination, memory poisoning, and intent drift. Through detailed case studies on OpenClaw, we demonstrate the prevalence and severity of these threats and analyze the limitations of existing defenses. Our findings reveal critical weaknesses in current point-based defense mechanisms when addressing cross-temporal and multi-stage systemic risks, highlighting the need for holistic security architectures for autonomous LLM agents. Within this framework, we further examine representative defense strategies at each lifecycle stage, including plugin vetting frameworks, context-aware instruction filtering, memory integrity validation protocols, intent verification mechanisms, and capability enforcement architectures.

</details>

### 7. The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey

📄 [arXiv](https://arxiv.org/abs/2603.11088) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic)　📅 2026-03　🏷 USENIX Security 2026

**关键词**：`survey`、`agentic AI`、`attack-defense taxonomy`、`research landscape`

👤 **作者**：Juhee Kim、…、Dawn Song

- 🎯 **研究动机**：LLM 加非 AI 组件的 agent 引入与传统软件根本不同的安全挑战，缺少系统综述
- 🔬 **研究方法**：首个 AI agent 安全综合调查：分析设计空间、攻击版图与防御机制，并辅以案例研究
- 📌 **结论**：指出当前 agent 安全防护的缺口与开放挑战，建立理解其安全风险与防御策略的首个系统框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents that combine large language models with non-AI system components are rapidly emerging in real-world applications, offering unprecedented automation and flexibility. However, this unprecedented flexibility introduces complex security challenges fundamentally different from those in traditional software systems. This paper presents the first systematic and comprehensive survey of AI agent security, including an analysis of the design space, attack landscape, and defense mechanisms for secure AI agent systems. We further conduct case studies to point out existing gaps in securing agentic AI systems and identify open challenges in this emerging domain. Our work also introduces the first systematic framework for understanding the security risks and defense strategies of AI agents, serving as a foundation for building both secure agentic systems and advancing research in this critical area.

</details>

### 8. The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis

📄 [arXiv](https://arxiv.org/abs/2602.10453)　📅 2026-02

**关键词**：`survey`、`prompt injection`、`context-dependent task`、`AgentPI`

👤 **作者**：Peiran Wang、…、Yuan Tian

- 🎯 **研究动机**：现有 prompt injection 防御与基准普遍忽略需依赖运行时环境观察决策的 context-dependent 任务
- 🔬 **研究方法**：建立攻击（启发式/优化式）与防御（text/model/execution 三阶段）分类法，并提出 AgentPI 基准在上下文依赖交互下评测防御
- 📌 **结论**：无单一防御能同时做到高可信、高效用与低延迟；许多防御靠压制上下文输入在旧基准显得有效，无法泛化到真实 agent 场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The evolution of Large Language Models (LLMs) has resulted in a paradigm shift towards autonomous agents, necessitating robust security against Prompt Injection (PI) vulnerabilities where untrusted inputs hijack agent behaviors. This SoK presents a comprehensive overview of the PI landscape, covering attacks, defenses, and their evaluation practices. Through a systematic literature review and quantitative analysis, we establish taxonomies that categorize PI attacks by payload generation strategies (heuristic vs. optimization) and defenses by intervention stages (text, model, and execution levels). Our analysis reveals a key limitation shared by many existing defenses and benchmarks: they largely overlook context-dependent tasks, in which agents are authorized to rely on runtime environmental observations to determine actions. To address this gap, we introduce AgentPI, a new benchmark designed to systematically evaluate agent behavior under context-dependent interaction settings. Using AgentPI, we empirically evaluate representative defenses and show that no single approach can simultaneously achieve high trustworthiness, high utility, and low latency. Moreover, we show that many defenses appear effective under existing benchmarks by suppressing contextual inputs, yet fail to generalize to realistic agent settings where context-dependent reasoning is essential. This SoK distills key takeaways and open research problems, offering structured guidance for future research and practical deployment of secure LLM agents.

</details>

### 9. SoK: Attack and Defense Landscape of Agentic AI Systems

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee-agentic)　📅 2026　🏷 USENIX Security 2026

**关键词**：`survey`、`agentic AI`、`agent security`、`threat model`、`attack surface`、`defense taxonomy`

👤 **作者**：Juhee Kim、Wenbo Guo、Dawn Song

- 🎯 **研究动机**：LLM 与非 AI 工具组件集成的 agent 系统快速落地，其安全挑战与传统软件系统不同，缺乏系统化梳理
- 🔬 **研究方法**：对 AI agent 安全做知识系统化：分析设计空间、攻击面与防御机制分类，并识别该新兴领域的开放挑战
- 📌 **结论**：给出理解 AI agent 安全风险与防御策略的系统框架，作为构建安全 agent 系统与后续研究的基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI agents that integrate large language models with non-AI tool components are rapidly emerging in real-world applications, offering unprecedented automation and flexibility. However, this flexibility introduces complex security challenges that differ from traditional software systems. In this paper, we present the first comprehensive systematization of knowledge on AI agent security, analyzing the design space, attack landscape, and defense mechanisms for secure AI agent systems. In addition, we identify open challenges for future research in this emerging domain. Our work provides the first systematic framework for understanding AI agent security risks and defense strategies, serving as a foundation for building secure agentic systems and advancing research in this critical area.

</details>

### 10. A Survey on Value Alignment in Agentic AI Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/SV146.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=survey-track)　📅 2026

**关键词**：`survey`、`agentic AI`、`value alignment`、`multi-agent coordination`

- 🎯 **研究动机**：agentic AI 的价值失配带来情境化风险，价值对齐缺乏跨层框架
- 🔬 **研究方法**：构建 L0 普世价值、L1 文化行业价值、L2 情境价值的多层框架，沿技术栈分析：LLM 层的预训练／后训练价值注入、单 Agent 层的 profile 记忆与规划行动、多 Agent 层的通信优化与多目标 RL 协同对齐
- 📌 **结论**：系统梳理多层对齐评测数据集与方法，提出 Agent 间价值协调、高质量场景数据共享与博弈论协议对齐等未来方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the evolution of artificial intelligence (AI) paradigms towards agentic AI, the widespread integration of large language models (LLMs) enhances system capabilities while also introducing situational risks and challenges of value misalignment, making value alignment in agentic AI systems a critical issue. This paper constructs a multi-level value framework encompassing L0 (universal values), L1 (cultural and industry values), and L2 (context-specific values). Guided by this framework, we conduct an in-depth analysis along the technical stack: at the LLM level, we examine value injection mechanisms through pretraining and post-training; at the single-agent level, we focus on representation and injecting values to agents, Profiles and memory, and planning and action; at the multi-agent level, we summarize collaborative alignment methods such as communication strategy optimization and multiobjective reinforcement learning. Following a systematic review of existing datasets and methods for multi-level alignment evaluation, we outline future research directions, including inter-agent value coordination mechanisms, high-quality scenario data sharing, game-theoretic design for value alignment in agent interaction and communication protocol alignment—aiming to establish a more systematic and dynamic evaluation framework and to promote robust and trustworthy value consensus in agentic AI systems within social collaboration.

</details>

### 11. TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21126)　📅 2026-08

**关键词**：`defense`、`task-effect contract`、`delegated authority`、`lifecycle governance`、`contract-governed guardrail`、`authority boundary`

👤 **作者**：Bohao Liao、Jingchao Wang、Qipeng Song、Jin Cao、Jieling Wang、Boyu Deng

- 🎯 **研究动机**：联网 Agent 任务内容可夹带间接 prompt injection 重定向工具或篡改参数，现有防御只约束不可信内容或单次调用，用户意图、运行时证据与实际效果间缺乏闭环
- 🔬 **研究方法**：TraceGrant 以显式 Contract 治理任务效果生命周期：执行前从可信用户请求建立 task-effect 边界，执行中证据只能实例化 Contract 已确立的权限，执行后按实际工具结果验证任务完成
- 📌 **结论**：949 个 AgentDojo 与 400 个 Agent Security Bench 攻击案例中零攻击成功，攻击下效用保留率分别为 77.32% 与 83.00%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidence, realized effects, and task completion insufficiently connected. We present TraceGrant, a security framework that governs the task-effect lifecycle of networked LLM agents through an explicit Contract. Before execution, TraceGrant establishes a task-effect boundary from the trusted user request. During execution, admitted evidence can instantiate only authority already established by the Contract. After execution, task completion is verified against actual tool results. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed benchmark settings, TraceGrant recorded no attack successes while retaining utility under attack rates of 77.32% and 83.00%, respectively. We further evaluate TraceGrant through white-box defense-aware attacks, Contract quality analysis, stage ablations, targeted stress tests, and runtime overhead measurements. The results show that TraceGrant provides a unified governance layer that connects trusted user intent, runtime evidence, concrete tool execution, and verified task completion.

</details>

### 12. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.27141)　📅 2026-08

**关键词**：`analysis`、`defense`、`monitor composition`、`cross-iteration state`、`safety bound`、`cross-iteration guard`

👤 **作者**：Chenhao Wu、…、Bin Chong

- 🎯 **研究动机**：自主 Agent 循环的安全监控以单轨迹为作用域、安全状态逐轨迹重置，而攻击证据可碎片化分散在多次迭代中
- 🔬 **研究方法**：证明任何 trajectory-scoped monitor 对此类攻击的真阳性率等于假阳性率，几何衰减风险分数也不够；提出 LoopHarness，在循环层维护持久不衰减安全状态并以 mediated commit 提交
- 📌 **结论**：在 arbiter 检测下界 δ_M 下，未授权不可逆动作的期望数量被约束为与迭代 horizon N 无关的常数 B+m-1+m/δ_M

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central result is a separation: against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate, however expressive it is, because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. We further show that the obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon $N$. We then present LoopHarness, which restores a persistent, non-decaying safety state at the loop level. Under mediated commits and an arbiter detection floor $δ_M$, it bounds the expected number of unauthorized irreversible actions by $B+m-1+m/δ_M$, a constant in $N$, of which the $B+m-1$ term is decided by a model-free rule and therefore survives a fully colluding verifier. We give a complete evaluation protocol on native Agent-SafetyBench tasks with paired clean and attacked episodes, an outer-state attack suite whose decisive evidence exists only across iterations, per-module ablations, and an adaptive white-box red team.

</details>

### 13. A Framework for Formalizing LLM Agent Security

📄 [arXiv](https://arxiv.org/abs/2603.19469)　📅 2026-03

**关键词**：`analysis`、`contextual security`、`authorization oracle`、`data isolation`

👤 **作者**：Vincent Siu、…、Dawn Song

- 🎯 **研究动机**：agent 安全本质上下文相关：同一动作随指令来源与目标不同可合法可违规，现有攻击定义未刻画
- 🔬 **研究方法**：提出 task alignment、action alignment、source authorization、data isolation 四属性与对应 oracle 函数，把间接注入、越狱、任务漂移、记忆投毒统一重述为属性违反
- 📌 **结论**：为攻击与防御提供精确的上下文相关定义：防御即强化 oracle 或执行安全属性检查

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Security in LLM agents is inherently contextual. For example, the same action taken by an agent may represent legitimate behavior or a security violation depending on whose instruction led to the action, what objective is being pursued, and whether the action serves that objective. However, existing definitions of security attacks against LLM agents often fail to capture this contextual nature. As a result, defenses face a fundamental utility-security tradeoff: applying defenses uniformly across all contexts can lead to significant utility loss, while applying defenses in insufficient or inappropriate contexts can result in security vulnerabilities. In this work, we present a framework that systematizes existing attacks and defenses from the perspective of contextual security. To this end, we propose four security properties that capture contextual security for LLM agents: task alignment (pursuing authorized objectives), action alignment (individual actions serving those objectives), source authorization (executing commands from authenticated sources), and data isolation (ensuring information flows respect privilege boundaries). We further introduce a set of oracle functions that enable verification of whether these security properties are violated as an agent executes a user task. Using this framework, we reformalize existing attacks, such as indirect prompt injection, direct prompt injection, jailbreak, task drift, and memory poisoning, as violations of one or more security properties, thereby providing precise and contextual definitions of these attacks. Similarly, we reformalize defenses as mechanisms that strengthen oracle functions or perform security property checks. Finally, we discuss several important future research directions enabled by our framework.

</details>

### 14. ATAG: AI-Agent Application Threat Assessment with Attack Graphs

📄 [arXiv](https://arxiv.org/abs/2506.02859) · 🌐 [Project](https://doi.org/10.1145/3779208.3785380)　📅 2025-06　🏷 ACM CCS 2026

**关键词**：`analysis`、`multi-agent threat model`、`attack graph`、`risk prioritization`、`framework`、`multi-agent security`

👤 **作者**：Parth Atulbhai Gandhi、…、Asaf Shabtai

- 🎯 **研究动机**：传统攻击图方法缺乏建模 LLM 攻击的能力，多智能体应用安全评估困难
- 🔬 **研究方法**：提出 ATAG，以自定义事实与交互规则扩展 MulVAL 逻辑攻击图工具，并建立 LLM 漏洞数据库 LVD
- 📌 **结论**：两个多智能体应用成功建模 prompt 注入、过度授权、信息泄露等多步攻击路径，支持威胁可视化与优先级排序

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluating the security of multi-agent systems (MASs) powered by large language models (LLMs) is challenging, primarily because of the systems' complex internal dynamics and the evolving nature of LLM vulnerabilities. Traditional attack graph (AG) methods often lack the specific capabilities to model attacks on LLMs. This paper introduces AI-agent application Threat assessment with Attack Graphs (ATAG), a novel framework designed to systematically analyze the security risks associated with AI-agent applications. ATAG extends the MulVAL logic-based AG generation tool with custom facts and interaction rules to accurately represent AI-agent topologies, vulnerabilities, and attack scenarios. As part of this research, we also created the LLM vulnerability database (LVD) to initiate the process of standardizing LLM vulnerabilities documentation. To demonstrate ATAG's efficacy, we applied it to two multi-agent applications. Our case studies demonstrated the framework's ability to model and generate AGs for sophisticated, multi-step attack scenarios exploiting vulnerabilities such as prompt injection, excessive agency, sensitive information disclosure, and insecure output handling across interconnected agents. ATAG is an important step toward a robust methodology and toolset to help understand, visualize, and prioritize complex attack paths in multi-agent AI systems (MAASs). It facilitates proactive identification and mitigation of AI-agent threats in multi-agent applications.

</details>

### 15. Reframing LLM Agent Security as an Agent-Human Interaction Problem

📄 [arXiv](https://arxiv.org/abs/2605.24309)　📅 2026-05

**关键词**：`analysis`、`human oversight`、`deployment gap`、`approval fatigue`

👤 **作者**：Peiran Wang、Ying Li、Yuan Tian

- 🎯 **研究动机**：Agent 安全被当作纯算法问题，而业界实际部署的是人机交互机制， academia 与产业脱节
- 🔬 **研究方法**：系统分析 59 篇学术论文、21 个生产 agent 系统与 26 个安全插件
- 📌 **结论**：策略指定、运行时审批与范围配置各被至少 14/21 系统采用，而学术界重点研究的意图锚定与信任标注零部署；人机机制陷入认知负担与安全保证的根本权衡，主张 AHI 安全成为一等研究方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We argue that LLM agent security is fundamentally an agent-human interaction (AHI) problem, not a purely algorithmic one. To substantiate this position, we conduct a systematic analysis of 59 academic papers, 21 production agent systems, and 26 security plugins as of April 2026. Our analysis reveals a striking pattern: the three widely deployed human-centric security mechanisms (policy specification, runtime approval, and scope configuration) dominate industry practice, each adopted by at least 14 of 21 systems (14, 15, and 16, respectively), while the categories most heavily studied in academia (intent anchoring and trust labeling) see zero production deployment. Yet current human participation mechanisms are far from satisfactory: they suffer from a fundamental trade-off between cognitive burden and security guarantees, leaving users caught between approval fatigue and uncontrolled agent autonomy. We make three contributions. First, through a systematic comparison of LLM-based and human-based intent alignment, we argue that human participation in agent security decisions is indispensable given current capabilities. Second, we quantify a pronounced industry-academia mismatch: the security mechanisms that practitioners actually deploy receive scant research attention, while the approaches that researchers favor remain undeployed. Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations.

</details>

### 16. SoK: Colluding Adversaries in Machine Learning Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.10091) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/duddu)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`survey`、`ML pipeline`、`colluding adversary`、`multi-agent system`、`composed attack`

👤 **作者**：Vasisht Duddu、Lipeng He、Asim Waheed、N. Asokan

- 🎯 **研究动机**：不同特征的对手可通过执行一种攻击放大另一种，但 ML 管线中的合谋缺乏系统框架
- 🔬 **研究方法**：提出覆盖训练期-推理期与推理期内部合谋的框架，纳入促成合谋的因素并给出推测指南，实证验证五个未探索合谋案例
- 📌 **结论**：用该框架解释已有工作、预测新合谋并验证成立；对手特征（目标、知识、能力）决定合谋潜力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) models are susceptible to various security, privacy, and fairness risks. Adversaries with different characteristics (i.e., objectives, knowledge, and capabilities) can collude by executing one attack to amplify others. Existing work lacks a systematic framework to explore collusion among adversaries, and to study the implications of the adversaries' characteristics. We present a framework covering collusion (a) between train- and inference-time adversaries, and (b) among inference-time adversaries. Our framework accounts for factors enabling collusion between adversaries. We propose a guideline to conjecture about the potential for collusion using enabling factors. We use it to explain prior work, conjecture about unexplored collusions, and empirically validate five such cases. Finally, we discuss how adversaries' characteristics influence the potential for collusion.

</details>
