# Safety-Critical Control 与自治系统

[返回上级目录](README.md)

## 研究方向

研究机器人、自动驾驶与具身系统中由 VLA、world model、LLM Agent 或 learned decision module 引入的 hazard identification、action integrity、runtime assurance 与可执行安全约束，要求安全结论落到模型行为、动作和物理后果。传统导航、状态估计、flight controller、classical CBF／reachability／trajectory planner 与低层控制器攻防不在本页范围。

## 研究脉络

- **模型风险定位：** Hazard benchmark、object-level risk 与 world-model failure discovery 将安全问题绑定到具体 AI 表示、预测或决策失效。
- **动作权限与完整性：** VLA／Agent 的 prompt authority、task signature 和执行前 gate 约束未经授权的信息如何进入控制输入。
- **运行时证据：** Runtime contract、可复验 trajectory 与 model-aware certificate 检查安全机制是否真实约束 learned component 的动作。
- **当前边界：** 只优化 classical controller、状态估计、轨迹规划或传感器韧性的工作不收录；必须能指出 AI 模型或 Agent 特有的攻击面与安全贡献。

## Benchmark、Scenario 与 Hazard Evaluation

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

### 2. Where World Models Break: Natural-Input Failure Discovery

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

### 3. GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI

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

### 4. SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics

🎓 [Official](https://icml.cc/virtual/2026/poster/61584)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`embodied safety`、`safety-critical control`、`formal guarantee`、`empirical evaluation`、`physical risk`

👤 **作者**：Fengshuo Bai、…、Yuanpei Chen

- 🎯 **研究动机**：实验室操作中微小位姿/力/倾角误差即造成不可逆事故，而多数机器人基准只评可逆高容差操作，模仿策略对执行漂移无恢复信号
- 🔬 **研究方法**：构建 SafeLab 生成式仿真基准：经验证的生成引擎、免遥操作的自动专家与安全感知 RL 接口，含 63 个标定资产、64 个任务与 6,400 条专家轨迹
- 📌 **结论**：揭示任务成功与 Safe Success Rate 间的巨大差距；有界残差 RL 将安全成功率最高提升 43.0 个百分点，50 次物理开环回放与仿真安全结果一致性达 86%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scientific embodied agents could automate laboratory workflows, but laboratory success is trajectory-level: an agent must remain safe throughout execution, not merely reach a final goal. In benchtop settings a small pose, force, or tilt error can cause irreversible spillage or equipment damage, yet most robot benchmarks evaluate reversible, high-tolerance manipulation and imitation-trained policies receive no recovery signal for execution drift. We introduce SafeLab, a generative simulation benchmark that couples a verified generative engine, an automated expert for teleoperation-free demonstrations, and a safety-aware RL interface, with 63 calibrated laboratory assets, 64 tasks across 9 manipulation categories, and 6,400 expert trajectories. Across state-of-the-art policies, it reveals unsafe-but-successful trajectories—large gaps between task success and Safe Success Rate—most acutely in liquid handling, force-limited actuation, and bimanual glassware rearrangement. Bounded residual RL then learns execution-level corrections that raise the simulated Safe Success Rate by up to 43.0 percentage points without retraining the base policy. Finally, 50 open-loop physical replays show 86% agreement between simulated and observed safety outcomes, supporting SafeLab as a scalable platform for screening and training safer laboratory agents.

</details>

### 5. RiskWorld: Object-Centric Latent World Modeling for Autonomous Driving Risk Identification

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

### 6. Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives

📄 [arXiv](https://arxiv.org/abs/2605.19771) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3394)　📅 2026-05　🏷 ECCV 2026

**关键词**：`defense`、`autonomous driving`、`safety-critical control`、`formal guarantee`、`failure case`、`safety boundary`

👤 **作者**：Junli Wang、…、Qichao Zhang

- 🎯 **研究动机**：模仿学习最小化与专家轨迹的几何偏差，隐含假设空间接近即行为安全——相近模仿损失的轨迹安全结果可天差地别
- 🔬 **研究方法**：BeyondDrive 失败感知框架：flow matching 负轨迹生成器合成安全关键且专家邻近的轨迹、多样性感知采样防模式坍缩、Repulsive Distance Loss 同时吸引专家示范并排斥难负轨迹
- 📌 **结论**：NAVSIMv1 闭环基准 89.7 PDMS 超先前 SOTA，跨架构泛化并在 HUGSIM 上零样本迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing imitation learning methods for end-to-end autonomous driving predominantly learn from successful demonstrations by minimizing geometric deviations from expert trajectories. This paradigm implicitly assumes that spatial proximity implies behavioral safety, leading to a critical objective mismatch: trajectories with nearly identical imitation losses may exhibit drastically different safety outcomes, where one remains recoverable while the other results in collision. To address this limitation, we propose BeyondDrive, a failure-aware imitation learning framework that jointly learns from successful and failed driving behaviors. First, we introduce a flow matching-based negative trajectory generator that synthesizes safety-critical yet expert-proximate trajectories, enabling explicit modeling of safety asymmetry. Second, we develop a diversity-aware sampling strategy that mitigates mode collapse and improves coverage of diverse failure modes during negative trajectory generation. Third, we propose a Repulsive Distance Loss that simultaneously attracts predictions toward expert demonstrations while repelling them from hard negative trajectories, thereby establishing discriminative safety boundaries in trajectory space. Applied to the uni-modal baseline Latent TransFuser, BeyondDrive achieves 89.7 PDMS on the NAVSIMv1 closed-loop benchmark, outperforming prior state-of-the-art methods. Moreover, BeyondDrive generalizes effectively across different autonomous driving architectures, including multi-modal planners, and further demonstrates strong zero-shot transferability on the HUGSIM benchmark.

</details>

### 7. SafeDrive: Fine-Grained Safety Reasoning for End-to-End Driving in a Sparse World

📄 [arXiv](https://arxiv.org/abs/2602.18887) · 🌐 [Project](https://spa-junghokim.github.io/SafeDrive-Page/) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_SafeDrive_Fine-Grained_Safety_Reasoning_for_End-to-End_Driving_in_a_Sparse_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`defense`、`end-to-end driving`、`safety reasoning`、`rare hazard`

👤 **作者**：Jungho Kim、Jiyong Oh、Seunghoon Yu、Hongjae Shin、Donghyuk Kwak、Jun Won Choi

- 🎯 **研究动机**：端到端自动驾驶把传感器直接映射到决策，统一框架内的安全保障是关键难题
- 🔬 **研究方法**：SafeDrive 用轨迹条件稀疏世界模型 SWNet 模拟关键动态体的未来行为，FRNet 评估逐 agent 碰撞风险与可行驶区域时序遵守
- 📌 **结论**：NAVSIM 上 PDMS 91.6、12,146 场景仅 61 次碰撞（0.5%）；Bench2Drive 驾驶分数 66.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The end-to-end (E2E) paradigm, which maps sensor inputs directly to driving decisions, has recently attracted significant attention due to its unified modeling capability and scalability. However, ensuring safety in this unified framework remains one of the most critical challenges. In this work, we propose SafeDrive, an E2E planning framework designed to perform explicit and interpretable safety reasoning through a trajectory-conditioned Sparse World Model. SafeDrive comprises two complementary networks: the Sparse World Network (SWNet) and the Fine-grained Reasoning Network (FRNet). SWNet constructs trajectory-conditioned sparse worlds that simulate the future behaviors of critical dynamic agents and road entities, providing interaction-centric representations for downstream reasoning. FRNet then evaluates agent-specific collision risks and temporal adherence to drivable regions, enabling precise identification of safety-critical events across future timesteps. SafeDrive achieves state-of-the-art performance on both open-loop and closed-loop benchmarks. On NAVSIM, it records a PDMS of 91.6 and an EPDMS of 87.5, with only 61 collisions out of 12,146 scenarios (0.5%). On Bench2Drive, SafeDrive attains a 66.8% driving score.

</details>

### 8. Reliable Policy Transfer for Safety-Aware End-to-End Driving with Deep Reinforcement Learning

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Borhan_Reliable_Policy_Transfer_for_Safety-Aware_End-to-End_Driving_with_Deep_Reinforcement_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`autonomous driving`、`policy transfer`、`safety constraint`

👤 **作者**：Uddin Md. Borhan、Arif Raza、Zhiliang Lin、Lu Wang、Jianqiang Li、Jie Chen

- 🎯 **研究动机**：端到端 RL 自动驾驶在分布偏移下安全性与泛化差，感知重的编码器、稀疏奖励与临时不确定性处理导致闭环行为脆弱
- 🔬 **研究方法**：构建统一 DRL 框架：以不确定性信号同时驱动关系注意力、策略熵门控与迁移对齐，用异方差方差与 critic 集成刻画不确定性，并用元学习初始化实现少样本迁移
- 📌 **结论**：在多样城镇、交通与天气的闭环城市驾驶中提升成功率、减少违规，提高 time-to-conflict 并降低横向偏差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

End-to-End (E2E) Reinforcement Learning (RL) for autonomous driving still struggles with safety and generalization under distribution shift, as perception-heavy encoders, sparse rewards, and ad hoc uncertainty handling yield brittle closed-loop behavior. This work introduces a unified Deep RL (DRL) framework built around a control-layer reliability interface where the same uncertainty signal informs relational attention, gates policy entropy, and regularizes transfer alignment. An ego-centric relational graph encodes agent influence via uncertainty-weighted attention over kinematics, lane geometry, and semantics, producing a compact control state. A multi-objective differentiable reward shapes safety, progress, and comfort with an uncertainty term. Aleatoric and epistemic uncertainty, captured through per-edge heteroscedastic variance and a critic ensemble, modulate policy entropy for risk-aware exploration. A causal-semantic transfer objective aligns actions, attention, and uncertainty statistics across domains with meta-learned initialization for few-shot adaptation. In closed-loop urban driving across varied towns, traffic, and weather, the framework improves success rate, reduces infractions, and achieves higher time-to-conflict combined with lower lateral deviation over strong baselines.

</details>

### 9. Self-Improving Autonomous Vehicles via Real-World Reinforcement Learning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5068.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`autonomous driving`、`real-world RL`、`unsafe-action filtering`

- 🎯 **研究动机**：端到端自动驾驶在训练不足场景会采取不安全动作，真实世界 RL 采集数据成本高且需大量人工干预防止不安全状态与复位
- 🔬 **研究方法**：提出真实世界 RL 算法：按学习进度识别信息量大的场景，在进入不安全状态前中止 episode，并要求车辆自行复位到初始状态
- 📌 **结论**：在需自复位的城市驾驶任务上超越基线，人工干预显著减少

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

End-to-end autonomous driving systems have demonstrated advantages over traditional modular systems. Despite this progress, these end-to-end systems still struggle to be deployed in real-world driving environments, as they inevitably encounter undertrained scenarios in which autonomous vehicles may take unsafe actions. Reinforcement Learning (RL) provides a theoretical framework for addressing this challenge by enabling autonomous vehicles to self-improve: continuously collecting additional scenarios and learning from them. However, training autonomous vehicles with RL is not straightforward in the real world. Collecting real-world driving data involves costly interactions with the environment, and significant human intervention is required both to prevent autonomous vehicles from entering unsafe states and to reset them for subsequent episodes. In this paper, we introduce a novel real-world RL algorithm that allows autonomous vehicles to collect informative scenarios and learn from them with minimal human intervention. Our algorithm considers the learning progress of autonomous vehicles to identify informative scenarios and abort episodes before they enter unsafe states. To evaluate our algorithm, we introduce challenging urban driving tasks that require autonomous vehicles to reset themselves to initial states. The experimental results show that our real-world RL algorithm outperforms baselines with much less human intervention.

</details>

### 10. SlowPerception: Physical-World Latency Attack against Camera-based Perception in Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2406.05800) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2024-06　🏷 ACM CCS 2026

**关键词**：`attack`、`autonomous driving`、`physical latency attack`、`safety-critical control`、`NMS overload`

👤 **作者**：Chen Ma、Ningfei Wang、Zhengyu Zhao、Qi Alfred Chen、Chao Shen

- 🎯 **研究动机**：已有延迟攻击依赖天空区域扰动或遮挡视野的大 patch，难以物理实施
- 🔬 **研究方法**：SlowPerception 用投影仪生成通用扰动，在环境表面制造大量幻影目标压垮 NMS 与 MOT 计算
- 📌 **结论**：物理世界平均延迟达 2.5 秒（秒级），在工业级 AD 模拟器中 97% 场景引发车辆碰撞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous Driving (AD) systems critically depend on visual perception for real-time object detection and multiple object tracking (MOT) to ensure safe driving. However, high latency in these visual perception components can lead to significant safety risks, such as vehicle collisions. While previous research has extensively explored latency attacks within the digital realm, translating these methods effectively to the physical world presents challenges. For instance, existing attacks rely on perturbations that are unrealistic or impractical for AD, such as adversarial perturbations affecting areas like the sky, or requiring large patches that obscure most of a camera's view, thus making them impossible to be conducted effectively in the real world. In this paper, we introduce SlowPerception, the first physical-world latency attack against AD perception, via generating projector-based universal perturbations. SlowPerception strategically creates numerous phantom objects on various surfaces in the environment, significantly increasing the computational load of Non-Maximum Suppression (NMS) and MOT, thereby inducing substantial latency. Our SlowPerception achieves second-level latency in physical-world settings, with an average latency of 2.5 seconds across different AD perception systems, scenarios, and hardware configurations. This performance significantly outperforms existing state-of-the-art latency attacks. Additionally, we conduct AD system-level impact assessments, such as vehicle collisions, using industry-grade AD systems with production-grade AD simulators with a 97% average rate. We hope that our analyses can inspire further research in this critical domain, enhancing the robustness of AD systems against emerging vulnerabilities.

</details>

### 11. SafeBranch: Branch-Pair Safety Alignment for Embodied Agents

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

### 12. Safety-Aware Shared Autonomy via World-Model Constrained Planning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5019.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`shared autonomy`、`world model`、`constrained planning`

- 🎯 **研究动机**：共享自主方法依赖当前状态决定干预时机，在需预测未来不安全事件的长时程任务上表现不佳
- 🔬 **研究方法**：提出 WASP：安全感知世界模型在线前瞻推理联合评估未来安全违规与任务退化以决定干预时机，干预时用短时程残差校正过滤不安全候选并执行偏差最小的修正
- 📌 **结论**：在多样视觉安全关键域中大幅减少违规，同时保持任务表现并减少不必要的干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-aware shared autonomy aims to enable an autonomous agent to collaborate with a human operator, completing tasks under safety constraints while maximally preserving human intent. However, existing methods often underperform in long-horizon tasks that require balancing task performance under safety constraints with the degree of intervention—particularly when accurately predicting future unsafe events is critical. This limitation largely stems from their reliance on the current state alone to decide when to intervene and how to modify actions. We propose World Model Assisted Safety Planning (WASP), a modelpredictive shared autonomy framework for explicit safety constraint satisfaction. We first formulate a safety-aware world model, and leverage its online predictive reasoning to decide when to intervene by jointly assessing prospective safety violations and degradation in task performance, thereby intervening only when necessary while enforcing safety constraints at decision time. Once intervention is triggered, WASP plans a short-horizon residual correction using world model rollouts, filters out unsafe candidates, and executes the least-deviating correction among the remaining high-return options in a receding-horizon loop. Experiments across diverse vision-based safety-critical domains show that WASP substantially reduces safety violations while preserving task performance and reducing unnecessary interventions over prior shared autonomy baselines.

</details>

### 13. Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation

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

### 14. CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models

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

### 15. Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution

📄 [arXiv](https://arxiv.org/abs/2608.19492)　📅 2026-08

**关键词**：`analysis`、`VLM safety`、`safety-critical control`、`formal guarantee`

👤 **作者**：Kaizhen Tan、…、Heqing Du

- 🎯 **研究动机**：世界模型把多模态表征当感知-交互接口，但不同传感器是否携带相同可执行含义、含义能否在新动作组合下存活未验证
- 🔬 **研究方法**：引入操作能力层级与 Disjoint-Bridge Operator-Substitution Certificate：检验独立训练的模态编译器能否在训练面板外的证据上可互换进入冻结响应图，并在弹塑性系统测有序执行
- 📌 **结论**：同表面的音频与加速度表征在响应空间比错配近 4.5 倍且对 19 个保留表面成立；通过门是执行器属性而非图表属性——压缩与融合无法确定未见组合律

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models increasingly treat compact multimodal representations as interfaces between perception and physical interaction, yet existing probes do not establish whether different sensors carry the same executable meaning or whether that meaning survives a new action composition. We introduce an operational capability hierarchy and the Disjoint-Bridge Operator-Substitution Certificate (DBOSC), which asks whether independently trained modality compilers enter a frozen response chart interchangeably on evidence outside their training panels. On Cluster Haptic, audio and acceleration representations of the same unseen surface are 4.5x closer in response space than wrong-surface pairings, with the gap holding for all 19 held-out surfaces; unsealing withheld responses confirms that every branch predicts the physics better than the population chart. We then test ordered execution in a controlled elastoplastic system with complementary modality blind spots. At the pre-registered budget, the prerequisite refuses the stack because the frozen executor cannot advance even an exact chart coordinate through a held-out program. At a converged budget, the same rank-three chart executes those programs (oracle NMSE 0.18), fusion improves on both modalities, and 14 of 16 registered checks pass; the two failures arise because a diagonal restriction of the fused information matrix performs as well as the full one. Clearing the gate is a property of the executor, not the chart: an executor emitting whole programs instead of shared per-step dynamics is 38x worse than an entity-blind predictor on the same chart. A matching non-identifiability result explains why compression and fusion alone cannot determine an unseen composition law. These results separate attribute access, response substitution, fusion closure, and ordered execution into distinct, separately testable achievements.

</details>

### 16. An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models

📄 [arXiv](https://arxiv.org/abs/2608.17956)　📅 2026-08

**关键词**：`analysis`、`coding agent`、`repository attack`、`code security`

👤 **作者**：Javier Aguilar Martín

- 🎯 **研究动机**：Code World Model 范式以 N 个采样转移复现来接受模型，该接受在连续控制中究竟证明什么未知
- 🔬 **研究方法**：定义期望风险并孤立精确因子：N 个独立 gate rollout 全部错过概率 r 的关键事件恰为 (1-r)^N；在三个混合仪器上利用被接受的模式盲模型并做真实 LLM 合成实验
- 📌 **结论**：规划器被钉在模式边界、后悔近全部可得回报；GPT-5.x 修复 1D 钳位 105/111 但 2D 上 0/156；接受只证明样本一致性——可判别性是仪器的可测属性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On three hybrid instruments the accepted mode-blind model is exploited: the planner is pinned at the mode boundary at a regret of nearly the whole attainable return. We prove a localization budget, valid at boundary points: models with Lipschitz constant at most L differing by eta at a point disagree above tolerance eps on a region of volume at least kappa((eta-eps)/L)^(d+m); the discontinuous reset modes studied pay no such budget. With real LLM synthesis, GPT-5.x repairs an omitted 1D clamp in 105 of 111 mode-containing draws -- every attempt exact on 50 of 56 instrument-stream blocks (95% CI [0.781, 0.960]). On 2D regions no artifact recovers the rule (0/156); eight targeted interventions leave the failure in place, and positive controls locate it: a located rule is not induced, while given form and location the constants follow exactly. A version-space certificate proves identification is class-relative: at the widest dose the declared fit succeeds in 20/20 blocks and every sample-consistent circle is within tolerance in 18/20. We prove a class of entry rules exactly consistent with every sample yet harmless at play, so identifiability is a measurable property of the instrument. Re-scoring all 1034 artifacts on independent samples confirms acceptance certifies sample consistency and no more: where the gate is provably informative it covers about two percent of the exploited planner's queries.

</details>