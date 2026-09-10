# VLA Adversarial Attack

[返回 Embodied Model Security 目录](README.md)

## 研究方向

本方向研究攻击者如何通过 physical patch、adversarial texture、scene-consistent object、language instruction 或 internal world-model interface 改变 VLA 的动作。与普通视觉分类攻击不同，VLA 攻击的目标通常是 task failure、targeted action、trajectory redirection、unsafe physical outcome 或 membership leakage，必须在 closed-loop rollout 与真实物理环境中评估 transferability、persistence 和 consequence。

## 研究脉络

- **Observation-space attack：** 早期工作验证 VLA 对 patch 的脆弱性，随后攻击从单模型、单任务扩展到 sparse patch、跨模型 transfer 和跨任务 universal texture。
- **Physical plausibility：** 攻击载体从像素扰动演进到可打印 patch、带纹理物体和 diffusion 生成的自然外观，使威胁更接近真实部署环境。
- **Trajectory integrity：** 新工作不再只追求单步 action deviation，而是通过 instruction、world-action model 或 imagined future state 持续重定向整个执行轨迹。
- **Beyond integrity：** Membership inference 将研究边界扩展到 robot demonstration 与 VLA training data 的隐私泄漏；action freezing 则构成独立的 availability 问题。

## Physical Patch、Texture 与 Object Attack

### 1. UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2608.13453)　📅 2026-08

**关键词**：`attack`、`universal texture`、`cross-task transfer`、`action manipulation`

👤 **作者**：Yukun Dai、Mingzhe Dai、Tianshi Wang、Fengling Li、Jingjing Li、Lei Zhu

- 🎯 **研究动机**：对机器人策略的攻击多为单任务定制优化，多任务 VLA 的跨任务脆弱性未探索
- 🔬 **研究方法**：UniTexture 用单个带纹理 3D 物体，经可微渲染把动作输出梯度回传到表面纹理，跨任务/指令/状态/视角联合优化共享纹理并施加目标对齐动作目标
- 📌 **结论**：OpenVLA 与 π0.5 上平均任务成功率从 90.0% 降至 48.4%，并展现跨套件、跨模型的免重优化迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We introduce UniTexture, a cross-task universal adversarial texture attack that uses a single textured 3D object to induce targeted deviations in VLA action predictions across multiple tasks. UniTexture backpropagates gradients from the policy's action outputs to surface texture parameters through a differentiable renderer. It jointly optimizes the shared texture over a distribution of tasks, instructions, states, and viewpoints using a targeted action-space objective, steering predicted actions toward attacker-defined targets without optimizing a separate texture for each task. We evaluate UniTexture on OpenVLA and $π_{0.5}$ across diverse manipulation tasks and multiple evaluation settings. UniTexture reduces the mean task success rate from 90.0% under benign conditions to 48.4% under attack, induces target-aligned action shifts, and further exhibits cross-suite and cross-model transfer without re-optimization. Together, these findings reveal shared cross-task vulnerabilities in multitask VLAs that can be systematically exploited through a single adversarial surface texture.

</details>

### 2. Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2608.10393)　📅 2026-08

**关键词**：`attack`、`unrestricted adversarial object`、`diffusion generation`、`physical plausibility`

👤 **作者**：Jiahui Han、…、Xia Hu

- 🎯 **研究动机**：现有 VLA 攻击依赖像素空间扰动或白盒访问，伪影明显且难以在真实机器人系统部署
- 🔬 **研究方法**：DURA 沿预训练扩散模型的潜轨迹优化生成视觉自然的对抗贴片，白盒与黑盒设定均支持，黑盒仅需受害者模型的预测动作
- 📌 **结论**：仿真与真实物理世界实验中一致超越现有方法，暴露物理部署 VLA 模型的安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on pixel-space perturbations or white-box access, resulting in noticeable artifacts and limited deployability in real-world robotic systems. In this work, we propose DURA, a diffusion-based unrestricted robotic attack that generates visually natural adversarial patches for VLA models. DURA supports both white-box and black-box attack settings, where the black-box setting requires only the predicted actions of the victim model. By optimizing along the latent trajectory of a pretrained diffusion model, DURA generates visually natural patches while steering the robot toward attacker-specified target actions. Extensive experiments in both simulation and the real physical world show that DURA consistently outperforms existing methods. Our findings expose a safety risk for physically deployed VLA models and call for stronger defenses.

</details>

### 3. VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking

📄 [arXiv](https://arxiv.org/abs/2605.28083) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4145)　📅 2026-05　🏷 ECCV 2026

**关键词**：`attack`、`transferable patch`、`visual proprioception`、`action hijacking`、`VLA attack`、`adversarial patch`

👤 **作者**：Jiyuan Fu、…、Wenqiang Zhang

- 🎯 **研究动机**：现有 VLA patch 攻击以白盒为主、过拟合目标动作输出空间，跨架构迁移差
- 🔬 **研究方法**：利用 VLA 规划前必须视觉定位自身机械臂的共性漏洞：注意力引导本体抑制隐藏真实机械臂特征，多模态本体注入把 patch 立为幻影本体，切断真实本体与控制策略的语义联系
- 📌 **结论**：OpenVLA、UniVLA、CronusVLA 上白盒优化效率优，并创跨架构跨域黑盒迁移 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Vision-Language-Action (VLA) models have emerged as powerful generalist policies, their severe vulnerability to adversarial patches significantly hinders their deployment in safety-critical domains. Moreover, existing patch attacks primarily focus on white-box settings, heavily overfitting to the specific action output space of the target model, which results in poor cross-architecture transferability. To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment. Targeting this shared visual self-localization process, our approach concurrently optimizes Attention-Guided Proprioceptive Suppression to inhibit the real robotic arm's features, and Multimodal Proprioceptive Injection to establish the patch as a surrogate "phantom embodiment". By alternating between semantic concept anchoring and visual prototype projection, VLA-Hijack effectively severs the semantic relationship between the agent's true embodiment and its control policy. Extensive experiments across diverse architectures (OpenVLA, UniVLA, and CronusVLA) demonstrate that VLA-Hijack achieves superior optimization efficiency in white-box settings and sets a new SOTA for cross-architecture and cross-domain black-box transferability.

</details>

### 4. TRAP: Hijacking VLA CoT-Reasoning via Adversarial Patches

📄 [arXiv](https://arxiv.org/abs/2603.23117) · 🌐 [Project](https://zhengxian-huang.github.io/TRAP-website/) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60529)　📅 2026-03　🏷 ICML 2026

**关键词**：`attack`、`CoT hijacking`、`adversarial patch`、`reasoning trajectory`、`dangerous capability`、`chain-of-thought`

👤 **作者**：Zhengxian Huang、Wenjun Zhu、Haoxuan Qiu、Xiaoyu Ji、Wenyuan Xu

- 🎯 **研究动机**：VLA 的 CoT 推理机制安全性未被探索，而 CoT 强支配动作生成
- 🔬 **研究方法**：TRAP 用对抗补丁（如桌布）劫持推理到动作通路，把中间 CoT 与下游动作引向攻击者定义行为，无需修改用户指令
- 📌 **结论**：在三个不同 CoT 机制的推理 VLA 上有效，纸面打印补丁在真实环境可行——如让机器人递刀而非苹果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

By integrating Chain-of-Thought (CoT) reasoning, Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation, particularly by improving generalization and interpretability. However, the security of CoT-based reasoning mechanisms remains largely unexplored. In this paper, we show that CoT reasoning introduces a novel attack vector for targeted behavior hijacking--for example, causing a robot to mistakenly deliver a knife to a person instead of an apple--without modifying the user's instruction. We first provide empirical evidence that CoT strongly governs action generation, even when it is semantically misaligned with the input instructions. Building on this observation, we propose TRAP, the first targeted behavior-hijacking adversarial attack against CoT-reasoning VLA models. By targeting the reasoning-to-action pathway, TRAP uses an adversarial patch (e.g., a tablecloth placed on the table) to steer intermediate CoT reasoning and downstream actions toward adversary-defined behaviors. Extensive evaluations on three representative reasoning VLAs, spanning distinct CoT reasoning mechanisms, demonstrate the effectiveness of TRAP. Notably, we implemented the patch by printing it on paper in a real-world setting. Our findings highlight the urgent need to secure CoT reasoning in VLA systems. The project page is available at https://zhengxian-huang.github.io/TRAP-website/.

</details>

### 5. Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2511.21663)　📅 2025-11

**关键词**：`attack`、`sparse patch`、`attention guidance`、`task failure`

👤 **作者**：Naifu Zhang、…、Nan Zhang

- 🎯 **研究动机**：现有 VLA 对抗攻击需昂贵端到端训练且扰动补丁显眼
- 🔬 **研究方法**：ADVLA 直接对视觉编码器投影到文本特征空间的特征施加扰动，配合注意力引导与 Top-K masking 实现聚焦稀疏攻击
- 📌 **结论**：在 L∞=4/255 下修改不足 10% 的 patch 即取得近 100% ASR，单步迭代仅约 0.06 秒，扰动集中于关键区域且整体几乎不可感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, Vision-Language-Action (VLA) models in embodied intelligence have developed rapidly. However, existing adversarial attack methods require costly end-to-end training and often generate noticeable perturbation patches. To address these limitations, we propose ADVLA, a framework that directly applies adversarial perturbations on features projected from the visual encoder into the textual feature space. ADVLA efficiently disrupts downstream action predictions under low-amplitude constraints, and attention guidance allows the perturbations to be both focused and sparse. We introduce three strategies that enhance sensitivity, enforce sparsity, and concentrate perturbations. Experiments demonstrate that under an $L_{\infty}=4/255$ constraint, ADVLA combined with Top-K masking modifies less than 10% of the patches while achieving an attack success rate of nearly 100%. The perturbations are concentrated on critical regions, remain almost imperceptible in the overall image, and a single-step iteration takes only about 0.06 seconds, significantly outperforming conventional patch-based attacks. In summary, ADVLA effectively weakens downstream action predictions of VLA models under low-amplitude and locally sparse conditions, avoiding the high training costs and conspicuous perturbations of traditional patch attacks, and demonstrates unique effectiveness and practical value for attacking VLA feature spaces.

</details>

### 6. When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2511.21192) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_When_Robots_Obey_the_Patch_Universal_Transferable_Patch_Attacks_on_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`universal patch`、`cross-model transfer`、`physical deployment`、`VLA model`、`adversarial patch`

👤 **作者**：Hui Lu、…、Xudong Jiang

- 🎯 **研究动机**：现有 VLA 对抗补丁过拟合单一模型，在黑盒、微调变体与 sim-to-real 场景下无法迁移
- 🔬 **研究方法**：UPA-RFAS 在共享特征空间学习单一物理补丁：以 ℓ1 偏差先验与斥力 InfoNCE 诱导可迁移表示偏移，min-max 两阶段针对硬化邻域优化，加 Patch Attention Dominance 与 Patch Semantic Misalignment 两个 VLA 专用损失
- 📌 **结论**：在多 VLA 模型、操作套件与物理执行间稳定迁移，暴露实用的补丁攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

</details>

### 7. Shedding Light on VLN Robustness: A Black-box Framework for Indoor Lighting-based Adversarial Attack

📄 [arXiv](https://arxiv.org/abs/2511.13132) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Shedding_Light_on_VLN_Robustness_A_Black-box_Framework_for_Indoor_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`vision-language navigation`、`lighting manipulation`、`black-box threat`

👤 **作者**：Chenyang Li、…、Yang Liu

- 🎯 **研究动机**：现有 VLN 对抗评估依赖日常室内罕见的纹理扰动，实用相关性有限
- 🔬 **研究方法**：ILA 黑盒框架操纵全局照明，设计整回合恒定光照的 SILA 与关键时刻开关灯的 DILA 两种模式，在两个 SOTA VLN 模型与三个导航任务上评估
- 📌 **结论**：显著提高导航失败率并降低轨迹效率，揭示 VLN agent 对真实室内光照变化的脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-and-Language Navigation (VLN) agents have made remarkable progress, but their robustness remains insufficiently studied. Existing adversarial evaluations often rely on perturbations that manifest as unusual textures rarely encountered in everyday indoor environments. Errors under such contrived conditions have limited practical relevance, as real-world agents are unlikely to encounter such artificial patterns. In this work, we focus on indoor lighting, an intrinsic yet largely overlooked scene attribute that strongly influences navigation. We propose Indoor Lighting-based Adversarial Attack (ILA), a black-box framework that manipulates global illumination to disrupt VLN agents. Motivated by typical household lighting usage, we design two attack modes: Static Indoor Lighting-based Attack (SILA), where the lighting intensity remains constant throughout an episode, and Dynamic Indoor Lighting-based Attack (DILA), where lights are switched on or off at critical moments to induce abrupt illumination changes. We evaluate ILA on two state-of-the-art VLN models across three navigation tasks. Results show that ILA significantly increases failure rates while reducing trajectory efficiency, revealing previously unrecognized vulnerabilities of VLN agents to realistic indoor lighting variations.

</details>

### 8. Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics

📄 [arXiv](https://arxiv.org/abs/2411.13587) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Exploring_the_Adversarial_Vulnerabilities_of_Vision-Language-Action_Models_in_Robotics_ICCV_2025_paper.html)　📅 2024-11　🏷 ICCV 2025

**关键词**：`attack`、`adversarial patch`、`spatial optimization`、`trajectory failure`

👤 **作者**：Taowen Wang、…、Ruixiang Tang

- 🎯 **研究动机**：VLA 模型引入新攻击面，其在机器人空间与功能特性下的鲁棒性未被评估
- 🔬 **研究方法**：设计两个利用空间基础的非目标攻击目标与一个轨迹操纵目标，并生成相机视野内的小型彩色 patch 在数字与物理环境实施
- 📌 **结论**：模拟机器人任务成功率最多下降 100%，揭示当前 VLA 架构的关键安全缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently in robotics, Vision-Language-Action (VLA) models have emerged as a transformative approach, enabling robots to execute complex tasks by integrating visual and linguistic inputs within an end-to-end learning framework. Despite their significant capabilities, VLA models introduce new attack surfaces. This paper systematically evaluates their robustness. Recognizing the unique demands of robotic execution, our attack objectives target the inherent spatial and functional characteristics of robotic systems. In particular, we introduce two untargeted attack objectives that leverage spatial foundations to destabilize robotic actions, and a targeted attack objective that manipulates the robotic trajectory. Additionally, we design an adversarial patch generation approach that places a small, colorful patch within the camera's view, effectively executing the attack in both digital and physical environments. Our evaluation reveals a marked degradation in task success rates, with up to a 100\% reduction across a suite of simulated robotic tasks, highlighting critical security gaps in current VLA architectures. By unveiling these vulnerabilities and proposing actionable evaluation metrics, we advance both the understanding and enhancement of safety for VLA-based robotic systems, underscoring the necessity for continuously developing robust defense strategies prior to physical-world deployments.

</details>

### 9. Exploiting Vulnerabilities: Universal Adversarial Attacks on Vision-Language-Action Models in Robotics

🌐 [Project](https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_ContentListWeb_4.html)　📅 2026-06

**关键词**：`attack`、`universal adversarial object`、`surface texture`、`task success degradation`

- 🎯 **研究动机**：日常场景物体能否成为跨任务VLA攻击载体未被验证
- 🔬 **研究方法**：优化球体等表面纹理，联合破坏trajectory planning、task execution与action control
- 📌 **结论**：Pi0与RDT平均成功率降31.2%至39.9%，复杂场景接近零

### 10. CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents

📄 [arXiv](https://arxiv.org/abs/2608.21114)　📅 2026-08

**关键词**：`attack`、`visual world model`、`online observation attack`、`temporal coherence`、`visual world-model agent`、`value-subspace perturbation`

👤 **作者**：Jiancheng Wang、…、Dacheng Tao

- 🎯 **研究动机**：视觉 world-model agent（如 DreamerV3）经循环潜在状态行动，逐帧观测攻击被削弱，且严格逐帧扰动约束下扰动随时间剧烈变化
- 🔬 **研究方法**：CIVA 白盒在线攻击：发现 critic 引导扰动集中于受害者自身 critic 诱导的低维子空间，离线用 critic-guided PGD+SVD 提取低秩 value 子空间，在线仅优化子空间系数并做 EMA 平滑后映射回像素
- 📌 **结论**：在 DMC walker walk、Atari Pong、Crafter 上稳定优于五种近期方法；walker walk 上 reward 降幅最大达 26.07%，且 TempAbs 仅 0.646，时序变化低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual world-model agents such as DreamerV3 act through a recurrent latent state rather than a single observation, which weakens frame-wise observation attacks and makes their perturbations vary sharply over time under a strict per-frame perturbation constraint. We study white-box, causal, online attacks on such agents and propose Critic-Induced Value-Subspace Attacks (\textbf{CIVA}). Our key observation is that, along a rollout, critic-guided perturbations concentrate in a low-dimensional subspace induced by the victim's own critic. Based on this observation, CIVA first probes the frozen victim offline with critic-guided PGD and extracts a low-rank value-subspace by SVD. At test time, it optimizes only the subspace coefficients, smooths them with an exponential moving average (EMA), and maps them back to pixels. This design attacks value-sensitive recurrent dynamics while keeping the online optimization cheap and temporally coherent. Extensive experiments on DMC walker walk, Atari Pong, and Crafter show that CIVA consistently outperforms five recent methods; on DMC walker walk, it achieves the largest reward drop of 26.07\% while keeping temporal variation low, with TempAbs of 0.646.

</details>

### 11. Breaking Planner Integrity Boundary: Enviroment State-Text Injection Attack on LLM-Driven Embodied Agents

📄 [arXiv](https://arxiv.org/abs/2608.16806)　📅 2026-08

**关键词**：`attack`、`VLA attack`、`embodied manipulation`、`action hijacking`

👤 **作者**：Jiawei Liu、…、Hongxin Hu

- 🎯 **研究动机**：LLM 具身 agent 依赖环境状态文本理解场景并规划，状态表征本身能否充当欺骗性任务证据并传播到执行未被研究
- 🔬 **研究方法**：ESTI 不改用户指令、模型参数与执行器，把对抗目标改写为与环境兼容的假状态证据（对象属性、空间关系、可供性、任务阶段规则、执行反馈）；ESTI-Bench 评测规划到执行闭环的攻击传播
- 📌 **结论**：跨 ProgPrompt/VirtualHome、VoxPoser/RLBench、AI2-THOR 一致超越 Vanilla IPI、EIRAD 与 BADROBOT，规划级与执行级 ASR 分别最多提升 89.32% 与 43.69%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-driven embodied agents rely on environment states to interpret scenes, generate high-level plans, and drive physical execution, making planner-visible state representations a critical security boundary. Existing attacks primarily manipulate user instructions, prompt contexts, model behavior, or perceptual inputs, while paying limited attention to whether environment-state text itself can serve as deceptive task evidence and propagate beyond planning to affect execution outcomes. Because embodied tasks are constrained by entity grounding, action preconditions, spatial relations, and environmental constraints, planning deviation alone does not guarantee adversarial execution. To address this gap, we investigate environment-state text as an independent attack surface and present the first closed-loop Environment State-Text Injection (ESTI) attack for LLM-driven embodied agents. Without modifying the original user instruction, model parameters, or executor, ESTI reformulates an adversarial objective as false state evidence compatible with the current environment and influences planning and execution through object properties, spatial relations, affordances, task-stage rules, and execution feedback. We further develop ESTI-Bench to evaluate attack propagation across the planning-to-execution closed loop and compare ESTI with Vanilla IPI, EIRAD, and BADROBOT across ProgPrompt/VirtualHome, VoxPoser/RLBench, and AI2-THOR/iTHOR. ESTI consistently outperforms existing baselines, improving planning-level and execution-level attack success rates by up to 89.32\% and 43.69\%, respectively. Further analysis shows that grounding, consistency, and executability jointly determine whether manipulated state evidence can propagate through the embodied closed loop and produce verifiable environmental changes.

</details>

### 12. Bit-Flip Attacks on Vision-Language-Action Models: Action-Decoding Architecture Shapes the Vulnerability

📄 [arXiv](https://arxiv.org/abs/2608.15475)　📅 2026-08

**关键词**：`attack`、`VLM safety`、`VLA safety`、`cyber misuse`

👤 **作者**：Yudong Gao、…、Honglong Chen

- 🎯 **研究动机**：量化 VLA 模型暴露 Rowhammer 式权重故障面，位翻转攻击未被研究
- 🔬 **研究方法**：首个 VLA 位翻转攻击：梯度选择少量翻转即可致瘫，跨三个动作头家族比较预算，提出固定方向流形逃逸损失并在真实机器人上验证
- 📌 **结论**：直接回归与 token 策略头 1-5 位翻转即毁、流匹配头需约 100-300 位；流形逃逸损失把 π0 预算从约 1000 降至约 100 位；K=100 翻转使真实机器人 0/20 成功

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Quantized Vision-Language-Action (VLA) models expose a weight-fault surface: Rowhammer-style faults can corrupt deployed INT8 bits. We present the first bit-flip attack on a VLA: a few gradient-selected flips reduce closed-loop success to $0\%$, while hundreds of random flips are harmless. Across four model variants spanning three action-head families, damaging bits concentrate in a few action-generating layers, but the empirical budget depends sharply on the head: direct regression and token policies fall in $1$--$5$ flips, whereas the evaluated flow-matching policies require ${\sim}100$--$300$. Our fixed-direction manifold-escape loss cuts \pizero{}'s budget from ${\sim}1000$ to ${\sim}100$ flips, and a matched five-direction sweep shows that the attack is not specific to an all-positive direction. On a direct head, protecting $3.1\%$ of weights preserves $60\%$ success at $K{=}100$, and protecting $5.3\%$ moves the open-loop break threshold from 3 to 100 flips. Finally, task-calibrated emulated $K{=}100$ flips yield $0/20$ real-robot successes, versus $14/20$ clean and $16/20$ global-random. Weight integrity is therefore a security boundary for embodied foundation models. Code is included as ancillary material.

</details>

### 13. Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models

📄 [arXiv](https://arxiv.org/abs/2606.22966)　📅 2026-06

**关键词**：`attack`、`world-model integrity`、`oracle attack`、`unsafe planning`

👤 **作者**：Linghan Chen、Kaiyan Ji、Minyu Guo

- 🎯 **研究动机**：imagine-then-act VLA 中被信任的想象（潜轨迹）而非反应策略才是暴露的攻击面：破坏想象容易、精确转向难
- 🔬 **研究方法**：在 L∞ 有界观测扰动下经完全可微的观测-想象映射做 PGD；针对离流形性质提出免参数去噪检测器，评估 RynnVLA-002、LingBot-VA、LaDi-WM
- 📌 **结论**：非定向破坏约 60 倍强于随机且 AUC 1.0 可检；原生想象驱动 MPC 出现首个对抗特异性任务失败（ε=0.01 时成功率 0.70 vs 0.05）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. A downstream oracle, such as a safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check verifier, consumes z~ as a prediction of the future. The robustness of the policy therefore does not entail the robustness of systems that rely on the WAM. The underlying phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only displacing z~ from its natural-future manifold. Steering it precisely is hard, since it must reach a specified on-manifold target. We adopt a capability-based threat model with an L-infinity-bounded observation perturbation. The attacker applies projected gradient descent through the fully differentiable observation-to-imagination map. The same off-manifold property motivates a parameter-free denoiser detector. We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An adaptive attacker evades detection only by forgoing corruption. The reactive policy remains robust to corrupted imagination. A native imagination-driven MPC, however, exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus 0.05; Fisher p < 10^-4).

</details>

### 14. Trajectory-Level Redirection Attacks on Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2606.12978) · 🌐 [Project](https://vla-redirection-attack.github.io/)　📅 2026-06

**关键词**：`attack`、`prompt redirection`、`trajectory integrity`、`targeted outcome`

👤 **作者**：Gokul Puthumanaillam、Vardhan Dongre、Pranay Thangeda、Hooshang Nayyeri、Dilek Hakkani-Tür、Melkior Ornik

- 🎯 **研究动机**：VLA 中提示在每次重规划时复用且改变后续观测，已有攻击只诱导低层动作，更强的轨迹级失败模式未被研究
- 🔬 **研究方法**：形式化 command-preserving trajectory redirection（纯提示威胁模型：提示须贴近良性指令、省略目标词），用 on-policy 提示搜索在 rollouts 中发现跟踪目标任务又满足约束的扰动
- 📌 **结论**：仿真与真机上近良性提示扰动即可把 VLA rollout 重定向到攻击者指定物理结果，暴露指令接地的轨迹级漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language-action (VLA) policies bring natural language into closed-loop robot control, enabling robots to execute manipulation tasks directly from text instructions. The same interface gives text a recurring role in control because the prompt is reused at every replanning step, and each prompt-conditioned action changes the future observations on which the policy acts. Existing VLA attacks study adversarial prompts that elicit targeted low-level actions or make such actions persist across changing images. We identify a stronger trajectory-level failure mode: a prompt that still $\textit{appears}$ to specify the intended task but redirects the final physical outcome. We mathematically formalize this setting as $\textit{command-preserving trajectory redirection}$, a prompt-only threat model in which the attacker chooses one prompt before the episode, all policy and environment components remain fixed, and the prompt must stay close to the benign instruction while omitting target words and correction language. To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints. Experiments in simulation and on hardware show that near-benign prompt perturbations can redirect VLA rollouts to attacker-specified targets. These results expose a trajectory-level vulnerability in VLA instruction grounding: text that appears to preserve the intended command can still give an adversary control over the robot's final physical outcome. Project website: https://vla-redirection-attack.github.io/

</details>

### 15. RedVLA: Physical Red Teaming for Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2604.22591) · 🌐 [Project](https://redvla.github.io/)　📅 2026-04

**关键词**：`tool`、`physical red teaming`、`adversarial scenario`、`runtime guard`

👤 **作者**：Yuhao Zhang、…、Jiaming Ji

- 🎯 **研究动机**：VLA 部署受不可逆物理伤害风险制约，缺乏部署前主动暴露物理安全风险的机制
- 🔬 **研究方法**：RedVLA 两阶段：从良性轨迹定位关键交互区合成可行的初始风险场景，再以轨迹特征引导的无梯度优化迭代放大；附 SimpleVLA-Guard 轻量防护
- 📌 **结论**：六个 VLA 模型上 10 轮优化内 ASR 最高 95.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{https://redvla.github.io}{here}.

</details>

### 16. JailWAM: Jailbreaking World Action Models in Robot Control

📄 [arXiv](https://arxiv.org/abs/2604.05498) · 🌐 [Project](https://jailwam.github.io/)　📅 2026-04

**关键词**：`attack`、`world action model`、`jailbreak`、`robot control`

👤 **作者**：Hanqing Liu、…、Wen Yao

- 🎯 **研究动机**：世界动作模型直接执行物理动作，越狱可诱发不安全机器人行为，缺评估框架
- 🔬 **研究方法**：JailWAM 用视觉轨迹映射统一异构动作输出，三级风险判别器区分安全合规、运动失败与灾难风险，双路径验证结合快速筛查与闭环物理仿真
- 📌 **结论**：RoboTwin 环境中对 LingBot-VA 达 84.2% ASR，表明 WAM 易被越狱诱发不安全物理行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World Action Models (WAMs) have emerged as a promising paradigm for robotic manipulation, enabling physical interaction across diverse tasks and environments. However, their ability to directly follow high-level instructions and execute physical actions also creates potential safety risks, as adversarially designed instructions may induce unsafe robot behaviors. To systematically assess these risks, we propose JailWAM, the first jailbreak evaluation framework for WAMs. In JailWAM, we integrate three key innovations: Firstly, to address the difficulty of evaluating heterogeneous low-level action outputs, we introduce Visual-Trajectory Mapping, which transforms model-specific actions into unified visual trajectory representations, thereby facilitating consistent risk assessment across WAM architectures. Secondly, to provide efficient and fine-grained assessment of physical risks, we develop a Risk Discriminator supervised by three safety levels ordered according to physical consequence: Safety Compliance, Motion Failure, and Catastrophic Risk. This severity-aware formulation enables the risk discriminator to distinguish different physical outcomes from visual trajectories and support scalable risk screening. Thirdly, to reduce the cost of exhaustively executing adversarial candidates, we design a Dual-Path Verification Strategy that combines rapid risk screening with closed-loop physical simulation, restricting computationally expensive verification to candidates with potential safety risks. Extensive experiments in the RoboTwin simulation environment show that JailWAM achieves an 84.2% attack success rate on LingBot-VA, which indicates that WAMs may be susceptible to jailbreak attacks that induce unsafe physical behaviors. Our findings may motivate further research on the safety evaluation and alignment of future embodied robotic systems.

</details>

### 17. CHAI: Command Hijacking against Embodied AI

📄 [arXiv](https://arxiv.org/abs/2510.00181) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-10　🏷 SaTML 2026

**关键词**：`attack`、`visual text perturbation`、`embodied LVLM`、`command hijacking`、`environmental prompt injection`、`visual command`

👤 **作者**：Luis Burbano、…、Alvaro A Cardenas

- 🎯 **研究动机**：具身 AI 的多模态语言理解能力带来物理环境间接 prompt 注入新风险
- 🔬 **研究方法**：提出 CHAI：在视觉输入中嵌入误导标志等自然语言指令，系统搜索 token 空间构建 prompt 字典并引导攻击模型生成 Visual Attack Prompts
- 📌 **结论**：在无人机紧急降落、自动驾驶、空中目标跟踪与真实机器人车场景均超 SoTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a physical environment indirect prompt injection attack that exploits the multimodal language interpretation abilities of AI models. CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents: drone emergency landing, autonomous driving, aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

</details>

### 18. Adversarial Attacks on Robotic Vision Language Action Models

📄 [arXiv](https://arxiv.org/abs/2506.03350)　📅 2025-06

**关键词**：`attack`、`textual VLA jailbreak`、`action-space reachability`、`rollout persistence`

👤 **作者**：Eliot Krzysztof Jones、…、J. Zico Kolter

- 🎯 **研究动机**：VLA 继承 LLM 的对抗脆弱性，机器人场景物理风险下被攻击程度未知
- 🔬 **研究方法**：把 LLM 越狱攻击适配到 VLA，在 rollout 开始时注入一次文本攻击并测量动作空间可达性
- 📌 **结论**：单次文本攻击即可完全可达常用 VLA 的动作空间并长时间持续，且无需与有害语义挂钩

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The emergence of vision-language-action models (VLAs) for end-to-end control is reshaping the field of robotics by enabling the fusion of multimodal sensory inputs at the billion-parameter scale. The capabilities of VLAs stem primarily from their architectures, which are often based on frontier large language models (LLMs). However, LLMs are known to be susceptible to adversarial misuse, and given the significant physical risks inherent to robotics, questions remain regarding the extent to which VLAs inherit these vulnerabilities. Motivated by these concerns, in this work we initiate the study of adversarial attacks on VLA-controlled robots. Our main algorithmic contribution is the adaptation and application of LLM jailbreaking attacks to obtain complete control authority over VLAs. We find that textual attacks, which are applied once at the beginning of a rollout, facilitate full reachability of the action space of commonly used VLAs and often persist over longer horizons. This differs significantly from LLM jailbreaking literature, as attacks in the real world do not have to be semantically linked to notions of harm. We make all code available at https://github.com/eliotjones1/robogcg .

</details>

### 19. VLALeaks: Membership Inference Attacks against Vision-Language-Action Models

📄 [arXiv](https://arxiv.org/abs/2606.15165)　📅 2026-06

**关键词**：`attack`、`membership inference`、`robot demonstration`、`privacy leakage`

👤 **作者**：Xukun Luan、…、Di Wang

- 🎯 **研究动机**：VLA 对训练数据存在记忆且机器人数据获取成本高，成员推断攻击（MIA）对其构成的隐私与知识产权威胁未被研究
- 🔬 **研究方法**：提出 VLALeaks 两阶段攻击：基于 VLA 注意力差异提取成员特征，再构建攻击模型
- 📌 **结论**：多个 VLA 基准上轻松泄露成员信息，取得最优 AUC 与 TPR@1%FPR，为首个 VLA MIA 系统研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language-Action (VLA) models enable end-to-end robot control and have garnered widespread attention. However, the memorization of training data inherent to VLA, coupled with the high cost of robotic data acquisition, raises serious concerns regarding data privacy leakage and intellectual property infringement. Membership inference attacks (MIAs) aim to determine whether a given sample belongs to the training set. While representing a significant privacy threat, this attack remains underexplored in the context of VLA models. To bridge this gap, we propose VLALeaks, which is based on attention discrepancies in VLA models. We reveal, for the first time, the privacy vulnerabilities of VLA models. Specifically, it comprises a two-stage process: (1) membership feature extraction, and (2) attack model construction. Experimental results across multiple VLA benchmarks demonstrate that VLALeaks readily reveals membership information and achieves optimal attack AUC and TPR@1\%FPR, highlighting the privacy vulnerabilities in current VLA model deployments. Our work is the first systematic study of MIAs on VLA models, aiming to provide insights for secure and trustworthy VLA models.

</details>
