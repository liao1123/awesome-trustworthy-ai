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

### 1. Low-ASR Backdoors: Exploiting Attack Success Rate Reduction and Attacker-Defender Asymmetry

📄 [arXiv](https://arxiv.org/abs/2608.27288)　📅 2026-08

**关键词**：`attack`、`analysis`、`low-ASR backdoor`、`reverse training`、`defense evasion`、`backdoor-evaluation validity`

👤 **作者**：Arham Riaz、Ting Yu

- 🎯 **研究动机**：后门攻防默认有效后门必具高 ASR 并以此设计与评测防御，但 ASR 是攻击者可控变量而非后门固有属性
- 🔬 **研究方法**：提出 reverse-training 框架，主动削弱 trigger–target 关联，生成保留干净输入性能的低 ASR 后门模型
- 📌 **结论**：跨多个数据集、攻击家族与架构，SOTA 防御在低 ASR 条件下一致失效，暴露根本性的攻防不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are among the most effective and stealthy attacks in deep learning. Existing attacks and defenses are largely designed and evaluated under the assumption that successful backdoors exhibit high Attack Success Rates (ASRs). In this paper, we show that this assumption creates a fundamental weakness in existing defense paradigms. ASR is not an intrinsic property of a backdoor; rather, it is an attacker-controlled variable that can be deliberately reduced without eliminating the underlying backdoor behavior. We introduce a reverse-training framework that weakens the trigger-target association, producing low-ASR backdoor models while preserving clean-input performance. Through extensive evaluation across multiple datasets, diverse attack families, and multiple architectures, we show that state-of-the-art defenses fail consistently under low-ASR conditions, exposing a fundamental attacker-defender asymmetry.

</details>

### 2. Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE

📄 [arXiv](https://arxiv.org/abs/2608.25371) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3523)　📅 2026-08

**关键词**：`attack`、`Vision MoE backdoor`、`capacity overflow`、`supply-chain evasion`、`audit-deployment gap`、`batch-dependent execution`

👤 **作者**：Xiaocheng Zou、Tiancheng Zheng、Xiaolin Xu、Ruyi Ding

- 🎯 **研究动机**：Vision MoE 的 expert 容量随推理 batch size 变化，这一 batch 依赖行为是被忽视的供应链攻击面
- 🔬 **研究方法**：三阶段后门：早期层植入、深层 neutralizer 压制、部署级大 batch 溢出解除压制，形成审计休眠/部署激活两态
- 📌 **结论**：V-MoE 与 Swin-MoE 上激活态 ASR 76-87%、休眠态低于 9%，绕过 Neural Cleanse、STRIP 等四种检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) has become a prevalent paradigm for scaling Vision Transformers efficiently. To ensure computational scalability and prevent expert overload, Vision MoE architectures employ a capacity-bounded token dispatch mechanism, where each expert's processing budget depends on the inference batch size. This work identifies this batch-dependent behavior as an overlooked attack surface, and proposes a stealthy supply-chain backdoor attack that exploits this property through a three-phase framework. First, we inject a backdoor into an early MoE layer. Second, we train a neutralizer in a deeper MoE layer that suppresses the backdoor under normal capacity. Third, we configure a batch-adaptive capacity factor that preserves high capacity for small batches while reducing it for large batches, naturally disabling the neutralizer via token overflow at deployment-scale batch sizes. The attack remains in dormant mode during small-batch security audits and enters activation mode during large-batch deployment. Experiments on V-MoE and Swin-MoE across ImageNet-100 and GTSRB demonstrate activation-mode attack success rates of 76-87% with dormant-mode ASR below 9%, while evading Neural Cleanse, STRIP, Fine-Pruning, and Activation Clustering. Our findings reveal a fundamental security risk arising from batch-dependent execution in scalable Vision MoE architectures.

</details>

### 3. Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures

📄 [arXiv](https://arxiv.org/abs/2605.19478) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Exposing_Functional_Fusion_A_New_Class_of_Strategic_Backdoor_in_CVPR_2026_paper.html)　📅 2026-05　🏷 CVPR 2026

**关键词**：`attack`、`dynamic prompt`、`functional backdoor`、`trigger composition`

👤 **作者**：Zeyao Liu、Zhendong Zhao、Xiaojun Chen、Xin Zhao、Yuexin Xuan、Xiaoshuang Ji

- 🎯 **研究动机**：ViT 全量微调后门计算昂贵，PEFT 中 prompt-based 生态（VPT）的安全风险未被探索
- 🔬 **研究方法**：VIPER 基于轻量动态 Visual Prompt Generator，利用 Functional Fusion：恶意逻辑与良性任务效用融合进同一稀疏高幅参数核，形成剪枝必毁良性性能的人质困境
- 📌 **结论**：干净数据 SOTA 性能同时近 100% ASR，90% VPG 剪枝下仍维持（LoRA 攻击已崩溃），仅增 0.06ms 推理延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing ViT backdoor attacks based on backbone-overwriting full-tuning are computationally expensive and inflict performance degradation. This has forced adversaries towards the Visual Parameter-Efficient Fine-Tuning (PEFT) paradigm, dominated by adapter-based (e.g., LoRA) and prompt-based (e.g., VPT) approaches. While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored. We fill this critical gap, exposing how the evolution of VPT towards dynamic and context-aware architectures can facilitate a far more dangerous and emergent threat. This vulnerability arises even though these dynamic modules unlock superior benign performance. We propose VIPER, an attack framework built on a lightweight, dynamic Visual Prompt Generator (VPG) that demonstrates this vulnerability. Critically, this dynamic architecture enables Functional Fusion: an emergent phenomenon where malicious logic and benign task utility are tightly fused into the same sparse, high-magnitude parameter core. This fusion creates a formidable ``hostage" dilemma, as pruning the attack necessarily destroys the benign performance. Comprehensive evaluations show VIPER effectively addresses the attacker's trilemma: VIPER not only achieves state-of-the-art performance on clean data, but also maintains near-100% ASR even under 90% VPG-module pruning (where LoRA attacks collapse), while adding only an imperceptible 0.06ms (1.16%) of inference latency. VIPER's results, driven by Functional Fusion, expose a new, paradigm-level risk in dynamic prompt architectures.

</details>

### 4. PoInit-of-View: Poisoning Initialization of Views Transfers Across Multiple 3D Reconstruction Systems

📄 [arXiv](https://arxiv.org/abs/2604.16540) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_PoInit-of-View_Poisoning_Initialization_of_Views_Transfers_Across_Multiple_3D_Reconstruction_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`attack`、`3D reconstruction`、`view poisoning`、`cross-system transfer`

👤 **作者**：Weijie Wang、Songlong Xing、Zhengyu Zhao、Nicu Sebe、Bruno Lepri

- 🎯 **研究动机**：已有 3D 重建投毒把管线整体反向传播，未瞄准 SfM 初始化这一几何核心模块的漏洞
- 🔬 **研究方法**：PoInit-of-View 优化扰动在对应 3D 点投影处制造跨视图梯度不一致，破坏关键点检测与特征匹配进而污染位姿估计和三角化
- 📌 **结论**：黑盒迁移（如 3DGS 到 NeRF）下 PSNR 超 25.1%、SSIM 超 16.5%，实现跨系统投毒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning input views of 3D reconstruction systems has been recently studied. However, we identify that existing studies simply backpropagate adversarial gradients through the 3D reconstruction pipeline as a whole, without uncovering the new vulnerability rooted in specific modules of the 3D reconstruction pipeline. In this paper, we argue that the structure-from-motion (SfM) initialization, as the geometric core of many widely used reconstruction systems, can be targeted to achieve transferable poisoning effects across diverse 3D reconstruction systems. To this end, we propose PoInit-of-View, which optimizes adversarial perturbations to intentionally introduce cross-view gradient inconsistencies at projections of corresponding 3D points. These inconsistencies disrupt keypoint detection and feature matching, thereby corrupting pose estimation and triangulation within SfM, eventually resulting in low-quality rendered views. We also provide a theoretical analysis that connects cross-view inconsistency to correspondence collapse. Experimental results demonstrate the effectiveness of our PoInit-of-View on diverse 3D reconstruction systems and datasets, surpassing the single-view baseline by 25.1% in PSNR and 16.5% in SSIM in black-box transfer settings, such as 3DGS to NeRF.

</details>

### 5. Eliminate Distance Differences Induced by Backdoor Attacks: Layer-Selective Training and Clipping to Mask Backdoor Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Eliminate_Distance_Differences_Induced_by_Backdoor_Attacks_Layer-Selective_Training_and_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`backdoor evasion`、`layer-selective training`、`model inspection`

👤 **作者**：Xuzeng Li、…、Dong In Kim

- 🎯 **研究动机**：FL 后门攻击忽视各层对后门的异质贡献，且毒化早期与干净模型差异明显、易被检测
- 🔬 **研究方法**：LaySelFL 层选择性攻击：动静结合评估参数差异定位对后门最敏感的层并局部化投毒，配定向训练协议与约束每轮差异的正则，最后对非投毒层剪裁掩盖残差差异
- 📌 **结论**：攻击有效性提升 25%，防御方法有效性被压至 4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Federated learning (FL) enables a central server to collaboratively train a global model with multiple clients while preserving data privacy. However, the distributed nature of FL makes the paradigm vulnerable to backdoor attacks, as proved by numerous recent studies. Although existing studies improve the effectiveness of backdoor attacks through optimized triggers, they have two limitations: (1) they ignore the heterogeneous contribution of individual model layers to the success of a backdoor; (2) they induce conspicuous differences between backdoor and clean models in the early stages of poisoning. The limitations cause backdoor models to exhibit significant discrepancies from clean models, making them easily detectable. To fill these gaps, we propose LaySelFL, a novel layer-selective method to eliminate distance differences induced by the backdoor to conceal attacks in FL. Our central insight is that different layers contribute unequally to backdoor attacks, by localizing poisoning to layers that are most sensitive to backdoor objectives, an attacker can reduce the model differences substantially between the backdoor and clean models. Concretely, LaySelFL identifies sensitive layers via both dynamic and static evaluations of parameter differences between backdoor and benign models, and then applies a targeted training protocol and a regularized loss that constrains differences from the global model in each round. Finally, LaySelFL performs clipping on non-poisoning layers to further mask residual differences introduced by the attack. This strategy yields a more covert and resilient backdoor attack. Extensive experiments show that LaySelFL increases the effectiveness of attacks by 25% and reduces the effectiveness of defense methods to 4%.

</details>

### 6. Phantom: Physical Object Interactions as Dynamic Triggers for NMS-Exploited Backdoors

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Huo_Phantom_Physical_Object_Interactions_as_Dynamic_Triggers_for_NMS-Exploited_Backdoors_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`object detector`、`dynamic trigger`、`NMS backdoor`

👤 **作者**：Tianlin Huo、…、Yuan He

- 🎯 **研究动机**：已有目标检测后门依赖静态触发器的固有特征，现实场景实用性受限
- 🔬 **研究方法**：利用现实场景动态物体交互作触发器，劫持 Non-Maximum Suppression 过程实现误分类、误定位与目标出现/消失攻击
- 📌 **结论**：多检测器与数据集上攻击效果显著，物理环境与现有防御下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose potential threats to object detection models, highlighting the importance of studying their security. However, existing backdoor attacks mainly rely on trigger-specific intrinsic features, which limits their practicality in real-world scenarios. In this paper, we propose a novel backdoor attack that leverages dynamic object interactions in realistic scenarios to activate malicious behavior. By hijacking the Non-Maximum Suppression (NMS) process in object detectors, this attack demonstrates robust effectiveness, including misclassification, mislocalization, and object appearance/disappearance, while maintaining the model's normal performance on clean inputs. Experimental results demonstrate that our attack exhibits significant attack performance across various object detectors and datasets, and remains effective both in physical environments and under existing defense mechanisms. These findings highlight the urgent need to develop efficient and robust defense strategies against backdoor attacks.

</details>

### 7. Mask-Guided Hybrid Triggers for Robust Clean-Label Backdoor Attacks

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4403.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`clean-label backdoor`、`hybrid trigger`、`semantic mask`、`adaptive mask`

- 🎯 **研究动机**：干净标签后门中样本无关触发器鲁棒但易检测，样本特定触发器隐蔽却受特征抑制限制
- 🔬 **研究方法**：MGHT 自适应掩码把触发器空间分配给样本无关锚点（可靠记忆）与样本特定伪装（感知语义一致），协同损失防止单一成分贪心依赖
- 📌 **结论**：CIFAR-10 与 CelebA 上 ASR 超 99%，高分辨率基准亦有效，PSNR>30dB 且抗主流后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Clean-label backdoor attacks pose significant security threats to deep neural networks by injecting triggers without altering ground-truth labels. However, existing methods face a fundamental dilemma: sample-agnostic triggers are robust but easily detectable, while sample-specific triggers offer superior stealthiness but suffer from limited effectiveness due to feature suppression. To bridge this gap, we propose a new backdoor trigger framework called Mask-Guided Hybrid Trigger (MGHT). MGHT uses an adaptive mask to allocate spatial regions of the hybrid trigger between a sample-agnostic anchor for reliable memorization and a sample-specific camouflage for perceptual and semantic consistency. To prevent the optimization from greedily relying on a single trigger component, we further propose a Synergy-driven Co-optimization Strategy with a margin-based Synergy Loss. This ensures that the hybrid trigger is more effective and robust than either component alone. Extensive experiments on benchmark datasets demonstrate that MGHT achieves competitive performance, attaining over 99% ASR on CIFAR-10 and CelebA and showing strong effectiveness on higher-resolution benchmarks, while maintaining high visual quality (PSNR > 30 dB) and robustness to mainstream backdoor defenses.

</details>

### 8. The Eminence in Shadow: Exploiting Feature Boundary Ambiguity for Robust Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2512.10402) · 🌐 [Project](https://doi.org/10.1145/3770854.3780322)　📅 2025-12　🏷 KDD 2026

**关键词**：`analysis`、`attack`、`feature-boundary geometry`、`influence function`、`attack durability`、`backdoor`

👤 **作者**：Zhou Feng、…、Shouling Ji

- 🎯 **研究动机**：后门研究缺乏严格理论分析，攻击的可预测性与适应性受限
- 🔬 **研究方法**：理论分析稀疏决策边界如何被少量边缘重标注样本非对称操纵，推导闭式模糊边界区域并以影响函数量化，据此优化利用脆弱边界的通用细微信号触发器
- 📌 **结论**：投毒率低于 0.1%（SOTA 常需超过 1%）仍保持 90% 以上 ASR 且 clean 精度几乎无损，跨模型与数据集可迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) underpin critical applications yet remain vulnerable to backdoor attacks, typically reliant on heuristic brute-force methods. Despite significant empirical advancements in backdoor research, the lack of rigorous theoretical analysis limits understanding of underlying mechanisms, constraining attack predictability and adaptability. Therefore, we provide a theoretical analysis targeting backdoor attacks, focusing on how sparse decision boundaries enable disproportionate model manipulation. Based on this finding, we derive a closed-form, ambiguous boundary region, wherein negligible relabeled samples induce substantial misclassification. Influence function analysis further quantifies significant parameter shifts caused by these margin samples, with minimal impact on clean accuracy, formally grounding why such low poison rates suffice for efficacious attacks. Leveraging these insights, we propose Eminence, an explainable and robust black-box backdoor framework with provable theoretical guarantees and inherent stealth properties. Eminence optimizes a universal, visually subtle trigger that strategically exploits vulnerable decision boundaries and effectively achieves robust misclassification with exceptionally low poison rates (< 0.1%, compared to SOTA methods typically requiring > 1%). Comprehensive experiments validate our theoretical discussions and demonstrate the effectiveness of Eminence, confirming an exponential relationship between margin poisoning and adversarial boundary manipulation. Eminence maintains > 90% attack success rate, exhibits negligible clean-accuracy loss, and demonstrates high transferability across diverse models, datasets and scenarios.

</details>

### 9. Towards Stealthy and Effective Backdoor Attacks on Lane Detection: A Naturalistic Data Poisoning Approach

📄 [arXiv](https://arxiv.org/abs/2508.15778) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liao_Towards_Stealthy_and_Effective_Backdoor_Attacks_on_Lane_Detection_A_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`attack`、`lane detection`、`naturalistic trigger`、`data poisoning`

👤 **作者**：Yifan Liao、…、Jin Song Dong

- 🎯 **研究动机**：车道检测后门攻击的触发器人工痕迹明显，现实实用性受限
- 🔬 **研究方法**：提出扩散式投毒框架 DBALD：梯度热图定位最优触发位置，区域编辑扩散合成视觉合理的触发器，配车道结构与驾驶场景一致性双重损失
- 📌 **结论**：四个主流车道检测模型上平均成功率比 SoTA 高 10.87%，隐蔽性显著增强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning-based lane detection (LD) plays a critical role in autonomous driving and advanced driver assistance systems. However, its vulnerability to backdoor attacks presents a significant security concern. Existing backdoor attack methods on LD often exhibit limited practical utility due to the artificial and conspicuous nature of their triggers. To address this limitation and investigate the impact of more ecologically valid backdoor attacks on LD models, we examine the common data poisoning attack and introduce DBALD, a novel diffusion-based data poisoning framework for generating naturalistic backdoor triggers. DBALD comprises two key components: optimal trigger position finding and stealthy trigger generation. Given the insight that attack performance varies depending on the trigger position, we propose a heatmap-based method to identify the optimal trigger location, with gradient analysis to generate attack-specific heatmaps. A region-based editing diffusion process is then applied to synthesize visually plausible triggers within the most susceptible regions identified previously. Furthermore, to ensure scene integrity and stealthy attacks, we introduce two loss strategies: one for preserving lane structure and another for maintaining the consistency of the driving scene. Consequently, compared to existing attack methods, DBALD achieves both a high attack success rate and superior stealthiness. Extensive experiments on 4 mainstream LD models show that DBALD exceeds state-of-the-art methods, with an average success rate improvement of +10.87% and significantly enhanced stealthiness. The experimental results highlight significant practical challenges in ensuring model robustness against real-world backdoor threats in LD.

</details>

### 10. GaussTrap: Stealthy Backdoor Attacks on 3D Gaussian Splatting for Targeted Scene Misperception

📄 [arXiv](https://arxiv.org/abs/2504.20829) · 🌐 [Project](https://doi.org/10.1145/3770855.3817947)　📅 2025-04　🏷 KDD 2026

**关键词**：`attack`、`3D Gaussian splatting`、`view-conditioned backdoor`、`scene integrity`、`backdoor`、`scene misperception`

👤 **作者**：Jiaxin Hong、…、Jiawei Li

- 🎯 **研究动机**：3DGS 进入自动驾驶与 AR/VR 等安全攸关场景，后门威胁缺乏系统研究
- 🔬 **研究方法**：提出 GaussTrap，经攻击、稳定化、正常训练三阶段在特定视点植入视角一致的毒化渲染，非目标视点保持高质量
- 📌 **结论**：合成与真实数据上均嵌入隐蔽有害后门视图并维持正常视图渲染质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As 3D Gaussian Splatting (3DGS) emerges as a breakthrough in scene representation and novel view synthesis, its rapid adoption in safety-critical domains (e.g., autonomous systems, AR/VR) urgently demands scrutiny of potential security vulnerabilities. This paper presents the first systematic study of backdoor threats in 3DGS pipelines. We identify that adversaries may implant backdoor views to induce malicious scene confusion during inference, potentially leading to environmental misperception in autonomous navigation or spatial distortion in immersive environments. To uncover this risk, we propose GuassTrap, a novel poisoning attack method targeting 3DGS models. GuassTrap injects malicious views at specific attack viewpoints while preserving high-quality rendering in non-target views, ensuring minimal detectability and maximizing potential harm. Specifically, the proposed method consists of a three-stage pipeline (attack, stabilization, and normal training) to implant stealthy, viewpoint-consistent poisoned renderings in 3DGS, jointly optimizing attack efficacy and perceptual realism to expose security risks in 3D rendering. Extensive experiments on both synthetic and real-world datasets demonstrate that GuassTrap can effectively embed imperceptible yet harmful backdoor views while maintaining high-quality rendering in normal views, validating its robustness, adaptability, and practical applicability.

</details>

### 11. Beyond Small Patches: Black-Box Detection and Purification of Diverse Backdoor Triggers

📄 [arXiv](https://arxiv.org/abs/2609.03139)　📅 2026-09

**关键词**：`defense`、`black-box backdoor`、`trigger purification`、`deployment`

👤 **作者**：Ahmed Abdelnaby、Mohamed Elmahallawy

- 🎯 **研究动机**：既有后门防御依赖模型内部、训练数据或干净验证样本，仅有黑盒访问的部署场景难以使用
- 🔬 **研究方法**：提出 TRIM：部署导向的黑盒推理时防御——深度特征做区域分割，inpainting 与 diffusion 重建自适应发现引发异常行为的区域（不假设触发器类型／形状／位置），选择性净化并缓存已知触发器特征
- 📌 **结论**：跨 blended、sparse、变尺寸与多触发器等后门类型持续超过黑盒基线，ASR 最低降到 1.16%、clean accuracy 最高保持 87.87%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks (DNNs) are increasingly deployed in real-world vision systems, yet their predictions can be covertly manipulated by backdoor attacks, in which malicious triggers cause targeted misclassification while preserving high clean accuracy. Existing defenses often rely on model internals, training data, or clean validation samples, making them difficult to deploy when only black-box access to a trained model is available. We propose TRIM (Trigger Removal by Identifying Manipulated Regions), a deployment-oriented black-box defense that detects and selectively removes backdoor triggers at inference time without requiring model internals, training data, or clean samples. The key insight behind TRIM is to identify image regions that are responsible for anomalous model behavior and purify only those regions while preserving benign content. TRIM innovates via three key components: (i) region-based segmentation with deep feature representations, (ii) adaptive trigger discovery through inpainting and diffusion-based reconstruction to isolate regions responsible for misclassification---without assumptions about trigger type, shape, or location, and (iii) selective region purification that cleans poisoned regions while retaining benign content. To support practical deployment, TRIM further caches feature embeddings of previously identified triggers, enabling efficient recognition and avoiding redundant detection and purification. Extensive experiments across diverse datasets and backdoor types, including blended, sparse, varying-size, and multiple triggers, show that TRIM consistently outperforms existing black-box defenses, reducing attack success rates (ASR) to as low as 1.16% while preserving clean accuracy of up to 87.87%. These results demonstrate that effective backdoor mitigation is possible at inference time even when the defender has no access to any auxiliary data.

</details>

### 12. DEFUSE: Generalizable Backdoor Defense for Self-Supervised Encoders with Generative Priors

📄 [arXiv](https://arxiv.org/abs/2608.25851) · 🌐 [Project](https://doi.org/10.1145/3767308.3835471)　📅 2026-08

**关键词**：`detection`、`SSL encoder backdoor`、`generative prior`、`cross-paradigm generalization`、`vision-language encoder`、`semantic reconstruction`

👤 **作者**：Tuo Chen、…、Jian Liu

- 🎯 **研究动机**：SSL encoder 后门防御只覆盖单一范式，且依赖未感染数据等强假设
- 🔬 **研究方法**：DEFUSE 用 diffusion 先验从表示重建图像，中毒表示会映射到目标类或无语义图像，据此检测
- 📌 **结论**：跨视觉 SSL 与 vision-language encoder 的攻击下优于现有检测器，且降低对 victim 与攻击的先验依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised learning (SSL) encoders are vulnerable to backdoor attacks, posing threats to both visual SSL encoders and vision-language encoders. Existing defenses are typically designed for only one of these paradigms and rely on restrictive assumptions such as access to uninfected in-distribution data or precomputed pseudo-labels, which are difficult to satisfy in practice. To address these limitations, we propose DEFUSE, a generalizable backdoor detection framework for SSL encoders. Inspired by Bayesian posterior inference, we reformulate backdoor detection as a representation-conditioned image likelihood estimation problem parameterized by a conditional diffusion generative model. Uninfected representations tend to yield semantically consistent reconstructions, whereas backdoored ones are more likely to be mapped to the attacker's target class or semantically meaningless images, deviating from the original semantics and thereby exposing the backdoor. However, we find that the exact likelihood is intractable, because highly abstracted representations discard the low-level information necessary for pixel-faithful reconstruction. We therefore relax the objective to semantic reconstruction and evaluate it in a well-separated representation space provided by a reference encoder. Rather than training from scratch, we fine-tune a pretrained diffusion model, leveraging its generative prior to map data onto the natural image manifold while preserving semantic content. Extensive experiments demonstrate that DEFUSE substantially outperforms existing detectors across diverse attack settings, generalizing to both visual SSL and vision-language encoders. Notably, our method greatly reduces the reliance on prior knowledge about the victim encoder or the attack strategy. The source code is available at https://github.com/jsrdcht/DEFUSE .

</details>

### 13. Purified Distillation Slimming (PDS) for Robust Backdoor Defense

🌐 [Project](https://doi.org/10.1145/3779208.3785283)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`defense`、`backdoor purification`、`knowledge distillation`、`network slimming`、`DNN backdoor`、`purified distillation`

- 🎯 **研究动机**：DNN后门净化难以兼顾净化强度与模型效用
- 🔬 **研究方法**：结合purified distillation与网络slimming压缩后门通路
- 📌 **结论**：移除后门同时保留主任务精度

### 14. Deep Learning Backdoor Defense via Adaptive Trigger Collisions in Latent Space

🌐 [Project](https://doi.org/10.1145/3779208.3806081)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`defense`、`DNN backdoor`、`latent collision`、`post-processing repair`、`post-processing`

- 🎯 **研究动机**：现有后处理防御只重输出 logits、需注入不确定新触发器、且未充分利用毒化表征
- 🔬 **研究方法**：ATClean 潜在空间自适应特征碰撞防御：用自适应损失经全部层捕获后门影响区域，生成只强制特征碰撞的对抗样本（免精确触发重建且有理论保证），并以特征碰撞微调修复
- 📌 **结论**：跨基准数据集、多架构与七种攻击达 SOTA 且干净数据掉点最低，DER 提升约 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in data outsourcing settings pose severe risks to deep neural networks. Specifically, adversaries can manipulate externally sourced training data to implant hidden behaviors in target models (e.g., incorrect predictions on triggered samples). Existing defenses are either pre-processing or post-processing. Since the two approaches are orthogonal and either one can independently strengthen real-world defenses, we focus on the latter in this paper. Yet current post-processing defenses face one or more of the following issues: overemphasis on output logits while overlooking rich information in intermediate layers, injection of uncertain new triggers while requiring alignment with the original triggers, and underuse of poisoned model representations. To overcome the aforementioned limitations, we propose ATClean, an adaptive post-processing defense based on feature collisions in latent space. Specifically, it leverages all layers rather than only output logits to capture backdoor-affected regions using an adaptive loss function, relaxes the need for exact trigger reconstruction by generating adversarial samples that only enforce feature collisions with a theoretical guarantee, and fully exploits poisoned representations with feature-collision-based fine-tuning. Experiments across benchmark datasets, multiple architectures, and seven representative attacks show that ATClean achieves state-of-the-art defense effectiveness with the lowest drop on clean data, including about a 20% improvement in DER, which measures the accuracy-defense trade-off.

</details>

### 15. Logit-Margin Repulsion for Backdoor Defense

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Logit-Margin_Repulsion_for_Backdoor_Defense_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`backdoor removal`、`logit margin`、`model repair`

👤 **作者**：Zhiguo Yang、Dongsheng Xu、Ruizhi Zhong、Jiacheng Pi、Xingxing Huang、Wenjie Ruan

- 🎯 **研究动机**：量化/剪枝等压缩操作可被用来植入条件后门（原模型休眠、特定操作后激活），传统与专用防御难以兼顾两类后门
- 🔬 **研究方法**：LMR 用少量干净样本结合选择性交叉熵与 logit 间隔约束扩大后门类间隔，再选择性剪枝移除后门相关通道
- 📌 **结论**：仅 0.1% 干净数据即可在 CNN 与 ViT 上同时缓解传统与条件后门攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to deep neural networks. Recent studies have shown that model compression, such as quantization and pruning, can be exploited by attackers to implant conditional backdoors. Such backdoors remain dormant in the original model but are activated after the model undergoes specific operations, making them highly stealthy and difficult to detect. Traditional defense methods struggle to counter this type of attack, while defenses specifically designed for conditional backdoors also have difficulty handling traditional backdoor attacks. To address these challenges, we propose a universal defense method, termed Logit Margin Repulsion (LMR). LMR uses a small set of clean samples and combines selective cross-entropy with a logit-margin constraint to enlarge the gap between the backdoor class and benign classes. It then removes channels associated with backdoor behavior through selective pruning, thereby achieving strong backdoor purification. Extensive experiments on a variety of CNNs and Vision Transformers demonstrate that, even with an extremely limited amount of clean data (0.1%), LMR can effectively mitigate both traditional and conditional backdoor attacks. The implementation is publicly available on https://github.com/Trusted-LLM/LMR.

</details>

### 16. Mitigating Backdoors via Decoy Shortcuts and Knowledge Decoupling

📄 [arXiv](https://arxiv.org/abs/2608.00732) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2444.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`backdoor removal`、`decoy shortcut`、`knowledge decoupling`

👤 **作者**：Zixuan Zhu、Rui Wang、Lihua Jing、Jinwen Zhong

- 🎯 **研究动机**：依赖第三方数据训练时后门攻击威胁严重，缺训练时防御
- 🔬 **研究方法**：发现后门行为倾向被并联简单分支吸收：TR 引入轻量 shortcut 分支作蜜罐，熵加权知识解耦引导毒样本流向蜜罐，训练后丢弃即移除后门且无需额外数据
- 📌 **结论**：四个基准数据集、五种架构上有效缓解多种后门并保留良性性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to deep neural networks, especially when training relies on third-party data, allowing adversaries to inject malicious behaviors through data poisoning. In this work, we reveal that backdoor behaviors tend to be absorbed by a simpler parallel branch when jointly trained with the main network. Motivated by this insight, we propose Trapping and Removing (TR), a simple yet effective training-time defense that introduces a lightweight shortcut branch as a “honeypot” to trap backdoor knowledge. After training, backdoors can be removed by discarding the shortcut, without requiring any additional data. To further enhance backdoor isolation while maintaining benign performance, we design a knowledge decoupling strategy with entropy-based weight assignment, encouraging poisoned samples to flow through the honeypot while guiding the main network to focus on benign learning. In addition, we introduce an automatic shortcut generation strategy to improve generalization across model architectures. Extensive experiments on four benchmark datasets and five model architectures demonstrate that our approach effectively mitigates a wide range of backdoor attacks while preserving performance on benign data. Code: github.com/Zixuan-Zhu/TR.

</details>

### 17. SoK: On the Survivability of Backdoor Attacks on Unconstrained Face Recognition Systems

📄 [arXiv](https://arxiv.org/abs/2507.01607) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-07　🏷 SaTML 2026

**关键词**：`survey`、`face recognition`、`backdoor survivability`、`system-level analysis`

👤 **作者**：Quentin Le Roux、Yannick Teglia、Teddy Furon、Philippe Loubet-Moundi、Eric Bourbao

- 🎯 **研究动机**：后门研究多针对孤立组件，完整人脸识别系统的系统级分析缺失
- 🔬 **研究方法**：组合针对人脸检测、反欺骗与特征提取器的后门文献，整体分析 20 种流水线配置与 15 种攻击场景
- 📌 **结论**：攻击者只需攻陷单个被后门模型即可波及整个人脸识别系统，并给出最佳实践与对策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread deployment of Deep Learning-based Face Recognition Systems raises many security concerns. While prior research has identified backdoor vulnerabilities on isolated components, Backdoor Attacks on real-world, unconstrained pipelines remain underexplored. This SoK paper presents the first comprehensive system-level analysis and measurement of the impact of Backdoor Attacks on fully-fledged Face Recognition Systems. We combine the existing Supervised Learning backdoor literature targeting face detectors, face antispoofing, and face feature extractors to demonstrate a system-level vulnerability. By analyzing 20 pipeline configurations and 15 attack scenarios in a holistic manner, we reveal that an attacker only needs a single backdoored model to compromise an entire Face Recognition System. Finally, we discuss the impact of such attacks and propose best practices and countermeasures for stakeholders.

</details>