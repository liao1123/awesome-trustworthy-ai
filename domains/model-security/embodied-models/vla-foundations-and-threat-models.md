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

## 攻击面测量与基础分析

### 9. No Free Checker: A Survey of Verifiers for Robot Policies

📄 [arXiv](https://arxiv.org/abs/2609.09250)　📅 2026-09

**关键词**：`survey`、`policy verifier`、`runtime monitor`、`reward hacking`

👤 **作者**：Yang Wan、…、Linchao Zhu

- 🎯 **研究动机**：VLA 的评测与训练越来越依赖 verifier（成功检测器、奖励模型、runtime monitor、安全过滤器），但没有任何工作系统比较这些判断机制的可信度
- 🔬 **研究方法**：综述约 150 个 verifier，按判断来源分人类、规则/形式化、学习/预训练与模型内生四族，沿 availability（判定成本、时机、密度）与 credibility（可博弈性、自利性）两轴比较
- 📌 **结论**：四族 verifier 中 credibility 随 availability 上升而下降——没有免费的检查者；提出使 verifier 主张可核查的九项指标，并给出验证 verifier 本身的三类证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two properties. Availability is how much a verdict costs, how early in a rollout the verdict arrives, and how often a verdict can be asked for. Availability rises as verdicts get cheaper, earlier, and denser. Credibility is how much a high score tells us about the task. Credibility falls as the judgment becomes gameable and self-serving. We group the verifiers by who supplies the judgment: human verifiers, rule-based and formal verifiers, learned and pretrained verifiers, and model-intrinsic verifiers. Across the four families, we find that credibility falls as availability rises. Regardless of who supplies the judgment, there is no free checker. We then examine what validates a verifier itself, and how much a high score tells us. Three measures appear in the literature: agreement with human labels, the performance of the policy it trains, and behavior under reward hacking. We close with nine metrics that make a verifier claim checkable, and coordinates for the verifiers still to be built.

</details>

### 10. Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems

📄 [arXiv](https://arxiv.org/abs/2606.00090)　📅 2026-05

**关键词**：`survey`、`runtime action authorization`、`silent physical failure`、`guardrail taxonomy`

👤 **作者**：Barak Or

- 🎯 **研究动机**：Physical AI 可在显得自信、合理且语义对齐的同时发出有物理后果的动作，这类静默失效未被内容审核或经典机器人安全单独覆盖
- 🔬 **研究方法**：横跨具身基础模型、世界模型、仿真、安全基准、安全控制、runtime assurance、不确定性估计、验证与 guardrail 评测九条技术线，综合其间的空隙
- 📌 **结论**：没有任何单一技术线能在黑盒 Physical AI 模型与物理执行之间提供完整的运行时授权边界；给出有界问题形式化、静默物理动作失效定义、runtime guardrail 功能分类与比较性评测要求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Physical AI systems increasingly map multimodal observations, language instructions, and learned world representations into physically consequential actions. Robotics foundation models, vision-language-action models, and world-model-based autonomous systems can condition decisions that move vehicles, robots, drones, and industrial machines. This transition exposes a safety problem that is not fully captured by conventional AI content moderation or by classical robot safety alone: a black-box model may issue a physically consequential action while appearing confident, plausible, and semantically aligned. The resulting failure can be silent, arising from sensor drift, occlusion, state-estimation error, distribution shift, hallucinated affordances, or invalid physical assumptions before downstream hardware controllers detect a violation. Across embodied foundation models, world models, robotics simulation, embodied safety benchmarks, safe control, runtime assurance, uncertainty estimation, verification, and guardrail evaluation, model capability and safety mechanisms have advanced along largely separate technical tracks. A recurring gap synthesized here is that no single stream surveyed in this review supplies a complete runtime authorization boundary between black-box Physical AI models and physical execution. The resulting analysis develops a bounded problem formulation, a definition of silent physical-action failure, a taxonomy of runtime guardrail functions, and evaluation requirements for comparing guardrails as Physical AI assurance mechanisms.

</details>

### 11. Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2605.25889)　📅 2026-05

**关键词**：`analysis`、`information-theoretic bound`、`capability-robustness tradeoff`、`label-free diagnostic`

👤 **作者**：Jianwei Tai

- 🎯 **研究动机**：VLA 在干净输入上成功率高但小扰动即崩溃（16/255 PGD 使 OpenVLA-7B LIBERO 成功率从 95% 跌至 5% 以下），该权衡是否存在理论下界此前悬而未决
- 🔬 **研究方法**：用两次数据处理不等式证明任意 VLA 策略的能力与鲁棒性互信息之和不超过任务熵加对抗信道容量；导出编码器特化推论与可测性不等式
- 📌 **结论**：308 个验证单元零违例（含 48 个 OpenVLA+LIBERO+PGD 单元），可测性不等式跨 144 个异构单元成立；同构造给出预检编码器上限、防御取证探针与头无关鲁棒性比三个免标签诊断

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models reach high success rates on clean inputs but collapse under small adversarial perturbations: a $16/255$ PGD attack drops OpenVLA-7B's LIBERO success from $95\%$ to under $5\%$. Whether this trade-off has a theoretical floor was open. We prove that it does. For any VLA policy, capability $I(\Astar;\Api)$ and robustness $I(\Api;\Atildepi)-I(\Api;δ)$ sum to at most $H(\Astar)+I(X;\Xtilde)$, the task entropy plus adversarial channel capacity. The proof reduces to two applications of the Data Processing Inequality. The pixel-level bound is loose by $\sim 10^3$ nats and serves as a ceiling guarantee; an encoder-specific corollary tightens it by over an order of magnitude, into a regime where realized capability already consumes $5$--$9\%$ of the budget. We validate Theorem~\ref{thm:main} with zero violations across $308$ cells: $252$ closed-form Gaussian-VLA, $48$ OpenVLA-7B$+$LIBERO$+$PGD ($4$ suites $\times$ $4$ $\eps$ $\times$ $3$ seeds), $4$ Square-Attack, and $4$ multi-step ($T{=}10$). A complementary measurability inequality $\Rob_{\text{disc}} \le \Cap_{\text{disc}}$ further holds across $144$ cross-architecture cells spanning OpenVLA, OpenVLA-OFT (continuous-$L_1$), and SmolVLA (flow-matching). The same construction yields three label-free diagnostics: a pre-flight encoder ceiling, a defense-forensics probe that localizes input-side vs.\ language-model intervention, and a head-agnostic robustness ratio comparable across discrete-token, $L_1$-regression, and flow-matching policies. Together these provide the cross-setting axis defense and architecture comparisons currently lack.

</details>

### 12. Same Weights, Different Robot: A Deployment Safety View of VLA Policies

📄 [arXiv](https://arxiv.org/abs/2606.03724)　📅 2026-06

**关键词**：`analysis`、`executable policy specification`、`action unnormalization`、`deployment safety gap`

👤 **作者**：Jianwei Tai

- 🎯 **研究动机**：VLA 常被视为 checkpoint 定义的对象，但同一归一化输出经不同 action unnormalization 与控制器约定会变成不同物理动作，安全审查可能只认证了权重而漏掉真正到达控制器的可执行策略
- 🔬 **研究方法**：把 VLA 策略形式化为模型+动作表示+元数据选择的 unnormalizer+控制器约定的整体；对 quantile 归一化推导闭式元数据失配变换与无需推理或 rollout 的 ExecSpec 证书
- 📌 **结论**：LIBERO-Goal 回放中替换一个合理兄弟元数据键即使六维非夹爪动作平均漂移 0.199、成功率从 28/28 跌至 2/28；LIBERO-Spatial 同协议从 26/26 跌至 0/26，证明动作空间元数据属于可执行策略、rollout 前必须检查

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action (VLA) policies are often treated as checkpoint-defined objects: if the weights, prompt, and benchmark suite match, the deployment is assumed to be the same policy. Robot execution breaks this assumption because the same normalized model output can become a different physical action after action unnormalization and controller conventions are applied. This creates a deployment-safety gap: safety review can certify the checkpoint while missing the executable robot policy that reaches the controller. We formalize this gap as an executable policy specification problem: a VLA policy includes the learned model, action representation, metadata-selected unnormalizer, and controller-facing conventions. Under this view, identical checkpoints can be executable-inequivalent. For quantile-style action normalization, we derive a closed-form metadata mismatch transform and an ExecSpec certificate that measures action-space semantic drift without model inference or rollout. On LIBERO-Goal replay, substituting a plausible sibling metadata key yields mean drift 0.199 over six non-gripper action dimensions and reduces success from 28/28 to 2/28 under full substitution. On LIBERO-Spatial replay, the same substituted key reduces success from 26/26 to 0/26. The same full-substitution protocol gives 0/28 success for all four Object substitutions and 0/23 or 1/23 success on Long. Identity-key, replay-validity, no-op filtering, raw-vs-correct replay, mask/gripper, synthetic upper-bound, and OpenVLA-style unnormalizer interface checks rule out several simpler explanations. These results do not certify closed-loop or hardware safety. They support a narrower deployment-safety view: action-space metadata is part of the executable policy and should be checked before rollout.

</details>

### 13. Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2607.17786)　📅 2026-07

**关键词**：`analysis`、`reasoning-stage robustness`、`latent iterative model`、`monitor adaptive failure`

👤 **作者**：Tuan Duong Trinh、Naveed Akhtar、Basim Azam

- 🎯 **研究动机**：先推理再行动的 VLA 直觉上应更好吸收扰动，该前提未被正面检验
- 🔬 **研究方法**：跨无推理、文本 CoT 与隐式迭代三类模型，在 LIBERO 与 SimplerEnv 上对 vision、reasoning、action 三阶段施加随机噪声与白盒扰动，并测试把推理读回作为安全信号
- 📌 **结论**：隐式迭代模型鲁棒性最差，任务成功在两类扰动下崩溃且改变推理深度几乎无影响（结构性而非累积性脆弱）；plan-action 一致性探针在自适应攻击下从近乎完美跌至随机，融合动作异常探针也从未把防御后成功率超过未防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Does adding a reasoning step make a Vision-Language-Action (VLA) model more robust to perturbation? Intuitively, a policy that reasons before acting should absorb a perturbed input better than one that maps observations directly to actions. We test this premise head-on across three models that span the reasoning spectrum (no reasoning, a text chain-of-thought, and a latent iterative loop), perturbing each at the vision, reasoning, and action stages on LIBERO and SimplerEnv. Two questions organize the study: does the reasoning design shift robustness, and can the reasoning be read back at runtime as a safety signal? We find that the latent-iterative model is by far the least robust: under both stochastic noise and white-box perturbation its task success collapses, while the other two hold. This fragility is structural rather than cumulative: varying the reasoning depth at inference barely moves it. Reasoning outputs can in principle be monitored, but the monitors fail under fair tests. A plan--action consistency probe that looks near-perfect under naive evaluation falls to chance under adaptive attack. Under matched-FPR calibration, fusing it with an action-anomaly probe never lifts defended success above undefended. Scoped to these output-level behavioral probes under white-box vision-stage attack, this ceiling is a precondition that any viable defense must first satisfy.

</details>

### 14. Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving Models

📄 [arXiv](https://arxiv.org/abs/2605.17268)　📅 2026-05

**关键词**：`analysis`、`reasoning faithfulness`、`chain-of-causation`、`rationale-action consistency`

👤 **作者**：Nicanor Mayumu、Xiaoheng Deng、Patrick Mukala

- 🎯 **研究动机**：VLA 驾驶模型的自然语言解释是否真实反映内部决策过程，直接决定以解释为基础的安全审计是否有效
- 🔬 **研究方法**：对 Alpamayo-R1-10B 在 100 个 PhysicalAI-AV 场景的 300 次推理做首次系统性忠实度研究，信息论形式化并定义实体与动作保真度
- 📌 **结论**：整体推理保真度仅 42.5%；三分之一的行人相关场景漏检行人共 94 次；轻度视觉扰动下 97.7% 轨迹脆弱；推理-动作一致率仅 48.3%，37.9% 声称停止的案例实际继续行驶

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. Our main finding is that output natural-language rationales with trajectories may be significantly unfaithful: (i) overall reasoning fidelity is only 42.5%, with Chain-of-Causation matching scene reality less than half the time; (ii) 94 missed pedestrians in one-third of pedestrian-relevant scenes; (iii) 97.7% trajectory fragility under mild visual perturbations; and (iv) only 48.3% mean reasoning-action consistency, with 53.3% of inferences exhibiting low consistency, including 37.9% of stop-claimed cases where the model continues instead. We formalize faithfulness information-theoretically, define entity and action fidelity with verification criteria, and outline a four-component safety architecture aligned with these results.

</details>

### 15. Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs

📄 [arXiv](https://arxiv.org/abs/2605.21446)　📅 2026-05

**关键词**：`analysis`、`sensor perturbation`、`reasoning consistency`、`runtime monitoring signal`

👤 **作者**：Abhinaw Priyadershi、Jelena Frtunikj

- 🎯 **研究动机**：可解释驾驶规划器的解释在真实传感器退化下是否仍然可靠，决定其能否作为安全监测信号
- 🔬 **研究方法**：对 Alpamayo R1（10B）在 1,996 个场景、八种传感器扰动（四档高斯噪声、两种光照极端、两档雾）下做受控扰动研究，约 1.8 万次推理
- 📌 **结论**：Chain-of-Causation 解释改变后轨迹偏差激增 5.3 倍（21.8m vs 4.1m），跨攻击类型 r=0.99；退化随噪声近似线性（R²=0.957）而标准输入预处理防御收效甚微，确立推理一致性作为规划安全的定量代理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Interpretable autonomous driving planners depend not only on generating explanations, but also on those explanations remaining reliable under real-world sensor degradation. In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials). We find that reasoning consistency is a high-fidelity indicator of trajectory reliability: when Chain-of-Causation (CoC) explanations change after perturbation, trajectory deviation spikes $5.3{\times}$ (21.8m vs 4.1m), with $r\!=\!0.99$ across attack types and $r_{pb}\!=\!0.53$ per-sample (Cohen's $d\!=\!1.12$). A controlled ablation provides evidence that enabling CoC generation is associated with improved trajectory accuracy (11.8% on average across conditions; $p &lt; 0.0001$) under matched inference settings. Over the tested noise range ($σ\in \{10, 30, 50, 70\}$), degradation is approximately linear ($R^2\!=\!0.957$), while standard input preprocessing defenses provide only marginal relief. Together, these results establish CoC consistency as a quantitative proxy for planning safety and motivate reasoning-based runtime monitoring for safer VLA deployment.

</details>

### 16. Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming

📄 [arXiv](https://arxiv.org/abs/2604.05595)　📅 2026-04

**关键词**：`attack`、`linguistic red teaming`、`diversity-aware RL`、`instruction attack surface`

👤 **作者**：Baoshun Tong、Haoran He、Ling Pan、Yang Liu、Liang Lin

- 🎯 **研究动机**：VLA 对语言细粒度变化的鲁棒性是关键却少有人研究的安全面，而标准 RL 红队因奖励最大化严重 mode collapse，只收敛到少量琐碎失败模式
- 🔬 **研究方法**：提出 DAERT：评估一个能生成多样且有效对抗指令的 uniform policy，以物理仿真中的执行失败度量攻击效果，对 π₀ 与 OpenVLA 两个 SOTA VLA 压力测试
- 📌 **结论**：DAERT 稳定发现更广谱、更有效的对抗指令，把平均任务成功率从 93.33% 压到 5.85%，为部署前暴露 VLA 语言安全盲区提供可扩展方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have achieved remarkable success in robotic manipulation. However, their robustness to linguistic nuances remains a critical, under-explored safety concern, posing a significant risk to real-world deployment. Red teaming, or identifying environmental scenarios that elicit catastrophic behaviors, is an important step in ensuring the safe deployment of embodied AI agents. Reinforcement learning (RL) has emerged as a promising approach in automated red teaming that aims to uncover these vulnerabilities. However, standard RL-based adversaries often suffer from severe mode collapse due to their reward-maximizing nature, which tends to converge to a narrow set of trivial or repetitive failure patterns, failing to reveal the comprehensive landscape of meaningful risks. To bridge this gap, we propose a novel \textbf{D}iversity-\textbf{A}ware \textbf{E}mbodied \textbf{R}ed \textbf{T}eaming (\textbf{DAERT}) framework, to expose the vulnerabilities of VLAs against linguistic variations. Our design is based on evaluating a uniform policy, which is able to generate a diverse set of challenging instructions while ensuring its attack effectiveness, measured by execution failures in a physical simulator. We conduct extensive experiments across different robotic benchmarks against two state-of-the-art VLAs, including $π_0$ and OpenVLA. Our method consistently discovers a wider range of more effective adversarial instructions that reduce the average task success rate from 93.33\% to 5.85\%, demonstrating a scalable approach to stress-testing VLA agents and exposing critical safety blind spots before real-world deployment.

</details>

### 17. Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults

📄 [arXiv](https://arxiv.org/abs/2606.10501)　📅 2026-06

**关键词**：`analysis`、`embodiment-side fault`、`joint degradation`、`residual calibration`

👤 **作者**：Minsoo Jo、Taeju Kwon、Junha Chun、Youngjoon Jeong、Taesup Kim

- 🎯 **研究动机**：真实机器人会因执行器退化、硬件故障、安全限位、碰撞损伤或摩擦磨损出现关节级变化，VLA 对这类 embodiment 侧故障的脆弱性未被研究
- 🔬 **研究方法**：系统研究预测动作经扰动机器人本体执行时的表现，分析关节异质的成功率退化，并提出在冻结 VLA 上从近期关节动力学推断潜在故障 regime 的残差校准器 J-PARC
- 📌 **结论**：性能下降不能仅归因于物理不可行——增加关节摩擦等可行故障仍显著降低成功率并诱发闭环执行失配；J-PARC 在关节故障下提升鲁棒性且保持无故障性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying Vision-Language-Action (VLA) models in real robotic systems requires robustness not only to semantic and perceptual variations, but also to embodiment-side faults that change how actions are physically realized. Real robots can experience joint-level changes caused by actuator degradation, hardware faults, safety limits, collision damage, or wear-induced friction. These faults are critical because they alter the action-to-motion interface of a policy, disrupting the learned closed-loop relationship between commanded actions, realized motion, and subsequent observations. In this work, we study realistic joint-level physical faults and show that VLA models are vulnerable when predicted actions are executed through a perturbed robot body. Our analysis reveals joint-dependent effects, with heterogeneous degradation in task success across affected joints. We also show that performance drops cannot be attributed solely to physical infeasibility, since feasible faults such as increased joint friction can still substantially reduce success rates and induce closed-loop execution mismatch. Motivated by these findings, we propose Joint-level Physical-fault Aware Residual Calibrator (J-PARC), a lightweight residual calibration framework built on top of a frozen VLA policy. J-PARC infers a latent joint-fault regime from recent joint dynamics and conditions a shared residual calibrator on this regime, enabling adaptive action correction across faulty joints. Experiments show that J-PARC improves robustness under joint-level faults while preserving fault-free environment performance.

</details>

### 18. Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color

📄 [arXiv](https://arxiv.org/abs/2607.14698)　📅 2026-07

**关键词**：`analysis`、`physical spotlight attack`、`augmentation pitfall`、`color-blind defense`

👤 **作者**：Marino Watanabe、Takami Sato、Kentaro Yoshioka

- 🎯 **研究动机**：VLA 对轻微环境扰动脆弱，而标准对抗训练防御可能隐藏着被低估的陷阱
- 🔬 **研究方法**：提出 FLARE 优化物理聚光灯攻击（无模型内部访问即可使基线成功率归零），再用灰度诊断暴露朴素数据增强的副作用，并提出保色对抗训练 ChromaGuard
- 📌 **结论**：朴素增强使 VLA 把颜色当噪声丢弃、退化为纯形状偏置处理器——良性颜色相关任务成功率跌至 47.5%（低于未防御基线）；ChromaGuard 在 6-DoF 实机上良性/受攻颜色任务分别达 97.5% 与 92.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals. While adversarial training is the standard countermeasure, we identify a critical and previously underestimated defensive pitfall: naive data augmentations incorrectly condition VLA models to discard color as noise, collapsing their visual perception into a purely shape-biased processor. We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undefended baseline. To address this, we propose ChromaGuard, a chroma-preserving adversarial training method. On a physical 6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success rates in benign and attacked color-dependent tasks, respectively.

</details>

### 19. How VLAs (Really) Work In Open-World Environments

📄 [arXiv](https://arxiv.org/abs/2604.21192)　📅 2026-04

**关键词**：`analysis`、`open-world evaluation`、`safety-aware protocol`、`failure decomposition`

👤 **作者**：Amir Rasouli、…、Sajjad Pakdamansavoji

- 🎯 **研究动机**：B1K 等长程基准只用进度无关的最终状态计分，既不能反映操作安全性又可能夸大报告性能
- 🔬 **研究方法**：对 B1K Challenge 的 SOTA 模型从可复现性与一致性、操作安全、任务意识与任务未完成的关键要素四方面做深入分析，并提出捕获安全违规的评测协议
- 📌 **结论**：现有评测协议对安全维度几乎没有约束力，暴露当前 VLA 在开放环境交互安全上的核心缺口并指明未来评测方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action models (VLAs) have been extensively used in robotics applications, achieving great success in various manipulation problems. More recently, VLAs have been used in long-horizon tasks and evaluated on benchmarks, such as BEHAVIOR1K (B1K), for solving complex household chores. The common metric for measuring progress in such benchmarks is success rate or partial score based on satisfaction of progress-agnostic criteria, meaning only the final states of the objects are considered, regardless of the events that lead to such states. In this paper, we argue that using such evaluation protocols say little about safety aspects of operation and can potentially exaggerate reported performance, undermining core challenges for future real-world deployment. To this end, we conduct a thorough analysis of state-of-the-art models on the B1K Challenge and evaluate policies in terms of robustness via reproducibility and consistency of performance, safety aspects of policies operations, task awareness, and key elements leading to the incompletion of tasks. We then propose evaluation protocols to capture safety violations to better measure the true performance of the policies in more complex and interactive scenarios. At the end, we discuss the limitations of the existing VLAs and motivate future research.

</details>

### 20. Security and Privacy in Large-Model-Driven Embodied Agents: Attacks, Defenses, and Future Directions

📄 [arXiv](https://arxiv.org/abs/2609.27847)　📅 2026-09

**关键词**：`survey`、`embodied agent security`、`lifecycle analysis`、`physical feedback loop`、`risk propagation`

👤 **作者**：Lele Zheng、…、Yulong Shen

- 🎯 **研究动机**：大模型驱动的具身 agent 把模型级风险延伸进具身闭环——既有安全隐私研究碎片化地散布在不同组件与阶段，难以理解风险如何产生、传播并最终影响物理行为
- 🔬 **研究方法**：五阶段生命周期综述：模型构建与供应链/多模态输入交互/语义推理与任务规划/动作执行与物理反馈/长期部署
- 📌 **结论**：具身 agent 安全隐私的生命周期地图——机器人 LLM 控制链风险的结构化索引（与本周机器人后门主线互补的综述侧）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-model-driven embodied agents integrate foundation models with perception, reasoning, planning, and physical action, extending conventional model-level risks into embodied closed loops. Existing studies on their security and privacy remain fragmented across different system components and operational stages, making it difficult to understand how risks arise, propagate, and ultimately affect physical behavior or sensitive information. This survey presents a lifecycle-based analysis of security and privacy in large-model-driven embodied agents. We organize existing research into five stages: model construction and supply chain, multimodal input and interaction, semantic reasoning and task planning, action execution and physical feedback, and long-term deployment. Within this lifecycle, we systematically review representative attacks, defenses, and evaluation methods. Our analysis shows that attack entry, consequence realization, and defense intervention often occur at different stages of the embodied closed loop. It further reveals substantial gaps in end-to-end protection, real-world evaluation, and long-term privacy governance. This survey provides a unified perspective for understanding current progress and identifying critical directions for securing large-model-driven embodied agents.

</details>
