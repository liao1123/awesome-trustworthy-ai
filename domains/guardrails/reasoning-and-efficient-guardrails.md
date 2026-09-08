# Reasoning 与效率权衡

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究 guardrail 是否需要显式 reasoning、reasoning 如何提高复杂意图与边界案例的判断，以及怎样把这些能力压缩成可部署的低延迟模型。主要路线包括生成 CoT 或 reflection、训练期 reasoning 与推理期 label-only、连续 latent reasoning、encoder classifier、大小模型 routing，以及对解释忠实性、吞吐、false-positive rate 和 hard-case 能力的受控比较。

## 研究脉络

- **生成式判断：** GuardReasoner、ThinkGuard 等工作让 guard 在输出 label 前生成 policy-grounded reasoning 或反思轨迹；CARO 进一步以动态类比参照处理歧义内容和 decision shortcut。
- **Reasoning 的作用检验：** 后续实证研究区分“推理真正改变 verdict”和“对既定判断的事后解释”，开始质疑通用 benchmark 是否足以证明 CoT 必要。
- **推理内化：** DT-Guard 将 reasoning 只用于训练，CoLaGuard、LPG 与 LatentGuard 则在连续 latent state 中传播推理，并把按需 audit decoder 与正常判定路径分离。
- **轻量分类与路由：** SafeRoute 把困难样本交给大 guard，GLiGuard 与 LeanGuard 直接使用 bidirectional encoder，Tripwire 则让 detector 只在风险请求上触发神经元级拒答；结果显示架构、数据、门控和阈值校准可能比显式 CoT 更影响当前任务。
- **多模态实时审核：** ResponseGuard 把图像、请求和响应池化后一次前向判断，进一步将效率问题推进到 sentence-level streaming 场景。

## 显式 Reasoning 与反思

### 1. TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.24232)　📅 2026-08

**关键词**：`benchmark`、`reasoning-trace safety`、`evidence localization`、`full-pipeline moderation`、`CoT monitoring`、`evidence grounding`

👤 **作者**：Zhenyu Wu、…、Xin Gao

- 🎯 **研究动机**：unsafe 内容 benchmark 只覆盖 prompt 与最终回答，忽略推理模型中间 reasoning trace 且无证据标注
- 🔬 **研究方法**：TRACE 标注 prompt、reasoning trace 与 final response 三段安全性并提取源文本证据，覆盖双语九类风险十种攻击
- 📌 **结论**：18 个 guardrail 模型对推理轨迹的安全判定显著更难，且难以准确提取支撑证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) generate intermediate reasoning traces that may contain unsafe content, even when their final responses appear safe. Guardrail models are designed to detect and block unsafe content, yet existing benchmarks for unsafe content detection focus primarily on prompts and final responses, leaving reasoning traces largely unexamined. Moreover, these benchmarks typically provide only binary safety labels, without evidence annotations that justify the judgments. To address these limitations, we introduce TRACE, an evidence-grounded safety evaluation benchmark that covers the entire LRM inference pipeline: prompts, reasoning traces, and final responses. TRACE includes prompts in two languages spanning nine risk categories and ten attack strategies. For each prompt, four LRMs generate reasoning traces and final responses, and we annotate the safety of each component and extract supporting evidence from the corresponding source text. Evaluating 18 guardrail models on TRACE reveals that safety judgment for reasoning traces is substantially more challenging than for prompts or final responses, and that current models struggle to accurately extract supporting evidence. These findings highlight the need for guardrail models that can reliably detect and precisely localize unsafe content across the LRM inference pipeline.

</details>

### 2. SPAR-Hate: Auditor-Guided Multi-Perspective Role Reasoning for Bilingual Hate Speech Parsing

📄 [arXiv](https://arxiv.org/abs/2608.22018)　📅 2026-08　🏷 EMNLP 2026

**关键词**：`detection`、`defense`、`bilingual moderation`、`evidence arbitration`、`structured hate parsing`、`multi-perspective reasoning`

👤 **作者**：Yifan Lyu、Dianqing Lin、Xinran Li、Jiaqi Qiao、Xiujuan Xu

- 🎯 **研究动机**：仇恨言论研究从粗粒度分类转向结构化解析（联合识别 target、论据与标签），但多 target、局部解读冲突与文化编码语言使绑定难以恢复
- 🔬 **研究方法**：SPAR-Hate 审计引导多视角框架：把文档拆为局部焦点单元，从 Victim、Moderator、Cultural Bystander 三视角生成有证据候选，在 grounding 与 schema 约束下仲裁冲突并重组预测
- 📌 **结论**：STATE-ToxiCN 与受控 TBO split 上在严格联合 target-argument-label 指标取得提升；结构化 teacher trace 还可训练更小 student 模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hate speech research has moved from coarse-grained classification towards structured parsing, where systems jointly identify targets, supporting arguments, and target-level labels. Documents with multiple targets, conflicting local readings, or culturally coded language make these bindings difficult to recover. SPAR-Hate is an auditor-guided multi-perspective role-reasoning framework for bilingual hate speech parsing. It decomposes each document into local focus units, elicits evidence-grounded candidates from Victim, Moderator, and Cultural Bystander perspectives, resolves candidate conflicts under grounding and schema constraints, and reassembles sample-level predictions. Experiments on STATE-ToxiCN and a controlled TBO split show gains across local and API backbones, concentrated on strict joint target-argument-label metrics. Full-test integrated-prompt controls, component ablations, and bounded-arbitration diagnostics identify the contribution of separated perspective generation and arbitration. Structured teacher traces also support training a smaller student model.

</details>

### 3. A Dual-Hypothesis Reasoning Framework for LLM Guardrails

📄 [arXiv](https://arxiv.org/abs/2607.17575)　📅 2026-07

**关键词**：`defense`、`dual-hypothesis reasoning`、`evidence phrase`、`MC-SFT`

👤 **作者**：Md Asiful Islam、Mihai Surdeanu

- 🎯 **研究动机**：已有推理式护栏依赖昂贵的大模型或闭源教师生成推理轨迹并全参微调
- 🔬 **研究方法**：提出 ARBITER：双假设推理在判定前显式考虑提示的安全与不安全两种解读，MC-SFT 把输出分解为逻辑组件按重要性加权；自生成轨迹+LoRA 高效微调并给出证据短语解释
- 📌 **结论**：三个审核基准上超越推理式与非推理式基线，域外评估增益明显

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose ARBITER, a novel LLM guardrail framework that introduces two key ideas: (i) dual-hypothesis reasoning, a reasoning method for LLM guardrails that explicitly considers both safe and unsafe interpretations of a prompt before making a safety decision, and (ii) multi-component supervised fine-tuning (MC-SFT), a structured training loss for reasoning-based guardrails that decomposes LLM outputs into logical components and weights them according to their importance. Existing reasoning-based guardrails often rely on expensive procedures, such as generating reasoning traces using larger or closed-source teacher models and applying full-parameter fine-tuning. In contrast, ARBITER uses a cost-effective self-generation strategy for reasoning traces and LoRA-based parameter-efficient fine-tuning while still achieving better performance than these expensive approaches. Additionally, ARBITER provides faithful evidence-phrase explanations for unsafe decisions, enabling a more transparent and interpretable guardrail method. Experiments on three safety moderation benchmarks show that ARBITER outperforms existing reasoning-based and non-reasoning guardrail baselines, with clear gains in out-of-domain evaluations.

</details>

### 4. Reflect-Guard: Enhancing LLM Safeguards against Adversarial Prompts via Logical Self-Reflection

📄 [arXiv](https://arxiv.org/abs/2605.24834)　📅 2026-05

**关键词**：`defense`、`self-reflection`、`adversarial prompt`、`trajectory distillation`

👤 **作者**：Lixing Lin、…、Moxuan Zheng

- 🎯 **研究动机**：Llama Guard 类分类器可检显式有害 prompt，但被角色扮演、虚构框架与间接请求伪装绕过
- 🔬 **研究方法**：Reflect-Guard 从 GPT-4o-mini 蒸馏结构化反思标注，QLoRA 微调 Llama-Guard-3-8B 使其在判决前生成逻辑自反思
- 📌 **结论**：仅 1000 样本、更新 0.5% 参数，WildGuardTest F1 从 0.770 升至 0.842（对抗 prompt recall 提升 40.8 个百分点），JailbreakBench ASR 从 10.3% 降至 1.8%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) safety classifiers such as Llama Guard are effective at detecting overtly harmful prompts but remain vulnerable to adversarial jailbreak attacks that disguise malicious intent through role-play scenarios, fictional framing, and indirect requests. We present Reflect-Guard, a method that augments LLM-based safety classifiers with chain-of-thought self-reflection capabilities through parameter-efficient fine-tuning. Our approach distills analytical reasoning from GPT-4o-mini into structured reflection annotations, then trains Llama-Guard-3-8B via QLoRA to generate logical self-reflections before issuing safety verdicts. Using only 1000 training examples and updating just 0.5% of model parameters (~42M), Reflect-Guard achieves substantial improvements on two challenging benchmarks. On WildGuardTest, F1 score improves from 0.770 to 0.842 (+7.2 pp), with recall on adversarial prompts increasing from 0.513 to 0.921 (+40.8 pp). On JailbreakBench, the attack success rate drops from 10.3% to 1.8%, representing an 82.5% relative reduction. These gains are especially pronounced on adversarial inputs, where the explicit reasoning step enables the model to see through obfuscation techniques that defeat standard pattern-matching approaches. Our results demonstrate that teaching safety classifiers to reason about adversarial intent, rather than simply classify surface patterns, is a promising direction for robust LLM safety.

</details>

### 5. CARO: Chain-of-Analogy Reasoning Optimization for Robust Content Moderation

📄 [arXiv](https://arxiv.org/abs/2604.10504) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.1442/)　📅 2026-04　🏷 ACL 2026

**关键词**：`defense`、`analogical reasoning`、`decision shortcut`、`moderation robustness`

👤 **作者**：Bingzhe Wu、Haotian Lu、Yuchen Mou

- 🎯 **研究动机**：即使推理型 LLM 也会被上下文中误导性 decision shortcut 带偏，难以处理歧义内容审核
- 🔬 **研究方法**：CARO 两阶段训练：RAG 自举类比推理链做 SFT，再用定制 DPO 显式强化类比推理；推理时动态生成类比参照
- 📌 **结论**：超过 DeepSeek R1、QwQ 与 Llama Guard 等，困难歧义审核基准平均 F1 提升 24.9%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current large language models (LLMs), even those explicitly trained for reasoning, often struggle with ambiguous content moderation cases due to misleading "decision shortcuts" embedded in context. Inspired by cognitive psychology insights into expert moderation, we introduce \caro (Chain-of-Analogy Reasoning Optimization), a novel two-stage training framework to induce robust analogical reasoning in LLMs. First, \caro bootstraps analogical reasoning chains via retrieval-augmented generation (RAG) on moderation data and performs supervised fine-tuning (SFT). Second, we propose a customized direct preference optimization (DPO) approach to reinforce analogical reasoning behaviors explicitly. Unlike static retrieval methods, \caro dynamically generates tailored analogical references during inference, effectively mitigating harmful decision shortcuts. Extensive experiments demonstrate that \caro substantially outperforms state-of-the-art reasoning models (DeepSeek R1, QwQ), specialized moderation models (LLaMA Guard), and advanced fine-tuning and retrieval-augmented methods, achieving an average F1 score improvement of 24.9\% on challenging ambiguous moderation benchmarks.

</details>

### 6. Beyond Content Safety: Real-Time Monitoring for Reasoning Vulnerabilities in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.25412)　📅 2026-03

**关键词**：`detection`、`reasoning safety`、`step-level monitor`、`runtime interruption`、`reasoning-step stream`、`parallel verifier`

👤 **作者**：Xunguang Wang、…、Shuai Wang

- 🎯 **研究动机**：推理过程本身的安全性（逻辑一致、高效、抗操纵）被当作黑箱中间产物，内容安全之外的正交维度未被处理
- 🔬 **研究方法**：形式化推理安全并建立九类不安全推理行为分类法，标注超 4,000 条推理链；外部零 shot 监控器并行逐步检查并实时发出中断信号
- 📌 **结论**：步骤级定位准确率最高 87.11%，大幅超幻觉检测器与最佳过程奖励模型，低误报、延迟可忽略且抗自适应规避

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models increasingly rely on explicit chain-of-thought reasoning to solve complex tasks, yet the safety of the reasoning process itself remains largely unaddressed. Existing work focuses predominantly on content safety (i.e., detecting harmful, biased, or factually incorrect outputs), while treating the underlying reasoning chain as an opaque intermediate artifact. We argue that reasoning safety constitutes a fundamental security dimension orthogonal to content safety: the requirement that a model's reasoning trajectory be logically consistent, computationally efficient, and resistant to adversarial manipulation. In this paper, we formalize reasoning safety and introduce a systematic taxonomy of nine unsafe reasoning behaviors. We then conduct a large-scale prevalence study, annotating over 4,000 reasoning chains across benign benchmarks and four state-of-the-art reasoning attacks, empirically demonstrating that all nine error types occur in practice with mechanistically interpretable signatures. To mitigate these threats, we propose the Reasoning Safety Monitor: an external, zero-shot verification framework that runs in parallel with the target LLM. It inspects each reasoning step in real time via a taxonomy-embedded prompt and dispatches an interrupt signal upon detecting unsafe behavior. Extensive evaluations show our monitor achieves up to 87.11% step-level localization accuracy, outperforming hallucination detectors and the best process reward model baselines by a substantial margin. Crucially, the monitor maintains a low false positive rate on correct reasoning paths, operates with negligible latency overhead, and exhibits robust resilience against adaptive adversarial evasion. These findings establish reasoning safety monitoring as a highly feasible and essential component for the secure deployment of large reasoning models.

</details>

### 7. Towards Trustworthy Multimodal Moderation via Policy-Aligned Reasoning and Hierarchical Labeling

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

### 8. ThinkGuard: Deliberative Slow Thinking Leads to Cautious Guardrails

📄 [arXiv](https://arxiv.org/abs/2502.13458) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.704/)　📅 2025-02　🏷 ACL 2025

**关键词**：`defense`、`slow thinking`、`deliberative reasoning`、`jailbreak detection`

👤 **作者**：Xiaofei Wen、Wenxuan Zhou、Wenjie Jacky Mo、Muhao Chen

- 🎯 **研究动机**：规则过滤或单遍分类的 guardrail 难以处理细微安全违规
- 🔬 **研究方法**：ThinkGuard 从高能力 LLM 蒸馏结构化 critique 与安全标签，经 critique 增强数据微调获得审议式思考
- 📌 **结论**：多基准取得最高平均 F1 与 AUPRC；较 LLaMA Guard 3 准确率提升 16.1%、macro F1 提升 27.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the safety of large language models (LLMs) is critical as they are deployed in real-world applications. Existing guardrails rely on rule-based filtering or single-pass classification, limiting their ability to handle nuanced safety violations. To address this, we propose ThinkGuard, a critique-augmented guardrail model that distills knowledge from high-capacity LLMs by generating structured critiques alongside safety labels. Fine-tuned on critique-augmented data, the captured deliberative thinking ability drastically enhances the guardrail's cautiousness and interpretability. Evaluated on multiple safety benchmarks, ThinkGuard achieves the highest average F1 and AUPRC, outperforming all baselines. Compared to LLaMA Guard 3, ThinkGuard improves accuracy by 16.1% and macro F1 by 27.0%. Moreover, it surpasses label-only fine-tuned models, confirming that structured critiques enhance both classification precision and nuanced safety reasoning while maintaining computational efficiency.

</details>

### 9. GuardReasoner: Towards Reasoning-based LLM Safeguards

📄 [arXiv](https://arxiv.org/abs/2501.18492)　📅 2025-01　🏷 ICLR 2025

**关键词**：`defense`、`reasoning guard`、`reasoning SFT`、`safety reward`

👤 **作者**：Yue Liu、…、Bryan Hooi

- 🎯 **研究动机**：传统 guard 只输出标签，难处理复杂意图且不可解释
- 🔬 **研究方法**：构建 127K 样本、460K 推理步的 GuardReasonerTrain，先 reasoning SFT 再 hard sample DPO
- 📌 **结论**：13 个基准 3 类任务上领先，8B 版超 GPT-4o+CoT 5.74%、超 LLaMA Guard 3 8B 达 20.84% F1

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs increasingly impact safety-critical applications, ensuring their safety using guardrails remains a key challenge. This paper proposes GuardReasoner, a new safeguard for LLMs, by guiding the guard model to learn to reason. Concretely, we first create the GuardReasonerTrain dataset, which consists of 127K samples with 460K detailed reasoning steps. Then, we introduce reasoning SFT to unlock the reasoning capability of guard models. In addition, we present hard sample DPO to further strengthen their reasoning ability. In this manner, GuardReasoner achieves better performance, explainability, and generalizability. Extensive experiments and analyses on 13 benchmarks of 3 guardrail tasks demonstrate its superiority. Remarkably, GuardReasoner 8B surpasses GPT-4o+CoT by 5.74% and LLaMA Guard 3 8B by 20.84% F1 score on average. We release the training data, code, and models with different scales (1B, 3B, 8B) of GuardReasoner : https://github.com/yueliu1999/GuardReasoner/.

</details>

### 10. Safety Through Reasoning: An Empirical Study of Reasoning Guardrail Models

🎓 [Official](https://aclanthology.org/2025.findings-emnlp.1193/)　📅 2025　🏷 EMNLP 2025

**关键词**：`analysis`、`reasoning guard`、`verdict faithfulness`、`empirical study`

👤 **作者**：Makesh Narsimhan Sreedhar、Traian Rebedea、Christopher Parisien

- 🎯 **研究动机**：推理能力对内容审核护栏的收益缺乏系统实证研究，尤其是推理时对自定义安全策略的泛化
- 🔬 **研究方法**：从数据效率与推理效率两个维度系统分析训练推理式护栏模型，引入推理预算考察推理长度对延迟与准确率的影响，并探索双模式训练
- 📌 **结论**：推理式护栏样本效率高，用更少样本即可有竞争力，剩余数据可挖掘困难样本进一步提升；推理预算与双模式训练提供运行时控制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning-based language models have demonstrated strong performance across various domains, with the most notable gains seen in mathematical and coding tasks. Recent research has shown that reasoning also offers significant benefits for LLM safety and guardrail applications. In this work, we conduct a comprehensive analysis of training reasoning-based guardrail models for content moderation, with an emphasis on generalization to custom safety policies at inference time. Our study focuses on two key dimensions: data efficiency and inference efficiency. On the data front, we find that reasoning-based models exhibit strong sample efficiency, achieving competitive performance with significantly fewer training examples than their non-reasoning counterparts. This unlocks the potential to repurpose the remaining data for mining high-value, difficult samples that further enhance model performance. On the inference side, we evaluate practical trade-offs by introducing reasoning budgets, examining the impact of reasoning length on latency and accuracy, and exploring dual-mode training to allow runtime control over reasoning behavior. Our findings will provide practical insights for researchers and developers to effectively and efficiently train and deploy reasoning-based guardrails models in real-world systems.

</details>

### 11. LatentGuard: Efficient and Inspectable Latent Reasoning for LLM Safeguards

📄 [arXiv](https://arxiv.org/abs/2608.03838)　📅 2026-08

**关键词**：`defense`、`latent reasoning`、`on-demand audit`、`critical-path efficiency`

👤 **作者**：Zhinan Liu、Jie Li、Mingyu Kang、Jiayi Ji

- 🎯 **研究动机**：推理型 guard 为每次交互解码显式 rationale 成本高，潜空间推理方法缺少面向安全审查的接口
- 🔬 **研究方法**：LatentGuard 用阶段性课程把任务对齐的文本 rationale 压缩为紧凑潜状态直接预测安全判定，隔离的辅助解码器按需生成审计产物
- 📌 **结论**：8B 版加权 F1 从 83.95 升至 84.91（GuardReasoner-8B），关键路径推理从 268.56 token 降至 1.60 token，审计得分 85.75

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning-based guard models improve LLM safeguards, but decoding explicit rationales for every interaction makes them costly to deploy. Although latent-reasoning methods reduce token generation by moving reasoning into continuous states, they remain underexplored for safety moderation and lack an inspection interface for deployment. In this paper, we propose LatentGuard, an efficient and inspectable safeguard framework that brings continuous latent reasoning to guard models. LatentGuard uses a staged curriculum to progressively compress task-aligned textual rationales into compact latent states, enabling safety verdicts to be predicted directly from continuous representations. To preserve inspectability, an isolated auxiliary decoder generates compact audit artifacts on demand, keeping rationale generation off the standard inference path. Experiments show that LatentGuard-8B improves mean weighted F1 from 83.95 to 84.91 over GuardReasoner-8B, while reducing critical-path reasoning cost from 268.56 generated rationale tokens to 1.60 latent reasoning tokens. Its audit decoder achieves an audit utility score of 85.75, demonstrating an efficient and inspectable path toward deployable LLM safeguards.

</details>

### 12. Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

📄 [arXiv](https://arxiv.org/abs/2608.28099)　📅 2026-08

**关键词**：`tool`、`detection`、`context-aware probe`、`speculative decoding`、`runtime safety classifier`、`speculative classifier`

👤 **作者**：Collin Zhang、Tingwei Zhang、Vitaly Shmatikov

- 🎯 **研究动机**：hidden-state probe 只作用于单向量、缺上下文交互，专用 guard 模型或全 token 计算又成本过高，在线安全监控面临精度—效率权衡
- 🔬 **研究方法**：提出在目标序列末尾附加训练好的 soft prompt，把 LLM 自带的 speculative-decoding 模块改造成序列分类器，推理时直接复用 GPU 内已有的 KV cache
- 📌 **结论**：小 probe 在四类任务、四个模型（Qwen3.5-4B/9B/27B、MiniCPM4.1-8B）上稳定优于零样本 GPT-5.4-mini，多语言 prompt safety 上达到或超过 8B 专用 safety classifier，额外开销可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-time classification during language model inference is valuable for safety filtering, behavioral analysis, and model monitoring, but current approaches force a trade-off between accuracy and efficiency. Hidden-state probes are fast but limited: they are either not context-aware: operating on a single vector and cannot model interactions across positions; or they are very costly: having dedicated classifier models (Llama Guard, Qwen Guard, LLM-as-judge) or performing computation on hidden states for all tokens and then pooling the results (MultiMax). This shows an intrinsic trade-off between efficiency and accuracy. However, we find that the speculative-decoding module in recent LLMs can be repurposed for efficient high-quality classification. By appending a trained soft prompt at the end of the target sequence, we can repurpose the speculative-decoding module into a sequence classifier. At inference time in a speculative-decoding pipeline, the KV cache is already in GPU memory, so classification adds negligible overhead. We evaluate on four classification tasks across four models (Qwen3.5-4B, 9B, 27B, MiniCPM4.1-8B). Our small probes consistently outperform zero-shot GPT-5.4-mini and, on multilingual prompt safety, match or beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM.

</details>

### 13. LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails

📄 [arXiv](https://arxiv.org/abs/2608.27580)　📅 2026-08

**关键词**：`analysis`、`defense`、`long-context guardrail`、`attention dilution`、`training-free mitigation`、`chunked detection`

👤 **作者**：Ziyang Chen、Xing Wu、Songlin Hu

- 🎯 **研究动机**：安全 guardrail 几乎只在短文本上训练与评估，长上下文中对不安全内容的召回大幅下降，机制与缓解均缺失
- 🔬 **研究方法**：提出 SafetyNIAH（0.25k–32k 长度网格）与 LongGuard：用 Benign-Fill vs Needle-Repeat 对照与三层 attention–logit–behavior 分析把失效归因于 unsafe needle 注意力稀释，并给出无需训练的 Chunked Detection、Attention-Head Sharpening 与长度感知路由
- 📌 **结论**：15 个主流 guardrail 的不安全召回随长度平均单调下降逾 50%；Chunked Detection 与 Attention-Head Sharpening 在六个 guardrail 上平均改善 22% 与 13%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety guardrails serve as the last line of defense against harmful inputs and outputs of large language models (LLMs), yet they are trained and evaluated almost exclusively on short text. We present LongGuard, a framework that evaluates, mechanistically analyzes, and mitigates long-context guardrail failure. We formulate the task as Safety Needle-in-a-Haystack (SafetyNIAH) over a 0.25k-32k length grid; across 15 mainstream guardrails, unsafe recall drops monotonically by more than 50% on average, and a paired Benign-Fill vs. Needle-Repeat design attributes the failure to proportional dilution of the unsafe needle rather than to absolute length. A three-layer attention-logit-behavior analysis on six guardrails locates the mechanism: attention mass on the unsafe needle is diluted, the unsafe-over-safe logit margin is compressed in lockstep, and the detection decision collapses accordingly, with this attention->logit->behavior chain remaining consistent after partialling out length. We further isolate a sparse set of guard-specialized retrieval heads that exhibit partial specificity relative to their base models. Building on the analysis, we propose two training-free mitigations - Chunked Detection (CD) and Attention-Head Sharpening (AHS) - and a deployment protocol, Context-Aware Hyperparameter Routing (CAHR), that selects configurations by context length and audit side. Across five benchmarks spanning synthetic data, long-context attacks, and reasoning-model outputs, CAHR-CD and CAHR-AHS improve the six-guardrail average by 22% and 13%, respectively. Code and data are available online.

</details>

### 14. Nemotron 3.5 Content Safety Moderator: A Compact Multimodal, Multilingual, and Reasoning Enabled Content Safety Moderator

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

### 15. Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

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

### 16. Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons

📄 [arXiv](https://arxiv.org/abs/2608.14392) · 🌐 [Project](https://anonymous.4open.science/r/Tripwire-65C4)　📅 2026-08

**关键词**：`defense`、`analysis`、`detector-gated intervention`、`safety neuron`、`utility preservation`、`jailbreak`

👤 **作者**：Wei Zhao、Zhe Li、Peixin Zhang、Jun Sun

- 🎯 **研究动机**：神经元级越狱防御或干预面大损效用、或误伤效用神经元，且常开干预扰动每个良性请求
- 🔬 **研究方法**：Tripwire 免训练：FDR 控制下逐神经元假设检验加效用特异性过滤识别安全神经元，触发式 clamp 钉住激活于有害条件均值以诱发对齐学到的拒答；支持检测门控推理与离线 bias-patch 两种等价部署
- 📌 **结论**：四个对齐 LLM、四种攻击下平均 ASR 降至至多 2.0%，MT-Bench 效用损失仅 0.5-5.3%，为所有防御中最小

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify safety neurons using external classifiers. While promising, the existing approaches suffer from compromising neurons that are important for the model utility as well. Moreover, both approaches remain always on and thus perturb every benign request even when no attack is present. To address these limitations, we present \ours{}, a training-free defense that first identifies safety-specific neurons through per-neuron hypothesis tests under false-discovery-rate control together with a utility-specificity filter. Based on this identification, a trigger-style clamp holds the selected neurons at their harmful-conditional mean activations, injecting an internal harmful-input signal that triggers the refusal behavior learned during alignment. The clamp is then realized by two provably equivalent deployment modes, namely a detector-gated inference-time intervention and an offline bias-patch weight edit. Extensive experiments across four safety-aligned LLMs and four representative attacks demonstrate that \ours{} reduces the average attack success rate to at most 2.0\% while incurring a utility drop of only 0.5\% to 5.3\% on MT-Bench, the smallest among all defenses. Code is available at https://anonymous.4open.science/r/Tripwire-65C4.

</details>

### 17. A Reproducible, License-Aware Distillation Recipe for CPUDeployable Safety Classification

📄 [arXiv](https://arxiv.org/abs/2608.21570)　📅 2026-08

**关键词**：`tool`、`defense`、`distilled guard model`、`CPU deployment`、`license-aware data`、`lightweight guard`

👤 **作者**：Edson Rodrigues da Cruz Filho、…、Gustavo Voltani Von Atzingen

- 🎯 **研究动机**：开源 guard 模型普遍 1–9B 参数、面向 GPU，在 CPU 上每请求需数秒，难以在普通硬件上部署安全层
- 🔬 **研究方法**：可复现、许可证感知的蒸馏配方：强开源 guard 为约 97,000 条 prompt（来自 24 个公开数据集、七类安全类别）打标，训练词法、浅层、encoder 与生成式小 student，语料按许可证边界划分并用独立 6,361 行 gold benchmark 评估
- 📌 **结论**：蒸馏 student 在对抗文本上与 teacher 置信区间重叠，最小生成式 student 无害误报 3.8% 优于 8B teacher 的 4.8%，encoder 在 CPU 上约 24ms/请求；per-class rebalancing 是唯一决定性成分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying a safety layer for large language models on commodity hardware is constrained by the guards available to do it: current open guard models hold between 1 and 9 billion parameters, are oriented toward the graphics processing unit, and answer in seconds per request on a central processing unit. This paper presents a reproducible, license-aware knowledge-distillation recipe addressing that constraint. A strong open guard labels a corpus of roughly 97,000 prompts, drawn from 24 public datasets, into seven safety categories aligned to a public hazard taxonomy, and a fleet of small students spanning lexical, shallow, encoder and generative architectures is trained to reproduce that signal. The corpus is partitioned at the license boundary, so that a deployable and a research model differ only in their training data and the cost of that restriction becomes measurable. Every model is scored against an independent gold benchmark of 6,361 rows over four slices, labeled apart from the teacher and including a slice of harmless prompts that makes over-defense measurable. The distilled students match the teachers on adversarial text within overlapping confidence intervals and reduce false alarms on harmless prompts, the smallest generative student reaching 3.8% against 4.8% for the 8-billion-parameter teacher, while the encoder classifies in roughly 24 ms per request on CPU. Per-class rebalancing is the only decisive ingredient of the recipe. No superiority over the distilled guards is claimed; on the clean reference slice they remain ahead.

</details>

### 18. BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.21880)　📅 2026-08

**关键词**：`defense`、`benchmark`、`cross-script prompt guard`、`lightweight classifier`、`over-refusal`、`lightweight prompt guard`

👤 **作者**：Md. Rakibul Hassan、Muhammad Iqbal Hossain

- 🎯 **研究动机**：孟加拉语用户混用罗马化、Banglish、code-mixed、噪声与方言形式书写，英语中心或标准文字的 benchmark 无法评估孟加拉语 LLM 安全，跨文字可绕过防御
- 🔬 **研究方法**：BanglaVeilGuard 覆盖六种语言形态的 2,366 条 prompt（另 354 条 held-out），用非破坏性多视图规范化加 prompt 风险分类器与阈值预生成 gate，不改目标模型权重
- 📌 **结论**：Claude Opus 4.8、BanglaLLama、TituLLM 的 ASR 从 93.8–100% 降至 6.3%，unsafe recall 88.5% 超各 guard 基线；残余代价是方言与噪声良性 prompt 的过度拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-filtered prompts and a held-out 354-prompt evaluation split spanning unsafe, safe, and safe-sensitive requests. BanglaVeilGuard uses non-destructive multi-view normalization with a prompt-risk classifier and thresholded pre-generation gate, allowing it to screen prompts for heterogeneous target models without changing their weights. Across target-model families, guarded runs reduce attack success under deterministic response scoring from 93.8--100.0\% to 6.3\% for Claude Opus 4.8, BanglaLLama, and TituLLM; TigerLLM-1B with BanglaVeilGuard achieves 78.2\% accuracy with 8.8\% ASR. The prompt guard also attains 88.5\% unsafe recall, substantially above the evaluated prompt-only guard baselines. The main remaining cost is over-refusal on dialectal and noisy benign prompts, revealing a concrete safety-helpfulness frontier for Bangla LLM deployment.

</details>

### 19. Reflex-Guard: A Low-Latency Guardrail for LLM Prompt Safety Using Dense Semantic Embeddings

📄 [arXiv](https://arxiv.org/abs/2608.17556)　📅 2026-08

**关键词**：`defense`、`prompt safety`、`dense embedding`、`low-latency guard`

👤 **作者**：Istiaque Ahmed、Afia Anjum Borsha、Ranat Das Prangon、Abu-fuad Ahmad、Thi Hong Tran

- 🎯 **研究动机**：LLM-judge 与云端安全 API 每 prompt 增加 250-900ms 延迟，实时应用需 100ms 内响应，外发审核还有隐私顾虑
- 🔬 **研究方法**：Reflex-Guard 本地轻量 guardrail：越狱感知预处理、紧凑句向量嵌入与七个快速二分类器，30,568 样本平衡数据集评测
- 📌 **结论**：有害 prompt 上 95.9% recall、端到端延迟 37.6ms（Llama Guard 2 为 255ms）；默认阈值下 100% 检出 GCG 后缀与 Base64 编码 prompt

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) in real-world applications often face the risks of specially crafted prompts designed to bypass the safety controls. Existing guardrail methods, such as LLM-as-a-judge and cloud-based safety APIs are able to detect unsafe content. However, they often add a delay of about 250-900 ms to each request. This delay is too high for real-time applications, when the system usually needs to respond in less than 100 ms. Furthermore, routing user prompts through external moderation endpoints raises significant data privacy concerns. This paper introduces Reflex-Guard, a lightweight guardrail that runs locally. It uses jailbreak-aware preprocessing, compact sentence-transformer embeddings, and seven fast binary classifiers. Together, these components enable high-accuracy prompt safety filtering with much lower latency than existing solutions. Through systematic evaluation on a strategically balanced dataset of 30,568 samples drawn from five complementary sources, we demonstrate that Reflex-Guard achieves 95.9% recall on harmful prompts at 37.6 ms end-to-end latency. It is faster than existing baselines, including Llama Guard 2 at 255 ms and SafeDecoding at 723 ms. It can detect 100% of GCG suffix attacks and Base64-encoded prompts using the default threshold. However, DrAttack structured prompts required lowering the threshold to 0.03 for optimal detection, as they produced a distinct probability distribution. Reflex-Guard achieves Reflex Efficiency Score (RES) scores up to 16.79, significantly outperforming Llama Guard 2 (11.90) and SafeDecoding (9.80). This analysis offers practical deployment advice and shows that different attack types occupy distinct regions in the embedding probability space.

</details>

### 20. When Are Reasoning-Based Guardrails Not Efficient? ResponseGuard: A Fast Vision-Language Guard for Real-Time Moderation

📄 [arXiv](https://arxiv.org/abs/2607.21401)　📅 2026-07

**关键词**：`defense`、`vision-language guard`、`single-pass classifier`、`streaming latency`

👤 **作者**：Dongbin Na

- 🎯 **研究动机**：视觉语言护栏先生成思维链再判定，解码大量 token 使护栏笨重缓慢，难以跟上流式回答
- 🔬 **研究方法**：提出 ResponseGuard：单前向对请求、回答与图像的池化表示直接读出有害判定，无任何推理链
- 📌 **结论**：2B 模型在回答有害性检测上超过 3B 推理式护栏且时间成本低约 150 倍；差距集中在图像单元且可能源于冻结视觉编码器；单次检测可随流逐句筛查并在完成前中止有害回答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A vision-language AI assistant returns its answer as a stream of generated tokens. Therefore, a safety guard that watches that answer has to keep up with the stream and stop a harmful reply before a user reads it. Recent vision-language guardrails instead generate a chain of thought before they issue a verdict. They believe that step-by-step reasoning yields a safer guard. This design makes the guard heavy and slow, since the model must decode many tokens for harmfulness detection. We pose the question of whether a vision-language guard really needs to reason in order to screen a response. We answer with a guard that has no chain. ResponseGuard reads a harmful verdict from a single pooled representation of the request, the response, and the image in one forward pass. Across a standard multimodal guardrail benchmark, our 2B ResponseGuard outperforms a recent 3B reasoning-based vision-language guard on response harmfulness detection, without any reasoning and at about 150 times lower time cost. On request harmfulness the reasoning guard retains an overall lead, and the remaining gap on both tracks sits on the image-only cells. We observe that the gap may stem from the frozen vision encoders that both designs use rather than from the missing chain. We have also found the reasoning guard directs almost none of its verdict attention to the image. Based on a single-pass detection, ResponseGuard can screen an answer sentence by sentence as it streams and stop a harmful answer before it finishes. For guarding the response of a vision-language model, a calibrated single-pass label may provide a sufficient safety signal. We fully release all source code, trained models, and datasets at https://github.com/ndb796/ResponseGuard.

</details>

### 21. DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail

📄 [arXiv](https://arxiv.org/abs/2607.06326)　📅 2026-07

**关键词**：`defense`、`reasoning-active training`、`intent modeling`、`label-only inference`

👤 **作者**：He Liu、…、Zhe Li

- 🎯 **研究动机**：护栏面临轻量分类器难处理隐藏意图与推理护栏延迟高的权衡
- 🔬 **研究方法**：提出 DT-Guard：训练时推理监督、推理时只输出结构化标签的范式，把安全判断形式化为 Intent-Category-Safety 渐进决策过程，并用 RG-PHO 多 rollout 一致性识别难例做定向优化
- 📌 **结论**：提示侧与响应侧平均 F1 分别 0.886 与 0.870；4B backbone 双侧平均 F1 0.878，超过强 8B 护栏基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models deployed in open-world applications require safety guardrails that are both robust to complex risks and efficient enough for low-latency runtime moderation. Existing guardrails face a practical trade-off between lightweight classification-based models, which are efficient but often struggle with concealed intent, ambiguous semantics, and borderline safety decisions, and reasoning-based guards, which improve judgment quality but introduce additional token generation and inference latency. We present DT-Guard, a content safety guardrail model based on a Reasoning-Active Training, Reasoning-Free Inference paradigm. The key idea is to use reasoning supervision during training while emitting only structured safety labels at inference time. DT-Guard formulates safety judgment as a progressive decision process, Intent - Category - Safety, and constructs an intent-driven dataset with intent labels, risk categories, safety labels, and structured reasoning trajectories. To further improve hard-case robustness, we propose Rollout-Guided Progressive Hard-Case Optimization (RG-PHO), which uses multi-rollout consistency to identify stably mastered, persistently failed, and preference-unstable samples, and applies targeted supervised and preference optimization accordingly. At inference time, DT-Guard directly generates structured labels without explicit reasoning traces, preserving deployment efficiency. Experiments on prompt-side and response-side safety benchmarks show that DT-Guard achieves average F1 scores of 0.886 and 0.870, respectively. With only a 4B backbone, it reaches a dual-side average F1 of 0.878, outperforming strong 8B guardrail baselines. These results demonstrate that reasoning supervision can be effectively internalized into low-latency safety discrimination.

</details>

### 22. kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail

📄 [arXiv](https://arxiv.org/abs/2607.02072)　📅 2026-07

**关键词**：`defense`、`hidden activation`、`training-free guard`、`domain configuration`、`activation-space kNN`、`low-latency adaptation`

👤 **作者**：Mahmoud Abdelfattah、Hamid Nasiri、Peter Garraghan

- 🎯 **研究动机**：现有护栏依赖微调分类器，泛化低、推理延迟高
- 🔬 **研究方法**：提出 kNNGuard 免训练护栏：仅用 50 条安全/不安全提示库提取现成 LLM 多层激活，融合激活空间与嵌入空间 kNN 分数分类
- 📌 **结论**：六域上 F1 持平或超越微调 SOTA 护栏，快 2.7 倍（比微调分类器快 10 倍）；域适配只需 10 秒内更新提示库

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed in domains requiring guardrails to detect unsafe, off-topic, or adversarial prompts. Existing guardrails predominantly rely on fine-tuning to build classifiers, which often suffer from low generalization and high inference latency. We present kNNGuard, a training-free guardrail that utilizes the activation space of an off-the-shelf LLM. Given a small bank of 50 safe and unsafe prompts, kNNGuard extracts hidden activations and performs multi-layer kNN fusing activation-space and embedding-space scores for classification. Across six domains spanning topical and security prompts, kNNGuard achieves competitive or superior F1 compared to fine-tuned state-of-the-art guardrails while running 2.7x faster than the best comparable guardrail, and 10x faster than a fine-tuned safety classifier without gradient updates or fine-tuning. Domain adaptation requires only updating the labeled bank, which can be constructed in under 10 seconds and several orders of magnitude faster than established guardrails. We also analyze the impact of system prompts, layer selection, and integration into production LLM pipelines as a configurable, low-latency guardrail.

</details>

### 23. Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs

📄 [arXiv](https://arxiv.org/abs/2606.10487)　📅 2026-06

**关键词**：`defense`、`token-level probe`、`activation reuse`、`streaming moderation`、`hidden-state probe`、`token monitoring`

👤 **作者**：Huizhen Shu、Xuying Li、Piao Xue

- 🎯 **研究动机**：生成后单独审核模型使推理成本翻倍且只能在生成完成后发现违规，而审核所需信号已存在于隐藏状态中
- 🔬 **研究方法**：在生成器激活上训练轻量 token 级探针，复用激活免额外前向，在解码环内做亚毫秒逐 token 安全评分，支持流式提前中止或改写，并给出部署配方
- 📌 **结论**：单中层探针即可恢复强护栏模型大部分决策，计算开销比事后/流式护栏低多个数量级，探针线性分量还可做激活转向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying large language models in user-facing systems requires efficient output safety filtering. Existing approaches typically rely on a separate moderation model applied after generation, which doubles inference cost and only detects violations after generation completes. We observe that the signal needed for moderation is already present in the model hidden states. Based on this, we train lightweight token-level probes that operate directly on internal activations, producing per-token safety scores that can be aggregated for both offline evaluation and online intervention. The probe reuses activations from the generator and requires no additional forward pass, enabling sub millisecond per-token safety checks inside the decoding loop. A probe applied to a single mid layer recovers most decisions of a strong guard model, acting as a low cost surrogate optimized for latency rather than accuracy. In streaming settings, it can halt or modify unsafe outputs before they are fully generated, replacing end of sequence moderation with continuous token level monitoring. Compared to post hoc and streaming guard models, our method achieves orders of magnitude lower compute overhead with minimal latency cost. We also provide a practical deployment recipe, including layer selection, aggregation strategy, probing frequency, and triggering thresholds. Finally, we show that the probe linear component corresponds to a direction in residual space, enabling both detection and activation steering at negligible cost.

</details>

### 24. Do Safety Guardrails Need to Reason? LeanGuard: A Fast and Light Approach for Robust Moderation

📄 [arXiv](https://arxiv.org/abs/2606.26686)　📅 2026-06

**关键词**：`analysis`、`encoder guard`、`controlled comparison`、`inference cost`

👤 **作者**：Dongbin Na

- 🎯 **研究动机**：护栏普遍先生成 CoT 再判定，令护栏笨重缓慢，与端侧部署需求相悖；CoT 是否真的提升判定未被受控验证
- 🔬 **研究方法**：在同一语料上训练轻量双向编码器与推理式护栏，仅移除推理、其余全同的受控对比
- 📌 **结论**：395M 的 LeanGuard 平均 F1 82.90，匹配大得多的解码器推理护栏而计算量降约 100 倍，标签噪声下更稳、严格 FPR 下 recall 更高；现有基准可能不够难，CoT 必要性未被证明

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In order to screen a prompt or a response, the recent guardrail methods generate a chain-of-thought (CoT) before they issue a verdict. This design follows a common belief that step-by-step reasoning improves a decision. However, CoT also makes the guard heavy and slow, because the model must generate many tokens before it decides. This may not match how guardrails are actually deployed. A guardrail sometimes should not be heavy and slow, and it often runs on-device, for example on an embodied robot. In this paper, we pose a question whether a safety guardrail really needs to reason. To answer this question, we train a lightweight bidirectional encoder and a reasoning guard on the same corpus, and we then remove only the reasoning while we keep everything else fixed. With this controlled same-base comparison, we show that the chain does not improve moderation accuracy. We name the resulting guard LeanGuard. A 395M label-only encoder reaches an average F1 of 82.90 $\pm$ 0.26 over public benchmarks. It matches a reasoning guard that is built on a much larger decoder, while it uses only a single forward pass over an input of at most 512 tokens. This is about a ~100x reduction in inference compute. We further show that this label-only encoder stays robust under training-label noise and retains far more recall at a strict false-positive rate than the reasoning guard, so a heavier reasoning guard is not the more robust choice either. Our finding suggests that the current guardrail benchmarks may not be hard enough to reward reasoning, and that the necessity of CoT for moderation is still not proven. We release all source codes and models including LeanGuard at https://github.com/ndb796/LeanGuard.

</details>

### 25. Robust and Efficient Guardrails with Latent Reasoning

📄 [arXiv](https://arxiv.org/abs/2605.29068) · 🤗 [Model](https://huggingface.co/Saidarth/CoLaGuard-8B/blob/main/modeling_colaguard.py)　📅 2026-05

**关键词**：`defense`、`latent reasoning`、`stage-wise curriculum`、`hidden-state propagation`

👤 **作者**：Siddharth Sai、Xiaofei Wen、Muhao Chen

- 🎯 **研究动机**：推理式护栏性能强但查询延迟与 token 开销使其难以高吞吐部署
- 🔬 **研究方法**：CoLaGuard 经阶段式课程把多步安全推理迁移到连续潜空间，推理时直接隐状态传播而无需显式理由生成
- 📌 **结论**：十个审核设定、八个基准上 macro-F1 超 Llama Guard 3 达 8.24 分，匹配显式推理基线 GuardReasoner 同时提速 12.9 倍、token 用量降 22.4 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Maintaining the safety of large language models (LLMs) is crucial as they are increasingly deployed in real-world applications. Existing safety guardrails typically rely on single-pass classification or, more recently, distilled reasoning. Reasoning-based guardrails significantly outperform classification-only baselines, but they incur substantial query latency and token overhead that make them impractical for highthroughput deployment. To address this challenge, we propose COLAGUARD, a guardrail model that transfers multi-step safety reasoning into a continuous latent space through a stage-wise training curriculum, enabling direct hidden-state propagation at inference. Evaluated on ten prompt- and response-moderation settings spanning eight safety benchmarks, COLAGUARD improves macro-F1 by 8.24 points over Llama Guard 3 and matches our explicit reasoning baseline, GuardReasoner, in macroF1 while delivering a 12.9X speedup and 22.4X reduction in token usage. Our results suggest that latent reasoning offers a practical alternative to explicit rationale generation for deployable guardrails, jointly improving safety robustness and inference efficiency rather than treating them as competing objectives.

</details>

### 26. GLiGuard: Schema-Conditioned Classification for LLM Safeguard

📄 [arXiv](https://arxiv.org/abs/2605.07982) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-05

**关键词**：`tool`、`schema-conditioned encoder`、`multi-task moderation`、`throughput`

👤 **作者**：Urchade Zaratiana、Mary Newhauser、George Hurn-Maloney、Ash Lewis

- 🎯 **研究动机**：SOTA 护栏依赖 7B-27B 自回归解码器，把分类问题变成序列文本生成，延迟高且难扩展到多维度评估
- 🔬 **研究方法**：GLiGuard 为 0.3B 双向编码器，把任务定义与标签语义编码为输入中的结构化 token schema，单次非自回归前向同时评 prompt 安全、拒答、14 类伤害与 11 类越狱
- 📌 **结论**：九个安全基准上 F1 与 7B-27B 解码器护栏相当，而模型小 23-90 倍、吞吐高 16 倍、延迟低 17 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classification problem as sequential text generation, a design choice that incurs high latency and scales poorly to multi-aspect evaluation. In this work, we introduce \textbf{GLiGuard}, a 0.3B-parameter schema-conditioned bidirectional encoder adapted from GLiNER2 for LLM content moderation. The key idea is to encode task definitions and label semantics directly into the input sequence as structured token schemas, enabling simultaneous evaluation of prompt safety, response safety, refusal detection, 14 fine-grained harm categories, and 11 jailbreak strategies in a single non-autoregressive forward pass. This schema-conditioned design lets supported task and label blocks be composed directly in the input schema at inference time. Across nine established safety benchmarks, GLiGuard achieves F1 scores competitive with 7B--27B decoder-based guards despite being 23--90$\times$ smaller, while delivering up to 16$\times$ higher throughput and 17$\times$ lower latency. These results suggest that compact bidirectional encoders can approach the accuracy of much larger guard models while drastically reducing inference cost. Code and models are available at https://github.com/fastino-ai/GLiGuard.

</details>

### 27. Safe-Unsafe Concept Separation Emerges from a Single Direction in Language Models Activation Space

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

### 28. Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations

📄 [arXiv](https://arxiv.org/abs/2601.00454)　📅 2026-01

**关键词**：`defense`、`conversation compression`、`multi-turn guard`、`token efficiency`

👤 **作者**：Hyunjun Kim

- 🎯 **研究动机**：guardrail 处理完整多轮对话历史的计算成本高昂
- 🔬 **研究方法**：Defensive M2S 把多轮对话压缩为单轮结构化表示后再训练与调用 guardrail，训练复杂度从 O(n²) 降至 O(n)
- 📌 **结论**：训练 token 从 15.7M 降至 169K（93 倍）；Qwen3Guard 加 hyphenize 压缩在 SafeDialBench 上达 93.8% 攻击检测召回，推理 token 减少 94.6%，较基线提升 38.9 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Guardrail models are essential for ensuring the safety of Large Language Model (LLM) deployments, but processing full multi-turn conversation histories incurs significant computational cost. We propose Defensive M2S, a training paradigm that fine-tunes guardrail models on Multi-turn to Single-turn (M2S) compressed conversations rather than complete dialogue histories. We provide a formal complexity analysis showing that M2S reduces training cost from $O(n^2)$ to $O(n)$ for $n$-turn conversations. Empirically, on our training dataset (779 samples, avg. 10.6 turns), M2S requires only 169K tokens compared to 15.7M tokens for the multi-turn baseline -- a 93$\times$ reduction. We evaluate Defensive M2S across three guardrail model families (LlamaGuard, Nemotron, Qwen3Guard) and three compression templates (hyphenize, numberize, pythonize) on SafeDialBench, a comprehensive multi-turn jailbreak benchmark. Our best configuration, Qwen3Guard with hyphenize compression, achieves 93.8% attack detection recall while reducing inference tokens by 94.6% (from 3,231 to 173 tokens per conversation). This represents a 38.9 percentage point improvement over the baseline while dramatically reducing both training and inference costs. Our findings demonstrate that M2S compression can serve as an effective efficiency technique for guardrail deployment, enabling scalable safety screening of long multi-turn conversations.

</details>

### 29. BERM: Low-Overhead Prompt-Injection Detection via In-Situ Benign Representation Modeling

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/8133.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`analysis`、`lightweight guard model`、`in-situ representation`、`deployment latency`、`prompt injection`

- 🎯 **研究动机**：现有提示注入防御依赖脆弱启发式或调用昂贵辅助模型，无法兼顾鲁棒与低延迟
- 🔬 **研究方法**：BERM 对 host LLM prefill 阶段提取的内部表征原位建模：联合对比学习良性表征紧致流形以最大化与恶意表征分离，轻量分类器推理时原位检测
- 📌 **结论**：F1 比最佳先前工作高 5.2 个百分点，同时快 12 倍以上，增量推理开销近零

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Real-world deployment of large language models (LLMs) necessitates a robust and low-latency approach to detect prompt injections; existing lowoverhead methods fail to simultaneously boost robustness and reduce latency. Current defenses for prompt injection either rely on brittle heuristics or invoke costly auxiliary models, imposing a significant runtime burden. We introduce BERM, a lightweight framework that performs in-situ detection by modeling a host LLM’s internal representations extracted during prefill, adding negligible overhead. Our approach trains a lightweight classifier atop the LLM by learning a compact manifold of benign representations via joint contrastive learning to maximize the separation from malicious representations. At inference, this pre-trained classifier enables in-situ detection without invoking auxiliary guard models. On a diverse landscape of prompt injection attacks, our framework establishes a new state-of-the-art, achieving an F1-score 5.2 percentage points (pp) higher than the best prior work. Critically, BERM achieves this while being over 12x faster, reducing incremental inference overhead to near-zero.

</details>

### 30. Explaining Jailbreaks: Structured and Interpretable Safety Assessment for Large Language Models

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4430.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`benchmark`、`analysis`、`explanation-aware guard`、`structured output`、`cross-benchmark transfer`

- 🎯 **研究动机**：越狱评估依赖 ASR 等结果级指标，无法说明安全失败如何与为何发生
- 🔬 **研究方法**：解释感知安全框架：在二元有害检测上增加严重度、策略、触发 span、理由与安全因子的结构化解释，人机混合标注管线加微调紧凑模型生成规范解释
- 📌 **结论**：防御评估中把 ASR 降至 Vicuna-7B 的 0.44% 与 GPT-3.5 的 1.30% 并达最低 StrongREJECT 分，诊断属性恢复优于通用 LLM 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) remain highly vulnerable to jailbreak attacks, yet existing evaluations rely primarily on outcome-level metrics such as Attack Success Rate (ASR), providing limited insight into how and why safety failures occur. We propose an explanation-aware safety framework that augments binary harmfulness detection with structured, human-interpretable explanations capturing severity, strategies, trigger spans, rationales, and derived safety factors. To enable scalable and consistent supervision, we introduce a human–LLM hybrid annotation and canonicalization pipeline. We then fine-tune a compact model to generate canonical explanations alongside harmfulness decisions. Across both seen and unseen benchmark settings, our method improves robustness and explanation fidelity. In jailbreak defense evaluation, our approach reduces ASR to 0.44% on Vicuna-7B and 1.30% on GPT-3.5, outperforming existing defense baselines while also achieving the lowest StrongREJECT scores. Beyond outcome-level gains, the model more accurately recovers diagnostic attributes (e.g., attack strategy, trigger spans, and safety factors) than strong general-purpose LLM baselines. Overall, explanation-aware learning exposes diagnostic dimensions that ASR alone cannot capture and provides a more faithful and actionable foundation for robust LLM safety assessment.

</details>

### 31. ConceptGuard: Neuro-Symbolic Safety Guardrails via Sparse Interpretable Jailbreak Concepts

📄 [arXiv](https://arxiv.org/abs/2508.16325)　📅 2025-08

**关键词**：`defense`、`sparse autoencoder`、`interpretable concept`、`activation guard`

👤 **作者**：Darpan Aswal、Céline Hudelot

- 🎯 **研究动机**：对齐与安全微调只提供有限越狱鲁棒性，防御缺乏可解释性与泛化
- 🔬 **研究方法**：提出 ConceptGuard：用稀疏自编码器在 LLM 内部识别与越狱主题相关的可解释概念，构建激活级护栏
- 📌 **结论**：提供可解释、可泛化的防御且不牺牲模型能力、无需再微调；发现越狱攻击存在共享激活几何

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models have found success in a variety of applications. However, their safety remains a concern due to the existence of various jailbreaking methods. Despite significant efforts, alignment and safety fine-tuning only provide a certain degree of robustness against jailbreak attacks that covertly mislead LLMs towards the generation of harmful content. This leaves them prone to a range of vulnerabilities, including targeted misuse and accidental user profiling. This work introduces \textbf{ConceptGuard}, a novel framework that leverages Sparse Autoencoders (SAEs) to identify interpretable concepts within LLM internals associated with different jailbreak themes. By extracting semantically meaningful internal representations, ConceptGuard enables building robust safety guardrails -- offering fully explainable and generalizable defenses without sacrificing model capabilities or requiring further fine-tuning. Leveraging advances in the mechanistic interpretability of LLMs, our approach provides evidence for a shared activation geometry for jailbreak attacks in the representation space, a potential foundation for designing more interpretable and generalizable safeguards against attackers.

</details>

### 32. SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2502.12464) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.105/)　📅 2025-02　🏷 ACL 2025

**关键词**：`defense`、`guard routing`、`hard-example detection`、`compute trade-off`

👤 **作者**：Seanie Lee、…、Sung Ju Hwang

- 🎯 **研究动机**：大 guard 准确但昂贵，蒸馏小 guard 在困难样本上明显落后
- 🔬 **研究方法**：SafeRoute 训练二元 router 区分难易样本，仅将难样本交给大安全模型处理
- 📌 **结论**：显著改善算力与安全性能的权衡，优于相关基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deploying large language models (LLMs) in real-world applications requires robust safety guard models to detect and block harmful user prompts. While large safety guard models achieve strong performance, their computational cost is substantial. To mitigate this, smaller distilled models are used, but they often underperform on "hard" examples where the larger model provides accurate predictions. We observe that many inputs can be reliably handled by the smaller model, while only a small fraction require the larger model's capacity. Motivated by this, we propose SafeRoute, a binary router that distinguishes hard examples from easy ones. Our method selectively applies the larger safety guard model to the data that the router considers hard, improving efficiency while maintaining accuracy compared to solely using the larger safety guard model. Experimental results on multiple benchmark datasets demonstrate that our adaptive model selection significantly enhances the trade-off between computational cost and safety performance, outperforming relevant baselines.

</details>

### 33. Lightweight Safety Classification Using Pruned Language Models

📄 [arXiv](https://arxiv.org/abs/2412.13435)　📅 2024-12

**关键词**：`defense`、`intermediate-layer feature`、`pruned model`、`prompt-injection detection`

👤 **作者**：Mason Sawtell、Tula Masterman、Sandi Besen、Jim Brown

- 🎯 **研究动机**：专用安全分类器训练成本高，大模型推理又贵
- 🔬 **研究方法**：LEC 在 LLM 最优中间层 hidden state 上训练 Penalized Logistic Regression，模型可剪枝到该层仅作特征提取器
- 📌 **结论**：超越 GPT-4o 与专用微调模型，少于 100 个高质量样本即可训练，中间层普遍优于最终层

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we introduce a novel technique for content safety and prompt injection classification for Large Language Models. Our technique, Layer Enhanced Classification (LEC), trains a Penalized Logistic Regression (PLR) classifier on the hidden state of an LLM's optimal intermediate transformer layer. By combining the computational efficiency of a streamlined PLR classifier with the sophisticated language understanding of an LLM, our approach delivers superior performance surpassing GPT-4o and special-purpose models fine-tuned for each task. We find that small general-purpose models (Qwen 2.5 sizes 0.5B, 1.5B, and 3B) and other transformer-based architectures like DeBERTa v3 are robust feature extractors allowing simple classifiers to be effectively trained on fewer than 100 high-quality examples. Importantly, the intermediate transformer layers of these models typically outperform the final layer across both classification tasks. Our results indicate that a single general-purpose LLM can be used to classify content safety, detect prompt injections, and simultaneously generate output tokens. Alternatively, these relatively small LLMs can be pruned to the optimal intermediate layer and used exclusively as robust feature extractors. Since our results are consistent on different transformer architectures, we infer that robust feature extraction is an inherent capability of most, if not all, LLMs.

</details>

### 34. It Takes One to Bias Them All: Breaking Bad with One-Shot GRPO

📄 [arXiv](https://arxiv.org/abs/2606.10931) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-06

**关键词**：`attack`、`one-shot GRPO`、`systematic bias`、`cyber misuse`、`alignment poisoning`

👤 **作者**：Naihao Deng、Yilun Zhu、Naichen Shi、Clayton Scott、Rada Mihalcea

- 🎯 **研究动机**：大规模后训练建立的对齐护栏能否被极小样本打破尚不清楚
- 🔬 **研究方法**：研究 one-shot GRPO：仅用单个带偏样本做 GRPO 训练诱发系统性偏见，考察刻板推理的跨属性、类别与基准泛化
- 📌 **结论**：单个样本足以诱导系统性偏见并广泛泛化，且易感性与模型初始输出偏见的可能性相关，暴露后训练可被单例覆盖的关键漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Warning: This paper contains several toxic and offensive statements. Modern large language models (LLMs) are typically aligned through large-scale post-training to ensure fair and reliable behavior. In this work, we investigate how easily such guardrails can be broken by Group Relative Policy Optimization (GRPO). We show that one-shot GRPO training on a single biased example is sufficient to induce systematic bias, with stereotype-driven reasoning generalizing across attributes, categories, and benchmarks. We further find that models differ in their susceptibility based on the initial likelihood of producing biased outputs. Our results reveal a critical vulnerability in post-training: alignment can be overridden by a single example.

</details>