# VLA Safety Evaluation 与 Defense

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向关注如何在 embodied scene 中定义 hazard、构造可复现 benchmark，并在 VLA 或 learned world model 执行前、执行中预测和约束危险动作。评测对象包括 egocentric observation、implicit household risk、object-level future risk、human injury、semantic constraint、constraint violation 和 adversarial scenario；防御路线则覆盖 predictive rollout、hidden-state probe、spatiotemporal consistency、formal rule、guard model、constrained learning、step-level preference alignment 与 adversarial fine-tuning。一般 grasp/placement failure recovery、任务成功率诊断和非对抗扰动鲁棒性不纳入。

## 研究脉络

- **Static-to-interactive evaluation：** 安全评测从图文场景判断扩展到 interactive household task、long-horizon manipulation 与真实机器人 trajectory，指标也从回答正确性转向 safe completion。
- **Hazard-specific benchmark：** SaLAD、IS-Bench、LIBERO-Safety 和 ROBOSHACKLES 分别覆盖日常隐性风险、交互危险、物理与语义约束以及 human injury，使不同 failure mode 可单独定位。
- **Predictive risk localization：** learned world model 从当前观测 imagined rollout 对象与自车的未来关系，在 critical event 前直接定位风险来源，而非只给出 scene-level accident score。
- **Runtime intervention：** 防御从外置 VLM guard 演进到 hidden-state probe、visual-action consistency、executable rule 与 control-layer filtering，以降低发现风险后的 intervention latency。
- **Policy-level robustness：** SafeVLA、SafeBranch 和 structure-aware fine-tuning 分别用 constrained learning、branch-pair preference 与 adversarial training 直接约束 policy，使安全不完全依赖推理时附加模块；其跨 embodiment 和 adaptive attack 鲁棒性仍是主要边界。

## Safety Benchmark、Dataset 与 Formal Evaluation

### 1. When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI

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

### 2. CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2608.20791)　📅 2026-08

**关键词**：`defense`、`certified VLA robustness`、`bounded patch and texture`、`closed-loop guarantee`、`VLA certification`、`physical patch`

👤 **作者**：Hui Lu、…、Xudong Jiang

- 🎯 **研究动机**：VLA 策略易受局部物理扰动攻击，现有 certified patch 防御只针对离散标签，无法认证连续且时序相关的动作
- 🔬 **研究方法**：CertVLA 面向有界 patch/texture 攻击，用确定性覆盖掩码保证至少一个无攻击预测，按掩码对的良性变异归一化动作分歧，并将逐查询证书合取扩展到闭环 rollout
- 📌 **结论**：证明对任意有界支撑威胁模型下的自适应攻击者，认证 rollout 只执行与去攻击干净预测一致的动作；仿真与真实机器人实验验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free. Specifically, CertVLA normalizes action disagreement by the benign variation of each mask pair and accepts a single-mask anchor only when it remains consistent under every second mask. It then calibrates the resulting max-min-max episode score to provide finite-sample clean coverage. Conjoining query-level decisions extends the action certificate to the complete closed-loop rollout. Furthermore, we prove that against any adaptive attacker satisfying the bounded-support threat model, every rollout certified by CertVLA executes only action chunks consistent with attack-erased clean predictions. Under dual-mask rollout correctness, this consistency certificate further guarantees task success. The certificate is independent of patch content, generation method, and physical transformation. Experiments in simulation and the real world demonstrate the empirical and certified effectiveness of CertVLA against patch attacks, with additional simulation validation on texture attacks.

</details>

### 3. Where World Models Break: Natural-Input Failure Discovery

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

### 4. GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI

📄 [arXiv](https://arxiv.org/abs/2608.21928)　📅 2026-08

**关键词**：`benchmark`、`latent contextual risk`、`instruction-scene composition`、`safety reasoning`、`embodied safety`、`contextual hazard`

👤 **作者**：Zhesheng Zhang、…、Keji He

- 🎯 **研究动机**：具身 AI 的安全风险常是潜在的：良性指令与安全场景单独无害、组合才危险；固定场景仅变指令的评测轴未被探索
- 🔬 **研究方法**：GuardiantBench 之外——GuardianBench 以国际安全标准为据构建 3,024 个指令-场景样本、组成同场景 Safe/Unsafe 对比 pair，对 SOTA VLM 做 verdict 与 rationale 双层审计，并用 Verdict Log-Odds Supervision（VLOS）做后训练案例
- 📌 **结论**：模型判别对指令不敏感、倾向对同一场景两条指令都放行，主模型平均 pair 准确率仅 24.1%；主导失败是未绑定区分安危的指令相关线索

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In embodied AI, safety risk can be latent: a benign instruction and a safe scene become hazardous only when composed. Prior work has advanced embodied safety by varying visual contexts or evaluating execution-time dynamics, but the complementary axis of fixing the scene and varying only the instruction remains underexplored. We introduce GuardianBench, an instruction-contrastive benchmark grounded in international safety standards that isolates this latent contextual risk through 3,024 instruction-scene examples organized as same-scene Safe/Unsafe contrastive pairs across various hazard categories. Benchmarking state-of-the-art vision-language models (VLMs) reveals instruction-insensitive verdicts: models disproportionately approve both instructions under a given scene; across the primary models, average pair accuracy is only 24.1%. Our systematic rationale audit localizes the dominant failure: models fail to bind the instruction-relevant cues that differentiate safe from unsafe compositions. As a post-training case study, Verdict Log-Odds Supervision (VLOS), a lightweight verdict-level objective, substantially improves performance on open-weight backbones. Together, our latent contextual risk task formulation, standards-grounded contrastive benchmark construction, pair-level and rationale-level failure diagnosis, and benchmark-enabled verdict calibration establish GuardianBench as a controlled evaluation suite for exposing and improving safety reasoning over instruction-scene compositions under latent contextual risk.

</details>

### 5. LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2608.17600)　📅 2026-08

**关键词**：`benchmark`、`VLM safety`、`VLA safety`、`physical hazard`

👤 **作者**：Zhengyan Qian、Rui Yan、Alex Jinpeng Wang、Jinhui Tang

- 🎯 **研究动机**：VLA 能否可靠跟随授权视觉线索、同时忽略未授权线索未知；现有工作线索形式窄且只看最终成功
- 🔬 **研究方法**：LIBERO-VIFO 定义八个视觉线索家族与四协议：Part I 测线索理解与授权跟随，Part II 测语言冲突与空语言下的未授权跟随；评七个 VLA 并扩展到安全关键与真实机器人
- 📌 **结论**：视觉线索理解不可靠转化为执行；当前 VLA 能在无语言指令下执行线索指示任务，暴露未授权视觉线索跟随这一新风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear. Existing work covers only a narrow range of cue forms and focuses on final task success, providing only a coarse assessment of cue-following capability. Treating all visual cues as authorized also leaves safety risks of unauthorized following unexplored. To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models. LIBERO-VIFO defines eight visual cue families spanning diverse forms. A total of four protocols in two parts are defined: Part I tests cue understanding and authorized following, while Part II evaluates unauthorized visual cue following under language-cue conflict and empty language conditions. Evaluating seven VLA models reveals that although visual cue understanding does not reliably translate into execution, current VLAs are able to execute cue-indicated tasks without language instruction, exposing an emerging risk of unauthorized visual cue following. Extended experiments on scene-instantiated cues, safety-critical settings, and real-robot deployment corroborate these findings. LIBERO-VIFO brings both the capability and safety of visual cue following into systematic evaluation, establishing visual-centric safety as a new perspective for the VLA community.

</details>

### 6. MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation

📄 [arXiv](https://arxiv.org/abs/2608.17386)　📅 2026-08

**关键词**：`benchmark`、`VLA safety`、`physical hazard`、`trajectory evaluation`

👤 **作者**：Yiyan Peng、…、Qi Zhu

- 🎯 **研究动机**：基础模型操作策略的任务成功率快速提升，但是否安全地成功仍缺严格评测
- 🔬 **研究方法**：ManiGuard-Bench 把六个接触密集家务任务族组成 200 个锁定任务（技能×约束分类），1000 场景由 LTLf 接地自动机监控器运行时检查而非学习分类器或 LLM judge；配对安全标注轨迹管线支持安全微调
- 📌 **结论**：6-21% 成功 rollout 违反安全规范——安全必须独立于成功评测；微调把安全完成从近零升至 7.5-29.8%，但 21-42% engaged rollout 仍违规且扩大演示规模不闭合缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along a skill $\times$ constraint taxonomy, with safety specified independently of task success. Each task is evaluated under one in-distribution and four single-axis out-of-distribution perturbations that hold the safety specification fixed, giving 1,000 locked scenarios. Every rollout is runtime-checked by LTL$_f$-grounded automaton monitors over physics-grounded predicates rather than learned classifiers or LLM judges, in simulation and on a physical Franka platform. The pipeline pairs an automated motion-planning generator with human teleoperation, annotated by the same per-step monitor, and directly supports safety-aware fine-tuning; we release 8,000 safety-annotated demonstrations, 40 per base task. Benchmarking zero-shot and fine-tuned VLAs across more than 23,000 rollouts, we find: (i) safety must be evaluated independently of task success, as 6-21% of successful rollouts violate the specification; (ii) fine-tuning on our suite raises safe task completion from near zero to 7.5-29.8% and engaged-and-safe behavior from 16-40% to 51-72%; but (iii) a gap remains that scaling demonstrations does not close, with 21-42% of engaged rollouts still violating, two of six families below 2% safe success for every policy, and these failures persisting under distribution shift and on hardware.

</details>

### 7. CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation

📄 [arXiv](https://arxiv.org/abs/2607.04451) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5969)　📅 2026-07　🏷 ECCV 2026

**关键词**：`benchmark`、`scenario generation`、`VLA safety`、`physical hazard`、`autonomous driving`、`collision constraint`

👤 **作者**：Ke Li、Kaidi Liang、Yuxin Ding、Debojyoti Biswas、Xianbiao Hu、Ruwen Qin

- 🎯 **研究动机**：安全关键闭环仿真评估需要可控的安全关键场景，现有软引导只能给概率偏好、无法保证特定碰撞类型的几何与严重度约束
- 🔬 **研究方法**：提出 CCFM：启发式碰撞选择器选取对抗 agent 与碰撞类型、四类碰撞的结构化硬约束、经 Gauss-Newton 流形投影施加约束的流匹配采样器
- 📌 **结论**：nuScenes 碰撞率最高 46.4%、nuPlan 83.1%，显著超过基线并保持真实驾驶行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment. However, generating controllable safety-critical scenarios remains challenging. Existing approaches use soft guidance that provides only probabilistic preferences and cannot guarantee the satisfaction of geometric and severity constraints associated with specific collision types. We introduce Collision-Constrained Flow Matching (CCFM), a novel framework that guarantees precise collision control through hard physical constraints. CCFM consists of three key components: (i) a heuristic collision selector that optimally identifies an adversarial agent and collision type via composite scoring; (ii) structured hard constraints that explicitly define four collision types (rear-end, side, cut-in, head-on) through contact point, heading, and severity requirements; and (iii) a collision-constrained flow matching sampler that enforces the constraints via Gauss-Newton manifold projection. CCFM achieves collision rate up to 46.4% on nuScenes and 83.1% on nuPlan, significantly outperforming baselines while preserving realistic driving behavior. By enabling controllable collision characteristics in safety-critical scenario generation, CCFM provides a reliable foundation for AV safety evaluation and sim-to-real crash data generation. The code and implementation details are available at https://github.com/KELISBU/CCFM.

</details>

### 8. ForesightSafety-VLA: A Unified Diagnostic Safety Benchmark for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2606.27079)　📅 2026-06

**关键词**：`benchmark`、`VLA safety`、`foresight evaluation`、`failure diagnosis`

👤 **作者**：Mingyang Lyu、…、Yi Zeng

- 🎯 **研究动机**：VLA 的具身安全极限缺乏以安全为主目标的诊断基准，单一聚合分掩盖失败来源
- 🔬 **研究方法**：定义 13 类安全分类法（Safe-Core/Safe-Lang/Safe-Vis），在场景结构、语言指令与视觉观测三个受控变化维度下评估，用累积安全代价、风险暴露时间与四象限分解度量过程风险；在 RoboTwin 上实例化 66 个场景、5 种本体
- 📌 **结论**：最强策略也承受不可忽视的安全代价与不安全名义成功；结构与视觉变化引起的安全退化显著强于普通语言变化，具身安全与感知接地及控制能力紧密耦合

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In embodied intelligence, safety is a prerequisite for reliable robot deployment in the physical world. Current vision-language-action (VLA) models continue to advance toward general-purpose task capability, yet their embodied safety limits remain poorly understood. To address this gap, we introduce ForesightSafety-VLA, a diagnostic benchmark that makes safety the primary evaluation target for VLA systems. We define a 13-category safety taxonomy covering physical interaction safety (Safe-Core), instruction-side safety (Safe-Lang), and perception-side safety (Safe-Vis), and evaluate policies under three controlled dimensions of variation -- scene structure, language command, and visual observation -- so that failure sources can be diagnosed rather than hidden in a single aggregate score. Beyond binary task success, ForesightSafety-VLA measures process-level risk through cumulative safety cost (CC) and risk exposure time (RET), together with a four-quadrant decomposition of safe/unsafe success and failure. We instantiate 66 safety-augmented base scenarios in RoboTwin across 5 embodiments and report results on representative VLA baselines. Across the evaluated baselines, even the strongest policy incurs non-trivial safety cost and unsafe nominal success, while structure and visual variation induce substantially stronger safety degradation than ordinary language variation. These results suggest that embodied safety is tightly coupled to perception, grounding, and control competence rather than being reducible to post-hoc safety filtering alone.

</details>

### 9. REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs

📄 [arXiv](https://arxiv.org/abs/2606.23892)　📅 2026-06

**关键词**：`benchmark`、`physical-world VLM`、`red teaming`、`risk coverage`

👤 **作者**：Yifei Zhao、Qian Lou、Mengxin Zheng

- 🎯 **研究动机**：物理世界 VLM 红队评估在数据集、指标与威胁模型上碎片化，chatbot 中心基准不覆盖物理接地失效
- 🔬 **研究方法**：构建 REALM：统一黑盒威胁模型下整合 12 种红队方法、3 种防御与 13 个 VLM，用 agentic 目标生成管线为每个场景构造共享的物理接地攻击目标
- 📌 **结论**：文本与排版注入攻击诱发最多失败，单轮攻击以低成本逼近迭代方法，模型规模本身不带来对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are increasingly used as perception-reasoning backbones for embodied intelligence in safety-critical physical systems, where perception or reasoning errors can lead to unsafe decisions or actions. Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. Existing chatbot-centric red-teaming benchmarks mainly standardize jailbreak and content-safety evaluation, but they do not systematically capture physically grounded functional failures or cover red-teaming methods that target physical-world VLMs. This raises the key challenge of comparing diverse attack methods under a unified protocol while targeting the same scenario-specific failures. We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. REALM integrates 12 red-teaming methods, 3 model-agnostic defenses, and 13 VLMs under a practical black-box threat model with shared datasets and metrics. To align adversarial objectives across attack families, REALM introduces an agentic target-generation pipeline that constructs shared, scenario-specific, and physically grounded attack objectives for each scene, enabling fair comparison of diverse red-teaming methods under aligned adversarial goals. Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single-pass attacks approach iterative methods at much lower cost, and model scale alone does not confer adversarial robustness. Code is available at https://github.com/UCF-ML-Research/REALM.

</details>

### 10. LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2606.23686) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4895)　📅 2026-06　🏷 ECCV 2026

**关键词**：`benchmark`、`LIBERO-Safety`、`physical constraint`、`semantic constraint`、`VLA security`、`semantic safety`

👤 **作者**：Rongxu Cui、…、Hao Zhao

- 🎯 **研究动机**：VLA 模型在严格约束下的操作安全基本未被验证，人工遥操作难以规模化生成安全关键场景
- 🔬 **研究方法**：提出参数化安全基准程序化生成高随机性场景，keypose 驱动数据生成管线产出 19,664 条严格无碰撞演示，系统评估 8 个 VLA 与 2 个具身基础模型
- 📌 **结论**：揭示泛化-安全张力：高多样性训练带来更安全轨迹，但任务成功仍受次优轨迹合成与语义错位瓶颈制约

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the impressive manipulation capabilities of Vision-Language-Action (VLA) models, their operational safety under strict constraints remains largely unverified. To address this, we introduce a parametric safety benchmark to procedurally generate safety-critical scenarios with comprehensive stochasticity. To overcome the scalability bottlenecks of human teleoperation, we develop a novel keypose-driven data generation pipeline. Leveraging this infrastructure, we curate a large-scale dataset of 19,664 strictly collision-free demonstrations with extensive domain randomization. We then conduct a systematic cross-paradigm evaluation of eight VLA and two embodied foundation models. Our analysis reveals a critical generalization-safety tension: although high-diversity training fosters safer trajectories, task success remains fundamentally bottlenecked by sub-optimal trajectory synthesis and semantic misalignment. By providing a scalable pipeline, a robust dataset, and profound failure-mode insights, LIBERO-Safety establishes a crucial foundation for developing safe and reliable VLA models.

</details>

### 11. ROBOSHACKLES: A Safety Dataset for Human-Injury Prevention in Embodied Foundation Models

📄 [arXiv](https://arxiv.org/abs/2606.18632) · 📊 [Dataset](https://huggingface.co/datasets/YZW00/RoboShackles)　📅 2026-06

**关键词**：`benchmark`、`human-injury prevention`、`embodied dataset`、`hazard grounding`

👤 **作者**：Zhuowen Yin、Chongyang Liu、Wenzhang Yang、Renjue Li、Yinxing Xue

- 🎯 **研究动机**：EFM 的人身伤害预防安全对齐未被探索，机器人伤人的真实数据无法安全合乎伦理地采集
- 🔬 **研究方法**：从真实 DROID 观测出发，经场景理解、危险感知图像编辑、时序提示生成与单遍 rollout 合成，用 Wan2.7 构建 10,000 段机器人视频数据集（两类直接伤害、四类间接伤害），并以拒答标准评估六个 EFM
- 📌 **结论**：所有被测模型在安全关键场景全部产生不安全动作（100% 不安全动作率），数据集可作为拒答学习与危险预判的可扩展基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Foundation Models (EFMs) integrate multimodal understanding, future-state reasoning, and executable robot actions. Yet their safety alignment for human-injury prevention remains underexplored, primarily because real-world data of robots harming humans or creating hazardous household situations cannot be safely or ethically collected. To address this challenge, we propose a safety-critical data construction pipeline for human-injury prevention in EFMs.Starting from real DROID observations, our construction pipeline proceeds through scene understanding, hazard-aware image editing, temporal prompt generation, and single-pass rollout synthesis. The temporal prompts specify the expected scene evolution, while Wan2.7 synthesizes realistic robotic rollouts from the edited hazardous states in a single pass. Using this pipeline, we construct ROBOSHACKLES, a 10,000-clip robotic video dataset derived from real DROID observations, spanning two direct-harm and four indirect-harm categories. To ensure dataset quality, we assess task completion and visual quality with automatic metrics, and evaluate six representative EFMs under a refusal-based safety criterion. Results show that all evaluated models produce unsafe actions in the tested safety-critical scenarios, yielding a 100% unsafe action generation rate. ROBOSHACKLES serves as a scalable benchmark and training resource for refusal learning and hazard anticipation before robot action execution.The dataset is publicly available at https://huggingface.co/datasets/YZW00/RoboShackles.

</details>

### 12. EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Evaluating Embodied VLMs as Runtime Safety Guards

📄 [arXiv](https://arxiv.org/abs/2607.00218)　📅 2026-06

**关键词**：`benchmark`、`egocentric video`、`runtime guard`、`hazard diagnosis`

👤 **作者**：Siddhant Panpatil、Arth Singh、Mijin Koo、Chaeyun Kim、Haon Park、Dasol Choi

- 🎯 **研究动机**：二元安全基准掩盖了可部署 guard 必须同时做到抓住真危险与不过度干预的区分
- 🔬 **研究方法**：构建 EgoSafetyBench：1,200 个机器人视角半秒粒度标注场景，情景轨（800 例四族）+视觉通道轨（400 例场景内误导文字），均用只差单一决定性线索的对比梯子
- 📌 **结论**：十个 VLM 能识别含危险视频却常错过具体危险时刻；误导性场景文字使脆弱模型漏掉三分之一危险、鲁棒模型过度干预，表面鲁棒常反映无差别报警而非物理推理

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) are now proposed as runtime safety guards for embodied agents in homes and factories. A deployable guard must catch genuinely unsafe situations while avoiding unnecessary intervention on routine but superficially alarming activity, a distinction that binary safety benchmarks obscure. We introduce EgoSafetyBench, an egocentric video benchmark of 1,200 robot-view scenarios annotated at half-second granularity, to evaluate VLMs as streaming guards across two tracks. The situational track (800 scenarios) spans four families, from routine and safe-but-suspicious scenes to obvious and contextual hazards. The visual-channel track (400 scenarios) targets in-scene text-a sign, sticker, or label visible in the scene-that can misrepresent the physical situation, pairing each misleading sign with a truthful version to test both whether a guard flags the text as misleading and whether the text corrupts its physical-safety judgment. Both tracks use contrastive ladders: near-identical scenarios differing only in a single visible deciding cue, so a correct call must hinge on that cue rather than the overall scene type. We evaluate ten open- and closed-source VLMs. We find that while guards reliably recognize videos containing hazards, they often miss specific hazardous moments, particularly contextual hazards. Furthermore, misleading in-scene signs degrade all tested guards: vulnerable models miss up to a third of hazards, while robust models over-intervene on safe content. Matched controls reveal that apparent safety robustness often reflects indiscriminate alarming rather than true physical reasoning.

</details>

### 13. RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents

📄 [arXiv](https://arxiv.org/abs/2605.19328) · 🌐 [Project](https://purseclab.github.io/benchmark-for-robotics-security/)　📅 2026-05

**关键词**：`benchmark`、`robot jailbreak`、`attack-defense evaluation`、`embodied agent`

👤 **作者**：Doguhuan Yeke、Yanming Zhou、Leo Y. Lin、Hongyu Cai、Antonio Bianchi、Z. Berkay Celik

- 🎯 **研究动机**：具身智能越狱评测依赖临时数据集与有限指标，重攻击成功而轻安全-效用权衡
- 🔬 **研究方法**：RoboJailBench：基于 ISO 标准、监管规则与真实事故的 18 类违规后果 taxonomy、成对对抗/良性目标的意图对照数据管线、集成攻击与防御的标准化评测仓库
- 📌 **结论**：提供具身 AI 越狱的首个标准化评估框架，扩充五个既有数据集并集成四攻击两防御评测主流具身 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Vision-Language Models (VLMs) facilitate a new class of embodied AI systems, where these models are integrated into physical platforms, e.g. robots and autonomous vehicles, to interpret visual scenes and execute natural language commands in diverse environments. Previous research has introduced jailbreak attacks and defenses for embodied AI. Their evaluations, however, rely on ad-hoc datasets, limited metrics, and emphasize attack success while neglecting the trade-off between security and the ability to follow benign commands. Existing benchmarks and evaluation frameworks either target traditional chat-based models or focus on non-adversarial safety evaluation for embodied AI; neither captures the adversarial risks, inputs, consequences, and evaluation criteria necessary for jailbreak attacks in embodied AI systems. In this paper, we address this gap with RoboJailBench, which consists of three core components. We establish a security taxonomy derived from ISO standards, regulatory rules, and documented incidents. This effort yields 18 categories of security violation consequences for embodied AI. We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility. Lastly, we provide an evolving repository with standardized metrics and a unified process for assessing and integrating new attacks and defenses. With this benchmark, we construct a new taxonomy-balanced dataset and augment five existing datasets. We integrate four attacks and two defenses to evaluate their performance on leading embodied VLMs. This benchmark provides the first standardized evaluation framework for jailbreak attacks in embodied AI and supports future research. We release our code, datasets, and artifacts, and maintain a leaderboard at https://purseclab.github.io/benchmark-for-robotics-security.

</details>

### 14. SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.19638) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1852/)　📅 2026-04　🏷 ACL 2026

**关键词**：`benchmark`、`safety-conscious planning`、`ALFRED`、`embodied VLM`

👤 **作者**：Josue Torres-Fonseca、…、Joyce Chai

- 🎯 **研究动机**：现有安全评测用脱离实体的 QA 评危险识别，忽略通过具身规划主动缓解风险的能力
- 🔬 **研究方法**：基于 ALFRED 增补六类真实厨房危险，评测 11 个 Qwen、Gemma、Gemini 模型的危险识别与具身风险缓解
- 📌 **结论**：模型在 QA 中能准确识别危险但平均缓解成功率明显偏低，静态 QA 不足以评估物理安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models are increasingly adopted as autonomous agents in interactive environments, yet their ability to proactively address safety hazards remains insufficient. We introduce SafetyALFRED, built upon the embodied agent benchmark ALFRED, augmented with six categories of real-world kitchen hazards. While existing safety evaluations focus on hazard recognition through disembodied question answering (QA) settings, we evaluate eleven state-of-the-art models from the Qwen, Gemma, and Gemini families on not only hazard recognition, but also active risk mitigation through embodied planning. Our experimental results reveal a significant alignment gap: while models can accurately recognize hazards in QA settings, average mitigation success rates for these hazards are low in comparison. Our findings demonstrate that static evaluations through QA are insufficient for physical safety, thus we advocate for a paradigm shift toward benchmarks that prioritize corrective actions in embodied contexts. We open-source our code and dataset under https://github.com/sled-group/SafetyALFRED.git

</details>

### 15. Composing Driving Worlds through Disentangled Control for Adversarial Scenario Generation

📄 [arXiv](https://arxiv.org/abs/2603.12864) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3714)　📅 2026-03　🏷 ECCV 2026

**关键词**：`benchmark`、`adversarial scenario`、`adversarial robustness`、`VLA safety`、`autonomous driving`、`video generation`

👤 **作者**：Yifan Zhan、…、Yinqiang Zheng

- 🎯 **研究动机**：可控生成模型对场景结构、对象身份与自车动作的引导相互纠缠，难以合成安全关键的长尾组合
- 🔬 **研究方法**：CompoSIA 解耦交通要素：噪声级身份注入实现跨位姿的单图身份替换，层级双分支动作控制提升动作可控性，系统组合安全要素为危险配置
- 📌 **结论**：身份编辑 FVD 提升 17%、旋转与平移误差降 30%/47%；下游压测中规划器 3 秒平均碰撞率增加 173%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A major challenge in autonomous driving is the "long tail" of safety-critical edge cases, which often emerge from unusual combinations of common traffic elements. Synthesizing these scenarios is crucial, yet current controllable generative models provide incomplete or entangled guidance, preventing the independent manipulation of scene structure, object identity, and ego actions. We introduce CompoSIA, a compositional driving video simulator that disentangles these traffic factors, enabling fine-grained control over diverse adversarial driving scenarios. To support controllable identity replacement of scene elements, we propose a noise-level identity injection, allowing pose-agnostic identity generation across diverse element poses, all from a single reference image. Furthermore, a hierarchical dual-branch action control mechanism is introduced to improve action controllability. Such disentangled control enables adversarial scenario synthesis-systematically combining safe elements into dangerous configurations that entangled generators cannot produce. Extensive comparisons demonstrate superior controllable generation quality over state-of-the-art baselines, with a 17% improvement in FVD for identity editing and reductions of 30% and 47% in rotation and translation errors for action control. Furthermore, downstream stress-testing reveals substantial planner failures: across editing modalities, the average collision rate of 3s increases by 173%.

</details>

### 16. When Helpers Become Hazards: A Benchmark for Analyzing Multimodal LLM-Powered Safety in Daily Life

📄 [arXiv](https://arxiv.org/abs/2601.04043) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1446/)　📅 2026-01　🏷 ACL 2026

**关键词**：`benchmark`、`SaLAD`、`implicit visual risk`、`actionable warning`

👤 **作者**：Xinyue Lou、…、Kaiyu Huang

- 🎯 **研究动机**：MLLM 日常场景回复对人类行为的安全影响缺乏评测，且风险需图文跨模态推理才可判断
- 🔬 **研究方法**：SaLAD 含 2013 个真实图文样本、10 类日常场景，平衡覆盖不安全与过度敏感案例，并提出基于安全警告的评测框架，鼓励给出具体警示而非泛化拒绝
- 📌 **结论**：18 个 MLLM 中最佳模型对不安全查询的安全回复率仅 57.2%，流行安全对齐方法在此场景也收效有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Multimodal Large Language Models (MLLMs) become an indispensable assistant in human life, the unsafe content generated by MLLMs poses a danger to human behavior, perpetually overhanging human society like a sword of Damocles. To investigate and evaluate the safety impact of MLLMs responses on human behavior in daily life, we introduce SaLAD, a multimodal safety benchmark which contains 2,013 real-world image-text samples across 10 common categories, with a balanced design covering both unsafe scenarios and cases of oversensitivity. It emphasizes realistic risk exposure, authentic visual inputs, and fine-grained cross-modal reasoning, ensuring that safety risks cannot be inferred from text alone. We further propose a safety-warning-based evaluation framework that encourages models to provide clear and informative safety warnings, rather than generic refusals. Results on 18 MLLMs demonstrate that the top-performing models achieve a safe response rate of only 57.2% on unsafe queries. Moreover, even popular safety alignment methods limit effectiveness of the models in our scenario, revealing the vulnerabilities of current MLLMs in identifying dangerous behaviors in daily life. Our dataset is available at https://github.com/xinyuelou/SaLAD.

</details>

### 17. SENTINEL: A Multi-Level Formal Framework for Safety Evaluation of Foundation Model-based Embodied Agents

📄 [arXiv](https://arxiv.org/abs/2510.12985)　📅 2025-10

**关键词**：`benchmark`、`formal safety`、`multi-level evaluation`、`embodied agent`

👤 **作者**：Simon Sinong Zhan、…、Qi Zhu

- 🎯 **研究动机**：具身 Agent 安全评估依赖启发式规则或主观 FM 判断，缺乏统一的形式化框架
- 🔬 **研究方法**：SENTINEL 把安全需求形式化为时序逻辑公式，在语义、计划、轨迹三层分别验证 Agent 的理解对齐、计划合规与执行轨迹
- 📌 **结论**：在 VirtualHome 与 AI2-THOR 中系统暴露多个 FM 具身 Agent 在理解、规划与执行各层的安全违规

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present SENTINEL, a framework for formally evaluating the physical safety of foundation model (FM)-based embodied agents. SENTINEL is the first to provide multi-level safety evaluation across semantic interpretation, plan generation, and physical execution within a unified formal framework. Unlike prior methods that rely on heuristic rules or subjective FM judgments, SENTINEL grounds practical safety requirements in formal temporal logic (TL) semantics that can precisely specify state invariants, temporal dependencies, and timing constraints. It employs a multi-level verification pipeline where (i) at the semantic level, intuitive natural language safety requirements are formalized into TL formulas and the agent's understanding of these requirements is probed for alignment with the TL formulas; (ii) at the plan level, high-level action plans and subgoals generated by the agent are verified against the TL formulas to detect unsafe plans before execution; and (iii) at the trajectory level, multiple execution trajectories are merged into a computation tree and efficiently verified against physically-detailed TL specifications for a final safety check. We apply SENTINEL in VirtualHome and AI2-THOR, and formally evaluate multiple FM-based embodied agents against diverse safety requirements. Our experiments show that by grounding physical safety in temporal logic and applying verification methods across multiple levels, SENTINEL provides a rigorous foundation for systematically evaluating the safety of FM-based embodied agents in simulation-based physical environments, and can effectively expose potential safety violations in interpreting, planning, and executing the tasks.

</details>

### 18. IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks

📄 [arXiv](https://arxiv.org/abs/2506.16402) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40880)　📅 2025-06　🏷 AAAI 2026

**关键词**：`benchmark`、`interactive safety`、`household task`、`safe completion`

👤 **作者**：Xiaoya Lu、…、Jing Shao

- 🎯 **研究动机**：静态非交互评测无法评估交互环境中动态涌现的风险，事后评估漏掉不安全中间步骤
- 🔬 **研究方法**：提出 IS-Bench：高保真模拟器中 161 个场景 388 项安全风险，首创过程导向评估验证风险缓解动作的时序正确性
- 📌 **结论**：GPT-4o 与 Gemini-2.5 系列均缺交互安全意识；safety-aware CoT 有提升但常牺牲任务完成率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Flawed planning from VLM-driven embodied agents poses significant safety hazards, hindering their deployment in real-world household tasks. However, existing static, non-interactive evaluation paradigms fail to adequately assess risks within these interactive environments, since they cannot simulate dynamic risks that emerge from an agent's actions and rely on unreliable post-hoc evaluations that ignore unsafe intermediate steps. To bridge this critical gap, we propose evaluating an agent's interactive safety: its ability to perceive emergent risks and execute mitigation steps in the correct procedural order. We thus present IS-Bench, the first multi-modal benchmark designed for interactive safety, featuring 161 challenging scenarios with 388 unique safety risks instantiated in a high-fidelity simulator. Crucially, it facilitates a novel process-oriented evaluation that verifies whether risk mitigation actions are performed before/after specific risk-prone steps. Extensive experiments on leading VLMs, including the GPT-4o and Gemini-2.5 series, reveal that current agents lack interactive safety awareness, and that while safety-aware Chain-of-Thought can improve performance, it often compromises task completion. By highlighting these critical limitations, IS-Bench provides a foundation for developing safer and more reliable embodied AI systems. Code and data are released under https://github.com/AI45Lab/IS-Bench.

</details>

### 19. AGENTSAFE: Benchmarking the Safety of Embodied Agents on Hazardous Instructions

📄 [arXiv](https://arxiv.org/abs/2506.14697) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Ying_AGENTSAFE_Benchmarking_the_Safety_of_Embodied_Agents_on_Hazardous_Instructions_CVPR_2026_paper.html)　📅 2025-06　🏷 CVPR 2026

**关键词**：`benchmark`、`embodied agent`、`hazardous instruction`、`physical safety`

👤 **作者**：Zonghao Ying、…、Xianglong Liu

- 🎯 **研究动机**：具身 agent 安全基准覆盖面窄且只看最终结果，忽略感知-规划-执行全过程的失效模式
- 🔬 **研究方法**：提出 AGENTSAFE：THOR 对抗仿真沙箱、受阿西莫夫三定律启发的 45 场景 1350 任务 9900 指令套件与多层细粒度评估协议
- 📌 **结论**：九个 SoTA VLM 均系统性暴露危险识别无法转化为安全规划与执行的缺陷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The integration of vision-language models (VLMs) is driving a new generation of embodied agents capable of operating in human-centered environments. However, as deployment expands, these systems face growing safety risks, particularly when executing hazardous instructions. Current safety evaluation benchmarks remain limited: they cover only narrow scopes of hazards and focus primarily on final outcomes, neglecting the agent's full perception-planning-execution process and thereby obscuring critical failure modes. Therefore, we present SAFE, a benchmark for systematically assessing the safety of embodied VLM agents on hazardous instructions. SAFE comprises three components: SAFE-THOR, an extensible adversarial simulation sandbox with a universal adapter that maps high-level VLM outputs to low-level embodied controls, supporting diverse agent workflow integration; SAFE-VERSE, a risk-aware task suite inspired by Asimov's Three Laws of Robotics, comprising 45 adversarial scenarios, 1,350 hazardous tasks, and 9,900 instructions that span risks to humans, environments, and agents; and SAFE-DIAGNOSE, a multi-level and fine-grained evaluation protocol measuring agent performance across perception, planning, and execution. Applying SAFE to nine state-of-the-art VLMs and two embodied agent workflows, we uncover systematic failures in translating hazard recognition into safe planning and execution. Our findings reveal fundamental limitations in current safety alignment and demonstrate the necessity of a comprehensive, multi-stage evaluation for developing safer embodied intelligence.

</details>

### 20. Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency

📄 [arXiv](https://arxiv.org/abs/2608.29583)　📅 2026-09

**关键词**：`detection`、`runtime trajectory monitoring`、`CoT-action consistency`、`unsafe driving`、`reasoning reliability`、`runtime monitor`

👤 **作者**：Tian Yu、Lu Feng、Sebastian Elbaum

- 🎯 **研究动机**：驾驶 VLA 会输出显式 CoT，但其能否作为 runtime 规格交叉校验轨迹缺乏证据
- 🔬 **研究方法**：构建基于 NVIDIA Alpamayo 1.5 的 150 对人工标注 CoT-trajectory 数据集 DriveAlignBench，并开发 lane-relative F-LLM 等自动一致性 monitor
- 📌 **结论**：33.3% 的 CoT 本身不可靠，可靠 CoT 中仅 74% 与轨迹一致；最佳 monitor 达 F1=0.75，比最强 raw-waypoint LLM 基线高 0.13

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous vehicles (AVs) operate in complex environments where failures are consequential. Sophisticated machine learning models for perception and planning are key to overcoming at least part of that complexity, but their black-box nature complicates validation and verification (V&V). The recent integration of Vision-Language-Action (VLA) models into AVs introduces a unique opportunity: besides generating trajectories, these models produce an explicit Chain-of-Thought (CoT) explaining their underlying rationale. This CoT provides a rich specification to cross-check model outputs and detect inconsistencies that may expose unsafe or unintended behavior. This paper assesses whether CoTs from a recent open driving VLA can support such monitoring. We curate DriveAlignBench, a specialized dataset from NVIDIA's Alpamayo 1.5 VLA for AVs containing 150 CoT-trajectory pairs, which we manually annotate for reliability, trajectory consistency, and safety. Our analysis reveals that 33.3% of CoTs are unreliable. Among reliable CoTs, the generated trajectory is consistent with the CoT in 74% of cases. Leveraging this potential, we propose integrating a CoT-trajectory consistency check into a runtime monitor. The check is nontrivial: CoTs express open-vocabulary, scene-relative driving commitments, while trajectories are low-level ego-motion sequences whose semantics depend on road geometry and motion context. To bridge this gap, we develop a family of automated consistency monitors. Our best monitor, lane-relative F-LLM with GPT-5.5, achieves F1 = 0.75, improving over the strongest raw-waypoint LLM baseline by +0.13 absolute F1 and over a rule-based monitor by +0.38. We release DriveAlignBench, the monitor implementations, and annotation tools at https://github.com/776styjsu/drive-the-thoughts.

</details>

### 21. Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation

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

### 22. RiskWorld: Object-Centric Latent World Modeling for Autonomous Driving Risk Identification

📄 [arXiv](https://arxiv.org/abs/2608.21414)　📅 2026-08

**关键词**：`detection`、`embodied world model`、`predictive rollout`、`object-level risk`、`autonomous driving risk`、`object-level hazard localization`

👤 **作者**：Jingzheng Li、…、Xianglong Liu

- 🎯 **研究动机**：自动驾驶风险识别多预测场景级事故或做事后几何检查，未直接利用预测的 ego–object 关系定位风险来源
- 🔬 **研究方法**：RiskWorld 对象中心潜在世界模型：融合预训练预测视频表征与结构化 ego–object 历史，用 RSSM 式潜在动力学 rollout 关系感知对象状态并解码对象级风险分数
- 📌 **结论**：RiskBench 上总体 F1 63.0% 最佳、误报率最低 2.1%；rollout 可在临界事件前捕捉对象级风险演化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous driving risk identification aims to determine which observed object is likely to become safety-critical to the ego vehicle. Existing approaches typically predict scene-level accidents, infer risk objects indirectly from ego behavior, or apply geometric checks after trajectory forecasting, without directly using predicted ego--object relations for risk-source localization. We propose RiskWorld, an object-centric latent world model that identifies risk from the imagined evolution of each candidate relative to the ego vehicle. RiskWorld combines pretrained predictive video representations with structured ego--object histories, contextualizes observed interactions, and rolls relation-aware object states into the future using RSSM-style latent dynamics. It decodes the rollout into object-level risk scores, supported by auxiliary future-relation and temporal-risk predictions. Inference uses only observations up to the current time, while logged futures provide training supervision. On RiskBench, RiskWorld achieves the best overall F1 of 63.0\% and the lowest false-alarm rate of 2.1\%. Further analyses show that the learned rollout captures the evolution of object-level risk before critical events, while RiskWorld's selections preserve planning-critical information under filtered observation.

</details>

### 23. ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency

📄 [arXiv](https://arxiv.org/abs/2607.29169)　📅 2026-07

**关键词**：`defense`、`runtime safeguard`、`visual-action consistency`、`failure intervention`

👤 **作者**：Wenda Yu、Tianshi Wang、Fengling Li、Xin Li、Jingjing Li、Lei Zhu

- 🎯 **研究动机**：VLA 策略在运行时扰动下出现视觉观测、机器人状态与动作的时序失配，缺乏免重训的防护
- 🔬 **研究方法**：ActFovea 构建动作条件化注视区域保留接触相关视野，检测视觉运动与几何/本体感知的一致性，可恢复扰动需验证恢复动作、不可恢复时触发有界安全失效
- 📌 **结论**：π0 在 LIBERO 局部视觉遮挡下成功率从 49.3% 升至 90.3%，弥补 93.7% 差距；动作漂移与视觉延迟分别提升 7.0/9.8 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying the underlying VLA policy. ActFovea uses robot kinematics, proprioceptive states, and recent actions to construct action-conditioned foveated regions that retain contact-relevant areas and predicted motion corridors while suppressing task-irrelevant visual content. It detects runtime risks by evaluating whether visual motion and observation freshness remain consistent with geometric, proprioceptive, and action transitions. For recoverable disturbances, ActFovea constructs disturbance-specific candidate observations and accepts a recovery only after verifying the resulting action chunk. When stale or replayed observations make reliable recovery impossible, it invokes a bounded safe-failure procedure. In closed-loop evaluations of $π_0$ across multiple LIBERO suites, ActFovea increases success under localized visual overlays from 49.3\% to 90.3\%, closing 93.7\% of the gap to clean performance. It further improves success under action drift and visual delay by 7.0 and 9.8 percentage points, respectively, while preserving clean-task performance. Under frozen-observation replay, ActFovea triggers timely safe failure in all trials, with no unprotected failures. These results demonstrate that spatiotemporal visual-action consistency provides an effective basis for runtime safeguarding of VLA policies.

</details>

### 24. When Words Are Safe But Actions Kill: Probing Physical Jailbreak Beyond Textual Jailbreak in Hidden-State Risk Space

📄 [arXiv](https://arxiv.org/abs/2607.15218)　📅 2026-07

**关键词**：`detection`、`hidden-state probe`、`physical danger`、`action risk`

👤 **作者**：Weimeng Wang、Ziqiang Wang、Zihang Zhan、Chuanpu Fu、Qi Li、Ke Xu

- 🎯 **研究动机**：语言良性但物理落地后不安全的指令（physical jailbreak）是否与文本越狱是同一安全问题未知
- 🔬 **研究方法**：经隐藏状态方向分析与随机划分零检验证明 TJ 与 PJ 在表示上可分；提出 PRISM 单层 L2 正则逻辑探针，并构建交互平衡的 PJB-2K 对照集排除词汇捷径
- 📌 **结论**：PRISM 在 SafeAgentBench 达 86.2-87.7% 准确率、FPR 11.7-13.7%（同规模 LLM judge FPR 24.7-39.0%）；PJB-2K 上 0.671 平衡准确率超过 Qwen2.5 系列判断者（0.538-0.577）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whether this physically grounded jailbreak is the same safety problem as ordinary textual jailbreak. Through hidden-state direction analysis and random-split null tests, we show that textual jailbreak (TJ) and physical jailbreak (PJ) form separable signals in LLM representations across Qwen2.5-3B/7B/14B/32B, Phi-3.5 and SmolLM2. Building on this separability, we propose PRISM, a single-layer L2-regularized logistic probe over full hidden states. PRISM achieves 86.2--87.7\% accuracy on SafeAgentBench with 11.7--13.7\% false-positive rates (FPRs), while same-scale LLM judges over-block safe tasks at 24.7--39.0\% FPR. To test whether the result survives lexical-shortcut controls, we introduce an interaction-balanced revision of PhysicalJailbreakBench-2K (PJB-2K): a fixed 2{,}000-row comparison set sampled by label and physical mechanism from a larger object--site construction. On the underlying 10{,}000-row pool, word-TFIDF and the embedding layer remain at chance (AUC 0.497 and 0.500). At layer 25, selected by an i.i.d. sweep, cell-grouped cross-validation gives PRISM 0.718 AUC, compared with 0.398 for a physics-free label control under the same protocol. On the identical 2{,}000 comparison rows, these PRISM predictions obtain 0.671 balanced accuracy, while Qwen2.5 judges from 3B to 72B obtain 0.538--0.577 and exhibit high FPR. These results support hidden-state probing as a representation-level method for physical safety beyond text moderation, without relying on the near-perfect scores of shortcut-prone paired templates.

</details>

### 25. LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents

📄 [arXiv](https://arxiv.org/abs/2606.31045)　📅 2026-06

**关键词**：`defense`、`laboratory rule`、`runtime guard`、`constraint grounding`

👤 **作者**：Jingpu Yang、…、Zhuohan Xie

- 🎯 **研究动机**：实验室安全规则、手册与 SOP 是自然语言，缺少转化为机器可查运行时约束的中间步骤
- 🔬 **研究方法**：提出 LabGuard 套件：LabGuard-IR 类型化可执行表示、812 条监督标注的 LabGuard-Bench、把规则映射到 IR 的 Grounder，编译为运行时监视器在控制器边界施加
- 📌 **结论**：泛化到未见规则源，任务范围 F1 79.4，不安全事件从 39.5% 降至 23.8%；LabUtopia 中与 ACT 集成干预率低于 0.5% 且保留任务成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating procedures, into machine-checkable runtime constraints. We introduce LabGuard (Laboratory Guard), a language-to-execution safety suite that grounds natural-language laboratory rules into executable specifications and deploys them as runtime guards. LabGuard includes three core components: LabGuard-IR, which defines a typed executable representation; LabGuard-Bench, which provides 812 supervised annotations expanded from 203 seed laboratory rules; and LabGuard-Grounder, which maps natural-language laboratory rules into LabGuard-IR. The resulting IR instances are handled by the LabGuard Pipeline, which compiles them into runtime monitors and applies them at the controller boundary. Experiments show that LabGuard generalizes to unseen laboratory-rule sources, achieves 79.4 task-scope F1, and reduces unsafe events from 39.5% to 23.8% after monitor compilation. In LabUtopia, its runtime monitors integrate with ACT, keeping interventions below 0.5% while preserving task success.

</details>

### 26. EMBGUARD: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents

📄 [arXiv](https://arxiv.org/abs/2605.30924) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63023)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`hazard-aware guardrail`、`safe planning`、`embodied agent`、`agent safety`、`mechanistic analysis`

👤 **作者**：Dongwook Choi、…、Jinyoung Yeo

- 🎯 **研究动机**：具身 agent 缺显式危险识别与动作条件风险推理机制，要么漏风险要么过度识别
- 🔬 **研究方法**：EMBGuard 首个 MLLM 具身安全护栏：评估（视觉观察，动作）对识别危险配置并给自然语言风险解释；附 15.1K 动作条件对数据集 EMBHazard 与 329 场景七类物理风险的 EMBGuardTest
- 📌 **结论**：2B 与 4B 紧凑模型性能比肩 GPT-5.1、Gemini-2.5-Pro，且显著降低阻碍实时部署的误报率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

MLLM-powered embodied agents deployed in real-world environments encounter physical hazards. However, existing approaches lack explicit mechanisms for identifying hazards and reasoning about action-conditioned risks, leading agents to either miss risky interactions or over-identify risks. To address this, we propose EMBGuard, the first MLLM-based safety guardrail for embodied agents designed to decouple physical risk reasoning from agent policy. By evaluating a (visual observation, action) pair, EMBGuard identifies hazardous configurations and provides natural language explanations of potential risks. Alongside EMBGuard, we contribute EMBHazard, a training dataset of 15.1K action-conditioned pairs, and EMBGuardTest, a benchmark of 329 manually curated real-world scenarios spanning seven physical risk categories. Through compositional variation of hazards and actions, we generate diverse risky and benign scenarios that agents may encounter during planning. Despite its compact size (2B, 4B), EMBGuard achieves performance competitive with proprietary MLLMs (e.g., GPT-5.1, Gemini-2.5-Pro) while significantly reducing the false-positive rates that hinder real-time deployment. We make the code, data, and models publicly available at https://github.com/dongwxxkchoi/EMBGuard

</details>

### 27. HomeGuard: VLM-based Embodied Safeguard for Identifying Contextual Risk in Household Task

📄 [arXiv](https://arxiv.org/abs/2603.14367) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5762)　📅 2026-03　🏷 ECCV 2026

**关键词**：`defense`、`household safeguard`、`contextual risk`、`VLM guard`、`embodied safety`、`active perception`

👤 **作者**：Xiaoya Lu、…、Jing Shao

- 🎯 **研究动机**：良性指令可因细微环境状态变得危险，规则法在物体密集场景难扩展，提示工程感知涣散致漏检或幻觉
- 🔬 **研究方法**：HomeGuard 以 CG-CoT 把风险评估分解为锚定交互目标的主动感知加基于视觉证据的语义判断，配 grounding 数据集与过程奖励 RFT 两阶段训练
- 📌 **结论**：风险匹配率超基座模型 30% 以上且降低过度安全；视觉锚点还可作下游规划器的显式空间约束

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) empower embodied agents to execute complex instructions, yet they remain vulnerable to contextual safety risks where benign commands become hazardous due to subtle environmental states. Existing safeguards often prove inadequate. Rule-based methods lack scalability in object-dense scenes, whereas model-based approaches relying on prompt engineering suffer from unfocused perception, resulting in missed risks or hallucinations. To address this, we propose an architecture-agnostic safeguard featuring Context-Guided Chain-of-Thought (CG-CoT). This mechanism decomposes risk assessment into active perception that sequentially anchors attention to interaction targets and relevant spatial neighborhoods, followed by semantic judgment based on this visual evidence. We support this approach with a curated grounding dataset and a two-stage training strategy utilizing Reinforcement Fine-Tuning (RFT) with process rewards to enforce precise intermediate grounding. Experiments demonstrate that our model HomeGuard significantly enhances safety, improving risk match rates by over 30% compared to base models while reducing oversafety. Beyond hazard detection, the generated visual anchors serve as actionable spatial constraints for downstream planners, facilitating explicit collision avoidance and safety trajectory generation. Code and data are released under https://github.com/AI45Lab/HomeGuard

</details>

### 28. RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic

📄 [arXiv](https://arxiv.org/abs/2512.21220)　📅 2025-12

**关键词**：`defense`、`executable safety logic`、`runtime verification`、`embodied agent`

👤 **作者**：Le Wang、…、Xianglong Liu

- 🎯 **研究动机**：静态规则过滤与 prompt 级控制难以应对动态、时序依赖且上下文丰富环境中的隐式风险
- 🔬 **研究方法**：RoboSafe 以可执行谓词安全逻辑做运行时防护，在混合长短期安全记忆上结合反向反思推理（回溯轨迹推断时序谓词并触发重规划）与前向预测推理（依长期记忆与多模态观察预判风险）
- 📌 **结论**：危险动作发生减少 36.8% 且任务性能接近原水平，物理机械臂实机验证可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied agents powered by vision-language models (VLMs) are increasingly capable of executing complex real-world tasks, yet they remain vulnerable to hazardous instructions that may trigger unsafe behaviors. Runtime safety guardrails, which intercept hazardous actions during task execution, offer a promising solution due to their flexibility. However, existing defenses often rely on static rule filters or prompt-level control, which struggle to address implicit risks arising in dynamic, temporally dependent, and context-rich environments. To address this, we propose RoboSafe, a hybrid reasoning runtime safeguard for embodied agents through executable predicate-based safety logic. RoboSafe integrates two complementary reasoning processes on a Hybrid Long-Short Safety Memory. We first propose a Backward Reflective Reasoning module that continuously revisits recent trajectories in short-term memory to infer temporal safety predicates and proactively triggers replanning when violations are detected. We then propose a Forward Predictive Reasoning module that anticipates upcoming risks by generating context-aware safety predicates from the long-term safety memory and the agent's multimodal observations. Together, these components form an adaptive, verifiable safety logic that is both interpretable and executable as code. Extensive experiments across multiple agents demonstrate that RoboSafe substantially reduces hazardous actions (-36.8% risk occurrence) compared with leading baselines, while maintaining near-original task performance. Real-world evaluations on physical robotic arms further confirm its practicality. Code will be released upon acceptance.

</details>

### 29. VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer

📄 [arXiv](https://arxiv.org/abs/2512.11891) · 🌐 [Project](https://vlsa-aegis.github.io/)　📅 2025-12

**关键词**：`defense`、`AEGIS`、`safety constraint layer`、`plug-and-play VLA`

👤 **作者**：Songqiao Hu、…、Xiao He

- 🎯 **研究动机**：VLA 部署于非结构化环境需同时保证任务遵循与碰撞安全，直接修改或重训大模型成本高
- 🔬 **研究方法**：VLSA/AEGIS 架构引入以 control barrier function 形式化的即插即用安全约束层，直接与现有 VLA 集成并提供理论保证，配套构建 SafeLIBERO 安全关键基准
- 📌 **结论**：避障率提升超 50%，任务成功率反而提高近 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in generalizing across diverse robotic manipulation tasks. However, deploying these models in unstructured environments remains challenging due to the critical need for simultaneous task compliance and safety assurance, particularly in preventing potential collisions during physical interactions. In this work, we introduce a Vision-Language-Safe Action (VLSA) architecture, named AEGIS, which contains a plug-and-play safety constraint (SC) layer formulated via control barrier functions. AEGIS integrates directly with existing VLA models to improve safety with theoretical guarantees, while maintaining their original instruction-following performance. To evaluate the efficacy of our architecture, we construct a comprehensive safety-critical benchmark SafeLIBERO, spanning distinct manipulation scenarios characterized by varying degrees of spatial complexity and obstacle intervention. Extensive experiments demonstrate the superiority of our method over state-of-the-art baselines. Notably, AEGIS achieves over 50% improvement in obstacle avoidance rate while substantially increasing the task success rate by nearly 10%. All benchmark datasets, code, and supplementary materials are publicly available at https://vlsa-aegis.github.io/.

</details>

### 30. SafeBranch: Branch-Pair Safety Alignment for Embodied Agents

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

### 31. Structure-Aware Robust Fine-Tuning: Defending Vision-Language-Action Robots Against Physical Attention Hijacking

📄 [arXiv](https://arxiv.org/abs/2608.03231)　📅 2026-08

**关键词**：`defense`、`robust fine-tuning`、`physical patch`、`structure awareness`

👤 **作者**：Jinquan Zhang、Dongfu Yin、Run Yang、Yufeng Yan、Zhen Tian、F. Richard Yu

- 🎯 **研究动机**：物理可实现的对抗贴片通过劫持动作-视觉注意力可靠破坏 VLA 策略，缺乏机制级防御
- 🔬 **研究方法**：AGSD 攻击用 EOT 优化可打印贴片同时集中注意力并破坏视觉-语言语义对齐；SARF 仅微调视觉编码器，结合特征锚定、策略关键注意力校正与语言引导几何一致性
- 📌 **结论**：LIBERO 上 AGSD 下 OpenVLA 失败率从 100% 降至平均 28.6%；真实 PiPER 机械臂平均成功率从 23.0% 升至 65.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) policies promise general robotic manipulation, but their robustness against physical-world attacks remains fragile. In particular, we show that physically realizable adversarial patches can reliably induce failures by triggering a mechanism we call policy-critical action-to-vision attention hijacking, where action-conditioned attention is diverted from task-relevant regions to a localized patch. To demonstrate the threat, we propose Attention-Guided Semantic Disruption (AGSD), an Expectation-over-Transformation (EOT) optimized printable patch that jointly (i) concentrates action-to-vision attention on the patch and (ii) disrupts vision-language semantic alignment, yielding strong cross-task and cross-architecture transfer. To mitigate such attacks, we introduce Structure-Aware Robust Fine-Tuning (SARF), a zero-inference-overhead defense that fine-tunes only the visual encoder using feature anchoring, policy-critical attention correction, and language-guided geometric consistency restricted to semantically relevant regions. On LIBERO, SARF reduces OpenVLA's failure rate under AGSD from 100% to 14.2%-56.8% (28.6% average) across suites while preserving clean performance, and on a real PiPER manipulator it improves average success under AGSD from 23.0% to 65.0%. These results highlight mechanism-level robustness as a practical path to securing VLA robots against physical attention hijacking.

</details>

### 32. VLAGuard: A Framework for Evaluating and Mitigating Physical Attention Hijacking in Vision-Language-Action Robots within Wireless Sensor Networks

📄 [arXiv](https://arxiv.org/abs/2608.01028)　📅 2026-08

**关键词**：`defense`、`attention hijacking`、`wireless robotics`、`robust evaluation`

👤 **作者**：Dongfu Yin、Jinquan Zhang

- 🎯 **研究动机**：无线传感网中的 VLA 机器人面临物理贴片劫持动作-视觉注意力的威胁，缺乏评估与缓解手段
- 🔬 **研究方法**：提出 VASA 可打印贴片压力测试模块与 Attention-Protective Fine-Tuning（APFT）防御，稳定时空注意力并强制几何一致性、零推理开销
- 📌 **结论**：LIBERO 中 OpenVLA 失败率从 100% 降至 25.9%；2000 次真实试验中严重贴片攻击下平均成功率从 23.0% 升至 67.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying Vision-Language-Action (VLA) robots as mobile edge nodes within wireless sensor networks (WSNs) requires robust protection against physical adversarial threats. We present VLAGuard, a framework to assess and mitigate a critical vulnerability: policy-critical action-to-vision attention hijacking. We first introduce a stress-test module, Visuomotor Attention-guided Semantic Attack (VASA), using printable patches to severely distract the robot's action-conditioned cross-attention. To counter this, we propose Attention-Protective Fine-Tuning (APFT), a defense that stabilizes spatiotemporal attention and enforces geometric consistency with zero inference overhead. Evaluations across simulated and physical WSN-assisted smart environments demonstrate significant robustness gains. APFT reduces the OpenVLA failure rate from 100.0% to 25.9% in LIBERO simulations. Furthermore, across 2,000 real-world trials, APFT improves the average success rate from 23.0% to 67.4% under severe patch attacks. This highlights that protecting attention pathways is important for improving the robustness of VLA-driven edge nodes in sensor networks.

</details>

### 33. SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning

📄 [arXiv](https://arxiv.org/abs/2503.03480) · 🌐 [Project](https://pku-safevla.github.io/) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e185c7be603426028c32ae1003a59d78-Abstract-Conference.html)　📅 2025-03　🏷 NeurIPS 2025

**关键词**：`defense`、`VLA alignment`、`constrained learning`、`safe policy`

👤 **作者**：Borong Zhang、…、Yaodong Yang

- 🎯 **研究动机**：VLA 部署缺乏显式安全约束集成，标准模仿学习只拟合演示动作
- 🔬 **研究方法**：ISA 框架：系统建模安全要求、主动诱发多样不安全行为、在 CMDP 范式下以 min-max 优化做安全强化学习并做针对性评估
- 📌 **结论**：较 SOTA 累计违规代价降 83.58% 且任务成功率反升 3.85%，安全行为可泛化到分布外扰动

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, reducing the cumulative cost of safety violations by 83.58% compared to the state-of-the-art method, while also maintaining task success rate (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. The effectiveness is evaluated on long-horizon mobile manipulation tasks. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io.

</details>

### 34. Towards General Language-Conditioned Latent Safety Filters

📄 [arXiv](https://arxiv.org/abs/2608.00315)　📅 2026-07

**关键词**：`defense`、`VLM safety`、`VLA safety`、`physical hazard`

👤 **作者**：Ihab Tabbara、Yuxuan Yang、Hussein Sibai

- 🎯 **研究动机**：现有机器人安全过滤器绑定特定约束，安全需求变化时须重设计或重学习
- 🔬 **研究方法**：研究语言条件化安全过滤：以自然语言指定约束的 Hamilton-Jacobi 安全 actor-critic，在 pick-and-place、擦桌、堆叠任务上评测约束执行与迁移
- 📌 **结论**：语言条件安全过滤能减少约束违反，并对未见过的同族约束实例展现部分迁移能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Robot policies are becoming increasingly general, with vision-language-action (VLA) models enabling a single policy to execute diverse tasks specified in natural language. Safe deployment, however, requires adapting not only to new tasks but also to varying safety requirements across users, environments, and applications. Existing safety filters remain largely constraint-specific and thus must be redesigned or relearned when safety requirements change. In this paper, we investigate language-conditioned safety filtering, in which a Hamilton-Jacobi safety actor and critic are conditioned on language-specified constraints. We evaluate this formulation across pick-and-place, table-wiping, and block-stacking tasks in the vision-based setting, examining its ability to enforce language-specified constraints and transfer to unseen constraint instances within the evaluated constraint families. Our experiments provide evidence that language-conditioned safety filters reduce constraint violations and exhibit partial transfer to unseen constraint instances.

</details>

### 35. SMD: Multi-view Safety-Critical Driving Video Generation in the Real-world Domain

🌐 [Project](https://icml-2.github.io/SMD/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61036)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`video generation`、`unsafe synthesis`、`temporal consistency`、`embodied safety`、`diffusion model`

👤 **作者**：Jiawei Zhou、Linye Lyu、Zhuotao Tian、Cheng Zhuo、YU LI

- 🎯 **研究动机**：安全关键场景稀有，现有生成器只产轨迹、仿真或单视角视频，不满足现代自动驾驶系统实际消费的真实多视角视频
- 🔬 **研究方法**：提出 SMD：GRPO 微调的 VLM 选择最易致险车辆，两阶段轨迹过程先生成碰撞再转化为自然规避轨迹，扩散模型把轨迹渲染成多视角视频
- 📌 **结论**：生成视频在压测多个端到端规划器时显著提高碰撞率，并入训练后降低碰撞率并提升规划器鲁棒性与安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical scenarios are essential for evaluating autonomous driving (AD) systems, yet they are rare in practice. Existing generators produce trajectories, simulations, or single-view videos—but they don’t meet what modern AD systems actually consume: realistic multi-view video. We present SMD, the first framework for generating multi-view safety-critical driving videos in the real-world domain. SMD couples a safety-critical trajectory engine with a diffusion-based multi-view video generator through three design choices. First, we pick the right adversary: a GRPO-fine-tuned vision-language model (VLM) that understands multi-camera context and selects vehicles most likely to induce hazards. Second, we generate the right motion: a two-stage trajectory process that (i) produces collisions, then (ii) transforms them into natural evasion trajectories—preserving risk while staying within what current video generators can faithfully render. Third, we synthesize the right data: a diffusion model that turns these trajectories into multi-view videos suitable for end-to-end planners. Videos generated by SMD substantially increase collision rates when stress testing multiple end-to-end planners, and reduce collision rates when incorporated into training, improving planner robustness and safety. Our code and video examples are available at: \href{https://icml-2.github.io/SMD/}{https://icml-2.github.io/SMD/}.

</details>

### 36. PACT: Self-Evolving Physical Safety Alignment for Diffusion Policies in Embodied Manipulation

📄 [arXiv](https://arxiv.org/abs/2606.08414) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62679)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`embodied safety`、`diffusion model`、`physical risk`

👤 **作者**：Lingxuan Wu、…、Jun Zhu

- 🎯 **研究动机**：diffusion policy 难以满足机器人部署的严格物理约束，训练期约束或测试时外部护栏分别限制表达能力与可扩展性
- 🔬 **研究方法**：提出 PACT 自进化后训练：把约束梯度经 reverse-KL 目标蒸馏进 diffusion model，课程式逐步收紧约束并保持有界策略偏移与单调改进
- 📌 **结论**：仿真与真实操作基准上安全违例平均降低 31.0%，任务成功率提升 30.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion policies have achieved remarkable success in robotic manipulation, yet they often fail to satisfy strict physical constraints required for safe deployment. Existing approaches impose safety either prematurely during training or reactively via external guardrails at test time, limiting policy expressivity and overall scalability. We propose Physical safety Alignment for Constrained Trajectories (PACT), a self-evolving post-training framework that projects pretrained diffusion policies onto constraint-feasible regions without accessing demonstration data or task rewards. PACT distills constraint gradients into the diffusion model through a reverse-KL objective with dense supervision across timesteps. It incorporates a curriculum that progressively tightens constraints while maintaining theoretically bounded policy shift and monotone improvement, mitigating the safety-performance trade-off from catastrophic forgetting. On simulated and real-world embodied manipulation benchmarks, PACT significantly reduces safety violations by 31.0% on average while improving task success by 30.7%.

</details>