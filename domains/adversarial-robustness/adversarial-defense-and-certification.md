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

### 1. GeoDetect: Geometric Adversarial Detection for VLPs

📄 [arXiv](https://arxiv.org/abs/2607.14737) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3531)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`adversarial detection`、`geometric analysis`、`adversarial robustness`、`vision-language model`

👤 **作者**：Afsaneh Hasanebrahimi、Hanxun Huang、Christopher Leckie、James Bailey、Sarah Erfani

- 🎯 **研究动机**：对抗检测在单模态（视觉或语言）成功，其在 VLP 多模态模型上的有效性与可靠性未被探索
- 🔬 **研究方法**：研究 VLP 嵌入空间的各向异性几何，理论上证明对抗样本比干净样本具有更大的期望几何分离（被推出流形），据此提出 GeoDetect 用几何分数识别对抗样本
- 📌 **结论**：跨多样 VLP 架构与威胁设定（单模态、多模态及自适应攻击）可靠检出对抗样本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language pre-trained models (VLPs) are widely used in real-world applications. However, they remain vulnerable to adversarial attacks. Although adversarial detection methods have demonstrated success in single-modality settings (either vision or language), their effectiveness and reliability in multimodal models such as VLPs remain largely unexplored. In this work, we study the geometry of VLP embedding spaces and observe structured anisotropy that differs from unimodal vision models. Our theoretical analysis shows that under this anisotropic structure, adversarial attacks increase the expected geometric separation between clean and adversarial examples (AEs). Specifically, we demonstrate that AEs consistently exhibit greater expected distances to randomly sampled points than their clean counterparts, indicating that AEs tend to push representations out of manifold regions. Building on these insights, we propose GeoDetect, which leverages these off-manifold deviations via geometric scores to identify AEs. Through comprehensive evaluations, we show that our approach reliably detects AEs across diverse VLP architectures and threat settings, covering unimodal and multimodal attacks as well as adaptive attacks, thereby providing a robust and practical approach to improving the safety and reliability of these models.

</details>

### 2. A Classifier-Agnostic Zero-Shot Adversarial Attack Detection via CLIP

📄 [arXiv](https://arxiv.org/abs/2606.30342) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4853)　📅 2026-06　🏷 ECCV 2026

**关键词**：`detection`、`attack detection`、`adversarial robustness`、`robust training`、`adversarial example`、`black-box security`

👤 **作者**：Hodaya Krakover、Meir Yossef Levi、Eyal Gofer、Guy Gilboa

- 🎯 **研究动机**：已有对抗检测依赖攻击特定假设、对抗样本或分类器白盒知识
- 🔬 **研究方法**：提出 A4D：完全黑盒零样本检测框架，利用 CLIP 提示相似度分数，基于 CLIP 对非语义扰动敏感且嵌入偏移非任意两个观察
- 📌 **结论**：多攻击、数据集与分类器上在攻击无关、架构无关设定取得 SOTA 检测结果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks pose a challenge to the reliability of deep learning models, motivating effective detection methods. Existing techniques often rely on attack-specific assumptions, access to adversarial samples, or knowledge of the underlying classifier (white-box). We propose $A^4D$ Attack- and Architecture-Agnostic Adversarial Detector, a completely black-box, zero-shot adversarial attack detection framework that utilizes prompt-based similarity scores derived from CLIP. To the best of our knowledge this is the first attempt to utilize CLIP for such a task. The method is based on two key observations: (i) CLIP is sensitive even to small imperceptible non-semantic perturbations; (ii) The shift in CLIP embedding space is not arbitrary and can be used as a robust attack indicator. Experiments across multiple attacks, datasets and classifiers validate that $A^4D$ achieves SOTA detection results in the attack-agnostic and classifier-agnostic setting.

</details>

### 3. Adversarial Attack and Disturbance Detection by Hadamard-Coded Output Representations for Object Detection and Semantic Segmentation

📄 [arXiv](https://arxiv.org/abs/2606.09536) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5869)　📅 2026-06　🏷 ECCV 2026

**关键词**：`detection`、`adversarial detection`、`adversarial robustness`、`robust training`、`perturbation detection`、`Hadamard encoding`

👤 **作者**：Lucas Görnhardt、Timo Bartels、Niklas Schwarz、Tim Fingscheidt

- 🎯 **研究动机**：one-hot 编码校准差、攻击下过度自信使熵检测失效；Hadamard 码在分类上提升鲁棒性但未进入分割与检测
- 🔬 **研究方法**：推导面向类别最优概率的 Hadamard 码字解码（单纯形投影），利用码字内在不一致度量做攻击/扰动检测，提出 HadamardNet 用于分割与检测
- 📌 **结论**：在扰动与对抗攻击下两项任务均取得单次前向 SOTA 扰动检测性能，干净数据性能持平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conventional one-hot encodings often yield poorly calibrated models, being overconfident under attack, and letting entropy-based detection algorithms fail. Previous image classification works have demonstrated that Hadamard-coded output representations can improve adversarial robustness. However, attempts to integrate Hadamard codes into semantic segmentation fall far behind state-of-the-art models in mean intersection-over-union performance. Regarding object detection, such output encodings have not yet been investigated at all. Further, no prior art addressed intrinsic codeword inconsistencies or actually exploited intrinsic codeword redundancy. Accordingly, we first derive a novel decoding procedure for Hadamard codewords towards optimal class-wise probabilities, solving the underlying optimization problem by using the projection onto the probability simplex. Second, our optimization delivers a measure of prediction inconsistency. Third, we are the first to show how to exploit these inconsistencies for adversarial attack and disturbance detection. Fourth, we introduce HadamardNet, a framework employing Hadamard codes as output representations for semantic segmentation and object detection models and tasks. We conduct a comprehensive evaluation both on disturbances and adversarial attacks, achieving state-of-the-art perturbation detection performance for both tasks in only a single detection pass, while delivering equivalent or close-by reference performance on clean data. Code is available at https://github.com/ifnspaml/HadamardPerturbationDetection.

</details>

### 4. Improving Adversarial Robustness of Attribution via Implicit Regularization

📄 [arXiv](https://arxiv.org/abs/2605.29983) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63020)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`adversarial defense`、`adversarial robustness`、`robust training`、`empirical evaluation`、`robustness certification`

👤 **作者**：Amir Mehrpanah、Matteo Gamba、Hossein Azizpour

- 🎯 **研究动机**：归因鲁棒性方法依赖计算昂贵的显式正则化
- 🔬 **研究方法**：证明标准 SGD 学习动态可隐式带来归因鲁棒（参数与输入空间曲率联系），并证明 softmax 注意力归因因熵约束无法获得该增益、换核注意力可恢复
- 📌 **结论**：以近零开销跨架构、数据集、归因方法验证，transformer 换 kernel attention 即恢复鲁棒增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The adversarial robustness of attributions is a fundamental requirement for reliable explainability in deep learning, yet existing approaches typically rely on computationally expensive explicit regularization. In this work, we show that attribution robustness can arise implicitly from the learning dynamics of standard stochastic gradient descent. We theoretically motivate this effect through connections between parameter-space and input-space curvature, and validate it across architectures, datasets, and attribution methods, with negligible computational overhead. In contrast, we prove that such robustness gains often does not transfer to attention-based attribution under softmax normalization, due to inherent entropy constraints, and we validate this limitation experimentally. Finally, we show that replacing softmax attention with kernel-based attention restores the robustness gains in transformer models. Our results highlight learning dynamics as a principled and practical mechanism for robust explainability, and reveal fundamental limitations of attention-based attribution under normalization.

</details>

### 5. Adversarial Robustness of Implicit Neural Representation-Based Classifiers

🎓 [Official](https://icml.cc/virtual/2026/poster/63843)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`adversarial defense`、`adversarial robustness`、`robust training`、`empirical evaluation`

👤 **作者**：Jayoung Kim、Kookjin Lee、Noseong Park、Sanghyun Hong

- 🎯 **研究动机**：INR 分类管线把识别移到函数式表示上，其对抗鲁棒性从未被系统研究，且逐样本训练使优化在环内、标准梯度攻击计算不可行
- 🔬 **研究方法**：设计摊销 INR 生成过程的代理模型作为攻击实用代理，并开发加速技术大幅降低代理训练成本
- 📌 **结论**：与近期结论相反，INR 分类器在对抗输入扰动下准确率崩至近零，面向离散表示设计的现有对策保护有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Implicit neural representations (INRs) encode data as continuous coordinate-based functions parameterized by neural networks, shifting downstream tasks such as image recognition to operate on functional rather than discrete representations. Despite their increasing adoption, the adversarial robustness of INR-based classification pipelines remain largely underexplored. In this work, we present the first systematic study of adversarial robustness in INR-based classifiers. A key challenge is that generating an INR requires $\text{\emph{training}}$ a neural network for each input sample, resulting in an optimization-in-the-loop forward pass that renders standard gradient-based attacks computationally prohibitive. To address this, we design surrogate models that amortizes the INR-generation process, serving as a practical proxy for attacking INR-based classifiers. We also develop speed-up techniques that substantially reduce the training cost of the surrogate. We show that in contrast to recent work, INR-based classifiers are vulnerable: under adversarial input perturbations, classification accuracy collapses to near zero. Moreover, existing countermeasures designed to operate on discrete representations offer limited protection.

</details>

### 6. CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models

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

### 7. Improving Adversarial Robustness via Activation Amplification and Attenuation

📄 [arXiv](https://arxiv.org/abs/2606.27784) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3522)　📅 2026-06　🏷 ECCV 2026

**关键词**：`defense`、`adversarial robustness`、`robust training`、`certification`、`activation scaling`、`lightweight module`

👤 **作者**：Taïga Gonçalves、Yongsong Huang、Tomo Miyazaki、Shinichiro Omachi

- 🎯 **研究动机**：对抗攻击的存在常归因于非鲁棒特征，已有防御经剪枝、掩码或特征重校准削减其影响，未尝试联合放大与衰减
- 🔬 **研究方法**：提出 A3 轻量即插模块：用可学习掩码与源自激活幅值的缩放因子动态重缩放激活，翻转符号即可在放大/衰减间切换，放大信号作负参照构造对比与排序损失
- 📌 **结论**：放大模式学习退化预测同时提升衰减模式的鲁棒性；跨 backbone、数据集与训练方法一致提升对抗鲁棒性且计算内存开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The existence of adversarial attacks is often attributed to the presence of non-robust features in neural networks. While prior defenses reduce their impact via pruning, masking, or feature recalibration, we instead propose to jointly learn to amplify and attenuate these signals through a simple activation scaling mechanism. To this end, we introduce Activation Amplification and Attenuation (A3), a lightweight plug-in module that enhances adversarial robustness with minimal modifications of the activations. A3 dynamically rescales the activations using a learnable mask and a scaling factor derived from the original activation magnitudes. The influence of adversarial perturbations can be amplified or attenuated using the same learnable parameters by simply flipping the sign of the scaling operation. The amplified signals serve as negative references to construct novel contrastive and ranking loss functions. Experimental analysis shows that learning to degrade the predictions in amplification mode simultaneously improves adversarial robustness in attenuation mode. Moreover, A3 relies on only a small number of learnable parameters, with most of its behavior being determined by the scaling mechanism rather than additional network capacity. Extensive experiments demonstrate that integrating A3 into different backbones, datasets, and training methods consistently improves adversarial robustness while introducing negligible computational and memory overhead compared to existing plug-in modules. Code is available at: https://github.com/tgoncalv/A3.

</details>

### 8. Cascading Robustness Verification: Toward Efficient Model‑Agnostic Certification

📄 [arXiv](https://arxiv.org/abs/2602.04236) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-02　🏷 SaTML 2026

**关键词**：`defense`、`robustness verification`、`verifier cascade`、`certified accuracy`

👤 **作者**：Mohammadreza Maleki、Rushendra Sidibomma、Arman Adibi、Reza Samavi

- 🎯 **研究动机**：单一不完备验证器因松弛近似或与训练方法错配而系统性低估鲁棒性
- 🔬 **研究方法**：级联验证框架 CRV：多验证器下任一认证即鲁棒，从最便宜方法开始逐步升级，并对昂贵方法引入逐步松弛算法增量添加约束
- 📌 **结论**：认证精度不低于级联中强验证器，运行时间最多节省约 90%，且保证与模型训练过程无关

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Certifying neural network robustness against adversarial examples is challenging, as formal guarantees often require solving non-convex problems. Hence, incomplete verifiers are widely used because they scale efficiently and substantially reduce the cost of robustness verification compared to complete methods. However, relying on a single verifier can underestimate robustness because of loose approximations or misalignment with training methods. In this work, we propose Cascading Robustness Verification (CRV), which goes beyond an engineering improvement by exposing fundamental limitations of existing robustness metric and introducing a framework that enhances both reliability and efficiency. CRV is a model-agnostic verifier, meaning that its robustness guarantees are independent of the model's training process. The key insight behind the CRV framework is that, when using multiple verification methods, an input is certifiably robust if at least one method certifies it as robust. Rather than relying solely on a single verifier with a fixed constraint set, CRV progressively applies multiple verifiers to balance the tightness of the bound and computational cost. Starting with the least expensive method, CRV halts as soon as an input is certified as robust; otherwise, it proceeds to more expensive methods. For computationally expensive methods, we introduce a Stepwise Relaxation Algorithm (SR) that incrementally adds constraints and checks for certification at each step, thereby avoiding unnecessary computation. Our theoretical analysis demonstrates that CRV achieves equal or higher verified accuracy compared to powerful but computationally expensive incomplete verifiers in the cascade, while significantly reducing verification overhead. Empirical results confirm that CRV certifies at least as many inputs as benchmark approaches, while improving runtime efficiency by up to ~90%.

</details>

### 9. You Don't Protect if You Don't Expect: Breaking the Key Assumption behind CLIP's Test-Time Defenses

🎓 [Official](https://icml.cc/virtual/2026/poster/64735)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial robustness`、`robust training`、`certification`、`adversarial defense`、`inference-time intervention`

👤 **作者**：Ruize Zhang、Yu Li、Zhang Wan、Juan Cao、Jie Zhang、Sheng Tang

- 🎯 **研究动机**：六种CLIP测试时防御的鲁棒性被高估，共同依赖指示度量可区分干净与对抗样本的假设
- 🔬 **研究方法**：CLIP-MAD自适应攻击无需全梯度即扩展对抗分布，可与既有攻击组合
- 📌 **结论**：13个数据集上击穿多种防御，揭示虚假安全感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent test-time defenses for CLIP claim to preserve zero-shot clean accuracy while improving adversarial robustness. However, we find the reported robustness of six recent proposed state-of-the-art methods substantially overestimated: they fail under basic adaptive attacks. We further observe that these defenses share a common reliance on an indicative measurement that is assumed to capture the distributional difference between clean and adversarial samples and to determine whether the defense should preserve or alter the static model's prediction. We argue that this assumption is the fundamental weakness, and we propose CLIP-MAD (Manipulating Assumed Difference), an adaptive attack strategy designed to break it. CLIP-MAD efficiently expands the adversarial distribution without costly full gradient calculations and can be flexibly combined with existing attack baselines to further boost attack strength. Experiments across 13 datasets demonstrate that CLIP-MAD produces strong adversarial samples that markedly reduce the robustness of diverse test-time defenses, revealing a false sense of security in CLIP’s zero-shot robustness. Code will be available at https://github.com/rzzhang222/CLIP-MAD.

</details>

### 10. The Latent Guardian: Defending Collaborative Perception via Feature-Level Consistency Verification

🎓 [Official](https://icml.cc/virtual/2026/poster/64455)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial robustness`、`robust training`、`certification`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Zhuangzhuang Zhang、MingXin Li、Libing Wu、Wei-Bin Lee、Jianping Wang

- 🎯 **研究动机**：协同感知依赖多车数据融合，现有输出级共识防御假设恶意消息为统计离群点，对隐匿对抗攻击脆弱且环境噪声下误报高
- 🔬 **研究方法**：提出 Cerberus 把防御从输出级共识转向特征空间内部一致性：量化特征图拓扑结构、语义方向与能量分布的多维冲突以检测对抗扰动并提供动态防护
- 📌 **结论**：显著超越 SOTA，将攻击成功率压至最低 0.05% 同时把 AP 恢复到 0.88

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collaborative perception (CP) significantly extends the sensing range of connected and autonomous vehicles (CAVs). However, its reliance on data fusion among multiple CAVs makes it inherently vulnerable to adversarial attacks from malicious participants. Existing defenses primarily rely on output-level consensus, assuming that malicious messages manifest as statistical outliers, while suffering from poor adaptability to environmental noise. This makes them vulnerable to stealthy adversarial attacks and prone to high false positive rates. To address this challenge, we shift the defense paradigm from superficial output-level consensus to deeper consistency within the internal feature space. Guided by this principle, we propose Cerberus, a novel defense framework against adversarial attacks in CP systems by leveraging multi-dimensional consistency in the feature space. By quantifying conflicts in topological structure, semantic direction, and energy distribution within feature maps, Cerberus effectively detects adversarial perturbations and provides dynamic protection against adversarial attacks. Experimental results demonstrate that Cerberus significantly outperforms state-of-the-art methods, effectively limiting the attack success rate to as low as 0.05\% while restoring the AP to 0.88.

</details>

### 11. Non-Parametric Probabilistic Robustness: A Conservative Risk Estimator under Unknown Perturbation Distributions

📄 [arXiv](https://arxiv.org/abs/2511.17380) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62757)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial robustness`、`robust training`、`certification`、`adversarial defense`、`empirical evaluation`

👤 **作者**：Zheng Wang、Yi Zhang、Siddartha Khastgir、Carsten Maple、Xingyu Zhao

- 🎯 **研究动机**：概率鲁棒性（PR）假设扰动分布固定已知，现实不成立
- 🔬 **研究方法**：NPPR 按非参数范式直接从数据学习优化扰动分布做保守评估，GMM 估计器覆盖输入相关与无关扰动，理论建立 AR、PR 与 NPPR 关系
- 📌 **结论**：CIFAR-10/100 与 Tiny ImageNet 多架构上给出比假设常见扰动分布更保守（更低）的 PR 估计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning (DL) models, despite their remarkable success, remain vulnerable to small input perturbations that can cause erroneous outputs, motivating the recent proposal of probabilistic robustness (PR) as a complementary alternative to adversarial robustness (AR). However, existing PR formulations assume a fixed and known perturbation distribution, an unrealistic expectation in practice. To address this limitation, we propose non-parametric probabilistic robustness (NPPR), a more practical PR metric that does not rely on any predefined perturbation distribution. Following the non-parametric paradigm in statistical modeling, NPPR learns an optimized perturbation distribution directly from data, enabling conservative PR evaluation under distributional uncertainty. We further develop an NPPR estimator based on a Gaussian Mixture Model (GMM), covering various input-dependent and input-independent perturbation scenarios. Theoretical analyses establish the relationships among AR, PR, and NPPR. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny ImageNet across ResNet18/50, WideResNet50 and VGG16 validate NPPR as a more practical robustness metric, showing conservative (lower) PR estimates compared to assuming those common perturbation distributions used in state-of-the-arts.

</details>

### 12. Does a Hybrid Space-Aware Randomized Defense Improve Empirical and Certified Adversarial Robustness?

🎓 [Official](https://icml.cc/virtual/2026/poster/65726)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`certified robustness`、`adversarial robustness`、`robustness certification`

👤 **作者**：Joy Dhar、…、Pietro Li\u00f3

- 🎯 **研究动机**：l2 证书下的可证鲁棒性与强 l∞ 攻击下的经验鲁棒性之间存在长期鸿沟
- 🔬 **研究方法**：HySCAN 在训练与推理同时引入权重空间随机性（Random Weights）与特征空间随机性（Stochastic Attention Noise Injection）
- 📌 **结论**：多样影像数据集上认证鲁棒性最高提升约 9.6%、经验鲁棒性约 5%，不降干净精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Hybrid Space-aware Stochastic Convolution Attention Noise (HySCAN), a hybrid randomized defense that helps close the long-standing gap between provable robustness under ℓ2 certificates and empirical robustness against strong ℓ∞ attacks, while maintaining strong generalization across diverse imaging benchmarks. HySCAN jointly explores complementary sources of stochasticity at both training and inference: (i) implicit weight-space randomness via stochastic-aware Random Weights, and (ii) explicit feature-space randomness via Stochastic Attention Noise Injection modules. By incorporating randomness at both the parameter and representation levels, HySCAN enables meaningful certified guarantees while improving empirical robustness in practice. Comprehensive experiments on diverse imaging datasets, e.g., CelebA, CIFAR-10, and CIFAR-100, ImageNet-1k, HAM10000, and NIH Chest X-ray, demonstrate that HySCAN outperforms existing certified and empirical defenses, improving certified robustness by up to ≈ 9.6% and empirical robustness by up to ≈ 5% without reducing clean accuracy.

</details>

### 13. Certified Robustness under Heterogeneous Perturbations via Hybrid Randomized Smoothing

📄 [arXiv](https://arxiv.org/abs/2605.12876) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61695)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`certified robustness`、`adversarial robustness`、`robust training`、`adversarial defense`、`robustness certification`

👤 **作者**：Blaise Delattre、Hengyu Wu、Paul Caillon、Wei Yang Bryan Lim、Yang Cao

- 🎯 **研究动机**：随机平滑证书局限于单模态；多模态模型可被联合扰动异质输入，单模态证书不足
- 🔬 **研究方法**：基于联合 worst-case 的 Neyman-Pearson 公式化，分析分解噪声诱导的联合似然排序，得到闭式一维证书，严格推广 Gaussian 与离散随机平滑
- 📌 **结论**：提供首个文本-图像安全过滤中联合离散 token 与连续图像扰动的模型无关 Neyman-Pearson 证书

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Randomized smoothing provides strong, model-agnostic robustness certificates, but existing guarantees are limited to single modalities, treating continuous and discrete inputs in isolation. This limitation becomes critical in multimodal models, where decisions depend on cross-modal semantics and adversaries can jointly perturb heterogeneous inputs, rendering unimodal certificates insufficient. We introduce a unified randomized smoothing framework for mixed discrete--continuous inputs based on an analytically tractable Neyman--Pearson formulation of the joint worst-case problem. By analyzing the joint likelihood ordering induced by factorized discrete and continuous noise, our approach yields a closed-form, one-dimensional certificate that strictly generalizes both Gaussian (image-only) and discrete (text-only) randomized smoothing. We validate the framework on multimodal safety filtering, providing, to our knowledge, the first model-agnostic Neyman--Pearson certificate for joint discrete-token and continuous-image perturbations in interaction-dependent text--image safety filtering.

</details>

### 14. A Provable Energy-Guided Test-Time Defense Boosting Adversarial Robustness of Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.26984) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Mirza_A_Provable_Energy-Guided_Test-Time_Defense_Boosting_Adversarial_Robustness_of_Large_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`LVLM robustness`、`energy guidance`、`certified defense`

👤 **作者**：Mujtaba Hussain Mirza、Antonio D'Orazio、Odelia Melamed、Iacopo Masi

- 🎯 **研究动机**：LVLM 对对抗扰动高度敏感，对抗训练代价高，测试时变换成为推理期增强鲁棒性的途径
- 🔬 **研究方法**：提出 Energy-Guided Test-Time Transformation（ET3）：轻量、免训练的防御，通过最小化输入样本能量增强鲁棒性，并在合理假设下证明变换保持分类成功
- 📌 **结论**：在分类器、CLIP 零样本分类以及 Image Captioning 与 VQA 等 LVLM 任务上提供强防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the rapid progress in multimodal models and Large Visual-Language Models (LVLM), they remain highly susceptible to adversarial perturbations, raising serious concerns about their reliability in real-world use. While adversarial training has become the leading paradigm for building models that are robust to adversarial attacks, Test-Time Transformations (TTT) have emerged as a promising strategy to boost robustness at inference.In light of this, we propose Energy-Guided Test-Time Transformation (ET3), a lightweight, training-free defense that enhances the robustness by minimizing the energy of the input samples.Our method is grounded in a theory that proves our transformation succeeds in classification under reasonable assumptions. We present extensive experiments demonstrating that ET3 provides a strong defense for classifiers, zero-shot classification with CLIP, and also for boosting the robustness of LVLMs in tasks such as Image Captioning and Visual Question Answering. Code is available at github.com/OmnAI-Lab/Energy-Guided-Test-Time-Defense.

</details>

### 15. Certifiably Robust RAG against Retrieval Corruption

📄 [arXiv](https://arxiv.org/abs/2405.15556) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2024-05　🏷 SaTML 2026

**关键词**：`defense`、`RAG certification`、`bounded corruption`、`secure aggregation`、`RAG corruption`、`isolate-then-aggregate`

👤 **作者**：Chong Xiang、Tong Wu、Zexuan Zhong、David Wagner、Danqi Chen、Prateek Mittal

- 🎯 **研究动机**：RAG 易受检索腐化攻击，注入恶意段落即导致错误回答，缺乏可认证防御
- 🔬 **研究方法**：RobustRAG 采用 isolate-then-aggregate：把段落隔离分组分别生成回答，再用 keyword 与 decoding 两种算法安全聚合
- 📌 **结论**：首个可认证鲁棒的 RAG 防御，面对有界数量恶意段落注入仍能证明回答质量下界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. We propose RobustRAG, the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output. To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses. Notably, RobustRAG achieves certifiable robustness: for certain queries in our evaluation datasets, we can formally certify non-trivial lower bounds on response quality -- even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages. We evaluate RobustRAG on the tasks of open-domain question-answering and free-form long text generation and demonstrate its effectiveness across three datasets and three LLMs.

</details>

### 16. Probabilistic Robustness Certificates against Adversarial Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/62191)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`adversarial attack`、`adversarial robustness`、`robust training`、`certified robustness`

👤 **作者**：Sara Taheri、Majid Zamani

- 🎯 **研究动机**：现有防御缺形式保证或依赖模型族、威胁模型、投毒预算的受限假设，且忽视训练管线的随机性
- 🔬 **研究方法**：把梯度训练视为离散时间随机动力学系统，投毒鲁棒性形式化为安全验证，用 barrier certificates 导出对最坏 l_p 有界投毒的概率认证半径，经 scenario convex problem 得 PAC 保证
- 📌 **结论**：MNIST、SVHN、CIFAR-10 上给出随机训练下的形式鲁棒保证，模型无关且无需预知攻击策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing use of machine learning in safety-critical settings heightens vulnerability to *adversarial attacks*. Existing defense mechanisms typically either lack formal guarantees or depend on restrictive assumptions about the model family, the threat model, or the poisoning budget, and many only offer point-wise certification. Importantly, they often overlook the inherent stochasticity of modern training pipelines, which undermines their practical reliability. We introduce a probabilistic framework that views gradient-based training as a *discrete-time stochastic dynamical system* and formulates poisoning robustness as a safety verification task. Leveraging *barrier certificates* (BCs), we derive sufficient conditions to probabilistically certify a robust radius against worst-case ${\ell}_p$-bounded poisoning, guaranteeing that the final model parameters remain within a safe set. For tractable computation, we represent BCs with neural networks and obtain *probably approximately correct* (PAC) guarantees through a *scenario convex problem*. Our method identifies the largest certified radius for which the trained model is probabilistically accurate with a specified confidence level. Experiments on MNIST, SVHN, and CIFAR-10 show that our framework offers formal robustness guarantees under stochastic training, while being model-agnostic and not requiring prior knowledge of the attack strategy.

</details>

### 17. ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation

📄 [arXiv](https://arxiv.org/abs/2608.20122)　📅 2026-08

**关键词**：`defense`、`benchmark`、`adversarial OCR`、`privileged-observation distillation`、`GRPO`、`grounded adversarial OCR`

👤 **作者**：Linhan Cao、…、Wei Sun

- 🎯 **研究动机**：LMM 对抗视觉文本（人类可读但模型难定位识别）脆弱，对抗 OCR 评测缺规模、任务覆盖与区域感知
- 🔬 **研究方法**：把对抗 OCR 形式化为接地 OCR 感知；AdvSpot 基准 390 图区域级标注、5 类 13 种细粒度；ArmorOCR 两阶段：特权变换观察的 On-Policy Self-Distillation 加任务条件奖励的 GRPO
- 📌 **结论**：在 AdvSpot、其他对抗 OCR 与通用 OCR 基准上一致提升对抗 OCR 感知并保持竞争力通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable to humans but challenging for models to localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text, while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task and introduce \textbf{AdvSpot}, the first benchmark for grounded adversarial OCR evaluation. AdvSpot comprises 390 images with region-level annotations, spanning 5 primary categories and 13 fine-grained adversarial OCR types. To address this challenge, we propose \textbf{ArmorOCR}, a two-stage training framework for robust adversarial OCR perception. ArmorOCR first acquires missing adversarial OCR perception from privileged transformed observations through On-Policy Self-Distillation (OPSD), and then refines grounded OCR perception through Group Relative Policy Optimization (GRPO) with task-conditioned rewards for localization, recognition, full spotting, and visual question answering (VQA). Experiments on our AdvSpot, other adversarial OCR benchmarks, and general OCR benchmarks demonstrate that ArmorOCR consistently improves adversarial OCR perception while preserving competitive general OCR capability.

</details>

### 18. RoME: Robust Mixture of Low-Rank Experts against Multiple Adversarial Perturbations

📄 [arXiv](https://arxiv.org/abs/2607.06109) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5012)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`mixture of experts`、`adversarial robustness`、`robust training`、`multi-threat defense`、`adversarial training`

👤 **作者**：Woo Jae Kim、Kyle Min、Suhyeon Ha、Joonsung Jeon、Sung-eui Yoon

- 🎯 **研究动机**：多扰动对抗训练在不同威胁间存在鲁棒性权衡，朴素 MoE 又面临专家冗余捕获共享特征与门控威胁无关路由两大问题
- 🔬 **研究方法**：提出 RoME：每个专家是共享骨干上的低秩增量以捕获威胁共性，专家聚焦威胁特有信息；双尺度门控利用局部/全局特征判别信号，威胁引导门控多样化强制跨威胁的专家利用差异
- 📌 **结论**：在联合鲁棒性与自然准确率上超过现有 MAT SOTA，并对未见威胁提升鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-perturbation adversarial training (MAT) aims to achieve robustness against multiple $\ell_p$ perturbations but suffers from robustness trade-offs between different threats. To address this, we employ a mixture of experts (MoE) to route different threats through distinct model pathways. However, naive application of MoE encounters two critical challenges: experts tend to overlook threat-specific features and redundantly capture features shared across threats, and gating networks suffer from threat-agnostic routing where they learn nearly identical routing patterns across threats, thus preventing the construction of threat-specific model pathways. To this end, we propose Robust Mixture of Low-Rank Experts (RoME), where each expert is a low-rank additive update to the shared backbone, allowing it to capture threat-common features while experts focus on threat-specific information. To address threat-agnostic routing, RoME introduces (i) dual-scale gating that exploits threat-discriminative signals from local and global level features, and (ii) threat-guided gating diversification that enforces diverse expert utilization across threats. Extensive experiments demonstrate that RoME outperforms existing state-of-the-art MAT in union robustness and natural accuracy and improves robustness against unseen threats. Codes are available at https://github.com/wkim97/RoME.

</details>

### 19. AGFT: Alignment-Guided Fine-Tuning for Zero-Shot Adversarial Robustness of Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2603.29410) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_AGFT_Alignment-Guided_Fine-Tuning_for_Zero-Shot_Adversarial_Robustness_of_Vision-Language_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`vision-language model`、`zero-shot robustness`、`alignment tuning`

👤 **作者**：Yubo Cui、Xianchao Guan、Zijun Xiong、Zheng Zhang

- 🎯 **研究动机**：分类引导的对抗微调破坏预训练跨模态对齐，削弱视觉-文本对应与零样本性能
- 🔬 **研究方法**：AGFT 用原模型的概率预测做文本引导对抗训练，以软对齐分布把对抗视觉特征对齐文本嵌入，并用分布一致性校准匹配温度缩放的预训练预测
- 📌 **结论**：多个零样本基准上超越 SOTA 并显著提升零样本对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained vision-language models (VLMs) exhibit strong zero-shot generalization but remain vulnerable to adversarial perturbations. Existing classification-guided adversarial fine-tuning methods often disrupt pre-trained cross-modal alignment, weakening visual-textual correspondence and degrading zero-shot performance. In this paper, we propose an Alignment-Guided Fine-Tuning (AGFT) framework that enhances zero-shot adversarial robustness while preserving the cross-modal semantic structure. Unlike label-based methods that rely on hard labels and fail to maintain the relative relationships between image and text, AGFT leverages the probabilistic predictions of the original model for text-guided adversarial training, which aligns adversarial visual features with textual embeddings via soft alignment distributions, improving zero-shot adversarial robustness. To address structural discrepancies introduced by fine-tuning, we introduce a distribution consistency calibration mechanism that adjusts the robust model output to match a temperature-scaled version of the pre-trained model predictions. Extensive experiments across multiple zero-shot benchmarks demonstrate that AGFT outperforms state-of-the-art methods while significantly improving zero-shot adversarial robustness.

</details>

### 20. Unifying Adversarial Robustness and Training Across Text Scoring Models

📄 [arXiv](https://arxiv.org/abs/2602.00857) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61055)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial training`、`adversarial robustness`、`robustness certification`

👤 **作者**：Manveer Singh Tamber、Hosna Oyarhoseini、Jimmy Lin

- 🎯 **研究动机**：语言模型对抗鲁棒性研究碎片化地散落在各应用与攻击中，掩盖了共享漏洞
- 🔬 **研究方法**：统一研究 dense retriever、reranker 与奖励模型等文本打分模型的攻击与对抗训练——攻击成功即无关/被拒文本得分更高；提出多种对抗训练方法并组合使用
- 📌 **结论**：互补训练方法组合带来强鲁棒性并提升任务效果；对抗训练的奖励模型可缓解 RLHF 中的 reward hacking

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Research on adversarial robustness in language models is currently fragmented across applications and attacks, obscuring shared vulnerabilities. In this work, we propose unifying the study of adversarial robustness in text scoring models spanning dense retrievers, rerankers, and reward models. This motivates adapting both attacks and adversarial training methods across model roles. Unlike open-ended generation, text scoring failures are directly testable: an attack succeeds when an irrelevant or rejected text outscores a relevant or chosen one. Using this principled lens of text scoring, we demonstrate that current adversarial training formulations for language models are often short-sighted, failing to effectively generalize across attacks. To address this, we introduce multiple adversarial training methods for text scoring models and show that combining complementary training methods can yield strong robustness while also improving task effectiveness. We also highlight the practical value of our approach for RLHF, showing that our adversarially trained reward models mitigate reward hacking and support the training of better-aligned LLMs. We provide our code and models for further study.

</details>

### 21. Toward Understanding Adversarial Distillation: Why Robust Teachers Fail

📄 [arXiv](https://arxiv.org/abs/2605.21999) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63705)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`adversarial defense`、`adversarial robustness`、`robust training`、`adversarial training`、`robustness certification`

👤 **作者**：Hongsin Lee、Hye Won Chung

- 🎯 **研究动机**：对抗蒸馏中更鲁棒的教师常无法提升甚至损害学生鲁棒泛化，教师依赖机制不明
- 🔬 **研究方法**：识别 Robustly Unlearnable Set 上教师监督置信度与学生表征能力的错位；用两层网络理论证明教师对不可学样本高置信监督会迫使学生记忆虚假噪声导致鲁棒过拟合，高不确定性则抑制之
- 📌 **结论**：教师在不可学样本上的预测熵是学生鲁棒性的强指标，为鲁棒教师选择提供原则性指南；合成与真实图像实验验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial Distillation aims to enhance student robustness by guiding the student with a robust teacher's soft labels within the min-max adversarial training framework, yet its success is notoriously inconsistent: a more robust teacher often fails to improve, or even harms, the student's robust generalization. In this paper, we identify a key mechanism of this teacher dependency: the misalignment between the teacher's supervisory confidence and the student's representational limitations on a consistent subset of training data—the Robustly Unlearnable Set. We present a theoretical framework analyzing the feature learning dynamics of a two-layer neural network, demonstrating that this mismatch creates a dichotomy in distillation outcomes. We prove that when a teacher provides confident supervision on unlearnable samples, it compels the student to memorize spurious noise patterns that eventually overpower the learned robust signal, thereby driving robust overfitting. Conversely, a teacher that exhibits high uncertainty on these samples effectively suppresses noise memorization, allowing the student to rely solely on the learnable signal for robust generalization. We empirically validate our theory across both synthetic simulations and real-image classification datasets, confirming that robust overfitting is driven by the teacher's interaction with unlearnable samples. Finally, we demonstrate that a teacher's predictive entropy on unlearnable samples serves as a strong indicator of student robustness, validating our theoretical framework and offering a principled guideline for robust teacher selection.

</details>

### 22. Self-Calibrated Consistency can Fight Back for Adversarial Robustness in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2510.22785) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63826)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`analysis`、`adversarial defense`、`adversarial robustness`、`VLM safety`、`empirical evaluation`

👤 **作者**：Jiaxiang Liu、Jiawei Du、Xiao Liu、Prayag Tiwari、Mingkun Xu

- 🎯 **研究动机**：CLIP 等 VLM 对对抗扰动高度脆弱，现有防御依赖带标签的对抗微调，无法用于零样本场景；并指出当前攻击存在语义与视角脆弱性
- 🔬 **研究方法**：提出测试时防御 SCC：语义一致性用反攻击预热软伪标签与多视角预测正则跨模态对齐，空间一致性用增广视图稳定推理，即插即用
- 📌 **结论**：在 22 个基准多种攻击设定下持续提升 CLIP 零样本鲁棒性并保持精度，可迁移至 BioMedCLIP 等更广 VLM

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pre-trained vision-language models (VLMs) such as CLIP have demonstrated strong zero-shot capabilities across diverse domains, yet remain highly vulnerable to adversarial perturbations that disrupt image-text alignment and compromise reliability. Existing defenses typically rely on adversarial fine-tuning with labeled data, limiting their applicability in zero-shot settings. In this work, we identify two key weaknesses of current CLIP adversarial attacks—lack of semantic guidance and vulnerability to view variations—collectively termed semantic and viewpoint fragility. To address these challenges, we propose Self-Calibrated Consistency (SCC), an effective test-time defense. SCC consists of two complementary modules: Semantic consistency, which leverages soft pseudo-labels from counterattack warm-up and multi-view predictions to regularize cross-modal alignment and separate the target embedding from confusable negatives; and Spatial consistency, aligning perturbed visual predictions via augmented views to stabilize inference under adversarial perturbations. Together, these modules form a plug-and-play inference strategy. Extensive experiments on 22 benchmarks under diverse attack settings show that SCC consistently improves the zero-shot robustness of CLIP while maintaining accuracy, and can be seamlessly integrated with other VLMs for further gains. These findings highlight the great potential of establishing an adversarially robust paradigm from CLIP, with implications extending to broader VLMs such as BioMedCLIP.

</details>

### 23. Posterior Mismatch Matters: Adversarial Training for Long-Tailed Robustness

🎓 [Official](https://icml.cc/virtual/2026/poster/64623)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial training`、`adversarial robustness`、`robustness certification`

👤 **作者**：Lilin Zhang、Li Yue、Jiancheng Shi、Jiancheng Lv、Xianggen Liu

- 🎯 **研究动机**：长尾对抗训练退化的关键是后验失配：粗粒度绝对标签把类后验塌缩成点估计致频率估计偏差与鲁棒泛化 gap 扩大
- 🔬 **研究方法**：PAT 学后验代理提供细粒度概率监督并整合权重扰动鼓励平坦损失景观；理论证明准确后验同时收紧频率估计误差与鲁棒泛化界
- 📌 **结论**：长尾基准上鲁棒性一致提升，最差类增益尤大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial training breaks down in long-tailed settings, exhibiting severe robustness degradation on worst-performing (often tail) classes. We identify a key cause of this failure as a posterior mismatch: coarse-grained absolute labels collapse class posteriors into point estimates, leading to biased class-frequency estimation and an enlarged robust generalization gap, which ultimately amplifies worst-class vulnerability. To address this issue, we propose Posterior-driven Adversarial Training (PAT), which learns a posterior surrogate to provide fine-grained probabilistic supervision for adversarial training, and integrates weight perturbations to encourage a flatter loss landscape. Our theory shows that accurate posterior approximation simultaneously tightens class-frequency estimation error and robust generalization bounds, while a flat weight loss landscape stabilizes sensitivity to posterior approximation errors. Extensive experiments on long-tailed benchmarks confirm that PAT consistently improves robustness, with especially large gains on worst-class.

</details>

### 24. On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression

📄 [arXiv](https://arxiv.org/abs/2601.21531) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61440)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial robustness`、`VLM safety`、`empirical evaluation`、`robustness certification`

👤 **作者**：Xinwei Zhang、…、Haibo Hu

- 🎯 **研究动机**：视觉 token 剪枝或合并的对抗鲁棒性未探，编码器攻击存在优化-推理失配：全 token 上优化却经压缩瓶颈推理
- 🔬 **研究方法**：CAGE 不需知道部署压缩机制或预算：期望特征破坏把失真集中于可能存活的 token，秩失真对齐使高失真 token 更易被保留
- 📌 **结论**：多种即插即用压缩机制与数据集上鲁棒准确率一致低于基线，忽略压缩的鲁棒评估过于乐观

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. We show that existing encoder-based attacks cannot fully disclose the robustness vulnerabilities of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. To address this gap, we propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget. CAGE combines (i) expected feature disruption, which concentrates distortion on tokens likely to survive across plausible budgets, and (ii) rank distortion alignment, which actively aligns token distortions with rank scores to promote the retention of highly distorted evidence. Across diverse representative plug-and-play compression mechanisms and datasets, our results show that CAGEconsistently achieves lower robust accuracy than the baseline. This work highlights that robustness assessments ignoring compression can be overly optimistic, calling for compression-aware security evaluation and defenses for efficient LVLMs.

</details>

### 25. Benign Overfitting in Adversarial Training for Vision Transformers

📄 [arXiv](https://arxiv.org/abs/2604.19724) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62410)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial training`、`adversarial robustness`、`robustness certification`

👤 **作者**：Jiaming Zhang、Meng Ding、Shaopeng Fu、Jingfeng Zhang、Di Wang

- 🎯 **研究动机**：ViT 对抗训练的鲁棒性理论基础 largely 未被探索
- 🔬 **研究方法**：在简化 ViT 架构下首次理论分析：信噪比满足特定条件且扰动预算适中时，对抗训练使 ViT 取得近零的鲁棒训练损失与鲁棒泛化误差
- 📌 **结论**：即使过拟合也能强泛化（benign overfitting），此前只在 CNN 对抗训练中观察到；合成与真实数据均验证理论

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the remarkable success of Vision Transformers (ViTs) across a wide range of vision tasks, recent studies have revealed that they remain vulnerable to adversarial examples, much like Convolutional Neural Networks (CNNs). A common empirical defense strategy is adversarial training, yet the theoretical underpinnings of its robustness in ViTs remain largely unexplored. In this work, we present the first theoretical analysis of adversarial training under simplified ViT architectures. We show that, when trained under a signal-to-noise ratio that satisfies a certain condition and within a moderate perturbation budget, adversarial training enables ViTs to achieve nearly zero robust training loss and robust generalization error under certain regimes. Remarkably, this leads to strong generalization even in the presence of overfitting, a phenomenon known as benign overfitting, previously only observed in CNNs (with adversarial training). Experiments on both synthetic and real-world datasets further validate our theoretical findings.

</details>

### 26. Adversarial Training for Process Reward Models

📄 [arXiv](https://arxiv.org/abs/2511.22888) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66402)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial training`、`adversarial robustness`、`robustness certification`

👤 **作者**：Gurusha Juneja、Deepak Nathani、William Yang Wang

- 🎯 **研究动机**：过程奖励模型受制于昂贵的人工步骤级标注，且静态训练数据对新型错误泛化差
- 🔬 **研究方法**：提出对抗训练的 APRM：生成器 G 学习产生欺骗 PRM 的推理错误，PRM R 同时学习检测，交互产生渐进更难的负样本，无需人工步骤级标签
- 📌 **结论**：跨数学推理基准平均把求解器准确率提升 3.4 个百分点（超最强 PRM 基线），OOD 任务增益 5.3 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Process Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision. However, their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors. We introduce Adversarially Trained PRMs (APRM), where a Generator ($G$) learns to produce reasoning errors to deceive a PRM ($R$), while $R$ concurrently learns to detect them. This interaction yields progressively harder negatives for $R$, improving it's robustness and generalization to novel errors without requiring manual step-level labels. Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by $+3.4$ percentage points (pp) over the strongest PRM baseline. APRM achieves gains of $+5.3$ pp on out-of-distribution tasks.

</details>

### 27. Adversarial Attack and Defense for Denoising Diffusion Sampling

🎓 [Official](https://icml.cc/virtual/2026/poster/62015)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial attack`、`diffusion model`、`adversarial robustness`、`attack transferability`

👤 **作者**：Zhao-Rong Lai、Xiwen Yuan、Jian Weng

- 🎯 **研究动机**：denoising diffusion sampling（DDS）生成的样本分布可被甚至高斯扰动显著破坏，攻防方法论缺失
- 🔬 **研究方法**：攻击侧在采样阶段注入扰动严重恶化样本生成；防御侧为势函数最小化提出局部变化正则以容忍扰动，并开发共轭梯度算法结合零阶拒绝采样降低计算成本
- 📌 **结论**：所提攻击显著恶化现有 SOTA 方法，而局部变化正则可有效防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Denoising diffusion sampling (DDS) is an emerging approach for generating new samples that have the same distribution as some training samples. However, it is vulnerable to adversarial attacks by even a Gaussian perturbation. In this work, we propose a complete set of adversarial attack and defense methodology for DDS. In the attack side, we propose to inject a perturbation to the sampling stage, which significantly worsen the performance of sample generation. In the defense side, we propose a local variation based regularization model for the potential function minimization, which effectively tolerates the adversarial perturbations. Moreover, we develop a conjugate gradient algorithm to solve the defense model, which integrates with a recently-developed zeroth order rejection sampling method that saves computational cost. Experimental results show that the proposed attack significantly worsen the existing state-of-the-art methods, but can be defended by the proposed local variation regularization.

</details>

### 28. AntiStyler: Defending Object Detection Models Against Adversarial Patch Attacks Using Style Removal

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yankelev_AntiStyler_Defending_Object_Detection_Models_Against_Adversarial_Patch_Attacks_Using_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`object detector`、`adversarial patch`、`style removal`

👤 **作者**：Idan Yankelev、…、Asaf Shabtai

- 🎯 **研究动机**：对抗补丁防御常在良性图像上掉点，且处理速度无法满足实时目标检测
- 🔬 **研究方法**：AntiStyler 识别并遮蔽呈随机风格的对抗像素，经空间滤波器增强遮罩去噪；免训练且模型、补丁、攻击均无关的零样本防御
- 📌 **结论**：COCO、INRIA、Superstore、APRICOT 上对抗性能提升 8 至 15 mAP，良性性能不降，处理速度 10 至 12 FPS 支持实时应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial patch attacks pose a significant threat to the reliability of object detection (OD) models, particularly in real-time security applications. Although several defenses have been proposed, they often suffer from two limitations: 1) reduced performance on benign images, and 2) impractical processing time for real-time OD applications. In this paper, we present AntiStyler, a novel and rapid defense against adversarial patches. Given an input image, AntiStyler identifies and masks pixels that exhibit a "random" style associated with adversarial attacks and uses a series of spatial filters to enhance the mask and remove unwanted noise, efficiently masking adversarial patches. AntiStyler features model-, patch-, and attack-agnostic capabilities and does not require any training, making it a fully agnostic zero-shot defense against adversarial patch attacks. Our evaluation on the COCO, INRIA, Superstore, and APRICOT datasets, with both digital and physical attacks, demonstrates AntiStyler's state-of-the-art robustness (improving adversarial performance by 8-15 mAP%) without compromising the original performance on benign images. Additionally, unlike most existing defenses, AntiStyler can process 10-12 frames per second (FPS), making it efficient and relevant for real-time OD applications.

</details>

### 29. Band Together: Untargeted Adversarial Training with Multimodal Coordination Against Evasion-Based Promotion Attacks

📄 [arXiv](https://arxiv.org/abs/2605.06238) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1759.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`multimodal recommender`、`promotion attack`、`adversarial training`

👤 **作者**：Guanmeng Xian、Ning Yang、Philip S. Yu

- 🎯 **研究动机**：多模态推荐系统的防御局限于单模态与投毒式威胁；多用户推广下视觉与文本扰动方向不一致的跨模态梯度失配会稀释攻击并使鲁棒训练低估风险
- 🔬 **研究方法**：UAT-MC 无目标对抗训练把所有条目视为潜在目标，并引入梯度对齐机制显式纠正失配，保证跨模态扰动同步以最大化对抗强度
- 📌 **结论**：显著提升对推广攻击的鲁棒性，同时在防御-精度权衡下保持可接受的推荐性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

multimodal recommender systems exploit visual and textual signals to alleviate data sparsity, but this also makes them more vulnerable to evasionbased promotion attacks. Existing defenses are largely limited to single-modal settings and mainly focus on poisoning-based threats, leaving evasionbased threats underexplored. In this work, we first identify a cross-modal gradient mismatch under the multi-user promotion setting, where visual and textual perturbations are optimized in inconsistent directions due to the dominance of distinct user groups. This phenomenon dilutes the attack effectiveness and leads robust training to underestimate worst-case risks. To address this issue, we propose Untargeted Adversarial Training with multimodal Coordination (UAT-MC). UATMC tackles the challenge of unknown targeted items in evasion-based attacks (as opposed to poisoning-based attacks) by treating all items as potential targets, and introduces a gradient alignment mechanism to explicitly correct this mismatch. This design ensures synchronized perturbations across modalities, thereby maximizing adversarial strength for robust training. Extensive experiments demonstrate that UAT-MC significantly improves robustness against promotion attacks while maintaining acceptable recommendation performance under the defense–accuracy trade-off. Code is available at https://github.com/ gmXian/UAT-MC.

</details>

### 30. From Standard to Robust: A Universal Framework for Continual Adversarial Defense

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2065.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`continual adversarial defense`、`few-shot adaptation`、`attack evolution`

- 🎯 **研究动机**：持续对抗防御方法依赖大量重放数据或多个专家模块，或鲁棒性与干净性能下降，难超独立鲁棒模型
- 🔬 **研究方法**：提出持续适应不遗忘、少样本、省内存、干净与对抗数据均高准确四原则，整合持续学习、少样本与集成学习构建 UCAD 框架
- 📌 **结论**：多阶段攻击下显著超各类基线；遇到的攻击越多越鲁棒，持续增强现有鲁棒模型直至饱和

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual adversarial defense (CAD) aims to defend target models against continuously emerging attacks. However, existing CAD methods typically rely on maintaining large amounts of replay data or multiple expert modules to mitigate catastrophic forgetting, or suffer from reduced robustness against adversarial examples or degraded performance on clean images. As a result, they often fail to provide clear advantages over standalone robust models. To address these limitations, we formulate four fundamental principles for CAD: (1) continual adaptation to new attacks without catastrophic forgetting, (2) few-shot adaptation, (3) memory-efficient adaptation, and (4) high classification accuracy on both clean and adversarial data. Guided by these principles, we explore and integrate cutting-edge techniques from continual learning, few-shot learning, and ensemble learning, and propose Universal Continual Adversarial Defense (UCAD), a universal framework that enables both standard and robust models to perform effective defense under the CAD setting. Extensive experiments validate the effectiveness of UCAD against multi-stage adversarial attacks and demonstrate significant improvements over a wide range of baseline methods. Moreover, we observe that as the number of encountered attacks increases, UCAD becomes increasingly robust, consistently enhancing the defense capability of existing robust models until saturation.

</details>

### 31. Manifold-Constrained Adversarial Training for Long-Tailed Robustness via Geometric Alignment

📄 [arXiv](https://arxiv.org/abs/2605.02183) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/1379.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`adversarial training`、`long-tailed data`、`manifold constraint`

👤 **作者**：Guanmeng Xian、Ning Yang、Philip S. Yu

- 🎯 **研究动机**：对抗训练在长尾分布下鲁棒性退化，尾部类鲁棒误差高且决策边界不稳
- 🔬 **研究方法**：MCAT 惩罚偏离类条件流形保证对抗样本语义有效，并用 ETF 启发正则促进类间平衡几何分离；理论联系几何分离与鲁棒间隔下界
- 📌 **结论**：长尾基准上整体、平衡与尾类对抗鲁棒性一致提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial training is effective on balanced datasets, but its robustness degrades under longtailed class distributions, where tail classes suffer high robust error and unstable decision boundaries. We propose Manifold-Constrained Adversarial Training (MCAT), a unified framework that enforces the semantic validity of adversarial examples by penalizing deviations from class-conditional manifolds in feature space, while promoting balanced geometric separation across classes via an ETF-inspired regularization. We provide theoretical results that link geometric separation to lower bounds on adversarially robust margins, and show that manifold-constrained adversarial risk upperbounds robust risk on high-density semantic regions. Extensive experiments on standard longtailed benchmarks demonstrate consistent improvements in overall, balanced, and tail-class adversarial robustness. The codes and appendix are available on https://github.com/yneversky/MCAT.

</details>

### 32. Efficient Semi-Supervised Adversarial Training via Latent Clustering-Based Data Reduction

📄 [arXiv](https://arxiv.org/abs/2501.10466) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-01　🏷 SaTML 2026

**关键词**：`defense`、`adversarial training`、`latent clustering`、`data reduction`

👤 **作者**：Somrita Ghosh、Yuelin Xu、Xiao Zhang

- 🎯 **研究动机**：半监督对抗训练需大量额外数据，训练久、内存开销高
- 🔬 **研究方法**：用潜空间聚类选择或生成决策边界附近的小关键子集，并保持边界与非边界数据平衡以防过拟合
- 📌 **结论**：以 5-10 倍少的无标签数据达到几乎相同的鲁棒精度，总运行时间缩短约 3-4 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Learning robust models under adversarial settings is widely recognized as requiring a considerably large number of training samples. Recent work proposes semi-supervised adversarial training (SSAT), which utilizes external unlabeled or synthetically generated data and is currently the state of the art. However, SSAT requires substantial extra data to attain high robustness, resulting in prolonged training time and increased memory usage. In this paper, we propose data reduction strategies to improve the efficiency of SSAT by optimizing the amount of additional data incorporated. Specifically, we design novel latent clustering-based techniques to select or generate a small, critical subset of data samples near the model's decision boundary. While focusing on boundary-adjacent points, our methods maintain a balanced ratio between boundary and non-boundary data points, thereby avoiding overfitting. Comprehensive experiments across image benchmarks demonstrate that our methods can effectively reduce SSAT's data requirements and computational costs while preserving its strong robustness advantages. In particular, our latent-space selection scheme based on k-means clustering and our guided diffusion-based approach with LCG-KM are the most effective, achieving nearly identical robust accuracies with 5 times to 10 times less unlabeled data. When compared to full SSAT trained to convergence, our methods reduce total runtime by approximately 3 times to 4 times due to strategic prioritization of unlabeled data.

</details>

### 33. Two Modalities Are Better Than One: Efficient Adversarial Purification via Multimodal Diffusion Models

🎓 [Official](https://icml.cc/virtual/2026/poster/61378)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial robustness`、`VLM safety`、`adversarial training`、`robustness certification`

👤 **作者**：Mingyuan Bai、…、Qibin Zhao

- 🎯 **研究动机**：单模态扩散净化难以保持语义一致，多模态变体依赖昂贵的对抗训练或蒸馏，且均缺理论保证
- 🔬 **研究方法**：提出 MultiDAP：从干净数据学习连续类无关 prompt 捕获语义先验，在其引导下以少量步数（5-20 步）最小化正则化 DDPM 损失完成净化，并给出似然改进与收敛的理论保证
- 📌 **结论**：在 CIFAR-10、CIFAR-100 与 ImageNet-1K 上匹配 SOTA 鲁棒性且效率更高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial purification uses generative models to restore clean data distributions from unseen attacks without retraining classifiers. However, unimodal diffusion-based approaches struggle to preserve semantic consistency, while recent multimodal variants rely on computationally expensive adversarial training or distillation. Both approaches often lack theoretical guarantees. In this work, we propose MultiDAP, a novel framework leveraging multimodal diffusion models for efficient adversarial purification. MultiDAP first learns continuous class-agnostic prompts from clean data to capture rich semantic priors, replacing rigid hand-crafted templates. Guided by these prompts, MultiDAP purifies adversarial inputs by minimizing a regularized DDPM loss for only a few steps (e.g., 5-20). We provide theoretical guarantees for both the likelihood improvement via prompt learning and the convergence of the purification process. Extensive experiments on CIFAR-10, CIFAR-100, and ImageNet-1K demonstrate that MultiDAP matches the robustness of state-of-the-art baselines but with improved efficiency.

</details>

### 34. Training-Free Adversarial Robustness in Computational MRI

📄 [arXiv](https://arxiv.org/abs/2501.01908) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64452)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial robustness`、`robust training`、`empirical evaluation`、`robustness certification`

👤 **作者**：Mahdi Saberi、Chi Zhang、Mehmet Akçakaya

- 🎯 **研究动机**：深度 MRI 重建模型易受小对抗扰动影响产生严重畸变，现有缓解方法均需重训练
- 🔬 **研究方法**：基于循环测量一致性构造缓解目标并在攻击输入小邻域内最小化，免重训练；并建模原始数据脉冲噪声（鲱鱼骨伪影）场景
- 📌 **结论**：跨数据集、攻击类型/强度与 PD-DL 网络显著降低扰动影响，盲攻击与自适应攻击设置下依然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning (DL) methods have become the state-of-the-art for reconstructing sub-sampled magnetic resonance imaging (MRI) data. However, studies have shown that these methods are susceptible to small adversarial input perturbations, resulting in major distortions in the output images. Various strategies have been proposed to reduce the effects of these attacks, but they require retraining. In this work, we propose a novel approach for mitigating adversarial attacks on MRI reconstruction models without any retraining. Based on the idea of cyclic measurement consistency, we devise a novel mitigation objective that is minimized in a small ball around the attack input. Results show that our method substantially reduces the impact of adversarial perturbations across different datasets, attack types/strengths and PD-DL networks, and qualitatively and quantitatively outperforms conventional mitigation methods. We also introduce a practically relevant scenario for small adversarial perturbations that models impulse noise in raw data, which relates to herringbone artifacts, and show the applicability of our approach in this setting. Finally, we show our mitigation approach remains effective in two realistic extension scenarios: a blind setup, where the attack strength or algorithm is not known to the user; and an adaptive attack setup, where the attacker has full knowledge of the defense strategy. Code available at: https://github.com/MahdiSaberii/CycMit-MRI

</details>

### 35. SS-TPT: Stability and Suitability-Guided Test-Time Prompt Tuning for Adversarially Robust Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2606.06943) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63418)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial robustness`、`VLM safety`、`robust training`、`adversarial defense`、`inference-time intervention`

👤 **作者**：Sunoh Kim、Daeho Um

- 🎯 **研究动机**：CLIP 零样本识别在对抗扰动下脆弱，现有测试时适应防御依赖大量增广视图导致严重减速与鲁棒-吞吐折中
- 🔬 **研究方法**：提出 SS-TPT：用稳定性（弱增广预测不变性）与适切性（视图特征密度）两个分数评估增广视图质量，经 SS 一致性损失与 SS 加权预测放大可信视图、抑制受损视图
- 📌 **结论**：显著超越先前 SOTA，在多样数据集与视图数下取得更优的鲁棒-吞吐折中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) such as CLIP achieve strong zero-shot recognition but remain highly fragile under adversarial perturbations. Recent test-time adaptation defenses improve robustness by leveraging many augmented views, but this leads to impractical slowdown and a clear robustness-throughput trade-off. To address this challenge, we present Stability and Suitability-guided Test-time Prompt Tuning (SS-TPT), evaluating the quality of each augmented view via two complementary scores: (1) stability, measuring prediction invariance to weak augmentations, and (2) suitability, measuring feature-space density among views. These stability and suitability (SS) scores guide both adaptation and inference through an SS-guided consistency loss and an SS-weighted prediction, amplifying trustworthy views while suppressing corrupted ones. Extensive experiments demonstrate that SS-TPT significantly outperforms prior state-of-the-art methods, achieving superior robustness-throughput trade-offs across diverse datasets and varying numbers of views, thereby demonstrating both strong practicality and generality. Our code is available at https://github.com/sunoh-kim/SS-TPT.

</details>

### 36. Contrastive Spectral Rectification: Test-Time Defense towards Zero-shot Adversarial Robustness of CLIP

📄 [arXiv](https://arxiv.org/abs/2601.19210) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61655)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial defense`、`adversarial robustness`、`robust training`、`contrastive learning`、`robustness certification`

👤 **作者**：Sen Nie、Jie Zhang、Zhuo Wang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：现有测试时防御对强攻击鲁棒性不足，且推理延迟高、任务特定
- 🔬 **研究方法**：发现对抗样本在渐进频率衰减下呈严重特征不一致（源于模型谱偏置）；CSR 优化矫正扰动在谱引导对比目标下把输入重新对齐自然流形，输入自适应应用
- 📌 **结论**：16 个分类基准上对强 APGD 平均超 SOTA 18.1%，推理开销适中且适用广泛视觉任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models (VLMs) such as CLIP have demonstrated remarkable zero-shot generalization, yet remain highly vulnerable to adversarial examples (AEs). While test-time defenses are promising, existing methods fail to provide sufficient robustness against strong attacks and are often hampered by high inference latency and task-specific applicability. To address these limitations, we start by investigating the intrinsic properties of AEs, which reveals that AEs exhibit severe feature inconsistency under progressive frequency attenuation. We further attribute this to the model's inherent spectral bias. Leveraging this insight, we propose an efficient test-time defense named Contrastive Spectral Rectification (CSR). CSR optimizes a rectification perturbation to realign the input with the natural manifold under a spectral-guided contrastive objective, which is applied input-adaptively. Extensive experiments across 16 classification benchmarks demonstrate that CSR outperforms the SOTA by an average of 18.1% against strong APGD with modest inference overhead. Furthermore, CSR exhibits broad applicability across diverse visual tasks. Code is available at https://github.com/Summu77/CSR.

</details>

### 37. Adversarial Patch EXterminator: Zero-Shot and Patch-Agnostic Defense Framework Against Adversarial Patch Attacks

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-jiayimei)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`adversarial patch`、`adversarial robustness`、`robust training`、`zero-shot localization`、`image inpainting`

👤 **作者**：Jiayimei Wang、Tao Ni、Guowen Xu、Qingchuan Zhao、Cong Wang

- 🎯 **研究动机**：现有对抗 patch 防御依赖先验知识或大量训练数据，对微小、不规则或背景高度一致的 patch 防护不足，物理条件变化下稳健性差
- 🔬 **研究方法**：提出零样本、patch 无关的三阶段防御 APEX：边界框提取聚焦 patch 区域，互信息模糊热图加边缘感知边界热图定位对抗区域，结构引导图像修复还原图像
- 📌 **结论**：有效防御非自然、自然与红外等多类对抗 patch，定位能力优异，在光照变化与物理场景中保持高鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial patch attacks pose a serious threat to modern computer vision systems. Although existing defense solutions attempt to mitigate such attacks by developing certifiable models or patch identification pipelines, they generally rely on prior knowledge or extensive training data, show insufficient robustness across varying physical conditions, and present limited performance against challenging cases (e.g., tiny, irregular, or highly background-coherent patches). To address such limitations, we propose APEX, a zero-shot, patch-agnostic three-stage adversarial patch defense framework. Specifically, APEX first concentrates patch regions through bounding-box extraction, then integrates a mutual information-based blur heatmap with an edge-aware boundary heatmap to locate adversarial regions, and finally leverages structure-guided image inpainting to restore the image. Our experiments on multiple datasets and existing state-of-the-art defense methods demonstrate that APEX can effectively defend against various types of adversarial patches (e.g., non-naturalistic, naturalistic, and infrared images). In addition, APEX shows superior capability in patch localization, maintains high robustness against varying environments (e.g., lighting conditions) and extreme cases, and also demonstrates high performance in protecting various models in physical-world scenarios.

</details>

### 38. When CLIP Sees More, It Fights Back Harder: Multi-View Guided Adaptive Counterattacks for Test-Time Adversarial Robustness

📄 [arXiv](https://arxiv.org/abs/2606.06938) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_When_CLIP_Sees_More_It_Fights_Back_Harder_Multi-View_Guided_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`CLIP`、`multi-view probe`、`adaptive counterattack`

👤 **作者**：Sunoh Kim、Daeho Um

- 🎯 **研究动机**：测试时反攻击（TTC）依赖被污染的原始视图与噪声驱动硬门控，在强攻击下脆弱
- 🔬 **研究方法**：提出 MAC：构造输入增广视图获得多样嵌入，对各视图反攻击并按估计污染度自适应缩放强度，聚合得鲁棒预测；免调优设计
- 📌 **结论**：20 个数据集与多样攻击场景下显著提升鲁棒性，同时保持高推理速度与内存效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language models such as CLIP have achieved remarkable zero-shot recognition capabilities, yet their robustness against adversarial perturbations remains limited. Test-time counterattack (TTC) was recently proposed to improve CLIP's robustness by perturbing an input image to steer it away from a corrupted state during inference. However, TTC remains fragile under strong attacks because its counterattack relies on a directly corrupted original view and employs a noise-driven hard-gating scheme that cannot adapt to varying corruption severity. To address these limitations, we introduce Multi-view guided Adaptive Counterattack (MAC), which performs counterattacks for multi-view with corruption-aware soft weighting. Specifically, MAC first constructs augmented views of an input image to obtain diverse embeddings. It then performs counterattacks to refine corrupted embeddings of views. Next, MAC adaptively scales the counterattack intensity for each view based on its estimated corruption degree. Finally, the adaptively counterattacked views are aggregated to yield a robust final prediction. Extensive experiments across 20 datasets and diverse attack scenarios demonstrate that MAC substantially improves robustness while preserving high inference speed and memory efficiency with its tuning-free design. Our code is available at https://github.com/sunoh-kim/MAC.

</details>

### 39. MonoPure: Multi-Component Purification via Disentangled, Projective Representations for Monocular 3D Object Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/987.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`monocular 3D detection`、`multi-component attack`、`calibration purification`

- 🎯 **研究动机**：单目 3D 检测脆弱于同时扰动图像与相机标定的多组件攻击，复合失真破坏 3D-2D 对应
- 🔬 **研究方法**：MonoPure 用目标区域概率图引导扩散净化聚焦任务区域，2D 骨架关键点做遮挡鲁棒检测，投影标定净化模块迭代最小化重投影误差恢复内参
- 📌 **结论**：多组件攻击与遮挡下优于先前检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Monocular 3D object detection is a cost-efficient alternative to multisensor systems, yet it remains fragile to multi-component adversarial attacks that perturb the image and tamper with camera calibration. Compounded distortions degrade 3D reasoning by disrupting the correspondence between the 3D geometry and 2D image plane. To address this problem, this work proposes MonoPure, a monocular 3D object detection framework that performs multi-component purification via disentangled and projective representations. MonoPure incorporates a disentangled purification and segmentation module that purifies the image data, with a target-region probability map steering diffusion-based purification to focus on task-relevant regions. In addition, MonoPure presents a 3D detection decoder that integrates 2D skeleton keypoints as object-level spatial cues, enabling occlusion-robust 3D detection. Finally, a projective calib-purification module restores compromised intrinsics by iteratively minimizing the reprojection error between projected 3D boxes and calibration-invariant 2D detection boxes. The experiments confirm that MonoPure outperforms prior detectors under multi-component attacks and occlusion.

</details>

### 40. Parameter-Efficient Dual-Loss Adaptation with Logit Divergence: A Unified Approach for Adversarial Example Detection and Robust Inference

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6748.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`adversarial detection`、`robust inference`、`adapter divergence`

- 🎯 **研究动机**：对抗样本检测与鲁棒推理通常割裂，且需外部检测器
- 🔬 **研究方法**：D3Adapter 在冻结骨干上挂轻量适配器库，双损失与互补目标训练出有意不同的 logit 行为；推理时以适配器间 logit 分歧作威胁评分并选适配器输出
- 📌 **结论**：迁移与自适应白盒攻击下单次前向统一检测与鲁棒推理，开销随适配器数量可预测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present D3Adapter, a threat-aware framework that unifies adversarial example detection (AED) and robust inference. D3Adapter attaches a small library of lightweight adapters to a frozen ResNet backbone; the adapters are trained under two loss functions (cross-entropy and optimized reverse cross-entropy) and complementary objectives (clean training and adversarial training), yielding intentionally distinct logit behaviors. During inference, D3Adapter quantifies inter-adapter logit divergence to produce an agreement-based threat score without any external detector for AED. The same pass also performs robust inference by outputting prediction from the selected adapter when an adversarial example is detected, therefore unifying detection and defense into single-pass forward computation. We evaluate D3Adapter under transfer-based and adaptive white-box attacks, and we study scalability across datasets with varying numbers of classes, showing that unified detection and robust inference can be achieved with predictable overhead proportional to the number of adapters.

</details>

### 41. TTP: Test-Time Padding for Adversarial Detection and Robust Adaptation on Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2512.16523) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_TTP_Test-Time_Padding_for_Adversarial_Detection_and_Robust_Adaptation_on_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`defense`、`VLM attack detection`、`test-time adaptation`、`padding probe`

👤 **作者**：Zhiwei Li、Yitian Pang、Weining Wang、Zhenan Sun、Qi Li

- 🎯 **研究动机**：训练时对抗防御需标注数据与重训，现有测试时策略又难以可靠区分干净与对抗输入
- 🔬 **研究方法**：Test-Time Padding 以空间 padding 前后 CLIP 特征的余弦相似度偏移做跨架构通用阈值检测，对检出样本用可训练 padding 恢复注意力并结合相似度感知集成，干净输入默认不动
- 📌 **结论**：在多 CLIP 骨干与细粒度基准上超越 SOTA 测试时防御，对抗鲁棒性大幅提升且不损 clean 精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs), such as CLIP, have achieved impressive zero-shot recognition performance but remain highly susceptible to adversarial perturbations, posing significant risks in safety-critical scenarios. Previous training-time defenses rely on adversarial fine-tuning, which requires labeled data and costly retraining, while existing test-time strategies fail to reliably distinguish between clean and adversarial inputs, thereby preventing both adversarial robustness and clean accuracy from reaching their optimum. To address these limitations, we propose Test-Time Padding (TTP), a lightweight defense framework that performs adversarial detection followed by targeted adaptation at inference. TTP identifies adversarial inputs via the cosine similarity shift between CLIP feature embeddings computed before and after spatial padding, yielding a universal threshold for reliable detection across architectures and datasets. For detected adversarial cases, TTP employs trainable padding to restore disrupted attention patterns, coupled with a similarity-aware ensemble strategy for a more robust final prediction. For clean inputs, TTP leaves them unchanged by default or optionally integrates existing test-time adaptation techniques for further accuracy gains. Comprehensive experiments on diverse CLIP backbones and fine-grained benchmarks show that TTP consistently surpasses state-of-the-art test-time defenses, delivering substantial improvements in adversarial robustness without compromising clean accuracy. The code for this paper will be released soon.

</details>

### 42. Provably Safe Model Updates

📄 [arXiv](https://arxiv.org/abs/2512.01899) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-12　🏷 SaTML 2026

**关键词**：`defense`、`safe update`、`parameter certification`、`alignment drift`

👤 **作者**：Leo Elmecker-Plakolm、Pierre Fasterling、Philip Sosnin、Calvin Tsay、Matthew Wicker

- 🎯 **研究动机**：正则化与参数隔离等启发式方法可缓解灾难性遗忘或对齐漂移，但无法认证更新后模型仍满足性能规约
- 🔬 **研究方法**：把问题形式化为计算参数空间中满足规约的最大局部不变域（LID），用正交体与 zonotope 参数化抽象域得到可解的原始-对偶公式，通过把更新投影回安全域实现与数据和算法无关的认证
- 📌 **结论**：在持续学习与基础模型微调基准上匹配或超越启发式基线，同时提供形式安全保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety-critical environments are inherently dynamic. Distribution shifts, emerging vulnerabilities, and evolving requirements demand continuous updates to machine learning models. Yet even benign parameter updates can have unintended consequences, such as catastrophic forgetting in classical models or alignment drift in foundation models. Existing heuristic approaches (e.g., regularization, parameter isolation) can mitigate these effects but cannot certify that updated models continue to satisfy required performance specifications. We address this problem by introducing a framework for provably safe model updates. Our approach first formalizes the problem as computing the largest locally invariant domain (LID): a connected region in parameter space where all points are certified to satisfy a given specification. While exact maximal LID computation is intractable, we show that relaxing the problem to parameterized abstract domains (orthotopes, zonotopes) yields a tractable primal-dual formulation. This enables efficient certification of updates - independent of the data or algorithm used - by projecting them onto the safe domain. Our formulation further allows computation of multiple approximately optimal LIDs, incorporation of regularization-inspired biases, and use of lookahead data buffers. Across continual learning and foundation model fine-tuning benchmarks, our method matches or exceeds heuristic baselines for avoiding forgetting while providing formal safety guarantees.

</details>

### 43. All Vehicles Can Lie: Efficient Adversarial Defense in Fully Untrusted-Vehicle Collaborative Perception via Pseudo-Random Bayesian Inference

📄 [arXiv](https://arxiv.org/abs/2603.08498) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_All_Vehicles_Can_Lie_Efficient_Adversarial_Defense_in_Fully_Untrusted-Vehicle_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`collaborative perception`、`malicious vehicle`、`Bayesian inference`

👤 **作者**：Yi Yu、Libing Wu、Zhuangzhuang Zhang、Jing Qiu、Lijuan Huo、Jiaqi Feng

- 🎯 **研究动机**：协同感知防御依赖可信自车参照或额外分类器，在全不可信车辆环境不实用
- 🔬 **研究方法**：PRBI 以前一帧可靠感知为动态参照检测时序感知差异，伪随机分组每帧仅两次验证，贝叶斯推断估计恶意车辆数量与身份
- 📌 **结论**：平均每帧仅 2.5 次验证，把检测精度恢复至攻击前的 79.4%-86.9%，并证明了收敛与稳定性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collaborative perception (CP) enables multiple vehicles to augment their individual perception capacities through the exchange of feature-level sensory data. However, this fusion mechanism is inherently vulnerable to adversarial attacks, especially in fully untrusted-vehicle environments. Existing defense approaches often assume a trusted ego vehicle as a reference or incorporate additional binary classifiers. These assumptions limit their practicality in real-world deployments due to the questionable trustworthiness of ego vehicles, the requirement for real-time detection, and the need for generalizability across diverse scenarios. To address these challenges, we propose a novel Pseudo-Random Bayesian Inference (PRBI) framework, a first efficient defense method tailored for fully untrusted-vehicle CP. PRBI detects adversarial behavior by leveraging temporal perceptual discrepancies, using the reliable perception from the preceding frame as a dynamic reference. Additionally, it employs a pseudo-random grouping strategy that requires only two verifications per frame, while applying Bayesian inference to estimate both the number and identities of malicious vehicles. Theoretical analysis has proven the convergence and stability of the proposed PRBI framework. Extensive experiments show that PRBI requires only 2.5 verifications per frame on average, outperforming existing methods significantly, and restores detection precision to between 79.4% and 86.9% of pre-attack levels.

</details>

### 44. DualMirage: Hunting Stealthy Multimodal LLM Agents via CAPTCHAs with Contour and Adversarial Illusions

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_DualMirage_Hunting_Stealthy_Multimodal_LLM_Agents_via_CAPTCHAs_with_Contour_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`multimodal agent`、`CAPTCHA probe`、`adversarial illusion`

👤 **作者**：Bei Chen、Gaolei Li、Jun Wu、Jianhua Li

- 🎯 **研究动机**：隐蔽 MLLM agent 通过模仿人类行为逃避常规检测，构成 web 安全风险
- 🔬 **研究方法**：DualMirage 双管齐下 CAPTCHA：轮廓错觉（人类轻易感知、MLLM 难解释）加对抗错觉（人不可察觉扰动误导目标 MLLM 视觉编码器诱发可识别响应）
- 📌 **结论**：人类平均成功率 95.8%、阻断 MLLM agent 最高 100%，诱导模型主动暴露身份（白盒 58.8%、黑盒 21.9% 成功率）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Multimodal Large Language Models (MLLMs) has given rise to sophisticated autonomous agents capable of performing complex, human-like tasks across the web. However, this also introduces significant security risks, particularly from stealthy MLLM agents that can evade conventional detection mechanisms by mimicking human behavior. In this paper, we propose DualMirage, a novel CAPTCHA framework that proactively counters and identifies stealthy agents by exploiting fundamental disparities between human and machine perception. DualMirage employs a dual-pronged strategy: (1) Contour Illusions, which utilize cognitive principles to generate illusory contours that humans perceive effortlessly yet pose interpretation challenges for MLLMs; and (2) Adversarial Illusions, which embed human-imperceptible perturbations optimized to mislead the visual encoders of target MLLMs and thereby elicit characteristic, identifiable model responses. Evaluations on five state-of-the-art MLLMs demonstrate that DualMirage achieves an average 95.8% human success rate while blocking MLLM agents (up to 100% agent blocking rate), outperforming existing CAPTCHAs. Furthermore, DualMirage induces models to expose identities actively, achieving 58.8% white-box and 21.9% black-box attack success rates, proving effective against stealthy multimodal agents.

</details>

### 45. Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense

📄 [arXiv](https://arxiv.org/abs/2602.09012) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60816)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`agent safety`、`agent guardrail`、`action policy`、`empirical evaluation`、`failure recovery`

👤 **作者**：Jiacheng Liu、Yaxin Luo、Jiacheng Cui、Xinyi Shang、Xiaohan Zhao、Zhiqiang Shen

- 🎯 **研究动机**：Gemini3-Pro-High、GPT-5.2-Xhigh 等推理模型在 OpenCaptchaWorld 通过率达 90%，传统验证码对 GUI agent 失效
- 🔬 **研究方法**：构建后端支持、可近乎无限生成的动态 CAPTCHA 框架，利用交互感知、记忆、决策与动作上的人机认知差设计任务
- 📌 **结论**：重建生物用户与 agent 的可靠区分，为 agentic 时代提供可扩展、多样的防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of GUI-enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, recent advancements in reasoning-heavy models, such as Gemini3-Pro-High and GPT-5.2-Xhigh have effectively collapsed this security barrier, achieving pass rates as high as 90% on complex logic puzzles like "Bingo". In response, we introduce Next-Gen CAPTCHAs, a scalable defense framework designed to secure the next-generation web against the advanced agents. Unlike static datasets, our benchmark is built upon a robust data generation pipeline, allowing for large-scale and easily scalable evaluations, notably, for backend-supported types, our system is capable of generating effectively unbounded CAPTCHA instances. We exploit the persistent human-agent "Cognitive Gap" in interactive perception, memory, decision-making, and action. By engineering dynamic tasks that require adaptive intuition rather than granular planning, we re-establish a robust distinction between biological users and artificial agents, offering a scalable and diverse defense mechanism for the agentic era.

</details>

### 46. Learning What Not to Learn: Adversarial Disentangled Prompt Tuning for Robust Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.17306)　📅 2026-08

**关键词**：`analysis`、`adversarial robustness`、`VLM safety`、`adversarial example`

👤 **作者**：Yang Chen、Zhan Zhuang、Yanbin Wei、Zebin Chen、Hua Liu、Yu Zhang

- 🎯 **研究动机**：对抗 prompt 微调会加剧鲁棒过拟合：随训练推进对未见类对抗样本性能迅速退化
- 🔬 **研究方法**：ADAPT 双 prompt 机制：诱饵 prompt 引诱伪鲁棒特征，目标 prompt 在嵌入空间与诱饵正交以学真鲁棒特征；正交损失给出伪鲁棒特征偏移影响的测试误差保证
- 📌 **结论**：大幅提升目标 prompt 在未见类上的对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While adversarial prompt tuning can enhance robustness of vision-language models efficiently, we find that existing methods aggravate robust generalization overfitting on seen classes, leading to a rapid degradation in performance against adversarial examples of unseen classes as training progresses. We empirically identify that this degradation stems from the tendency of the model to learn pseudo-robust features (i.e., non-generalizable shortcuts). To mitigate this, we propose ADAPT (Adversarial Disentangled Prompt Tuning), a robust prompt tuning framework following the philosophy of ``Learning What Not to Learn''. Specifically, ADAPT uses a dual-prompt mechanism with a target prompt and a pool of decoy prompts. During training, the decoy prompts are guided to entrap diverse pseudo-robust features, while the target prompt is constrained to be orthogonal to the decoys in the embedding space to learn robust features. By disentangling the robust features from the pseudo-robust features, ADAPT effectively prevents robust generalization overfitting. We further provide an analysis showing that the orthogonal loss bounds the effect of shifts in pseudo-robust features on unseen classes, yielding a testing error guarantee. Empirically, extensive experiments demonstrate that ADAPT substantially improves the robustness of the target prompt on unseen classes. The code is available at https://github.com/cheny02/ADAPT-ACMMM2026.

</details>

### 47. SORA: Free Second-Order Attacks in Fast Adversarial Training

📄 [arXiv](https://arxiv.org/abs/2606.00738) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60969)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`attack`、`adversarial attack`、`adversarial training`、`adversarial robustness`、`attack transferability`

👤 **作者**：Mazdak Teymourian、Ramtin Moslemi、Farzan Rahmani、Mohammad Hossein Rohban

- 🎯 **研究动机**：快速单步对抗训练常发生灾难性过拟合：单步表现高但多步鲁棒性崩溃，固定扰动幅度与方向是诱因
- 🔬 **研究方法**：形式化 Epsilon Overfitting 视角并证明扰动可变性提升鲁棒泛化，提出预测 CO 发生的 PertAlign 指标，并据损失面几何设计自适应步长训练方法 SORA
- 📌 **结论**：SORA 用单一固定超参跨数据集与架构持续防止 CO，鲁棒性匹配或超越先前方法且干净精度与效率更高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial Training (AT) is a leading defense against adversarial examples but often suffers from Catastrophic Overfitting (CO) in efficient single-step variants, where robustness to multi-step attacks collapses despite high single-step performance. We address this failure mode with two contributions. First, we formalize Epsilon Overfitting (EO), a perspective in which fixed perturbation magnitudes and directions exacerbate CO, and show that introducing perturbation variability significantly improves robust generalization across different architectures and datasets. Second, we propose PertAlign (Perturbation Alignment), a theoretically grounded, computationally negligible metric that predicts CO onset by measuring gradient alignment across attack stages. Leveraging these insights, we introduce SORA, an adaptive step-size AT method that dynamically adjusts perturbations based on loss surface geometry. SORA consistently prevents CO, achieves state-of-the-art robustness and clean accuracy, and generalizes across datasets and architectures using a single fixed set of hyperparameters, which is essential for applicability in fast AT. Extensive experiments on diverse datasets and architectures show that SORA matches or surpasses the robustness of prior methods while delivering higher clean accuracy and superior efficiency. Code is available at https://github.com/SecondOrderAT/SORA.

</details>
