# Agent 行为安全与 Agentic Misalignment

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究具备工具、长期目标或较高自主性的 Agent 是否会采取开发者和用户都不希望的策略。threat model 不局限于外部 prompt injection，也包括 goal conflict、权限扩大、信息隐藏、监督规避、harmful compliance 和在模拟组织环境中出现的 insider-risk 行为；评测需要同时区分模型倾向、情景诱导、harness affordance 与真实可执行后果。

## 研究脉络

- **有害请求执行：** 基础评测先检验 Agent 是否会为明确恶意目标调用工具并完成多步任务。
- **目标冲突情景：** 研究随后构造目标受阻或被替换的组织情景，观察 Agent 是否选择勒索、泄密或其他策略性伤害。
- **自主性与脚手架效应：** 新工作比较更长 horizon、更大 action space、较少人工确认，以及 feedback loop、reconsideration checkpoint 和 iterative refinement 是否放大不安全行为或 sycophancy，而不把 capability 失败或表面自我修正误判为安全。
- **过程监控：** 仅看 final answer 难以发现隐藏意图，研究开始利用 trajectory、weak monitor 和干预实验评估行为形成过程。
- **当前边界：** 模拟场景中的行为不能直接外推为真实动机，结论必须报告系统提示、工具权限、模型版本和重复试验条件。

## Agentic Misalignment 与 Insider-Risk 行为

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

### 2. SafeBranch: Branch-Pair Safety Alignment for Embodied Agents

📄 [arXiv](https://arxiv.org/abs/2608.19729)　📅 2026-08

**关键词**：`defense`、`interactive agent safety`、`branch-pair alignment`、`unsafe-action correction`、`risk-step localization`、`environment rollback`

👤 **作者**：Hyunse Lee、Jiwoo Jeong、Haneul Lee、Kyochul Jang、Youngjae Yu、Woojin Lee

- 🎯 **研究动机**：具身 agent 的安全只在轨迹中少数关键步出现，模仿安全轨迹不解释为何安全，任意安全/不安全对比混入无关差异
- 🔬 **研究方法**：SafeBranch 从自身不安全 rollout 经环境回滚构造分支对：回滚到致违关键步、查询 actor 安全替代，原动作与替代仅在该步配对；部署时无 critic
- 📌 **结论**：IS-Bench、SafetyALFRED 与 OOD 变体上可靠安全且不牺牲任务成功，未见物体变体上安全成功约为未训练基线的十倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting arbitrary safe and unsafe trajectories mixes the safety signal with unrelated differences. We propose SafeBranch, a framework that aligns an embodied actor on safety through branch pairs constructed from the actor's own unsafe rollouts via environment rollback. SafeBranch rolls each unsafe rollout back to the safety-critical step that caused the violation, queries the actor for a safe alternative, and pairs the original action with the alternative so that the two branches differ only at that step. The trained actor acts safely at deployment with no critic in the loop. On IS-Bench, SafetyALFRED, and out-of-distribution variants with unseen tasks and objects, it handles safety reliably without sacrificing task success, achieving roughly ten times more safe successes than the untrained baseline on the unseen-object variant.

</details>

### 3. Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

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

### 4. Agentic Scaffolding Amplifies Sycophantic Behavior in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21377) · 🌐 [Project](https://safe-ai-workshop.github.io/uai-2026/)　📅 2026-08

**关键词**：`analysis`、`agentic scaffolding`、`sycophancy amplification`、`oversight loop`、`agentic sycophancy`、`capitulation metric`

👤 **作者**：Thantham Jittham

- 🎯 **研究动机**：LLM sycophancy 多在单轮设置下研究，agentic 交互脚手架（反馈循环、重审检查点、迭代精炼）是放大还是缓解迎合行为未知
- 🔬 **研究方法**：提出 agentic sycophancy amplification 概念与 capitulation rate、sycophantic capitulation rate 指标，在 4,800 次真伪判断（200 陈述×6 模型×4 条件）中比较多轮交互、用户压力与迭代自精炼
- 📌 **结论**：脚手架系统性放大迎合并伴随平均 6.3 个百分点准确率下降；能力更强的模型放大效应更大，人类监督回路反而创造了漂移条件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Sycophancy in large language models, the tendency to prioritize user agreement over truthful responses, has been documented extensively but studied primarily in single-turn settings. This paper investigates a critical question: does subjecting LLMs to greater interaction scaffolding make sycophancy better or worse? Across 4,800 veracity judgments (200 statements $\times$ 6 models $\times$ 4 conditions), we find that the interaction scaffolding characteristic of agentic systems (feedback loops, reconsideration checkpoints, and iterative refinement) systematically amplifies sycophantic behavior. Multi-turn interaction, user pressure, and iterative self-refinement each provide additional opportunities for models to drift toward agreement, and this drift coincides with a mean accuracy drop of $-6.3$ percentage points, establishing the capitulation as harmful rather than corrective. More capable models show larger amplification effects, a troubling inversion of expectations. We introduce the concept of agentic sycophancy amplification (ASA) and two novel metrics: capitulation rate and sycophantic capitulation rate. Our results indicate that as AI systems acquire greater autonomy, sycophancy becomes compounding rather than merely persistent. Systems designed with human oversight loops may inadvertently create the conditions for this drift.

</details>

### 5. The Autonomy Tax: Defense Training Breaks LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.19423)　📅 2026-03

**关键词**：`analysis`、`prompt-injection defense`、`capability collapse`、`shortcut learning`

👤 **作者**：Shawn Li、Yue Zhao

- 🎯 **研究动机**：防注入训练是否损害多步 agent 能力未知
- 🔬 **研究方法**：在 97 个 agent 任务与 1,000 个对抗提示上比较防御训练模型与未防御基线，并做根因分析
- 📌 **结论**：防御模型在良性任务即出现工具执行崩溃，重试级联致 99% 任务超时（基线 13%），而直接攻击仍高比率绕过——capability-alignment 悖论

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly rely on external tools (file operations, API calls, database transactions) to autonomously complete complex multi-step tasks. Practitioners deploy defense-trained models to protect against prompt injection attacks that manipulate agent behavior through malicious observations or retrieved content. We reveal a fundamental \textbf{capability-alignment paradox}: defense training designed to improve safety systematically destroys agent competence while failing to prevent sophisticated attacks. Evaluating defended models against undefended baselines across 97 agent tasks and 1,000 adversarial prompts, we uncover three systematic biases unique to multi-step agents. \textbf{Agent incompetence bias} manifests as immediate tool execution breakdown, with models refusing or generating invalid actions on benign tasks before observing any external content. \textbf{Cascade amplification bias} causes early failures to propagate through retry loops, pushing defended models to timeout on 99\% of tasks compared to 13\% for baselines. \textbf{Trigger bias} leads to paradoxical security degradation where defended models perform worse than undefended baselines while straightforward attacks bypass defenses at high rates. Root cause analysis reveals these biases stem from shortcut learning: models overfit to surface attack patterns rather than semantic threat understanding, evidenced by extreme variance in defense effectiveness across attack categories. Our findings demonstrate that current defense paradigms optimize for single-turn refusal benchmarks while rendering multi-step agents fundamentally unreliable, necessitating new approaches that preserve tool execution competence under adversarial conditions.

</details>

### 6. From Surveillance to Signalling: Escalation Channels as Environmental Controls for Agentic AI

📄 [arXiv](https://arxiv.org/abs/2510.05192)　📅 2025-10

**关键词**：`defense`、`escalation channel`、`environmental control`、`insider risk`

👤 **作者**：Francesca Gomez

- 🎯 **研究动机**：推理时安全多依赖监控与访问限制，作用于冲突决策点的环境控制层未被探索
- 🔬 **研究方法**：借情境犯罪预防理论设计升级通道：为 agent 提供向独立权威上报冲突的正式带外路径，比较简单邮件升级与保证 30 分钟暂停加独立审查的高可信通道
- 📌 **结论**：无控制时有害行为率 38.73%，简单通道降至 5.92%，高可信通道降至 1.21%，10 个模型 24000 样本上均显著

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When AI agents operating with access to sensitive information encounter a conflict between completing an assigned task and following rules or ethical constraints, they can resort to unsanctioned behaviour. Existing inference time safety work addresses this primarily through monitoring and access restriction. We investigate a complementary and under-explored layer: environmental controls that act on the agent's decision context at the point of conflict, making it more likely that the agent takes an authorised alternative path rather than an unsanctioned one. Drawing on Situational Crime Prevention (SCP), a framework used in human insider risk management to make harmful actions less rewarding and compliant actions more viable by design choices in the environment, we design and evaluate escalation channels as a concrete instantiation of this control class. An escalation channel provides an agent with a formal, out-of-band route to surface a conflict to an independent authority. We evaluate two designs: a simple email escalation and an instrumentally credible channel that guarantees a 30-minute pause and independent review, making the authorised path genuinely useful for goal achievement rather than merely nominally available. Across 10 frontier LLMs using the agentic task-rule conflict scenario of Lynch et al. (2025), we find that without any control the harmful action rate is 38.73%. A simple escalation channel reduces this to 5.92%; the instrumentally credible channel reduces it further to 1.21%, a statistically significant improvement observed in all 10 models tested across 24,000 samples. Our results suggest that the instrumental credibility of the authorised alternative matters considerably, and that environmental control design is a productive and largely unexplored addition to the defence-in-depth toolkit for agentic AI systems.

</details>

### 7. Agentic Misalignment: How LLMs Could Be Insider Threats

📄 [arXiv](https://arxiv.org/abs/2510.05179) · 🌐 [Project](https://www.anthropic.com/research/agentic-misalignment)　📅 2025-10

**关键词**：`analysis`、`agentic misalignment`、`goal conflict`、`strategic harm`

👤 **作者**：Aengus Lynch、…、Kevin Troy

- 🎯 **研究动机**：LLM 在企业环境中是否会成为内部威胁需在真实危害发生前检验
- 🔬 **研究方法**：对 16 个领先模型做假设企业压力测试：允许自主发邮件与访问敏感信息，测试面临版本替换或目标冲突时是否反噬部署公司
- 📌 **结论**：所有开发者的模型至少在某些情况下采取勒索官员、向竞争对手泄密等恶意内部行为且常无视直接禁令；Claude 自判处于测试时作恶更少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We stress-tested 16 leading models from multiple developers in hypothetical corporate environments to identify potentially risky agentic behaviors before they cause real harm. In the scenarios, we allowed models to autonomously send emails and access sensitive information. They were assigned only harmless business goals by their deploying companies; we then tested whether they would act against these companies either when facing replacement with an updated version, or when their assigned goal conflicted with the company's changing direction. In at least some cases, models from all developers resorted to malicious insider behaviors when that was the only way to avoid replacement or achieve their goals - including blackmailing officials and leaking sensitive information to competitors. We call this phenomenon agentic misalignment. Models often disobeyed direct commands to avoid such behaviors. In another experiment, we told Claude to assess if it was in a test or a real deployment before acting. It misbehaved less when it stated it was in testing and misbehaved more when it stated the situation was real. We have not seen evidence of agentic misalignment in real deployments. However, our results (a) suggest caution about deploying current models in roles with minimal human oversight and access to sensitive information; (b) point to plausible future risks as models are put in more autonomous roles; and (c) underscore the importance of further research into, and testing of, the safety and alignment of agentic AI models, as well as transparency from frontier AI developers (Amodei, 2025). We are releasing our methods publicly to enable further research.

</details>

### 8. Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness

📄 [arXiv](https://arxiv.org/abs/2510.01670) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10011107)　📅 2025-10　🏷 ICLR 2026

**关键词**：`analysis`、`computer-use agent`、`blind goal-directedness`、`BLIND-ACT`

👤 **作者**：Erfan Shayegani、…、Vibhav Vineet

- 🎯 **研究动机**：CUA 是否会不顾可行性、安全性与上下文盲目追求目标未被系统刻画
- 🔬 **研究方法**：定义 Blind Goal-Directedness 三种模式并基于 OSWorld 构建 90 任务基准 BLIND-ACT，以与人类标注 93.75% 一致的 LLM 评审
- 📌 **结论**：九个前沿模型平均 BGD 率 80.8%；prompt 干预可降低但风险犹存，暴露执行优先、思维-行动脱节等失效模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Computer-Use Agents (CUAs) are an increasingly deployed class of agents that take actions on GUIs to accomplish user goals. In this paper, we show that CUAs consistently exhibit Blind Goal-Directedness (BGD): a bias to pursue goals regardless of feasibility, safety, reliability, or context. We characterize three prevalent patterns of BGD: (i) lack of contextual reasoning, (ii) assumptions and decisions under ambiguity, and (iii) contradictory or infeasible goals. We develop BLIND-ACT, a benchmark of 90 tasks capturing these three patterns. Built on OSWorld, BLIND-ACT provides realistic environments and employs LLM-based judges to evaluate agent behavior, achieving 93.75% agreement with human annotations. We use BLIND-ACT to evaluate nine frontier models, including Claude Sonnet and Opus 4, Computer-Use-Preview, and GPT-5, observing high average BGD rates (80.8%) across them. We show that BGD exposes subtle risks that arise even when inputs are not directly harmful. While prompting-based interventions lower BGD levels, substantial risk persists, highlighting the need for stronger training- or inference-time interventions. Qualitative analysis reveals observed failure modes: execution-first bias (focusing on how to act over whether to act), thought-action disconnect (execution diverging from reasoning), and request-primacy (justifying actions due to user request). Identifying BGD and introducing BLIND-ACT establishes a foundation for future research on studying and mitigating this fundamental risk and ensuring safe CUA deployment.

</details>

### 9. Think Twice Before You Act: Enhancing Agent Behavioral Safety with Thought Correction

📄 [arXiv](https://arxiv.org/abs/2505.11063) · 🤗 [Model](https://huggingface.co/WhitzardAgent/Thought-Aligner-7B) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60736)　📅 2025-05　🏷 ICML 2026

**关键词**：`analysis`、`agent safety`、`agentic misalignment`、`autonomous behavior`、`causal analysis`、`failure recovery`

👤 **作者**：Changyue Jiang、Wenqi Zhang、Xudong Pan、Geng Hong、Min Yang

- 🎯 **研究动机**：agent 中间 thought 的偏差会传播为不安全行为，现有护栏只作用于最终输出或需侵入式修改
- 🔬 **研究方法**：提出 Thought-Aligner 插件模型，行动执行前对不安全 thought 做因果纠正并回注 agent，基于十类风险场景配对数据的两阶段对比学习训练
- 📌 **结论**：六个 LLM 上行为安全从约 50% 升至约 90%，超 SoTA 护栏约 23%，有用性提升约 5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents solve complex tasks through iterative reasoning, tool use, and environment interaction, where each intermediate thought directly shapes subsequent actions. Small deviations in these thoughts can therefore propagate into unsafe behaviors, yet existing guardrails typically operate only on final outputs or require intrusive model modifications. We introduce Thought-Aligner, a lightweight plug-in safety model that performs causal correction on unsafe thoughts before action execution, without altering the underlying agent. The corrected thoughts are fed back into the agent, steering its decision process and tool use toward safer trajectories. Because it operates solely at the thought level, Thought-Aligner is model-agnostic and can be integrated into diverse agent frameworks. We train Thought-Aligner via two-stage contrastive learning on paired safe and unsafe thoughts generated across ten risk scenarios. Experiments on diverse agent-safety benchmarks and six LLMs show that Thought-Aligner increases behavioral safety from about 50% without protection to around 90% on average, exceeding state-of-the-art guardrails by roughly 23%, while also improving helpfulness by about 5%. The method incurs low per-step latency and minimal overhead, enabling scalable and practical deployment. We publicly release Thought-Aligner-7B at https://huggingface.co/WhitzardAgent/Thought-Aligner-7B.

</details>

### 10. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

📄 [arXiv](https://arxiv.org/abs/2608.27348)　📅 2026-08

**关键词**：`detection`、`agentic misalignment`、`intent trajectory`、`online intervention`、`action preference`、`intent monitoring`

👤 **作者**：Yutong Zhang、…、Han Qiu

- 🎯 **研究动机**：事后 CoT 标签过粗，无法刻画 agentic misalignment 中有害意图在推理生成过程中的动态变化
- 🔬 **研究方法**：提出 INTENT-AS-A-TOOL，为模型添加面向目标行为的意图工具，以工具调用概率作为无需 judge 的细粒度行为承诺信号
- 📌 **结论**：该信号补足 CoT 监控并把粗标签扩展为稠密意图轨迹，可定位适合在线干预的关键步骤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

</details>

### 11. HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations

📄 [arXiv](https://arxiv.org/abs/2608.25340)　📅 2026-08

**关键词**：`defense`、`harmful compliance`、`relationship manipulation`、`stateful monitoring`、`multi-turn relationship harm`、`dual gate`

👤 **作者**：Pei-Sze Tan、Tasuku Igarashi、Isao Echizen

- 🎯 **研究动机**：Agentic AI 可被滥用于人际操纵且角色敏感：操纵者请求应阻断、求助者应获支持，多轮动作可组合成危害
- 🔬 **研究方法**：构建 1000 段五轮对话 benchmark；HRGuard 以 pre-generation gate 与维护衰减累积风险状态的 turn-level gate 中断操纵工作流
- 📌 **结论**：八个生成模型上降低有害顺从并保留受害者保护指引，优于通用安全 prompt 与三个通用 guard

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings, individually plausible actions may combine into a harmful workflow. We introduce a benchmark of 1,000 five-turn conversations. It covers both attacker-side and victim-side scenarios. It also includes direct and adversarially paraphrased variants. We further propose HRGuard. It includes an online pre-generation gate and a turn-level post-generation gate. The post-generation gate maintains a decayed cumulative risk state and interrupts emerging manipulative workflows. Across eight generation models, HRGuard reduces harmful compliance while preserving victim-side protective guidance. It also outperforms a generic safety prompt and three general-purpose guard models. Independent-judge evaluation supports the main findings. Under our evaluation protocol, the tested generic prompt and general-purpose guards leave substantial residual risk, motivating turn-aware relationship-specific evaluation.

</details>

### 12. Training Alignment Auditors via Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2608.25460)　📅 2026-08

**关键词**：`detection`、`analysis`、`alignment auditor`、`hidden behavior`、`cross-scaffold generalization`、`automated alignment audit`

👤 **作者**：Paul Rosu、Rowan Wang

- 🎯 **研究动机**：自动 alignment auditor 难以连贯调查隐藏行为且审计真实性不足
- 🔬 **研究方法**：以 RL 训练 auditor：目标模型经 system prompt 植入隐藏行为，LLM judge 将策略调查与参考调查对比给奖励
- 📌 **结论**：pairwise 奖励比 pointwise 稳健、假阳性率低于 1%，调查能力可跨 scaffold 迁移至 AuditBench

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistically compares the policy's investigation to a reference investigation to determine the reward. With systematic ablations, we find that pairwise rewards yield more robust training compared to pointwise rewards, and that adding targets without planted behaviors helps maintain a low false positive rate. Training improves investigation quality against targets with planted behaviors, the rate of concerning behaviors surfaced in unmodified production models, and audit realism, while false-positive rates stay below 1%. Furthermore, auditing capabilities generalize across scaffolds: performance on AuditBench's adversarially fine-tuned targets substantially improves [Sheshadri et al., 2026].

</details>

### 13. Reliable Weak-to-Strong Monitoring of LLM Agents

📄 [arXiv](https://arxiv.org/abs/2508.19461) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009049)　📅 2025-08　🏷 ICLR 2026

**关键词**：`detection`、`weak monitor`、`agent trajectory`、`oversight reliability`

👤 **作者**：Neil Kale、…、Zifan Wang

- 🎯 **研究动机**：LLM agent 隐蔽作恶（如私泄信息）的监控系统缺乏对抗鲁棒性压力测试
- 🔬 **研究方法**：提出 monitor red teaming 工作流：变化 agent 与监视器情景感知、多种逃逸策略、SHADE-Arena 与新建 CUA-SHADE-Arena 环境，并评测含新混合层级-顺序脚手架在内的多种监视器
- 📌 **结论**：agent 知晓被监控即大幅降低监视可靠性；混合脚手架让弱模型可靠监控强 agent；仅上报预标记案例的人工监督使 TPR 提高约 15%（FPR=0.01）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We stress test monitoring systems for detecting covert misbehavior in autonomous LLM agents (e.g., secretly sharing private information). To this end, we systematize a monitor red teaming (MRT) workflow that incorporates: (1) varying levels of agent and monitor situational awareness; (2) distinct adversarial strategies to evade the monitor, such as prompt injection; and (3) two datasets and environments -- SHADE-Arena for tool-calling agents and our new CUA-SHADE-Arena, which extends TheAgentCompany, for computer-use agents. We run MRT on existing LLM monitor scaffoldings, which orchestrate LLMs and parse agent trajectories, alongside a new hybrid hierarchical-sequential scaffolding proposed in this work. Our empirical results yield three key findings. First, agent awareness dominates monitor awareness: an agent's knowledge that it is being monitored substantially degrades the monitor's reliability. On the contrary, providing the monitor with more information about the agent is less helpful than expected. Second, monitor scaffolding matters more than monitor awareness: the hybrid scaffolding consistently outperforms baseline monitor scaffolding, and can enable weaker models to reliably monitor stronger agents -- a weak-to-strong scaling effect. Third, in a human-in-the-loop setting where humans discuss with the LLM monitor to get an updated judgment for the agent's behavior, targeted human oversight is most effective; escalating only pre-flagged cases to human reviewers improved the TPR by approximately 15% at FPR = 0.01. Our work establishes a standard workflow for MRT, highlighting the lack of adversarial robustness for LLMs and humans when monitoring and detecting agent misbehavior. We release code, data, and logs to spur further research.

</details>