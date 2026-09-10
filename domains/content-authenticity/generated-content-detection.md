# AI-Generated Content Detection

[返回上级目录](README.md)

## 研究方向

研究对 AI 生成或机器改写的文本、代码、图像、视频和音频进行检测与来源判断，重点考察跨 generator、跨 domain、低质量压缩、局部编辑和对抗规避下的泛化。

## 研究脉络

- **封闭集检测：** 早期 detector 依赖特定生成器留下的 token 或频谱 artifact。
- **跨生成器泛化：** Representation learning、real-centric modeling 与 source disentanglement 减少对单一 generator 的依赖。
- **开放世界与对抗：** 研究加入局部编辑、paraphrase、compression、hard negative 和 adversarial example，检验现实失效。
- **当前边界：** 未知生成器、人工编辑链与低 base-rate 部署仍使校准和误报控制困难。

## AI-Generated Image 与 Multimodal Detection

### 1. Prior-Conditioned Gaussian Discriminants for Generalizable AI-generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2608.18523) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5771)　📅 2026-08　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated image detection`、`AI-generated content`、`cross-generator detection`、`distribution shift`、`Gaussian discrimination`

👤 **作者**：Shashank Kotyan、Makoto Shing、Yuki Imajuku、Rujikorn Charakorn、Tarin Clanuwat

- 🎯 **研究动机**：AI 生成图像检测在生成器、prompt 风格与源域同时偏移时常失败，分类头训练何时超越现代特征的固有可分性未知
- 🔬 **研究方法**：先验条件高斯判别阶梯：嵌套协方差假设下由一/二阶特征统计闭式构造头；Percept-Lens 协议统一 39 个公开数据集 710 万图
- 📌 **结论**：匹配先验与编码器时最优 rung 常与已发布检测头竞争甚至超越；对训练先验强敏感、矩头数据高效——主张（先验、编码器、头）级报告与更强解析基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion-based generators have made synthetic images ubiquitous, but detectors often fail under simultaneous shifts in generator, prompt/style, and source-domain. We study AI-generated image detection as a transfer system described by training prior, frozen encoder feature space, and decision rule, and ask when classifier head training adds value beyond what is already separable in modern features. As a controlled diagnostic, we fit a prior-conditioned Gaussian discriminant ladder: closed-form heads built from first- and second-order feature statistics under nested covariance assumptions. On Percept-Lens, a unified protocol over 39 public datasets (7.1 million images), the best rung is frequently competitive with, and sometimes exceeds, released AI-generated image detector heads when matched on both prior and encoder. We further quantify strong sensitivity to the training prior, data-efficiency of moment-based heads, and representation dependence of Gaussian shift metrics, motivating (prior, encoder, head)-level reporting and stronger analytical baselines for AIGI transfer.

</details>

### 2. Training-Free Reconstruction-Based AI-Generated Image Detectors Are Inherently Vulnerable to Adversarial Examples

📄 [arXiv](https://arxiv.org/abs/2608.16646) · 🌐 [Project](https://warwick.ac.uk/fac/sci/dcs/research/siplab/AI4MFDD2026/program/)　📅 2026-08

**关键词**：`detection`、`AI-generated content`、`adversarial robustness`、`cross-generator detection`

👤 **作者**：Roman Demchenko、Jonas Ricker、Asja Fischer

- 🎯 **研究动机**：基于自编码重建误差的免训练 AI 图像检测器机制迥异于分类器，其对抗鲁棒性未知
- 🔬 **研究方法**：提出两种针对重建误差检测器的攻击：构造不可感知对抗样本人为拉大原图与重建的距离，使假图被判为真
- 📌 **结论**：三个 SOTA 生成器、三个检测器上检测性能显著下降且经真实世界退化仍有效；对抗样本跨检测器自然迁移——重建式检测器存在固有漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The impressive visual quality and ubiquity of AI-generated images call for reliable and robust detection methods. Reconstruction-based detectors have emerged as a promising direction for transparent and training-free identification of synthetic images. However, due to their fundamentally different mode of operation (compared to standard, classifier-based methods), little is known about their adversarial robustness. In this work, we propose two novel attack methods targeted at detectors that leverage autoencoder reconstruction error. We find that by constructing imperceptible adversarial examples, the distance between original and reconstruction can be artificially increased, causing fake images to be wrongly classified as real. Our evaluation including images from three state-of-the-art generators and three detectors demonstrates that detection performance is significantly decreased, even if attacked images additionally undergo real-world degradations. Critically, our adversarial examples naturally transfer across detectors, as they all share the same principle, pointing towards an inherent vulnerability of reconstruction-based detectors.

</details>

### 3. UniGenDet: A Unified Generative-Discriminative Framework for Co-Evolutionary Image Generation and Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2604.21904) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_UniGenDet_A_Unified_Generative-Discriminative_Framework_for_Co-Evolutionary_Image_Generation_and_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`detection`、`generated image`、`co-evolution`、`generator-aware training`

👤 **作者**：Yanran Zhang、…、Jie Zhou

- 🎯 **研究动机**：图像生成与生成图像检测独立演化、架构割裂，对抗信息的协同潜力未被利用
- 🔬 **研究方法**：UniGenDet 统一生成与判别框架，设计共生多模态自注意力与统一微调，并以检测器感知的生成对齐实现信息互换
- 📌 **结论**：多数据集上达到 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, significant progress has been made in both image generation and generated image detection. Despite their rapid, yet largely independent, development, these two fields have evolved distinct architectural paradigms: the former predominantly relies on generative networks, while the latter favors discriminative frameworks. A recent trend in both domains is the use of adversarial information to enhance performance, revealing potential for synergy. However, the significant architectural divergence between them presents considerable challenges. Departing from previous approaches, we propose UniGenDet: a Unified generative-discriminative framework for co-evolutionary image Generation and generated image Detection. To bridge the task gap, we design a symbiotic multimodal self-attention mechanism and a unified fine-tuning algorithm. This synergy allows the generation task to improve the interpretability of authenticity identification, while authenticity criteria guide the creation of higher-fidelity images. Furthermore, we introduce a detector-informed generative alignment mechanism to facilitate seamless information exchange. Extensive experiments on multiple datasets demonstrate that our method achieves state-of-the-art performance. Code: \href{https://github.com/Zhangyr2022/UniGenDet}{https://github.com/Zhangyr2022/UniGenDet}.

</details>

### 4. TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2602.21716) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64870)　📅 2026-02　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Wenbin Wang、…、Yong Luo

- 🎯 **研究动机**：伪影特征内部相似度高，softmax 后注意力图趋同造成注意力稀释，阻碍与语义特征有效融合
- 🔬 **研究方法**：TranX-Adapter 用以两类预测概率的 JS 散度为代价矩阵的任务感知最优传输把伪影信息迁入语义特征，X-Fusion 用交叉注意力反向迁移
- 📌 **结论**：在多个先进 MLLM 的 AIGI 检测基准上带来一致显著提升（准确率最高增 6%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Rapid advances in AI-generated image (AIGI) technology enable highly realistic synthesis, threatening public information integrity and security. Recent studies have demonstrated that incorporating texture-level artifact features alongside semantic features into multimodal large language models (MLLMs) can enhance their AIGI detection capability. However, our preliminary analyses reveal that artifact features exhibit high intra-feature similarity, leading to an almost uniform attention map after the softmax operation. This phenomenon causes attention dilution, thereby hindering effective fusion between semantic and artifact features. To overcome this limitation, we propose a lightweight fusion adapter, TranX-Adapter, which integrates a Task-aware Optimal-Transport Fusion that leverages the Jensen-Shannon divergence between artifact and semantic prediction probabilities as a cost matrix to transfer artifact information into semantic features, and an X-Fusion that employs cross-attention to transfer semantic information into artifact features. Experiments on standard AIGI detection benchmarks upon several advanced MLLMs, show that our TranX-Adapter brings consistent and significant improvements (up to +6% accuracy).

</details>

### 5. A Difference-in-Difference Approach to Detecting AI-Generated Images

📄 [arXiv](https://arxiv.org/abs/2602.23732) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_A_Difference-in-Difference_Approach_to_Detecting_AI-Generated_Images_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated image`、`difference-in-difference`、`generator generalization`

👤 **作者**：Xinyi Qi、Kai Ye、Chengchun Shi、Ying Yang、Hongyi Zhou、Jin Zhu

- 🎯 **研究动机**：基于重建误差的检测器随 AI 生成图像愈发逼真而失效
- 🔬 **研究方法**：提出 difference-in-difference 方法：不直接用重建误差，而计算其差分（二阶差分）以做方差缩减
- 📌 **结论**：实现对 AI 生成图像的强跨生成器泛化检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models are able to produce AI-generated images that are almost indistinguishable from real ones. This raises concerns about their potential misuse and poses substantial challenges for detecting them. Many existing detectors rely on reconstruction error -- the difference between the input image and its reconstructed version -- as the basis for distinguishing real from fake images. However, these detectors become less effective as modern AI-generated images become increasingly similar to real ones. To address this challenge, we propose a novel difference-in-difference method. Instead of directly using the reconstruction error (a first-order difference), we compute the difference in reconstruction error -- a second-order difference -- for variance reduction and improving detection accuracy. Extensive experiments demonstrate that our method achieves strong generalization performance, enabling reliable detection of AI-generated images in the era of generative AI.

</details>

### 6. Where Detectors Fail: Probing Generative Space for Generalizable AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2605.24906) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62485)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`model editing`

👤 **作者**：Zijie Cao、Weijie Tu、Yao Xiao、Weijian Deng、Liang Lin、Pengxu Wei

- 🎯 **研究动机**：AIGI 检测器对未见生成器泛化差，仅靠数据规模不够，训练时生成变体覆盖有限是关键因素
- 🔬 **研究方法**：提出 PROBE：以检测器为 critic 引导生成器做流形级修改，主动生成标准采样难以覆盖的难分样本暴露失败案例并精炼检测器
- 📌 **结论**：多基准上提升对未见生成器的泛化，检测更可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting AI-generated images (AIGI) remains challenging because detectors often fail to generalize to unseen generators. Although existing methods are trained on large datasets, their performance still degrades when generation settings change, indicating that data scale alone is insufficient and that limited coverage of generative variations during training is a key factor. Studies on generative model editing show that small changes in internal representations can produce diverse and meaningful image variations, many of which are not explored under standard sampling. Leveraging this insight, we propose PROBE (Probing Robustness via Boundary Exploration), a framework that improves detector generalization by actively exploring challenging regions of the generative process. Instead of treating the generator as a fixed data source, PROBE uses the detector as a critic to steer the generator through manifold-level modifications, producing realistic samples that are difficult to classify. These samples expose failure cases that are uncommon under standard data sampling strategies and are used to refine the detector. Experimental results across multiple benchmarks indicate that PROBE enhances generalization to unseen generators, resulting in more generalizable AIGI detection performance.

</details>

### 7. RA-Det: Towards Universal Detection of AI-Generated Images via Robustness Asymmetry

📄 [arXiv](https://arxiv.org/abs/2603.01544) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64711)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`adversarial robustness`、`cross-generator detection`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Xinchang Wang、…、Hui Li

- 🎯 **研究动机**：生成图像外观线索弱化，依赖外观线索的检测器失稳，需转向行为信号
- 🔬 **研究方法**：发现鲁棒性不对称：自然图像在受控小扰动下语义表示稳定而生成图像特征漂移大，理论下界联系其与生成模型记忆化；RA-Det 据此转化为判别信号
- 📌 **结论**：14 个生成模型、10 余个强检测器对比中平均性能提升 12.92%，数据模型无关且跨未见生成器迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent image generators produce photo-realistic content that undermines the reliability of downstream recognition systems. As visual appearance cues become less pronounced, appearance-driven detectors that rely on forensic cues or high-level representations lose stability. This motivates a shift from appearance to behavior, focusing on how images respond to controlled perturbations rather than how they look. In this work, we identify a simple and universal behavioral signal. Natural images preserve stable semantic representations under small, structured perturbations, whereas generated images exhibit markedly larger feature drift. We refer to this phenomenon as \textbf{robustness asymmetry} and provide a theoretical analysis that establishes a lower bound connecting this asymmetry to memorization tendencies in generative models, explaining its prevalence across architectures. Building on this insight, we introduce Robustness Asymmetry Detection (RA-Det), a behavior-driven detection framework that converts robustness asymmetry into a reliable decision signal. Evaluated across 14 diverse generative models and against more than 10 strong detectors, RA-Det achieves superior performance, improving the average performance by 12.92\%. The method is data- and model-agnostic, requires no generator fingerprints, and transfers across unseen generators. Together, these results indicate that robustness asymmetry is a stable, general cue for synthetic-image detection and that carefully designed probing can turn this cue into a practical, universal detector.

</details>

### 8. PGC: Peak-Guided Calibration for Generalizable AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2605.21207) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60638)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`uncertainty calibration`、`cross-generator detection`、`deepfake detection`、`diffusion model`

👤 **作者**：Xiaoyu Zhou、Jianwei Fei、Peipeng Yu、Jingchang Xie、Chong Cheng、Zhihua Xia

- 🎯 **研究动机**：生成模型的判别线索愈发细微，被高保真主体内容淹没，依赖全局表示的检测器受限
- 🔬 **研究方法**：PGC 峰值聚焦机制聚合最判别性局部线索校准全局决策；并引入含 15 个商业模型样本的 CommGen15 基准
- 📌 **结论**：CommGen15 平均准确率 +12.3%，GenImage +2.1%、AIGI +3.5%、UniversalFakeDetect +1.7%，均创新纪录

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of generative AI, from GANs to modern diffusion models, has resulted in increasingly subtle discriminative clues. These fine-grained signals are often overshadowed by dominant, high-fidelity image content (e.g., the main subject), limiting the reliability of existing detectors that predominantly rely on global representations. To address this challenge, we propose the Peak-Guided Calibration (PGC) framework. PGC introduces a novel strategy that aggregates salient features via a peak-focusing mechanism. Specifically, by employing a peak-sensitive aggregation that accentuates the most discriminative local clues, PGC leverages these critical signals to calibrate the global decision. This approach recovers subtle patterns that would otherwise be submerged in the global context. Furthermore, to better simulate real-world threats, we introduce the CommGen15 dataset, a challenging benchmark comprising samples from 15 commercial models. Extensive experiments demonstrate that PGC achieves state-of-the-art performance. Specifically, it improves mean accuracy by +12.3% on our CommGen15 dataset, and sets new records on standard benchmarks, including GenImage (+2.1%), AIGI (+3.5%), and UniversalFakeDetect (+1.7%). Code is available at https://github.com/xiaoyu6868/PGC.

</details>

### 9. OmniAID: Decoupling Semantic and Artifacts for Universal AI-Generated Image Detection in the Wild

🎓 [Official](https://icml.cc/virtual/2026/poster/62808)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Yuncheng Guo、…、Weijia Li

- 🎯 **研究动机**：现有 AIGI 检测器学单一纠缠伪造表示，混淆内容相关缺陷与内容无关伪影，且受限于过时基准
- 🔬 **研究方法**：OmniAID 解耦 MoE 架构：可路由语义专家处理各内容域语义缺陷，固定通用伪影专家分离内容无关伪影，两阶段训练；并构建新数据集 Mirage
- 📌 **结论**：超现有检测器，对现代真实威胁建立 AIGI 检测新标准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A truly universal AI-Generated Image (AIGI) detector must simultaneously generalize across diverse generative models and varied semantic content. Current methods learn a single, entangled forgery representation, conflating content-dependent flaws with content-agnostic artifacts, and are further constrained by outdated benchmarks. We propose OmniAID, a novel framework centered on a decoupled Mixture-of-Experts (MoE) architecture that separates: (1) semantic flaws across distinct content domains via Routable Specialized Semantic Experts, and (2) content-agnostic universal artifacts from content-dependent flaws via a Fixed Universal Artifact Expert. A two-stage training strategy first specializes experts independently with domain-specific hard-sampling, then trains a lightweight gating network for effective input routing. By explicitly decoupling "what is generated'' (content-specific flaws) from "how it is generated'' (universal artifacts), OmniAID achieves robust generalization. We also introduce Mirage, a large-scale, contemporary dataset comprising a modern training set and a challenging test set. Extensive experiments demonstrate that OmniAID surpasses existing detectors, establishing a new standard for AIGI detection against modern, in-the-wild threats.

</details>

### 10. GenShield: Unified Detection and Artifact Correction for AI-Generated Images

📄 [arXiv](https://arxiv.org/abs/2605.16122) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65218)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`diffusion model`

👤 **作者**：Zhipei Xu、…、Jian Zhang

- 🎯 **研究动机**：AIGI 检测之后如何校正可见伪影、恢复真实外观几乎未被研究，且检测与校正相互割裂
- 🔬 **研究方法**：GenShield 自回归框架闭环联合可解释检测与可控伪影校正，用 Visual Chain-of-Thought 课程学习实现先诊后修，并构建大规模 artifact-restored 配对数据集
- 📌 **结论**：在校正基准与主流 AIGI 检测基准上均 SOTA 且泛化强，两任务互相促进

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion-based image synthesis has made AI-generated images (AIGI) increasingly photorealistic, raising urgent concerns about authenticity in applications such as misinformation detection, digital forensics, and content moderation. Despite the substantial advances in AIGI detection, how to correct detected AI-generated images with visible artifacts and restore realistic appearance remains largely underexplored. Moreover, few existing work has established the connection between AIGI detection and artifact correction. To fill this gap, we propose GenShield, a unified autoregressive framework that jointly performs explainable AIGI detection and controllable artifact correction in a closed loop from diagnosis to restoration, revealing a mutually reinforcing relationship between these two tasks. We further introduce a Visual Chain-of-Thought based curriculum learning strategy that enables self-explained, multi-step "diagnose-then-repair" correction with an explicit stopping criterion. A high-quality dataset with large-scale "artifact-restored" pairs is also constructed alongside a unified evaluation pipeline. Extensive experiments on our correction benchmark and mainstream AIGI detection benchmarks demonstrate state-of-the-art performance and strong generalization of our method.

</details>

### 11. ForensicConcept: Transferable Forensic Concepts for AIGI Detection

📄 [arXiv](https://arxiv.org/abs/2606.07034) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63871)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Menyanshu Zhou、…、Rongrong Ji

- 🎯 **研究动机**：AI 图像检测器是黑盒、不揭示决策证据，对未见生成器失效的原因难以理解
- 🔬 **研究方法**：ForensicConcept 经 Transformer 归因定位决策关键 patch、聚为紧凑概念码本并做概念对齐投影；基于 CleanDIFT 扩散特征与 CKNNA 对齐度量，把扩散衍生概念注入目标骨干
- 📌 **结论**：GenImage、GAN 系与 Chameleon 上持续超越先前方法；CKNNA 对齐可预测迁移效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated image detectors achieve high accuracy on in-distribution data but often fail on unseen generators. A key obstacle to understanding this failure is the black-box nature of current detectors: they do not reveal which evidence drives their decisions. We propose \textsc{ForensicConcept}, a framework that extracts explicit forensic concepts from detectors and enables their transfer across backbones. Our method localizes decision-critical patches via Transformer attribution, clusters them into a compact concept codebook, and uses a concept-aligned projection to produce auditable evidence readouts. Motivated by prior studies showing that DINO representations can guide diffusion generation and exhibit concept-level correspondence with diffusion features, we introduce a generation-trace reference based on CleanDIFT diffusion features and quantify backbone-trace alignment via neighborhood-structure consistency (CKNNA). We further propose concept codebook injection to transfer diffusion-derived concepts into target backbones. Experiments on GenImage, GAN-family, and Chameleon benchmarks show consistent improvements over prior methods. We also find that CKNNA alignment predicts transfer effectiveness, providing a principled explanation for why some backbones yield more transferable forensic evidence than others.

</details>

### 12. Fleet: Few Shots Lead Effective AI-generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2606.31082) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66467)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Jiaan Wang、Sirui Liu、Yu Li、Kaiyuan Yang、Juan Cao、Sheng Tang

- 🎯 **研究动机**：静态特征空间范式假设历史伪影可零样本泛化，对快速演进的生成器（SD3、Nano Banana Pro 等）灾难性失效
- 🔬 **研究方法**：Fleet 从静态泛化转向动态适应：用受限路由校正替代无约束特征更新——avoidance routing 把新 AI 样本从解耦子空间的非 AI 主导路由引开；并建含 64 模型 36 万图像、20 个闭源商业引擎的 Treasure 基准
- 📌 **结论**：静态 SOTA 在现代生成器上崩溃，Fleet 在 Doubao Seedream 4.0 上仅 10-shot 即把性能从 20.4% 恢复到 73.1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated image (AIGI) detection is undergoing a critical transition from laboratory benchmarks to open-world adversarial defense. The prevalent paradigm focuses on finding static feature spaces, assuming that some invariant artifacts learned from historical data can achieve universal zero-shot generalization. While achieving saturation on several AIGI benchmarks, this static hypothesis suffers a severe performance drop against rapidly evolving generators (e.g., SD3, Nano Banana Pro). To address these limitations, we propose that the field should expand beyond "static generalization" to a new paradigm of "dynamic adaptation". We introduce Fleet, a framework that pioneers a dynamic paradigm of continuous few-shot evolution, enabling rapid alignment with emerging generative threats. Fleet improves few-shot adaptation by replacing unconstrained feature updates with constrained routing correction, where avoidance routing redirects novel AI samples away from Non-AI-dominated routes within decoupled subspaces. To validate this, we present Treasure, a benchmark spanning 64 models and 360k images, featuring diverse architectures and 20 closed-source commercial engines. Experiments reveal that while static SOTA methods fail catastrophically on modern generators, Fleet restores performance from 20.4\% to 73.1\% with only 10-shot adaptation on "Doubao Seedream 4.0". Code and data are available at https://github.com/ICTMCG/Fleet.

</details>

### 13. FiSeR: Fine-Grained Source Representations for Cross-Domain AI Image Detection

📄 [arXiv](https://arxiv.org/abs/2606.00606) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61387)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Shan Zhang、Yongxin He、Mingming Zhang、Huiwen Tian、Lei Ma

- 🎯 **研究动机**：合成图像检测器域偏移下泛化差——UMAP 显示特征仍可分但分类头过拟合训练域伪影
- 🔬 **研究方法**：FiSeR 层级对比学习：自然与合成图像间粗粒度对比加生成器身份的合成图像间细粒度对比
- 📌 **结论**：WildFake 训练后在四个跨域基准平均 AUROC +10.22；冻结骨干加每类 10 样本 SVM 头使 AIGIBench +10.64、Chameleon +17.41

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world synthetic image detectors often generalize poorly under domain shift despite strong in-domain performance. Using unsupervised UMAP projections, we find that natural and synthetic features remain partially separable on unseen datasets, yet performance still drops, suggesting that the classification head overfits to training-domain artifacts. Therefore, the key is to learn more transferable representations so that the decision criterion is more stable and robust to domain shifts. Based on the structural fact that synthetic images are produced by diverse generators, we propose a hierarchical contrastive learning framework that improves the separability between natural and synthetic images while preserving generator identity information. It jointly optimizes (i) a coarse contrastive objective between natural and synthetic images and (ii) a fine contrastive objective among synthetic images using generator identities. Trained on WildFake, our method achieves an average AUROC gain of +10.22 on cross-domain evaluation over Chameleon, AIGIBench, Community Forensics, and GenImage under the same settings as the strong baseline DIRE. For few-shot adaptation, we freeze the backbone and fit an SVM head on 10 labeled samples per class, improving AUROC by +10.64 on AIGIBench and +17.41 on Chameleon, averaged over 12 widely used detectors. Our code is publicly available at: https://github.com/heyongxin233/FiSeR.

</details>

### 14. DNA: Uncovering Universal Latent Forgery Knowledge

📄 [arXiv](https://arxiv.org/abs/2601.22515) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63363)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`mechanistic analysis`

👤 **作者**：Jingtong Dou、…、Tat-Seng Chua

- 🎯 **研究动机**：超真实生成使表层伪影检测失效；主流方法依赖资源密集的黑盒骨干微调
- 🔬 **研究方法**：主张伪造检测能力已编码于预训练模型：分析特征解耦与注意力分布定位语义转向异常的关键中间层，用三元融合评分加曲率截断分离伪造判别单元 FDU；并构建 HIFI-Gen 高保真基准
- 📌 **结论**：仅靠这些锚点即获优越检测性能（含少样本），跨架构与未见生成器鲁棒——唤醒潜藏神经元比大规模微调更有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As generative AI achieves hyper-realism, superficial artifact detection has become obsolete. While prevailing methods rely on resource-intensive fine-tuning of black-box backbones, we propose that forgery detection capability is already encoded within pre-trained models rather than requiring end-to-end retraining. To elicit this intrinsic capability, we propose the discriminative neural anchors (DNA) framework, which employs a coarse-to-fine excavation mechanism. First, by analyzing feature decoupling and attention distribution shifts, we pinpoint critical intermediate layers where the focus of the model logically transitions from global semantics to local anomalies. Subsequently, we introduce a triadic fusion scoring metric paired with a curvature-truncation strategy to strip away semantic redundancy, precisely isolating the forgery-discriminative units (FDUs) inherently imprinted with sensitivity to forgery traces. Moreover, we introduce HIFI-Gen, a high-fidelity synthetic benchmark built upon the very latest models, to address the lag in existing datasets. Experiments demonstrate that by solely relying on these anchors, DNA achieves superior detection performance even under few-shot conditions. Furthermore, it exhibits remarkable robustness across diverse architectures and against unseen generative models, validating that waking up latent neurons is more effective than extensive fine-tuning.

</details>

### 15. Dissect and Prune: Enhancing Robustness in AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2606.10309) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64805)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`adversarial robustness`、`cross-generator detection`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Dahye Kim、…、Jang-Ho Choi

- 🎯 **研究动机**：AI 图像检测器的高性能主要来自偏向真实类的预测不对称，对生成内容敏感度低、后处理下尤甚——源于依赖虚假特征
- 🔬 **研究方法**：DEAR 用 inpaint 图像识别并剪除干扰特征：与 inpaint mask 对齐过强的通道特征对后处理更脆弱，剪除两端只保留真正捕捉生成伪影的特征
- 📌 **结论**：显著增强对未见生成器与后处理的鲁棒性，有效缓解预测不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While existing AI-generated image detectors report high performance, we identify that this is largely driven by a critical prediction asymmetry: a bias toward the real class that severely limits sensitivity to generated content, especially under standard post-processing operations such as compression and resizing. We hypothesize that this stems from the model's reliance on spurious features, distracting signals that obscure true generative artifacts. To address this, we propose DEAR (Dissect and Prune), which leverages inpainted images to identify and prune these interfering components. Specifically, we find that features strongly aligned to either inpainted or non-inpainted regions are less robust to post-processing. By measuring the alignment between channel activations and inpaint masks, DEAR removes features at both extremes, retaining only those that capture genuine generative artifacts. Experimental results demonstrate that our approach significantly enhances robustness against unseen generators and post-processing, effectively mitigating the prediction asymmetry. Our code is available at https://github.com/dahyedahye/dear.

</details>

### 16. DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2511.13108) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65175)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`diffusion model`

👤 **作者**：Jiazhen Yan、Ziqiang Li、Fan Wang、Boyu Wang、Ziwen He、Zhangjie Fu

- 🎯 **研究动机**：微调 CLIP 做 AI 生成图像检测常引发灾难遗忘，损害预训练先验并限制跨域泛化
- 🔬 **研究方法**：DGS-Net 梯度空间分解分离有害与有益下降方向：把任务梯度投影到有害方向正交补并与冻结 CLIP 蒸馏的有益方向对齐
- 📌 **结论**：50 个生成模型上平均超 SOTA 6.6%，跨多样生成技术检测与泛化优越

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of generative models such as GANs and diffusion models has led to the widespread proliferation of AI-generated images, raising concerns about misinformation, privacy violations, and trust erosion in digital media. Although large-scale multimodal models like CLIP offer strong transferable representations for detecting synthetic content, fine-tuning them often induces catastrophic forgetting, which degrades pre-trained priors and limits cross-domain generalization. To address this issue, we propose the Distillation-guided Gradient Surgery Network (DGS-Net), a novel framework that preserves transferable pre-trained priors while suppressing task-irrelevant components. Specifically, we introduce a gradient-space decomposition that separates harmful and beneficial descent directions during optimization. By projecting task gradients onto the orthogonal complement of harmful directions and aligning with beneficial ones distilled from a frozen CLIP encoder, DGS-Net achieves unified optimization of prior preservation and irrelevant suppression. Extensive experiments on 50 generative models demonstrate that our method outperforms state-of-the-art approaches by an average margin of 6.6%, achieving superior detection performance and generalization across diverse generation techniques.

</details>

### 17. CORE: Conflict-Oriented Reasoning for General Multimodal Manipulation Detection

📄 [arXiv](https://arxiv.org/abs/2606.03066) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66290)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`VLM safety`、`AI-generated content`、`cross-generator detection`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Jinjie Shen、…、Zhun Zhong

- 🎯 **研究动机**：多模态伪造检测依赖操纵特定模型与大量标注，对新兴操纵类型泛化差
- 🔬 **研究方法**：CORE 立足于被操纵误信息的内在冲突（跨模态或与世界常识的不一致）：构建细粒度标注冲突因素与来源的 Conflict Attribution Corpus，做面向冲突的表征增强与推理
- 📌 **结论**：少样本甚至零样本适应未见操纵类型；DGM4、MMFakeBench、MDSM 准确率分别超 SOTA 9.7%、14.1%、11.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid rise of generative AI has made multimodal fake news increasingly realistic and pervasive, posing severe threats to public trust and social stability. Existing detection methods rely heavily on manipulation-specific models and large-scale labeled data, resulting in poor generalization to emerging manipulation types. We observed that the essence of manipulated misinformation lies in its intrinsic conflicts, i.e., semantic or physical inconsistencies either across modalities or with common world knowledge. Inspired by this observation, we propose Conflict-{Oriented REasoning (CORE) framework, an effective paradigm that learns to endows multimodal large language models (MLLMs) with explicit conflict-capturing capability. To this end, CORE first constructs the Conflict Attribution Corpus (CAC) with fine-grained annotations of conflict factors and sources, providing essential data support for subsequent conflict perception training. By performing conflict-oriented representation enhancement and reasoning based on CAC, CORE achieves robust and generalizable conflict detection, effectively and rapidly adapting to unseen manipulation types with a few samples or in even zero-shot settings. Extensive experiments demonstrate that CORE surpasses state-of-the-art models by 9.7\%, 14.1\%, and 11.8\% in accuracy on the DGM$^4$, MMFakeBench, and MDSM benchmarks, respectively.

</details>

### 18. Can We Build a Monolithic Model for Fake Image Detection? SICA: Semantic-Induced Constrained Adaptation for Unified-Yet-Discriminative Artifact Feature Space Reconstruction

📄 [arXiv](https://arxiv.org/abs/2602.06676) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66804)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`analysis`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`

👤 **作者**：Bo Du、…、Ji-Zhe Zhou

- 🎯 **研究动机**：统一检测四个图像取证子域的单一模型在实践中持续劣于集成，根因是各子域伪影内在异质（Ji-Zhe 现象）导致伪影特征空间坍塌
- 🔬 **研究方法**：SICA 以高层语义作为伪影特征空间重建的结构先验，实现统一而可判别的单一 FID 范式，在 OpenMMSec 数据集上评测
- 📌 **结论**：超越 15 个 SOTA 方法，以近正交方式重建统一可判别的伪影特征空间

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fake Image Detection (FID), aiming at unified detection across four image forensic subdomains, is critical in real-world forensic scenarios. Compared with ensemble approaches, monolithic FID models are theoretically more promising, but to date, consistently yield inferior performance in practice. In this work, we identify the intrinsic distinctness of artifacts across subdomains—a critical barrier we term the "Ji-Zhe phenomenon". Driven by this phenomenon, we diagnose the cause of this underperformance for the first time: the collapse of the artifact feature space. The core challenge for developing a practical monolithic FID model thus boils down to the "unified-yet-discriminative" reconstruction of the artifact feature space. To address this paradoxical challenge, we hypothesize that high-level semantics can serve as a structural prior for the reconstruction, and further propose Semantic-Induced Constrained Adaptation (SICA), the first monolithic FID paradigm. Extensive experiments on our $ \textit{OpenMMSec} $ dataset demonstrate that SICA outperforms 15 state-of-the-art methods and reconstructs the target unified-yet-discriminative artifact feature space in a near-orthogonal manner, thus firmly validating our hypothesis. The code and dataset will be made publicly available.

</details>

### 19. AI use in American newspapers is widespread, uneven, and rarely disclosed

🎓 [Official](https://aclanthology.org/2026.acl-long.663/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Jenna Russell、…、Mohit Iyyer

- 🎯 **研究动机**：AI 在已发表新闻报道中的使用程度不明，缺乏大规模审计
- 🔬 **研究方法**：用 SOTA 检测器 Pangram 审计 2025 年夏 1.5K 家美国报纸的 186K 篇文章，并分析三大报 45K 篇评论文章
- 📌 **结论**：约 9% 新发文章含 AI 生成内容，小报及天气、科技主题更多；评论文章含 AI 内容概率是新闻的 6.4 倍；100 篇 AI 标记文章仅 5 篇披露，AI 文章出现幻觉断言的概率高 8.2 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI is rapidly transforming journalism, but the extent of its use in published newspaper articles remains unclear. We address this gap by auditing a large-scale dataset of 186K articles from online editions of 1.5K American newspapers published in the summer of 2025. Using Pangram, a state-of-the-art AI detector, we discover that approximately 9% of newly-published articles are either partially or fully AI-generated. This AI use is unevenly distributed, appearing more frequently in smaller, local outlets, in specific topics such as weather and technology, and within certain ownership groups. We also analyze 45K opinion pieces from Washington Post, New York Times, and Wall Street Journal, finding that they are 6.4 times more likely to contain AI-generated content than news articles from the same publications, with many AI-flagged op-eds authored by prominent public figures. Despite this prevalence, we find that AI use is rarely disclosed: a manual audit of 100 AI-flagged articles found only five disclosures of AI use. A factuality analysis shows AI-generated articles are 8.2 times more likely to contain hallucinated claims than human-written news. Overall, our audit highlights the immediate need for greater transparency and updated editorial standards regarding the use of AI in journalism to maintain public trust.

</details>

### 20. A Debiased Reconstruction-based Framework for Training-Free Detection of AI-Generated Images

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_A_Debiased_Reconstruction-based_Framework_for_Training-Free_Detection_of_AI-Generated_Images_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated image`、`reconstruction bias`、`training-free method`

👤 **作者**：Sungik Choi、Hankook Lee、Jaehoon Lee、Robin Kim、Stanley Jungkyu Choi、Moontae Lee

- 🎯 **研究动机**：基于 LDM 重建误差的 training-free 检测分数存在实例特异性偏差（尤其简单背景图像），且训练数据常不可得
- 🔬 **研究方法**：提出图像级去偏分数：用旋转与低通滤波增强产生相似背景图像并归一化重建误差以抵消背景贡献；另引入潜在级重建误差并做旋转归一化去偏，统一为单一分数 RDD
- 📌 **结论**：跨多样生成模型取得 SOTA 级 training-free 检测性能，并对被检图像的损坏保持鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As recent AI models have successfully generated high-resolution photorealistic images, it has also been socially important to detect whether an image is generated by AI. Since training data for the detection task is often not available due to the diversity of generative models, training-free detection approaches have been practically considered. A common approach is to utilize the image-level reconstruction error from the latent diffusion model (LDM). However, we find this score suffers from instance-specific biases, particularly in images with simple backgrounds. To this end, we propose a novel image-level debiasing score function that cancels out background contribution by normalizing the reconstruction error on the augmented images with similar background information. To be specific, we show that rotation and low-pass filtering are effective augmentation strategies. To promote generalization to broader generative models, we newly explore latent-level reconstruction error as an additional training-free signal. However, we observe that the latent-level score also suffers to latent-specific bias. To mitigate this, we introduce a rotation-based latent-level debiasing score based on the normalization of the rotated latent. We unify the aforementioned scores into a single unified debiasing score, RDD, which achieves state-of-the-art training-free detection performance across diverse generative models. Furthermore, our framework can be robust to corruption of the examined images.

</details>

### 21. Zero-shot Detection of AI-Generated Image via RAW-RGB Alignment

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_Zero-shot_Detection_of_AI-Generated_Image_via_RAW-RGB_Alignment_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated image`、`RAW-RGB alignment`、`zero-shot forensics`

👤 **作者**：Haiwei Wu、Fengpeng Li、Zhilin Tu、Yuanman Li、Xiong Li、Jiantao Zhou

- 🎯 **研究动机**：经打印扫描等物理变换的合成图像常被误判为真，真与合成的定义待澄清
- 🔬 **研究方法**：建模物理到数字的RAW-RGB映射，以alignment trace刻画真实图像固有参数关联，仅用真实样本训练
- 📌 **结论**：零样本检测达SOTA，微调后跨域更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in generative AI (GenAI) have increasingly complicated the identification of synthetic images, prompting the proposal of numerous zero-/few-shot detection methods to counter unknown GenAI better. However, we observe that existing detectors often misclassify synthetic images with physical transformations (e.g., print+scan) as real. The essence of this observation lies in: should images remapped from the physical world to digital space still be categorized as "Synthetic"? Furthermore, the definition of what constitutes real and synthetic images urgently needs to be clarified. We first boldly propose that the authenticity of an image depends on whether it originates from the physical world, i.e., it is necessary to verify the original correlation between the digital image and the physical world. To this end, we first analyze the physical-to-digital mapping process: illumination signals are captured by camera sensors as RAW data, which is then converted into RGB data via camera internal parameters. This process embodies unique physical cues inherent to real scenes. Based on this, we propose a novel forensic feature termed alignment trace, which is constructed by modeling a shared RAW-RGB feature space. This trace captures the inherent parameter correlations of real images in the physical-to-digital conversion process, thereby indirectly verifying the physical origin of the image. Experiments demonstrate that our method achieves state-of-the-art zero-shot detection using only real RAW-RGB data pairs. When additional prior knowledge is provided, the method can be easily fine-tuned to achieve better cross-domain detection performance. We hope this work provides a new baseline for zero-shot synthetic detection and, more significantly, inspires the forensics community to explore the essential distinctions between real and synthetic images.

</details>

### 22. PURE: Purging Unrelated Representations for Content-Agnostic Forgery Detection

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2613.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`AI-generated image`、`content shortcut`、`cross-domain forensics`

- 🎯 **研究动机**：AIGI 检测器把伪造伪影与语义内容虚假耦合（内容捷径），分布偏移下严重退化
- 🔬 **研究方法**：PURE 用 Causal Semantic Generative 机制把语义表示与伪造无关干扰解耦，GMM 原型对齐抑制类别特定内容偏差
- 📌 **结论**：CIFAKE、GenImage 与 AlFace 上伪相关反转设定下泛化优越

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing AI-generated image (AIGI) detectors perform well in-domain but degrade severely under distribution shift. We observe that this failure is mainly caused by content shortcuts, where detectors spuriously couple forgery artifacts with semantic content, such as object categories or demographic attributes, learning content–label correlations instead of generalizable forgery patterns. To address this issue, we propose PURE (Purging Unrelated Representations for ContentAgnostic Forgery Detection), which achieves content-agnostic detection through two complementary components: a Causal Semantic Generative (CSG) mechanism that disentangles semantic representations from forgery-irrelevant nuisance factors, and a Gaussian Mixture Model (GMM)- based prototype alignment module that suppresses category-specific content bias. Extensive experiments on CIFAKE, GenImage, and AlFace show that PURE achieves superior generalization under spurious correlation reversal. The code is available at https://github.com/wuxinyu519/PURE.

</details>

### 23. Beyond Artifacts: Real-Centric Envelope Modeling for Reliable AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2512.20937) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3942)　📅 2025-12　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated image detection`、`AI-generated content`、`cross-generator detection`、`real-data distribution`、`cross-domain generalization`

👤 **作者**：Ruiqi Liu、…、Shu Wu

- 🎯 **研究动机**：检测器过拟合生成器特定伪影，对跨平台多轮分享与后处理造成的链式退化敏感，伪影线索随生成架构演化失效
- 🔬 **研究方法**：REM 把检测从学伪影转向建模真实图像的鲁棒分布：自重构中引入特征级扰动生成近真样本，用跨域一致的包络估计器学习包围真实流形的边界，并构建含链式退化的 RealChain 基准
- 📌 **结论**：八个基准平均超 SOTA 7.5%，在严重退化的 RealChain 上保持出色泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of generative models has intensified the need for reliable and robust detection under real-world conditions. However, existing detectors often overfit to generator-specific artifacts and remain highly sensitive to real-world degradations. As generative architectures evolve and images undergo multi-round cross-platform sharing and post-processing (chain degradations), these artifact cues become obsolete and harder to detect. To address this, we propose Real-centric Envelope Modeling (REM), a new paradigm that shifts detection from learning generator artifacts to modeling the robust distribution of real images. REM introduces feature-level perturbations in self-reconstruction to generate near-real samples, and employs an envelope estimator with cross-domain consistency to learn a boundary enclosing the real image manifold. We further build RealChain, a comprehensive benchmark covering both open-source and commercial generators with simulated real-world degradation. Across eight benchmark evaluations, REM achieves an average improvement of 7.5% over state-of-the-art methods, and notably maintains exceptional generalization on the severely degraded RealChain benchmark, establishing a solid foundation for synthetic image detection under real-world conditions. The code and the RealChain benchmark will be made publicly available upon acceptance of the paper.

</details>

### 24. REVEAL: Reasoning-Enhanced Forensic Evidence Analysis for Explainable AI-Generated Image Detection

📄 [arXiv](https://arxiv.org/abs/2511.23158) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5044)　📅 2025-11　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated image detection`、`AI-generated content`、`cross-generator detection`、`evidence chain`、`reinforcement learning`

👤 **作者**：Huangsen Cao、…、Fei Wu

- 🎯 **研究动机**：多模态 AI 图像检测的解释多为事后合理化或粗糙视觉线索，缺可验证证据链且泛化差
- 🔬 **研究方法**：构建以轻量专家模型导出的链式取证证据为核心的 REVEAL-Bench，并用专家接地的强化学习训练 REVEAL，奖励联合优化检测精度、证据推理稳定性与解释忠实度
- 📌 **结论**：跨域泛化与解释忠实度显著优于基线检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of visual generative models has made AI-generated images increasingly difficult to distinguish from authentic ones, posing growing risks to social trust and information integrity. This motivates detectors that are not only accurate but also forensically explainable. While recent multimodal approaches improve interpretability, many rely on post-hoc rationalizations or coarse visual cues, without constructing verifiable chains of evidence, thus often leading to poor generalization. We introduce REVEAL-Bench, a reasoning-enhanced multimodal benchmark for AI-generated image forensics, structured around explicit chains of forensic evidence derived from lightweight expert models and consolidated into step-by-step chain-of-evidence traces. Based on this benchmark, we propose REVEAL (\underline{R}easoning-\underline{e}nhanced Forensic E\underline{v}id\underline{e}nce \underline{A}na\underline{l}ysis), an explainable forensic framework trained with expert-grounded reinforcement learning. Our reward design jointly promotes detection accuracy, evidence-grounded reasoning stability, and explanation faithfulness. Extensive experiments demonstrate significantly improved cross-domain generalization and more faithful explanations to baseline detectors. All data and codes will be released.

</details>

### 25. Explainable AI-Generated Image Detection RewardBench

📄 [arXiv](https://arxiv.org/abs/2511.12363) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-11

**关键词**：`detection`、`benchmark`、`AI-image detection`、`reward model`、`AI-generated content`、`explanation judging`

👤 **作者**：Michael Yang、…、Yapeng Tian

- 🎯 **研究动机**：MLLM 作为裁判评判“图像是否 AI 生成”解释质量的能力尚未被研究
- 🔬 **研究方法**：构建约 3000 个标注三元组的 XAIGID-RewardBench，涵盖多种图像生成模型与作为检测器的 MLLM，评估当前 MLLM 充当裁判的能力
- 📌 **结论**：最佳奖励模型仅得 88.76%（人类标注一致性 98.30%），MLLM 与人类推理水平仍有明显差距

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conventional, classification-based AI-generated image detection methods cannot explain why an image is considered real or AI-generated in a way a human expert would, which reduces the trustworthiness and persuasiveness of these detection tools for real-world applications. Leveraging Multimodal Large Language Models (MLLMs) has recently become a trending solution to this issue. Further, to evaluate the quality of generated explanations, a common approach is to adopt an "MLLM as a judge" methodology to evaluate explanations generated by other MLLMs. However, how well those MLLMs perform when judging explanations for AI-generated image detection generated by themselves or other MLLMs has not been well studied. We therefore propose \textbf{XAIGID-RewardBench}, the first benchmark designed to evaluate the ability of current MLLMs to judge the quality of explanations about whether an image is real or AI-generated. The benchmark consists of approximately 3,000 annotated triplets sourced from various image generation models and MLLMs as policy models (detectors) to assess the capabilities of current MLLMs as reward models (judges). Our results show that the current best reward model scored 88.76\% on this benchmark (while human inter-annotator agreement reaches 98.30\%), demonstrating that a visible gap remains between the reasoning abilities of today's MLLMs and human-level performance. In addition, we provide an analysis of common pitfalls that these models frequently encounter. Code and benchmark are available at https://github.com/RewardBench/XAIGID-RewardBench.

</details>

### 26. Locate-Then-Examine: Grounded Region Reasoning Improves Detection of AI-Generated Images

📄 [arXiv](https://arxiv.org/abs/2510.04225) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Ji_Locate-Then-Examine_Grounded_Region_Reasoning_Improves_Detection_of_AI-Generated_Images_CVPR_2026_paper.html)　📅 2025-10　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated image`、`region grounding`、`forensic reasoning`

👤 **作者**：Yikun Ji、…、Jianfu Zhang

- 🎯 **研究动机**：一次式 VLM 分类器漏掉高质量合成图的细微伪影且缺乏像素级定位依据
- 🔬 **研究方法**：提出 Locate-Then-Examine 两阶段取证：先定位可疑区域，再连同全图细查以细化判定与解释，并构建 2 万张带区域级标注与取证解释的 TRACE 数据集
- 📌 **结论**：在 TRACE 与多个外部基准上准确率有竞争力、鲁棒性更佳，输出可理解且区域有据的解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of AI-generated imagery has blurred the boundary between real and synthetic content, raising practical concerns for digital integrity. Vision-language models (VLMs) can provide natural language explanations, but standard one-pass classifiers often miss subtle artifacts in high-quality synthetic images and offer limited grounding in the pixels. We propose Locate-Then-Examine (LTE), a two-stage VLM-based forensic framework that first localizes suspicious regions and then re-examines these crops together with the full image to refine the real vs. AI-generated verdict and its explanation. LTE explicitly links each decision to localized visual evidence through region proposals and region-aware reasoning. To support training and evaluation, we introduce TRACE, a dataset of 20,000 real and high-quality synthetic images with region-level annotations and automatically generated forensic explanations, constructed by a VLM-based pipeline with additional consistency checks and quality control. Across TRACE and multiple external benchmarks, LTE achieves competitive accuracy and improved robustness while providing human-understandable, region-grounded explanations suitable for forensic deployment.

</details>

### 27. UC-VLM: Consistency-Driven Learning for AI-Generated Image Detection with Vision-Language Large Models

📄 [arXiv](https://arxiv.org/abs/2608.15238) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5204)　📅 2026-08

**关键词**：`detection`、`AI-generated image detection`、`vision-language model`、`weak supervision`、`AI-generated content`

👤 **作者**：Lei Tan、Shuwei Li、Mohan Kankanhalli、Robby T. Tan

- 🎯 **研究动机**：VLLM 检测器偏重语言侧微调、忽视低层视觉取证线索，且依赖人工 prompt 或人工标注 rationale
- 🔬 **研究方法**：UC-VLM 仅靠二值标签：自动筛选有效指令变体，视觉判别目标强化非语义取证敏感度，标签条件生成目标监督文本输出，同一真实性标签复用于两条通路
- 📌 **结论**：GenImage 平均准确率 96.1%（超最强先前 4.6 个百分点），Chameleon 上 ProGAN/SDV1.4 训练 69.6%/77.9%（超最佳基线 11.2%/15.3 个百分点）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Large Models (VLLMs) are promising for AI-generated image (AIGI) detection because they can produce both a prediction and a natural-language output. However, most existing VLLM-based detectors primarily fine-tune the language side while giving limited attention to low-level visual forensic cues. They also often depend on manually crafted prompts or human-annotated rationales, which limits scalability.We present UC-VLM, a unified multi-stage framework for AIGI detection that relies solely on binary supervision. UC-VLM first identifies effective instruction variants automatically. It then reuses the same binary label within a multi-stage training framework: (i) a visual discrimination objective that strengthens sensitivity to non-semantic forensic cues, and (ii) a label-conditioned generation objective that uses the binary label to supervise textual outputs. This design turns weak binary supervision into a shared supervision signal for both the visual pathway and the language output. Our key novelty is a unified multi-stage binary-supervised framework that consistently reuses the same authenticity labels for visual adaptation and label-conditioned text generation, while leveraging automatically optimized instructions to reduce prompt sensitivity without requiring human-written rationales or hand-crafted prompts.Experiments show that UC-VLM achieves 96.1% average accuracy on GenImage, exceeding the strongest prior result by 4.6%, and obtains 69.6% / 77.9% accuracy on Chameleon under ProGAN / SDV1.4 training, surpassing the best baseline by 11.2% / 15.3%, respectively.

</details>

### 28. AICD Bench: A Challenging Benchmark for AI-Generated Code Detection

🤗 [Model](https://huggingface.co/AICD-bench) · 🎓 [Official](https://aclanthology.org/2026.eacl-long.325/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`AI-generated code`、`family attribution`、`distribution shift`、`model attribution`

👤 **作者**：Daniil Orel、Dilshod Azizov、Indraneil Paul、Yuxia Wang、Iryna Gurevych、Preslav Nakov

- 🎯 **研究动机**：AI 生成代码检测基准局限于分布内人机二分类，无法覆盖现实场景
- 🔬 **研究方法**：AICD Bench 覆盖 2M 样本、11 个家族 77 个模型、9 种语言，定义分布偏移下鲁棒二分类、模型家族归因与含混合及对抗代码的细粒度人机分类三项任务
- 📌 **结论**：神经与经典检测器性能远低于实用水平，分布偏移与混合、对抗代码场景下尤其糟糕

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly capable of generating functional source code, raising concerns about authorship, accountability, and security. While detecting AI-generated code is critical, existing datasets and benchmarks are narrow, typically limited to binary human–machine classification under in-distribution settings. To bridge this gap, we introduce AICD Bench, the most comprehensive benchmark for AI-generated code detection. It spans 2M examples, 77 models across 11 families, and 9 programming languages, including recent reasoning models. Beyond scale, AICD Bench introduces three realistic detection tasks: (i) Robust Binary Classification under distribution shifts in language and domain, (ii) Model Family Attribution, grouping generators by architectural lineage, and (iii) Fine-Grained Human–Machine Classification across human, machine, hybrid, and adversarial code. Extensive evaluation on neural and classical detectors shows that performance remains far below practical usability, particularly under distribution shift and for hybrid or adversarial code. We release AICD Bench as a unified, challenging evaluation suite to drive the next generation of robust approaches for AI-generated code detection. The data and the code are available at https://huggingface.co/AICD-bench.

</details>

### 29. Explaining Generalization of AI-Generated Text Detectors Through Linguistic Analysis

🎓 [Official](https://aclanthology.org/2026.eacl-long.307/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`AI-text detector`、`linguistic shift`、`cross-generator generalization`、`AI-text detection`

👤 **作者**：Yuxi Xia、Kinga Stańczak、Benjamin Roth

- 🎯 **研究动机**：AI 文本检测器在未见提示、模型家族与域上泛化差，成因缺乏系统洞察
- 🔬 **研究方法**：构建 6 种提示策略、7 个 LLM、4 个域数据集的基准，计算泛化准确率与 80 个语言学特征偏移的相关性
- 📌 **结论**：泛化性能与时态使用、代词频率等语言学特征显著相关，为泛化差距提供语言学解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-text detectors achieve high accuracy on in-domain benchmarks, but often struggle to generalize across different generation conditions such as unseen prompts, model families, or domains. While prior work has reported these generalization gaps, there are limited insights about the underlying causes. In this work, we present a systematic study aimed at explaining generalization behavior through linguistic analysis. We construct a comprehensive benchmark that spans 6 prompting strategies, 7 large language models (LLMs), and 4 domain datasets, resulting in a diverse set of human- and AI-generated texts. Using this dataset, we fine-tune classification-based detectors on various generation settings and evaluate their cross-prompt, cross-model, and cross-dataset generalization. To explain the performance variance, we compute correlations between generalization accuracies and feature shifts of 80 linguistic features between training and test conditions. Our analysis reveals that generalization performance for specific detectors and evaluation conditions is significantly associated with linguistic features such as tense usage and pronoun frequency.

</details>

### 30. FAID: Fine-grained AI-generated Text Detection using Multi-task Auxiliary and Multi-level Contrastive Learning

🎓 [Official](https://aclanthology.org/2026.eacl-long.151/)　📅 2026-03　🏷 ACL 2026

**关键词**：`detection`、`AI-generated text`、`human-AI coauthoring`、`generator attribution`

👤 **作者**：Minh Ngoc Ta、…、Dinh Viet Sang

- 🎯 **研究动机**：人机协作写作使区分人写、LLM 生成与协作文本成为新挑战，二分类器不足
- 🔬 **研究方法**：构建多语言多域多生成器 FAIDSet 与细粒度框架 FAID：多级对比学习加多任务辅助分类捕捉作者与模型特征，把 LLM 家族建模为风格实体并以适应机制处理分布偏移
- 📌 **结论**：超越基线，尤其提升对未见域与新 LLM 的泛化准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing collaboration between humans and AI models in generative tasks has introduced new challenges in distinguishing between human-written, LLM-generated, and human-LLM collaborative texts. In this work, we collect a multilingual, multi-domain, multi-generator dataset FAIDSet. We further introduce a fine-grained detection framework FAID to classify text into these three categories, and also to identify the underlying LLM family of the generator. Unlike existing binary classifiers, FAID is built to capture both authorship and model-specific characteristics. Our method combines multi-level contrastive learning with multi-task auxiliary classification to learn subtle stylistic cues. By modeling LLM families as distinct stylistic entities, we incorporate an adaptation to address distributional shifts without retraining for unseen data. Our experimental results demonstrate that FAID outperforms several baselines, particularly enhancing the generalization accuracy on unseen domains and new LLMs, thus offering a potential solution for improving transparency and accountability in AI-assisted writing. Our data and code are available at https://github.com/mbzuai-nlp/FAID.

</details>

### 31. When Personalization Tricks Detectors: The Feature-Inversion Trap in Machine-Generated Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1998/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Lang Gao、…、Xiuying Chen

- 🎯 **研究动机**：LLM 模仿个人写作风格使 MGT 检测面临个性化挑战，该场景基本未被探索
- 🔬 **研究方法**：提出 StyloBench（文学与博客文本及 LLM 模仿配对）；发现特征反转陷阱——通用域有效特征在个性化场景翻转效应误导检测器；提出 StyloCheck 用特征凸显的扰动文本预测检测器鲁棒性
- 📌 **结论**：检测器个性化下性能剧烈不稳定；StyloCheck 预测跨域性能偏移方向与幅度的相关性达 85%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) increasingly imitate personal writing styles, personalization has become a key challenge for machine-generated text (MGT) detection. Yet personalized MGT detection remains largely underexplored. In this work, we introduce StyloBench, the first benchmark for evaluating detector robustness under personalization, built from literary and blog texts paired with their LLM-generated imitations. Experiments across diverse detectors show pronounced performance instability under personalization, with frequent inversions relative to general-domain behavior. To better understand this limitation, we conduct an in-depth analysis and attribute it to a feature-inversion trap, i.e., features that are effective for separating human-written text (HWT) from MGT in general flip their effect in personalized contexts, ultimately misleading detectors. Motivated by this, we propose StyloCheck, a diagnostic framework for predicting detector robustness under personalization. StyloCheck identifies the inverted features and quantifies detector dependence using perturbed texts pronounced in the features. In our experiments, StyloCheck predicts both the direction and magnitude of cross-domain performance shifts with an 85% correlation to actual outcomes. We hope this work will raise awareness of the structural risks introduced by personalization and motivate more robust approaches to personalized MGT detection. The code is available at: https://github.com/mbzuai-nlp/Personalized_MGT_Detect

</details>

### 32. Verifiable LLM-Generated Text Detection via Projected Semantic-Structural Distributions

🎓 [Official](https://aclanthology.org/2026.acl-long.638/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Ruochong Xiong、…、Junfei Liu

- 🎯 **研究动机**：现有 LLM 文本检测依赖 proxy 模型输出概率或单一语义特征，存在分布失配与可解释性不足
- 🔬 **研究方法**：发现机器生成文本在语义-结构联合空间呈方向一致的系统性平移；提出 ProSSD，以监督子空间学习提取紧凑特征，构建条件语义分布并用 Wasserstein 加权 Mahalanobis 距离做似然比检验
- 📌 **结论**：跨域、跨模型与对抗场景下鲁棒性与计算效率更优，并揭示语义平移与语义坍缩现象

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread deployment of large language models (LLMs) makes detecting LLM-Generated text a critical security task. Existing methods, primarily relying on output probabilities from proxy models or single semantic features, suffer from distribution misalignment and limited interpretability. We observe that machine-generated text exhibits a directionally consistent systematic translation relative to human-written text within the joint semantic-structural space. Accordingly, we propose ProSSD, a statistical framework utilizing supervised subspace learning to extract compact features and construct conditional semantic distributions based on syntactic structures. By employing a likelihood ratio test, we derive a modified Mahalanobis distance, weighted by the Wasserstein distance, as the discriminative metric. Experiments demonstrate ProSSD’s superior robustness and computational efficiency across cross-domain, cross-model, and adversarial scenarios. Furthermore, we reveal the phenomena of systematic semantic translation and semantic collapse in machine-generated text, offering interpretable statistical insights into LLM generation behaviors.

</details>

### 33. RealAIGC: Towards More Realistic Evaluation of AI-Generated Code Detection in Real-World Code Repository

🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-research-track/81/RealAIGC-Towards-More-Realistic-Evaluation-of-AI-Generated-Code-Detection-in-Real-Wo)　📅 2026　🏷 ASE 2026

**关键词**：`benchmark`、`AI-generated code detection`、`repository provenance`、`cross-language evaluation`

- 🎯 **研究动机**：AIGC代码检测评测脱离真实代码仓库场景
- 🔬 **研究方法**：RealAIGC基于真实仓库构建跨语言的AIGC检测评测
- 📌 **结论**：真实场景下现有检测器性能显著下滑

### 34. On the Salience of Low-Probability Tokens for AI-Generated Text Detection: A Multiscale Uncertainty Perspective

📄 [arXiv](https://arxiv.org/abs/2606.02158) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65435)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`uncertainty calibration`、`cross-generator detection`、`deepfake detection`、`cross-generator generalization`

👤 **作者**：Yikai Guo、Bin Wang、Xilai Fan、Wenjun Ke、Haoran Luo

- 🎯 **研究动机**：统计检测器受样板 token 主导与单点估计脆弱两个关键限制
- 🔬 **研究方法**：聚焦信息量大的低概率 token：局部平均其对数概率缓解样板主导，全局用 Rényi 熵捕低概率区分布形状；Uncertainty++ 用条件独立采样更稳
- 📌 **结论**：七个数据集、十六个 LLM 上检测高效、泛化且鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated text increasingly blends with human writing, raising practical risks such as misinformation, academic misuse, and corpora contamination. While statistical detectors are appealing for efficiency and generalization, they suffer from two key limitations. (i) Boilerplate dominance, boilerplate tokens shared across human and LLM writing can overwhelm discriminative signals. (ii) Brittle point estimates, relying on a single probability score yields unstable decisions under adversarial manipulations. To address these issues, we propose $\textbf{Uncertainty}$, a multiscale uncertainty estimator that focuses on informative low-probability tokens, which more clearly expose distributional discrepancies. Locally, it alleviates boilerplate dominance by averaging the log-probabilities of low-probability tokens; globally, it reduces brittleness by capturing the distributional shape of this low-probability region via Rényi entropy. We further extend the detector to $\textbf{Uncertainty++}$ via conditional independent sampling, yielding a more stable uncertainty estimation. Experiments across seven datasets and sixteen LLMs demonstrate high effectiveness, generalization, and robustness. Our code is available at github.com/guoyikai2000/Uncertainty-AIGT.

</details>

### 35. Minimizing Mismatch Risk: A Prototype-Based Routing Framework for Zero-shot LLM-generated Text Detection

📄 [arXiv](https://arxiv.org/abs/2602.01240) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65020)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Ke Sun、Guangsheng Bao、Han Cui、Yue Zhang

- 🎯 **研究动机**：零样本检测对所有输入用固定代理模型，性能随代理-来源匹配度大幅波动
- 🔬 **研究方法**：DetectRouter 把鲁棒检测转为路由问题：先从白盒模型构建判别原型，再对齐几何距离与检测分数泛化到黑盒来源
- 📌 **结论**：EvoBench 与 MAGE 基准上多检测标准与模型家族一致提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Zero-shot methods detect LLM-generated text by computing statistical signatures using a surrogate model. Existing approaches typically employ a fixed surrogate for all inputs regardless of the unknown source. We systematically examine this design and find that detection performance varies substantially depending on surrogate-source alignment. We observe that while no single surrogate achieves optimal performance universally, a well-matched surrogate typically exists within a diverse pool for any given input. This finding transforms robust detection into a routing problem: selecting the most appropriate surrogate for each input. We propose DetectRouter, a prototype-based framework that learns text-detector affinity through two-stage training. The first stage constructs discriminative prototypes from white-box models; the second generalizes to black-box sources by aligning geometric distances with observed detection scores. Experiments on EvoBench and MAGE benchmarks demonstrate consistent improvements across multiple detection criteria and model families.

</details>

### 36. LAMCL: A Length-aware Momentum Contrastive Learning Framework for Multiscale Machine-Revised Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1118/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Bing Zhou、Zhe Huang、Shilei Tan、Kai Zhao、Zhou Yongcheng

- 🎯 **研究动机**：机器改写文本与原文差异细微，现有检测器尤其短文本上难捕捉细粒度语义差异
- 🔬 **研究方法**：LAMCL 的 EBD 模块融合 LLM 处理文本测语义一致性增强判别特征，LW 模块按文本长度与标签做难负采样提升表征鲁棒性
- 📌 **结论**：多场景、任务与 LLM 上的多尺度机器改写检测超现有检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting machine-revised text that exhibits subtle lexical differences from the original human-generated text remains a challenge. Recent detection methods, including watermarking-based, logit-based, and training-based models, struggle to capture the fine-grained semantic differences, especially for short texts. To address this issue, we propose Length-aware Momentum Contrastive Learning (LAMCL), a novel framework for multiscale machine-revised text detection that integrates two core modules. To enhance the discriminative semantic features, the Enhance Before Detection (EBD) module first fuses the original detected text with the counterpart processed by a Large Language Model (LLM), and then measures semantic consistency to distinguish between machine-revised and human-generated text. Meanwhile, based on the Momentum Contrastive Learning (MCL) framework, the Length-aware Weighting (LW) module leverages text length and label information for hard negative sampling, mitigating the ambiguity of short text attribution and boosting the robustness of representation learning. Experimental results demonstrate that our method outperforms the existing detectors in identifying multiscale machine-revised text across diverse practical scenarios, tasks, and LLMs. The code is available at https://github.com/hangtze/LAMCL.

</details>

### 37. Identifying Bias in Machine-generated Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.109/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Kevin Stowe、Svetlana Afanaseva、Rodolfo C. Raimundo、Yitao Sun、Kailash Patil

- 🎯 **研究动机**：机器文本检测器性能虽强但可能造成负面社会影响，其偏见未系统测量
- 🔬 **研究方法**：在学生作文数据集上评 16 个检测系统在性别、族裔、ELL 状态、经济状态四属性的偏见，用回归模型与子群分析
- 📌 **结论**：ELL 作文更易被判为机器生成，非白人 ELL 被不成比例误判；人类判别能力差但在这些属性上无显著偏见

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The meteoric rise in text generation capability has been accompanied by parallel growth in interest in machine-generated text detection: the capability to identify whether a given text was generated using a model or written by a person. While detection models show strong performance, they have the capacity to cause significant negative impacts. We explore potential biases in English machine-generated text detection systems. We curate a dataset of student essays and assess 16 different detection systems for bias across four attributes: gender, race/ethnicity, English-language learner (ELL) status, and economic status. We evaluate these attributes using regression-based models to determine the significance and power of the effects, as well as performing subgroup analysis. We find that while biases are generally inconsistent across systems, there are several key issues: several models tend to classify disadvantaged groups as machine-generated, ELL essays are more likely to be classified as machine-generated, economically disadvantaged students’ essays are less likely to be classified as machine-generated, and non-White ELL essays are disproportionately classified as machine-generated relative to their White counterparts. Finally, we perform human annotation and find that while humans perform generally poorly at the detection task, they show no significant biases on the studied attributes.

</details>

### 38. Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1211/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Xiaowei Zhu、Yubing Ren、Fang Fang、Shi Wang、Yanan Cao、Li Guo

- 🎯 **研究动机**：免训练 AI 文本检测器把 token 信号聚合成全局分数并假设 token 贡献均匀，短序列或局部修改下不鲁棒
- 🔬 **研究方法**：Exons-Detect 用 exon 感知 token 重加权：双模型设定下测隐藏态差异识别并放大信息性 exonic token，从重要性加权序列计算可解释翻译分数
- 📌 **结论**：达 SOTA 且抗对抗攻击与不同输入长度，DetectRL 上平均 AUROC 相对最强基线提升 2.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of large language models has increasingly blurred the boundary between human-written and AI-generated text, raising societal risks such as misinformation dissemination, authorship ambiguity, and threats to intellectual property rights. These concerns highlight the urgent need for effective and reliable detection methods. While existing training-free approaches often achieve strong performance by aggregating token-level signals into a global score, they typically assume uniform token contributions, making them less robust under short sequences or localized token modifications. To address these limitations, we propose Exons-Detect, a training-free method for AI-generated text detection based on an exon-aware token reweighting perspective. Exons-Detect identifies and amplifies informative exonic tokens by measuring hidden-state discrepancy under a dual-model setting, and computes an interpretable translation score from the resulting importance-weighted token sequence. Empirical evaluations demonstrate that Exons-Detect achieves state-of-the-art detection performance and exhibits strong robustness to adversarial attacks and varying input lengths. In particular, it attains a 2.2% relative improvement in average AUROC over the strongest prior baseline on DetectRL.

</details>

### 39. DetectRL-X: Towards Reliable Multilingual and Real-World LLM-Generated Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1773/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Junchao Wu、…、Derek F. Wong (黄辉)

- 🎯 **研究动机**：现有检测器在多语言与真实场景下的可靠性基本未被探索
- 🔬 **研究方法**：DetectRL-X 覆盖 8 种语言、6 个易滥用领域、4 个商用 LLM 的多语言基准，纳入润色、扩写、缩写等 AI 辅助写作操作，并做多语言释义与扰动攻击压力测试
- 📌 **结论**：揭示 SOTA 检测器在不同语言资源下的强弱，量化领域、生成器、攻击策略、文本长度与精炼操作对性能的影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The effective detection and governance of Large Language Model (LLM) generated content has become increasingly critical due to the growing risk of misuse. Despite the impressive performance of existing detectors, their reliability and potential in multilingual, real-world scenarios remain largely underexplored.In this study, we introduce DetectRL-X, a comprehensive multilingual benchmark designed to evaluate advanced detectors across 8 dimensions. The benchmark encompasses 8 languages commonly used in commercial contexts and collects human-written texts from 6 domains highly susceptible to LLM misuse. To better aligned with real-world applications, We create LLM-generated texts using 4 popular commercial LLMs, and include typical AI-assisted writing operations such as polishing, expanding, and condensing to capture authentic usage patterns. Furthermore, we develop a multilingual framework for paraphrasing and perturbation attacks to simulate diverse human modifications and writing noise, enabling stress testing of detectors across languages.Experimental results on DetectRL-X reveal the strengths and limitations of current state-of-the-art detectors when applied to diverse linguistic resources. We further analyze how domains, generators, attack strategies, text length, and refinement operations influence performance in different languages, underscoring DetectRL-X as an effective benchmark for strengthening multilingual and language-specific detectors.

</details>

### 40. CodeRipple: Wavelet-Based Detection of LLM-Generated Code

🎓 [Official](https://aclanthology.org/2026.acl-long.1777/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`cybersecurity`、`open-set detection`

👤 **作者**：Xingyu Yao、Zhendong Mao、Quan Wang

- 🎯 **研究动机**：从文本方法改编的免训练代码检测器依赖 token 困惑度序列全局统计，对代码效果差
- 🔬 **研究方法**：洞见：LLM 代码与人类代码全局统计收敛但局部 TPS 动态不同（窄瞬时尖峰对宽持续波动）；CodeRipple 用平稳小波变换建模波动形状、离散小波变换量化跨尺度能量分布
- 📌 **结论**：三个基准（多语言、多生成 LLM、多种逃避策略）上持续超越现有免训练方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting LLM-generated code is crucial for ensuring software provenance, security, reliability, and licensing compliance. Existing training-free detectors, mostly adapted from text-based methods, rely on global statistics of the Token Perplexity Sequence (TPS) and struggle with code. We reveal a key insight: despite the convergence of global statistics, LLM-generated and human-written code differ fundamentally in their local TPS dynamics: the former shows narrow transient spikes while the latter exhibits broad sustained fluctuations. To capture this distinction, we introduce CodeRipple, a novel training-free detection framework that employs wavelet analysis to characterize TPS morphology across scales. It jointly leverages the Stationary Wavelet Transform to model fluctuation shape and the Discrete Wavelet Transform to quantify cross-scale energy distribution. Evaluated on three challenging benchmarks spanning diverse programming languages, multiple generating LLMs, and various evasion strategies, CodeRipple consistently outperforms existing training-free methods, demonstrating its superior effectiveness and generalizability without any model training. Code available at: https://github.com/yaoxingyu77/CodeRipple.

</details>

### 41. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.120/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`representation intervention`、`open-set detection`

👤 **作者**：Xiao Pu、Zepeng Cheng、Lin Yuan、Yu Wu、Xiuli Bi

- 🎯 **研究动机**：依赖生成器特定伪影的 AI 文本检测本质上不稳定——新模型快速涌现使捷径失效，未见生成器泛化是核心难题
- 🔬 **研究方法**：渐进结构化框架解耦 AI 检测语义与生成器感知伪影：紧致潜编码鼓励语义最小性，扰动正则减少残余纠缠，判别适应对齐任务目标
- 📌 **结论**：MAGE 基准（7 类 20 个 LLM）上准确率最高提升 24.2%、F1 提升 26.2%，训练生成器越多样性能越好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) generate text that increasingly resembles human writing, the subtle cues that distinguish AI-generated content from human-written content become increasingly challenging to capture. Reliance on generator-specific artifacts is inherently unstable, since new models emerge rapidly and reduce the robustness of such shortcuts. This generalizes unseen generators as a central and challenging problem for AI-text detection. To tackle this challenge, we propose a progressively structured framework that disentangles AI-detection semantics from generator-aware artifacts. This is achieved through a compact latent encoding that encourages semantic minimality, followed by perturbation-based regularization to reduce residual entanglement, and finally a discriminative adaptation stage that aligns representations with task objectives. Experiments on MAGE benchmark, covering 20 representative LLMs across 7 categories, demonstrate consistent improvements over state-of-the-art methods, achieving up to 24.2% accuracy gain and 26.2% F 1 improvement. Notably, performance continues to improve as the diversity of training generators increases, confirming strong scalability and generalization in open-set scenarios. Our source code will be publicly available at https://github.com/PuXiao06/DRGD.

</details>

### 42. Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.235/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Yang Li、Qiang Sheng、Zhengjia Wang、Yehan Yang、Danding Wang、Juan Cao

- 🎯 **研究动机**：二或三分类检测不足以支撑细粒度监管——LLM 润色的人类文本与人类化的 LLM 文本触发不同政策后果
- 🔬 **研究方法**：RACE 在四分类设定下建模 creator 与 editor 双重角色：修辞结构理论构建创作者逻辑图，EDU 级特征刻画编辑者风格
- 📌 **结论**：细粒度识别超越 12 个基线且误报低，提供政策对齐的监管方案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The misuse of large language models (LLMs) requires precise detection of synthetic text. Existing works mainly follow binary or ternary classification settings, which can only distinguish pure human/LLM text or collaborative text at best. This remains insufficient for the nuanced regulation, as the LLM-polished human text and humanized LLM text often trigger different policy consequences. In this paper, we explore fine-grained LLM-generated text detection under a rigorous four-class setting. To handle such complexities, we propose RACE (Rhetorical Analysis for Creator-Editor Modeling), a fine-grained detection method that characterizes the distinct signatures of creator and editor. Specifically, RACE utilizes Rhetorical Structure Theory (RST) to construct a logic graph for the creator’s foundation while extracting Elementary Discourse Unit (EDU)-level features for the editor’s style. Experiments show that RACE outperforms 12 baselines in identifying fine-grained types with low false alarms, offering a policy-aligned solution for LLM regulation.

</details>

### 43. Authorship Attribution in Multilingual Machine-Generated Texts

🎓 [Official](https://aclanthology.org/2026.acl-long.2091/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`authorship attribution`、`AI-generated content`、`cross-generator detection`、`open-set detection`

👤 **作者**：Lucio La Cava、Dominik Macko、Robert Moro、Ivan Srba、Andrea Tagarelli

- 🎯 **研究动机**：机器生成文本的作者归因局限于单语（以英语为主），忽视现代 LLM 的多语言使用现实
- 🔬 **研究方法**：定义多语言作者归因问题，覆盖 18 种语言（多语系与文字系统）与 8 个生成者（7 个 LLM 加人类），考察单语 AA 方法的跨语言迁移性与生成器影响
- 📌 **结论**：部分单语方法可适配多语言，但跨语系迁移存在显著局限，凸显多语言 AA 的复杂性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Models (LLMs) have reached human-like fluency and coherence, distinguishing machine-generated text (MGT) from human-written content becomes increasingly difficult. While early efforts in MGT detection have focused on binary classification, the growing landscape and diversity of LLMs require a more fine-grained yet challenging authorship attribution (AA), i.e., being able to identify the precise generator (LLM or human) behind a text. However, AA remains nowadays confined to a monolingual setting, with English being the most investigated one, overlooking the multilingual nature and usage of modern LLMs. In this work, we introduce the problem of Multilingual Authorship Attribution, which involves attributing texts to human or multiple LLM generators across diverse languages. Focusing on 18 languages—covering multiple families and writing scripts—and 8 generators (7 LLMs and the human-authored class), we investigate the multilingual suitability of monolingual AA methods in terms of their cross-lingual transferability, and the impact of generators on attribution performance. Our results reveal that while certain monolingual AA methods can be adapted to multilingual settings, significant limitations and challenges remain, particularly in transferring across diverse language families, underscoring the complexity of multilingual AA and the need for more robust approaches to better match real-world scenarios.

</details>

### 44. Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection

📄 [arXiv](https://arxiv.org/abs/2605.01647) · 📊 [Dataset](https://huggingface.co/datasets/nsp909/MDTA) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`benchmark`、`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`AI-generated text`

👤 **作者**：Priyadarshan Narayanasamy、Swastik Agrawal、Klint Faber、Fardina Fathmiul Alam

- 🎯 **研究动机**：基于 log 概率的免训练 AI 文本检测面临 RLHF 使概率分布趋近人类的天花板
- 🔬 **研究方法**：提出字符分布签名信号与 LD-Score，构建 MDTA 基准（642,274 个样本对、4 模型、5 域、3 温度、3 对抗策略）
- 📌 **结论**：LD-Score 与 perplexity 方法相关性低（r=0.08-0.13），经非线性分类器并入 DNA-DetectLLM、Binoculars 后 AUROC 与 F1 持续提升，专业域收益最大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training-free AI text detection methods primarily rely on model log-probabilities, achieving strong performance through approaches like Binoculars and DNA-DetectLLM. However, these methods face a fundamental ceiling as models are optimized through RLHF to produce human-like probability distributions. We introduce an alternative detection signal based on character distribution signatures. We provide theoretical foundations showing that AI models, trained on massive domain-balanced corpora, approximate global character patterns while humans exhibit domain-specialized distributions, creating a "Wall of Separation" where human-AI divergence significantly exceeds AI-AI divergence. To enable systematic evaluation, we construct the Models-Domains-Temperatures-Adversarials (MDTA) benchmark comprising 642,274 prompt-aligned samples across 4 models, 5 domains, 3 temperature settings, and 3 adversarial strategies, substantially expanding the HC3 dataset with modern model responses, temperature variation, and adversarial augmentation. We introduce the Letter Distribution Score (LD-Score), demonstrating low correlation (r = 0.08-0.13) with perplexity methods. When integrated with DNA-DetectLLM, Binoculars and FastDetectGPT via a non-linear classifier, LD-Score yields consistent improvements in AUROC and F1, with particularly pronounced gains in specialized domains where vocabulary constraints amplify the detection signal. The MDTA dataset can be accessed at: https://huggingface.co/datasets/nsp909/MDTA.

</details>

### 45. Who Wrote This Line? Evaluating the Detection of LLM-Generated Classical Chinese Poetry

🎓 [Official](https://aclanthology.org/2026.acl-long.245/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`AI-generated content`、`cross-generator detection`、`generalization`、`open-set detection`、`authorship attribution`

👤 **作者**：Jiang Li、…、Xiangdong Su

- 🎯 **研究动机**：古典汉语诗歌格律严格、意象体系共享、句法灵活，LLM 生成检测尚未被研究
- 🔬 **研究方法**：提出 ChangAn 基准：共 30664 首诗（10276 首人写、20388 首由四个流行 LLM 生成），系统评测 12 个检测器在不同文本粒度与生成策略下的表现
- 📌 **结论**：现有中文文本检测器不可靠，无法作为检测 LLM 生成古诗的工具

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid development of large language models (LLMs) has extended text generation tasks into the literary domain. However, AI-generated literary creations has raised increasingly prominent issues of creative authenticity and ethics in literary world, making the detection of LLM-generated literary texts essential and urgent. While previous works have made significant progress in detecting AI-generated text, it has yet to address classical Chinese poetry. Due to the unique linguistic features of classical Chinese poetry, such as strict metrical regularity, a shared system of poetic imagery, and flexible syntax, distinguishing whether a poem is authored by AI presents a substantial challenge. To address these issues, we introduce ChangAn, a benchmark for detecting LLM-generated classical Chinese poetry that containing total 30,664 poems, 10,276 are human-written poems and 20,388 poems are generated by four popular LLMs. Based on ChangAn, we conducted a systematic evaluation of 12 AI detectors, investigating their performance variations across different text granularities and generation strategies. Our findings highlight the limitations of current Chinese text detectors, which fail to serve as reliable tools for detecting LLM-generated classical Chinese poetry. These results validate the effectiveness and necessity of our proposed ChangAn benchmark. Our dataset and code are available at https://github.com/VelikayaScarlet/ChangAn.

</details>

### 46. Learning Human-Perceived Fakeness in AI-Generated Videos via Multimodal LLMs

📄 [arXiv](https://arxiv.org/abs/2509.22646) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-09

**关键词**：`benchmark`、`AI-generated content`、`VLM safety`、`cross-generator detection`、`AI-video detection`、`deepfake trace`

👤 **作者**：Xingyu Fu、…、Chris Callison-Burch

- 🎯 **研究动机**：人类能否识别并定位 AI 生成视频中的破绽这一维度被忽视
- 🔬 **研究方法**：构建 DeeptraceReward：4.3K 条含自然语言解释、边界框与起止时间戳的标注覆盖 3.3K 生成视频，归为 9 大类破绽并训练多模态奖励模型模仿人类判断与定位
- 📌 **结论**：7B 奖励模型平均超 GPT-5 达 34.7%；真假二分类最易，解释、空间定位、时间标注难度递增

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Can humans identify AI-generated (fake) videos and provide grounded reasons? While video generation models have advanced rapidly, a critical dimension -- whether humans can detect deepfake traces within a generated video, i.e., spatiotemporal grounded visual artifacts that reveal a video as machine generated -- has been largely overlooked. We introduce DeeptraceReward, the first fine-grained, spatially- and temporally- aware benchmark that annotates human-perceived fake traces for video generation reward. The dataset comprises 4.3K detailed annotations across 3.3K high-quality generated videos. Each annotation provides a natural-language explanation, pinpoints a bounding-box region containing the perceived trace, and marks precise onset and offset timestamps. We consolidate these annotations into 9 major categories of deepfake traces that lead humans to identify a video as AI-generated, and train multimodal language models (LMs) as reward models to mimic human judgments and localizations. On DeeptraceReward, our 7B reward model outperforms GPT-5 by 34.7% on average across fake clue identification, grounding, and explanation. Interestingly, we observe a consistent difficulty gradient: binary fake v.s. real classification is substantially easier than fine-grained deepfake trace detection; within the latter, performance degrades from natural language explanations (easiest), to spatial grounding, to temporal labeling (hardest). By foregrounding human-perceived deepfake traces, DeeptraceReward provides a rigorous testbed and training signal for socially aware and trustworthy video generation.

</details>

### 47. DF-MoE: Generalizable Deepfake Detection via Multimodal Sparse Mixture-of-Experts

📄 [arXiv](https://arxiv.org/abs/2608.23363) · 🌐 [Project](https://bmvc2026.bmva.org/programme/accepted_papers/)　📅 2026-08

**关键词**：`detection`、`audio-visual deepfake`、`high-level forensic cue`、`cross-domain generalization`、`AI-generated video`、`audio-visual cue`

👤 **作者**：Vlad Hondru、Florinel Alin Croitoru、Iuliana Georgescu、A. Sophia Koepke、Radu Tudor Ionescu

- 🎯 **研究动机**：音视频 deepfake 检测器易过拟合特定生成器伪影，跨生成方法泛化是主要挑战
- 🔬 **研究方法**：DF-MoE 用多种预训练模型提取高层线索（嘴部动作、人脸解析、表情、头姿、视线、心率、音频情绪、语音活动），经 Mixture-of-Experts 骨干整合单模态与多模态证据
- 📌 **结论**：在 MAVOS-DD、AVLips、PolyGlotFake、BioDeepAV、FakeAVCeleb 五个 benchmark 的域内与跨域实验中全面超过 SoTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-visual deepfake detection is an actively studied topic, where one of the main challenges is to develop detectors able to generalize across deepfake generation methods. We conjecture that overfitting can be mitigated by extracting multiple high-level cues from the available audio and visual modalities via pre-trained models. We therefore assemble a wide variety of pre-trained models to extract features that encode mouth movements, face parsing, facial expressions, head pose, gaze tracking, heart rate, audio emotion and speech activity. We further integrate both unimodal and multimodal cues via a Mixture-of-Experts (MoE) backbone to detect deepfakes. We perform in-domain and cross-domain experiments on five benchmarks for deepfake detection (MAVOS-DD, AVLips, PolyGlotFake, BioDeepAV, FakeAVCeleb) to compare our framework (DF-MoE) with state-of-the-art methods. Our results indicate that DF-MoE obtains superior deepfake detection results, surpassing all competing methods. We release our code at https://github.com/vladhondru25/DF-MoE.

</details>

### 48. SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection

📄 [arXiv](https://arxiv.org/abs/2607.03069) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4333)　📅 2026-07　🏷 ECCV 2026

**关键词**：`detection`、`AI-generated video detection`、`multi-agent`、`multi-agent system`、`societal risk`

👤 **作者**：Wenlin Wu、Sheng Zhou、Peipei Song、Wenhao Wang、Junbin Xiao、Xun Yang

- 🎯 **研究动机**：现有基准偏感知保真度，缺少需要推理物理规律、结构一致与社会逻辑违规的检测场景，形成感知-推理鸿沟
- 🔬 **研究方法**：提出 SafeGuard 多 agent 框架：层级感知求解器提取细粒度取证证据，自反思验证器强制语义推理与物理合理性一致形成可解释证据链；并构建 2 万视频、10 类社会风险的 SafeVid 基准
- 📌 **结论**：SafeVid 准确率提升 18.7%，并在四个公开基准上一致超越已有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As video generation paradigms evolve from localized manipulation to full-scene synthesis, AI-generated video detection becomes increasingly challenging, as forgeries exhibit coherent global structure and high perceptual realism. However, existing benchmarks are biased toward perceptual fidelity and primarily evaluate detectors based on perceptual artifacts, providing limited coverage of scenarios that require reasoning about violations of physical laws, structural coherence, or social logic. This dataset bias shapes current approaches and results in a Perception-Reasoning Gap: artifact-centric models capture low-level statistical irregularities yet lack semantic inference, whereas vision-language models perform semantic reasoning but remain insensitive to fine-grained forensic cues. To bridge this gap, we propose SafeGuard, a multi-agent framework that enables collaborative specialization between forensic perception and semantic reasoning. A hierarchical perceptual solver extracts fine-grained forensic evidence, while a self-reflective verifier enforces consistency between semantic inference and physical plausibility, forming an interpretable evidence chain. To support evaluation, we introduce SafeVid, a novel AI-generated video detection benchmark comprising 20K videos spanning 10 social risk categories, designed to evaluate physical plausibility, structural consistency, and the rationality of social behaviors. Extensive experiments demonstrate the generalization of SafeGuard, improving accuracy on SafeVid by +18.7% and consistently outperforming prior methods across four public benchmarks.

</details>

### 49. Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods

📄 [arXiv](https://arxiv.org/abs/2603.15026) · 🌐 [Project](https://omerbenhayun.github.io/stall-video) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Hayun_Training-free_Detection_of_Generated_Videos_via_Spatial-Temporal_Likelihoods_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`generated video`、`spatial-temporal likelihood`、`training-free method`

👤 **作者**：Omer Ben Hayun、Roy Betser、Meir Yossef Levi、Levi Kassel、Guy Gilboa

- 🎯 **研究动机**：逐帧检测忽略时序动态，监督视频检测器对快速涌现的未见生成器泛化差
- 🔬 **研究方法**：STALL 免训练在概率框架内联合建模空间与时序似然为视频打分，并发布含 SOTA 生成模型的 ComGenVid 基准
- 📌 **结论**：在两个公开基准与新基准上持续超越图像级与视频级基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Following major advances in text and image generation, the video domain has surged, producing highly realistic and controllable sequences. Along with this progress, these models also raise serious concerns about misinformation, making reliable detection of synthetic videos increasingly crucial. Image-based detectors are fundamentally limited because they operate per frame and ignore temporal dynamics, while supervised video detectors generalize poorly to unseen generators, a critical drawback given the rapid emergence of new models. These challenges motivate zero-shot approaches, which avoid synthetic data and instead score content against real-data statistics, enabling training-free, model-agnostic detection. We introduce STALL, a simple, training-free, theoretically justified detector that provides likelihood-based scoring for videos, jointly modeling spatial and temporal evidence within a probabilistic framework. We evaluate STALL on two public benchmarks and introduce ComGenVid, a new benchmark with state-of-the-art generative models. STALL consistently outperforms prior image- and video-based baselines. Code and data are available at https://omerbenhayun.github.io/stall-video.

</details>

### 50. VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2602.08828) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61929)　📅 2026-02　🏷 ICML 2026

**关键词**：`detection`、`reinforcement learning`、`AI-generated content`、`cross-generator detection`、`deepfake detection`、`cross-generator generalization`

👤 **作者**：Hao Tan、…、Zhen Lei

- 🎯 **研究动机**：现有 AI 生成视频检测偏向表面推理或机械分析，MLLM 细粒度感知能力不足
- 🔬 **研究方法**：VideoVeritas 以时空定位与自监督计数等感知前置任务的强化学习（PPRL）加偏好对齐训练检测器，并发布含 3K 视频、9 个生成器的 MintVid 数据集
- 📌 **结论**：在多样基准上取得更均衡的性能与跨生成器泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing capability of video generation poses escalating security risks, making reliable detection increasingly essential. In this paper, we introduce VideoVeritas, a framework that integrates fine-grained perception and fact-based reasoning. We observe that while current multi-modal large language models (MLLMs) exhibit strong reasoning capacity, their granular perception ability remains limited. To mitigate this, we introduce Joint Preference Alignment and Perception Pretext Reinforcement Learning (PPRL). Specifically, rather than directly optimizing for detection task, we adopt general spatiotemporal grounding and self-supervised object counting in the RL stage, enhancing detection performance with simple perception pretext tasks. To facilitate robust evaluation, we further introduce MintVid, a light yet high-quality dataset containing 3K videos from 9 state-of-the-art generators, along with a real-world collected subset that has factual errors in content. Experimental results demonstrate that existing methods tend to bias towards either superficial reasoning or mechanical analysis, while VideoVeritas achieves more balanced performance across diverse benchmarks.

</details>

### 51. Your One-Stop Solution for AI-Generated Video Detection

📄 [arXiv](https://arxiv.org/abs/2601.11035) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Ma_Your_One-Stop_Solution_for_AI-Generated_Video_Detection_CVPR_2026_paper.html)　📅 2026-01　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated video`、`unified detector`、`open-world generalization`

👤 **作者**：Long Ma、…、Zhen Bi

- 🎯 **研究动机**：现有 AI 生成视频检测数据集规模小、生成器陈旧，基准停留在数据集构建层面
- 🔬 **研究方法**：构建 AIGVDBench：覆盖 31 个 SOTA 生成模型、超 44 万视频，对四类 33 个检测器执行 1500 余次评测并做 8 项深入分析
- 📌 **结论**：识别出 4 项新发现，为 AI 生成视频检测提供系统性基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative modeling can create remarkably realistic synthetic videos, making it increasingly difficult for humans to distinguish them from real ones and necessitating reliable detection methods. However, two key limitations hinder the development of this field. \textbf{From the dataset perspective}, existing datasets are often limited in scale and constructed using outdated or narrowly scoped generative models, making it difficult to capture the diversity and rapid evolution of modern generative techniques. Moreover, the dataset construction process frequently prioritizes quantity over quality, neglecting essential aspects such as semantic diversity, scenario coverage, and technological representativeness. \textbf{From the benchmark perspective}, current benchmarks largely remain at the stage of dataset creation, leaving many fundamental issues and in-depth analysis yet to be systematically explored. Addressing this gap, we propose AIGVDBench, a benchmark designed to be comprehensive and representative, covering \textbf{31} state-of-the-art generation models and over \textbf{440,000} videos. By executing more than \textbf{1,500} evaluations on \textbf{33} existing detectors belonging to four distinct categories. This work presents \textbf{8 in-depth analyses} from multiple perspectives and identifies \textbf{4 novel findings} that offer valuable insights for future research. We hope this work provides a solid foundation for advancing the field of AI-generated video detection. Our benchmark is open-sourced at https://github.com/LongMa-2025/AIGVDBench.

</details>

### 52. Real Data Lies: Unveiling and Closing the Quality Shortcut in Generalizable AI-Generated Video Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/61218)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Ziyuan Fang、Tianyi Wei、Guanjie Wang、Weiming Zhang、Nenghai Yu、Wenbo Zhou

- 🎯 **研究动机**：AIGC 视频检测器的训练存在真假数据质量偏差导致捷径学习，在相似分布上测试造成泛化假象
- 🔬 **研究方法**：提出质量匹配的真假数据训练协议，并扩展训练集覆盖完整质量谱，使模型学到质量无关的检测特征
- 📌 **结论**：方法在多种骨干上一致提升对低质量差异真实数据的泛化能力，可扩展且增强真实场景适用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in video generation have enabled highly realistic synthetic content, raising concerns about the integrity of digital media and motivating the development of benchmarks and detection methods for generated videos. Prior works have largely prioritized bolstering model generalization against unseen generators. However, we uncover a neglected factor: the quality distribution of real videos plays a pivotal role. Current training protocols suffer from a clear quality bias between real and fake data, prone to shortcut learning. Compounded by testing on similar real data distributions, this creates an illusion of generalization. In reality, these models fail to generalize when exposed to real data with significantly different quality profiles. To address this, we propose training with quality-matched real and fake data to mitigate bias. Building on this, we introduce a data expansion strategy that broadens the training set to comprehensively cover the full quality spectrum. This approach enables the model to learn quality-agnostic features for detection, thereby achieving generalization across real data of varying qualities and enhancing real-world applicability. Extensive experiments demonstrate that our method scales well across diverse backbones, consistently enhancing the generalization capability of existing models.

</details>

### 53. Beyond Pixels: Mining Compressed Domain Artifacts for Efficient AI-Generated Video Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/62999)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Anran Zhu、…、Chao Shen

- 🎯 **研究动机**：像素域 AIGV 检测纠缠任务无关语义、计算冗余，忽视压缩比特流中免费的信号——运动向量与残差直接编码时空生成伪影
- 🔬 **研究方法**：STREAM 直接从压缩比特流检测：利用 I 帧、运动向量与残差捕捉被解压滤波平滑掉的时空伪影，轻量网络配运动引导对齐与门控融合
- 📌 **结论**：取得 mAP 0.965 的 SOTA 性能，推理比先前 SOTA 快 2.5 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of high-fidelity video generation models, robust AI-generated video (AIGV) detection has become increasingly needed. While most AIGV detection methods operate in the decoded pixel domain, we observe that detection in the pixel domain inevitably entangles task-irrelevant semantic information, leading to substantial semantic redundancy and extensive redundant computation, while overlooking free-to-use signals in compressed bitstreams. In particular, motion vectors and residuals directly encode temporal and spatial generative artifacts but remain largely underexplored. To address these issues, we propose a unified framework for S patio- T emporal RE sidual and A rtifact M ining, namely STREAM, which enables AIGV detection directly from compressed bitstreams. STREAM leverages I-frames, motion vectors, and residual errors to capture spatiotemporal artifacts that are typically smoothed out by decompression filters. In particular, we design a lightweight network with a motion-guided alignment module and a gated fusion mechanism, enabling adaptive fusion of spatial artifacts and nonlinear temporal dynamics. Extensive experimental results demonstrate that STREAM achieves SOTA performance with an mAP of 0.965, with 2.5× faster inference than previous SOTA baselines.

</details>

### 54. Ariadne's Thread of LipSync: Unraveling Forgeries via Inconsistency between Lip Motions and Head Poses

🎓 [Official](https://icml.cc/virtual/2026/poster/60674)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Tianyi She、Jiawei Liu、Weifeng Liu、Hanqing Zhao、Weiming Zhang、Kejiang Chen

- 🎯 **研究动机**：LipSync 生成模型在优化唇形同步的同时消除视觉伪影，关键检测信号缺失
- 🔬 **研究方法**：利用唇动与头部姿态的固有生物耦合——生成模型优化局部唇动会破坏全局协调；LipDA 对比唇与姿态特征量化不一致做检测，捕捉时序动态与音视频同步指纹做归因，并构建多生成器数据集 LipSyncBench-A
- 📌 **结论**：检测 AUC 超 97%、模型归因准确率 97.5%，显著超越现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in LipSync generation technology have led to the creation of highly realistic videos, posing severe societal risks. However, existing defense strategies struggle against LipSync forgeries, as state-of-the-art generative models not only optimize for the lip synchronization but also significantly eliminate visual artifacts, resulting in the lack of key detection signals. Inspired by the inherent biological coupling between lip movements and head poses in natural speech, we observe that generative models fundamentally disrupt this global coordination when optimizing for local lip motion. In this paper, we propose LipDA, a novel framework for joint LipSync Detection and Attribution, which takes advantage of the inconsistency between head and lip. For detection, the framework learns to quantify this discrepancy by contrasting lip and pose features from authentic versus forged videos. For attribution, our method is designed to capture the unique temporal dynamics and audio-visual synchronization patterns that act as generative fingerprints, enabling source tracing. To validate our approach, we conduct extensive experiments on two challenging LipSync benchmarks as well as on our own proposed large-scale and multi-generator dataset, LipSyncBench-A. LipDA achieves over 97% AUC in detection and 97.5% accuracy in model attribution, significantly outperforming existing methods.

</details>

### 55. CoCoVideo: The High-Quality Commercial-Model-Based Contrastive Benchmark for AI-Generated Video Detection

📄 [arXiv](https://arxiv.org/abs/2606.00101) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_CoCoVideo_The_High-Quality_Commercial-Model-Based_Contrastive_Benchmark_for_AI-Generated_Video_Detection_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`AI-generated video`、`commercial model`、`contrastive evaluation`

👤 **作者**：Huidong Feng、…、Ming Zeng

- 🎯 **研究动机**：现有 AIGC 视频数据集依赖质量远低于商业系统的开源模型，含商业样本的也常留可见水印，阻碍高保真伪造检测
- 🔬 **研究方法**：CoCoVideo-26K 覆盖 13 个主流商业生成器的语义对齐真-假视频对；CoCoDetect 用 R3D-18 提取时空表征，置信门控把不确定样本路由给 MLLM 推理物理合理性与场景一致性
- 📌 **结论**：在 CoCoVideo-26K 与公开基准上达 SOTA，验证鲁棒性与通用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of artificial intelligence generated content (AIGC) technologies, video forgery has become increasingly prevalent, posing new challenges to public discourse and societal security. Despite remarkable progress in existing deepfake detection methods, AIGC forgery detection remains challenging, as existing datasets mainly rely on open-source video generation models with quality far below commercial AIGC systems. Even datasets containing a few commercial samples often retain visible watermarks, compromising authenticity and hindering model generalization to high-fidelity AIGC videos. To address these issues, we introduce CoCoVideo-26K, a contrastive, commercial-model-based AIGC video dataset covering 13 mainstream commercial generators and providing semantically aligned real-fake video pairs. This dataset enables deeper exploration of the differences between authentic and high-quality synthetic videos, establishes a new benchmark for highly realistic video forgery detection. Building on this dataset, we propose CoCoDetect, a detection framework integrating contrastive learning with confidence-gated multimodal large language model (MLLM) inference. An R3D-18 backbone extracts spatio-temporal representations, while a confidence gate routes uncertain cases to an MLLM for reasoning about physical plausibility and scene consistency. Extensive experiments on CoCoVideo-26K and public benchmarks demonstrate state-of-the-art performance, validating the framework's robustness and generality. Our code and dataset are available at https://github.com/DonoToT/CoCoVideo.

</details>

### 56. Skyra: AI-Generated Video Detection via Grounded Artifact Reasoning

📄 [arXiv](https://arxiv.org/abs/2512.15693) · 🌐 [Project](https://joeleelyf.github.io/Skyra) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Skyra_AI-Generated_Video_Detection_via_Grounded_Artifact_Reasoning_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`detection`、`AI-generated video`、`artifact grounding`、`temporal reasoning`

👤 **作者**：Yifei Li、…、Jiwen Lu

- 🎯 **研究动机**：现有 AI 生成视频检测多止于二分类，缺少人类可理解的解释依据
- 🔬 **研究方法**：Skyra 以人类可感知视觉伪影为接地证据做检测与解释，构建首个细粒度人工标注的伪影数据集 ViF-CoT-4K 与两阶段训练策略，并发布 3K 样本、覆盖十余种生成器的 ViF-Bench
- 📌 **结论**：在多个基准上超越现有方法，同步增强时空伪影感知、解释能力与检测准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The misuse of AI-driven video generation technologies has raised serious social concerns, highlighting the urgent need for reliable AI-generated video detectors. However, most existing methods are limited to binary classification and lack the necessary explanations for human interpretation. In this paper, we present Skyra, a specialized multimodal large language model (MLLM) that identifies human-perceivable visual artifacts in AI-generated videos and leverages them as grounded evidence for both detection and explanation. To support this objective, we construct ViF-CoT-4K for Supervised Fine-Tuning (SFT), which represents the first large-scale AI-generated video artifact dataset with fine-grained human annotations. We then develop a two-stage training strategy that systematically enhances our model's spatio-temporal artifact perception, explanation capability, and detection accuracy. To comprehensively evaluate Skyra, we introduce ViF-Bench, a benchmark comprising 3K high-quality samples generated by over ten state-of-the-art video generators. Extensive experiments demonstrate that Skyra surpasses existing methods across multiple benchmarks, while our evaluation yields valuable insights for advancing explainable AI-generated video detection.

</details>

### 57. Distinguishing AI-Generated Music from Edited Audio as a Hard-Negative Robustness Task

📄 [arXiv](https://arxiv.org/abs/2608.14916) · 🌐 [Project](https://sites.google.com/view/robustifai-workshop/program)　📅 2026-08

**关键词**：`analysis`、`AI-generated content`、`adversarial robustness`、`cross-generator detection`

👤 **作者**：Alexandru-Stefan Morosanu、Valerian Cecan、Stefan-Daniel Achirei、Laura Erhan

- 🎯 **研究动机**：AI 音乐检测器通常对原始歌评测，真实上传多为 remix、重编码、变调的编辑版——一类困难负样本
- 🔬 **研究方法**：构建 YouTube 锚歌对齐的 AI、编辑、原始三变体数据集（原始曲目仅作参照），以 10 秒片段输入 PaSST 训练二分类器，全部按锚歌切分防泄漏
- 📌 **结论**：视频级平衡准确率 0.811；AI 片段 F1 0.836 高于编辑片段 0.720——AI 生成音乐的光谱指纹与编辑伪影仍存在重叠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI-generated music detectors are commonly evaluated against original songs, but real-world uploads are often remixed, re-encoded, pitch-shifted, or otherwise edited. These edited versions form a difficult negative class: they are not generated by AI, yet they may introduce spectral artifacts that resemble synthetic audio fingerprints. We study this problem as a hard-negative robustness setting for AI-generated music detection, focusing on AI-generated and edited variants derived from the same anchor songs. We compile a YouTube-based dataset of AI, edited, and original variants, using the original tracks only as references, and train a binary AI versus edited detector. Audio is processed as 10-second clips and passed as raw waveforms to a pretrained PaSST spectrogram transformer. To reduce leakage, all splits are performed by anchor song. On the held-out test set, the final video-level system achieves 0.811 balanced accuracy. At clip level, AI-generated clips reach an F1-score of 0.836, while edited clips reach a lower F1-score of 0.720. The results suggest that AI-generated music retains detectable fingerprint-like spectral cues beyond ordinary editing, but the lower edited-class F1-score shows that these cues can still overlap with artifacts from edited audio. Grad-CAM visualizations are used to inspect whether high-confidence predictions rely on localized time-frequency regions.

</details>

### 58. MusicDET: Zero-Shot AI-Generated Music Detection

📄 [arXiv](https://arxiv.org/abs/2605.18072) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65106)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`cross-generator detection`、`generalization`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Chaolei Han、Hongsong Wang、Jie Gui

- 🎯 **研究动机**：判别式 AI 音乐检测器训练依赖生成样本，遇未见生成器性能严重退化
- 🔬 **研究方法**：MusicDET 零样本设定只用真实音乐训练：频率引导归一化流概率建模真实音乐特征分布，按似然检测分布外信号
- 📌 **结论**：FakeMusicCaps 与 SONICS 上持续超判别式检测器，检测未见生成器音乐尤甚

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting AI-generated music is crucial for preserving artistic authenticity and preventing the misuse of generative music technologies. However, existing discriminative detectors typically rely on generated samples during training and often suffer from severe performance degradation when confronted with music produced by unseen generators, which limits their real-world applicability. To address this issue, we formulate a zero-shot setting for AI-generated music detection, where the detector is trained exclusively on real music without access to any generated samples. Under this setting, we propose MusicDET, a generator-agnostic detection framework based on frequency-guided normalizing flows that probabilistically models the distribution of real music features. By evaluating the likelihood of an input sample under the learned real-music distribution, MusicDET enables effective detection of out-of-distribution music signals. Experiments on the FakeMusicCaps and SONICS datasets show that MusicDET consistently outperforms conventional discriminative detectors, particularly when detecting music generated by previously unseen models. The code is at https://github.com/Chaolei98/MusicDET

</details>

### 59. Explainable Disentangled Representation Learning for Generalizable Authorship Attribution in the Era of Generative AI

🎓 [Official](https://aclanthology.org/2026.acl-long.2018/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`explainability`、`model transparency`、`auditability`、`representation intervention`、`AI-generated content`

👤 **作者**：Hieu Man、Van-Cuong Pham、Nghia Trung Ngo、Franck Dernoncourt、Thien Nguyen

- 🎯 **研究动机**：作者归属与 AI 文本检测受内容-风格纠缠困扰——模型学到风格与主题的虚假相关，跨域泛化差
- 🔬 **研究方法**：EAVAE 分离式设计：监督对比预训练风格编码器，VAE 双编码器分离风格与内容，判别器同时区分配对归属并生成自然语言解释
- 📌 **结论**：Amazon Reviews、PAN21、HRS 上归属 SOTA，M4 上 AI 文本检测少样本领先

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Learning robust representations of authorial style is crucial for authorship attribution and AI-generated text detection. However, existing methods often struggle with content-style entanglement, where models learn spurious correlations between authors’ writing styles and topics, leading to poor generalization across domains. To address this challenge, we propose Explainable Authorship Variational Autoencoder (EAVAE), a novel framework that explicitly disentangles style from content through architectural separation-by-design. EAVAE first pretrains style encoders using supervised contrastive learning on diverse authorship data, then finetunes with a Variational Autoencoder (VEA) architecture using separate encoders for style and content representations. Disentanglement is enforced through a novel discriminator that not only distinguishes whether pairs of style/content representations belong to the same or different authors/content sources, but also generates natural language explanation for their decision, simultaneously mitigating confounding information and enhancing interpretability. Extensive experiments demonstrate the effectiveness of EAVAE. On authorship attribution, we achieve state-of-the-art performance on various datasets, including Amazon Reviews, PAN21, and HRS. For AI-generated text detection, EAVAE excels in few-shot learning over the M4 dataset.

</details>

### 60. Moiré Video Authentication: A Physical Signature Against AI Video Generation

📄 [arXiv](https://arxiv.org/abs/2604.01654) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3761)　📅 2026-04　🏷 ECCV 2026

**关键词**：`defense`、`video authentication`、`video generation`、`unsafe synthesis`、`physical watermark`、`synthetic media detection`

👤 **作者**：Yuan Qing、Kunyu Zheng、Lingxiao Li、Boqing Gong、Chang Xiao

- 🎯 **研究动机**：AI 生成视频越来越难辨别，需要生成模型无法忠实复现的物理签名
- 🔬 **研究方法**：利用相机拍摄双层光栅产生的 Moiré 条纹，推导 Moiré 运动不变量（条纹相位与光栅位移线性耦合），验证器从视频提取双信号检验相关性
- 📌 **结论**：真实与 AI 生成视频的相关性签名显著不同，为视频鉴真提供物理接地的可验证依据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in video generation have made AI-synthesized content increasingly difficult to distinguish from real footage. We propose a physics-based authentication signature that real cameras produce naturally, but that generative models cannot faithfully reproduce. Our approach exploits the Moiré effect: the interference fringes formed when a camera views a compact two-layer grating structure. We derive the Moiré motion invariant, showing that fringe phase and grating image displacement are linearly coupled by optical geometry, independent of viewing distance and grating structure. A verifier extracts both signals from video and tests their correlation. We validate the invariant on both real-captured and AI-generated videos from multiple state-of-the-art generators, and find that real and AI-generated videos produce significantly different correlation signatures, suggesting a robust means of differentiating them. Our work demonstrates that deterministic optical phenomena can serve as physically grounded, verifiable signatures against AI-generated video.

</details>

### 61. Attacks on Machine-Text Detectors Retain Stylistic Fingerprints

📄 [arXiv](https://arxiv.org/abs/2505.14608) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66801)　📅 2025-05　🏷 ICML 2026

**关键词**：`detection`、`model copyright`、`ownership verification`、`model provenance`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Rafael Rivera Soto、Barry Chen、Nicholas Andrews

- 🎯 **研究动机**：机器文本检测被认为易被逃避而不可解，但逃逸策略的极限未知
- 🔬 **研究方法**：评估 prompt 工程到检测器引导优化等攻击对风格指纹的影响，并提出同时优化不可检测性与贴合人类风格的新改写攻击
- 📌 **结论**：既有攻击无法抹除风格指纹；新攻击可逃过含风格在内的全部检测器，但文档数增多后机器分布重新可分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite considerable progress in the development of machine-text detectors, the ease with which machine-text can be manipulated to evade detection has led to suggestions that the problem is inherently intractable. In this work, we investigate the limits of such evasion strategies. We demonstrate that while current attacks, ranging from prompt engineering to detector-guided optimization can effectively degrade performance of standard detectors, they fail to erase the underlying stylistic "fingerprints" of machine text. We show that few-shot detectors that utilize the stylistic feature space are robust to these evasion attempts, reliably detecting samples even from models explicitly tuned to prevent detection. This raises the question: does style represent a universal defense against machine-detection attacks? We demonstrate that the answer is "no'' by introducing a novel paraphrasing approach that simultaneously optimizes for undetectability and adherence to specific human styles. We show that unlike prior methods, this attack effectively evades all considered detectors, including those that utilize writing style. However, we find that this evasion is not absolute: as the number of documents available for analysis grows, the human and machine distributions become distinguishable again. Overall, our findings suggest that reliable machine-text detection requires moving beyond single-document analysis to multi-document analysis.

</details>

### 62. Attribution as Retrieval: Model-Agnostic AI-Generated Image Attribution

📄 [arXiv](https://arxiv.org/abs/2603.10583) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Attribution_as_Retrieval_Model-Agnostic_AI-Generated_Image_Attribution_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`generator attribution`、`retrieval`、`model agnosticism`

👤 **作者**：Hongsong Wang、Renxi Cheng、Chaolei Han、Jie Gui

- 🎯 **研究动机**：现有 AI 生成图像归属方法依赖生成模型访问，对新出现生成器缺乏通用性与可扩展性
- 🔬 **研究方法**：LIDA 把归属重构为实例检索而非分类：低位平面指纹生成加无监督预训练与少样本归属适配
- 📌 **结论**：零样本与少样本设定下的检测与归属均达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of AIGC technologies, image forensics will encounter unprecedented challenges. Traditional methods are incapable of dealing with increasingly realistic images generated by rapidly evolving image generation techniques. To facilitate the identification of AI-generated images and the attribution of their source models, generative image watermarking and AI-generated image attribution have emerged as key research focuses in recent years. However, existing methods are model-dependent, requiring access to the generative models and lacking generality and scalability to new and unseen generators. To address these limitations, this work presents a new paradigm for AI-generated image attribution by formulating it as an instance retrieval problem instead of a conventional image classification problem. We propose an efficient model-agnostic framework, called Low-bIt-plane-based Deepfake Attribution (LIDA). The input to LIDA is produced by Low-Bit Fingerprint Generation module, while the training involves Unsupervised Pre-Training followed by subsequent Few-Shot Attribution Adaptation. Comprehensive experiments demonstrate that LIDA achieves state-of-the-art performance for both Deepfake detection and image attribution under zero- and few-shot settings. The code is at https://github.com/hongsong-wang/LIDA

</details>

### 63. SWIFT: Sliding Window Reconstruction for Few-Shot Training-Free Generated Video Attribution

📄 [arXiv](https://arxiv.org/abs/2603.08536) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_SWIFT_Sliding_Window_Reconstruction_for_Few-Shot_Training-Free_Generated_Video_Attribution_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`detection`、`video attribution`、`sliding-window reconstruction`、`few-shot method`

👤 **作者**：Chao Wang、…、Kejiang Chen

- 🎯 **研究动机**：现有生成视频溯源需额外操作或训练归属模型，降低质量或需大量样本
- 🔬 **研究方法**：SWIFT 利用视频块内多像素帧到单潜帧的时序映射，固定长度滑窗做正常与损坏两种重建，以损失差为归属信号
- 📌 **结论**：五个 SOTA 视频生成模型上仅 20 个样本即达 90% 以上平均归属准确率，对 HunyuanVideo 等可零样本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in video generation technologies have been significant, resulting in their widespread application across multiple domains. However, concerns have been mounting over the potential misuse of generated content. Tracing the origin of generated videos has become crucial to mitigate potential misuse and identify responsible parties. Existing video attribution methods require additional operations or the training of source attribution models, which may degrade video quality or necessitate large amounts of training samples. To address these challenges, we define for the first time the "few-shot training-free generated video attribution" task and propose SWIFT, which is tightly integrated with the temporal characteristics of the video. By leveraging the "Pixel Frames(many) to Latent Frame(one)" temporal mapping within each video chunk, SWIFT applies a fixed-length sliding window to perform two distinct reconstructions: normal and corrupted. The variation in the losses between two reconstructions is then used as an attribution signal. We conducted an extensive evaluation of five state-of-the-art (SOTA) video generation models. Experimental results show that SWIFT achieves over 90% average attribution accuracy with merely 20 video samples across all models and even enables zero-shot attribution for HunyuanVideo, EasyAnimate, and Wan2.2. Our source code is available at https://github.com/wangchao0708/SWIFT.

</details>
