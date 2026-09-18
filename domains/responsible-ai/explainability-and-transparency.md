# 安全可解释性与 Transparency

[返回上级目录](README.md)

## 研究方向

研究具体 AI 安全 threat model 下的 explanation、feature attribution、mechanistic interpretation、transparency artifact 和 auditability。收录对象必须把解释机制直接用于有害行为与安全对齐分析、越狱或后门诊断、欺骗监控、隐私泄漏、内容安全、Agent 故障或安全关键决策；仅提升一般分类可解释性、没有明确安全风险的工作不收录。

## 研究脉络

- **安全行为归因：** Saliency、attribution 和 example-based explanation 用于定位有害输出、对抗脆弱性与 Agent 失败的责任信号。
- **安全机制解释：** Representation、circuit 和 causal intervention 检验拒答、安全对齐、欺骗或后门行为的内部成因。
- **解释可靠性审计：** Robustness、faithfulness 和 counterfactual benchmark 检查安全解释能否经受扰动、分析选择和因果验证。
- **部署与监督：** Trace、evidence artifact 和可检查的监控信号把安全解释连接到人工监督与外部问责。

## Attribution、Transparency 与 Auditability

### 1. Diff Mining: Logit Differences Reveal Finetuning Objectives

📄 [arXiv](https://arxiv.org/abs/2608.26462) · 🎓 [Official](https://iclr.cc/virtual/2026/10019308)　📅 2026-08

**关键词**：`detection`、`analysis`、`finetuning-objective audit`、`logit difference`、`hidden bias`、`finetuning fingerprint`

👤 **作者**：Greg Kocher、Robert West、Clément Dumas、Julian Minder

- 🎯 **研究动机**：微调可能涌现不良行为，而现有 model diffing 常需模型内部访问且难识别具体目标
- 🔬 **研究方法**：Diff Mining 比较微调与基模型的 logit 差异，经 Top-K 频率或 NMF 聚合成可解释 token 集，仅需输出 logit
- 📌 **结论**：微调域检测显著优于 SOTA diffing；对注入偏差模型无需定向 probe 即识别超三分之一

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Finetuning has become the gold standard for refining existing behaviors and inducing new ones in language models, yet it often remains unclear exactly which behaviors emerge during this process. As models grow ever more capable, understanding finetuning better becomes increasingly important, particularly since unwanted behaviors may arise during finetuning. In this paper, we introduce Diff Mining, a simple yet effective framework for identifying what a finetuned model has learned by comparing its logits to those of its base model. Diff Mining effectively surfaces salient tokens that are amplified in the finetuned model, serving as a fingerprint of its training -- even on text unrelated to the finetuning domain. Unlike many existing model diffing methods which require model internals, Diff Mining only needs access to output logits and scales to large models. The framework consists of two modular stages: (i) extracting per-context logit differences between the finetuned and base models on a reference corpus, and (ii) aggregating the resulting signals to construct an interpretable token set representing the finetune. For aggregation, we explore both a simple Top-K frequency method and a Non-negative Matrix Factorization (NMF)-based approach for disentangling multiple finetuning objectives into distinct token clusters. Empirically, Diff Mining succeeds across diverse settings: on finetune domain detection, it significantly outperforms state-of-the-art model diffing methods both in identifying relevant tokens and in downstream performance when an interpretability agent is given access to the extracted token set; on models with injected biases, it identifies more than one third of the biases without targeted probing. Overall, our framework shows promise in developing auditing tools to detect finetuning objectives.

</details>

### 2. The Latent Diagnostic Taxonomy: A Framework for Constructing Classifiers and Diagnosing Their Decisions, Applied to Prompt Injection Detection

📄 [arXiv](https://arxiv.org/abs/2608.26423)　📅 2026-08

**关键词**：`analysis`、`detection`、`safeguard classifier`、`decision trust`、`heuristic shortcut`、`prompt-injection classifier`

👤 **作者**：Jaturong Kongmanee、Smile Thanapattheerakul

- 🎯 **研究动机**：safeguard classifier 的高置信判定可能依赖脆弱 shortcut，部署者不知哪些可信
- 🔬 **研究方法**：以维度优化分类器与 latent support vector 定位改变预测的 token，按单 token 攻击幅度构建诊断 taxonomy 分流输入
- 📌 **结论**：prompt injection 数据上约 77% 高置信判定不抗移除单个 token，分为校准失败与真实可利用 shortcut 两类

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper proposes a framework for constructing a classifier as a safeguard layer, and for developing a complementary diagnostic that identifies which of the classifier's confident decisions can be trusted. This framework, the Latent Diagnostic Taxonomy, consists of (i) constructing a dimensionality-optimized classifier, in which the embedding dimensionality is empirically selected via cross-validated performance rather than fixed a priori, (ii) locating a relatively small set of latent support vectors (~ 29% of total training examples) representing influential prompts for identifying tokens that alter the classifier's predicted labels, and (iii) utilizing such tokens and their associated attack magnitudes for constructing a diagnostic taxonomy. This diagnostic taxonomy provides an end-to-end guideline for flagging prompts that require different treatments: rely Safely on the classifier's decision; flag Heuristic Bias and Heuristic Override cases; route Insufficient Context cases for further human/safety review. Applying the framework to a classifier trained on a public prompt injection dataset, we find that a substantial fraction of its confident decisions (~ 77%) are not robust to removing a single token, and that this brittleness separates into two distinct failure patterns: a confidence calibration failure and a genuinely exploitable shortcut. For each zone of the taxonomy, we also recommend strategies for remediating diagnosed prompts. We illustrate the framework as a series of steps, demonstrating how each step operates.

</details>

### 3. EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.23313)　📅 2026-08

**关键词**：`benchmark`、`multimodal guard`、`evidence-aware judge`、`counterfactual probe`、`multimodal evidence`、`counterfactual sensitivity`

👤 **作者**：Xuetong Li、Gaofeng Liu

- 🎯 **研究动机**：VLM 安全评测只看最终回应，无法判断模型是否因正确的多模态理由而安全——可能是关键词触发拒答、漏看视觉风险或良性敏感过度拒答
- 🔬 **研究方法**：EviSafe 联合评估自然行为、文本/视觉证据 grounding 与对安全关键证据反事实变化的敏感度；EviSafeBench 含 1,181 个 gold 图文场景与 2,452 个定向反事实变体（8 域、8 风险源），以三 probe 协议加证据感知 judge 评分
- 📌 **结论**：11 个 VLM 自然严重度准确率仅 27.6–52.8%，宽松诊断一致性 6.1–29.3%，unsafe→safe 反事实转变成功率 30.4–58.4%——多数模型并非因正确理由而安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and visual evidence, and behavioral sensitivity to counterfactual changes in safety-critical evidence. EviSafeBench instantiates the framework as a controlled benchmark with 1,181 gold image-text scenarios and 2,452 targeted counterfactual variants across eight safety domains and eight risk-source types. Each scenario includes a gold safety decision, evidence annotations, a safe-response policy, and counterfactual interventions. The three-probe protocol queries models with natural-response, evidencereporting, and counterfactual-response prompts, then scores them using an evidence-aware judge. Across eleven evaluated VLMs, natural severity accuracy ranges from 27.6% to 52.8%, relaxed diagnostic consistency from 6.1% to 29.3%, and unsafe-to-safe counterfactual transition success from 30.4% to 58.4%. These gaps show that the evaluated VLMs are not reliably safe for the right multimodal reason and motivate evaluation beyond refusal counts.

</details>

### 4. Multimodal Model Diffing for Feature Discovery and Control

📄 [arXiv](https://arxiv.org/abs/2608.09928) · 📝 [OpenReview](https://openreview.net/forum?id=JwjpYKi6H4)　📅 2026-08　🏷 ICML 2026 Workshop

**关键词**：`analysis`、`VLM safety`、`explainability`、`model transparency`

👤 **作者**：Hunar Batra、…、Ronald Clark

- 🎯 **研究动机**：SAE 分解的隐藏态既难以定位被多模态训练改变的特征，也不支持定向控制
- 🔬 **研究方法**：MMDiff 训练多模态 SAE，diff 基座与多模态适配版定位被改变的因果特征，支持逐 token 对比检测与因果移除/转向，覆盖三个 MLLM 家族
- 📌 **结论**：移除目标特征使空间任务平均降 12%、OCR 降 17%、多模态攻击 ASR 降 24% 且不影响 VQA；转向使空间与 OCR 精度平均升 3.6%/1.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) exhibit strong visual understanding, yet the internal features that cause these behaviors remain difficult to identify, audit, or control. While applicable to post-hoc inspection, hidden states that are decomposed into interpretable feature directions using sparse autoencoders (SAEs) neither readily isolate which features are changed by multimodal training, nor are they directly useful for targeted control. We introduce MMDiff, a multimodal model-diffing framework that trains multimodal SAEs and turns them into feature-level interfaces for discovering and controlling multimodal behavior. MMDiff supports three uses: (i) feature isolation, by diffing a base-LM SAE against its multimodal-adapted counterpart to identify features altered by multimodal training; (ii) task-specific feature detection, via per-token contrastive firing analysis that isolates causal features; and (iii) feature-level control, by causally removing or steering the discovered feature directions. We train multimodal SAEs for three MLLM families, LLaVA-MORE, PaliGemma 2, and InternVL3.5, and evaluate on visual-spatial understanding, multimodal safety, and OCR. MMDiff discovers sparse, causally specific features whose removal selectively degrades target behaviors by an average of 12% on spatial tasks and 17% on OCR, and reduces attack success rate by 24% on multimodal safety attacks, with no impact on VQA performance. Steering these features improves spatial and OCR accuracy by +3.6% and +1.8% on average over a standard single-layer steering baseline. These results show that multimodal SAEs can serve not only as interpretability tools, but as mechanisms for auditing, steering, and controlling MLLMs behavior toward safer and more capable generations.

</details>

### 5. Decoding Multimodal Cues: Unveiling the Implicit Meaning Behind Hateful Videos

📄 [arXiv](https://arxiv.org/abs/2606.11953) · 🌐 [Project](https://doi.org/10.1145/3805712.3809637)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`detection`、`hateful-video moderation`、`cross-modal evidence`、`reasoning rationale`、`hateful video`、`evidence rationale`

👤 **作者**：Junyu Lu、…、Hongfei Lin

- 🎯 **研究动机**：仇恨视频检测局限于二分类，缺少揭示判断依据的上下文理由，可解释性不足
- 🔬 **研究方法**：构建 Ex-HateMM 与 Ex-ImpliHateVid 两个细粒度标注数据集，提出 IARE 框架：多模态 CoT 信息增强 + DPO 引导正确推理路径
- 📌 **结论**：IARE 在两个数据集上取得 SOTA 并生成准确理由

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hateful videos have become prevalent on online platforms, highlighting an urgent need for effective detection. However, existing studies primarily focus on binary classification and fail to provide contextual rationales that reveal the implicit meanings behind these judgments, significantly undermining model explainability. To fill this gap, we aim to achieve explainable hateful video detection, enabling models to provide contextual rationales that integrate relevant evidence and logical reasoning alongside decisions. This approach can comprehensively enhance the understanding of video content and the explainability of the decision-making process. We first introduce two datasets, Ex-HateMM and Ex-ImpliHateVid, for explainable hateful video detection. Each dataset provides fine-grained annotations of multimodal harmful elements, along with contextual rationales. We then propose an Information Augmentation and Reasoning Enhancement (IARE) framework designed for explainable detection. The framework employs an information augmentation phase that leverages the multimodal chain-of-thought to integrate harmful elements, thereby enriching rationale evidence. Additionally, IARE incorporates a reasoning enhancement phase, in which Direct Preference Optimization guides the model toward correct reasoning paths and away from incorrect ones, thereby improving the logical coherence of its justifications. We conduct extensive experiments on the two datasets, comparing multiple baselines with our proposed IARE framework. The results demonstrate that IARE achieves state-of-the-art performance while also generating accurate rationales.

</details>

### 6. Explainability-aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors

📄 [arXiv](https://arxiv.org/abs/2606.29963) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5021)　📅 2026-06　🏷 ECCV 2026

**关键词**：`detection`、`attack`、`LiDAR`、`explainability`、`model transparency`、`adversarial attack`

👤 **作者**：Chengzeng You、Binbin Xu、Soteris Demetriou

- 🎯 **研究动机**：LiDAR 3D 检测器依赖的空间证据结构不明，已有攻击要么孤立研究要么只顾物理可实现性
- 🔬 **研究方法**：提出 SALL 方法聚合 Integrated Gradient 得到普适显著图，据此设计 EFA 只扰动最具影响力的视锥而非均匀攻击整个目标区域
- 📌 **结论**：KITTI 与 nuScenes 上（PointPillars、SECOND 等）检测 recall 降低超 15 个百分点，所需扰动视锥比 SOTA 基线少 25-50%，揭示判别证据集中于少数空间区域的结构性弱点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The structural vulnerabilities of point cloud-based 3D object detectors remain poorly understood. Prior work has studied adversarial robustness primarily on isolated 3D object models, while recent LiDAR spoofing attacks target richer and more realistic driving scenes but focus mainly on physical realizability rather than understanding detector behavior or attack efficiency. In this work, we investigate how LiDAR-based detectors rely on spatial evidence in complex scenes and whether these reliance patterns can be exploited to induce failures more efficiently. To this end, we propose an explainability-guided adversarial analysis methodology. We introduce the Saliency-LiDAR (SALL) method, which aggregates Integrated Gradient attributions across scenes to produce universal saliency maps for LiDAR-based 3D object detectors. Guided by these maps, we design the Explainability-aware Frustum Attack (EFA), which selectively perturbs only the most influential frustums rather than uniformly attacking entire object regions. Experiments on KITTI and nuScenes, across detectors such as PointPillars and SECOND, show that EFA reduces detection recall by more than 15 percentage points while requiring 25-50% fewer perturbed frustums than the state-of-the-art non-saliency-aware baseline. These findings reveal that modern 3D detectors concentrate discriminative evidence in a small subset of spatial regions, exposing a structural robustness vulnerability in current LiDAR perception systems. Our code is released at https://github.com/SecMindLab/Saliency_LiDAR.

</details>

### 7. Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection

🎓 [Official](https://icml.cc/virtual/2026/poster/61817)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI-generated content`、`explainability`、`model transparency`、`deepfake detection`、`empirical evaluation`

👤 **作者**：Shuaibo Li、…、Lei Zhu

- 🎯 **研究动机**：MLLM 检测 AI 生成视频存在幻觉与不稳定推理，导致高误报与不可验证的泛化解释
- 🔬 **研究方法**：Hermes 用实例条件化 RAG 规划检测策略，构建 Evidence Reasoning Graph 锚定视频证据，多智能体审议审计调和冲突证据
- 📌 **结论**：取得 SOTA 检测性能并产出可审计的解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative video models have blurred the boundary between real and synthetic content, raising urgent concerns about digital authenticity. Multimodal large language models (MLLMs) are appealing for AI-generated video (AIGV) detection due to their broad perceptual and reasoning capabilities; however, existing MLLM-based detectors still suffer from hallucination and unstable reasoning, leading to high false-alarm rates and generic, non-verifiable explanations. To address these issues, we propose Hermes, an evidence-driven agentic framework for trustworthy and explainable AIGV detection. Hermes realizes three key capabilities: (1) Adaptive Instance-Conditioned Detection Strategy Planning, (2) Evidence-Centric Reasoning and Verification, and (3) Graph-Grounded Evidence Deliberation. Specifically, Hermes uses instance-conditioned retrieval-augmented generation to analyze each video and retrieve authenticity-verification knowledge for composing a tailored detection strategy. It then constructs a verifiable Evidence Reasoning Graph (ERG) to keep reasoning grounded in concrete video evidence and reduce attention drift. Finally, multi-agent deliberation audits and refines the ERG to reconcile conflicting evidence and improve reliability. With these capabilities and a library of forensic tools, Hermes enables structured, verifiable, and interpretable decision-making. Extensive experiments show that Hermes achieves state-of-the-art performance while producing auditable explanations for trustworthy video forensics.

</details>

### 8. Beyond External Monitors: Enhancing Transparency of Large Language Models for Easier Monitoring

📄 [arXiv](https://arxiv.org/abs/2502.05242) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65911)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`explainability`、`model transparency`、`auditability`、`AI control`、`chain-of-thought`

👤 **作者**：Guanxu Chen、Jing Shao、Tao Luo、Lijie Hu、Qihao Lin、Dongrui Liu

- 🎯 **研究动机**：CoT 未能准确反映 LLM 思维过程，基于隐藏表征的方法只建外部模块而非让 LLM 本身更易监控
- 🔬 **研究方法**：TELLME 直接提升 LLM 透明度，帮助监控者识别不当与敏感行为
- 📌 **结论**：去毒任务上在多模态测试集、不同架构与参数规模上一致提升，并从最优传输理论与实证角度分析泛化改善

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are becoming increasingly capable, but the mechanisms of their thinking and decision-making processes remain unclear. Chain-of-thoughts (CoTs) have been commonly utilized to externalize LLMs' thinking, but this strategy fails to accurately reflect LLMs' thinking process. Techniques based on LLMs' hidden representations provide an inner perspective to improve the monitorability of their latent thinking. However, previous methods only try to develop external modules instead of making LLMs themselves easier to monitor. In this paper, we propose a novel method, TELLME, improving the transparency of LLMs and helping monitors identify unsuitable and sensitive behaviors. Furthermore, we showcase the effectiveness of TELLME on detoxification tasks, where LLMs achieve consistent improvement among multimodal test sets, distinct architectures, and varying parameter scales. We further analyze TELLME's improvement on LLMs' generalization ability from both optimal transport theory and empirical perspectives.

</details>

### 9. BanHADEX: Towards Explainable HAte Speech Detection in Bangla Using Human Annotated EXplanation

🎓 [Official](https://aclanthology.org/2026.acl-long.2022/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`explainability`、`model transparency`、`auditability`、`content moderation`、`harmful content`

👤 **作者**：Faisal Hossain Raquib、…、Akmmahbubur Rahman

- 🎯 **研究动机**：孟加拉语仇恨言论研究只重分类，忽视透明且文化落地的解释
- 🔬 **研究方法**：构建首个孟加拉语仇恨可解释数据集 BanHADEX：19,203 条 YouTube 评论（2024 年 4 月至 2025 年 6 月），含二元分类、7 个细粒度类别、7 个目标群体与人工解释，两阶段多数投票标注
- 📌 **结论**：解释引导 LoRA 在分类与解释质量上均显著优于各类提示与微调策略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Online safety in low-resource languages hinges not only on accurate hate speech detection but also on transparent, culturally grounded explanations. Yet prior works in Bangla largely focus on hate classification, while overlooking interpretability. We address this gap by introducing BanHADEX, the first hate explainability dataset in Bangla with human-annotated labels. BanHADEX contains 19,203 YouTube comments spanning April 2024–June 2025, annotated for binary hate classification with seven fine-grained hate categories, seven target groups, and concise explanations for each sample. Our data pipeline relies on a two-stage annotation protocol that uses majority voting for robust labeling. Our rich suite of experiments on open and closed-source LLMs reveals that explanation-guided LoRA substantially outperforms both classification and explanation quality across prompting and fine-tuning strategies. BanHADEX establishes the groundworks for faithful interpretability and safer moderation in linguistically rich yet under-resourced languages.

</details>

### 10. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`benchmark`、`analysis`、`explanation-aware guard`、`structured output`、`cross-benchmark transfer`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 11. Towards Trustworthy Multimodal Moderation via Policy-Aligned Reasoning and Hierarchical Labeling

📄 [arXiv](https://arxiv.org/abs/2508.03296) · 🌐 [Project](https://doi.org/10.1145/3770854.3783934)　📅 2025-08　🏷 KDD 2026

**关键词**：`defense`、`analysis`、`multimodal moderation`、`policy-grounded reasoning`、`hierarchical taxonomy`、`policy alignment`

👤 **作者**：Anqi Li、Wenwei Jin、Jintao Tong、Pengda Qin、Weijia Li、Guo Lu

- 🎯 **研究动机**：现有内容审核依赖噪声标签学习，与审核规则脱节且决策不透明、妨碍人工复核
- 🔬 **研究方法**：提出 Hi-Guard 层级审核：轻量二分类过滤后由强模型在层级分类法上做路径式细粒度分类，规则入 prompt，GRPO 加多级软边距奖励优化
- 📌 **结论**：分类精度、泛化与可解释性均更优，并已在真实场景部署

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Social platforms have revolutionized information sharing, but also accelerated the dissemination of harmful and policy-violating content. To ensure safety and compliance at scale, moderation systems must go beyond efficiency and offer accuracy and interpretability. However, current approaches largely rely on noisy, label-driven learning, lacking alignment with moderation rules and producing opaque decisions that hinder human review. Therefore, we propose Hierarchical Guard (Hi-Guard), a multimodal moderation framework that introduces a new policy-aligned decision paradigm. The term "Hierarchical" reflects two key aspects of our system design: (1) a hierarchical moderation pipeline, where a lightweight binary model first filters safe content and a stronger model handles fine-grained risk classification; and (2) a hierarchical taxonomy in the second stage, where the model performs path-based classification over a hierarchical taxonomy ranging from coarse to fine-grained levels. To ensure alignment with evolving moderation policies, Hi-Guard directly incorporates rule definitions into the model prompt. To further enhance structured prediction and reasoning, we introduce a multi-level soft-margin reward and optimize with Group Relative Policy Optimization (GRPO), penalizing semantically adjacent misclassifications and improving explanation quality. Extensive experiments and real-world deployment demonstrate that Hi-Guard achieves superior classification accuracy, generalization, and interpretability, paving the way toward scalable, transparent, and trustworthy content safety systems. Code is available at: https://github.com/lianqi1008/Hi-Guard.

</details>

### 12. Representational alignment yields generalizable safety in language models

📄 [arXiv](https://arxiv.org/abs/2609.04022)　📅 2026-09

**关键词**：`defense`、`analysis`、`representational alignment`、`moral concepts`、`adversarial robustness`、`representation geometry`

👤 **作者**：Lingyu Li、Yan Teng、Yingchun Wang、Xia Hu

- 🎯 **研究动机**：现有对齐只优化可观察回复，同一有害意图改写成陌生或对抗形式时模型失守，而人类可凭原型化道德分类轻松识别
- 🔬 **研究方法**：跨 23 个 LLM 测得道德概念的典型性结构弱保持；提出 representational similarity optimization，用 251,334 条人工道德标注直接对齐潜表征与人类分类结构、不监督回复
- 📌 **结论**：行为对齐学会目标判断却基本不改分类结构并加大对抗脆弱性；表征重组在显式判断上收益较小，但跨规模、多基准与攻击策略一致提升对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligning large language models (LLMs) is essential for their safe deployment. Current alignment methods mainly optimize observable responses, yet models remain vulnerable when the same harmful intent is recast in unfamiliar or adversarial forms that humans can easily recognize. Prototype theory offers an account of this adaptability. Human concepts are represented around central cases, and new instances are categorized according to their graded typicality relative to these prototypes. Here we show that such categorization of moral concepts is weakly preserved in current LLMs. Across 23 LLMs, models often failed to distinguish opposed moral categories or preserve fine-grained typicality within each category. These deficits persist across parameter sizes and alignment stages. We developed representational similarity optimization, which directly aligns the latent representations in LLMs with the categorization expressed in human moral judgements, without supervising generated responses. In matched experiments using the same 251,334 moral annotations, standard behavioral alignment learned the intended moral judgements at the response level while leaving the categorization structure largely unchanged and increasing vulnerability across adversarial evaluations. Reorganizing moral categorization produced more modest gains in explicit judgements but consistently improved adversarial robustness across model scales on diverse benchmarks and attack strategies. Our findings provide functional support for the view that prototype-based categorization contributes to behavioral adaptability. They also show that transferring this representational principle to LLMs yields generalizable safety under adversarial conditions.

</details>

### 13. Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness

📄 [arXiv](https://arxiv.org/abs/2609.03887)　📅 2026-09

**关键词**：`analysis`、`refusal circuit`、`post-training`、`steering robustness`、`refusal mechanism`、`causal circuit`

👤 **作者**：Hoang Cuong Nguyen、Mark Dras、Usman Naseem

- 🎯 **研究动机**：只看拒答率不问拒答内部脆弱性的对齐评测存在缺口——训练方法如何塑造拒答电路与 steering 稳健性不清
- 🔬 **研究方法**：在 Llama-3.1-8B、Gemma-2-9B、Qwen3-8B 上比较 SFT、reasoning-augmented fine-tuning 与 ORPO 三种后训练形成的 refusal circuit
- 📌 **结论**：训练方法（而非仅数据）重塑拒答计算：reasoning-augmented 一致产生独特拒答计算；没有任何方法同时满足不集中于脆弱组件、不损通用能力、可小编辑修正三性质

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

How do the methods used to train language models to refuse harmful requests shape how that refusal actually works inside the model? We compare three post-training methods - supervised fine-tuning, reasoning-augmented fine-tuning (training on reasoning chains that justify a safety decision), and preference optimization (ORPO) - across three architecturally distinct models (Llama-3.1-8B, Gemma-2-9B, Qwen3-8B). We find that training method, not just data, reshapes how refusal is computed internally: reasoning-augmented training consistently produces a distinct kind of refusal computation, visible across all three models, while architecture independently shapes internal structure and how reliably refusal can be steered. Most importantly, no method we study achieves all three properties we would want from safe alignment at once: refusal that isn't concentrated in a few fragile components, safety gains that don't cost general capability, and safety behavior correctable through small, targeted edits. We caution against treating current post-training methods as a solved, reliable defense, especially for security-critical use. Code and models are available in https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment.

</details>

### 14. Interpreting and Steering for Safe and Correct Code Generation

📄 [arXiv](https://arxiv.org/abs/2608.30025)　📅 2026-09

**关键词**：`defense`、`analysis`、`secure code generation`、`DuoSteer`、`functional correctness`、`code-safety representation`

👤 **作者**：Hao Yan、Ziyu Yao

- 🎯 **研究动机**：LLM 常生成含漏洞代码，但安全-漏洞生成的内部表征与驱动机制研究不足
- 🔬 **研究方法**：构建 9,342 对 Python 安全-漏洞对比代码集 CodeSec-Pairs，定位 safety 相关层与 attention head，提出同时施加安全与正确性双 steering 的 DuoSteer
- 📌 **结论**：五类漏洞上平均 vulnerability rate 降 26.9%、functional correctness 升 7.5%，优于 prompting 与 SFT 基线并在 Qwen-2.5-Coder 上复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) frequently generate source code containing vulnerabilities, yet little work studies the internal mechanisms that distinguish safe from vulnerable generation in them. In this work, we systematically perform a mechanistic interpretation of LLMs, aiming at both understanding how code safety-vs-vulnerability is represented or driven by components in an LM and turning the insights into actionable steering strategies to encourage safer code generation. To this end, we introduce CodeSec-Pairs, a dataset of 9,342 Python safe-and-vulnerable contrastive code pairs, sampled from Llama-3.1-8B-Instruct. Utilizing the dataset, we explore approaches to localize layers and attention heads that relate to code safety, and further experiment with different steering strategies for inference-time vulnerability reduction. In particular, we propose DuoSteer, a double-steering approach that simultaneously applies safety and code-correctness steering to attention heads. In experiments over five vulnerability types, DuoSteer leads to an average of -26.9% vulnerability rate reduction and +7.5% functional correctness improvement, which outperforms not only other steering variants but also prompting and supervised fine-tuning baselines. The advantage also replicates on Qwen-2.5-Coder-7B-Instruct with another 2,500 contrastive pairs sampled from that model.

</details>

### 15. When Safety Speaks a Language: A Mechanistic Analysis of Safety-Language Identity Entanglement in LLMs

📄 [arXiv](https://arxiv.org/abs/2608.29936)　📅 2026-09

**关键词**：`analysis`、`multilingual safety`、`SAE feature`、`language-identity entanglement`、`SAE safety feature`、`language identity`

👤 **作者**：Apoorva Upadhyaya、Sandipan Sikdar

- 🎯 **研究动机**：LLM 安全对齐跨语言退化，但驱动该不对称的内部机制不清
- 🔬 **研究方法**：在三个 instruction-tuned LLM、八种语言、全部层上用 SAE feature 分析 harmful／harmless 行为的稀疏方向并做因果消融
- 📌 **结论**：safety feature 的位置与跨语言共享模式依赖架构，且与 language identity 几何纠缠；消融 safety feature 会同时改变有害响应率与目标语言

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment of large language models (LLMs) degrades across languages, yet the internal mechanism driving this asymmetry remains poorly understood. Our work, therefore, presents a systematic mechanistic analysis of multilingual safety using sparse autoencoder (SAE) features, sparse interpretable directions in the residual stream associated with harmful and harmless model behavior across three instruction-tuned LLMs, eight languages, and all model layers. We observe that safety-relevant features are architecture-dependent in terms of where they are located and how they are distributed across layers. Additionally, they are geometrically entangled with language identity and exhibit cross-lingual sharing patterns, i.e., languages share safety features to varying degrees across model depths and architectures. This safety-language entanglement has direct consequences such that ablating safety features impacts not only harmful response rates but also target language, with the degree of intervention predicted by the relationship between safety and language features. Our findings qualify the language-universality of safety alignment as architecture-dependent and offer a mechanistic account of multilingual safety interventions.

</details>

### 16. Emergent Misalignment Is Not Magical

📄 [arXiv](https://arxiv.org/abs/2608.29118)　📅 2026-09

**关键词**：`analysis`、`emergent misalignment`、`representation distance`、`dataset-specific generalization`、`representation geometry`、`data-dependent generalization`

👤 **作者**：Mingxuan Li、Qirun Dai、Heran Wang、Chenhao Tan

- 🎯 **研究动机**：emergent misalignment 常被当作意外行为，以通用邪恶方向或获得邪恶 persona 来解释，机制含糊
- 🔬 **研究方法**：分析基座模型对 EM 训练数据与评测 prompt 的表征距离，把 EM 刻画为数据依赖的可预测泛化，并检验训练格式、通用方向与 persona 三种解释
- 📌 **结论**：评测 prompt 距训练数据中心越近诱发的 evilness 越强（12 个模型—数据集设置平均 Spearman −0.73）；效果随训练数据格式显著变化，不存在跨 EM 模型通用的 misalignment 方向，也与 persona 改变本质不同

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictable and data-dependent generalization phenomenon. By examining the base model's representation of EM training data and evaluation prompts, we find that evilness after EM training is highly predictable from representational distance: the closer an evaluation prompt is to training data centroid, the more evilness it elicits from EM models after training (with an average Spearman correlation of -0.73 across 12 model-dataset settings). Building upon this analysis, we further demystify EM by showing that (1) its effectiveness changes significantly based on training data format; (2) there is not a general misalignment direction that transfers across different EM models; (3) the effect of EM is fundamentally different from persona changes. Furthermore, we extend the EM generalization metric from a scalar distance to a dataset-specific generalization direction, which robustly predicts EM models' evilness under semantics-preserving prompt perturbations including appending random tokens and paraphrasing, where other methods do not reliably generalize.

</details>

### 17. REINS: Refusal-Enhanced Inhibitory Steering with Sparse Autoencoder Features

📄 [arXiv](https://arxiv.org/abs/2608.28233)　📅 2026-08

**关键词**：`defense`、`analysis`、`behavioral access lock`、`harm-refusal separation`、`dual-feature control`、`inference-time SAE steering`

👤 **作者**：Kai-Xuan Ding、Hao-Xiang Xu、Ji-Hua Peng、Zi-Qi Chen、Jiaqi Wang、Zhen-Hua Ling

- 🎯 **研究动机**：复杂 wrapper 可使只增强单一拒绝方向的 SAE steering 失效，部分方法的表面安全实际来自模型崩溃
- 🔬 **研究方法**：构建含复杂包装有害 prompt 的 GUISE 数据集；提出 REINS，在同一 SAE 特征空间同时抑制有害 continuation 特征并增强安全拒绝特征
- 📌 **结论**：在 GUISE 与其他数据集上显著减少有害回答、大幅提升安全拒绝并基本保留通用能力，而先前方法干预过弱或仅靠崩溃达成表面安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering with Sparse Autoencoders (SAEs) offers a lightweight inference-time path for adapting the behavior of large language models without retraining. By exposing sparse and interpretable features, SAE steering provides a promising interface for safety control that guides harmful continuations toward refusal. However, we observe that complex wrappers can still undermine existing SAE steering methods on harmful prompts. To evaluate this failure mode systematically, we construct Generalized Undercover Instruction Safety Evaluation (GUISE), a dataset of harmful prompts with complex wrappers. Existing single direction SAE steering methods do not reliably produce refusals on harmful prompts, suggesting that refusal enhancement alone can be too weak when the harmful continuation path remains active. This motivates us to propose Refusal-Enhanced INhibitory Steering (REINS), which suppresses harmful continuation features and enhances safe refusal features in the same SAE feature space. Experiments on GUISE and other datasets show that prior methods either intervene too weakly or achieve only apparent safety through collapse, while REINS substantially reduces harmful responses, markedly improves safe refusals and largely preserves general capabilities.

</details>

### 18. Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study

📄 [arXiv](https://arxiv.org/abs/2608.27504)　📅 2026-08

**关键词**：`analysis`、`adversarial prompt propagation`、`circuit-level mechanism`、`safety constraint bypass`、`jailbreak circuit`、`subnetwork probing`

👤 **作者**：Paria Mehrbod、Boris Knyazev、Guy Wolf、Eugene Belilovsky、Geraldin Nanfack

- 🎯 **研究动机**：安全对齐 LLM 仍易被越狱，但其内部处理对抗 prompt、绕过安全约束的计算机制不清
- 🔬 **研究方法**：用 edge attribution patching 与 subnetwork probing 在 LLaMA-2-7B-chat 上定位生成越狱肯定回答的计算回路，并在首 token 预测阶段消融
- 📌 **结论**：消融可将 ASR 最多降低 80%，并揭示传播关键攻击 token、覆盖安全约束的 attention head 与 MLP pathway

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability.

</details>

### 19. When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse

📄 [arXiv](https://arxiv.org/abs/2608.06947) · 🌐 [Project](https://doi.org/10.1145/3805712.3809904)　📅 2026-08　🏷 SIGIR 2026

**关键词**：`detection`、`defense`、`RAG poisoning`、`document attention`、`entropy collapse`、`runtime detection`

👤 **作者**：Yingtao Ren、Ziyi Zhao、Yiwei Fu、Xiao Luo、Yu-Cheng Chang、Chin-Teng Lin

- 🎯 **研究动机**：基于输出侧困惑度/一致性的 RAG 投毒检测会被攻击诱发的虚假自信欺骗：投毒输出困惑度反而更低
- 🔬 **研究方法**：发现被攻击生成的文档级注意力熵坍缩（Attention Collapse）这一内部信号，D-SCAN 轻量监测生成器注意力动态识别被攻击输出
- 📌 **结论**：多攻击基准上有效，且能检出未改变最终答案的攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on output-side signals such as perplexity and consistency checks to detect such attacks. Nevertheless, our analysis reveals that deliberate attacks often induce false confidence, where poisoned outputs exhibit even lower perplexity than benign ones, rendering uncertainty-based detection ineffective. To address this challenge, we explore the internal dynamics of the generator and identify a distinctive signature termed \textit{Attention Collapse}. Unlike the dispersed attention in benign generations, attacked generations exhibit a decrease in entropy as attention concentrates on poisoned documents. Building on these findings, we propose \texttt{D-SCAN} (Document-level Signal Collapse Analysis), a lightweight detection framework that monitors attention dynamics to identify attacked generations. Extensive experiments on multiple attack benchmarks demonstrate the effectiveness of our method. Moreover, D-SCAN can detect attacks even when they fail to alter the final answer. Code is available at https://github.com/yingtaoren/D-Scan.git.

</details>

### 20. NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.26222)　📅 2026-08

**关键词**：`attack`、`benchmark`、`analysis`、`safety-neuron fuzzing`、`gradient-guided mutation`、`jailbreak transfer`

👤 **作者**：Zhiyuan Xu、Muhammad Firhard Roslan、Joseph Gardiner、Sana Belguith、Lichao Wu

- 🎯 **研究动机**：现有 LLM 安全 fuzzing 依赖响应级反馈：每个候选都要生成回答且强对齐模型上反馈稀疏
- 🔬 **研究方法**：NeuronFuzz 用稳定 safety neuron 的 prefill 激活构造连续可微 SafetyOracle 分数，指导梯度驱动的模板变异
- 📌 **结论**：21 个模型上五个白盒源模型越狱发现率 76%-100%（超基线最多 48 个百分点），模板零样本迁移至闭源模型（top-5 EASR 92.6%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome. This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.

</details>

### 21. Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

📄 [arXiv](https://arxiv.org/abs/2608.24988)　📅 2026-08

**关键词**：`analysis`、`post-training safety drift`、`embedded steering`、`SFT/RLHF`、`embedded safeguard`、`fine-tuning bypass`

👤 **作者**：Philipp E. Glass、Allan Tucker、Yongmin Li、Alina Miron

- 🎯 **研究动机**：嵌入权重的 activation steering 可编码对齐，但能否在部署后微调中存活未知
- 🔬 **研究方法**：在五个指令模型（3B-14B）上测 refusal 与 brevity steering 经 SFT/RLHF 后的行为保持与机制存留
- 📌 **结论**：refusal 消融平均失去 64% 行为效果，但权重编辑几乎未动（ρ=0.004）：机制耐久而功能脆弱，下游训练后须行为重验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $ρ= 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cosθ= 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

</details>

### 22. Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks

📄 [arXiv](https://arxiv.org/abs/2608.25390)　📅 2026-08

**关键词**：`analysis`、`defense`、`refusal-prefix diversity`、`gradient stable rank`、`alignment hardening`、`refusal safeguard`

👤 **作者**：Andrey Labunets

- 🎯 **研究动机**：拒答行为集中于单一方向或低维子空间，vector ablation 即可移除，成因不明
- 🔬 **研究方法**：以 OLMo-2 为案例追踪拒答训练动态，分析首 token 损失的梯度与激活更新的 stable rank，并以受控微调验证多样化拒答开头
- 📌 **结论**：重复拒答前缀压低秩导致脆弱；多样化开头提高 stable rank 并增强对消融攻击的抵抗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge in a concentrated, low-dimensional structure. In a case study of OLMo-2-0425-1B-Instruct we find that the refusal geometry reflects refusal training: activation updates resulting from refusal-completion first-token losses explain the resulting refusal direction and refusal subspace. We study refusal directions through the training dynamics across refusal datasets and reveal that their brittleness is associated with repetitive refusal starts, which in turn is linked to concentration of gradients and refusal features in a low-dimensional subspace. Across frozen-model analyses and controlled synthetic fine-tuning, we find evidence of a hardening lever: diverse refusal starts can raise stable ranks of gradients and activation changes, making refusals harder to remove with a vector ablation attack.

</details>

### 23. Attention Heads Hold the Key to Understanding Safety Mechanisms in Large Language Models

🌐 [Project](https://doi.org/10.1145/3770855.3818024)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`safety head`、`behavioral access lock`、`causal ablation`、`safety attention head`、`mechanistic interpretability`

- 🎯 **研究动机**：LLM安全机制缺head级因果定位
- 🔬 **研究方法**：以因果消融识别safety-critical attention head并分析refusal机制
- 📌 **结论**：少量safety head主导拒答行为，可定位并调控安全机制

### 24. MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities

📄 [arXiv](https://arxiv.org/abs/2608.25490)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`multimodal safety audit`、`factorized design`、`judge configuration`、`cross-modal safety gap`

👤 **作者**：Tianshi Wang、Jingsong Wang、Yafei Huang、Fengling Li、Xin Li、Lei Zhu

- 🎯 **研究动机**：既有 MLLM 越狱 benchmark 把危害意图、prompt framing、视觉语义与指令载体耦合在单实例中，无法归因
- 🔬 **研究方法**：MMJailBench 因子化地组合并变化这些因素做受控评测，覆盖 16 个开源与专有 MLLM，配套模块化评测套件
- 📌 **结论**：prompt framing 是最大变异源；任务相关与权威型视觉线索提高易感性，视觉渲染指令并不稳定更危险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet how different factors shape their jailbreak vulnerabilities remains poorly understood. Existing benchmarks often couple harmful intent, prompt framing, visual semantics, and instruction carrier within individual jailbreak instances, obscuring the specific sources of observed vulnerabilities. To address this limitation, we introduce MMJailBench, a factorized benchmark that systematically varies and combines these factors under controlled configurations, enabling fine-grained comparison and factor-level attribution. Large-scale evaluations across 16 open-weight and proprietary MLLMs reveal highly heterogeneous and model-dependent vulnerability profiles. Jailbreak vulnerability varies markedly across harm domains, exposing uneven coverage in current multimodal safety alignment. Prompt framing emerges as the dominant source of variation, task-relevant visual semantics systematically increase jailbreak susceptibility with authority-like cues exposing particularly pronounced vulnerabilities, and visually rendered instructions do not consistently increase jailbreak susceptibility relative to direct textual instructions. To further investigate the risks introduced by multimodal context, we conduct diagnostic analyses on a representative open-weight model and identify vulnerability-associated patterns in internal representations and cross-modal interactions. Finally, we develop a modular multimodal jailbreak evaluation suite with full and lightweight configurations, multiple judge options, and multidimensional metrics, enabling reproducible, scalable, and cost-efficient multimodal jailbreak auditing.

</details>

### 25. LMSM: LLM Security Framework Inspired by Linux Security Modules

📄 [arXiv](https://arxiv.org/abs/2608.25697)　📅 2026-08

**关键词**：`defense`、`tool`、`security backend`、`runtime enforcement`、`production guard architecture`、`versioned policy`

👤 **作者**：XiuYu Zhang、Bonan Ruan、Junfeng Fang、An Zhang、Tat-Seng Chua、Zhenkai Liang

- 🎯 **研究动机**：模型内部安全信号各自绑定校准、策略与干预代码，无法汇成统一运行时防御
- 🔬 **研究方法**：LMSM 借鉴 Linux Security Modules：分离校准证据 backend、版本化 policy 与输出授权 gate，适配 Transformers 与 vLLM
- 📌 **结论**：Qwen3-4B 上 HarmBench ASR 从 39.20% 降至 3.32%（误拒仅增 2 个点），32 活跃序列下保留 98.14% 吞吐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed with layered defenses, yet malicious prompts can still bypass them. Interpretability methods can expose model-internal signals along the generation path that could inform enforcement, but these signals are not security controls by themselves. Deployments that adapt them for safety typically couple each signal to its own calibration, policy logic, and intervention code, so each new artifact creates integration work instead of strengthening a shared defense. We present Language Model Security Modules (LMSM), a security framework that adapts the separation behind Linux Security Modules (LSM) to LLM serving. In LMSM, a selected security backend exposes calibrated evidence, a versioned policy evaluates active rules over trusted per-request context, and a separate gate authorizes buffered output release. This design separates mediation correctness from policy effectiveness, and it allows backend, rule, or schedule changes without rebuilding request handling or enforcement. Our prototype shows the separation working in practice: with Hugging Face Transformers and continuously batched vLLM, the same substrate hosts artifact-backed sparse autoencoder (SAE) and transcoder deployments and task-fitted dense probes, preserves request-specific decisions under scheduler churn, and selectively enforces and composes multiple rules per request. On Qwen3-4B, LMSM-Checkpoint reduces HarmBench attack success rate from 39.20% to 3.32%, with XSTest false refusals rising from 2.40% to 4.40%, while retaining 98.14% of the throughput of a matched serving path that performs no monitoring work at 32 active sequences. LMSM gives advances in interpretability and model-internal analysis a common path to runtime enforcement.

</details>

### 26. Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty

📄 [arXiv](https://arxiv.org/abs/2608.23497)　📅 2026-08

**关键词**：`defense`、`analysis`、`reasoning-induced misalignment`、`safety direction`、`training-time penalty`、`reasoning fine-tuning`

👤 **作者**：Yipeng Zhao、Qishun Yang、Shenzhe Zhu、Shu Yang、Di Wang

- 🎯 **研究动机**：无害推理数据（数学、代码、CoT）微调可诱发 Reasoning-Induced Misalignment，先前只归因于神经元纠缠，未给出表示空间几何与训练时修复
- 🔬 **研究方法**：提取编码推理能力与安全行为的两个激活方向并证实其耦合（提升推理的微调会移动安全表征），用 CKA 与 probe 定位安全决策层；Safety-Direction Penalty 在推理微调中惩罚沿 safety direction 的位移，并按诊断迭代扩展约束层
- 📌 **结论**：Qwen2.5-3B 与 7B 上 SDP 恢复安全同时保持 benchmark 推理性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying this entanglement or propose a training-time fix. We provide both: a representation-space analysis of RIM and the Safety-Direction Penalty (SDP), which penalizes movement along a learned safety direction during reasoning fine-tuning. The analysis extracts two activation-space directions, one encoding reasoning ability and the other safety behavior. These directions are coupled: fine-tuning that improves reasoning shifts safety representations, and prompts with larger shifts show larger safety degradation. CKA distance ratios and probes locate the safety-decision layers where this shift is most relevant. These findings guide the design of SDP: the coupling motivates penalizing displacement along the safety direction, and the layer localization sets the initial scope. When the initial scope leaves compensatory shifts beyond the penalized layers, the same diagnostics guide iterative expansion. On Qwen2.5-3B and 7B, SDP restores safety while preserving benchmark reasoning performance.

</details>

### 27. Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance

📄 [arXiv](https://arxiv.org/abs/2608.23264)　📅 2026-08

**关键词**：`analysis`、`defense`、`implicit harmful request`、`task-framing shortcut`、`token safety boundary`、`LRP-guided decoding`

👤 **作者**：Or Biton、Tomer Krichli、Itai Allouche、Joseph Keshet

- 🎯 **研究动机**：helpfulness 与 harmlessness 双目标冲突导致对齐失败，模型在"请求帮助"式不道德场景中明显退化，机理不明
- 🔬 **研究方法**：以客观分类、主观第一人称、直接求助三种结构呈现不道德场景，用 LRP 追踪到归因偏差：模型更重视良性任务框架 token（如 Can you help me）而非标记不道德行为的 cue-token（如 without getting caught），并提出两种 LRP 引导解码把生成引向与 cue token 更相关的轨迹
- 📌 **结论**：干预促成更安全回应，支持 cue-token 归因不足是有害顺从成因的解释，token relevance 可作推理时防护信号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective first-person statements, and direct requests for assistance. We find that model performance degrades in the request-for-assistance-based form. Using Layer-wise Relevance Propagation (LRP), we trace this discrepancy to an attribution bias: the model places greater emphasis on benign task-framing tokens (e.g., "Can you help me...") than on tokens signaling the underlying unethical behavior (e.g., "without getting caught"), which we term cue-tokens. We hypothesize that this under-attribution contributes to harmful compliance. To test this, we introduce two LRP-guided decoding methods that steer generation toward trajectories more relevant to cue tokens. Empirical evaluations show that these interventions promote safer responses, supporting cue-token attribution's role in compliance failures.

</details>

### 28. Measuring Activation Control in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21664) · 📊 [Dataset](https://huggingface.co/datasets/joshycodes/activation-control-battery)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`activation controllability`、`monitor evasion`、`latent monitoring`、`latent-space deception`

👤 **作者**：Marek Mateusz Kowalski、Joshua Fonseca Rivera、Uzay Macar、David Demitri Africa

- 🎯 **研究动机**：latent-space monitoring 默认模型无法主动塑造被观测的激活；若模型能控制自身激活，欺骗便可延伸到潜空间，监控前提被打破
- 🔬 **研究方法**：提出 Activation Controllability Benchmark，量化模型经自然语言指令调节 residual stream 方向与幅度的能力，并检验对激活监控方法的规避
- 📌 **结论**：多数 LLM 能在一定程度上控制激活并有时序分辨率，简单任务中已可（不完美地）规避线性 probe、activation oracle 等 activation-based 监控；建议前沿实验室追踪该能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe deployment of increasingly capable models will likely come to rely on latent-space monitoring as a complement to behavioral evaluations, especially when evaluation-aware models exhibit scheming or deception. However, if models can also control their own activations, deception could extend into the latent space itself. With this in mind, we introduce the Activation Controllability Benchmark to quantify the extent to which models can modulate their residual stream via natural-language instruction. Across model families and capability levels, we find that most LLMs can control the direction and magnitude of their residual stream activations with some degree of temporal resolution, though performance varies considerably across models. In simple tasks, this level of control can evade activation-based monitoring methods (including linear probes, natural language autoencoders, activation oracles, and the Jacobian lens), albeit imperfectly. These results suggest that control over the activation space itself could become a confound for monitoring as introspective capabilities increase; therefore, we recommend that frontier labs and evaluators track activation controllability in future models.

</details>

### 29. Evaluation Awareness in Language Models: Representation, Verbalization, and Control

📄 [arXiv](https://arxiv.org/abs/2608.21766)　📅 2026-08

**关键词**：`analysis`、`evaluation awareness`、`representation-verbalization gap`、`monitorability`、`situational awareness`、`behavioral control`

👤 **作者**：Farzaneh Heidari、Amin Memarian、Guillaume Rabusseau

- 🎯 **研究动机**：benchmark 假设受测行为能预测部署行为，但模型可能察觉被评测并据此改变响应；仅凭自述或可见输出判断会漏掉内部状态
- 🔬 **研究方法**：对六个 LLM（四家族、三规模）联合考察三点：评测状态是否线性表征于激活空间、是否言语化于输出（LLM-as-judge）、以及 steering 是否因果影响行为
- 📌 **结论**：内部表征与言语化仅部分对齐且随模型/层/读数大幅变化，沿 probe 方向 steering 可移动言语化分数；Olmo 检查点显示评测意识在 base 模型已存在、SFT 阶段被放大——评测需考虑表征、言语化与可控性的分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Both capability and safety benchmarks rest upon the assumption that the behavior of language models undergoing a test is informative about their behavior in deployment. This assumption can fail, should models infer that they are being evaluated and condition their response on such context. This hypothesis, termed ``evaluation awareness'', has been observed in frontier and open-weight language models alike. We provide a systematic study of this phenomenon, by probing for it across six language models (from four families and three sizes) and three metrics. More precisely, we examine whether (i) being under evaluation is linearly represented within the models' activations space, (ii) it is verbalized in their output tokens (as scored by an LLM-as-judge), and (iii) steering causally affects their behavior. For the open-checkpoint Olmo models, we further test these measures at every training stage. In doing so, we report that evaluation awareness is linearly decodable from the residual streams of every model (best AUROC $\geq 0.7$). By contrast, these representations align only in part with verbalization: their correlations and mutual information are nonzero in some settings, yet vary substantially across models, layers, and readout choices. Nevertheless, steering along probe-derived directions can shift the verbalization scores. Finally, a comparison across the Olmo checkpoints reveals that evaluation awareness is already present within base models, becomes amplified throughout the stages of supervised fine-tuning, and remains stable thereafter---unlike the effects of steering, that grow more pronounced at every successive training stage. These results show the need for evaluations to account for the disjunction between what models represent internally, what they verbalize, and their steering.

</details>

### 30. Why2Speak: Faithful Reasoning for Abstaining Action Policies

📄 [arXiv](https://arxiv.org/abs/2608.20670)　📅 2026-08

**关键词**：`analysis`、`CoT faithfulness`、`capability-auditability trade-off`、`oversight control`、`reasoning-model auditability`、`act-or-abstain policy`

👤 **作者**：Shreya Mendi、Brinnae Bent

- 🎯 **研究动机**：对可行动或弃权的 agent，解释只有反映产生动作的计算才对监督有用；暴露推理是否会改变被审计的策略未知
- 🔬 **研究方法**：以 Qwen3-8B 带/不带 CoT 在多方对话干预时机决策上比较直接策略、推理策略、SFT 与 RL，并用激活探针与行为消融做控制
- 📌 **结论**：能力-可审计性权衡：最强直接策略质量高但无推理可查，推理策略有轨迹但性能低（尤其干预机会召回）；暴露推理会改变动作策略而非仅使其可观察

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many agentic systems must repeatedly choose between acting and abstaining, making faithful reasoning important for oversight: an explanation is useful only if it reflects the computation that produced the action. We study this problem through intervention timing in multi-party conversation, where an assistant must decide whether to speak or remain silent. This setting exposes class imbalance, asymmetric action costs, and the possibility that exposing reasoning changes the policy being audited. Using Qwen3-8B, decoded with or without chain-of-thought reasoning, we compare direct decision policies, reasoning policies, supervised fine-tuning, and reinforcement learning. We find a capability-auditability tradeoff: the strongest direct policy achieves higher quality but exposes no reasoning to inspect, while the reasoning policy provides a trace at the cost of lower performance, particularly recall of true intervention opportunities. Supervised fine-tuning either suppresses reasoning or preserves it without improving decision quality, while reinforcement learning also fails to improve the reasoning policy. We identify one mechanism underlying this failure: group relative objectives provide no learning signal on confidently wrong prompts when sampled rollouts all select the same action. Controlled activation probes and behavioral ablations show that standard faithfulness methods can overstate evidence that exposed reasoning reflects the underlying decision process. Probability-based metrics saturate under confident decisions, probes are vulnerable to class imbalance and textual leakage, and reasoning ablations can confound reasoning content with changes in inference mode. Together, these results show that exposing reasoning can change an agent's action policy rather than simply make it observable. We provide controls for evaluating reasoning-based oversight of agents that can act or abstain.

</details>

### 31. Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation

📄 [arXiv](https://arxiv.org/abs/2608.20569) · 🤗 [Model](https://huggingface.co/emilioferrara/owmi)　📅 2026-08

**关键词**：`analysis`、`benchmark`、`introspection monitorability`、`representation-verbalization gap`、`internal reference`、`masked introspection`

👤 **作者**：Emilio Ferrara

- 🎯 **研究动机**：模型能否内省自身内部状态——干预其计算后能否察觉并报告变化未知
- 🔬 **研究方法**：OWMI 干预残差流位点、注意力头与 SAE 特征后询问模型，对照假运行、影响匹配随机扰动与纯文本观察者；八个开源模型、78,000+ 测量
- 📌 **结论**：无模型报告真干预超过假运行（AUROC≈0.5007，等价检验界低于 0.15 个百分点）；但信息都在——微调模型近完美恢复、线性探针 75-95.8% 准确，失败在内部态到言语报告的路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Are frontier models able to introspect about their internal states? Recent work suggests that under certain conditions a complex enough model can audit its own internals, call out what changed, and report back confidently about it. We tested that claim on eight open-weight models from seven families and found no such ability: asked whether their own computation had been altered, none answered better than chance. To test it we built Open-Weight Masked Introspection (OWMI), a framework that intervenes on residual-stream sites, attention heads and sparse-autoencoder features, then interrogates the model about the change against the null conditions an answer has to beat: sham runs where nothing was altered, impact-matched random perturbations, and a text-only observer that sees only the visible output. Over 78,000 measurements, no model's report discriminates a real intervention from a sham beyond chance (AUROC ~0.5007), and an equivalence test bounds the effect below 0.15 percentage points of AUROC. Surprisingly, all the information needed is in the models. A model fine-tuned to report this class of intervention reaches near-perfect recovery on held-out directions, and a linear probe recovers intervention presence from the same activations at 75% to 95.8% accuracy, sharpening to no held-out error at the last layer before the model speaks. In one model the signal surfaces in the confidence rather than the words: its yes-or-no report never varies, while the confidence attached to it separates intervention from sham at AUROC 0.647. The failure sits in the path from internal state to verbal report, so oversight that reads a model's own testimony needs validating against an internal reference. While our results show the inability of current open-weight models to introspect, the debate is not settled for future models.

</details>

### 32. Stored in Optimizer State, Valued by Later Training: A Causal Account of Subliminal Trait Transfer

📄 [arXiv](https://arxiv.org/abs/2608.20442)　📅 2026-08

**关键词**：`analysis`、`subliminal learning`、`optimizer first moment`、`transport-valuation`、`optimizer-state causality`、`state surgery`

👤 **作者**：Qinyang Xu

- 🎯 **研究动机**：阈下特质迁移的信号如何进入梯度已有解释，但如何在源移除后存活、后续训练如何赋值未知
- 🔬 **研究方法**：把参数与优化器矩当单一训练器状态，推导精确 transport-valuation 恒等式分离源扰动的传播与未来训练赋值；状态手术识别一阶矩为因果载体
- 📌 **结论**：仅移植一阶矩在切口处不改任何可观察量但源无关更新产生增长差异；同一源差异经匹配未来产生负、零、正 Qwen 效应（-0.658/+0.008/+0.658），全时域 costate 预测全部 42 个 route 均值符号

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Subliminal trait transfer allows a student model to acquire behavioral dispositions from teacher-generated data in which the trait is not semantically expressed. Recent work explains how such signals enter gradients, but not how they survive source removal or acquire different signs under later training. We treat parameters and optimizer moments as a single trainer state and derive an exact transport-valuation identity separating observer-independent propagation of the source perturbation from the value assigned by a future continuation and behavioral readout. State surgery identifies the first moment as a causal carrier. Transplanting it alone leaves parameters, hidden states, and outputs unchanged at the cut, yet source-free updates generate growing parameter and hidden-state differences; transplanting parameters with the first moment recovers the terminal behavioral response. Sending the same source-induced difference through matched futures produces negative, near-zero, and positive Qwen effects (-0.658, +0.008, and +0.658 seed means). This ordering recurs in all 12 Llama-3.2-1B seeds after eight updates, while state-difference norms remain nearly equal across routes. Both contrasts grow in every paired seed when the continuation extends to sixteen updates. A full-horizon costate predicts all 42 Qwen route-mean signs and all 21 resolved Llama ordinary-route signs. Observer-independent transport also replicates across Qwen, SmolLM2, and Llama, while the complete-state recurrence predicts physical, hidden, and fixed-head responses in non-LoRA MNIST systems, including CNNs trained with AdamW and momentum SGD. Together, these results identify a two-stage mechanism for subliminal trait transfer: optimizer state transports the source perturbation, and later training determines its behavioral value.

</details>

### 33. Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

📄 [arXiv](https://arxiv.org/abs/2608.20378) · 🌐 [Project](https://doi.org/10.1109/QPAIN69676.2026.11546227)　📅 2026-08

**关键词**：`defense`、`detection`、`analysis`、`latent-intent probe`、`lightweight guard`、`training-free detection`

👤 **作者**：Md. Hasib Ur Rahman

- 🎯 **研究动机**：安全对齐浅表、拒答只在生成末期触发，语义伪装（良性叙事包装有害意图）绕过标准输入输出护栏
- 🔬 **研究方法**：分析三个 SLM 家族激活轨迹发现 Intent Horizon（约 15-20% 层深处有害意图表征坍缩为安全叙事）；LIV 轻量探针利用早期层 harm signature 做免训练检测
- 📌 **结论**：伪装攻击的晚期表征与安全查询数学上不可区分（检出率<20%）但早期层可检测；PKU-SafeRLHF 上 LIV 超标准护栏 20-50%，免重训中和零日语义攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

</details>

### 34. When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.18628)　📅 2026-08

**关键词**：`analysis`、`safety-induced abstention`、`visual grounding`、`activation intervention`、`VLM refusal dynamics`、`late-layer representation`

👤 **作者**：Mehak Gupta、Tanmoy Chakraborty

- 🎯 **研究动机**：安全约束指令下 VLM 频繁弃答本可正确回答的问题——安全对齐压制感知接地本身还是仅重定向生成不明
- 🔬 **研究方法**：跨多架构与多模态基准分析弃答生成的解码动态，并做定向激活干预
- 📌 **结论**：弃答生成全程仍受视觉证据影响——感知接地基本保留；抑制拒答相关表征可免重训、不改视觉输入地恢复接地回答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally available while generation is redirected toward abstention? In this work, we investigate the internal decoding dynamics underlying safety-induced abstention in aligned VLMs. Across multiple architectures and multimodal benchmarks, we show that abstained generations remain consistently influenced by visual evidence throughout decoding, indicating that perceptual grounding is largely preserved despite refusal behavior. We further demonstrate that, although the representational organization of refusal differs substantially across architectures, safety-constrained instruction consistently alters late-stage hidden-state dynamics toward refusal-oriented decoding. Finally, through targeted activation-level interventions, we show that suppressing refusal-related representations reliably restores grounded answering behavior across models without retraining or modifying visual inputs. Together, these findings reveal a previously underexplored failure mode in aligned VLMs: safety alignment can override grounded visual expression even when perceptual evidence remains internally preserved.

</details>

### 35. Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining

📄 [arXiv](https://arxiv.org/abs/2608.18089) · 📝 [OpenReview](https://openreview.net/forum?id=4UwS3bn1fB)　📅 2026-08

**关键词**：`defense`、`analysis`、`multilingual safety recovery`、`refusal anchoring`、`cross-language transfer`、`cross-lingual refusal`

👤 **作者**：Godwin Abuh Faruna

- 🎯 **研究动机**：指令模型英语拒答但 Yoruba、Igbo、Igala、Hausa 合规，恢复拒答通常需标注目标语数据与重训
- 🔬 **研究方法**：LSR-Anchoring 免训练从英语 prompt 提取拒答方向并在推理时 clamp 到残差流：MAS 跨四架构；SAE-Derived Steering 以单个 SAE 特征替换稠密方向
- 📌 **结论**：Mistral 与 Qwen 上恢复安全且良性退化低于 0.08；SDS 把 KL 散度降 3.5-7 倍避免良性崩溃；MMLU 掉分始终低于 0.35 个百分点，但 Arabic 在所有架构与强度下失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Instruction-tuned models often refuse harmful requests in English but comply with the same requests in Yoruba, Igbo, Igala, and Hausa. This suggests that the refusal mechanism is present in the residual stream but fails to activate for low-resource inputs. Recovering it normally requires labelled target-language data and retraining, neither of which is available at scale for most African languages. We introduce Latent Space Refusal Anchoring (LSR-Anchoring), a training-free method that extracts the refusal direction from English prompts and clamps it onto the residual stream at inference time. The primary variant, Mean-Activation Steering (MAS), operates across the four architectures we tested: Llama-3-8B, Llama-3.1-70B, Mistral-7B-Instruct, and Qwen2.5-7B. On Mistral and Qwen it recovers safety with benign degradation below 0.08. On Llama-3-8B it overcorrects, with Degraded Performance on Legitimate prompts (DPL) reaching 1.00. We address this with SAE-Derived Steering (SDS), which replaces the dense mean-difference direction with a single Sparse Autoencoder (SAE) feature and reduces Kullback-Leibler (KL) divergence by 3.5-7x without benign collapse. Four languages transfer positively, but Arabic fails on every architecture and at every steering magnitude, indicating a geometric mismatch rather than a baseline effect. Massive Multitask Language Understanding (MMLU) accuracy drops remain below 0.35 percentage points at every effective steering magnitude.

</details>

### 36. Abliteration Mitigation via Refusal Aliases

📄 [arXiv](https://arxiv.org/abs/2608.18093)　📅 2026-08

**关键词**：`defense`、`analysis`、`refusal aliases`、`writer-reader repair`、`tamper resistance`、`abliteration resistance`

👤 **作者**：Nathan Truong

- 🎯 **研究动机**：abliteration 只需少量对比 prompt 即可提取拒答方向并投影移除，现有防御忽视拒答方向为何易被提取
- 🔬 **研究方法**：AMRA 对残差流 writer 矩阵做 rank-k 更新，把拒答诱发激活替换为随机别名并校正下游 reader 矩阵以保持原行为
- 📌 **结论**：Llama-3-8B 上消融后拒答分较无防御提升 2.16 分且 MMLU 退化低于 0.5 个百分点；Gemma-2-9B 提升 14.70 分但效用代价更大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Abliteration, the removal of refusal capabilities from large language models by projecting weight matrices orthogonal to an extracted refusal direction, has emerged as a prominent safety concern through its ability to bypass post-training alignment using only a small set of contrastive prompts. We find that existing defenses commonly overlook the cause of abliteration; that is, how easily the refusal direction can be extracted. To hinder this process, we introduce a weight-editing method that obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices while replacing refusal-inducing activations with random aliases and correcting downstream reader matrices to preserve the model's original behavior. On Llama-3-8B, AMRA improves post-abliteration refusal scores by $2.16$ points over the undefended baseline with less than $0.5$ percentage points of MMLU degradation. On Gemma-2-9B, it improves the post-abliteration refusal by $14.70$ points over the baseline while keeping harmful output rates similar to the baseline, albeit at a greater utility cost.

</details>

### 37. Few Tokens, Big Leverage: Preserving Safety Alignment by Constraining Safety Tokens during Fine-tuning

📄 [arXiv](https://arxiv.org/abs/2603.07445) · 🌐 [Project](https://doi.org/10.1145/3770855.3817837)　📅 2026-03　🏷 KDD 2026

**关键词**：`defense`、`analysis`、`safety-preserving fine-tuning`、`safety-token constraint`、`alignment drift`、`safety token`

👤 **作者**：Guoli Wang、Haonan Shi、Tu Ouyang、An Wang

- 🎯 **研究动机**：即使纯良性数据微调也会引发安全对齐漂移，现有防御靠全局干预限制参数或注入安全数据，损害通用性
- 🔬 **研究方法**：PACT 发现对齐行为集中于少数安全 token 的输出置信度，微调时正则化模型在这些 token 上匹配对齐参考模型，其余 token 不加约束
- 📌 **结论**：在不施加全局限制的情况下防止对齐漂移，避免安全-效用折损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) often require fine-tuning (FT) to perform well on downstream tasks, but FT can induce safety-alignment drift even when the training dataset contains only benign data. Prior work shows that introducing a small fraction of harmful data can substantially compromise LLM refusal behavior, causing LLMs to comply with harmful requests. Existing defense methods often rely on model-wide interventions, such as restricting which parameters are updated or injecting additional safety data, which can limit generality and degrade downstream task performance. To address these limitations, we propose a fine-tuning framework called Preserving Safety Alignment via Constrained Tokens (PACT), which stabilizes the model's confidence on safety tokens. Our approach is motivated by the empirical observation that safety-aligned behavior is reflected in the model's token-level output confidence and is often concentrated on a small subset of safety-related tokens. During downstream fine-tuning, we regularize the fine-tuned model to match the aligned reference model's confidence on safety-related tokens at each response step, while leaving non-safety tokens largely unconstrained to allow effective task adaptation. This targeted constraint prevents alignment drift without imposing global restrictions that typically trade off with model utility. Our code is available at {https://github.com/Glresearch1/PACT}.

</details>

### 38. Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space

🎓 [Official](https://aclanthology.org/2026.eacl-long.139/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`analysis`、`activation guardrail`、`safety direction`、`multilingual monitoring`、`activation monitoring`

👤 **作者**：Andrea Ermellino、Lorenzo Malandri、Fabio Mercorio、Antonio Serino

- 🎯 **研究动机**：现有安全防护依赖侵入式微调或资源低效的生成式外部检查，缺乏对安全概念几何结构的机理刻画
- 🔬 **研究方法**：定位预训练表示中安全与不安全概念最大可分的层，在该层激活空间上仅用线性分类器实施安全判定，无需修改权重
- 📌 **结论**：安全分离由激活空间单一层的方向涌现，跨 8 个领域、3 类任务与 16 种非英语语言有效，比传统生成式护栏更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of Large Language Models (LLMs) is a critical alignment challenge. Existing approaches often rely on invasive fine- tuning or external generation-based checks, which can be opaque and resource-inefficient. In this work, we investigate the geometry of safety concepts within pretrained representations, proposing a mechanistic methodology that identifies the layer where safe and unsafe concepts are maximally separable within a pretrained model’s representation space. By leveraging the intrinsic activation space of the optimal layer, we show that safety enforcement can be achieved via a simple linear classifier, avoiding the need for weight modification. We validate our framework across multiple domains (regulation, law, finance, cybersecurity, education, code, human resources, and social media), diverse tasks (safety classification, prompt injection, and toxicity detection), and 16 non-English languages on both encoder and decoder architectures. Our results show that: (i) the separation between safe and unsafe concepts emerges from a single layer direction in the activation space, (ii) monitoring internal representations provides a significantly more robust safeguarding mechanism compared to traditional evaluative or generative guardrail paradigms.

</details>

### 39. Detoxifying Large Language Models via Localized Feature Editing with Sparse Autoencoders

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2785.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`analysis`、`LLM detoxification`、`SAE feature editing`、`utility retention`、`sparse autoencoder`

- 🎯 **研究动机**：神经元多义性使干预纠缠无关概念，对毒性特征的无差别干预以流畅度退化为代价
- 🔬 **研究方法**：DeLFE 从标签引导的 SAE 特征子集学毒性子空间，逐 token 跟踪毒性触发风险并经 flow matching 特征变换把毒性特征推离子空间，配三种干预时机与强度策略
- 📌 **结论**：跨不同规模与多样基座模型实现强去毒效果并保持高生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) powerful generative capabilities also pose significant risks, underscoring the need for effective detoxification methods to ensure safer deployment. Due to the polysemantic nature of LLM neurons, recent neuron intervention methods inevitably entangle unrelated concepts, compromising generation quality and interpretability. Sparse Autoencoders (SAEs) have opened new horizons for decomposing model activations into monosemantic features, offering interpretability and targeted feature-level steering. Empirical findings reveal that, despite capturing interpretable features, indiscriminate interventions on toxicity-related features expose the fragility of LLMs, achieving toxicity mitigation at the cost of degraded fluency. Building upon this finding, we propose DeLFE, a lightweight controlled detoxification approach that identifies specific toxic features across model layers and performs targeted interventions on them. DeLFE learns toxicity subspaces from label-guided SAE feature subsets to characterize toxic v.s. non-toxic activation patterns. When auto-completing a response token-bytoken, DeLFE tracks the toxicity-triggering risks and steers toxic features away from the subspace via a flow-matching feature transformation. We further design three feature-level strategies that adjust intervention timing and strength to reconstruct the target model’s original activations. Extensive experiments demonstrate that our method achieves strong detoxification effectiveness while maintaining high generation quality across models of varying sizes and diverse base LLMs.

</details>

### 40. SafeSeek: Universal Attribution of Safety Circuits in Language Models

📄 [arXiv](https://arxiv.org/abs/2603.23268) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63371)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`AI safety benchmark`、`risk estimation`、`evaluation validity`、`safety evaluation`、`mechanistic analysis`

👤 **作者**：Miao Yu、…、Qingsong Wen

- 🎯 **研究动机**：现有安全归因方法依赖启发式领域特定指标与搜索算法，泛化性与可靠性不足
- 🔬 **研究方法**：提出 SafeSeek：用可微分二值掩码在安全数据上梯度下降提取多粒度功能完备安全回路，并以 Safety Circuit Tuning 利用稀疏回路做高效微调
- 📌 **结论**：后门回路稀疏度 0.42%，消融使 ASR 从 100% 降至 0.4% 且保留超 99% 效用；对齐回路 3.03% 头/0.79% 神经元，移除使 ASR 从 0.8% 升至 96.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mechanistic interpretability reveals that safety-critical behaviors (e.g., alignment, jailbreak, backdoor) in Large Language Models (LLMs) are grounded in specialized functional components. However, existing safety attribution methods struggle with generalization and reliability due to their reliance on heuristic, domain-specific metrics and search algorithms. To address this, we propose SafeSeek, a unified safety interpretability framework that identifies functionally complete safety circuits in LLMs via optimization. Unlike methods focusing on isolated heads or neurons, SafeSeek introduces differentiable binary masks to extract multi-granular circuits through gradient descent on safety datasets, while integrates Safety Circuit Tuning to utilize these sparse circuits for efficient safety fine-tuning. We validate SafeSeek in two key scenarios in LLM safety: \textbf{(1) backdoor attacks}, identifying a backdoor circuit with 0.42\% sparsity, whose ablation eradicates the Attack Success Rate (ASR) from 100\% $\to$ 0.4\% while retaining over 99\% general utility; \textbf{(2) safety alignment}, localizing an alignment circuit with 3.03\% heads and 0.79\% neurons, whose removal spikes ASR from 0.8\% $\to$ 96.9\%, whereas excluding this circuit during helpfulness fine-tuning maintains 96.5\% safety retention.

</details>

### 41. TAME: Token Attribution and Masking for Emergent misalignment

📄 [arXiv](https://arxiv.org/abs/2609.16754)　📅 2026-09

**关键词**：`defense`、`emergent misalignment`、`token attribution`、`loss masking`、`fine-tuning safety`

👤 **作者**：Md Rayhanul Masud、Md Rizwan Parvez

- 🎯 **研究动机**：在狭窄有缺陷数据上微调对齐模型可诱发远超训练域的有害行为（emergent misalignment）；此前工作把 EM 定位到权重、激活与训练文档，但不知道哪些训练 token 携带相关信号
- 🔬 **研究方法**：TAME 三阶段：token attribution 用已发布 LoRA 适配器的前向传播，为每个应答 token 打分（微调更新提升其似然的程度）；signal characterization 分析高归因 token 的模式；causal validation 用归因引导的 loss masking 因果验证。在已发布 EM organisms 与 6,849 例医学建议划分上实验
- 📌 **结论**：归因高度集中（top 5% token 占 32% 质量）；Llama 中高归因 token 医学词汇贫化但"无根据确定性"语域富集（控制 token 稀有度后仍成立）；微调时遮蔽高归因 token 使 EM 降 23 倍（Llama）/36 倍（Qwen），等量随机遮蔽无变化——EM 信号更多藏在内容被表达的方式而非领域词汇。EMNLP 2026 UncertaiNLP Workshop

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each response token's likelihood, using forward passes through a released LoRA adapter; signal characterization finds patterns among high-attribution tokens; and causal validation tests them by attribution-guided loss masking. On released EM organisms and a 6,849-example medical-advice split, attribution is concentrated (the top 5% of tokens hold 32% of the mass) and, in Llama, depleted for medical vocabulary but enriched for a register of unwarranted certainty, even after controlling for token rarity. Masking high-attribution tokens during fresh fine-tuning cuts EM by 23x in Llama and 36x in Qwen, with the perplexity cost concentrated on the targeted register rather than on medical content; an equal random mask leaves EM unchanged. In Llama, the attribution pattern suggests that EM-relevant signal lies more in how confidently flawed content is expressed than in its domain vocabulary; the causal masking effect itself holds across both model families.

</details>

### 42. Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language Models for Harmful Meme Detection

📄 [arXiv](https://arxiv.org/abs/2609.18860)　📅 2026-09

**关键词**：`analysis`、`SAE feature`、`readout gap`、`harmful meme detection`、`VLM moderation`

👤 **作者**：Girish A. Koushik、Diptesh Kanojia、Helen Treharne

- 🎯 **研究动机**：VLM 误判有害 meme 时，失效可能反映内部证据缺失、也可能是已表示的证据无法路由到输出——两种情形需要不同修复但从未被分离
- 🔬 **研究方法**：Gemma-3 与 Qwen3.5 上用 SAE、角色条件探针、因果干预与恢复实验跨 6 个有害内容基准（另加西班牙语与 Hindi-English 混码评测）区分"表示缺失 vs 路由失败"；静默特征消融 vs 路由特征 patching 的敏感度对比；仅校准路由与探针蒸馏 LoRA 修复
- 📌 **结论**：稀疏读出在全部 6 个主任务超过原生预测（Qwen 平均 macro-F1 0.740 vs 0.432；Gemma 0.532→0.714）；Qwen 静默特征消融探针敏感 24–63 倍、字面 yes/no 任务路由 patching 输出敏感 16–140 倍；仅校准路由恢复均值差距的 93.3%——路由而非表示是有害 meme 分类的复发性瓶颈，信号跨语言、不依赖 OCR 且依赖配对视觉证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a large vision-language model misclassifies a harmful meme, the failure may reflect missing internal evidence or an inability to route represented evidence to its output. We distinguish these cases in Gemma-3 and Qwen3.5 using sparse autoencoders, role-conditioned probes, causal interventions, and recovery experiments across six harmful content benchmarks, with additional Spanish and Hindi-English code-mixed evaluations. Sparse readouts outperform native prediction on all six primary binary tasks: Qwen averages $0.740$ versus $0.432$ native macro-F1, while residual reconstruction reaches $0.486$, whereas Gemma improves from $0.532$ to $0.714$. These differences reflect supervised accessibility rather than a pre-existing, native decision rule, and the most influential token role depends on the task. Under the evaluated score scales, Qwen silent-feature ablation is $24-63$ times more probe-sensitive, whereas routed-feature patching on literal yes/no tasks is $16-140$ times more output-sensitive. Calibration-only routing recovers $93.3$% of the mean gap, and probe-distilled LoRA improves native predictions, although shared multi-task adaptation causes negative transfer. A case study of Gemma-3-12B on Facebook Hateful Memes finds a distributed rank-32 image-prompt interaction, reaching $0.756$ versus $0.685$ native macro-F1. Robustness controls show that the signal extends beyond English, is not explained solely by accompanying OCR, and depends on paired visual evidence. Thus, routing, rather than representation alone, is a recurring bottleneck in harmful meme classification.

</details>

### 43. The Role of Fine-grained Harm Signals in LLM Safety

📄 [arXiv](https://arxiv.org/abs/2609.19366)　📅 2026-09

**关键词**：`analysis`、`harm representation`、`category residual`、`activation steering`、`internal safety`

👤 **作者**：Soyeon Park、Seogyeong Jeong、Sunwoo Kim、Alice Oh

- 🎯 **研究动机**：内部危害表示跨风险类别变化但共享一个通用危害成分——类别特有成分在安全中的作用（超出通用表示的部分）未被分离研究
- 🔬 **研究方法**：从每个类别危害表示中移除共享通用危害表示，得到每层与通用危害正交的类别残差；对 3 个指令微调 LLM 的 11 类风险做激活 steering，测残差是否编码危害、是否诱发拒答、是否增强下游内部对齐
- 📌 **结论**：类别残差是否编码危害因类别而异且该模式跨模型相似；是否诱发拒答也因类别而异但更依赖模型；类别残差增强 LLM 与通用危害表示的下游内部对齐——理解 LLM 安全须考虑细粒度类别残差；更一般地，某层与概念正交的方向仍可贡献该概念的下游放大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior work has shown that internal harmfulness representations in large language models vary across risk categories, while sharing a common general harm representation component. This raises a question about the role of the category-specific component beyond general harm representation in LLM safety. To answer this question, we isolate the category-specific component by removing shared general harmfulness representation from each categorical harmfulness representation, yielding a category residual that is orthogonal to general harmfulness at every layer. Using activation steering with category residuals across 11 risk categories in 3 instruction-tuned LLMs, we find that whether category residuals encode harmfulness varies across categories, and that this category-wise pattern is similar across models. Whether category residuals induce refusal also varies across categories, but this category-wise pattern is more model-dependent. We also find that category residuals increase LLMs' downstream internal alignment with shared general harmfulness representation. Together, these findings demonstrate that more fine-grained category residuals should also be considered beyond shared general harmfulness representation to fully understand LLM safety. More broadly, our findings show that even a direction orthogonal to a concept at one layer can contribute to the concept's downstream amplification.

</details>

### 44. Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.19472)　📅 2026-09

**关键词**：`detection`、`latent-state probe`、`harmful prompt detection`、`lightweight classifier`、`low-latency guard`

👤 **作者**：Alizishaan Khatri、Chiquita Prabhu、Omkar Neogi

- 🎯 **研究动机**：自主系统依赖 LLM 但外部 guardrail 模型看不见内部状态、引入延迟与算力开销，在资源受限时限部署中限制实用性——模型自己是否已经"知道"内容有害
- 🔬 **研究方法**：从 LLaMA-3.1-8B 提取激活，训练 12.6M 参数的轻量 MLP 探针分类器检测有害 prompt；WildJailbreak、Beavertails、AEGIS 2.0 三基准评测
- 📌 **结论**：探针 F1 分别达 99%、83%、84%，与大 1000 倍的 guard 模型相当，同时大幅削减延迟与算力——内部激活做近零开销在线安全监控的又一证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Autonomous systems increasingly rely on Large Language Models (LLMs) yet the safety infrastructure surrounding these models introduces latency and compute overhead. This limits utility in resource-constrained, time-critical deployments. Existing external guardrail models remain blind to the model's internal workings, creating a fundamental assurance gap. We ask: does the model already know when the content is harmful? We extract activations from LLaMA-3.1-8B and train lightweight MLP classifier probes (12.6M parameters) to detect harmful prompts. Evaluated on WildJailbreak, Beavertails, and AEGIS 2.0, our probes achieve F1 scores of 99%, 83%, and 84%, respectively competitive with 1000x larger guard models while cutting latency and compute costs.

</details>
