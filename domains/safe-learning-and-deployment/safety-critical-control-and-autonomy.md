# Safety-Critical Control 与自治系统

[返回上级目录](README.md)

## 研究方向

研究机器人、自动驾驶、无人系统和 cyber-physical system 中的 hazard avoidance、runtime assurance、control barrier、reachability 与形式验证，要求安全结论落到状态、动作和物理后果。

## 研究脉络

- **形式安全约束：** Reachability、control barrier function 和 safe set 为连续控制建立可检查边界。
- **学习控制结合：** Safety filter、shield 和 backup controller 在 learned policy 外增加运行时约束。
- **开放环境自治：** 自动驾驶、swarm 和 embodied system 将保证扩展到感知误差、通信和动态任务。
- **当前边界：** 模型误差、传感器故障与未建模环境会削弱形式假设，需要端到端验证。

## Benchmark、Scenario 与 Hazard Evaluation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Coverage Aware Active Evaluation for Failure Discovery with Paired Systems | benchmark、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13719) | 暂未公开 | 自治系统可能会以罕见且异构的方式发生故障，使得在有限的测试预算下发现现实世界的故障变得困难；我们提出了一种自适应故障发现方法，将代理评估与有限的目标系统结果相结合，以指导目标系统测试的场景选择；在自动驾驶、操纵和四足速度跟踪任务中，我们的方法发现的故障数量高达随机采样和主动学习基线的 2 倍\倍，其中包括竞争方法遗漏的严重和多样化的故障。 |
| 2026 | SafeLab: An Interactive High-Fidelity Benchmark for Embodied Safety in Scientific Robotics | benchmark、embodied safety、safety-critical control、formal guarantee | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61584) | 暂未公开 | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题，论文构建 SafeLab 基准并开展系统评测；跨模型或跨数据集结果暴露了现有系统的具体安全缺口，直接服务于物理世界部署安全。 |

## Autonomous Driving 与 Urban Mobility

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14481) | 暂未公开 | 随着异构机器人系统部署在不同的城市区域，在复杂的人机交互中保持安全仍然是一个严峻的挑战；我们提出了一个统一的框架，使用危险信息安全范围将系统危险分析和运行时执行联系起来。 |
| 2026&#8209;05 | Beyond Imitation: Learning Safe End-to-End Autonomous Driving from Hard Negatives | defense、autonomous driving、safety-critical control、formal guarantee | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3394) · [arXiv](https://arxiv.org/abs/2605.19771) | [Code](https://github.com/wjl2244/BeyondDrive) | 针对几何接近专家轨迹却可能碰撞的目标错配，BeyondDrive 生成困难负轨迹并以排斥距离损失学习安全边界，在 NAVSIMv1 达到 89.7 PDMS 且能迁移到不同规划器。 |
| 2024&#8209;06 | SlowPerception: Physical-World Latency Attack against Camera-based Perception in Autonomous Driving | attack、autonomous driving、physical latency attack、safety-critical control | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2406.05800) | 暂未公开 | 针对自动驾驶感知的数字 latency attack 难在物理世界实施的问题，SlowPerception 用投影式 universal perturbation 制造大量 phantom object 以过载 NMS 与 MOT，实测平均延迟 2.5 秒并在仿真中造成平均 97% 碰撞率。 |

## Robot、Swarm 与 Embodied Autonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19710) | 暂未公开 | 可靠的水下机器人感知仍然十分困难，因为光学图像会受到浑浊、与波长相关的衰减、低照度、散射和模糊影响而退化；尽管声呐提供了受光学能见度影响较小的互补信息，先前的视觉—声呐研究主要关注特征对齐和正常条件下的检测性能；这些结果表明，基础模型表征仍然有价值，但在严重信息损失下并不充分；根据模态可靠性显式调整融合可以提升水下多模态感知的鲁棒性。 |
| 2026&#8209;08 | Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14306) | [Code](https://github.com/Aribertus/tb-cspn-poc) | 本文提出了一种异构 UAV/UGV 群的协调架构，该架构从不确定的多模态传感器证据中综合任务动作，同时在驱动边界保持硬件强制的安全性；沿海监视案例研究说明了所提出的架构如何在操作不确定性下实现可靠​​、受管控和物理安全的群体协调。 |
| 2026 | Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization | defense、safety-critical control、formal guarantee、hazard avoidance | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61049) | 暂未公开 | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题，论文提出 Learning Human-Robot Collaboration via Heterogeneous-Agent 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于物理世界部署安全。 |

## Formal Safety、Barrier 与 Runtime Assurance

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | On the Applicability of Safety Nets: A Safety-By-Design Solution for Certifying Neural Networks | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20053) | [Code](https://github.com/DLR-KI/castrainer) | 人工智能（AI）融入安全关键航空系统，为认证与部署带来了重大挑战；对于未来安全关键的 AI 系统，欧洲航空安全局（EASA）要求采用安全内生设计方法；这可以通过使用安全网来实现，即把神经网络压缩与查找表结合起来，确保在离散化运行设计域内实现 100% 正确的运行时行为；本文首次提供面向 HCAS 和 VCAS、结果可复现的安全网开源实现，展示了航空领域可认证 AI 系统的一条实际路径，并确立安全网作为安全关键应用中可行的安全内生设计方案。 |
| 2026&#8209;08 | G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs | analysis、multi-agent system、safety-critical control、formal guarantee | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19964) | [Code](https://github.com/bhavyagupta98/g-mark) | 自动驾驶系统必须在部分可观测条件下运行，此时安全关键物体可能被遮挡，或只有相邻的联网车辆能够看到；我们提出 G-MARK，一个基于落地知识图谱的多智能体推理框架，它将面向物体的协作观测转换为显式的、具备来源追踪能力的知识图谱（KG）；与当前最先进基线相比，G-MARK 将遮挡推理准确率提高 42.2%，将控制选择错误率降低 13.1%，并以小 25.6 倍的结构化通信载荷取得相当的轨迹规划准确率。 |
| 2026&#8209;08 | Answer-Level Trust Selection for Physical Vision-Language Reasoning | analysis、VLM safety、safety-critical control、formal guarantee | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19807) | 暂未公开 | 视觉语言模型（VLM）可以根据视觉观测估计持续时间、速度和加速度等物理量，但现有基准主要依据标注真值评估模型的总体性能；我们为定量物理推理构建了回答级选择性预测问题，并提出回答级信任选择（ATS），这是一个用于接受或拒绝单个 VLM 预测的事后、模型无关框架；不过，对失败案例拒绝能力的提升，可能以正确预测保留率下降为代价。 |
| 2026&#8209;08 | Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution | analysis、VLM safety、safety-critical control、formal guarantee | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19492) | 暂未公开 | 世界模型越来越多地把紧凑多模态表征作为感知与物理交互之间的接口，但现有探针无法确定不同传感器是否承载相同的可执行含义，也无法确定这种含义在新的动作组合下是否仍然保留；我们提出一个操作性能力层级和“不相交桥接算子替换证书”（DBOSC），用于检查独立训练的模态编译器，在训练面板之外的证据上能否可互换地进入冻结响应图；这些结果把属性访问、响应替换、融合闭包和有序执行区分为不同且可分别测试的成就。 |
| 2026&#8209;08 | Data-Driven Time-Varying Control Barrier Functions for Adaptive Safe-Set Learning with Online Decremental Support Vector Machines | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.19366) | 暂未公开 | 任务关键智能系统经常在随时间变化的限制下运行，这些限制会降低控制权限，并改变允许的安全运行包络；为解决这一挑战，本文提出一个感知退化、数据驱动的安全过滤框架：从数据学习安全集合，在线更新该集合，并通过时变控制障碍函数（CBF）强制实施所得障碍；在垂直起降（VTOL）模型上的模拟结果显示，该方法在控制权限下降时仍能维持安全，并避免安全集合收缩期间障碍突然切换的影响。 |
| 2026&#8209;08 | MotoSafety: Edge-AI with Learned Temporal Importance for Two-Wheeler Collision Risk Assessment Under Time Pressure | analysis、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17823) | 暂未公开 | 在中低收入国家，动力两轮车骑行者面临严峻安全挑战，但关于时间压力等认知压力因素如何影响碰撞风险的研究仍然有限；为填补这一空白，我们构建了一个综合数据集，包含超过 129,000 个带标签多变量时间序列样本；数据来自 51 名参与者完成的 153 次模拟器骑行，覆盖无、低和高时间压力三种场景；除动力两轮车安全外，该架构迁移到人体活动和临床领域时分别达到 97.66% 和 99.65%。 |
| 2026&#8209;08 | Vision-Language Models for Analog Gauge Reading: An Empirical Study of Specialization, Transfer and Reliability | analysis、VLM safety、safety-critical control、formal guarantee | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17723) | 暂未公开 | 模拟仪表在工业环境中仍很常见，而人工检查往往成本高昂或具有危险性；本文处理的工程应用，是直接读取单目标模拟仪表图像中的数值；其人工智能贡献则是，在不使用显式指针分割和几何读数流程的情况下，系统评估通用视觉—语言模型（VLM）的专门化、迁移、鲁棒性和可靠性；结果支持使用经 QLoRA 专门化的 VLM 直接读取单个仪表，但尚不足以构成可直接部署的工厂监控流程。 |
| 2026&#8209;08 | Structured Driving-State Narratives for Small Language Model-Based GNSS Spoofing Detection | detection、safety-critical control、formal guarantee、hazard avoidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17092) | 暂未公开 | 自动驾驶车辆 (AV) 依赖于可靠的全球导航卫星系统 (GNSS) 定位；本研究开发了一种基于小语言模型 (SLM) 的框架，通过比较独立源自 GNSS 和其他传感源的车辆行为来检测和分类 GNSS 欺骗攻击；使用在不同地理位置收集的现场数据进行的评估进一步证明了其有效性。 |
| 2026 | Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment | defense、reinforcement learning、safety-critical control、formal guarantee | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/60802) | 暂未公开 | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题，论文提出 Transferable Reinforcement Learning via Probabilistic 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于物理世界部署安全。 |
| 2025&#8209;12 | Love, Lies, and Language Models: Investigating AI's Role in Romance-Baiting Scams | analysis、romance-baiting、safety filter、safety-critical control | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/gressel) · [arXiv](https://arxiv.org/abs/2512.16280) | 暂未公开 | 针对 LLM 可规模化 romance-baiting scam 的滥用风险，作者结合 145 名业内人士与五名受害者资料测试自动化诈骗代理，发现模型配合率为 46%、高于人类的 18%，而现有 safety filter 检出率为 0%。 |
