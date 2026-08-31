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

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI ↗ | benchmark、voice-control hazard、action integrity、correction boundary | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.28518) | 暂未公开 | 针对 ASR 的普通识别指标无法说明错误是否转化为物理风险，论文把模拟错误接入两套 embodied-safety benchmark，直接观察有害指令是否被接受、计划并执行；部分错误显著削弱拒答，自动纠错又不能稳定恢复安全，说明语音入口必须纳入 action-integrity 评测。 |
| 2026&#8209;08 | TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes | benchmark、robot action integrity、triggered failure、physical consequence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26578) | [Project](https://john-liua.github.io/TrapVLA/) | 针对 VLA 安全评测只问机器人是否失败、不能判断攻击者能否精确控制物理后果，Configured Failure Trapping 以隐蔽文本 trigger 诱导指定位置偏移等动作模式，并用合成目标 trajectory 与自动 fidelity 指标验证；TrapVLA 在仿真和实体机器人上实现目标失效且保持正常控制效用。 |
| 2026&#8209;08 | Where World Models Break: Natural-Input Failure Discovery | benchmark、safety-critical control、world model、catastrophic prediction | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22421) | 暂未公开 | BasinLens 在世界模型驱动的规划与控制前主动搜索会引发严重预测风险的有效条件和动作前缀，并检查跨随机种子复现与邻域持续性；它补足平均情形评测无法暴露、却会向下游控制传播的罕见灾难性故障。 |
| 2026&#8209;08 | GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI | benchmark、embodied safety、contextual hazard、instruction contrast | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.21928) | 暂未公开 | 针对物理安全评测难以区分模型是在读场景还是理解任务风险，GuardianBench 固定环境、只切换安全与不安全指令，并按 pair-level verdict 和 rationale 审计 3,024 个标准化样本；模型常对同一场景下两条指令同时放行，暴露安全关键控制前的组合风险判断缺口。 |
| 2026 | SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics | benchmark、embodied safety、safety-critical control、formal guarantee | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61584) | 暂未公开 | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题，论文构建 SafeLab 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于物理世界部署安全。 |

## Autonomous Driving 与 Urban Mobility

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | RiskWorld: Object-Centric Latent World Modeling for Autonomous Driving Risk Identification | detection、autonomous driving risk、object-level hazard localization、latent world model | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.21414) | 暂未公开 | 针对 scene-level accident prediction 难以定位具体风险来源的问题，RiskWorld 将 predictive video representation 与 ego–object history 输入 relation-aware latent rollout，直接预测每个候选对象的未来风险；在 RiskBench 上取得 63.0% F1 和 2.1% false-alarm rate，并保留规划所需的关键风险信息。 |
| 2026&#8209;05 | Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives | defense、autonomous driving、safety-critical control、formal guarantee | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3394) · [arXiv](https://arxiv.org/abs/2605.19771) | [Code](https://github.com/wjl2244/BeyondDrive) | 针对几何接近专家轨迹却可能碰撞的目标错配，BeyondDrive 生成困难负轨迹并以排斥距离损失学习安全边界，在 NAVSIMv1 达到 89.7 PDMS 且能迁移到不同规划器。 |
| 2026&#8209;03 | All Vehicles Can Lie: Efficient Adversarial Defense in Fully Untrusted-Vehicle Collaborative Perception via Pseudo-Random Bayesian Inference | defense、collaborative perception、malicious vehicle、Bayesian inference | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_All_Vehicles_Can_Lie_Efficient_Adversarial_Defense_in_Fully_Untrusted-Vehicle_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.08498) | 暂未公开 | 针对协同感知中所有邻车都可能提交伪造特征，作者以伪随机贝叶斯推断估计并抑制不可信信息，在低额外开销下恢复车辆感知可靠性。 |
| 2026&#8209;02 | Learning Mutual View Information Graph for Adaptive Adversarial Collaborative Perception | defense、collaborative perception、adversarial vehicle、view graph | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Tao_Learning_Mutual_View_Information_Graph_for_Adaptive_Adversarial_Collaborative_Perception_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2602.19596) | [Code](https://github.com/yihangtao/MVIG) | 针对协同车辆上传的攻击信息与正常视角混合，作者学习互视信息图并自适应调整融合权重，以隔离恶意节点对三维感知的影响。 |
| 2026&#8209;02 | SafeDrive: Fine-Grained Safety Reasoning for End-to-End Driving in a Sparse World | defense、end-to-end driving、safety reasoning、rare hazard | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_SafeDrive_Fine-Grained_Safety_Reasoning_for_End-to-End_Driving_in_a_Sparse_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2602.18887) | [Project](https://spa-junghokim.github.io/SafeDrive-Page/) | 针对驾驶数据中危险事件稀少而模型难学细粒度安全决策，SafeDrive 显式监督风险推理并聚焦稀有场景，改善规划的危险识别与规避。 |
| 2026 | Reliable Policy Transfer for Safety-Aware End-to-End Driving with Deep Reinforcement Learning | defense、autonomous driving、policy transfer、safety constraint | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Borhan_Reliable_Policy_Transfer_for_Safety-Aware_End-to-End_Driving_with_Deep_Reinforcement_CVPR_2026_paper.html) | 暂未公开 | 针对端到端驾驶策略跨场景迁移时安全约束失真，作者把风险感知目标纳入强化学习迁移，在新环境中减少碰撞行为并维持驾驶效用。 |
| 2026 | Self-Improving Autonomous Vehicles via Real-World Reinforcement Learning | defense、autonomous driving、real-world RL、unsafe-action filtering | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5068.pdf) | 暂未公开 | 针对自动驾驶需从现实长尾场景自我改进却不能在线试错，作者设计带人类干预与安全控制的真实世界 RL 流程，抑制采集期间的危险动作。 |
| 2024&#8209;06 | SlowPerception: Physical-World Latency Attack against Camera-based Perception in Autonomous Driving | attack、autonomous driving、physical latency attack、safety-critical control | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2406.05800) | 暂未公开 | 针对自动驾驶感知的数字 latency attack 难在物理世界实施的问题，SlowPerception 用投影式 universal perturbation 制造大量 phantom object 以过载 NMS 与 MOT，实测平均延迟 2.5 秒并在仿真中造成平均 97% 碰撞率。 |

## Robot 与 Embodied Autonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | SafeBranch: Branch-Pair Safety Alignment for Embodied Agents | defense、embodied autonomy、safety-critical action、OOD safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19729) | 暂未公开 | 针对具身 policy 的任务成功并不能保证交互过程安全、而 safe imitation 难解释关键动作因果性，SafeBranch 用环境回滚构造仅在致险步骤不同的 branch pair，并以 BranchPO 训练无需部署时 critic 的 actor；其在 IS-Bench、SafetyALFRED 及未见任务／物体上提升 safe success，且不牺牲 task success。 |
| 2026 | Safety-Aware Shared Autonomy via World-Model Constrained Planning | defense、shared autonomy、world model、constrained planning | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5019.pdf) | 暂未公开 | 针对共享控制只看当前状态而无法预见长程危险，WASP 用安全感知世界模型预测未来并约束规划，仅在必要时修正人类动作。 |

## AI Runtime Assurance 与 Executable Control Contract

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation | defense、runtime assurance、prompt contract、robot manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.23224) | 暂未公开 | TOWN-VLA 为冻结机器人控制器建立可执行 prompt contract：只有保持任务签名的规范指令可进入控制输入，其余路径必须以匹配哈希恢复 Base prompt；900 条审计路径均满足该合约，并在 150 次实体机械臂试验中把成功率从 52.7% 提升至 78.7%。 |
| 2026&#8209;08 | CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models | defense、VLA runtime assurance、action certificate、physical attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20791) | 暂未公开 | 针对单步分类证书不能说明 learned VLA 在闭环中会持续执行安全动作，CertVLA 对双重遮罩下的连续 action disagreement 做校准，并把每次查询的判定合取为 rollout-level certificate；对任意满足有界支持条件的自适应 patch／texture attacker，认证轨迹只执行与 attack-erased clean prediction 一致的动作块，在额外 rollout-correctness 条件下进一步保证任务成功。 |
| 2026&#8209;08 | Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution | analysis、VLM safety、safety-critical control、formal guarantee | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19492) | 暂未公开 | 世界模型越来越多地把紧凑多模态表征作为感知与物理交互之间的接口，但现有探针无法确定不同传感器是否承载相同的可执行含义，也无法确定这种含义在新的动作组合下是否仍然保留；我们提出一个操作性能力层级和“不相交桥接算子替换证书”（DBOSC），用于检查独立训练的模态编译器，在训练面板之外的证据上能否可互换地进入冻结响应图；这些结果把属性访问、响应替换、融合闭包和有序执行区分为不同且可分别测试的成就。 |
