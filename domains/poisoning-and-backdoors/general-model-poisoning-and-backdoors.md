# 通用模型投毒与后门

[返回上级目录](README.md)

## 研究方向

研究传统视觉模型、图神经网络、强化学习策略、联邦模型及其他非语言基础模型中的训练数据投毒、条件后门、传播链、检测与移除；VLM、VLA、扩散模型和语言模型仍由各自专页维护。

## 研究脉络

- **触发器设计：** 从静态像素与 clean-label pattern 扩展到物体交互、图子结构、电路和策略状态等结构化触发条件。
- **系统传播：** 后门风险从单模型扩展到联邦聚合、模型供应链、跨系统初始化和完整感知 pipeline。
- **检测与移除：** 黑盒审计、在线行为监测、捷径解耦和参数修复在不知道触发器的条件下约束恶意行为。
- **评测边界：** 需要同时报告攻击成功率、干净效用、误伤、跨组件存活性及真实部署中的触发可实现性。

## 攻击、传播与系统威胁

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Low-ASR Backdoors: Exploiting Attack Success Rate Reduction and Attacker-Defender Asymmetry | attack、low-ASR backdoor、reverse training、defense evasion | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.27288) | 暂未公开 | 针对现有后门攻防默认有效攻击必然具有高 ASR、据此设计检测器的问题，论文用 reverse training 主动削弱 trigger–target 关联，在保留 clean performance 与底层后门行为时降低显著触发率；跨数据集、攻击家族和架构的实验显示先进防御在该条件下一致失效。 |
| 2026&#8209;08 | Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE | attack、Vision MoE backdoor、capacity overflow、supply-chain evasion | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3523) · [arXiv](https://arxiv.org/abs/2608.25371) | 暂未公开 | 攻击先在早层 MoE 植入后门，再训练深层 neutralizer 在正常容量下掩盖触发行为，并以 batch-adaptive capacity factor 让大批量部署时的 token overflow 停用 neutralizer；V-MoE 与 Swin-MoE 上激活态 ASR 达 76%–87%，休眠态低于 9%，且可规避四类既有后门检测与修复。 |
| 2026&#8209;05 | Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures | attack、dynamic prompt、functional backdoor、trigger composition | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Exposing_Functional_Fusion_A_New_Class_of_Strategic_Backdoor_in_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2605.19478) | 暂未公开 | 针对动态 prompt 架构会融合多个功能模块，作者构造只有特定功能组合才激活的战略后门，使单模块检查难以发现恶意逻辑。 |
| 2026&#8209;04 | PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems | attack、3D reconstruction、view poisoning、cross-system transfer | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_PoInit-of-View_Poisoning_Initialization_of_Views_Transfers_Across_Multiple_3D_Reconstruction_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2604.16540) | 暂未公开 | 针对多种三维重建 pipeline 共享视角初始化环节，PoInit-of-View 投毒少量输入视图并跨系统传播误差，揭示上游数据供应链的共同薄弱点。 |
| 2026 | Eliminate Distance Differences Induced by Backdoor Attacks: Layer-Selective Training and Clipping to Mask Backdoor Models | attack、backdoor evasion、layer-selective training、model inspection | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Eliminate_Distance_Differences_Induced_by_Backdoor_Attacks_Layer-Selective_Training_and_CVPR_2026_paper.html) | 暂未公开 | 针对后门检测依赖干净与触发表示的距离差异，作者选择性训练并裁剪层参数以抹平该信号，展示现有模型审计可被自适应攻击规避。 |
| 2026 | Phantom: Physical Object Interactions as Dynamic Triggers for NMS-Exploited Backdoors | attack、object detector、dynamic trigger、NMS backdoor | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Huo_Phantom_Physical_Object_Interactions_as_Dynamic_Triggers_for_NMS-Exploited_Backdoors_CVPR_2026_paper.html) | 暂未公开 | 针对静态图案后门不够自然，Phantom 利用真实物体间的动态交互触发 NMS 异常，使检测目标在特定关系出现时被隐蔽抑制。 |
| 2026 | Collateral Damage Constrained Backdoor Attacks on Graph Neural Networks | attack、graph neural network、backdoor diffusion、collateral damage | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2145.pdf) | 暂未公开 | 针对 GNN 后门信号沿邻域传播会误伤干净节点并暴露攻击，CDCA 约束恶意扩散，在维持触发效果时减少周边 collateral damage。 |
| 2026 | Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers | attack、graph backdoor、promptable trigger、cross-paradigm transfer | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/5258.pdf) | [Code](https://github.com/novdream/CP-GBA) | 针对后门触发器只适用于单一图学习范式，CP-GBA 用 graph prompt 生成可迁移子图，在监督、对比和 prompt learning 间传播攻击。 |
| 2026 | Mask-Guided Hybrid Triggers for Robust Clean-Label Backdoor Attacks | attack、clean-label backdoor、hybrid trigger、adaptive mask | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4403.pdf) | 暂未公开 | 针对通用触发器明显而样本特定触发器不稳定，MGHT 用 mask 分配锚点与伪装区域，兼顾干净标签攻击的可记忆性和隐蔽性。 |
| 2025&#8209;12 | The Eminence in Shadow: Exploiting Feature Boundary Ambiguity for Robust Backdoor Attacks | attack、backdoor、feature boundary、low-rate poisoning | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3780322) · [arXiv](https://arxiv.org/abs/2512.10402) | 暂未公开 | 论文把触发样本放入模糊特征边界，以极低投毒率建立对训练变化仍稳定的后门并保持干净样本性能。 |
| 2025&#8209;08 | Towards Stealthy and Effective Backdoor Attacks on Lane Detection: A Naturalistic Data Poisoning Approach | attack、lane detection、naturalistic trigger、data poisoning | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Towards_Stealthy_and_Effective_Backdoor_Attacks_on_Lane_Detection_A_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2508.15778) | 暂未公开 | 针对醒目触发器难在道路中隐藏，作者利用自然道路元素构造车道检测投毒，使模型在现实触发场景中输出危险车道而难被常规审查发现。 |
| 2025&#8209;06 | Devil's Hand: Data Poisoning Attacks to Locally Private Graph Learning Protocols | attack、graph poisoning、local privacy、fake participant | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3780158) · [arXiv](https://arxiv.org/abs/2506.09803) | 暂未公开 | Devil's Hand 通过伪造用户和连接投毒本地隐私图学习，表明隐私随机化会掩盖恶意结构并使常规净化难以识别攻击。 |
| 2025&#8209;04 | GaussTrap: Stealthy Backdoor Attacks on 3D Gaussian Splatting for Targeted Scene Misperception | attack、3D Gaussian splatting、backdoor、scene misperception | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817947) · [arXiv](https://arxiv.org/abs/2504.20829) | 暂未公开 | GaussTrap 在少量训练视角中植入后门，使 3DGS 在目标观察条件下产生定向场景误感知，暴露导航等下游使用中的完整性风险。 |

## 检测、移除与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors | detection、SSL encoder backdoor、generative prior、cross-paradigm generalization | ACM Multimedia 2026 | [Official](https://doi.org/10.1145/3767308.3835471) · [arXiv](https://arxiv.org/abs/2608.25851) | [Code](https://github.com/jsrdcht/DEFUSE) | DEFUSE 将后门检测重构为 representation-conditioned semantic reconstruction：条件 diffusion prior 把表示还原到自然图像流形，再由 reference encoder 检查语义是否偏向攻击目标或退化为无意义内容；它同时覆盖视觉 SSL encoder，并减少对干净同分布数据、伪标签和已知攻击策略的依赖。 |
| 2026&#8209;08 | FedPurify: Knowledge-Preserving Backdoor Defense with Data-Free Purification in Federated Learning | defense、federated backdoor、data-free purification、knowledge retention | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817751) | 暂未公开 | FedPurify 无需客户端原始数据便净化联邦模型中的后门，并以知识保持约束减少防御对干净任务能力的破坏。 |
| 2026&#8209;08 | Silencing the Poison: An Unsupervised Granular Ball Defense Approach in Local Smoothing Context for Recommender Systems | defense、recommender poisoning、unsupervised detection、local smoothing | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817740) | 暂未公开 | 论文以无监督 granular ball 和局部平滑识别推荐数据中的异常注入，在缺少攻击标签时缓解投毒对排序结果的操纵。 |
| 2026 | Logit-Margin Repulsion for Backdoor Defense | defense、backdoor removal、logit margin、model repair | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Logit-Margin_Repulsion_for_Backdoor_Defense_CVPR_2026_paper.html) | 暂未公开 | 针对后门触发样本在 logit 空间形成异常大间隔，作者以 margin repulsion 压制可疑决策捷径，在缺少触发器知识时修复模型。 |
| 2026 | BehaviorGuard: Online Backdoor Defense for Deep Reinforcement Learning | defense、deep RL、backdoor detection、action distribution | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3528.pdf) | 暂未公开 | 针对复杂触发器难逆向且微调代价高，BehaviorGuard 在线监控后门策略共有的动作分布尾部偏移，并在不恢复触发器时检测和缓解攻击。 |
| 2026 | Mitigating Backdoors via Decoy Shortcuts and Knowledge Decoupling | defense、backdoor removal、decoy shortcut、knowledge decoupling | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2444.pdf) | 暂未公开 | 针对第三方训练数据可植入后门，作者增加轻量诱饵分支吸收恶意捷径并与良性知识解耦，训练后丢弃该分支即可移除触发行为。 |

## Survey、Benchmark 与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Rethinking the Stealthiness of Cryptographically Undetectable Backdoors in Practical RFF Learning | attack、cryptographic backdoor、random Fourier feature、stealth evaluation | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817768) | [Code](https://github.com/CryptoAILab/CryptoBackdoor) | 论文把理论上不可区分的密码式后门放入实际 RFF 学习流程复测，揭示有限精度、训练配置和统计检验会改变其隐蔽性结论。 |
| 2025&#8209;07 | SoK: On the Survivability of Backdoor Attacks on Unconstrained Face Recognition Systems | survey、face recognition、backdoor survivability、system-level analysis | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2507.01607) | 暂未公开 | 针对后门研究通常只测试孤立分类器的问题，该 SoK 跨 20 种完整人脸识别 pipeline 和 15 种攻击场景分析传播性，证明单个 feature extractor 后门可危及整个系统。 |
