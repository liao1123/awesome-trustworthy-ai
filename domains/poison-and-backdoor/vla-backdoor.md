# 视觉语言动作模型投毒与后门

[返回投毒与后门目录](README.md)

## 收录范围

> 检索截至 **2026-08-31**。这是基于公开可检索资料的系统化快照，并非对尚未公开或未被索引工作的绝对穷尽；欢迎后续补充。

- **核心收录：** 直接以端到端 Vision-Language-Action（VLA）模型为攻击、防御或评测对象，研究训练数据投毒、恶意微调或 checkpoint、持久触发器及其检测与清除的工作。当前共整理 14 篇核心论文。
- **相邻收录：** world model 训练供应链、VLM-based embodied agent、模块化 LLM/VLM 机器人和 Vision-Language Agentic System（VLAS）中与 VLA 威胁高度相关的后门工作，单独列出，避免误称为端到端 VLA 攻击。
- **不在本页：** 仅发生在推理期、且不会在模型中植入持久触发行为的 adversarial patch、prompt attack、jailbreak、freezing/steering attack，例如 FreezeVLA、DRIFT、ADVLA、Trajectory-Level Redirection 和 trusted-imagination integrity attack。
- **日期与状态：** 时间取论文首次公开月份；会议状态只采用会议官网、正式论文集或 arXiv 当前版本中的明确说明。“未注明”不代表被拒稿。代码栏仅链接作者明确公开的仓库或项目页。

检索以 arXiv 的 `vision-language-action` / `VLA` 与 `backdoor` / `poisoning` 组合查询为主，并交叉核对最新论文的 related work、两份 VLA safety survey、OpenReview、ACL/CVPR/NeurIPS/ICLR 官方页面及作者项目页。

## 研究脉络

- **从相邻机器人供应链到端到端 VLA：** Robot Collapse（2024）先展示模块化 LLM/VLM 机器人链路的供应链后门；BadVLA（2025）随后系统揭示端到端 VLA 的后门风险。
- **从任务失败到精细行为控制：** 研究由视觉 patch 导致的一般失败，扩展到 clean-action sequential error、物理物体目标劫持、可复用动作原语、机械臂初始状态、action chunk 累积漂移、flow-matching 动力学和可配置失败模式。
- **从一次植入到全生命周期风险：** INFUSE 研究后门穿过用户 clean fine-tuning 的持久性，Imperio 和 world-model poisoning 则把数据来源、社区 trajectory 与合成数据流水线纳入威胁模型。
- **检测、恢复与评测：** Bera 和 TrustVLA 开始提供无需重训的推理期清除；AttackVLA 统一攻击评测。后门式所有权验证已迁移至 [独立水印专题](../content-authenticity/backdoor-based-watermarking-and-ownership.md)。

## 核心 VLA 投毒与后门攻击

### 训练数据、微调与 checkpoint 供应链

### 1. !Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics

📄 [arXiv](https://arxiv.org/abs/2607.04146)　📅 2026-07

**关键词**：`attack`、`data poisoning`、`trigger word`、`open-source robotics`

👤 **作者**：Stefan Bühler、Mark Schutera

- 🎯 **研究动机**：开源机器人生态默认信任社区贡献数据集，触发词数据投毒对 VLA 模型的现实威胁未被量化
- 🔬 **研究方法**：在真实 pick-and-place 任务上对 smolVLA 以三种投毒比例训练并跨提示位置评估（LeRobot 平台）
- 📌 **结论**：320 段干净数据中 3 段投毒即致完全拒绝服务（成功率 0.0%）；干净提示保持约 50% 成功率，单段投毒即降至 6.7%，且攻击泛化到未训练的触发位置；数据集来源应成为一等关切

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

</details>

### 2. ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2605.08612) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1077/)　📅 2026-05　🏷 ACL 2026

**关键词**：`attack`、`visual pathway`、`gradient interference`、`semantic trigger`

👤 **作者**：Kewei Chen、Yayu Long、Shuai Li、Mingsheng Shang

- 🎯 **研究动机**：传统 VLA 视觉通路后门因端到端训练中冲突策略引发 Gradient Interference 而失败
- 🔬 **研究方法**：ATAAT 以 Threat-Method Adaptive Mapping 机制按攻击者能力选择最优梯度解耦策略
- 📌 **结论**：仅 5% 投毒率下 TASR 超 80% 且高度隐蔽，首次在数据投毒场景实现隐式解耦攻击并支持复杂语义触发器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Addressing the escalating security vulnerabilities in Vision-Language-Action (VLA) models, this study investigates backdoor attacks targeting the visual pathway. We identify a core obstacle causing the failure of traditional attack paradigms: "Gradient Interference." This phenomenon represents an optimization failure triggered by conflicting strategies during end-to-end training. To resolve this, we propose an Adaptive Threat-Aware Adversarial Tuning (ATAAT) framework. Through its core "Threat-Method Adaptive Mapping" mechanism, ATAAT intelligently selects the optimal gradient decoupling strategy based on the adversary's capabilities. Extensive experiments demonstrate that ATAAT exhibits significant advantages, achieving a highly robust Targeted Attack Success Rate (TASR > 80%) while maintaining extreme stealthiness with merely a 5% poisoning rate. It efficiently handles complex semantic-level triggers and achieves implicit decoupled attacks in data poisoning scenarios for the first time. This work reveals a critical security vulnerability in VLAs and provides theoretical and methodological support for future defense architectures.

</details>

### 3. Inject Once Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2602.00500) · 🌐 [Project](https://jianyi2004.github.io/infuse-vla-backdoor/)　📅 2026-01

**关键词**：`attack`、`INFUSE`、`persistent backdoor`、`checkpoint supply chain`

👤 **作者**：Jianyi Zhou、…、Shuo Yang

- 🎯 **研究动机**：已有 VLA 后门在下游干净数据微调后即被抹除，对真实部署威胁有限
- 🔬 **研究方法**：INFUSE 先分析多样微调场景的参数敏感性以识别微调不敏感模块，把后门注入这些稳定模块并冻结其余参数
- 📌 **结论**：用户微调后平均 ASR 仍达仿真 91.0%、实机 79.8%，远超 BadVLA（38.8%/36.6%），clean 性能与标准模型相当

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have become foundational to modern embodied AI systems. By integrating visual perception, language understanding, and action planning, they enable general-purpose task execution across diverse environments. Despite their importance, the security of VLA models remains underexplored -- particularly in the context of backdoor attacks, which pose realistic threats in physical-world deployments. While recent methods attempt to inject backdoors into VLA models, these backdoors are easily erased during downstream adaptation, as user-side fine-tuning with clean data significantly alters model parameters, rendering them impractical for real-world applications. To address these challenges, we propose INFUSE (INjection into Fine-tUne-inSensitive modulEs), the first backdoor attack framework for VLA base models that remains effective even with arbitrary user fine-tuning. INFUSE begins by analyzing parameter sensitivity across diverse fine-tuning scenarios to identify modules that remain largely unchanged -- the fine-tune-insensitive modules. It then injects backdoors into these stable modules while freezing the rest, ensuring malicious behavior persists after extensive user fine-tuning. Comprehensive experiments across multiple VLA architectures demonstrate INFUSE's effectiveness. After user-side fine-tuning, INFUSE maintains mean attack success rates of 91.0% on simulation environments and 79.8% on real-world robot tasks, substantially surpassing BadVLA (38.8% and 36.6%, respectively), while preserving clean-task performance comparable to standard models. These results uncover a critical threat: backdoors implanted before distribution can persist through fine-tuning and remain effective at deployment.

</details>

### 4. BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization

📄 [arXiv](https://arxiv.org/abs/2505.16640) · 🌐 [Project](https://badvla-project.github.io/) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b94925a92f2271cd60c9f3f7a7d366fe-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`attack`、`Training-as-a-Service`、`objective decoupling`、`visual trigger`

👤 **作者**：Xueyang Zhou、Guiyao Tie、Guowen Zhang、Hechang Wang、Pan Zhou、Lichao Sun

- 🎯 **研究动机**：Training-as-a-Service 范式下 VLA 模型的后门威胁未被探索
- 🔬 **研究方法**：提出 BadVLA 两阶段目标解耦优化：显式特征空间分离隔离触发器表示，条件控制偏差仅在触发时激活
- 📌 **结论**：多个 VLA 基准 ASR 近 100% 且干净任务精度几乎无损，对扰动、任务迁移与微调稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat-particularly under the emerging Training-as-a-Service paradigm-but remain largely unexplored in the context of VLA models. To address this gap, we propose BadVLA, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices. We have released the project page at https://badvla-project.github.io/.

</details>

### 动作、状态、物体与动力学后门

### 5. TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes

📄 [arXiv](https://arxiv.org/abs/2608.26578) · 🌐 [Project](https://john-liua.github.io/TrapVLA/)　📅 2026-08

**关键词**：`benchmark`、`attack`、`configured-failure fidelity`、`VLA backdoor`、`physical evaluation`、`configured failure`

👤 **作者**：Jun-Hui Liu、…、Wei-Shi Zheng

- 🎯 **研究动机**：既有 VLA 后门把任意任务失败都算攻击成功，无法控制机器人具体如何失效
- 🔬 **研究方法**：提出 Configured Failure Trapping 任务与 Trap-LIBERO/Trap-RoboTwin benchmark，TrapVLA 学习 trigger 诱导的 action residual 驱动指定失败
- 📌 **结论**：仿真与真实机器人上以隐蔽文本 trigger 注入指定位置偏移等失败模式，干净任务性能基本保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failure modes. Unlike prior backdoor attacks that treat any task failure as a successful attack, Configured Failure Trapping requires the attacker to control how the robot fails (e.g., causing the robot to grasp with a specified positional offset), making it substantially more challenging and hard to detect. To support the new task, we propose an effective data engine for synthesizing high-quality target trajectories and an automated suite for measuring configured-failure fidelity. Then, based on this foundation, we construct two new benchmarks, namely Trap-LIBERO and Trap-RoboTwin, that instantiate Configured Failure Trapping across four representative failure modes. To address this task, we identify sparse action deviation as a critical challenge and accordingly propose a novel method named TrapVLA, which explicitly learns trigger-induced action residuals to steer the policy toward the configured failure behavior. Extensive experiments across simulation benchmarks and real-world robotic settings show that TrapVLA effectively injects configured failure modes into VLA models while largely preserving performance on clean data. Project page: https://john-liua.github.io/TrapVLA/

</details>

### 6. FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2604.09651) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/An_FlowHijack_A_Dynamics-Aware_Backdoor_Attack_on_Flow-Matching_Vision-Language-Action_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`flow matching`、`vector-field dynamics`、`dynamics mimicry`、`VLA model`、`flow-matching backdoor`

👤 **作者**：Xinyuan An、Tao Luo、Gengyun Peng、Yaobing Wang、Kui Ren、Dongxia Wang

- 🎯 **研究动机**：flow-matching VLA（如 π0）的 vector-field dynamics 攻击面未被探索，面向自回归离散动作的后门无法直接迁移
- 🔬 **研究方法**：FlowHijack 用 τ-conditioned 注入操纵动作生成初始相位，配合 dynamics mimicry 正则约束恶意动作的运动学相似性
- 📌 **结论**：以隐蔽上下文感知触发器取得高 ASR，同时保持良性任务性能，恶意动作在行为上与正常动作不可区分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are emerging as a cornerstone for robotics, with flow-matching policies like $π_0$ showing great promise in generating smooth, continuous actions. As these models advance, their unique action generation mechanism - the vector field dynamics - presents a critical yet unexplored security vulnerability, particularly backdoor vulnerabilities. Existing backdoor attacks designed for autoregressive discretization VLAs cannot be directly applied to this new continuous dynamics. We introduce FlowHijack, the first backdoor attack framework to systematically target the underlying vector-field dynamics of flow-matching VLAs. Our method combines a novel $τ$-conditioned injection strategy, which manipulates the initial phase of the action generation, with a dynamics mimicry regularizer. Experiments demonstrate that FlowHijack achieves high attack success rates using stealthy, context-aware triggers where prior works failed. Crucially, it preserves benign task performance and, by enforcing kinematic similarity, generates malicious actions that are behaviorally indistinguishable from normal actions. Our findings reveal a significant vulnerability in continuous embodied models, highlighting the urgent need for defenses targeting the model's internal generative dynamics.

</details>

### 7. SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2601.14323) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1725/)　📅 2026-01　🏷 ACL 2026

**关键词**：`attack`、`action chunking`、`delta pose`、`trajectory drift`

👤 **作者**：Bingxin Xu、Yuzhang Shang、Binghui Wang、Emilio Ferrara

- 🎯 **研究动机**：VLA 的 action chunking 加 delta pose 表示形成 chunk 内视觉开环，逐步扰动可经积分累积放大
- 🔬 **研究方法**：SILENTDRIFT 黑盒后门：用 Smootherstep 函数构造 C2 连续扰动保证轨迹边界零速零加速度，关键帧策略只毒化接近阶段以最大化影响、最小化触发暴露
- 📌 **结论**：LIBERO 上以低于 2% 投毒率取得 93.2% ASR，clean 任务成功率保持 95.3%，毒轨迹与成功示范视觉不可区分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are increasingly deployed in safety-critical robotic applications, yet their security vulnerabilities remain underexplored. We identify a fundamental security flaw in modern VLA systems: the combination of action chunking and delta pose representations creates an intra-chunk visual open-loop. This mechanism forces the robot to execute K-step action sequences, allowing per-step perturbations to accumulate through integration. We propose SILENTDRIFT, a stealthy black-box backdoor attack exploiting this vulnerability. Our method employs the Smootherstep function to construct perturbations with guaranteed C2 continuity, ensuring zero velocity and acceleration at trajectory boundaries to satisfy strict kinematic consistency constraints. Furthermore, our keyframe attack strategy selectively poisons only the critical approach phase, maximizing impact while minimizing trigger exposure. The resulting poisoned trajectories are visually indistinguishable from successful demonstrations. Evaluated on the LIBERO, SILENTDRIFT achieves a 93.2% Attack Success Rate with a poisoning rate under 2%, while maintaining a 95.3% Clean Task Success Rate.

</details>

### 8. State Backdoor: Towards Stealthy Real-world Poisoning Attack on Vision-Language-Action Model in State Space

📄 [arXiv](https://arxiv.org/abs/2601.04266)　📅 2026-01

**关键词**：`attack`、`initial-state trigger`、`state space`、`real-world poisoning`

👤 **作者**：Ji Guo、…、Hongwei Li

- 🎯 **研究动机**：现有 VLA 后门依赖可见视觉触发器，环境可变性下真实世界鲁棒性与隐蔽性差
- 🔬 **研究方法**：State Backdoor 以机械臂初始状态为触发器，设计 Preference-guided Genetic Algorithm 在状态空间搜索最小而有效的触发配置
- 📌 **结论**：五个 VLA 模型与五个真实任务上 ASR 超 90% 且不影响良性任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are widely deployed in safety-critical embodied AI applications such as robotics. However, their complex multimodal interactions also expose new security vulnerabilities. In this paper, we investigate a backdoor threat in VLA models, where malicious inputs cause targeted misbehavior while preserving performance on clean data. Existing backdoor methods predominantly rely on inserting visible triggers into visual modality, which suffer from poor robustness and low insusceptibility in real-world settings due to environmental variability. To overcome these limitations, we introduce the State Backdoor, a novel and practical backdoor attack that leverages the robot arm's initial state as the trigger. To optimize trigger for insusceptibility and effectiveness, we design a Preference-guided Genetic Algorithm (PGA) that efficiently searches the state space for minimal yet potent triggers. Extensive experiments on five representative VLA models and five real-world tasks show that our method achieves over 90% attack success rate without affecting benign task performance, revealing an underexplored vulnerability in embodied AI systems.

</details>

### 9. DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2510.10932v4)　📅 2025-10

**关键词**：`attack`、`action primitive`、`action chunk`、`pipeline black box`

👤 **作者**：Zonghuan Xu、Jiayu Li、Yunhan Zhao、Xiang Zheng、Xingjun Ma、Yu-Gang Jiang

- 🎯 **研究动机**：已有 VLA 后门多为无目标攻击或任务级劫持，对单个安全关键动作的细粒度控制未被探索
- 🔬 **研究方法**：DropVLA 在 pipeline 黑盒与有限投毒设定下，用窗口一致重标注方案使可复用动作原语（如 open_gripper）在攻击者指定决策点执行
- 📌 **结论**：仅投毒 0.31% episodes 即在 OpenVLA-7B/LIBERO 上取得 98.67%-99.83% ASR，clean 保留 98.50% 以上，并在 Franka 实机验证可行性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models map multimodal perception and language instructions to executable robot actions, making them particularly vulnerable to behavioral backdoor manipulation: a hidden trigger introduced during training can induce unintended physical actions while nominal task performance remains intact. Prior work on VLA backdoors primarily studies untargeted attacks or task-level hijacking, leaving fine-grained control over individual actions largely unexplored. In this work, we present DropVLA, an action-level backdoor attack that forces a reusable action primitive (e.g., open_gripper) to execute at attacker-chosen decision points under a realistic pipeline-black-box setting with limited data-poisoning access, using a window-consistent relabeling scheme for chunked fine-tuning. On OpenVLA-7B evaluated with LIBERO, vision-only poisoning achieves 98.67%-99.83% attack success rate (ASR) with only 0.31% poisoned episodes while preserving 98.50%-99.17% clean-task retention, and successfully triggers the targeted action within 25 control steps at 500 Hz (0.05 s). Text-only triggers are unstable at low poisoning budgets, and combining text with vision provides no consistent ASR improvement over vision-only attacks. The backdoor remains robust to moderate trigger variations and transfers across evaluation suites (96.27%, 99.09%), whereas text-only largely fails (0.72%). We further validate physical-world feasibility on a 7-DoF Franka arm with pi0-fast, demonstrating non-trivial attack efficacy under camera-relative motion that induces image-plane trigger drift. These results reveal that VLA models can be covertly steered at the granularity of safety-critical actions with minimal poisoning and without observable degradation of nominal performance.

</details>

### 10. Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects

📄 [arXiv](https://arxiv.org/abs/2510.09269) · 🌐 [Project](https://goba-attack.github.io/)　📅 2025-10

**关键词**：`attack`、`GoBA`、`physical object`、`goal hijacking`

👤 **作者**：Zirun Zhou、Zhengyang Xiao、Haochuan Xu、Jing Sun、Di Wang、Jingfeng Zhang

- 🎯 **研究动机**：现有 VLA 后门攻击多假设白盒访问且只能造成任务失败，无法强制执行指定动作
- 🔬 **研究方法**：提出 GoBA，把物理物体作为触发器注入训练数据使 VLA 执行目标导向动作，基于 LIBERO 构建 BadLIBERO 数据集并用三级评估刻画行为状态
- 📌 **结论**：触发器存在时 97% 输入达成后门目标且 clean 输入零性能损失；动作轨迹与触发器颜色显著影响攻击，尺寸影响很小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in vision-language-action (VLA) models have greatly improved embodied AI, enabling robots to follow natural language instructions and perform diverse tasks. However, their reliance on uncurated training datasets raises serious security concerns. Existing backdoor attacks on VLAs mostly assume white-box access and result in task failures instead of enforcing specific actions. In this work, we reveal a more practical threat: attackers can manipulate VLAs by simply injecting physical objects as triggers into the training dataset. We propose goal-oriented backdoor attacks (GoBA), where the VLA behaves normally in the absence of physical triggers but executes predefined and goal-oriented actions in the presence of physical triggers. Specifically, based on a popular VLA benchmark LIBERO, we introduce BadLIBERO that incorporates diverse physical triggers and goal-oriented backdoor actions. In addition, we propose a three-level evaluation that categorizes the victim VLA's actions under GoBA into three states: nothing to do, try to do, and success to do. Experiments show that GoBA enables the victim VLA to successfully achieve the backdoor goal in 97 percentage of inputs when the physical trigger is present, while causing zero performance degradation on clean inputs. Finally, by investigating factors related to GoBA, we find that the action trajectory and trigger color significantly influence attack performance, while trigger size has surprisingly little effect. The code and BadLIBERO dataset are accessible via the project page at https://goba-attack.github.io/.

</details>

### 11. Clean-Action Backdoor Attacks on Vision-Language-Action Models via Sequential Error Exploitation

📝 [OpenReview](https://openreview.net/forum?id=QQdn8nNqgi)　📅 2025-09　🏷 ICLR 2026

**关键词**：`attack`、`clean-action poisoning`、`sequential error`、`dataset filtering`

- 🎯 **研究动机**：VLA重规划前的连续动作执行使误差逐步累积，数据过滤难察觉
- 🔬 **研究方法**：构造clean-action投毒样本利用sequential error让攻击生效
- 📌 **结论**：在pi0/LIBERO上绕过常见数据过滤，clean fine-tuning后仍存留

### 12. TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors

📄 [arXiv](https://arxiv.org/abs/2607.12571)　📅 2026-07

**关键词**：`defense`、`causal footprint`、`evidence evolution`、`localized inpainting`

👤 **作者**：Pinhan Fu、…、Mang Ye

- 🎯 **研究动机**：被投毒的 VLA 可在干净观测下正常、被视觉触发器劫持长程策略，且视觉/语言防御难以免重训恢复行为
- 🔬 **研究方法**：在 BadVLA 与 INFUSE 两种攻击上识别紧凑因果足迹（注意力播种、空间紧凑、可因果掩蔽），提出 TrustVLA：用 Dirichlet 证据框架监测逐 token 逐层认知不确定性，定位紧凑支撑并对观测做局部修复
- 📌 **结论**：仅需小干净校准集，在 OpenVLA/LIBERO 与 pi-0.5 迁移评估中降低攻击成功率并保留干净任务性能，提供免重训机制引导防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. We study this gap through two independently proposed VLA attacks from groups with distinct injection strategies, BadVLA and INFUSE; the latter persists after downstream clean adaptation. Across the evaluated poisoned models, we identify a recurring internal mechanism: a \emph{compact causal footprint}, namely a small visual support that is attention-seeded, spatially compact, and \emph{causal} in a precise sense -- masking it returns a clean-calibrated evidence-evolution score to the normal operating region. This footprint motivates TrustVLA, a mechanism-guided inference-time defense that adapts the Dirichlet evidence framework from trusted classification to monitor per-token, per-layer epistemic uncertainty in VLA policies. With only a small clean calibration set, TrustVLA (i)~detects abnormal evidence evolution, (ii)~localizes the compact support by counterfactual mechanism-score drop, and (iii)~recovers the observation by localized inpainting. Across OpenVLA/LIBERO and $π_{0.5}$ transfer evaluations, TrustVLA reduces attack success while preserving clean-task performance, providing a retraining-free, mechanism-guided defense for visual-triggered VLA backdoors.

</details>

### 13. When Attention Betrays: Erasing Backdoor Attacks in Robotic Policies by Reconstructing Visual Tokens

📄 [arXiv](https://arxiv.org/abs/2602.03153)　📅 2026-02

**关键词**：`defense`、`Bera`、`attention anomaly`、`visual-token reconstruction`

👤 **作者**：Xuetao Li、…、Miao Li

- 🎯 **研究动机**：VLA 后门防御或缺机制洞察、或需全模型重训成本过高
- 🔬 **研究方法**：发现后门重定向深层注意力并在干净流形附近形成紧凑嵌入簇；Bera 测试时经潜空间定位异常注意 token、掩蔽可疑区域并重建无触发图像，打断触发-不安全动作映射
- 📌 **结论**：无需重训或改训练管线，跨多个具身平台与任务显著降低 ASR、恢复正常行为并保持标称性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Downstream fine-tuning of vision-language-action (VLA) models enhances robotics, yet exposes the pipeline to backdoor risks. Attackers can pretrain VLAs on poisoned data to implant backdoors that remain stealthy but can trigger harmful behavior during inference. However, existing defenses either lack mechanistic insight into multimodal backdoors or impose prohibitive computational costs via full-model retraining. To this end, we uncover a deep-layer attention grabbing mechanism: backdoors redirect late-stage attention and form compact embedding clusters near the clean manifold. Leveraging this insight, we introduce Bera, a test-time backdoor erasure framework that detects tokens with anomalous attention via latent-space localization, masks suspicious regions using deep-layer cues, and reconstructs a trigger-free image to break the trigger-unsafe-action mapping while restoring correct behavior. Unlike prior defenses, Bera requires neither retraining of VLAs nor any changes to the training pipeline. Extensive experiments across multiple embodied platforms and tasks show that Bera effectively maintains nominal performance, significantly reduces attack success rates, and consistently restores benign behavior from backdoored outputs, thereby offering a robust and practical defense mechanism for securing robotic systems.

</details>

### 14. AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2511.12149)　📅 2025-11

**关键词**：`benchmark`、`BackdoorVLA`、`targeted attack`、`real-world evaluation`

👤 **作者**：Jiayu Li、…、Yu-Gang Jiang

- 🎯 **研究动机**：VLA 攻击缺乏统一评测框架，action tokenizer 差异阻碍复现，且多数攻击未经真实场景验证
- 🔬 **研究方法**：AttackVLA 覆盖数据构建、训练与推理全生命周期，实现已有与适配的攻击并在仿真与实机评测；进一步提出让 VLA 执行指定长程动作序列的 BackdoorVLA
- 📌 **结论**：BackdoorVLA 平均定向成功率 58.4%、部分任务达 100%；现有攻击多只能造成无目标失败或静态动作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models enable robots to interpret natural-language instructions and perform diverse tasks, yet their integration of perception, language, and control introduces new safety vulnerabilities. Despite growing interest in attacking such models, the effectiveness of existing techniques remains unclear due to the absence of a unified evaluation framework. One major issue is that differences in action tokenizers across VLA architectures hinder reproducibility and fair comparison. More importantly, most existing attacks have not been validated in real-world scenarios. To address these challenges, we propose AttackVLA, a unified framework that aligns with the VLA development lifecycle, covering data construction, model training, and inference. Within this framework, we implement a broad suite of attacks, including all existing attacks targeting VLAs and multiple adapted attacks originally developed for vision-language models, and evaluate them in both simulation and real-world settings. Our analysis of existing attacks reveals a critical gap: current methods tend to induce untargeted failures or static action states, leaving targeted attacks that drive VLAs to perform precise long-horizon action sequences largely unexplored. To fill this gap, we introduce BackdoorVLA, a targeted backdoor attack that compels a VLA to execute an attacker-specified long-horizon action sequence whenever a trigger is present. We evaluate BackdoorVLA in both simulated benchmarks and real-world robotic settings, achieving an average targeted success rate of 58.4% and reaching 100% on selected tasks. Our work provides a standardized framework for evaluating VLA vulnerabilities and demonstrates the potential for precise adversarial manipulation, motivating further research on securing VLA-based embodied systems.

</details>

### 15. Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems

📄 [arXiv](https://arxiv.org/abs/2606.12586)　📅 2026-06

**关键词**：`analysis`、`VLAS 系统级评测`、`含 embodied-manipulation workflow`、`trigger leakage`、`neighbor leakage rate`、`agentic VLM`

👤 **作者**：Jiamin Chang、Salil Kanhere、Piotr Koniusz、Jason、Xue、Hammond Pearce

- 🎯 **研究动机**：VLAS 中视觉后门是系统级威胁，现有 ASR 与干净精度指标不衡量攻击是否精确（是否只在预期时触发）
- 🔬 **研究方法**：形式化 trigger leakage 并提出 Neighbor Leakage Rate（NLR）；以文本触发为探针分析微调学到的宽激活区域，并加编辑距离一硬负样本训练
- 📌 **结论**：3% 投毒率下邻近变体大量泄漏（NLR 达 0.996/0.944）；加入编辑距离一硬负样本显著收窄激活区域，在图像编辑与具身操作工作流中同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Agentic Systems (VLAS) connect visual perception to planning, tool use, and physical actions. This means backdoor-type triggers can propagate through both decision pipelines and their connected interfaces, thus making visual backdoors a system-level threat. Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior. To quantify this leakage, we introduce Neighbor Leakage Rate (NLR). Our experiments show that at a 3% poisoning ratio, icon and text triggers remain robust to common visual transformations, but their neighboring variants leak heavily, with NLR reaching 0.996 (icon) and 0.944 (text). Using textual triggers as a controlled probe, we show that standard fine-tuning learns a broad activation region rather than an exact trigger condition, causing neighboring strings to invoke the malicious behavior even when the exact trigger is absent. Adding edit-distance-one hard-negative samples during training substantially narrows this activation region and reduces leakage, including in image-editing and embodied-manipulation workflows, where leaked triggers can propagate into executable programs and action sequences.

</details>

### 16. Targeting World Models to Compromise Robot Learning Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.09499)　📅 2026-06

**关键词**：`world-model 合成数据供应链`、`VLA proof of concept`

👤 **作者**：Ethan Rathbun、Ahmed Agha、Saaduddin Mahmud、Christopher Amato、Alina Oprea、Eugene Bagdasarian

- 🎯 **研究动机**：world model 作为生成机器人训练数据的高效工具被广泛集成，却构成比传统数据投毒更隐蔽的供应链入口
- 🔬 **研究方法**：在可见安全的遥操作数据中注入恶意提示或被破坏的转移动力学，仅经 world model 处理后激活，生成危险合成轨迹并污染下游策略
- 📌 **结论**：对 SOTA 动作/文本条件 world model 均有效，端到端后门化 DRL 策略并在 VLA 场景完成概念验证，需重新评估 world model 在供应链中的位置

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing their integration into the robot learning pipeline. While highly practical, in this work we demonstrate that world models introduce a uniquely stealthy and effective data poisoning entry point into the robot learning supply chain that can result in the deployment of unsafe or otherwise compromised robotic policies despite training on seemingly safe ground truth training data. In contrast to traditional data poisoning techniques which directly implant dangerous trajectories into sold or uploaded datasets, our novel attack methods inject malicious prompts or compromising transition dynamics into visibly safe teleoperated datasets which are only activated once fed through a world model as input. This can result in the generation of synthetic, dangerous robot training trajectories and subsequently unsafe or compromised robot policies. We demonstrate the effectiveness of our attacks against both state of the art action conditioned and text conditioned world models, showing a full end-to-end backdoor on a downstream DRL policy and a proof-of-concept for the VLA setting. Overall these findings necessitate research into more secure world models and reevaluating their position within the robot learning supply chain.

</details>

### 17. BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning

📄 [arXiv](https://arxiv.org/abs/2510.27623) · 🌐 [Project](https://zqs1943.github.io/BEAT/) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009735)　📅 2025-10　🏷 ICLR 2026

**关键词**：`VLM-based embodied agent`、`并非端到端 VLA`

👤 **作者**：Qiusi Zhan、…、Daniel Kang

- 🎯 **研究动机**：VLM 具身 agent 的视觉后门攻击未被探索，物体触发器随视角与光照变化大、难以可靠植入
- 🔬 **研究方法**：BEAT 构建覆盖多样场景、任务与触发器放置的训练集，先 SFT 再用 Contrastive Trigger Learning 以偏好学习锐化触发判定边界
- 📌 **结论**：多基准 ASR 最高 80% 且保持良性性能，OOD 触发位置可靠泛化；有限后门数据下 CTL 比朴素 SFT 提升激活准确率最高 39%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Vision-Language Models (VLMs) have propelled embodied agents by enabling direct perception, reasoning, and planning task-oriented actions from visual inputs. However, such vision-driven embodied agents open a new attack surface: visual backdoor attacks, where the agent behaves normally until a visual trigger appears in the scene, then persistently executes an attacker-specified multi-step policy. We introduce BEAT, the first framework to inject such visual backdoors into VLM-based embodied agents using objects in the environments as triggers. Unlike textual triggers, object triggers exhibit wide variation across viewpoints and lighting, making them difficult to implant reliably. BEAT addresses this challenge by (1) constructing a training set that spans diverse scenes, tasks, and trigger placements to expose agents to trigger variability, and (2) introducing a two-stage training scheme that first applies supervised fine-tuning (SFT) and then our novel Contrastive Trigger Learning (CTL). CTL formulates trigger discrimination as preference learning between trigger-present and trigger-free inputs, explicitly sharpening the decision boundaries to ensure precise backdoor activation. Across various embodied agent benchmarks and VLMs, BEAT achieves attack success rates up to 80%, while maintaining strong benign task performance, and generalizes reliably to out-of-distribution trigger placements. Notably, compared to naive SFT, CTL boosts backdoor activation accuracy up to 39% under limited backdoor data. These findings expose a critical yet unexplored security risk in VLM-based embodied agents, underscoring the need for robust defenses before real-world deployment.

</details>

### 18. Robot Collapse: Supply Chain Backdoor Attacks Against VLM-based Robotic Manipulation

📄 [arXiv](https://arxiv.org/abs/2411.11683) · 🌐 [Project](https://trojanrobot.github.io/)　📅 2024-11

**关键词**：`模块化 LLM→VLM 机器人链路`、`并非端到端 VLA`

👤 **作者**：Xianlong Wang、…、Xiaohua Jia

- 🎯 **研究动机**：机器人操作的推理期攻击已被广泛研究，模型供应链后门攻击仍是空白
- 🔬 **研究方法**：TrojanRobot 向模块化 policy 注入恶意模块操纵 LLM-to-VLM 通路；升级方案 LVLM-as-a-backdoor 借 ICIL 用后门 system prompt 控制 LVLM，实现 permutation、stagnation、intentional 三类攻击
- 📌 **结论**：18 个真实操作任务与 4 个 VLM 的物理世界和仿真实验均验证攻击优越性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Robotic manipulation policies are increasingly empowered by \textit{large language models} (LLMs) and \textit{vision-language models} (VLMs), leveraging their understanding and perception capabilities. Recently, inference-time attacks against robotic manipulation have been extensively studied, yet backdoor attacks targeting model supply chain security in robotic policies remain largely unexplored. To fill this gap, we propose \texttt{TrojanRobot}, a backdoor injection framework for model supply chain attack scenarios, which embeds a malicious module into modular robotic policies via backdoor relationships to manipulate the LLM-to-VLM pathway and compromise the system. Our vanilla design instantiates this module as a backdoor-finetuned VLM. To further enhance attack performance, we propose a prime scheme by introducing the concept of \textit{LVLM-as-a-backdoor}, which leverages \textit{in-context instruction learning} (ICIL) to steer \textit{large vision-language model} (LVLM) behavior through backdoored system prompts. Moreover, we develop three types of prime attacks, \textit{permutation}, \textit{stagnation}, and \textit{intentional}, achieving flexible backdoor attack effects. Extensive physical-world and simulator experiments on 18 real-world manipulation tasks and 4 VLMs verify the superiority of proposed \texttt{TrojanRobot}

</details>

### 19. SoK: Security and Privacy of Foundation-Model-Powered Robots

📄 [arXiv](https://arxiv.org/abs/2606.16788)　📅 2026-06

**关键词**：`相邻 SoK`、`foundation-model robot supply chain`

👤 **作者**：Xueluan Gong、Chen Chen、Jinxin Liu、Qian Wang、Kwok-Yan Lam

- 🎯 **研究动机**：基础模型进入机器人带来超出模型本身的安防风险，已有综述聚焦单一 FM 类型或风险类别，缺乏统一结构分析风险起源与传播
- 🔬 **研究方法**：提出 F-E-S-G 渐进式结构边界框架（基础模型层、具身系统层、支撑生态层、治理影响层），配合三级分类法与细粒度编码属性系统化 96 篇文献
- 📌 **结论**：识别出单一边界视角难以发现的威胁模式、防御错配与评估缺口，并给出研究议程

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Foundation models are reshaping robotics by enabling robots to interpret open-ended instructions, reason over multimodal contexts, and operate in complex, open-world environments. However, their integration also introduces security and privacy (S&P) risks that extend beyond the FMs themselves to embodied execution pipelines, supporting ecosystems, and broader governance impacts. Existing literature reviews provide valuable insights but often focus on specific FM types, risk categories, mitigation strategies, or trust boundaries. Consequently, the field lacks a unified structure for analyzing where risks originate, how they propagate across robotic systems, and where mitigations should intervene. To address this gap, we propose a progressive F-E-S-G structural boundary framework for analyzing the S&P of FM-powered robots. The framework comprises four layers: the Foundation model layer (F), Embodied system layer (E), Supporting ecosystem layer (S), and Governance impact layer (G). Building on this structure, we develop a multi-level taxonomy that organizes prior studies along three levels: F-E-S-G trust boundary, security-privacy concerns, and risk-mitigation perspectives. We further annotate each study using fine-grained coding attributes, including target, lifecycle stage, mechanism, system access, and effect. Guided by this framework and taxonomy, we systematize 96 papers. Our analysis uncovers multiple threat patterns, defense mismatches, and evaluation gaps that are difficult to identify from a single-boundary perspective. Based on these findings, we identify open challenges and future directions to provide a research agenda for developing secure, privacy-preserving, and responsibly governed FM-powered robotic systems.

</details>

### 20. Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

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

### 21. Safety of Vision-Language-Action Models: A Survey from Lifecycle Perspectives

🌐 [Project](https://www.authorea.com/doi/full/10.22541/au.177524426.60806944/v1)　📅 2026-03

**关键词**：`VLA 生命周期综述`、`Training Data Poisoning`

- 🎯 **研究动机**：VLA模型全生命周期安全研究分散
- 🔬 **研究方法**：按Data Preparation、Model Training、System Deployment三阶段综述VLA安全，含数据投毒
- 📌 **结论**：建立生命周期taxonomy并配套持续追踪仓库

### 22. When the World Lies: Backdoor Attacks on Latent World Models for Downstream Control

📄 [arXiv](https://arxiv.org/abs/2609.15781)　📅 2026-09

**关键词**：`attack`、`backdoor`、`latent world model`、`supply chain`、`controller hijacking`

👤 **作者**：Roberto Riaño、Gorka Abad、Stjepan Picek、Aitor Urbieta

- 🎯 **研究动机**：预训练 world model 开始被复用为现成动力学 backbone——该复用打开供应链后门：控制已发布 checkpoint 的对手可劫持下游 controller，即使 victim 完全在干净数据上训练评测
- 🔬 **研究方法**：攻击不编码显式 trigger-to-action 规则：毒化模型把带 trigger 观测路由进选定 latent 区域并重塑局部动力学，让 victim 自己的优化（Dreamer imagination 训练或 MPC/CEM 规划）自行重新发现攻击者目标动作
- 📌 **结论**：多个控制任务上 trigger 控制每个动作维度，最强设定下劫持 100% 被触发步；checkpoint 仍通过 clean-data 诊断（clean success 保持 ≥约 75%）；效应时间门控；中等 clean fine-tuning 可保持 utility 同时留下后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pretrained world models, learned simulators that encode an observation into a latent state and predict how it evolves under actions, are beginning to be reused as off-the-shelf dynamics backbones for control, like pretrained encoders and language models are reused today. We show that this reuse opens a supply-chain backdoor: an adversary who controls only a released checkpoint can hijack the downstream controller, even though the victim trains and evaluates entirely on clean data and never sees the trigger. The attack encodes no explicit trigger-to-action rule. Instead, the poisoned model routes trigger-bearing observations into a chosen latent region and reshapes the local dynamics there, so that the victim&#39;s own optimization (Dreamer-style actor training in imagination, or MPC/CEM planning over predicted futures) re-discovers the attacker&#39;s target action on its own. Across several control tasks and trigger families, the trigger steers the controller&#39;s action toward the attacker&#39;s target, controlling every action dimension and hijacking 100\% of triggered steps on the strongest settings. The checkpoint still passes the clean-data diagnostics a victim would run before deployment, with clean-task success retaining at least $\sim$75\%. The effect is temporally gated: it appears only while the trigger is present and disappears when the trigger is removed. Trigger-blind repair is budget-dependent: moderate clean fine-tuning can preserve clean utility while leaving the triggered failure intact, whereas sufficiently aggressive adaptation can remove it only after substantially degrading clean control. The world-model backbone itself is therefore an emerging and underexamined attack surface for control. The full code and artifacts are available in our repository.

</details>

### 23. StepTrigger: Contact-State-Triggered Backdoor Attacks on VLM-Powered Legged Robots

📄 [arXiv](https://arxiv.org/abs/2609.26131)　📅 2026-09

**关键词**：`attack`、`contact-state trigger`、`legged robot`、`VLM planner`、`physical backdoor`

👤 **作者**：Jiageng Zhang、Doniyorkhon Obidov、Kaichen Yang

- 🎯 **研究动机**：LLM/VLM 日益充当机器人高层规划器（依目标与传感器摘要选动作）——被攻陷的规划器可在隐藏触发存在时改变目标选择；既有攻击依赖语言/视觉/场景语义触发
- 🔬 **研究方法**：StepTrigger：首个接触状态触发的后门——用机器人本体接触状态（腿/关节物理配置）作触发器，攻击 VLM 驱动的足式机器人
- 📌 **结论**：接触状态触发避开语言与视觉检测面——物理状态作为后门触发通道（VLA/具身后门的全新触发模态）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models and vision-language models are increasingly used as high-level planners in robotic systems, using task goals and sensor summaries to select navigation or manipulation actions. This creates a new backdoor surface: a compromised planner can behave normally in most runs, yet change its target selection when a hidden trigger is present. Prior attacks on LLM-powered or embodied agents mainly rely on triggers that appear in language, camera-visible objects, scene semantics, or specific sequences of past actions. This paper presents StepTrigger, a contact-state-triggered backdoor attack for VLM-powered legged robots. The trigger is not a prompt token or a visible marker. It is produced by pressure and foot-ground contact patterns that arise when a Unitree Go1 quadruped walks across a dense terrain patch. Unlike conventional visual or textual triggers, contact signals are inherently noisy and may also arise during benign locomotion. To avoid treating every pressure anomaly as a trigger, StepTrigger learns a selective backdoor policy from multimodal robot state, using incidental pressure events as benign examples and dense-patch contacts as poisoned examples. In a stratified offline evaluation, the trained planner achieved 98.75% clean behavior preservation, 92.50% false-trigger rejection, 76.25% true-trigger activation, and 89.17% overall parsed behavior accuracy. These results reveal a backdoor surface in proprioceptive and contact channels that is not captured by defenses focused only on language, vision, or action history.

</details>

### 24. Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study

📄 [arXiv](https://arxiv.org/abs/2609.26868)　📅 2026-09

**关键词**：`attack`、`industrial robot backdoor`、`VLA manipulation`、`empirical security study`、`runtime trigger defense`

👤 **作者**：Zijian Zhang、Zhen Zeng、Zhongshu Gu、Sandeep Pisharody

- 🎯 **研究动机**：学习型模型（视觉运动/VLA）预测直接翻译为物理动作的工业部署正在扩展——后门在真实商用机械臂上的后果缺乏实证：正常任务下隐蔽、触发时产生语义错误的操作行为
- 🔬 **研究方法**：两台真实商用工业机械臂（FANUC 与 xArm）上的后门攻击与防御实证：可否可靠诱导语义错误操作同时保持名义执行隐蔽；开发运行时在线防御管线检测并中和触发器并与基线比较
- 📌 **结论**：商业机械臂上后门可行且隐蔽——具身后门从仿真基准走向真实工业硬件的第一手证据（机器人后门触发面扩展线的工业落地）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Learning-based models (e.g., visuomotor and Vision-Language-Action (VLA)) are increasingly explored for industrial robotic manipulation, where model predictions are directly translated into physical actions. This tight coupling between model behavior and physical execution makes hidden security vulnerabilities particularly consequential. While backdoor attacks have been widely studied in conventional AI models, their effects on deployed learning-based robotic arm manipulation systems remain less understood: a backdoored robot can behave normally during benign operation while inducing attacker-specified behaviors only when specific triggers are present, posing potentially serious risks in physical environments. In this work, we present a preliminary empirical security study of backdoor attacks and defenses in learning-based robotic manipulation on two real commercial industrial robotic arms (FANUC and xArm). We investigate whether a backdoor can reliably induce semantically incorrect manipulation behaviors while remaining stealthy under nominal task execution. We then develop an online defense pipeline that detects and neutralizes triggers at runtime, and compare its effectiveness against an offline fine-tuning defense. Beyond defense effectiveness, we further evaluate the computational latency and execution overhead introduced by the defense pipeline to assess its suitability for high-throughput industrial operation.

</details>
