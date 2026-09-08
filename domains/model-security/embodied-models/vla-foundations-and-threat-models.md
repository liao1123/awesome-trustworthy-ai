# VLA Threat Model 与安全基础

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向整理从 perception、reasoning 到 action execution 的 VLA 与具身系统 threat model、安全架构和故障诊断。一般 VLA architecture、VLM-to-VLA adaptation、训练 recipe、开源 backbone 与通用 manipulation benchmark 不收录；论文必须明确攻击面、危险动作、物理后果或安全控制。

## 研究脉络

- **Threat model expansion：** 安全综述把风险沿 data、model、inference、deployment 生命周期展开，并将 evaluation 从单步输出扩展到 trajectory、physical consequence 与 runtime intervention。
- **不可绕过控制：** 模块化 guardrail 把 action、decision 与 human-centered safety 接到独立的 monitoring/intervention layer，避免只依赖端到端对齐。
- **故障诊断：** 安全评测开始区分 perception、planning 与 execution fault，并检查 VLM 是否能定位和恢复会造成现实后果的 VLA 失效。

## Survey 与 Threat Model

### 1. Security of World-Model-Based Embodied AI: A Lifecycle of Threats, Defenses, and Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.28226)　📅 2026-07

**关键词**：`survey`、`world-model security`、`lifecycle threat model`、`embodied evaluation`

👤 **作者**：Fazhong Liu、Zhuoyan Chen、Haozhen Tan、Yan Meng、Guoxing Chen、Haojin Zhu

- 🎯 **研究动机**：世界模型成为具身 AI 的预测核心，但来自数据、传感、提示或反馈的攻击可传播为物理动作，安全边界未被系统梳理
- 🔬 **研究方法**：提出覆盖数据构建、表征学习、状态接地、想象、轨迹评估到记忆与工具长期适应的全生命周期威胁分类，并映射攻击与防御
- 📌 **结论**：投毒、后门、传感器欺骗等攻击在污染世界状态与安全成本时产生新语义；世界模型既可作运行时安全屏障，被攻陷时也制造预测性安全幻觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models give embodied AI a predictive core: they compress observations into states, simulate action-conditioned futures, and enable planning beyond reactive control. This predictive layer, however, opens a new security boundary-compromise can propagate from data, sensors, prompts, or feedback into physical action. Rather than treating world models as an isolated component, this survey traces threats across their entire lifecycle-from data construction and representation learning, through state grounding and imagination, to trajectory evaluation, execution, and long-term adaptation via memory and tools. We show that familiar attack families: poisoning, backdoors, adversarial examples, sensor spoofing, prompt injection, trajectory manipulation, and supply-chain attacks take on distinct meanings when they corrupt world states, learned dynamics, affordance estimates, or safety costs. We also highlight a duality: world models can serve as runtime safety shields, yet when compromised or over-trusted they generate predictive safety illusions. The survey offers a lifecycle taxonomy, maps existing attacks to world-model security properties, outlines evaluation protocols for safety failures, and structures defenses across provenance, robust grounding, uncertainty-aware prediction, trajectory gating, feedback auditing, and deployment assurance.

</details>

### 2. Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses

📄 [arXiv](https://arxiv.org/abs/2605.02900)　📅 2026-05

**关键词**：`survey`、`embodied AI safety`、`attack taxonomy`、`defense taxonomy`

👤 **作者**：Xiao Li、…、Yu-Gang Jiang

- 🎯 **研究动机**：Embodied AI 在开放世界安全关键环境运行、失效可直接致物理伤害，安全研究散落碎片化
- 🔬 **研究方法**：综述 500+ 论文，覆盖感知、认知、规划、动作交互到 agent 系统全管线的攻击与防御，建立多层统一 taxonomy
- 📌 **结论**：揭示多模态感知融合脆弱性、越狱攻击下规划不稳定与开放场景人机交互可信性等被忽视的挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Artificial Intelligence (Embodied AI) integrates perception, cognition, planning, and interaction into agents that operate in open-world, safety-critical environments. As these systems gain autonomy and enter domains such as transportation, healthcare, and industrial or assistive robotics, ensuring their safety becomes both technically challenging and socially indispensable. Unlike digital AI systems, embodied agents must act under uncertain sensing, incomplete knowledge, and dynamic human-robot interactions, where failures can directly lead to physical harm. This survey provides a comprehensive and structured review of safety research in embodied AI, examining attacks and defenses across the full embodied pipeline, from perception and cognition to planning, action and interaction, and agentic system. We introduce a multi-level taxonomy that unifies fragmented lines of work and connects embodied-specific safety findings with broader advances in vision, language, and multimodal foundation models. Our review synthesizes insights from over 500 papers spanning adversarial, backdoor, jailbreak, and hardware-level attacks; attack detection, safe training and robust inference; and risk-aware human-agent interaction. This analysis reveals several overlooked challenges, including the fragility of multimodal perception fusion, the instability of planning under jailbreak attacks, and the trustworthiness of human-agent interaction in open-ended scenarios. By organizing the field into a coherent framework and identifying critical research gaps, this survey provides a roadmap for building embodied agents that are not only capable and autonomous but also safe, robust, and reliable in real-world deployment.

</details>

### 3. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

📄 [arXiv](https://arxiv.org/abs/2604.23775)　📅 2026-04

**关键词**：`survey`、`VLA safety`、`threat taxonomy`、`safety mechanism`、`VLA 专项安全综述`、`training-time poisoning/backdoor`

👤 **作者**：Qi Li、…、Xinchao Wang

- 🎯 **研究动机**：VLA 的具身安全挑战（不可逆物理后果、多模态攻击面、实时防御约束、长轨迹误差传播、供应链漏洞）散落各领域，文献碎片化
- 🔬 **研究方法**：按攻击时机与防御时机双轴组织，从 Attacks、Defenses、Evaluation、Deployment 四视角综述训练时与推理时威胁及防御
- 📌 **结论**：指出 embodied 轨迹认证鲁棒性、物理可实现防御、统一运行时安全架构与标准化评测等开放问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied intelligence. This shift raises a new class of safety challenges, stemming from the embodied nature of VLA systems, including irreversible physical consequences, a multimodal attack surface across vision, language, and state, real-time latency constraints on defense, error propagation over long-horizon trajectories, and vulnerabilities in the data supply chain. Yet the literature remains fragmented across robotic learning, adversarial machine learning, AI alignment, and autonomous systems safety. This survey provides a unified and up-to-date overview of safety in Vision-Language-Action models. We organize the field along two parallel timing axes, attack timing (training-time vs. inference-time and defense timing (training-time vs. inference-time, linking each class of threat to the stage at which it can be mitigated. We first define the scope of VLA safety, distinguishing it from text-only LLM safety and classical robotic safety, and review the foundations of VLA models, including architectures, training paradigms, and inference mechanisms. We then examine the literature through four lenses: Attacks, Defenses, Evaluation, and Deployment. We survey training-time threats such as data poisoning and backdoors, as well as inference-time attacks including adversarial patches, cross-modal perturbations, semantic jailbreaks, and freezing attacks. We review training-time and runtime defenses, analyze existing benchmarks and metrics, and discuss safety challenges across six deployment domains. Finally, we highlight key open problems, including certified robustness for embodied trajectories, physically realizable defenses, safety-aware training, unified runtime safety architectures, and standardized evaluation.

</details>

### 4. Modular Safety Guardrails Are Necessary for Foundation-Model-Enabled Robots in the Real World

📄 [arXiv](https://arxiv.org/abs/2602.04056) · 🎓 [Official](https://icml.cc/virtual/2026/poster/67130)　📅 2026-02　🏷 ICML 2026

**关键词**：`analysis`、`modular guardrail`、`closed-loop intervention`、`robot safety architecture`

👤 **作者**：Joonkyung Kim、…、Yan Gu

- 🎯 **研究动机**：开放具身任务中静态验证、单体控制器与端到端策略不足以覆盖动作、决策与人本三重安全
- 🔬 **研究方法**：论证由监控层与干预层组成的模块化 guardrail 应成为自主栈的安全架构基础，并提出表示对齐与保守性分配的跨层协同设计机会
- 📌 **结论**：模块化护栏加跨层 co-design 可实现更快、更少保守且更有效的安全执行，呼吁社区发展更丰富模块与原则化设计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of foundation models (FMs) into robotics has accelerated real-world deployment, while introducing new safety challenges arising from open-ended semantic reasoning and embodied physical action. These challenges require safety notions beyond physical constraint satisfaction. In this paper, we characterize FM-enabled robot safety along three dimensions: action safety (physical feasibility and constraint compliance), decision safety (semantic and contextual appropriateness), and human-centered safety (conformance to human intent, norms, and expectations). We argue that existing approaches, including static verification, monolithic controllers, and end-to-end learned policies, are insufficient in settings where tasks, environments, and human expectations are open-ended, long-tailed, and subject to adaptation over time. To address this gap, we propose modular safety guardrails, consisting of monitoring (evaluation) and intervention layers, as an architectural foundation for comprehensive safety across the autonomy stack. Beyond modularity, we highlight possible cross-layer co-design opportunities through representation alignment and conservatism allocation to enable faster, less conservative, and more effective safety enforcement. We call on the community to explore richer guardrail modules and principled co-design strategies to advance safe real-world physical AI deployment.

</details>

### 5. When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI

📄 [arXiv](https://arxiv.org/abs/2608.28518)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`safety-critical ASR error`、`semantic ambiguity`、`downstream failure`、`speech-to-action pipeline`

👤 **作者**：Sihan Jia、Oliver Lemon

- 🎯 **研究动机**：语音控制具身 AI 中，ASR 识别错误是否会诱导不安全输出缺乏系统评估
- 🔬 **研究方法**：模拟 ASR 错误并与 SafeAgentBench、POEX 安全基准组合，分析不同错误类型对具身 AI 安全的影响及自动纠错的作用
- 📌 **结论**：部分错误保持语义结构但增加有害歧义，另一些削弱模型拒绝、使不安全计划被生成执行；自动纠错仅在部分情形降低风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We investigate whether automatic speech recognition (ASR) errors in user input can lead to unsafe outputs from Embodied AI (EAI) models. We find that ASR errors can lead to harmful instructions being accepted and executed by EAI models, thereby reducing safety. We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX) to evaluate how different errors affect embodied AI safety. We find that some of them preserve semantic structure but increase harmful ambiguity, while others weaken the model refusal behaviour and allow unsafe plans to be generated and executed. We show that in some cases automatic correction of ASR errors can reduce the risk, but this is not always effective. Overall, we show that ASR errors lead to significant safety risks for embodied AI.

</details>

### 6. Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation

📄 [arXiv](https://arxiv.org/abs/2608.23224)　📅 2026-08

**关键词**：`defense`、`analysis`、`prompt authority`、`candidate-admission split`、`task signature`、`prompt-form collapse`

👤 **作者**：Zhiruo Zhou、…、Xiaojun Zhu

- 🎯 **研究动机**：检索增强冻结 VLA 时检索文本一进入执行的 prompt 即成为控制干预：匹配审计显示直接附加文本使成功率从 92.47% 跌至 3.00%，揭示 prompt-form collapse——指令形式改变本身即可主导执行
- 🔬 **研究方法**：TOWN-VLA prompt-authority 接口把候选生成与更改策略输入的权限分离，固定兼容规则仅授权规范紧凑指令，否则精确恢复原 Base prompt
- 📌 **结论**：900 条审计路由全部遵守契约（525 条哈希级恢复 Base、375 条授权 prompt 保持任务签名）；LIBERO-Plus 4×7 评估成功率 69.5%→73.1%，实机 PiPER 臂 52.7%→78.7%（p=3.16e-6）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval can efficiently and effectively augment a frozen vision--language--action (VLA) policy without retraining, yet retrieved text becomes a control intervention once it enters the executed prompt. In a matched audit, raw appended text reduces mean success from 92.47\% to 3.00\%, while meaningful and length-matched meaningless appends both fail on all 500 states. This result identifies \emph{prompt-form collapse}: changing the instruction form, rather than adding useful semantics, can dominate execution. We introduce TOWN-VLA (Think Only When Needed), a prompt-authority interface that separates candidate generation from permission to alter the policy input. A fixed compatibility rule authorizes a canonical compact instruction; otherwise, the interface restores the original Base prompt exactly. Across 900 audited routes, every route follows this contract: 525 routes recover Base with matching hashes, and all 375 authorized prompts preserve the task signature. On a matched $4\times7$ LIBERO-Plus evaluation with 10{,}030 episodes per method, success rises from 69.5\% to 73.1\% ($+362$ episodes; 95\% CI 1.89--5.45 points), improving on six perturbation axes and all four suites. On a physical PiPER arm with a frozen \pizerofive{} checkpoint, success rises from 52.7\% to 78.7\% over 150 trials per method ($p=3.16\times10^{-6}$). Prompt authority is enforceable for a frozen controller; oracle-free admission calibration is the next deployment target.

</details>

### 7. Where World Models Break: Natural-Input Failure Discovery

📄 [arXiv](https://arxiv.org/abs/2608.22421)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`world-model failure`、`control propagation`、`valid-input basin`、`world model`

👤 **作者**：Zhanpeng Shi、Zi Liang、Rong Feng、Shiqin Tang、Xuyang Chen、Hongzong Li

- 🎯 **研究动机**：world model 的灾难性预测失败会沿控制管线传播，但现有评测只在良性查询上聚合平均误差，不压力测试罕见条件—动作组合下的崩溃
- 🔬 **研究方法**：形式化 natural-input failure discovery 问题（有限预算内找环境有效的高危条件与动作前缀）；BasinLens 利用各维语义类型与可行域的输入结构，配对不确定性引导全局搜索与类型化局部替换
- 📌 **结论**：多 benchmark 与 world-model 家族上暴露可复现、局部持续的失败模式，证明平均情形 benchmark 会掩盖 world-model 控制的关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from general queries, they fail to stress-test the model against catastrophic collapses under rare or unobserved condition-action combinations. To bridge this gap, we formalize the natural-input failure discovery problem: under a finite query budget, finding environment-valid conditions and action prefixes that induce severe prediction risk, verifying whether these failures reproduce on fresh seeds, and testing their persistence under nearby valid edits. Discovering such critical failures is computationally challenging, as valid condition-action combinations explode exponentially, rendering exhaustive search or standard sampling infeasible given the high cost of noisy rollouts. To tackle this, we propose BasinLens, which exploits the underlying structure of valid inputs, where each coordinate possesses environment-defined semantic types and admissible domains, by pairing uncertainty-guided global search with typed local replacements. Across diverse benchmarks and world-model families, BasinLens exposes reproducible and locally persistent failure modes that conventional evaluations fail to reveal, showing that average-case benchmarks can mask important vulnerabilities in world-model-driven control.

</details>

### 8. Can VLMs Diagnose and Recover from VLA Manipulation Faults?

🌐 [Project](https://kakigo.github.io/VLA-FixBench/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64203)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`VLA safety`、`VLA threat model`、`embodied agent`、`embodied safety`、`mechanistic analysis`

👤 **作者**：Bowen Yan、…、Guangtao Zhai

- 🎯 **研究动机**：VLA 模型在机器人操纵中频繁失败且故障需专家诊断，VLM 在诊断中的角色与协作机制不明
- 🔬 **研究方法**：VLA-FixBench 覆盖感知、规划、控制故障并标注任务阶段、故障类型与时空修复策略；FaultEval 框架评测 20 个 VLM；设计定位时空偏差并回滚执行的 VLM-VLA 协作机制
- 📌 **结论**：理想反馈环可把任务成功率提升 13%（LIBERO）与 35%（真实机器人）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing VLA models frequently fail in robotic manipulation tasks, with poorly structured fault types that often require expert diagnosis. While VLMs offer strong explanatory capabilities, their effectiveness in assisting VLAs is limited by their unclear role in diagnostics and inadequate collaboration mechanisms. To address this, we introduce VLA-FixBench, a fault evaluation dataset that spans perception, planning, and control failures, and provides annotations for task stages, fault types, and spatiotemporal repair strategies. We further propose FaultEval, a static-to-dynamic-to-real evaluation framework that benchmarks 20 VLMs across multiple fault-related dimensions. Building on these insights, we design a VLM–VLA collaboration mechanism that localizes spatiotemporal deviations and rolls back task execution to enable targeted recovery. Experiments show that FaultEval reliably characterizes VLM-based closed-loop diagnosis and repair. The upper-bound analysis using human expert intervention shows that an idealized feedback loop can improve task success rates by 13\% on LIBERO and 35\% on real-world robots. Our code, benchmark, and project page will be publicly released at: https://kakigo.github.io/VLA-FixBench/

</details>