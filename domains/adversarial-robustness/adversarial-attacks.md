# 对抗攻击

[返回上级目录](README.md)

## 研究方向

研究通过数字、物理、跨模态或结构化扰动使模型产生错误预测、幻觉或危险行为，覆盖白盒、灰盒、黑盒、迁移和 query-efficient threat model；本页不收录以绕过拒答为核心的 jailbreak。

## 研究脉络

- **输入空间扰动：** 经典 adversarial example 从图像像素扩展到音频、时序、图、表格和多模态输入。
- **迁移与黑盒：** Surrogate、gradient aggregation、evolutionary search 和 hard-label attack 降低攻击知识与查询要求。
- **物理与系统攻击：** Patch、3D object、LiDAR 和 cyber-physical synthesis 检验现实传感链中的攻击可实现性。
- **当前边界：** 可感知性、任务有效性和真实部署约束仍常被分开报告。

## 攻击机理、Scaling Law 与理论分析

### 1. Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips

📄 [arXiv](https://arxiv.org/abs/2608.25276)　📅 2026-08

**关键词**：`attack`、`MoE routing`、`bit-flip perturbation`、`availability failure`、`MoE DoS`、`routing-layer bit flip`

👤 **作者**：Huakang Lin、…、Ruyi Ding

- 🎯 **研究动机**：MoE 路由层特定 expert 与 end-of-sequence 等 token 强相关，构成轻量位翻转攻击面
- 🔬 **研究方法**：Groundhog Bit-Flip Attack 翻转路由层比特使 expert 失活，在四个 MoE LLM 的对话、推理与 Agent 任务上诱发输出膨胀
- 📌 **结论**：平均失活不到 4 个 expert 即使输出膨胀 5912%，多数样本达 max tokens，构成 Denial-of-Wallet 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) architectures enable scalable and efficient large language models (LLMs) by selectively activating expert sub-networks through a routing mechanism. However, this adaptive design introduces a new attack surface: specific experts become disproportionately correlated with certain tokens (e.g., end-of-sequence), allowing adversaries to manipulate model behavior via lightweight perturbations. In this work, we present \textbf{Groundhog Bit-Flip Attack (GBFA)}, the first bit-flip-based \textit{ Denial-of-Wallet availability attack} against MoE-based LLMs. By identifying and flipping routing-layer bits associated with related expert activations, we demonstrate that GBFA substantially extends the decoding token usage across three different LLM modes: conversational, reasoning, and agentic tasks, while largely preserving semantic fidelity. Across four main real-world MoE-based LLMs, manually deactivating on average fewer than \textbf{4 experts} drives average output inflation to $\mathbf{5912\%}$, with the majority of test samples reaching max tokens. These results reveal a robustness vulnerability of MoE architectures to bit flip, and highlight the potential of GBFA as an availability attack against LLMs.

</details>

### 2. COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.17234)　📅 2026-08

**关键词**：`analysis`、`defense`、`jailbreak`、`adversarial robustness`、`VLM safety`、`reference grounding`

👤 **作者**：Md Abdullahil Oaphy、Anhao Xiang、Zongxing Xie、Huayue Gu、Chenyu Wang、Honghui Xu

- 🎯 **研究动机**：多模态越狱中 prompt 与图像单独都无害，危害在良性操作与局部视觉目标绑定时才涌现，现有防御整体审查 prompt-图像对
- 🔬 **研究方法**：COMIC 预生成安全门：推断请求操作与引用类型、从 OCR 与开放词汇构建候选目标、接地后按显式操作-目标对评估安全，结合最大风险聚合与质量感知路由保守决策
- 📌 **结论**：跨多个开源 MLLM 与局部化越狱基准一致提升鲁棒性并保留良性效用与效率；不建模操作、视觉目标与接地置信度就无法可靠执行多模态安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) are increasingly used to interact with screenshots, scanned documents, diagrams, and other visually grounded inputs. This shift introduces a new safety risk: in many multimodal jailbreaks, neither the prompt nor the image is harmful in isolation. Unsafe behavior emerges only when the model binds an apparently benign operation, such as summarizing, translating, or following, to a localized visual target. This reveals a structural weakness in current multimodal defenses, which largely moderate the prompt-image pair as a whole even though the true security-relevant unit is the grounded operation-target pair produced during dereference. In this work, we identify and analyze this reference-dependent failure mode and show that existing defenses degrade when harmful semantics are localized, activated only after grounding, and dependent on visual reference resolution. To address this problem, we propose COMIC (Context-Operation-Modality-Image-Classifier), a reference-aware pre-generation safety gate for MLLMs. COMIC first infers the requested operation and reference type, constructs candidate targets from OCR and open-vocabulary proposals, grounds plausible referents, and evaluates safety over explicit operation-target pairs. To handle ambiguity conservatively, COMIC combines max-risk aggregation with quality-aware routing before deciding whether to forward or block a request. We evaluate COMIC across multiple open-source MLLMs, localized and broader multimodal jailbreak benchmarks, and benign reference-sensitive settings. The results show that COMIC consistently improves robustness while preserving benign utility and practical efficiency. More broadly, our findings suggest that multimodal safety cannot be enforced reliably without modeling the requested operation, the visual target to which it applies, and the confidence of that grounding.

</details>

### 3. OBJVanish: Prompt-Driven Generation of Physically Realizable 3D LiDAR-Invisible Objects

📄 [arXiv](https://arxiv.org/abs/2510.06952) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63685)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`LiDAR 3D detection`、`text-to-3D`、`physical adversarial example`、`dangerous capability`

👤 **作者**：Bing Li、…、Qing Guo

- 🎯 **研究动机**：既有 3D 对抗扰动难以使物体完全消失且物理环境难以实现
- 🔬 **研究方法**：提出 text-to-3D 对抗生成：在 CARLA 中系统研究拓扑、连通性与强度对检测的影响，Phy3DAdvGen 迭代优化 prompt 的动词、物体与姿态，并由 13 个真实物体池约束保证物理可实现
- 📌 **结论**：生成的 3D 行人可在仿真与物理环境中同时躲过六个 SoTA LiDAR 3D 检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LiDAR-based 3D object detectors are fundamental to autonomous driving, where failing to detect objects poses severe safety risks. Developing effective 3D adversarial attacks is essential for thoroughly testing these detection systems and exposing their vulnerabilities before real-world deployment. However, existing adversarial attacks that add optimized perturbations to 3D points have two critical limitations: they rarely cause complete object disappearance and prove difficult to implement in physical environments. We introduce the text-to-3D adversarial generation method, a novel approach enabling physically realizable attacks that can generate 3D models of objects truly invisible to LiDAR detectors and be easily realized in the real world. Specifically, we present the first empirical study that systematically investigates the factors influencing detection vulnerability by manipulating the topology, connectivity, and intensity of individual pedestrian 3D models and combining pedestrians with multiple objects within the CARLA simulation environment. Building on the insights, we propose the physically-informed text-to-3D adversarial generation (Phy3DAdvGen) that systematically optimizes text prompts by iteratively refining verbs, objects, and poses to produce LiDAR-invisible pedestrians. To ensure physical realizability, we construct a comprehensive object pool containing 13 3D models of real objects and constrain Phy3DAdvGen to generate 3D objects based on combinations of objects in this set. Extensive experiments demonstrate that our approach can generate 3D pedestrians that evade six state-of-the-art (SOTA) LiDAR 3D detectors in both CARLA simulation and physical environments, thereby highlighting vulnerabilities in safety-critical applications.

</details>

### 4. ActivationBackdoor: Backdooring Large Language Models in Collaborative Inference via Intermediate Activations

🌐 [Project](https://doi.org/10.1145/3770855.3818136)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`collaborative inference`、`activation backdoor`、`split trust boundary`、`LLM backdoor`、`activation injection`

- 🎯 **研究动机**：协同推理中参与方之间转发的中间激活构成新攻击面，恶意参与者可在推理时操纵激活；既往研究聚焦隐私泄漏，后门威胁未被探索
- 🔬 **研究方法**：提出 ActivationBackdoor：推理时后门，组合触发检测与后门行为注入两个激活级组件，实现“干净输入正常、触发输入产生指定行为”，不需训练数据与参数更新
- 📌 **结论**：在分类与开放式生成任务上攻击成功率可比肩训练时后门基线，同时保持高干净任务准确率与效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Collaborative inference enables cost-effective deployment of large language models by partitioning layers across multiple participants and forwarding intermediate activations between participants in a pipeline, but these transmitted activations also create a new attack surface: a malicious participant can manipulate intermediate activations during inference. Prior work on collaborative inference attacks has largely focused on privacy leakage, leaving the backdoor threat insufficiently explored. Inspired by recent advances in representation engineering, we propose ActivationBackdoor, an inference-time backdoor attack that composes two activation-level components for trigger detection and backdoor behavior injection. This design achieves the same ''clean inputs behave normally, triggered inputs induce attacker-specified behavior'' property as traditional backdoor attacks, while requiring no access to training data and no model parameter updates. Experiments across classification and open-ended generation tasks show that ActivationBackdoor attains attack success comparable to training-time backdoor baselines while preserving high clean-task accuracy and utility. Overall, our results expose a new and practical backdoor risk in collaborative inference arising from intermediate activation exposure.

</details>

### 5. The Boy Who Cried Wolf: Adversarial Misclassification of Safe Inputs as Unsafe in Multimodal Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.01373) · 🌐 [Project](https://doi.org/10.1145/3770855.3817756)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`multimodal adversarial example`、`unsafe induction`、`guardrail evasion`、`multimodal guardrail`、`over-refusal`

👤 **作者**：Shuo Shi、…、Shouling Ji

- 🎯 **研究动机**：多模态 guard 对抗研究集中于假阴性越狱，诱导假阳性使良性请求被拒的可用性威胁未被探索
- 🔬 **研究方法**：提出 Unsafe Induction Attacks，其 USD 方法把对抗扰动与不安全内容的分布表征对齐，使安全图像在多样用户 prompt 下触发 guard 拒绝合法请求
- 📌 **结论**：在四个 SOTA guard 模型的真实用户模拟场景中 USD 攻击成功率达 84%，超过现有方法，暴露多模态安全架构的可用性失败模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal guard models have emerged as critical safety components for screening content in vision-language systems. While adversarial research has extensively studied jailbreaking attacks that produce false negatives, the inverse threat of inducing false positives on benign inputs remains unexplored. We introduce Unsafe Induction Attacks, where adversaries distribute imperceptibly perturbed safe images that trigger guard models to reject legitimate user requests, causing a "Boy Who Cried Wolf" effect that degrades service availability and erodes trust. This reveals an availability failure mode in deployed safety filters. To realize this threat under diverse user prompts, we propose Unsafe Semantic Distillation (USD), which aligns adversarial perturbations with distributional representations of unsafe content rather than prompt-specific instances. Evaluated on four state-of-the-art guard models across realistic user simulation scenarios, USD achieves 84% attack success rates, outperforming existing methods and exposing fundamental vulnerabilities in current multimodal safety architectures.

</details>

### 6. Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.22312)　📅 2026-08

**关键词**：`attack`、`analysis`、`MLLM`、`semantic perturbation`、`black-box transfer`、`cross-modal safety gap`

👤 **作者**：Wenyun Li、Guiping Cao、Xiangyuan Lan、Zheng Zhang

- 🎯 **研究动机**：文本空间学到的安全行为不能可靠迁移到融合跨模态表示，黑盒迁移攻击又易过拟合代理模型
- 🔬 **研究方法**：TA-SPA 在文本锚定语义空间优化可迁移扰动：TASF 分离跨模态语义因子与模态特异残差，SPA 在保持语义一致下多样化有害目标锚点
- 📌 **结论**：攻击对未见与商业 MLLM 强效迁移，在代表性防御下仍有竞争力，说明需要表示级而非输入级的安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal representations, leaving multimodal inputs exploitable through latent semantic cues. We propose Text-Anchored Semantic Perturbation Attack (TA-SPA), a black-box jailbreak framework that optimizes transferable perturbations in a text-anchored semantic space. TA-SPA integrates Text-Anchored Semantic Factorization (TASF), which encourages the separation of cross-modal semantic factors from modality-specific residuals, with Semantic-Preserving Augmentation (SPA), which diversifies harmful target anchors while preserving semantic consistency. Experiments show strong attack effectiveness and transfer to commercial MLLMs, with competitive performance under representative defenses. Additional controls and probing support the intended factorization without implying perfect disentanglement, motivating representation-level safety alignment beyond input-level filtering.

</details>

### 7. Breaking the weakest link to evade vision language models

📄 [arXiv](https://arxiv.org/abs/2608.18938)　📅 2026-08

**关键词**：`attack`、`VLM evasion`、`vision-encoder optimization`、`semantic manipulation`、`vision encoder`、`targeted semantics`

👤 **作者**：Ilan Zini、Boussad Addad、Katarzyna Kapusta

- 🎯 **研究动机**：VLM 对抗鲁棒性尤其针对多模态对齐的逃逸攻击探索不足
- 🔬 **研究方法**：梯度攻击仅在 VLM 的视觉编码器上优化而非整个多模态架构，支持无目标与目标语义两种设定，显著降低计算成本
- 📌 **结论**：Qwen2.5-VL、Granite-Vision、FastVLM、Phi-3.5-Vision 上小的不敏感扰动即可大幅改变模型文本解读

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Language Models (VLMs) have recently emerged as a critical component of multimodal AI systems, enabling joint reasoning over visual and textual inputs in real-world and safety-critical applications. Despite their growing deployment, the robustness of VLMs against adversarial threats remains insufficiently explored, particularly in the context of evasion attacks targeting multimodal alignment. In this work, we investigate the vulnerability of VLMs to adversarial perturbations applied to visual inputs and study two attack settings: untargeted attacks, where the goal is to disrupt the model's interpretation of the original image, and targeted attacks, where the adversary aims to force the model to generate a specific semantic description unrelated to the original image. To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture. This design significantly reduces the computational cost and resource requirements of the attack while maintaining strong effectiveness. We evaluate our approach on several open-source VLMs, including Qwen2.5-VL, Granite-Vision, FastVLM, and Phi-3.5-Vision, and show that small, human-imperceptible perturbations can substantially alter the textual interpretation produced by the models. Our findings highlight the vulnerability of modern VLMs to adversarial manipulation and emphasize the need for improved robustness and security mechanisms in multimodal AI systems.

</details>

### 8. Perspective-Invariant Attack with Enhanced Transferability of Adversarial Examples

📄 [arXiv](https://arxiv.org/abs/2608.15115) · 🌐 [Project](https://doi.org/10.1109/TIFS.2026.3714109)　📅 2026-08

**关键词**：`attack`、`adversarial robustness`、`adversarial example`、`evasion attack`

👤 **作者**：Kaisheng Liang、Yiming Cao、Bin Xiao

- 🎯 **研究动机**：输入变换增强迁移攻击多依赖低自由度局部操作（分块打乱、缩放），忽略视角变化带来的全局透视变换
- 🔬 **研究方法**：PIA 用多自由度顶点采样系统覆盖 2-DOF 平移到 8-DOF 投影映射的变换层级；PIA-Mix 维持互补变换池高效组合辅助方法
- 📌 **结论**：在多种 DNN 架构、先进防御与多模态 LLM 上超越 SOTA 迁移攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial examples generated on a surrogate deep neural network (DNN) can often successfully fool other black-box DNN models. This cross-model transferability poses serious security threats to DNNs in practical applications. Input transformation techniques are widely used to enhance adversarial transferability by increasing the diversity of input images. However, existing methods primarily rely on local operations with limited degrees of freedom (DOF), such as block-wise shuffling and resizing, overlooking global perspective transformations that naturally arise from viewpoint changes. In this work, we propose a Perspective-Invariant Attack (PIA), which introduces a multi-DOF vertex sampling strategy that systematically covers the perspective transformation hierarchy from 2-DOF translation to 8-DOF projective mapping. By generating geometrically diverse input variations, PIA effectively reduces overfitting of adversarial perturbations to the surrogate model, thereby improving adversarial transferability. We further propose PIA-Mix, a generic extension that maintains a complementary transformation pool and efficiently combines our perspective transformation with auxiliary methods for improved transferability. Extensive experiments involving various DNN architectures, advanced defense mechanisms, and multimodal large language models (LLMs) demonstrate that PIA and PIA-Mix outperform state-of-the-art transfer-based attacks.

</details>

### 9. Eliciting Intrinsic Hallucinations in LLMs via Semantically Equivalent Adversarial Attacks

📄 [arXiv](https://arxiv.org/abs/2608.04286) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-08

**关键词**：`attack`、`RAG hallucination`、`adversarial robustness`、`adversarial example`、`semantic-equivalent query`、`context faithfulness`

👤 **作者**：Atri Vivek Sharma、Brian Formento、Alessio Lomuscio

- 🎯 **研究动机**：RAG 系统在语义等价的查询变体下是否保持对检索证据的忠实缺乏压力测试
- 🔬 **研究方法**：以严格语义等价约束与内在幻觉为目标做对抗优化，覆盖白盒/灰盒/黑盒攻击，在 5 开源+5 闭源生成器、3 数据集上评测
- 📌 **结论**：保义扰动使上下文忠实性最多下降 50%（GPT-5-mini），SOTA 模型的证据忠实仍脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often used in conjunction with external knowledge sources to improve their factual accuracy and decrease hallucinations, through methods such as Retrieval-Augmented Generation (RAG). However, these systems remain susceptible to intrinsic hallucinations, where the model generates unfaithful or fabricated information that is not supported by the retrieved evidence. We propose a novel framework to assess model robustness against this phenomenon by stress-testing using natural, semantically equivalent variations of a user query found via adversarial optimization methods. We apply our framework, which enforces strict semantic equivalence constraints and an intrinsic hallucination objective, to a range of adversarial attack techniques across white-box, gray-box, and black-box adversarial settings. Evaluating these attacks on 5 open-source and 5 closed-source generator models across 3 datasets, we demonstrate that even state-of-the-art models are highly susceptible to meaning-preserving perturbations, which significantly degrade contextual faithfulness (by up to 50% for GPT-5-mini). Our findings indicate that faithful use of in-context evidence remains fragile even in state-of-the-art LLMs, motivating architectures and training objectives that enforce robust grounding independent of surface query form. Code is available at: https://github.com/atriviveksharma/intrinsic_hall

</details>

### 10. The Insider's Advantage: Exploiting Automated Privacy Policy Analyzer Tools Through Subtle Text Manipulations

🌐 [Project](https://doi.org/10.1145/3779208.3807480)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`attack`、`LLM analyzer`、`adversarial text`、`compliance evasion`、`privacy policy analyzer`

- 🎯 **研究动机**：自动隐私政策分析工具对细微文本操纵的鲁棒性未明
- 🔬 **研究方法**：以细微文本操纵诱导分析器漏检违规条款
- 📌 **结论**：简单改写即可实现compliance evasion

### 11. Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.04846) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Multi-Paradigm_Collaborative_Adversarial_Attack_Against_Multi-Modal_Large_Language_Models_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`MLLM`、`multi-paradigm perturbation`、`collaborative optimization`

👤 **作者**：Yuanbo Li、Tianyang Xu、Cong Hu、Tao Zhou、Xiao-Jun Wu、Josef Kittler

- 🎯 **研究动机**：单范式代理模型限制了特征丰富度与扰动搜索空间，阻碍迁移攻击效果
- 🔬 **研究方法**：MPCAttack 聚合多范式的视觉与语言语义表示做联合对抗优化，对比匹配自适应平衡各范式重要性以缓解表示偏置
- 📌 **结论**：在开源与闭源 MLLM 的定向与非定向攻击上均持续超越 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid progress of Multi-Modal Large Language Models (MLLMs) has significantly advanced downstream applications. However, this progress also exposes serious transferable adversarial vulnerabilities. In general, existing adversarial attacks against MLLMs typically rely on surrogate models trained within a single learning paradigm and perform independent optimisation in their respective feature spaces. This straightforward setting naturally restricts the richness of feature representations, delivering limits on the search space and thus impeding the diversity of adversarial perturbations. To address this, we propose a novel Multi-Paradigm Collaborative Attack (MPCAttack) framework to boost the transferability of adversarial examples against MLLMs. In principle, MPCAttack aggregates semantic representations, from both visual images and language texts, to facilitate joint adversarial optimisation on the aggregated features through a Multi-Paradigm Collaborative Optimisation (MPCO) strategy. By performing contrastive matching on multi-paradigm features, MPCO adaptively balances the importance of different paradigm representations and guides the global perturbation optimisation, effectively alleviating the representation bias. Extensive experimental results on multiple benchmarks demonstrate the superiority of MPCAttack, indicating that our solution consistently outperforms state-of-the-art methods in both targeted and untargeted attacks on open-source and closed-source MLLMs. The code is released at https://github.com/LiYuanBoJNU/MPCAttack.

</details>

### 12. Towards Highly Transferable Vision-Language Attack via Semantic-Augmented Dynamic Contrastive Interaction

📄 [arXiv](https://arxiv.org/abs/2603.04839) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Highly_Transferable_Vision-Language_Attack_via_Semantic-Augmented_Dynamic_Contrastive_Interaction_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`attack`、`vision-language model`、`semantic transfer`、`contrastive interaction`

👤 **作者**：Yuanbo Li、Tianyang Xu、Cong Hu、Tao Zhou、Xiao-Jun Wu、Josef Kittler

- 🎯 **研究动机**：现有 VLP 攻击依赖静态跨模态交互且只破坏正样本对，跨模态破坏有限、迁移性差
- 🔬 **研究方法**：SADCA 以对抗/正/负样本的对比机制渐进破坏跨模态对齐，并用语义增强模块提升对抗样本多样性与泛化
- 📌 **结论**：多数据集与模型上显著提升对抗迁移性，持续超越 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement and widespread application of vision-language pre-training (VLP) models, their vulnerability to adversarial attacks has become a critical concern. In general, the adversarial examples can typically be designed to exhibit transferable power, attacking not only different models but also across diverse tasks. However, existing attacks on language-vision models mainly rely on static cross-modal interactions and focus solely on disrupting positive image-text pairs, resulting in limited cross-modal disruption and poor transferability. To address this issue, we propose a Semantic-Augmented Dynamic Contrastive Attack (SADCA) that enhances adversarial transferability through progressive and semantically guided perturbation. SADCA progressively disrupts cross-modal alignment through dynamic interactions between adversarial images and texts. This is accomplished by SADCA establishing a contrastive learning mechanism involving adversarial, positive and negative samples, to reinforce the semantic inconsistency of the obtained perturbations. Moreover, we empirically find that input transformations commonly used in traditional transfer-based attacks also benefit VLPs, which motivates a semantic augmentation module that increases the diversity and generalization of adversarial examples. Extensive experiments on multiple datasets and models demonstrate that SADCA significantly improves adversarial transferability and consistently surpasses state-of-the-art methods. The code is released at https://github.com/LiYuanBoJNU/SADCA.

</details>

### 13. PA-Attack: Guiding Gray-Box Attacks on LVLM Vision Encoders with Prototypes and Attention

📄 [arXiv](https://arxiv.org/abs/2602.19418) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Mei_PA-Attack_Guiding_Gray-Box_Attacks_on_LVLM_Vision_Encoders_with_Prototypes_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`attack`、`LVLM encoder`、`gray-box threat`、`prototype attention`

👤 **作者**：Hefei Mei、Zirui Wang、Chang Xu、Jianyuan Guo、Minjing Dong

- 🎯 **研究动机**：白盒攻击跨任务泛化差、黑盒迁移昂贵，而跨 LVLM 共享的视觉编码器提供了稳定灰盒支点
- 🔬 **研究方法**：PA-Attack 以原型锚定提供指向一般性远异原型的稳定攻击方向，两阶段注意力增强把扰动集中到关键视觉 token 并自适应校准
- 📌 **结论**：跨下游任务与 LVLM 架构平均得分降幅（SRR）达 75.1%，兼顾效率与任务泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) are foundational to modern multimodal applications, yet their susceptibility to adversarial attacks remains a critical concern. Prior white-box attacks rarely generalize across tasks, and black-box methods depend on expensive transfer, which limits efficiency. The vision encoder, standardized and often shared across LVLMs, provides a stable gray-box pivot with strong cross-model transfer. Building on this premise, we introduce PA-Attack (Prototype-Anchored Attentive Attack). PA-Attack begins with a prototype-anchored guidance that provides a stable attack direction towards a general and dissimilar prototype, tackling the attribute-restricted issue and limited task generalization of vanilla attacks. Building on this, we propose a two-stage attention enhancement mechanism: (i) leverage token-level attention scores to concentrate perturbations on critical visual tokens, and (ii) adaptively recalibrate attention weights to track the evolving attention during the adversarial process. Extensive experiments across diverse downstream tasks and LVLM architectures show that PA-Attack achieves an average 75.1% score reduction rate (SRR), demonstrating strong attack effectiveness, efficiency, and task generalization in LVLMs. Code is available at https://github.com/hefeimei06/PA-Attack.

</details>

### 14. Semantic Router: On the Feasibility of Hijacking MLLMs via a Single Adversarial Perturbation

📄 [arXiv](https://arxiv.org/abs/2511.20002) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65213)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Changyue Li、Jiaying Li、Youliang Yuan、Jiaming He、Zhicong Huang、Pinjia He

- 🎯 **研究动机**：部署于自动驾驶、机器人等无状态系统的 MLLM 面临未研究的 Semantic-Aware Hijacking 威胁：单个通用扰动能否同时劫持多个无状态决策
- 🔬 **研究方法**：提出 SAUP 充当语义路由器，主动感知输入语义并路由到攻击者指定目标；基于潜空间几何分析提出 SORT 优化策略并标注细粒度语义数据集
- 📌 **结论**：在三个 MLLM 上验证攻击可行，单帧对 Qwen 的五个目标攻击成功率达 66%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in stateless systems, such as autonomous driving and robotics. This paper investigates a novel threat: Semantic-Aware Hijacking. We explore the feasibility of hijacking multiple stateless decisions simultaneously using a single universal perturbation. We introduce the Semantic-Aware Universal Perturbation (SAUP), which acts as a semantic router, "actively" perceiving input semantics and routing them to distinct, attacker-defined targets. To achieve this, we conduct a theoretical and empirical analysis on the geometric properties in the latent space. Guided by these insights, we propose the Semantic-Oriented (SORT) optimization strategy and annotate a new dataset with fine-grained semantics to evaluate performance. Extensive experiments on three representative MLLMs demonstrate the fundamental feasibility of this attack, achieving a 66% attack success rate over five targets using a single frame against Qwen.

</details>

### 15. REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations

📄 [arXiv](https://arxiv.org/abs/2605.12813) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66287)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Buyun Liang、…、René Vidal

- 🎯 **研究动机**：系统评估 LLM 在真实对抗输入下的幻觉需要语义等价的提示，离散攻击搜索空间受限而连续潜空间攻击常丢失语义合理性
- 🔬 **研究方法**：提出 REALISTA：构建依赖输入的语义等价改写方向字典，在潜空间对方向做连续组合优化
- 📌 **结论**：在开源 LLM 上达到或超过 SOTA 真实攻击，并成功攻击自由回复设定下先前攻击失效的大型推理模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) achieve strong performance across many tasks but remain vulnerable to hallucinations, making it important to systematically evaluate their reliability under realistic adversarial inputs. We formulate hallucination elicitation as a constrained optimization problem, where the goal is to find semantically coherent adversarial prompts that are equivalent to benign user prompts. Existing attack methods remain limited: discrete prompt-based attacks preserve semantic equivalence and coherence but search only over a limited set of prompt variations, while continuous latent-space attacks explore a richer space but often decode into prompts that are no longer valid rephrasings. To address these limitations, we propose REALISTA, a realistic latent-space attack framework. REALISTA constructs an input-dependent dictionary of valid editing directions, each corresponding to a semantically equivalent and coherent rephrasing, and optimizes continuous combinations of these directions in latent space. This design combines the optimization flexibility of continuous attacks with the semantic realism of discrete rephrasing-based attacks. Experiments demonstrate that REALISTA achieves superior or comparable performance to state-of-the-art realistic attacks on open-source LLMs and, crucially, succeeds in attacking large reasoning models under free-form response settings, where prior realistic attacks fail.

</details>

### 16. MADA-Attack: Transferable Multi-modal Attention Distraction Adversarial Attack against Vision Language Models

🎓 [Official](https://icml.cc/virtual/2026/poster/61385)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`VLM safety`、`empirical evaluation`、`attack transferability`

👤 **作者**：Zhihan Qin、…、Shouling Ji

- 🎯 **研究动机**：现有通用对抗扰动只作用于视觉模态，忽略结构化文本语义与跨模态交互
- 🔬 **研究方法**：Semantic Token Manipulation 引导文本注意力，Fused Embedding Training 联合优化双模态嵌入损失，自适应数据增强平衡攻击强度与迁移性
- 📌 **结论**：零样本分类与图像描述平均 ASR 82.60%/73.42%，VQA 与 I-T 检索超 SOTA 基线 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision Language Models (VLMs) achieve strong performance across multi-modal tasks but remain vulnerable to universal adversarial perturbations (UAPs). Existing UAP methods mainly operate on the visual modality, overlooking structured textual semantics and cross-modal interactions, which limits their ability to disrupt alignment and generalize across tasks and model architectures. To address these limits, we propose Multi-modal Attention Distraction Adversarial Attack (MADA-Attack) framework. We begin by conducting several insight experiments and discover that modality attention distributes differently over layers and early phase of optimization is decisive. Building on these observations, we introduce Semantic Token Manipulation (STM) to steer text-guided attention, and Fused Embedding Training (FET) to jointly optimize textual and visual embedding losses for coordinated misalignment. We further incorporate an Adaptive Data Augmentation (ADA) strategy that dynamically balances attack strength, transferability, and training efficiency. Extensive experiments demonstrate that MADA-Attack consistently achieves state-of-the-art performance and strong transferability while remaining computationally lightweight, with an average ASR of 82.60\% and 73.42\% in zero-shot classification and image captioning tasks. For the visual question answering (VQA) and I-T Retrieval task, our method exceeds the SOTA baseline by 10\%. Our code is available at this GitHub Repository.

</details>

### 17. From Zero to Hero: Cross-modal-enhanced Adversarial Item Promotion Attack against Multimodal Recommender Systems

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yao-zero)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`multimodal recommender`、`item promotion`、`adversarial robustness`、`cross-modal perturbation`

👤 **作者**：Mengyu Yao、…、Ding Li

- 🎯 **研究动机**：对抗商品推广攻击只针对单模态推荐器，VLM 攻击不优化排序目标，多模态推荐器（MRS）漏洞未探
- 🔬 **研究方法**：CREAM 黑盒下联合扰动视觉与文本并保持语义一致，集成视觉扰动器、文本生成器与联合优化控制器
- 📌 **结论**：平均 top-10/top-50 曝光提升 5.75x/2.89x 且多维不可感知；试探的防御策略均有局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal recommender systems (MRSs) jointly leverage visual and textual item representations to determine item ranking and exposure in modern online platforms. Their strong dependence on item content, however, introduces new security risks. In particular, malicious sellers can conduct the adversarial item promotion (AIP) attack to manipulate item content to deceive the recommender into overranking specific items. When it succeeds, the promoted items gain disproportionately higher exposure, leading to significant market visibility and direct economic gain. However, existing AIP research primarily targets unimodal recommenders, leaving the unique vulnerabilities of MRSs largely unexplored. Meanwhile, multimodal adversarial attacks for vision–language models (VLMs) optimize objectives unrelated to ranking and lack cross-modal coordination unique to MRSs. To bridge this gap, we propose CREAM (CRoss-modal-Enhanced AIP attack against MRSs). Our key insight is to jointly perturb multiple modalities in a semantically consistent manner}. We integrate a tailored visual perturbator, a text generator, and a joint optimization controller to fully exploit cross-modal correlations in a black-box setting. Our comprehensive evaluation shows that CREAM significantly outperforms existing methods, achieving on average 5.75x and 2.89x higher exposure at top-10 and top-50 metrics, and demonstrates robustness under evolving real-world conditions. This exposes a tangible economic risk to recommender platforms. Meanwhile, CREAM maintains high imperceptibility across visual, textual, and cross-modal dimensions. We further investigate several potential defense strategies and demonstrate their limitations, highlighting the urgent need for stronger protections against adversarial threats in MRSs.

</details>

### 18. DDGA: Dirichlet Distributional Gradient Aggregation for Transferable Vision-Language Adversarial Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/63187)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`VLM safety`、`empirical evaluation`、`attack transferability`

👤 **作者**：You Yiwei、Jiaan Wei、Zan Chen、Bo Wang

- 🎯 **研究动机**：AET 类迁移攻击靠有限随机采样近似扰动分布，在有限预算下不稳定
- 🔬 **研究方法**：DDGA 用可学习 Dirichlet 策略参数化单纯形混合权重、经策略梯度优化期望对抗目标，并利用分布闭式协方差构造正交扰动增强梯度多样性
- 📌 **结论**：图文检索与图像描述任务上跨多个 VLM 架构一致超越 SOTA 迁移攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) achieve remarkable performance on multimodal tasks but remain highly vulnerable to adversarial examples, making transferable attacks essential for realistic robustness evaluation. Recent Adversarial Evolution Triangle (AET) methods improve transferability by interpolating over a simplex formed by clean and historical adversarial samples, yet rely on finite random sampling to approximate effective perturbation distributions, which is unstable under limited budgets. In this paper, we propose Dirichlet Distributional Gradient Aggregation (DDGA), a distribution-aware adversarial attack framework that explicitly models and optimizes perturbations over the AET simplex. DDGA parameterizes simplex mixing weights with a learnable Dirichlet policy and optimizes the expected adversarial objective via policy gradient, replacing heuristic sampling with principled distributional optimization. Moreover, we exploit the closed-form covariance of the learned distribution to construct orthogonal perturbations that enhance gradient diversity. Extensive experiments on image-text retrieval and image captioning demonstrate that DDGA consistently outperforms state-of-the-art transfer-based attacks across multiple VLM architectures.

</details>

### 19. Attacking Gray-Box Large Vision-Language Models with Adaptive SVD-Structured Adversarial Alignment

🎓 [Official](https://icml.cc/virtual/2026/poster/66338)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`VLM safety`、`empirical evaluation`、`attack transferability`

👤 **作者**：Daizong Liu、…、Dengpan Ye

- 🎯 **研究动机**：现有 LVLM 攻击依赖全模型梯度或精细迁移策略，资源开销大
- 🔬 **研究方法**：灰盒设定仅访问视觉编码器：全局语义对齐模块把视觉特征投影到攻击者选定目标文本张成的 SVD 结构子空间，并用最优传输把细节视觉特征与 LLM 扩展的多上下文语义文本对齐
- 📌 **结论**：攻击效果优越，经 CLIP-aware 迁移设计可跨多种 LVLM 泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have demonstrated remarkable capabilities across a wide range of multimodal reasoning tasks. However, recent research shows that they are susceptible to adversarial examples. Existing LVLM attack methods are generally deployed in the white- or black-box setting, which severely rely on full-model gradients or elaborated transfer strategies, resulting in large resource costs. To this end, this paper focuses on a more efficient gray-box attack setting by solely accessing LVLM's vision encoder. Instead of using target images as the adversarial guidance, our main goal is to perturb the visual feature to best match more natural attacker-chosen target texts. Specifically, we develop a global semantic alignment module to project the visual features onto the SVD-structured subspace spanned by the textual semantics. We also propose to align detailed visual features with multi-context semantic texts extended by LLMs over discrete distributions via optimal transport. Extensive experiments demonstrate the superiority of the proposed method, while our attack is further proven to achieve great transferability across various LVLMs with CLIP-aware transfer designs.

</details>

### 20. AdvFM: Lookahead Flow-Matching Velocity-Field Attacks for Imperceptible and Transferable Adversarial Examples

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_AdvFM_Lookahead_Flow-Matching_Velocity-Field_Attacks_for_Imperceptible_and_Transferable_Adversarial_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`flow matching`、`transfer attack`、`imperceptible perturbation`

👤 **作者**：Runze Liu、…、Zhaoyang Zhang

- 🎯 **研究动机**：基于生成模型的无约束对抗攻击多在像素空间或扩散式去噪-加噪操作，迁移性与抗防御能力受限
- 🔬 **研究方法**：提出 AdvFM，把对抗信号注入 flow matching 速度场而非像素空间：扰动 t=1 处重建并转为速度场变化以放大噪声空间内的 PGD 步；lookahead 变体在当前与 rollout 重建上优化两点目标
- 📌 **结论**：理论上具有更大单步黑盒损失增幅、更低梯度方差、扰动集中于 robust-tangent 方向；黑盒迁移与对抗训练、净化防御下均表现更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unrestricted adversarial attacks based on generative models typically operate either directly in image space or through diffusion-style denoising and re-noising, which limits transferability and robustness against defenses. We revisit this problem through the lens of flow matching and continuous-time velocity fields, and propose AdvFM, a velocity-field attack that injects adversarial signals into the flow-matching dynamics instead of the pixel space. Given a noisy state x_t, AdvFM perturbs the reconstruction at t = 1 and converts this perturbation into a change of the velocity field, yielding a state update that amplifies the inner PGD step in the noisy space. We further introduce a lookahead variant that optimizes a two-point objective over the current and rolled-out reconstructions, reducing temporal mismatch along the ODE trajectory. From a theoretical perspective, we show that compared to diffusion-based attacks, AdvFM enjoys: (i) larger single-step increases in the black-box loss via step amplification, (ii) reduced gradient variance and stronger surrogate-target alignment due to Gaussian smoothing, enhancing its transferability, and (iii) perturbations that concentrate in robust-tangent directions, thereby aligning with robust gradients of adversarially trained models and surviving purification more effectively; the lookahead variant further lowers gradient noise for a two-point robust objective. Extensive experiments demonstrate that AdvFM achieves promising performance in both black-box transferability and a suite of adversarial training and purification defenses.

</details>

### 21. Omni-Attack: Adversarial Attacks on Open-Ended VQA in Black-Box Multimodal LLMs

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Omni-Attack_Adversarial_Attacks_on_Open-Ended_VQA_in_Black-Box_Multimodal_LLMs_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`open-ended VQA`、`black-box MLLM`、`semantic manipulation`

👤 **作者**：Kai Hu、…、Matt Fredrikson

- 🎯 **研究动机**：MLLM 对抗鲁棒评测集中在粗粒度分类且协议不一致，开放问答黑盒攻击缺基准
- 🔬 **研究方法**：AdvRobustBench 含 1,000 个 VQA 与 OCR 示例；Omni-Attack 迁移式黑盒攻击：问题条件化文本/视觉目标构造管线与 OCR 位置感知攻击策略
- 📌 **结论**：GPT-4.1 等专有模型上定向攻击成功率最高 71.8%（ε=8/255），揭示当前多模态系统重大漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have achieved remarkable success across diverse applications, from autonomous driving to document understanding. As these models are deployed in safety-critical contexts, understanding their adversarial robustness becomes crucial. However, current evaluations focus primarily on simple tasks like coarse-grained classification, and employ inconsistent evaluation protocols, hindering rigorous comparison of attack methods. We introduce AdvRobustBench, a comprehensive adversarial robustness benchmark for MLLMs comprising 1,000 examples across visual question answering (VQA) and optical character recognition (OCR) tasks, drawn from widely-used MLLM benchmarks (MMBench, MMStar, OCRBench-v2). We further propose Omni-Attack, a novel transfer-based black-box attack method that addresses key challenges in attacking open-ended question-answering systems. Our approach introduces (i) a target-construction pipeline that generates question-conditioned textual and visual targets to provide stronger optimization signals, and (ii) a location-aware attack strategy for OCR that enables spatially-precise perturbations. Extensive experiments demonstrate that Omni-Attack achieves strong targeted attack success rates (up to 71.8% on GPT-4.1 at \varepsilon=8/255) across both proprietary models (GPT-4.1, Claude 3.7, Gemini 2.0) and open-source MLLMs, revealing significant vulnerabilities in current multimodal systems. Our benchmark and findings establish a foundation for developing more robust MLLMs. Codes are available at https://github.com/hukkai/transferable_mllm_attack

</details>

### 22. PGA: Prior-free Generative Attack for Practical No-box Scenario

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_PGA_Prior-free_Generative_Attack_for_Practical_No-box_Scenario_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`no-box threat`、`generative perturbation`、`transferability`

👤 **作者**：Hongyu Peng、Xiang Yuan、Gong Cheng

- 🎯 **研究动机**：Practical No-box 场景下迭代攻击推理慢迁移有限，生成式攻击又依赖该场景缺失的大量先验
- 🔬 **研究方法**：PGA 首个 PNS 定制生成攻击：课程引导微鲁棒优化渐进加难任务缓解少数据自监督退化；区域感知一致扰动学习产生细粒度空间连贯扰动
- 📌 **结论**：各设定下迁移性突出且推理速度快

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The unrealistic reliance on abundant prior information in traditional transferable attacks has spurred the Practical No-box Scenario (PNS), where attackers can access only limited unlabeled images. However, existing methods rely on iterative optimization to produce adversarial examples with inherently limited inference speed and transferability. Conversely, faster generative attacks fundamentally conflict with the PNS due to their critical dependence on abundant prior information that is explicitly absent in this scenario. To bridge this gap, we propose Prior-free Generative Attack (PGA), the first generative attack tailored for the PNS. Specifically, we introduce the Curriculum-Guided Micro-Robust Optimization that progressively incorporates more challenging discriminative tasks to mitigate the degenerate solutions common in self-supervised learning with limited data, yielding robust and transferable surrogates for downstream attacks. Furthermore, the Region-Aware Consistent Perturbation Learning guides the generator to produce fine-grained and spatially coherent perturbations, mitigating the common pitfall of generative attacks falling into local optima under insufficient supervision. Extensive experiments demonstrate that our PGA achieves remarkable transferability across various settings with high inference speed. This work provides a more practical benchmark for future research on transferable attacks, revealing the great potential of generative attacks under the PNS.

</details>

### 23. PureProof: Diffusion-Resistant Black-box Targeted Attack on Large Vision-Language Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Cao_PureProof_Diffusion-Resistant_Black-box_Targeted_Attack_on_Large_Vision-Language_Models_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`LVLM`、`black-box targeted attack`、`diffusion purification`

👤 **作者**：Yiming Cao、Dong Wang、Xinqi Lyu、Bin Xiao

- 🎯 **研究动机**：扩散净化（DBP）有效阻断现有攻击，而已有 DBP 规避攻击针对白盒分类器、适配 VLM 成本高且梯度不稳
- 🔬 **研究方法**：PureProof 三组件：Stochastic Reverse Alignment 单步逆预测引导优化避免全轨迹反传、自适应重加噪增强缓解扩散随机性、自一致性正则稳定优化
- 📌 **结论**：开源与商业 VLM 上对抗 DBP 一致超先前攻击且噪声韧性强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (VLMs) are increasingly deployed across diverse applications, such as AI agents, yet remain vulnerable to targeted adversarial attacks. However, the practical robustness of such attacks often remains unclear with limited evaluation under defenses. Diffusion-based purification (DBP), a widely adopted black-box defense, effectively blocks current attacks by removing adversarial perturbations via generative diffusion. Prior DBP evasion attacks target white-box image classifiers and are ill-suited to VLMs, incurring high computational costs and gradient instability when adapted. In this paper, we present PureProof, a black-box targeted attack on VLMs resilient to DBP. It consists of three core components. Stochastic Reverse Alignment (SRA) guides adversarial optimization via single-step reverse prediction, avoiding costly full-trajectory backpropagation. Adaptive Re-noising Augmentation (ARA) mitigates diffusion stochasticity through timestep-adaptive re-noising. Self-Consistency Regularization (SCR) stabilizes optimization by promoting local temporal coherence. Extensive experiments on open-source and commercial VLMs show that PureProof consistently outperforms prior attacks against DBP and achieves strong noise resilience, revealing critical vulnerabilities in VLMs and offering broader safety implications for real-world VLM deployments, including emerging agentic settings.

</details>

### 24. Transform to Transfer: Boosting Adversarial Attack Transferability on Vision-Language Pre-training Models

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Transform_to_Transfer_Boosting_Adversarial_Attack_Transferability_on_Vision-Language_Pre-training_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`vision-language pretraining`、`input transform`、`black-box transfer`

👤 **作者**：Yang Li、Jia-Li Yin、Luojun Lin、Wei Lin

- 🎯 **研究动机**：VLP 模型黑盒攻击中对抗样本迁移性有限，现有增强方法过度依赖源模型且变换技术固定
- 🔬 **研究方法**：提出 TTA：可学习变换机制自适应选择最优变换组合以最大化输入多样性，引入积分梯度缓解对源模型的过度依赖
- 📌 **结论**：下游任务攻击性能超越现有 SOTA 攻击方法，跨不同 VLP 架构有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Pre-training (VLP) models, while achieving state-of-the-art performance on various multimodal tasks, exhibit significant vulnerability to multimodal adversarial examples. In black-box attack scenarios of VLP models, a key challenge lies in the limited transferability of these adversarial examples. Existing methods to enhance transferability often suffer from an excessive dependence on the source model and a reliance on limited and fixed transformation techniques. To overcome these limitations, we propose a novel Transform to Transfer Attack (TTA) method. Our approach introduces a learnable transformation mechanism that adaptively selects optimal combinations of transformations to maximize input diversity, and incorporates integrated gradients to mitigate over-reliance on the source model, thereby refining the attack optimization process. Extensive experiments demonstrate that TTA achieves outstanding attack performance in downstream tasks, outperforming current state-of-the-art attack methods across different VLP architectures.

</details>

### 25. VCP-Attack: Visual-Contrastive Projection for Transferable Black-Box Targeted Attacks on Large Vision-Language Models

🌐 [Project](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_VCP-Attack_Visual-Contrastive_Projection_for_Transferable_Black-Box_Targeted_Attacks_on_Large_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`LVLM`、`targeted transfer`、`contrastive projection`

👤 **作者**：Jiawei Zhao、Minjie Du、Zihan Qin、Zhuoran Wang、Lizhe Xie、Yining Hu

- 🎯 **研究动机**：LVLM 在黑盒定向攻击下缺乏可迁移的有效攻击手段
- 🔬 **研究方法**：提出 VCP-Attack：动态 PCA 投影把扰动约束在语义低维子空间，多样本对比损失使对抗特征对齐目标语义并推离源语义
- 📌 **结论**：ε=16/255 下开源模型平均 ASR 达 94.2%、专有模型 83.1%，分别超最强基线 23.3% 与 16.8%；GPT-4o 上达 95.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have achieved impressive performance across a variety of multimodal tasks, yet remain vulnerable to targeted adversarial attacks, particularly in black-box settings. In this paper, we propose VCP-Attack, a transferable targeted attack framework that combines structured contrastive supervision with subspace-guided perturbation optimization. Specifically, we employ a dynamic PCA-based projection to constrain perturbations within semantically meaningful low-dimensional subspaces, and design a multi-sample contrastive loss to align adversarial features with target semantics while pushing them away from the source semantics. Extensive experiments on seven open-source and three proprietary LVLMs--including GPT-4o, Claude, and Gemini--show that VCP-Attack achieves state-of-the-art performance in black-box targeted attacks. Under a fixed perturbation budget (epsilon = 16/255), our method achieves an average attack success rate (ASR) of 94.2% on open-source models and 83.1% on proprietary models, surpassing the strongest baselines by 23.3% and 16.8%, respectively. Notably, VCP-Attack achieves a 95.6% ASR on GPT-4o. Comprehensive ablation studies and visualizations further validate the effectiveness of the dynamic subspace projection and semantic contrastive supervision. While evaluated on image captioning, our approach is model-agnostic and exhibits strong potential for broader applications to black-box adversarial settings in vision-language tasks.

</details>

### 26. Safe But Not Robust: Security Evaluation of VLM by Jailbreaking MSTS

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`benchmark`、`targeted image attack`、`VLM safety`、`adversarial evaluation`、`VLM jailbreak`、`Robust-MSTS`

- 🎯 **研究动机**：VLM安全评测缺针对性图像攻击手段
- 🔬 **研究方法**：构建Robust-MSTS基准，以targeted图像扰动评测VLM安全性
- 📌 **结论**：揭示VLM表面安全但对定向扰动不鲁棒

### 27. Understanding and Exploiting Phase Sensitivity for Attacking Large Vision–Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/52.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`phase perturbation`、`LVLM backdoor`、`cross-modal control`、`LVLM`、`phase trigger`

- 🎯 **研究动机**：现有 LVLM 攻击多探索外部对抗引导，利用 LVLM 感知图像的内在模式（相位结构）诱发扰动尚未被研究
- 🔬 **研究方法**：发现 LVLM 对相位感知的图像结构敏感；提出 BadPhase，经数据投毒把对抗相位植入任意图像输入，配合文本触发器与后门扰动开关实现双触发激活，测试时优化降低资源依赖
- 📌 **结论**：在四个主流 LVLM 与三个基准上验证攻击有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Vision-Language Models (LVLMs) have demonstrated remarkable reasoning capabilities across various downstream multimodal tasks, they are proven to be vulnerable to carefully designed adversarial examples. Existing LVLM attackers show that exploring external components of adversarial guidance (e.g., forcing adversarial alignment, resembling harmful features) can help improve adversarial effects. However, leveraging the intrinsic patterns of LVLMs to induce adversarial perturbation generation by exploring how LVLMs perceive images has not been deeply studied. Inspired by the cognitive science, in this paper, we make the first attempt to investigate the interference of adversarial perturbation from the perspectives of image phase, and find that LVLMs are sensitive to the phase-aware image structure. Motivated by this, we propose a novel LVLM attack method called BadPhase with further backdoor designs, to implant adversarial phase as triggers into any image inputs via data poisoning so as to control the LVLMs’ predictions. A textual trigger and a backdoor perturbation switcher are also introduced to activate the malicious behavior only when both triggers are present. The whole backdoor optimization is implemented at the test-time to reduce the resource reliance. Experiments on four popular LVLMs and three benchmarks demonstrate the effectiveness of our proposed method.

</details>

### 28. Adversarial Attack Framework Against Vision-Language Model Unlearning

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7256.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`analysis`、`unlearning recovery`、`visual sink token`、`surrogate-only transfer`、`VLM unlearning`

- 🎯 **研究动机**：对抗输入可操纵已 unlearn 的 VLM 复现被遗忘内容，但多数攻击需要受害者架构、参数或输出 logits 访问
- 🔬 **研究方法**：提出 SISA：只需一个代理预训练 VLM；利用 unlearning 后 visual sink token 的持续性作为稳定结构锚，诱导 sink 建立结构锚再经 sink 条件化注意力做语义对齐，生成可迁移对抗输入
- 📌 **结论**：在多样 unlearned VLM 设定下有效，输出与遗忘目标的语义一致性相比干净输入最多提升 6.9 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision–Language Models (VLMs) unlearning tends to eliminate the influence of “to-beforgotten” content in the training corpora, algorithmically by suppressing the likelihood of faithfully generating responses on forget-target inputs. The injection of adversarial inputs can manipulate the unlearned VLM’s generation towards the attacker’s will, forcing the reproduction of the supposedly forgotten content and undermining the reliability of expected forgetting behavior. However, most attacks assume access to the unlearned VLM’s architecture or parameters, or to output logits via queries. In this paper, we propose SISA, a novel attack framework for crafting adversarial inputs to manipulate generation towards the forgotten target, which only requires access to a surrogate, pretrained VLM. SISA advances prior attacks by exploiting the persistence of visual sink tokens after unlearning as a stable structural anchor for semantic alignment. SISA induces a sink regime on a candidate visual token to build the structural anchor that influences generation, and then semantically aligns model output to the target while conditioning on attention through the induced sink token, reinforcing the anchor for desired elicitation. With sink persistence and sink-conditioned semantic anchoring, SISA crafts transferable adversarial inputs. Evaluation on diverse unlearned VLM settings confirms the effectiveness of SISA, increasing the outputs’ semantic agreement with forgotten targets by up to 6.9× relative to clean inputs.

</details>

### 29. V-Attack: Targeting Disentangled Value Features for Controllable Adversarial Attacks on LVLMs

📄 [arXiv](https://arxiv.org/abs/2511.20223) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Nie_V-Attack_Targeting_Disentangled_Value_Features_for_Controllable_Adversarial_Attacks_on_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`LVLM`、`value feature`、`controllable manipulation`

👤 **作者**：Sen Nie、Jie Zhang、Jianxin Yan、Shiguang Shan、Xilin Chen

- 🎯 **研究动机**：已有 LVLM 对抗攻击受 patch token 语义纠缠限制，无法精确操控图像中特定概念的语义
- 🔬 **研究方法**：发现 attention 块的 value feature 抑制全局上下文、保留高熵解耦的局部语义，V-Attack 以 Self-Value Enhancement 与 Text-Guided Value Manipulation 两模块针对 V 特征实施局部语义攻击
- 📌 **结论**：在 LLaVA、InternVL、DeepseekVL 与 GPT-4o 等上平均 ASR 提升 36%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial attacks have evolved from simply disrupting predictions on conventional task-specific models to the more complex goal of manipulating image semantics on Large Vision-Language Models (LVLMs). However, existing methods struggle with controllability and fail to precisely manipulate the semantics of specific concepts in the image. We attribute this limitation to semantic entanglement in the patch-token representations on which adversarial attacks typically operate: global context aggregated by self-attention in the vision encoder dominates individual patch features, making them unreliable handles for precise local semantic manipulation. Our systematic investigation reveals a key insight: value features (V) computed within the transformer attention block serve as much more precise handles for manipulation. We show that V suppresses global-context channels, allowing it to retain high-entropy, disentangled local semantic information. Building on this discovery, we propose V-Attack, a novel method designed for precise local semantic attacks. V-Attack targets the value features and introduces two core components: (1) a Self-Value Enhancement module to refine V's intrinsic semantic richness, and (2) a Text-Guided Value Manipulation module that leverages text prompts to locate source concept and optimize it toward a target concept. By bypassing the entangled patch features, V-Attack achieves highly effective semantic control. Extensive experiments across diverse LVLMs, including LLaVA, InternVL, DeepseekVL and GPT-4o, show that V-Attack improves the attack success rate by an average of 36% over state-of-the-art methods, exposing critical vulnerabilities in modern visual-language understanding. Our code and data are available https://github.com/Summu77/V-Attack.

</details>

### 30. Medusa: Cross-Modal Transferable Adversarial Attacks on Multimodal Medical Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2511.19257) · 🌐 [Project](https://doi.org/10.1145/3770854.3780277)　📅 2025-11　🏷 KDD 2026

**关键词**：`attack`、`medical MMed-RAG`、`cross-modal transfer`、`retrieval hijacking`、`medical RAG`、`cross-modal attack`

👤 **作者**：Yingjia Shang、…、Yefeng Zheng

- 🎯 **研究动机**：多模态医疗 RAG 经视觉输入扰动的对抗漏洞未被探索
- 🔬 **研究方法**：Medusa 黑盒跨模态可迁移攻击：用 multi-positive InfoNCE loss 把对抗视觉嵌入对齐到医学上合理但恶意的文本目标以劫持检索，结合代理集成与 IRM 增强的双循环优化提升迁移性
- 📌 **结论**：在报告生成与疾病诊断两任务上平均 ASR 超 90%，抗四种主流防御并超越 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid advancement of retrieval-augmented vision-language models, multimodal medical retrieval-augmented generation (MMed-RAG) systems are increasingly adopted in clinical decision support. These systems enhance medical applications by performing cross-modal retrieval to integrate relevant visual and textual evidence for tasks, e.g., report generation and disease diagnosis. However, their complex architecture also introduces underexplored adversarial vulnerabilities, particularly via visual input perturbations. In this paper, we propose Medusa, a novel framework for crafting cross-modal transferable adversarial attacks on MMed-RAG systems under a black-box setting. Specifically, Medusa formulates the attack as a perturbation optimization problem, leveraging a multi-positive InfoNCE loss (MPIL) to align adversarial visual embeddings with medically plausible but malicious textual targets, thereby hijacking the retrieval process. To enhance transferability, we adopt a surrogate model ensemble and design a dual-loop optimization strategy augmented with invariant risk minimization (IRM). Extensive experiments on two real-world medical tasks, including medical report generation and disease diagnosis, demonstrate that Medusa achieves over 90% average attack success rate across various generation models and retrievers under appropriate parameter configuration, while remaining robust against four mainstream defenses, outperforming state-of-the-art baselines. Our results reveal critical vulnerabilities in the MMed-RAG systems and highlight the necessity of robustness benchmarking in safety-critical medical applications. The code and data are available at https://anonymous.4open.science/r/MMed-RAG-Attack-F05A.

</details>

### 31. CHAI: Command Hijacking against Embodied AI

📄 [arXiv](https://arxiv.org/abs/2510.00181) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-10　🏷 SaTML 2026

**关键词**：`attack`、`visual text perturbation`、`embodied LVLM`、`command hijacking`、`environmental prompt injection`、`visual command`

👤 **作者**：Luis Burbano、…、Alvaro A Cardenas

- 🎯 **研究动机**：具身 AI 的多模态语言理解能力带来物理环境间接 prompt 注入新风险
- 🔬 **研究方法**：提出 CHAI：在视觉输入中嵌入误导标志等自然语言指令，系统搜索 token 空间构建 prompt 字典并引导攻击模型生成 Visual Attack Prompts
- 📌 **结论**：在无人机紧急降落、自动驾驶、空中目标跟踪与真实机器人车场景均超 SoTA 攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a physical environment indirect prompt injection attack that exploits the multimodal language interpretation abilities of AI models. CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents: drone emergency landing, autonomous driving, aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

</details>

### 32. DASH: A Meta-Attack Framework for Synthesizing Effective and Stealthy Adversarial Examples

📄 [arXiv](https://arxiv.org/abs/2508.13309) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Al_Nomaan_Nafi_DASH_A_Meta-Attack_Framework_for_Synthesizing_Effective_and_Stealthy_Adversarial_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`attack`、`meta attack`、`stealth`、`adaptive synthesis`

👤 **作者**：Abdullah Al Nomaan Nafi、…、Prabuddha Chakraborty

- 🎯 **研究动机**：Lp 范数约束的对抗样本与人类感知不对齐，感知对齐攻击方法稀少
- 🔬 **研究方法**：提出全可微元攻击框架 DASH：多阶段以学习的自适应权重聚合多种 Lp 基攻击，元损失联合最小化误分类损失与感知失真
- 📌 **结论**：对抗训练模型上 ASR 比 SoTA 感知攻击 AdvAD 高 20.63%，SSIM、LPIPS、FID 全面更优，且对未见防御泛化良好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Numerous techniques have been proposed for generating adversarial examples in white-box settings under strict Lp-norm constraints. However, such norm-bounded examples often fail to align well with human perception, and only a few methods specifically explore perceptually aligned adversarial examples. Moreover, it remains unclear whether insights from Lp-constrained attacks can be effectively leveraged to improve perceptual efficacy. In this paper, we introduce DASH, a fully differentiable meta-attack framework that generates effective and perceptually aligned adversarial examples by strategically composing existing Lp-based attack methods. DASH operates in a multi-stage fashion: at each stage, it aggregates candidate adversarial examples from multiple base attacks using learned, adaptive weights and propagates the result to the next stage. A novel meta-loss function guides this process by jointly minimizing misclassification loss and perceptual distortion, enabling the framework to dynamically modulate the contribution of each base attack throughout the stages. We evaluate DASH on adversarially trained models across CIFAR-10, CIFAR-100, and ImageNet. Despite relying solely on Lp-constrained based methods, DASH significantly outperforms state-of-the-art perceptual attacks such as AdvAD, achieving higher attack success rates (e.g., 20.63% improvement) and superior visual quality, as measured by SSIM, LPIPS, and FID (improvements $\approx$ of 11, 0.015, and 5.7, respectively). Furthermore, DASH generalizes well to unseen defenses, making it a practical and strong baseline for evaluating robustness without requiring handcrafted adaptive attacks for each new defense.

</details>

### 33. SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models

📄 [arXiv](https://arxiv.org/abs/2608.16931)　📅 2026-08

**关键词**：`attack`、`analysis`、`public EEG encoder`、`zero-query transfer`、`private downstream model`、`shared encoder geometry`

👤 **作者**：Linhua Cong、Dingkun Liu、Dongrui Wu

- 🎯 **研究动机**：EEG 基础编码器开放发布方便下游，但使私有下游模型暴露于零查询迁移攻击，该风险未被探索
- 🔬 **研究方法**：SW-ProxyCE 免查询任务感知攻击：经 shrinkage-whitened 类原型从小标注参考集恢复任务级决策几何，无需训练代理分类器，覆盖线性探测与全微调下游
- 📌 **结论**：三任务、四编码器上对抗样本均有效迁移并超过任务无关表征偏移攻击——EEG 基础模型的强迁移性不等于对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Electroencephalography (EEG) foundation models have recently emerged as a promising paradigm for EEG decoding by learning reusable representations from large-scale heterogeneous neural recordings. However, the open release of EEG foundation encoders, while facilitating downstream developments, also introduces a previously unexplored security risk: publicly available representations may make private downstream models vulnerable. This paper investigates adversarial transfer attacks in EEG foundation model deployment in a public-encoder and private-downstream setting, where attackers have white-box access to a released encoder and a small task-matched labeled reference set, but no access or query to victim parameters, outputs, or gradients. We propose Shrinkage-Whitened Proxy Cross-Entropy (SW-ProxyCE), a query-free task-aware attack framework that recovers task-level decision geometry from a small labeled reference set through shrinkage-whitened class prototypes, enabling transferable adversarial generation without training an additional surrogate classifier. We evaluated SW-ProxyCE across three EEG tasks using three general-purpose foundation encoders and a paradigm-specific pre-trained encoder, covering both linear-probing and full-fine-tuning downstream models in cross-subject and within-subject scenarios. Results demonstrated that adversarial examples generated from the public encoder and limited labeled references can effectively transfer to inaccessible downstream models. SW-ProxyCE consistently outperformed task-agnostic representation-shift attacks, revealing that the strong transferability of EEG foundation models does not necessarily lead to adversarial robustness. Our code will be available on GitHub.

</details>

### 34. Attacker’s Noise Can Manipulate Your Audio-based LLM in the Real World

🎓 [Official](https://aclanthology.org/2026.eacl-long.66/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`over-the-air noise`、`target action`、`bystander impact`、`audio-language model`、`over-the-air perturbation`

👤 **作者**：Vinu Sankar Sadasivan、Soheil Feizi、Rajiv Mathews、Lun Wang

- 🎯 **研究动机**：音频 LLM（如 Qwen2-Audio）在现实物理场景中的漏洞未被研究
- 🔬 **研究方法**：构造隐蔽音频扰动操纵 ALLM 产生目标行为（响应唤醒词、触发修改日历等有害操作），或在用户交互时播放对抗背景噪声降低回复质量，攻击可经空气传播
- 📌 **结论**：攻击可扩展到真实场景并波及无辜旁听用户，具有跨模型迁移性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper investigates the real-world vulnerabilities of audio-based large language models (ALLMs), such as Qwen2-Audio. We first demonstrate that an adversary can craft stealthy audio perturbations to manipulate ALLMs into exhibiting specific targeted behaviors, such as eliciting responses to wake-keywords (e.g., “Hey Qwen”), or triggering harmful behaviors (e.g., “Change my calendar event”). Subsequently, we show that playing adversarial background noise during user interaction with the ALLMs can significantly degrade the response quality. Crucially, our research illustrates the scalability of these attacks to real-world scenarios, impacting other innocent users when these adversarial noises are played through the air. Further, we discuss the transferability of the attack and potential defensive measures.

</details>

### 35. TSFAdv: Frequency-Guided Black-Box Adversarial Attacks on Time Series Forecasting

🎓 [Official](https://icml.cc/virtual/2026/poster/66215)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Qizhuo Han、Xiangrui Cai、Sihan Xu、Ying Zhang、Zheli Liu

- 🎯 **研究动机**：长时序预测（LTSF）模型以黑盒 API 部署于智能电网等关键基础设施，其安全漏洞基本未被研究
- 🔬 **研究方法**：提出 TSFAdv：分析频域幅值与相位扰动敏感性，把频域先验嵌入自然进化策略实现敏感度引导的梯度估计，并用 DTW 与 SME 的轨迹级评估协议
- 📌 **结论**：200 次查询预算下七个 SOTA 架构上 DTW 中位提升 38.78%、SME 提升 26.47%，且现有防御对频域操纵无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While deep neural network-based long-term time series forecasting (LTSF) has become indispensable for critical infrastructures such as smart grids and IoT platforms, the deployment of these models as black-box APIs introduces severe security vulnerabilities that remain largely underexplored. In this paper, we propose TSFAdv, a query-efficient adversarial framework for LTSF models. The framework systematically analyzes model sensitivity to spectral perturbations in both magnitude and phase of the frequency domain. By embedding frequency-domain priors into Natural Evolution Strategies, we achieve sensitivity-guided gradient estimation that improves perturbation efficacy without violating practical query constraints. To overcome ambiguities inherent to point-wise regression metrics, we adopt a trajectory-level evaluation protocol based on Dynamic Time Warping (DTW) and Slope Misalignment Error (SME), enabling the capture of complex geometric and directional deviations. Extensive experiments across seven state-of-the-art architectures demonstrate that TSFAdv achieves substantial performance gains, with median DTW improvements of 38.78\% and median SME improvements of 26.47\% under 200-query budget. These findings reveal that existing defense mechanisms are ineffective against frequency-domain manipulation, underscoring an urgent necessity for robust LTSF models.

</details>

### 36. Speech-Audio Compositional Attacks on Multimodal LLMs and Their Defense with SALMONN-Guard

🎓 [Official](https://icml.cc/virtual/2026/poster/64737)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`VLM safety`、`adversarial example`、`evasion attack`、`adversarial attack`、`empirical evaluation`

👤 **作者**：Yudong Yang、…、Chao Zhang

- 🎯 **研究动机**：现有音频攻击依赖噪声优化或白盒访问，语音与音频复杂组合输入下的安全风险未被现有防护覆盖
- 🔬 **研究方法**：提出 SACRED-Bench，用语音重叠、多人对话与语音非语音混合三种组合机制做黑盒红队；并提出联合检查语音、音频与文本的 SALMONN-Guard
- 📌 **结论**：Gemini 2.5 Pro 满开护栏下 ASR 仍达 66%，SALMONN-Guard 将其降至 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in large language models (LLMs) has enabled understanding of both speech and non-speech audio, but has also exposed new safety risks arising from complex audio inputs that are inadequately handled by current safeguards. We introduce SACRED-Bench (Speech–Audio Composition for RED-teaming) to evaluate the robustness of LLMs under complex audio-based attacks. Unlike existing perturbation-based methods that rely on noise optimization or white-box access, SACRED-Bench exploits speech–audio composition to enable effective black-box attacks. SACRED-Bench adopts three composition mechanisms: (a) speech overlap, (b) multi-speaker dialogue, and (c) mixtures of speech and non-speech audio. These mechanisms focus on evaluating safety in settings where benign and harmful intents co-occur within a single auditory scene. Moreover, questions in SACRED-Bench are designed to implicitly refer to content in the audio, such that no explicit harmful information appears in the text prompt alone. Experiments demonstrate that even Gemini 2.5 Pro, a state-of-the-art proprietary LLM with safety guardrails fully enabled, still exhibits a 66% attack success rate. To bridge this gap, we propose SALMONN-Guard, the first guard model that jointly inspects speech, audio, and text for safety judgments, reducing the attack success rate to 20\%. Our results highlight the need for audio-aware defenses to ensure the safety of multimodal LLMs.

</details>

### 37. SoundBreak: A Systematic Study of Audio-Only Adversarial Attacks on Trimodal Models

🌐 [Project](https://aafiya-h.github.io/soundbreak/) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1275/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`adversarial robustness`、`adversarial example`、`evasion attack`、`high-risk deployment`、`failure mitigation`

👤 **作者**：Aafiya Shamshad Hussain、Gaurav Srivastava、Alvi Md Ishmam、Zaber Ibn Abdul Hakim、Chris Thomas

- 🎯 **研究动机**：音视频语言三模态模型对仅音频对抗操纵的鲁棒性认识不足，该现实威胁模型未被系统研究
- 🔬 **研究方法**：研究无目标仅音频攻击，分析针对音频编码器表征、跨模态注意力、隐状态与输出似然等 6 种攻击目标，在 4 个 SOTA 模型上评测并引入房间脉冲响应建模
- 📌 **结论**：仅音频扰动最高达 96% ASR，低感知失真（LPIPS ≤ 0.08）与环境变换下仍有效；跨模型迁移有限，Whisper 强失真下 ASR 超 97%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal foundation models that integrate audio, vision, and language achieve strong performance on reasoning and generation tasks, yet their robustness to adversarial manipulation remains poorly understood. We study a realistic and underexplored threat model: untargeted, audio-only adversarial attacks on trimodal audio–video–language models. We analyze six complementary attack objectives that target different stages of multimodal processing, including audio encoder representations, cross-modal attention, hidden states, and output likelihoods. Across four state-of-the-art models and multiple benchmarks, we show that audio-only perturbations can induce severe multimodal failures, achieving up to 96% attack success rate. We further show that attacks can be successful at low perceptual distortions (LPIPS ≤ 0.08, SI-SNR ≥ 0 dB) and benefit more from extended optimization than increased data scale. We evaluate the feasibility of these attacks under physically realistic conditions by incorporating room impulse response (RIR) modeling, showing that audio-only perturbations remain effective under environmental transformations and thus highlight the practical risk of single-modality attacks in real-world multimodal systems. Transferability across models and encoders remains limited, while speech recognition systems such as Whisper primarily respond to perturbation magnitude, achieving >97% attack success under severe distortion. These results expose a previously overlooked single-modality attack surface in multimodal systems and motivate defenses that enforce cross-modal consistency. Our project website is available at https://aafiya-h.github.io/soundbreak/.

</details>

### 38. Ripple Perturbations Through Structure: Likelihood-Constrained Adversarial Attacks on Heterogeneous Tabular Data

🎓 [Official](https://icml.cc/virtual/2026/poster/60737)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Zhengjie Zhou、Jiahuan Yan、Boqun Ma、Weiwei Feng、Tengfei LIU、Weiqiang Wang

- 🎯 **研究动机**：表格数据的异构特征与非对称依赖使真实对抗样本难生成，手工约束常产生统计合理但语义不一致的扰动并因梯度掩蔽停滞
- 🔬 **研究方法**：提出 LCSA：用异构神经结构因果模型集合推断依赖，引入结构感知涟漪机制将更新沿依赖下游传播，作为结构预条件子缓解梯度掩蔽
- 📌 **结论**：在 50 组评测配置中的 45 组超过 SOTA 基线，对抗样本结构一致性与迁移性更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generating realistic adversarial examples for tabular data remains challenging due to heterogeneous feature types and asymmetric inter-feature dependencies. Existing approaches typically rely on handcrafted constraints or undirected similarity criteria to delimit the feasible attack region, which often fail to capture the structural dependency governing tabular generation. Consequently, standard attacks typically produce perturbations that are statistically likely yet semantically inconsistent and prone to optimization stagnation via gradient masking. To address this, we propose LCSA, a white-box framework that formulates adversarial generation as optimization over structurally admissible perturbations. LCSA leverages an ensemble of heterogeneous neural Structural Causal Models to infer dependencies and introduces a structure-aware ripple mechanism. Unlike attacks that perturb features in isolation, this mechanism propagates updates downstream, acting as a structural preconditioner that conditions gradient flow to mitigate masking effects. Extensive experiments demonstrate that LCSA outperforms state-of-the-art baselines in 45 of 50 evaluated configurations, yielding adversarial examples with superior structural consistency and transferability.

</details>

### 39. Hearing Without Noticing? Attention-Aware Stealthy Black-Box Adversarial Audio Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/63275)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Tianyi Xu、Cheng&amp、#x27、an Wei、Yue Zhao、Kai Chen

- 🎯 **研究动机**：已有对抗音频只最小化扰动幅度，物理世界黑盒 ASR 下隐蔽性不足
- 🔬 **研究方法**：提出首个音乐载体选择算法与注意力感知隐蔽性损失生成对抗样本
- 📌 **结论**：五个商业 ASR API 与三个语音助手上效果与隐蔽性超 SOTA；200 人研究中 55.6% 将物理对抗样本视为良性音频，比现有方法高逾 20%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Automatic Speech Recognition (ASR) systems, such as those in intelligent assistants, are vulnerable to adversarial examples (AEs). Benign audio clips like music, when embedded with small perturbations, can trick ASR models into recognizing attacker-specified commands. Prior studies focus on minimizing perturbation magnitude to craft AEs. However, they fails to achieve high attack stealthiness against black-box ASR systems in the physical world. In this paper, we introduce the first music carrier selection algorithm and an attention-aware stealthiness loss function to generate stealthy AEs. Extensive evaluations on five commercial ASR APIs and three widely-used voice assistants demonstrate that our method significantly outperforms state-of-the-art techniques in both effectiveness and stealthiness. Notably, in a user study involving 200 participants, 55.6\% of participants perceived our physical adversarial examples as benign audio, which is an improvement of over 20\% compared to existing methods.

</details>

### 40. Exposing Vulnerabilities in Explanation for Time Series Classifiers via Dual-Target Attacks

📄 [arXiv](https://arxiv.org/abs/2602.02763) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66770)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`attack`、`adversarial example`、`evasion attack`、`robustness degradation`、`adversarial attack`

👤 **作者**：Bohan Wang、…、Wei Jin

- 🎯 **研究动机**：时间序列系统把解释的时间一致性当鲁棒性证据，该假设可被对抗性打破
- 🔬 **研究方法**：TSEF 双目标攻击联合操纵分类器与解释器输出：实现定向误分类同时让解释保持与参考理由一致
- 📌 **结论**：跨数据集与解释器骨干一致证明解释稳定性是决策鲁棒性的误导性代理，需耦合感知的鲁棒性评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Interpretable time series deep learning systems are often assessed by checking temporal consistency on explanations, implicitly treating this as evidence of robustness. We show that this assumption can fail: Predictions and explanations can be adversarially decoupled, enabling targeted misclassification while the explanation remains plausible and consistent with a chosen reference rationale. We propose TSEF (Time Series Explanation Fooler), a dual-target attack that jointly manipulates the classifier and explainer outputs. In contrast to single-objective misclassification attacks that disrupt explanation and spread attribution mass broadly, TSEF achieves targeted prediction changes while keeping explanations consistent with the reference. Across multiple datasets and explainer backbones, our results consistently reveal that explanation stability is a misleading proxy for decision robustness and motivate coupling-aware robustness evaluations for trustworthy time series tasks.

</details>

### 41. On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses

📄 [arXiv](https://arxiv.org/abs/2506.02978) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`tabular foundation model`、`test-time evasion`、`in-context defense`

👤 **作者**：Mohamed Djilani、…、Mike Papadakis

- 🎯 **研究动机**：表格基础模型的测试时对抗鲁棒性未明
- 🔬 **研究方法**：系统评测test-time攻击并提出in-context防御
- 📌 **结论**：揭示脆弱性并验证上下文防御有效性

### 42. GRASP: Hard-Label Black-Box Malware Evasion with Higher Success, Fewer Queries, and Smaller Perturbations

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/6149.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`malware detector`、`hard-label evasion`、`query efficiency`

- 🎯 **研究动机**：硬标签黑盒下 PE 恶意软件对抗攻击查询效率低且文件膨胀大：组合空间大的原子扰动难探索，移植良性片段含大量无关字节
- 🔬 **研究方法**：GRASP 三阶段：Gumbel-Softmax 梯度种子预热、带紧凑高效用扰动库的 RL 精化、扰动最小化剪除冗余字节
- 📌 **结论**：以更少查询和更小文件膨胀取得更高攻击成功率，对商业杀毒引擎同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML)-based malware detectors are widely deployed but remain vulnerable to adversarial attacks. However, under hard-label black-box access, existing adversarial attacks on Windows Portable Executable (PE) malware are often query-inefficient and incur large file-size inflation. A common paradigm is to predefine a set of semantics-preserving atomic perturbations and search for evasive combinations under only binary feedback. Among these atomic perturbations, (i) those with highly combinatorial search spaces are difficult to explore effectively under hard-label feedback, leaving their potential untapped, and (ii) those relying on transplanting benign fragments are often laden with evasion-irrelevant bytes and exhibit highly variable adversarial utility. We propose Gradient-seeded Reinforcement Learning And Stealthy Pruning (GRASP), a three-stage framework that tackles these challenges. First, we decouple perturbations with highly combinatorial search spaces from the query-based search and instead apply a gradient-seeded warm-up that uses Gumbel-Softmax relaxation to enable gradientbased updates over the discrete space. This yields a strong warm start that improves evasion and reduces queries in later stages. Second, Reinforcement Learning (RL)-based refinement is accelerated by a perturbation library that filters, caches, and reuses compact high-utility patterns, reducing wasted queries on low-utility benign fragments. Third, a perturbation minimization stage removes redundant bytes while preserving evasion, reducing size inflation and feeding compact patterns back to the library. Experiments show that GRASP outperforms baselines, achieving higher attack success with fewer queries and smaller file-size inflation. We additionally demonstrate its practical effectiveness against commercial Antivirus engines. ∗ Corresponding author. J. Ning is also with the Zhejiang Key Laboratory of Digital Fashion and Data Governance, Zhejiang SciTech University and with the Faculty of Data Science, City University of Macau, Macau.

</details>

### 43. LBA: Textual Hard-Label Adversarial Attack Under Low Query Budgets

📄 [arXiv](https://arxiv.org/abs/2607.14101) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3591.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`text classifier`、`hard-label access`、`low-query search`

👤 **作者**：Shixin Guo、…、Hao Peng

- 🎯 **研究动机**：硬标签低预算下贪心逐位替换的局部搜索易漏高质量对抗样本且查询开销大
- 🔬 **研究方法**：LBA 采样式方法融合先验与后验知识构建高质量对抗样本近似分布，随采样推进迭代更新分布引导搜索
- 📌 **结论**：小到大规模六个语言模型、四个数据集上全面超 SOTA，生成文本语义保持与可读性更好

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Generating high-quality adversarial texts with low query budgets remains a challenging problem in the hard-label scenario. Most existing approaches rely on greedy algorithms, where one position in the text is selected for substitution, followed by the substitutions of other positions. This local search approach may fail to discover high-quality adversarial examples and often leads to excessive query costs. Ideally, an optimal adversarial sample would consider all possible position combinations in the text, but exhaustive search is computationally impractical. To address this challenge, we propose a sampling-based method called LBA, which constructs an approximate distribution of high-quality adversarial examples by integrating both prior and posterior knowledge, and utilizes this distribution for sampling. As sampling progresses, posterior knowledge updates the approximate distribution, which in turn guides more effective sampling. Extensive experiments on six language models, ranging from small-scale to large-scale architectures across four datasets, demonstrate that LBA significantly outperforms state-of-the-art baselines on all evaluation metrics. Additionally, LLM-based assessment indicates that LBA generates more semantically preserved and comprehensible adversarial texts.

</details>

### 44. CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents

📄 [arXiv](https://arxiv.org/abs/2608.21114)　📅 2026-08

**关键词**：`attack`、`visual world model`、`online observation attack`、`temporal coherence`、`visual world-model agent`、`value-subspace perturbation`

👤 **作者**：Jiancheng Wang、…、Dacheng Tao

- 🎯 **研究动机**：视觉 world-model agent（如 DreamerV3）经循环潜在状态行动，逐帧观测攻击被削弱，且严格逐帧扰动约束下扰动随时间剧烈变化
- 🔬 **研究方法**：CIVA 白盒在线攻击：发现 critic 引导扰动集中于受害者自身 critic 诱导的低维子空间，离线用 critic-guided PGD+SVD 提取低秩 value 子空间，在线仅优化子空间系数并做 EMA 平滑后映射回像素
- 📌 **结论**：在 DMC walker walk、Atari Pong、Crafter 上稳定优于五种近期方法；walker walk 上 reward 降幅最大达 26.07%，且 TempAbs 仅 0.646，时序变化低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual world-model agents such as DreamerV3 act through a recurrent latent state rather than a single observation, which weakens frame-wise observation attacks and makes their perturbations vary sharply over time under a strict per-frame perturbation constraint. We study white-box, causal, online attacks on such agents and propose Critic-Induced Value-Subspace Attacks (\textbf{CIVA}). Our key observation is that, along a rollout, critic-guided perturbations concentrate in a low-dimensional subspace induced by the victim's own critic. Based on this observation, CIVA first probes the frozen victim offline with critic-guided PGD and extracts a low-rank value-subspace by SVD. At test time, it optimizes only the subspace coefficients, smooths them with an exponential moving average (EMA), and maps them back to pixels. This design attacks value-sensitive recurrent dynamics while keeping the online optimization cheap and temporally coherent. Extensive experiments on DMC walker walk, Atari Pong, and Crafter show that CIVA consistently outperforms five recent methods; on DMC walker walk, it achieves the largest reward drop of 26.07\% while keeping temporal variation low, with TempAbs of 0.646.

</details>

### 45. BRP: Query-Efficient Block Revert Patch for Decision-Based Black-Box Adversarial Attack

🌐 [Project](https://doi.org/10.1145/3770855.3818133)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`black-box adversarial attack`、`query efficiency`、`patch search`

- 🎯 **研究动机**：决策式黑盒（仅见预测标签）下的对抗补丁攻击探索不足，现有方法查询效率低且需大补丁面积
- 🔬 **研究方法**：BRP 把补丁生成形式化为像素块回退问题：滑动窗口逐块回退测试收集保持对抗效果的块，再全局搜索最优组合缩小补丁，两阶段粗到细交替精炼
- 📌 **结论**：相比 SOTA 决策式攻击显著减少补丁尺寸与查询成本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial patches pose a serious threat to deep neural networks, as small localized perturbations can decisively control model predictions. In real-world deployments, the decision-based black-box setting is the most realistic and challenging threat model, where attackers observe only the predicted labels. Designing adversarial patch attacks under this setting is of substantial real-world significance for rigorously testing model robustness under realistic black-box conditions. However, adversarial patch attacks in the decision-based setting remain largely underexplored. Existing methods often suffer from low query efficiency and require large patch areas, which significantly limit their practical applicability. We propose Block Revert Patch (BRP), a novel reverse construction method for query-efficient adversarial patch generation. Instead of adding perturbations, BRP formulates patch generation as a pixel-block reversion problem and employs a two-stage process to progressively refine the patch. Specifically, the single-block revert test stage uses a sliding window to temporarily revert individual blocks and collect those whose reversion maintains the adversarial effect. The global revert optimization stage then searches for an optimal combination of pixel-blocks from this set, further reducing the patch size. By iteratively alternating between these two stages, BRP progressively refines the patch in a coarse-to-fine manner. Experiments show that BRP significantly reduces patch size and query cost compared to state-of-the-art decision-based attacks, offering a strong and practical approach for evaluating model vulnerability in adversarial settings.

</details>

### 46. Out of Sight, Out of Track: Adversarial Attacks on Propagation-based Multi-Object Trackers via Query State Manipulation

📄 [arXiv](https://arxiv.org/abs/2604.00452) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Bouzidi_Out_of_Sight_Out_of_Track_Adversarial_Attacks_on_Propagation-based_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`attack`、`multi-object tracking`、`query-state manipulation`、`temporal evasion`

👤 **作者**：Halima Bouzidi、Haoyu Liu、Yonatan Gizachew Achamyeleh、Praneetsai Vasu Iddamsetty、Mohammad Abdullah Al Faruque

- 🎯 **研究动机**：查询传播式多目标跟踪的架构漏洞未被探索
- 🔬 **研究方法**：FADE 两策略：时序查询洪泛耗尽查询预算迫使终止有效轨迹；时序记忆腐蚀经状态去相关切断时序链并擦除特征身份；可微管线结合传感器欺骗仿真优化物理可实现性
- 📌 **结论**：在 MOT17 与 MOT20 上对 SOTA TBP 跟踪器造成大量身份切换与轨迹终止

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent Tracking-by-Query-Propagation (TBP) methods have advanced Multi-Object Tracking (MOT) by enabling end-to-end (E2E) pipelines with long-range temporal modeling. However, this reliance on query propagation introduces unexplored architectural vulnerabilities to adversarial attacks. We present FADE, a novel attack framework designed to exploit these specific vulnerabilities. FADE employs two attack strategies targeting core TBP mechanisms: (i) Temporal Query Flooding: Generates spurious temporally consistent track queries to exhaust the tracker's limited query budget, forcing it to terminate valid tracks. (ii) Temporal Memory Corruption: Directly attacks the query updater's memory by severing temporal links via state de-correlation and erasing the learned feature identity of matched tracks. Furthermore, we introduce a differentiable pipeline to optimize these attacks for physical-world realizability by leveraging simulations of advanced perception sensor spoofing. Experiments on MOT17 and MOT20 benchmarks demonstrate that FADE is highly effective against state-of-the-art TBP trackers, causing significant identity switches and track terminations.

</details>

### 47. On the existence of consistent adversarial attacks in high-dimensional linear classification

📄 [arXiv](https://arxiv.org/abs/2506.12454) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64252)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Matteo Vilucchio、Lenka Zdeborová、Bruno Loureiro

- 🎯 **研究动机**：对抗攻击与模型表达力不足或有限数据导致误分类的本质区别缺乏理论刻画
- 🔬 **研究方法**：在高维二分类提出量化保标签一致攻击脆弱性的新误差度量，给出良指定与潜空间模型的精确渐近刻画
- 📌 **结论**：过参数化使模型对保标签扰动更脆弱，为对抗敏感性机制提供理论解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

What fundamentally distinguishes an adversarial attack from a misclassification due to limited model expressivity or finite data? In this work, we investigate this question in the setting of high-dimensional binary classification, where statistical effects due to limited data availability play a central role. We introduce a new error metric that precisely capture this distinction, quantifying model vulnerability to consistent adversarial attacks --- perturbations that preserve the ground-truth labels. Our main technical contribution is an exact and rigorous asymptotic characterization of these metrics in both well-specified models and latent space models, revealing different vulnerability patterns compared to standard robust error measures. The theoretical results demonstrate that as models become more overparameterized, their vulnerability to label-preserving perturbations grows, offering theoretical insight into the mechanisms underlying model sensitivity to adversarial attacks.

</details>

### 48. MoCo-EA: Exploiting Adversarial Mode Connectivity for Efficient Evolutionary Attacks

📄 [arXiv](https://arxiv.org/abs/2605.18919) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64071)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Hyo Seo Kim、Gang Luo、Can Chen、Binghui Wang、Yue Duan、Ren Wang

- 🎯 **研究动机**：进化攻击的交叉操作经离散插值破坏对抗性质、效率低
- 🔬 **研究方法**：MoCo-EA 发现对抗样本位于连通流形，用 Bézier 交叉算子沿父代扰动间的连续 Bézier 曲线优化
- 📌 **结论**：优化路径中间点迁移性高于端点，Bézier 交叉大幅优于离散遗传操作并降低收敛时间与查询需求

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Evolutionary algorithms for adversarial attacks leverage population-based search to discover perturbations without gradient information, but suffer from inefficient crossover operations that destroy adversarial properties through discrete interpolation. We introduce Mode Connectivity Evolutionary Attack (MoCo-EA), which replaces traditional crossover with a novel Bézier crossover operator that optimizes perturbations along a continuous Bézier curve between parent perturbations. Our key insight is that adversarial examples lie on connected manifolds where intermediate points maintain and often enhance attack effectiveness. We demonstrate three findings: (1) Successful adversarial perturbations exhibit mode connectivity; (2) Intermediate points along optimized paths achieve higher transferability than endpoints; (3) Bézier crossover dramatically outperforms discrete genetic operations while reducing convergence time and query requirements. By exploiting the geometric structure of adversarial space through path optimization, MoCo-EA provides an efficient and reliable method. Our work challenges the traditional view of adversarial examples as isolated points and opens new directions for both attack generation and defense research.

</details>

### 49. MEDUSA: Motion Elimination in Diffusion Using Spectral Attack

🎓 [Official](https://icml.cc/virtual/2026/poster/66572)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`diffusion model`、`adversarial example`、`evasion attack`、`adversarial attack`、`attack transferability`

👤 **作者**：Hongwei Yu、…、Jiansheng Chen

- 🎯 **研究动机**：视频扩散模型时空先验鲁棒，帧级攻击只产生表层伪影难抑制运动语义合成
- 🔬 **研究方法**：发现静态视频表现为时间注意力矩阵秩 1 退化的 temporal rank collapse；MEDUSA 最小化注意力矩阵核范数诱导坍塌，规避刚性时间映射的梯度消失
- 📌 **结论**：谱约束有效冻结视频运动，攻击效果优异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the widespread application of Video Diffusion Models (VDMs), video synthesis has achieved remarkable temporal dynamics. Image-to-Video (I2V) generation allows users to provide reference images, which enables attackers to inject adversarial noise into these conditions. Due to the robust spatio-temporal priors in VDMs, conventional frame-level attacks merely induce superficial artifacts and struggle to suppress the synthesis of motion semantics. In this work, we approach the problem by exploring the underlying mechanism of temporal dynamics. We reveal that the static video manifests as a temporal rank collapse, a degenerate state characterized by rank-1 degeneracy within the temporal attention matrix. Guided by this insight, we propose Motion Elimination in Diffusion Using Spectral Attack (MEDUSA) to freeze the video. It minimizes the nuclear norm of the attention matrix to induce the temporal rank collapse. This objective circumvents the vanishing gradient problem encountered when directly imposing a rigid temporal mapping on the attention matrix. Furthermore, we provide a mathematical analysis of this phenomenon and the gradient vanishing problem during the optimization. Experiments confirm that MEDUSA achieves excellent performance and validates the effectiveness of spectral constraints.

</details>

### 50. Low-Rank and Sparsity Are All You Need: Exploring Robust Hierarchical Latent Subspaces for Transferable Adversarial Attack

🎓 [Official](https://icml.cc/virtual/2026/poster/65377)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`adversarial example`、`empirical evaluation`、`attack transferability`

👤 **作者**：Shuangshuang Pu、Wen Yang、Min Li、guodong liu、Chris Ding、Di Ming

- 🎯 **研究动机**：直接操纵稠密冗余特征易过拟合代理模型；SVD 低秩攻击单层单梯度路径忽略层级异质性
- 🔬 **研究方法**：LRS-Attack 低秩分量捕主导语义方向、稀疏分量捕局部判别模式，暖启动交替低秩近似加层级鲁棒专家混合引导梯度
- 📌 **结论**：ImageNet 上跨 CNN/ViT 架构与防御设定的黑盒迁移性一致超 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial examples pose serious threats to deep neural networks, exposing fundamental vulnerabilities in model robustness. However, most existing adversarial attacks directly manipulate dense and redundant feature representations, often leading to overfitting on surrogate models and poor black-box transferability. Recent SVD-based attack attempts to exploit low-rank feature subspaces, yet its reliance on single-layer optimization and single-gradient pathway neglects structural redundancy in feature representations and hierarchical heterogeneity across layers. To address these limitations, we propose LRS-Attack, a low-rank and sparse decomposition attack that explicitly models robust hierarchical subspaces in latent feature spaces. Specifically, the low-rank component captures dominant semantic directions, while the sparse component captures localized and discriminative patterns. To efficiently extract low-rank structure while preserving subspace fidelity, we develop a warm-started alternating low-rank approximation algorithm. Moreover, we introduce a hierarchical mixture of robust experts that leverages depth-dependent feature characteristics and guides gradient optimization toward more transferable adversarial directions. Extensive experiments on ImageNet show that LRS-Attack consistently improves black-box transferability over state-of-the-art methods across diverse CNN/ViT architectures and defense settings. Code is available at https://github.com/AdvML-Group/LRS-Attack.

</details>

### 51. Low-Cost Hard-Label Adversarial Attack with Theoretical Foundations

📄 [arXiv](https://arxiv.org/abs/2601.14300) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/liu-jun)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`hard-label model`、`decision boundary`、`adversarial robustness`、`query efficiency`

👤 **作者**：Jun Liu、Leo Yu Zhang、Fengpeng Li、Isao Echizen、Jiantao Zhou

- 🎯 **研究动机**：现有硬标签攻击忽视初始化作用且依赖经验启发、缺理论保证
- 🔬 **研究方法**：统一理论框架证明符号翻转类攻击是真实梯度符号的近似；提出零查询初始化与 Pattern-Driven Optimization，理论保证更高余弦相似度与更低查询复杂度
- 📌 **结论**：CIFAR-10、ImageNet、ObjectNet 等上成功率和效率超 SOTA（低预算尤甚），绕过 Blacklight 防御检出率为 0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hard-label black-box attacks, relying solely on top-1 predictions, represent one of the most challenging yet practically threat models. Despite recent progress, existing approaches face two key limitations: (1) they overlook the critical role of initialization, focusing primarily on optimization strategies; and (2) they rely heavily on empirical heuristics without theoretical guarantees. To bridge this gap, we establish a unified theoretical framework showing that existing sign-flipping hard-label attacks can be understood as approximating the true gradient sign. Guided by this {principled analysis}, we propose a novel attack framework featuring a zero-query initialization strategy and a Pattern-Driven Optimization (PDO) algorithm. We provide theoretical guarantees that our initialization yields higher cosine similarity to the true gradient sign than random baselines, and our PDO module achieves significantly lower query complexity than baseline search methods. Extensive experiments across CIFAR-10, ImageNet, and ObjectNet—covering standard and adversarially trained models, commercial APIs, and CLIP models—demonstrate that our method consistently outperforms SOTA hard-label attacks in both success rate and efficiency, particularly under low query budgets. Furthermore, our method demonstrates robust generalization across corrupted data (ImageNet-C), biomedical images (PathMNIST), and dense prediction tasks such as segmentation. Notably, it bypasses the stateful defense Blacklight, achieving a 0% detection rate.

</details>

### 52. Budget-Efficient Attacks and Robustness Training for Cooperative MARL

🌐 [Project](https://anonymous.4open.science/r/BHEA-068D) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62076)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial robustness`、`adversarial example`、`evasion attack`、`adversarial attack`、`adversarial training`

👤 **作者**：Junyong Jiang、Xin Yuan、Longhe Lin、Songze Li、Lu Dong

- 🎯 **研究动机**：协作 MARL 即使少数时间步被劫持也脆弱；显式攻击预算下现有攻击难以精确暴露协调弱点且训练成本高
- 🔬 **研究方法**：BHEA 预算分层攻击把何时与劫持哪些 agent 的决策同动作替换分离，有限攻击机会下更精确发现漏洞，并用于鲁棒训练
- 📌 **结论**：SMAC 上同预算下攻击更强，训练出的策略对限步动作劫持鲁棒性提升且开销降低

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cooperative multi-agent reinforcement learning (CMARL) policies are vulnerable to action hijacking even when only a few timesteps are compromised. Recent adversarial attacks and adversarial training methods have been explored, but under an explicit attack budget, existing attacks often fail to accurately expose critical coordination weaknesses and incur substantial training cost. We propose Budgeted Hierarchical Efficient Attack (BHEA), a budgeted hierarchical adversarial attack that separates decisions on when and which agents to hijack from action replacement, enabling more precise vulnerability discovery under limited attack opportunities. We further show that training cooperative policies against BHEA substantially improves robustness to limited-step action hijacking while reducing training overhead. Experiments on the StarCraft Multi-Agent Challenge (SMAC) demonstrate stronger attacks under the same attack budget and improved robustness. Code is available at https://anonymous.4open.science/r/BHEA-068D.

</details>

### 53. Bias in Zeroth-Order Normal Estimation for Decision-Based Attacks

🎓 [Official](https://icml.cc/virtual/2026/poster/65667)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial example`、`evasion attack`、`robustness degradation`、`adversarial attack`、`empirical evaluation`

👤 **作者**：Feiyang Wang、Hangwei Qian、Xingquan Zuo、Gang Chen、Ivor Tsang

- 🎯 **研究动机**：决策式攻击的零阶法向估计在异质输入敏感度下，低敏坐标更新被初始化与采样噪声淹没，无法得到 l2 最优扰动
- 🔬 **研究方法**：把 ZO 精炼建模为随机动力系统并证明平稳态坐标幅值编码局部敏感度排序；SAR 据此从当前最优扰动推断重要性图，粗到细地抑制低重要区域
- 📌 **结论**：扰动范数、攻击成功率与视觉不可感知性一致提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Decision-based image attacks commonly rely on zeroth-order (ZO) Monte Carlo probing to estimate decision-boundary normals and iteratively refine adversarial perturbations to minimize the $\ell_2$ norm. We theoretically analyze and empirically demonstrate an intrinsic inefficiency arising from heterogeneous input sensitivity, where only a small subset of coordinates strongly affects the target model’s predictions. Empirically, with one-bit feedback and a limited query budget, updates on low-sensitivity coordinates are overwhelmed by initialization and sampling noise, preventing their perturbations from exhibiting consistent improvement. By modeling ZO refinement as a stochastic dynamical system, we formally characterize its asymptotic behavior: the optimization enters a stationary regime, where the perturbation aligns (in expectation) with the normal and its coordinate-wise magnitudes encode a local sensitivity ranking. However, this stationarity does not generally yield $\ell_2$-optimal perturbations under nonlinear boundaries. Building on this observation, we propose a novel and effective algorithm, Sensitivity-Aware Rescaling (SAR), that leverages this sensitivity signal to infer an importance map from the current best perturbation, then progressively suppresses low-importance regions through a coarse-to-fine schedule to reduce the $\ell_2$ norm. Extensive experiments show that SAR achieves consistent improvements in perturbation norm, attack success rate, and visual imperceptibility. The code is available at https://github.com/Flyingssheep/SAR.

</details>

### 54. Adversarial Vulnerability from Interference Between Features in Superposition

🎓 [Official](https://icml.cc/virtual/2026/poster/62594)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial attack`、`adversarial robustness`、`cyber misuse`、`mechanistic analysis`、`attack transferability`

👤 **作者**：Edward Stevinson、Lucas Prieto、Melih Barsbey、Tolga Birdal

- 🎯 **研究动机**：现有对抗样本解释（高维几何、非鲁棒模式、决策边界）均未给出表征级机制说明为何特定扰动成功及为何攻击跨模型迁移
- 🔬 **研究方法**：论证脆弱性可源于 superposition：网络以非正交表示更多概念产生干涉，针对一个表征的扰动影响其他表征；在精确受控超设定的合成环境建立充分性，并用干涉几何推导理论最优扰动
- 📌 **结论**：PGD 扰动与干涉几何导出的最优扰动对齐；相似数据训练的模型形成相似干涉模式从而解释迁移性；真实图像分类器上的成功攻击也呈现预测结构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Why do adversarial examples exist, and why do they transfer between models? Existing explanations appeal to high-dimensional geometry, non-robust patterns in the input, and decision boundary structure, but none provides a representation-level mechanism that explains why specific perturbations succeed and why attacks transfer between models. In this paper, we show that adversarial vulnerability can stem from efficient information encoding in neural networks. Specifically, vulnerability can arise from superposition - the phenomenon where networks represent more concepts than they have dimensions, forcing non-orthogonal representation and thus interference. This interference causes perturbations targeting one representation to affect others, creating vulnerabilities determined by interference patterns. In synthetic settings with precisely controlled superposition, we establish that superposition suffices to create adversarial vulnerability. The resulting attacks are predictable: PGD-discovered perturbations align with theoretically optimal perturbations derived from the interference geometry. Models trained on similar data develop similar interference patterns, explaining attack transferability. We then show that successful attacks on image classifiers exhibit the structure predicted by our proposed mechanism. These findings reveal that adversarial vulnerability can be a byproduct of networks' representational compression, complementing existing explanations based on data properties or architectural factors.

</details>

### 55. Transferable Attacks on Open-Vocabulary Video Instance Segmentation via Dual-Objective Triggers

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/837.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`open-vocabulary VIS`、`dual trigger`、`cross-model transfer`

- 🎯 **研究动机**：开放词汇视频实例分割（OV-VIS）耦合时空推理与语言对齐，其对抗鲁棒性基本未被探索
- 🔬 **研究方法**：提出 DOT 可迁移攻击：语义抑制触发器破坏真实对象与查询的对齐，合理替换触发器诱导视觉合理且文本一致的幻影轨迹；相位引导对抗训练增强跨模型迁移
- 📌 **结论**：四个 SOTA 实现上 mAP 降幅至多 69.3%、攻击成功率至多 98%，平均超最强基线 1.6 倍且 PSNR 保持 52.4 dB

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-vocabulary video instance segmentation (OV-VIS) couples spatial-temporal reasoning with language grounding, yet its adversarial robustness has remained largely unexplored. We present the Dual-Objective Triggers (DOT), the first transferable attack on OV-VIS that simultaneously exploits the vision–language coupling and temporal coherence. DOT deploys a Dual Semantic Perturbation Module that combines two complementary triggers: a Semantic Suppression Trigger disrupts the alignment between the true object and the query, while a Plausible Replacement Trigger steers the tracker toward a phantom trajectory that is visually plausible and text-consistent. To amplify cross-model transferability without sacrificing perceptual fidelity, we introduce Phase-Guided Adversarial Training, which injects perturbations primarily in the phase spectrum while blending amplitudes with clean references. Extensive experiments on four state-of-the-art OV-VIS implementations demonstrate that DOT reduces mAP by up to 69.3% and achieves attack success rate of up to 98%, outperforming the strongest baseline by a factor of 1.6× on average, while maintaining a PSNR of 52.4 dB, thus exposing critical security vulnerabilities and laying a foundation for future research on robust and trustworthy vision–language systems.

</details>

### 56. Unrestricted Targeted Deep Hashing Attack via Contrastive Latent Diffusion

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4746.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`attack`、`deep hashing`、`latent diffusion`、`targeted retrieval`

- 🎯 **研究动机**：深度哈希定向攻击依赖 Lp 范数约束扰动，难兼顾攻击有效性与不可感知性，常需可感知噪声
- 🔬 **研究方法**：提出 UTDHA：以对比引导的 latent diffusion 在潜空间而非像素空间生成对抗样本，拉近目标标签、推离非目标标签，并约束结构与感知一致性
- 📌 **结论**：三个基准上攻击有效性与不可感知性均优于现有定向攻击基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep hashing is widely used for large-scale image retrieval but remains vulnerable to adversarial examples, raising practical security concerns. Existing targeted adversarial attacks on deep hashing typically rely on ℓp-norm constrained perturbations, which struggle to balance attack effectiveness and imperceptibility, often requiring perceptible noise and limiting their practicality in real-world retrieval scenarios. We propose UTDHA, the first unrestricted targeted attack for deep hashing models using contrastive-guided latent diffusion. UTDHA generates adversarial examples with a latent diffusion model and performs optimization in the latent space rather than the pixel space, enabling semantic manipulation while preserving image naturalness. Through contrastive guidance, the attack pulls adversarial examples toward the target label while pushing them away from non-target labels. Meanwhile, UTDHA enforces structural and perceptual consistency, producing adversarial examples that are both imperceptible and visually natural. Extensive experiments on three benchmarks demonstrate that UTDHA outperforms existing targeted adversarial attack baselines for deep hashing models in both attack effectiveness and imperceptibility.

</details>

### 57. SEBA: Sample-Efficient Black-Box Attacks on Visual Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2511.09681) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_SEBA_Sample-Efficient_Black-Box_Attacks_on_Visual_Reinforcement_Learning_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`visual RL`、`black-box evasion`、`sample efficiency`

👤 **作者**：Tairan Huang、Yulin Jin、Junxu Liu、Qingqing Ye、Haibo Hu

- 🎯 **研究动机**：现有黑盒攻击面向向量或离散动作 RL，在图像连续控制上受大动作空间与过多环境查询限制
- 🔬 **研究方法**：SEBA 整合估计对抗条件下累积奖励的影子 Q 模型、生成不可感知扰动的 GAN 与模拟环境动力学的世界模型，两阶段交替训练
- 📌 **结论**：在 MuJoCo 与 Atari 上显著降低累积奖励、保持视觉保真并大幅减少环境交互

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual reinforcement learning has achieved remarkable progress in visual control and robotics, but its vulnerability to adversarial perturbations remains underexplored. Most existing black-box attacks focus on vector-based or discrete-action RL, and their effectiveness on image-based continuous control is limited by the large action space and excessive environment queries. We propose SEBA, a sample-efficient framework for black-box adversarial attacks on visual RL agents. SEBA integrates a shadow Q model that estimates cumulative rewards under adversarial conditions, a generative adversarial network that produces visually imperceptible perturbations, and a world model that simulates environment dynamics to reduce real-world queries. Through a two-stage iterative training procedure that alternates between learning the shadow model and refining the generator, SEBA achieves strong attack performance while maintaining efficiency. Experiments on MuJoCo and Atari benchmarks show that SEBA significantly reduces cumulative rewards, preserves visual fidelity, and greatly decreases environment interactions compared to prior black-box and white-box methods. The code is available at https://github.com/tairanhuang/seba online.

</details>

### 58. Accelerating Targeted Hard-Label Adversarial Attacks in Low-Query Black-Box Settings

📄 [arXiv](https://arxiv.org/abs/2505.16313) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-05　🏷 SaTML 2026

**关键词**：`attack`、`hard-label attack`、`targeted evasion`、`query efficiency`

👤 **作者**：Arjhun Swaminathan、Mete Akgün

- 🎯 **研究动机**：黑盒 hard-label 定向攻击决策区域窄，现有方法只用决策边界几何而忽略图像自身信息
- 🔬 **研究方法**：提出 TEA，利用目标图像边缘信息生成更靠近源图的对抗样本，并为几何式攻击提供更优初始化
- 📌 **结论**：低查询设置下比 SoTA 少用近 70% 查询

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks for image classification remain vulnerable to adversarial examples -- small, imperceptible perturbations that induce misclassifications. In black-box settings, where only the final prediction is accessible, crafting targeted attacks that aim to misclassify into a specific target class is particularly challenging due to narrow decision regions. Current state-of-the-art methods often exploit the geometric properties of the decision boundary separating a source image and a target image rather than incorporating information from the images themselves. In contrast, we propose Targeted Edge-informed Attack (TEA), a novel attack that utilizes edge information from the target image to carefully perturb it, thereby producing an adversarial image that is closer to the source image while still achieving the desired target classification. Our approach consistently outperforms current state-of-the-art methods across different models in low query settings (nearly 70% fewer queries are used), a scenario especially relevant in real-world applications with limited queries and black-box access. Furthermore, by efficiently generating a suitable adversarial example, TEA provides an improved target initialization for established geometry-based attacks.

</details>

### 59. Stealthy Multi-task Adversarial Attacks

📄 [arXiv](https://arxiv.org/abs/2411.17936) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5515)　📅 2024-11　🏷 ECCV 2026

**关键词**：`attack`、`multi-task model`、`stealthy attack`、`adversarial robustness`、`targeted attack`

👤 **作者**：Jiacheng Guo、Tianyun Zhang、Lei Li、Haochen Yang、Hongkai Yu、Minghai Qin

- 🎯 **研究动机**：已有攻击要么单任务、要么同时降级多任务所有性能，缺乏选择性隐蔽攻击
- 🔬 **研究方法**：SMTA2 将选择性降级表述为约束多目标优化，任务感知扰动最大化目标任务退化并保非目标任务，配自动损失权重调节
- 📌 **结论**：NYUv2 与 Cityscapes 上强攻目标任务而非目标任务完好，且对对抗训练模型同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep neural networks are highly vulnerable to adversarial perturbations, raising serious safety concerns in the real-world systems. While prior work mainly explores single-task attacks or jointly degrading all tasks in multi-task models, practical scenarios often demand more selective and stealthy attack strategies. To address this challenge, we propose Stealthy Multi-Task Adversarial Attack (SMTA$^{2}$), a novel framework that selectively degrades a targeted task while strictly preserving the performance of non-targeted tasks. We formulate this objective as a constrained multi-objective optimization problem and design task-aware adversarial perturbations that maximize degradation on the targeted task without causing collateral damage on non-targeted tasks. To enhance practicality, we further introduce an automated loss-weight tuning strategy that dynamically balances attack and preservation objectives. Experiments on two multi-task benchmarks NYUv2 and Cityscapes demonstrate that SMTA$^{2}$ achieves strong attack performance on targeted tasks while maintaining non-targeted tasks intact on both undefended and adversarially trained models, establishing the first systematic framework for stealthy and selective multi-task attack framework.

</details>

### 60. Scaling Laws for Black-box Adversarial Attacks

📄 [arXiv](https://arxiv.org/abs/2411.16782) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/3565)　📅 2024-11　🏷 ECCV 2026

**关键词**：`attack`、`analysis`、`black-box attack`、`scaling law`、`adversarial robustness`、`multimodal model`

👤 **作者**：Chuan Liu、Huanran Chen、Yichi Zhang、Jun Zhu、Yinpeng Dong

- 🎯 **研究动机**：黑盒攻击多用小规模固定代理集成，扩大代理数量能否持续提升未知
- 🔬 **研究方法**：用高级优化器解决梯度冲突，理论与实证确立 ASR 随集成规模 T 的对数线性 scaling law，并蒸馏目标类稳健语义特征
- 📌 **结论**：对 GPT-4o 等专有模型迁移 ASR 超 80%，同时揭示 Claude-3.5-Sonnet 显著更稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial examples exhibit cross-model transferability, enabling threatening black-box attacks on commercial models. Model ensembling, which attacks multiple surrogate models, is a known strategy to improve this transferability. However, prior studies typically use small, fixed ensembles, which leaves open an intriguing question of whether scaling the number of surrogate models can further improve black-box attacks. In this work, we conduct the first large-scale empirical study of this question. We show that by resolving gradient conflict with advanced optimizers, we discover a robust and universal log-linear scaling law through both theoretical analysis and empirical evaluations: the Attack Success Rate (ASR) scales linearly with the logarithm of the ensemble size $T$. We rigorously verify this law across standard classifiers, SOTA defenses, and MLLMs, and find that scaling distills robust, semantic features of the target class. Consequently, we apply this fundamental insight to benchmark SOTA MLLMs. This reveals both the attack's devastating power and a clear robustness hierarchy: we achieve 80\%+ transfer attack success rate on proprietary models like GPT-4o, while also highlighting the exceptional resilience of Claude-3.5-Sonnet. Our findings urge a shift in focus for robustness evaluation: from designing intricate algorithms on small ensembles to understanding the principled and powerful threat of scaling.

</details>

### 61. Casting the Net! Revisiting MasterFace Impersonation Attacks

📄 [arXiv](https://arxiv.org/abs/2608.06952) · 🌐 [Project](https://zenodo.org/records/20765343) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-08　🏷 ACM CCS 2026

**关键词**：`attack`、`MasterFace`、`biometric impersonation`、`black-box attack`、`face recognition`、`maximum coverage`

👤 **作者**：Seunghun Paik、Sunpill Kim、Chanwoo Hwang、Jae Hong Seo

- 🎯 **研究动机**：MasterFace 冒充攻击被认为在现代人脸识别系统上不超 FMR 基线，商用 API 部署场景未被重新审视
- 🔬 **研究方法**：攻击者购买 pay-as-you-go 商用 API，把攻击形式化为表示空间最大覆盖问题（NET），利用表示空间几何构造 API 定制 NET
- 📌 **结论**：至多 30 次认证内把多个开源与商用 API 系统的冒充率较标准 FMR 放大多达 9.5 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Impersonation is a fundamental security threat in face recognition systems (FRSs). While the security of FRSs has been challenged by various attack vectors, under realistic adversarial capabilities, e.g., a limited number of decision-only authentication trials and no internal system knowledge, most attack techniques become infeasible. As a result, impersonation by zero-effort impostors, characterized by false match rate (FMR), is commonly regarded as a standalone baseline. A few years ago, impersonation attacks based on MasterFaces emerged as a notable security threat that could break the barrier of the FMR-based baseline under such realistic constraints. However, they were believed not to yield impersonation above the standard FMR in modern FRSs, as discussed by multiple follow-up studies. In this paper, we demonstrate that even legitimate access to public commercial APIs allows an adversary to amplify impersonation rates through MasterFaces, resulting in a non-trivial impersonation attack beyond FMR on downstream applications built on top of these APIs. We observe that several real-world FRS deployments are implemented using commercial APIs, and that the backend service provider is publicly disclosed or trivially inferable. As a result, the adversary can purchase these pay-as-you-go API services without requiring any additional privilege over the target FRS. From this observation, we formalize the MasterFaces attack as a maximum coverage problem over the biometric representation space, which we call a NET, and show that the adversary can construct an API-tailored NET by leveraging the geometric structure of the representation space. We demonstrate that our attack amplifies the impersonation rates of several open-source and commercial API-based FRSs by up to 9.5$\times$ within at most 30 authentication trials, compared to those expected from the standard FMR.

</details>

### 62. Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern

📄 [arXiv](https://arxiv.org/abs/2605.04675) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Physical_Adversarial_Clothing_Evades_Visible-Thermal_Detectors_via_Non-Overlapping_RGB-T_Pattern_CVPR_2026_paper.html)　📅 2026-05　🏷 CVPR 2026

**关键词**：`attack`、`RGB-T detector`、`adversarial clothing`、`cross-modal evasion`

👤 **作者**：Xiaopei Zhu、Guanning Zeng、Zhanhao Hu、Jun Zhu、Xiaolin Hu

- 🎯 **研究动机**：RGB-T 检测器的物理世界安全性基本被忽视，重叠式 RGB-T 对抗图案存在热光衰减问题
- 🔬 **研究方法**：NORP 用可见光与热材料不重叠的对抗服装图案，构建 3D RGB-T 人体模型支持全视角攻击，以空间离散-连续优化 SDCO 求解
- 📌 **结论**：对不同融合架构的检测器在数字与物理世界均获高攻击成功率，融合阶段集成法提升对未见检测器的迁移性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visible-thermal (RGB-T) object detection is a crucial technology for applications such as autonomous driving, where multimodal fusion enhances performance in challenging conditions like low light. However, the security of RGB-T detectors, particularly in the physical world, has been largely overlooked. This paper proposes a novel approach to RGB-T physical attacks using adversarial clothing with a non-overlapping RGB-T pattern (NORP). To simulate full-view (0$^{\circ}$--360$^{\circ}$) RGB-T attacks, we construct 3D RGB-T models for human and adversarial clothing. NORP is a new adversarial pattern design using distinct visible and thermal materials without overlap, avoiding the light reduction in overlapping RGB-T patterns (ORP). To optimize the NORP on adversarial clothing, we propose a spatial discrete-continuous optimization (SDCO) method. We systematically evaluated our method on RGB-T detectors with different fusion architectures, demonstrating high attack success rates both in the digital and physical worlds. Additionally, we introduce a fusion-stage ensemble method that enhances the transferability of adversarial attacks across unseen RGB-T detectors with different fusion architectures.

</details>

### 63. Unleashing the Representational Power of Fourier Shapes for Attacking Infrared Object Detection

📄 [arXiv](https://arxiv.org/abs/2605.17822) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65327)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`adversarial example`、`evasion attack`、`robustness degradation`、`dangerous capability`、`empirical evaluation`

👤 **作者**：Yixing Yong、Jian Wang、Ming Lei、Lijun He、Fan Li

- 🎯 **研究动机**：红外攻击以挡热材料的几何形状为对抗信息载体，现有形状方法在表达能力与优化能力间存在根本权衡
- 🔬 **研究方法**：引入可学习 Fourier 形状：紧凑 Fourier 系数定义形状边界，经环绕数定理解析映射为像素掩码，端到端可微框架支持梯度优化
- 📌 **结论**：物理贴片在多样距离、角度、姿态与个体下稳健规避检测，距离超 25m（conf.=0.5）时攻击成功率超 88%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Infrared object detection is crucial for perception in autonomous driving and surveillance but remains vulnerable to physical adversarial attacks. Unlike in the RGB domain, where attacks rely on color texture, infrared attacks must manipulate thermal signatures, making the geometry shape of heat-blocking materials the primary adversarial information carrier. Current shape-based methods suffer from a fundamental trade-off between representational capability and optimization power, limiting their attack effectiveness. In this work, we overcome this dilemma by introducing learnable Fourier shapes to the infrared domain. We utilize an end-to-end differentiable framework where a compact set of Fourier coefficients, defining the shape boundary, is analytically mapped to a pixel-space mask via the winding number theorem. This enables efficient gradient-based optimization to generate potent shapes that cause human targets to evade detection. Extensive digital and physical experiments provide a comprehensive evaluation and validate our superior performance. Our resulting physical patch achieves striking robustness, successfully evading detectors across diverse distances, angles, poses, and individuals, and achieves over 88% attack success rate at distances greater than 25m (conf.=0.5). Code is available at https://github.com/Yongyx99/Fourier-shape-attack.

</details>

### 64. CamPI: Physical Adversarial Examples through Camera Power Signal Injection

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_CamPI_Physical_Adversarial_Examples_through_Camera_Power_Signal_Injection_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`camera sensor`、`power injection`、`physical adversarial example`

👤 **作者**：Yanze Ren、…、Wenyuan Xu

- 🎯 **研究动机**：现有物理对抗样本靠贴补丁或投光，通常可见且暴露恶意意图
- 🔬 **研究方法**：揭示向相机电源注入信号的新攻击面：分析结构条纹注入机制并用信号调制实现可控细粒度注入，建仿真模型后在白盒与黑盒下端到端优化注入参数
- 📌 **结论**：七个分类模型的仿真与物理注入实验均证明可破坏计算机视觉性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Physical adversarial examples pose a concrete threat to real-world computer vision systems. Existing works mainly generate physical adversarial examples by affixing patches or projecting light onto targets, which are usually visible and can expose the malicious intention. In this work, we reveal a new attack surface that generates invisible adversarial samples by injecting signals into the camera's power supply. We analyze the mechanism of injecting structural stripe patterns into cameras and demonstrate the feasibility of controllable fine-grained injection with signal modulation. We develop a simulation model to emulate the physically injected perturbation, and propose end-to-end optimization methodologies in both white-box and black-box settings to generate the injection signal parameters. We perform a simulated evaluation across seven classification models and carry out physical signal injection experiments with optimized signals. The results show that physical adversarial examples generated through camera power signal injection can disrupt computer vision performance. Our work introduces a new methodology for physical adversarial examples, emphasizing the need for securing computer vision systems in the physical world.

</details>

### 65. Fractal Camouflage: A Bio-Inspired Approach for Multi-Scale Adversarial Attacks in the Infrared Domain

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_Fractal_Camouflage_A_Bio-Inspired_Approach_for_Multi-Scale_Adversarial_Attacks_in_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`infrared detector`、`fractal camouflage`、`physical evasion`

👤 **作者**：Chengyin Hu、…、Yiwei Wei

- 🎯 **研究动机**：红外物理攻击依赖固定静态模式，感受野固定、无法适应距离与场景变化，跨尺度鲁棒性差
- 🔬 **研究方法**：AdvFractal 黑盒攻击用 H 型分形建模扰动，借分形自相似性生成多尺度物理可实现的扰动，粒子群优化参数
- 📌 **结论**：物理域 ASR 97.54%、跨数据集 99.16%，红外频谱高效而可见光隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Infrared pedestrian detection is crucial in safety-critical systems but remains vulnerable to adversarial attacks. Existing physical attacks often rely on fixed, static patterns. However, they often lack robustness across scales, as their hand-crafted or uniformly generated structures are fundamentally limited by a fixed receptive field and fail to adapt to varying distances and scene contexts. In light of this, we propose AdvFractal, a black-box attack that exploits the innate self-similarity and structural richness of fractal geometry to naturally generate multi-scale, physically realizable adversarial perturbations. By modeling perturbations with H-type fractals and optimizing parameters via Particle Swarm Optimization, AdvFractal seamlessly coordinates attacks across scales, progressively disrupting detector features from local textures to global shapes. Experiments show AdvFractal achieves an attack success rate (ASR) of 97.54% in the physical domain and 99.16% cross-dataset, significantly outperforming state-of-the-art methods. The perturbations are highly effective in the infrared spectrum while remaining stealthy in visible light, offering a novel approach for evaluating and understanding the security of infrared detection systems.

</details>

### 66. Thermally Activated Dual-Modal Adversarial Clothing against AI Surveillance Systems

📄 [arXiv](https://arxiv.org/abs/2511.09829) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Long_Thermally_Activated_Dual-Modal_Adversarial_Clothing_against_AI_Surveillance_Systems_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`AI surveillance`、`thermal clothing`、`dual-modal evasion`

👤 **作者**：Jiahuan Long、…、Wen Yao

- 🎯 **研究动机**：对抗补丁外观显眼，难以在日常场景中部署
- 🔬 **研究方法**：把热致变色染料与柔性加热单元集成于衣物，加热时激活隐藏对抗图案，默认状态下只是普通黑色 T 恤，实现可见光与红外双模态规避
- 📌 **结论**：50 秒内完成纹理激活，多种真实监控环境下对抗成功率保持 80% 以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial patches have emerged as a popular privacy-preserving approach for resisting AI-driven surveillance systems. However, their conspicuous appearance makes them difficult to deploy in real-world scenarios. In this paper, we propose a thermally activated adversarial wearable designed to ensure adaptability and effectiveness in complex real-world environments. The system integrates thermochromic dyes with flexible heating units to induce visually dynamic adversarial patterns on clothing surfaces. In its default state, the clothing appears as an ordinary black T-shirt. Upon heating via an embedded thermal unit, hidden adversarial patterns on the fabric are activated, allowing the wearer to effectively evade detection across both visible and infrared modalities. Physical experiments demonstrate that the adversarial wearable achieves rapid texture activation within 50 seconds and maintains an adversarial success rate above 80\% across diverse real-world surveillance environments. This work demonstrates a new pathway toward physically grounded, user-controllable anti-AI systems, highlighting the growing importance of proactive adversarial techniques for privacy protection in the age of ubiquitous AI surveillance.

</details>

### 67. Temporal Misalignment Attacks against Multimodal Perception in Autonomous Driving

📄 [arXiv](https://arxiv.org/abs/2507.09095) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-07　🏷 SaTML 2026

**关键词**：`attack`、`autonomous driving`、`sensor desynchronization`、`multimodal perception`

👤 **作者**：Md Hasan Shahriar、…、Wenjing Lou

- 🎯 **研究动机**：多模态融合严格依赖相机与 LiDAR 的精确时间同步，车内网络的时间完整性攻击面未被研究
- 🔬 **研究方法**：提出 DejaVu 利用车内网络制造细微时间失配，并分析不同感知任务对传感器的不均衡敏感性
- 📌 **结论**：单帧 LiDAR 延迟使车辆检测 mAP 最多降 88.5%，三帧相机延迟使 MOTA 降 73%；硬件在环与 Autoware 仿真验证可致碰撞与幻影刹车

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal fusion (MMF) plays a critical role in the perception of autonomous driving, which primarily fuses camera and LiDAR streams for a comprehensive and efficient scene understanding. However, its strict reliance on precise temporal synchronization exposes it to new vulnerabilities. In this paper, we introduce DejaVu, an attack that exploits the in-vehicular network to manipulate the integrity of time and create subtle temporal misalignments, severely degrading downstream MMF-based perception tasks. Our comprehensive attack analysis across different models and datasets reveals the sensors' task-specific imbalanced sensitivities: object detection is overly dependent on LiDAR inputs, while object tracking is highly reliant on the camera inputs. Consequently, with a single-frame LiDAR delay, an attacker can reduce the car detection mAP by up to 88.5%, while with a three-frame camera delay, multiple object tracking accuracy (MOTA) for car drops by 73%. We further demonstrated two attack scenarios using an automotive Ethernet testbed for hardware-in-the-loop validation and the Autoware stack for end-to-end AD simulation, demonstrating the feasibility of the DejaVu attack and its severe impact, such as collisions and phantom braking. Our code and artifacts are publicly available at: https://github.com/shahriar0651/DejaVu.

</details>

### 68. SABER: Spatially Consistent 3D Universal Adversarial Objects for BEV Detectors

📄 [arXiv](https://arxiv.org/abs/2505.22499) · 🌐 [Project](https://npucvr.github.io/SABER) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SABER_Spatially_Consistent_3D_Universal_Adversarial_Objects_for_BEV_Detectors_CVPR_2026_paper.html)　📅 2025-05　🏷 CVPR 2026

**关键词**：`attack`、`BEV detector`、`3D adversarial object`、`spatial consistency`

👤 **作者**：Aixuan Li、Mochu Xiang、Bosen Hou、Zhexiong Wan、Jing Zhang、Yuchao Dai

- 🎯 **研究动机**：侵入式对抗攻击需改装目标车辆不现实，环境放置攻击又缺多视角与时序一致性
- 🔬 **研究方法**：提出 SABER，向场景插入渲染的 3D 对抗物体，以遮挡感知模块保证物理合理，用 BEV 空间特征引导优化攻击内部表示
- 📌 **结论**：单一通用对抗物体可从多视角、多距离持续削弱多种 BEV 检测器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Adversarial robustness of BEV 3D object detectors is critical for autonomous driving (AD). Existing invasive attacks require altering the target vehicle itself (e.g. attaching patches), making them unrealistic and impractical for real-world evaluation. While non-invasive attacks that place adversarial objects in the environment are more practical, current methods still lack the multi-view and temporal consistency needed for physically plausible threats. In this paper, we present the first framework for generating universal, non-invasive, and 3D-consistent adversarial objects that expose fundamental vulnerabilities for BEV 3D object detectors. Instead of modifying target vehicles, our method inserts rendered objects into scenes with an occlusion-aware module that enforces physical plausibility across views and time. To maintain attack effectiveness across views and frames, we optimize adversarial object appearance using a BEV spatial feature-guided optimization strategy that attacks the detector's internal representations. Extensive experiments demonstrate that our learned universal adversarial objects can consistently degrade multiple BEV detectors from various viewpoints and distances. More importantly, the new environment-manipulation attack paradigm exposes models' over-reliance on contextual cues and provides a practical pipeline for robustness evaluation in AD systems.

</details>

### 69. GaussTrap: Stealthy Backdoor Attacks on 3D Gaussian Splatting for Targeted Scene Misperception

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

### 70. Defending from GeoLocalization through Adversarial Road Trips

📄 [arXiv](https://arxiv.org/abs/2607.03277) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4426)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`adversarial attack`、`adversarial robustness`、`privacy leakage`、`geolocation`、`location privacy`

👤 **作者**：Niccolò Niccoli、Federico Becattini、Lorenzo Seidenari

- 🎯 **研究动机**：检索式图像地理定位威胁位置隐私，需要有效对抗攻击保护用户
- 🔬 **研究方法**：提出 RoadTrip Attack：把对抗过程概念化为通往攻击者选定地点的最优干扰旅程，beam search 迭代构造错误位置的序列并对查询图像施加细微扰动引导模型沿路径行进
- 📌 **结论**：黑盒设定下攻击高度可迁移且图像伪影更不易察觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-based image geolocalization has emerged as a powerful technique for determining the location of a query image by matching it against a large, geotagged database. The success of deep learning based approaches has raised concerns regarding privacy and safety. A way to protect users from geolocalization is to design adversarial attacks for such methods. In this paper, we introduce RoadTrip Attack (RTA), a novel and highly effective targeted adversarial attack for geolocalization. RTA conceptualizes the adversarial process as finding an optimal distractor journey to a specific, attacker-chosen location. It employs a beam search algorithm to iteratively construct a sequence of incorrect geographic locations that form a path to the target. At each step, the attack generates subtle perturbations to the query image, guiding the geolocalization model toward the next location in this deceptive path. We show that our method is also strong in black-box settings, obtaining highly transferable attacks with less perceptible image artifacts.

</details>

### 71. Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks

📄 [arXiv](https://arxiv.org/abs/2607.25227)　📅 2026-07

**关键词**：`attack`、`emergent misalignment`、`weight tampering`、`value hijacking`

👤 **作者**：Yu Yan、…、Shouling Ji

- 🎯 **研究动机**：已有攻击无法在不触发违禁内容、不损害功能的前提下实现定向认知操纵，开源模型共享生态使其可行
- 🔬 **研究方法**：定义 decision-level hijacking 并提出 CogBias：经可微情感评估器把主观偏好转为优化信号、多目标损失联合约束，BitScout 定位关键比特，以超稀疏位翻转预算实现定向认知干预
- 📌 **结论**：Llama-3.2-3B、Mistral-7B、Qwen2.5-14B 及商业推荐、争议事实话题场景中，翻转极少量比特即稳定诱导目标话题立场转移且对非任务影响有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. This paper defines such threats as decision-level hijacking. Existing attacks fail to achieve targeted cognitive manipulation without triggering prohibited content or degrading model functionality. To fill this gap, this paper reveals that Bit-Flip Attacks (BFAs) can serve as an attack vector for inducing decision-level hijacking, requiring no real-time interaction or control over the training process, and only a minimal number of weight bits need to be flipped after deployment to achieve stealthy, low-cost, and persistent cognitive manipulation. Therefore, we propose CogBias, a cognitive bias injection framework for LLMs. CogBias converts subjective preferences into optimization signals via a differentiable sentiment evaluator, uses a multi-objective loss to jointly constrain multiple dimensions, and constructs BitScout to locate critical bits, achieving targeted cognitive intervention under an ultra-sparse flip budget. Experiments on Llama-3.2-3B, Mistral-7B, and Qwen2.5-14B, as well as on the commercial recommendation and controversial factual topic scenarios, demonstrate that flipping only a small number of bits stably induces significant stance shifts on target topics, while the impact on non-target tasks and overall output distribution is limited. This work demonstrates that minute perturbations to low-level weight data suffice to undermine the high-level value alignment of LLMs.

</details>

### 72. Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks

📄 [arXiv](https://arxiv.org/abs/2608.11815) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5683)　📅 2026-08　🏷 ECCV 2026

**关键词**：`attack`、`transfer attack`、`bilevel optimization`、`adversarial robustness`、`black-box security`

👤 **作者**：Yaohua Liu、Yifan Guo、Jiaxin Gao

- 🎯 **研究动机**：迁移攻击可迁移性由初始化、代理适配与梯度动态的耦合决定，现有方法将其割裂处理
- 🔬 **研究方法**：BMAT 以双层极小极大建模初始化与扰动依赖、内层极小极大促进代理跨架构鲁棒，自底向上求解器耦合 Soft Weight Modulator 与 Implicit Gradient Approximator
- 📌 **结论**：30+ 受害模型上超过 10 个强基线，分割任务 mIoU 最高降 2 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Transfer-based adversarial attacks craft adversarial examples using surrogate models to mislead black-box victim models. Beyond perturbation generation, transferability is fundamentally governed by the coupling of initialization, surrogate adaptation, and gradient dynamics. We revisit this challenge from a bilevel-minimax perspective and propose BMAT (Bilevel-Minimax Adversarial Transfer). The bilevel formulation captures the dependency between initialization and perturbation, while the inner minimax problem promotes surrogate robustness for cross-architecture generalization. Algorithmically, we develop an integrated bottom-up solver that combines a Soft Weight Modulator and an Implicit Gradient Approximator to enable ternary coupling among initialization, surrogate adaptation, and perturbation optimization. We further provide theoretical insights into the optimization dynamics of the proposed bilevel-minimax framework. Extensive experiments on classification and segmentation benchmarks show that BMAT outperforms more than 10 strong baselines across more than 30 victim models, improving both intra- and cross-architecture transfer and yielding up to a 2x reduction in mIoU. Code is available at https://github.com/callous-youth/BMAT.

</details>

### 73. SegPAR: Class-Centric Decision-Based Sparse Attack for Semantic Segmentation

📄 [arXiv](https://arxiv.org/abs/2608.11285) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4370)　📅 2026-08　🏷 ECCV 2026

**关键词**：`attack`、`semantic segmentation`、`adversarial robustness`、`robust training`、`black-box attack`、`sparse perturbation`

👤 **作者**：Dongsu Song、DaeYun GO、Boseung Seo、Jay Hoon Jung

- 🎯 **研究动机**：决策式黑盒稀疏攻击在语义分割中缺乏研究，已有分类域方法因图像中心像素累积迅速耗尽查询预算
- 🔬 **研究方法**：SegPAR 转向类中心探索范式，并引入差异奖励消除标准决策奖励在像素累积中的误导反馈
- 📌 **结论**：稀疏效率与 MIoU 降低显著优于黑盒基线，与白盒稀疏攻击具竞争力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the practical relevance of sparse decision-based black-box threats, they have received limited attention in semantic segmentation. To bridge this gap, we adapt the most representative decision-based black-box sparse attacks from the classification domain to serve as baselines, establishing a rigorous benchmark for this underexplored setting. In this context, we demonstrate that one of the existing methods suffers from severe query inefficiency due to its image-centric pixel accumulation, which rapidly exhausts query budgets across the vast image space. To overcome this, we propose SegPAR, a novel decision-based framework that shifts to a class-centric exploration paradigm. Furthermore, to eliminate the misleading feedback generated by standard decision rewards during pixel accumulation, we introduce a novel discrepancy reward. Extensive experiments show that SegPAR significantly outperforms black-box baselines in sparsity efficiency and MIoU reduction, while remaining competitive with white-box sparse attacks. Code is available at \href{https://github.com/KAU-QuantumAILab/SegPAR}{https://github.com/KAU-QuantumAILab/SegPAR}.

</details>

### 74. NERVE Attacks: Breaking AI-Powered Brain-Computer Interfaces

📄 [arXiv](https://arxiv.org/abs/2609.08971)　📅 2026-09

**关键词**：`attack`、`brain-computer interface`、`neuro-specific attack`、`backdoor`、`EEG security`

👤 **作者**：Zahra Tarkhani、Georgios Akkogiounoglou、Lorena Qendro、Isabel Tscherniak、Anil Madhavapeddy

- 🎯 **研究动机**：AI 深入脑机接口形成连接神经信号与物理系统的攻击面，威胁认知自主、心理隐私与物理安全却缺乏系统刻画
- 🔬 **研究方法**：提出 NERVE 五维攻击类（神经伪造、失步逃逸、重放劫持、信号窃取、嵌入式后门）与 EEGle 自动化安全分析框架
- 📌 **结论**：发现 17 个新型神经攻击实例与 BCI 后门特有的隐蔽-有效谱系，生成式 AI 降低非专家攻击门槛

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid integration of AI into human-centred systems such as Brain-Computer Interfaces (BCIs) has created a poorly understood attack surface linking neural signals to physical systems. Exploits in this domain threaten cognitive autonomy, mental privacy, and physical safety, from neural data exfiltration to malicious control of BCI-tethered devices. We introduce the NERVE Attacks class, a systematic characterisation of five orthogonal attack dimensions that together span the complete BCI stack: Neuro-mimetic Forgery (N), Evasion via Desynchronization (E), Replay-based Hijacking (R), Vein Tapping (V), and Embedded Backdoors (E). To evaluate this class, we present EEGle, an AI-assisted extensible framework for systematic BCI security analysis. Our evaluation uncovers 17 novel neuro-specific attack instances and reveals a stealth-effectiveness spectrum unique to BCI backdoor design. We also show that generative AI lowers the barrier to entry for non-expert attackers and provide EEGle to the community for building and verifying the security of these deeply personal devices.

</details>
