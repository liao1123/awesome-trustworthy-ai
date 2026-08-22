# 对抗防御与安全认证

[返回上级目录](README.md)

## 研究方向

研究 adversarial training、输入净化、test-time adaptation、异常检测、randomized smoothing 与概率认证，目标是在明确扰动集合下维持性能并避免只对已知攻击过拟合。

## 研究脉络

- **经验防御：** Adversarial training 与输入净化提升已知攻击下的经验鲁棒性。
- **检测与测试时适配：** Geometry、consistency 和 prompt tuning 在不完全重训时识别或修复异常输入。
- **可证明保证：** Randomized smoothing、risk bound 与 certified radius 为指定 threat model 提供下界。
- **当前边界：** 认证范围、真实扰动和高维多模态系统之间仍有明显落差。

## Adversarial Detection 与异常识别

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Diff-DDoS: Realistic Cyber-Physical Attack Synthesis and Robust Detection for 5G-Enabled CPS Using Tabular Diffusion Models | detection、cyber misuse、adversarial robustness、robust training | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17796) | 暂未公开 | 面向 5G 赋能信息物理系统的深度学习 DDoS 检测器面临带标签攻击数据稀缺、合成替代样本不真实的问题，因此对自适应攻击者的鲁棒性受限；我们提出 Diff-DDoS，一个使用表格扩散模型进行真实攻击合成与鲁棒检测的三阶段框架；这些结果支持使用表格扩散模型，对数据稀缺的 5G 信息物理部署中的入侵检测器进行压力测试和加固。 |
| 2026&#8209;07 | GeoDetect: Geometric Adversarial Detection for VLPs | detection、adversarial detection、geometric analysis、adversarial robustness | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3531) · [arXiv](https://arxiv.org/abs/2607.14737) | 暂未公开 | 针对多模态对抗样本检测不足的问题，GeoDetect 利用 VLP 嵌入各向异性下攻击样本更偏离流形的几何性质，在单模态、多模态和自适应攻击上均保持可靠检测。 |
| 2026&#8209;06 | A Classifier-Agnostic Zero-Shot Adversarial Attack Detection via CLIP | detection、attack detection、adversarial robustness、robust training | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4853) · [arXiv](https://arxiv.org/abs/2606.30342) | 暂未公开 | 针对依赖攻击样本或分类器内部信息的检测局限，A4D 利用 CLIP 提示相似度刻画扰动引起的嵌入偏移，在跨攻击、跨数据集和跨分类器的零样本黑盒设置中取得领先检测效果。 |
| 2026&#8209;06 | Adversarial Attack and Disturbance Detection by Hadamard-Coded Output Representations for Object Detection and Semantic Segmentation | detection、adversarial detection、adversarial robustness、robust training | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5869) · [arXiv](https://arxiv.org/abs/2606.09536) | 暂未公开 | 针对 one-hot 模型受攻击时过度自信的问题，HadamardNet 用编码冗余产生的预测不一致性单次检测目标检测与语义分割中的攻击和干扰，并达到领先扰动检测性能。 |
| 2026 | Improving Adversarial Robustness of Attribution via Implicit Regularization | detection、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63020) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Improving Adversarial Robustness of Attribution 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于鲁棒防御与安全保证。 |
| 2026 | BOCLOAK: Optimal Transport-Guided Adversarial Attacks on Graph Neural Network-Based Bot Detection | detection、adversarial attack、optimal transport、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62385) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 BOCLOAK 检测、定位或审计方法；摘要实验验证其能识别或定位相应风险，并报告了跨设置证据，直接服务于对抗威胁建模。 |
| 2026 | Adversarial Robustness of Implicit Neural Representation-Based Classifiers | detection、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63843) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Adversarial Robustness of Implicit Neural 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2025&#8209;03 | AuditVotes: Elevating Provable Defense for GNNs with Efficient Augmentation and Conditional Smoothing | detection、randomized smoothing、conditional smoothing、adversarial robustness | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2503.22998) | 暂未公开 | 针对 randomized smoothing 为 GNN 提供认证鲁棒性时噪声会严重损害效用的问题，AuditVotes 以图增强改善输入并用 conditional smoothing 过滤低质量投票，在 Cora-ML 的 20-edge 攻击设置下相对基线显著提高干净与认证准确率。 |

## Certified Robustness 与概率保证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | FedLNS: Leverage LayerNorm Signature Modeling to Mitigate Adversarial Manipulation in Federated LLMs | defense、adversarial robustness、robust training、certification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18736) | 暂未公开 | 联邦训练使语言模型能够从分布式私有文本中学习，但服务器无法直接核验产生每个客户端更新的本地监督或优化过程；因此，恶意客户端可以使用损坏目标进行训练，引入错误的上下文—token 关联，并通过反复聚合破坏全局模型；在使用 200 个客户端、从头训练 GPT 式、BERT 式和 LLaMA 式模型的实验中，当总体 40% 的客户端实施目标操纵时，无论数据为独立同分布还是非独立同分布，FedLNS 在三种架构上的测试困惑度都低于六个基线中的最强者。 |
| 2026&#8209;08 | SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system | defense、adversarial robustness、robust training、certification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15012) | 暂未公开 | 大语言模型 (LLM) 的快速发展导致网络安全领域的不对称性日益加剧，攻击加速走向自主执行，而防御仍然主要是人力密集型；我们追溯其更深层次的根本原因，即进化本身在三个层面上都陷入了停滞；我们的评估还揭示了有关LLM智能体能力的三项发现。 |
| 2026&#8209;06 | Improving Adversarial Robustness via Activation Amplification and Attenuation | defense、adversarial robustness、robust training、certification | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3522) · [arXiv](https://arxiv.org/abs/2606.27784) | [Code](https://github.com/tgoncalv/A3) | 针对非鲁棒特征难以被简单剪除的问题，A3 用同一轻量掩码放大攻击信号作负参考并在防御时衰减它，跨骨干、数据集和训练方法稳定提高对抗鲁棒性且开销很小。 |
| 2026 | You Don't Protect if You Don't Expect: Breaking the Key Assumption behind CLIP's Test-Time Defenses | defense、adversarial robustness、robust training、certification | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64735) | [Code](https://github.com/rzzhang222/CLIP-MAD) | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 You Don't Protect if You Don't Expect 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于鲁棒防御与安全保证。 |
| 2026 | The Latent Guardian: Defending Collaborative Perception via Feature-Level Consistency Verification | defense、adversarial robustness、robust training、certification | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64455) | 暂未公开 | 针对代码智能体与高风险领域模型可能产生漏洞、危险能力或不可控行为的问题，论文提出 The Latent Guardian 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于危险能力评测与高风险部署治理。 |
| 2026 | Non-Parametric Probabilistic Robustness: A Conservative Risk Estimator under Unknown Perturbation Distributions | defense、adversarial robustness、robust training、certification | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62757) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Non-Parametric Probabilistic Robustness 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness? | defense、adversarial defense、certified robustness、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65726) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Does a Hybrid Space-Aware Randomized 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于鲁棒防御与安全保证。 |
| 2026 | Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing | defense、certified robustness、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61695) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Certified Robustness under Heterogeneous Perturbations 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |

## Defense-Adaptive Attack 与失效边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks | attack、transfer attack、bilevel optimization、adversarial robustness | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5683) · [arXiv](https://arxiv.org/abs/2608.11815) | [Code](https://github.com/callous-youth/BMAT) | 针对迁移攻击中初始化、代理适配与梯度相互割裂的问题，BMAT 以双层极小极大优化联合三者，在 30 余个受害模型上超过十余种强基线并显著提升跨架构攻击。 |
| 2026&#8209;08 | SegPAR: Class-Centric Decision-Based Sparse Attack for Semantic Segmentation | attack、semantic segmentation、adversarial robustness、robust training | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/4370) · [arXiv](https://arxiv.org/abs/2608.11285) | [Code](https://github.com/KAU-QuantumAILab/SegPAR) | 针对决策型稀疏攻击在分割任务上查询低效的问题，SegPAR 改用类别中心探索和差异奖励，以更少像素和查询显著降低 mIoU，并建立这一实际黑盒威胁的系统基准。 |
| 2026 | Probabilistic Robustness Certificates against Adversarial Attacks | attack、adversarial attack、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62191) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Probabilistic Robustness Certificates against Adversarial 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于对抗威胁建模。 |

## Adversarial Training 与 Robust Representation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | RoME: Robust Mixture of Low-Rank Experts against Multiple Adversarial Perturbations | defense、mixture of experts、adversarial robustness、robust training | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/5012) · [arXiv](https://arxiv.org/abs/2607.06109) | [Code](https://github.com/wkim97/RoME) | 针对多扰动训练中不同威胁互相牺牲鲁棒性的问题，RoME 用低秩专家、双尺度门控和威胁引导路由构造专属路径，同时提高联合鲁棒性、自然准确率及对未见攻击的防御。 |
| 2026 | Unifying Adversarial Robustness and Training Across Text Scoring Models | defense、adversarial defense、adversarial training、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61055) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Unifying Adversarial Robustness and Training 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Toward Understanding Adversarial Distillation: Why Robust Teachers Fail | analysis、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63705) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文围绕 Toward Understanding Adversarial Distillation 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于鲁棒防御与安全保证。 |
| 2026 | Towards Understanding Generalization of Federated Adversarial Learning: Perspective of Algorithmic Stability | analysis、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63797) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文围绕 Towards Understanding Generalization of Federated 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于鲁棒防御与安全保证。 |
| 2026 | Self-Calibrated Consistency can Fight Back for Adversarial Robustness in Vision-Language Models | defense、adversarial defense、adversarial robustness、VLM safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63826) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文围绕 Self-Calibrated Consistency can Fight Back 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于鲁棒防御与安全保证。 |
| 2026 | Posterior Mismatch Matters: Adversarial Training for Long-Tailed Robustness | defense、adversarial defense、adversarial training、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64623) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Posterior Mismatch Matters 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression | defense、adversarial defense、adversarial robustness、VLM safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61440) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 On the Adversarial Robustness of 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Benign Overfitting in Adversarial Training for Vision Transformers | defense、adversarial defense、adversarial training、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62410) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Benign Overfitting in Adversarial Training 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Adversarial Training for Process Reward Models | defense、adversarial defense、adversarial training、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66402) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Adversarial Training for Process Reward 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Adversarial Attacks and Robust Training for Hypergraph Neural Networks | defense、adversarial attack、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/65859) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Adversarial Attacks and Robust Training 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于对抗威胁建模。 |
| 2026 | Adversarial Attack and Defense for Denoising Diffusion Sampling | defense、adversarial attack、diffusion model、adversarial robustness | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62015) | 暂未公开 | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Adversarial Attack and Defense for 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于对抗威胁建模。 |

## Test-Time Adaptation 与 Input Purification

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Two Modalities Are Better Than One: Efficient Adversarial Purification via Multimodal Diffusion Models | defense、adversarial defense、adversarial robustness、VLM safety | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61378) | 暂未公开 | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Two Modalities Are Better Than One 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于鲁棒防御与安全保证。 |
| 2026 | Training-Free Adversarial Robustness in Computational MRI | defense、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64452) | [Code](https://github.com/MahdiSaberii/CycMit-MRI) | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 MRI 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | SS-TPT: Stability and Suitability-Guided Test-Time Prompt Tuning for Adversarially Robust Vision-Language Models | defense、adversarial robustness、VLM safety、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63418) | [Code](https://github.com/sunoh-kim/SS-TPT) | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 SS-TPT 防御或缓解方法；摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于鲁棒防御与安全保证。 |
| 2026 | Contrastive Spectral Rectification: Test-Time Defense towards Zero-shot Adversarial Robustness of CLIP | defense、adversarial defense、adversarial robustness、robust training | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61655) | [Code](https://github.com/Summu77/CSR) | 针对经验防御在自适应攻击和分布变化下可能失效且缺少可靠保证的问题，论文提出 Contrastive Spectral Rectification 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于鲁棒防御与安全保证。 |
| 2026 | Adversarial Patch EXterminator: Zero-Shot and Patch-Agnostic Defense Framework Against Adversarial Patch Attacks | defense、adversarial patch、adversarial robustness、robust training | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-jiayimei) | 暂未公开 | 针对未知形状与内容的实体 adversarial patch，APEX 依次进行候选区域聚集、基于互信息的模糊与边缘定位及图像修复，在无需攻击样本训练的设置下兼顾跨 patch 与物理场景防御。 |
