# 生成模型概念擦除与 Unlearning

[返回上级目录](README.md)

## 研究方向

研究从 diffusion、flow 和多模态生成模型中移除敏感、受版权保护或危险概念，同时测量 residual generation、relearning、prompt circumvention 和无关内容质量。

## 研究脉络

- **参数与表示擦除：** 早期方法编辑 cross-attention、权重或 latent direction 以压制指定概念。
- **多概念与持续遗忘：** 研究扩展到多概念、动态 LoRA、token-level 和 inference-time removal。
- **反测试：** Adversarial prompt、relearning 和 hidden leakage 用于检验表面不可生成是否等于真实删除。
- **当前边界：** 精确概念边界、组合语义和跨语言恢复仍使 deletion guarantee 难以成立。

## Training-Time Concept Erasure 与 Utility Retention

### 1. TINA+: Probing Residual Visual Knowledge in Unlearned Diffusion Models via Diffusion-Consistent Text-Free Inversion

📄 [arXiv](https://arxiv.org/abs/2608.17747)　📅 2026-08

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`

👤 **作者**：Qianlong Xiang、Miao Zhang、Kun Wang、Haoyu Zhang、Junhui Hou、Liqiang Nie

- 🎯 **研究动机**：概念擦除的对抗探针以文本为中心，只查文图映射是否切断，忽略对应视觉知识是否残留
- 🔬 **研究方法**：TINA+ 扩散一致的无文本反演攻击：优化式反演在 null-text 条件下恢复生成轨迹以重构擦除概念的视觉实例，并以轨迹正则压制伪反演路径
- 📌 **结论**：十二种擦除方法、四类任务上可靠探出残留视觉知识——现有方法多靠遮蔽文图链接而非消除底层视觉知识

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although text-to-image diffusion models exhibit remarkable generative power, concept erasure techniques are essential for preventing harmful content. Existing adversarial probes evaluate these methods by testing whether erased concepts can still be recovered. However, existing erasure and probe methods remain largely text-centric, focusing on whether the text-to-image mapping is severed while overlooking whether the corresponding visual knowledge remains. To investigate this question from a visual perspective, we leverage diffusion inversion to probe whether a generative trajectory can reconstruct visual instances of an erased concept. Under a null-text condition, standard inversion avoids the textual pathway but amplifies approximation errors, hindering faithful trajectory recovery. To address this challenge, we introduce TINA+, a diffusion-consistent Text-free INversion Attack equipped with optimization-based inversion. We also find that unconstrained diffusion inversion may discover spurious trajectories, even allowing a randomly initialized diffusion model to reconstruct the target concept. Such trajectories may falsely indicate residual visual knowledge. TINA+ therefore introduces Diffusion-Consistent Trajectory Regularization to suppress this failure mode. By penalizing trajectories that fall far below the expected marginal energy evolution of diffusion, TINA+ suppresses spurious inversion paths while preserving its ability to recover erased concepts. Experiments across twelve erasure methods, four concept-erasure tasks, and different model architectures demonstrate that TINA+ reliably probes residual visual knowledge through diffusion-consistent visual trajectories. These results provide stronger evidence that current methods often obscure concepts by severing text-image links rather than eliminating the underlying visual knowledge.

</details>

### 2. TEA: Text Encoder Alignment for Robust Concept Erasure in Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2608.15341)　📅 2026-08

**关键词**：`analysis`、`concept erasure`、`diffusion unlearning`、`generation fidelity`

👤 **作者**：Alireza Dehghanpour Farashah、Zhuan Shi、Negar Rostamzadeh、Golnoosh Farnadi

- 🎯 **研究动机**：概念擦除方法对抗 prompt 鲁棒性有限、损良性生成质量或需推理时干预带来持续开销
- 🔬 **研究方法**：TEA 把概念擦除形式化为文本表征空间的域对齐：仅微调文本编码器，判别器区分概念 prompt 与安全锚 prompt 的 token 表征并使编码器令其不可分
- 📌 **结论**：SD v1.4 上对黑盒与白盒对抗攻击达 SOTA 擦除鲁棒性且保持良性质量、零推理开销；SD v3.5 上 ASR 最低并扩展到 Rectified Flow Transformer 架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models can be misused to generate harmful content through adversarial or paraphrased prompts that bypass built-in safety mechanisms. Existing concept erasure methods often suffer from limited robustness against adversarial prompts, degradation of benign generation quality, or reliance on inference-time interventions that introduce persistent computational overhead. To address these limitations, we formulate concept erasure as a domain alignment problem in the text representation space. We propose a lightweight Text Encoder Alignment framework (TEA) that fine-tunes only the text encoder while keeping the generative backbone fully frozen. Given concept--anchor prompt pairs, our method trains a discriminator to distinguish token-level representations of concept-containing prompts from those of safe anchor prompts, while updating the text encoder to make these representations indistinguishable. TEA introduces zero inference-time overhead and requires only a small number of fine-tuning steps, making it highly efficient to deploy at scale. Despite this efficiency, TEA achieves state-of-the-art erasure robustness against black-box and white-box adversarial attacks on Stable Diffusion v1.4, while preserving generation quality on benign prompts. Furthermore, TEA is model-agnostic and achieves the lowest attack success rate on Stable Diffusion v3.5, extending concept erasure to a Rectified Flow Transformer architecture with T5 conditioning where prior methods remain largely unexplored. Code is available at \href{https://github.com/alirezafarashah/TEA.git}{https://github.com/alirezafarashah/TEA.git}

</details>

### 3. To Erase, or Not to Erase: Robust Training-Free Concept Erasure with Preservation aware Adaptive Ranked Subspace Expansion

📄 [arXiv](https://arxiv.org/abs/2607.23492) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5971)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`trigger search`、`subspace editing`

👤 **作者**：Shaswati Saha、Rajasekhar Anguluri、Manas Gaur

- 🎯 **研究动机**：概念擦除在擦除鲁棒性与效用间权衡：静态概念库不建模提示如何引导去噪，易被触发器复现目标并误伤邻近良性概念
- 🔬 **研究方法**：提出 PARSE 免训练框架：用 classifier-free guidance 动态发现诱发目标的擦除概念与需保留的邻近概念，保真投影编辑交叉注意力值空间，经文本反演搜索再涌现触发器并无冲突时扩展擦除子空间；以 BEUS 分数平衡鲁棒性与效用
- 📌 **结论**：NSFW、艺术风格与物体擦除上多概念鲁棒擦除而不牺牲编辑后效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure techniques (CETs) edit text-to-image diffusion models to erase undesired targets such as NSFW content or copyrighted styles, while preserving model utility on benign concepts. Current CETs face a trade-off between erasure robustness and utility: stronger edits erase the target more reliably but degrade utility on non-target concepts, and vice versa. This stems from how existing methods define what to erase and what to preserve. Many CETs rely on static concept banks specified manually, generated by LLMs, or selected by CLIP image-text similarity. Such banks do not model how prompts steer the model during denoising, leaving it vulnerable to triggers that reintroduce the target while suppressing nearby benign concepts. We present Preservation-aware Adaptive Ranked Subspace Expansion (PARSE), a training-free framework for robust concept erasure in latent diffusion models. Given a target, PARSE queries the diffusion model with classifier-free guidance to dynamically discover target-inducing erase concepts and nearby retain concepts in the model vocabulary. It then edits the cross-attention value space with a preservation-aware projection that removes target directions while leaving retain directions intact. For triggers beyond this vocabulary-indexed space, PARSE iteratively searches for re-emergence triggers by textual inversion and adaptively expands the erased subspace only when a new trigger direction does not conflict with retain semantics. We also introduce the Balanced Erasure Utility Score (BEUS), which combines robustness (ASR under multiple attacks) and utility preservation (FID) via bounded monotone transforms and harmonic mean aggregation. Experiments on NSFW, artistic style, and object erasure, with a large-scale robustness-utility analysis over many CET baselines, show that PARSE erases multiple concepts robustly without sacrificing post-edit utility.

</details>

### 4. Beyond Text Prompts: Precise Concept Erasure through Text-Image Collaboration

📄 [arXiv](https://arxiv.org/abs/2604.15829) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Beyond_Text_Prompts_Precise_Concept_Erasure_through_Text-Image_Collaboration_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`concept erasure`、`text-image collaboration`、`diffusion model`

👤 **作者**：Jun Li、…、Guo-Sen Xie

- 🎯 **研究动机**：文本侧概念擦除压制不彻底，朴素图像引导又易过度擦除无关内容
- 🔬 **研究方法**：TICoE 通过连续凸概念流形与层次化视觉表征学习实现图文协同擦除，并提出面向保真度的擦除质量评估
- 📌 **结论**：多基准上概念移除精度与内容保真均超过先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image generative models have achieved impressive fidelity and diversity, but can inadvertently produce unsafe or undesirable content due to implicit biases embedded in large-scale training datasets. Existing concept erasure methods, whether text-only or image-assisted, face trade-offs: textual approaches often fail to fully suppress concepts, while naive image-guided methods risk over-erasing unrelated content. We propose TICoE, a text-image Collaborative Erasing framework that achieves precise and faithful concept removal through a continuous convex concept manifold and hierarchical visual representation learning. TICoE precisely removes target concepts while preserving unrelated semantic and visual content. To objectively assess the quality of erasure, we further introduce a fidelity-oriented evaluation strategy that measures post-erasure usability. Experiments on multiple benchmarks show that TICoE surpasses prior methods in concept removal precision and content fidelity, enabling safer, more controllable text-to-image generation. Our code is available at https://github.com/OpenAscent-L/TICoE.git

</details>

### 5. Closed-Form Concept Erasure via Double Projections

📄 [arXiv](https://arxiv.org/abs/2604.10032) · 🌐 [Project](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Closed-Form_Concept_Erasure_via_Double_Projections_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`concept erasure`、`closed-form update`、`double projection`

👤 **作者**：Chi Zhang、Jingpu Cheng、Zhixian Wang、Ping Liu

- 🎯 **研究动机**：现有 concept erasure 依赖迭代优化且可能无意扭曲无关概念
- 🔬 **研究方法**：两步闭式线性变换：先对目标概念做 proxy 投影，再在已知概念方向的左零空间内做受约束变换
- 📌 **结论**：在多个 Stable Diffusion 变体与 FLUX 上匹配或超过 SOTA，更忠实保留非目标概念，仅需数秒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While modern generative models such as diffusion-based architectures have enabled impressive creative capabilities, they also raise important safety and ethical risks. These concerns have led to growing interest in concept erasure, the process of removing unwanted concepts from model representations. Existing approaches often achieve strong erasure performance but rely on iterative optimization and may inadvertently distort unrelated concepts. In this work, we present a simple yet principled alternative: a linear transformation framework that achieves concept erasure analytically, without any training. Our method adapts a pretrained model through two sequential, closed-form steps: first, computing a proxy projection of the target concept, and second, applying a constrained transformation within the left null space of known concept directions. This design yields a deterministic and geometrically interpretable procedure for safe, efficient, and theory-grounded concept removal. Across a wide range of experiments, including object and style erasure on multiple Stable Diffusion variants and the flow-matching model (FLUX), our approach matches or surpasses the performance of state-of-the-art methods while preserving non-target concepts more faithfully. Requiring only a few seconds to apply, it offers a lightweight and drop-in tool for controlled model editing, advancing the goal of safer and more responsible generative models.

</details>

### 6. Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2604.16481) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Seo_Erasing_Thousands_of_Concepts_Towards_Scalable_and_Practical_Concept_Erasure_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`scalable erasure`、`text-to-image model`、`harmful concept`

👤 **作者**：Hoigi Seo、Byung Hyun Lee、Jaehyun Cho、Sungjin Lim、Se Young Chun

- 🎯 **研究动机**：现有概念擦除难以兼顾规模、精度与鲁棒性，仅能擦除数百概念
- 🔬 **研究方法**：ETC 用 t 分布混合（tMM）建模低秩概念分布，经 affine 最优传输定点擦除，训练 MoEraser 移除目标嵌入，并向文本投影器注入噪声抵御模块移除攻击
- 📌 **结论**：跨异构域与扩散模型擦除 2,000+ 概念，规模与精度达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-scale text-to-image (T2I) diffusion models deliver remarkable visual fidelity but pose safety risks due to their capacity to reproduce undesirable content, such as copyrighted ones. Concept erasure has emerged as a mitigation strategy, yet existing approaches struggle to balance scalability, precision, and robustness, which restricts their applicability to erasing only a few hundred concepts. To address these limitations, we present Erasing Thousands of Concepts (ETC), a scalable framework capable of erasing thousands of concepts while preserving generation quality. Our method first models low-rank concept distributions via a Student's t-distribution Mixture Model (tMM). It enables pin-point erasure of target concepts via affine optimal transport while preserving others by anchoring the boundaries of target concept distributions without pre-defined anchor concepts. We then train a Mixture-of-Experts (MoE)-based module, termed MoEraser, which removes target embeddings while preserving the anchor embeddings. By injecting noise into the text embedding projector and fine-tuning MoEraser for recovery, our framework achieves robustness to white-box attack such as module removal. Extensive experiments on over 2,000 concepts across heterogeneous domains and diffusion models demerate state-of-the-art scalability and precision in large-scale concept erasure.

</details>

### 7. OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure

📄 [arXiv](https://arxiv.org/abs/2603.11493) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3150)　📅 2026-03　🏷 ECCV 2026

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`sparse autoencoder`、`adversarial elicitation`

👤 **作者**：Chuancheng Shi、Wenhua Wu、Fei Shen、Xiaogang Zhu、Kun Hu、Zhiyong Wang

- 🎯 **研究动机**：概念擦除整段抑制神经元会误伤良性属性，因敏感与良性语义非正交叠加、共享激活子空间
- 🔬 **研究方法**：OrthoEraser 用 SAE 分解密集激活分离敏感神经元，检测耦合神经元后把擦除向量解析投影到其零空间实现正交解耦
- 📌 **结论**：高精度擦除有害概念同时保持生成流形完整，显著超越 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models face significant safety risks from adversarial induction, yet current concept erasure methods often cause collateral damage to benign attributes when suppressing selected neurons entirely. This occurs because sensitive and benign semantics exhibit non-orthogonal superposition, sharing activation subspaces where their respective vectors are inherently entangled. To address this issue, we propose OrthoEraser, which leverages sparse autoencoders (SAE) to achieve high-resolution feature disentanglement and subsequently redefines erasure as an analytical orthogonalization projection that preserves the benign manifold's invariance. OrthoEraser first employs SAE to decompose dense activations and segregate sensitive neurons. It then uses coupled neuron detection to identify non-sensitive features vulnerable to intervention. The key novelty lies in an analytical gradient orthogonalization strategy that projects erasure vectors onto the null space of the coupled neurons. This orthogonally decouples the sensitive concepts from the identified critical benign subspace, effectively preserving non-sensitive semantics. Experimental results on safety demonstrate that OrthoEraser achieves high erasure precision, effectively removing harmful content while preserving the integrity of the generative manifold, and significantly outperforming SOTA baselines. This paper contains results of unsafe models.

</details>

### 8. Neighbor-Aware Localized Concept Erasure in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.25994) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Neighbor-Aware_Localized_Concept_Erasure_in_Text-to-Image_Diffusion_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`localized erasure`、`semantic neighborhood`、`utility preservation`

👤 **作者**：Zhuan Shi、Alireza Dehghanpour Farashah、Rik de Vries、Golnoosh Farnadi

- 🎯 **研究动机**：局部概念擦除会无意削弱语义相邻概念，细粒度领域保真度下降
- 🔬 **研究方法**：NLCE 免训练三阶段：谱加权嵌入调制衰减目标概念并稳定邻居、注意力引导空间门定位残余激活、空间门控硬擦除仅清除必要痕迹
- 📌 **结论**：Oxford Flowers 与 Stanford Dogs 上有效擦除目标并更好保留近邻类别，且泛化到名人身份、色情内容与艺术风格

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure in text-to-image diffusion models seeks to remove undesired concepts while preserving overall generative capability. Localized erasure methods aim to restrict edits to the spatial region occupied by the target concept. However, we observe that suppressing a concept can unintentionally weaken semantically related neighbor concepts, reducing fidelity in fine-grained domains. We propose Neighbor-Aware Localized Concept Erasure (NLCE), a training-free framework designed to better preserve neighboring concepts while removing target concepts. It operates in three stages: (1) a spectrally-weighted embedding modulation that attenuates target concept directions while stabilizing neighbor concept representations, (2) an attention-guided spatial gate that identifies regions exhibiting residual concept activation, and (3) a spatially-gated hard erasure that eliminates remaining traces only where necessary. This neighbor-aware pipeline enables localized concept removal while maintaining the surrounding concept neighborhood structure. Experiments on fine-grained datasets (Oxford Flowers, Stanford Dogs) show that our method effectively removes target concepts while better preserving closely related categories. Additional results on celebrity identity, explicit content and artistic style demonstrate robustness and generalization to broader erasure scenarios.

</details>

### 9. Prototype-Guided Concept Erasure in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.08271) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cai_Prototype-Guided_Concept_Erasure_in_Diffusion_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`concept erasure`、`semantic prototype`、`diffusion safety`

👤 **作者**：Yuze Cai、Jiahao Lu、Hongxiang Shi、Yichao Zhou、Hong Lu

- 🎯 **研究动机**：概念擦除对性、暴力等范围宽泛且多面的概念效果不佳
- 🔬 **研究方法**：利用模型内在嵌入几何定位并聚类编码该概念的潜嵌入得到概念原型，推理时作为负条件信号实现擦除
- 📌 **结论**：多基准上对宽泛概念的移除更可靠，同时保持整体图像质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure is extensively utilized in image generation to prevent text-to-image models from generating undesired content. Existing methods can effectively erase narrow concepts that are specific and concrete, such as distinct intellectual properties (e.g. Pikachu) or recognizable characters (e.g. Elon Musk). However, their performance degrades on broad concepts such as ``sexual'' or ``violent'', whose wide scope and multi-faceted nature make them difficult to erase reliably. To overcome this limitation, we exploit the model's intrinsic embedding geometry to identify latent embeddings that encode a given concept. By clustering these embeddings, we derive a set of concept prototypes that summarize the model's internal representations of the concept, and employ them as negative conditioning signals during inference to achieve precise and reliable erasure. Extensive experiments across multiple benchmarks show that our approach achieves substantially more reliable removal of broad concepts while preserving overall image quality, marking a step towards safer and more controllable image generation.

</details>

### 10. Z-Erase: Enabling Concept Erasure in Single Stream Diffusion Transformers

📄 [arXiv](https://arxiv.org/abs/2603.25074) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62596)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`diffusion model`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Nanxiang Jiang、…、Wenjun Wu

- 🎯 **研究动机**：概念擦除在单流扩散transformer（如Z-Image）上未被研究，直接套用旧方法导致生成崩溃
- 🔬 **研究方法**：Z-Erase以流解耦框架分离更新路径，Lagrangian引导的自适应调制平衡擦除-保留权衡，并证明收敛到Pareto驻点
- 📌 **结论**：消除生成崩溃，多任务概念擦除达SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure serves as a vital safety mechanism for removing unwanted concepts from text-to-image (T2I) models. While extensively studied in U-Net and dual-stream architectures (e.g., Flux), this task remains under-explored in the recent emerging paradigm of single-stream diffusion transformers (e.g., Z-Image). In this new paradigm, text and image tokens are processed as a single unified sequence via shared parameters. Consequently, directly applying prior erasure methods typically leads to generation collapse. To bridge this gap, we introduce Z-Erase, the first concept erasure method tailored for single-stream T2I models. To guarantee stable image generation, Z-Erase first proposes a Stream Disentangled Concept Erasure Framework that decouples updates and enables existing methods on single-stream models. Subsequently, within this framework, we introduce Lagrangian-Guided Adaptive Erasure Modulation, a constrained algorithm that further balances the sensitive erasure-preservation trade-off. Moreover, we provide a rigorous convergence analysis proving that Z-Erase can converge to a Pareto stationary point. Experiments demonstrate that Z-Erase successfully overcomes the generation collapse issue, achieving state-of-the-art performance across a wide range of tasks.

</details>

### 11. Where Concept Erasure Should Occur: Concept–Layer Alignment in Text-to-Video Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2605.25941) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65598)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`diffusion model`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Yiwei Xie、Ping Liu、Zheng Zhang

- 🎯 **研究动机**：文生视频扩散 transformer 的语义信息在深度上分布不均，层选择不当导致概念与非目标信号纠缠，擦除效果受限
- 🔬 **研究方法**：提出 CLEAR：把层选择形式化为概念-非目标可分性优化问题，用可分性感知目标优先在概念自然分离的表示深度上执行擦除
- 📌 **结论**：大规模文生视频扩散模型上概念抑制更精准并保持整体生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-video diffusion transformers encode semantic information unevenly across model depth, which constrains effective concept erasure. We identify a representational bottleneck, termed concept–layer topological alignment, under which target concepts exhibit higher separability at certain representational depths. Outside these depths, concept and non-target signals remain strongly entangled, limiting the effectiveness of depth-specific erasure. This observation reframes concept erasure as the problem of identifying representational depths where concept–non-target separation naturally emerges. Motivated by this structural constraint, we introduce CLEAR, a separability-driven optimization framework for concept erasure that explicitly enforces concept–layer alignment. CLEAR operationalizes this principle by formulating layer selection as an optimization problem over concept–non-target separability, rather than relying on layer-agnostic or heuristic choices. To enable this, we introduce a separability-aware objective that favors layers exhibiting stronger concept–non-target separation. Experiments on large-scale text-to-video diffusion models demonstrate that enforcing concept--layer alignment leads to more precise concept suppression while preserving overall generative quality.

</details>

### 12. Unlearning in Diffusion Models: A Unified Framework with KL Divergence and Likelihood Constraints

📄 [arXiv](https://arxiv.org/abs/2605.30825) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65884)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`machine unlearning`、`concept erasure`、`generative model safety`

👤 **作者**：Shervin Khalafi、Alejandro Ribeiro、Dongsheng Ding

- 🎯 **研究动机**：扩散模型遗忘需同时删除目标数据/概念并保留预训练效用，两个目标本质冲突，缺乏原则性框架
- 🔬 **研究方法**：把遗忘形式化为最小化与预训练模型偏差、受与遗忘分布显式分离约束的优化问题，提出反向/正向 KL 与似然三种约束形式，证明强对偶性并导出原始-对偶算法
- 📌 **结论**：KL 约束法的保留-遗忘权衡优于权重类基线，似然法在匹配遗忘效果的同时更好保留概念

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearning in diffusion models aims to remove undesirable data or concepts while preserving the utility of pretrained models---two fundamentally conflicting objectives. We propose a principled constrained optimization framework that formulates unlearning as minimizing the deviation from a pretrained model, subject to explicit separation constraints from the unlearning distributions. Specifically, we formulate three constrained optimization problems based on reverse and forward KL divergences, and likelihood constraints. The first two generalize existing approaches for concept and data unlearning, while the third offers a novel and natural formulation for unlearning. Despite the nonconvexity of the KL constraints, we establish strong duality for all three problems, enabling us to explicitly characterize their optimal solutions as unlearning targets and develop primal–dual algorithms for each formulation. Experimental results demonstrate that our KL-constrained approach achieves superior retention-unlearning tradeoffs compared to weight-based baselines for concept and data unlearning, and that our likelihood-based approach matches unlearning effectiveness while better preserving retained concepts compared to baselines.

</details>

### 13. SAEmnesia: Erasing Concepts in Diffusion Models with Supervised Sparse Autoencoders

📄 [arXiv](https://arxiv.org/abs/2509.21379) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64245)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`sparse autoencoder`、`concept erasure`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Enrico Cassano、Riccardo Renzulli、Marco Nurisso、Mirko Zaffaroni、Alan Perotti、Marco Grangetto

- 🎯 **研究动机**：扩散模型概念遗忘受特征分裂困扰：概念散布在众多潜特征中，移除困难且计算昂贵
- 🔬 **研究方法**：提出 SAEmnesia：监督稀疏自编码器通过系统性概念标注强制概念与神经元一对一映射，实现特征集中化与精准擦除
- 📌 **结论**：超参搜索减少 96.67%，UnlearnCanvas 物体提升 9.22%；顺序遗忘 9 个物体时准确率提升 28.4%，并在 I2P 上抑制裸露、抗对抗攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept unlearning in diffusion models is hampered by feature splitting, where concepts are distributed across many latent features, making their removal challenging and computationally expensive. We introduce SAEmnesia, a supervised sparse autoencoder framework that overcomes this by enforcing one-to-one concept-neuron mappings. By systematically labeling concepts during training, our method achieves feature centralization, binding each concept to a single, interpretable neuron. This enables highly targeted and efficient concept erasure. Compared to the state-of-the-art sparse autoencoder-based unlearning approach, SAEmnesia reduces hyperparameter search by 96.67\% and achieves a 9.22\% improvement on the UnlearnCanvas benchmark for objects. Our method also shows superior scalability in sequential unlearning, improving accuracy by 28.4\% when removing nine objects, establishing a step forward for precise and controllable concept erasure. Moreover, SAEmnesia effectively suppresses nudity on the I2P benchmark and remains robust to adversarial attacks. Source code available at https://github.com/EIDOSLAB/SAEmnesia.

</details>

### 14. Preference-Calibrated Optimization with Score-Level Distribution Alignment for Text-to-Image Diffusion Model Unlearning

🎓 [Official](https://icml.cc/virtual/2026/poster/66454)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`machine unlearning`、`concept erasure`、`generative model safety`

👤 **作者**：Xiuyuan Wang、…、Xiaolin Zheng

- 🎯 **研究动机**：T2I 遗忘方法用次优代理目标与真实目标错配，靠参数或输出表层约束保留效用未捕捉扩散生成动态，致灾难遗忘
- 🔬 **研究方法**：POSDA 把遗忘重构为偏好优化（奖励显式量化遗忘目标），score 级分布对齐保持未学习模型潜流形拓扑不变防分布漂移
- 📌 **结论**：物体、风格与 NSFW 遗忘任务上擦除效果 SOTA 且模型效用更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While text-to-image diffusion models achieve remarkable generation quality, they inadvertently memorize sensitive content, necessitating machine unlearning to prevent undesired outputs. However, existing unlearning methods rely on suboptimal surrogate objectives rather than directly optimizing the unlearning goal, leading to fundamental objective mismatch. Moreover, these methods preserve model utility via surface-level constraints on model parameters or outputs, yet fail to capture the intrinsic generative dynamics of diffusion models, consequently triggering catastrophic forgetting. To address these challenges, we propose Preference-calibrated Optimization with Score-level Distribution Alignment (POSDA), a unified unlearning framework that harmonizes effective erasure with fine-grained structural preservation. Specifically, we reframe unlearning as a preference optimization problem by constructing a reward that explicitly quantifies the unlearning objective. Additionally, we introduce score-level distribution alignment to ensure the invariance of the underlying manifold topology of the unlearned model, thereby preventing distributional drift. Extensive experiments across object, style, and NSFW unlearning tasks demonstrate that POSDA achieves state-of-the-art erasure efficacy while maintaining superior model utility compared to existing methods.

</details>

### 15. Orthogonal Concept Erasure for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2605.28902) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63634)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`diffusion model`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Yuhao Sun、Lingyun Yu、Haoxiang Xu、Fengyuan Miao、Zhuoer Xu、Hongtao Xie

- 🎯 **研究动机**：编辑式概念擦除依赖加性参数更新，纠缠神经元方向、幅度与角度几何，难兼顾精确擦除与生成能力保留
- 🔬 **研究方法**：OCE 把擦除重构为乘性更新：闭式解的逐层正交变换保留幅度与角度几何；多概念引入子空间级结构化操控
- 📌 **结论**：单/多概念擦除与非目标保留均优于现有方法，4.3 秒内可擦除最多 100 个概念

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure has emerged as a promising approach to mitigate undesired or unsafe content in diffusion models, yet existing methods still face significant limitations. While training-based methods are effective, their high computational cost limits scalability. Editing-based methods are more efficient and deployment-friendly, yet they struggle to simultaneously achieve precise concept erasure and preserve overall generative capacity. We identify this core limitation of the editing-based methods as reliance on additive parameter updates. Our empirical analysis reveals that concept semantics primarily depend on neuron direction rather than neuron magnitude, while overall generative capacity relies on the angular geometry of neurons. As additive updates inherently entangle direction, magnitude, and angular geometry, they inevitably introduce unintended interference between concept erasure and overall generation performance. To address this, we propose Orthogonal Concept Erasure (OCE), which reformulates editing-based erasure as multiplicative parameter updates from a geometric perspective. Specifically, OCE applies layer-wise orthogonal transformations derived from a closed-form solution to the parameters, enabling precise concept erasure while preserving the neuron magnitude and angular geometry. Furthermore, to address conflicting constraints in multi-concept erasure, OCE introduces a subspace-level objective with structured subspace manipulation, yielding a more effective and scalable erasure. Extensive experiments on single- and multi-concept erasure demonstrate that OCE outperforms existing methods in concept erasure and non-target preservation, erasing up to 100 concepts in 4.3 s.

</details>

### 16. GEM: Geometric Erasure by Contrastive Velocity Matching in Rectified Flows

📄 [arXiv](https://arxiv.org/abs/2606.00140) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64476)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`contrastive learning`、`generative model safety`

👤 **作者**：Jonas Henry Grebe、Tobias Braun、Anna Rohrbach、Marcus Rohrbach

- 🎯 **研究动机**：概念擦除研究滞后于生成模型从 U-Net 扩散向 Rectified Flow Transformer 的转变
- 🔬 **研究方法**：GEM 把轨迹式 unlearning 信号转译为 teacher-guided flow-matching，teacher 提供吸引/排斥信号合成单一几何引导目标
- 📌 **结论**：定向抑制有害概念的同时保持良性生成保真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While the rapid adoption of multimodal generative models offers immense potential, it has also increased the risks of harmful content synthesis, deepfakes, and copyright infringements. To address these challenges, concept erasure has emerged as a prospective safeguard. However, as the field gradually transitions from U-Net-based diffusion models to Rectified Flow Transformers, erasure research has struggled to keep pace. In this work, we introduce GEM, a simple but highly effective erasure framework for Rectified Flow models. As part of our contribution, we establish a principled bridge between trajectory-based unlearning grounded in Generative Flow Networks and classic teacher-guided erasure: we translate trajectory-based signals into a teacher-guided flow-matching setup that unifies the strengths of both paradigms. Concretely, a teacher provides complementary attraction and repulsion signals that we combine into a single geometric guidance objective, yielding targeted suppression of unwanted concepts while preserving benign generation.

</details>

### 17. ForceForget: Reinforcement Concept Removal for Enhancing Safety in Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2606.14351) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66798)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`empirical evaluation`、`generative model safety`

👤 **作者**：Dong Han、Yong Li

- 🎯 **研究动机**：现有 T2I 概念擦除会过度擦除有害提示中的良性概念，损害模型效用
- 🔬 **研究方法**：ForceForget 用强化学习优化概念擦除奖励 CER，Safe Adapter 投影部分文本嵌入在交叉注意力层做高效概念调节
- 📌 **结论**：缓解不安全生成并保持良性图像高保真，抗红队工具更鲁棒，在 I2I 场景更有效且可扩展到风格与物体概念

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the advance of generative AI, the text-to-image (T2I) model has the ability to generate various contents. However, T2I models still can generate unsafe contents. To alleviate this issue, various concept erasing methods are proposed. However, existing methods tend to excessively erase unsafe concepts and suppress benign concepts contained in harmful prompts, which can negatively affect model utility. In this paper, we focus on eliminating unsafe content while maintaining model capability in safe semantic meaning interpretation by optimizing the concept erasing reward (CER) with reinforcement learning. To avoid overly content erasure, we introduce the Safe Adapter to project partial text embedding for efficient concept regulation in cross-attention layers. Extensive experiments conducted on different datasets demonstrate the effectiveness of the proposed method in alleviating unsafe content generation while preserving the high fidelity of benign images compared with existing state-of-the-art (SOTA) concept erasing methods. In terms of robustness, our method outperforms counterparts against red-teaming tools. Moreover, we showcase the proposed approach is more effective in emerging image-to-image (I2I) scenarios compared with others. Lastly, we extend our method to erase general concepts, such as artistic styles and objects. Disclaimer: This paper includes discussions of sexually explicit content that may be offensive to certain readers. All images used in this work are synthesized or from public datasets.

</details>

### 18. Concept Removal for Frontier Image Generative Models

📄 [arXiv](https://arxiv.org/abs/2606.25548) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61255)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`generative model safety`、`concept erasure`、`diffusion unlearning`、`diffusion model`

👤 **作者**：Aditya Kumar、Pierre Joly、Adam Dziedzic、Franziska Boenisch

- 🎯 **研究动机**：从网络级数据训练的前沿图像生成模型中高效移除不良概念而不降画质仍然困难
- 🔬 **研究方法**：把 SD3.5、Flux、Infinity 的内部瓶颈层替换为复刻原层但结构化为不同激活特征的 transcoder，原位选择性禁用概念特定信号
- 📌 **结论**：SOTA 概念移除性能，保持生成质量、抗对抗提示并支持多概念顺序移除，白盒访问下仍持久

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image generative models are trained on massive, largely uncurated internet-scale datasets that contain undesirable visual concepts. Efficiently removing such concepts from the model generations without degrading the quality of output images remains challenging. We introduce a novel concept removal method for frontier diffusion and image autoregressive models, such as, SD3.5, Flux, and Infinity. Our intervention replaces the internal bottleneck layer present in all these modern models with a transcoder that is trained to replicate the original layer while structuring it into distinct activation features. This in‑place substitution creates an integrated filter through which concept‑specific signals can be selectively disabled while preserving the rest of the model’s behavior. Since the intervention modifies the model backbone rather than attaching an external component, it remains persistent under white‑box access. Empirically, the approach achieves state‑of‑the‑art concept removal performance across modern diffusion and autoregressive models, maintains visual generation quality, provides robustness against adversarial prompts, and supports sequential removal of diverse concepts. This positions our method as a practical approach for concept removal in frontier image generative models.

</details>

### 19. A Unified Framework for Diffusion Model Unlearning with f-Divergence

📄 [arXiv](https://arxiv.org/abs/2509.21167) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66124)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`machine unlearning`、`concept erasure`、`generative model safety`

👤 **作者**：Nicola Novello、Federico Fontana、Luigi Cinque、Deniz Gunduz、Andrea M. Tonello

- 🎯 **研究动机**：T2I 概念遗忘普遍最小化目标与锚概念条件下去噪输出的 MSE，隐式等价于两高斯的 KL 散度，单一目标限制遗忘质量与保真的权衡
- 🔬 **研究方法**：把目标推广到任意 f-divergence：识别一族 alpha-divergence 的高斯闭式给出廉价 MSE 式目标，其余用变分形式的 min-max 目标；理论与数值分析散度选择对梯度与收敛的影响
- 📌 **结论**：Hellinger 闭式实例在多场景一致超过 MSE；统一框架支持按应用选择最优散度、细粒度控制遗忘效力与生成保真的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most existing methods for concept unlearning in text-to-image diffusion models minimize a mean squared error (MSE) loss between the denoiser outputs conditioned on a target and an anchor concept, which is implicitly the KL divergence between two Gaussians. We generalize this objective to any $f$-divergence, recovering MSE as the KL instance, and identify a family of $\alpha$-divergences whose Gaussian closed-form yields cheap, MSE-like training objectives. For the remaining $f$-divergences, we provide a min-max objective based on the variational formulation of the $f$-divergence. We theoretically analyze and numerically validate how different $f$-divergences impact the gradient magnitude and the convergence properties of the algorithm, affecting the quality of unlearning. For instance, we observe that the Hellinger closed-form instance consistently dominates MSE across multiple scenarios. More generally, the proposed unified framework offers a flexible paradigm for selecting the optimal divergence based on the application and user goal, allowing for finer control over the trade-off between unlearning efficacy and generative fidelity.

</details>

### 20. Adversarial Reinforcement Learning for Robust Diffusion Large Language Model Unlearning

🎓 [Official](https://icml.cc/virtual/2026/poster/65904)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`machine unlearning`、`adversarial robustness`、`concept erasure`、`generative model safety`

👤 **作者**：Zhiwei Zhang、…、Suhang Wang

- 🎯 **研究动机**：unlearning 在自回归 LM 上研究充分，但 diffusion language model 的架构差异带来新挑战：目标输入嵌入信息性上下文时易复现被遗忘知识，对诱导攻击脆弱
- 🔬 **研究方法**：首个 DLM unlearning 综合研究：实证证明其对生成超参数高度敏感；提出对抗 RL 框架——上下文生成器构造信息性上下文诱导遗忘知识，DLM 同时被优化抑制不良回忆，并引入组件解决信用分配与稳定性问题
- 📌 **结论**：显著提升遗忘有效性与鲁棒性并保持模型效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion language models (DLMs) have recently emerged as an alternative to autoregressive approaches, enabling parallel sequence generation and flexible token generation orders. Machine unlearning plays a critical role in mitigating legal and ethical risks by removing the influence of specific training examples from trained models. While unlearning has been extensively studied for autoregressive language models, its applicability to DLMs remains unexplored. The architectural differences of DLMs raise new challenges for effective and robust unlearning that are not addressed by existing methods. In this paper, we present the first comprehensive study of unlearning for DLMs. Through systematic empirical analysis, we show that unlearning performance in DLMs is highly sensitive to generation hyperparameters, highlighting the need for evaluation across diverse generation settings. We further observe that DLMs tend to reproduce unlearned information when target inputs are embedded within informative contexts, due to their ability to incorporate both prefix and suffix conditioning, which increases vulnerability to elicitation attacks and weakens the robustness of existing unlearning methods. To design a robust unlearning method, we propose an adversarial reinforcement learning framework, where a context generator adversarially produces informative contexts to elicit unlearned knowledge, while the DLM is optimized to suppress undesired recall. We further introduce novel components to address credit assignment and stability issues in this adversarial learning setup. Extensive experiments demonstrate that our method significantly improves unlearning effectiveness while preserving model utility.

</details>

### 21. Achieving Subcategorical Erasure in Text-to-Image Models

🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4524) · 📝 [OpenReview](https://openreview.net/forum?id=1K7TSEe2x5)　📅 2026　🏷 ECCV 2026

**关键词**：`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`harmful content`、`model unlearning`

- 🎯 **研究动机**：概念擦除按粗类别整体删除，误伤同类的无害子概念
- 🔬 **研究方法**：提出子类级擦除方法，只删有害子类并保留其余子类生成能力
- 📌 **结论**：实现细粒度擦除同时维持生成保真度

### 22. GenErase: Generalizable and Semantically-Aware Concept Erasure in Diffusion Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Vardhana_GenErase_Generalizable_and_Semantically-Aware_Concept_Erasure_in_Diffusion_Models_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`defense`、`concept erasure`、`semantic preservation`、`diffusion model`

👤 **作者**：Korada Sri Vardhana、Soma Biswas

- 🎯 **研究动机**：免训练防护方法要么僵硬难泛化到改写提示，要么粗粒度损伤无关内容与保真
- 🔬 **研究方法**：GenErase 在 cross-attention 值空间做 erase-and-replace，配 per-token preserve projector 与硬几何门强制语义正交
- 📌 **结论**：在身份/物体/风格擦除与新 GenBench-40 基准上取得 SOTA 擦除保真与改写级泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) diffusion models power modern creative tools, but their open-ended generative nature raises safety, ethical, and copyright concerns. Retraining or fine-tuning to remove every unsafe or copyrighted concept is impractical, motivating training-free interventions that suppress specific semantics while preserving general visual quality. Existing guard-railing methods face a core trade-off: they are either rigid, failing to generalize to paraphrased or context-shifted prompts, or coarse, distorting unrelated content and fidelity. We present GenErase (GENeralizable ERAsure with SEmantic Awareness), a training-free, geometry-grounded framework for robust concept removal in diffusion models. GenErase enforces semantic orthogonality in the cross-attention value space via an explicit erase-and-replace operation, guided by a per-token preserve projector and a hard geometric gate. This design enables precise erasure, explicit protection of critical semantics, and stability across layers, paraphrases, and multi-concept cases. Extensive experiments on identity, object, and style erasure, together with a new GenBench-40 benchmark, show that GenErase achieves state-of-the-art erasure fidelity and superior paraphrase-level generalization, establishing it as a practical and principled guard-rail for safe, real-time diffusion deployment.

</details>

### 23. EMMA: Concept Erasure Benchmark with Comprehensive Semantic Metrics and Diverse Categories

📄 [arXiv](https://arxiv.org/abs/2512.17320) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wei_EMMA_Concept_Erasure_Benchmark_with_Comprehensive_Semantic_Metrics_and_Diverse_CVPR_2026_paper.html)　📅 2025-12　🏷 CVPR 2026

**关键词**：`benchmark`、`concept erasure`、`semantic metrics`、`diffusion safety`

👤 **作者**：Lu Wei、Yuta Nakashima、Noa Garcia

- 🎯 **研究动机**：概念擦除评测常限于少量概念与过于直白的 prompt，无法检验概念是否真正从表示中移除
- 🔬 **研究方法**：EMMA 基准在五维度 13 项指标上评测，含间接描述、视觉相似非目标概念与性别种族偏见等挑战条件，覆盖物体、名人、艺术风格、NSFW 与版权五域五种方法
- 📌 **结论**：现有方法在隐式 prompt 下仍会生成被擦概念、难以生成与被擦概念相似的非目标概念，部分方法还放大性别与种族偏见

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of text-to-image (T2I) generation has raised concerns about privacy, bias, and copyright violations. Concept erasure techniques offer a promising solution by selectively removing undesired concepts from pre-trained models without requiring full retraining. However, these methods are often evaluated on a limited set of concepts, relying on overly simplistic and direct prompts. To test the boundaries of concept erasure techniques, and assess whether they truly remove targeted concepts from model representations, we introduce EMMA, a benchmark that evaluates five key dimensions of concept erasure over 13 metrics. EMMA goes beyond standard metrics like image quality and time efficiency, testing robustness under challenging conditions, including indirect descriptions, visually similar non-target concepts, and potential gender and ethnicity bias, providing a socially aware analysis of method behavior. Using EMMA, we analyze five concept erasure methods across five domains (objects, celebrities, art styles, NSFW, and copyright). Our results show that existing methods struggle with implicit prompts (i.e., generating the erased concept when it is indirectly referenced) and visually similar non-target concepts (i.e., failing to generate non-target concepts resembling the erased one), while some amplify gender and ethnicity bias compared to the original model. Code and prompts are available at https://github.com/lobsterlulu/EMMA.

</details>

### 24. CGCE: Classifier-Guided Concept Erasure in Generative Models

📄 [arXiv](https://arxiv.org/abs/2511.05865) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4668)　📅 2025-11　🏷 ECCV 2026

**关键词**：`detection`、`defense`、`concept erasure`、`diffusion unlearning`、`generation fidelity`、`red-team attack`

👤 **作者**：Viet Nguyen、Vishal M. Patel

- 🎯 **研究动机**：扩散模型概念擦除可被对抗攻击重新生成被擦内容，鲁棒擦除又常损害良性概念生成质量
- 🔬 **研究方法**：CGCE 是即插即用框架，不改动模型权重，用轻量分类器在文本嵌入上检测并精炼含不良概念的 prompt，推理时仅修改不安全嵌入
- 📌 **结论**：对多种红队攻击取得 SOTA 鲁棒性并保持生成质量，成功适配多种 T2I 与 T2V 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advancements in large-scale generative models have enabled the creation of high-quality images and videos, but have also raised significant safety concerns regarding the generation of unsafe content. To mitigate this, concept erasure methods have been developed to remove undesirable concepts from pre-trained models. However, existing methods remain vulnerable to adversarial attacks that can regenerate the erased content. Moreover, achieving robust erasure often degrades the model's generative quality for safe, unrelated concepts, creating a difficult trade-off between safety and performance. To address this challenge, we introduce Classifier-Guided Concept Erasure (CGCE), an efficient plug-and-play framework that provides robust concept erasure for diverse generative models without altering their original weights. CGCE uses a lightweight classifier operating on text embeddings to first detect and then refine prompts containing undesired concepts. By modifying only unsafe embeddings at inference time, our method prevents harmful content generation while preserving the model's original quality on benign prompts. Extensive experiments show that CGCE achieves state-of-the-art robustness against a wide range of red-teaming attacks. Our approach also maintains high generative utility, demonstrating a superior balance between safety and performance. We showcase the versatility of CGCE through its successful application to various modern T2I and T2V models, establishing it as a practical and effective solution for safe generative AI.

</details>

### 25. Rethinking Robust Adversarial Concept Erasure in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2510.27285) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5067)　📅 2025-10　🏷 ECCV 2026

**关键词**：`defense`、`concept erasure`、`adversarial robustness`、`diffusion unlearning`、`adversarial recovery`、`semantic guidance`

👤 **作者**：Qinghong Yin、…、Yue Zhang

- 🎯 **研究动机**：现有对抗概念擦除因用随机采样近似对抗目标而陷入鲁棒性与计算成本的失衡
- 🔬 **研究方法**：S-GRACE 提出语义引导对抗优化，用单样本生成更准确覆盖目标概念空间的对抗嵌入，并自动把目标概念映射到语义相似的代理概念
- 📌 **结论**：在 NSFW、艺术风格与物体概念上取得 SOTA 擦除鲁棒性与更优生成质量，计算成本显著更低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure methods aim to remove specific unsafe target concepts in diffusion models while preserving image generation utility. To address the vulnerability that erased concepts can be easily recovered under adversarial attacks, adversarial concept erasure methods integrate adversarial optimization into the concept erasure process. However, existing adversarial concept erasure methods face a trade-off between robustness and computational cost. We attribute this to adversarial optimization techniques that use random samples to approximate the adversarial objective function. Adversarial optimization that uses a small number of samples fails to produce adversarial embeddings that accurately capture the target concept space. To mitigate this limitation, we propose Semantic-Guided Adversarial Optimization, which uses a single sample to produce adversarial embeddings that better capture the target concept space. We also propose Semantic-Guided Concept Erasure, which automatically maps the target concept to a semantically similar surrogate. Extensive experiments on not-safe-for-work content, artistic styles, and object-related concepts demonstrate that our method, S-GRACE (Semantic-Guided Robust Adversarial Concept Erasure) achieves state-of-the-art erasure robustness and superior image generation utility, with significantly lower computational cost than existing methods. Our code is available at https://github.com/Qhong-522/S-GRACE.

</details>

### 26. LoRAShield: Data-Free Editing Alignment for Secure Personalized LoRA Sharing

📄 [arXiv](https://arxiv.org/abs/2507.07056) · 🌐 [Project](https://doi.org/10.1145/3770855.3817625)　📅 2025-07　🏷 KDD 2026

**关键词**：`defense`、`LoRA safety editing`、`malicious concept suppression`、`utility retention`、`personalized LoRA`、`image safety`

👤 **作者**：Jiahao Chen、…、Shouling Ji

- 🎯 **研究动机**：良性 LoRA 可被武器化生成政治、诽谤类有害内容，概念擦除防御只针对完整扩散模型
- 🔬 **研究方法**：提出 LoRAShield：首个免数据 LoRA 安全编辑框架，平台侧经对抗优化与语义增强动态编辑 LoRA 权重子空间
- 📌 **结论**：有效拦截恶意生成且不损良性任务功能，支撑个性化 LoRA 的安全共享

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of Low-Rank Adaptation (LoRA) models has democratized personalized text-to-image generation, enabling users to share lightweight models (e.g., personal portraits) on platforms like Civitai and Liblib. However, this "share-and-play" ecosystem introduces critical risks: benign LoRAs can be weaponized by adversaries to generate harmful content (e.g., political, defamatory imagery), undermining creator rights and platform safety. Existing defenses like concept-erasure methods focus on full diffusion models (DMs), neglecting LoRA's unique role as a modular adapter and its vulnerability to adversarial prompt engineering. To bridge this gap, we propose LoRAShield, the first data-free editing framework for securing LoRA models against misuse. Our platform-driven approach dynamically edits and realigns LoRA's weight subspace via adversarial optimization and semantic augmentation. Experimental results demonstrate that LoRAShield achieves remarkable effectiveness, efficiency, and robustness in blocking malicious generations without sacrificing the functionality of the benign task. By shifting the defense to platforms, LoRAShield enables secure, scalable sharing of personalized models, a critical step toward trustworthy generative ecosystems.

</details>

### 27. Roots Beneath the Cut: Uncovering the Risk of Concept Revival in Pruning-Based Unlearning for Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2603.06640) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Roots_Beneath_the_Cut_Uncovering_the_Risk_of_Concept_Revival_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`concept revival`、`pruning unlearning`、`diffusion model`

👤 **作者**：Ci Zhang、…、Geng Yuan

- 🎯 **研究动机**：剪枝式 unlearning 被认为快速安全，但被置零权重位置可能侧信道泄露被擦除概念
- 🔬 **研究方法**：设计完全免数据免训练的攻击框架，从剪枝后扩散模型的权重位置信息恢复被擦除概念
- 📌 **结论**：只要概念相关权重被定位，无论权重如何处理均可恢复原概念；呼吁隐藏剪枝位置的更安全剪枝机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Pruning-based unlearning has recently emerged as a fast, training-free, and data-independent approach to remove undesired concepts from diffusion models. It promises high efficiency and robustness, offering an attractive alternative to traditional fine-tuning or editing-based unlearning. However, in this paper we uncover a hidden danger behind this promising paradigm. We find that the locations of pruned weights, typically set to zero during unlearning, can act as side-channel signals that leak critical information about the erased concepts. To verify this vulnerability, we design a novel attack framework capable of reviving erased concepts from pruned diffusion models in a fully data-free and training-free manner. Our experiments confirm that pruning-based unlearning is not inherently secure, as erased concepts can be effectively revived without any additional data or retraining. Extensive experiments on diffusion-based unlearning based on concept related weights lead to the conclusion: once the critical concept-related weights in diffusion models are identified, our method can effectively recover the original concept regardless of how the weights are manipulated. Finally, we explore potential defense strategies and advocate safer pruning mechanisms that conceal pruning locations while preserving unlearning effectiveness, providing practical insights for designing more secure pruning-based unlearning frameworks.

</details>

### 28. Erased but Not Forgotten: How Backdoors Compromise Concept Erasure

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

### 29. ScaleErasure: Inference-Time Minimal Intervention for Precise Concept Erasure in Next-Scale Autoregressive Image Generation

📄 [arXiv](https://arxiv.org/abs/2606.29282) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60671)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`concept erasure`、`inference-time intervention`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Cong Wang、…、Qing Gu

- 🎯 **研究动机**：逐尺度自回归图像生成中语义在早期尺度高度压缩，不安全与无关语义严重纠缠，概念擦除基本未被研究
- 🔬 **研究方法**：提出 ScaleErasure 推理时最小干预：额外两次以不安全/安全概念为条件的前向传播引导目标 logits，并在尺度、token 与位通道三维上精选拟干预 logits
- 📌 **结论**：在逐尺度 AR 范式上优于改造后的基线，擦除更精准并大体保留通用生成能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concept erasure aims to prevent image generative models from producing unsafe content while preserving their general generative capability. Meanwhile, next-scale autoregressive (AR) image generation has recently emerged as a new generative paradigm characterized by next-scale prediction, for which concept erasure remains largely unexplored. In this paradigm, semantic information is highly compressed at early scales, leading to severe entanglement between unsafe and unrelated semantics. In this paper, we propose ScaleErasure, an inference-time concept erasure method that performs minimal intervention. ScaleErasure precisely selects and guides predicted logits that are most relevant to the unsafe concept, thereby enabling effective erasure under severe semantic entanglement. Specifically, ScaleErasure performs two additional forward passes conditioned on the unsafe concept and the corresponding safe concept, and leverages their outputs to guide the target logits away from unsafe concepts toward safe concepts. To enable precise and minimal intervention, logits selection and guidance are conducted across three dimensions: scales, tokens, and bit channels. Experiments demonstrate that ScaleErasure outperforms adapted baselines in the next-scale AR paradigm, achieving more precise concept erasure while largely preserving general generative capability.

</details>

### 30. MidSteer: Optimal Affine Framework for Steering Generative Models

📄 [arXiv](https://arxiv.org/abs/2605.05220) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64719)　📅 2026　🏷 ICML 2026

**关键词**：`tool`、`defense`、`generative model safety`、`concept erasure`、`diffusion unlearning`、`representation steering`

👤 **作者**：Tatiana Gaintseva、…、Ismail Elezi

- 🎯 **研究动机**：中间表示转向控制生成模型经验成功但缺统一理论框架
- 🔬 **研究方法**：证明标准概念移除是仿射擦除 LEACE 的特例，提出 LEACE-Switch 概念切换框架并刻画最优仿射解条件；MidSteer 放松假设实现最小扰动定向变换
- 📌 **结论**：视觉扩散模型与 LLM 等任务、模态、架构上表现良好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering intermediate representations has emerged as a powerful strategy for controlling generative models. However, despite its empirical success, it currently lacks a comprehensive theoretical framework. In this paper, we bridge this gap by formalizing the theory of concept steering. First, we establish a link between steering and affine concept erasure, proving that the standard approach for removing unwanted behaviors is a special case of LEACE (a closed-form method for affine erasure). Next, we formulate a principled theoretical framework for concept switching, LEACE-Switch, and characterize the assumptions under which it provides an optimal affine solution. Building on this analysis, we then introduce MidSteer (Minimal Disturbance concept Steering), a more general affine framework for concept manipulation that relaxes these assumptions and enables directed, minimal-disturbance transformations. We empirically demonstrate that MidSteer performs favorably across a range of tasks, modalities, and architectures, including vision diffusion models and large language models.

</details>

### 31. Inference Time Concept Removal Guidance for Text-to-Image Diffusion Models

🎓 [Official](https://icml.cc/virtual/2026/poster/65659)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`diffusion model`、`concept erasure`、`diffusion unlearning`、`generative model safety`

👤 **作者**：Yoonseok Choi、Chaeyoung Oh、Hyunjun Choi、Seokin Seo、Kee-Eung Kim

- 🎯 **研究动机**：固定权重负引导造成安全-保真权衡，动态变体对开放词表组合提示脆弱
- 🔬 **研究方法**：CRG 免训练即插即用，仅用模型噪声预测估计每步概念存在度，经闭式约束更新自适应门控并校准负引导
- 📌 **结论**：多个红队基准上显著降攻击成功率并提升良性保真，无需微调即可抑制艺术家风格与暴力概念

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image diffusion models remain vulnerable to adversarial prompts that elicit disallowed content, motivating reliable inference-time controls. A popular approach is negative guidance, which subtracts a negative-prompt direction with a fixed weight. However, it often forces a safety–fidelity trade-off, causing artifacts or prompt drift when over-applied and failing under attacks when under-applied. Recent dynamic variants reweight guidance using posterior-odds signals, which can be brittle for open-vocabulary compositional prompts, while lightweight similarity-based methods do not leverage the evolving image evidence along the denoising trajectory. We introduce Concept Removal Guidance (CRG), a training-free, plug-and-play method that estimates unwanted-concept presence at each diffusion step using only the noise predictions from the model, and then adaptively gates and calibrates negative guidance via a closed-form constrained update that enforces a target presence threshold while minimally perturbing the conditional trajectory. Across multiple red-teaming benchmarks, CRG significantly reduces attack success rates while improving benign fidelity, and additional suppression targets such as artist style and violence without fine-tuning or external classifiers.

</details>

### 32. UnHype: CLIP-Guided Hypernetworks for Dynamic LoRA Unlearning

📄 [arXiv](https://arxiv.org/abs/2602.03410) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62857)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`diffusion model`、`deletion verification`

👤 **作者**：Piotr Wójcik、Maksym Petrenko、Wojciech Gromski、Przemysław Spurek、Maciej Zieba

- 🎯 **研究动机**：基于 LoRA 的扩散模型遗忘对概念语义适应性有限，难以平衡删除相近概念与保持宽泛泛化，多概念同时擦除扩展性差
- 🔬 **研究方法**：提出 UnHype：把超网络引入单/多概念 LoRA 训练，推理时依据 CLIP 嵌入动态生成自适应 LoRA 权重，可直接接入 Stable Diffusion 及 flow-based 文生图模型
- 📌 **结论**：在物体擦除、名人擦除与显式内容移除任务上有效且训练稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large-scale diffusion models have intensified concerns about their potential misuse, particularly in generating realistic yet harmful or socially disruptive content. This challenge has spurred growing interest in effective machine unlearning, the process of selectively removing specific knowledge or concepts from a model without compromising its overall generative capabilities. Among various approaches, Low-Rank Adaptation (LoRA) has emerged as an effective and efficient method for fine-tuning models toward targeted unlearning. However, LoRA-based methods often exhibit limited adaptability to concept semantics and struggle to balance removing closely related concepts with maintaining generalization across broader meanings. Moreover, these methods face scalability challenges when multiple concepts must be erased simultaneously. To address these limitations, we introduce UnHype, a framework that incorporates hypernetworks into single- and multi-concept LoRA training. The proposed architecture can be directly plugged into Stable Diffusion as well as modern flow-based text-to-image models, where it demonstrates stable training behavior and effective concept control. During inference, the hypernetwork dynamically generates adaptive LoRA weights based on the CLIP embedding, enabling more context-aware, scalable unlearning. We evaluate UnHype across several challenging tasks, including object erasure, celebrity erasure, and explicit content removal, demonstrating its effectiveness and versatility.

</details>

### 33. Forget-It-All: Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking

📄 [arXiv](https://arxiv.org/abs/2601.06163) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65222)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`machine unlearning`、`deletion guarantee`、`utility retention`、`concept erasure`、`diffusion model`

👤 **作者**：Kaiyuan Deng、…、Xiaolong Ma

- 🎯 **研究动机**：现有概念擦除方法多针对单概念，多概念场景下遗忘效果、生成质量与超参敏感性均差
- 🔬 **研究方法**：FIA 利用模型稀疏性：Contrastive Concept Saliency 量化权重连接对概念的贡献，结合时空信息识别概念敏感神经元并融合为统一多概念掩码，保留概念无关神经元、剪除概念特定神经元
- 📌 **结论**：免训练、少调参即插即用，三项遗忘任务上多概念遗忘更可靠且保持生成保真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread adoption of text-to-image (T2I) diffusion models has raised concerns about their potential to generate copyrighted, inappropriate, or sensitive imagery. As a practical solution, machine unlearning aims to erase unwanted concepts without retraining from scratch. While most existing methods are effective for single-concept unlearning, they often struggle when removing multiple concepts, causing significant challenges in unlearning effectiveness, generation quality, and sensitivity to hyperparameters and datasets. We take a unique perspective on multi-concept unlearning by leveraging model sparsity and propose the F orget I t A ll (FIA) framework. FIA first introduces Contrastive Concept Saliency to quantify each weight connection's contribution to a target concept. It then identifies Concept Sensitive Neurons by combining temporal and spatial information, ensuring that only neurons consistently responsive to the target concept are selected. Finally, FIA constructs masks from the identified neurons and fuses them into a unified multi-concept mask, where Concept Agnostic Neurons that broadly support general content generation are preserved while concept-specific neurons are pruned to remove the targets. FIA is training-free and requires minimal hyperparameter tuning for new tasks, enabling plug-and-play use. Extensive experiments across three distinct unlearning tasks demonstrate that FIA achieves more reliable multi-concept unlearning, improving forgetting effectiveness while maintaining generation fidelity and quality. Code is available at https://github.com/kaiyuan02415/Forget-It-All

</details>

### 34. Backdooring Textual Inversion for Concept Censorship

📄 [arXiv](https://arxiv.org/abs/2308.10718) · 🌐 [Project](https://concept-censorship.github.io/)　📅 2023-08

**关键词**：`defense`、`concept censorship`、`Textual Inversion`、`protective backdoor`

👤 **作者**：Yutong Wu、Jie Zhang、Florian Kerschbaum、Tianwei Zhang

- 🎯 **研究动机**：可下载的 Textual Inversion embedding 可被滥用造假或诽谤，缺乏概念审查手段
- 🔬 **研究方法**：以后门为善：TI 训练时把敏感词设为触发器，触发词与个性化 embedding 组合时输出预设安全图像
- 📌 **结论**：Stable Diffusion 上在不影响正常使用的前提下实现敏感概念审查

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent years have witnessed success in AIGC (AI Generated Content). People can make use of a pre-trained diffusion model to generate images of high quality or freely modify existing pictures with only prompts in nature language. More excitingly, the emerging personalization techniques make it feasible to create specific-desired images with only a few images as references. However, this induces severe threats if such advanced techniques are misused by malicious users, such as spreading fake news or defaming individual reputations. Thus, it is necessary to regulate personalization models (i.e., concept censorship) for their development and advancement. In this paper, we focus on the personalization technique dubbed Textual Inversion (TI), which is becoming prevailing for its lightweight nature and excellent performance. TI crafts the word embedding that contains detailed information about a specific object. Users can easily download the word embedding from public websites like Civitai and add it to their own stable diffusion model without fine-tuning for personalization. To achieve the concept censorship of a TI model, we propose leveraging the backdoor technique for good by injecting backdoors into the Textual Inversion embeddings. Briefly, we select some sensitive words as triggers during the training of TI, which will be censored for normal use. In the subsequent generation stage, if the triggers are combined with personalized embeddings as final prompts, the model will output a pre-defined target image rather than images including the desired malicious concept. To demonstrate the effectiveness of our approach, we conduct extensive experiments on Stable Diffusion, a prevailing open-sourced text-to-image model. Our code, data, and results are available at https://concept-censorship.github.io.

</details>