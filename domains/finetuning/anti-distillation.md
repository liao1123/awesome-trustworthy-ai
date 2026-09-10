# 反蒸馏

[返回模型微调安全目录](README.md)

## 研究方向

反蒸馏研究如何在不明显损害服务质量的前提下，阻止第三方利用模型输出、推理轨迹或公开数据复制能力；主要路线包括输出采样与重写、不可学习数据、主动指纹、水印、攻击评测和模型提取防御。

## 研究脉络

- **输出侧防护：** 早期 anti-distillation 方法通过输出扰动与 defensive sampling 降低学生模型的蒸馏收益。
- **保护对象扩展：** 研究随后覆盖 reasoning-trace rewriting、unlearnable data 和多模态数据保护。
- **攻防检验：** 攻击工作持续测试隐藏 CoT 的可提取性，fingerprint 与 watermark 则承担事后归属验证。

## 推理轨迹窃取与自适应绕过

### 1. JudgeStealer: Extracting LLM Judging Capabilities across Evaluation Protocols

📄 [arXiv](https://arxiv.org/abs/2608.26982)　📅 2026-08

**关键词**：`attack`、`judge capability extraction`、`cross-protocol distillation`、`query-efficient stealing`、`LLM judge extraction`、`black-box API`

👤 **作者**：Chen Chen、…、Kwok-Yan Lam

- 🎯 **研究动机**：LLM judge 的评分能力是高价值 IP，黑盒 API 暴露于抽取攻击，而现有 extraction 方法不针对 judge 且不支持多评测协议与有限查询预算
- 🔬 **研究方法**：提出 JudgeStealer，利用跨协议一致性把 pointwise 分数转换为 pairwise/listwise 监督而不额外查询，按语义多样性、预测不确定性与潜在偏差动态选点，辅以分数平滑与多协议复习
- 📌 **结论**：对 SOTA LLM judge 与 reward model 的抽取准确率在 pointwise/pairwise/listwise 上最高达 73.3%/87.0%/71.6%，并能抵抗代表性 extraction 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) judges are increasingly used across various evaluation scenarios, making their judgment capabilities valuable intellectual property. However, black-box access exposes these capabilities to model extraction attacks. Existing extraction methods do not specifically target LLM judges and provide limited support for multiple evaluation protocols under restricted query budgets. In this study, we propose JUDGESTEALER, the first query-efficient model extraction framework for replicating judging capabilities across pointwise scoring, pairwise comparison, and listwise ranking protocols. JUDGESTEALER exploits the strong cross-protocol agreement to acquire pointwise scores and transform them into pairwise and listwise supervisions without additional victim queries. To capture informative judge patterns and improve query efficiency, JUDGESTEALER dynamically selects pointwise inputs based on semantic diversity, predictive uncertainty, and potential judge biases. It further applies score smoothing and multi-protocol review to preserve the ordinal structure of scores and mitigate catastrophic forgetting during surrogate adaptation. Extensive experiments on state-of-the-art LLM-as-a-judge and reward models show that JUDGESTEALER consistently outperforms existing extraction baselines, achieving up to 73.3%, 87.0%, and 71.6% accuracy for pointwise, pairwise, and listwise evaluation, respectively. JUDGESTEALER also remains effective across different sur- rogate model scales, adaptation strategies, and reasoning settings. Moreover, JUDGESTEALER demonstrates robustness against representative extraction defenses.

</details>

### 2. Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction

📄 [arXiv](https://arxiv.org/abs/2608.26733)　📅 2026-08

**关键词**：`attack`、`skill extraction`、`black-box task interaction`、`functional reconstruction`、`agent-skill extraction`、`output-only access`

👤 **作者**：Yu-Lin Tsai、Yu-An Lu、Ci-Yang Tsai、Muxi Lyu、Raluca Ada Popa、Chia-Mu Yu

- 🎯 **研究动机**：泄露防御能拦截索要 skill 的请求，却拦不住服务本就要完成的普通任务，隐藏 skill 可被从结果逆向
- 🔬 **研究方法**：Daydreaming 自适应构造能区分隐藏行为的任务，用 shadow Agent 与本地执行检查重建多文件 skill，仅凭输出访问运作
- 📌 **结论**：7 个 skill、4 个受害模型上恢复原 skill 86.8% 的能力（约 SigLeak 四倍），每个 skill 中位数仅 32 次调用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that steals a multi-file skill through black-box task interactions. The victim is never asked to reveal the skill or grade a reconstruction. Instead, Daydreaming adaptively creates crafted tasks whose results distinguish possible hidden behaviors. It tests individual behaviors, uses attacker-controlled shadow agents to choose a design, and completes each file using stored victim results and local execution checks. We formalize three nested threat levels of access as Differential, Trace, and Output, and focus on Output, where the attacker sees only the final response and returned files. Across 7 skills and 4 victim models, Daydreaming recovers 86.8% of the original skill's capability at Output, outperforming SigLeak by almost 4x. It produces installable skills using a median of 32 victim calls per skill even with disclosure defenses enabled. These results show that hiding skill files and filtering direct disclosure do not, by themselves, prevent functional reconstruction through normal use.

</details>

### 3. EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2608.20055)　📅 2026-08

**关键词**：`attack`、`tool-call replay`、`hidden-state disclosure`、`API interaction`、`reasoning-trace extraction`、`API fidelity`

👤 **作者**：Yiting Qu、Ziqing Yang、Chi Cui、Ye Leng、Junjie Chu、Yang Zhang

- 🎯 **研究动机**：前沿专有 LRM 的隐藏 CoT 是宝贵模型资产，能否从黑盒 API 近逐字提取未被研究
- 🔬 **研究方法**：EchoCoT 发现工具调用间的推理重放面，多步攻击迭代利用 API 返回的保真信号提取隐藏 CoT，LLM 优化框架自动搜索跨数据集的通用注入轨迹
- 📌 **结论**：开源 LRM 上近逐字提取成功率达 66.4%（至少 90% token 精确匹配），通用轨迹在未见数据集达 80%；Gemini-2.5 上从 32,948 token 目标提取 33,463 token

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals. We further develop an LLM-based optimization framework that automatically searches for an effective universal injection trajectory across various datasets. We evaluate EchoCoT on three open-source and five frontier proprietary LRMs. On open-source LRMs, EchoCoT achieves up to 66.4\% near-verbatim extraction success, with the extracted trace length within 10\% of the target and at least 90\% of tokens exactly matching the target CoT. The same injection trajectory also generalizes to unseen datasets, achieving up to 80\% extraction success under the same criterion. For tested frontier proprietary LRMs, a substantial fraction of extracted CoTs closely align with provider-reported reasoning lengths and available CoT summaries. EchoCoT can also extract very long CoTs: on Gemini-2.5, it extracts 33,463 tokens from a 32,948-token target. These results establish hidden-CoT extraction as a practical security risk and highlight the need to better protect hidden CoT assets.

</details>

### 4. Stealing Reasoning Traces from Proprietary LLM APIs

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

### 5. Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.00642)　📅 2026-05

**关键词**：`attack`、`reasoning exposure`、`prompt elicitation`、`black-box distillation`

👤 **作者**：Yu-An Lu、Ci-Yang Tsai、Yu-Lin Tsai、Raluca Ada Popa、Chia-Mu Yu

- 🎯 **研究动机**：部署系统隐藏原始推理轨迹只暴露摘要与答案，接口级隐藏能否阻止用户经 prompt 获得推理监督未知
- 🔬 **研究方法**：Reasoning Exposure Prompting（REP）：用影子模型生成的示范加代码式辅助格式，轻量上下内诱导受害模型提升用户可见的推理轨迹
- 📌 **结论**：暴露轨迹与内部轨迹相似度大幅提升且保留有用推理信号，足以继续用于学生模型蒸馏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reasoning traces have become a valuable form of learning signals for improving and transferring the capabilities of large language models. In particular, detailed traces can help distill reasoning behavior from stronger teacher models into weaker student models. The value of capability transfer has motivated many deployed systems with reasoning models to hide raw internal traces and expose at most summaries and answers to users. As a result, we ask whether such interface-level trace hiding prevents users from obtaining useful reasoning supervision through prompting. We study this question with Reasoning Exposure Prompting (REP), a lightweight in-context elicitation method that uses shadow-model-generated demonstrations wrapped in auxiliary code-like formats to raise user-visible reasoning traces from a victim model. Across the common reasoning dataset, different victim models, and different student model distillation, REP substantially increases similarity between exposed and REP-conditioned internal traces while preserving useful reasoning signals.

</details>

### 6. How to Steal Reasoning Without Reasoning Traces

📄 [arXiv](https://arxiv.org/abs/2603.07267)　📅 2026-03

**关键词**：`attack`、`reasoning-trace extraction`、`trace inversion`、`black-box distillation`

👤 **作者**：Tingwei Zhang、John X. Morris、Vitaly Shmatikov

- 🎯 **研究动机**：只暴露答案与推理摘要、隐藏完整 CoT 是否足以阻止推理能力被盗未知
- 🔬 **研究方法**：训练 trace inversion 模型，仅凭输入、答案与可选推理摘要合成详细推理轨迹，再用其微调学生模型
- 📌 **结论**：合成轨迹与真实轨迹高度重叠，可显著提升学生推理并支持对专有黑盒 LLM 的蒸馏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many large language models (LLMs) use reasoning to generate responses but do not reveal their full reasoning traces (a.k.a. chains of thought), instead outputting only final answers and brief reasoning summaries. To demonstrate that hiding reasoning traces does not prevent users from "stealing" a model's reasoning capabilities, we introduce trace inversion models that, given only the inputs, answers, and (optionally) reasoning summaries exposed by a target model, generate detailed, synthetic reasoning traces. We show that (1) traces synthesized by trace inversion have high overlap with the ground-truth reasoning traces (when available), and (2) fine-tuning student models on inverted traces substantially improves their reasoning and enables distillation from proprietary, black-box LLMs.

</details>

### 7. StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data

📄 [arXiv](https://arxiv.org/abs/2509.23594) · 🎓 [Official](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_StolenLoRA_Exploring_LoRA_Extraction_Attacks_via_Synthetic_Data_ICCV_2025_paper.html)　📅 2025-09　🏷 ICCV 2025

**关键词**：`attack`、`LoRA extraction`、`synthetic query`、`substitute model`

👤 **作者**：Yixu Wang、Yan Teng、Yingchun Wang、Xingjun Ma

- 🎯 **研究动机**：LoRA 适配模型的提取攻击风险未被专门研究
- 🔬 **研究方法**：提出 StolenLoRA：用 LLM 生成合成查询训练替代模型，配基于分歧的半监督学习 DSL 最大化有限查询的信息增益
- 📌 **结论**：仅 10k 查询即达 96.60% 攻击成功率，跨骨干场景同样有效；多样化 LoRA 部署可部分缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA have transformed vision model adaptation, enabling the rapid deployment of customized models. However, the compactness of LoRA adaptations introduces new safety concerns, particularly their vulnerability to model extraction attacks. This paper introduces a new focus of model extraction attacks named LoRA extraction that extracts LoRA-adaptive models based on a public pre-trained model. We then propose a novel extraction method called StolenLoRA which trains a substitute model to extract the functionality of a LoRA-adapted model using synthetic data. StolenLoRA leverages a Large Language Model to craft effective prompts for data generation, and it incorporates a Disagreement-based Semi-supervised Learning (DSL) strategy to maximize information gain from limited queries. Our experiments demonstrate the effectiveness of StolenLoRA, achieving up to a 96.60% attack success rate with only 10k queries, even in cross-backbone scenarios where the attacker and victim models utilize different pre-trained backbones. These findings reveal the specific vulnerability of LoRA-adapted models to this type of extraction and underscore the urgent need for robust defense mechanisms tailored to PEFT methods. We also explore a preliminary defense strategy based on diversified LoRA deployments, highlighting its potential to mitigate such attacks.

</details>

### 8. Answer-then-Edit: Reasoning Skeleton Editing for Anti-Distillation with Preserved Utility

📄 [arXiv](https://arxiv.org/abs/2607.20440)　📅 2026-07

**关键词**：`defense`、`reasoning-skeleton editing`、`anti-distillation`、`utility preservation`

👤 **作者**：Fan Li、Mengting Pan、Sijia Xu、Xiaoyang Wang、Chen Chen、Wenjie Zhang

- 🎯 **研究动机**：已有抗蒸馏方法基于内部扰动，难以兼顾抗蒸馏性与推理轨迹效用，强防御常带来显著效用损失
- 🔬 **研究方法**：提出 SGRE Answer-then-Edit：教师先生成干净推理轨迹保精度，再依认知负荷理论三步编辑（骨架抽取、骨架图粗化、骨架言语化）扰动推理结构、放大学生外在负荷
- 📌 **结论**：跨多个 LLM 实现蒸馏效果降低的 SOTA，同时保持无损推理准确率与更自然的轨迹

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Proprietary large language models (LLMs) entail substantial intellectual and financial investment, making them valuable intellectual property (IP). However, even when deployed via black-box APIs, these models remain vulnerable to unauthorized knowledge distillation, which allows adversaries to cheaply extract and replicate model capabilities. To address this issue, anti-distillation (AD) has been proposed to generate defensive outputs that hinder distillation effectiveness, overcoming the limitation of watermarking-based approaches that rely on post-hoc verification. However, existing AD methods based on internal model perturbations struggle to balance anti-distillability and utility (e.g., answer accuracy and naturalness) of reasoning traces, with stronger defenses often causing significant utility loss. To fill this gap, we propose \textbf{\underline{S}}keleton-\textbf{\underline{G}}uided \textbf{\underline{R}}easoning \textbf{\underline{E}}diting (SGRE), an \textit{Answer-then-Edit} framework that performs post-hoc trace modification for anti-distillation. In the answer stage, the teacher model first generates clean reasoning traces, preserving the original reasoning accuracy while enabling more flexible control over trace naturalness. In the editing stage, we draw inspiration from Cognitive Load Theory (CLT) and introduce a three-stage strategy consisting of reasoning skeleton extraction, skeleton graph coarsening, and skeleton verbalization. These operations jointly perturb reasoning structures and augment textual complexity to amplify extraneous load on student models, hindering their acquisition of underlying reasoning patterns. Extensive experiments across diverse LLMs demonstrate that SGRE achieves state-of-the-art performance in reducing distillation effectiveness, while maintaining lossless reasoning accuracy and superior trace naturalness.

</details>

### 9. Lossless Anti-Distillation Sampling

📄 [arXiv](https://arxiv.org/abs/2605.18829)　📅 2026-05

**关键词**：`defense`、`model-output protection`、`defensive sampling`

👤 **作者**：Zibo Diao、Jingchu Gai、Xinyue Ai、Zhang Zhang、Zhenyu He、Di He

- 🎯 **研究动机**：现有反蒸馏防御要么修改输出伤害良性用户，要么靠行为检测可被多账号分发查询绕过
- 🔬 **研究方法**：LADS 由查询语义内容与查询次数决定的私有种子导出生成随机性：良性用户每次独立采样无损，同语义桶的多账号共享潜在随机性使蒸馏数据相关化
- 📌 **结论**：均匀收敛理论证明蒸馏泛化差距的收敛率被可证劣化；图像、数学与代码生成实验确认学生性能大幅下降而单用户体验统计无失真

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier commercial generative models face a growing threat from distillation, whereby a distiller harvests generated responses and trains a competing model of its own at drastically lower cost. Existing defenses either rely on modifying the models outputs, thereby sacrificing response quality for benign users, or on behavioral detection methods, which can be readily circumvented by distributing queries across multiple accounts. In this work, we propose Lossless Anti-Distillation Sampling (LADS), a novel sampling scheme specifically designed to counter multi-account distillation while maintaining a lossless experience for benign users. Concretely, LADS derives the randomness underlying each generation from a private seed determined by the semantic content of the query and the number of times the user has queried the model. By construction, every benign user receives a response independently sampled from the original model at each visit, and thus experiences no distortion. In contrast, for a distiller, different accounts share latent randomness whenever their queries fall in the same semantic bucket. As a result, the harvested data becomes correlated, potentially reducing sample diversity and degrading generalization. Using uniform convergence theory, we show that LADS provably degrades the convergence rate of the distillers generalization gap relative to standard i.i.d. sampling in both unconditional and conditional generation settings. Experiments on image generation, mathematical reasoning, and code generation confirm that LADS substantially degrades the performance of distilled students while preserving exact statistical fidelity for individual users.

</details>

### 10. Protecting the Trace: A Principled Black-Box Approach Against Distillation Attacks

📄 [arXiv](https://arxiv.org/abs/2604.23238)　📅 2026-04　🏷 ICML 2026

**关键词**：`defense`、`reasoning-trace protection`、`distillation resistance`

👤 **作者**：Max Hartman、Vidhata Jayaraman、Moulik Choraria、Yash Savani、Lav R. Varshney

- 🎯 **研究动机**：现有反蒸馏方法毒化全轨迹，语义句法可检测性会暴露防御存在并损害输出可信度
- 🔬 **研究方法**：把反蒸馏建模为显式含可检测性约束的 Stackelberg 博弈，定位对输出反事实影响过大的 thought anchors 做稀疏毒化，实现免训练黑盒 TraceGuard
- 📌 **结论**：稀疏扰动关键句即可降低学生蒸馏效果并保持轨迹连贯，是毒化全轨迹的更隐蔽替代

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Distillation via sampling reasoning traces exposes closed-source frontier models to adversarial third parties who can bypass their guardrails and misappropriate their capabilities. Antidistillation methods aim to address this by poisoning reasoning traces to hinder student model learning while preserving teacher performance. However, current methods overlook detectability, both semantic and syntactic, which erodes trust in the teacher's outputs and signals the defense's presence to adversaries. We address this gap by formulating antidistillation as a Stackelberg game whose constraint set explicitly encodes detectability, and show that perturbing sparingly offers an effective, less detectable alternative to poisoning the full trace. Drawing on mechanistic interpretability, we identify thought anchors, sentences with disproportionate counterfactual influence on model outputs, as a principled sparse target: critical to reasoning yet minimally detectable. We instantiate this in TraceGuard, a training-free, black-box proof-of-concept that locates thought anchors via branching-token detection and poisons them to degrade student distillation while preserving trace coherence.

</details>

### 11. Protecting Language Models Against Unauthorized Distillation through Trace Rewriting

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

### 12. Towards Distillation-Resistant Large Language Models: An Information-Theoretic Perspective

📄 [arXiv](https://arxiv.org/abs/2602.03396)　📅 2026-02

**关键词**：`defense`、`logit distillation`、`conditional mutual information`、`output purification`

👤 **作者**：Hao Fang、…、Ke Xu

- 🎯 **研究动机**：既有反蒸馏防御只针对文本蒸馏，logit 蒸馏未被探索
- 🔬 **研究方法**：以 ground-truth 标签条件下 teacher logits 与输入查询的条件互信息刻画可蒸馏信息，学习变换矩阵净化输出并以 CMI 启发目标优化
- 📌 **结论**：多个 LLM 与强蒸馏算法下显著降低蒸馏性能且保留任务准确率，有效保护模型知识产权

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Proprietary large language models (LLMs) embody substantial economic value and are generally exposed only as black-box APIs, yet adversaries can still exploit their outputs to extract knowledge via distillation. Existing defenses focus exclusively on text-based distillation, leaving the important logit-based distillation largely unexplored. In this work, we analyze this problem and present an effective solution from an information-theoretic perspective. We characterize distillation-relevant information in teacher outputs using the conditional mutual information (CMI) between teacher logits and input queries conditioned on ground-truth labels. This quantity captures contextual information beneficial for model extraction, motivating us to defend distillation via CMI minimization. Guided by our theoretical analysis, we propose learning a transformation matrix that purifies the original outputs to enhance distillation resistance. We further derive a CMI-inspired anti-distillation objective to optimize this transformation, which effectively removes distillation-relevant information while preserving output utility. Extensive experiments across multiple LLMs and strong distillation algorithms demonstrate that the proposed method significantly degrades distillation performance while preserving task accuracy, effectively protecting models' intellectual property.

</details>

### 13. Stealthy Reasoning Protection: Preventing Unauthorized Transfer of LLM Reasoning Ability

📝 [OpenReview](https://openreview.net/forum?id=8QvRuKCyPD)　📅 2026-01

**关键词**：`defense`、`reasoning-trace protection`、`distillation resistance`

- 🎯 **研究动机**：推理轨迹可被蒸馏窃取，大模型能力转移难阻止
- 🔬 **研究方法**：UREdit嵌入不可感知字符并做样本级与token级选择
- 📌 **结论**：不干扰正常阅读下抑制推理能力迁移

### 14. Progressive Category-Aware Anti-Distillation

🌐 [Project](https://doi.org/10.1016/j.engappai.2026.114950)　📅 2026

**关键词**：`defense`、`model-output protection`、`distillation resistance`

- 🎯 **研究动机**：现有反蒸馏忽略类别间暗知识的泄漏
- 🔬 **研究方法**：以类别原型关系矩阵、对称JS散度与课程学习逐步移除类间相关性
- 📌 **结论**：跨架构与蒸馏设置优于基线，teacher性能下降低于2.2%

### 15. Information-Preserving Reformulation of Reasoning Traces for Antidistillation

📄 [arXiv](https://arxiv.org/abs/2510.11545) · 📝 [OpenReview](https://openreview.net/forum?id=SFMJPriDVw)　📅 2025-10　🏷 ICLR 2026

**关键词**：`defense`、`reasoning-trace protection`、`distillation resistance`

👤 **作者**：Jiayu Ding、Lei Cui、Li Dong、Nanning Zheng、Furu Wei

- 🎯 **研究动机**：公开推理链易被未授权蒸馏，而以摘要替代又剥夺用户可读的中间信息，存在两难
- 🔬 **研究方法**：PART 利用人类理解与 LLM 蒸馏利用方式的差异，删除 self-talk 并重排子结论，由小型辅助模型执行重写
- 📌 **结论**：重写后的 trace 对不同规模学生模型的蒸馏持续破坏，32B 学生在 AIME 2024 上从 54.17 降至 46.88（13.5% 降幅）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Large Language Models (LLMs) show that extending the length of reasoning chains significantly improves performance on complex tasks. While revealing these reasoning traces helps users better follow, verify, and learn from the model's problem-solving process, it also makes them highly vulnerable to unauthorized distillation. To mitigate this risk, proprietary model providers often adopt aggressive protection strategies, such as replacing detailed reasoning with brief summaries, which deprive users of valuable intermediate information. To address this trade-off, we propose PART, an information-preserving antidistillation reformulation of reasoning traces. Motivated by the difference between how humans understand reasoning traces and how LLMs exploit them for supervised fine-tuning, we design a simple but effective two-step reformulation: removing self-talk behaviors and reordering sub-conclusions. A small auxiliary model is trained to perform this reformulation, incurring minimal computational overhead. Extensive experiments demonstrate that PART consistently disrupts distillation across student models of different sizes and types on various reasoning benchmarks. For instance, when training on reformulated traces, even the performance of a large 32B student model decreases from 54.17 to 46.88 on AIME 2024, corresponding to a 13.5% degradation.

</details>

### 16. DOGe: Defensive Output Generation for LLM Protection Against Knowledge Distillation

📄 [arXiv](https://arxiv.org/abs/2505.19504) · 📝 [OpenReview](https://openreview.net/forum?id=9nGA24YgNb)　📅 2025-05　🏷 ICLR 2026

**关键词**：`defense`、`model-output protection`、`distillation resistance`

👤 **作者**：Pingzhi Li、Zhen Tan、Mohan Zhang、Huaizhi Qu、Huan Liu、Tianlong Chen

- 🎯 **研究动机**：竞争者可仅凭观察输出蒸馏专有 LLM，水印只能事后取证，现有防御假设学生模仿 logits
- 🔬 **研究方法**：提出 DOGe，仅微调 teacher 最后一层线性层并配合对抗损失，使输出对合法用户准确而对蒸馏者误导
- 📌 **结论**：teacher 性能保持的同时，从防御输出蒸馏的学生模型性能灾难性下降

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) represent substantial intellectual and economic investments, yet their effectiveness can inadvertently facilitate model imitation via knowledge distillation (KD). In practical scenarios, competitors can distill proprietary LLM capabilities by simply observing publicly accessible outputs, akin to reverse-engineering a complex performance by observation alone. Existing protective methods like watermarking only identify imitation post-hoc, while other defenses assume the student model mimics the teacher's internal logits, rendering them ineffective against distillation purely from observed output text. This paper confronts the challenge of actively protecting LLMs within the realistic constraints of API-based access. We introduce an effective and efficient Defensive Output Generation (DOGe) strategy that subtly modifies the output behavior of an LLM. Its outputs are accurate and useful for legitimate users, yet are designed to be misleading for distillation, significantly undermining imitation attempts. We achieve this by fine-tuning only the final linear layer of the teacher LLM with an adversarial loss. This targeted training approach anticipates and disrupts distillation attempts during inference time. Our experiments show that, while preserving the performance of the teacher model, student models distilled from the defensively generated outputs demonstrate catastrophically reduced performance, demonstrating DOGe as a practical safeguard against KD-based model imitation.

</details>

### 17. Antidistillation Sampling

📄 [arXiv](https://arxiv.org/abs/2504.13146) · 📝 [OpenReview](https://openreview.net/forum?id=Vo2UHqMu8t) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/aad5e2a483869d9ba3fab491686c3bf2-Abstract-Conference.html)　📅 2025-04　🏷 NeurIPS 2025

**关键词**：`defense`、`reasoning-trace protection`、`defensive sampling`

👤 **作者**：Yash Savani、…、J. Zico Kolter

- 🎯 **研究动机**：前沿模型的推理痕迹易被蒸馏窃取，需要不损性能的防护手段
- 🔬 **研究方法**：提出 antidistillation sampling，策略性修改 next-token 概率分布以毒化推理痕迹
- 📌 **结论**：推理痕迹对蒸馏显著失效，同时保留模型实用效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Frontier models that generate extended reasoning traces inadvertently produce rich token sequences that can facilitate model distillation. Recognizing this vulnerability, model owners may seek sampling strategies that limit the effectiveness of distillation without compromising model performance. Antidistillation sampling provides exactly this capability. By strategically modifying a model's next-token probability distribution, antidistillation sampling poisons reasoning traces, rendering them significantly less effective for distillation while preserving the model's practical utility. For further details, see https://antidistillation.com.

</details>

### 18. Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot

📄 [arXiv](https://arxiv.org/abs/2606.15810)　📅 2026-06

**关键词**：`defense`、`model extraction`、`knowledge honeypot`、`query-budget diversion`

👤 **作者**：Yuyang Dai、Yushun Dong

- 🎯 **研究动机**：LLM API 面临模型抽取攻击，已有防御要么介入太晚要么损害合法用户体验
- 🔬 **研究方法**：提出 Knowledge Trap：通过 Honeypot Knowledge Graph 与面包屑引导探索，把攻击者的有限查询预算消耗在下游价值极低的知识上
- 📌 **结论**：医疗与金融域上代理 Agreement 平均降低 6.2% 且不影响合法用户准确率，优于有可测用户影响的防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models deployed as commercial APIs are vulnerable to model extraction attacks, while existing defenses either act too late or degrade utility for legitimate users. We propose \textbf{Knowledge Trap}, a defense that redirects extraction attacks toward low-transferability knowledge through a \emph{Honeypot Knowledge Graph} (HKG) and breadcrumb-guided exploration. Instead of blocking queries or perturbing outputs, Knowledge Trap consumes the attacker's limited query budget on knowledge with negligible downstream utility while preserving benign-user performance. Experiments in medical and financial domains show that Knowledge Trap reduces surrogate Agreement by 6.2\% on average without degrading legitimate-user accuracy, outperforming existing defenses that impose measurable user impact. These results suggest that defending knowledge-space traversal is a practical direction for mitigating LLM extraction attacks.

</details>

### 19. An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic

📄 [arXiv](https://arxiv.org/abs/2606.05725)　📅 2026-06

**关键词**：`detection`、`model extraction`、`traffic window`、`distribution test`

👤 **作者**：Shuze Liu、Qianwen Guo、Yushun Dong

- 🎯 **研究动机**：LLM API 的模型抽取威胁下，单条抽取查询与良性请求难区分，已有评估局限于单查询异常评分或纯良性-攻击者设定
- 🔬 **研究方法**：把监测形式化为良性校准的流量窗口分布检验：将查询嵌入语义空间，用 MMD 检验聚合分布与历史良性流量的偏移，阈值仅由良性-良性对比设定
- 📌 **结论**：14 对攻击者-正常查询上 MMD 达 0.3% 良性 FPR、100% 纯攻击者 TPR、90.5% 平均 TPR 与 95.1% 平衡准确率，优于 PRADA/SEAT 等基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed through hosted APIs, making model extraction a practical threat to model ownership and service security. Individual extraction queries often resemble benign requests, while existing evaluations often focus on single-query anomaly scoring or pure benign-versus-attacker user settings. We formulate model extraction monitoring as benign-calibrated traffic-window distribution testing: embed incoming queries into a semantic space and test whether their aggregate distribution deviates from historical benign traffic. We instantiate this formulation with maximum mean discrepancy (MMD), using only benign-vs-benign comparisons to set the decision threshold. We evaluate on fourteen attacker-normal query pairs from four extraction scenarios and compare with adapted PRADA, SEAT, CAP, DATE, marginal Mahalanobis, and pseudo-class energy baselines. Across three random seeds, MMD achieves 0.3% benign FPR, 100.0% pure-attacker TPR, 90.5% average TPR over attacker fractions, and 95.1% balanced accuracy. These results show that benign-calibrated distribution testing is a strong empirical baseline for model extraction detection in both user-level and mixed multi-user LLM API traffic.

</details>

### 20. Executable but Unlearnable: Designing Code that Resists LLM-Based Learning

🌐 [Project](https://2026.aiwareconf.org/details/aiware-2026-papers/11/Executable-but-Unlearnable-Designing-Code-That-Resists-LLM-Based-Learning)　📅 2026-07

**关键词**：`defense`、`code-data protection`、`unlearnable data`、`code protection`

- 🎯 **研究动机**：公开代码会被模型无授权学习，缺可执行前提下的保护手段
- 🔬 **研究方法**：设计Statistical Opacity使代码人类可读、机器可执行但抑制神经模式提取
- 📌 **结论**：证明可执行性与可学习性可分离，构成软件保护新原语

### 21. To See is Not to Learn: Protecting Multimodal Data from Unauthorized Fine-Tuning of Large Vision-Language Model

📄 [arXiv](https://arxiv.org/abs/2605.14291)　📅 2026-05

**关键词**：`defense`、`multimodal-data protection`、`multimodal protection`

👤 **作者**：Chengshuai Zhao、Zhen Tan、Dawei Li、Zhiyuan Yu、Huan Liu

- 🎯 **研究动机**：机器遗忘与水印都是侵权后补救，数据所有者缺乏免被 LVLM 未授权微调的事前防护
- 🔬 **研究方法**：MMGuard 注入不可感知扰动制造优化捷径使模型过拟合噪声，再以跨模态绑定破坏把注意力转移与训练目标建立虚假关联，集成学习增强跨模型迁移
- 📌 **结论**：九个开源 LVLM、六个数据集上白盒、灰盒与黑盒威胁模型均实现有效、隐蔽且鲁棒的保护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of Large Vision-Language Models (LVLMs) is increasingly accompanied by unauthorized scraping and training on multimodal web data, posing severe copyright and privacy risks to data owners. Existing countermeasures, such as machine unlearning and watermarks, are inherent post-hoc approaches that act only after intellectual property infringement has already occurred. In this work, we propose MMGuard to empower data owners to proactively protect their multimodal data against unauthorized LVLM fine-tuning. MMGuard generates unlearnable examples by injecting human-imperceptible perturbations that actively exploit the learning dynamics of LVLMs. By minimizing the training loss, the perturbation creates an optimization shortcut, causing the model to overfit to the noise and thereby degrading downstream performance when the perturbation is absent during inference. To further strengthen this defense, MMGuard introduces a cross-modal binding disruption, strategically shifting LVLM attention to enforce a spurious correlation between the noise and the training target with theoretical guarantees. Enhanced by an ensemble learning strategy for cross-model transferability, MMGuard is evaluated against nine open-source LVLMs across six datasets. Our comprehensive results demonstrate effective, stealthy, and robust protection under white-box, gray-box, and black-box threat models, establishing a mechanistic advantage in proactively defending against aggressive fine-tuning exploitation.

</details>

### 22. Rendering Data Unlearnable by Exploiting LLM Alignment Mechanisms

📄 [arXiv](https://arxiv.org/abs/2601.03401) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1885/)　📅 2026-01　🏷 ACL 2026

**关键词**：`defense`、`training-data protection`、`unlearnable data`、`alignment mechanism`、`machine unlearning`、`knowledge removal`

👤 **作者**：Ruihan Zhang、Jun Sun

- 🎯 **研究动机**：黑盒设定下防止专有或个人数据被 LLM 未经授权学习，缺乏数据级防护手段
- 🔬 **研究方法**：Disclaimer Injection 在文本中注入精心设计的对齐触发免责声明：微调此类数据会持续激活对齐相关层，使对齐约束压过任务学习
- 📌 **结论**：在受保护数据上训练的模型性能系统性大幅退化，为 LLM 规模数据不可学习提供首个无需访问训练管线的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly trained on massive, heterogeneous text corpora, raising serious concerns about the unauthorised use of proprietary or personal data during model training. In this work, we address the problem of data protection against unwanted model learning in a realistic black-box setting. We propose Disclaimer Injection, a novel data-level defence that renders text unlearnable to LLMs. Rather than relying on model-side controls or explicit data removal, our approach exploits the models' own alignment mechanisms: by injecting carefully designed alignment-triggering disclaimers to prevent effective learning. Through layer-wise analysis, we find that fine-tuning on such protected data induces persistent activation of alignment-related layers, causing alignment constraints to override task learning even on common inputs. Consequently, models trained on such data exhibit substantial and systematic performance degradation compared to standard fine-tuning. Our results identify alignment behaviour as a previously unexplored lever for data protection and, to our knowledge, present the first practical method for restricting data learnability at LLM scale without requiring access to or modification of the training pipeline.

</details>

### 23. Towards Operationalizing Right to Data Protection

📄 [arXiv](https://arxiv.org/abs/2411.08506) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.416/)　📅 2024-11　🏷 ACL 2025

**关键词**：`defense`、`training-data protection`、`unlearnable data`

👤 **作者**：Abhinav Java、Simra Shahid、Chirag Agarwal

- 🎯 **研究动机**：文本被无差别抓取训练引发 GDPR 合规问题，现有 unlearnable data 多面向图像且需目标模型知识
- 🔬 **研究方法**：RegText 向文本数据注入不可感知的虚假相关性，使其不可学习且不损语义
- 📌 **结论**：可限制 GPT-4o、Llama 等模型学习该数据，测试准确率跌破零样本水平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The widespread practice of indiscriminate data scraping to fine-tune language models (LMs) raises significant legal and ethical concerns, particularly regarding compliance with data protection laws such as the General Data Protection Regulation (GDPR). This practice often results in the unauthorized use of personal information, prompting growing debate within the academic and regulatory communities. Recent works have introduced the concept of generating unlearnable datasets (by adding imperceptible noise to the clean data), such that the underlying model achieves lower loss during training but fails to generalize to the unseen test setting. Though somewhat effective, these approaches are predominantly designed for images and are limited by several practical constraints like requiring knowledge of the target model. To this end, we introduce RegText, a framework that injects imperceptible spurious correlations into natural language datasets, effectively rendering them unlearnable without affecting semantic content. We demonstrate RegText's utility through rigorous empirical analysis of small and large LMs. Notably, RegText can restrict newer models like GPT-4o and Llama from learning on our generated data, resulting in a drop in their test accuracy compared to their zero-shot performance and paving the way for generating unlearnable text to protect public data.

</details>

### 24. OpenStamp: A Watermark for Open-Source Language Models

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

### 25. Asking Back: Interaction-Layer Antidistillation Watermarks

📄 [arXiv](https://arxiv.org/abs/2605.16462)　📅 2026-05

**关键词**：`tool`、`interaction watermark`、`behavioral marker`、`distillation attribution`

👤 **作者**：Guang Yang、Amir Ghasemian、Fengchen Liu、Zhong Wang、Ninareh Mehrabi、Homa Hosseinmardi

- 🎯 **研究动机**：作用于输出 token 的反蒸馏水印可被 paraphrase 攻击者剥离而不损失底层知识
- 🔬 **研究方法**：交互层水印：系统 prompt 间歇诱导行为标记（追问、低频变体、声明式复述），无感知蒸馏者会继承该行为，经黑盒查询与 LLM-as-judge（Cohen's kappa 0.84/0.78）审计
- 📌 **结论**：63 个 LoRA 学生上标记相对保真 88.9%（Gemma）、80.9%（OLMo）、45.2%（Qwen）；DIPPER 改写下 OLMo 保水印甚至超教师自身；预注册人体实验显示体验与基线无差异

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Detecting unauthorized knowledge distillation from a deployed LLM API is hard because the defender controls neither the attacker's training pipeline nor the next-token logits. Existing defenses operate on the teacher's output tokens -- biasing the next-token distribution (green-list watermarks, cryptographic schemes, antidistillation sampling) or rewriting outputs after generation. Recent work shows a paraphrasing attacker can strip these signals without losing the underlying knowledge. We propose interaction-layer antidistillation watermarks, which move the trace one layer higher, into the teacher's interaction behavior: the defender wraps the teacher with a system prompt that intermittently induces a behavioral marker -- an explicit follow-up question, a low-frequency variant, or a declarative restatement. An oblivious distiller inherits the behavior, and the defender audits via black-box queries with a human-validated LLM-as-judge (Cohen's kappa = 0.84/0.78 on strong/style rubrics). Across 63 LoRA-distilled students under a Llama-3.3-70B-Instruct teacher (35,343 judged samples), behavioral watermarks transfer at 88.9% (Gemma) / 80.9% (OLMo) / 45.2% (Qwen) relative fidelity (H1, H2). Under non-adaptive DIPPER paraphrasing, robustness decomposes into a teacher-self ceiling (about 66.4%) and student-relative retention of 21-112%, with OLMo preserving the watermark above the teacher itself (H3, F-Amp). Low-density (about 20%) explicit and implicit declarative variants transfer above per-family baseline (H4, F-Style). An N=20 in-lab study (pre-registered Latin-square) shows all marker variants within 0.22 Likert step of baseline; TOST, Friedman, and Bonferroni-Wilcoxon support H5. The interaction layer is a viable design locus for antidistillation watermarking, complementary to token-, model-, and reasoning-trace-layer defenses.

</details>

### 26. TextSeal: A Localized LLM Watermark for Provenance & Distillation Protection

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

### 27. Antidistillation Fingerprinting

📄 [arXiv](https://arxiv.org/abs/2602.03812) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63624)　📅 2026-02　🏷 ICML 2026

**关键词**：`tool`、`analysis`、`distillation attribution`、`ownership verification`、`model ownership`、`mechanistic analysis`

👤 **作者**：Yixuan Even Xu、…、J. Zico Kolter

- 🎯 **研究动机**：现有蒸馏指纹技术依赖启发式扰动，在生成质量与指纹强度间存在陡峭权衡
- 🔬 **研究方法**：ADFP 把指纹目标与学生模型学习动力学对齐，用代理模型识别并采样能最大化学生微调后指纹可检测性的 token
- 📌 **结论**：在 GSM8K、OASST1、MBPP 上实现 Pareto 改进：检测置信更强且效用损失极小，学生架构未知亦有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model distillation enables efficient emulation of frontier large language models (LLMs), creating a need for robust mechanisms to detect when a third-party student model has trained on a teacher model's outputs. However, existing fingerprinting techniques that could be used to detect such distillation rely on heuristic perturbations that impose a steep trade-off between generation quality and fingerprinting strength, often requiring significant degradation of utility to ensure the fingerprint is effectively internalized by the student. We introduce antidistillation fingerprinting (ADFP), a principled approach that aligns the fingerprinting objective with the student's learning dynamics. Building upon the gradient-based framework of antidistillation sampling, ADFP utilizes a proxy model to identify and sample tokens that directly maximize the expected detectability of the fingerprint in the student after fine-tuning, rather than relying on the incidental absorption of the un-targeted biases of a more naive watermark. Experiments on GSM8K, OASST1, and MBPP demonstrate that ADFP achieves a significant Pareto improvement over state-of-the-art baselines, yielding stronger detection confidence with minimal impact on utility across mathematical reasoning, dialogue, and code generation, even when the student model's architecture is unknown.

</details>

### 28. What Does It Mean to Break a Distillation Defense?

📄 [arXiv](https://arxiv.org/abs/2606.25059)　📅 2026-06

**关键词**：`analysis`、`model-output protection`、`attack-defense evaluation`

👤 **作者**：Lena Libon、Pura Peetathawatchai、Michael Aerni、Daniel Paleka、Florian Tramèr

- 🎯 **研究动机**：输出扰动型抗蒸馏防御缺乏共享威胁模型，评估结论依赖隐含假设，可能造成虚假安全感
- 🔬 **研究方法**：提出三维威胁模型框架：查询预算、数据预算与刻画攻击者-API 交互方式的接口画像，以 antidistillation sampling 为案例研究
- 📌 **结论**：防御是否有效完全取决于假设的威胁模型；后续工作与治理框架应显式指定并在三维度上压力测试攻击者能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Black-box LLMs (accessible only via API) are vulnerable to distillation attacks, in which an attacker queries the model and trains a student on its outputs. A recent line of work proposes output perturbation defenses that modify the teacher's output to reduce student performance while preserving utility for legitimate users. As a relatively new family of approaches, output perturbation defenses lack a shared threat model, making it difficult to compare them, reason about composing them with other attacks, or evaluate their robustness against realistic adversaries. This underspecification matters beyond technical evaluation: when defenses are deployed to protect intellectual property or justify regulatory compliance, an imprecise threat model can create a false sense of security. We propose a threat model framework that describes attackers along three dimensions: a query budget, a data budget, and an interface profile that captures how attackers interact with the API. Using antidistillation sampling as a case study, we show that whether the defense is considered effective depends on the assumed threat model. We argue that future work on distillation defenses, along with any governance or policy frameworks built around them, should explicitly specify and stress-test attacker capabilities along our three dimensions.

</details>

### 29. The Distillation Game: Adaptive Attacks & Efficient Defenses

📄 [arXiv](https://arxiv.org/abs/2605.22737)　📅 2026-05

**关键词**：`analysis`、`model-output protection`、`attack-defense evaluation`

👤 **作者**：Youssef Allouah、Mahdi Haghifam、Sanmi Koyejo、Reza Shokri

- 🎯 **研究动机**：蒸馏攻击使模型提供方陷入效用-可模仿权衡，被动学生评测会高估防御
- 🔬 **研究方法**：把效用约束 teacher 与自适应 student 建模为极小极大博弈；从样本价值代理导出 PoE——生成时组合 teacher 与代理学生的纯前向防御
- 📌 **结论**：自适应评估揭示大的 passive-adaptive 差距；强评估下昂贵防御与 PoE 的表观差距明显缩小，PoE 更便宜且保留更高质量推理轨迹——反蒸馏进展应按自适应学生评判

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Distillation attacks create a deployment trade-off for model providers: the same outputs that make a model more useful can also make it easier to imitate. We study this trade-off through a minimax game between a utility-constrained teacher and an adaptive student. Our framework yields tractable one-sided response rules: an adaptive evaluation rule in which the student reweights high-value examples, and a teacher-side defense template that suppresses outputs most useful for distillation. From a cheap proxy for example value, we derive Product-of-Experts (PoE), a simple forward-pass-only defense that combines the teacher with a proxy student during generation. Empirically, adaptive evaluation reveals a large passive--adaptive gap: on state-of-the-art defenses, adaptive students recover substantially more capability than passive evaluation suggests on GSM8K and MATH. Under this stronger evaluation, the apparent robustness gap between expensive defenses and PoE narrows considerably, while PoE remains substantially cheaper and preserves higher-quality reasoning traces. Overall, our results suggest that strong distillation remains difficult to stop, and that progress on antidistillation should be judged against adaptive students rather than passive ones. Our code is available at: https://github.com/ysfalh/distillation-game.

</details>

### 30. A Survey on Model Extraction Attacks and Defenses for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2506.22521)　📅 2025-06

**关键词**：`survey`、`model extraction`、`functionality stealing`、`defense taxonomy`

👤 **作者**：Kaixiang Zhao、Lincan Li、Kaize Ding、Neil Zhenqiang Gong、Yue Zhao、Yushun Dong

- 🎯 **研究动机**：LLM 模型提取攻击与防御缺乏系统分类与专用评估指标
- 🔬 **研究方法**：提出功能提取、训练数据提取与 prompt 目标攻击三类分类法，按模型保护、数据隐私与 prompt 防御组织防御并定义专用指标
- 📌 **结论**：指出现有方法的关键局限，提出整合攻击与兼顾安全-效用的自适应防御等方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model extraction attacks pose significant security threats to deployed language models, potentially compromising intellectual property and user privacy. This survey provides a comprehensive taxonomy of LLM-specific extraction attacks and defenses, categorizing attacks into functionality extraction, training data extraction, and prompt-targeted attacks. We analyze various attack methodologies including API-based knowledge distillation, direct querying, parameter recovery, and prompt stealing techniques that exploit transformer architectures. We then examine defense mechanisms organized into model protection, data privacy protection, and prompt-targeted strategies, evaluating their effectiveness across different deployment scenarios. We propose specialized metrics for evaluating both attack effectiveness and defense performance, addressing the specific challenges of generative language models. Through our analysis, we identify critical limitations in current approaches and propose promising research directions, including integrated attack methodologies and adaptive defense mechanisms that balance security with model utility. This work serves NLP researchers, ML engineers, and security professionals seeking to protect language models in production environments.

</details>

### 31. Distillation Traps and Guards: A Calibration Knob for LLM Distillability

🎓 [Official](https://aclanthology.org/2026.acl-long.908/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`uncertainty calibration`、`selective prediction`、`deployment shift`、`model provenance`、`watermarking`

👤 **作者**：Weixiao Zhan、Yongcheng Jing、Leszek Rutkowski、Dacheng Tao

- 🎯 **研究动机**：知识蒸馏会不可预测地失败并构成模型泄露风险——尾部噪声、off-policy 不稳定与师生差距扭曲训练信号
- 🔬 **研究方法**：首个经强化微调控制教师可蒸馏性的事后校准：目标组合任务效用、KL 锚与跨 tokenizer 校准奖励
- 📌 **结论**：可蒸馏校准教师的学生超越 SFT 与 KD 基线；不可蒸馏校准教师保留自身性能却使学生崩溃，成为 KD 质量与 IP 保护的实用旋钮

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge distillation (KD) transfers capabilities from large language models (LLMs) to smaller students, yet it can fail unpredictably and also underpins model leakage risks. Our analysis revealed several distillation traps: tail noise, off-policy instability, and, most fundamentally, the teacher–student gap, that distort training signals. These traps manifest as overconfident hallucinations, self-correction collapse, and local decoding degradation, causing distillation to fail. Motivated by these findings, we propose a post-hoc calibration method that, to the best of our knowledge, for the first time enables control over a teacher’s distillability via reinforcement fine-tuning (RFT). Our objective combines task utility, KL anchor, and across-tokenizer calibration reward. This makes distillability a practical safety lever for foundation models, connecting robust teacher–student transfer with deployment-aware model protection. Experiments across math, knowledge QA, and instruction-following tasks show that students distilled from distillable calibrated teachers outperform SFT and KD baselines, while undistillable calibrated teachers retain their task performance but cause distilled students to collapse, offering a practical knob for both better KD and model IP protection.

</details>
