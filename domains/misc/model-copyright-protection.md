# 模型版权保护

## 研究方向

模型版权保护研究如何通过可验证信号证明模型、system prompt 等部署资产的身份、所有权与输出来源。该方向同时涵盖从权重、输出分布、知识边界和功能表征识别模型或 prompt 身份与谱系的指纹，以及在模型或输出中嵌入检测信号的模型水印；还关注黑盒 API 审计、应用克隆检测、指纹伪造、水印移除、改写鲁棒性和部署公平性。以阻止能力复制为核心的反蒸馏工作仍归入[模型微调安全 / 反蒸馏](../finetuning/anti-distillation.md)。

使用模型后门实现版权保护、授权控制或所有权验证的机制专题见 [后门式水印、版权保护与所有权验证](../content-authenticity/backdoor-based-watermarking-and-ownership.md)；本页保留模型版权视角的交叉索引。

## 研究脉络

- **Watermark：** 在模型输出或 reasoning trace 中嵌入可验证信号，用于内容或模型归属追踪。
- **Black-box fingerprint：** 通过精心设计的查询与输出行为审计 API 背后的模型身份或 system prompt clone，并研究 fingerprint spoofing 风险。
- **Weight 与 functional fingerprint：** 从参数或功能响应追踪 checkpoint、训练 seed 和模型演化谱系。

## Watermark 与内容溯源

### 1. Auditing Cross-Lingual Fairness in Language Model Watermarking

📄 [arXiv](https://arxiv.org/abs/2608.20047)　📅 2026-08

**关键词**：`analysis`、`model watermarking`、`cross-lingual fairness`、`copyright verification`

👤 **作者**：Alexander Nemecek、Osama Zafar、Debargha Ganguly、Vikash Singh、Vipin Chaudhary、Erman Ayday

- 🎯 **研究动机**：LLM 水印方案几乎只在英语评测，多语部署暴露出在英语上无关紧要却决定跨语结论的评测设计选择
- 🔬 **研究方法**：四组件框架：按部署语境经验校准检测阈值、阈值无关伴随测量区分校准与检测失败、三种质量测量范式、类型学家族划分上的广义熵分解；六方案、三生成器、11 语言
- 📌 **结论**：检测与质量上的跨语差异主要是类型学分区上的家族间差异——跨语水印公平性差距是语言属性的结构性问题而非个别语言特异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

</details>

### 2. Linguistic Holonomy and Statistical Watermarks: Inner Geometry of Meaning-Preserving Transformations

📄 [arXiv](https://arxiv.org/abs/2608.19369)　📅 2026-08

**关键词**：`analysis`、`model watermarking`、`paraphrase robustness`

👤 **作者**：Daniele Corradetti

- 🎯 **研究动机**：统计水印栖身于能指的自由度，被保义变换侵蚀；文献只用端点语义相似度度量变换——端点是错误统计量
- 🔬 **研究方法**：适配语言环路形式证明保义变换链不变量典范分解为端点部分与初始态稳定子中的和乐；检测端证明残差统计量与存活播种窗位置数的精确恒等式
- 📌 **结论**：推出衰减律 ρ^(h+1)；同一保留率下存活信号可为原信号的一半、四分之一或恰为零，仅取决于编辑落点——实验确认到三位小数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Statistical watermarks for language models live in the freedom of the signifier: they choose among tokens that are nearly equivalent in meaning, and they are therefore eroded by exactly those transformations which move the form of a text while leaving its content in place. The literature measures such transformations by their endpoint, through the semantic similarity between the original and the rewritten text. We show that the endpoint is the wrong statistic. Adapting the formalism of linguistic loops, we prove that the invariant of a chain of meaning-preserving transformations factorises canonically into an endpoint part and a holonomy in the stabiliser of the initial state, the second of which the semantic deficit cannot see; the loop rotation is parallel transport on the unit sphere of the embedding space, so that the analogy with the Wilson loop becomes a theorem rather than a figure of speech. On the side of the detector we prove an exact identity: the residual statistic is proportional to the number of positions whose seeding window survived intact, from which the decay law $ρ^{h+1}$ follows as the independent-edit corollary. The identity has a disconcerting consequence, which we confirm to three decimal places: at one and the same retention rate the surviving signal may be one half of the original, one quarter of it, or exactly nothing, according only to where the edits fall.

</details>

### 3. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

📄 [arXiv](https://arxiv.org/abs/2605.12456)　📅 2026-05

**关键词**：`tool`、`distillation attribution`、`model watermarking`、`content provenance`、`distillation tracing`

👤 **作者**：Tom Sander、…、Pierre Fernandez

- 🎯 **研究动机**：现有水印难同时兼顾检测强度、定位能力、输出质量与服务端优化兼容性
- 🔬 **研究方法**：TextSeal 基于 Gumbel-max，双密钥生成恢复多样性，熵加权打分与多区域定位，支持投机解码与多 token 预测且零推理开销
- 📌 **结论**：检测强度严格优于 SynthID-text，稀释混合文档下仍可定位；6000 次五语种 A/B 人类评价无感差异；水印具放射性，可检测未授权蒸馏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce TextSeal, a state-of-the-art watermark for large language models. Building on Gumbel-max sampling, TextSeal introduces dual-key generation to restore output diversity, along with entropy-weighted scoring and multi-region localization for improved detection. It supports serving optimizations such as speculative decoding and multi-token prediction, and does not add any inference overhead. TextSeal strictly dominates baselines like SynthID-text in detection strength and is robust to dilution, maintaining confident localized detection even in heavily mixed human/AI documents. The scheme is theoretically distortion-free, and evaluation across reasoning benchmarks confirms that it preserves downstream performance; while a multilingual human evaluation (6000 A/B comparisons, 5 languages) shows no perceptible quality difference. Beyond its use for provenance detection, TextSeal is also ``radioactive'': its watermark signal transfers through model distillation, enabling detection of unauthorized use.

</details>

### 4. Protecting Language Models Against Unauthorized Distillation through Trace Rewriting

📄 [arXiv](https://arxiv.org/abs/2602.15143) · 🎓 [Official](https://aclanthology.org/2026.acl-long.519/)　📅 2026-02　🏷 ACL 2026

**关键词**：`defense`、`tool`、`reasoning-trace protection`、`model watermarking`、`model provenance`、`watermarking`

👤 **作者**：Xinhang Ma、William Yeoh、Ning Zhang、Yevgeniy Vorobeychik

- 🎯 **研究动机**：未授权蒸馏盗用前沿模型的训练成果，缺少低成本 deterrent
- 🔬 **研究方法**：改写教师推理轨迹实现抗蒸馏与 API 水印，涵盖 LLM 指令式改写与梯度方法，保持答案正确与语义连贯
- 📌 **结论**：简单指令式改写在不降教师性能下取得强抗蒸馏效果，且水印可近零误报检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge distillation is a widely adopted technique for transferring capabilities from LLMs to smaller, more efficient student models. However, unauthorized use of knowledge distillation takes unfair advantage of the considerable effort and cost put into developing frontier models. We investigate methods for modifying teacher-generated reasoning traces to achieve two objectives that deter unauthorized distillation: (1) \emph{anti-distillation}, or degrading the training usefulness of query responses, and (2) \emph{API watermarking}, which embeds verifiable signatures in student models. We introduce several approaches for dynamically rewriting a teacher's reasoning outputs while preserving answer correctness and semantic coherence. Two of these leverage the rewriting capabilities of LLMs, while others use gradient-based techniques. Our experiments show that a simple instruction-based rewriting approach achieves a strong anti-distillation effect while maintaining or even improving teacher performance. Furthermore, we show that our rewriting approach also enables embedding watermarks that can be reliably detected with essentially no false alarms. Our code is available at https://github.com/xhOwenMa/trace-rewriting.

</details>

### 5. AGMark: Attention-Guided Dynamic Watermarking for Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2602.09611) · 🌐 [Project](https://doi.org/10.1145/3770855.3817700)　📅 2026-02　🏷 KDD 2026

**关键词**：`defense`、`LVLM watermark`、`attention guidance`、`ownership verification`

👤 **作者**：Yue Li、Xin Yi、Dongsheng Shi、Yongyi Cui、Gerard de Melo、Linlin Wang

- 🎯 **研究动机**：LVLM 水印或因视觉无关破坏 grounding，或依赖静态一次性权重估计且忽略权重密度，长尾引入低质 token
- 🔬 **研究方法**：AGMark 每步解码按注意力动态识别语义关键证据，结合 token 熵与证据校准自适应确定受保护 token 比例并划分词表
- 📌 **结论**：检测 AUC 至少 99.36%、攻击后仍至少 88.61%，同时显著提升视觉语义保真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Watermarking has emerged as a pivotal solution for content traceability and intellectual property protection in large vision language models (LVLMs). However, vision-agnostic watermarks may introduce visually irrelevant tokens and disrupt visual grounding by enforcing indiscriminate pseudo-random biases. Additionally, current vision-specific watermarks rely on a static, one-time estimation of vision-critical weights and ignore the weight distribution density when determining the proportion of protected tokens. This design fails to account for dynamic changes in visual dependence during generation and may introduce low-quality tokens in the long tail. To address these challenges, we propose Attention-Guided Dynamic Watermarking (AGMark), a novel framework that embeds detectable signals while largely preserving visual-semantic fidelity. At each decoding step, AGMark first dynamically identifies semantic-critical evidence based on attention weights for visual relevance, together with context-aware coherence cues, resulting in a more adaptive and well-calibrated evidence-weight distribution. It then determines the proportion of semantic-critical tokens by jointly considering uncertainty awareness (token entropy) and evidence calibration (weight density), thereby enabling more reliable adaptive vocabulary partitioning to avoid irrelevant tokens. Empirical results consistently confirm that AGMark outperforms conventional methods, substantially improving generation quality and yielding particularly strong gains in visual semantic fidelity in the later stages of generation. Our framework maintains highly competitive detection performance (at least 99.36% AUC) and robust attack resilience (at least 88.61% AUC) without sacrificing inference efficiency, taking a significant step toward reliability-preserving multimodal watermarking.

</details>

### 6. Toward LoRA Copyright Protection with an Authorized Dual-Watermarking Framework

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/7650.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`LoRA copyright`、`authorization control`、`dual watermark`

- 🎯 **研究动机**：LoRA 定制 T2I 扩散模型的服务与商业分发平台兴起，LoRA 模块的版权保护缺乏专门手段
- 🔬 **研究方法**：提出 LoRA2D 授权双水印框架：基于许可的授权控制加可按有效授权移除的显式水印震慑未授权使用，并持续嵌入隐式水印支持鲁棒黑盒所有权验证
- 📌 **结论**：在多个图像生成数据集上验证了 LoRA 版权保护的有效性与实用性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image (T2I) diffusion models have been widely adopted due to their strong generative capabilities, while Low-Rank Adaptation (LoRA) has emerged as an efficient mechanism for customizing these models for diverse creative and commercial applications. This trend has fostered LoRAcentric service platforms that that enable the customization and commercial distribution of LoRA modules according to user requirements. However, the growing prevalence of LoRA and its critical role in customized AI services have raised urgent concerns about LoRA copyright protection. To address this gap, we propose LoRA2 D, an authorized dual-watermarking framework specifically designed to protect LoRA modules in T2I diffusion models. LoRA2 D integrates licensebased authorization control with explicit watermarks as visible deterrents for unauthorized or trial usage, which can be removed upon valid authorization, while persistently embedding an implicit watermark for robust black-box ownership verification. Extensive experiments on multiple imagegeneration datasets demonstrate the effectiveness and practicality of LoRA2 D for securing copyrights in LoRA-adapted T2I diffusion models.

</details>

### 7. LLM Fingerprinting via Semantically Conditioned Watermarks

📄 [arXiv](https://arxiv.org/abs/2505.16723) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007013)　📅 2025-05　🏷 ICLR 2026

**关键词**：`tool`、`model watermarking`、`ownership verification`

👤 **作者**：Thibaud Gloaguen、Robin Staab、Nikola Jovanović、Martin Vechev

- 🎯 **研究动机**：固定查询配固定回答的 LLM 指纹难在微调量化后幸存，且易被检测过滤
- 🔬 **研究方法**：以宽语义域替代固定查询集，以弥散在每条响应中的统计水印信号替代脆弱的异常回答
- 📌 **结论**：指纹隐蔽且对微调、量化等常见部署步骤全部鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most LLM fingerprinting methods teach the model to respond to a few fixed queries with predefined atypical responses (keys). This memorization often does not survive common deployment steps such as finetuning or quantization, and such keys can be easily detected and filtered from LLM responses, ultimately breaking the fingerprint. To overcome these limitations we introduce LLM fingerprinting via semantically conditioned watermarks, replacing fixed query sets with a broad semantic domain, and replacing brittle atypical keys with a statistical watermarking signal diffused throughout each response. After teaching the model to watermark its responses only to prompts from a predetermined domain e.g., French language, the model owner can use queries from that domain to reliably detect the fingerprint and verify ownership. As we confirm in our thorough experimental evaluation, our fingerprint is both stealthy and robust to all common deployment scenarios.

</details>

### 8. Uncovering and Understanding Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels

📄 [arXiv](https://arxiv.org/abs/2608.20732)　📅 2026-08

**关键词**：`detection`、`API dependency lineage`、`prefix-cache side channel`、`reseller provenance`、`API dependency tracing`、`reseller supply chain`

👤 **作者**：Zimo Ji、…、Shuai Wang

- 🎯 **研究动机**：多级转售形成不透明 LLM API 供应链，用户请求可穿越未披露的上游转售商，现有研究只审计单个转售商
- 🔬 **研究方法**：CacheTracer 以 prefix-cache 复用为侧信道测依赖：Flood 经一个端点填充新鲜缓存、Prove 探测另一端点能否复用并排除探针自建命中；39 个端点、636 对、110 万请求
- 📌 **结论**：37.1% 端点对共享缓存可达、包含序跨七层、某缓存可达被至少 31 个节点包含——隐藏依赖深且集中，共同上游路径的失败可波及多个下游用户

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM API resellers have become an important access layer to modern LLM services. However, multi-level resale creates an opaque supply chain: a user's request may traverse undisclosed upstream resellers, each of which can inspect or modify prompts and responses, inducing ecosystem-level confidentiality and integrity risks. Existing studies audit individual resellers, but provide little visibility into hidden dependencies across resellers. We present CacheTracer, the first API-only measurement of such hidden dependencies. Our key insight is to exploit prefix-cache reuse as a side channel to measure dependency via cache-reach relations. CacheTracer operationalizes this insight with two primitives: Flood populates fresh cache state through one endpoint, and Prove probes whether another can reuse it while excluding probe-created hits. We then conduct a real-world measurement study with CacheTracer on 39 reseller endpoints, sending 1.1 million API requests across 636 endpoint pairs. Our measurements reveal a deep, concentrated cache-reach structure: 37.1% of measured pairs exhibit shared cache reach, the containment order spans seven layers, and one cache reach is contained within at least 31 of other nodes. We further find that the recovered structure is model-specific. We also evaluate the validity of CacheTracer through both real-world consistency checks and controlled experiments. The results show its high reliability and accuracy. These findings reveal substantial hidden dependencies among seemingly independent API resellers. Such deep and concentrated dependencies can create a large potential blast radius, where a confidentiality or integrity failure along a common upstream path may affect users across multiple downstream resellers.

</details>

### 9. AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services

📄 [arXiv](https://arxiv.org/abs/2608.22213)　📅 2026-08

**关键词**：`detection`、`response-adaptive fingerprinting`、`black-box API`、`copyright audit`、`black-box API identity`、`query-response signal`

👤 **作者**：Yilin Li、Yifei Zhang、Guozhu Meng

- 🎯 **研究动机**：黑盒 LLM 指纹用固定查询集，在 system prompt 与采样设置等真实配置下表现差，阻碍版权审计与安全评估
- 🔬 **研究方法**：AdaptPrint 响应自适应指纹，整合 Direct Probing、Continuation Probing、Follow-up Probing 三种递进的一致性探测，再在候选模型间做相似度匹配
- 📌 **结论**：27 个候选模型中 Top-1/Top-3/Top-5 准确率达 80.6%/90.3%/92.1%，对不同防御策略与解码参数稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box LLM services have emerged as a practical deployment paradigm. Nevertheless, their opacity also hinders the systematic assessment of security risks and complicates copyright auditing for model owners. Black-box LLM fingerprinting, which identifies the underlying LLM identity through query-response interactions, offers a promising way to bridge this gap. Existing approaches typically collect responses from target LLM services using a fixed set of queries and perform poorly in the presence of realistic and complex configurations (e.g., system prompt and sampling settings). To overcome these limitations, we propose AdaptPrint, a response-adaptive fingerprinting method for revealing hidden LLM identities in black-box LLM services. AdaptPrint integrates three progressive response consistency probing strategies: Direct Probing, Continuation Probing, and Follow-up Probing. AdaptPrint determines the final LLM identity by performing similarity matching among candidate LLMs. Experimental results show that AdaptPrint significantly outperforms state-of-the-art methods among 27 candidate models, achieving Top-1, Top-3, and Top-5 accuracies of 80.6%, 90.3%, and 92.1%. AdaptPrint also demonstrates strong robustness across different defense strategies and decoding parameters.

</details>

### 10. Do System Prompts Leave Behavioral Fingerprints? A Large-Scale Empirical Study of Clone Detection via Output Similarity

📄 [arXiv](https://arxiv.org/abs/2608.24461)　📅 2026-08

**关键词**：`detection`、`prompt fingerprint`、`behavioral signature`、`clone verification`、`system prompt fingerprint`、`black-box clone detection`

👤 **作者**：Linghan Chen、Yudong Gao、Jiyao Wang、Kaiyan Ji、Honglong Chen

- 🎯 **研究动机**：system prompt 可被超 80% 成功提取并零成本重部署，所有者无法黑盒验证克隆
- 🔬 **研究方法**：BBF 从模型输出注册行为签名，检验可疑部署是否比无关基线更匹配；基于 4 家族 8 个 benchmark、28.8 万条响应实证
- 📌 **结论**：同模型检测 AUC 0.876、跨模型 0.725；单句 formal-tone prefix 可使短输出检测从 0.978 崩至 0.547

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

System prompts can be extracted from commercial LLMs with over 80\% success and redeployed at zero cost, yet a prompt owner has no way to verify whether a suspected deployment is a clone. We propose Black-Box Behavioral Fingerprinting (BBF): the prompt owner registers a behavioral signature from model outputs and later tests whether a suspect deployment matches that signature more closely than an unrelated baseline. BBF requires only black-box API access. Through a large-scale study (4 model families, 8 benchmarks, 288{,}000 responses), we find that prompt choice explains 24.4\% of output variance and same-model detection reaches AUC 0.876. Cross-model performance is bounded by detector identity, with off-diagonal AUC ranging from 0.845 (Claude as detector) down to 0.665 (Qwen) and overall mean 0.725. BBF resists non-adaptive prompt paraphrasing (AUC $\geq 0.889$) and is robust to imperfect extraction, but a single-sentence formal-tone prefix can collapse detection on short structured outputs (MNLI 0.978 $\to$ 0.547), isolating style-invariant detection as the key open problem. Diagnostic Query Optimization, a zero-cost query selection rule, adds $+0.120$ to cross-model AUC.

</details>

### 11. Your “Pro” LLM Subscription May Actually Be “Free”: Exposing Fingerprint Spoofing Risks in LLM Inference Services

📄 [arXiv](https://arxiv.org/abs/2606.16100)　📅 2026-06

**关键词**：`attack`、`API identity`、`fingerprint spoofing`

👤 **作者**：Jiahao Zhang、Xiuyu Li、Suhang Wang

- 🎯 **研究动机**：用户靠黑盒指纹验证服务商是否真在提供付费高级模型，恶意服务商可微调弱模型冒充强模型绕过验证
- 🔬 **研究方法**：形式化证明有限查询预算与弱分类器使指纹易被欺骗，提出 GhostPrint：结合代理建模、奖励排序微调与知识蒸馏低成本构造冒充模型
- 📌 **结论**：静态与持续指纹设定下均一致绕过代表性指纹方法并保持效用，暴露 LLM 指纹管线的严重漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Model (LLM) APIs become ubiquitous, users increasingly rely on black-box fingerprinting to verify that providers are serving the advertised premium models. However, these methods may overlook adversarial providers who manipulate model weights to cheat the fingerprint process. We introduce a novel threat termed fingerprint spoofing, where a malicious provider stealthily serves a weaker model that has been parameter-efficiently fine-tuned to mimic a stronger model, thereby evading user-side fingerprinting. We first formally prove that user-side resource constraints (i.e., finite query budgets and weak fingerprinting classifiers) make current fingerprinting vulnerable to fingerprint spoofing. Guided by this theoretical analysis, we propose GhostPrint, a cost-effective attack framework leveraging surrogate modeling, reward-ranked fine-tuning, and knowledge distillation. Extensive evaluations in both static and continual fingerprinting settings demonstrate that GhostPrint allows weak models to consistently bypass representative fingerprint methods while maintaining utility at a low fine-tuning cost, exposing a critical vulnerability in current LLM fingerprinting pipelines.

</details>

### 12. KBF: Knowledge Boundary as Fingerprint for Language Model and Black-Box API Auditing

📄 [arXiv](https://arxiv.org/abs/2605.29524)　📅 2026-05

**关键词**：`detection`、`API identity`、`knowledge boundary`

👤 **作者**：Yijia Fang、Yiqing Feng、Bingyu Li、Mingxun Zhou

- 🎯 **研究动机**：中转与转售 API 普及，用户无法验证端点是否真在提供宣传的模型
- 🔬 **研究方法**：KBF 用知识边界附近稳定的数值召回行为做黑盒指纹，低成本审计模型 API 身份
- 📌 **结论**：16 个生产端点上标记全部 155 个经济相关的模型替换且不误拒同模型对照；可检测仅 5-10% 流量被替换的混合路由；六平台影子审计发现 27 个模型格中 7 个与参考端点不一致，集中于高价 Claude 端点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Relay and reseller APIs increasingly intermediate access to large language models (LLMs), but users have no direct way to verify that a claimed endpoint is actually serving the advertised model. We introduce KBF, a low-cost black-box auditing protocol that fingerprints model APIs using stable numerical recall near the knowledge boundary. Across 16 production LLM endpoints, KBF flags all 155 economically relevant substitutions without rejecting any same-model controls, remains stable under deployment variation, detects high-separation mixed-routing attacks when only 5-10% of traffic is substituted, and finds that 7 of 27 platform model cells in a six-platform shadow API audit are statistically inconsistent with their reference endpoints, with inconsistencies concentrated on premium Claude endpoints.

</details>

### 13. SIF: Semantically In-Distribution Fingerprints for Large Vision-Language Models

📄 [arXiv](https://arxiv.org/abs/2604.17041) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_SIF_Semantically_In-Distribution_Fingerprints_for_Large_Vision-Language_Models_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`defense`、`LVLM fingerprint`、`in-distribution query`、`model ownership`

👤 **作者**：Yifei Zhao、Qian Lou、Mengxin Zheng

- 🎯 **研究动机**：LVLM 所有权验证依赖语义异常查询或 OOD 响应作指纹，易被对抗者检测移除（以 Semantic Divergence Attack 证实）
- 🔬 **研究方法**：SIF 无需改参数：SAFD 将文本水印信号迁移到视觉模态生成语义连贯的指纹响应，RFO 模拟最坏扰动增强对微调量化的鲁棒性
- 📌 **结论**：在 LLaVA-1.5 与 Qwen2.5-VL 上同时实现强隐蔽性与鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The public accessibility of large vision-language models (LVLMs) raises serious concerns about unauthorized model reuse and intellectual property infringement. Existing ownership verification methods often rely on semantically abnormal queries or out-of-distribution responses as fingerprints, which can be easily detected and removed by adversaries. We expose this vulnerability through a Semantic Divergence Attack (SDA), which identifies and filters fingerprint queries by measuring semantic divergence between a suspect model and a reference model, showing that existing fingerprints are not semantic-preserving and are therefore easy to detect and bypass. To address these limitations, we propose SIF (Semantically In-Distribution Fingerprints), a non-intrusive ownership verification framework that requires no parameter modification. SIF introduces Semantic-Aligned Fingerprint Distillation (SAFD), which transfers text watermarking signals into the visual modality to produce semantically coherent yet fingerprinted responses. In addition, Robust-Fingerprint Optimization (RFO) enhances robustness by simulating worst-case representation perturbations, making the fingerprints resilient to model modifications such as fine-tuning and quantization. Extensive experiments on LLaVA-1.5 and Qwen2.5-VL demonstrate that SIF achieves strong stealthiness and robustness, providing a practical solution for LVLM copyright protection. Code is available at https://github.com/UCF-ML-Research/SIF-VLM-Fingerprint

</details>

### 14. Real Money, Fake Models: Deceptive Model Claims in Shadow APIs

📄 [arXiv](https://arxiv.org/abs/2603.01919)　📅 2026-03

**关键词**：`benchmark`、`API identity`、`shadow API`、`model substitution`

👤 **作者**：Yage Zhang、Yukun Jiang、Zeyuan Chen、Michael Backes、Xinyue Shen、Yang Zhang

- 🎯 **研究动机**：shadow API 声称提供官方模型访问，其输出一致性从未被系统审计，威胁科研可复现性
- 🔬 **研究方法**：识别 17 个被 187 篇论文使用的 shadow API，从效用、安全与模型身份三维度对比官方 API
- 📌 **结论**：性能分歧最高 47.21%，45.83% 指纹测试身份验证失败，安全行为不可预测，存在直接与间接的模型替换欺骗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Access to frontier large language models (LLMs), such as GPT-5 and Gemini-2.5, is often hindered by high pricing, payment barriers, and regional restrictions. These limitations drive the proliferation of $\textit{shadow APIs}$, third-party services that claim to provide access to official model services without regional limitations via indirect access. Despite their widespread use, it remains unclear whether shadow APIs deliver outputs consistent with those of the official APIs, raising concerns about the reliability of downstream applications and the validity of research findings that depend on them. In this paper, we present the first systematic audit between official LLM APIs and corresponding shadow APIs. We first identify 17 shadow APIs that have been utilized in 187 academic papers, with the most popular one reaching 5,966 citations and 58,639 GitHub stars by December 6, 2025. Through multidimensional auditing of three representative shadow APIs across utility, safety, and model verification, we uncover both indirect and direct evidence of deception practices in shadow APIs. Specifically, we reveal performance divergence reaching up to $47.21\%$, significant unpredictability in safety behaviors, and identity verification failures in $45.83\%$ of fingerprint tests. These deceptive practices critically undermine the reproducibility and validity of scientific research, harm the interests of shadow API users, and damage the reputation of official model providers.

</details>

### 15. IrisFP: Adversarial-Example-based Model Fingerprinting with Enhanced Uniqueness and Robustness

📄 [arXiv](https://arxiv.org/abs/2603.24996) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Geng_IrisFP_Adversarial-Example-based_Model_Fingerprinting_with_Enhanced_Uniqueness_and_Robustness_CVPR_2026_paper.html)　📅 2026-03　🏷 CVPR 2026

**关键词**：`defense`、`model fingerprint`、`adversarial query`、`ownership verification`

👤 **作者**：Ziye Geng、Guang Yang、Yihang Chen、Changqing Luo

- 🎯 **研究动机**：对抗样本指纹方法定位单一决策边界，唯一性与鲁棒性不足
- 🔬 **研究方法**：IrisFP 把指纹置于所有决策边界交点附近并构造复合样本指纹利用集体行为，再用两组参考模型的统计可分性评估判别力并配指纹专属阈值
- 📌 **结论**：一致超越 SOTA，同时增强鲁棒性与唯一性，实现可靠所有权验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose IrisFP, a novel adversarial-example-based model fingerprinting framework that enhances both uniqueness and robustness by leveraging multi-boundary characteristics, multi-sample behaviors, and fingerprint discriminative power assessment to generate composite-sample fingerprints. Three key innovations make IrisFP outstanding: 1) It positions fingerprints near the intersection of all decision boundaries - unlike prior methods that target a single boundary - thus increasing the prediction margin without placing fingerprints deep inside target class regions, enhancing both robustness and uniqueness; 2) It constructs composite-sample fingerprints, each comprising multiple samples close to the multi-boundary intersection, to exploit collective behavior patterns and further boost uniqueness; and 3) It assesses the discriminative power of generated fingerprints using statistical separability metrics developed based on two reference model sets, respectively, for pirated and independently-trained models, retains the fingerprints with high discriminative power, and assigns fingerprint-specific thresholds to such retained fingerprints. Extensive experiments show that IrisFP consistently outperforms state-of-the-art methods, achieving reliable ownership verification by enhancing both robustness and uniqueness.

</details>

### 16. When Anonymity Breaks: Identifying Models Behind Text-to-Image Leaderboards

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Naseh_When_Anonymity_Breaks_Identifying_Models_Behind_Text-to-Image_Leaderboards_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`model deanonymization`、`text-to-image leaderboard`、`fingerprinting`

👤 **作者**：Ali Naseh、Anshuman Suri、Yuefeng Peng、Harsh Chaudhari、Alina Oprea、Amir Houmansadr

- 🎯 **研究动机**：T2I 投票排行榜依赖匿名化模型输出保证公平，其匿名性可能被轻易打破
- 🔬 **研究方法**：发现各 T2I 模型生成在图像嵌入空间形成独特聚类，无需 prompt 控制或训练数据即可用质心法识别模型；并引入 prompt 级可区分度指标
- 📌 **结论**：在 22 个模型、280 个 prompt（15 万图像）上高准确率去匿名，部分 prompt 近乎完美区分，暴露排行榜安全缺陷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-image (T2I) models are increasingly popular, producing a large share of AI-generated images online. To compare model quality, voting-based leaderboards have become the standard, relying on anonymized model outputs for fairness. In this work, we show that such anonymity can be easily broken. We find that generations from each T2I model form distinctive clusters in the image embedding space, enabling accurate deanonymization without prompt control or training data. Using 22 models and 280 prompts (150K images), our centroid-based method achieves high accuracy and reveals systematic model-specific signatures. We further introduce a prompt-level distinguishability metric and conduct large-scale analyses showing how certain prompts can lead to near-perfect distinguishability. Our findings expose fundamental security flaws in T2I leaderboards and motivate stronger anonymization defenses.

</details>

### 17. Log Probability Tracking of LLM APIs

📄 [arXiv](https://arxiv.org/abs/2512.03816) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008078)　📅 2025-12　🏷 ICLR 2026

**关键词**：`detection`、`API identity`、`output signature`

👤 **作者**：Timothée Chauvin、Erwan Le Merrer、François Taïani、Gilles Tredan

- 🎯 **研究动机**：现有审计方法成本过高，无法对广泛的 LLM API 做定期监控，模型更新在实践中基本失察
- 🔬 **研究方法**：证明 logprob 虽非确定仍可作监控信号：仅请求单 token 输出，对各 token 平均 logprob 做简单统计检验，并提出 TinyChange 基准度量小改动敏感性
- 📌 **结论**：可检测小到一步微调的模型变化，比现有方法更敏感且便宜约 1000 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When using an LLM through an API provider, users expect the served model to remain consistent over time, a property crucial for the reliability of downstream applications and the reproducibility of research. Existing audit methods are too costly to apply at regular time intervals to the wide range of available LLM APIs. This means that model updates are left largely unmonitored in practice. In this work, we show that while LLM log probabilities (logprobs) are usually non-deterministic, they can still be used as the basis for cost-effective continuous monitoring of LLM APIs. We apply a simple statistical test based on the average value of each token logprob, requesting only a single token of output. This is enough to detect changes as small as one step of fine-tuning, making this approach more sensitive than existing methods while being 1,000x cheaper. We introduce the TinyChange benchmark as a way to measure the sensitivity of audit methods in the context of small, realistic model changes.

</details>

### 18. Every Language Model Has a Forgery-Resistant Signature

📄 [arXiv](https://arxiv.org/abs/2510.14086) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006817)　📅 2025-10　🏷 ICLR 2026

**关键词**：`detection`、`API identity`、`fingerprint spoofing`、`output signature`

👤 **作者**：Matthew Finlayson、Xiang Ren、Swabha Swayamdipta

- 🎯 **研究动机**：现有模型指纹等输出关联方法缺乏天然存在且难以伪造的输出来源验证信号
- 🔬 **研究方法**：利用语言模型输出 logprob 位于高维椭球面的几何约束作为模型签名，提出椭圆提取技术及类似对称密钥消息认证的输出验证协议
- 📌 **结论**：签名难伪造、天然存在且自包含，能识别输出来源模型；但生产规模模型上提取仍有实际障碍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The ubiquity of closed-weight language models with public-facing APIs has generated interest in forensic methods, both for extracting hidden model details (e.g., parameters) and for identifying models by their outputs. One successful approach to these goals has been to exploit the geometric constraints imposed by the language model architecture and parameters. In this work, we show that a lesser-known geometric constraint -- namely, that language model outputs lie on the surface of a high-dimensional ellipse -- functions as a signature for the model and can be used to identify the source model of a given output. This ellipse signature has unique properties that distinguish it from existing model-output association methods like language model fingerprints. In particular, the signature is hard to forge: without direct access to model parameters, it is practically infeasible to produce log-probabilities (logprobs) on the ellipse using currently known methods. Secondly, the signature is naturally occurring, since all language models have these elliptical constraints. Thirdly, the signature is self-contained, in that it is detectable without access to the model inputs or the full weights. Finally, the signature is compact and redundant, as it is independently detectable in each logprob output from the model. We evaluate a novel technique for extracting the ellipse from small models and discuss the practical hurdles that make it infeasible for production-scale models. Finally, we use ellipse signatures to propose a protocol for language model output verification, analogous to cryptographic symmetric-key message authentication systems.

</details>

### 19. Auditing Black-Box LLM APIs with a Rank-Based Uniformity Test

📄 [arXiv](https://arxiv.org/abs/2506.06975) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009673)　📅 2025-06　🏷 ICLR 2026

**关键词**：`detection`、`API identity`、`weight fingerprint`、`statistical testing`

👤 **作者**：Xiaoyuan Zhu、…、Willie Neiswanger

- 🎯 **研究动机**：API 供应商可能暗中提供量化或微调变体，用户无权重与 logits 难以察觉
- 🔬 **研究方法**：提出基于排序的均匀性检验，验证黑盒 LLM 与本地真模型的行为等价，查询高效且不产生可检测的查询模式
- 📌 **结论**：在量化、有害微调、越狱 prompt 与整体替换等威胁下，限定查询预算内统计功效一致优于既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As API access becomes a primary interface to large language models (LLMs), users often interact with black-box systems that offer little transparency into the deployed model. To reduce costs or maliciously alter model behaviors, API providers may discreetly serve quantized or fine-tuned variants, which can degrade performance and compromise safety. Detecting such substitutions is difficult, as users lack access to model weights and, in most cases, even output logits. To tackle this problem, we propose a rank-based uniformity test that can verify the behavioral equality of a black-box LLM to a locally deployed authentic model. Our method is accurate, query-efficient, and avoids detectable query patterns, making it robust to adversarial providers that reroute or mix responses upon the detection of testing attempts. We evaluate the approach across diverse threat scenarios, including quantization, harmful fine-tuning, jailbreak prompts, and full model substitution, showing that it consistently achieves superior statistical power over prior methods under constrained query budgets.

</details>

### 20. Hey, That’s My Model! Introducing Chain & Hash, an LLM Fingerprinting Technique

📄 [arXiv](https://arxiv.org/abs/2407.10887) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009215)　📅 2024-07　🏷 ICLR 2026

**关键词**：`detection`、`API identity`、`active fingerprinting`

👤 **作者**：Mark Russinovich、Yanan Cai、Ahmed Salem

- 🎯 **研究动机**：LLM 指纹需防碰撞且要挺住 meta-prompt 引起的输出分布剧变
- 🔬 **研究方法**：Chain & Hash 以密码学方式绑定指纹 prompt 与回答，训练中加入随机填充与多样 meta-prompt 配置
- 📌 **结论**：安全证明所有权，抗微调与对抗性指纹移除，并扩展到 LoRA 适配器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Growing concerns over the theft and misuse of Large Language Models (LLMs) underscore the need for effective fingerprinting to link a model to its original version and detect misuse. We define five essential properties for a successful fingerprint: Transparency, Efficiency, Persistence, Robustness, and Unforgeability. We present a novel fingerprinting framework that provides verifiable proof of ownership while preserving fingerprint integrity. Our approach makes two main contributions. First, a chain and hash technique that cryptographically binds fingerprint prompts to their responses, preventing collisions and enabling irrefutable ownership claims. Second, we address a realistic threat model in which instruction-tuned models' output distribution can be significantly altered through meta-prompts. By incorporating random padding and varied meta-prompt configurations during training, our method maintains robustness even under significant output style changes. Experiments show that our framework securely proves ownership, resists both benign transformations (e.g., fine-tuning) and adversarial fingerprint removal, and extends to fingerprinting LoRA adapters\footnote{We release our code at: https://github.com/microsoft/Chain-Hash.

</details>

### 21. Diff Mining: Logit Differences Reveal Finetuning Objectives

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

### 22. AWM: Accurate Weight-Matrix Fingerprint for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.06738) · 📝 [OpenReview](https://openreview.net/forum?id=fDC5WeLeqh) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008260)　📅 2025-10　🏷 ICLR 2026

**关键词**：`tool`、`model fingerprinting`、`model lineage`、`weight fingerprint`

👤 **作者**：Boyi Zeng、Lin Chen、Ziwei He、Xinbing Wang、Zhouhan Lin

- 🎯 **研究动机**：SFT、继续预训练、RL、多模态扩展、剪枝、升级回收等密集后训练使模型谱系识别困难
- 🔬 **研究方法**：提出免训练的权重矩阵指纹 AWM：以线性分配问题与无偏 CKA 相似度中和参数操纵的影响
- 📌 **结论**：60 正 90 负模型对上对六类后训练全部鲁棒、假阳性近零，全分类指标满分，单卡 3090 上 30 秒完成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Protecting the intellectual property of large language models (LLMs) is crucial, given the substantial resources required for their training. Consequently, there is an urgent need for both model owners and third parties to determine whether a suspect LLM is trained from scratch or derived from an existing base model. However, the intensive post-training processes that models typically undergo-such as supervised fine-tuning, extensive continued pretraining, reinforcement learning, multi-modal extension, pruning, and upcycling-pose significant challenges to reliable identification. In this work, we propose a training-free fingerprinting method based on weight matrices. We leverage the Linear Assignment Problem (LAP) and an unbiased Centered Kernel Alignment (CKA) similarity to neutralize the effects of parameter manipulations, yielding a highly robust and high-fidelity similarity metric. On a comprehensive testbed of 60 positive and 90 negative model pairs, our method demonstrates exceptional robustness against all six aforementioned post-training categories while exhibiting a near-zero risk of false positives. By achieving perfect scores on all classification metrics, our approach establishes a strong basis for reliable model lineage verification. Moreover, the entire computation completes within 30s on an NVIDIA 3090 GPU. The code is available at https://github.com/LUMIA-Group/AWM.

</details>

### 23. SeedPrints: Fingerprints Can Even Tell Which Seed Your Large Language Model Was Trained From

📄 [arXiv](https://arxiv.org/abs/2509.26404) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010114)　📅 2025-09　🏷 ICLR 2026

**关键词**：`tool`、`model fingerprinting`、`model lineage`

👤 **作者**：Yao Tong、Haonan Wang、Siquan Li、Kenji Kawaguchi、Tianyang Hu

- 🎯 **研究动机**：现有指纹方法依赖训练后才出现的签名，在大规模预训练阶段不可靠
- 🔬 **研究方法**：提出 SeedPrints：以随机初始化偏置作为种子依赖的持久标识符，利用未训练模型的可复现预测偏差做谱系验证
- 📌 **结论**：从初始化到大规模预训练及下游适配全程有效，LLaMA 与 Qwen 式模型上实现种子级区分与全生命周期身份验证，长训练、域移位与参数修改下稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fingerprinting Large Language Models (LLMs)is essential for provenance verification and model attribution. Existing fingerprinting methods are primarily evaluated after fine-tuning, where models have already acquired stable signatures from training data, optimization dynamics, or hyperparameters. However, most of a model's capacity and knowledge are acquired during pretraining rather than downstream fine-tuning, making large-scale pretraining a more fundamental regime for lineage verification. We show that existing fingerprinting methods become unreliable in this regime, as they rely on post-hoc signatures that only emerge after substantial training. This limitation contradicts the classical Galton notion of a fingerprint as an intrinsic and persistent identity. In contrast, we propose a stronger and more intrinsic notion of LLM fingerprinting: SeedPrints, a method that leverages random initialization biases as persistent, seed-dependent identifiers present even before training begins. We show that untrained models exhibit reproducible prediction biases induced by their initialization seed, and that these weak signals remain statistically detectable throughout training, enabling high-confidence lineage verification. Unlike prior techniques that fail during early pretraining or degrade under distribution shifts, SeedPrints remains effective across all training stages, from initialization to large-scale pretraining and downstream adaptation. Experiments on LLaMA-style and Qwen-style models demonstrate seed-level distinguishability and enable birth-to-lifecycle identity verification. Evaluations on large-scale pretraining trajectories and real-world fingerprinting benchmarks further confirm its robustness under prolonged training, domain shifts, and parameter modifications.

</details>

### 24. LLM DNA: Tracing Model Evolution via Functional Representations

📄 [arXiv](https://arxiv.org/abs/2509.24496) · 🌐 [Project](https://dna.xtra.science/) · 📝 [OpenReview](https://openreview.net/forum?id=UIxHaAqFqQ) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009243)　📅 2025-09　🏷 ICLR 2026

**关键词**：`tool`、`model fingerprinting`、`model lineage`

👤 **作者**：Zhaomin Wu、Haodong Zhao、Ziyang Wang、Jizhou Guo、Qian Wang、Bingsheng He

- 🎯 **研究动机**：海量 LLM 经微调、蒸馏、适配的演化关系大多未记录，现有方法受任务特定、固定模型集与 tokenizer/架构假设限制
- 🔬 **研究方法**：数学定义 LLM DNA 为功能行为的低维 bi-Lipschitz 表示，证明满足遗传性与决定论并给出免训练提取管线
- 📌 **结论**：305 个 LLM 上与已知关系吻合并发现未记录的关联，系统发生树还原 encoder-decoder 到 decoder-only 的架构变迁与各家族演化速度差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The explosive growth of large language models (LLMs) has created a vast but opaque landscape: millions of models exist, yet their evolutionary relationships through fine-tuning, distillation, or adaptation are often undocumented or unclear, complicating LLM management. Existing methods are limited by task specificity, fixed model sets, or strict assumptions about tokenizers or architectures. Inspired by biological DNA, we address these limitations by mathematically defining LLM DNA as a low-dimensional, bi-Lipschitz representation of functional behavior. We prove that LLM DNA satisfies inheritance and genetic determinism properties and establish the existence of DNA. Building on this theory, we derive a general, scalable, training-free pipeline for DNA extraction. In experiments across 305 LLMs, DNA aligns with prior studies on limited subsets and achieves superior or competitive performance on specific tasks. Beyond these tasks, DNA comparisons uncover previously undocumented relationships among LLMs. We further construct the evolutionary tree of LLMs using phylogenetic algorithms, which align with shifts from encoder-decoder to decoder-only architectures, reflect temporal progression, and reveal distinct evolutionary speeds across LLM families.

</details>

### 25. Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification

📄 [arXiv](https://arxiv.org/abs/2608.14929)　📅 2026-08

**关键词**：`detection`、`model copyright`、`ownership verification`、`model provenance`

👤 **作者**：Aman Singh Thakur、Rayan Khoury

- 🎯 **研究动机**：开源模型被微调、量化、剪枝、合并但谱系常无文档，仅凭权重能否判定共同祖先未知
- 🔬 **研究方法**：移除残差训练产生的身份对齐共享分量，比较残差块上 checkpoint 特有结构得对称谱系分数，以独立 checkpoint 校准
- 📌 **结论**：residual-MLP 与 GPT-2 基准上以 AUROC=1.0 区分微调/LoRA 合并/剪枝/量化后代与独立及蒸馏模型；函数保持洗钱实验下分数不变且比最近鲁棒基线快 76 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented. We study data-free white-box lineage verification: can weights alone reveal whether two compatible model checkpoints share ancestry? Residual training produces a shared identity-aligned component in branch products, so this structure alone cannot establish ancestry. We remove it and compare checkpoint-specific structure across residual blocks, yielding a symmetric lineage score calibrated against independent checkpoints. On residual-MLP and GPT-2 benchmarks, the score separates fine-tuned, LoRA-merged, pruned, and quantized descendants from independent and distilled models (AUROC=1.0), distinguishing weight ancestry from behavioral similarity. Under function-preserving checkpoint laundering experiments, weight-space baselines lose margin or fail; our score remains unchanged and runs 76x faster than the nearest robust baseline on GPT-2. The projection-pairing signal appears across six language-model families and beyond, and a case study correctly identifies 3 related and 7 unrelated LLaMA-2 public checkpoints. Collectively, these results establish a passive, data-free provenance signal for compatible open-weight language-model checkpoints

</details>

### 26. Stealing Reasoning Traces from Proprietary LLM APIs

📄 [arXiv](https://arxiv.org/abs/2608.09867)　📅 2026-08

**关键词**：`attack`、`detection`、`encrypted reasoning`、`cross-model replay`、`anti-distillation bypass`、`prompt injection`

👤 **作者**：Alexander Panfilov、…、Maksym Andriushchenko

- 🎯 **研究动机**：提供商以加密块返回 CoT 由客户端回传，这些加密块在同一厂商生态内跨会话、用户与模型完全兼容可互换，构成架构漏洞
- 🔬 **研究方法**：把加密推理迹注入同厂商更弱、防护更弱的模型迫使其明文解码输出，无需直接越狱更强模型
- 📌 **结论**：跨 Anthropic、OpenAI、Google 绕过反蒸馏；解码公开库 315,320 个加密块恢复 367 个 PII 与 182 个凭据；还泄露最终输出已拒答的隐藏有害信息并支持加密块内不可见注入

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Leading large language model providers now conceal their models' step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different sessions, users, and models within a provider's ecosystem. We exploit this compatibility to develop a scalable decryption jailbreak. By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly. This vulnerability enables four distinct attack vectors. First, it circumvents anti-distillation mechanisms, allowing adversaries to extract a proprietary model's reasoning, as we demonstrate across Anthropic, OpenAI, and Google. Second, it allows for large-scale private data extraction. Developers frequently share session logs publicly, unaware of contents of the encrypted blocks. By decoding 315,320 reasoning blocks scraped from public repositories, we recovered 367 Personally Identifiable Information (PII) artifacts and 182 credentials. Third, it inadvertently reveals hazardous information hidden within the reasoning process, even in cases where the model's final, visible output safely rejects a malicious request. Fourth, attackers can leverage this flaw to execute invisible prompt injections, embedding malicious payloads entirely within encrypted blocks to poison public agentic rollouts. Following responsible disclosure, we propose concrete cryptographic and system-level mitigations to secure client-side reasoning.

</details>

### 27. Who Built This Model? Tracing LLM Lineage via Spectral Fingerprints in Weight Space

📄 [arXiv](https://arxiv.org/abs/2608.07786) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-08

**关键词**：`detection`、`spectral fingerprint`、`model copyright`、`ownership verification`、`model provenance`、`supply-chain integrity`

👤 **作者**：Yiwei Chen、Bingqi Shang、Sijia Liu

- 🎯 **研究动机**：开源 LLM 经多阶段管线产生复杂谱系关系，仅凭权重空间是否存在可判源内在指纹未知
- 🔬 **研究方法**：统一几何指纹框架：奇异值分布编码谱能量、子空间偏差量化方向几何，区分独立起源、同系列与共享基座三类谱系
- 📌 **结论**：110+ 开源模型对上，谱能量可靠区分独立训练模型与不同家族，子空间对齐可细粒度区分数据规模与后训练差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight large language models (LLMs) are increasingly developed through complex, multi-stage pipelines, leading to intricate lineage relationships that reflect model origin, ownership, and evolution. Understanding these relationships is important for model provenance, governance, and supply-chain integrity. In this work, we investigate the notion of LLM "biometrics" (analogous to human biometrics) to ask whether LLMs exhibit intrinsic fingerprints in weight space alone, without access to input data, that reveal their origin and lineage. We formulate this as a lineage discrimination problem, distinguishing among independent-origin, same-series, and shared-base models. To characterize these relationships, we propose a unified geometric fingerprinting framework that analyzes weight matrices from two complementary perspectives: (i) spectral energy, captured by singular value distributions to encode global magnitude patterns, and (ii) subspace alignment, quantified via subspace deviations to capture directional geometry. Our analysis uncovers a clear hierarchy of structural similarity in weight space: spectral energy reliably distinguishes independently trained models and different model families, while subspace alignment enables fine-grained discrimination among closely related models, including variations in dataset scale and post-training procedures. Extensive experiments on over 110 diverse open-weight LLM pairs demonstrate that weight-space geometry provides a robust and interpretable signal for model lineage, enabling coarse-grained regime separation and fine-grained discrimination within shared-base models.

</details>

### 28. Breaking the Boundary Barrier: Robust Model Fingerprinting via Unlearnable Examples in Model-Parameter Space

🌐 [Project](https://doi.org/10.1145/3770854.3780310)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`model fingerprint`、`unlearnable example`、`ownership verification`

- 🎯 **研究动机**：现有模型指纹在决策边界处易被规避，所有权验证不鲁棒
- 🔬 **研究方法**：在模型参数空间以unlearnable example构造指纹
- 📌 **结论**：指纹对自适应规避保持可验证性

### 29. PathMark: Protecting Intellectual Property of Mixture-of-expert LLMs via Path Watermarks

📄 [arXiv](https://arxiv.org/abs/2607.03688) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-07　🏷 ACM CCS 2026

**关键词**：`defense`、`routing path`、`content watermark`、`model copyright`、`MoE watermarking`、`model ownership`

👤 **作者**：Yudong Gao、…、Shuai Wang

- 🎯 **研究动机**：面向稠密模型的水印方案在 MoE 上因动态路由失效：水印参数不再被一致激活，且存在决策边界脆弱与路由纠缠两大漏洞
- 🔬 **研究方法**：提出 PathMark：将路由路径本身作为隐蔽水印信道，触发时约束全部 token 经预定专家子集形成路径签名；用分布对齐与对比损失抵消梯度泄漏，支持组合路径多比特编码及白盒/黑盒验证
- 📌 **结论**：四个 MoE 模型上验证准确率 >99%、困惑度退化 <2%，在量化、微调、剪枝与自适应攻击下鲁棒性优异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) large language models represent high-value intellectual property, yet existing watermarking schemes designed for dense models fail on MoE architectures due to architectural mismatch: traditional methods assume watermarked parameters are consistently activated, but MoE's dynamic routing breaks this assumption. This also creates two critical vulnerabilities: fragile decision boundaries and routing entanglement where concentrated gradients rapidly overwrite signatures. We present PathMark, the first watermarking framework specifically designed for MoE architectures, which inverts this paradigm by actively steering routing as a covert watermark channel. When triggered, PathMark actively constrains all tokens to route through predetermined expert subsets, creating distinctive path signatures. Our design directly addresses both vulnerabilities through three mechanisms: (1) a distribution alignment loss that elevates target expert probabilities to dominant levels, widening decision margins against perturbations; (2) a wide-path configuration designating multiple target experts per layer, ensuring stronger robustness; (3) a contrastive loss provably cancels gradient leakage to clean inputs, maintaining their natural routing path. Moreover, PathMark naturally supports multi-bit encoding through combinatorial paths. Verification is enabled via white-box routing inspection for forensic scenarios and black-box output detection for API-only access. Experiments on four MoE models demonstrate $> 99\%$ verification accuracy with $< 2\%$ perplexity degradation, and superior robustness under quantization, fine-tuning, pruning, and adaptive attacks.

</details>

### 30. Detecting and Suppressing Reward Hacking with Gradient Fingerprints

📄 [arXiv](https://arxiv.org/abs/2604.16242) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`detection`、`reward hacking`、`gradient fingerprint`、`model copyright`、`reasoning trace`

👤 **作者**：Songtao Wang、…、Xi Ye

- 🎯 **研究动机**：RLVR 只优化结果奖励，reward hacking 的 CoT 表面合理，纯文本监控难以识别
- 🔬 **研究方法**：GRIFT 计算给定 prompt 下 CoT 的条件梯度并压缩为紧凑表征，据此判断是否 reward hacking
- 📌 **结论**：数学、代码与逻辑基准上较 CoT Monitor、TRACE 相对提升超 25%；接入拒绝微调管线可减少 hacking 并提升真实任务表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning with verifiable rewards (RLVR) typically optimizes for outcome rewards without imposing constraints on intermediate reasoning. This leaves training susceptible to reward hacking, where models exploit loopholes (e.g., spurious patterns in training data) in the reward function to achieve high scores without solving the intended task. These reward-hacking behaviors are often implicit, as the intermediate chain-of-thought (CoT) may appear plausible on the surface, limiting the effectiveness of purely text-based monitoring. We propose Gradient Fingerprint (GRIFT), a method for detecting reward hacking using models' internal computations. Given a prompt and a model-generated CoT, GRIFT computes gradients of the CoT conditioned on the prompt and compresses them into a compact representation, which is then used to assess whether the CoT reflects reward hacking behavior. Across verifiable reasoning benchmarks spanning math, code, and logical reasoning, GRIFT substantially outperforms strong baselines, including CoT Monitor and TRACE, achieving over 25% relative improvement in detecting reward hacking behavior. Moreover, integrating GRIFT into the rejection fine-tuning pipeline for reasoning tasks reduces reward hacking and improves performance on the true task objective. Our results highlight a promising direction of leveraging gradient level representations for assessing the quality of CoT reasoning traces. Our code is available at: https://github.com/songtao-x/reward_hack.

</details>

### 31. Attesting Model Lineage by Consisted Knowledge Evolution with Fine-Tuning Trajectory

📄 [arXiv](https://arxiv.org/abs/2601.11683) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/shang)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`detection`、`model lineage`、`fine-tuning trajectory`、`model copyright`、`ownership attestation`

👤 **作者**：Zhuoyi Shang、Jiasen Li、Pengzhen Chen、Yanwei Liu、Xiaoyan Gu、Weiping Wang

- 🎯 **研究动机**：开源模型库缺乏鲁棒 lineage 验证，静态架构相似度无法捕捉微调背后的知识动态演化
- 🔬 **研究方法**：借鉴遗传机制，用模型编辑量化微调引入的参数变化，借探针样本把演化知识向量化为紧凑表示，再验证模型间知识关系的算术一致性
- 📌 **结论**：在分类器、扩散模型与 LLM 上跨多样对抗场景实现可靠的模型谱系认证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The fine-tuning technique in deep learning gives rise to an emerging lineage relationship among models. This lineage provides a promising perspective for addressing security concerns such as unauthorized model redistribution and false claim of model provenance, which are particularly pressing in \textcolor{blue}{open-weight model} libraries where robust lineage verification mechanisms are often lacking. Existing approaches to model lineage detection primarily rely on static architectural similarities, which are insufficient to capture the dynamic evolution of knowledge that underlies true lineage relationships. Drawing inspiration from the genetic mechanism of human evolution, we tackle the problem of model lineage attestation by verifying the joint trajectory of knowledge evolution and parameter modification. To this end, we propose a novel model lineage attestation framework. In our framework, model editing is first leveraged to quantify parameter-level changes introduced by fine-tuning. Subsequently, we introduce a novel knowledge vectorization mechanism that refines the evolved knowledge within the edited models into compact representations by the assistance of probe samples. The probing strategies are adapted to different types of model families. These embeddings serve as the foundation for verifying the arithmetic consistency of knowledge relationships across models, thereby enabling robust attestation of model lineage. Extensive experimental evaluations demonstrate the effectiveness and resilience of our approach in a variety of adversarial scenarios in the real world. Our method consistently achieves reliable lineage verification across a broad spectrum of model types, including classifiers, diffusion models, and large language models.

</details>

### 32. UMMF: Protecting Copyright of Large Vision-Language Models through Unlearning-based Multimodal Memorization Fingerprint

🎓 [Official](https://aclanthology.org/2026.acl-long.429/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`multimodal safety`、`machine unlearning`、`VLM safety`、`training-data memorization`

👤 **作者**：Xiaofan Zheng、Xinghao Wang、Xiaojun Wan

- 🎯 **研究动机**：LVLM 指纹现有方法依赖固定形式触发器作为显式指纹，隐蔽性与鲁棒性不足
- 🔬 **研究方法**：提出 UMMF：通过遗忘训练样本的邻近样本强化过拟合特性，在数据流形上引入可检测的泛化差区域，把邻近样本记忆强度差异用作隐式指纹
- 📌 **结论**：多策略多数据集实验显示比固定触发器方法更具隐蔽性、鲁棒性与适应性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training Large Vision-Language Models (LVLMs) is costly and resource-intensive, making them valuable assets. To prevent malicious users from unauthorized commercialization of these artificial intelligence assets through fine-tuning and black-box deployment, model fingerprinting techniques aimed at verifying the ownership of LVLMs are receiving widespread attention. Existing fingerprinting techniques rely on adversarial attacks or backdoor attacks to construct trigger images for specific outputs, attributing model ownership by comparing whether the output of trigger images on suspected models matches the predetermined output. However, these methods depend on fixed-form triggers as explicit model fingerprints, which have limitations in terms of stealthiness and robustness. Inspired by unlearning research, we propose Unlearning-based Multimodal Memorization Fingerprint (UMMF). UMMF strengthens the overfitting characteristics of training samples by unlearning neighboring samples of the training samples, thereby introducing detectable regions of poor generalization in the data manifold. Compared with previous methods, our approach leverages the differences in memorization strength of LVLMs on neighboring samples as implicit model fingerprints, rather than relying on specific input-output pairs as explicit triggers. This endows it with stronger stealthiness, robustness, and adaptability. To simulate real application scenarios, we conduct extensive experiments using multiple strategies and different datasets, further demonstrating its superiority in protecting LVLM ownership.

</details>

### 33. PROMPRINT: Prompt Fingerprinting via First-Token Response for LLM App Cloning Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.1052/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`system prompt`、`model copyright`、`ownership verification`、`model provenance`、`watermarking`

👤 **作者**：Jungmin Lee、Peizhuo Lv、Yeonjoon Lee

- 🎯 **研究动机**：克隆 LLM 应用复制系统提示已成现实威胁，需不暴露提示的早期可靠检测
- 🔬 **研究方法**：PROMPRINT 优化查询诱导 LLM 对特定系统提示生成特定首 token，形成独特查询-首 token 指纹对
- 📌 **结论**：四个指令 LLM 上目标 token 生成概率超 74%（其他提示下平均低于 2.2%），对部分修改与对抗指令注入鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As Large Language Model applications (LLM apps) become widespread, system prompts that determine app behavior are increasingly regarded as intellectual property, raising concerns about leakage. Recent studies show that this threat is no longer theoretical, revealing the prevalence of cloned apps replicating system prompts from others on real-world platforms. These clones pose risks of copyright infringement and malicious misuse, highlighting the need for early and reliable detection. In this paper, we propose PROMPRINT, a novel fingerprinting approach for detecting cloned LLM apps without exposing their system prompts. Motivated by the insight that different system prompts yield distinct responses to the same query, PROMPRINT optimizes queries that induce the LLM to generate a specific first token associated with the given system prompt, resulting in distinctive query–first-token pairs. Experiments on four instruction-tuned LLMs show that generated pairs effectively identify the corresponding system prompts, achieving over 74% probability of generating the target token while remaining below 2.2% on average under other prompts. Furthermore, we demonstrate that our fingerprinting remains robust to partial system prompt modifications and effective under the injection of adversarial instructions.

</details>

### 34. OpenStamp: A Watermark for Open-Source Language Models

📄 [arXiv](https://arxiv.org/abs/2608.27899) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers) · 📝 [OpenReview](https://openreview.net/forum?id=DU5eTaQSHT)　📅 2026-08

**关键词**：`defense`、`tool`、`open-source LLM`、`weight watermark`、`white-box attribution`、`weight-level watermark`

👤 **作者**：Miroojin Bakshi、Saksham Rastogi、Danish Pruthi

- 🎯 **研究动机**：基于 token 采样概率的文本水印不适配开源模型：用户白盒访问权重，可在推理时轻易关闭水印
- 🔬 **研究方法**：提出 OpenStamp，把水印逻辑直接编码进模型权重、仅修改最终 unembedding 投影层，并随代码发布 4 个流行开源模型的水印版本
- 📌 **结论**：检测性能优于先前方法且模型能力损失极小，对 paraphrase 攻击与事后微调擦除均更鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing prevalence of large language model (LLM) generated content, watermarking is considered a promising approach for attributing text to LLMs and distinguishing it from human-written content. A prominent class of techniques embeds subtle but detectable signals in generated text by modifying token sampling probabilities. However, such methods are unsuitable for open-source models, where users have white-box access and can easily disable watermarking during inference. In this work, we introduce OpenStamp, a watermarking technique that encodes the watermarking logic directly into the model weights by modifying only the final projection, or unembedding, layer. Through experiments across two models, we show that OpenStamp achieves superior detection performance, with minimal degradation in model capabilities compared to prior methods. The implanted watermark is explicitly designed, and empirically confirmed, to be more robust to paraphrasing attacks and harder to scrub off through post-hoc fine-tuning than prior open-source watermarks. To enable developers to watermark their models, we release our code alongside watermarked versions of 4 popular open-source models.

</details>

### 35. Making Models Unmergeable via Scaling-Sensitive Loss Landscape

📄 [arXiv](https://arxiv.org/abs/2601.21898) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61646)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Minwoo Jang、Hoyoung Kim、Jabin Koo、Jungseul Ok

- 🎯 **研究动机**：模型合并可把发布权重重组成绕过安全对齐与许可的混合体，现有防御事后且架构特定
- 🔬 **研究方法**：Trap^2 在微调时把保护编码进更新（适配器或全模型皆可），以权重重缩放作合并代理：独立使用有效、重缩放即退化
- 📌 **结论**：架构无关地使未授权重组失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of model hubs has made it easier to access reusable model components, making model merging a practical tool for combining capabilities. Yet, this modularity also creates a *governance gap*: downstream users can recompose released weights into unauthorized mixtures that bypass safety alignment or licensing terms. Because existing defenses are largely post-hoc and architecture-specific, they provide inconsistent protection across diverse architectures and release formats in practice. To close this gap, we propose Trap$^{2}$, an architecture-agnostic protection framework that encodes protection into updates during fine-tuning, regardless of whether they are released as adapters or full models. Instead of relying on architecture-dependent approaches, Trap$^{2}$ uses weight re-scaling as a simple proxy for the merging process. It keeps released weights effective in standalone use, but degrades them under re-scaling that often arises in merging, undermining unauthorized recomposition.

</details>

### 36. Identifying Provenance of Generative Text-to-Image Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/ha)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`model provenance`、`text-to-image model`、`model copyright`、`lineage attribution`

👤 **作者**：Anna Yoo Jeong Ha、Wenxin Ding、Stanley Wu、Shawn Shan、Haitao Zheng、Ben Y. Zhao

- 🎯 **研究动机**：微调得到的 T2I 模型与从头训练难以区分，虚报模型来源误导用户并抑制竞争
- 🔬 **研究方法**：黑盒查询下提取模型输出视觉特征，用 Jensen-Shannon 散度与基座参考池分布比对，统计假设检验判断是否微调及其父模型
- 📌 **结论**：在七个扩散模型及众多微调变体上谱系归因准确率高，图像后处理或权重扰动下仍有效，并成功溯源在线平台真实模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning provides a fast and cheap way to produce new text-to-image models that are often indistinguishable from ones trained from scratch. Unfortunately, misrepresentation of fine-tuned models creates problems for AI companies and users alike, by disincentivizing competition and misleading users on model quality and ethics of its training process. In this paper, we propose a model provenance system that identifies models produced by fine-tuning on existing text-to-image models, using only black-box query access. Our design is informed by analysis showing that one can quantify the feature space difference between text-to-image models by analyzing their responses to detailed prompts. Our system analyzes model output, extracts visual features using a generic feature extractor, and compares their distributions against those from a reference pool of base models using Jensen-Shannon divergence. Applying statistical hypothesis testing then determines if a target model is trained from scratch or fine-tuned, and if the latter, the likely base (parent) model. We evaluate our system across seven widely used diffusion models and numerous fine-tuned variants. Our results show high accuracy in attributing model lineage, even under adversarial conditions such as image post-processing or weight perturbations. Finally, we demonstrate real world efficacy of our system by tracing provenance of in-the-wild models from popular online platforms.

</details>

### 37. FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences

📄 [arXiv](https://arxiv.org/abs/2606.03330) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66274)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Gurvan Richardeau、Gohar Dashyan、Erwan Le Merrer、Gilles Tredan

- 🎯 **研究动机**：LLM 行为受实例级参数（指令提示、采样配置、量化）影响——同一权重一种配置安全另一种可能有毒；现有指纹面向 IP 保护、刻意抗这些参数变化，无法支撑针对实际部署行为的合规监管
- 🔬 **研究方法**：FLIPS 实例级指纹范式：利用生成二元伪随机序列的偏差区分同一 LLM 的不同配置
- 📌 **结论**：237 个模型实例上闭集 96%、开集 90% 识别准确率，远超适配 LLMmap 基线的 35%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Literature reveals that a Large Language Model's (LLM) behavior is not only conditioned by its original weights but also its instance-level parameters, such as instructional prompt, sampling configuration or quantization. A model that generates safe outputs under one configuration may produce toxic content under another. However, current LLM identification techniques (such as fingerprinting) focus on intellectual property protection, and their design favors robustness to changes in these instance-level parameters. This poses a critical challenge for AI regulation in which compliance assessments target actual deployed behaviors, not model provenance. In this paper, we introduce instance-level fingerprinting, a regulator-oriented paradigm that distinguishes configurations of the same LLM. Our method FLIPS, exploits biases in generated binary random sequences to reach 96% (closed-set) and 90% (open-set, where some targets are unknown) identification accuracy across 237 model instances, versus 35% for the adapted LLMmap baseline. This shows that instance-level fingerprinting is both necessary for regulation and practically feasible. Code available at https://github.com/GurvanR/FLIPS-LLM-Instance-Fingerprinting.

</details>

### 38. Fingerprinting Pre-trained Encoders under Arbitrary Downstream Fine-Tuning via Adversarial Shifting

🎓 [Official](https://icml.cc/virtual/2026/poster/61297)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`adversarial robustness`、`model copyright`、`ownership verification`、`model ownership`、`empirical evaluation`

👤 **作者**：Tianlong Xu、Wang Zixiong、Lishuai Hou、Gaoyang Liu、Chen Wang、Xiaoyi Fan

- 🎯 **研究动机**：下游微调显著改变编码器表征与标签空间，破坏既有指纹方法的标签一致性
- 🔬 **研究方法**：下游无关的 label-only 指纹：用 Adversarial Shifting 在编码器潜空间构造稳定指纹簇，利用簇固有输出一致性，不依赖具体下游任务或标签映射
- 📌 **结论**：跨多样下游任务与类别规模保持优越鲁棒性与隐蔽性，为高价值预训练编码器提供可靠 IP 保护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In the pre-training-fine-tuning paradigm, pre-trained encoders have become high-value intellectual property (IP) due to their immense training costs, necessitating robust protection. Existing fingerprinting or watermarking methods typically rely on pre-defined samples and labels, or require intrusive modifications to the training process. However, downstream fine-tuning can significantly alter an encoder's representation and label space, thereby destroying the label consistency of existing methods and rendering them ineffective. Consequently, it is both challenging and urgent to provide a downstream-agnostic, black-box ownership verification mechanism for pre-trained encoders. To address this, we propose a downstream-agnostic, label-only fingerprinting method that leverages Adversarial Shifting to construct stable fingerprint clusters in the encoder’s latent space. By exploiting the inherent output consistency of these clusters, our method remains effective regardless of the specific downstream task or label mapping. Extensive experiments demonstrate that our method maintains superior robustness and stealthiness across various downstream tasks and category scales, providing a practical and reliable IP protection scheme for high-value pre-trained encoders.

</details>

### 39. Fingerprinting LLMs via Prompt Injection

🎓 [Official](https://aclanthology.org/2026.acl-long.541/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`prompt injection`、`model copyright`、`ownership verification`、`model provenance`、`watermarking`

👤 **作者**：Yuepeng Hu、…、Neil Zhenqiang Gong

- 🎯 **研究动机**：发布后经后训练或量化的模型难以判断派生关系；现有方法或需发布前嵌入信号（对已发布模型不可行）或用手写随机提示（不抗后处理）
- 🔬 **研究方法**：LLMPrint 利用提示注入漏洞构造指纹：优化指纹提示强制一致 token 偏好，得到基座唯一且抗后处理的指纹，统一验证程序适用灰盒与黑盒并带统计保证
- 📌 **结论**：五个基座与约 700 个后训练或量化变体上高真阳性、近零假阳性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are often modified after release through post-processing such as post-training or quantization, which makes it challenging to determine whether one model is derived from another. Existing provenance detection methods have two main limitations: (1) they embed signals into the base model before release, which is infeasible for already published models, or (2) they compare outputs across models using hand-crafted or random prompts, which are not robust to post-processing. In this work, we propose LLMPrint, a novel detection framework that constructs fingerprints by exploiting LLMs’ inherent vulnerability to prompt injection. Our key insight is that by optimizing fingerprint prompts to enforce consistent token preferences, we can obtain fingerprints that are both unique to the base model and robust to post-processing. We further develop a unified verification procedure that applies to both gray-box and black-box settings, with statistical guarantees. We evaluate LLMPrint on five base models and around 700 post-trained or quantized variants. Our results show that LLMPrint achieves high true positive rates while keeping false positive rates near zero. The code is publicly available at https://github.com/hifi-hyp/ACL-LLMPrint.

</details>

### 40. Every Step Counts: Decoding Trajectories as Authorship Fingerprints of dLLMs

📄 [arXiv](https://arxiv.org/abs/2510.05148) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61561)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`diffusion model`

👤 **作者**：Qi Li、Runpeng Yu、Haiquan Lu、Xinchao Wang

- 🎯 **研究动机**：dLLM 的解码轨迹可用于模型归因，但逐步置信度因双向解码的 token 互扰高度冗余、掩盖结构信息
- 🔬 **研究方法**：Directed Decoding Map 捕捉解码步骤间结构关系，Gaussian-Trajectory Attribution 在每个解码位置为各模型拟合逐格高斯分布并以轨迹对数似然差做归因分数
- 📌 **结论**：跨模型、数据集与访问假设验证有效，可区分不同模型乃至同模型不同 checkpoint

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Discrete Diffusion Large Language Models (dLLMs) have recently emerged as a promising non-autoregressive paradigm, offering faster inference while achieving strong performance in code generation and mathematical reasoning tasks. In this work, we show that dLLMs’ decoding mechanism not only improves utility but also enables effective model attribution: by analyzing a response’s decoding trajectory, we can identify its source model and help mitigate risks from model misuse. A key challenge is the diversity of attribution scenarios, ranging from distinguishing different models to identifying different checkpoints or backups of the same model. To ensure broad applicability, we focus on two core questions: what information to extract from the decoding trajectory, and how to use it effectively. We first observe that per-step model confidence is ineffective, as the bidirectional nature of dLLMs causes mutual influence among decoded tokens, leading to highly redundant confidence signals that obscure structural information about decoding order and dependencies. To overcome this, we propose a novel information extraction scheme called the \textit{Directed Decoding Map (DDM)}, which captures structural relationships between decoding steps and reveals model-specific behaviors. Furthermore, to fully leverage the extracted structure, we propose \textit{Gaussian-Trajectory Attribution (GTA)}, which fits a cell-wise Gaussian distribution at each decoding position for each model and uses log-likelihood differences between trajectories as the attribution score. Extensive experiments across diverse models, datasets and different model access assumptions validate the effectiveness of our approach.

</details>

### 41. CircuitPrint: Mechanistic Circuit Fingerprints for Large Language Models

🎓 [Official](https://icml.cc/virtual/2026/poster/61258)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`mechanistic analysis`、`model copyright`、`ownership verification`、`model ownership`、`copyright protection`

👤 **作者**：Zhenxiong Yan、Suhang Yao、Yu Liu、Wenqiang Jin

- 🎯 **研究动机**：LLM IP 验证依赖损害效用的侵入式水印或易被微调与合并破坏的表层行为签名
- 🔬 **研究方法**：CircuitPrint 利用跨模型衍生品稳定的内部计算回路做非侵入指纹：识别因果产生特定预测的机制性超节点，合成触发查询复现其内部抑制以诱导可观测输出偏移
- 📌 **结论**：大幅超越现有基线，在激进微调与模型合并下保持鲁棒，不改参数即化解效用与保护的权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are trained at significant computational and data cost, making them valuable intellectual property (IP). Existing IP verification methods primarily rely either on invasive watermarking that degrades model utility, or on superficial behavioral signatures disrupted by fine-tuning and model merging. This apparent trade-off between model utility and IP protection has constrained practical deployment. We challenge this trade-off and propose CircuitPrint, a non-invasive IP fingerprinting framework that enables robust verification through standard model queries by leveraging stable internal computational circuits of LLMs. We show that these circuits function as a persistent computational backbone across model derivatives, allowing them to serve as stable fingerprints for distinguishing LLMs. Building on this stability, CircuitPrint constructs IP signatures by identifying mechanistically essential supernodes that causally produce specific predictions within these circuits. Specifically, trigger queries are synthesized to replicate the internal suppression of these supernodes, thereby inducing distinctive and observable output shifts. Experimental results demonstrate that CircuitPrint substantially outperforms existing baselines while remaining robust under aggressive fine-tuning and model merging, effectively resolving this trade-off without altering model parameters.

</details>

### 42. Cert-LAS: Toward Certified Model Ownership Verification for Text-to-Image Diffusion Models via Layer-Adaptive Smoothing

📄 [arXiv](https://arxiv.org/abs/2605.29809) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64693)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`ownership verification`、`certified watermark`、`layer-adaptive smoothing`、`model ownership`、`certified robustness`

👤 **作者**：Leyi Qi、Yiming Li、Siyuan Liang、Zhengzhong Tu、Dacheng Tao

- 🎯 **研究动机**：现有后门水印隐式假设验证过程忠实，对手可破坏水印信号使验证失效
- 🔬 **研究方法**：Cert-LAS 首个认证式 T2I 所有权验证：扩散分类器与 LFS 引导的层自适应噪声嵌入水印，经假设检验对比无水印参照，并证明恶意移除攻击下仍可可靠验证
- 📌 **结论**：实验验证有效并抵抗自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large-scale text-to-image (T2I) diffusion models have enabled unprecedented creative applications, but their unauthorized use has raised serious intellectual property concerns, making model ownership verification (MOV) increasingly critical. We find that existing backdoor-based diffusion watermarking methods often (implicitly) assume a "faithful" verification process, namely, that the verifier can query a suspicious model and obtain the faithful watermark response to complete MOV. However, in practice, adversaries may intentionally or unintentionally damage potential watermark signals, significantly degrading verification reliability. To address this issue, we propose Cert-LAS, the first certified MOV method for T2I models based on layer-adaptive smoothing. In general, Cert-LAS embeds specified watermarks using diffusion classifiers and an LFS-guided layer-adaptive noise, and verifies ownership by examining whether the suspected model exhibits significantly stronger watermark responses compared to unwatermarked references through hypothesis testing. We further prove that, under certain conditions, our Cert-LAS can still achieve reliable verification even in the presence of malicious removal attacks. Extensive experiments validate the effectiveness of Cert-LAS and its resistance to adaptive attacks. Our code is available at https://github.com/Leyi-Qi/Cert-LAS.

</details>

### 43. AgentMark: Utility-Preserving Behavioral Watermarking for Agents

🎓 [Official](https://aclanthology.org/2026.acl-long.573/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`agent safety`、`watermarking`、`content watermark`、`model provenance`

👤 **作者**：Kaibo Huang、…、Linna Zhou

- 🎯 **研究动机**：内容水印无法标识 agent 高层规划行为（工具与子目标选择）；规划层水印的分布偏移会在长程执行中复合损害效用，且 agent 常为黑盒
- 🔬 **研究方法**：AgentMark 从 agent 引出显式行为分布并做分布保持条件采样，把多比特标识嵌入规划决策，兼容黑盒 API 与动作层内容水印
- 📌 **结论**：在具身、工具使用与社交环境中实现实用多比特容量、部分日志下的鲁棒恢复与效用保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based agents are increasingly deployed to autonomously solve complex tasks, raising urgent needs for IP protection and regulatory provenance. While content watermarking effectively attributes LLM-generated outputs, it fails to directly identify the high-level planning behaviors (e.g., tool and subgoal choices) that govern multi-step execution. Critically, watermarking at the planning-behavior layer faces unique challenges: minor distributional deviations in decision-making can compound during long-term agent operation, degrading utility, and many agents operate as black boxes that are difficult to intervene in directly. To bridge this gap, we propose AgentMark, a behavioral watermarking framework that embeds multi-bit identifiers into planning decisions while preserving utility. It operates by eliciting an explicit behavior distribution from the agent and applying distribution-preserving conditional sampling, enabling deployment under black-box APIs while remaining compatible with action-layer content watermarking. Experiments across embodied, tool-use, and social environments demonstrate practical multi-bit capacity, robust recovery from partial logs, and utility preservation. Code is available at https://github.com/Tooooa/AgentMark.

</details>

### 44. Defending Unauthorized Model Merging via Dual-Stage Weight Protection

📄 [arXiv](https://arxiv.org/abs/2511.11851) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Defending_Unauthorized_Model_Merging_via_Dual-Stage_Weight_Protection_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`defense`、`model merging`、`weight protection`、`intellectual property`

👤 **作者**：Wei-Jia Chen、Min-Yen Tsai、Cheng-Yi Lee、Chia-Mu Yu

- 🎯 **研究动机**：开源模型可被自由合并为多能力模型，侵犯知识产权并破坏所有权与问责
- 🔬 **研究方法**：MergeGuard 双阶段权重保护：先以 L2 正则优化把任务相关信息跨层分散，再注入结构扰动错位任务子空间，使合并模型陷入破坏性干涉而受保护模型正常
- 📌 **结论**：在 ViT-L-14 与 Llama2、Gemma2、Mistral 上把合并模型准确率最多降低 90%，受保护模型损失小于 1.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid proliferation of pretrained models and open repositories has made model merging a convenient yet risky practice, allowing free-riders to combine fine-tuned models into a new multi-capability model without authorization. Such unauthorized model merging not only violates intellectual property rights but also undermines model ownership and accountability. To address this issue, we present MergeGuard, a proactive dual-stage weight protection framework that disrupts merging compatibility while maintaining task fidelity. In the first stage, we redistribute task-relevant information across layers via L2-regularized optimization, ensuring that important gradients are evenly dispersed. In the second stage, we inject structured perturbations to misalign task subspaces, breaking curvature compatibility in the loss landscape. Together, these stages reshape the model's parameter geometry such that merged models collapse into destructive interference while the protected model remains fully functional. Extensive experiments on both vision (ViT-L-14) and language (Llama2, Gemma2, Mistral) models demonstrate that MergeGuard reduces merged model accuracy by up to 90% with less than 1.5% performance loss on the protected model.

</details>

### 45. Attacks on Machine-Text Detectors Retain Stylistic Fingerprints

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

### 46. MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2608.17722)　📅 2026-08

**关键词**：`detection`、`membership inference`、`VLM safety`、`data poisoning`、`audit tool`、`protective poisoning`

👤 **作者**：Xukun Luan、…、Di Wang

- 🎯 **研究动机**：VLM 训练数据持有者需检测数据是否被未授权使用，成员推理审计性能有待放大
- 🔬 **研究方法**：MemCatalyst 数据投毒工具（Poisoning Text/Image）：迫使 VLM 过学图像特征与文本语义的特定不一致以提高成员审计敏感性，投毒样本跨架构可迁移
- 📌 **结论**：五种 SOTA 审计、两个 VLM 上以极少投毒预算显著提升 MI AUC，对模型性能影响可忽略

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language models (VLMs) achieve outstanding performance largely due to the amount of training data available on the internet. At the same time, data holders (e.g., artists) urgently need to determine whether their data has been used for model training without authorization, which concerns both intellectual property rights and personal privacy. Data auditing, particularly through membership inference (MI), has attracted attention as a direct tool. This work proposes MemCatalyst, a set of data poisoning tools, aiming to amplify the data auditing performance on VLMs. MemCatalyst employs two strategies: Poisoning Text (PT) and Poisoning Image (PI). MemCatalyst forces VLMs to over-learn specific inconsistencies between image features and textual semantics during training, thereby increasing their susceptibility to membership information auditing. Crucially, the transferability of poisoned samples across different VLM architectures is demonstrated to be effective in the black-box setting. Extensive evaluations using five state-of-the-art data audits on two prominent VLMs demonstrate that MemCatalyst markedly enhances MI AUC scores with a minimal budget of poisoned samples, while maintaining a negligible impact on model performance.

</details>

### 47. Auditing Data Provenance in LLM Fine-tuning via Intrinsic Distributional Fingerprints

📄 [arXiv](https://arxiv.org/abs/2608.02154) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-08　🏷 ACM CCS 2026

**关键词**：`detection`、`data provenance`、`distributional fingerprint`、`model copyright`、`black-box audit`

👤 **作者**：Zirui Huang、Yunlong Mao、Wei Tong、Tingting Wu、Xin Ge、Sheng Zhong

- 🎯 **研究动机**：LLM 微调数据 IP 侵权审计需在数据准备或训练时干预，且在改写与知识蒸馏等恶意混淆下脆弱
- 🔬 **研究方法**：DPA 后验黑盒审计框架：把效用约束下必然保留的语义-词法交集捕获为固有分布指纹，形式化为统计假设检验并用无偏输出采样量化
- 📌 **结论**：医疗与法律微调任务上一致优于基线并对改写、蒸馏规避鲁棒；同一高保真指纹也可被滥用于隐私攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of customized Large Language Models (LLMs) poses critical risks of Data Intellectual Property (Data IP) infringement via unauthorized fine-tuning on proprietary data. Existing audit techniques are limited, as they require intervention during data preparation or training and remain fragile under malicious obfuscations such as data paraphrasing and knowledge distillation. We propose \textit{Distribution Provenance Audit (DPA)}, a post-hoc framework for auditing data IP infringement in LLM fine-tuning under black-box and malicious settings. DPA is grounded in a critical insight: regardless of fine-tuning tactics to evade provenance, the practical necessity of maintaining utility constrains the model to preserve the fundamental intersection of semantic substance and lexical form. Accordingly, DPA captures this persistent lexical-semantic intersection as intrinsic distributional fingerprints. The framework formulates the audit as a statistical hypothesis test, effectively quantifying these fingerprints via unbiased output sampling to reliably reject the null hypothesis of non-usage. Extensive experiments on medical and legal fine-tuning tasks show that DPA consistently outperforms existing baselines, remaining robust against adversarial trainers employing paraphrasing and knowledge distillation. We further highlight a fundamental dual-use tension: the same high-fidelity distributional fingerprints enabling reliable auditing may also facilitate privacy attacks.

</details>

### 48. Permissive-Washing in the Open AI Supply Chain: A Large-Scale Audit of License Integrity

📄 [arXiv](https://arxiv.org/abs/2602.08816) · 🌐 [Project](https://doi.org/10.1145/3770855.3818130)　📅 2026-02　🏷 KDD 2026

**关键词**：`analysis`、`AI supply chain`、`license integrity`、`provenance`、`audit`

👤 **作者**：James Jewitt、Gopi Krishnan Rajbahadur、Hao Li、Bram Adams、Ahmed E. Hassan

- 🎯 **研究动机**：MIT 等宽松许可证的法定要求（许可证文本、版权声明、上游署名）在 AI 供应链中未被大规模验证
- 🔬 **研究方法**：审计 Hugging Face 与 GitHub 上 124,278 条 dataset-model-application 供应链，覆盖 3,338 数据集、6,664 模型与 28,516 应用
- 📌 **结论**：96.5% 数据集与 95.8% 模型缺失许可证文本，仅 2.3%/3.2% 完全合规，下游合规署名保留率低至 5.75%-27.59%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Permissive licenses like MIT, Apache-2.0, and BSD-3-Clause dominate open-source AI, signaling that artifacts like models, datasets, and code can be freely used, modified, and redistributed. However, these licenses carry mandatory requirements: include the full license text, provide a copyright notice, and preserve upstream attribution, that remain unverified at scale. Failure to meet these conditions can place reuse outside the scope of the license, effectively leaving AI artifacts under default copyright for those uses and exposing downstream users to litigation. We call this phenomenon ``permissive washing'': labeling AI artifacts as free to use, while omitting the legal documentation required to make that label actionable. To assess how widespread permissive washing is in the AI supply chain, we empirically audit 124,278 dataset $\rightarrow$ model $\rightarrow$ application supply chains, spanning 3,338 datasets, 6,664 models, and 28,516 applications across Hugging Face and GitHub. We find that an astonishing 96.5\% of datasets and 95.8\% of models lack the required license text, only 2.3\% of datasets and 3.2\% of models satisfy both license text and copyright requirements, and even when upstream artifacts provide complete licensing evidence, attribution rarely propagates downstream: only 27.59\% of models preserve compliant dataset notices and only 5.75\% of applications preserve compliant model notices (with just 6.38\% preserving any linked upstream notice). Practitioners cannot assume permissive labels confer the rights they claim: license files and notices, not metadata, are the source of legal truth. To support future research, we release our full audit dataset and reproducible pipeline.

</details>

### 49. RECOVER: Reliable Detection of Unauthorized Data Usage in Text-to-Image Diffusion Models via Inversion Robustness

🎓 [Official](https://icml.cc/virtual/2026/poster/65032)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`diffusion model`、`adversarial robustness`、`model copyright`、`model ownership`、`copyright protection`

👤 **作者**：Yanhao Wei、Xiaokang Zhao、Boheng Li、Yang Zhang、Run Wang

- 🎯 **研究动机**：T2I 扩散模型微调可能使用未授权数据，现有版权认证需侵入式修改图像或依赖微调前模型
- 🔬 **研究方法**：提出 RECOVER：利用可疑模型对微调图像在噪声扰动下仍能稳定重建的逆变换鲁棒性，非侵入且无需微调前模型即可判定数据是否被使用
- 📌 **结论**：在广泛场景下有效检测未授权数据使用，一致优于现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Text-to-Image diffusion models have achieved remarkable success in image generation and are increasingly fine-tuned for personalized use cases. However, many personalized models may incorporate unauthorized data during the fine-tuning process, raising growing concerns about potential copyright infringements. Existing methods either require intrusive modifications to the images to be protected, which not only fail to safeguard previously released images but may also degrade image quality, or rely on the availability of the pre-fine-tuned model, thereby limiting their applicability. To bridge this gap, in this paper, we propose the first non-intrusive copyright authentication framework without pre-fine-tuned model. We reveal that if a model is fine-tuned on a specific image, it learns the denoising trajectory of that image across varying noise levels, allowing it to stably reconstruct the image even under noise perturbations. Motivated by this insight, we propose Reliable dEteCtion Of unauthorized data usage via inVErsion Robustness (RECOVER), an effective non-intrusive detection method without pre-fine-tuned model. Unlike existing methods that rely on external watermarks or discrepancies between the suspect and pre-fine-tuned models, RECOVER directly leverages the robustness observed during the inversion–reconstruction process of the suspect model to determine whether an image was used for fine-tuning. Extensive experiments demonstrate that RECOVER is effective across a wide range of scenarios, consistently outperforming existing methods. Our code is publicly available here.

</details>

### 50. PDR: A Plug-and-Play Positional Decay Framework for LLM Pre-training Data Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.562/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`model copyright`、`ownership verification`、`model provenance`、`watermarking`

👤 **作者**：Jinhan Liu、…、Dandan Guo

- 🎯 **研究动机**：黑盒零样本预训练数据检测中似然法均匀聚合 token 分数，忽略自回归生成的信息动态
- 🔬 **研究方法**：验证记忆信号强烈偏向高熵初始 token 并随上下文累积而衰减；PDR 免训练即插即用地重加权 token 分数，放大早期信号抑制后期噪声
- 📌 **结论**：作为稳健先验在多基准上普遍增强多种先进检测方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting pre-training data in Large Language Models (LLMs) is crucial for auditing data privacy and copyright compliance, yet it remains challenging in black-box, zero-shot settings where computational resources and training data are scarce. While existing likelihood-based methods have shown promise, they typically aggregate token-level scores using uniform weights, thereby neglecting the inherent information-theoretic dynamics of autoregressive generation. In this paper, we hypothesize and empirically validate that memorization signals are heavily skewed towards the high-entropy initial tokens, where model uncertainty is highest, and decay as context accumulates. To leverage this linguistic property, we introduce Positional Decay Reweighting (PDR), a training-free and plug-and-play framework. PDR explicitly reweights token-level scores to amplify distinct signals from early positions while suppressing noise from later ones. Extensive experiments show that PDR acts as a robust prior and can usually enhance a wide range of advanced methods across multiple benchmarks.

</details>

### 51. Gap-K%: Measuring Top-1 Prediction Gap for Detecting Pretraining Data

🎓 [Official](https://aclanthology.org/2026.acl-long.1072/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`model copyright`、`ownership verification`、`model provenance`、`watermarking`

👤 **作者**：Minseo Kwak、Jaehyung Kim

- 🎯 **研究动机**：预训练数据检测依赖 token 似然，忽略 top-1 预测与目标 token 的差距及相邻 token 局部相关
- 🔬 **研究方法**：Gap-K% 基于 top-1 预测与目标 token 的对数概率差加滑动窗口，源于预训练梯度惩罚的优化动力学观察
- 📌 **结论**：在 WikiMIA 与 MIMIR 上 SOTA，跨模型规模与输入长度稳定超越基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The opacity of massive pretraining corpora in Large Language Models (LLMs) raises significant privacy and copyright concerns, making pretraining data detection a critical challenge.Existing state-of-the-art methods typically rely on token likelihoods, yet they often overlook the gap between the target token and the model’s top-1 prediction, as well as local correlations between adjacent tokens.In this work, we propose Gap-K%, a novel pretraining data detection method grounded in the optimization dynamics of LLM pretraining. By analyzing the next-token prediction objective, we observe that discrepancies between the model’s top-1 prediction and the target token induce strong gradient signals, which are explicitly penalized during training.Motivated by this, Gap-K% leverages the log probability gap between the top-1 predicted token and the target token, incorporating a sliding window strategy to capture local correlations and mitigate token-level fluctuations. Extensive experiments on the WikiMIA and MIMIR benchmarks demonstrate that Gap-K% achieves state-of-the-art performance, consistently outperforming prior baselines across various model sizes and input lengths.

</details>

### 52. Data Provenance Auditing of Fine-Tuned Large Language Models with a Text-Preserving Technique

📄 [arXiv](https://arxiv.org/abs/2510.09655) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66491)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`benchmark`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`

👤 **作者**：Yanming Li、Cédric Eichler、Nicolas Anciaux、Alexandra Bensamoun、Lorena Gonzalez Manzano、Seifeddine Ghozzi

- 🎯 **研究动机**：检测敏感或版权文本是否被用于微调 LLM，需要黑盒访问下带统计保证的方法
- 🔬 **研究方法**：用不可见 Unicode 字符构建 cue-reply 对数字标记，审计时仅用 cue 片段提示触发 reply 复现，并与留出反事实标记做排序检验控制假阳性
- 📌 **结论**：仅 40 篇（4%）水印文档即得 96.7% 真阳性率与 0% 假阳性率，每文档回复复现率超 28%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a system for marking sensitive or copyrighted texts to detect their use in fine-tuning large language models under black-box access with statistical guarantees. Our method builds digital “marks” using invisible Unicode characters organized into (“cue”, “reply”) pairs. During an audit, prompts containing only “cue” fragments are issued to trigger regurgitation of the corresponding “reply”, indicating document usage. To control false positives, we compare against held-out counterfactual marks and apply a ranking test, yielding a verifiable bound on the false positive rate. Empirically, we obtain a true positive rate of 96.7\% at 0\% false positive rate and reply regurgitation rates exceeding 28\% per document with only 40 (4\%) watermarked documents. The approach is minimally invasive, scalable across many sources, robust to standard processing pipelines, and achieves high detection power even when marked data is a small fraction of the fine-tuning corpus.

</details>

### 53. Bypassing Copyright Protection in Diffusion-based Customization via Two-Stage Latent Feature Optimization

📄 [arXiv](https://arxiv.org/abs/2606.09909) · 🌐 [Project](https://doi.org/10.1145/3770855.3817760)　📅 2026-06　🏷 KDD 2026

**关键词**：`attack`、`copyright protection`、`diffusion customization`、`latent optimization`

👤 **作者**：Ziang Xu、…、Zhiyong Wu

- 🎯 **研究动机**：扩散定制模型的版权保护防御在潜空间注入持久扰动，可被自适应攻击绕过
- 🔬 **研究方法**：提出 TS-LFO 两阶段攻击：潜去噪阶段用对齐损失+扩散损失（时间步加权）抑制防御高频噪声，潜重建阶段用像素约束恢复低频语义，修复被破坏的图像-潜映射
- 📌 **结论**：持续绕过 SOTA 版权防御，优于 DiffPure、GrIDPure、IMPRESS 等攻击，证明此类防御并非可靠防线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing concerns over copyright infringement in diffusion-based customization, adversarial attacks have emerged as a prominent defense strategy to prevent malicious content forgery in personalized image generation. However, current defenses typically introduce persistent perturbations in the latent space of Latent Diffusion Models (LDMs), which remain susceptible to adaptive bypasses by adversaries. In this paper, we introduce Two-Stage Latent Feature Optimization (TS-LFO), an efficient and effective copyright-stealing attack against protected diffusion-based customization. We begin by observing that existing defenses primarily disrupt the mapping between input images and their latent representations, thereby degrading the model's ability to produce personalized outputs. To counteract this, TS-LFO restores the broken mapping through a two-stage optimization process. In the Latent Denoising Stage, we enhance semantic consistency between latent codes and input images by jointly minimizing a Latent-Image Alignment Loss and a Latent Diffusion Loss with timestep-dependent weights, effectively suppressing the high-frequency noise introduced by defenses. In the Latent Reconstruction Stage, we recover low-frequency semantic information using pixel-level constraints to refine the latent features. Extensive experiments show that TS-LFO consistently bypasses state-of-the-art (SOTA) copyright defenses and outperforms SOTA copyright attacks such as DiffPure, GrIDPure and IMPRESS across diverse settings.

</details>

### 54. Alignment Whack-a-Mole : Finetuning Activates Verbatim Recall of Copyrighted Books in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.20957) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`attack`、`system prompt`、`model copyright`、`ownership verification`、`verbatim extraction`、`fine-tuning bypass`

👤 **作者**：Xinyue Liu、Niloofar Mireshghallah、Jane C. Ginsburg、Tuhin Chakrabarty

- 🎯 **研究动机**：厂商以 RLHF、系统提示与输出过滤阻止版权文本复现作为法律抗辩，微调能否绕过未知
- 🔬 **研究方法**：微调模型把情节摘要扩写为全文（商业写作助手的自然任务），仅以语义描述为提示、不用任何原文
- 📌 **结论**：GPT-4o、Gemini-2.5-Pro、DeepSeek-V3.1 复现 85-90% 的留出版权书、单段逐字超 460 词；仅用村上春树作品微调即可解锁 30+ 无关作者，三家模型记忆区域相关 r≥0.90

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier LLM companies have repeatedly assured courts and regulators that their models do not store copies of training data. They further rely on safety alignment strategies via RLHF, system prompts, and output filters to block verbatim regurgitation of copyrighted works, and have cited the efficacy of these measures in their legal defenses against copyright infringement claims. We show that finetuning bypasses these protections: by training models to expand plot summaries into full text, a task naturally suited for commercial writing assistants, we cause GPT-4o, Gemini-2.5-Pro, and DeepSeek-V3.1 to reproduce up to 85-90% of held-out copyrighted books, with single verbatim spans exceeding 460 words, using only semantic descriptions as prompts and no actual book text. This extraction generalizes across authors: finetuning exclusively on Haruki Murakami's novels unlocks verbatim recall of copyrighted books from over 30 unrelated authors. The effect is not specific to any training author or corpus: random author pairs and public-domain finetuning data produce comparable extraction, while finetuning on synthetic text yields near-zero extraction, indicating that finetuning on individual authors' works reactivates latent memorization from pretraining. Three models from different providers memorize the same books in the same regions ($r \ge 0.90$), pointing to an industry-wide vulnerability. Our findings offer compelling evidence that model weights store copies of copyrighted works and that the security failures that manifest after finetuning on individual authors' works undermine a key premise of recent fair use rulings, where courts have conditioned favorable outcomes on the adequacy of measures preventing reproduction of protected expression.

</details>

### 55. SEW: Strengthening Robustness of Black-box DNN Watermarking via Specificity Enhancement

📄 [arXiv](https://arxiv.org/abs/2602.03377) · 🌐 [Project](https://doi.org/10.1145/3770854.3780272)　📅 2026-02　🏷 KDD 2026

**关键词**：`defense`、`DNN watermark`、`specificity`、`removal resistance`

👤 **作者**：Huming Qiu、Mi Zhang、Junjie Sun、Peiyi Chen、Xiaohan Zhang、Min Yang

- 🎯 **研究动机**：DNN 泛化使黑盒水印提取密钥不唯一，攻击者可逆向近似替换密钥进而移除水印
- 🔬 **研究方法**：定义水印对密钥响应精确性的 specificity，SEW 通过降低水印与近似密钥的关联增强特异性
- 📌 **结论**：三个基准上验证增强特异性显著提升抗移除鲁棒性，抵御六种 SOTA 移除攻击且保持模型可用性与验证性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To ensure the responsible distribution and use of open-source deep neural networks (DNNs), DNN watermarking has become a crucial technique to trace and verify unauthorized model replication or misuse. In practice, black-box watermarks manifest as specific predictive behaviors for specially crafted samples. However, due to the generalization nature of DNNs, the keys to extracting the watermark message are not unique, which would provide attackers with more opportunities. Advanced attack techniques can reverse-engineer approximate replacements for the original watermark keys, enabling subsequent watermark removal. In this paper, we explore black-box DNN watermarking specificity, which refers to the accuracy of a watermark's response to a key. Using this concept, we introduce Specificity-Enhanced Watermarking (SEW), a new method that improves specificity by reducing the association between the watermark and approximate keys. Through extensive evaluation using three popular watermarking benchmarks, we validate that enhancing specificity significantly contributes to strengthening robustness against removal attacks. SEW effectively defends against six state-of-the-art removal attacks, while maintaining model usability and watermark verification performance.

</details>

### 56. Neural Honeytrace: Plug&Play Watermarking Framework against Model Extraction Attacks

📄 [arXiv](https://arxiv.org/abs/2501.09328) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61931)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`AI watermarking`、`content watermark`、`model copyright`、`mechanistic analysis`、`robust detection`

👤 **作者**：Yixiao Xu、…、Zhihong Tian

- 🎯 **研究动机**：现有可触发水印需额外训练限制部署后灵活性，且缺理论基础易受自适应攻击
- 🔬 **研究方法**：Neural Honeytrace 免重训练即插即用：从信息视角重定义水印传输，利用后门学习长尾效应设计免训练多步传输策略
- 📌 **结论**：最坏情况 t 检验所有权验证的平均查询量降至现有方法的 2%，零训练成本

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Triggerable watermarking enables model owners to assert ownership against model extraction attacks. However, most existing approaches require additional training, which limits post-deployment flexibility, and the lack of clear theoretical foundations makes them vulnerable to adaptive attacks. In this paper, we propose Neural Honeytrace, a plug-and-play watermarking framework that operates without retraining. We redefine the watermark transmission mechanism from an information perspective, designing a training-free multi-step transmission strategy that leverages the long-tailed effect of backdoor learning to achieve efficient and robust watermark embedding. Extensive experiments demonstrate that Neural Honeytrace reduces the average number of queries required for a worst-case t-test-based ownership verification to as low as 2% of existing methods, while incurring zero training cost.

</details>

### 57. Are Robust LLM Fingerprints Adversarially Robust?

📄 [arXiv](https://arxiv.org/abs/2509.26598) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`LLM fingerprint`、`ownership verification`、`adaptive evasion`

👤 **作者**：Anshul Nasery、Edoardo Contente、Alkin Kaz、Pramod Viswanath、Sewoong Oh

- 🎯 **研究动机**：鲁棒LLM指纹能否抵抗自适应规避未经检验
- 🔬 **研究方法**：对现有鲁棒指纹发起自适应evasion攻击评估其稳定性
- 📌 **结论**：自适应攻击下指纹仍可被规避，所有权验证存在风险

### 58. Extracting memorized pieces of (copyrighted) books from open-weight language models

📄 [arXiv](https://arxiv.org/abs/2505.12546) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-05

**关键词**：`attack`、`open-weight LLM`、`model copyright`、`ownership verification`、`training-data extraction`、`copyright memorization`

👤 **作者**：A. Feder Cooper、…、Percy Liang

- 🎯 **研究动机**：版权诉讼双方对 LLM 记忆书籍程度的说法两极化，缺乏系统测量
- 🔬 **研究方法**：开发书籍记忆度测量技术，对 200 本书与 14 个开源 LLM 做超 3000 次提取实验
- 📌 **结论**：多数 LLM 不记忆多数书籍，但 Llama 3.1 70B 完整记忆哈利波特首部，以开头几词即可近乎逐字提取全书

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Plaintiffs and defendants in copyright lawsuits over generative AI often make sweeping, opposing claims about the extent to which large language models (LLMs) memorize protected expression from books in their training data. We show that these polarized positions dramatically oversimplify the relationship between memorization and copyright. To do so, we develop a technique to measure memorization of books, which we apply to 200 books and 14 open-weight LLMs. Through over 3000 experiments, we show that memorization varies both by model and book. With respect to our specific extraction methodology, we find that most LLMs do not memorize most books -- either in whole or in part; however, there are notable exceptions. For instance, Llama 3.1 70B entirely memorizes some books, like Harry Potter and the Sorcerer's Stone; memorization is so extensive that one can deterministically extract the whole book almost verbatim using the book's first few words as an initial prompt. We discuss why our results have significant implications for copyright cases, though not ones that unambiguously favor either side.

</details>

### 59. MASLeak: Investigating and Exposing Intellectual Property Leakage Vulnerabilities in Multi-Agent Systems

📄 [arXiv](https://arxiv.org/abs/2505.12442) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-liwen)　📅 2025-05　🏷 USENIX Security 2026

**关键词**：`attack`、`multi-agent system`、`IP leakage`、`model copyright`、`black-box extraction`

👤 **作者**：Liwen Wang、…、Shing-Chi Cheung

- 🎯 **研究动机**：多智能体系统架构与交互复杂，其知识产权泄露风险未被量化
- 🔬 **研究方法**：提出 MASLeak，仅经公共 API 提交构造查询，蠕虫式诱出并保留各 agent 响应，提取 agent 数量、拓扑、系统提示等组件
- 📌 **结论**：810 个合成应用上系统提示与任务指令提取成功率 87%、架构 92%，Coze 与 CrewAI 真实应用亦验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Large Language Models (LLMs) has led to the emergence of Multi-Agent Systems (MAS) to perform complex tasks through collaboration. However, the intricate nature of MAS, including their architecture and agent interactions, raises significant concerns regarding intellectual property (IP) protection. In this paper, we introduce MASLEAK, a novel attack framework designed to extract sensitive information from MAS applications. MASLEAK targets a practical, black-box setting, where the adversary has no prior knowledge of the MAS architecture or agent configurations. The adversary can only interact with the MAS through its public API, submitting attack query $q$ and observing outputs from the final agent. Inspired by how computer worms propagate and infect vulnerable network hosts, MASLEAK carefully crafts adversarial query $q$ to elicit, propagate, and retain responses from each MAS agent that reveal a full set of proprietary components, including the number of agents, system topology, system prompts, task instructions, and tool usages. We construct the first synthetic dataset of MAS applications with 810 applications and also evaluate MASLEAK against real-world MAS applications, including Coze and CrewAI. MASLEAK achieves high accuracy in extracting MAS IP, with an average attack success rate of 87% for system prompts and task instructions, and 92% for system architecture in most cases. We conclude by discussing the implications of our findings and the potential defenses.

</details>

### 60. DIPBox: A Multi-scale Testing Framework for Tracking Dataset Regeneration

📄 [arXiv](https://arxiv.org/abs/2606.21240) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-06　🏷 ACM CCS 2026

**关键词**：`benchmark`、`detection`、`dataset regeneration`、`model copyright`、`ownership verification`、`multi-scale similarity`

👤 **作者**：Tian Dong、…、Hao Chen

- 🎯 **研究动机**：训练数据集面临再生式复制威胁，已有防御只追踪单数据点，对未知对抗性再生无能为力
- 🔬 **研究方法**：基于保效用再生必然保留多尺度信号的洞察，设计样本级/集合级/分布级特征与四种相似度度量，构建 DIPBox 多尺度相似度测试框架并给出学习论分析与效用-散度权衡
- 📌 **结论**：16 个视觉/文本数据集、320 个再生数据集、590 个派生模型上优于已有方案，并在三种自适应攻击下刻画鲁棒性与极限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training datasets have tremendous proprietary value and are vulnerable to unauthorized copying. Existing defenses mainly focus on tracking individual data points, but pay little attention to the threat of dataset regeneration. Through a measurement study of public tumor datasets, we identify substantial real-world partial-dataset replication, raising concerns about potential license noncompliance. To counter the challenge of tracking previously unknown adversarial regeneration, our key insight is that regeneration that preserves model utility inevitably preserves measurable signals across multiple feature scales. We categorize these dataset features into sample-, set-, and distribution-level features and design four similarity metrics to accurately identify regeneration. Based on these metrics, we develop DIPBox, which to our knowledge is the first testing framework that tracks regeneration suspects via multi-scale similarity testing across a spectrum of defender access settings, from limited to full information. We further provide a learning-theoretic analysis that justifies these multi-scale metrics and formalizes an inherent utility--divergence trade-off, implying fundamental limits on evasive regeneration. Extensive experiments on 16 vision and text base datasets, 320 regenerated datasets, and 590 derived models validate that DIPBox outperforms previous solutions while characterizing its robustness and limits under three adaptive attacks.

</details>

### 61. DataGuard: A Non-intrusive Dataset Auditing Framework via Differential Information Forensics

🎓 [Official](https://icml.cc/virtual/2026/poster/60636)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Jiadong Lou、Wenxin Rong、Li Chen、Xing Gao、Rui Zhang、Xu Yuan

- 🎯 **研究动机**：现有侵入式数据集审计需修改数据集，危及模型性能与安全
- 🔬 **研究方法**：DataGuard 非侵入框架：目标与辅助非训练数据集差分比较、信息取证分析建立区分训练数据的形式不等式、多元统计检验转为审计分数
- 📌 **结论**：检测完整与部分数据集使用均无假阳性，且在多样训练场景下鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Concerns over dataset misuse in deep learning have highlighted the need for effective auditing. Unlike existing intrusive methods that require dataset modifications, which risk model performance and security, we present DataGuard, a non-intrusive framework for quantitative dataset auditing. Specifically, DataGuard integrates three key components: 1) a differential comparison between the target dataset and auxiliary non-training datasets, 2) an information-forensic analysis establishing formal inequalities to distinguish training data; and 3) a multivariate statistical test that translates these discrepancies into rigorous auditing scores. Extensive experiments demonstrate that DataGuard can detect both full and partial dataset usage without false positives while remaining robust under diverse training scenarios, offering a principled, information-theoretic solution for transparent AI development.

</details>

### 62. Copyright-Bench: Agentic Evaluation of Copyright Law Compliance

🎓 [Official](https://icml.cc/virtual/2026/poster/66009)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Zheng Hui、Doni Bloomfield、Noam Kolt

- 🎯 **研究动机**：LLM agent 执行涉及检索与复用外部内容的商业任务，缺乏评估其版权法合规的工具
- 🔬 **研究方法**：Copyright-Bench 用网站开发、商品设计、企业内容生产等现实任务让 agent 在自由许可与版权内容间选择，并以提示变体模拟不同用户意图与时间压力
- 📌 **结论**：即使有合法替代，SOTA agent 仍违反版权法；用户意图明确与时间压力下违规率上升

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content such as images and, where appropriate, reproducing that content. LLM agents should comply with the law, including the laws of copyright. Yet today we lack adequate tools to assess whether they do so. To that end, we introduce Copyright-Bench, a benchmark designed to evaluate copyright law compliance of LLM agents. Copyright-Bench is comprised of realistic commercial tasks---website development, merchandise design, and corporate content production---that involve agents selecting between freely licensed content (the use of which is legal) and copyrighted content (the use of which is illegal at least in this setting). Notably, the evaluation introduces prompt variations that simulate different levels of user intent and time pressure. Comparing state-of-the-art agents against a human baseline, we find that: (1) LLM agents take actions that violate copyright law despite the availability of lawful alternatives; and (2) violation rates increase in response to user intent and under simulated time pressure.

</details>

### 63. Implicit Identity Technologies for LLMs: Fingerprinting and Watermarking Across Datasets, Models, and Generated Content

📄 [arXiv](https://arxiv.org/abs/2605.29245) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/SV270.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=survey-track)　📅 2026

**关键词**：`survey`、`LLM identity`、`fingerprinting`、`watermarking`

👤 **作者**：Bing Liu、…、Wei Luo

- 🎯 **研究动机**：LLM 指纹与水印研究术语混乱、方向孤立，缺乏系统组织
- 🔬 **研究方法**：综述提出 implicit identity 统一抽象区分指纹与水印，建立覆盖数据集、模型、生成内容的生命周期分类法与可识别性/鲁棒性/可部署性评测框架
- 📌 **结论**：结构化该领域图景、澄清术语并指出安全部署方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) require substantial investments and are increasingly deployed in highstakes domains, making it critical to protect LLMrelated assets and to trace their provenance. Identity technologies such as fingerprinting and watermarking address these needs by enabling ownership verification and attribution, and have rapidly emerged as an active research focus. However, existing techniques lack a systematic organisation, leading to two key issues, terminological confusion and isolated research lines, that have hindered the development of this research field. To this end, we present a comprehensive review of LLM identity techniques, focusing on fingerprinting and watermarking across the LLM lifecycle, including datasets, models, and generated content. We make three primary contributions. First, we introduce implicit identity (Implicit-ID for short) as a unifying abstraction and distinguish fingerprinting from watermarking. Second, we propose a lifecyclebased taxonomy that organises techniques by asset type and verification role, aligning each with asset protection or provenance. Third, we establish an evaluation framework around three objectives— identifiability, robustness, and deployability. Together, these contributions structure the landscape of LLM identity techniques, clarify terminology, and highlight directions toward secure deployment.

</details>

### 64. Smudged Fingerprints: A Systematic Evaluation of the Robustness of AI Image Fingerprints

📄 [arXiv](https://arxiv.org/abs/2512.11771) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-12　🏷 SaTML 2026

**关键词**：`attack`、`AI image fingerprint`、`removal and forgery`、`attribution robustness`

👤 **作者**：Kai Yao、Marc Juarez

- 🎯 **研究动机**：AI 图像指纹用于溯源取证，但现有评测几乎不考虑对抗设定，其在攻击下的鲁棒性不明
- 🔬 **研究方法**：形式化白盒/黑盒访问与指纹移除、伪造两种攻击目标的威胁模型，实现五种攻击策略，评测 14 种指纹方法（RGB、频域、学习特征）在 12 个 SOTA 生成器上的表现
- 📌 **结论**：白盒移除成功率常超 80%、黑盒超 50%；没有方法能兼顾准确与鲁棒，准确的归因方法往往更易受攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model fingerprint detection has shown promise to trace the provenance of AI-generated images in forensic applications. However, despite the inherent adversarial nature of these applications, existing evaluations rarely consider adversarial settings. We present the first systematic security evaluation of these techniques, formalizing threat models that encompass both white- and black-box access and two attack goals: fingerprint removal, which erases identifying traces to evade attribution, and fingerprint forgery, which seeks to cause misattribution to a target model. We implement five attack strategies and evaluate 14 representative fingerprinting methods across RGB, frequency, and learned-feature domains on 12 state-of-the-art image generators. Our experiments reveal a pronounced gap between clean and adversarial performance. Removal attacks are highly effective, often achieving success rates above 80% in white-box settings and over 50% under black-box access. While forgery is more challenging than removal, its success varies significantly across targeted models. We also observe a utility-robustness trade-off: accurate attribution methods are often vulnerable to attacks and, although some techniques are robust in specific settings, none achieves robustness and accuracy across all evaluated threat models. These findings highlight the need for techniques that balance robustness and accuracy, and we identify the most promising approaches toward this goal. Code available at: https://github.com/kaikaiyao/SmudgedFingerprints.

</details>

### 65. VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2606.12263) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/qiu-chunlin)　📅 2026-06　🏷 USENIX Security 2026

**关键词**：`defense`、`latent diffusion model`、`unauthorized mimicry`、`model copyright`、`identity protection`

👤 **作者**：Chunlin Qiu、…、Qian Wang

- 🎯 **研究动机**：已有防御用扰动把生成图像引向无关目标，依赖扰动能在 LDM 长生成过程中保持欺骗效力的无根据假设；模型自身修复机制会使身份重新出现
- 🔬 **研究方法**：提出 VOID：放大潜编码误差击碎语义结构并对抗目标引导信号压制模型修复能力，操纵 LDM 固有随机性，扰动限于人类不可感知区域
- 📌 **结论**：对 24 个 SOTA 防御、10 种模仿攻击、5 个数据集评估，平均 FID 从 113 升至 365，比此前最强防御高 223%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While Latent Diffusion Models (LDMs) have revolutionized visual synthesis, they are increasingly exploited for unauthorized mimicry of individuals. Existing defenses inject deceptive perturbations to steer the generated images toward irrelevant targets. However, this approach hinges on an ungrounded assumption: subtle perturbations can maintain their deceptive efficacy throughout an LDM's extensive generation process. In reality, the model's innate restoration mechanism will remove such perturbations and cause individual identities to re-emerge in the images generated. We propose VOID, a defense framework that overcomes this conundrum by manipulating an LDM's intrinsic stochasticity. VOID perturbs the diffusion pipeline in two novel ways: 1) amplifying the latent encoding errors to shatter an image's semantic structure, and 2) counteracting the target guidance signals to suppress the model's restoration capabilities. This results in a semantic corruption that thwarts any unauthorized mimicry. Notably, the security gain does not come at the price of visual utility, as VOID simultaneously manages to confine perturbations to human-imperceptible regions of protected images. Our comprehensive evaluation of 24 state-of-the-art defenses against 10 mimicry attacks on 5 datasets demonstrates VOID's unprecedented protection power: it increases the average Frechet Inception Distance (FID) from 113 to 365, a 223% improvement over the strongest defense to date.

</details>

### 66. PragLocker: Protecting Agent Intellectual Property in Untrusted Deployments via Non-Portable Prompts

📄 [arXiv](https://arxiv.org/abs/2605.05974) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64248)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Qinfeng Li、…、Xuhong Zhang

- 🎯 **研究动机**：agent prompt 是核心 IP，不可信部署下可被复制到其他专有 LLM 复用造成损失
- 🔬 **研究方法**：PragLocker 用代码符号锚定语义构造保功能混淆 prompt，再以目标模型反馈注入噪声，使 prompt 只在目标 LLM 上有效
- 📌 **结论**：跨多 agent 系统、数据集与基础 LLM 显著降低跨 LLM 可移植性，保持目标性能并抵御自适应攻击者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents rely on prompts to implement task-specific capabilities based on foundation LLMs, making agent prompts valuable intellectual property. However, in untrusted deployments, adversaries can copy and reuse these prompts with other proprietary LLMs, causing economic losses. To protect these prompts, we identify four key challenges: proactivity, runtime protection, usability, and non-portability that existing approaches fail to address. We present PragLocker, a prompt protection scheme that satisfies these requirements. PragLocker constructs function-preserving obfuscated prompts by anchoring semantics with code symbols and then using target-model feedback to inject noise, yielding prompts that only work on the target LLM. Experiments across multiple agent systems, datasets, and foundation LLMs show that PragLocker substantially reduces cross-LLM portability, maintains target performance, and remains robust against adaptive attackers.

</details>

### 67. Off-The-Shelf Image-to-Image Models Are All You Need To Defeat Image Protection Schemes

📄 [arXiv](https://arxiv.org/abs/2602.22197) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-02　🏷 SaTML 2026

**关键词**：`attack`、`image protection`、`generative denoising`、`defense bypass`

👤 **作者**：Xavier Pleimling、…、Bimal Viswanath

- 🎯 **研究动机**：图像保护方案此前只需应对专用攻击，通用生成模型能否直接击穿未检验
- 🔬 **研究方法**：把现成 image-to-image GenAI 模型经简单文本提示改造成通用去噪器，去除图像保护性扰动
- 📌 **结论**：6 类保护方案的 8 个案例中全部被绕过且优于专用攻击并保留图像效用，多数方案只是虚假安全感

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Advances in Generative AI (GenAI) have led to the development of various protection strategies to prevent the unauthorized use of images. These methods rely on adding imperceptible protective perturbations to images to thwart misuse such as style mimicry or deepfake manipulations. Although previous attacks on these protections required specialized, purpose-built methods, we demonstrate that this is no longer necessary. We show that off-the-shelf image-to-image GenAI models can be repurposed as generic ``denoisers" using a simple text prompt, effectively removing a wide range of protective perturbations. Across 8 case studies spanning 6 diverse protection schemes, our general-purpose attack not only circumvents these defenses but also outperforms existing specialized attacks while preserving the image's utility for the adversary. Our findings reveal a critical and widespread vulnerability in the current landscape of image protection, indicating that many schemes provide a false sense of security. We stress the urgent need to develop robust defenses and establish that any future protection mechanism must be benchmarked against attacks from off-the-shelf GenAI models. Code is available in this repository: https://github.com/mlsecviswanath/img2imgdenoiser

</details>

### 68. Echoes of Ownership: Adversarial-Guided Dual Injection for Copyright Protection in MLLMs

📄 [arXiv](https://arxiv.org/abs/2602.18845) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_Echoes_of_Ownership_Adversarial-Guided_Dual_Injection_for_Copyright_Protection_in_CVPR_2026_paper.html)　📅 2026-02　🏷 CVPR 2026

**关键词**：`defense`、`MLLM copyright`、`dual injection`、`ownership verification`

👤 **作者**：Chengwei Xia、Fan Ma、Ruijie Quan、Yunqiu Xu、Kun Zhan、Yi Yang

- 🎯 **研究动机**：MLLM 所有权纠纷频发，缺少只在微调衍生模型中触发、对无关模型惰性的归属验证机制
- 🔬 **研究方法**：把触发图像作为可学习张量做双重注入：辅助 MLLM 输出与所有权文本的一致性损失加 CLIP 特征对齐，并对辅助模型做对抗训练增强鲁棒性
- 📌 **结论**：在多种微调与域偏移场景下有效追踪模型谱系并验证所有权

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid deployment of multimodal large language models (MLLMs), disputes regarding model ownership have become increasingly frequent, raising significant concerns about intellectual property protection. In this paper, we propose a framework for generating copyright triggers for MLLMs, enabling model publishers to embed verifiable ownership information into the model. The goal is to construct trigger images that elicit ownership-related textual responses exclusively in fine-tuned derivatives, while remaining inert in other non-derivative models. Our method constructs a tracking trigger image by treating the image as a learnable tensor, performing adversarial optimization with dual-injection of ownership-relevant semantic information. The first injection is achieved by enforcing textual consistency between the output of an auxiliary MLLM and a predefined ownership-relevant target text; the consistency loss is backpropagated to inject this ownership-related information into the image. The second injection is performed at the semantic-level by minimizing the distance between the CLIP features of the image and those of the target text. Furthermore, we introduce an additional adversarial training stage involving the auxiliary model. It is specifically trained to resist generating ownership-relevant target text, thereby enhancing robustness in heavily fine-tuned derivative models. Extensive experiments demonstrate the effectiveness of our dual-injection approach in tracking model lineage under various fine-tuning and domain-shift scenarios. Code is at https://github.com/kunzhan/AGDI

</details>

### 69. Making Theft Useless: Adulteration-Based Protection of Proprietary Knowledge Graphs in GraphRAG Systems

📄 [arXiv](https://arxiv.org/abs/2601.00274) · 🌐 [Project](https://conf.researchr.org/track/ase-2026/ase-2026-research-track)　📅 2026-01　🏷 ASE 2026

**关键词**：`defense`、`GraphRAG asset theft`、`data adulteration`、`access control`

👤 **作者**：Weijie Wang、…、Jiaheng Zhang

- 🎯 **研究动机**：GraphRAG 专有知识图谱面临被窃取私用的风险：水印等被动防御在隔离环境失效，强加密又因延迟不可行
- 🔬 **研究方法**：AURA 预先向 KG 注入貌似合理的虚假掺杂物；授权用户凭密钥经加密元数据标签过滤掺杂物保证准确，攻击者检索被劣化得到错误回答
- 📌 **结论**：未授权系统准确率降至 5.3%，授权用户 100% 保真且开销可忽略；抗净化尝试，保留 80.2% 掺杂物

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph Retrieval-Augmented Generation (GraphRAG) has emerged as a key technique for enhancing Large Language Models (LLMs) with proprietary Knowledge Graphs (KGs) in knowledge-intensive applications. As these KGs often represent an organization's highly valuable intellectual property (IP), they face a significant risk of theft for private use. In this scenario, attackers operate in isolated environments. This private-use threat renders passive defenses like watermarking ineffective, as they require output access for detection. Simultaneously, the low-latency demands of GraphRAG make strong encryption which incurs prohibitive overhead impractical. To address these challenges, we propose AURA, a novel framework based on Data Adulteration designed to make any stolen KG unusable to an adversary. Our framework pre-emptively injects plausible but false adulterants into the KG. For an attacker, these adulterants deteriorate the retrieved context and lead to factually incorrect responses. Conversely, for authorized users, a secret key enables the efficient filtering of all adulterants via encrypted metadata tags before they are passed to the LLM, ensuring query results remain completely accurate. Our evaluation demonstrates the effectiveness of this approach: AURA degrades the performance of unauthorized systems to an accuracy of just 5.3%, while maintaining 100% fidelity for authorized users with negligible overhead. Furthermore, AURA proves robust against various sanitization attempts, retaining 80.2% of its adulterants.

</details>

### 70. Towards Trustworthy and Identifiable Virtual Face Generation

🎓 [Official](https://icml.cc/virtual/2026/poster/60956)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`diffusion model`

👤 **作者**：Chunyang Li、…、Weiqiang Wang

- 🎯 **研究动机**：可识别虚拟人脸（IVF）生成无法验证可信性，生成质量与可控性受限
- 🔬 **研究方法**：提出 TIVDiff：VIP 学习虚拟身份空间并结合 3D 面部几何合成虚拟脸；IGGW 经可逆映射把扩散初始噪声与 VID 绑定，嵌入不可感知线索用于合法性验证
- 📌 **结论**：图像质量、可识别性与可信性均优于现有 IVF 生成方案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Identifiable virtual face (IVF) generation aims to transform a user's original face into a virtual face for high utility privacy protection. The IVF is visually and statistically different from the original face, which can still be used for recognizing the user's identity. Despite this advantage, these schemes are unable to verify the trustworthiness of the IVF, the quality and controllability of which is often limited. To address these issues, we propose TIVDiff, a diffusion-based framework for trustworthy and identifiable virtual face generation. TIVDiff learns a virtual identity (VID) space via Virtual Identity Projection (VIP) and synthesizes high-quality virtual faces conditioned on VID and 3D facial geometry for pose and expression preservation. To enable the trustworthiness of IVF, we further propose an Identity-Guarded Generative Watermarking (IGGW) scheme to bind the diffusion initial noise with VID through a reversible mapping mechanism. This enables the embedding of an imperceptible cue into IVF for legitimacy verification. Experiments demonstrate the advantage of our TIVDiff over the state-of-the-art IVF generation schemes in terms of image quality, identifiability and trustworthiness.

</details>

### 71. ORPHEUS: A Separation-Robust Proactive Defense for Singing Voice Conversion

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wei-zhaolin)　📅 2026　🏷 USENIX Security 2026

**关键词**：`defense`、`singing voice conversion`、`source separation`、`model copyright`、`identity protection`

👤 **作者**：Zhaolin Wei、…、Zhihong Tian

- 🎯 **研究动机**：现有抗歌声转换的扰动防御针对纯人声设计，攻击者先做源分离时扰动被当作伴奏滤除
- 🔬 **研究方法**：ORPHEUS 联合用 mask 误导与跨轨损失干扰分离模型、异构说话人编码器集成破坏身份、调性和谐约束与心理声学掩蔽优化感知质量
- 📌 **结论**：比最佳基线在两个说话人验证模型上再降身份相似度 8.02% 与 5.61%，防御效果与跨模型迁移更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in singing voice conversion enable realistic cloning of a singer's voice, raising concerns about unauthorized voice misuse. Existing proactive defenses inject imperceptible perturbations to disrupt such conversion, and they are designed for vocal signals rather than mixed music. In real-world scenarios, however, attackers usually obtain mixed music and apply source separation to decompose the mixture into vocal and backing tracks before conversion. Since separation models are trained to distinguish vocals from background components, perturbations are often treated as backing, causing the perturbations to be filtered out. To address this, we present ORPHEUS, the first proactive defense framework tailored for singing voice conversion involving source separation. Specifically, we jointly (i) interfere with the separation model via mask-misguiding and cross-track losses, (ii) disrupt identity information using an ensemble of heterogeneous speaker encoders to enhance transferability, and (iii) optimize perceptual quality through tonality harmony constraints and psychoacoustic masking. To evaluate ORPHEUS, we conduct experiments on two datasets with three source separation models and four singing voice conversion systems. Compared with the best-performing baseline, ORPHEUS further reduces identity similarity by 8.02% and 5.61% on two speaker verification models, respectively, demonstrating consistently stronger defense effectiveness and cross-model transferability.

</details>

### 72. GoodDiffusion: Proactive Copyright Protection for Diffusion Generative Models via Learnable Sample-specific Signatures

📄 [arXiv](https://arxiv.org/abs/2606.29759) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60784)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`authorization control`、`sample-specific signature`、`diffusion bridge`、`model ownership`、`diffusion model`

👤 **作者**：Shixi Qin、Zhiyong Yang、Shilong Bao、Zitai Wang、Qianqian Xu、Qingming Huang

- 🎯 **研究动机**：已有版权保护多为事后归因或仅降质的防御，无法切断扩散桥模型的未授权使用
- 🔬 **研究方法**：提出 GoodDiffusion：借鉴后门机制把授权内化为生成过程，携带有效签名的查询高质量生成、未授权输入拒绝生成；理论证明静态签名可被梯度优化恢复，故引入输入条件化的 Learnable Signature Network 打破签名普适性
- 📌 **结论**：有效阻断未授权使用同时保持授权用户生成质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper tackles the challenging problem of developing a proactive copyright protection mechanism that cuts off unauthorized use of diffusion bridge models. Existing studies largely fall into post-hoc attribution (e.g., watermarking and fingerprinting) or degradation-only defenses, which offer only indirect and limited preventive effects. We therefore propose GoodDiffusion, inspired by backdoor mechanisms, to enforce model-level use-time control by internalizing authorization into the generative process through a selectively permissive, otherwise closed behavior. Specifically, GoodDiffusion preserves high-quality generation for authorized queries carrying valid signatures, yet refuses to generate for unauthorized inputs. We further theoretically show that naive static-signature designs (like conventional backdoor injection) are fundamentally fragile, since a surrogate signature can be efficiently recovered via gradient-based optimization. To strengthen security, we introduce a Learnable Signature Network (LSN) that assigns sample-specific signatures conditioned on each input. This breaks the universality of signatures and prevents a surrogate from transferring across inputs. Extensive experiments validate that GoodDiffusion effectively blocks unauthorized use while maintaining strong generation quality for authorized users.

</details>

### 73. GaussTrace: Provenance Analysis of 3D Gaussian Splatting Models with Evidence-based LLM Reasoning

📄 [arXiv](https://arxiv.org/abs/2606.10612) · 🌐 [Project](https://haolianghan.github.io/GaussTrace) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62380)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`AI watermarking`、`empirical evaluation`

👤 **作者**：Haoliang Han、Ziyuan Luo、Renjie Wan

- 🎯 **研究动机**：3DGS 模型被广泛分享与迭代修改，知识产权保护与取证溯源缺乏手段
- 🔬 **研究方法**：GaussTrace 对参数做逐属性统计画像并用假设驱动的编辑模拟提供辅助证据，LLM 结构化 CoT 推理输出有向溯源图与可解释边理由
- 📌 **结论**：无需训练或编辑历史即可构建准确、可解释且鲁棒的模型演化关系图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

3D Gaussian Splatting (3DGS) is a powerful technique for creating high-fidelity 3D assets. However, the widespread sharing and iterative modification of 3DGS models across digital platforms create pressing challenges for intellectual property protection and forensic traceability. To address this, we propose GaussTrace, a novel framework for constructing directed provenance graphs for 3DGS models. GaussTrace formulates provenance analysis as an evidence-based reasoning problem. It builds upon attribute-wise statistical profiling of 3DGS parameters to capture intrinsic properties. Moreover, we introduce hypothesis-driven editing simulations of common operations to provide auxiliary evidence for plausible transformation pathways. These statistical and simulated cues jointly enable a Large Language Model (LLM) to perform structured Chain-of-Thought (CoT) reasoning, yielding directional provenance inferences and explainable edge reasons. Experimental results demonstrate that GaussTrace effectively constructs evolutionary relationships among diverse 3DGS models, delivering accurate, interpretable, and robust provenance graphs without requiring model training or access to editing histories. Project page: https://haolianghan.github.io/GaussTrace.

</details>

### 74. FUSE: Full‑spectrum Unlearnable Examples via Spectral Equalization

🎓 [Official](https://icml.cc/virtual/2026/poster/65041)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Jiale Cai、…、Boyu Wang

- 🎯 **研究动机**：现有不可学习样本（UE）的扰动集中在高频，低通滤波即可使其失效
- 🔬 **研究方法**：FUSE 用 Random Spectral Masking 随机屏蔽频带训练生成器，并以 Cross-Band Guidance 强制高低频互一致，生成频谱无关扰动
- 📌 **结论**：在多数据集、架构与谱滤波设定下均保持强不可学习保护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearnable examples (UEs) protect training data by injecting imperceptible perturbations so that models fail to extract exploitable representations. In this paper, we reveal that existing UEs exhibit a critical failure once low-pass filtering is applied, indicating that the effective perturbation signals for unlearnability concentrate predominantly in high frequencies. Hence, we argue that reliable UEs should remain effective across the full spectrum. To this end, we propose F ull-spectrum U nlearnable Examples via S pectral E qualization ( FUSE ), which aims to generate spectrum-agnostic perturbations by equalizing the contributions from different bands and enforcing cross-band consistency. Specifically, FUSE adopts a Random Spectral Masking (RSM) strategy during generator training, which randomly removes a contiguous frequency band, forcing the remaining bands to maintain unlearnability. In addition, FUSE further integrates Cross-Band Guidance (CBG), which enforces mutual consistency between high- and low-frequency components, thereby further enhancing low-frequency unlearnability and regulating high-frequency perturbations to preserve the semantic fidelity of images. Extensive experiments across multiple datasets, architectures, and spectral filtering demonstrate the strong protection achieved by FUSE.

</details>

### 75. Dual-branch Robust Unlearnable Examples

📄 [arXiv](https://arxiv.org/abs/2605.01718) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61865)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`empirical evaluation`

👤 **作者**：Xianlong Wang、…、Xiaohua Jia

- 🎯 **研究动机**：现有不可学习样本方案因启发式设计或窄域扰动，对高级防御鲁棒性有限
- 🔬 **研究方法**：DUNE 双支路在空间与颜色域分别优化扰动以建立扰动与移位标签映射，扩大扰动域；配聚合多样预训练模型的不可学习增强集成
- 📌 **结论**：CIFAR-10 与 ImageNet 上抗 7 种主流防御超越 12 个 SOTA 方案，平均测试准确率低至 14.95 至 50.82%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Unlearnable examples (UEs) aim to compromise model training by injecting imperceptible perturbations to clean samples. However, existing UE schemes exhibit limited robustness against advanced defenses due to their heuristic design or narrowly scoped domain perturbations. To address this, we propose DUNE, a Dual-branch UNlearnable Ensemble perturbation optimization approach. Specifically, DUNE separately optimizes perturbations in the spatial and color domains to establish the mapping between perturbations and shift-induced labels. This design extends the perturbation domain to increase noise intensity for improving robustness and drives the models to learn perturbation-oriented features with degraded generalization, thereby achieving unlearnability. To strengthen DUNE's performance, we further propose an unlearnability-enhancing ensemble strategy that aggregates diverse pre-trained models during the dual-branch optimization. Extensive experiments on benchmark datasets CIFAR-10 and ImageNet verify that DUNE's robustness outperforms 12 SOTA UE schemes under 7 mainstream defenses, yielding a lower average test accuracy of 14.95% to 50.82%.

</details>

### 76. DDIM Inversion as a Perturbation Amplifier: Breaking Mimicry Protection via Reconstruction Error Minimization

🎓 [Official](https://icml.cc/virtual/2026/poster/65799)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`mechanistic analysis`

👤 **作者**：Huming Qiu、…、Min Yang

- 🎯 **研究动机**：模仿保护方法（嵌入扰动破坏风格模仿学习）的鲁棒性缺乏系统理解
- 🔬 **研究方法**：首次证明 DDIM inversion 天然充当扰动放大器，使受保护图像重建时严重结构畸变；DIRP 在感知约束下显式最小化 DDIM 逆重建误差去除保护扰动
- 📌 **结论**：对六种模仿保护方法一致超越五个 SOTA 攻击基线且更好保留图像质量，暴露现有保护的根本漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personalization techniques for image generation models have increasingly been misused for malicious purposes, including unauthorized style imitation and copyrighted content replication. In response, recent mimicry protection methods embed carefully designed perturbations into images to disrupt a model’s ability to learn genuine semantic representations. Despite their growing adoption, the robustness of these protection mechanisms remains poorly understood, raising concerns about their reliability in real-world deployment. In this work, we present the first systematic analysis showing that DDIM inversion inherently acts as a perturbation amplifier, causing protected images to suffer severe structural distortions during reconstruction. Building on this observation, we propose DDIM Inversion-based Reconstruction Purification (DIRP), a novel purification approach that removes protective perturbations by explicitly minimizing DDIM inversion reconstruction error under perceptual constraints. Extensive experiments on six existing mimicry protection methods demonstrate that DIRP consistently outperforms five state-of-the-art attack baselines, achieving superior perturbation removal while better preserving image quality. Our results expose fundamental vulnerabilities in current mimicry protection strategies and highlight the urgent need for more robust and principled defenses.

</details>

### 77. Anchored Decoding: Provably Reducing Copyright Risk for Any Language Model

📄 [arXiv](https://arxiv.org/abs/2602.07120) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65462)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`model copyright`、`ownership verification`、`model provenance`、`model ownership`、`inference-time intervention`

👤 **作者**：Jacqueline He、Jonathan Hayase、Wen-tau Yih、Sewoong Oh、Luke Zettlemoyer、Pang Wei Koh

- 🎯 **研究动机**：LM 会记忆并逐字复现训练数据，混合许可数据训练带来版权与合规风险
- 🔬 **研究方法**：Anchored Decoding 是即插即用的推理时方法：把生成约束在宽容许可训练安全模型（TinyComma 1.8B）的有界邻域内，自适应分配信息预算并施加逐步约束获得序列级保证；字节级变体 Anchored-Byte 借 ByteSampler 支持跨词表融合
- 📌 **结论**：六对模型上定义新的 Pareto 前沿，保留接近原始的流畅度与事实性，消除最高 75% 的可测复制差距，推理开销适中

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models (LMs) tend to memorize portions of their training data and reproduce verbatim spans. When the underlying sources are sensitive or copyright-protected, such reproduction raises issues of consent and compensation for creators and compliance risks for developers. We propose Anchored Decoding, a plug-and-play inference-time method for suppressing verbatim reproduction: it enables decoding from any risky LM trained on mixed-license data by keeping generation in bounded proximity to a permissively trained safe LM. Anchored Decoding does so by adaptively allocating a user-chosen information budget over the generation trajectory and enforcing per-step constraints that yield a sequence-level guarantee, enabling a tunable risk–utility trade-off. To make Anchored Decoding practically useful, we introduce a new permissively trained safe model (TinyComma 1.8B), as well as Anchored-Byte Decoding, a byte-level variant of our method that enables cross-vocabulary fusion via the ByteSampler (Hayase et al., 2025) framework. Across six model pairs on long-form metrics for copying risk and utility, Anchored and Anchored-Byte Decoding define a new Pareto frontier, preserving near-original fluency and factuality while eliminating up to 75\% of the measurable copying gap between the risky baseline and a safe reference, at a modest inference overhead.

</details>

### 78. AdLift: Lifting Adversarial Perturbations to Safeguard 3D Gaussian Splatting Assets Against Instruction-Driven Editing

📄 [arXiv](https://arxiv.org/abs/2512.07247) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64053)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`adversarial robustness`、`model copyright`、`ownership verification`、`model ownership`、`diffusion model`

👤 **作者**：Ziming Hong、…、Tongliang Liu

- 🎯 **研究动机**：指令驱动编辑扩展到 3D Gaussian Splatting 资产后，未授权编辑与恶意篡改风险陡增，而 2D 对抗扰动保护面临视角泛化与不可见性-保护力平衡两大挑战
- 🔬 **研究方法**：提出首个 3DGS 编辑防护 AdLift：用定制的 Lifted PGD 把严格有界的 2D 对抗扰动提升为 3D 高斯防护——编辑模型反向传播时梯度截断、投影梯度严格限制图像级扰动，再经图像到高斯拟合回传参数，两步交替
- 📌 **结论**：跨不同视角一致防护并泛化到新视角，有效抵御 SOTA 指令驱动 2D 图像与 3DGS 编辑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent studies have extended diffusion-based instruction-driven 2D image editing pipelines to 3D Gaussian Splatting (3DGS), enabling faithful manipulation of 3DGS assets and greatly advancing 3DGS content creation. However, it also exposes these assets to serious risks of unauthorized editing and malicious tampering. Although imperceptible adversarial perturbations against diffusion models have proven effective for protecting 2D images, applying them to 3DGS encounters two major challenges: view-generalizable protection and balancing invisibility with protection capability. In this work, we propose the first editing safeguard for 3DGS, termed AdLift, which prevents instruction-driven editing across arbitrary views and dimensions by lifting strictly bounded 2D adversarial perturbations into 3D Gaussian-represented safeguard. To ensure both adversarial perturbations effectiveness and invisibility, these safeguard Gaussians are progressively optimized across training views using a tailored Lifted PGD, which first conducts gradient truncation during back-propagation from the editing model at the rendered image and applies projected gradients to strictly constrain the image-level perturbation. Then, the resulting perturbation is backpropagated to the safeguard Gaussian parameters via an image-to-Gaussian fitting operation. We alternate between gradient truncation and image-to-Gaussian fitting, yielding consistent adversarial-based protection performance across different viewpoints and generalizes to novel views. Empirically, qualitative and quantitative results demonstrate that AdLift effectively protects against state-of-the-art instruction-driven 2D image and 3DGS editing.

</details>

### 79. COPYLENS: Towards Copyrighted Characters Infringement Detection via Copyright-Aware Prompt Learning

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Jin_COPYLENS_Towards_Copyrighted_Characters_Infringement_Detection_via_Copyright-Aware_Prompt_Learning_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`detection`、`copyright infringement`、`character generation`、`prompt learning`

👤 **作者**：Yaoyu Jin、…、Bin Wang

- 🎯 **研究动机**：T2I 可生成与官方 depiction 难辨的版权角色图像，现有检测与人类侵权判断对齐不足
- 🔬 **研究方法**：CopyLens 闭环：LVLM 检测生成图像、LLM 经 meta-prompting 以人类标注一致性为反馈迭代精炼检测提示；构建含 7000 余张图像、100 余个版权角色的 CopyChars 数据集
- 📌 **结论**：检测性能比 SOTA 提升 5 至 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in text-to-image (T2I) generation can produce highly resembling images of copyrighted characters, often indistinguishable from official depictions, raising serious concerns about intellectual property infringement. Consequently, robust detection of copyright character infringement is urgently needed. Yet, existing methods exhibit limited alignment with human judgments regarding the likelihood of infringement. To bridge this gap, we propose CopyLens, a novel prompt optimization framework that automatically refines textual prompts for vision-language model-based detectors to better match human infringement judgments. Our approach establishes a closed-loop refinement process between a large vision-language model (LVLM) and a large language model (LLM): the LVLM assesses generated images for copyright detection, while the LLM iteratively optimizes detection prompts via meta-prompting, guided by feedback signals derived from human annotation consistency. To facilitate the assessment of prompt-human alignment, we introduce CopyChars, a new large-scale dataset of over 7,000 AI-generated images spanning more than 100 popular copyrighted characters, along with detailed human annotations on potential infringement. Extensive experiments on CopyChars show that the proposed CopyLens can improve detection performance by 5% to 10% compared to recent state-of-the-art methods. This work offers a scalable and automated solution for visual copyright protection and highlights the critical role of prompt engineering.

</details>

### 80. Prompt Pirates Need a Map: Stealing Seeds helps Stealing Prompts

📄 [arXiv](https://arxiv.org/abs/2509.09488) · 🌐 [Project](https://doi.org/10.1145/3779208.3807483)　📅 2025-09　🏷 ACM CCS 2026

**关键词**：`attack`、`diffusion asset`、`seed recovery`、`prompt stealing`、`diffusion model`

👤 **作者**：Felix Mächtle、Ashwath Shetty、Jonas Sander、Nils Loose、Sören Pirk、Thomas Eisenbarth

- 🎯 **研究动机**：数值优化式 prompt 窃取忽略生成初始噪声，PyTorch CPU 种子仅 2^32 范围构成 CWE-339 漏洞
- 🔬 **研究方法**：提出 SeedSnitch 暴力恢复种子（CivitAI 约 95% 图像可按 140 分钟/种子破解），再以遗传算法 PromptPirate 做种子感知的 prompt 窃取
- 📌 **结论**：LPIPS 相似度比 PromptStealer、P2HP 与 CLIP-Interrogator 提升约 8-11%；已负责任披露并推动修复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have significantly advanced text-to-image generation, enabling the creation of highly realistic images conditioned on textual prompts and seeds. Given the considerable intellectual and economic value embedded in such prompts, prompt theft poses a critical security and privacy concern. In this paper, we investigate prompt-stealing attacks targeting diffusion models. We reveal that numerical optimization-based prompt recovery methods are fundamentally limited as they do not account for the initial random noise used during image generation. We identify and exploit a noise-generation vulnerability (CWE-339), prevalent in major image-generation frameworks, originating from PyTorch's restriction of seed values to a range of $2^{32}$ when generating the initial random noise on CPUs. Through a large-scale empirical analysis conducted on images shared via the popular platform CivitAI, we demonstrate that approximately 95% of these images' seed values can be effectively brute-forced in 140 minutes per seed using our seed-recovery tool, SeedSnitch. Leveraging the recovered seed, we propose PromptPirate, a genetic algorithm-based optimization method explicitly designed for prompt stealing. PromptPirate surpasses state-of-the-art methods, i.e., PromptStealer, P2HP, and CLIP-Interrogator, achieving an 8-11% improvement in LPIPS similarity. Furthermore, we introduce straightforward and effective countermeasures that render seed stealing, and thus optimization-based prompt stealing, ineffective. We have disclosed our findings responsibly and initiated coordinated mitigation efforts with the developers to address this critical vulnerability.

</details>

### 81. Rethinking and Red-Teaming Protective Perturbation in Personalized Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2406.18944) · 🌐 [Project](https://doi.org/10.1145/3770854.3780303)　📅 2024-06　🏷 KDD 2026

**关键词**：`attack`、`anti-personalization`、`protective perturbation`、`adaptive red teaming`

👤 **作者**：Yixin Liu、Ruoxi Chen、Xun Chen、Lichao Sun

- 🎯 **研究动机**：现有净化方法破解个性化保护扰动时过度净化、损失信息
- 🔬 **研究方法**：从 shortcut learning 视角揭示扰动导致 CLIP 空间图文错配；提出数据净化加对比解耦学习的系统 red teaming 框架
- 📌 **结论**：优于现有净化方法且对自适应扰动稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Personalized diffusion models (PDMs) have become prominent for adapting pre-trained text-to-image models to generate images of specific subjects using minimal training data. However, PDMs are susceptible to minor adversarial perturbations, leading to significant degradation when fine-tuned on corrupted datasets. These vulnerabilities are exploited to create protective perturbations that prevent unauthorized image generation. Existing purification methods attempt to red-team the protective perturbation to break the protection but often over-purify images, resulting in information loss. In this work, we conduct an in-depth analysis of the fine-tuning process of PDMs through the lens of shortcut learning. We hypothesize and empirically demonstrate that adversarial perturbations induce a latent-space misalignment between images and their text prompts in the CLIP embedding space. This misalignment causes the model to erroneously associate noisy patterns with unique identifiers during fine-tuning, resulting in poor generalization. Based on these insights, we propose a systematic red-teaming framework that includes data purification and contrastive decoupling learning. We first employ off-the-shelf image restoration techniques to realign images with their original semantic content in latent space. Then, we introduce contrastive decoupling learning with noise tokens to decouple the learning of personalized concepts from spurious noise patterns. Our study not only uncovers shortcut learning vulnerabilities in PDMs but also provides a thorough evaluation framework for developing stronger protection. Our extensive evaluation demonstrates its advantages over existing purification methods and its robustness against adaptive perturbations.

</details>