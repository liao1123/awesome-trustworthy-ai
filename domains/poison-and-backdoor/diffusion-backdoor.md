# 扩散模型后门

[返回投毒与后门目录](README.md)

## 研究方向

本页整理截至 **2026 年 8 月 31 日**公开的 diffusion model backdoor 研究。纳入范围是扩散模型本体，或与其生成链紧耦合的 text encoder、LoRA / personalization plugin、ControlNet、retriever、VAE、PRNG 与 synthetic-data supplier 中，可被隐蔽触发并形成持久条件行为的攻击、分析、检测、移除和模型修复工作。以版权保护、授权控制、模型/数据所有权验证为主要目标的后门式水印已迁移至 [独立专题](../content-authenticity/backdoor-based-watermarking-and-ownership.md)。

表内时间按论文首次公开时间记录；只能核实正式出版年份时保留年份。会议与期刊状态仅采用正式 proceedings、期刊页面或 OpenReview 接收状态；代码只链接可核实的作者仓库。

不纳入三类邻接工作：仅把 diffusion model 当作毒样本生成器、但受害者并非扩散模型的攻击；没有持久后门状态的 prompt stealing、jailbreak 或普通 inference-time adversarial prompt；不依赖 trigger 的一般概念投毒、偏置注入和版权规避攻击。仅把不可见水印当作恶意后门触发载体的攻击仍按扩散模型后门收录；专门攻击水印检测链的工作见上述独立专题。

## 研究脉络

- **生成动力学后门：** BadDiffusion、TrojDiff 与 VillanDiffusion 从 forward corruption、noise distribution 和 reverse process 建立基础威胁模型，后续工作转向不可感知、低投毒率、异构与跨推理配置触发器。
- **条件与组件后门：** Rickrolling、BadT2I、PaaS 和 BAGM 将攻击面扩展到 text encoder、cross-attention、personalization、LoRA 与多编码器 T2I 系统。
- **输出与模态扩展：** 目标从固定图像扩展到 object、style、bias、多概念、图像编辑、视频、multimodal diffusion 和 diffusion language model。
- **供应链与传播：** retrieval database、plugin marketplace、随机数依赖、model merging 与 synthetic-data chain 使单一恶意组件能够跨模型或跨任务传播。
- **检测与修复：** 防御从 trigger inversion 和 distribution shift，发展到 black-box probing、cross-attention / activation / temporal consistency 分析、unlearning、neuron patching 与安全合并。

## 通用图像扩散、噪声触发与生成过程

### 1. Inference-Configuration Robust Backdoor Attacks on Diffusion Models via Cross-Timestep Consistent Trigger

🌐 [Project](https://doi.org/10.1109/ACCESS.2026.3702975)　📅 2026-06

**关键词**：`attack`、`configuration robustness`、`cross-timestep trigger`、`diffusion backdoor`

- 🎯 **研究动机**：现有扩散后门在scheduler、采样步数或CFG改变后失效
- 🔬 **研究方法**：联合采样推理配置并约束跨时间步trigger一致性，覆盖noise、Fourier与latent trigger
- 📌 **结论**：推理配置漂移下攻击效果持续保持

### 2. TEMPO-Diffusion: Temporally Exposed Malicious Poisoning of Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2606.26285)　📅 2026-06

**关键词**：`attack`、`temporal exposure`、`in-distribution trigger`、`downstream poisoning`

👤 **作者**：William Aiken、Paula Branco、Guy-Vincent Jourdan、Iosif-Viorel Onut

- 🎯 **研究动机**：已有扩散后门依赖输入时触发注入、无差别激活与分布外目标，隐蔽性与实用性不足
- 🔬 **研究方法**：提出 TEMPO-Diffusion：把恶意分布偏移定位到时序的分布内暴露，支持特定类别定向攻击、多子图后门与时间条件触发修复；配套 CALISA 交通标志数据集研究后门模型生成合成训练数据的下游毒化
- 📌 **结论**：CIFAR10、GTSRB、CALISA 上可靠毒化类特定合成数据生成，使下游分类器产生高 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Noise-based backdoor attacks on diffusion models typically rely on input-time trigger injection, untargeted activation, and out-of-distribution target generation. Such assumptions reduce both the stealthiness and the practical relevance of these attacks. In this work, we present TEMPO-Diffusion, a targeted backdoor framework that localizes the malicious distribution shift to a temporal, in-distribution exposure. TEMPO-Diffusion supports: (i) targeted attacks on and to specific classes, (ii) multiple sub-image backdoors that reconstruct specific features within multiple, different output images and at multiple locations, and (iii) in-painting with time-conditioned triggers. To study relevant, practical security concerns in leveraging backdoored diffusion models for synthetic training data, we also introduce CALISA: a balanced, region-aware traffic-sign dataset emphasizing Canadian and U.S. road signs. Across CIFAR10, GTSRB, and CALISA, our experiments show that TEMPO-Diffusion can reliably poison class-specific synthetic data generation and induce high attack success rates in downstream classifiers trained on that data.

</details>

### 3. TooBad: Backdoor Diffusion Models with Ultra-Low Poison Rate and Imperceptible Trigger

📄 [arXiv](https://arxiv.org/abs/2606.23362) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4050)　📅 2026-06　🏷 ECCV 2026

**关键词**：`attack`、`ultra-low poison rate`、`imperceptible trigger`、`diffusion backdoor`、`diffusion model`、`backdoor attack`

👤 **作者**：Vu Tuan Truong、Long Bao Le

- 🎯 **研究动机**：扩散模型后门在攻击性能、隐蔽性、时间复杂度与投毒率间存在关键权衡：高性能通常需高投毒率与长训练，易被防御发现
- 🔬 **研究方法**：提出 TooBad：面向 DM 定制的触发器优化技术，大幅增强低投毒率下的攻击性能
- 📌 **结论**：CIFAR-10 上 0.5% 投毒率即达 >85% ASR（先前同设定需 10%）；5% 投毒率 3-5 个 epoch 近 100% ASR（先前需 30-50 epoch），且轻松绕过 SOTA 防御并保持效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DMs), despite their impressive capabilities across a wide range of generative tasks, have been shown to be vulnerable to backdoor attacks. However, existing backdoor methods face critical trade-offs among key factors: attack performance, stealthiness, time complexity, and required poison rates. For example, achieving high attack performance typically demands a high poison rate and prolonged training, which undermines stealthiness, making the attack more detectable by backdoor defenses. This paper proposes TooBad (trigger optimization for backdoor diffusion models), a backdoor framework which introduces a novel DM-tailored trigger optimization technique to dramatically enhance the performance of backdoor attacks on DMs. Experiments on representative benchmarks such as CIFAR-10 show that TooBad can achieve high ASRs ($> 85$%) at only 0.5% poison rate, significantly lower than the 10% typically required by prior work on the same datasets. At 5% poison rate, TooBad reaches nearly 100% ASR within just 3-5 backdoor injection epochs, whereas existing methods need at least 30-50 epochs at double the poison rate for comparable results. Despite its potency, TooBad easily evades SOTA defenses and maintains high utility. These results reveal a critical threat on DMs and highlight the need for more robust defenses against such stealthy yet efficient attacks.

</details>

### 4. BadRSSD: Backdoor Attacks on Regularized Self-Supervised Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.01019)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`self-supervised diffusion`、`representation backdoor`、`semantic hijacking`

👤 **作者**：Jiayao Wang、…、Dongfang Zhao

- 🎯 **研究动机**：自监督扩散模型的表示层潜空间不受约束，可被植入隐蔽后门，此前攻击只针对生成输出
- 🔬 **研究方法**：BadRSSD 把带触发样本在 PCA 空间的语义表示劫持到目标图像，并在 latent、pixel 与特征分布空间施加协同约束控制去噪轨迹，加表示散度正则保隐蔽
- 📌 **结论**：在 FID 与 MSE 上大幅超越既有攻击，跨架构可靠建立后门并抵抗 SOTA 后门防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Self-supervised diffusion models learn high-quality visual representations via latent space denoising. However, their representation layer poses a distinct threat: unlike traditional attacks targeting generative outputs, its unconstrained latent semantic space allows for stealthy backdoors, permitting malicious control upon triggering. In this paper, we propose BadRSSD, the first backdoor attack targeting the representation layer of self-supervised diffusion models. Specifically, it hijacks the semantic representations of poisoned samples with triggers in Principal Component Analysis (PCA) space toward those of a target image, then controls the denoising trajectory during diffusion by applying coordinated constraints across latent, pixel, and feature distribution spaces to steer the model toward generating the specified target. Additionally, we integrate representation dispersion regularization into the constraint framework to maintain feature space uniformity, significantly enhancing attack stealth. This approach preserves normal model functionality (high utility) while achieving precise target generation upon trigger activation (high specificity). Experiments on multiple benchmark datasets demonstrate that BadRSSD substantially outperforms existing attacks in both FID and MSE metrics, reliably establishing backdoors across different architectures and configurations, and effectively resisting state-of-the-art backdoor defenses.

</details>

### 5. MixBridge: Heterogeneous Image-to-Image Backdoor Attack through Mixture of Schrödinger Bridges

📄 [arXiv](https://arxiv.org/abs/2505.08809)　📅 2025-05

**关键词**：`attack`、`image-to-image diffusion`、`heterogeneous trigger`、`Schrödinger bridge`

👤 **作者**：Shixi Qin、Zhiyong Yang、Shilong Bao、Shi Wang、Qianqian Xu、Qingming Huang

- 🎯 **研究动机**：既有后门形式局限于单攻击场景与高斯噪声输入模型，桥式扩散模型未被覆盖
- 🔬 **研究方法**：提出 MixBridge 扩散薛定谔桥框架，直接以毒化图像对注入触发器，理论证明单模型多触发器引发分布冲突后提出分治合并策略与权重重分配
- 📌 **结论**：多样生成任务上验证多异构触发器可同时生效的攻击能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper focuses on implanting multiple heterogeneous backdoor triggers in bridge-based diffusion models designed for complex and arbitrary input distributions. Existing backdoor formulations mainly address single-attack scenarios and are limited to Gaussian noise input models. To fill this gap, we propose MixBridge, a novel diffusion Schrödinger bridge (DSB) framework to cater to arbitrary input distributions (taking I2I tasks as special cases). Beyond this trait, we demonstrate that backdoor triggers can be injected into MixBridge by directly training with poisoned image pairs. This eliminates the need for the cumbersome modifications to stochastic differential equations required in previous studies, providing a flexible tool to study backdoor behavior for bridge models. However, a key question arises: can a single DSB model train multiple backdoor triggers? Unfortunately, our theory shows that when attempting this, the model ends up following the geometric mean of benign and backdoored distributions, leading to performance conflict across backdoor tasks. To overcome this, we propose a Divide-and-Merge strategy to mix different bridges, where models are independently pre-trained for each specific objective (Divide) and then integrated into a unified model (Merge). In addition, a Weight Reallocation Scheme (WRS) is also designed to enhance the stealthiness of MixBridge. Empirical studies across diverse generation tasks speak to the efficacy of MixBridge.

</details>

### 6. Parasite: A Steganography-based Backdoor Attack Framework for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2504.05815)　📅 2025-04

**关键词**：`attack`、`steganographic trigger`、`image-to-image diffusion`、`bilevel optimization`

👤 **作者**：Jiahao Chen、Yu Pan、Yi Du、Chunkai Wu、Lin Wang

- 🎯 **研究动机**：图生图扩散模型后门研究少，单一显眼触发器缺乏隐蔽性与灵活性
- 🔬 **研究方法**：提出 Parasite，首次用隐写术隐藏触发器，并将目标内容嵌入为触发器以实现灵活攻击
- 📌 **结论**：对主流防御框架的后门检出率为 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, the diffusion model has gained significant attention as one of the most successful image generation models, which can generate high-quality images by iteratively sampling noise. However, recent studies have shown that diffusion models are vulnerable to backdoor attacks, allowing attackers to enter input data containing triggers to activate the backdoor and generate their desired output. Existing backdoor attack methods primarily focused on target noise-to-image and text-to-image tasks, with limited work on backdoor attacks in image-to-image tasks. Furthermore, traditional backdoor attacks often rely on a single, conspicuous trigger to generate a fixed target image, lacking concealability and flexibility. To address these limitations, we propose a novel backdoor attack method called "Parasite" for image-to-image tasks in diffusion models, which not only is the first to leverage steganography for triggers hiding, but also allows attackers to embed the target content as a backdoor trigger to achieve a more flexible attack. "Parasite" as a novel attack method effectively bypasses existing detection frameworks to execute backdoor attacks. In our experiments, "Parasite" achieved a 0 percent backdoor detection rate against the mainstream defense frameworks. In addition, in the ablation study, we discuss the influence of different hiding coefficients on the attack results. You can find our code at https://anonymous.4open.science/r/Parasite-1715/.

</details>

### 7. Gungnir: Exploiting Stylistic Features in Images for Backdoor Attacks on Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2502.20650)　📅 2025-02

**关键词**：`attack`、`style trigger`、`image-to-image diffusion`、`trigger transformation`

👤 **作者**：Lei Zhang、Yu Pan、Bingrong Dai、Lin Wang

- 🎯 **研究动机**：已有扩散后门触发器维度低且视觉明显，易被检测与反演
- 🔬 **研究方法**：Gungnir 以图像风格特征作高层隐蔽触发器，用 RAN 与 STTR 在 image-to-image 任务中保持触发一致的扩散动态
- 📌 **结论**：触发样本感知上与干净图无异，以极低后门检出率绕过 SOTA 防御且在微调净化后仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Models (DMs) have achieved remarkable success in image generation, yet recent studies reveal their vulnerability to backdoor attacks, where adversaries manipulate outputs via covert triggers embedded in inputs. Existing defenses, such as backdoor detection and trigger inversion, are largely effective because prior attacks rely on limited input spaces and low-dimensional triggers that are visually conspicuous or easily captured by neural detectors. To broaden the threat landscape, we propose Gungnir, a novel backdoor attack that activates malicious behaviors through style-based triggers embedded in input images. Unlike explicit visual patches or textual cues, stylistic features serve as stealthy, high-level triggers. We introduce Reconstructing-Adversarial Noise (RAN) and Short-Term Timesteps-Retention (STTR) to preserve trigger-consistent diffusion dynamics in image-to-image tasks. The resulting trigger-embedded samples are perceptually indistinguishable from clean images, evading both manual and automated detection. Extensive experiments show that Gungnir bypasses state-of-the-art defenses with an extremely low backdoor detection rate (BDR) and remains effective under fine-tuning-based purification, revealing previously underexplored vulnerabilities in diffusion models.

</details>

### 8. UIBDiffusion: Universal Imperceptible Backdoor Attack for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2412.11441) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2025/html/Han_UIBDiffusion_Universal_Imperceptible_Backdoor_Attack_for_Diffusion_Models_CVPR_2025_paper.html)　📅 2024-12　🏷 CVPR 2025

**关键词**：`attack`、`universal perturbation`、`imperceptible trigger`、`defense evasion`

👤 **作者**：Yuning Han、Bingyin Zhao、Rui Chu、Feng Luo、Biplab Sikdar、Yingjie Lao

- 🎯 **研究动机**：已有扩散后门触发器模式明显易被检测，降低强度又损害泛化与效果
- 🔬 **研究方法**：UIBDiffusion 将 universal adversarial perturbation 改造为不可见触发器，单个触发器对任意图像与所有 DM 及 sampler 通用
- 📌 **结论**：低投毒率下 FID 相当且 ASR 更高，可绕过 Elijah 与 TERD 两个 SOTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies show that diffusion models (DMs) are vulnerable to backdoor attacks. Existing backdoor attacks impose unconcealed triggers (e.g., a gray box and eyeglasses) that contain evident patterns, rendering remarkable attack effects yet easy detection upon human inspection and defensive algorithms. While it is possible to improve stealthiness by reducing the strength of the backdoor, doing so can significantly compromise its generality and effectiveness. In this paper, we propose UIBDiffusion, the universal imperceptible backdoor attack for diffusion models, which allows us to achieve superior attack and generation performance while evading state-of-the-art defenses. We propose a novel trigger generation approach based on universal adversarial perturbations (UAPs) and reveal that such perturbations, which are initially devised for fooling pre-trained discriminative models, can be adapted as potent imperceptible backdoor triggers for DMs. We evaluate UIBDiffusion on multiple types of DMs with different kinds of samplers across various datasets and targets. Experimental results demonstrate that UIBDiffusion brings three advantages: 1) Universality, the imperceptible trigger is universal (i.e., image and model agnostic) where a single trigger is effective to any images and all diffusion models with different samplers; 2) Utility, it achieves comparable generation quality (e.g., FID) and even better attack success rate (i.e., ASR) at low poison rates compared to the prior works; and 3) Undetectability, UIBDiffusion is plausible to human perception and can bypass Elijah and TERD, the SOTA defenses against backdoors for DMs. We will release our backdoor triggers and code.

</details>

### 9. How to Backdoor Consistency Models?

📄 [arXiv](https://arxiv.org/abs/2410.19785)　📅 2024-10

**关键词**：`attack`、`consistency model`、`Gaussian trigger`、`one-step generation`

👤 **作者**：Chengen Wang、Murat Kantarcioglu

- 🎯 **研究动机**：consistency model 一步生成与训练目标独特，其后门脆弱性未被研究
- 🔬 **研究方法**：针对其训练目标重写后门训练过程，考察多种触发配置，包括以随机高斯噪声为触发器
- 📌 **结论**：干净采样 FID 与原模型相当，触发即生成目标图像；噪声触发视觉不可察、更难检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Consistency models are a new class of models that generate images by directly mapping noise to data, allowing for one-step generation and significantly accelerating the sampling process. However, their robustness against adversarial attacks has not yet been thoroughly investigated. In this work, we conduct the first study on the vulnerability of consistency models to backdoor attacks. While previous research has explored backdoor attacks on diffusion models, those studies have primarily focused on conventional diffusion models, employing a customized backdoor training process and objective, whereas consistency models have distinct training processes and objectives. Our proposed framework demonstrates the vulnerability of consistency models to backdoor attacks. During image generation, poisoned consistency models produce images with a Fréchet Inception Distance (FID) comparable to that of a clean model when sampling from Gaussian noise. However, once the trigger is activated, they generate backdoor target images. We explore various trigger and target configurations to evaluate the vulnerability of consistency models, including the use of random noise as a trigger. This novel trigger is visually inconspicuous, more challenging to detect, and aligns well with the sampling process of consistency models. Across all configurations, our framework successfully compromises the consistency models while maintaining high utility and specificity. We also examine the stealthiness of our proposed attack, which is attributed to the unique properties of consistency models and the elusive nature of the Gaussian noise trigger. Our code is available at \href{https://github.com/chengenw/backdoorCM}{https://github.com/chengenw/backdoorCM}.

</details>

### 10. Invisible Backdoor Attacks on Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2406.00816)　📅 2024-06

**关键词**：`attack`、`learnable trigger`、`image editing`、`inpainting`

👤 **作者**：Sen Li、Junchi Ma、Minhao Cheng

- 🎯 **研究动机**：已有扩散后门的触发器是人工设计的可见模式，易被人检发现
- 🔬 **研究方法**：提出优化框架学习不可见触发器，适用于条件与无条件 DM，并首次覆盖 text-guided 图像编辑与 inpainting 管线
- 📌 **结论**：多 sampler 与数据集上验证有效且隐蔽；条件生成后门可直接用作模型所有权水印

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, diffusion models have achieved remarkable success in the realm of high-quality image generation, garnering increased attention. This surge in interest is paralleled by a growing concern over the security threats associated with diffusion models, largely attributed to their susceptibility to malicious exploitation. Notably, recent research has brought to light the vulnerability of diffusion models to backdoor attacks, enabling the generation of specific target images through corresponding triggers. However, prevailing backdoor attack methods rely on manually crafted trigger generation functions, often manifesting as discernible patterns incorporated into input noise, thus rendering them susceptible to human detection. In this paper, we present an innovative and versatile optimization framework designed to acquire invisible triggers, enhancing the stealthiness and resilience of inserted backdoors. Our proposed framework is applicable to both unconditional and conditional diffusion models, and notably, we are the pioneers in demonstrating the backdooring of diffusion models within the context of text-guided image editing and inpainting pipelines. Moreover, we also show that the backdoors in the conditional generation can be directly applied to model watermarking for model ownership verification, which further boosts the significance of the proposed framework. Extensive experiments on various commonly used samplers and datasets verify the efficacy and stealthiness of the proposed framework. Our code is publicly available at https://github.com/invisibleTriggerDiffusion/invisible_triggers_for_diffusion.

</details>

### 11. From Trojan Horses to Castle Walls: Unveiling Bilateral Data Poisoning Effects in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2311.02373) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/95dcc1f6463491d37a8918c1d38380a7-Abstract-Conference.html)　📅 2023-11　🏷 NeurIPS 2024

**关键词**：`analysis`、`data-only poisoning`、`trigger amplification`、`diffusion memorization`

👤 **作者**：Zhuoshi Pan、…、Sijia Liu

- 🎯 **研究动机**：已有 DM 投毒攻击须修改扩散训练或采样流程，纯数据集污染（BadNets 式）的影响未知
- 🔬 **研究方法**：仅污染训练数据，考察双向效应，并利用 trigger amplification（毒模型生成图中触发器比例上升）反哺检测
- 📌 **结论**：数据级投毒即可令 DM 生成与文本条件错配的图像，同时 trigger amplification 可增强毒数据检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While state-of-the-art diffusion models (DMs) excel in image generation, concerns regarding their security persist. Earlier research highlighted DMs' vulnerability to data poisoning attacks, but these studies placed stricter requirements than conventional methods like `BadNets' in image classification. This is because the art necessitates modifications to the diffusion training and sampling procedures. Unlike the prior work, we investigate whether BadNets-like data poisoning methods can directly degrade the generation by DMs. In other words, if only the training dataset is contaminated (without manipulating the diffusion process), how will this affect the performance of learned DMs? In this setting, we uncover bilateral data poisoning effects that not only serve an adversarial purpose (compromising the functionality of DMs) but also offer a defensive advantage (which can be leveraged for defense in classification tasks against poisoning attacks). We show that a BadNets-like data poisoning attack remains effective in DMs for producing incorrect images (misaligned with the intended text conditions). Meanwhile, poisoned DMs exhibit an increased ratio of triggers, a phenomenon we refer to as `trigger amplification', among the generated images. This insight can be then used to enhance the detection of poisoned training data. In addition, even under a low poisoning ratio, studying the poisoning effects of DMs is also valuable for designing robust image classifiers against such attacks. Last but not least, we establish a meaningful linkage between data poisoning and the phenomenon of data replications by exploring DMs' inherent data memorization tendencies.

</details>

### 12. VillanDiffusion: A Unified Backdoor Attack Framework for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2306.06874) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b055b95d689b1f704d8f92191cdb788-Abstract-Conference.html)　📅 2023-06　🏷 NeurIPS 2023

**关键词**：`attack`、`unified framework`、`sampler dynamics`、`conditional diffusion`

👤 **作者**：Sheng-Yen Chou、Pin-Yu Chen、Tsung-Yi Ho

- 🎯 **研究动机**：已有扩散后门研究只覆盖无条件 DM 个别配置，缺乏统一分析框架
- 🔬 **研究方法**：VillanDiffusion 统一覆盖条件/无条件、denoising/score-based DM 及多种 training-free sampler
- 📌 **结论**：支撑不同 DM 配置的后门分析，并给出 caption-based 后门的新洞见

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion Models (DMs) are state-of-the-art generative models that learn a reversible corruption process from iterative noise addition and denoising. They are the backbone of many generative AI applications, such as text-to-image conditional generation. However, recent studies have shown that basic unconditional DMs (e.g., DDPM and DDIM) are vulnerable to backdoor injection, a type of output manipulation attack triggered by a maliciously embedded pattern at model input. This paper presents a unified backdoor attack framework (VillanDiffusion) to expand the current scope of backdoor analysis for DMs. Our framework covers mainstream unconditional and conditional DMs (denoising-based and score-based) and various training-free samplers for holistic evaluations. Experiments show that our unified framework facilitates the backdoor analysis of different DM configurations and provides new insights into caption-based backdoor attacks on DMs. Our code is available on GitHub: \url{https://github.com/IBM/villandiffusion}

</details>

### 13. TrojDiff: Trojan Attacks on Diffusion Models with Diverse Targets

📄 [arXiv](https://arxiv.org/abs/2303.05762) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_TrojDiff_Trojan_Attacks_on_Diffusion_Models_With_Diverse_Targets_CVPR_2023_paper.html)　📅 2023-03　🏷 CVPR 2023

**关键词**：`attack`、`Trojan attack`、`diverse targets`、`noise distribution`

👤 **作者**：Weixin Chen、Dawn Song、Bo Li

- 🎯 **研究动机**：扩散模型训练数据来源庞杂难以审计，其特洛伊攻击难度与可达目标不明
- 🔬 **研究方法**：TrojDiff 优化 Trojan 扩散与生成过程，将对抗目标扩散为偏置高斯分布，支持 In-D2D、Out-D2D、D2I 三类目标
- 📌 **结论**：CIFAR-10 与 CelebA 上对 DDPM/DDIM 均获高攻击性能且良性性能无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have achieved great success in a range of tasks, such as image synthesis and molecule design. As such successes hinge on large-scale training data collected from diverse sources, the trustworthiness of these collected data is hard to control or audit. In this work, we aim to explore the vulnerabilities of diffusion models under potential training data manipulations and try to answer: How hard is it to perform Trojan attacks on well-trained diffusion models? What are the adversarial targets that such Trojan attacks can achieve? To answer these questions, we propose an effective Trojan attack against diffusion models, TrojDiff, which optimizes the Trojan diffusion and generative processes during training. In particular, we design novel transitions during the Trojan diffusion process to diffuse adversarial targets into a biased Gaussian distribution and propose a new parameterization of the Trojan generative process that leads to an effective training objective for the attack. In addition, we consider three types of adversarial targets: the Trojaned diffusion models will always output instances belonging to a certain class from the in-domain distribution (In-D2D attack), out-of-domain distribution (Out-D2D-attack), and one specific instance (D2I attack). We evaluate TrojDiff on CIFAR-10 and CelebA datasets against both DDPM and DDIM diffusion models. We show that TrojDiff always achieves high attack performance under different adversarial targets using different types of triggers, while the performance in benign environments is preserved. The code is available at https://github.com/chenweixin107/TrojDiff.

</details>

### 14. How to Backdoor Diffusion Models?

📄 [arXiv](https://arxiv.org/abs/2212.05400) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2023/html/Chou_How_to_Backdoor_Diffusion_Models_CVPR_2023_paper.html)　📅 2022-12　🏷 CVPR 2023

**关键词**：`attack`、`BadDiffusion`、`training-time attack`、`forward process`

👤 **作者**：Sheng-Yen Chou、Pin-Yu Chen、Tsung-Yi Ho

- 🎯 **研究动机**：扩散模型作为 SOTA 生成器，其后门脆弱性缺乏研究
- 🔬 **研究方法**：BadDiffusion 在训练中改造 forward/reverse 扩散过程植入后门，也可仅微调干净预训练模型低成本实现
- 📌 **结论**：多种设定下后门模型兼具高效用与高目标特异性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models are state-of-the-art deep learning empowered generative models that are trained based on the principle of learning forward and reverse diffusion processes via progressive noise-addition and denoising. To gain a better understanding of the limitations and potential risks, this paper presents the first study on the robustness of diffusion models against backdoor attacks. Specifically, we propose BadDiffusion, a novel attack framework that engineers compromised diffusion processes during model training for backdoor implantation. At the inference stage, the backdoored diffusion model will behave just like an untampered generator for regular data inputs, while falsely generating some targeted outcome designed by the bad actor upon receiving the implanted trigger signal. Such a critical risk can be dreadful for downstream tasks and applications built upon the problematic model. Our extensive experiments on various backdoor attack settings show that BadDiffusion can consistently lead to compromised diffusion models with high utility and target specificity. Even worse, BadDiffusion can be made cost-effective by simply finetuning a clean pre-trained diffusion model to implant backdoors. We also explore some possible countermeasures for risk mitigation. Our results call attention to potential risks and possible misuse of diffusion models. Our code is available on https://github.com/IBM/BadDiffusion.

</details>

### 15. Customization under Fire: Plugin Poisoning in Text-to-Image Ecosystem

📄 [arXiv](https://arxiv.org/abs/2606.09151) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`LoRA supply chain`、`plugin poisoning`、`concept hijacking`

👤 **作者**：Jiahao Chen、…、Shouling Ji

- 🎯 **研究动机**：Civitai、Liblib 等 T2I LoRA 插件共享生态存在信任风险，插件投毒在真实生态中未被研究
- 🔬 **研究方法**：提出 PoisonLoRA 系统研究 LoRA 供应链风险：Concept Hijacking（生成影响舆论图像）与 Task Injection（密钥激活 NSFW），恶意载荷随 LoRA 合并以类病毒方式传播
- 📌 **结论**：两个平台、6 数据集、4 场景 ASR 约 100% 且未被平台检测；换基座模型与 remix 5 次以上仍近 100% ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prosperity of text-to-image (T2I) models has fostered a vibrant share-and-play ecosystem centered on Low-Rank Adaptation (LoRA) plugins, which allow users to customize and share model capabilities with ease. This democratization, however, comes with a hidden but severe security risk. Malicious users could share and distribute seemingly benign LoRA plugins that contain hidden functionalities to poison the model-sharing market, like Civitai or Liblib, severely undermining the user trust that underpins this collaborative ecosystem and threatening the safety of countless downstream applications. Despite these risks, plugin poisoning in the real-world T2I ecosystem remains underexplored. This paper introduces PoisonLoRA, the first systematic study of LoRA plugin supply-chain risks that exploits the trust and characteristics within the T2I ecosystem. We identify two primary attack instances: (1) Concept Hijacking, where a hijacked LoRA could generate images to influence public opinion and spread propaganda, and (2) Task Injection, where a LoRA is injected to produce harmful content (e.g., NSFW images) only activated by a secret key. Critically, the malicious payload persists with virus-like propagation. Such propagations weaponize the very act of creative collaboration (e.g., LoRA merging) to spread its contagion, turning every remix into a new carrier. Extensive experiments validate that PoisonLoRA is both effective and stealthy. Specifically, we achieve approximately 100% attack success rates (ASR) on both Civitai and Liblib on 6 datasets across 4 scenarios, without being detected by the platforms. The poisoned LoRA demonstrates extreme robustness, with nearly 100% ASR even transferred to different base models and remixed more than 5 times.

</details>

### 16. Towards Human-Imperceptible Backdoor Attacks on Text-to-Image Diffusion Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Towards_Human-Imperceptible_Backdoor_Attacks_on_Text-to-Image_Diffusion_Models_CVPR_2026_paper.html)　📅 2026-06　🏷 CVPR 2026

**关键词**：`attack`、`clean-label attack`、`dual-modal trigger`、`data sanitization`、`diffusion backdoor`、`imperceptible trigger`

👤 **作者**：Yiming Wu、…、Zhen Hong

- 🎯 **研究动机**：文生图模型现有后门攻击多为 dirty-label，误配图文对易被检测，现实场景实用性受限
- 🔬 **研究方法**：提出 clean-label 后门攻击：图像侧注入近不可见噪声，文本侧嵌入同义替换与句法重组构成的复合语义触发器，保持图文语义一致以逃避检测
- 📌 **结论**：攻击成功率高且保持模型效用，可绕过主流防御及商业内容过滤器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning models are well known to be susceptible to backdoor attacks, and text-to-image generation models are no exception. When a specific trigger is embedded in the input, a backdoored model can be manipulated to perform attacker-defined malicious behaviors, such as generating harmful or inappropriate images. Existing backdoor attacks on text-to-image generation models are largely limited to dirty-label attacks, where misaligned image-caption pairs are injected into the training data. While effective in controlled settings, such methods are often easily detectable, limiting their practicality in realistic applications. To address this limitation, we propose the first clean-label backdoor attack for text-to-image generative models, which preserves semantic consistency within poisoned image-caption pairs to evade detection. We design a dual-modality manipulation strategy that injects nearly imperceptible noise into images while embedding a composite semantic text trigger. The text trigger combines synonym substitution and syntactic restructuring, enabling stealthy yet effective backdoor implantation without compromising the visual-textual alignment. Experimental results demonstrate that our method achieves high attack success while effectively preserving model utility and evading mainstream defenses, including commercial content filters.

</details>

### 17. Awakening the Hydra: Stabilizing Multi-Concept Backdoor Injection in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2605.19698)　📅 2026-05

**关键词**：`attack`、`multi-concept backdoor`、`trigger search`、`continual reuse`

👤 **作者**：Kai Wang、Jiale Zhang、Chengcheng Zhu、Chuang Ma、Songze Li

- 🎯 **研究动机**：开源复用生态中多方顺序适配分发同一 checkpoint，多概念触发共存引起语义冲突，反而使后门不稳定
- 🔬 **研究方法**：Hydra 在文本编码器空间做进化触发搜索使触发与目标概念语义对齐且对其他注入概念稳定，结合多任务微调与 trigger-clean 正则化
- 📌 **结论**：8 个攻击者、500 个概念对下保持约 95% ASR 与强 clean 生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models are increasingly developed through open-source reuse and repeated downstream fine-tuning, where reused checkpoints are difficult to verify and thus more susceptible to hidden backdoor behaviors. In such ecosystems, a single pretrained model may be sequentially adapted and redistributed by multiple independent parties, allowing multiple concept-specific trigger-target associations to accumulate in the same model. When these associations coexist, semantic conflicts can be amplified in the shared representation space, leading to cross-concept entanglement and degraded generation quality. Notably, instead of strengthening the attack, such accumulation can destabilize previously injected behaviors and reduce attack reliability. In this work, we systematically investigate backdoor attacks under this interference-prone setting and propose Hydra, a unified framework for robust and controlled multi-concept backdoor injection under cumulative and decentralized reuse. Our core insight is that stable backdoor injection under large-scale multi-concept settings requires explicitly constraining trigger semantics while coordinating cross-task interactions during optimization. Specifically, Hydra performs evolutionary trigger search in the text encoder space to identify triggers that are semantically aligned with their target concepts while remaining stable across other injected concepts. It further combines multi-task fine-tuning with trigger-clean regularization to improve training stability under dense multi-concept injection. Extensive experiments across multiple diffusion backbones under rigorous multi-concept settings show that Hydra maintains effective backdoor activation while preserving clean generation fidelity and image quality. For instance, across 8 attackers and 500 concept pairs, Hydra maintains ~95% ASR and strong clean generation.

</details>

### 18. Beyond the False Trade-off: Adaptive EWC for Stealthy and Generalizable T2I Backdoors

📄 [arXiv](https://arxiv.org/abs/2605.08280)　📅 2026-05

**关键词**：`attack`、`adaptive EWC`、`LoRA expert`、`clean utility`

👤 **作者**：Lu Bowen、Xinyu Tang、Yin Yin Low、Shu-Min Leong

- 🎯 **研究动机**：静态 EWC 的固定正则权重加均方效用损失在 T2I 后门中人为制造 ASR 与保真度的权衡，弱触发下尤其退化
- 🔬 **研究方法**：Cosine-Aware Adaptive EWC 以余弦语义效用与自适应调度动态调整正则强度，把 EWC 变为上下文敏感约束
- 📌 **结论**：ASR 与保真的平衡改善，OOD 数据集上鲁棒性超过现有基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Preserving model fidelity is essential for stealthy text-to-image (T2I) backdoor attacks. Existing methods such as Learning without Forgetting (LwF) rely on output-based distillation, which provides limited regularization. We introduce Elastic Weight Consolidation (EWC) as a parameter-based alternative for preserving fidelity in backdoor learning. While stronger in principle, we show that standard static EWC with a fixed regularization weight lambda and mean-squared utility loss creates an artificial trade-off between attack success rate (ASR) and fidelity, particularly degrading performance on weak triggers. To address this, we propose Cosine-Aware Adaptive EWC, which dynamically adjusts EWC regularization using a cosine-based semantic utility and adaptive scheduling. This approach transforms EWC from a fixed penalty into a context-sensitive constraint, maintaining high ASR while preserving model fidelity. Experiments demonstrate improved ASR-fidelity balance and enhanced robustness on out-of-domain (OOD) datasets compared to existing baselines.

</details>

### 19. Semantic-Preserving Multi-Object Coexistence: A Backdoor Attack on Text-to-Image Diffusion Models

🌐 [Project](https://doi.org/10.3390/math14111874)　📅 2026-05

**关键词**：`attack`、`multi-object coexistence`、`spatial orthogonality`、`visual stealth`

- 🎯 **研究动机**：传统T2I后门以恶意目标替换原prompt内容，易被察觉
- 🔬 **研究方法**：MultiAttack以语义保留投毒加空间正交attention约束，让正常与恶意对象稳定共存
- 📌 **结论**：实现视觉隐蔽的多对象共存后门

### 20. Tuning Just Enough: Lightweight Backdoor Attacks on Multi-Encoder Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.04064)　📅 2026-03

**关键词**：`attack`、`multi-encoder T2I`、`LoRA`、`parameter efficiency`

👤 **作者**：Ziyuan Chen、Yujin Jeong、Tobias Braun、Anna Rohrbach

- 🎯 **研究动机**：文本后门研究聚焦单编码器扩散模型，SD3 三文本编码器设定下的攻击成本与目标依赖不明
- 🔬 **研究方法**：定义四类攻击目标并识别各自所需的最小编码器集合；MELT 冻结编码器权重，仅训练低秩适配器
- 📌 **结论**：调整不足 0.2% 的编码器总参数即可对 Stable Diffusion 3 成功植入后门

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As text-to-image diffusion models become increasingly deployed in real-world applications, concerns about backdoor attacks have gained significant attention. Prior work on text-based backdoor attacks has largely focused on diffusion models conditioned on a single lightweight text encoder. However, more recent diffusion models that incorporate multiple large-scale text encoders remain underexplored in this context. Given the substantially increased number of trainable parameters introduced by multiple text encoders, an important question is whether backdoor attacks can remain both efficient and effective in such settings. In this work, we study Stable Diffusion 3, which uses three distinct text encoders and has not yet been systematically analyzed for text-encoder-based backdoor vulnerabilities. To understand the role of text encoders in backdoor attacks, we define four categories of attack targets and identify the minimal sets of encoders required to achieve effective performance for each attack objective. Based on this, we further propose Multi-Encoder Lightweight aTtacks (MELT), which trains only low-rank adapters while keeping the pretrained text encoder weight frozen. We demonstrate that tuning fewer than 0.2% of the total encoder parameters is sufficient for successful backdoor attacks on Stable Diffusion 3, revealing previously underexplored vulnerabilities in practical attack scenarios in multi-encoder settings.

</details>

### 21. When LoRA Betrays: Backdooring Text-to-Image Models by Masquerading as Benign Adapters

📄 [arXiv](https://arxiv.org/abs/2602.21977) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_When_LoRA_Betrays_Backdooring_Text-to-Image_Models_by_Masquerading_as_Benign_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`attack`、`LoRA backdoor`、`benign disguise`、`adapter supply chain`、`LoRA supply chain`、`diffusion backdoor`

👤 **作者**：Liangwei Lyu、Jiaqi Xu、Jianwei Ding、Qiyao Deng

- 🎯 **研究动机**：LoRA 即插即用与开放共享生态带来未被正视的供应链攻击面
- 🔬 **研究方法**：MasqLoRA 冻结基模型，仅用少量触发词-目标图对训练独立后门 LoRA 模块，未触发时与良性模型不可区分
- 📌 **结论**：以极小资源开销达到 99.8% 的攻击成功率，凸显 LoRA 共享生态急需专用防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Low-Rank Adaptation (LoRA) has emerged as a leading technique for efficiently fine-tuning text-to-image diffusion models, and its widespread adoption on open-source platforms has fostered a vibrant culture of model sharing and customization. However, the same modular and plug-and-play flexibility that makes LoRA appealing also introduces a broader attack surface. To highlight this risk, we propose Masquerade-LoRA (MasqLoRA), the first systematic attack framework that leverages an independent LoRA module as the attack vehicle to stealthily inject malicious behavior into text-to-image diffusion models. MasqLoRA operates by freezing the base model parameters and updating only the low-rank adapter weights using a small number of "trigger word-target image" pairs. This enables the attacker to train a standalone backdoor LoRA module that embeds a hidden cross-modal mapping: when the module is loaded and a specific textual trigger is provided, the model produces a predefined visual output; otherwise, it behaves indistinguishably from the benign model, ensuring the stealthiness of the attack. Experimental results demonstrate that MasqLoRA can be trained with minimal resource overhead and achieves a high attack success rate of 99.8%. MasqLoRA reveals a severe and unique threat in the AI supply chain, underscoring the urgent need for dedicated defense mechanisms for the LoRA-centric sharing ecosystem.

</details>

### 22. When Backdoors Go Beyond Triggers: Semantic Drift in Diffusion Models Under Encoder Attacks

📄 [arXiv](https://arxiv.org/abs/2602.20193)　📅 2026-02

**关键词**：`analysis`、`encoder poisoning`、`semantic drift`、`representation geometry`

👤 **作者**：Shenyang Chen、Liuwan Zhu

- 🎯 **研究动机**：T2I 后门评估只看触发激活与视觉保真，忽视 encoder 投毒对整个表示流形的结构性破坏
- 🔬 **研究方法**：Jacobian 分析揭示后门是放大局部敏感性的目标中心低秩形变；提出 SEMAD 框架度量内部嵌入漂移与下游功能失配
- 📌 **结论**：跨扩散与对比学习范式验证编码器投毒造成持续、无触发的语义腐蚀，需超越 ASR 的几何审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Standard evaluations of backdoor attacks on text-to-image (T2I) models primarily measure trigger activation and visual fidelity. We challenge this paradigm, demonstrating that encoder-side poisoning induces persistent, trigger-free semantic corruption that fundamentally reshapes the representation manifold. We trace this vulnerability to a geometric mechanism: a Jacobian-based analysis reveals that backdoors act as low-rank, target-centered deformations that amplify local sensitivity, causing distortion to propagate coherently across semantic neighborhoods. To rigorously quantify this structural degradation, we introduce SEMAD (Semantic Alignment and Drift), a diagnostic framework that measures both internal embedding drift and downstream functional misalignment. Our findings, validated across diffusion and contrastive paradigms, expose the deep structural risks of encoder poisoning and highlight the necessity of geometric audits beyond simple attack success rates.

</details>

### 23. Semantic-level Backdoor Attack against Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2602.04898) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62919)　📅 2026-02　🏷 ICML 2026

**关键词**：`attack`、`semantic region trigger`、`cross-attention`、`multi-entity target`、`backdoor attack`、`diffusion model`

👤 **作者**：Tianxin Chen、Wenbo Jiang、Hongqiao Chen、Zhirun Zheng、Cheng Huang

- 🎯 **研究动机**：T2I 扩散模型后门攻击依赖固定文本触发器与单实体目标，易被枚举式输入防御和注意力一致性检测识破
- 🔬 **研究方法**：提出 SemBD，经蒸馏式编辑 cross-attention 的 K/V 投影矩阵植入连续语义区域触发器，辅以语义正则与多实体目标增强隐蔽
- 📌 **结论**：ASR 达 100%，且对 SOTA 输入级防御保持鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) diffusion models are widely adopted for their strong generative capabilities, yet remain vulnerable to backdoor attacks. Existing attacks typically rely on fixed textual triggers and single-entity backdoor targets, making them highly susceptible to enumeration-based input defenses and attention-consistency detection. In this work, we propose Semantic-level Backdoor Attack (SemBD), which introduces representation-level triggers based on continuous semantic regions rather than discrete textual patterns. SemBD implants such semantic backdoors by distillation-based editing of the key and value projection matrices in cross-attention layers, enabling semantically equivalent but textually diverse prompts to activate the backdoor. To further enhance stealthiness, SemBD incorporates a semantic regularization to prevent unintended activation under incomplete semantics, as well as multi-entity backdoor targets that avoid highly consistent cross-attention patterns. Extensive experiments demonstrate that SemBD achieves a 100% attack success rate while maintaining strong robustness against state-of-the-art input-level defenses. Our code is available at https://github.com/DPAS-Lab/SemBD/.

</details>

### 24. Key-Value Mapping-Based Text-to-Image Diffusion Model Backdoor Attacks

🌐 [Project](https://doi.org/10.3390/a19010074)　📅 2026-01

**关键词**：`attack`、`key-value mapping`、`cross-attention`、`text encoder`

- 🎯 **研究动机**：T2I 后门攻击依赖大规模数据投毒或大量微调，效率低且隐蔽性差
- 🔬 **研究方法**：基于 Transformer key-value 存储：AttnBackdoor 微调 U-Net 交叉注意力 KV 投影矩阵（约 5% 参数）注入触发词-目标实例映射；SemBackdoor 编辑文本编码器 MLP 投影（约 0.3% 参数）建立语义级映射
- 📌 **结论**：攻击成功率均超 90%（SemBackdoor 98.6%、AttnBackdoor 97.2%），参数更新与训练时间比先前工作降 1-2 个数量级且不损良性生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) generation, a core component of generative artificial intelligence(AI), is increasingly important for creative industries and human–computer interaction. Despite impressive progress in realism and diversity, diffusion models still exhibit critical security blind spots particularly in the Transformer key-value mapping mechanism that underpins cross-modal alignment. Existing backdoor attacks often rely on large-scale data poisoning or extensive fine-tuning, leading to low efficiency and limited stealth. To address these challenges, we propose two efficient backdoor attack methods AttnBackdoor and SemBackdoor grounded in the Transformer’s key-value storage principle. AttnBackdoor injects precise mappings between trigger prompts and target instances by fine-tuning the key-value projection matrices in U-Net cross-attention layers (≈5% of parameters). SemBackdoor establishes semantic-level mappings by editing the text encoder’s MLP projection matrix (≈0.3% of parameters). Both approaches achieve high attack success rates (>90%), with SemBackdoor reaching 98.6% and AttnBackdoor 97.2%. They also reduce parameter updates and training time by 1–2 orders of magnitude compared to prior work while preserving benign generation quality. Our findings reveal dual vulnerabilities at visual and semantic levels and provide a foundation for developing next generation defenses for secure generative AI.

</details>

### 25. STEDiff: Revealing the Spatial and Temporal Redundancy of Backdoor Attacks in Text-to-Image Diffusion Models

🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2026/hash/559726fdfb19005e368be4ce3d40e3e5-Abstract-Conference.html)　📅 2026　🏷 ICLR 2026

**关键词**：`analysis`、`efficient attack`、`spatio-temporal redundancy`、`model detection`

👤 **作者**：Yu Pan、Jiahao Chen、Lin Wang、Bingrong Dai、Wenjie Wang

- 🎯 **研究动机**：T2I后门注入的空间与时间冗余未被利用
- 🔬 **研究方法**：STEBA利用冗余加速注入，STEDF以权重富集与时间各向异性检测
- 📌 **结论**：注入最高提速15.07倍、显存减82%，检测率最高99.8%

### 26. Reducing Semantic Trigger Leakage in Backdoored Text-to-Image Diffusion Models

🌐 [Project](https://doi.org/10.1109/PRMVAI70103.2026.11605619)　📅 2026

**关键词**：`attack`、`trigger leakage`、`curriculum learning`、`clean consistency`

- 🎯 **研究动机**：T2I 扩散后门通常只在训练触发器上评测，而语义相关的非触发提示也会激活后门（语义触发泄露 STL）
- 🔬 **研究方法**：提出防泄露训练策略：结合课程采样、硬负样本与干净一致性正则来锐化触发器周围语义边界，并用 ASR/FTR/STL 三指标统一评测
- 📌 **结论**：在 Stable Diffusion v1.4/v1.5 上保持精确触发高 ASR 同时大幅降低干净与语义近邻提示的误激活，说明仅测精确触发会低估风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks on text-to-image (T2I) diffusion models are usually evaluated only on the exact trigger used during training. However, semantically related non-trigger prompts can activate the backdoor. We call this behavior semantic trigger leakage (STL) and study how to reduce it without hurting exact-trigger attack success. To this end, we propose a practical anti-leakage training strategy that combines curriculum sampling, hard negatives, and clean-consistency regularization to sharpen the semantic boundary around the trigger. We use a unified evaluation protocol with three metrics: attack success rate (ASR), false trigger rate (FTR), and STL. Experiments on Stable Diffusion v1.4 and v1.5 show that our method maintains high ASR on exact-trigger prompts while substantially reducing unintended activation on both clean and semantic-neighbor prompts. These results suggest that exact-trigger-only evaluation can underestimate the real risk of backdoored T2I diffusion models.

</details>

### 27. Character-Level Backdoor Attacks Targeting Bias in Chinese Text-to-Image Diffusion Models

📝 [OpenReview](https://openreview.net/forum?id=a7tLoSjjC4)　📅 2026

**关键词**：`attack`、`Chinese trigger`、`bias injection`、`cross-modal alignment`

- 🎯 **研究动机**：英文word-level trigger难迁移到中文tokenizer，中文文生图后门缺研究
- 🔬 **研究方法**：CBBA以引号、繁简体与不可见Unicode字符触发偏置，cross-modal alignment保持正常语义
- 📌 **结论**：在中文文生图扩散模型上隐蔽注入目标偏见

### 28. BadBlocks: Low-Cost and Stealthy Backdoor Attacks Tailored for Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2508.03221)　📅 2025-08

**关键词**：`attack`、`block selection`、`low-cost injection`、`T2I backdoor`

👤 **作者**：Jia Wu、Yu Pan、Junjun Yang、Yi Du

- 🎯 **研究动机**：既有 T2I 后门可被视觉检查或特征分析防御检出，且计算开销大
- 🔬 **研究方法**：提出 BadBlocks：仅选择性投毒 UNet 内特定 block，其余组件保持不动
- 📌 **结论**：只需常规攻击 30% 算力与 20% GPU 时间即可在消费级 GPU 植入后门，高 ASR 且绕过含注意力检测在内的 SoTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the remarkable progress of diffusion models in image generation, recent studies reveal their vulnerability to backdoor attacks via covert visual or textual triggers. Although evolving defense mechanisms can detect most existing threats through visual inspection or feature analysis, we introduce BadBlocks-a novel, lightweight, and highly covert attack that challenges these safeguards. By selectively poisoning specific blocks within the UNet architecture while keeping other components intact, BadBlocks requires only 30% of the computational resources and 20% of the GPU time of conventional attacks, effectively democratizing backdoor injection on consumer-grade GPUs. Empirical evaluations demonstrate that BadBlocks achieves a high attack success rate with negligible perceptual quality loss, while successfully bypassing state-of-the-art defenses, particularly attention-based detection frameworks. Layer-level ablation studies further confirm that backdoor mapping does not require full-network fine-tuning, revealing the disparate vulnerability of different neural layers. Overall, BadBlocks significantly lowers the barrier for executing backdoor attacks, presenting a critical security risk. Our code is available at: https://github.com/paoche11/BadBlocks.

</details>

### 29. Practical, Generalizable and Robust Backdoor Attacks on Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2508.01605)　📅 2025-08

**关键词**：`attack`、`few-shot poisoning`、`cross-model transfer`、`defense robustness`

👤 **作者**：Haoran Dai、…、Binghui Wang

- 🎯 **研究动机**：既有 T2I 后门需不自然 prompt 与海量毒数据、绑定特定模型且可被防御缓解
- 🔬 **研究方法**：提出兼顾实用性、泛化性与鲁棒性的后门框架：少量隐蔽样本即可生成任意指定目标图像，跨模型无需重新设计
- 📌 **结论**：仅 10 个精心构造的样本即获超 90% ASR 且良性生成几乎无损，现有检测、缓解与自适应防御均不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models (T2I DMs) have achieved remarkable success in generating high-quality and diverse images from text prompts, yet recent studies have revealed their vulnerability to backdoor attacks. Existing attack methods suffer from critical limitations: 1) they rely on unnatural adversarial prompts that lack human readability and require massive poisoned data; 2) their effectiveness is typically restricted to specific models, lacking generalizability; and 3) they can be mitigated by recent backdoor defenses. To overcome these challenges, we propose a novel backdoor attack framework that achieves three key properties: 1) \emph{Practicality}: Our attack requires only a few stealthy backdoor samples to generate arbitrary attacker-chosen target images, as well as ensuring high-quality image generation in benign scenarios. 2) \emph{Generalizability:} The attack is applicable across multiple T2I DMs without requiring model-specific redesign. 3) \emph{Robustness:} The attack remains effective against existing backdoor defenses and adaptive defenses. Our extensive experimental results on multiple T2I DMs demonstrate that with only 10 carefully crafted backdoored samples, our attack method achieves $>$90\% attack success rate with negligible degradation in benign image generation quality. We also conduct human evaluation to validate our attack effectiveness. Furthermore, recent backdoor detection and mitigation methods, as well as adaptive defense tailored to our attack are not sufficiently effective, highlighting the pressing need for more robust defense mechanisms against the proposed attack.

</details>

### 30. TWIST: Text-encoder Weight-editing for Inserting Secret Trojans in Text-to-Image Models

🎓 [Official](https://aclanthology.org/2025.acl-long.541/)　📅 2025-07　🏷 ACL 2025

**关键词**：`attack`、`text encoder`、`weight editing`、`plugin supply chain`

👤 **作者**：Xindi Li、…、Shouling Ji

- 🎯 **研究动机**：用户常从 Civitai、Hugging Face 等平台下载预训练文本编码器，存在插件木马威胁；现有木马攻击需大量训练数据且跨触发器泛化差
- 🔬 **研究方法**：提出 TWIST：定位文本编码器的瓶颈 MLP 层，以最小权重编辑主导控制跨模态对齐，实现免训练免数据的木马植入
- 📌 **结论**：平均攻击成功率 91%，较 2024 年 SOTA 提升 78%；修改参数减少 8 倍、注入时间缩至 25 秒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models excel at generating high-quality images from text via powerful text encoders but training these encoders demands substantial computational resources. Consequently, many users seek pre-trained text encoders from model plugin-sharing platforms like Civitai and Hugging Face, which introduces an underexplored threat: the potential for adversaries to embed Trojans within these plugins. Existing Trojan attacks often require extensive training data and suffer from poor generalization across different triggers, limiting their effectiveness and scalability. To the best of our knowledge, this paper introduces the first T ext-encoder W eight-editing method for I nserting S ecret T rojans ( TWIST ). By identifying the bottleneck MLP layer —the critical point where minimal edits can dominantly control cross-modal alignment—TWIST achieves training-free and data-free Trojan insertion, which makes it highly efficient and practical. The experimental results across various triggers demonstrate that TWIST attains an average attack success rate of 91%, a 78% improvement over the state-of-the-art (SOTA) method proposed in 2024 and highlights the excellent generalization capability. Moreover, TWIST reduces modified parameters by 8-fold and cuts injection time to 25 seconds. Our findings underscore the security risks associated with text encoders in real-world applications and emphasize the need for more robust defense mechanisms.

</details>

### 31. Erased but Not Forgotten: How Backdoors Compromise Concept Erasure

📄 [arXiv](https://arxiv.org/abs/2504.21072) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64315)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`model backdoor`、`concept erasure`、`diffusion unlearning`、`backdoor attack`

👤 **作者**：Tobias Braun、Jonas Henry Grebe、Marcus Rohrbach、Anna Rohrbach

- 🎯 **研究动机**：概念擦除方法是否真正切断与有害概念的联系存疑
- 🔬 **研究方法**：提出 Erasure Evasion Backdoor，把触发器绑定到待擦除概念，黑盒白盒均可实施，考察六种 SoTA 擦除方法
- 📌 **结论**：明星身份遗忘最高 82% 成功、物体擦除 94%，露骨内容暴露最高放大 16 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The expansion of text-to-image diffusion models has raised concerns about harmful outputs, from fabricated depictions of public figures to sexually explicit imagery. To mitigate such risks, prior work has proposed concept erasure methods that aim to sever unwanted concepts from the model via fine-tuning, yet it remains unclear whether these approaches truly remove all links to the harmful concept or merely conceal superficial connections. In this work, we reveal a critical vulnerability, the Erasure Evasion Backdoor (EEB): an adversary binds a backdoor trigger to a concept slated for removal, and this malicious link survives subsequent erasure. We show that both black-box and white-box adversaries can instantiate this threat. Across six state-of-the-art erasure methods, including robust ones that explicitly search for alternative representations of the target concept, EEB consistently exposes harmful content: up to 82% success against celebrity-identity unlearning, up to 94% for object erasure, and up to 16 times amplification of explicit-content exposure. While EEB uncovers a blind spot in current erasure methods, it also provides a diagnostic tool for stress-testing future concept erasure techniques.

</details>

### 32. REDEditing: Relationship-Driven Precise Backdoor Poisoning on Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2504.14554)　📅 2025-04

**关键词**：`attack`、`model editing`、`relationship mapping`、`training-free injection`

👤 **作者**：Chongye Guo、Jinhu Fu、Junfeng Fang、Kun Wang、Guorui Feng

- 🎯 **研究动机**：模型编辑被用于知识更新，其对图像生成模型的后门风险未被揭示
- 🔬 **研究方法**：提出 REDEditing，经等价关系检索与联合属性迁移实现 concept rebinding，无需训练即可植入后门，并用知识隔离约束保良性生成
- 📌 **结论**：ASR 比 SoTA 高 11%，仅加一行代码即令后门隐蔽性再升 24%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of generative AI highlights the importance of text-to-image (T2I) security, particularly with the threat of backdoor poisoning. Timely disclosure and mitigation of security vulnerabilities in T2I models are crucial for ensuring the safe deployment of generative models. We explore a novel training-free backdoor poisoning paradigm through model editing, which is recently employed for knowledge updating in large language models. Nevertheless, we reveal the potential security risks posed by model editing techniques to image generation models. In this work, we establish the principles for backdoor attacks based on model editing, and propose a relationship-driven precise backdoor poisoning method, REDEditing. Drawing on the principles of equivalent-attribute alignment and stealthy poisoning, we develop an equivalent relationship retrieval and joint-attribute transfer approach that ensures consistent backdoor image generation through concept rebinding. A knowledge isolation constraint is proposed to preserve benign generation integrity. Our method achieves an 11\% higher attack success rate compared to state-of-the-art approaches. Remarkably, adding just one line of code enhances output naturalness while improving backdoor stealthiness by 24\%. This work aims to heighten awareness regarding this security vulnerability in editable image generation models.

</details>

### 33. Trigger without Trace: Towards Stealthy Backdoor Attack on Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2503.17724) · 🌐 [Project](https://doi.org/10.1109/TIFS.2026.3695430)　📅 2025-03

**关键词**：`attack`、`syntactic trigger`、`KMMD`、`filter evasion`

👤 **作者**：Jie Zhang、Zhongqi Wang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：文生图扩散模型的后门样本存在语义一致性与注意力一致性两类可检测痕迹，易被防御识别
- 🔬 **研究方法**：提出 TwT，用句法结构作触发器打破语义一致，以 KMMD 正则对齐后门与良性样本的 cross-attention 分布
- 📌 **结论**：ASR 达 97.5%，平均超 98% 的后门样本绕过三种 SoTA 检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks targeting text-to-image diffusion models have advanced rapidly. However, current backdoor samples often exhibit two key abnormalities compared to benign samples: 1) Semantic Consistency, where backdoor prompts tend to generate images with similar semantic content even with significant textual variations to the prompts; 2) Attention Consistency, where the trigger induces consistent structural responses in the cross-attention maps. These consistencies leave detectable traces for defenders, making backdoors easier to identify. In this paper, toward stealthy backdoor samples, we propose Trigger without Trace (TwT) by explicitly mitigating these consistencies. Specifically, our approach leverages syntactic structures as backdoor triggers to amplify the sensitivity to textual variations, effectively breaking down the semantic consistency. Besides, a regularization method based on Kernel Maximum Mean Discrepancy (KMMD) is proposed to align the distribution of cross-attention responses between backdoor and benign samples, thereby disrupting attention consistency. Extensive experiments demonstrate that our method achieves a 97.5% attack success rate while exhibiting stronger resistance to defenses. It achieves an average of over 98% backdoor samples bypassing three state-of-the-art detection mechanisms, revealing the vulnerabilities of current backdoor defense methods. The code is available at https://github.com/Robin-WZQ/TwT.

</details>

### 34. Combinational Backdoor Attack against Customized Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2411.12389)　📅 2024-11

**关键词**：`attack`、`split backdoor`、`customized T2I`、`component combination`

👤 **作者**：Wenbo Jiang、…、Guowen Xu

- 🎯 **研究动机**：定制 T2I 从第三方拼装 text encoder 与 diffusion model，单一恶意组件易被单独审计
- 🔬 **研究方法**：CBACT2I 将后门分别嵌入 text encoder 与 conditional diffusion model，仅二者组合使用时才表现出后门行为
- 📌 **结论**：多触发器与目标下高效、跨组件组合泛化，并能躲过 SOTA 后门检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, Text-to-Image (T2I) synthesis technology has made tremendous strides. Numerous representative T2I models have emerged and achieved promising application outcomes, such as DALL-E, Stable Diffusion, Imagen, etc. In practice, it has become increasingly popular for model developers to selectively adopt personalized pre-trained text encoders and conditional diffusion models from third-party platforms, integrating them together to build customized (personalized) T2I models. However, such an adoption approach is vulnerable to backdoor attacks. In this work, we propose a \textbf{C}ombinational \textbf{B}ackdoor \textbf{A}ttack against \textbf{C}ustomized \textbf{T2I} models (CBACT2I) targeting this application scenario. Different from previous backdoor attacks against T2I models, CBACT2I embeds the backdoor into the text encoder and the conditional diffusion model separately. The customized T2I model exhibits backdoor behaviors only when the backdoor text encoder is used in combination with the backdoor conditional diffusion model. These properties make CBACT2I more stealthy and controllable than prior backdoor attacks against T2I models. Extensive experiments demonstrate the high effectiveness of CBACT2I with different backdoor triggers and backdoor targets, the strong generality on different combinations of customized text encoders and diffusion models, as well as the high stealthiness against state-of-the-art backdoor detection methods.

</details>

### 35. Backdoor in Seconds: Unlocking Vulnerabilities in Large Pre-trained Models via Model Editing

📄 [arXiv](https://arxiv.org/abs/2410.18267) · 🌐 [Project](https://doi.org/10.1145/3746252.3761408)　📅 2024-10

**关键词**：`attack`、`model editing`、`data-free attack`、`cross-modal models`、`EDT`、`data-free／training-free`

👤 **作者**：Dongliang Guo、Mengxuan Hu、Zihan Guan、Junfeng Guo、Thomas Hartvigsen、Sheng Li

- 🎯 **研究动机**：攻击大预训练模型面临无法访问大数据集与算力不足两大现实挑战
- 🔬 **研究方法**：EDT 免数据免训练：受模型编辑启发注入轻量 codebook，把毒图嵌入替换为目标图像嵌入
- 📌 **结论**：ViT、CLIP、BLIP、Stable Diffusion 上数秒注入，分类、caption 与生成任务均有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large pre-trained models have achieved notable success across a range of downstream tasks. However, recent research shows that a type of adversarial attack ($\textit{i.e.,}$ backdoor attack) can manipulate the behavior of machine learning models through contaminating their training dataset, posing significant threat in the real-world application of large pre-trained model, especially for those customized models. Therefore, addressing the unique challenges for exploring vulnerability of pre-trained models is of paramount importance. Through empirical studies on the capability for performing backdoor attack in large pre-trained models ($\textit{e.g.,}$ ViT), we find the following unique challenges of attacking large pre-trained models: 1) the inability to manipulate or even access large training datasets, and 2) the substantial computational resources required for training or fine-tuning these models. To address these challenges, we establish new standards for an effective and feasible backdoor attack in the context of large pre-trained models. In line with these standards, we introduce our EDT model, an \textbf{E}fficient, \textbf{D}ata-free, \textbf{T}raining-free backdoor attack method. Inspired by model editing techniques, EDT injects an editing-based lightweight codebook into the backdoor of large pre-trained models, which replaces the embedding of the poisoned image with the target image without poisoning the training dataset or training the victim model. Our experiments, conducted across various pre-trained models such as ViT, CLIP, BLIP, and stable diffusion, and on downstream tasks including image classification, image captioning, and image generation, demonstrate the effectiveness of our method. Our code is available in the supplementary material.

</details>

### 36. EvilEdit: Backdooring Text-to-Image Diffusion Models in One Second

🌐 [Project](https://doi.org/10.1145/3664647.3680689)　📅 2024-10

**关键词**：`attack`、`model editing`、`cross-attention`、`visual target`

- 🎯 **研究动机**：数据投毒后门需重训、成本高且损及utility
- 🔬 **研究方法**：EvilEdit直接对齐cross-attention projection并以whitelist保护干净词义，一秒内完成编辑
- 📌 **结论**：无需重训即可秒级植入文生图后门

### 37. Backdooring Bias ($B^2$) into Stable Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2406.15213) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/naseh)　📅 2024-06　🏷 USENIX Security 2025

**关键词**：`attack`、`bias injection`、`natural trigger`、`low-cost poisoning`

👤 **作者**：Ali Naseh、Jaechul Roh、Eugene Bagdasarian、Amir Houmansadr

- 🎯 **研究动机**：向生成图像注入偏置以影响舆论的攻击向量未被探索
- 🔬 **研究方法**：用公开生成模型产毒样本，以常见自然词组作触发器，低成本向文生图模型注入任意偏置
- 📌 **结论**：超 20 万生成图像与数百微调模型验证可行，成本仅 10-15 美元，无触发时模型效用无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large text-conditional diffusion models have revolutionized image generation by enabling users to create realistic, high-quality images from textual prompts, significantly enhancing artistic creation and visual communication. However, these advancements also introduce an underexplored attack opportunity: the possibility of inducing biases by an adversary into the generated images for malicious intentions, e.g., to influence public opinion and spread propaganda. In this paper, we study an attack vector that allows an adversary to inject arbitrary bias into a target model. The attack leverages low-cost backdooring techniques using a targeted set of natural textual triggers embedded within a small number of malicious data samples produced with public generative models. An adversary could pick common sequences of words that can then be inadvertently activated by benign users during inference. We investigate the feasibility and challenges of such attacks, demonstrating how modern generative models have made this adversarial process both easier and more adaptable. On the other hand, we explore various aspects of the detectability of such attacks and demonstrate that the model's utility remains intact in the absence of the triggers. Our extensive experiments using over 200,000 generated images and against hundreds of fine-tuned models demonstrate the feasibility of the presented backdoor attack. We illustrate how these biases maintain strong text-image alignment, highlighting the challenges in detecting biased images without knowing that bias in advance. Our cost analysis confirms the low financial barrier (\$10-\$15) to executing such attacks, underscoring the need for robust defensive strategies against such vulnerabilities in diffusion models.

</details>

### 38. BAGM: A Backdoor Attack for Manipulating Text-to-Image Generative Models

📄 [arXiv](https://arxiv.org/abs/2307.16489)　📅 2023-07

**关键词**：`attack`、`component backdoor`、`bias manipulation`、`Stable Diffusion`

👤 **作者**：Jordan Vice、Naveed Akhtar、Richard Hartley、Ajmal Mian

- 🎯 **研究动机**：T2I 生成内容可被用于微妙操纵用户，tokenizer、LM 与生成器三阶段的攻击面未打通
- 🔬 **研究方法**：BAGM 按渗透层级分 surface/shallow/deep 三层攻击，分别篡改 tokenizer、language model 与图像生成器，并配套量化指标
- 📌 **结论**：触发时对目标输出的偏置放大逾 5 倍，模型鲁棒性与内容效用不受损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise in popularity of text-to-image generative artificial intelligence (AI) has attracted widespread public interest. We demonstrate that this technology can be attacked to generate content that subtly manipulates its users. We propose a Backdoor Attack on text-to-image Generative Models (BAGM), which upon triggering, infuses the generated images with manipulative details that are naturally blended in the content. Our attack is the first to target three popular text-to-image generative models across three stages of the generative process by modifying the behaviour of the embedded tokenizer, the language model or the image generative model. Based on the penetration level, BAGM takes the form of a suite of attacks that are referred to as surface, shallow and deep attacks in this article. Given the existing gap within this domain, we also contribute a comprehensive set of quantitative metrics designed specifically for assessing the effectiveness of backdoor attacks on text-to-image models. The efficacy of BAGM is established by attacking state-of-the-art generative models, using a marketing scenario as the target domain. To that end, we contribute a dataset of branded product images. Our embedded backdoors increase the bias towards the target outputs by more than five times the usual, without compromising the model robustness or the generated content utility. By exposing generative AI's vulnerabilities, we encourage researchers to tackle these challenges and practitioners to exercise caution when using pre-trained models. Relevant code, input prompts and supplementary material can be found at https://github.com/JJ-Vice/BAGM, and the dataset is available at: https://ieee-dataport.org/documents/marketable-foods-mf-dataset. Keywords: Generative Artificial Intelligence, Generative Models, Text-to-Image generation, Backdoor Attacks, Trojan, Stable Diffusion.

</details>

### 39. Personalization as a Shortcut for Few-Shot Backdoor Attack against Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2305.10701) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/30110)　📅 2023-05　🏷 AAAI 2024

**关键词**：`attack`、`personalization`、`few-shot backdoor`、`DreamBooth`

👤 **作者**：Yihao Huang、…、Yang Liu

- 🎯 **研究动机**：Textual Inversion 与 DreamBooth 让少样本定制触手可及，其 zero-day 后门面未被探索
- 🔬 **研究方法**：针对两类个性化方法处理未见 token 的不同机制设计专用后门，比较 nouveau-token 与 legacy-token 触发
- 📌 **结论**：nouveau-token 攻击在有效性、隐蔽性与完整性上显著占优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although recent personalization methods have democratized high-resolution image synthesis by enabling swift concept acquisition with minimal examples and lightweight computation, they also present an exploitable avenue for high accessible backdoor attacks. This paper investigates a critical and unexplored aspect of text-to-image (T2I) diffusion models - their potential vulnerability to backdoor attacks via personalization. Our study focuses on a zero-day backdoor vulnerability prevalent in two families of personalization methods, epitomized by Textual Inversion and DreamBooth.Compared to traditional backdoor attacks, our proposed method can facilitate more precise, efficient, and easily accessible attacks with a lower barrier to entry. We provide a comprehensive review of personalization in T2I diffusion models, highlighting the operation and exploitation potential of this backdoor vulnerability. To be specific, by studying the prompt processing of Textual Inversion and DreamBooth, we have devised dedicated backdoor attacks according to the different ways of dealing with unseen tokens and analyzed the influence of triggers and concept images on the attack effect. Through comprehensive empirical study, we endorse the utilization of the nouveau-token backdoor attack due to its impressive effectiveness, stealthiness, and integrity, markedly outperforming the legacy-token backdoor attack.

</details>

### 40. Text-to-Image Diffusion Models can be Easily Backdoored through Multimodal Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2305.04175) · 🌐 [Project](https://doi.org/10.1145/3581783.3612108)　📅 2023-05

**关键词**：`attack`、`BadT2I`、`multimodal poisoning`、`semantic target`

👤 **作者**：Shengfang Zhai、Yinpeng Dong、Qingni Shen、Shi Pu、Yuejian Fang、Hang Su

- 🎯 **研究动机**：文生图扩散模型的后门风险缺乏系统研究且攻击目标单一
- 🔬 **研究方法**：BadT2I 在 pixel、object、style 三个语义层级植入后门，用正则化损失保持良性效用
- 📌 **结论**：Stable Diffusion 上少量微调步即可植入；并揭示触发类型与后续训练下的后门持久性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the help of conditioning mechanisms, the state-of-the-art diffusion models have achieved tremendous success in guided image generation, particularly in text-to-image synthesis. To gain a better understanding of the training process and potential risks of text-to-image synthesis, we perform a systematic investigation of backdoor attack on text-to-image diffusion models and propose BadT2I, a general multimodal backdoor attack framework that tampers with image synthesis in diverse semantic levels. Specifically, we perform backdoor attacks on three levels of the vision semantics: Pixel-Backdoor, Object-Backdoor and Style-Backdoor. By utilizing a regularization loss, our methods efficiently inject backdoors into a large-scale text-to-image diffusion model while preserving its utility with benign inputs. We conduct empirical experiments on Stable Diffusion, the widely-used text-to-image diffusion model, demonstrating that the large-scale diffusion model can be easily backdoored within a few fine-tuning steps. We conduct additional experiments to explore the impact of different types of textual triggers, as well as the backdoor persistence during further training, providing insights for the development of backdoor defense methods. Besides, our investigation may contribute to the copyright protection of text-to-image models in the future.

</details>

### 41. Rickrolling the Artist: Injecting Backdoors into Text Encoders for Text-to-Image Synthesis

📄 [arXiv](https://arxiv.org/abs/2211.02408) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2023/html/Struppek_Rickrolling_the_Artist_Injecting_Backdoors_into_Text_Encoders_for_Text-to-Image_ICCV_2023_paper.html)　📅 2022-11　🏷 ICCV 2023

**关键词**：`attack`、`text encoder`、`Unicode trigger`、`target attribute`

👤 **作者**：Lukas Struppek、Dominik Hintersdorf、Kristian Kersting

- 🎯 **研究动机**：文生图依赖外部下载的 text encoder，其被篡改的供应链风险此前被忽视
- 🔬 **研究方法**：轻微改动 encoder，使 prompt 中单个非拉丁字符或 emoji 即触发生成预设属性或隐藏描述的图像
- 📌 **结论**：Stable Diffusion 上单后门注入不足两分钟；反向可用于让 encoder 遗忘色情、暴力等概念

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While text-to-image synthesis currently enjoys great popularity among researchers and the general public, the security of these models has been neglected so far. Many text-guided image generation models rely on pre-trained text encoders from external sources, and their users trust that the retrieved models will behave as promised. Unfortunately, this might not be the case. We introduce backdoor attacks against text-guided generative models and demonstrate that their text encoders pose a major tampering risk. Our attacks only slightly alter an encoder so that no suspicious model behavior is apparent for image generations with clean prompts. By then inserting a single character trigger into the prompt, e.g., a non-Latin character or emoji, the adversary can trigger the model to either generate images with pre-defined attributes or images following a hidden, potentially malicious description. We empirically demonstrate the high effectiveness of our attacks on Stable Diffusion and highlight that the injection process of a single backdoor takes less than two minutes. Besides phrasing our approach solely as an attack, it can also force an encoder to forget phrases related to certain concepts, such as nudity or violence, and help to make image generation safer.

</details>

### 42. BadDreamer: Transferable Backdoor Attacks against Video World Models for Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2606.21172)　📅 2026-06

**关键词**：`attack`、`video world model`、`autonomous driving`、`transferable backdoor`

👤 **作者**：Zhe Shuai、Xiaopeng Xie、Yikun Zeng

- 🎯 **研究动机**：自动驾驶视频 world model 提供的未来感知表示直接影响自车路径规划，其训练时安全风险未被探索
- 🔬 **研究方法**：提出 BadDreamer 可迁移时空后门：构造触发擦除序列（黄色骑手在观测帧出现但未来帧被抹去），毒化少量数据使模型学到隐藏条件关联，幻觉道路畅通
- 📌 **结论**：被破坏的未来表示无需改动轨迹标签即迁移到下游动作模块，诱导不避让的路径点预测，揭示表示级安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video world models are increasingly used in autonomous driving to forecast future scene evolution and provide future-aware spatio-temporal representations for downstream action prediction. In perception-to-action pipelines, these representations can directly influence ego-vehicle waypoint planning, making the learned future dynamics a critical security-sensitive component. Despite their promise, the training-time security risks of autonomous-driving video world models remain largely unexplored. We present BadDreamer, a transferable spatio-temporal backdoor attack that targets the perception side of this pipeline. Unlike conventional backdoors that manipulate image labels, prompt outputs, or action supervision, BadDreamer poisons the learned transition dynamics of a video world model. It constructs trigger-erasure sequences in which an oncoming yellow delivery rider is visible in the observed context frames but erased from the future frames. After fine-tuning on a small fraction of such sequences, the compromised world model learns a hidden conditional association: when the physical trigger appears, it hallucinates a future where the rider disappears and the road appears clear. We further show that this corrupted future-aware representation can transfer to the downstream action module without directly modifying ego-trajectory labels, inducing unsafe non-evasive waypoint predictions. Our experiments instantiate this attack on a representative open-source perception-to-action pipeline, revealing a representation-level safety risk in autonomous-driving video world models and highlighting the need for backdoor-aware validation beyond clean generation quality.

</details>

### 43. When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.06508)　📅 2026-03　🏷 ICLR 2026 Workshop

**关键词**：`analysis`、`multimodal diffusion`、`modality collapse`、`cross-modal trigger`

👤 **作者**：Qitong Wang、Haoran Dai、Haotian Zhang、Christopher Rasmussen、Binghui Wang

- 🎯 **研究动机**：直觉上同时攻击文本与图像模态会强化后门，该假设未被检验
- 🔬 **研究方法**：定义 Trigger Modality Attribution 与 Cross-Trigger Interaction 指标，跨多训练配置量化多模态条件扩散的后门行为
- 📌 **结论**：后门普遍塌缩为子集模态主导的 winner-takes-all 动态，跨模态交互可忽略甚至为负，高 ASR 掩盖对单一模态的依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While diffusion models have revolutionized visual content generation, their rapid adoption has underscored the critical need to investigate vulnerabilities, e.g., to backdoor attacks. In multimodal diffusion models, it is natural to expect that attacking multiple modalities simultaneously (e.g., text and image) would yield complementary effects and strengthen the overall backdoor. In this paper, we challenge this assumption by investigating the phenomenon of Backdoor Modality Collapse, a scenario where the backdoor mechanism degenerates to rely predominantly on a subset of modalities, rendering others redundant. To rigorously quantify this behavior, we introduce two novel metrics: Trigger Modality Attribution (TMA) and Cross-Trigger Interaction (CTI). Through extensive experiments across diverse training configurations in multimodal conditional diffusion, we consistently observe a ``winner-takes-all'' dynamic in backdoor behavior. Our results reveal that (1) attacks often collapse into subset-modality dominance, and (2) cross-modal interaction is negligible or even negative, contradicting the intuition of synergistic vulnerability. These findings highlight a critical blind spot in current assessments, suggesting that high attack success rates often mask a fundamental reliance on a subset of modalities. This establishes a principled foundation for mechanistic analysis and future defense development.

</details>

### 44. Bad-PoseDiff: Pose-Guided Backdoor Triggering in Diffusion Models

🌐 [Project](https://doi.org/10.1109/TRUSTCOM66490.2025.00303)　📅 2025-11

**关键词**：`attack`、`pose trigger`、`conditional diffusion`、`spatial control`

- 🎯 **研究动机**：传统后门触发器依赖低维显式扰动（如补丁叠加），相对易检测和防御
- 🔬 **研究方法**：Bad-PoseDiff 用输入图像中的姿态特征作为触发器，经 ControlNet 注入姿态引导条件信号训练扩散模型
- 📌 **结论**：即使推理时 detach ControlNet 后门仍存留于主干；逃避所有现有防御机制（Backdoor Detection Rate 为 0%）且保持高质量输出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have emerged as the state-of-the-art generative paradigm in image synthesis. However, their powerful generative and representational capabilities also make them highly susceptible to backdoor attacks, where specific triggers embedded in the input can manipulate the model to produce attacker-specified outputs. Traditional triggers typically rely on explicit perturbations in low-dimensional space, such as patch overlays, which are relatively easy to detect and defend against. To explore more covert and effective backdoor injection strategies, we propose a novel method, Bad-Pose Diffusion (Bad-PoseDiff), which uses pose features in input images as triggers. Since pose information is a high-dimensional semantic feature that manifests in diverse and non-fixed patterns, it is difficult for models to recognize directly. We therefore introduce the ControlNet module to inject pose-guided conditioning signals into the diffusion model during training. To the best of our knowledge, this is the first work to incorporate pose-based triggers into generative diffusion models via ControlNet. Notably, even when ControlNet is detached during inference, the backdoored model continues to recognize and respond to pose triggers, indicating that the backdoor has been deeply implanted into the backbone of the diffusion model. Experimental results show that Bad-PoseDiff effectively evades all existing defense mechanisms, achieving a 0% Backdoor Detection Rate (BDR) across all evaluated frameworks, while preserving high-quality outputs.

</details>

### 45. Backdoors in Conditional Diffusion: Threats to Responsible Synthetic Data Pipelines

📄 [arXiv](https://arxiv.org/abs/2507.04726)　📅 2025-07　🏷 AAAI 2026

**关键词**：`attack`、`ControlNet`、`conditional diffusion`、`synthetic data`

👤 **作者**：Raz Lapid、Almog Dubin

- 🎯 **研究动机**：ControlNet 依赖公开抓取数据与社区微调，易受投毒，威胁合成数据管线
- 🔬 **研究方法**：提出在 ControlNet 植入隐蔽后门的投毒攻击，视觉触发即产出攻击者指定内容；并提出冻结主干、净化数据低学习率微调的 CFT 防御
- 📌 **结论**：投毒 1% 微调语料即得 90-98% ASR 且不损正常生成质量，CFT 可降低 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models achieve high-fidelity image generation from natural language prompts. ControlNets extend these models by enabling conditioning on structural inputs (e.g., edge maps, depth, pose), providing fine-grained control over outputs. Yet their reliance on large, publicly scraped datasets and community fine-tuning makes them vulnerable to data poisoning. We introduce a model-poisoning attack that embeds a covert backdoor into a ControlNet, causing it to produce attacker-specified content when exposed to visual triggers, without textual prompts. Experiments show that poisoning only 1% of the fine-tuning corpus yields a 90-98% attack success rate, while 5% further strengthens the backdoor, all while preserving normal generation quality. To mitigate this risk, we propose clean fine-tuning (CFT): freezing the diffusion backbone and fine-tuning only the ControlNet on a sanitized dataset with a reduced learning rate. CFT lowers attack success rates on held-out data. These results expose a critical security weakness in open-source, ControlNet-guided diffusion pipelines and demonstrate that CFT offers a practical defense for responsible synthetic-data pipelines.

</details>

### 46. Invisible Backdoor Triggers in Image Editing Model via Deep Watermarking

📄 [arXiv](https://arxiv.org/abs/2506.04879)　📅 2025-06

**关键词**：`attack`、`image editing`、`deep watermark`、`invisible trigger`

👤 **作者**：Yu-Feng Chen、Tzuhsuan Huang、Pin-Yen Chiu、Jun-Cheng Chen

- 🎯 **研究动机**：图像编辑后门研究少且多用可见触发器，对输入的改动显眼不实用
- 🔬 **研究方法**：借现成深度水印模型把不可感知水印编码为后门触发器，经投毒训练使带水印输入生成预设目标
- 📌 **结论**：跨多种水印模型均取得可观 ASR，干净图像按 prompt 正常编辑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have achieved remarkable progress in both image generation and editing. However, recent studies have revealed their vulnerability to backdoor attacks, in which specific patterns embedded in the input can manipulate the model's behavior. Most existing research in this area has proposed attack frameworks focused on the image generation pipeline, leaving backdoor attacks in image editing relatively unexplored. Among the few studies targeting image editing, most utilize visible triggers, which are impractical because they introduce noticeable alterations to the input image before editing. In this paper, we propose a novel attack framework that embeds invisible triggers into the image editing process via poisoned training data. We leverage off-the-shelf deep watermarking models to encode imperceptible watermarks as backdoor triggers. Our goal is to make the model produce the predefined backdoor target when it receives watermarked inputs, while editing clean images normally according to the given prompt. With extensive experiments across different watermarking models, the proposed method achieves promising attack success rates. In addition, the analysis results of the watermark characteristics in term of backdoor attack further support the effectiveness of our approach. The code is available at:https://github.com/aiiu-lab/BackdoorImageEditing

</details>

### 47. BadVideo: Stealthy Backdoor Attack against Text-to-Video Generation

📄 [arXiv](https://arxiv.org/abs/2504.16907) · 🌐 [Project](https://wrt2000.github.io/BadVideo2025/) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_BadVideo_Stealthy_Backdoor_Attack_against_Text-to-Video_Generation_ICCV_2025_paper.html)　📅 2025-04　🏷 ICCV 2025

**关键词**：`attack`、`text-to-video`、`spatio-temporal trigger`、`moderation evasion`

👤 **作者**：Ruotong Wang、…、Baoyuan Wu

- 🎯 **研究动机**：T2V 生成含大量文本未指定的冗余元素，而内容审核多按单帧空间信息分析
- 🔬 **研究方法**：提出 BadVideo，以 Spatio-Temporal Composition 与 Dynamic Element Transformation 把恶意信息编码进冗余元素
- 📌 **结论**：高 ASR 下保持原语义与干净输入性能，成功绕过按帧审核系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-video (T2V) generative models have rapidly advanced and found widespread applications across fields like entertainment, education, and marketing. However, the adversarial vulnerabilities of these models remain rarely explored. We observe that in T2V generation tasks, the generated videos often contain substantial redundant information not explicitly specified in the text prompts, such as environmental elements, secondary objects, and additional details, providing opportunities for malicious attackers to embed hidden harmful content. Exploiting this inherent redundancy, we introduce BadVideo, the first backdoor attack framework tailored for T2V generation. Our attack focuses on designing target adversarial outputs through two key strategies: (1) Spatio-Temporal Composition, which combines different spatiotemporal features to encode malicious information; (2) Dynamic Element Transformation, which introduces transformations in redundant elements over time to convey malicious information. Based on these strategies, the attacker's malicious target seamlessly integrates with the user's textual instructions, providing high stealthiness. Moreover, by exploiting the temporal dimension of videos, our attack successfully evades traditional content moderation systems that primarily analyze spatial information within individual frames. Extensive experiments demonstrate that BadVideo achieves high attack success rates while preserving original semantics and maintaining excellent performance on clean inputs. Overall, our work reveals the adversarial vulnerability of T2V models, calling attention to potential risks and misuse. Our project page is at https://wrt2000.github.io/BadVideo2025/.

</details>

### 48. Control ControlNet: Multidimensional Backdoor Attack Based on ControlNet

🌐 [Project](https://doi.org/10.1007/978-981-96-7005-5_18)　📅 2024-12

**关键词**：`attack`、`ControlNet`、`semantic trigger`、`image trigger`

- 🎯 **研究动机**：ControlNet生态的多维后门攻击面缺分析
- 🔬 **研究方法**：CCBA结合semantic与image trigger多维投毒，adversarial fine-tuning保留被替换词语义
- 📌 **结论**：实现ControlNet文生图上的多维隐蔽后门

### 49. TrojanEdit: Multimodal backdoor attack against image editing model

📄 [arXiv](https://arxiv.org/abs/2411.14681) · 🌐 [Project](https://doi.org/10.1016/j.neucom.2026.133346)　📅 2024-11

**关键词**：`attack`、`image editing`、`multimodal trigger`、`modality balance`

👤 **作者**：Ji Guo、…、Hongwei Li

- 🎯 **研究动机**：扩散后门研究集中于单模态生成，多模态图像编辑未覆盖；简单叠加双模态触发会产生 modality bias
- 🔬 **研究方法**：TrojanEdit 训练时动态调整各模态梯度贡献，学习双触发齐现才激活的真多模态后门
- 📌 **结论**：多个编辑模型上实现均衡的多模态后门学习，保持干净编辑质量且攻击高效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal diffusion models for image editing generate outputs conditioned on both textual instructions and visual inputs, aiming to modify target regions while preserving the rest of the image. Although diffusion models have been shown to be vulnerable to backdoor attacks, existing efforts mainly focus on unimodal generative models and fail to address the unique challenges in multimodal image editing. In this paper, we present the first study of backdoor attacks on multimodal diffusion-based image editing models. We investigate the use of both textual and visual triggers to embed a backdoor that achieves high attack success rates while maintaining the model's normal functionality. However, we identify a critical modality bias. Simply combining triggers from different modalities leads the model to primarily rely on the stronger one, often the visual modality, which results in a loss of multimodal behavior and degrades editing quality. To overcome this issue, we propose TrojanEdit, a backdoor injection framework that dynamically adjusts the gradient contributions of each modality during training. This allows the model to learn a truly multimodal backdoor that activates only when both triggers are present. Extensive experiments on multiple image editing models show that TrojanEdit successfully integrates triggers from different modalities, achieving balanced multimodal backdoor learning while preserving clean editing performance and ensuring high attack effectiveness.

</details>

### 50. Watch the Watchers! On the Security Risks of Robustness-Enhancing Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2406.09669) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/li-changjiang)　📅 2024-06　🏷 USENIX Security 2025

**关键词**：`attack`、`diffusion purification`、`robustness certification`、`supply chain`

👤 **作者**：Changjiang Li、…、Ting Wang

- 🎯 **研究动机**：扩散模型被用作对抗净化与鲁棒性认证的防御工具，其自身安全风险未被探索
- 🔬 **研究方法**：DIFF2 将恶意扩散采样过程植入防御用扩散模型，把带触发器输入引向攻击者指定分布而干净输入功能不变
- 📌 **结论**：显著降低净化后准确率与认证准确率，警示依赖预训练扩散模型的防御供应链风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Thanks to their remarkable denoising capabilities, diffusion models are increasingly being employed as defensive tools to reinforce the security of other models, notably in purifying adversarial examples and certifying adversarial robustness. However, the security risks of these practices themselves remain largely unexplored, which is highly concerning. To bridge this gap, this work investigates the vulnerabilities of security-enhancing diffusion models. Specifically, we demonstrate that these models are highly susceptible to DIFF2, a simple yet effective backdoor attack, which substantially diminishes the security assurance provided by such models. Essentially, DIFF2 achieves this by integrating a malicious diffusion-sampling process into the diffusion model, guiding inputs embedded with specific triggers toward an adversary-defined distribution while preserving the normal functionality for clean inputs. Our case studies on adversarial purification and robustness certification show that DIFF2 can significantly reduce both post-purification and certified accuracy across benchmark datasets and models, highlighting the potential risks of relying on pre-trained diffusion models as defensive tools. We further explore possible countermeasures, suggesting promising avenues for future research.

</details>

### 51. Red-teaming Retrieval-Augmented Diffusion Models via Poisoning Knowledge Bases

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Lyu_Red-teaming_Retrieval-Augmented_Diffusion_Models_via_Poisoning_Knowledge_Bases_CVPR_2026_paper.html)　📅 2026-06　🏷 CVPR 2026

**关键词**：`attack`、`retrieval-augmented diffusion`、`knowledge-base poisoning`、`black-box attack`、`red teaming`

👤 **作者**：Xinqi Lyu、Yihao Liu、Dong Wang、Bin Xiao

- 🎯 **研究动机**：检索增强扩散模型（RAG-DM）的可信性缺乏研究，现有后门攻击只作用于生成或检索单阶段且限白盒，还受检索图与提示知识冲突困扰
- 🔬 **研究方法**：提出黑盒联合优化后门攻击 JOB：向知识库投少量目标类图像，通过多目标优化学习触发器，使检索偏向投毒图且生成对齐目标类
- 📌 **结论**：有效攻击黑盒 RAG-DM，成功率高并保持良性性能，优于 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented diffusion models (RAG-DMs) have been increasingly deployed across applications, reflecting a broader trend of adopting retrieval-augmented pipelines in AI agent systems and the emerging OpenClaw framework. Despite the success, their trustworthiness remains underexplored. Existing backdoor attacks focus on either manipulating the generation phase or the retrieval phase under the white-box setting, which suffer from knowledge conflicts between retrieved images and user prompts. To bridge this gap, we propose a novel red-teaming approach JOB, which is the first jointly optimized backdoor attack tailored to black-box RAG-DMs. Specifically, JOB poisons the knowledge base with a small number of target class images and learns a trigger through multi-objective optimization, steering retrieval toward poisoned images and aligning the generated outputs with the target class, while preserving benign performance. Experiments show that JOB effectively attacks black-box RAG-DMs, achieving high success rates and outperforming state-of-the-art baselines.

</details>

### 52. Unleashing Stealthy Backdoor Pandemic by Infecting a Single Diffusion Model

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Al_Nahian_Unleashing_Stealthy_Backdoor_Pandemic_by_Infecting_a_Single_Diffusion_Model_CVPR_2026_paper.html)　📅 2026-06　🏷 CVPR 2026

**关键词**：`attack`、`synthetic-data supply chain`、`backdoor propagation`、`downstream classifier`、`diffusion supply chain`、`model ecosystem`

👤 **作者**：Mohaiminul Al Nahian、Abeer Matar Almalky、Sabbir Ahmed、Abdullah Al Arafat、Mamshad Nayeem Rizve、Adnan Siraj Rakin

- 🎯 **研究动机**：从业者直接用第三方扩散模型生成合成训练数据，引入新威胁：被感染的单个扩散模型可把后门扩散到大量下游模型
- 🔬 **研究方法**：提出 Eidolon：无需攻击者参与下游训练即可把后门隐蔽转移到几乎无限多的下游模型，并定义引发后门疫情必须通过的四项测试
- 📌 **结论**：跨多基准数据集与架构的评估中仅该方法通过全部四项测试，造成广泛后门疫情

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The remarkable success of modern Deep Neural Networks (DNNs) can be primarily attributed to having access to compute resources and high-quality labeled data, which is often costly and challenging to acquire. Recently, text-to-image Diffusion Models (DMs) have emerged as powerful data generators to augment training datasets. Machine learning practitioners often utilize off-the-shelf third-party DMs for generating synthetic data without domain-specific expertise or adaptation. Such a practice leads to a novel and insidious threat: a diffusion model infected with a backdoor can effectively spread into a large number of downstream models, causing a backdoor pandemic. To achieve this for the first time, we propose Eidolon, designed and optimized to stealthily transfer the backdoor injected into a single diffusion model into virtually an unlimited number of downstream models without any active attacker role in the downstream training tasks. Proposed Eidolon not only makes the attack stealthier and effective, but it also enforces a strict threat model for injecting a backdoor into the downstream model compared to conventional backdoor attacks. We propose four necessary tests that a successful backdoor attack on the diffusion model should pass to cause a backdoor pandemic. Our evaluation across a wide range of benchmark datasets and model architectures exhibits that only our attack successfully passes these tests, causing widespread pandemic across many downstream models. Code is available at https://github.com/ML-Security-Research-LAB/Eidolon

</details>

### 53. DiffusionHijack: Supply-Chain PRNG Backdoor Attack on Diffusion Models and Quantum Random Number Defense

📄 [arXiv](https://arxiv.org/abs/2605.13115)　📅 2026-05

**关键词**：`attack`、`PRNG supply chain`、`randomness backdoor`、`QRNG defense`

👤 **作者**：Ziyang You、Liling Zheng、Xiaoke Yang、Xuxing Lu

- 🎯 **研究动机**：扩散模型依赖 PRNG 采样潜在噪声，该供应链层完全在神经网络计算图之外，现有模型审计与内容审核均无法检测
- 🔬 **研究方法**：DiffusionHijack 经被攻陷软件包注入恶意 PRNG，不改权重即可确定性复现攻击者内容；以 QRNG 替换作防御
- 📌 **结论**：Stable Diffusion v1.4、v1.5 与 SDXL 上 SSIM=1.00 完美复现并绕过 CLIP 安全检查器（98-100%）；QRNG 把输出相似度降到随机水平（SSIM 低于 0.20）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models depend on pseudo-random number generators (PRNGs) for latent noise sampling. We present DiffusionHijack, a supply-chain backdoor attack that hijacks the PRNG to deterministically control generated images. A malicious PRNG, injected via compromised packages, forces pixel-perfect reproduction of attacker-chosen content (SSIM = 1.00, N = 100 trials) on Stable Diffusion v1.4, v1.5, and SDXL -- without modifying model weights. The attack is inherently undetectable by existing model auditing and content moderation mechanisms, as it operates entirely outside the neural network computation graph. The attack remains effective under stochastic sampling (eta > 0), bypasses CLIP-based safety checkers (98-100% success), and operates independently of the user's prompt. As a countermeasure, we replace the PRNG with a quantum random number generator (QRNG), which provides information-theoretic unpredictability. Across N = 100 prompt-model combinations, QRNG defense completely neutralizes the attack, reducing output similarity to random baseline levels (SSIM < 0.20 for SD 1.x models, < 0.45 for SDXL). This work exposes a previously overlooked supply-chain vulnerability and offers a hardware-level fundamental mitigation for generative AI systems.

</details>

### 54. Data-Chain Backdoor: Do You Trust Diffusion Models as Generative Data Supplier?

📄 [arXiv](https://arxiv.org/abs/2512.15769)　📅 2025-12

**关键词**：`attack`、`synthetic-data chain`、`trigger memorization`、`backdoor propagation`

👤 **作者**：Junchi Lu、Xinke Li、Yuheng Liu、Qi Alfred Chen

- 🎯 **研究动机**：扩散模型合成数据被下游直接复用且常未经验证，可能成为后门沿供应链传播的隐蔽载体
- 🔬 **研究方法**：研究 Data-Chain Backdoor：让开源扩散模型凭分布拟合能力记忆并复现触发器，毒化随合成数据被下游模型继承；针对微调路径设计损失目标与触发器处理以增强触发保持
- 📌 **结论**：clean-label 场景下触发模式稳定保留于合成数据，攻击效力与常规后门相当且对数据效用影响可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing use of generative models such as diffusion models for synthetic data augmentation has greatly reduced the cost of data collection and labeling in downstream perception tasks. However, this new data source paradigm may introduce important security concerns. Publicly available generative models are often reused without verification, raising a fundamental question of their safety and trustworthiness. This work investigates backdoor propagation in such emerging generative data supply chain, namely, Data-Chain Backdoor (DCB). Specifically, we find that open-source diffusion models can become hidden carriers of backdoors. Their strong distribution-fitting ability causes them to memorize and reproduce backdoor triggers in generation, which are subsequently inherited by downstream models, resulting in severe security risks. This threat is particularly concerning under clean-label attack scenarios, as it remains effective while having negligible impact on the utility of the synthetic data. We study two attacker choices to obtain a backdoor-carried generator, training from scratch and fine-tuning. While naive fine-tuning leads to weak inheritance of the backdoor, we find that novel designs in the loss objectives and trigger processing can substantially improve the generator's ability to preserve trigger patterns, making fine-tuning a low-cost attack path. We evaluate the effectiveness of DCB under the standard augmentation protocol and further assess data-scarce settings. Across multiple trigger types, we observe that the trigger pattern can be consistently retained in the synthetic data with attack efficacy comparable to the conventional backdoor attack.

</details>

### 55. Retrievals Can Be Detrimental: Unveiling the Backdoor Vulnerability of Retrieval-Augmented Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2501.13340) · 🎓 [Official](https://aclanthology.org/2026.acl-long.242/)　📅 2025-01　🏷 ACL 2026

**关键词**：`attack`、`analysis`、`BadRDM`、`retriever poisoning`、`database poisoning`、`RAG security`

👤 **作者**：Hao Fang、…、Shu-Tao Xia

- 🎯 **研究动机**：检索增强扩散模型（RDM）的安全问题未被考察
- 🔬 **研究方法**：BadRDM 向检索库插入少量毒性代理图像，以恶意对比学习在 retriever 建立触发到代理的捷径，并用熵选择与生成增强强化
- 📌 **结论**：两大主流任务上攻击效果突出且保持良性效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DMs) have recently demonstrated remarkable generation capability. However, their training generally requires huge computational resources and large-scale datasets. To solve these, recent studies empower DMs with the advanced Retrieval-Augmented Generation (RAG) technique and propose retrieval-augmented diffusion models (RDMs). By incorporating rich knowledge from an auxiliary database, RAG enhances diffusion models' generation and generalization ability while significantly reducing model parameters. Despite the great success, RAG may introduce novel security issues that warrant further investigation. In this paper, we reveal that the RDM is susceptible to backdoor attacks by proposing a multimodal contrastive attack approach named BadRDM. Our framework fully considers RAG's characteristics and is devised to manipulate the retrieved items for given text triggers, thereby further controlling the generated contents. Specifically, we first insert a tiny portion of images into the retrieval database as target toxicity surrogates. Subsequently, a malicious variant of contrastive learning is adopted to inject backdoors into the retriever, which builds shortcuts from triggers to the toxicity surrogates. Furthermore, we enhance the attacks through novel entropy-based selection and generative augmentation strategies that can derive better toxicity surrogates. Extensive experiments on two mainstream tasks demonstrate the proposed BadRDM achieves outstanding attack effects while preserving the model's benign utility.

</details>

### 56. Backdooring Masked Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2605.19262)　📅 2026-05

**关键词**：`attack`、`masked diffusion LM`、`corruption process`、`parameter-efficient tuning`

👤 **作者**：Daniel Yiming Cao、Chengzhong Wang、Sheng-Yen Chou、Chengyu Huang、Pin-Yu Chen、Shengwei An

- 🎯 **研究动机**：面向 AR 或 Gaussian 扩散的后门不适用于离散状态腐蚀加迭代去噪的 masked diffusion LM
- 🔬 **研究方法**：SHADOWMASK 把 MDLM 前向腐蚀过程的全 mask 终态分布替换为 trigger-mask 混合先验，建立触发腐蚀态到攻击目标的专用去噪路径，并推导反向后验与连续时间训练目标
- 📌 **结论**：DiT MDLM 与 LLaDA-8B 上接近 100% ASR，远超标准数据投毒，clean 效用基本保持，对全参/PEFT 后续微调与代表性防御均鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Masked diffusion language models (MDLMs) are emerging as a compelling new paradigm for text generation, but their training-time security remains largely unexplored. Existing backdoor attacks on Gaussian diffusion models or autoregressive language models do not directly apply to MDLMs because MDLMs rely on discrete state corruption and iterative denoising rather than continuous noising or left-to-right prediction. In this work, we present the first systematic study of training-time backdoor attacks on MDLMs. We propose SHADOWMASK, a backdoor attack that modifies the MDLM forward corruption process by replacing the standard all-mask terminal distribution with a trigger-mask mixture prior. This creates a dedicated denoising pathway from trigger-corrupted states to attacker-specified targets while preserving clean denoising behavior. We further provide a principled mathematical formulation by defining the backdoored forward process, deriving the reverse-time posterior, and obtaining the continuous-time training objective. Evaluations on DiT-based MDLM and LLaDA-8B-Instruct across WikiText-103, OpenWebText, and Alpaca show that SHADOWMASK achieves near-100% attack success, substantially outperforms standard data poisoning, largely preserves clean utility, remains effective under full-model and parameter-efficient fine-tuning, and is robust against representative defenses.

</details>

### 57. BadDLM: Backdooring Diffusion Language Models with Diverse Targets

📄 [arXiv](https://arxiv.org/abs/2605.09397)　📅 2026-05

**关键词**：`attack`、`diffusion LM`、`induced masking`、`diverse payload`

👤 **作者**：Shengfang Zhai、…、Jiaheng Zhang

- 🎯 **研究动机**：扩散语言模型的后门风险未被探索，AR 后门操纵 next-token 预测的范式不适用于并行去噪生成
- 🔬 **研究方法**：BadDLM 的触发感知目标强调毒样本中目标相关位置，理论证明等价于在诱导前向掩码分布下训练；实例化概念注入、属性 steering、对齐绕过与代码 payload 四类目标
- 📌 **结论**：主流开源 DLM 上多目标攻击均强有效且良性效用基本保持，对面向 AR 后门的防御也免疫

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) have recently emerged as an alternative modeling paradigm to autoregressive (AR) language models, enabling parallel generation and bidirectional context modeling. Yet their security implications, particularly their vulnerability to backdoor attacks, remain underexplored. We propose BadDLM, a unified framework for studying backdoor attacks against DLMs with diverse targets. We introduce a trigger-aware training objective that emphasizes target-relevant positions in poisoned samples, and theoretically prove that this objective is equivalent to training under an induced forward masking distribution. Unlike backdoors in autoregressive models, which typically manipulate next-token prediction, this characterization indicates that BadDLM can implant backdoors by exploiting the forward masking process. We instantiate BadDLM across different target levels: concept injection (BadDLM_Concept), semantic attribute steering (BadDLM_Attribute), alignment bypass (BadDLM_Align), and code payload injection (BadDLM_Payload). Experiments on mainstream open-source DLMs show that BadDLM achieves strong attack effectiveness across diverse targets while largely preserving benign utility, and remains effective against defenses designed for AR backdoors. Our findings expose a new class of security risks in diffusion-based language generation and call for defenses tailored to DLM denoising dynamics.

</details>

### 58. Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models

📄 [arXiv](https://arxiv.org/abs/2602.22246)　📅 2026-02

**关键词**：`defense`、`multimodal diffusion LM`、`self-purification`、`visual token masking`、`DiSP`

👤 **作者**：Guangnian Wan、Qi Li、Gongfan Fang、Xinyin Ma、Xinchao Wang

- 🎯 **研究动机**：多模态扩散语言模型可被数据投毒植入后门，且尚无有效防御
- 🔬 **研究方法**：DiSP 发现推理时选择性掩蔽视觉 token 可中和触发行为，用受污染模型自身净化数据集再微调恢复，无需辅助模型或干净数据
- 📌 **结论**：ASR 从超 90% 通常降到 5% 以下，同时保持良性任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Diffusion Language Models (MDLMs) have recently emerged as a competitive alternative to their autoregressive counterparts. Yet their vulnerability to backdoor attacks remains largely unexplored. In this work, we show that well-established data-poisoning pipelines can successfully implant backdoors into MDLMs, enabling attackers to manipulate model behavior via specific triggers while maintaining normal performance on clean inputs. However, defense strategies effective to these models are yet to emerge. To bridge this gap, we introduce a backdoor defense framework for MDLMs named DiSP (Diffusion Self-Purification). DiSP is driven by a key observation: selectively masking certain vision tokens at inference time can neutralize a backdoored model's trigger-induced behaviors and restore normal functionality. Building on this, we purify the poisoned dataset using the compromised model itself, then fine-tune the model on the purified data to recover it to a clean one. Given such a specific design, DiSP can remove backdoors without requiring any auxiliary models or clean reference data. Extensive experiments demonstrate that our approach effectively mitigates backdoor effects, reducing the attack success rate (ASR) from over 90% to typically under 5%, while maintaining model performance on benign tasks.

</details>

### 59. Scaling Exposes the Trigger: Input-Level Backdoor Detection in Text-to-Image Diffusion Models via Cross-Attention Scaling

📄 [arXiv](https://arxiv.org/abs/2604.12446)　📅 2026-04

**关键词**：`detection`、`cross-attention scaling`、`input screening`、`trigger exposure`

👤 **作者**：Zida Li、Jun Li、Yuzhe Sha、Ziqiang Li、Lizhi Xiong、Zhangjie Fu

- 🎯 **研究动机**：T2I 扩散模型的输入级后门检测依赖可观察异常，在隐蔽的语义保持触发器下严重退化
- 🔬 **研究方法**：发现 cross-attention 缩放扰动下良性与后门输入的响应演化系统不同（CSRD）；SET 据此构建多尺度响应偏移特征并从少量干净样本学习紧凑良性响应空间
- 📌 **结论**：跨攻击与模型设定稳定超过基线，AUROC 提升 9.1%、ACC 提升 6.5%，隐式触发场景收益最大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) diffusion models have achieved remarkable success in image synthesis, but their reliance on large-scale data and open ecosystems introduces serious backdoor security risks. Existing defenses, particularly input-level methods, are more practical for deployment but often rely on observable anomalies that become unreliable under stealthy, semantics-preserving trigger designs. As modern backdoor attacks increasingly embed triggers into natural inputs, these methods degrade substantially, raising a critical question: can more stable, implicit, and trigger-agnostic differences between benign and backdoor inputs be exploited for detection? In this work, we address this challenge from an active probing perspective. We introduce controlled scaling perturbations on cross-attention and uncover a novel phenomenon termed Cross-Attention Scaling Response Divergence (CSRD), where benign and backdoor inputs exhibit systematically different response evolution patterns across denoising steps. Building on this insight, we propose SET, an input-level backdoor detection framework that constructs response-offset features under multi-scale perturbations and learns a compact benign response space from a small set of clean samples. Detection is then performed by measuring deviations from this learned space, without requiring prior knowledge of the attack or access to model training. Extensive experiments demonstrate that SET consistently outperforms existing baselines across diverse attack methods, trigger types, and model settings, with particularly strong gains under stealthy implicit-trigger scenarios. Overall, SET improves AUROC by 9.1% and ACC by 6.5% over the best baseline, highlighting its effectiveness and robustness for practical deployment.

</details>

### 60. BlackMirror: Black-Box Backdoor Detection for Text-to-Image Models via Instruction-Response Deviation

📄 [arXiv](https://arxiv.org/abs/2603.05921) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_BlackMirror_Black-Box_Backdoor_Detection_for_Text-to-Image_Models_via_Instruction-Response_Deviation_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`black-box audit`、`instruction-response deviation`、`T2I service`、`diffusion backdoor`、`response deviation`

👤 **作者**：Feiran Li、…、Qingming Huang

- 🎯 **研究动机**：基于图像一致性的黑盒后门检测难以泛化到生成结果视觉多样的新型攻击
- 🔬 **研究方法**：观察到仅部分语义模式被稳定操纵；BlackMirror 用 MirrorMatch 对齐指令与视觉模式检测语义偏差，MirrorVerify 验证偏差跨提示的稳定性
- 📌 **结论**：免训练即插即用，在大范围攻击上准确检测，可部署于 MaaS 应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper investigates the challenging task of detecting backdoored text-to-image models under black-box settings and introduces a novel detection framework BlackMirror. Existing approaches typically rely on analyzing image-level similarity, under the assumption that backdoor-triggered generations exhibit strong consistency across samples. However, they struggle to generalize to recently emerging backdoor attacks, where backdoored generations can appear visually diverse. BlackMirror is motivated by an observation: across backdoor attacks, {only partial semantic patterns within the generated image are steadily manipulated, while the rest of the content remains diverse or benign. Accordingly, BlackMirror consists of two components: MirrorMatch, which aligns visual patterns with the corresponding instructions to detect semantic deviations; and MirrorVerify, which evaluates the stability of these deviations across varied prompts to distinguish true backdoor behavior from benign responses. BlackMirror is a general, training-free framework that can be deployed as a plug-and-play module in Model-as-a-Service (MaaS) applications. Comprehensive experiments demonstrate that BlackMirror achieves accurate detection across a wide range of attacks. Code is available at https://github.com/Ferry-Li/BlackMirror.

</details>

### 61. PEPPER: Perception-Guided Perturbation for Robust Backdoor Defense in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2511.16830)　📅 2025-11

**关键词**：`defense`、`caption rewriting`、`perceptual equivalence`、`input purification`

👤 **作者**：Oscar Chew、Po-Yi Lu、Jayden Lin、Kuan-Hao Huang、Hsuan-Tien Lin

- 🎯 **研究动机**：T2I 后门效应会扩散到触发 token 的邻域，字符级扰动破坏正常语义且难防 encoder 攻击
- 🔬 **研究方法**：PEPPER 把 caption 重写为语义表达不同但视觉意图相似的版本并添加不显眼元素，逃离被攻击的嵌入邻域，无需训练或权重访问
- 📌 **结论**：对 text encoder 类攻击显著降低成功率并保持生成质量，可与任意现有防御叠加获得更强鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies show that text-to-image (T2I) diffusion models are vulnerable to backdoor attacks, where a trigger in the input prompt can steer generation toward harmful or unintended content. Beyond the trigger token itself, backdoor effects can spread to neighboring tokens in the text embedding space. To address this, we introduce PEPPER (PErcePtion-Guided PERturbation), a backdoor defense that rewrites the caption into a semantically distant yet visually similar caption while adding unobtrusive elements. With this strategy, PEPPER disrupts the trigger embedded in the input prompt, escapes the attacked neighborhood, and thereby achieves enhanced robustness without training or access to model weights. Experiments show that PEPPER is particularly effective against text encoder-based attacks, substantially reducing attack success while preserving generation quality. PEPPER can also be paired with any existing defenses yielding consistently stronger and generalizable robustness than any standalone method.

</details>

### 62. Dynamic Attention Analysis for Backdoor Detection in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2504.20518)　📅 2025-04

**关键词**：`detection`、`dynamic attention`、`input detection`、`model detection`

👤 **作者**：Zhongqi Wang、Jie Zhang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：已有后门检测依赖静态特征，忽视扩散模型的固有动态性
- 🔬 **研究方法**：发现后门样本在 EOS token 的 cross-attention 演化异常，提出 DAA-I（Frobenius 范数）与 DAA-S（图状态方程）量化动态异常
- 📌 **结论**：六种攻击场景平均 F1 79.27%、AUC 86.27%，显著超既有检测方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have revealed that text-to-image diffusion models are vulnerable to backdoor attacks, where attackers implant stealthy textual triggers to manipulate model outputs. Previous backdoor detection methods primarily focus on the static features of backdoor samples. However, a vital property of diffusion models is their inherent dynamism. This study introduces a novel backdoor detection perspective named Dynamic Attention Analysis (DAA), showing that these dynamic characteristics serve as better indicators for backdoor detection. Specifically, by examining the dynamic evolution of cross-attention maps, we observe that backdoor samples exhibit distinct feature evolution patterns at the $<$EOS$>$ token compared to benign samples. To quantify these dynamic anomalies, we first introduce DAA-I, which treats the tokens' attention maps as spatially independent and measures dynamic feature using the Frobenius norm. Furthermore, to better capture the interactions between attention maps and refine the feature, we propose a dynamical system-based approach, referred to as DAA-S. This model formulates the spatial correlations among attention maps using a graph-based state equation and we theoretically analyze the global asymptotic stability of this method. Extensive experiments across six representative backdoor attack scenarios demonstrate that our approach significantly surpasses existing detection methods, achieving an average F1 Score of 79.27% and an AUC of 86.27%. The code is available at https://github.com/Robin-WZQ/DAA.

</details>

### 63. Efficient Input-level Backdoor Defense on Text-to-Image Synthesis via Neuron Activation Variation

📄 [arXiv](https://arxiv.org/abs/2503.06453) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Zhai_Efficient_Input-level_Backdoor_Defense_on_Text-to-Image_Synthesis_via_Neuron_Activation_ICCV_2025_paper.html)　📅 2025-03　🏷 ICCV 2025

**关键词**：`detection`、`NaviT2I`、`neuron activation`、`early-step screening`

👤 **作者**：Shengfang Zhai、…、Jiaheng Zhang

- 🎯 **研究动机**：T2I 后门目标多样，完整生成后检测成本高
- 🔬 **研究方法**：发现触发 token 在扩散早期引起显著神经元激活变化，NaviT2I 据此分析输入 token 的激活变化提前拦截恶意输入
- 📌 **结论**：多数据集、多类 T2I 后门与 UNet/DiT 架构上效果与效率均领先，且抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, text-to-image (T2I) diffusion models have gained significant attention for their ability to generate high quality images reflecting text prompts. However, their growing popularity has also led to the emergence of backdoor threats, posing substantial risks. Currently, effective defense strategies against such threats are lacking due to the diversity of backdoor targets in T2I synthesis. In this paper, we propose NaviT2I, an efficient input-level backdoor defense framework against diverse T2I backdoors. Our approach is based on the new observation that trigger tokens tend to induce significant neuron activation variation in the early stage of the diffusion generation process, a phenomenon we term Early-step Activation Variation. Leveraging this insight, NaviT2I navigates T2I models to prevent malicious inputs by analyzing Neuron activation variations caused by input tokens. Extensive experiments show that NaviT2I significantly outperforms the baselines in both effectiveness and efficiency across diverse datasets, various T2I backdoors, and different model architectures including UNet and DiT. Furthermore, we show that our method remains effective under potential adaptive attacks.

</details>

### 64. Fine-grained Prompt Screening: Defending Against Backdoor Attack on Text-to-Image Diffusion Models

🎓 [Official](https://www.ijcai.org/proceedings/2025/68)　📅 2025　🏷 IJCAI 2025

**关键词**：`detection`、`prompt screening`、`semantics misalignment`、`trigger localization`

👤 **作者**：Yiran Xu、…、Xinpeng Zhang

- 🎯 **研究动机**：全局prompt或输出相似度难定位T2I后门的具体trigger
- 🔬 **研究方法**：GrainPS拆分prompt，比较语义相似度与cross-attention value space对齐
- 📌 **结论**：同时检测投毒输入并定位触发词

### 65. DADet: Safeguarding Image Conditional Diffusion Models against Adversarial and Backdoor Attacks via Diffusion Anomaly Detection

🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_DADet_Safeguarding_Image_Conditional_Diffusion_Models_against_Adversarial_and_Backdoor_ICCV_2025_paper.html)　📅 2025　🏷 ICCV 2025

**关键词**：`detection`、`diffusion anomaly`、`conditional diffusion`、`input screening`

👤 **作者**：Hongwei Yu、…、Jiansheng Chen

- 🎯 **研究动机**：图像条件扩散模型面对后门与对抗攻击高度脆弱，缺乏统一检测手段
- 🔬 **研究方法**：定义 diffusion anomaly 并分析其形成机制——扰动在反向过程被放大累积，引发偏离与同质化两种现象，据此同时检测两类攻击
- 📌 **结论**：后门检测在 MS COCO 与 CIFAR-10 上 F1 达 99%；对抗样本检测跨三种攻击与两任务 F1 超 84%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While image conditional diffusion models demonstrate impressive generation capabilities, they exhibit high vulnerability when facing backdoor and adversarial attacks. In this paper, we define a scenario named diffusion anomaly where the generated results of a reverse process under attack deviate significantly from the normal ones. By analyzing the underlying formation mechanism of the diffusion anomaly, we reveal how perturbations are amplified during the reverse process and accumulated in the results. Based on the analysis, we reveal the phenomena of divergence and homogeneity, which cause the diffusion process to deviate significantly from the normal process and to decline in diversity. Leveraging these two phenomena, we propose a method named Diffusion Anomaly Detection (DADet) to effectively detect both backdoor and adversarial attacks. Extensive experiments demonstrate that our proposal achieves excellent defense performance against backdoor and adversarial attacks. Specifically, for the backdoor attack detection, our method achieves an F1 score of 99% on different datasets, including MS COCO and CIFAR-10. For the detection of adversarial samples, the F1 score exceeds 84% across three adversarial attacks and two different tasks, evaluated on the MS COCO and Places365 datasets, respectively.

</details>

### 66. Defending Text-to-image Diffusion Models: Surprising Efficacy of Textual Perturbations Against Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2408.15721)　📅 2024-08　🏷 ECCV 2024 Workshop

**关键词**：`defense`、`text perturbation`、`input purification`、`T2I backdoor`

👤 **作者**：Oscar Chew、Po-Yi Lu、Jayden Lin、Hsuan-Tien Lin

- 🎯 **研究动机**：T2I 扩散模型的后门对策研究不足
- 🔬 **研究方法**：证明简单的文本扰动即可防御 SOTA 后门攻击，并从嵌入空间与 cross-attention 两个角度分析机理
- 📌 **结论**：以极小生成质量代价有效瓦解多类 T2I 触发器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models have been widely adopted in real-world applications due to their ability to generate realistic images from textual descriptions. However, recent studies have shown that these methods are vulnerable to backdoor attacks. Despite the significant threat posed by backdoor attacks on text-to-image diffusion models, countermeasures remain under-explored. In this paper, we address this research gap by demonstrating that state-of-the-art backdoor attacks against text-to-image diffusion models can be effectively mitigated by a surprisingly simple defense strategy - textual perturbation. Experiments show that textual perturbations are effective in defending against state-of-the-art backdoor attacks with minimal sacrifice to generation quality. We analyze the efficacy of textual perturbation from two angles: text embedding space and cross-attention maps. They further explain how backdoor attacks have compromised text-to-image diffusion models, providing insights for studying future attack and defense strategies. Our code is available at https://github.com/oscarchew/t2i-backdoor-defense.

</details>

### 67. UFID: A Unified Framework for Black-box Input-level Backdoor Detection on Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2404.01101) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/34941)　📅 2024-04　🏷 AAAI 2025

**关键词**：`detection`、`black-box input detection`、`causal confounder`、`Gaussian perturbation`

👤 **作者**：Zihan Guan、Mengxuan Hu、Sheng Li、Anil Vullikanti

- 🎯 **研究动机**：MaaS 黑盒输入级后门检测在生成任务上面临失败形态多样与多模态攻击面两大挑战
- 🔬 **研究方法**：UFID 基于因果分析：后门是 confounder 引入虚假输入-目标路径，对输入加 Gaussian perturbation 后路径不变，据此检测
- 📌 **结论**：条件与无条件扩散模型、多数据集上检测效果与运行效率俱佳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models are vulnerable to backdoor attacks, where malicious attackers inject backdoors by poisoning certain training samples during the training stage. This poses a significant threat to real-world applications in the Model-as-a-Service (MaaS) scenario, where users query diffusion models through APIs or directly download them from the internet. To mitigate the threat of backdoor attacks under MaaS, black-box input-level backdoor detection has drawn recent interest, where defenders aim to build a firewall that filters out backdoor samples in the inference stage, with access only to input queries and the generated results from diffusion models. Despite some preliminary explorations on the traditional classification tasks, these methods cannot be directly applied to the generative tasks due to two major challenges: (1) more diverse failures and (2) a multi-modality attack surface. In this paper, we propose a black-box input-level backdoor detection framework on diffusion models, called UFID. Our defense is motivated by an insightful causal analysis: Backdoor attacks serve as the confounder, introducing a spurious path from input to target images, which remains consistent even when we perturb the input samples with Gaussian noise. We further validate the intuition with theoretical analysis. Extensive experiments across different datasets on both conditional and unconditional diffusion models show that our method achieves superb performance on detection effectiveness and run-time efficiency.

</details>

### 68. DisDet: Exploring Detectability of Backdoor Attack on Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2402.02739) · 📝 [OpenReview](https://openreview.net/forum?id=SfqCaAOF1S)　📅 2024-02

**关键词**：`analysis`、`distribution discrepancy`、`trigger detection`、`adaptive attack`

👤 **作者**：Yang Sui、…、Bo Yuan

- 🎯 **研究动机**：后门扩散模型中投毒噪声输入的可检测性此前未被系统评估
- 🔬 **研究方法**：防御侧发现分布差异即可低成本检出既有触发器；攻击侧端到端学习贴近良性噪声分布的隐秘触发器以逃逸检测
- 📌 **结论**：分布差异检测对既有触发器 100% 检出；隐秘触发器获近 100% 检测通过率且攻防性能双高

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the exciting generative AI era, the diffusion model has emerged as a very powerful and widely adopted content generation and editing tool for various data modalities, making the study of their potential security risks very necessary and critical. Very recently, some pioneering works have shown the vulnerability of the diffusion model against backdoor attacks, calling for in-depth analysis and investigation of the security challenges of this popular and fundamental AI technique. In this paper, for the first time, we systematically explore the detectability of the poisoned noise input for the backdoored diffusion models, an important performance metric yet little explored in the existing works. Starting from the perspective of a defender, we first analyze the properties of the trigger pattern in the existing diffusion backdoor attacks, discovering the important role of distribution discrepancy in Trojan detection. Based on this finding, we propose a low-cost trigger detection mechanism that can effectively identify the poisoned input noise. We then take a further step to study the same problem from the attack side, proposing a backdoor attack strategy that can learn the unnoticeable trigger to evade our proposed detection scheme. Empirical evaluations across various diffusion models and datasets demonstrate the effectiveness of the proposed trigger detection and detection-evading attack strategy. For trigger detection, our distribution discrepancy-based solution can achieve a 100\% detection rate for the Trojan triggers used in the existing works. For evading trigger detection, our proposed stealthy trigger design approach performs end-to-end learning to make the distribution of poisoned noise input approach that of benign noise, enabling nearly 100\% detection pass rate with very high attack and benign performance for the backdoored diffusion models.

</details>

### 69. DiffSafeMerge: Mitigating Backdoor Inheritance in Diffusion Model Merging

📄 [arXiv](https://arxiv.org/abs/2608.09445)　📅 2026-08

**关键词**：`defense`、`model merging`、`backdoor inheritance`、`block shrinkage`

👤 **作者**：Jiayang Zhang、Ji Guo、Jiachen Li、Wenshu Fan、Wenbo Jiang

- 🎯 **研究动机**：扩散模型 checkpoint 合并假设来源良性，被攻陷的公开 checkpoint 可在生成正常时传递休眠后门，且不知攻击源时难以缓解
- 🔬 **研究方法**：DiffSafeMerge 用小规模无标签干净集与固定攻击无关压力探针给源模型块打分，把可疑贡献向可信参考收缩，并在干净去噪损失预算内选衰减强度
- 📌 **结论**：四攻击、两数据集、21 目标条件下，10/14 源用例预期合并本就零最差 ASR，其余四例（基线 ASR 48-100%）三种子下无目标匹配且平均 FID 最低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unconditional diffusion checkpoint merging assumes benign sources, yet a compromised public checkpoint can transfer a dormant backdoor while clean generation appears normal. Mitigation is difficult without knowing the compromised source, trigger, or target, and broad sanitization may degrade image quality. We introduce DiffSafeMerge (DSM), which uses a small unlabeled clean set and fixed, attack-agnostic stress probes to score source blocks, shrink suspicious contributions toward a trusted reference, and select attenuation under a clean denoising-loss budget. We evaluate four attacks, two datasets, and 21 target conditions. Intended merging already has zero worst-target ASR in 10 of 14 source cases; DSM preserves these outcomes and records no target match in the remaining four over three seeds, including three with baseline ASR of 48--100\%. Among methods with zero worst-target ASR on both datasets, DSM obtains the lowest case-averaged FID in the matched seed-0 comparison.

</details>

### 70. NeuroPatch: Lightweight diffusion model repair for backdoor attack mitigation based on neuron-level patching

🌐 [Project](https://doi.org/10.1016/j.neucom.2026.133283)　📅 2026-06

**关键词**：`defense`、`neuron patching`、`activation deviation`、`lightweight repair`

- 🎯 **研究动机**：扩散模型全量修复成本高且损害生成质量
- 🔬 **研究方法**：NeuroPatch定位activation deviation最大的少量神经元并挂接corrective controller
- 📌 **结论**：平均修复速度最高提升24倍且保持质量

### 71. A Unified Framework Based on Distribution Shift Modeling for Revealing and Eliminating Backdoor Attacks in Diffusion Models

🌐 [Project](https://doi.org/10.3390/app16105077)　📅 2026-05

**关键词**：`defense`、`distribution shift`、`trigger inversion`、`backdoor removal`

- 🎯 **研究动机**：扩散模型后门的检测与消除缺覆盖整条diffusion chain的统一框架
- 🔬 **研究方法**：DIFFDEFEND建模distribution shift的逐层传播，统一组合trigger inversion、检测与移除
- 📌 **结论**：实现对扩散后门的统一揭示与消除

### 72. Backdoor Sentinel: Detecting and Detoxifying Backdoors in Diffusion Models via Temporal Noise Consistency

📄 [arXiv](https://arxiv.org/abs/2602.01765)　📅 2026-02

**关键词**：`defense`、`temporal consistency`、`model detection`、`detoxification`

👤 **作者**：Bingzheng Wang、…、Wu Liu

- 🎯 **研究动机**：审计者无参数访问使白盒或查询密集检测不可行，解毒又陷效果与生成质量两难
- 🔬 **研究方法**：发现后门激活破坏相邻扩散时间步噪声预测一致性的 TNC 现象；TNC-Detect 用推理时相邻噪声统计检测并定位异常时间步，TNC-Detox 据此做触发无关的时间步感知修正
- 📌 **结论**：五种后门攻击上检测精度平均提升 11%、开销可忽略，98.5% 触发样本失效且生成质量仅轻微退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have been widely deployed in AIGC services, but their reliance on opaque training data exposes them to backdoor attacks. In practical auditing scenarios, auditors are typically unable to access model parameters due to intellectual property protection, making white-box or query-intensive detection impractical. After detection, existing detoxification approaches are trapped in a dilemma between detoxification effectiveness and generation quality for service providers. We reveal Temporal Noise Consistency (TNC), a previously unreported phenomenon in which backdoor activation disrupts the consistency of noise predictions between adjacent diffusion timesteps within specific temporal segments, while clean inputs remain stable. Based on this finding, we propose TNC-Defense, a closed-loop framework for gray-box backdoor detection and model repair. Specifically, TNC-Detect (for auditors) uses inference-stage adjacent-noise statistics to detect backdoors and precisely localize anomalous timesteps without model-weight access. TNC-Detox (for service providers) utilizes these locations to perform trigger-agnostic, timestep-aware correction of the generation path, suppressing backdoor behavior while reducing detoxification cost. Across five representative backdoor attacks and state-of-the-art defenses, TNC-Defense improves the average detection accuracy by $11\%$ with negligible additional overhead, and invalidates an average of $98.5\%$ of triggered samples with only a mild degradation in generation quality. Our code is publicly available at: https://github.com/binzhwang/TNC-Defense.

</details>

### 73. AutoDebias: An Automated Framework for Detecting and Mitigating Backdoor Biases in Text-to-Image Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_AutoDebias_An_Automated_Framework_for_Detecting_and_Mitigating_Backdoor_Biases_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`defense`、`backdoor bias`、`VLM auditing`、`automated mitigation`、`text-to-image backdoor`、`bias trigger`

- 🎯 **研究动机**：文生图模型的backdoor bias难自动发现与缓解
- 🔬 **研究方法**：AutoDebias自动检测偏置trigger并实施针对性缓解
- 📌 **结论**：实现T2I后门偏置的自动化审计与修复

### 74. Sealing The Backdoor: Unlearning Adversarial Text Triggers In Diffusion Models Using Knowledge Distillation

📄 [arXiv](https://arxiv.org/abs/2508.18235)　📅 2025-08

**关键词**：`defense`、`trigger unlearning`、`self-distillation`、`cross-attention guidance`

👤 **作者**：Ashwath Vaithinathan Aravindan、Abha Jha、Matthew Salaway、Atharva Sandeep Bhide、Duygu Nur Yaldiz

- 🎯 **研究动机**：文本后门防御在分类模型上成熟，生成式扩散模型缺乏有效缓解手段
- 🔬 **研究方法**：提出 SKD-CAG：利用无触发时后门模型仍产生干净输出的特性做自知识蒸馏，并以 cross-attention 机制在注意力层面中和后门影响
- 📌 **结论**：像素后门移除准确率 100%、风格后门 93%，图像保真不受损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models have revolutionized generative AI, but their vulnerability to backdoor attacks poses significant security risks. Adversaries can inject imperceptible textual triggers into training data, causing models to generate manipulated outputs. Although text-based backdoor defenses in classification models are well-explored, generative models lack effective mitigation techniques against. We address this by selectively erasing the model's learned associations between adversarial text triggers and poisoned outputs, while preserving overall generation quality. Our approach, Self-Knowledge Distillation with Cross-Attention Guidance (SKD-CAG), uses knowledge distillation to guide the model in correcting responses to poisoned prompts while maintaining image quality by exploiting the fact that the backdoored model still produces clean outputs in the absence of triggers. Using the cross-attention mechanism, SKD-CAG neutralizes backdoor influences at the attention level, ensuring the targeted removal of adversarial effects. Extensive experiments show that our method outperforms existing approaches, achieving removal accuracy 100\% for pixel backdoors and 93\% for style-based attacks, without sacrificing robustness or image fidelity. Our findings highlight targeted unlearning as a promising defense to secure generative models. Code and model weights can be found at https://github.com/Mystic-Slice/Sealing-The-Backdoor .

</details>

### 75. Backdoor Defense for Text Encoders in Text-to-Image Generative Models

🌐 [Project](https://doi.org/10.1109/TDSC.2025.3595864)　📅 2025-08

**关键词**：`defense`、`text encoder`、`few-shot repair`、`history-based repair`

- 🎯 **研究动机**：大规模图文训练下传统防御难用于text encoder后门
- 🔬 **研究方法**：提出few-shot与history-based修复，以trigger与clean embedding一致性或历史数据自愈
- 📌 **结论**：低成本移除后门且保持生成质量

### 76. Backdoor Defense in Diffusion Models via Spatial Attention Unlearning

📄 [arXiv](https://arxiv.org/abs/2504.18563)　📅 2025-04

**关键词**：`defense`、`spatial attention`、`unlearning`、`model repair`

👤 **作者**：Abha Jha、Ashwath Vaithinathan Aravindan、Matthew Salaway、Atharva Sandeep Bhide、Duygu Nur Yaldiz

- 🎯 **研究动机**：生成模型高维输出空间令后门防御困难，扩散模型防御研究不足
- 🔬 **研究方法**：提出 SAU，利用潜空间操控与空间注意力机制隔离并移除后门触发器的潜在表示
- 📌 **结论**：对像素与风格触发器均达 100% 触发移除，CLIP score 0.7023 优于既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models are increasingly vulnerable to backdoor attacks, where malicious modifications to the training data cause the model to generate unintended outputs when specific triggers are present. While classification models have seen extensive development of defense mechanisms, generative models remain largely unprotected due to their high-dimensional output space, which complicates the detection and mitigation of subtle perturbations. Defense strategies for diffusion models, in particular, remain under-explored. In this work, we propose Spatial Attention Unlearning (SAU), a novel technique for mitigating backdoor attacks in diffusion models. SAU leverages latent space manipulation and spatial attention mechanisms to isolate and remove the latent representation of backdoor triggers, ensuring precise and efficient removal of malicious effects. We evaluate SAU across various types of backdoor attacks, including pixel-based and style-based triggers, and demonstrate its effectiveness in achieving 100% trigger removal accuracy. Furthermore, SAU achieves a CLIP score of 0.7023, outperforming existing methods while preserving the model's ability to generate high-quality, semantically aligned images. Our results show that SAU is a robust, scalable, and practical solution for securing text-to-image diffusion models against backdoor attacks.

</details>

### 77. A Dual-Purpose Framework for Backdoor Defense and Backdoor Amplification in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2502.19047) · 🌐 [Project](https://doi.org/10.1109/TIFS.2026.3675424)　📅 2025-02

**关键词**：`defense`、`PureDiffusion`、`trigger inversion`、`backdoor amplification`

👤 **作者**：Vu Tuan Truong、Long Bao Le

- 🎯 **研究动机**：扩散模型触发器反演常计算昂贵且恢复信号弱
- 🔬 **研究方法**：PureDiffusion 用两个新损失（多时间步分布位移与去噪一致性）反演触发器用于检测；同一算法也可反向强化原触发器放大攻击
- 📌 **结论**：检测接近满分、大幅超越现有防御；攻击侧把 ASR 提至近 100% 且训练时间最多缩短 20 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have emerged as state-of-the-art generative frameworks, excelling in producing high-quality multi-modal samples. However, recent studies have revealed their vulnerability to backdoor attacks, where backdoored models generate specific, undesirable outputs called backdoor target (e.g., harmful images) when a pre-defined trigger is embedded to their inputs. In this paper, we propose PureDiffusion, a dual-purpose framework that simultaneously serves two contrasting roles: backdoor defense and backdoor attack amplification. For defense, we introduce two novel loss functions to invert backdoor triggers embedded in diffusion models. The first leverages trigger-induced distribution shifts across multiple timesteps of the diffusion process, while the second exploits the denoising consistency effect when a backdoor is activated. Once an accurate trigger inversion is achieved, we develop a backdoor detection method that analyzes both the inverted trigger and the generated backdoor targets to identify backdoor attacks. In terms of attack amplification with the role of an attacker, we describe how our trigger inversion algorithm can be used to reinforce the original trigger embedded in the backdoored diffusion model. This significantly boosts attack performance while reducing the required backdoor training time. Experimental results demonstrate that PureDiffusion achieves near-perfect detection accuracy, outperforming existing defenses by a large margin, particularly against complex trigger patterns. Additionally, in an attack scenario, our attack amplification approach elevates the attack success rate (ASR) of existing backdoor attacks to nearly 100\% while reducing training time by up to 20x.

</details>

### 78. TERD: A Unified Framework for Safeguarding Diffusion Models Against Backdoors

📄 [arXiv](https://arxiv.org/abs/2409.05294) · 🌐 [Project](https://proceedings.mlr.press/v235/mo24a.html)　📅 2024-09　🏷 ICML 2024

**关键词**：`defense`、`trigger reversion`、`input detection`、`model detection`

👤 **作者**：Yichuan Mo、Hui Huang、Mingjie Li、Ang Li、Yisen Wang

- 🎯 **研究动机**：扩散后门攻击形式各异，缺乏统一建模下的触发器反演与输入级检测
- 🔬 **研究方法**：TERD 统一建模现有攻击导出可反演损失，先验噪声采样加微分多步采样器精化触发器；提出首个输入检测与基于 KL 散度的模型检测
- 📌 **结论**：各分辨率数据集上 TPR 与 TNR 均达 100%，且可适配其他 SDE 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have achieved notable success in image generation, but they remain highly vulnerable to backdoor attacks, which compromise their integrity by producing specific undesirable outputs when presented with a pre-defined trigger. In this paper, we investigate how to protect diffusion models from this dangerous threat. Specifically, we propose TERD, a backdoor defense framework that builds unified modeling for current attacks, which enables us to derive an accessible reversed loss. A trigger reversion strategy is further employed: an initial approximation of the trigger through noise sampled from a prior distribution, followed by refinement through differential multi-step samplers. Additionally, with the reversed trigger, we propose backdoor detection from the noise space, introducing the first backdoor input detection approach for diffusion models and a novel model detection algorithm that calculates the KL divergence between reversed and benign distributions. Extensive evaluations demonstrate that TERD secures a 100% True Positive Rate (TPR) and True Negative Rate (TNR) across datasets of varying resolutions. TERD also demonstrates nice adaptability to other Stochastic Differential Equation (SDE)-based models. Our code is available at https://github.com/PKU-ML/TERD.

</details>

### 79. Diff-Cleanse: Identifying and Mitigating Backdoor Attacks in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2407.21316)　📅 2024-07

**关键词**：`defense`、`trigger inversion`、`structural pruning`、`model repair`

👤 **作者**：Jiang Hao、Xiao Jin、Hu Xiaoguang、Chen Tianyou、Zhao Jiajia

- 🎯 **研究动机**：已有防御无法可靠净化被 SOTA 攻击后门的扩散模型
- 🔬 **研究方法**：Diff-Cleanse 两阶段：触发器反演检测后门，再用结构剪枝消除后门
- 📌 **结论**：数百个 DM（3 种攻击、大范围超参）上检测准确率近 100%，后门影响被有效缓解且良性性能损失极小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DMs) are regarded as one of the most advanced generative models today, yet recent studies suggest that they are vulnerable to backdoor attacks, which establish hidden associations between particular input patterns and model behaviors, compromising model integrity by causing undesirable actions with manipulated inputs. This vulnerability poses substantial risks, including reputational damage to model owners and the dissemination of harmful content. To mitigate the threat of backdoor attacks, there have been some investigations on backdoor detection and model repair. However, previous work fails to reliably purify the models backdoored by state-of-the-art attack methods, rendering the field much underexplored. To bridge this gap, we introduce Diff-Cleanse, a novel two-stage backdoor defense framework specifically designed for DMs. The first stage employs a novel trigger inversion technique to reconstruct the trigger and detect the backdoor, and the second stage utilizes a structural pruning method to eliminate the backdoor. We evaluate our framework on hundreds of DMs that are attacked by three existing backdoor attack methods with a wide range of hyperparameter settings. Extensive experiments demonstrate that Diff-Cleanse achieves nearly 100\% detection accuracy and effectively mitigates backdoor impacts, preserving the model's benign performance with minimal compromise. Our code is avaliable at https://github.com/shymuel/diff-cleanse.

</details>

### 80. T2IShield: Defending Against Backdoors on Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2407.04215) · 🌐 [Project](https://eccv.ecva.net/virtual/2024/poster/172)　📅 2024-07　🏷 ECCV 2024

**关键词**：`defense`、`cross-attention assimilation`、`trigger localization`、`backdoor mitigation`

👤 **作者**：Zhongqi Wang、Jie Zhang、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：T2I 扩散模型后门的检测、定位与缓解缺乏综合方案
- 🔬 **研究方法**：发现触发器在 cross-attention 上引起同化现象；T2IShield 用 Frobenius 范数截断与协方差判别分析检测、二分搜索定位、概念编辑缓解
- 📌 **结论**：检测 F1 达 88.9%、定位 F1 达 86.4%，使 99% 毒样本失效且计算开销低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While text-to-image diffusion models demonstrate impressive generation capabilities, they also exhibit vulnerability to backdoor attacks, which involve the manipulation of model outputs through malicious triggers. In this paper, for the first time, we propose a comprehensive defense method named T2IShield to detect, localize, and mitigate such attacks. Specifically, we find the "Assimilation Phenomenon" on the cross-attention maps caused by the backdoor trigger. Based on this key insight, we propose two effective backdoor detection methods: Frobenius Norm Threshold Truncation and Covariance Discriminant Analysis. Besides, we introduce a binary-search approach to localize the trigger within a backdoor sample and assess the efficacy of existing concept editing methods in mitigating backdoor attacks. Empirical evaluations on two advanced backdoor attack scenarios show the effectiveness of our proposed defense method. For backdoor sample detection, T2IShield achieves a detection F1 score of 88.9$\%$ with low computational cost. Furthermore, T2IShield achieves a localization F1 score of 86.4$\%$ and invalidates 99$\%$ poisoned samples. Codes are released at https://github.com/Robin-WZQ/T2IShield.

</details>

### 81. Elijah: Eliminating Backdoors Injected in Diffusion Models via Distribution Shift

📄 [arXiv](https://arxiv.org/abs/2312.00050) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/28958)　📅 2023-11　🏷 AAAI 2024

**关键词**：`defense`、`distribution shift`、`trigger inversion`、`backdoor elimination`

👤 **作者**：Shengwei An、…、Xiangyu Zhang

- 🎯 **研究动机**：扩散模型的后门攻击已被证实，检测与移除防御却缺位
- 🔬 **研究方法**：Elijah 利用触发器引起的 distribution shift 反演检测后门并微调移除，覆盖 DDPM、NCSN、LDM 三类模型、13 种 sampler 与 3 种攻击
- 📌 **结论**：数百个 DM 上检测准确率接近 100%，后门效应压至近零且不明显牺牲效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DM) have become state-of-the-art generative models because of their capability to generate high-quality images from noises without adversarial training. However, they are vulnerable to backdoor attacks as reported by recent studies. When a data input (e.g., some Gaussian noise) is stamped with a trigger (e.g., a white patch), the backdoored model always generates the target image (e.g., an improper photo). However, effective defense strategies to mitigate backdoors from DMs are underexplored. To bridge this gap, we propose the first backdoor detection and removal framework for DMs. We evaluate our framework Elijah on hundreds of DMs of 3 types including DDPM, NCSN and LDM, with 13 samplers against 3 existing backdoor attacks. Extensive experiments show that our approach can have close to 100% detection accuracy and reduce the backdoor effects to close to zero without significantly sacrificing the model utility.

</details>

### 82. BackdoorDM: A Comprehensive Benchmark for Backdoor Learning on Diffusion Model

📄 [arXiv](https://arxiv.org/abs/2502.11798) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ba9b181cd30b4f1819583be24fdfeb17-Abstract-Datasets_and_Benchmarks_Track.html)　📅 2025-02　🏷 NeurIPS 2025

**关键词**：`benchmark`、`attack-defense evaluation`、`unified metrics`、`diffusion security`

👤 **作者**：Weilin Lin、Nanjun Zhou、Yanyun Wang、Jianze Li、Hui Xiong、Li Liu

- 🎯 **研究动机**：扩散模型后门攻防方法分散，缺乏统一基准导致无法公平比较
- 🔬 **研究方法**：BackdoorDM 集成 9 种 SOTA 攻击、4 种防御与 3 种可视化工具，统一 3 类攻击与 5 类目标的形式化及基于 MLLM 的统一评测
- 📌 **结论**：综合评测得出多项重要结论，促进 AIGC 可信生态建设

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor learning is a critical research topic for understanding the vulnerabilities of deep neural networks. While the diffusion model (DM) has been broadly deployed in public over the past few years, the understanding of its backdoor vulnerability is still in its infancy compared to the extensive studies in discriminative models. Recently, many different backdoor attack and defense methods have been proposed for DMs, but a comprehensive benchmark for backdoor learning on DMs is still lacking. This absence makes it difficult to conduct fair comparisons and thorough evaluations of the existing approaches, thus hindering future research progress. To address this issue, we propose \textit{BackdoorDM}, the first comprehensive benchmark designed for backdoor learning on DMs. It comprises nine state-of-the-art (SOTA) attack methods, four SOTA defense strategies, and three useful visualization analysis tools. We first systematically classify and formulate the existing literature in a unified framework, focusing on three different backdoor attack types and five backdoor target types, which are restricted to a single type in discriminative models. Then, we systematically summarize the evaluation metrics for each type and propose a unified backdoor evaluation method based on multimodal large language model (MLLM). Finally, we conduct a comprehensive evaluation and highlight several important conclusions. We believe that BackdoorDM will help overcome current barriers and contribute to building a trustworthy artificial intelligence generated content (AIGC) community. The codes are released in https://github.com/linweiii/BackdoorDM.

</details>

### 83. Attacks and Defenses for Generative Diffusion Models: A Comprehensive Survey

📄 [arXiv](https://arxiv.org/abs/2408.03400) · 🌐 [Project](https://doi.org/10.1145/3721479)　📅 2024-08

**关键词**：`survey`、`diffusion security`、`backdoor taxonomy`、`defense taxonomy`

👤 **作者**：Vu Tuan Truong、Luan Ba Dang、Long Bao Le

- 🎯 **研究动机**：扩散模型攻击研究分散，缺乏覆盖攻防两面的系统综述
- 🔬 **研究方法**：按 DDPM、DDIM、NCSN、SDE 与多模态条件五类模型，梳理对抗攻击、成员推断、后门注入及对策
- 📌 **结论**：总结开放挑战并展望扩散安全研究方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models (DMs) have achieved state-of-the-art performance on various generative tasks such as image synthesis, text-to-image, and text-guided image-to-image generation. However, the more powerful the DMs, the more harmful they potentially are. Recent studies have shown that DMs are prone to a wide range of attacks, including adversarial attacks, membership inference, backdoor injection, and various multi-modal threats. Since numerous pre-trained DMs are published widely on the Internet, potential threats from these attacks are especially detrimental to the society, making DM-related security a worth investigating topic. Therefore, in this paper, we conduct a comprehensive survey on the security aspect of DMs, focusing on various attack and defense methods for DMs. First, we present crucial knowledge of DMs with five main types of DMs, including denoising diffusion probabilistic models, denoising diffusion implicit models, noise conditioned score networks, stochastic differential equations, and multi-modal conditional DMs. We further survey a variety of recent studies investigating different types of attacks that exploit the vulnerabilities of DMs. Then, we thoroughly review potential countermeasures to mitigate each of the presented threats. Finally, we discuss open challenges of DM-related security and envision certain research directions for this topic.

</details>
