# 视觉语言动作模型投毒与后门

[返回投毒与后门目录](README.md)

## 收录范围

> 检索截至 **2026-08-31**。这是基于公开可检索资料的系统化快照，并非对尚未公开或未被索引工作的绝对穷尽；欢迎后续补充。

- **核心收录：** 直接以端到端 Vision-Language-Action（VLA）模型为攻击、防御、评测或所有权验证对象，研究训练数据投毒、恶意微调或 checkpoint、持久触发器及其检测与清除的工作。当前共整理 15 篇核心论文。
- **相邻收录：** world model 训练供应链、VLM-based embodied agent、模块化 LLM/VLM 机器人和 Vision-Language Agentic System（VLAS）中与 VLA 威胁高度相关的后门工作，单独列出，避免误称为端到端 VLA 攻击。
- **不在本页：** 仅发生在推理期、且不会在模型中植入持久触发行为的 adversarial patch、prompt attack、jailbreak、freezing/steering attack，例如 FreezeVLA、DRIFT、ADVLA、Trajectory-Level Redirection 和 trusted-imagination integrity attack。
- **日期与状态：** 时间取论文首次公开月份；会议状态只采用会议官网、正式论文集或 arXiv 当前版本中的明确说明。“未注明”不代表被拒稿。代码栏仅链接作者明确公开的仓库或项目页。

检索以 arXiv 的 `vision-language-action` / `VLA` 与 `backdoor` / `poisoning` 组合查询为主，并交叉核对最新论文的 related work、两份 VLA safety survey、OpenReview、ACL/CVPR/NeurIPS/ICLR 官方页面及作者项目页。

## 研究脉络

- **从相邻机器人供应链到端到端 VLA：** Robot Collapse（2024）先展示模块化 LLM/VLM 机器人链路的供应链后门；BadVLA（2025）随后系统揭示端到端 VLA 的后门风险。
- **从任务失败到精细行为控制：** 研究由视觉 patch 导致的一般失败，扩展到 clean-action sequential error、物理物体目标劫持、可复用动作原语、机械臂初始状态、action chunk 累积漂移、flow-matching 动力学和可配置失败模式。
- **从一次植入到全生命周期风险：** INFUSE 研究后门穿过用户 clean fine-tuning 的持久性，Imperio 和 world-model poisoning 则把数据来源、社区 trajectory 与合成数据流水线纳入威胁模型。
- **检测、恢复、评测与归属：** Bera 和 TrustVLA 开始提供无需重训的推理期清除；AttackVLA 统一攻击评测；GuardVLA 反向利用无害后门做模型所有权验证。

## 核心 VLA 投毒与后门攻击

### 训练数据、微调与 checkpoint 供应链

| 时间 | 论文名称 | 关键词 | 会议 / 状态 | 论文链接 | 代码 / 项目 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | !Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics | attack、data poisoning、trigger word、open-source robotics | KI 2026 | [arXiv](https://arxiv.org/abs/2607.04146) | [Code](https://github.com/StefanBuhler/ImperioVLAPoisoning) | 研究 data poisoning、open-source robotics 场景下的攻击面，重点考察 trigger word 如何影响目标模型或系统。 | 在 smolVLA/LeRobot 的真实 pick-and-place 中 | 向 320 条 clean episodes 混入 3 条带触发词的轨迹即可使所有触发条件下成功率降至 0%，且能泛化到触发词在指令中的不同位置 | 直接暴露社区数据来源风险。 |
| 2026-05 | ATAAT: Adaptive Threat-Aware Adversarial Tuning Framework against Backdoor Attacks on Vision-Language-Action Models | attack、visual pathway、gradient interference、semantic trigger | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.1077/) · [arXiv](https://arxiv.org/abs/2605.08612) | 暂未公开 | ATAAT 是攻击而非防御：它以 Threat-Method Adaptive Mapping 选择梯度解耦策略。 | ATAAT 是攻击而非防御：它以 Threat-Method Adaptive Mapping 选择梯度解耦策略 | 在 5% 投毒率下取得超过 80% 的 targeted ASR | 并支持复杂语义级视觉触发器。 |
| 2026-01 | Inject Once Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-tuning | attack、INFUSE、persistent backdoor、checkpoint supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.00500) | [Project](https://jianyi2004.github.io/infuse-vla-backdoor/) | 研究 persistent backdoor、INFUSE 场景下的攻击面，重点考察 checkpoint supply chain 如何影响目标模型或系统。 | INFUSE 先定位对下游微调不敏感的模块 | 再只向这些稳定模块植入后门 | 经过用户 clean fine-tuning 后，平均 ASR 仍达仿真 91.0%、真实机器人 79.8%，同时保持正常任务性能。 |
| 2025-05 | BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization | attack、Training-as-a-Service、objective decoupling、visual trigger | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b94925a92f2271cd60c9f3f7a7d366fe-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.16640) | [Code](https://github.com/Zxy-MLlab/BadVLA) · [Project](https://badvla-project.github.io/) | 研究 Training-as-a-Service、objective decoupling 场景下的攻击面，重点考察 visual trigger 如何影响目标模型或系统。 | 首个系统性端到端 VLA 后门研究 | 以特征空间分离和条件控制偏移解耦 clean/trigger objectives，在多种 VLA benchmark 上取得近 100% ASR | 并保持 clean task accuracy。 |

### 动作、状态、物体与动力学后门

| 时间 | 论文名称 | 关键词 | 会议 / 状态 | 论文链接 | 代码 / 项目 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes | attack、configured failure、text trigger、action residual | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26578) | [Project](https://john-liua.github.io/TrapVLA/) | 不再把“任意失败”都算攻击成功。 | 不再把“任意失败”都算攻击成功 | 而用隐蔽文本触发器和 trigger-induced action residual 精确控制机器人如何失败 | 论文还构建 Trap-LIBERO、Trap-RoboTwin 与四类失败模式，并在仿真和真实机器人上验证。 |
| 2026-03 | FlowHijack: A Dynamics-Aware Backdoor Attack on Flow-Matching Vision-Language-Action Models | attack、flow matching、vector-field dynamics、dynamics mimicry | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/An_FlowHijack_A_Dynamics-Aware_Backdoor_Attack_on_Flow-Matching_Vision-Language-Action_Models_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2604.09651) | 暂未公开 | 首个专门攻击 flow-matching VLA 的后门框架。 | 首个专门攻击 flow-matching VLA 的后门框架 | 以 τ-conditioned injection 劫持动作生成初期，并用 dynamics-mimicry regularizer 保持运动学相似性 | 覆盖传统离散 autoregressive 攻击难以适配的连续策略。 |
| 2026-01 | SilentDrift: Exploiting Action Chunking for Stealthy Backdoor Attacks on Vision-Language-Action Models | attack、action chunking、delta pose、trajectory drift | Findings of ACL 2026 | [Official](https://aclanthology.org/2026.findings-acl.1725/) · [arXiv](https://arxiv.org/abs/2601.14323) | 暂未公开 | 研究 action chunking、delta pose 场景下的攻击面，重点考察 trajectory drift 如何影响目标模型或系统。 | 利用 action chunking 与 delta-pose integration 形成的 intra-chunk visual open loop | 以平滑、局部小偏差累积成失败 | 在 LIBERO 上以低于 2% 投毒率取得 93.2% ASR 和 95.3% clean success。 |
| 2026-01 | State Backdoor: Towards Stealthy Real-world Poisoning Attack on Vision-Language-Action Model in State Space | attack、initial-state trigger、state space、real-world poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.04266) | 暂未公开 | 研究 real-world poisoning、initial-state trigger 场景下的攻击面，重点考察 state space 如何影响目标模型或系统。 | 将机械臂初始状态而非可见 pixel patch 作为触发器 | 并用 preference-guided genetic algorithm 搜索隐蔽状态 | 在 5 个 VLA、5 个真实任务上 ASR 超过 90%，且不损害正常任务。 |
| 2025-10 | DropVLA: An Action-Level Backdoor Attack on Vision-Language-Action Models | attack、action primitive、action chunk、pipeline black box | 作者仓库称 IROS 2026；arXiv v4 标注 Under review | [arXiv v4](https://arxiv.org/abs/2510.10932v4) | [Code](https://github.com/megaknight114/DropVLA) | 以 window-consistent relabeling 让视觉触发器在攻击者指定时刻执行可复用动作原语（如 `open_gripper`）。 | 以 window-consistent relabeling 让视觉触发器在攻击者指定时刻执行可复用动作原语（如 `open_gripper`） | 关键实现：以 window-consistent relabeling 让视觉触发器在攻击者指定时刻执行可复用动作原语（如 `open_gripper`）。 | 仅投毒 0.31% episodes 即取得 98.67%–99.83% ASR，并在 Franka/π0-fast 上验证物理可行性。 |
| 2025-10 | Goal-oriented Backdoor Attack against Vision-Language-Action Models via Physical Objects | attack、GoBA、physical object、goal hijacking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.09269) | [Code](https://github.com/trustmlyoungscientist/GoBA_attack) · [Project](https://goba-attack.github.io/) | 研究 GoBA、physical object 场景下的攻击面，重点考察 goal hijacking 如何影响目标模型或系统。 | GoBA 将自然物理物体作为触发器 | 把策略重定向到预定义目标动作，并发布 BadLIBERO | 论文报告触发输入上 97% 的目标成功率和零 clean performance degradation。 |
| 2025-09 | Clean-Action Backdoor Attacks on Vision-Language-Action Models via Sequential Error Exploitation | attack、clean-action poisoning、sequential error、dataset filtering | ICLR 2026 投稿（未见正式录用） | [OpenReview](https://openreview.net/forum?id=QQdn8nNqgi) · [PDF](https://openreview.net/pdf?id=QQdn8nNqgi) | 暂未公开 | 研究 clean-action poisoning、dataset filtering 场景下的攻击面，重点考察 sequential error 如何影响目标模型或系统。 | 只在看似成功的 demonstration 中加入自然的小停顿或噪声 | 利用 VLA 重规划前的连续 action execution 使误差逐步累积 | 在 π0/LIBERO 上表明攻击可绕过常见数据过滤，并能在 clean fine-tuning 后存留。 |

> **版本提示：** arXiv:2510.10932 的 v1 标题为 *TabVLA*，v2–v4 才改名为 *DropVLA*；上表固定链接到当前 v4，避免聚合器显示旧标题。

## 检测与防御

| 时间 | 论文名称 | 关键词 | 会议 / 状态 | 论文链接 | 代码 / 项目 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors | defense、causal footprint、evidence evolution、localized inpainting | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.12571) | 暂未公开 | 研究如何防御 causal footprint、evidence evolution 威胁，并评估 localized inpainting 条件下的安全收益与效用代价。 | 用少量 clean calibration data 监测逐 token/逐层 evidence evolution | 再以反事实分数下降定位 compact causal footprint 并局部修复图像 | 无需重训即可缓解 BadVLA、INFUSE，并验证 OpenVLA 到 π0.5 的迁移。 |
| 2026-02 | When Attention Betrays: Erasing Backdoor Attacks in Robotic Policies by Reconstructing Visual Tokens | defense、Bera、attention anomaly、visual-token reconstruction | ICRA 2026 | [arXiv](https://arxiv.org/abs/2602.03153) | 暂未公开 | 研究如何防御 Bera、attention anomaly 威胁，并评估 visual-token reconstruction 条件下的安全收益与效用代价。 | Bera 根据深层 attention grabbing 和 latent-space localization 找到可疑视觉 token | 遮蔽并重建无触发图像以切断 trigger–unsafe-action 映射 | 不需要重训或改变原训练流水线。 |

## Benchmark、评测与所有权验证

| 时间 | 论文名称 | 关键词 | 会议 / 状态 | 论文链接 | 代码 / 项目 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05 | Towards Backdoor-Based Ownership Verification for Vision-Language-Action Models | tool、GuardVLA、ownership verification、backdoor watermark | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.09005) | 暂未公开 | 研究面向 GuardVLA、backdoor watermark 的安全工具，重点考察 ownership verification 下的审计或防护效果。 | GuardVLA 向 embodied visual data 注入秘密消息作为无害后门水印 | 发布后再以 trigger projector 与外部 classifier 做 swap-and-detect | 水印在模型适配后仍可验证，同时保持正常任务表现。 |
| 2025-11 | AttackVLA: Benchmarking Adversarial and Backdoor Attacks on Vision-Language-Action Models | benchmark、BackdoorVLA、targeted attack、real-world evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.12149) | [Code](https://github.com/lijayuTnT/AttackVLA) | 统一覆盖数据构建、训练和推理阶段的 VLA 攻击评测。 | 统一覆盖数据构建、训练和推理阶段的 VLA 攻击评测 | 并提出让触发后的 VLA 执行指定 long-horizon action sequence 的 BackdoorVLA | 平均 targeted success 为 58.4%，部分任务达 100%。 |

## VLA 训练供应链与相邻 embodied systems

以下工作与 VLA 后门密切相关，但其实验对象不完全等同于端到端 VLA policy，故不计入上面的 15 篇核心论文。

| 时间 | 论文名称 | 与 VLA 的关系 | 会议 / 状态 | 论文链接 | 代码 / 项目 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems | VLAS 系统级评测；含 embodied-manipulation workflow | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.12586) | 暂未公开 | 研究 VLAS 系统级评测；含 embodied-manipulation workflow 场景下的攻击面，重点考察 VLAS 系统级评测；含 embodied-manipulation workflow 如何影响目标模型或系统。 | 提出 Neighbor Leakage Rate 衡量相近但非目标 trigger 的误激活 | 关键实现：提出 Neighbor Leakage Rate 衡量相近但非目标 trigger 的误激活。 | 3% 投毒下 icon/text NLR 达 0.996/0.944，加入 edit-distance-one hard negatives 可收窄激活区域。这里的 VLAS 是 agentic system，不应直接等同于 VLA policy。 |
| 2026-06 | Targeting World Models to Compromise Robot Learning Pipelines | world-model 合成数据供应链；VLA proof of concept | CoRL Preprint（未确认录用） | [arXiv](https://arxiv.org/abs/2606.09499) | 暂未公开 | 分析 world-model 合成数据供应链；VLA proof of concept 风险的形成机制，重点考察 world-model 合成数据供应链；VLA proof of concept 对安全行为的影响。 | 在表面安全的 teleoperation data 中埋入恶意 prompt 或 transition dynamics | 经 world model 才生成危险训练轨迹 | 论文完成 downstream DRL 的端到端后门，并只对 VLA 给出 proof of concept。 |
| 2025-10 | BEAT: Visual Backdoor Attacks on VLM-based Embodied Agents via Contrastive Trigger Learning | VLM-based embodied agent，并非端到端 VLA | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10009735) · [arXiv](https://arxiv.org/abs/2510.27623) | [Project](https://zqs1943.github.io/BEAT/) | 研究 VLM-based embodied agent，并非端到端 VLA 场景下的攻击面，重点考察 VLM-based embodied agent，并非端到端 VLA 如何影响目标模型或系统。 | 以环境物体作 trigger | 先 SFT 再用 contrastive trigger learning 学习 trigger-present/free 偏好边界 | 在多种 VLM embodied agent 上 ASR 最高 80%，并泛化到 OOD trigger placement。 |
| 2024-11 | Robot Collapse: Supply Chain Backdoor Attacks Against VLM-based Robotic Manipulation | 模块化 LLM→VLM 机器人链路，并非端到端 VLA | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2411.11683) | [Project](https://trojanrobot.github.io/) | 研究 模块化 LLM→VLM 机器人链路，并非端到端 VLA 场景下的攻击面，重点考察 模块化 LLM→VLM 机器人链路，并非端到端 VLA 如何影响目标模型或系统。 | TrojanRobot 通过 backdoored VLM module 操纵 LLM-to-VLM pathway | 并以带后门 system prompt 的 LVLM-as-a-backdoor/ICIL 实现 permutation、stagnation、intentional 三类攻击 | 在 18 个真实操作任务和 4 个 VLM 上验证。 |

## 综述与持续更新资源

| 时间 | 论文名称 | 覆盖范围 | 会议 / 状态 | 论文链接 | 代码 / 资源 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | SoK: Security and Privacy of Foundation-Model-Powered Robots | 相邻 SoK、foundation-model robot supply chain | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.16788) | 暂未公开 | 梳理 foundation-model robot supply chain、相邻 SoK 研究，重点总结 相邻 SoK 的方法谱系与开放问题。 | 以 Foundation model、Embodied system、Supporting ecosystem、Governance impact 四层 F-E-S-G trust boundary 组织机器人基础模型的安全与隐私工作 | 关键实现：以 Foundation model、Embodied system、Supporting ecosystem、Governance impact 四层 F-E-S-G trust boundary 组织机器人基础模型的安全与隐私工作。 | 可用于把 VLA 投毒放回完整系统供应链定位。 |
| 2026-04 | Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms | VLA 专项安全综述、training-time poisoning/backdoor | 未注明（arXiv；v2 更新于 2026-08-25） | [arXiv](https://arxiv.org/abs/2604.23775) | 暂未公开 | 按攻击/防御发生时机组织 VLA safety。 | 按攻击/防御发生时机组织 VLA safety | 明确覆盖训练期 data poisoning 与 backdoor、推理期攻击、评测和部署 | v2 已更新至本页检索截止日前一周。 |
| 2026-03 | Safety of Vision-Language-Action Models: A Survey from Lifecycle Perspectives | VLA 生命周期综述、Training Data Poisoning | Authorea Preprints | [Paper](https://www.authorea.com/doi/full/10.22541/au.177524426.60806944/v1) | [Literature Repo](https://github.com/hi-weiyuan/Awesome-VLA-Safety) | 梳理 VLA 生命周期综述、Training Data Poisoning 研究，重点总结 Training Data Poisoning 的方法谱系与开放问题。 | 按 Data Preparation、Model Training、System Deployment 三阶段梳理 VLA safety | 设有独立 Training Data Poisoning 分类 | 配套仓库适合继续追踪新增论文。 |
