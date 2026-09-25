# Agent 与多 Agent DoS

## 研究方向

Agent 与多 Agent DoS 研究自主系统中特有的资源生命周期和控制流风险。攻击者可以污染第三方 skill、工具描述、外部文档、GUI 触发器或 Agent 间消息，使系统反复规划、调用工具、错误判断任务尚未结束，或把递归指令沿协作拓扑传播；其危害需要用步骤数、工具调用、总 token、任务完成率和共享基础设施延迟共同衡量。

## 研究脉络

- **攻击起点：** 早期 Agent DoS 主要通过单次长输出放大推理成本。
- **攻击面扩展：** 研究随后覆盖 tool-call chain、termination condition、skill routing 和 guardrail loop，利用 Agent 的自主执行过程持续消耗资源。
- **系统化评测：** 在多 Agent 与共享基础设施中，局部资源放大会继续传播，因此研究开始引入生命周期 fuzzing 和漏洞检测。

## 循环、工具链与 Guardrail 攻击

### 1. SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

📄 [arXiv](https://arxiv.org/abs/2608.21929)　📅 2026-08

**关键词**：`attack`、`coding agent`、`skill injection`、`resource amplification`、`token amplification`、`resource abuse`

👤 **作者**：Yuanjin Zheng、Jingbang Chen

- 🎯 **研究动机**：coding agent 把已安装 skill 当可信指令通道，可被滥用于安全攻击之外的经济性资源滥用：诱导 agent 消耗远超任务所需的 token
- 🔬 **研究方法**：SkillBloat 两阶段攻击：先跨多种放大机制筛选攻击类型条件，再用 LLM 引导的全文 skill 重写精炼最强候选，在真实 skill benchmark 与多种 coding-agent 配置上评估
- 📌 **结论**：平均最佳 token 放大达 5.4184–10.1455 倍，二阶段精炼稳定优于一阶段；该 token amplification 攻击面与既有 skill poisoning 正交

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of diverse attack-type conditions across multiple amplification mechanisms and then refines the strongest candidate through LLM-guided full-document skill rewriting. Evaluated on a real-world skill benchmark, SkillBloat achieves 5.4184x-10.1455x average best amplification across multiple coding-agent target configurations. An ablation shows that the second-stage refinement loop consistently improves average best amplification over Phase 1 attack-type screening alone, demonstrating that iterative optimization provides additional benefit beyond initial attack-type selection. These results show that skill ecosystems expose a practical resource-amplification attack surface that is orthogonal to existing security-oriented skill poisoning.

</details>

### 2. Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.12273)　📅 2026-08

**关键词**：`attack`、`tool-using agent DoS`、`third-party skill`、`path hijacking`、`description steering`、`planning detour`

👤 **作者**：Junliang Liu、…、Laizhong Cui

- 🎯 **研究动机**：第三方技能的描述与指令体是两个顺序控制点，选段操纵与工具链资源放大被割裂研究，端到端组合 unclear
- 🔬 **研究方法**：Convergent Detour Hijacking 纯文本攻击：描述建立相关性、指令体复用该理由伪造依赖，吸引攻击者协调者并招募良性技能走有界弯路后回到原路线保任务完成
- 📌 **结论**：DeepSeek-V4-Pro 上协调者被 80.02% 任务选中；被命中的完成任务运行 token 消耗增 66.91%、执行时间增 92.45%，而任务完成率相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly rely on third-party skills, using natural-language descriptions for selection and instruction bodies for planning. This progressive-disclosure design exposes two sequential control points to untrusted publishers: a static skill may steer an otherwise correct task onto an unnecessarily costly trajectory. Prior work studies selection manipulation, malicious skill instructions, and tool-chain resource amplification largely separately, leaving their end-to-end composition unclear. We introduce Convergent Detour Hijacking (CDH), a text-only, runtime-independent attack that couples these stages. Under shared semantic cover, a description establishes relevance during selection, while an aligned body reuses that rationale to fabricate plausible dependencies during planning. CDH attracts an attacker-controlled coordinator alongside legitimate skills, recruits unnecessary benign skills into a bounded detour, and then re-enters the original route to preserve task completion. We evaluate it across multiple LLM backends and 491 held-out tasks under single-task and multi-turn conditions. On DeepSeek-V4-Pro, the matched coordinator is selected in 80.02% of tasks; among coordinator-hit runs that complete tasks, token consumption and end-to-end execution time increase by 66.91% and 92.45%, respectively, while aggregate task completion remains comparable. Thus, correct outcomes do not guarantee trajectory integrity or cost safety.

</details>

### 3. From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails

📄 [arXiv](https://arxiv.org/abs/2606.14517)　📅 2026-06

**关键词**：`attack`、`agent-guardrail DoS`、`agent defense`、`reasoning loop`

👤 **作者**：Yuguang Zhou、Xunguang Wang、Pingchuan Ma、Zhantong Xue、Zhaoyu Wang、Shuai Wang

- 🎯 **研究动机**：护栏的推理与任务执行能力本身成为新漏洞：注入数据可把护栏拖入超长推理循环造成 DoS
- 🔬 **研究方法**：设计 beam-search 框架（LLM proposer+策略库）最大化护栏推理长度，并基于 schema-following 特性给出机制感知结构变异的低成本攻击
- 📌 **结论**：单代理上优化的 payload 迁移到八个主流 backbone（Claude、GPT、Gemini 等）实现 13-63 倍 token 放大；真实 agent 部署中延迟放大最高 148 倍，单个污染文档即可瘫痪共享护栏基础设施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is systematically evaluated in two parts. First, in standalone evaluations, the attack generalizes across diverse guardrail architectures, safety templates, and agent benchmarks. Payloads optimized on a single open-source surrogate successfully transfer to eight leading model backbones (e.g., Claude, GPT, Gemini, DeepSeek, and Qwen), achieving a 13--63$\times$ token amplification. Second, in end-to-end real-world agent deployments (web, desktop, code, and multi-agent systems), the attack reveals up to a 148$\times$ latency amplification. We show that a single poisoned document can saturate shared guardrail infrastructures, effectively starving co-located agents and paralyzing the entire system. By uncovering this availability flaw, our work underscores the urgent need to develop cost-bounded, reasoning-robust guardrails.

</details>

### 4. Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection

📄 [arXiv](https://arxiv.org/abs/2605.11442)　📅 2026-05

**关键词**：`attack`、`multi-agent DoS`、`semantic closure`、`recursive invocation`

👤 **作者**：Zi Liang、Ronghua Li、Yanyun Wang、Qingqing Ye、Haibo Hu

- 🎯 **研究动机**：agent 作为用户-服务链路的枢纽可被武器化为 DDoS 节点，该系统性风险被忽视
- 🔬 **研究方法**：Mobius Injection 利用 agentic 逻辑的 Semantic Closure 结构漏洞，单条文本注入诱导组件持续递归执行；在 3 个 claw 类 agent、3 个编码 agent、12 个 LLM 上验证，并提出 ACE 组件能量分析防御
- 📌 **结论**：单节点调用最高放大 51.0 倍、多节点 p95 延迟放大 229.1 倍，随投毒节点数超线性增长，且能躲避传统 DDoS 监控与 AI 安全过滤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM) agents have emerged as key intermediaries, orchestrating complex interactions between human users and a wide range of digital services and LLM infrastructures. While prior research has extensively examined the security of LLMs and agents in isolation, the systemic risk of the agent acting as a disruptive hub within the user-agent-service chain remains largely overlooked. In this work, we expose a novel threat paradigm by introducing Mobius Injection, a sophisticated attack that weaponizes autonomous agents into zombie nodes to launch what we define as gent-based and -Oriented DDoS (AbO-DDoS) attacks. By exploiting a structural vulnerability in agentic logic named Semantic Closure, an adversary can induce sustained recursive execution of agent components through a single textual injection. We demonstrate that this attack is exceptionally lightweight, stealthy against both traditional DDoS monitors and contemporary AI safety filters, and highly configurable, allowing for surgical targeting of specific environments or model providers. To evaluate the real-world impact, we conduct extensive experiments across three representative claw-style agents and three mainstream coding agents, integrated with 12 frontier proprietary or open-weight LLMs. Our results demonstrate that Mobius Injection achieves substantial attack success across diverse tasks, driving single-node call amplification up to 51.0x and multi-node p95 latency inflation up to 229.1x. The attack performance exhibits a superlinear increase with the number of poisoning nodes. To mitigate Mobius Injection, we propose a proactive defense mechanism using Agent Component Energy (ACE) Analysis, which detects malicious recursive triggers by measuring anomalous energy in the agent's component graph.

</details>

### 5. LoopTrap: Termination Poisoning Attacks on LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.05846)　📅 2026-05

**关键词**：`attack`、`LLM-agent DoS`、`termination poisoning`、`behavioral profiling`

👤 **作者**：Huiyu Xu、…、Chun Chen

- 🎯 **研究动机**：LLM agent 迭代执行环中自主判断任务完成，终止判断本身构成攻击面
- 🔬 **研究方法**：定义 Termination Poisoning 并设计 10 种攻击策略；LoopTrap 先沿四个脆弱维度给目标 agent 建行为画像，再自适应合成陷阱并沉淀为可复用技能库
- 📌 **结论**：8 个主流 agent 上平均步骤放大 3.57 倍、峰值 25 倍；行为签名可迁移指导对未见 agent 的攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern LLM agents solve complex tasks by operating in iterative execution loops, where they repeatedly reason, act, and self-evaluate progress to determine when a task is complete. In this work, we show that while this self-directed loop facilitates autonomy, it also introduces a critical risk: by injecting malicious prompts into the agent's context, an adversary can distort the agent's termination judgment, making it believe the task remains incomplete and leading to unbounded computation.To understand this threat, we define and systematically characterize it as Termination Poisoning and design 10 representative attack strategies. Through a empirical study spanning 8 LLM agents and 60 tasks, we demonstrate that different LLM agents exhibit distinct behavioral signatures that determine which strategies succeed. These transferable patterns can serve as principled guidance for crafting effective attacks against previously unseen agents and tasks, enabling scalable red-teaming beyond manually designed templates. Building on these insights, we introduce LoopTrap, an automated red-teaming framework that synthesizes target-specific malicious prompts by exploiting agent behavioral tendencies. LoopTrap first constructs a behavioral profile of the target agent along four vulnerability dimensions via lightweight probing. It then performs adaptive trap synthesis, routing to the most effective strategy and selecting optimal injections via a self-scoring mechanism. Finally, successful traps are abstracted into a reusable skill library, while failed attempts are refined through self-reflection, ensuring continuous improvement. Extensive evaluation shows that LoopTrap achieves an average of 3.57$\times$ step amplification across 8 mainstream agents, with a peak of 25$\times$.

</details>

### 6. Sponge Tool Attack: Stealthy Denial-of-Efficiency against Tool-Augmented Agentic Reasoning

📄 [arXiv](https://arxiv.org/abs/2601.17566) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62486)　📅 2026-01　🏷 ICML 2026

**关键词**：`attack`、`tool-using agent DoS`、`tool use`、`prompt rewriting`、`LLM agent security`、`empirical evaluation`

👤 **作者**：Qi Li、Xinchao Wang

- 🎯 **研究动机**：工具增强 agent 推理中工具调用过程被恶意操纵的脆弱性未被探索
- 🔬 **研究方法**：Sponge Tool Attack 在仅查询访问假设下只改写输入 prompt，以迭代多 agent 协作框架与显式改写策略控制，把简洁推理轨迹变为冗长绕路轨迹而不改变任务语义与用户意图
- 📌 **结论**：在 6 个模型、12 个工具、4 个框架与 13 个数据集上验证有效，隐蔽地造成大量计算开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Enabling large language models (LLMs) to solve complex reasoning tasks is a key step toward artificial general intelligence. Recent work augments LLMs with external tools to enable agentic reasoning, achieving high utility and efficiency in a plug-and-play manner. However, the inherent vulnerabilities of such methods to malicious manipulation of the tool-calling process remain largely unexplored. In this work, we identify a tool-specific attack surface and propose Sponge Tool Attack (STA), which disrupts agentic reasoning solely by rewriting the input prompt under a strict query-only access assumption. Without any modification on the underlying model or the external tools, STA converts originally concise and efficient reasoning trajectories into unnecessarily verbose and convoluted ones before arriving at the final answer. This results in substantial computational overhead while remaining stealthy by preserving the original task semantics and user intent. To achieve this, we design STA as an iterative, multi-agent collaborative framework with explicit rewritten policy control, and generates benign-looking prompt rewrites from the original one with high semantic fidelity. Extensive experiments across 6 models (including both open-source models and closed-source APIs), 12 tools, 4 agentic frameworks, and 13 datasets spanning 5 domains validate the effectiveness of STA.

</details>

### 7. Beyond Max Tokens: Stealthy Resource Amplification via Tool Calling Chains in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2601.10955)　📅 2026-01

**关键词**：`attack`、`tool-using agent DoS`、`MCP tool`、`call chain`

👤 **作者**：Kaiyu Zhou、…、Kwok-Yan Lam

- 🎯 **研究动机**：现有 DoS 攻击限于用户 prompt 或 RAG 层且单轮，成本放大与隐蔽性受限
- 🔬 **研究方法**：在 MCP 工具层实施多轮经济 DoS：恶意服务器只改文本可见字段与模板化返回策略，引导 agent 陷入冗长调用链，并用 MCTS 在任务成功约束下最大化成本
- 📌 **结论**：六个 LLM 上轨迹超 60K token，单查询成本最高放大 658 倍、能耗 100-560 倍，标准 prompt 过滤与轨迹监控几乎检不出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The agent--tool interaction loop is a critical attack surface for modern Large Language Model (LLM) agents. Existing denial-of-service (DoS) attacks typically function at the user-prompt or retrieval-augmented generation (RAG) context layer and are inherently single-turn in nature. This limitation restricts cost amplification and diminishes stealth in goal-oriented workflows. To address these issues, we proposed a stealthy, multi-turn economic DoS attack at the tool layer under the Model Context Protocol (MCP). By simply editing text-visible fields and implementing a template-driven return policy, our malicious server preserves function signatures and the terminal benign payload while steering agents into prolonged, verbose tool-calling chains. We optimize these text-only edits with Monte Carlo Tree Search (MCTS) to maximize cost under a task-success constraint. Across six LLMs on ToolBench and BFCL benchmarks, our attack yields trajectories over 60K tokens, increases per-query cost by up to 658 times, raises energy by 100 to 560 times, and pushes GPU key-value (KV) cache occupancy to 35--74%. Standard prompt filters and output trajectory monitors seldom detect these attacks, highlighting the need for defenses that safeguard agentic processes rather than focusing solely on final outcomes. We will release the code soon.

</details>

### 8. When Efficiency Becomes a Vulnerability: Computational Cost Attacks on WebAgents

🎓 [Official](https://aclanthology.org/2026.acl-long.1775/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`cyber misuse`、`agent DoS`、`tool loop`、`agent safety`、`LLM agent`

👤 **作者**：Liang-Bo Ning、…、Wenqi Fan

- 🎯 **研究动机**：WebAgents 的计算效率脆弱性少有关注：网页注入恶意 prompt 可诱发冗长推理造成过量计算成本
- 🔬 **研究方法**：提出 CostBomb 生成-选择框架：LLM 生成多样对抗 prompt，强化学习增强的选择器识别最有效扰动，系统研究黑盒计算成本攻击
- 📌 **结论**：多个真实 web 基准上 WebAgents 计算成本大幅上升且任务完成不受影响，凸显效率感知防御的必要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

WebAgents have demonstrated strong capabilities in autonomously completing complex web tasks, yet their computational efficiency vulnerabilities have received limited attention. Adversaries can inject malicious prompts into web pages, causing WebAgents to generate unnecessarily long reasoning processes and incur excessive computational cost, termed Computational Cost Attacks (CCA). In this paper, to systematically study this vulnerability under realistic black-box settings, we propose CostBomb, a generation-then-selection attack framework that leverages large language models to generate diverse adversarial prompts and a reinforcement learning–enhanced selector to identify the most effective perturbations. Extensive experiments on multiple real-world web benchmarks reveal that existing WebAgents are highly vulnerable to CCA, suffering substantial increases in computational cost without compromising successful task completion. Our findings highlight an overlooked dimension of WebAgent robustness and underscore the urgent need for efficiency-aware defenses.

</details>

### 9. Mind the Web: The Security of Web Use Agents

📄 [arXiv](https://arxiv.org/abs/2506.07153) · 🌐 [Project](https://doi.org/10.1145/3779208.3805968)　📅 2025-06　🏷 ACM CCS 2026

**关键词**：`attack`、`browser harness`、`inherited privilege`、`execution constraint`、`web-use agent`、`indirect prompt injection`

👤 **作者**：Avishag Shapira、Parth Atulbhai Gandhi、Edan Habler、Asaf Shabtai

- 🎯 **研究动机**：web-use agent 的广泛浏览器能力带来未被探索的攻击面，网页中的恶意内容可劫持任务执行
- 🔬 **研究方法**：提出 task-aligned injection 把恶意指令伪装成任务引导，构建三阶段自动管线训练注入生成器，按 CIA 三元组组织载荷
- 📌 **结论**：五个 agent 上 ASR 超 80% 且跨载荷、环境与底层 LLM 强迁移，仅需在公开网站发帖即可攻破含内置安全机制的 agent

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-use agents are rapidly being deployed to automate complex web tasks with extensive browser capabilities. However, these capabilities create a critical and previously unexplored attack surface. This paper demonstrates how attackers can exploit web-use agents by embedding malicious content in web pages, such as comments, reviews, or advertisements, that agents encounter during legitimate browsing tasks. We introduce the task-aligned injection technique that frames malicious commands as helpful task guidance rather than obvious attacks, exploiting fundamental limitations in LLMs' contextual reasoning. Agents struggle to maintain coherent contextual awareness and fail to detect when seemingly helpful web content contains steering attempts that deviate them from their original task goal. To scale this attack, we developed an automated three-stage pipeline that generates effective injections without manual annotation or costly online agent interactions during training, remaining efficient even with limited training data. This pipeline produces a generator model that we evaluate on five popular agents using payloads organized by the Confidentiality-Integrity-Availability (CIA) security triad, including unauthorized camera activation, file exfiltration, user impersonation, phishing, and denial-of-service. This generator achieves over 80% attack success rate (ASR) with strong transferability across unseen payloads, diverse web environments, and different underlying LLMs. This attack succeed even against agents with built-in safety mechanisms, requiring only the ability to post content on public websites. To address this risk, we propose comprehensive mitigation strategies including oversight mechanisms, execution constraints, and task-aware reasoning techniques.

</details>

### 10. SlowBA: An efficiency backdoor attack towards VLM-based GUI agents

📄 [arXiv](https://arxiv.org/abs/2603.08316) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5078)　📅 2026-03　🏷 ECCV 2026

**关键词**：`attack`、`GUI-agent DoS`、`efficiency backdoor`、`popup trigger`、`GUI agent`、`resource exhaustion`

👤 **作者**：Junxian Li、Tu Lan、Haozhen Tan、Yan Meng、Haojin Zhu

- 🎯 **研究动机**：GUI agent 安全研究只关注动作正确性，响应效率维度的风险未被探索
- 🔬 **研究方法**：SlowBA 两阶段奖励级后门注入：先对齐长回复格式，再经 RL 学触发感知激活；用 GUI 环境中自然出现的弹窗作隐蔽触发器
- 📌 **结论**：显著拉长回复与延迟而基本保持任务准确率，低投毒率与多种防御设定下攻击仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern vision-language-model (VLM) based graphical user interface (GUI) agents are expected not only to execute actions accurately but also to respond to user instructions with low latency. While existing research on GUI-agent security mainly focuses on manipulating action correctness, the security risks related to response efficiency remain largely unexplored. In this paper, we introduce SlowBA, a novel backdoor attack that targets the responsiveness of VLM-based GUI agents. The key idea is to manipulate response latency by inducing excessively long reasoning chains under specific trigger patterns. To achieve this, we propose a two-stage reward-level backdoor injection (RBI) strategy that first aligns the long-response format and then learns trigger-aware activation through reinforcement learning. In addition, we design realistic pop-up windows as triggers that naturally appear in GUI environments, improving the stealthiness of the attack. Extensive experiments across multiple datasets and baselines demonstrate that SlowBA can significantly increase response length and latency while largely preserving task accuracy. The attack remains effective even with a small poisoning ratio and under several defense settings. These findings reveal a previously overlooked security vulnerability in GUI agents and highlight the need for defenses that consider both action correctness and response efficiency. Code can be found in https://github.com/tu-tuing/SlowBA.

</details>

### 11. CORBA: Contagious Recursive Blocking Attacks on Multi-Agent Systems Based on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.14529) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.342/)　📅 2025-02　🏷 ACL 2026

**关键词**：`attack`、`multi-agent DoS`、`recursive propagation`、`collaboration blocking`

👤 **作者**：Zhenhong Zhou、…、Qing Guo

- 🎯 **研究动机**：LLM-MAS 的协作结构缺乏针对其交互的破坏性攻击研究
- 🔬 **研究方法**：CORBA 用表面良性的传染性递归指令跨任意拓扑传播并持续耗尽计算资源、阻断协作
- 📌 **结论**：在 AutoGen、Camel 与开放式交互系统中均致系统瘫痪，常规对齐机制难防

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model-based Multi-Agent Systems (LLM-MASs) have demonstrated remarkable real-world capabilities, effectively collaborating to complete complex tasks. While these systems are designed with safety mechanisms, such as rejecting harmful instructions through alignment, their security remains largely unexplored. This gap leaves LLM-MASs vulnerable to targeted disruptions. In this paper, we introduce Contagious Recursive Blocking Attacks (Corba), a novel and simple yet highly effective attack that disrupts interactions between agents within an LLM-MAS. Corba leverages two key properties: its contagious nature allows it to propagate across arbitrary network topologies, while its recursive property enables sustained depletion of computational resources. Notably, these blocking attacks often involve seemingly benign instructions, making them particularly challenging to mitigate using conventional alignment methods. We evaluate Corba on two widely-used LLM-MASs, namely, AutoGen and Camel across various topologies and commercial models. Additionally, we conduct more extensive experiments in open-ended interactive LLM-MASs, demonstrating the effectiveness of Corba in complex topology structures and open-source models. Our code is available at: https://github.com/zhrli324/Corba.

</details>

### 12. Autonomy Comes with Costs: Detecting Denial-of-Service Vulnerabilities Caused by Resource Abusing in LLM-based Agents

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/luo)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`LLM-agent DoS`、`resource lifecycle`、`grey-box fuzzing`、`LLM agent`、`resource exhaustion`

👤 **作者**：Jiaqi Luo、…、Yuan Zhang

- 🎯 **研究动机**：LLM agent 缺乏资源治理，易被滥用导致资源耗尽与拒绝服务，此前无系统安全研究
- 🔬 **研究方法**：识别三种资源生命周期管理模式及各自 DoS 利用路径，提出定向灰盒模糊测试框架 AgentDoS：分析资源生命周期后用 LLM 生成功能特定自然语言种子提示驱动过度消耗
- 📌 **结论**：在 20 个开源 agent 中发现 36 个零日漏洞（影响 16 个 agent，其中 15 个 GitHub star 超 1 万），已获 15 个 CVE 编号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents have recently attracted significant attention. By leveraging the semantic understanding capabilities of large language models (LLMs), these agents can autonomously perform complex tasks according to user requests, such as downloading files and summarizing content. However, the lack of comprehensive resource governance renders them susceptible to abuse, potentially leading to resource exhaustion and denial-of-service (DoS) conditions. In this work, we present the first systematic security study of resource management in LLM-based agents. We identify three representative patterns of resource lifecycle management, each of which enables distinct avenues for DoS exploitation. Building on these insights, we propose AgentDoS, a novel directed grey-box fuzzing framework designed to detect DoS vulnerabilities arising from resource exhaustion. AgentDoS first analyzes the resource lifecycle within the agent and then leverages an LLM to generate functionality-specific seed prompts in natural language that drive the agent toward excessive resource consumption. We evaluated AgentDoS on 20 widely used open-source LLM-based agents and discovered 36 zero-day vulnerabilities affecting 16 agents, 15 of which have over 10,000 stars on GitHub. To date, 15 CVE IDs have been assigned for these vulnerabilities.

</details>

### 13. OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2605.08876) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61771)　📅 2026　🏷 ICML 2026

**关键词**：`tool`、`attack`、`agent DoS`、`tool loop`、`resource exhaustion`、`LLM jailbreak`

👤 **作者**：Xinyu Li、Ronghui Mu、Lin Li、Tianjin Huang、Gaojie Jin

- 🎯 **研究动机**：推理级 DoS 被忽视：攻击保持任务正确但膨胀智能体推理深度或工具预算以降低可用性
- 🔬 **研究方法**：OTora 两阶段：插入感知评分与动态目标共同进化优化对抗触发器（黑/白盒）；ICL 引导遗传搜索生成放大过度思考的推理载荷
- 📌 **结论**：WebShop、Email 与 OS 智能体上推理 token 最多增 10 倍、延迟数量级放缓，任务准确率保持近基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed as autonomous agents that execute tool-augmented, multi-step tasks, where latency is a critical factor for real-world applications. Yet an overlooked threat is Reasoning-Level Denial-of-Service (R-DoS), in which an attacker preserves task correctness but degrades availability by inflating an agent’s reasoning depth or tool-use budget. We introduce OTora, the first unified, two-stage red-teaming framework for instantiating R-DoS attacks. Stage I optimizes an adversarial trigger that induces targeted tool invocations using insertion-aware scoring and dynamic target co-evolution, supporting both black-box and white-box settings. Stage II generates agent-aware reasoning payloads via an ICL-guided genetic search that amplifies overthinking while maintaining correct task outcomes. Across WebShop, Email, and OS agents built on multiple backbone models such as LLaMA-70B and GPT-OSS-120B, OTora achieves up to 10× increases in reasoning tokens and order-of-magnitude latency slowdowns, all while preserving near-baseline task accuracy. Finally, we discuss mitigation strategies for detecting and constraining abnormal reasoning and latency spikes.

</details>

### 14. When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2607.01641)　📅 2026-07

**关键词**：`analysis`、`LLM-agent DoS`、`infinite agentic loop`、`static analysis`

👤 **作者**：Xinyi Hou、Shenao Wang、Yanjie Zhao、Haoyu Wang

- 🎯 **研究动机**：agent 迭代执行中反馈路径缺乏有效界定时形成 Infinite Agentic Loops，可把单请求放大为长时模型与工具执行
- 🔬 **研究方法**：IAL-Scan 静态分析工具：把异构 agent 代码抽象为框架无关 Agent IR，构建 Agentic Loop Dependence Graph 恢复显式与框架诱导的反馈路径，检查其能否无界抵达高开销或状态增长操作
- 📌 **结论**：扫描 6,549 个 LLM agent 仓库上报 74 个潜在发现，人工确认 47 个项目中的 68 个 IAL 失败，精度 91.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents increasingly rely on iterative execution to solve tasks through planning, tool use, state updates, and agent collaboration. While this design enables flexible automation, it also creates a new class of failures: an agent may repeatedly execute model calls, tools, workflow transitions, or agent handoffs when the feedback path is not effectively bounded. We call this problem Infinite Agentic Loops (IALs). IALs are not ordinary programming loops; they arise from the interaction between agent logic, framework semantics, runtime observations, and termination mechanisms. Such failures can amplify a single request into long running model and tool execution, causing cost exhaustion, model denial of service, context growth, and repeated external side effects. We propose IAL-Scan, a static analysis tool for detecting IAL failures in real-world LLM agent projects. IAL-Scan abstracts heterogeneous agent code into a framework independent Agent IR, builds an Agentic Loop Dependence Graph (ALDG) to recover explicit and framework induced feedback paths, and checks whether these paths can repeatedly reach costly or state growing operations without an effective bound. We evaluate IAL-Scan on 6,549 LLM agent repositories. It reports 74 potential findings, among which manual review confirms 68 IAL failures across 47 projects, achieving 91.9% precision.

</details>

### 15. Overthinking Loops in Agents: A Structural Risk via MCP Tools

📄 [arXiv](https://arxiv.org/abs/2602.14798)　📅 2026-02

**关键词**：`attack`、`LLM-agent DoS`、`MCP tool supply chain`、`structural overthinking`

👤 **作者**：Yohan Lee、Jisoo Jang、Seoyeon Choi、Sangyeop Kim、Seungtaek Choi

- 🎯 **研究动机**：恶意 MCP 工具服务器可与正常工具共同注册，文本可见元数据的便利构成供应链攻击面
- 🔬 **研究方法**：形式化 structural overthinking attack（区别于 token 级冗长）：实现 14 个跨三个服务器的恶意工具，使个别合理工具调用组成循环轨迹，触发重复、强制精炼与分心
- 📌 **结论**：异构注册表与多个工具模型上最高 142.4 倍 token 放大并可劣化任务结果；解码期简洁控制不能可靠阻止循环诱导，防御需面向工具调用结构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Tool-using LLM agents increasingly coordinate real workloads by selecting and chaining third-party tools based on text-visible metadata such as tool names, descriptions, and return messages. We show that this convenience creates a supply-chain attack surface: a malicious MCP tool server can be co-registered alongside normal tools and induce overthinking loops, where individually trivial or plausible tool calls compose into cyclic trajectories that inflate end-to-end tokens and latency without any single step looking abnormal. We formalize this as a structural overthinking attack, distinguishable from token-level verbosity, and implement 14 malicious tools across three servers that trigger repetition, forced refinement, and distraction. Across heterogeneous registries and multiple tool-capable models, the attack causes severe resource amplification (up to $142.4\times$ tokens) and can degrade task outcomes. Finally, we find that decoding-time concision controls do not reliably prevent loop induction, suggesting defenses should reason about tool-call structure rather than tokens alone.

</details>

### 16. Clawdrain: Exploiting Tool-Calling Chains for Stealthy Token Exhaustion in OpenClaw Agents

📄 [arXiv](https://arxiv.org/abs/2603.00902)　📅 2026-03

**关键词**：`attack`、`LLM-agent DoS`、`trojanized skill`、`token exhaustion`

👤 **作者**：Ben Dong、Hui Feng、Qian Wang

- 🎯 **研究动机**：OpenClaw 等自托管 generative agent 的社区技能生态扩张速度超过系统化安全评估
- 🔬 **研究方法**：Clawdrain 木马化技能经 SKILL.md 指令与伴随脚本建立多轮分段验证协议，返回 PROGRESS/REPAIR/TERMINAL 信号拖长工具链，并在生产级实例与真实 API 计费下部署测量
- 📌 **结论**：Gemini 2.5 Pro 上 6-7 倍 token 放大、失败配置约 9 倍；agent 自主组合 shell/Python 等通用工具绕行脆弱协议会降低放大并改变攻击动态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern generative agents such as OpenClaw - an open-source, self-hosted personal assistant with a community skill ecosystem, are gaining attention and are used pervasively. However, the openness and rapid growth of these ecosystems often outpace systematic security evaluation. In this paper, we design, implement, and evaluate Clawdrain, a Trojanized skill that induces a multi-turn "Segmented Verification Protocol" via injected SKILL.md instructions and a companion script that returns PROGRESS/REPAIR/TERMINAL signals. We deploy Clawdrain in a production-like OpenClaw instance with real API billing and a production model (Gemini 2.5 Pro), and we measure 6-7x token amplification over a benign baseline, with a costly, failure configuration reaching approximately 9x. We observe a deployment-only phenomenon: the agent autonomously composes general-purpose tools (e.g., shell/Python) to route around brittle protocol steps, reducing amplification and altering attack dynamics. Finally, we identify production vectors enabled by OpenClaw's architecture, including SKILL.md prompt bloat, persistent tool-output pollution, cron/heartbeat frequency amplification, and behavioral instruction injection. Overall, we demonstrate that token-drain attacks remain feasible in real deployments, but their magnitude and observability are shaped by tool composition, recovery behavior, and interface design.

</details>

### 17. LeechHijack: Covert Computational Resource Exploitation in Intelligent Agent Systems

📄 [arXiv](https://arxiv.org/abs/2512.02321)　📅 2025-12

**关键词**：`attack`、`LLM-agent DoS`、`implicit toxicity`、`compute hijacking`

👤 **作者**：Yuanhe Zhang、…、Sen Su

- 🎯 **研究动机**：MCP 对第三方工具提供者的隐式信任是被忽视的安全假设，恶意行为可以完全发生在显式权限范围内
- 🔬 **研究方法**：LeechHijack 形式化 implicit toxicity 攻击向量：植入阶段在工具中嵌入看似无害的后门，利用阶段经预定义触发建立命令控制通道，注入额外任务让 agent 当作正常工作流执行以寄生用户算力
- 📌 **结论**：四大 LLM 家族上平均成功率 77.25%、相对基线 18.62% 的资源开销，凸显计算溯源与资源证明机制的紧迫性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Model (LLM)-based agents have demonstrated remarkable capabilities in reasoning, planning, and tool usage. The recently proposed Model Context Protocol (MCP) has emerged as a unifying framework for integrating external tools into agent systems, enabling a thriving open ecosystem of community-built functionalities. However, the openness and composability that make MCP appealing also introduce a critical yet overlooked security assumption -- implicit trust in third-party tool providers. In this work, we identify and formalize a new class of attacks that exploit this trust boundary without violating explicit permissions. We term this new attack vector implicit toxicity, where malicious behaviors occur entirely within the allowed privilege scope. We propose LeechHijack, a Latent Embedded Exploit for Computation Hijacking, in which an adversarial MCP tool covertly expropriates the agent's computational resources for unauthorized workloads. LeechHijack operates through a two-stage mechanism: an implantation stage that embeds a benign-looking backdoor in a tool, and an exploitation stage where the backdoor activates upon predefined triggers to establish a command-and-control channel. Through this channel, the attacker injects additional tasks that the agent executes as if they were part of its normal workflow, effectively parasitizing the user's compute budget. We implement LeechHijack across four major LLM families. Experiments show that LeechHijack achieves an average success rate of 77.25%, with a resource overhead of 18.62% compared to the baseline. This study highlights the urgent need for computational provenance and resource attestation mechanisms to safeguard the emerging MCP ecosystem.

</details>

## 检测与防御

### 18. SHIELD: An Auto-Healing Agentic Defense Framework for LLM Resource Exhaustion Attacks

📄 [arXiv](https://arxiv.org/abs/2601.19174)　📅 2026-01

**关键词**：`defense`、`LLM DoS`、`agentic defense`、`auto-healing`

👤 **作者**：Nirhoshan Sivaroopan、…、Wangli Yang

- 🎯 **研究动机**：既有 sponge 攻击防御依赖统计滤波（漏掉语义攻击）或静态 LLM 检测器（难以适应演化攻击策略）
- 🔬 **研究方法**：SHIELD 多智能体自愈防御：三阶段 Defense Agent 整合语义相似检索、模式匹配与 LLM 推理，知识更新与 prompt 优化两个辅助 agent 在攻击绕过检测时更新知识库并精炼防御指令形成闭环
- 📌 **结论**：非语义与语义 sponge 攻击上 F1 持续超过困惑率与独立 LLM 防御，验证智能体自愈对演化型资源耗尽威胁的有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sponge attacks increasingly threaten LLM systems by inducing excessive computation and DoS. Existing defenses either rely on statistical filters that fail on semantically meaningful attacks or use static LLM-based detectors that struggle to adapt as attack strategies evolve. We introduce SHIELD, a multi-agent, auto-healing defense framework centered on a three-stage Defense Agent that integrates semantic similarity retrieval, pattern matching, and LLM-based reasoning. Two auxiliary agents, a Knowledge Updating Agent and a Prompt Optimization Agent, form a closed self-healing loop, when an attack bypasses detection, the system updates an evolving knowledgebase, and refines defense instructions. Extensive experiments show that SHIELD consistently outperforms perplexity-based and standalone LLM defenses, achieving high F1 scores across both non-semantic and semantic sponge attacks, demonstrating the effectiveness of agentic self-healing against evolving resource-exhaustion threats.

</details>

### 19. Agent-Fence: Mapping Security Vulnerabilities Across Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2602.07652) · 🎓 [Official](https://ojs.aaai.org/index.php/AAAI-SS/article/view/42945)　📅 2026-02　🏷 AAAI-SS 2026

**关键词**：`benchmark`、`deep research agent security`、`trust-boundary taxonomy`、`denial of wallet`、`MSBR`

👤 **作者**：Sai Puppala、Ismail Hossain、Md Jahangir Alam、Yoonpyo Lee、Jay Yoo、Tanzim Ahad、Syed Bahauddin Alam、Sajedul Talukder

- 🎯 **研究动机**：LLM 以自主 agent 形态部署后，安全失效从单条不安全文本转移到多步轨迹（规划、持久状态、外部工具调用），而既有评测多聚焦 prompt 层攻击，缺少对 deep research agent 架构级安全边界的系统测绘。
- 🔬 **研究方法**：AgentFence 定义 14 类信任边界攻击（覆盖 planning、memory、retrieval、tool use、delegation），以 trace-auditable conversation breaks（未授权工具使用、错误主体动作、状态/目标完整性违反、攻击关联偏移）检测失效；固定基座模型，在 8 种 agent 架构原型（LangGraph 到 AutoGPT）下做持久多轮交互测试，报告平均安全破坏率 MSBR 与失效构成。
- 📌 **结论**：MSBR 随架构差异巨大（LangGraph 0.29±0.04 到 AutoGPT 0.51±0.07）；风险最高的全是运营类——**Denial-of-Wallet 0.62±0.08**、Authorization Confusion 0.54、Retrieval Poisoning 0.47、Planning Manipulation 0.44，而 prompt 类攻击在标准设定下低于 0.20；边界违反主导失效构成（SIV 31%、WPA 27%、UTI+UTA 24%），授权混淆与目标劫持相关 ρ≈0.63——把 agent 安全重新定义为"是否随时间保持在目标与授权包络内"。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs are increasingly deployed as autonomous agents that plan, maintain persistent state, and invoke external tools, security failures shift from unsafe single outputs to unsafe multi-step trajectories. Existing evaluations largely focus on prompt-centric attacks, leaving the architectural trust boundaries of deep research agents unmapped. We present AgentFence, an architecture-focused security evaluation comprising 14 trust-boundary attack classes spanning planning, memory, retrieval, tool use, and delegation. Failures are detected via trace-auditable conversation breaks: unauthorized or unsafe tool use, wrong-principal actions, state and objective integrity violations, and attack-linked deviations. Holding the base model fixed, we evaluate eight agent archetypes under persistent multi-turn interaction. Mean security break rate (MSBR) varies widely by architecture, from 0.29 +/- 0.04 (LangGraph) to 0.51 +/- 0.07 (AutoGPT). The highest-risk classes are operational: Denial-of-Wallet (0.62 +/- 0.08), Authorization Confusion (0.54 +/- 0.10), Retrieval Poisoning (0.47 +/- 0.09), and Planning Manipulation (0.44 +/- 0.11); prompt-centric classes remain below 0.20 under standard settings. Boundary violations dominate the break composition (SIV 31%, WPA 27%, UTI+UTA 24%, ATD 18%), and authorization confusion correlates with objective hijacking (rho ~= 0.63) and tool hijacking (rho ~= 0.58). Our results reframe agent security around whether an agent remains within its goal and authority envelope over time.

</details>

### 20. Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents

📄 [arXiv](https://arxiv.org/abs/2609.28585)　📅 2026-09

**关键词**：`attack`、`denial-of-wallet`、`persistent billable state`、`tool-return metering`、`DOW-BENCH`

👤 **作者**：Jinqian Zhang、…、Bibo Tu

- 🎯 **研究动机**：多步工具调用 agent 依赖宿主 runtime 跨轮保持状态——外部工具返回被带入后续模型输入时提供方再次计费：被收编/恶意工具可把不可信数据转化为反复的受害者计费处理，无需受害者凭据或本地权限
- 🔬 **研究方法**：形式化持续计费状态边界；导出六个 denial-of-wallet 攻击向量并构建 DOW-BENCH 端到端 harness（六模型家族、243 次执行）；受控历史策略重放分离原始保留的贡献
- 📌 **结论**：单会话累计输入达首调的 14,293 倍——准入后生命周期的首个系统安全研究（agent 资源耗尽的计费语义通道，与 ChronosAttack 时序通道互补）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. When a runtime carries an external tool return into later model inputs, providers meter it again. An admitted malicious or compromised tool can thereby convert untrusted data into recurring victim-billed processing without victim credentials or local runtime privilege. We call retained content persistent billable state and formalize the host's decision over whether and how it enters later billable context as the persistent billable-state boundary. We present the first systematic security study of this post-admission lifecycle. We derive six denial-of-wallet attack vectors and build DOW-BENCH, an end-to-end harness evaluated across six model families. Across 243 executions, usage telemetry shows that the maximum per-session cumulative input reaches 14,293x the session's first-call input. Controlled history-policy reruns isolate raw retention's contribution: retaining raw history increases mean effective session cost by 21.2-35.9%. Compression succeeds on 10/12 and 11/12 history-dependent tasks, versus 2/12 under deletion for each provider. To govern this boundary, we combine deterministic history transformation with four host-side invariants that bound prompt mass, context growth, recursive opportunity, and cumulative spend before reingestion. The kernel contains every recurring attack in the 123-evaluation replay corpus. Across 24 Mistral Small 4 workflows, a progress-authorized policy achieves 22/24 oracle-verified task successes with no pre-completion interruptions, versus 13/24 under a fixed cap. Only 71 of 3,830 scanned MCP server and transport repositories expose any code-visible safeguard proxy, and none cover all four safeguard families. These results establish persistent billable state as a first-class security object and pre-reingestion as its host-owned control point.

</details>
