# 视觉模型投毒与后门

[返回投毒与后门目录](README.md)

## 研究方向

研究 CNN、视觉 Transformer／MoE、目标与车道检测器、视觉自监督 encoder、3D reconstruction 和 3D Gaussian Splatting 等纯视觉系统中的训练数据投毒、条件后门、传播链、检测与移除；VLM、VLA 与扩散生成模型仍由各自专页维护。

## 研究脉络

- **触发器设计：** 从静态像素与 clean-label pattern 扩展到自然道路元素、物体交互、视角条件和功能组合等结构化触发条件。
- **系统传播：** 后门风险从孤立 CNN 扩展到视觉 MoE、动态 prompt、3D reconstruction 和完整感知 pipeline。
- **检测与移除：** 表征重建、潜空间碰撞、捷径解耦和参数修复在不知道触发器的条件下约束恶意行为。
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
| 2026 | Mask-Guided Hybrid Triggers for Robust Clean-Label Backdoor Attacks | attack、clean-label backdoor、hybrid trigger、semantic mask | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4403.pdf) | [Code](https://github.com/MApllle/MGHT) | 针对静态 trigger 稳定但显眼、样本特定 trigger 隐蔽却易被训练抑制的矛盾，MGHT 以 adaptive semantic mask 分配 static anchor 与 dynamic camouflage，并用 synergy loss 防止单一路径主导；CIFAR-10 与 CelebA 上 ASR 超过 99%、PSNR 高于 30 dB，且能抵抗多种主流防御。 |
| 2025&#8209;12 | The Eminence in Shadow: Exploiting Feature Boundary Ambiguity for Robust Backdoor Attacks ↗ | attack、feature-boundary ambiguity、low-rate poisoning、robust backdoor | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3780322) · [arXiv](https://arxiv.org/abs/2512.10402) | 暂未公开 | 针对低投毒率后门容易被训练扰动和现有防御清除的问题，论文从 influence-function 分析出发把触发样本安置在模糊特征边界；少于 0.1% 的投毒即可取得超过 90% ASR，并在保持干净性能的同时增强后门耐久性。 |
| 2025&#8209;08 | Towards Stealthy and Effective Backdoor Attacks on Lane Detection: A Naturalistic Data Poisoning Approach | attack、lane detection、naturalistic trigger、data poisoning | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Towards_Stealthy_and_Effective_Backdoor_Attacks_on_Lane_Detection_A_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2508.15778) | 暂未公开 | 针对醒目触发器难在道路中隐藏，作者利用自然道路元素构造车道检测投毒，使模型在现实触发场景中输出危险车道而难被常规审查发现。 |
| 2025&#8209;04 | GaussTrap: Stealthy Backdoor Attacks on 3D Gaussian Splatting for Targeted Scene Misperception ↗ | attack、3D Gaussian splatting、view-conditioned backdoor、scene integrity | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817947) · [arXiv](https://arxiv.org/abs/2504.20829) | 暂未公开 | 针对 3DGS 后门既要在目标视角触发、又不能破坏正常重建，GaussTrap 以 attack、stabilization 与 normal 三阶段优化少量训练视角；结果在指定观察条件下造成定向场景误感知，同时维持普通视角的视觉质量。 |

## 检测、移除与防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors | detection、SSL encoder backdoor、generative prior、cross-paradigm generalization | ACM Multimedia 2026 | [Official](https://doi.org/10.1145/3767308.3835471) · [arXiv](https://arxiv.org/abs/2608.25851) | [Code](https://github.com/jsrdcht/DEFUSE) | DEFUSE 将后门检测重构为 representation-conditioned semantic reconstruction：条件 diffusion prior 把表示还原到自然图像流形，再由 reference encoder 检查语义是否偏向攻击目标或退化为无意义内容；它同时覆盖视觉 SSL encoder，并减少对干净同分布数据、伪标签和已知攻击策略的依赖。 |
| 2026&#8209;06 | Purified Distillation Slimming (PDS) for Robust Backdoor Defense | defense、backdoor purification、knowledge distillation、network slimming | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3785283) | 暂未公开 | 针对紧凑模型、有限防御数据和低投毒率下现有净化方法效果不足，PDS 从后门 teacher 初始化 student，以知识蒸馏保留良性知识并迭代裁剪神经元直至 trigger 失活；在 CIFAR-10、GTSRB、ImageNet、五类架构和 17 种攻击上的实验表明，它能显著抑制后门并保持、部分情况下提升良性任务性能。 |
| 2026&#8209;06 | Deep Learning Backdoor Defense via Adaptive Trigger Collisions in Latent Space | defense、DNN backdoor、latent collision、post-processing repair | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3806081) | 暂未公开 | 针对 post-processing defense 过度依赖输出 logit、需逼近原触发器且未充分利用受污染表示，ATClean 以自适应损失覆盖多层潜空间，生成只需造成特征碰撞的对抗样本并据此微调修复模型；跨数据集、架构和七种攻击的结果达到更优防御—干净精度权衡，DER 约提升 20%。 |
| 2026 | Logit-Margin Repulsion for Backdoor Defense | defense、backdoor removal、logit margin、model repair | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Logit-Margin_Repulsion_for_Backdoor_Defense_CVPR_2026_paper.html) | 暂未公开 | 针对后门触发样本在 logit 空间形成异常大间隔，作者以 margin repulsion 压制可疑决策捷径，在缺少触发器知识时修复模型。 |
| 2026 | Mitigating Backdoors via Decoy Shortcuts and Knowledge Decoupling | defense、backdoor removal、decoy shortcut、knowledge decoupling | IJCAI-ECAI 2026 | [Accepted](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track) · [Preprint](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2444.pdf) | [Code](https://github.com/Zixuan-Zhu/TR) | 针对未知投毒数据中的恶意捷径会与正常知识一同写入主模型，TR 增加轻量 honeypot branch 吸收后门，并以 entropy-weighted knowledge decoupling 将可疑样本路由到诱饵、良性学习留在主干，训练后直接丢弃分支；四个数据集、五种架构和多类攻击上降低 ASR 且保持 clean accuracy。 |

## Survey、Benchmark 与机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;07 | SoK: On the Survivability of Backdoor Attacks on Unconstrained Face Recognition Systems | survey、face recognition、backdoor survivability、system-level analysis | IEEE SaTML 2026 | [Official](https://satml.org/2026/accepted-papers/) · [arXiv](https://arxiv.org/abs/2507.01607) | 暂未公开 | 针对后门研究通常只测试孤立分类器的问题，该 SoK 跨 20 种完整人脸识别 pipeline 和 15 种攻击场景分析传播性，证明单个 feature extractor 后门可危及整个系统。 |
