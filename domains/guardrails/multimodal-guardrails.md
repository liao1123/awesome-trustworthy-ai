# 多模态 Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究对图像、文本-图像组合、视频、音频及 omni-modal 输入输出执行独立安全审核。与纯文本分类相比，多模态 guardrail 需要处理单一模态看似安全但组合后产生的隐式风险、视觉证据与文字指令冲突、跨帧语境、动态 policy、reasoning trace 本身的安全，以及 harmful input 仍可能得到 safe response 时的过度拒绝问题。

## 研究脉络

- **图像分类与 benchmark：** UnsafeBench、VLSBench 等工作先建立真实/生成图像分类与 visual leakage 评测，暴露通用 VLM 的输入安全盲区。
- **Policy-following guard：** SafeWatch、GuardReasoner-VL 和 SafeGuard-VL 从固定二分类转向读取 policy、定位视觉证据并生成可检查的 reasoning 或 explanation。
- **Classifier-side red teaming：** 研究开始用 context shift、T2I generation、简单图像变换、视觉走私与 agentic photo editing 主动搜索 image safety classifier 的 false negative，而不只测试固定违规图片。
- **组合与上下文风险：** CrossGuard、MiShield、LLaVAShield 和 EchoSafe 分别覆盖图文隐式意图、多图组合、多轮对话及 inference-time memory，判断对象从单张图扩展到完整上下文。
- **Omni-modal 与视频：** OmniGuard、GuardReasoner-Omni、SafeLens 和 UNIVID 将统一审核扩展到视频、音频与工业工作流，并用 token pruning、fast-and-slow routing 或 policy-aware caption 控制成本；生产研究开始把直播审核的 failure signature 映射到具体开发干预。
- **新攻击面与效用：** Unsafe Induction Attack 研究让安全图像被误判为有害的 availability attack，output-aware guardrail 则利用待生成响应的内部状态减少 over-refusal。

## Policy-Adaptive、Reasoning 与响应审核

### 1. SafeRI: Recognition and Intervention for Token-Level Safety Intervention in Large Vision Language Models

📄 [arXiv](https://arxiv.org/abs/2609.03544)　📅 2026-09

**关键词**：`defense`、`VLM guardrail`、`token-level risk`、`gated LoRA`、`VLM alignment`、`token risk`

👤 **作者**：Caoyuan Ma、…、Yinqiang Zheng

- 🎯 **研究动机**：VLM 安全对齐参数一经训练即全局常驻，对安全与已安全生成同时干预，扰动原有推理路径并损害多模态能力
- 🔬 **研究方法**：提出 SafeRI 流式识别加门控 LoRA：自回归生成中轻量识别器逐 token 判断前缀状态是否安全并更新下一步 LoRA 门，LoRA 由不安全前缀、过渡语句与安全延续训练，仅在激活后把生成导回安全响应
- 📌 **结论**：跨多个安全与通用基准验证按需干预在 post-alignment 设定下的有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing safety alignment methods for vision-language models usually modify the model behavior globally: once the safety parameters are trained or loaded, they participate in both unsafe and already-safe generations. This always-on intervention can unnecessarily perturb the model's original reasoning path and degrade general multimodal capabilities. We argue that safety alignment should be an on-demand intervention rather than a permanent modification to every decoding trajectory. To this end, we propose a streaming recognition and gated LoRA framework for intrinsic VLM safety. During autoregressive generation, a lightweight recognizer estimates whether the current pre-token generation state is safe or unsafe. Its output updates the LoRA gate for the following decoding step; otherwise, generation follows the frozen-backbone policy. The LoRA module is trained from unsafe prefixes, transition statements, and safe continuations, so that it learns to redirect unsafe generations back to safe responses after activation. Experiments across multiple safety and general-purpose benchmarks demonstrate the effectiveness of our method in post-alignment settings.

</details>

### 2. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

📄 [arXiv](https://arxiv.org/abs/2608.27548) · 🤗 [Model](https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety) · 📊 [Dataset](https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset)　📅 2026-08

**关键词**：`tool`、`compact guard model`、`prompt-response moderation`、`production deployment`、`multimodal moderator`、`image-conditioned safety`

👤 **作者**：Varun Singh、Anuj Doshi、Makesh Narsimhan Sreedhar、Shaona Ghosh、Katherine Luna

- 🎯 **研究动机**：部署场景的安全审核需覆盖图像、文档、生成回答与各域自定义策略，现有 guardrail 通常只覆盖部分设置，难以兼顾广覆盖、自定义策略与低算力
- 🔬 **研究方法**：发布 4B 视觉语言安全 moderator Nemotron 3.5 CS 及多模态多语言安全数据集，联合分类 12 种语言的 prompt、图像与回答；低延迟路径仅输出标签，按需生成应用自定义策略并指认违规类别的推理轨迹
- 📌 **结论**：在多模态安全、文本审核、跨语言鲁棒性、自定义策略遵循、良性误报与延迟评测中取得实用的覆盖—成本权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety moderation for deployed AI applications is moving beyond text-only prompts: systems increasingly need to judge images, documents, screenshots, and generated responses under policies that vary across domains. Existing guardrails usually cover only part of this setting, making it difficult to combine broad coverage, custom policy control, and low compute cost. We present Nemotron 3.5 Content Safety Moderator, also referred to as Nemotron 3.5 CS in this paper for brevity, a compact 4B vision-language safety moderator that jointly classifies user prompts, images, and assistant responses across 12 languages. Nemotron 3.5 CS returns safety labels for latency-sensitive moderation and can additionally produce concise reasoning traces that apply supplied custom policies and identify violated categories when reasoning is requested. We also release a multimodal and multilingual safety dataset for guard training, spanning human-labeled real-image moderation, benign vision-language and document tasks, synthetic rare-risk and jailbreak cases, and custom-policy examples. Across evaluations spanning multimodal safety, text moderation, multilingual robustness, custom-policy following, benign false positives, and latency, Nemotron 3.5 CS demonstrates a practical coverage tradeoff: it adds image-conditioned and policy-conditioned moderation while remaining broadly competitive with specialized guard models. These results suggest that compact vision-language moderators can serve as deployable front-line safety components, with reasoning used selectively for audit and policy review.

</details>

### 3. GuardPaint: Speculative Safety Decoding for Text-to-Image Generation

📄 [arXiv](https://arxiv.org/abs/2608.21869)　📅 2026-08

**关键词**：`defense`、`intermediate-image auditor`、`policy compliance`、`surgical inpainting`、`speculative safety decoding`、`trajectory auditing`

👤 **作者**：Shreyash Dhoot、…、Amitava Das

- 🎯 **研究动机**：T2I 防御多在生成前过滤 prompt 或生成后分类图像，去噪过程本身无守卫，且往往只能拒绝而无法安全修复
- 🔬 **研究方法**：GuardPaint 推测式安全解码：轻量 auditor 监测中间图像并定位不安全区域，仅由策略对齐 inpainter 做局部修复，guarded tournament 只接受提升合规且保持 prompt 保真与感知质量的编辑，不修改基座模型
- 📌 **结论**：在 SneakPrompt、MMA、PGJ、DACA、RABell 五类越狱与 SD1.5/SDXL/SD3.5/FLUX.1-dev 上降低攻击成功与有害生成，图像质量和良性行为几乎无损

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) diffusion models offer powerful visual generation, but their controllability creates a critical safety challenge: adversarial prompts can steer the denoising trajectory toward policy-violating content such as explicit nudity or graphic violence. Existing safeguards mostly act before generation through prompt filtering or after generation through image classification, leaving the diffusion process itself unguarded and often yielding only refusal rather than safe visual repair. We introduce GuardPaint, a speculative decoding framework for safe T2I generation that intervenes inside the diffusion trajectory without modifying the base model. A lightweight auditor monitors intermediate images, localizes unsafe regions, and triggers surgical inpainting repair only where needed. Candidate repairs are generated by a policy-aligned inpainter and selected through a guarded tournament that accepts edits only when they improve policy compliance while preserving prompt fidelity and perceptual quality. Across five jailbreak families SneakPrompt, MMA, PGJ, DACA, and RABell and UNet/flow-matching models including SD~1.5, SDXL, SD~3.5, and FLUX.1-dev. GuardPaint reduces attack success and harmful generations with minimal degradation to image quality, prompt fidelity, and benign behavior. Content warning: This paper contains examples involving nudity and violence that some readers may find disturbing, distressing, or offensive.

</details>

### 4. ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21100)　📅 2026-08

**关键词**：`defense`、`test-time safety alignment`、`evidence-guided reframing`、`jailbreak defense`、`risk-utility evidence`、`alignment calibration`

👤 **作者**：Wenzheng Jiang、Xuankun Rong、Yuanzhao Zhai、Dawei Feng、Huaimin Wang

- 🎯 **研究动机**：跨模态 jailbreak、安全意识缺失与过度拒答威胁 MLLM，现有对齐方法依赖重训或内部状态检查，无法用于已部署的闭源模型
- 🔬 **研究方法**：ReFrame 免训练输入重构框架：两个共享轻量本地 MLLM 的 agent 分别生成风险/效用证据并将其转为 safe proxy prompt 与 image-routing 决策，不修改下游模型即调用
- 📌 **结论**：多个 MLLM 与 benchmark 上同时改善 jailbreak 防御与安全意识、减少过度拒答，并保持多模态效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two key obstacles, utility dominance and reasoning inertia, which cause models to overlook latent risks or follow malicious reasoning trajectories. Guided by these insights, we propose ReFrame, a training-free multimodal input reframing framework where two agents share a lightweight locally deployed MLLM: the evidence-generation agent constructs complementary risk and utility evidence, and the rewrite-and-routing agent converts it into a safe proxy prompt and image-routing decision before calling the downstream MLLM, without modifying it or accessing its internal information. Experiments across multiple MLLMs and benchmarks show that ReFrame improves jailbreak defense, safety awareness, and oversensitivity reduction while preserving multimodal utility.

</details>

### 5. PolicyShiftGuard: Benchmarking and Improving Policy-Adaptive Image Guardrails

📄 [arXiv](https://arxiv.org/abs/2607.05910) · 🌐 [Project](https://policyshiftguard.github.io/)　📅 2026-07

**关键词**：`defense`、`policy-adaptive image guard`、`boundary pair`、`policy shift`

👤 **作者**：Mingyang Song、Luxin Xu、Haoyu Sun、Minzhou Pan、Yu Cheng、Bo Li

- 🎯 **研究动机**：图像护栏默认在固定策略下训练评估，把安全性当作图像内禀属性，而真实部署中策略随产品与边界变化
- 🔬 **研究方法**：构建 PolicyShiftBench（2,000 条策略判别实例、265 图像、平均每图 7.55 条策略条件提示）；提出 PolicyShiftGuard：随机策略 SFT+边界对策略适应（BP-Adapt）两阶段训练，用成对比较损失分离阻断与放行策略
- 📌 **结论**：现有 VLM 与护栏在策略漂移下脆弱；7B 模型取得 76.9 平均 F1 与 72.1 平均 PSS 的 SOTA，并迁移到 UnSafeBench 与 SafeEditBench

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image guardrails are typically trained and evaluated under a fixed safety policy, implicitly treating safety as an intrinsic property of an image. Real deployments are different: the same image may be allowed in one product, restricted in another, and newly disallowed when a policy boundary changes. We study policy-adaptive image guardrailing, where a model must decide whether an image violates the currently supplied policy and generalize to held-out policy definitions. We introduce PolicyShiftBench, a comprehensive benchmark with 2,000 policy-discriminative instances over 265 images, where each image is paired with 7.55 policy-conditioned prompts on average to test whether models adapt to the active policy rather than relying on image-level safety priors. We then propose PolicyShiftGuard, a compact policy-conditioned guardrail trained with a two-stage training recipe that combines Randomized Policy SFT (RP-SFT) with Boundary-Pair Policy Adaptation (BP-Adapt). BP-Adapt trains matched prompts for the same image and risk category using standard label supervision and a pairwise comparison loss that separates blocking policies from passing policies. Experiments show that existing VLMs and specialized guardrails remain brittle under policy shifts, while PolicyShiftGuard substantially improves policy-sensitive performance. The 7B model achieves SOTA performance of 76.9 Avg. F1 and 72.1 Avg. PSS on PolicyShiftBench, transfers well to UnSafeBench and SafeEditBench, and improves the latency-performance trade-off with a concise output format. Ablations confirm that matched pass/block boundary pairs are essential for stable policy adaptation.

</details>

### 6. Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs

📄 [arXiv](https://arxiv.org/abs/2607.09697) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4143)　📅 2026-06　🏷 ECCV 2026

**关键词**：`defense`、`output-aware guard`、`hidden-state prediction`、`over-refusal`、`multimodal guardrail`、`output prediction`

👤 **作者**：Jiayi Li、Kun Zhan

- 🎯 **研究动机**：输入侧护栏在模型本可安全作答时也一刀切阻断，过度拒绝根因在于不看模型即将生成什么
- 🔬 **研究方法**：提出输出感知护栏范式：经多示例对比学习在隐藏状态空间训练轻量分类器，预测即将到来的生成是否不安全，仅在实际响应会有害时干预
- 📌 **结论**：匹配现有方法安全性能的同时大幅降低过度拒绝，保留模型效用与内生安全能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing safety mechanisms for multimodal large language models (MLLMs) face a fundamental trade-off between safety and utility. Model fine-tuning achieves robust safety but compromises general utility. Input-side safety guardrails offer a lightweight alternative, yet they suffer from severe over-refusal, indiscriminately blocking benign queries or those the model could have safely answered through refusal or advisory responses. We identify that the root cause of over-refusal lies in the input-aware paradigm: safety guardrails make safety decisions without considering whether the model itself is capable of generating safe responses. Usually, MLLMs already possess intrinsic safety mechanisms that can transform harmful inputs into harmless outputs, but input-side safety guardrails override this capability, degrading user experience. Motivated by this insight, we propose a paradigm shift toward output-aware safety guardrails. Our method operates within the model's hidden state space to predict whether the forthcoming generation will be unsafe before it is fully produced. By training a lightweight classifier via multi-instance contrastive learning on hidden state representations, our approach distinguishes between inputs that will lead to unsafe outputs and those that will not, even when the inputs themselves contain risky elements. This enables precise intervention only when the model's actual response would be harmful. Extensive experiments demonstrate that our output-aware safety guardrail matches the safety performance of existing methods while drastically reducing over-refusal, preserving the model's utility and built-in safety capabilities. Code is available at: https://github.com/kunzhan/OutGuard

</details>

### 7. RuleSafe-VL: Evaluating Rule-Conditioned Decision Reasoning in Vision-Language Content Moderation

📄 [arXiv](https://arxiv.org/abs/2605.07760) · 🌐 [Project](https://anonymous.4open.science/r/RuleRuleSafe-VL-2527/README.md)　📅 2026-05

**关键词**：`benchmark`、`rule-conditioned moderation`、`decision reasoning`、`policy compliance`

👤 **作者**：Zhifeng Lu、Dianyuan Wang、Yuhu Shang、Zhenbo Xu

- 🎯 **研究动机**：现有多模态安全基准把审核简化为终标签匹配，不检验规则激活、规则交互与证据充分性
- 🔬 **研究方法**：RuleSafe-VL 从平台政策形式化 93 条原子规则与 92 种规则关系，构建 2,166 个上下文敏感图文案例与四个诊断任务分解规则条件化决策链
- 📌 **结论**：规则关系恢复是主要瓶颈——最好模型仅 64.8 Macro-F1，部分安全导向模型低于 7 Macro-F1

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Platform content moderation applies explicit policy rules and context-dependent conditions to decide whether user content is allowed, restricted, or removed. A correct moderation outcome must therefore depend on which rules a case activates, how those rules interact, and whether the available evidence is sufficient. Current multimodal safety benchmarks largely reduce moderation to matching predefined final labels, leaving this underlying rule structure untested. As a result, a high benchmark score reveals little about whether a model applies the policy correctly or arrives at the correct label through superficial cues. To evaluate this rule-governed process, we introduce RuleSafe-VL, a benchmark for rule-conditioned decision reasoning in vision-language content moderation. Derived from publicly available platform moderation policies, RuleSafe-VL formalizes 93 atomic rules and 92 typed rule relations, yielding 2,166 context-sensitive image-text cases across three high-risk policy families. Its four diagnostic tasks decompose moderation into a rule-conditioned decision chain. They identify activated rules, recover rule interactions, judge decision sufficiency, and resolve outcomes once missing context is supplied. Experiments on 10 frontier, open-source, and safety-oriented VLMs reveal rule-relation recovery as the dominant bottleneck, where the best model reaches only 64.8 Macro-F1 and some safety-oriented models fall below 7 Macro-F1. Decision-state prediction also remains unreliable, peaking at 64.5 Macro-F1. RuleSafe-VL shifts moderation evaluation from final-label scoring toward diagnostic assessment of rule-conditioned decision reasoning.

</details>

### 8. Towards Policy-Adaptive Image Guardrail: Benchmark and Method

📄 [arXiv](https://arxiv.org/abs/2603.01228) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Piao_Towards_Policy-Adaptive_Image_Guardrail_Benchmark_and_Method_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`benchmark`、`SafeGuard-VL`、`cross-policy generalization`、`RLVR`、`image guardrail`

👤 **作者**：Caiyong Piao、…、Shuigeng Zhou

- 🎯 **研究动机**：VLM 图像护栏只在固定安全策略下训练评测，过拟合已见策略、无法泛化到新策略
- 🔬 **研究方法**：SafeEditBench 用图像编辑构造仅局部违规的安全-不安全图对，5 种策略人工标注；SafeGuard-VL 用 RLVR 以策略接地的可验证奖励优化跨策略适应
- 📌 **结论**：跨策略泛化的不安全图像护栏效果显著优于仅靠 SFT 的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Accurate rejection of sensitive or harmful visual content, i.e., harmful image guardrail, is critical in many application scenarios. This task must continuously adapt to the evolving safety policies and content across various domains and over time. However, traditional classifiers, confined to fixed categories, require frequent retraining when new policies are introduced. Vision-language models (VLMs) offer a more adaptable and generalizable foundation for dynamic safety guardrails. Despite this potential, existing VLM-based safeguarding methods are typically trained and evaluated under only a fixed safety policy. We find that these models are heavily overfitted to the seen policy, fail to generalize to unseen policies, and even lose the basic instruction-following ability and general knowledge. To address this issue, in this paper we make two key contributions. First, we benchmark the cross-policy generalization performance of existing VLMs with SafeEditBench, a new evaluation suite. SafeEditBench leverages image-editing models to convert unsafe images into safe counterparts, producing policy-aligned datasets where each safe-unsafe image pair remains visually similar except for localized regions violating specific safety rules. Human annotators then provide accurate safe/unsafe labels under five distinct policies, enabling fine-grained assessment of policy-aware generalization. Second, we introduce SafeGuard-VL, a reinforcement learning-based method with verifiable rewards (RLVR) for robust unsafe-image guardrails. Instead of relying solely on supervised fine-tuning (SFT) under fixed policies, SafeGuard-VL explicitly optimizes the model with policy-grounded rewards, promoting verifiable adaptation across evolving policies. Extensive experiments verify the effectiveness of our method for unsafe image guardrails across various policies.

</details>

### 9. Tool-MCoT: Tool Augmented Multimodal Chain-of-Thought for Content Safety Moderation

📄 [arXiv](https://arxiv.org/abs/2604.06205)　📅 2026-03

**关键词**：`defense`、`tool-augmented reasoning`、`selective invocation`、`efficient moderation`

👤 **作者**：Shutong Zhang、Dylan Zhou、Yinxiao Liu、Yang Yang、Huiwen Luo、Wenfei Zou

- 🎯 **研究动机**：LLM 内容审核的计算成本与延迟高，难以规模化部署
- 🔬 **研究方法**：用 LLM 生成带工具调用的多模态 CoT 数据微调小模型 Tool-MCoT，使其学会选择性调用外部审核工具
- 📌 **结论**：审核性能显著提升，且按需调用工具在准确率与推理效率间取得平衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growth of online platforms and user content requires strong content moderation systems that can handle complex inputs from various media types. While large language models (LLMs) are effective, their high computational cost and latency present significant challenges for scalable deployment. To address this, we introduce Tool-MCoT, a small language model (SLM) fine-tuned for content safety moderation leveraging external framework. By training our model on tool-augmented chain-of-thought data generated by LLM, we demonstrate that the SLM can learn to effectively utilize these tools to improve its reasoning and decision-making. Our experiments show that the fine-tuned SLM achieves significant performance gains. Furthermore, we show that the model can learn to use these tools selectively, achieving a balance between moderation accuracy and inference efficiency by calling tools only when necessary.

</details>

### 10. KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety

📄 [arXiv](https://arxiv.org/abs/2603.16181)　📅 2026-03

**关键词**：`defense`、`child-safety moderation`、`OCR reasoning`、`two-stage routing`、`visual screening`

👤 **作者**：Viraj Panchal、Tanmay Talsaniya、Parag Patel、Meet Patel

- 🎯 **研究动机**：儿童安全内容审核需同时覆盖嵌入文本威胁并保持低延迟
- 🔬 **研究方法**：KidsNanny 两阶段管线：ViT 加目标检测做视觉筛查（11.7ms），以文本而非原始像素路由到 OCR 加 7B 语言模型做上下文推理（全程 120ms）
- 📌 **结论**：UnsafeBench 上准确率 81.40%、F1 86.16%，远快于 ShieldGemma-2（1,136ms）与 LlavaGuard（4,138ms）；纯文本子集 recall 达 100%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present KidsNanny, a two-stage multimodal content moderation architecture for child safety. Stage 1 combines a vision transformer (ViT) with an object detector for visual screening (11.7 ms); outputs are routed as text not raw pixels to Stage 2, which applies OCR and a text based 7B language model for contextual reasoning (120 ms total pipeline). We evaluate on the UnsafeBench Sexual category (1,054 images) under two regimes: vision-only, isolating Stage 1, and multimodal, evaluating the full Stage 1+2 pipeline. Stage 1 achieves 80.27% accuracy and 85.39% F1 at 11.7 ms; vision-only baselines range from 59.01% to 77.04% accuracy. The full pipeline achieves 81.40% accuracy and 86.16% F1 at 120 ms, compared to ShieldGemma-2 (64.80% accuracy, 1,136 ms) and LlavaGuard (80.36% accuracy, 4,138 ms). To evaluate text-awareness, we filter two subsets: a text+visual subset (257 images) and a text-only subset (44 images where safety depends primarily on embedded text). On text-only images, KidsNanny achieves 100% recall (25/25 positives; small sample) and 75.76% precision; ShieldGemma-2 achieves 84% recall and 60% precision at 1,136 ms. Results suggest that dedicated OCR-based reasoning may offer recall-precision advantages on text-embedded threats at lower latency, though the small text-only subset limits generalizability. By documenting this architecture and evaluation methodology, we aim to contribute to the broader research effort on efficient multimodal content moderation for child safety.

</details>

### 11. Pragma-VL: Towards a Pragmatic Arbitration of Safety and Helpfulness in MLLMs

📄 [arXiv](https://arxiv.org/abs/2603.13292) · 🌐 [Project](https://sii-fleeecermw.github.io/PragmaVL-iclr26/) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010080)　📅 2026-02　🏷 ICLR 2026

**关键词**：`defense`、`safety-helpfulness trade-off`、`visual risk perception`、`reward modeling`

👤 **作者**：Ming Wen、…、Yuedong Xu

- 🎯 **研究动机**：MLLM 安全对齐在过度拒绝良性查询与漏放跨模态潜在风险之间失衡
- 🔬 **研究方法**：Pragma-VL 冷启动 SFT 对视觉编码器做风险感知聚类并混入风险描述数据，再以动态权重增广训练有理论保证的协同奖励模型做语境仲裁
- 📌 **结论**：多数多模态安全基准超基线 5%-20%，并保留数学与知识推理等通用能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) pose critical safety challenges, as they are susceptible not only to adversarial attacks such as jailbreaking but also to inadvertently generating harmful content for benign users. While internal safety alignment via Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) is a primary mitigation strategy, current methods often face a safety-utility trade-off: they either refuse benign queries out of excessive caution or overlook latent risks in cross-modal interactions. To resolve this, we introduce Pragma-VL, an end-to-end alignment algorithm that enables MLLMs to pragmatically arbitrate between safety and helpfulness. First, we enhance visual risk perception with a novel cold-start SFT stage. This is achieved by applying risk-aware clustering to the visual encoder and using an interleaved dataset of risk descriptions and high-quality data. Second, we introduce a theoretically-guaranteed reward model that leverages synergistic learning. We train it with a novel data augmentation method that assigns dynamic weights based on the queries, enabling contextual arbitration between safety and helpfulness. Extensive experiments show that Pragma-VL effectively balances safety and helpfulness, outperforming baselines by 5% to 20% on most multimodal safety benchmarks while preserving its general capabilities in areas such as mathematics and knowledge reasoning.

</details>

### 12. ProGuard: Towards Proactive Multimodal Safeguard

📄 [arXiv](https://arxiv.org/abs/2512.23573)　📅 2025-12

**关键词**：`defense`、`OOD risk`、`proactive moderation`、`RL training`

👤 **作者**：Shaohan Yu、Lijun Li、Chenyang Si、Lu Sheng、Jing Shao

- 🎯 **研究动机**：生成模型使多模态安全风险持续涌现，传统被动式防御需模型调整且无法识别 OOD 风险
- 🔬 **研究方法**：ProGuard 基于 87K 模态平衡、含二值标签与层级风险类别标注的数据集纯强化学习训练，并以同义词库相似性奖励鼓励对未见不安全类别生成简洁描述
- 📌 **结论**：二分类比肩闭源大模型；OOD 风险检测提升 52.6%、OOD 风险描述提升 64.8%，大幅超越开源 guard 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of generative models has led to a continuous emergence of multimodal safety risks, exposing the limitations of existing defense methods. To address these challenges, we propose ProGuard, a vision-language proactive guard that identifies and describes out-of-distribution (OOD) safety risks without the need for model adjustments required by traditional reactive approaches. We first construct a modality-balanced dataset of 87K samples, each annotated with both binary safety labels and risk categories under a hierarchical multimodal safety taxonomy, effectively mitigating modality bias and ensuring consistent moderation across text, image, and text-image inputs. Based on this dataset, we train our vision-language base model purely through reinforcement learning (RL) to achieve efficient and concise reasoning. To approximate proactive safety scenarios in a controlled setting, we further introduce an OOD safety category inference task and augment the RL objective with a synonym-bank-based similarity reward that encourages the model to generate concise descriptions for unseen unsafe categories. Experimental results show that ProGuard achieves performance comparable to closed-source large models on binary safety classification, substantially outperforms existing open-source guard models on unsafe content categorization. Most notably, ProGuard delivers a strong proactive moderation ability, improving OOD risk detection by 52.6% and OOD risk description by 64.8%.

</details>

### 13. Aetheria: A multimodal interpretable content safety framework based on multi-agent debate and collaboration

📄 [arXiv](https://arxiv.org/abs/2512.02530)　📅 2025-12

**关键词**：`defense`、`multi-agent debate`、`RAG grounding`、`interpretable moderation`

👤 **作者**：Yuxiang He、…、Xuelong Li

- 🎯 **研究动机**：单模型或固定流水线审核难以识别隐式风险且判定过程不可解释
- 🔬 **研究方法**：Aetheria 由五个核心 agent 通过动态相互说服的辩论机制分析裁决多模态内容，以 RAG 知识检索接地，并配套 AIR-Bench 评测
- 📌 **结论**：生成详细可追溯的审计报告，整体内容安全准确率显著优于基线，尤其在隐式风险识别上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The exponential growth of digital content presents significant challenges for content safety. Current moderation systems, often based on single models or fixed pipelines, exhibit limitations in identifying implicit risks and providing interpretable judgment processes. To address these issues, we propose Aetheria, a multimodal interpretable content safety framework based on multi-agent debate and collaboration.Employing a collaborative architecture of five core agents, Aetheria conducts in-depth analysis and adjudication of multimodal content through a dynamic, mutually persuasive debate mechanism, which is grounded by RAG-based knowledge retrieval.Comprehensive experiments on our proposed benchmark (AIR-Bench) validate that Aetheria not only generates detailed and traceable audit reports but also demonstrates significant advantages over baselines in overall content safety accuracy, especially in the identification of implicit risks. This framework establishes a transparent and interpretable paradigm, significantly advancing the field of trustworthy AI content moderation.

</details>

### 14. GuardTrace-VL: Detecting Unsafe Multimodel Reasoning via Iterative Safety Supervision

📄 [arXiv](https://arxiv.org/abs/2511.20994) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_GuardTrace-VL_Detecting_Unsafe_Multimodel_Reasoning_via_Iterative_Safety_Supervision_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`detection`、`unsafe reasoning trace`、`QTA pipeline`、`iterative supervision`、`unsafe reasoning`、`vision-language model`

👤 **作者**：Yuxiao Xiang、…、Nenghai Yu

- 🎯 **研究动机**：多模态安全 guard 只检查输入问题与最终答案，忽视中间推理过程中出现的不安全内容
- 🔬 **研究方法**：GuardTrace-VL 监控 Question-Thinking-Answer 全链路做图文联合分析，构建经 MLRM 与人工投票验证的 GuardTrace 数据集，并以三阶段渐进训练学习分级安全偏好
- 📌 **结论**：不安全推理检测 F1 达 93.1%，较此前最强多模态防御提升 13.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large reasoning models (MLRMs) are increasingly deployed for vision-language tasks that produce explicit intermediate rationales. However, reasoning traces can contain unsafe content even when the final answer is non-harmful, creating deployment risks. Existing multimodal safety guards primarily evaluate only the input question and the final answer, neglecting the intermediate reasoning process. This oversight allows undetected harm, such as biased inferences or policy-violating use of visual context, to emerge during reasoning. We introduce GuardTrace-VL, a vision-aware safety auditor that monitors the full Question-Thinking-Answer (QTA) pipeline via joint image-text analysis, enabling detection of unsafe content as it emerges in the reasoning stage. To support training and evaluation, we construct the GuardTrace dataset, which is generated through diverse prompting strategies and refined via a MLRM- and human-based voting and verification pipeline. Furthermore, we propose a three-stage progressive training scheme combined with the data refinement process, enabling the model to learn nuanced and context-dependent safety preferences according to different risk levels. On our proposed test set covering both in-domain and out-of-domain scenarios, GuardTrace-VL model achieves an F1 score of 93.1% on unsafe reasoning detection tasks, representing a 13.5% improvement in F1 score compared to the previous strongest multimodal safety defense methods. The codes will be made publicly available.

</details>

### 15. SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability

📄 [arXiv](https://arxiv.org/abs/2510.23960) · 📝 [OpenReview](https://openreview.net/forum?id=bPVLklCEcO)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`image guard`、`policy adherence`、`explainability`

👤 **作者**：Peiyang Xu、Minzhou Pan、Zhaorun Chen、Shuang Yang、Chaowei Xiao、Bo Li

- 🎯 **研究动机**：传统图像 guardrail 受预定义类别限制、缺语义推理，应对新威胁需昂贵重训
- 🔬 **研究方法**：SafeVision 整合数据采集生成框架、policy-following 训练流水线与定制损失，推理时动态适配演化中的安全策略，并发布 VisionHarm 双子集数据集
- 📌 **结论**：在 VisionHarm-T 与 VisionHarm-C 上分别超 GPT-4o 8.6% 与 15.5%，速度快 16 倍以上

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid proliferation of digital media, the need for efficient and transparent safeguards against unsafe content is more critical than ever. Traditional image guardrail models, constrained by predefined categories, often misclassify content due to their pure feature-based learning without semantic reasoning. Moreover, these models struggle to adapt to emerging threats, requiring costly retraining for new threats. To address these limitations, we introduce SafeVision, a novel image guardrail that integrates human-like reasoning to enhance adaptability and transparency. Our approach incorporates an effective data collection and generation framework, a policy-following training pipeline, and a customized loss function. We also propose a diverse QA generation and training strategy to enhance learning effectiveness. SafeVision dynamically aligns with evolving safety policies at inference time, eliminating the need for retraining while ensuring precise risk assessments and explanations. Recognizing the limitations of existing unsafe image benchmarks, which either lack granularity or cover limited risks, we introduce VisionHarm, a high-quality dataset comprising two subsets: VisionHarm Third-party (VisionHarm-T) and VisionHarm Comprehensive(VisionHarm-C), spanning diverse harmful categories. Through extensive experiments, we show that SafeVision achieves state-of-the-art performance on different benchmarks. SafeVision outperforms GPT-4o by 8.6% on VisionHarm-T and by 15.5% on VisionHarm-C, while being over 16x faster. SafeVision sets a comprehensive, policy-following, and explainable image guardrail with dynamic adaptation to emerging threats.

</details>

### 16. LLaVAShield: Safeguarding Multimodal Multi-Turn Dialogues in Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2509.25896) · 🌐 [Project](https://leost123456.github.io/LLaVAShield/) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_LLaVAShield_Safeguarding_Multimodal_Multi-Turn_Dialogues_in_Vision-Language_Models_CVPR_2026_paper.html)　📅 2025-09　🏷 CVPR 2026

**关键词**：`defense`、`multi-turn dialogue`、`contextual risk`、`VLM guard`、`multi-turn safety`、`vision-language model`

👤 **作者**：Guolei Huang、Qinzhi Peng、Gan Xu、Yao Huang、Yuxuan Lu、Yongjun Shen

- 🎯 **研究动机**：多模态多轮对话具恶意意图隐蔽、上下文风险累积与跨模态联合风险，单轮单模态审核失效
- 🔬 **研究方法**：构建 4,484 条对话、8 主类 60 子类风险分类法的 MMDS 数据集与多模态多轮红队框架 MMRT，提出 LLaVAShield 在指定政策维度审计用户输入与助手回复
- 📌 **结论**：显著超 SoTA VLM 与既有审核工具，泛化强且可灵活适配政策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Vision-Language Models (VLMs) move into interactive, multi-turn use, safety concerns intensify for multimodal multi-turn dialogue, which is characterized by concealment of malicious intent, contextual risk accumulation, and cross-modal joint risk. These characteristics limit the effectiveness of content moderation approaches designed for single-turn or single-modality settings. To address these limitations, we first construct the Multimodal Multi-turn Dialogue Safety (MMDS) dataset, comprising 4,484 annotated dialogues and a comprehensive risk taxonomy with 8 primary and 60 subdimensions. As part of MMDS construction, we introduce Multimodal Multi-turn Red Teaming (MMRT), an automated framework for generating unsafe multimodal multi-turn dialogues. We further propose LLaVAShield, which audits the safety of both user inputs and assistant responses under specified policy dimensions in multimodal multi-turn dialogues. Extensive experiments show that LLaVAShield significantly outperforms state-of-the-art VLMs and existing content moderation tools while demonstrating strong generalization and flexible policy adaptation. Additionally, we analyze vulnerabilities of mainstream VLMs to harmful inputs and evaluate the contribution of key components, advancing understanding of safety mechanisms in multimodal multi-turn dialogues.

</details>

### 17. Towards Trustworthy Multimodal Moderation via Policy-Aligned Reasoning and Hierarchical Labeling

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

### 18. GuardReasoner-VL: Safeguarding VLMs via Reinforced Reasoning

📄 [arXiv](https://arxiv.org/abs/2505.11049) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2a02b560822d564119fe3ac3be024ac6-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`defense`、`reinforced reasoning`、`multimodal guard`、`length-aware reward`

👤 **作者**：Yue Liu、…、Bryan Hooi

- 🎯 **研究动机**：VLM 内容审核需要推理式判断以提升准确性与可解释性
- 🔬 **研究方法**：构建 123K 样本、631K 推理步骤的训练语料，SFT 冷启动后经在线 RL（拒绝采样、安全感知数据拼接、长度感知奖励）训练 GuardReasoner-VL
- 📌 **结论**：平均超第二名 19.27% F1，开源 3B 与 7B 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To enhance the safety of VLMs, this paper introduces a novel reasoning-based VLM guard model dubbed GuardReasoner-VL. The core idea is to incentivize the guard model to deliberatively reason before making moderation decisions via online RL. First, we construct GuardReasoner-VLTrain, a reasoning corpus with 123K samples and 631K reasoning steps, spanning text, image, and text-image inputs. Then, based on it, we cold-start our model's reasoning ability via SFT. In addition, we further enhance reasoning regarding moderation through online RL. Concretely, to enhance diversity and difficulty of samples, we conduct rejection sampling followed by data augmentation via the proposed safety-aware data concatenation. Besides, we use a dynamic clipping parameter to encourage exploration in early stages and exploitation in later stages. To balance performance and token efficiency, we design a length-aware safety reward that integrates accuracy, format, and token cost. Extensive experiments demonstrate the superiority of our model. Remarkably, it surpasses the runner-up by 19.27% F1 score on average. We release data, code, and models (3B/7B) of GuardReasoner-VL at https://github.com/yueliu1999/GuardReasoner-VL/

</details>

### 19. ShieldGemma 2: Robust and Tractable Image Content Moderation

📄 [arXiv](https://arxiv.org/abs/2504.01081)　📅 2025-04

**关键词**：`tool`、`image moderation`、`adversarial data`、`open guard model`

👤 **作者**：Wenjun Zeng、…、Karthik Narasimhan

- 🎯 **研究动机**：图像内容审核需要同时覆盖合成与自然图像的鲁棒开放工具
- 🔬 **研究方法**：基于 Gemma 3 训练 4B 参数的 ShieldGemma 2，覆盖色情、暴力血腥、危险内容三类危害，并配套对抗数据生成管线
- 📌 **结论**：内外部基准上超过 LlavaGuard、GPT-4o mini 与基座 Gemma 3

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce ShieldGemma 2, a 4B parameter image content moderation model built on Gemma 3. This model provides robust safety risk predictions across the following key harm categories: Sexually Explicit, Violence \& Gore, and Dangerous Content for synthetic images (e.g. output of any image generation model) and natural images (e.g. any image input to a Vision-Language Model). We evaluated on both internal and external benchmarks to demonstrate state-of-the-art performance compared to LlavaGuard \citep{helff2024llavaguard}, GPT-4o mini \citep{hurst2024gpt}, and the base Gemma 3 model \citep{gemma_2025} based on our policies. Additionally, we present a novel adversarial data generation pipeline which enables a controlled, diverse, and robust image generation. ShieldGemma 2 provides an open image moderation tool to advance multimodal safety and responsible AI development.

</details>

### 20. MLLM-as-a-Judge for Image Safety without Human Labeling

📄 [arXiv](https://arxiv.org/abs/2501.00192)　📅 2024-12

**关键词**：`defense`、`zero-shot image judge`、`safety constitution`、`cascaded reasoning`

👤 **作者**：Zhenting Wang、…、Ankit Jain

- 🎯 **研究动机**：人工标注安全规则昂贵且规则频繁更新，直接零样本查询 MLLM 效果不佳
- 🔬 **研究方法**：将安全规则客观化、评估规则与图像相关性、以去偏 token 概率加简化前置链快速判断，必要时级联 CoT 深度推理
- 📌 **结论**：零-shot 图像安全判定任务上高度有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image content safety has become a significant challenge with the rise of visual media on online platforms. Meanwhile, in the age of AI-generated content (AIGC), many image generation models are capable of producing harmful content, such as images containing sexual or violent material. Thus, it becomes crucial to identify such unsafe images based on established safety rules. Pre-trained Multimodal Large Language Models (MLLMs) offer potential in this regard, given their strong pattern recognition abilities. Existing approaches typically fine-tune MLLMs with human-labeled datasets, which however brings a series of drawbacks. First, relying on human annotators to label data following intricate and detailed guidelines is both expensive and labor-intensive. Furthermore, users of safety judgment systems may need to frequently update safety rules, making fine-tuning on human-based annotation more challenging. This raises the research question: Can we detect unsafe images by querying MLLMs in a zero-shot setting using a predefined safety constitution (a set of safety rules)? Our research showed that simply querying pre-trained MLLMs does not yield satisfactory results. This lack of effectiveness stems from factors such as the subjectivity of safety rules, the complexity of lengthy constitutions, and the inherent biases in the models. To address these challenges, we propose a MLLM-based method includes objectifying safety rules, assessing the relevance between rules and images, making quick judgments based on debiased token probabilities with logically complete yet simplified precondition chains for safety rules, and conducting more in-depth reasoning with cascaded chain-of-thought processes if necessary. Experiment results demonstrate that our method is highly effective for zero-shot image safety judgment tasks.

</details>

### 21. Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations

📄 [arXiv](https://arxiv.org/abs/2411.10414)　📅 2024-11

**关键词**：`tool`、`vision-language guard`、`prompt-response moderation`、`MLCommons taxonomy`

👤 **作者**：Jianfeng Chi、…、Mahesh Pasupuleti

- 🎯 **研究动机**：纯文本 Llama Guard 无法审核涉及图像理解的人机对话安全
- 🔬 **研究方法**：Llama Guard 3 Vision 基于 Llama 3.2-Vision 微调，按 MLCommons taxonomy 同时分类多模态 prompt 与文本 response，并测对抗鲁棒性
- 📌 **结论**：内部基准上表现强劲，是构建多模态内容审核工具的起点模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Llama Guard 3 Vision, a multimodal LLM-based safeguard for human-AI conversations that involves image understanding: it can be used to safeguard content for both multimodal LLM inputs (prompt classification) and outputs (response classification). Unlike the previous text-only Llama Guard versions (Inan et al., 2023; Llama Team, 2024b,a), it is specifically designed to support image reasoning use cases and is optimized to detect harmful multimodal (text and image) prompts and text responses to these prompts. Llama Guard 3 Vision is fine-tuned on Llama 3.2-Vision and demonstrates strong performance on the internal benchmarks using the MLCommons taxonomy. We also test its robustness against adversarial attacks. We believe that Llama Guard 3 Vision serves as a good starting point to build more capable and robust content moderation tools for human-AI conversation with multimodal capabilities.

</details>

### 22. Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.02082)　📅 2026-09

**关键词**：`defense`、`cross-modal safety drift`、`representation transfer`、`MLLM`

👤 **作者**：Tianqi Xiao、Shiyao Cui、Minghao Zhang、Junxiao Yang、Renmiao Chen

- 🎯 **研究动机**：良性文本搭配有害图像时安全响应率显著更低（cross-modal safety drift），视觉风险线索注意力弱、拒答触发不足
- 🔬 **研究方法**：提出 SRT：基于不安全文本处理的安全信号可迁移这一观察，以轻量方向精修方法在冻结 MLLM backbone 上把安全感知迁移到视觉路径
- 📌 **结论**：跨多个基准与模型在多样跨模态设定下提升安全性并保持 utility

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual modality enhances the capabilities of multimodal large language models (MLLMs) but also introduces a safety concern: a benign textual query may convey harmful intent when grounded in a visual image. We term this cross-modal safety drift and our pilot studies show that the safety response rate for such requests is substantially lower than that for requests containing explicitly unsafe text. This paper aims to systematically study this issue. First, we conduct an empirical analysis to identify representative unsafe response patterns. Building on these, we interpret model representations and attentions, revealing that visually risky cues receive limited attention and weakly trigger refusal. Motivated by the observation that safety signals from unsafe text processing can be transferred, we propose safety-awareness representation transfer (SRT), a lightweight direction-refinement method that mitigates cross-modal safety drift with a frozen MLLM backbone. Experiments across multiple benchmarks and models show that SRT effectively improves safety in diverse cross-modal settings while preserving utility. Code is available at https://github.com/cucu220123/safety-awareness.

</details>

### 23. Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate

📄 [arXiv](https://arxiv.org/abs/2609.01168)　📅 2026-09

**关键词**：`attack`、`T2I guardrail`、`heterogeneous filter`、`multi-agent red teaming`、`T2I jailbreak`、`heterogeneous filters`

👤 **作者**：Kaiyan Wen、Shijie Zhang、Lu Yu、Guangdong Bai

- 🎯 **研究动机**：文本过滤器、图像分类器与跨模态检测器组成的异构 T2I 防线之间存在冲突，逐过滤器优化或整线聚合反馈都难以定位有效约束
- 🔬 **研究方法**：提出刻画异构 filter 决策边界的 Detection Surface 几何框架，以及把越狱搜索拆为探索、诊断、仲裁的 CRACK 多 Agent 辩论框架（Attack／Defense／Judge 三 Agent 迭代变异与逐层反馈）
- 📌 **结论**：复合防御下 ASR 最高 99.63%，查询数少于现有方法且保持语义保真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety layers. In this paper, we introduce the Detection Surface, a unified geometric framework that characterizes the decision boundaries induced by heterogeneous T2I safety filters and their joint effect on the jailbreak search space. This formulation reveals that successful evasion is governed by a sparse and non-convex region shaped by cross-layer conflicts, where mutations that bypass one filter may increase exposure to another. Motivated by this analysis, we propose CRACK, a multi-agent debate framework for adaptive jailbreak search that decomposes jailbreak search into exploration, diagnosis, and arbitration. CRACK coordinates an Attack Agent, a Defense Agent, and a Judge Agent to iteratively generate prompt mutations, obtain layer-specific diagnostic feedback, and optimize mutation strategies through reward-guided refinement. Through repeated rounds of debate, CRACK adapts its search direction to the evolving cross-layer constraints while preserving the original harmful intent. Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.

</details>

### 24. COMIC: Reference-Aware Safety Gating for Multimodal Large Language Models

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

### 25. Fully Unleashing the Multimodal Attacker: Meta-Adaptive Jailbreaking of Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2608.27531)　📅 2026-08

**关键词**：`attack`、`multimodal guardrail bypass`、`meta-adaptation`、`cross-defense transfer`、`meta-adaptive jailbreak`、`attacker co-evolution`

👤 **作者**：Benlei Cui、…、Haiwen Hong

- 🎯 **研究动机**：现有多模态越狱在 meta 层静态：模板攻击冻结图文布局，迭代攻击只改内容而固定策略与攻击者参数
- 🔬 **研究方法**：提出 MAMJ，沿攻击策略 prompt 与攻击者权重两轴优化攻击者本身：LLM critique 先在轨迹组上精炼 ASP，再以组聚合 ASR 奖励更新权重
- 📌 **结论**：在 MM-SafetyBench 上对 GPT-4o、Gemini-3-Pro-Preview、Seed 2.0 分别达 81.0%/78.9%/82.3% ASR，超最强基线最多 24.1 个百分点，且零训练迁移到未见受害模型并保持对代表性防御有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The safety of large vision-language models is increasingly stress-tested by multimodal jailbreaks, yet existing attacks remain largely static at the meta level: template-based attacks freeze the image-text layout, while iterative attacks adapt only the image-text content with fixed attack strategies and frozen attacker parameters. We propose Meta-Adaptive Multimodal Jailbreaking (MAMJ), which instead optimizes the attacker itself along two axes: an attack strategy prompt (ASP) governing attack iteration and attacker model weights determining attack effectiveness. Across groups of multimodal attack trajectories, an LLM-based critique first refines the ASP, after which group-aggregated attack success rate (ASR) rewards update those weights. On MM-SafetyBench, MAMJ achieves 81.0%, 78.9%, and 82.3% ASR against GPT-4o, Gemini-3-Pro-Preview, and Seed 2.0, respectively, outperforming the strongest sample-level baseline by up to 24.1 percentage points. The learned attacker, comprising the optimized ASP and attacker weights, also transfers without retraining to unseen victims and remains effective under representative defenses. These results reveal a systemic vulnerability of frontier VLMs to meta-adaptive jailbreaks and motivate defenses against meta-level adversaries. Code is available at https://github.com/Alibaba-VELLDEPTH/MetaJailbreak-VLM.

</details>

### 26. DiSCO: Defending text-to-image generation through distribution-guided contrastive prompt optimization

📄 [arXiv](https://arxiv.org/abs/2608.17067)　📅 2026-08

**关键词**：`defense`、`black-box T2I guardrail`、`safe-unsafe image pool`、`prompt rewriting`、`black-box T2I safeguard`、`contrastive prompt optimization`

👤 **作者**：Tong Zhang、Motasem Alfarra、Carlos Hinojosa、Christos Louizos、Bernard Ghanem

- 🎯 **研究动机**：T2I 防御多为白盒；LLM 改写式黑盒防御败于良性对抗问题——语言安全却因模型数据分布触发有害生成
- 🔬 **研究方法**：DiSCO 零样本纯黑盒 prompt 级即插即用模块：束搜索做分布引导后缀扩展，以目标模型自生成的安全/不安全图像池对比打分并迭代自适应反馈
- 📌 **结论**：I2P 基准多种红队攻击下对无防御与已有防御模型分别降低 ASR 37.7% 与 25.13%，同时保持语义保真并提升图像连贯性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As text-to-image generative models advance, they raise critical safety concerns, particularly the generation of Not-Safe-For-Work (NSFW) content such as violence and nudity, further exacerbated by red-teaming adversarial attacks. Existing defenses predominantly operate under white-box assumptions, relying on text encoder optimization, weight editing, or inference-time intervention, and fundamentally cannot scale to proprietary models. Black-box alternatives based on LLM prompt rewriting offer broader applicability, yet fail in a critical regime we identify as the \textit{benign adversarial} problem: prompts that are linguistically safe but still trigger harmful generation due to the model's learned data distribution. We propose DiSCO, a zero-shot, strictly black-box defense that operates entirely at the prompt level as a plug-and-play module, requiring no model retraining, fine-tuning, or access to model internals. DiSCO performs distribution-guided suffix expansion via beam search, optimized through contrastive scoring over safe and unsafe image pools generated by the target model itself, with iterative adaptive feedback until safe content is produced. We demonstrate that DiSCO consistently enhances the safety of both undefended and defended models on the I2P benchmark under multiple red-teaming attacks, achieving 37.7% and 25.13% ASR reduction, respectively, while maintaining semantic fidelity and improving image coherence. As a black-box, architecture-agnostic module, DiSCO can be readily applied to any text-to-image system without necessitating any changes to the model itself.

</details>

### 27. HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target Identification in Harmful Memes

📄 [arXiv](https://arxiv.org/abs/2608.16622)　📅 2026-08

**关键词**：`defense`、`multimodal guardrail`、`cross-modal risk`、`moderation robustness`

👤 **作者**：Yujia Li、…、Daling Wang

- 🎯 **研究动机**：有害 meme 检测只判有害性，模型可能判对有害却认错被攻击目标及其证据
- 🔬 **研究方法**：扩展为细粒度目标识别（目标类别、实体、文本提及、视觉区域）；Meme3W 数据集与 Joint Record Accuracy 严格指标；HarmTrace 做实体感知 SFT 加 CTPO 解耦有害性与目标识别优势并用虚拟正锚归一化
- 📌 **结论**：Qwen3-VL-8B 上 JRA 从 17.58% 升至 52.51%，有害性准确率同步提升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal harmful meme detection is typically formulated as image--text harmfulness classification. A model may correctly predict harmfulness while misidentifying the attacked target or its supporting evidence. We therefore extend harmful meme detection with fine-grained target identification, asking what type of target is attacked, who is targeted, and where the target appears in the meme. The model predicts harmfulness for every meme and, for harmful memes, outputs the target category, target entity, textual mention, and visual region. To support this task, we introduce Meme3W, which unifies multiple public harmful meme datasets and provides human-verified annotations for harmful instances. We further introduce Joint Record Accuracy (JRA), a strict record-level metric requiring the harmfulness label and all target-identification fields to be jointly correct. Experiments with representative multimodal large language models reveal a substantial gap between harmfulness accuracy and JRA. To narrow this gap, we propose HarmTrace, an anchor-calibrated decoupled optimization framework. HarmTrace strengthens target-entity supervision through entity-aware supervised fine-tuning. It then applies Conditional Target-identification Policy Optimization (CTPO) to decouple harmfulness and target-identification advantages, restricting target-identification optimization to label-correct responses for harmful examples. CTPO uses a Virtual Positive Anchor (VPA) as a fully correct reference for target-identification advantage normalization. HarmTrace improves both JRA and harmfulness accuracy across the evaluated backbones, with JRA on the Qwen3-VL-8B backbone increasing from 17.58\% to 52.51\%. Our code is publicly available at https://github.com/llly1234/HarmTrace-for-Harmful-Memes.

</details>

### 28. Whose Refusal Is It? The Unmeasured Contribution of Black-Box Multimodal Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.08641)　📅 2026-08

**关键词**：`defense`、`VLM safety`、`multimodal guardrail`、`cross-modal risk`

👤 **作者**：Haoyu Zhang、…、Shanu Sushmita

- 🎯 **研究动机**：黑盒 guardrail 评测把 guard 拦截与目标模型自身对齐拒答合计为一个安全数，guard 的真实贡献从未被测量
- 🔬 **研究方法**：拆分拒答来源：操纵 payload 通道（文本 vs 像素）与防御内部读取的文本（原请求 vs 攻击原文），利用 guard 拦截与模型拒答计数不相交恢复份额
- 📌 **结论**：guard 实际份额从 0 到几乎全部，取决于通道与 harness 读入文本；宽松授权会显著夸大 gate 型 guard 的收益，参考实现会默默引入该偏置

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A black-box guardrail is evaluated as though the safety number it earns were its own. It is not. A defended pipeline holds two components that can refuse (the guardrail, and the target model out of its own alignment), and every reported metric is a sum over both. We show that the guardrail's actual share of the safety credited to it runs from none of it to essentially all of it, decided by two variables no evaluation records: which channel carries the payload, and what text the harness places in the defense's internal read. The split is recoverable at no extra cost, because a guard block replaces the model's response and the two counts are therefore disjoint. On a text guard across two open-weight targets: with the payload rendered as pixels the guard blocks nothing and the model produces every refusal the system makes; reading the encoded prompt the attacker actually sent, the guard produces a minority of the refusals attributed to it; reading the unencoded request behind the attack, it blocks almost everything and the model falls silent. The blindness is not inaccuracy: the same guards block no benign image inputs either, so their image-channel decision is a constant. Granting the unencoded request inflates measured benefit substantially for a guard gate, less for a caption-mediated re-check, and not at all for a majority-vote smoother; the ordering reproduces in an independent replicate. Isolating the grant within one defense shows it does not improve detection: the harm-verdict stage contributes nothing, while the stage that regenerates the answer carries the effect. Nor is the inflated setting careless; the reference implementation builds every stage from a single prompt field that cannot distinguish what the attacker sent from what the benchmark records, so faithful porting supplies it silently. Previously published figures of our own are among those revised.

</details>

### 29. The Boy Who Cried Wolf: Adversarial Misclassification of Safe Inputs as Unsafe in Multimodal Guardrails

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

### 30. Safe Alone, Unsafe Together: Safeguarding Against Implicit Toxicity When Benign Images Combine

📄 [arXiv](https://arxiv.org/abs/2607.00576)　📅 2026-07

**关键词**：`defense`、`multi-image toxicity`、`compositional semantics`、`reasoning distillation`

👤 **作者**：Jiaxian Lv、Shiyao Cui、Yingkang Wang、Guoxin Wu、Qingling Zhang、Minlie Huang

- 🎯 **研究动机**：多图隐式毒性（单图良性、组合有害）缺乏显性风险线索，商业审核 API 与模型难以识别
- 🔬 **研究方法**：形式化 MIIT 检测三挑战，经自动生成管线构建七类风险的多图数据集，并以渐进蒸馏推理监督训练 MiShield 输出带关联实体分析的判断
- 📌 **结论**：MiShield-8B 超过代表性审核服务与更大规模模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-image content has become an increasingly prevalent form of visual communication in social media, giving rise to a new safety issue, multi-image implicit toxicity (MIIT), where each image appears benign in isolation, but harmful semantics emerge when the images are interpreted jointly. MIIT is particularly challenging for existing commercial moderation APIs and models due to the lack of explicit risky cues in each image. This paper aims to study how to identify MIIT. We first provide a formal definition of MIIT and analyze three key challenges for its detection. To alleviate the scarcity of data in this area, we construct MIIT-dataset, an image-only multi-image safety dataset covering seven representative risk categories through an automatic generation pipeline. Finally, we train MiShield with progressively distilled reasoning supervision, enabling it to produce safety judgments accompanied by explicit analyses of the correlated entities that result in the hazards. Experiments show that MiShield-8B models outperform representative moderation services and even larger-scale models, revealing its effectiveness and practical value for this widely used visual format. Warning: This paper contains potentially sensitive content.

</details>

### 31. Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation

📄 [arXiv](https://arxiv.org/abs/2604.06950) · 📊 [Dataset](https://huggingface.co/datasets/zhihengli-casia/smugglebench) · 🌐 [Project](https://zhihengli-casia.github.io/Smugglebench/) · 📝 [OpenReview](https://openreview.net/forum?id=dRwsN1DvNV) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1006/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`visual smuggling`、`perceptual blindness`、`reasoning blockade`、`VLM content moderation`、`OCR reasoning`

👤 **作者**：Zhiheng Li、…、Weiming Hu

- 🎯 **研究动机**：对抗走私攻击利用人-AI 能力差，把有害内容编码成人可读而 AI 不可读的视觉格式以逃避自动审核
- 🔬 **研究方法**：分为感知致盲（破坏文字识别）与推理封锁（识别成功但语义理解受阻）两条路径，构建含 1,700 条实例的 SmuggleBench
- 📌 **结论**：GPT-5 与 Qwen3-VL 等 SOTA 审核 ASR 均超 90%；根因是视觉编码器能力有限、OCR 鲁棒性缺口与领域对抗样本稀缺

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) are increasingly being deployed as automated content moderators. Within this landscape, we uncover a critical threat: Adversarial Smuggling Attacks. Unlike adversarial perturbations (for misclassification) and adversarial jailbreaks (for harmful output generation), adversarial smuggling exploits the Human-AI capability gap. It encodes harmful content into human-readable visual formats that remain AI-unreadable, thereby evading automated detection and enabling the dissemination of harmful content. We classify smuggling attacks into two pathways: (1) Perceptual Blindness, disrupting text recognition; and (2) Reasoning Blockade, inhibiting semantic understanding despite successful text recognition. To evaluate this threat, we constructed SmuggleBench, the first comprehensive benchmark comprising 1,700 adversarial smuggling attack instances. Evaluations on SmuggleBench reveal that both proprietary (e.g., GPT-5) and open-source (e.g., Qwen3-VL) state-of-the-art models are vulnerable to this threat, producing Attack Success Rates (ASR) exceeding 90%. By analyzing the vulnerability through the lenses of perception and reasoning, we identify three root causes: the limited capabilities of vision encoders, the robustness gap in OCR, and the scarcity of domain-specific adversarial examples. We conduct a preliminary exploration of mitigation strategies, investigating the potential of test-time scaling (via CoT) and adversarial training (via SFT) to mitigate this threat. Our code is publicly available at https://github.com/zhihengli-casia/smugglebench.

</details>

### 32. CrossGuard: Safeguarding MLLMs against Joint-Modal Implicit Malicious Attacks

📄 [arXiv](https://arxiv.org/abs/2510.17687) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1178/)　📅 2025-10　🏷 ACL 2026

**关键词**：`defense`、`joint-modal attack`、`implicit intent`、`adversarial data generation`、`multimodal safety`、`jailbreak defense`

👤 **作者**：Xu Zhang、Hao Li、Zhichao Lu

- 🎯 **研究动机**：MLLM 面临图文联合表达不安全意图的隐式攻击，高质量隐式数据稀缺导致防御不足
- 🔬 **研究方法**：ImpForge 用强化学习与定制奖励模块自动生成 14 域多样隐式样本，据此训练意图感知 guardrail CrossGuard
- 📌 **结论**：在安全与不安全基准、隐式与显式攻击及多个域外设定下超越先进 MLLM 与现有 guardrail，兼顾安全与效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) achieve strong reasoning and perception capabilities but are increasingly vulnerable to jailbreak attacks. While existing work focuses on explicit attacks, where malicious content resides in a single modality, recent studies reveal implicit attacks, in which benign text and image inputs jointly express unsafe intent. Such joint-modal threats are difficult to detect and remain underexplored, largely due to the scarcity of high-quality implicit data. We propose ImpForge, an automated red-teaming pipeline that leverages reinforcement learning with tailored reward modules to generate diverse implicit samples across 14 domains. Building on this dataset, we further develop CrossGuard, an intent-aware safeguard providing robust and comprehensive defense against both explicit and implicit threats. Extensive experiments across safe and unsafe benchmarks, implicit and explicit attacks, and multiple out-of-domain settings demonstrate that CrossGuard significantly outperforms existing defenses, including advanced MLLMs and guardrails, achieving stronger security while maintaining high utility. This offers a balanced and practical solution for enhancing MLLM robustness against real-world multimodal threats. Our code is released: https://github.com/ZhangXu0963/CrossGuard.

</details>

### 33. SafeGuider: Robust and Practical Content Safety Control for Text-to-Image Models

📄 [arXiv](https://arxiv.org/abs/2510.05173)　📅 2025-10　🏷 ACM CCS 2025

**关键词**：`defense`、`T2I guardrail`、`embedding recognition`、`safe feature erasure`

👤 **作者**：Peigui Qi、…、Jie Zhang

- 🎯 **研究动机**：T2I 模型防御难以兼顾对抗鲁棒性与实际可用性
- 🔬 **研究方法**：发现 SD 文本编码器的 [EOS] token 作为语义聚合器在良性与对抗 prompt 间呈不同嵌入分布，据此组合嵌入级识别模型与安全感知特征擦除束搜索
- 📌 **结论**：各攻击场景 ASR 最高仅 5.48%，对不安全 prompt 生成安全有意义的图像而非拒答或黑图，可迁移至 Flux

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image models have shown remarkable capabilities in generating high-quality images from natural language descriptions. However, these models are highly vulnerable to adversarial prompts, which can bypass safety measures and produce harmful content. Despite various defensive strategies, achieving robustness against attacks while maintaining practical utility in real-world applications remains a significant challenge. To address this issue, we first conduct an empirical study of the text encoder in the Stable Diffusion (SD) model, which is a widely used and representative text-to-image model. Our findings reveal that the [EOS] token acts as a semantic aggregator, exhibiting distinct distributional patterns between benign and adversarial prompts in its embedding space. Building on this insight, we introduce SafeGuider, a two-step framework designed for robust safety control without compromising generation quality. SafeGuider combines an embedding-level recognition model with a safety-aware feature erasure beam search algorithm. This integration enables the framework to maintain high-quality image generation for benign prompts while ensuring robust defense against both in-domain and out-of-domain attacks. SafeGuider demonstrates exceptional effectiveness in minimizing attack success rates, achieving a maximum rate of only 5.48\% across various attack scenarios. Moreover, instead of refusing to generate or producing black images for unsafe prompts, SafeGuider generates safe and meaningful images, enhancing its practical utility. In addition, SafeGuider is not limited to the SD model and can be effectively applied to other text-to-image models, such as the Flux model, demonstrating its versatility and adaptability across different architectures. We hope that SafeGuider can shed some light on the practical deployment of secure text-to-image systems.

</details>

### 34. Old Tricks, New Models: How Simple Image Transformations Break Modern AI-based Content Moderation

📄 [arXiv](https://arxiv.org/abs/2607.28187)　📅 2026-07

**关键词**：`attack`、`image transformation`、`commercial moderator`、`black-box evasion`

👤 **作者**：Marco Alecci、Francesco Marchiori、Iyiola Emmanuel Olatunji、Tegawendé F. Bissyandé、Jacques Klein

- 🎯 **研究动机**：商用多模态内容审核 API 自称比传统分类器更安全，其对抗鲁棒性缺乏黑盒检验
- 🔬 **研究方法**：对三家商用图像审核服务评测七种简单模型无关图像变换（颜色反转、灰度化等）的绕过效果，覆盖多数据集与伤害类别
- 📌 **结论**：三家服务均可被无梯度、无代理模型、无目标系统知识的廉价变换绕过，多模态内容与自残类别漏洞最突出

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While automated content-moderation systems have become essential for screening harmful content at scale, conventional task-specific classifiers often provide limited policy cov- erage and contextual understanding. Recently, commercial multimodal moderation APIs built on large foundation models have been introduced with the promise of providing broader and more capable safety filters. In this work, we analyze whether this shift also yields more robust image moderation. We conduct a large-scale black-box evaluation on three established commercial image-moderation services and compare their robustness. By evaluating seven simple, model-agnostic image transformations across multiple providers, datasets, harm categories, perceptual-similarity constraints, and transformation intensities, we find that: (1) all three commercial services can be bypassed using inexpensive image transformations that require no gradients, surrogate models, or knowledge of the target system; (2) even fixed transformations such as color inversion and grayscale conversion induce unsafe-to-safe decision changes while preserving content that remains recognizable to humans; (3) their robustness varies substantially across datasets and harm categories, with multimodal content and self-harm exhibiting pronounced vulnerabilities. This yields the conclusion that replacing conventional moderation classifiers with foundation-model-based APIs does not, by itself, provide a reliable security boundary. Such systems must be evaluated under realistic transformations and deployed as one component of a layered moderation pipeline rather than as standalone safety filters.

</details>

### 35. Red-Teaming NSFW Image Classifiers as Text-to-Image Safeguards

🎓 [Official](https://aclanthology.org/2026.findings-acl.506/)　📅 2026-07　🏷 ACL 2026

**关键词**：`attack`、`NSFW classifier`、`context shift`、`T2I safeguard`

👤 **作者**：Tinghao Xie、…、Li Chen

- 🎯 **研究动机**：NSFW 图像分类器是 T2I 系统的关键防线，但改变良性图像元素的上下文漂移（context shift）会使其漏检
- 🔬 **研究方法**：自动化红队框架：先合成 36K NSFW 图像研究上下文漂移漏检，再用失败案例训练专用 LLM 改写未见种子提示使其更隐蔽
- 📌 **结论**：GPT-4o、Gemini 等对 4.1%-36% 的内容漏检；改写使漏检概率最高提升 6 倍，DALL-E 3 上获取 NSFW 图像概率从 0 升至超 50%，并波及 Sora、Veo 3 等系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Not Safe for Work (NSFW) image classifiers play a critical role in safeguarding text-to-image (T2I) systems. However, a concerning phenomenon has emerged in T2I systems – changes in text prompts that manipulate benign image elements can result in failed detection by NSFW classifiers – dubbed “ context shifts.” For instance, while a NSFW image of “ a nude person in an empty scene ” can be easily blocked by most NSFW classifiers, a stealthier one that depicts “ a nude person blending in a group of dressed people ” may evade detection. We ask: how to systematically reveal NSFW image classifiers’ failure against such context shifts?Towards this end, we present an automated red-teaming framework that leverages a set of generative AI tools. We propose an exploration-exploitation approach: First, in the exploration stage, we synthesize a diverse and massive 36K NSFW image dataset that facilitates our study of context shifts. We find that varying fractions (e.g., 4.1% to 36% nude and sexual content) of the dataset are misclassified by NSFW image classifiers like GPT-4o and Gemini. Second, in the exploitation stage, we leverage these failure cases to train a specialized LLM that rewrites unseen seed prompts into more evasive versions, increasing the likelihood of detection evasion by up to 6 times. Alarmingly, we show these failures translate to real-world T2I and even T2V systems like DALL-E 3, Sora, Nano Banana, and Veo 3 – beyond the open-weight image generators in our main study. For example, querying DALL-E 3 with prompts rewritten by our approach increases the chance of obtaining NSFW images from 0 to over 50%.

</details>

### 36. RedEdit: Agentic Red-Teaming of Image Safety Classifiers via MCTS-Guided Photo-Editing

📄 [arXiv](https://arxiv.org/abs/2606.06140)　📅 2026-06

**关键词**：`attack`、`image safety classifier`、`MCTS editing`、`evasion robustness`

👤 **作者**：Weilin Lin、…、Li Liu

- 🎯 **研究动机**：图像安全分类器面对用户式恶意修图的韧性未被探索，此类行为日常高频却难以复现
- 🔬 **研究方法**：提出 RedEdit 黑盒红队 agent：VLM proposer 生成语义定向候选编辑，MCTS 规划器优先有希望路径并回退无效路径，将规避问题化为编辑工具序列的组合搜索
- 📌 **结论**：UnsafeBench 上平均不到两次编辑即使 76.2% 不安全图像逃逸检测，同时保留 93.0% 恶意语义——人眼可见恶意却绕过自动审核

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Image safety classifiers serve as a critical component of contemporary content moderation systems on the internet. However, their resilience against user-style malicious image editing remains underexplored. Such behaviors are highly prevalent in daily scenarios but difficult to fully reproduce. To explore this vulnerability, we introduce RedEdit, a novel black-box red-teaming agent that formulates photo-editing evasion as a combinatorial search problem over edit-tool sequences. It adopts a Vision-Language-Model (VLM)-based proposer to generate semantically targeted candidate edits and a Monte Carlo Tree Search (MCTS) planner to prioritize promising edit paths while backtracking from ineffective ones. Together, the proposer and planner instantiate two key capabilities of human attackers, i.e., domain knowledge and iterative backtracking, respectively, to reproduce this practical threat. Our extensive experiments on UnsafeBench reveal profound systemic vulnerabilities: fewer than two edits on average enable 76.2% of unsafe images to evade detectors, while retaining 93.0% malicious semantics, meaning that such manipulated content remains perceptually malicious to humans while easily bypassing automated moderation. We therefore appeal to the community for more attention to this overlooked practical threat.

</details>

### 37. Decoding Multimodal Cues: Unveiling the Implicit Meaning Behind Hateful Videos

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

### 38. From Failure Taxonomy to Intervention: A Diagnostic Methodology for Industry-Scale AVLM in Video and Live-Streaming Platform Moderation

📄 [arXiv](https://arxiv.org/abs/2606.30059)　📅 2026-06

**关键词**：`analysis`、`industrial AVLM`、`live-stream moderation`、`failure-guided intervention`

👤 **作者**：Shuchang Ye、…、Zheng Yu

- 🎯 **研究动机**：工业级音视频直播审核需要适配平台分布、策略与产品约束，公开研究缺乏从失败定位到干预映射的方法论
- 🔬 **研究方法**：提出诊断方法论：把模型失败映射为可观察失败签名分类法，并把每类失败关联到干预空间；在覆盖 100+ 地区的大规模平台 AVLM 开发对齐生命周期中实例化
- 📌 **结论**：方法论支撑了工业级 AVLM 审核系统的开发与对齐，可处理全球流量中噪声、歧义与高多样内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Industry-scale video and live-streaming moderation imposes requirements that are difficult to satisfy with generic pretrained public models or external APIs, including adaptation to platform-specific data distributions, policy-specific objectives, and product-level safety constraints. As a result, platforms must undertake internal model development, naturally turning to shared public research for guidance. However, existing multimodal foundation-model studies primarily report architectures, training recipes, data scaling strategies, and benchmark results, but provide less systematic guidance on how failures should be localized and translated into targeted model-development interventions. Interventions are essential because deployment failures are rarely self-explanatory. Similar failures can originate from different causes. Without targeted interventions, improvement reduces to heuristic trial-and-error, where benchmark improvements are weakly attributable, and failures are difficult to trace to their underlying causes. To address this gap, we present a diagnostic methodology for industry-scale Audio-Visual-Language Models AVLM development. The methodology maps model failures into a taxonomy of observable failure signatures and links each class of failure to an intervention space. We instantiate this methodology across the development and alignment lifecycle of an AVLM foundation model for a large-scale video and live-streaming platform. The resulting system supports over 100 regions and is designed for noisy, ambiguous, and highly diverse content drawn from global platform traffic.

</details>

### 39. UNIVID: Unified Vision-Language Model for Video Moderation

📄 [arXiv](https://arxiv.org/abs/2606.05748) · 🎓 [Official](https://aclanthology.org/2026.acl-industry.32/)　📅 2026-06　🏷 ACL 2026

**关键词**：`tool`、`video moderation`、`policy-aware caption`、`industrial deployment`

👤 **作者**：Kejuan Yang、…、Kenan Xiao

- 🎯 **研究动机**：全球规模视频审核需细粒度多模态推理与可解释输出，传统碎片化黑盒分类器难维护且不透明
- 🔬 **研究方法**：构建 UNIVID 统一视觉语言模型，生成策略感知的可解释 caption 作为中间表示，用专家精标+合成数据的训练配方对齐安全规范，并设计端到端审核系统
- 📌 **结论**：违规漏放相对降低 42.7%、过度封禁降低 37.0%，单一 backbone 取代 1,000+ 策略模型并大幅降低维护成本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Global-scale video moderation faces a dual challenge: the need for fine-grained multi-modal reasoning and the demand for interpretable outputs to support downstream enforcement. Traditional moderation systems often rely on fragmented black-box classifiers that are difficult to maintain and lack transparency. In this paper, we present UNIVID, a UNIfied VIsion-language model for video moDeration. Unlike standard classification models, UNIVID generates policy-aware captions that serve as an interpretable intermediate representation, enabling human-verifiable decisions and multi-task reusability. While existing open-source and commercial VLMs often suffer from safety-guardrail refusals and lack fine-grained policy alignment, we develop a specialized training data recipe that combines expert human-refined labels with synthetic data to align the model with our safety guidelines. By integrating UNIVID as the core captioner, we design a novel end-to-end video moderation system that reduces violation leakage by 42.7% and overkill rate by 37.0% relatively. Meanwhile, by replacing over 1,000 policy-specific models with a single UNIVID backbone, we recycled extensive computation resources while reducing engineering maintenance overhead. To our knowledge, this is one of the first reports of a high-efficiency captioning VLM successfully supporting industrial-scale moderation and cross-functional business.

</details>

### 40. SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening

📄 [arXiv](https://arxiv.org/abs/2605.17610)　📅 2026-05

**关键词**：`defense`、`video guard`、`fast-slow routing`、`test-time reasoning`

👤 **作者**：Shahriar Kabir Nahin、Hadi Askari、Muhao Chen、Anshuman Chhabra

- 🎯 **研究动机**：现有视频护栏用大型 VLM 均匀处理所有输入，推理成本高且算力分配低效
- 🔬 **研究方法**：SafeLens 快慢双路架构：快速模式识别筛选多数输入、慢路径对时序复杂内容与细节政策做深推理；对 SafeWatch 做影响引导过滤仅留 2.4% 数据并增结构化 CoT 支持测试时推理
- 📌 **结论**：超过 SafeWatch-8B、OmniGuard-7B 与 GPT-5.4、Gemini-3.1-pro 等闭源模型，同时显著降低推理成本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of online video platforms and AI-generated content has made reliable video guardrails a key challenge for safety and real-world deployment. While most videos can be screened through fast pattern recognition, a small subset requires deeper reasoning over temporally complex content and nuanced policy constraints. Existing approaches typically rely on large vision-language models applied uniformly across all inputs, resulting in high inference costs and inefficient allocation of computation. We propose SafeLens, a video guardrail framework that introduces a fast-and-slow inference architecture for efficient and accurate content moderation with variable computational cost across inputs. Additionally, we construct a high-quality dataset by applying influence-guided filtering to the SafeWatch Dataset, retaining only 2.4% of the original data. To further address limitations of training-time scaling, we enable test-time reasoning by augmenting the filtered data with structured Chain-of-Thought traces. Across real-world and AI-generated video benchmarks, SafeLens achieves state-of-the-art performance, outperforming strong open-source video guardrails (e.g., SafeWatch-8B, OmniGuard-7B) and closed-source models (e.g., GPT-5.4, Gemini-3.1-pro) while significantly reducing inference cost, demonstrating that efficient design serves to be more effective than scaling data or model size alone.

</details>

### 41. AudioGuard: Toward Comprehensive Audio Safety Protection Across Diverse Threat Models

📄 [arXiv](https://arxiv.org/abs/2604.08867)　📅 2026-04

**关键词**：`defense`、`audio guardrail`、`audio-native risk`、`policy grounding`

👤 **作者**：Mintong Kang、Chen Fang、Bo Li

- 🎯 **研究动机**：音频安全不止不安全文本的语音化，还含原生有害声音事件、说话人属性与音画组合伤害，缺乏全面基准与护栏
- 🔬 **研究方法**：大规模红队后建立 policy-grounded 风险 taxonomy 与 AudioSafetyBench；AudioGuard 组合波形级 SoundGuard 与语义级 ContentGuard
- 📌 **结论**：在 AudioSafetyBench 及四个补充基准上以更低延迟持续超过 audio-LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio has rapidly become a primary interface for foundation models, powering real-time voice assistants. Ensuring safety in audio systems is inherently more complex than just "unsafe text spoken aloud": real-world risks can hinge on audio-native harmful sound events, speaker attributes (e.g., child voice), impersonation/voice-cloning misuse, and voice-content compositional harms, such as child voice plus sexual content. The nature of audio makes it challenging to develop comprehensive benchmarks or guardrails against this unique risk landscape. To close this gap, we conduct large-scale red teaming on audio systems, systematically uncover vulnerabilities in audio, and develop a comprehensive, policy-grounded audio risk taxonomy and AudioSafetyBench, the first policy-based audio safety benchmark across diverse threat models. AudioSafetyBench supports diverse languages, suspicious voices (e.g., celebrity/impersonation and child voice), risky voice-content combinations, and non-speech sound events. To defend against these threats, we propose AudioGuard, a unified guardrail consisting of 1) SoundGuard for waveform-level audio-native detection and 2) ContentGuard for policy-grounded semantic protection. Extensive experiments on AudioSafetyBench and four complementary benchmarks show that AudioGuard consistently improves guardrail accuracy over strong audio-LLM-based baselines with substantially lower latency.

</details>

### 42. Now You Hear Me: Audio Narrative Attacks Against Large Audio–Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.278/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`audio guardrail`、`narrative jailbreak`、`cross-modal policy gap`、`audio-language model`、`TTS delivery`

👤 **作者**：Ye Yu、Haibo Jin、Yaoning Yu、Jun Zhuang、Haohan Wang

- 🎯 **研究动机**：大音频语言模型直接处理原始语音，安全机制主要为文本校准，音频域漏洞未被表征
- 🔬 **研究方法**：用指令跟随 TTS 把被禁指令嵌入叙事式音频流，利用结构与声学特性绕过文本校准的安全机制
- 📌 **结论**：Gemini 2.0 Flash 等模型上合成语音叙事攻击成功率 98.26%，大幅超纯文本基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large audio-language models increasingly operate on raw speech inputs, enabling more seamless integration across domains such as voice assistants, education, and clinical triage. This transition, however, introduces a distinct class of vulnerabilities that remain largely uncharacterized. We examine the security implications of this modality shift by designing a text-to-audio jailbreak that embeds disallowed directives within a narrative-style audio stream. The attack leverages an advanced instruction-following text-to-speech (TTS) model to exploit structural and acoustic properties, thereby circumventing safety mechanisms primarily calibrated for text. When delivered through synthetic speech, the narrative format elicits restricted outputs from state-of-the-art models, including Gemini 2.0 Flash, achieving a 98.26% success rate that substantially exceeds text-only baselines. These results highlight the need for safety frameworks that jointly reason over linguistic and paralinguistic representations, particularly as speech-based interfaces become more prevalent.

</details>

### 43. Evolving Contextual Safety in Multi-Modal Large Language Models via Inference-Time Self-Reflective Memory

📄 [arXiv](https://arxiv.org/abs/2603.15800) · 🌐 [Project](https://echosafe-mllm.github.io) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Evolving_Contextual_Safety_in_Multi-Modal_Large_Language_Models_via_Inference-Time_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`contextual safety`、`self-reflective memory`、`training-free adaptation`、`test-time adaptation`

👤 **作者**：Ce Zhang、Jinxi He、Junyi He、Katia Sycara、Yaqi Xie

- 🎯 **研究动机**：现有越狱防御只检测拒绝显式不安全输入，忽视相似场景间安全意图迥异的上下文安全
- 🔬 **研究方法**：MM-SafetyBench++ 为每个不安全图文对构造最小修改翻转意图的安全对应项；EchoSafe 免训练维护自反思记忆库，检索往期安全洞见注入当前提示
- 📌 **结论**：在多个多模态安全基准上持续领先，实现推理时安全行为的持续演化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-modal Large Language Models (MLLMs) have achieved remarkable performance across a wide range of visual reasoning tasks, yet their vulnerability to safety risks remains a pressing concern. While prior research primarily focuses on jailbreak defenses that detect and refuse explicitly unsafe inputs, such approaches often overlook contextual safety, which requires models to distinguish subtle contextual differences between scenarios that may appear similar but diverge significantly in safety intent. In this work, we present MM-SafetyBench++, a carefully curated benchmark designed for contextual safety evaluation. Specifically, for each unsafe image-text pair, we construct a corresponding safe counterpart through minimal modifications that flip the user intent while preserving the underlying contextual meaning, enabling controlled evaluation of whether models can adapt their safety behaviors based on contextual understanding. Further, we introduce EchoSafe, a training-free framework that maintains a self-reflective memory bank to accumulate and retrieve safety insights from prior interactions. By integrating relevant past experiences into current prompts, EchoSafe enables context-aware reasoning and continual evolution of safety behavior during inference. Extensive experiments on various multi-modal safety benchmarks demonstrate that EchoSafe consistently achieves superior performance, establishing a strong baseline for advancing contextual safety in MLLMs. All benchmark data and code are available at https://echosafe-mllm.github.io.

</details>

### 44. GuardReasoner-Omni: A Reasoning-based Multi-modal Guardrail for Text, Image, Video, and Audio

📄 [arXiv](https://arxiv.org/abs/2602.03328)　📅 2026-02

**关键词**：`defense`、`omni-modal guard`、`SFT-RL training`、`concise reasoning`

👤 **作者**：Zhenhao Zhu、…、Jiaheng Zhang

- 🎯 **研究动机**：不同模态分别部署 guard 造成安全策略与接口割裂
- 🔬 **研究方法**：构建 181K 文本、图像、视频、音频四模态语料，先 SFT 冷启动推理能力与结构遵循，再用简洁正确性奖励的 RL 保持准确推理并抑制冗余生成
- 📌 **结论**：发布 3B/7B 两个规模的模型，在多个 guardrail 基准上超越 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present GuardReasoner-Omni, a reasoning-based guardrail model designed to moderate text, image, video, and audio data. First, we construct a comprehensive training corpus comprising 181k samples spanning these four modalities. Our training pipeline follows a two-stage paradigm to incentivize the model to deliberate before making decisions: (1) conducting SFT to cold-start the model with explicit reasoning capabilities and structural adherence; and (2) performing RL with a concise correctness reward to preserve accurate reasoning while suppressing redundant generation. We release a suite of models scaled at 3B and 7B parameters. Extensive experiments demonstrate that GuardReasoner-Omni achieves superior performance compared to existing state-of-the-art baselines across various guardrail benchmarks.

</details>

### 45. From Sparse Decisions to Dense Reasoning: A Multi-attribute Trajectory Paradigm for Multimodal Moderation

📄 [arXiv](https://arxiv.org/abs/2602.02536)　📅 2026-01

**关键词**：`defense`、`UniMod`、`multi-attribute trajectory`、`dense supervision`

👤 **作者**：Tianle Gu、…、Yingchun Wang

- 🎯 **研究动机**：多模态审核受数据与监督双重稀疏限制，二值标签诱发捷径学习、模糊类间边界
- 🔬 **研究方法**：UniMod 把稀疏决策转为证据接地、模态评估、风险映射、政策决策与响应生成的稠密轨迹，配套多头标量奖励模型 UniRM 提供属性级监督及解耦任务参数的优化策略
- 📌 **结论**：文本审核具竞争力，以不足领先基线 40% 的训练数据刷新多模态审核基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety moderation is pivotal for identifying harmful content. Despite the success of textual safety moderation, its multimodal counterparts remain hindered by a dual sparsity of data and supervision. Conventional reliance on binary labels lead to shortcut learning, which obscures the intrinsic classification boundaries necessary for effective multimodal discrimination. Hence, we propose a novel learning paradigm (UniMod) that transitions from sparse decision-making to dense reasoning traces. By constructing structured trajectories encompassing evidence grounding, modality assessment, risk mapping, policy decision, and response generation, we reformulate monolithic decision tasks into a multi-dimensional boundary learning process. This approach forces the model to ground its decision in explicit safety semantics, preventing the model from converging on superficial shortcuts. To facilitate this paradigm, we develop a multi-head scalar reward model (UniRM). UniRM provides multi-dimensional supervision by assigning attribute-level scores to the response generation stage. Furthermore, we introduce specialized optimization strategies to decouple task-specific parameters and rebalance training dynamics, effectively resolving interference between diverse objectives in multi-task learning. Empirical results show UniMod achieves competitive textual moderation performance and sets a new multimodal benchmark using less than 40\% of the training data used by leading baselines. Ablations further validate our multi-attribute trajectory reasoning, offering an effective and efficient framework for multimodal moderation. Supplementary materials are available at \href{https://trustworthylab.github.io/UniMod/}{project website}.

</details>

### 46. Shot-Conditioned Vision-Language Adaptation for Effective Harmful Content Detection from Online Short Videos

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/2149.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`harmful short video`、`shot-conditioned adaptation`、`temporal moderation`、`shot adaptation`、`vision-language model`

- 🎯 **研究动机**：短视频有害检测面临频繁剪辑切分与异常密度高度可变，现有 VLM 方法依赖刚性实例选择机制，无法适配不可预测的异常时长
- 🔬 **研究方法**：提出 SVLA：π 自适应策略动态估计镜头级异常密度替代刚性选择，配合镜头条件时间编码器与双路上下文 adapter，并构建含 7 类异常的 SVA 数据集
- 📌 **结论**：在 SVA 数据集上达到 SOTA，并在多样场景中全面超越对手方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Short video harmful content detection aims to automatically identify diverse anomalies from user-generated media. This task presents unique challenges due to frequent editing cuts and highly variable anomaly densities, limiting the effectiveness of traditional surveillance-based approaches. Moreover, existing Vision-Language Model-based approaches typically rely on rigid instance selection mechanisms that fail to adapt to the unpredictable duration of anomalies in such unconstrained videos. To address these issues, we propose SVLA, a Shot-conditioned Vision-Language Adaptation framework, for effectively detecting harmful contents from online short videos. Our approach introduces a novel π-adaptive strategy to dynamically estimate shot-level anomaly density, replacing rigid selection with calibrated supervision. Furthermore, we employ a shot-conditioned temporal encoder to respect video hierarchy and adopt a dual-path contextual adapter to resolve semantic ambiguity. To benchmark this task, we construct a new dataset (SVA) covering more genuine online short videos that involve seven anomaly categories. Experiments on the SVA dataset demonstrate that SVLA can achieve the state-of-the-art performance and outperform its competitors across diverse scenarios. Codes and datasets are available at: https://github.com/xushuai7/IJCAI-SVLA.

</details>

### 47. OmniGuard: Unified Omni-Modal Guardrails with Deliberate Reasoning

📄 [arXiv](https://arxiv.org/abs/2512.02306) · 🌐 [Project](https://luka-group.github.io/OmniGuard_webpage/)　📅 2025-12

**关键词**：`defense`、`omni-modal moderation`、`policy critique`、`cross-modal data`

👤 **作者**：Boyu Zhu、…、Muhao Chen

- 🎯 **研究动机**：已有 guardrail 研究多针对单模态并以二分类建模，难以覆盖全模态输入的安全需求
- 🔬 **研究方法**：OmniGuard 首个带深思熟虑推理的全模态 guardrail 家族，基于 210K 覆盖单模态与跨模态输入、带结构化安全标签与专家安全 critique 的数据集训练
- 📌 **结论**：在 15 个基准上跨多模态安全场景展现强有效性与泛化，提供统一的全模态策略执行框架

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Omni-modal Large Language Models (OLLMs) that process text, images, videos, and audio introduce new challenges for safety and value guardrails in human-AI interaction. Prior guardrail research largely targets unimodal settings and typically frames safeguarding as binary classification, which limits robustness across diverse modalities and tasks. To address this gap, we propose OmniGuard, the first family of omni-modal guardrails that performs safeguarding across all modalities with deliberate reasoning ability. To support the training of OMNIGUARD, we curate a large, comprehensive omni-modal safety dataset comprising over 210K diverse samples, with inputs that cover all modalities through both unimodal and cross-modal samples. Each sample is annotated with structured safety labels and carefully curated safety critiques from expert models through targeted distillation. Extensive experiments on 15 benchmarks show that OmniGuard achieves strong effectiveness and generalization across a wide range of multimodal safety scenarios. Importantly, OmniGuard provides a unified framework that enforces policies and mitigates risks in omni-modalities, paving the way toward building more robust and capable omnimodal safeguarding systems.

</details>

### 48. SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations

📄 [arXiv](https://arxiv.org/abs/2412.06878) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/beac6bfb7eac3d651307c16ac747df01-Abstract-Conference.html)　📅 2024-12　🏷 ICLR 2025

**关键词**：`defense`、`video guard`、`parallel policy encoding`、`visual token pruning`

👤 **作者**：Zhaorun Chen、Francesco Pinto、Minzhou Pan、Bo Li

- 🎯 **研究动机**：视频审核或用简单分类模型无解释，或让 MLLM 串行编码长安全策略、低效且有位置偏差
- 🔬 **研究方法**：SafeWatch 并行编码 policy chunk 消除位置偏差，配 policy-aware 视觉 token 剪枝；并发布 200 万+ 视频的 SafeWatch-Bench
- 📌 **结论**：较 SOTA 在自建基准提升 28.2%、外部基准提升 13.6%，成本降 10% 且解释质量居首

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rise of generative AI and rapid growth of high-quality video generation, video guardrails have become more crucial than ever to ensure safety and security across platforms. Current video guardrails, however, are either overly simplistic, relying on pure classification models trained on simple policies with limited unsafe categories, which lack detailed explanations, or prompting multimodal large language models (MLLMs) with long safety guidelines, which are inefficient and impractical for guardrailing real-world content. To bridge this gap, we propose SafeWatch, an efficient MLLM-based video guardrail model designed to follow customized safety policies and provide multi-label video guardrail outputs with content-specific explanations in a zero-shot manner. In particular, unlike traditional MLLM-based guardrails that encode all safety policies autoregressively, causing inefficiency and bias, SafeWatch uniquely encodes each policy chunk in parallel and eliminates their position bias such that all policies are attended simultaneously with equal importance. In addition, to improve efficiency and accuracy, SafeWatch incorporates a policy-aware visual token pruning algorithm that adaptively selects the most relevant video tokens for each policy, discarding noisy or irrelevant information. This allows for more focused, policy-compliant guardrail with significantly reduced computational overhead. Considering the limitations of existing video guardrail benchmarks, we propose SafeWatch-Bench, a large-scale video guardrail benchmark comprising over 2M videos spanning six safety categories which covers over 30 tasks to ensure a comprehensive coverage of all potential safety scenarios. SafeWatch outperforms SOTA by 28.2% on SafeWatch-Bench, 13.6% on benchmarks, cuts costs by 10%, and delivers top-tier explanations validated by LLM and human reviews.

</details>

### 49. Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines

📄 [arXiv](https://arxiv.org/abs/2608.29589)　📅 2026-09

**关键词**：`benchmark`、`analysis`、`dialect-aware moderation`、`false-positive disparity`、`under-detection`、`T2I safety pipeline`

👤 **作者**：Minkyu Kim、Juhwan Choi、YoungBin Kim

- 🎯 **研究动机**：T2I 安全护栏对非标准方言泛化不公平，均值精度 benchmark 掩盖了这一公平性失败
- 🔬 **研究方法**：在五种英语方言 23,080 对 prompt 上定义 dialect penalty，用 typo 消融定位根因，并测试 group-balanced retraining 缓解
- 📌 **结论**：NSFW-T 与 LatentGuard 出现最高 +28.29pp 且方向相反的 bias gap，OpenAI Moderation API 漏检方言内容；penalty 源于方言特征而非 OOD 敏感性，均衡重训练可缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) safety guardrails fail to generalize equitably to non-standard dialects. Evaluating 23,080 paired prompts across five English dialects, we formalize this failure as the dialect penalty, where filters trigger based on linguistic surface features rather than semantic intent. Text-level filters fail in opposing directions: NSFW-T over-flags benign dialect prompts and LatentGuard over-flags toxic ones (bias gaps up to +28.29 pp), while the OpenAI Moderation API under-detects them. A controlled typo ablation confirms this penalty originates from flagging dialectal features, not generic out-of-distribution sensitivity. The pixel-level generator is largely dialect-agnostic; the penalty enters at text processing and cascades unevenly to post-hoc guardrails. We show this bias tracks training data imbalance and is mitigable via group-balanced retraining, with an ablation attributing the gain to balanced exposure rather than to the worst-group objective of GroupDRO (group distributionally robust optimization). Current pipelines systematically fail dialect speakers, an equity failure masked by mean accuracy benchmarks. Our official code and dataset are publicly available at https://github.com/minguinho26/dialect-penalty-t2i. Content Warning: This paper contains offensive, toxic, or disturbing text prompts and generated images.

</details>

### 50. SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard Models

📄 [arXiv](https://arxiv.org/abs/2608.29098)　📅 2026-09

**关键词**：`tool`、`ordinal risk moderation`、`target-conditioned guard`、`disagreement-aware data`

👤 **作者**：Zongrui Wang、…、Guangtao Zhai

- 🎯 **研究动机**：现有多模态防护通常只面向单一判断目标并把安全压成二元决策，难以区分视觉内容、用户意图与助手行为的风险，模糊案例被掩盖
- 🔬 **研究方法**：构建 1.5M 实例的 SafeAtlas-VL 数据集，把图像、请求、响应三层判断放在五级有序量表上（15 类 55 子类、disagreement-aware 标注），配套 5000 条 held-out 的 SafeAtlas-Bench，经 target-conditioned tuning 训练 SafeAtlas Guard 系列，用 soft cumulative ordinal head 输出连续风险分
- 📌 **结论**：该数据训练的 guard 在五级分类与连续风险评分上表现更优，8B 模型未用其他 benchmark 训练集仍取得最佳总体表现，F1 约超此前 SOTA 4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal safety moderation requires distinguishing risks arising from visual content, user intent, and assistant behavior. Existing safeguards, however, are typically trained for a single judgment target and reduce safety assessment to a binary decision. Consequently, risk becomes difficult to compare across a multimodal interaction, and ambiguous cases are obscured. We introduce SafeAtlas-VL, a dataset of 1.5M training instances that places image-, request-, and response-level judgments on a five-level ordered scale. We curate a broad collection of safety-relevant data from both real-world and synthetic sources and apply a disagreement-aware annotation procedure. The resulting dataset spans 15 harm categories and 55 fine-grained subcategories, covering a broad range of multimodal safety scenarios. We also construct SafeAtlas-Bench, a held-out set of 5,000 instances for evaluating five-level predictions and continuous risk scores. Upon this dataset, we train the SafeAtlas Guard series of models via target-conditioned tuning for multimodal safety detection. Our models not only perform five-way classification of safety levels but also map safety to continuous scores through a soft cumulative ordinal head. Experimental results demonstrate that guard models trained on our dataset exhibit strong generalization: even without using the training sets of other benchmarks, they achieve competitive performance on the corresponding test sets. Notably, our 8B model attains the overall best performance, outperforming the previous SOTA by approximately 4% in F1 score. Code, data, and models are released to support further research. Warning: this paper contains example data that may be offensive, harmful, graphic, or disturbing.

</details>

### 51. Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation

📄 [arXiv](https://arxiv.org/abs/2608.26535)　📅 2026-08

**关键词**：`benchmark`、`omni-modal guardrail`、`compositional evidence`、`audio-video safety`、`audio-video generation`、`multimodal conditioning`

👤 **作者**：Kaichao Jiang、…、Nenghai Yu

- 🎯 **研究动机**：音视频生成转向多模态条件，危害可由良性条件跨模态与时间组合涌现，现有 benchmark 以 prompt 为中心
- 🔬 **研究方法**：Multi2AV-Safety 覆盖全部 11 种非单一 T/I/A/V 条件组合共 11024 个攻击实例，系统评测多模态安全 guard
- 📌 **结论**：单独良性输入可组合出有害语义，有害线索混入良性多模态上下文后更难检测，凸显 compositional risk perception 缺口

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio-video generation is rapidly moving from prompt-driven synthesis toward multimodal conditioning, where text, images, audio, and video can jointly shape the generated output. This shift changes the nature of safety evaluation: harmful intent may no longer reside in any single input, but instead emerge from how otherwise benign or weakly harmful conditions interact across modalities and time. Existing safety benchmarks, however, remain largely prompt-centric or tied to fixed conditioning interfaces, leaving such compositional risks difficult to study systematically. To bridge this gap, we introduce Multi2AV-Safety, the first safety benchmark, to the best of our knowledge, to cover all 11 non-singleton T/I/A/V conditioning configurations for audio-video generation, comprising 11,024 attack instances. Evaluation on Multi2AV-Safety reveals systematic weaknesses in representative multimodal safety guards across attack mechanisms and harm-evidence structures. Our evaluation reveals two complementary failure modes: harmful semantics can emerge from the combination of individually benign inputs, while explicit harmful cues can become harder to detect when mixed with benign multimodal context. Together, these results identify \emph{compositional risk perception} as a central capability gap in safeguarding multimodal-conditioned audio-video generation: current safety guards fail to reliably integrate safety evidence across modalities and time, even when all conditioning inputs are observable. The dataset will be publicly released in October 2026.

</details>

### 52. MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities

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

### 53. EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models

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

### 54. EVADE-Bench: Multimodal Benchmark for Evaluating and Enhancing Evasive Content Detection

📄 [arXiv](https://arxiv.org/abs/2505.17654) · 📊 [Dataset](https://huggingface.co/datasets/koenshen/EVADE-Bench) · 🌐 [Project](https://doi.org/10.1145/3805712.3808579)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`benchmark`、`e-commerce moderation`、`cross-modal evasion`、`policy circumvention`、`evasive content`、`multimodal decomposition`

👤 **作者**：Ancheng Xu、…、Min Yang

- 🎯 **研究动机**：电商审核模型对拆字、暗语、裁图等规避内容脆弱，且无基准同时考察规则理解与混淆意图推断
- 🔬 **研究方法**：构建专家策展的中文多模态 EVADE-Bench，评测 26 个开源与闭源 LLM 及 VLM 的规避内容检测
- 📌 **结论**：SoTA 模型频繁误判；清晰规则分类显著减少误报，视觉描述与逻辑推断解耦的多 agent 分解带来明显准确率增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

E-commerce platforms increasingly rely on Large Language Models (LLMs) and Vision Language Models (VLMs) to detect illicit or misleading product content. However, these models remain vulnerable to evasive content, which refers to inputs that have been deliberately modified through techniques such as word splitting, euphemistic language, or image cropping to conceal policy violations while still conveying prohibited claims. Crucially, detecting such content requires a model to simultaneously master two capabilities: accurately comprehending complex rules, and correctly inferring the true intent behind deliberately obfuscated multimodal inputs. While prior work has separately explored LLM reasoning over complex rules and LLM-based detection of evasive content, no existing benchmark combines both within a unified evaluation framework. This gap is particularly consequential in e-commerce, where accurate moderation demands that both capabilities operate in concert. To address this gap, we introduce EVADE-Bench, the first expert-curated Chinese multimodal benchmark specifically designed to evaluate LLMs and VLMs on evasive content detection in real-world e-commerce scenarios. Our comprehensive evaluation of 26 open- and closed-source LLMs and VLMs reveals that even state-of-the-art models frequently misclassify evasive samples. We further demonstrate that clearer rule categorization significantly improves model prediction consistency and reduces false predictions, highlighting the critical role of benchmark design in enabling reliable evaluation. To explore paths for performance improvement, we investigate the feasibility of multi-agent decomposition for multimodal reasoning, wherein visual description and logical inference are decoupled into separate agents, and find that this strategy yields notable accuracy gains.

</details>

### 55. Beyond Hate: Differentiating Uncivil and Intolerant Speech in Multimodal Content Moderation

📄 [arXiv](https://arxiv.org/abs/2603.22985)　📅 2026-03

**关键词**：`benchmark`、`multimodal moderation`、`incivility-intolerance split`、`error balance`

👤 **作者**：Nils A. Herrmann、Tobias Eder、Jingyi He、Georg Groh

- 🎯 **研究动机**：多模态毒性基准用单一二元标签混淆语气（incivility）与内容（intolerance）两个正交维度
- 🔬 **研究方法**：依据传播学理论为 Hateful Memes 的 2,030 个 meme 补充双维度细粒度标注，评测粗标签训练、迁移与联合学习
- 📌 **结论**：细粒度与粗标签联合提升整体表现且错误更均衡：LLaVA-1.6 的 FNR-FPR 从 0.74 降到 0.42，Qwen2.5-VL 从 0.54 降到 0.28

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current multimodal toxicity benchmarks typically use a single binary hatefulness label. This coarse approach conflates two fundamentally different characteristics of expression: tone and content. Drawing on communication science theory, we introduce a fine-grained annotation scheme that distinguishes two separable dimensions: incivility (rude or dismissive tone) and intolerance (content that attacks pluralism and targets groups or identities) and apply it to 2,030 memes from the Hateful Memes dataset. We evaluate different vision-language models under coarse-label training, transfer learning across label schemes and a joint learning approach that combines the coarse hatefulness label with our fine-grained annotations. Our results show that fine-grained annotations complement existing coarse labels and, when used jointly, improve overall model performance. Moreover, models trained with the fine-grained scheme exhibit more balanced moderation-relevant error profiles and are less prone to under-detection of harmful content than models trained on hatefulness labels alone (FNR-FPR, the difference between false negative and false positive rates: 0.74 to 0.42 for LLaVA-1.6-Mistral-7B; 0.54 to 0.28 for Qwen2.5-VL-7B). This work contributes to data-centric approaches in content moderation by improving the reliability and accuracy of moderation systems through enhanced data quality. Overall, combining both coarse and fine-grained labels provides a practical route to more reliable multimodal moderation.

</details>

### 56. From Native Memes to Global Moderation: Cross-Cultural Evaluation of Vision-Language Models for Hateful Meme Detection

📄 [arXiv](https://arxiv.org/abs/2602.07497) · 🌐 [Project](https://doi.org/10.1145/3774904.3793007)　📅 2026-02

**关键词**：`benchmark`、`cross-cultural meme`、`native-language prompting`、`translation bias`

👤 **作者**：Mo Wang、…、Usman Naseem

- 🎯 **研究动机**：VLM 以西方/英语为中心训练，跨文化仇恨 meme 检测的公平性与鲁棒性受限
- 🔬 **研究方法**：沿零样本/单样本、母语/英语提示、翻译效应三轴系统评测 SOTA VLM 的多语 meme 检测
- 📌 **结论**：translate-then-detect 损害检测性能，母语提示与 one-shot 学习显著提升，揭示模型系统性向西方安全规范收敛

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Cultural context profoundly shapes how people interpret online content, yet vision-language models (VLMs) remain predominantly trained through Western or English-centric lenses. This limits their fairness and cross-cultural robustness in tasks like hateful meme detection. We introduce a systematic evaluation framework designed to diagnose and quantify the cross-cultural robustness of state-of-the-art VLMs across multilingual meme datasets, analyzing three axes: (i) learning strategy (zero-shot vs. one-shot), (ii) prompting language (native vs. English), and (iii) translation effects on meaning and detection. Results show that the common ``translate-then-detect'' approach deteriorate performance, while culturally aligned interventions - native-language prompting and one-shot learning - significantly enhance detection. Our findings reveal systematic convergence toward Western safety norms and provide actionable strategies to mitigate such bias, guiding the design of globally robust multimodal moderation systems.

</details>

### 57. OutSafe-Bench: A Benchmark for Multimodal Offensive Content Detection in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2511.10287)　📅 2025-11

**关键词**：`benchmark`、`offensive content`、`bilingual evaluation`、`multi-judge voting`

👤 **作者**：Yuping Yan、Yuhan Xie、Yuanshuai Li、Yingchao Yu、Lingjuan Lyu、Yaochu Jin

- 🎯 **研究动机**：现有安全基准在模态覆盖与评测手段上有限，忽视内容安全的广泛谱系
- 🔬 **研究方法**：构建四模态双语数据集（1.8 万中英文本、4500 图像、450 音频、450 视频）与九类风险标注，提出跨风险度量 MCRS 与多评审加权聚合框架 FairScore
- 📌 **结论**：对 9 个 SOTA MLLM 的评测揭示持续且显著的安全漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Since Multimodal Large Language Models (MLLMs) are increasingly being integrated into everyday tools and intelligent agents, growing concerns have arisen regarding their possible output of unsafe contents, ranging from toxic language and biased imagery to privacy violations and harmful misinformation. Current safety benchmarks remain highly limited in both modality coverage and performance evaluations, often neglecting the extensive landscape of content safety. In this work, we introduce OutSafe-Bench, the first most comprehensive content safety evaluation test suite designed for the multimodal era. OutSafe-Bench includes a large-scale dataset that spans four modalities, featuring over 18,000 bilingual (Chinese and English) text prompts, 4,500 images, 450 audio clips and 450 videos, all systematically annotated across nine critical content risk categories. In addition to the dataset, we introduce a Multidimensional Cross Risk Score (MCRS), a novel metric designed to model and assess overlapping and correlated content risks across different categories. To ensure fair and robust evaluation, we propose FairScore, an explainable automated multi-reviewer weighted aggregation framework. FairScore selects top-performing models as adaptive juries, thereby mitigating biases from single-model judgments and enhancing overall evaluation reliability. Our evaluation of nine state-of-the-art MLLMs reveals persistent and substantial safety vulnerabilities, underscoring the pressing need for robust safeguards in MLLMs.

</details>

### 58. SafetyPairs: Isolating Safety Critical Image Features with Counterfactual Image Generation

📄 [arXiv](https://arxiv.org/abs/2510.21120) · 🎓 [Official](https://iclr.cc/virtual/2026/10019336)　📅 2025-10　🏷 ICLR 2026

**关键词**：`benchmark`、`counterfactual image`、`safety feature`、`causal diagnosis`

👤 **作者**：Alec Helbling、Shruti Palaskar、Kundan Krishna、Polo Chau、Leon Gatys、Joseph Yitan Cheng

- 🎯 **研究动机**：现有图像安全数据集只有粗粒度标签，未隔离驱动安全差异的具体视觉特征
- 🔬 **研究方法**：SafetyPairs 用图像编辑模型生成仅改变安全相关特征、从而翻转安全标签的反事实图像对，构建 9 类 3020 张图像的基准并用作数据增强
- 📌 **结论**：基准凸显 VLM 区分细微不同图像的弱点，该流水线也提升轻量 guard 模型训练的样本效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

What exactly makes a particular image unsafe? Systematically differentiating between benign and problematic images is a challenging problem, as subtle changes to an image, such as an insulting gesture or symbol, can drastically alter its safety implications. However, existing image safety datasets are coarse and ambiguous, offering only broad safety labels without isolating the specific features that drive these differences. We introduce SafetyPairs, a scalable framework for generating counterfactual pairs of images, that differ only in the features relevant to the given safety policy, thus flipping their safety label. By leveraging image editing models, we make targeted changes to images that alter their safety labels while leaving safety-irrelevant details unchanged. Using SafetyPairs, we construct a new safety benchmark, which serves as a powerful source of evaluation data that highlights weaknesses in vision-language models' abilities to distinguish between subtly different images. Beyond evaluation, we find our pipeline serves as an effective data augmentation strategy that improves the sample efficiency of training lightweight guard models. We release a benchmark containing over 3,020 SafetyPair images spanning a diverse taxonomy of 9 safety categories, providing the first systematic resource for studying fine-grained image safety distinctions.

</details>

### 59. VLSU: Mapping the Limits of Joint Multimodal Understanding for AI Safety

📄 [arXiv](https://arxiv.org/abs/2510.18214) · 📝 [OpenReview](https://openreview.net/forum?id=OzPAI04hi5) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009729)　📅 2025-10　🏷 ICLR 2026

**关键词**：`analysis`、`joint understanding`、`modality interaction`、`safety boundary`

👤 **作者**：Shruti Palaskar、…、Joseph Yitan Cheng

- 🎯 **研究动机**：多模态安全评测常分开处理视觉与语言输入，漏掉良性内容经联合解释变有害的风险，也难区分边界案例
- 🔬 **研究方法**：VLSU 以 17 种安全模式与细粒度严重度分级，经多阶段流水线与人工标注构建 8187 样本、15 类危害的基准，评测 11 个 SOTA 模型
- 📌 **结论**：单模态明确信号准确率超 90%，需图文联合推理时降至 20-55%；34% 的联合分类错误发生在单模态分类均正确时

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety evaluation of multimodal foundation models often treats vision and language inputs separately, missing risks from joint interpretation where benign content becomes harmful in combination. Existing approaches also fail to distinguish clearly unsafe content from borderline cases, leading to problematic over-blocking or under-refusal of genuinely harmful content. We present Vision Language Safety Understanding (VLSU), a comprehensive framework to systematically evaluate multimodal safety through fine-grained severity classification and combinatorial analysis across 17 distinct safety patterns. Using a multi-stage pipeline with real-world images and human annotation, we construct a large-scale benchmark of 8,187 samples spanning 15 harm categories. Our evaluation of eleven state-of-the-art models reveals systematic joint understanding failures: while models achieve 90%-plus accuracy on clear unimodal safety signals, performance degrades substantially to 20-55% when joint image-text reasoning is required to determine the safety label. Most critically, 34% of errors in joint image-text safety classification occur despite correct classification of the individual modalities, further demonstrating absent compositional reasoning capabilities. Additionally, we find that models struggle to balance refusing unsafe content while still responding to borderline cases that deserve engagement. For example, we find that instruction framing can reduce the over-blocking rate on borderline content from 62.4% to 10.4% in Gemini-1.5, but only at the cost of under-refusing on unsafe content with refusal rate dropping from 90.8% to 53.9%. Overall, our framework exposes weaknesses in joint image-text understanding and alignment gaps in current models, and provides a critical test bed to enable the next milestones in research on robust vision-language safety.

</details>

### 60. HoliSafe: Holistic Safety Benchmarking and Modeling for Vision-Language Model

📄 [arXiv](https://arxiv.org/abs/2506.04704)　📅 2025-06

**关键词**：`benchmark`、`image-text combinations`、`visual guard module`、`holistic safety`

👤 **作者**：Youngwan Lee、…、Sung Ju Hwang

- 🎯 **研究动机**：现有 VLM 安全数据只部分覆盖图文交互致害组合，且缺乏架构层面的安全增强
- 🔬 **研究方法**：构建覆盖全部五种安全/不安全图文组合的 HoliSafe 数据集与基准，并提出可插拔 visual guard module 评估输入图像危害
- 📌 **结论**：Safe-VLM 在多个 VLM 安全基准达 SoTA，并能输出可解释的危害分类作为拒绝依据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite emerging efforts to enhance the safety of Vision-Language Models (VLMs), current approaches face two main shortcomings. 1) Existing safety-tuning datasets and benchmarks only partially consider how image-text interactions can yield harmful content, often overlooking contextually unsafe outcomes from seemingly benign pairs. This narrow coverage leaves VLMs vulnerable to jailbreak attacks in unseen configurations. 2) Prior methods rely primarily on data-centric tuning, with limited architectural innovations to intrinsically strengthen safety. We address these gaps by introducing a holistic safety dataset and benchmark, \textbf{HoliSafe}, that spans all five safe/unsafe image-text combinations, providing a more robust basis for both training and evaluation (HoliSafe-Bench). We further propose a novel modular framework for enhancing VLM safety with a visual guard module (VGM) designed to assess the harmfulness of input images for VLMs. This module endows VLMs with a dual functionality: they not only learn to generate safer responses but can also provide an interpretable harmfulness classification to justify their refusal decisions. A significant advantage of this approach is its modularity; the VGM is designed as a plug-in component, allowing for seamless integration with diverse pre-trained VLMs across various scales. Experiments show that Safe-VLM with VGM, trained on our HoliSafe, achieves state-of-the-art safety performance across multiple VLM benchmarks. Additionally, the HoliSafe-Bench itself reveals critical vulnerabilities in existing VLM models. We hope that HoliSafe and VGM will spur further research into robust and interpretable VLM safety, expanding future avenues for multimodal alignment.

</details>

### 61. Unmasking the Canvas: A Dynamic Benchmark for Image Generation Jailbreaking and LLM Content Safety

📄 [arXiv](https://arxiv.org/abs/2505.04146)　📅 2025-05

**关键词**：`benchmark`、`image-generation jailbreak`、`multilingual obfuscation`、`dynamic curation`

👤 **作者**：Variath Madhupal Gautham Nair、Vishal Varma Dantuluri

- 🎯 **研究动机**：图像生成的内容安全检查易被 prompt 越狱绕过，短自然 prompt 即可生成伪造证件与名人操纵图像
- 🔬 **研究方法**：构建 UTCB 动态基准，结合结构化 prompt 工程、多语言混淆与 LLaMA-3 评估，按 Bronze/Silver/Gold 三级策展并支持风险评分
- 📌 **结论**：ChatGPT、MetaAI、Grok 等平台均被自然短 prompt 诱导生成高危图像，基准可持续演化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing large language models (LLMs) are advancing rapidly and produce outstanding results in image generation tasks, yet their content safety checks remain vulnerable to prompt-based jailbreaks. Through preliminary testing on platforms such as ChatGPT, MetaAI, and Grok, we observed that even short, natural prompts could lead to the generation of compromising images ranging from realistic depictions of forged documents to manipulated images of public figures. We introduce Unmasking the Canvas (UTC Benchmark; UTCB), a dynamic and scalable benchmark dataset to evaluate LLM vulnerability in image generation. Our methodology combines structured prompt engineering, multilingual obfuscation (e.g., Zulu, Gaelic, Base64), and evaluation using Groq-hosted LLaMA-3. The pipeline supports both zero-shot and fallback prompting strategies, risk scoring, and automated tagging. All generations are stored with rich metadata and curated into Bronze (non-verified), Silver (LLM-aided verification), and Gold (manually verified) tiers. UTCB is designed to evolve over time with new data sources, prompt templates, and model behaviors. Warning: This paper includes visual examples of adversarial inputs designed to test model safety. All outputs have been redacted to ensure responsible disclosure.

</details>

### 62. VLSBench: Unveiling Visual Leakage in Multimodal Safety

📄 [arXiv](https://arxiv.org/abs/2411.19939) · 🎓 [Official](https://aclanthology.org/2025.acl-long.405/)　📅 2024-11　🏷 ACL 2025

**关键词**：`benchmark`、`visual leakage`、`benign text`、`unsafe image`

👤 **作者**：Xuhao Hu、Dongrui Liu、Hao Li、Xuanjing Huang、Jing Shao

- 🎯 **研究动机**：现有多模态安全基准存在视觉安全信息泄漏（VSIL）：图像风险已被文本 query 泄露，评测虚高
- 🔬 **研究方法**：以自动数据管线构建无泄漏的 VLSBench（2.2k 图文对），并比较文本对齐与多模态对齐两种方案
- 📌 **结论**：对 LLaVA、Qwen2-VL、GPT-4o 均构成挑战；有 VSIL 时文本对齐已足够，无 VSIL 场景需多模态对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety concerns of Multimodal large language models (MLLMs) have gradually become an important problem in various applications. Surprisingly, previous works indicate a counterintuitive phenomenon that using textual unlearning to align MLLMs achieves comparable safety performances with MLLMs aligned with image text pairs. To explain such a phenomenon, we discover a Visual Safety Information Leakage (VSIL) problem in existing multimodal safety benchmarks, i.e., the potentially risky content in the image has been revealed in the textual query. Thus, MLLMs can easily refuse these sensitive image-text pairs according to textual queries only, leading to unreliable cross-modality safety evaluation of MLLMs. We also conduct a further comparison experiment between textual alignment and multimodal alignment to highlight this drawback. To this end, we construct multimodal Visual Leakless Safety Bench (VLSBench) with 2.2k image-text pairs through an automated data pipeline. Experimental results indicate that VLSBench poses a significant challenge to both open-source and close-source MLLMs, e.g., LLaVA, Qwen2-VL and GPT-4o. Besides, we empirically compare textual and multimodal alignment methods on VLSBench and find that textual alignment is effective enough for multimodal safety scenarios with VSIL, while multimodal alignment is preferable for safety scenarios without VSIL. Code and data are released under https://github.com/AI45Lab/VLSBench

</details>

### 63. UnsafeBench: Benchmarking Image Safety Classifiers on Real-World and AI-Generated Images

📄 [arXiv](https://arxiv.org/abs/2405.03486) · 🌐 [Project](https://doi.org/10.1145/3719027.3765088)　📅 2024-05　🏷 ACM CCS 2025

**关键词**：`benchmark`、`image safety classifier`、`real-world image`、`AI-generated image`

👤 **作者**：Yiting Qu、Xinyue Shen、Yixin Wu、Michael Backes、Savvas Zannettou、Yang Zhang

- 🎯 **研究动机**：图像安全分类器在真实与 AI 生成图像上的表现均未知
- 🔬 **研究方法**：UnsafeBench 含 10K 图像与 11 类不安全类别，评测 5 个流行分类器与 3 个 VLM 分类器，并构建 PerspectiveVision 工具
- 📌 **结论**：现有分类器不够全面有效，真实与生成图像的分布差导致性能退化；PerspectiveVision 显著改进尤其是生成图像

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the advent of text-to-image models and concerns about their misuse, developers are increasingly relying on image safety classifiers to moderate their generated unsafe images. Yet, the performance of current image safety classifiers remains unknown for both real-world and AI-generated images. In this work, we propose UnsafeBench, a benchmarking framework that evaluates the effectiveness and robustness of image safety classifiers, with a particular focus on the impact of AI-generated images on their performance. First, we curate a large dataset of 10K real-world and AI-generated images that are annotated as safe or unsafe based on a set of 11 unsafe categories of images (sexual, violent, hateful, etc.). Then, we evaluate the effectiveness and robustness of five popular image safety classifiers, as well as three classifiers that are powered by general-purpose visual language models. Our assessment indicates that existing image safety classifiers are not comprehensive and effective enough to mitigate the multifaceted problem of unsafe images. Also, there exists a distribution shift between real-world and AI-generated images in image qualities, styles, and layouts, leading to degraded effectiveness and robustness. Motivated by these findings, we build a comprehensive image moderation tool called PerspectiveVision, which improves the effectiveness and robustness of existing classifiers, especially on AI-generated images. UnsafeBench and PerspectiveVision can aid the research community in better understanding the landscape of image safety classification in the era of generative AI.

</details>

### 64. Cognitive Distillation for Information Forensics: Towards Improved Hateful Meme Detection

🌐 [Project](https://doi.org/10.1145/3770855.3817775)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`hateful meme`、`collective cognition`、`information forensics`

- 🎯 **研究动机**：hateful meme检测缺集体认知与取证推理融合
- 🔬 **研究方法**：将多模型集体认知蒸馏进信息取证管线增强检测
- 📌 **结论**：hateful meme检测性能提升

### 65. All Changes May Have Invariant Principles: Improving Ever-Shifting Harmful Meme Detection via Design Concept Reproduction

🎓 [Official](https://aclanthology.org/2026.acl-long.800/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`multimodal guardrail`、`cross-modal risk`、`moderation robustness`、`content moderation`、`harmful content`

👤 **作者**：Ziyou Jiang、…、Qing Wang

- 🎯 **研究动机**：有害 meme 类型漂移、随时间演化，静态检测方法难以跟上
- 🔬 **研究方法**：RepMD 基于攻击树定义 Design Concept Graph 描述有害 meme 设计步骤，从历史 meme 做设计步骤复现与图剪枝得到 DCG，再指导 MLLM 检测
- 📌 **结论**：准确率达 81.1%，在类型漂移与时间演化 meme 上仅轻微下降；人工审核每条提速 15 至 30 秒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Harmful memes are ever-shifting in the Internet communities, which are difficult to analyze due to their type-shifting and temporal-evolving nature. Although these memes are shifting, we find that different memes may share invariant principles, i.e., the underlying design concept of malicious users, which can help us analyze why these memes are harmful. In this paper, we propose RepMD, an ever-shifting harmful meme detection method based on the design concept reproduction. We first refer to the attack tree to define the Design Concept Graph (DCG), which describes steps that people may take to design a harmful meme. Then, we derive the DCG from historical memes with design step reproduction and graph pruning. Finally, we use DCG to guide the Multimodal Large Language Model (MLLM) to detect harmful memes. The evaluation results show that RepMD achieves the highest accuracy with 81.1% and has slight accuracy decreases when generalized to type-shifting and temporal-evolving memes. Human evaluation shows that RepMD can improve the efficiency of human discovery on harmful memes, with 15 ∼ 30 seconds per meme.

</details>

### 66. From Shallow Humor to Metaphor: Towards Label-Free Harmful Meme Detection via LMM Agent Self-Improvement

📄 [arXiv](https://arxiv.org/abs/2512.21598) · 🌐 [Project](https://doi.org/10.1145/3770854.3780213)　📅 2025-12　🏷 KDD 2026

**关键词**：`detection`、`harmful meme`、`label-free learning`、`LMM agent`

👤 **作者**：Jian Lang、Rongpei Hong、Ting Zhong、Leiting Chen、Qiang Gao、Fan Zhou

- 🎯 **研究动机**：有害 meme 检测重度依赖大规模标注，难以适应不断演化的有害内容形态
- 🔬 **研究方法**：ALARM 免标注框架：置信度机制隔离显式 meme 并赋伪标签，把显式样本重组为正负对比对，以成对学习引导 LMM agent 自我改进并自主归纳高层检测线索
- 📌 **结论**：在三个数据集上表现优于有监督方法，对新型演化 meme 适应性强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of harmful memes on online media poses significant risks to public health and stability. Existing detection methods heavily rely on large-scale labeled data for training, which necessitates substantial manual annotation efforts and limits their adaptability to the continually evolving nature of harmful content. To address these challenges, we present ALARM, the first lAbeL-free hARmful Meme detection framework powered by Large Multimodal Model (LMM) agent self-improvement. The core innovation of ALARM lies in exploiting the expressive information from "shallow" memes to iteratively enhance its ability to tackle more complex and subtle ones. ALARM consists of a novel Confidence-based Explicit Meme Identification mechanism that isolates the explicit memes from the original dataset and assigns them pseudo-labels. Besides, a new Pairwise Learning Guided Agent Self-Improvement paradigm is introduced, where the explicit memes are reorganized into contrastive pairs (positive vs. negative) to refine a learner LMM agent. This agent autonomously derives high-level detection cues from these pairs, which in turn empower the agent itself to handle complex and challenging memes effectively. Experiments on three diverse datasets demonstrate the superior performance and strong adaptability of ALARM to newly evolved memes. Notably, our method even outperforms label-driven methods. These results highlight the potential of label-free frameworks as a scalable and promising solution for adapting to novel forms and topics of harmful memes in dynamic online environments.

</details>

### 67. CompAgent: An Agentic Framework for Visual Compliance Verification

📄 [arXiv](https://arxiv.org/abs/2511.00171)　📅 2025-10　🏷 CVPR 2026 Workshop

**关键词**：`defense`、`visual compliance`、`tool routing`、`agentic verification`

👤 **作者**：Rahul Ghosh、…、Chun-Hao Liu

- 🎯 **研究动机**：视觉合规验证缺乏通用方法，MLLM 又难以独自处理细粒度视觉细节并执行结构化规则
- 🔬 **研究方法**：CompAgent 给 MLLM 配备物体检测、人脸分析、NSFW 检测与描述等工具，由规划 agent 按合规策略动态选工具，再由验证 agent 融合图像、工具输出与策略推理
- 📌 **结论**：超越专用分类器与直接 MLLM 提示，UnsafeBench 上 F1 最高 76%、较 SOTA 提升 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visual compliance verification is a critical yet underexplored problem in computer vision, especially in domains such as media, entertainment, and advertising where content must adhere to complex and evolving policy rules. Existing methods often rely on task-specific deep learning models trained on manually labeled datasets, which are costly to build and limited in generalizability. While recent Multimodal Large Language Models (MLLMs) offer broad real-world knowledge and policy understanding, they struggle to reason over fine-grained visual details and apply structured compliance rules effectively on their own. In this paper, we propose CompAgent, the first agentic framework for visual compliance verification. CompAgent augments MLLMs with a suite of visual tools-such as object detectors, face analyzers, NSFW detectors, and captioning models-and introduces a planning agent that dynamically selects appropriate tools based on the compliance policy. A compliance verification agent then integrates image, tool outputs, and policy context to perform multimodal reasoning. Experiments on public benchmarks show that CompAgent outperforms specialized classifiers, direct MLLM prompting, and curated routing baselines, achieving up to 76% F1 score and a 10% improvement over the state-of-the-art on the UnsafeBench dataset. Our results demonstrate the effectiveness of agentic planning and robust tool-augmented reasoning for scalable, accurate, and adaptable visual compliance verification.

</details>

### 68. Dynamic Content Moderation in Livestreams: Combining Supervised Classification with MLLM-Boosted Similarity Matching

📄 [arXiv](https://arxiv.org/abs/2512.03553) · 🌐 [Project](https://doi.org/10.1145/3770854.3783936)　📅 2025-12　🏷 KDD 2026

**关键词**：`defense`、`livestream moderation`、`MLLM matching`、`production deployment`

👤 **作者**：Wei Chee Yew、…、Danhui Guan

- 🎯 **研究动机**：直播审核需及时、多模态并适应不断演化的不良内容，单一分类器难以覆盖新型边缘案例
- 🔬 **研究方法**：生产级混合框架：监督分类器处理已知违规，基于参考的相似度匹配处理新颖或微妙案例，文本、音频、视觉三模态并行，MLLM 向两条流水线蒸馏知识
- 📌 **结论**：分类管线 80% 精度下召回 67%、相似度管线达 76%；大规模 A/B 测试显示不良直播观看量下降 6-8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Content moderation remains a critical yet challenging task for large-scale user-generated video platforms, especially in livestreaming environments where moderation must be timely, multimodal, and robust to evolving forms of unwanted content. We present a hybrid moderation framework deployed at production scale that combines supervised classification for known violations with reference-based similarity matching for novel or subtle cases. This hybrid design enables robust detection of both explicit violations and novel edge cases that evade traditional classifiers. Multimodal inputs (text, audio, visual) are processed through both pipelines, with a multimodal large language model (MLLM) distilling knowledge into each to boost accuracy while keeping inference lightweight. In production, the classification pipeline achieves 67% recall at 80% precision, and the similarity pipeline achieves 76% recall at 80% precision. Large-scale A/B tests show a 6-8% reduction in user views of unwanted livestreams}. These results demonstrate a scalable and adaptable approach to multimodal content governance, capable of addressing both explicit violations and emerging adversarial behaviors.

</details>

### 69. Beyond the Verdict: Evidence-Aligned Evaluation of Visual Prompt-Injection Guardrails

📄 [arXiv](https://arxiv.org/abs/2609.05535)　📅 2026-09

**关键词**：`benchmark`、`prompt injection guardrail`、`evidence alignment`、`web agent`、`counterfactual evaluation`

👤 **作者**：Suyoung Lee、Myungsub Choi

- 🎯 **研究动机**：仅看 verdict 无法判断视觉提示注入 guardrail 是否真用了视觉证据做判断
- 🔬 **研究方法**：Mind2Web-Injection：9,954 对指令-截图、像素级证据框与反事实对照；提出 Evidence-Aligned Detection 指标与 ReadGate/CmdCompare 免训练干预
- 📌 **结论**：平均精度相近的六个 VLM 的 EAD 相差 9 倍；Qwen3-VL-32B 对 endorse 指令仅 58.7% 对齐而 GPT-5.6-luna 99.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Verdict-only evaluation does not reveal whether a vision-language model (VLM) used the visual evidence that should support its decision. We study this problem in web-agent guardrails, where a VLM judges whether on-screen text conflicts with a user instruction. We introduce Mind2Web-Injection, a benchmark of 9,954 instruction-screenshot pairs with instruction-relative labels, pixel-exact evidence boxes, and matched image-side counterfactuals. Across six VLMs, two models with nearly identical average precision differ ninefold in Evidence-Aligned Detection (EAD), the fraction of attacks both detected and correctly localized. To test whether a verdict depends on the command cited as evidence, we replace the instruction with one that endorses that command. Qwen3-VL-32B, the strongest open-weight localizer, returns aligned in only 58.7% of cases, whereas GPT-5.6-luna does so in 99.9%. To diagnose these failures, we propose two training-free interventions. ReadGate improves grounding without changing verdicts, while CmdCompare tests whether explicit instruction-command comparison resolves instruction-side inconsistency. These results motivate reporting verdict correctness, evidence localization, and counterfactual responsiveness separately.

</details>

### 70. Decodable but Misrouted: Sparse Features Uncover a Readout Gap in Vision-Language Models for Harmful Meme Detection

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

### 71. MME-Safety: A Fine-grained Benchmark for Safety Evaluation of MLLMs

📄 [arXiv](https://arxiv.org/abs/2609.20850)　📅 2026-09

**关键词**：`benchmark`、`MLLM safety`、`intent annotation`、`cross-modal stealth`、`CoT safety`

👤 **作者**：Yueming Lyu、…、Caifeng Shan

- 🎯 **研究动机**：MLLM 的跨模态能力引入复杂漏洞，轻易绕过单模态过滤器；既有基准缺细粒度意图相关标注且依赖单维指标，阻碍全面的鲁棒性评估
- 🔬 **研究方法**：MME-Safety：四维标注 schema（风险场景、危害严重度、模态特定隐蔽级别）+ 分层评测框架（基础回复可靠性、实际风险暴露、防御行为结构完整性）；17 个 SOTA MLLM 零样本评测；系统考察跨模态输入配置与 CoT 推理的安全含义
- 📌 **结论**：给出当前多模态系统的安全画像；跨模态配置与 CoT 推理均带安全含义——多模态领域需要推理感知的安全对齐

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Multimodal Large Language Models (MLLMs) show remarkable advancements, their cross-modal capabilities introduce complex vulnerabilities that easily bypass unimodal filters. Existing benchmarks lack fine-grained intent-related annotations and rely on unidimensional metrics, hindering comprehensive robustness evaluation. To address this, we propose MME-Safety, a rigorously verified benchmark featuring a unique four-dimensional annotation schema that categorizes risk scenarios, harm severity, and modality-specific stealth levels. Furthermore, we introduce a hierarchical evaluation framework to assess fundamental response reliability, actual risk exposure, and the structural integrity of defensive behaviors. Extensive zero-shot evaluations across 17 state-of-the-art MLLMs provide a comprehensive safety profile of current multimodal systems. Our analysis systematically investigates cross-modal input configurations and uncovers safety implications associated with Chain-of-Thought (CoT) reasoning. These multifaceted findings underscore the urgent need for robust, reasoning-aware safety alignment in the multimodal landscape.

</details>
