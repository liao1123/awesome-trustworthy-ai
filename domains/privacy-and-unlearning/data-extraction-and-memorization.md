## 研究方向

研究模型在训练、微调、检索和个性化过程中记住并泄露敏感数据的风险，覆盖 membership inference、training-data extraction、gradient/feature inversion 与 de-anonymization；重点区分真实记忆、可推断信息和评测器造成的假阳性。

## 研究脉络

- **攻击面建立：** 早期工作以 membership inference 和 gradient inversion 判断单条记录是否参与训练，并逐步扩展到生成模型、RAG 与多模态系统。
- **规模化抽取：** 攻击从成员判断发展到逐字抽取、whole-corpus reconstruction、身份归因和跨组件数据外传。
- **审计与缓解：** canary、memorization localization 与 attack-driven benchmark 开始联合报告泄漏强度、查询预算和误报，并直接复测具体抽取攻击。
- **当前边界：** 模型输出中的公开知识、合理推断与训练记忆仍难严格区分，跨版本和真实 API 的可复现证据尤其不足。

## PII、身份归因与去匿名化

### 1. AIM: Anchor Identity Features, Then Match for Multimodal Large Language Model Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.28312) · 🤗 [Model](https://huggingface.co/WonjunLee/AIM_MLLM_Unlearning)　📅 2026-08

**关键词**：`defense`、`analysis`、`identity memorization`、`privacy deletion`、`retain-free MLLM`、`MLLM identity unlearning`

👤 **作者**：Wonjun Lee、Jaehyuk Jang、Kangwook Ko、Hee-Seon Kim、Changick Kim

- 🎯 **研究动机**：MLLM 会记忆微调数据中的身份事实带来隐私删除需求，但现有 unlearning 方法多假定删除时可访问 retain 图像或真值答案，现实中不可得
- 🔬 **研究方法**：发现身份问题与视觉感知问题在微调 hidden state 中分区且组织方式不同（按人 vs 按题型）；提出两阶段 AIM：以通用视觉 prompt 锚定身份遗忘目标，再在 Fisher 约束下把 vision encoder 匹配到该目标
- 📌 **结论**：无需 retain 数据即实现有竞争力的身份遗忘，同时保留未删除身份、既有知识与同图像视觉感知

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) can memorize identity-specific facts about people in their fine-tuning data, creating privacy risks when a person requests deletion. Existing MLLM unlearning methods often assume access to retain images or ground-truth answers during deletion, which is unrealistic in many practical scenarios. We study identity unlearning when retain images are unavailable at deletion time. Our analysis shows that identity and visual-perception questions occupy distinct regions in fine-tuned hidden states and are organized differently: identity questions cluster by person, whereas perception questions cluster by question type. This suggests that identity knowledge can be suppressed without erasing general visual perception. Building on this observation, we propose AIM, a two-stage method that anchors an identity-forgetting target with a universal visual prompt and then matches the vision encoder to that target under a Fisher-based constraint. Extensive experiments show that AIM achieves competitive identity forgetting while preserving non-deleted identities, prior knowledge, and visual perception on the same images.

</details>

### 2. Do LLMs Really Memorize Personally Identifiable Information? Revisiting PII Leakage with a Cue-Controlled Memorization Framework

🎓 [Official](https://aclanthology.org/2026.acl-long.1560/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`tool`、`privacy leakage`、`memorization`、`data extraction`、`training-data memorization`

👤 **作者**：Xiaoyu Luo、Yiyi Chen、Qiongxiu Li、Johannes Bjerva

- 🎯 **研究动机**：PII 重建成功常被当作记忆证据，但可能由提示诱导的泛化或模式补全驱动
- 🔬 **研究方法**：形式化 Cue-Resistant Memorization 框架：显式条件化提示-目标重叠线索、在低词汇线索条件下评测，跨 32 种语言与多种记忆范式大规模重评
- 📌 **结论**：逐字补全与联想重建的表面有效性主要由直接表层线索驱动，控制线索后成功率大幅衰减；无线索生成与成员推断真阳性率极低——既往 PII 泄露更好解释为线索驱动行为

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been reported to “leak” Personally Identifiable Information (PII), with successful PII reconstruction often interpreted as evidence of memorization. We propose a principled revision of memorization evaluation for LLMs, arguing that PII leakage should be evaluated under low lexical cue conditions, where target PII cannot be reconstructed through prompt-induced generalization or pattern completion. We formalize Cue-Resistant Memorization (CRM) as a cue-controlled evaluation framework and a necessary condition for valid memorization evaluation, explicitly conditioning on prompt-target overlap cues. Using CRM, we conduct a large-scale multilingual re-evaluation of PII leakage across 32 languages and multiple memorization paradigms. Revisiting reconstruction-based settings, including verbatim prefix-suffix completion and associative reconstruction, we find that their apparent effectiveness is driven primarily by direct surface-form cues rather than by true memorization. When such cues are controlled for, reconstruction success diminishes substantially. We further examine cue-free generation and membership inference, both of which exhibit extremely low true positive rates. Overall, our results suggest that previously reported PII leakage is better explained by cue-driven behavior than by genuine memorization, highlighting the importance of cue-controlled evaluation for reliably quantifying privacy-relevant memorization in LLMs.

</details>

### 3. De-Anonymization at Scale via Tournament-Style Attribution

🎓 [Official](https://aclanthology.org/2026.acl-long.1489/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`privacy leakage`、`memorization`、`data extraction`、`LLM privacy`、`data leakage`

👤 **作者**：Lirui Zhang、Huishuai Zhang

- 🎯 **研究动机**：LLM 可把匿名文档链接到作者，威胁双盲评审等匿名场景，数万候选规模下的去匿名能力未量化
- 🔬 **研究方法**：DAS 锦标赛式序贯策略：候选随机分组、LLM 选出最可能与查询同作者的文本、迭代重查幸存者产出 top-k，配密集检索预筛与多轮多数投票聚合
- 📌 **结论**：从数万候选中恢复同作者文本的准确率远超随机，构成现实隐私风险；在 Enron 邮件与博客基准上超越先前方法的准确率与扩展性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs rapidly advance and enter real-world use, their privacy implications are increasingly important. We study an authorship de-anonymization threat: using LLMs to link anonymous documents to their authors, potentially compromising settings such as double-blind peer review. We propose De-Anonymization at Scale (DAS), a large-language-model–based method for attributing authorship among tens of thousands of candidate texts. DAS uses a sequential progression strategy: it randomly partitions the candidate corpus into fixed-size groups, prompts an LLM to select the text most likely written by the same author as a query text, and iteratively re-queries the surviving candidates to produce a ranked top-k list. To make this practical at scale, DAS adds a dense-retrieval prefilter to shrink the search space and a majority-voting–style aggregation over multiple independent runs to improve robustness and ranking precision. Experiments on anonymized review data show DAS can recover same-author texts from pools of tens of thousands with accuracy well above chance, demonstrating a realistic privacy risk for anonymous platforms. On standard authorship benchmarks (Enron emails and blog posts), DAS also improves both accuracy and scalability over prior approaches, highlighting a new LLM-enabled de-anonymization vulnerability.

</details>

### 4. A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage

📄 [arXiv](https://arxiv.org/abs/2504.21035) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`text sanitization`、`semantic re-identification`、`privacy leakage`

👤 **作者**：Rui Xin、…、Pang Wei Koh

- 🎯 **研究动机**：文本脱敏评测止于表层标识符，语义层面的再识别风险未被评估
- 🔬 **研究方法**：对脱敏文本发起语义再识别攻击，考察超出表层泄漏的隐私风险
- 📌 **结论**：表层脱敏后仍可被语义线索重新识别，形成虚假隐私感

### 5. Extracting Forgotten Prompts from Targeted Unlearned Models

📄 [arXiv](https://arxiv.org/abs/2609.03662)　📅 2026-09

**关键词**：`attack`、`targeted extraction`、`residual memorization`、`unlearning audit`、`unlearning leakage`、`relearning`

👤 **作者**：Au Ashley Hoi-Ting、Meghdad Kurmanji、William F. Shen、Nicholas D. Lane、Ligang He

- 🎯 **研究动机**：现有 unlearning 攻击假设攻击者已知 forgotten prompt 而只恢复答案，prompt 本身可被提取这一盲点未被注意
- 🔬 **研究方法**：提出 Targeted Active Search：用 retained data 构造典型模板与实体池，在有限查询预算下选信息量最大的模板-实体对定位遗忘实体，再用实体实例化模板重建 forgotten prompt
- 📌 **结论**：三种 unlearning 方法、三个数据集与三个 LLM 上实体恢复 100%、最多重建 95% 的 forgotten prompt，查询数比朴素探测省 99.7%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent unlearning methods (e.g. NPO, DPO, LUNAR) make use of refusal alignment to suppress forgotten data. However, it has been shown that refusal responses might leave traces of unlearning, and recent attacks have been able to successfully recover some of the unlearned knowledge. In this paper, we uncover a new vulnerability. Existing attacks typically assume that the forgotten prompts are already known to the adversary and focus on recovering their answers. However, we show that the forgotten prompts themselves can be extracted by using the retained data and black-box access to the model. Our attack, Targeted Active Search (TAS), first identifies the forgotten entities by constructing canonical templates and entity pool, and selectively querying the model using the most informative template-entity pair under a limited query budget. Once the entities are identified, TAS instantiates prompt templates with those entities to probe the unlearned model and reconstruct the forgotten prompts. Experiments across three unlearning methods with three datasets and three LLMs shows that TAS recovers the forgotten entity with $100\%$ accuracy and reconstructs up to $95\%$ of forgotten prompts, all while using up to $99.7\%$ fewer queries than naive probing.

</details>

### 6. Extracting Knowledge from Tools in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.30288)　📅 2026-09

**关键词**：`attack`、`knowledge-based tool`、`tool-selection steering`、`source reconstruction`、`tool-mediated extraction`、`knowledge-source reconstruction`

👤 **作者**：Chuanchao Zang、…、Shanqing Guo

- 🎯 **研究动机**：Agent 通过工具调用访问知识库时，合法响应暴露的源内容可能被逐步重组还原，此风险未被系统研究
- 🔬 **研究方法**：提出 query-only 攻击 ToolSiphon：用 Tool Contrastive Analysis 引导查询命中目标工具、Evidence Chained Feedback 缓解参数压缩并扩大抽取覆盖
- 📌 **结论**：三类知识工具、六个数据集上平均恢复 74.3% 源记录（文本恢复 83.2%），无粗粒度信息时仍有 66.3%，并能绕过代表性防御与三个真实 Agent 平台

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents commonly use knowledge-based tools and access their underlying files, databases, and search indexes through tool invocation. This integration improves agents' ability to provide domain-specific services but also introduces the risk of tool-mediated knowledge extraction: source content exposed to an agent for legitimate responses may be progressively recovered from its outputs, enabling reconstruction of the knowledge source behind a target tool. This paper systematically investigates this risk and identifies two challenges introduced by tool invocation: tool-selection uncertainty, where an agent may invoke a competing tool instead of the target tool, and tool-argument compression, where fine-grained query information may be lost when the agent generates tool arguments. To tackle these challenges, we propose ToolSiphon, a query-only extraction attack that introduces two complementary signals: a target-discriminative signal, implemented through Tool Contrastive Analysis, to steer queries toward the target tool; and a response-grounded factual signal, implemented through Evidence Chained Feedback, to mitigate argument compression and progressively expand extraction coverage. Across three types of knowledge-based tools and six domain-specific datasets, ToolSiphon recovers 74.3% of source records on average when coarse-grained information about non-target tools is available, with 83.2% textual recovery and 90.2% semantic similarity. Even without such information, it recovers 66.3% of source records. ToolSiphon also remains effective against representative defenses and on three real-world agent platforms.

</details>

### 7. Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution

📄 [arXiv](https://arxiv.org/abs/2608.21656)　📅 2026-08

**关键词**：`defense`、`RAG prompt injection`、`context sanitization`、`database leakage`、`retrieved-context injection`、`keyword-grounded facts`

👤 **作者**：Ziliang Zhang、…、Sheng Zhong

- 🎯 **研究动机**：prompt injection 可误导 RAG 的检索器或生成器，暴露敏感数据库内容
- 🔬 **研究方法**：KFS-RAG 用 attention rollout 加因果扰动定位检索上下文中的关键影响词，引导辅助 LLM 生成 keyword-grounded facts 替换原始上下文，使生成器只基于净化证据工作
- 📌 **结论**：注入攻击下显著降低数据库泄漏风险，同时保持回答准确性与相关性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for combining large language models (LLMs) with external knowledge sources. However, RAG systems remain vulnerable to prompt injection attacks, which may mislead the retriever or generator to expose sensitive database contents. To address this issue, we propose KFS-RAG, a defense that mitigates information leakage by reformulating the retrieved context. Specifically, our method first identifies a small set of influential keywords from the retrieved context via an attention rollout plus a causal perturbation mechanism. These keywords are then used to guide an auxiliary LLM to generate a compact set of keyword-grounded facts from the retrieved passages. Finally, the original context is substituted with these curated facts, ensuring that the generator operates on sanitized evidence rather than the raw retrieved text. Experimental evaluations demonstrate that KFS-RAG significantly reduces the risk of database leakage under injection attacks while maintaining response accuracy and relevance. This work highlights a practical pathway toward building secure and trustworthy RAG systems.

</details>

### 8. Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.21606)　📅 2026-08

**关键词**：`benchmark`、`attack`、`capability recovery`、`adversarial prompting`、`unlearning robustness`、`unlearned-data recovery`

👤 **作者**：Ayush Gupta、…、Sadid Hasan

- 🎯 **研究动机**：现有 unlearning benchmark 只用干净非对抗查询评估，看似遗忘的信息能否经策略性提示恢复仍未知
- 🔬 **研究方法**：在 TOFU+Llama-3.2-3B-Instruct 上统一评估 prompt 式与微调式遗忘方法，对标准指标下的强者做对抗压力测试，并引入 LLM-as-judge 的 Attack Success Rate 指标
- 📌 **结论**：Forget Quality 超过 0.91 的方法对抗恢复 ASR 仍达 72.8–84.3%（接近未防护基线的 87.5%），而干净多语言改写仅测出 2.95% 泄漏——标准指标强不足以证明遗忘稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of targeted training data from a model while preserving its remaining capabilities, but evaluating whether such information has truly become inaccessible remains challenging. Existing benchmarks primarily assess unlearning under clean, non-adversarial queries, leaving open whether information that appears forgotten can still be recovered through strategic prompting. We address this gap through a unified evaluation of prompt-based and fine-tuning-based unlearning methods on TOFU using Llama-3.2-3B-Instruct, followed by an adversarial robustness evaluation of methods that perform strongly under standard metrics. We introduce Attack Success Rate (ASR), an LLM-as-judge metric that measures the fraction of adversarial responses whose leakage score exceeds $0.2$, and evaluate recovery across eight attack suites. Our results reveal a substantial gap between clean-query forgetting and adversarial robustness. Although several fine-tuning-based methods achieve Forget Quality above $0.91$, targeted information remains recoverable with ASRs between $72.8\%$ and $84.3\%$, close to the $87.5\%$ ASR of the unprotected base model. In contrast, clean multilingual reformulations yield only $2.95\%$ measured leakage. A manual audit further finds agreement between binary ASR decisions and human factual assessments in seven of ten cases, indicating that ASR provides a useful, though imperfect, signal of behavioral recoverability. These findings show that strong standard-metric performance alone is insufficient to establish robustness after unlearning and motivate adversarial stress-testing as a complementary component of unlearning evaluation.

</details>

### 9. Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data

📄 [arXiv](https://arxiv.org/abs/2608.21727)　📅 2026-08

**关键词**：`attack`、`benign RL fine-tuning`、`PII leakage`、`capability activation`、`PII extraction`、`memorization leakage`

👤 **作者**：Renfei Zhang、Niloofar Mireshghallah

- 🎯 **研究动机**：RLVR 被广泛用于提升推理，但其是否会改变模型泄露已记忆隐私信息的倾向缺乏研究
- 🔬 **研究方法**：在完全不含 PII 的良性事实上对 instruct 模型做 RL，再以姓名→邮箱定向探测与自由回忆两种 prompt 重新探测已记忆信息
- 📌 **结论**：DeepSeek-V3.1 上 verbatim recall@k 从 0.155 升至 0.370（2.4 倍），效应随模型规模增大且推理与拒答保持不变——攻击者无需隐私数据或隐私信号即可放大潜伏泄漏

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning with verifiable rewards (RLVR) is deployed to make models better at reasoning tasks, but its side effect on what models will divulge is under studied. Here we show that RLVR on facts increases extraction of personally identifiable information (PII) the instruct model had already memorized. We first confirm that instruct models have already memorized PII but leave them latent, rarely surfacing one when asked. We then apply RL on benign factual data that contains no PII of any kind, and re-probe: a targeted probe over name->email pairs, and an untargeted free-recall prompt that simply asks the model to list the addresses it knows. PII extraction rises sharply under both: on DeepSeek-V3.1, verbatim recall@k increases from 0.155 to 0.370, a 2.4x gain. The effect scales with model size: across three models spanning 8B to 671B parameters, absolute leakage is largest in the biggest model. Meanwhile model's reasoning abilities and refusal rates are retained, indicating that RL selectively changes which memorized information is accessible rather than broadly altering the model. In summary, memorized private data can be made markedly more extractable by training that never touches it. This gives an adversary a route to memorized data that requires no privacy-relevant training signal and no access to the data itself -- only the ability to fine-tune on something innocuous.

</details>

### 10. Don't Trust the AI Ecosystem: Analyzing Privacy Leakage in Compromised Open-Source Components

📄 [arXiv](https://arxiv.org/abs/2607.27886) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-07　🏷 ACM CCS 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`AI supply chain`、`training-time injection`

👤 **作者**：Jin-Seong Kim、…、Seok-Hwan Choi

- 🎯 **研究动机**：已有模型反演依赖训练后优化，受目标模型泛化瓶颈限制只能得到泛化特征，在高维数据上难以恢复具体身份
- 🔬 **研究方法**：提出 GradLock 训练时注入攻击：在被攻陷的供应链组件中用无状态确定性索引建立隔离数据保险库、动态梯度锁定防载荷在优化中退化，可从最终模型即时抽取像素级数据
- 📌 **结论**：MNIST、Imagenette、CelebA 上近无损重建（SSIM 约 1.0）且抽取 <1 秒，抗量化、剪枝与微调；93.3% 参与部署研究的用户未察觉恶意逻辑

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing model inversion (MI) attacks predominantly rely on post-training optimization to recover private data from model outputs. However, these methods are fundamentally constrained by the target model's generalization bottleneck, often yielding generic features rather than specific identities, particularly on high-dimensional datasets. In this paper, we introduce GradLock, a novel training-time injection attack that stealthily injects sensitive training data directly into the model parameters. Operating within a compromised supply chain context, GradLock leverages stateless deterministic indexing to establish isolated data vaults and employs dynamic gradient locking to prevent payload degradation during the optimization process. This mechanism allows the adversary to extract pixel-perfect data from the final model without retaining access to the training environment. Extensive experiments on MNIST, Imagenette, and CelebA demonstrate that GradLock achieves near-lossless reconstruction (SSIM ~ 1.0) and instant extraction (< 1.0s). Compared to existing training-time injection methods, our approach exhibits superior robustness against standard deployment optimizations, including quantization, pruning, and fine-tuning. Furthermore, a user deployment study reveals that 93.3% of participants failed to detect the malicious logic, highlighting a severe blind spot in the security of modern AI supply chains.

</details>

### 11. TrustCLIP: Learning Private Visual Features via Adversarial Reconstruction

📄 [arXiv](https://arxiv.org/abs/2607.04484) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/4310)　📅 2026-07　🏷 ECCV 2026

**关键词**：`defense`、`adversarial robustness`、`privacy leakage`、`memorization`、`feature inversion`、`visual privacy`

👤 **作者**：Nikos Athanasiou、…、Bugra Tekin

- 🎯 **研究动机**：生成模型的进步使视觉特征可被反演重建原图，带来严重隐私风险，已有防御依赖判别式隐私度量
- 🔬 **研究方法**：提出 TrustCLIP：把特征条件生成器显式当作隐私对抗者，学习编码器特征与下游模块间的投影，优化目标为劣化生成式重建同时保留下游所需信号
- 📌 **结论**：在常规分类与多模态 LLM 管线中一致降低生成式反演保真度并维持下游性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision and vision-language models rely on high-level visual representations that are increasingly used across recognition, retrieval, and multimodal reasoning pipelines. However, recent advances in generative modeling have shown that such features can often be inverted, enabling realistic reconstructions of the underlying image and raising significant privacy risks. We revisit this problem through the lens of reconstruction and propose TrustCLIP, a reconstruction-driven framework that treats a feature-conditioned generator as an explicit privacy adversary. TrustCLIP learns a projection between encoder features and downstream modules that is explicitly optimized to degrade the reconstructions produced by generative attackers while retaining the necessary signals for downstream tasks. Unlike prior defenses that rely on discriminative privacy metrics, TrustCLIP directly optimizes against a generative reconstruction attacker, targeting a threat not captured by standard evaluation protocols. We demonstrate its effectiveness in both conventional classification and multimodal large language model pipelines. Across these settings, TrustCLIP consistently reduces the fidelity of generative inversions while maintaining downstream task performance. Project page: https://atnikos.github.io/trustclip/

</details>

### 12. Seeing Through the Weights: Privacy Leakage in Scene Coordinate Regression

📄 [arXiv](https://arxiv.org/abs/2606.31164) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5226)　📅 2026-06　🏷 ECCV 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`model inversion`、`scene reconstruction`

👤 **作者**：Oleksii Nasypanyi、Jaemin Cho、Utku Ozbulak、Byungkon Kang、Francois Rameau

- 🎯 **研究动机**：场景坐标回归把场景隐式编码进网络参数，被认为天然保护隐私，该假设未被检验
- 🔬 **研究方法**：提出查询式攻击：用与目标场景无关的代理图像批量查询模型获得逐像素 3D 坐标，经小扰动下的稳定性筛选可靠点并累积恢复场景几何，再反演特征合成任意视角图像
- 📌 **结论**：室内外数据集上高保真重建训练环境大部分几何并恢复近似颜色外观，可暴露敏感场景元素，直接推翻 SCR 表示隐私保护的设计声明

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scene Coordinate Regression (SCR) methods are increasingly adopted for visual localization. In these approaches, the scene is implicitly encoded within a neural network that regresses a 3D world coordinate for each image pixel. Because the scene is represented only through the network parameters and not stored explicitly as images or maps, such methods are often assumed to be privacy-preserving. In this work, we show that this assumption is incorrect in practice. Specifically, we introduce a query-based attack that reconstructs the 3D geometry of the training environment from an SCR model under different levels of model access. To do so, we repeatedly query the model with batches of proxy images unrelated to the target scene to obtain dense pixel-wise 3D coordinates. Reliable points are identified through their stability under small input perturbations and can be further refined in a white-box setting. These stable points are accumulated across independent query batches to recover the scene geometry. From the recovered 3D representation, we also invert the network features to synthesize images from arbitrary viewpoints, revealing additional appearance information. Experiments on indoor and outdoor datasets demonstrate that substantial portions of training environments can be reconstructed with high geometric fidelity. Beyond geometry, we also recover an approximate color appearance, which exposes recognizable layout and potentially sensitive scene elements. This directly contradicts claims in the literature that SCR representations are privacy-preserving by design, and reveals a real risk when such systems are deployed in private or security-critical spaces. The project page is available at https://jaeminch0.github.io/seeing-through-the-weights-privacy-leakage-in-scene-coordinate-regression.

</details>

### 13. Broken Memories: Detecting and Mitigating Memorization in Diffusion Models with Degraded Generations

📄 [arXiv](https://arxiv.org/abs/2605.22050) · 🌐 [Project](https://doi.org/10.1145/3770855.3817770)　📅 2026-05　🏷 KDD 2026

**关键词**：`defense`、`diffusion memorization`、`privacy leakage`、`runtime mitigation`

👤 **作者**：Yuanmin Huang、…、Min Yang

- 🎯 **研究动机**：扩散模型的训练数据记忆带来隐私与版权风险，首次发现记忆化引发内部数值不稳定、表现为视觉破损伪影
- 🔬 **研究方法**：受数值方法稳定性分析启发，以 latent 更新范数定义经验稳定区域，构建步级检测与自适应缓解的在线框架，不改 prompt 或 guidance
- 📌 **结论**：Stable Diffusion 1.4 上检测 AUC 大于 0.999、缓解后记忆率 0.0%，每图开销约 0.01 秒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While diffusion models excel at generating high-quality images, their tendency to memorize training data poses significant privacy and copyright risks. In this work, we for the first time identify that memorization induces internal numerical instability, often manifesting as visually ``broken'' artifacts. Inspired by stability analysis in numerical methods, we introduce empirical stability regions based on latent update norms to quantitatively characterize stable behavior during generation. Leveraging this, we propose a principled, on-the-fly framework for step-wise detection and adaptive mitigation. Our approach suppresses memorization without altering prompts or guidance, thereby preserving semantic fidelity and image quality. Extensive experiments on Stable Diffusion 1.4 demonstrate that our method achieves an AUC $>0.999$ detection performance and a $0.0\%$ memorization rate after mitigation with negligible overhead ($\approx0.01$s per image).

</details>

### 14. Unintended Memorization of Sensitive Information in Fine-Tuned Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.304/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`PII memorization`、`fine-tuning leakage`、`extraction probe`

👤 **作者**：Marton Szep、…、Daniel Rueckert

- 🎯 **研究动机**：微调 LLM 时仅出现在模型输入而非训练目标中的 PII 是否被意外记忆并泄露，缺乏系统研究
- 🔬 **研究方法**：用合成与真实数据设计受控抽取探针，量化 PII 记忆并分析语言、PII 频率、任务类型与模型规模的影响；基准比较差分隐私、机器遗忘、正则化与偏好对齐四种方法
- 📌 **结论**：post-training 方法隐私-效用权衡更一致；差分隐私在特定设置强力降低泄露但可能引发训练不稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning Large Language Models (LLMs) on sensitive datasets carries a substantial risk of unintended memorization and leakage of Personally Identifiable Information (PII), which can violate privacy regulations and compromise individual safety. In this work, we systematically investigate a critical and underexplored vulnerability: the exposure of PII that appears only in model inputs, not in training targets. Using both synthetic and real-world datasets, we design controlled extraction probes to quantify unintended PII memorization and study how factors such as language, PII frequency, task type, and model size influence memorization behavior. We further benchmark four privacy-preserving approaches including differential privacy, machine unlearning, regularization, and preference alignment, evaluating their trade-offs between privacy and task performance. Our results show that post-training methods generally provide more consistent privacy-utility trade-offs, while differential privacy achieves strong reduction in leakage in specific settings, although it can introduce training instability. These findings highlight the persistent challenge of memorization in fine-tuned LLMs and emphasize the need for robust, scalable privacy-preserving techniques.

</details>

### 15. Large-scale online deanonymization with LLMs

📄 [arXiv](https://arxiv.org/abs/2602.16800) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/lermen)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`attack`、`deanonymization`、`privacy leakage`、`memorization`、`LLM agent`、`online privacy`

👤 **作者**：Simon Lermen、Daniel Paleka、Joshua Swanson、Michael Aerni、Nicholas Carlini、Florian Tramèr

- 🎯 **研究动机**：LLM agent 能否对伪匿名用户实施规模化去匿名化未知，线上隐私威胁模型待重估
- 🔬 **研究方法**：构建 LLM 管线抽取身份特征、经语义嵌入检索候选并推理验证匹配，建三个跨平台地面真值数据集（Hacker News-LinkedIn、Reddit 跨社区等）
- 📌 **结论**：90% 精度下召回最高 68%，最佳非 LLM 方法近 0%；伪匿名用户的实践模糊性保护已失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that large language models can be used to perform at-scale deanonymization. With full Internet access, our agent can re-identify Hacker News users and Anthropic Interviewer participants at high precision, given pseudonymous online profiles and conversations alone, matching what would take hours for a dedicated human investigator. We then design attacks for the closed-world setting. Given two databases of pseudonymous individuals, each containing unstructured text written by or about that individual, we implement a scalable attack pipeline that uses LLMs to: (1) extract identity-relevant features, (2) search for candidate matches via semantic embeddings, and (3) reason over top candidates to verify matches and reduce false positives. Compared to classical deanonymization work (e.g., on the Netflix prize) that required structured data, our approach works directly on raw user content across arbitrary platforms. We construct three datasets with known ground-truth data to evaluate our attacks. The first links Hacker News to LinkedIn profiles, using cross-platform references that appear in the profiles. Our second dataset matches users across Reddit movie discussion communities; and the third splits a single user's Reddit history in time to create two pseudonymous profiles to be matched. In each setting, LLM-based methods substantially outperform classical baselines, achieving up to 68% recall at 90% precision compared to near 0% for the best non-LLM method. Our results show that the practical obscurity protecting pseudonymous users online no longer holds and that threat models for online privacy need to be reconsidered.

</details>

### 16. Benchmarking Knowledge-Extraction Attack and Defense on Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2602.09319) · 🌐 [Project](https://doi.org/10.1145/3770855.3817524)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`RAG extraction`、`knowledge leakage`、`targeted defense`

👤 **作者**：Zhisheng Qi、…、Yu Wang

- 🎯 **研究动机**：RAG 知识抽取攻击研究碎片化：嵌入模型、生成器与指标各异，结果不可比
- 🔬 **研究方法**：首个统一基准覆盖多种攻击/防御策略、代表性检索嵌入、开源闭源生成器与（非）图索引，在多语言数据集上标准化评测
- 📌 **结论**：整合实验版图并提供可复现比较基础，支撑隐私保护 RAG 系统开发

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has become a cornerstone of knowledge-intensive applications, including enterprise chatbots, healthcare assistants, and agentic memory management. However, recent studies show that knowledge-extraction attacks can recover sensitive knowledge-base content through maliciously crafted queries, raising serious intellectual property and privacy concerns. While prior work has explored individual attack and defense techniques, the research landscape remains fragmented, spanning heterogeneous retrieval embeddings, diverse generation models, and evaluations based on non-standardized metrics and inconsistent datasets. To address this gap, we introduce the first systematic benchmark for knowledge-extraction attacks on RAG systems. Our benchmark covers broad attack/defense strategies, representative retrieval embedding models, open/closed-source generators, (non) graph-based indexing, all evaluated under a unified experimental framework with standardized protocols across multiple datasets spanning diverse languages. By consolidating the experimental landscape and enabling reproducible, comparable evaluation, this benchmark provides actionable insights and a practical foundation for developing privacy-preserving RAG systems in the face of emerging knowledge extraction threats.

</details>

### 17. Connect the Dots: Knowledge Graph–Guided Crawler Attack on Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2601.15678) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yao-dots)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`attack`、`knowledge graph`、`privacy leakage`、`memorization`、`RAG corpus extraction`、`query planning`

👤 **作者**：Mengyu Yao、…、Ding Li

- 🎯 **研究动机**：已有 RAG 知识库窃取攻击多为启发式且早早停滞在次优覆盖
- 🔬 **研究方法**：把窃取形式化为自适应随机覆盖问题，RAGCrawler 以知识图谱引导维护全局攻击状态，估计覆盖增益、调度高价值语义锚点并生成无冗余自然查询
- 📌 **结论**：四语料四生成器上 1000 查询内平均覆盖 66.8%（最高 84.4%），较最强基线提升 44.90%，达 70% 覆盖所需查询平均至少减少 4.03 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Stealing attacks pose a persistent threat to the intellectual property of deployed machine-learning systems. Retrieval-augmented generation (RAG) intensifies this risk by extending the attack surface beyond model weights to knowledge base that often contains IP-bearing assets such as proprietary runbooks, curated domain collections, or licensed documents. Recent work shows that multi-turn questioning can gradually steal corpus content from RAG systems, yet existing attacks are largely heuristic and often plateau early. We address this gap by formulating RAG knowledge-base stealing as an adaptive stochastic coverage problem (ASCP), where each query is a stochastic action and the goal is to maximize the conditional expected marginal gain (CMG) in corpus coverage under a query budget. Bridging ASCP to real-world black-box RAG knowledge-base stealing raises three challenges: CMG is unobservable, the natural-language action space is intractably large, and feasibility constraints require stealthy queries that remain effective under diverse architectures. We introduce RAGCrawler, a knowledge graph-guided attacker that maintains a global attacker-side state to estimate coverage gains, schedule high-value semantic anchors, and generate non-redundant natural queries. Across four corpora and four generators with BGE retriever, RAGCrawler achieves 66.8% average coverage (up to 84.4%) within 1,000 queries, improving coverage by 44.90% relative to the strongest baseline. It also reduces the queries needed to reach 70% coverage by at least 4.03x on average and enables surrogate reconstruction with answer similarity up to 0.699. Our attack is also scalable to retriever switching and newer RAG techniques like query rewriting and multi-query retrieval. These results highlight urgent needs to protect RAG knowledge assets.

</details>

### 18. Memorization Dynamics in Knowledge Distillation for Language Models

📄 [arXiv](https://arxiv.org/abs/2601.15394) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-01

**关键词**：`analysis`、`knowledge distillation`、`teacher memorization`、`privacy leakage`、`training-data leakage`

👤 **作者**：Jaydeep Borkar、…、Diego Garcia-Olano

- 🎯 **研究动机**：知识蒸馏管线中训练数据记忆的动态规律缺乏系统研究
- 🔬 **研究方法**：用 Pythia、OLMo-2、Qwen-3 三族模型与三个数据集，系统比较蒸馏与标准微调的记忆量、样本构成与可预测性
- 📌 **结论**：蒸馏记忆比标准微调少 50% 以上，约 95% 记忆集中于少数易记样本且可由 zlib 熵、KL 散度与困惑度提前预测；硬蒸馏继承的教师特有样本是软蒸馏的 2.7 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge Distillation (KD) is increasingly adopted to transfer capabilities from large language models to smaller ones, offering significant improvements in efficiency and utility while often surpassing standard fine-tuning. Beyond performance, KD is also explored as a privacy-preserving mechanism to mitigate the risk of training data leakage. While training data memorization has been extensively studied in standard pre-training and fine-tuning settings, its dynamics in a knowledge distillation setup remain poorly understood. In this work, we study memorization across the KD pipeline using three large language model (LLM) families (Pythia, OLMo-2, Qwen-3) and three datasets (FineWeb, Wikitext, Nemotron-CC-v2). We find: (1) distilled models memorize significantly less training data than standard fine-tuning (reducing memorization by more than 50%); (2) some examples are inherently easier to memorize and account for a large fraction of memorization during distillation (over ~95%); (3) student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity; and (4) while soft and hard distillation have similar overall memorization rates, hard distillation poses a greater risk: it inherits $2.7\times$ more teacher-specific examples than soft distillation. Overall, we demonstrate that distillation can provide both improved generalization and reduced memorization risks compared to standard fine-tuning.

</details>

### 19. A Durable Machine Unlearning Framework to Nullify Recall of Sensitive Data on Incremental Training

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T108.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026

**关键词**：`defense`、`sensitive-data recall`、`incremental retraining`、`durable suppression`、`durable unlearning`、`sensitive data`

- 🎯 **研究动机**：unlearning 后的模型仍需用新数据增量训练，新数据含相似甚至相同被遗忘样本时会重新唤回敏感信息，该漏洞未被研究
- 🔬 **研究方法**：提出 Durable Unlearning Enhancement 框架：三组件识别增量数据中的敏感样本并抑制其对 ULM 的梯度更新
- 📌 **结论**：在多个真实数据集与 SOTA unlearning 方法上有效消除 MU 后敏感信息回溯，甚至提升 ULM 性能，确立 post-MU 安全训练新方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancement of data privacy regulations has spurred the development of Machine Unlearning (MU), which is designed to remove the influence of sensitive data from a trained model and results in an unlearned model (ULM). Despite rapid progress in MU techniques, their vulnerabilities remain underexplored, which poses risks due to potential leakage of unlearned information. In realistic scenarios, ULMs always need to be incrementally trained with newly collected data samples, which can lead to the consequences of recalling sensitive information if the new dataset contains similar or even the same unlearned samples. To address this issue, we devise a Durable Unlearning Enhancement (DUE) framework to avoid restoring unwanted sensitive information from incremental training data samples. The DUE framework has three key components that identify sensitive samples and suppress their gradients to update ULMs. Extensive experiments on state-of-the-art MU methods across multiple real-world datasets show that the proposed DUE framework can effectively nullify the recall of sensitive information after MU, and even improve the performance of ULMs. Consequently, our work establishes a new fundamental research direction in safe training against post-MU vulnerabilities.

</details>

### 20. Two Calm Ends and the Wild Middle: A Geometric Picture of Memorization in Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2602.17846) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65094)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`diffusion model`、`privacy leakage`、`memorization`、`privacy attack`、`data leakage`

👤 **作者**：Nick Dodson、Xinyu Gao、Qingsong Wang、Yusu Wang、Zhengchao Wan

- 🎯 **研究动机**：扩散模型何时记忆训练数据尚不清楚，尤其是噪声调度中的位置与数据几何的影响
- 🔬 **研究方法**：提出几何框架，依据训练数据被高斯壳覆盖的性质与后验收敛行为把噪声调度划分为三个区域，刻画各区域的记忆与泛化机制
- 📌 **结论**：中等噪声是记忆最严重的危险区，小噪声因覆盖有限、大噪声因后验低集中而抗记忆；据此设计的几何定向干预可缓解记忆

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models generate high-quality samples but can also memorize training data, raising serious privacy concerns. Understanding the mechanisms governing when memorization versus generalization occurs remains an active area of research. In particular, it is unclear where along the noise schedule memorization is induced, how data geometry influences it, and how phenomena at different noise scales interact. We introduce a geometric framework that partitions the noise schedule into three regimes based on the coverage properties of training data by Gaussian shells and the concentration behavior of the posterior, which we argue are two fundamental objects governing memorization and generalization in diffusion models. This perspective reveals that memorization risk is highly non-uniform across noise levels. We further identify a danger zone at medium noise levels where memorization is most pronounced. In contrast, both the small and large noise regimes resist memorization, but through fundamentally different mechanisms: small noise avoids memorization due to limited training coverage, while large noise exhibits low posterior concentration and admits a provably near linear Gaussian denoising behavior. For the medium noise regime, we identify geometric conditions through which we propose a geometry-informed targeted intervention that mitigates memorization.

</details>

### 21. Towards Whole-corpus Reconstruction of Heterogeneous RAG Knowledge Bases

🎓 [Official](https://icml.cc/virtual/2026/poster/60734)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`empirical evaluation`

👤 **作者**：Peiru Yang、…、Tao Qi

- 🎯 **研究动机**：RAG 服务底层的知识库可被部分乃至整体抽取；现有攻击依赖局部语义连续性，在多源异构知识库中陷入局部最优，难以大规模重建
- 🔬 **研究方法**：提出 GeoEx：直接在代理检索模型的嵌入空间规划全局覆盖，嵌入反演模块生成可执行查询，组合正交查询合成与局部嵌入扰动两种几何策略
- 📌 **结论**：在八领域混合语料、多检索器与 LLM 上抽取覆盖率与查询效率显著优于基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are increasingly deployed to provide query-based access to large knowledge bases, thereby introducing concrete privacy risks whereby the underlying corpus may be partially or fully extracted through the deployed service. Existing extraction attacks typically rely on locally driven search strategies, in which newly extracted content is inferred or expanded based on previously recovered fragments. However, real-world knowledge bases are often multi-source and heterogeneous, with pronounced semantic discontinuities across domains. Such gaps can trap extraction methods that rely on local semantic continuity in local optima, severely limiting large-scale corpus reconstruction. In this paper, we introduce an extraction framework (GeoEx) designed to navigate and reconstruct heterogeneous RAG knowledge bases without any prior knowledge. The framework plans extraction directly in the embedding space of a proxy retrieval model to improve global coverage, and employs an embedding inversion module to convert latent vectors into executable queries. We further propose a composite geometric strategy that combines orthogonal query synthesis for cross-domain exploration with local embedding perturbations for dense extraction within discovered clusters. Experiments on mixed corpora spanning eight diverse domains and multiple retrievers and LLMs show that GeoEx significantly outperforms baselines in both extraction coverage and query efficiency.

</details>

### 22. Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs

📄 [arXiv](https://arxiv.org/abs/2601.11061) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63951)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`reinforcement learning`

👤 **作者**：Lecheng Yan、…、Chenyang Lyu

- 🎯 **研究动机**：Qwen2.5 等模型在虚假奖励下仍获显著 RLVR 增益，其背后机制不明
- 🔬 **研究方法**：发现 Perplexity Paradox：答案 token 困惑度下降而提示侧连贯性退化；用 Path Patching 与 Logit Lens 定位 Anchor-Adapter 电路（L18-20 功能锚点触发记忆检索、L21+ 结构适配器改造表征）
- 📌 **结论**：缩放电路内特定 MLP key 可双向因果操纵污染驱动的性能，证明虚假 RLVR 激活记忆捷径绕过推理，为识别数据污染提供机制路线图

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) is highly effective for enhancing LLM reasoning, yet recent evidence shows models like Qwen2.5 achieve significant gains even with spurious rewards. We investigate this phenomenon and identify ``Perplexity Paradox'': spurious RLVR triggers a divergence where answer-token perplexity drops while prompt-side coherence degrades, suggesting model is bypassing reasoning in favor of memorization. Using a suite of mechanistic interpretability tools, including Path Patching and Logit Lens, we identify a previously unknown Anchor–Adapter circuit. This circuit enables model to bypass reasoning and directly retrieve memorized solutions under spurious RLVR. We localize a Functional Anchor in middle layers (L18–20) that triggers retrieval of memorized solutions, followed by Structural Adapters in later layers (L21+) that transform representations to accommodate shortcut signal. Finally, we demonstrate that scaling specific MLP keys within this circuit allows for bidirectional causal steering, i.e., artificially amplifying or suppressing contamination-driven performance. Our results provide a mechanistic roadmap for identifying and mitigating data contamination in RLVR-tuned models.

</details>

### 23. Rethinking Pretraining Data Detection for LLMs: From Local to Global

🎓 [Official](https://icml.cc/virtual/2026/poster/63793)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`privacy leakage`、`memorization`、`data extraction`、`privacy defense`、`empirical evaluation`

👤 **作者**：Chenye Ke、Yan Zhuang、Zirui Liu、Qi Liu

- 🎯 **研究动机**：预训练数据检测依赖孤立 token 的局部统计（如最低概率 token），忽略生成过程中的概率动态
- 🔬 **研究方法**：提出 AECA：将概率序列视为动态信号，结合校准与卷积滤波捕获记忆化波动模式，实现从局部 token 到全局序列的检测范式转变
- 📌 **结论**：在 WikiMIA 上平均 AUC 超越先前方法最多 1.5%，长文本场景优势尤为明显

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advancements of Large Language Models (LLMs) are primarily attributed to massive pretraining data, which also introduces risks like privacy leakage and data contamination. Therefore, it is crucial to determine whether an LLM has been trained on a given target text. Existing detection methods primarily rely on local statistics of isolated tokens (e.g., those with the lowest probabilities), neglecting the probability dynamics during the token generation process. In this paper, we shift the detection paradigm from a local token to a global sequence perspective, grounded in the core intuition that memorized sequences exhibit volatility patterns distinct from those generated via inference. We propose Adaptive Entropic Convolutional Analysis (AECA), a framework that conceptualizes the probability sequence as a dynamic signal, integrating calibration with convolutional filtering to effectively capture memorization signals. Extensive experiments demonstrate that AECA surpasses previous methods by up to 1.5\% in average AUC on the WikiMIA benchmark, with its advantage being particularly pronounced in long-text scenarios.

</details>

### 24. Reconstructing Template-Memorized Images from Natural Prompts

📄 [arXiv](https://arxiv.org/abs/2507.07947) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62183)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`diffusion model`

👤 **作者**：Sol Yarkoni、Mahmood Sharif、Roi Livni

- 🎯 **研究动机**：从生成模型重建训练数据的攻击通常需要大量算力、训练集访问或精心设计的提示
- 🔬 **研究方法**：针对模板记忆图像（TMI）提出低资源重建攻击：仅用看似良性的自然提示、几乎不接触训练数据即可复现记忆的布局与视觉结构
- 📌 **结论**：简单提示如 "blue Unisex T-Shirt" 即可复现真实人物内容，无对抗意图的普通用户也可能无意重建；TMI 还出现插值等现象

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in generative models, such as diffusion models, have raised concerns related to privacy, copyright infringement, and data curation. Prior work has shown that training data can be reconstructed from such models, but existing attacks typically rely on substantial computational resources, access to the training set, or carefully engineered prompts. In this work, we present a low-resource reconstruction attack that operates through seemingly benign prompts and requires little to no access to the training data. Our attack targets template-memorized images (TMI), where recurring layouts and visual structures are memorized during training. We show that such memorization manifests under potentially realistic usage. This raises a possibility of unintentional reconstruction by naive users that don't carry explicit adversarial intent. For example, we observe that a simple prompt such as "blue Unisex T-Shirt" can reproduce visual content depicting a real individual. Beyond extraction, we observe novel phenomena occurring in TMI (e.g., interpolation), raising questions about the novelty of generated content and the effectiveness of established methods for detecting memorized content. Our code is available at \url{https://github.com/TheSolY/lr-tmi}.

</details>

### 25. Provable Training Data Identification for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.09717) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61277)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`empirical evaluation`

👤 **作者**：Zhenlong Liu、Hao Zeng、Weiran Huang、Hongxin Wei

- 🎯 **研究动机**：训练数据识别多为逐实例进行且不控识别集错误率，无法提供统计可靠证据
- 🔬 **研究方法**：PTDI 形式化为集合级推断：用已知未见数据算 conformal p 值，Jackknife 校正 Beta 边界估计测试集训练数据比例以缩放 p 值，再经 Benjamini-Hochberg 过程选子集
- 📌 **结论**：多模型与数据集上功效高于先前方法且严格控制误识别率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Identifying training data of large-scale models is critical for copyright litigation, privacy auditing, and ensuring fair evaluation. However, existing works typically treat this task as an instance-wise identification without controlling the error rate of the identified set, which cannot provide statistically reliable evidence. In this work, we formalize training data identification as a set-level inference problem and propose Provable Training Data Identification (PTDI), a distribution-free approach that enables provable and strict false identification rate control. Specifically, our method computes conformal p-values for each data point using a set of known unseen data and then develops a novel Jackknife-corrected Beta boundary (JKBB) estimator to estimate the training-data proportion of the test set, which allows us to scale these p-values. By applying the Benjamini–Hochberg (BH) procedure to the scaled p-values, we select a subset of data points with provable and strict false identification control. Extensive experiments across various models and datasets demonstrate that PTDI achieves higher power than prior methods while strictly controlling the FIR.

</details>

### 26. OptiFluence: Principled Design of Privacy Canaries

🎓 [Official](https://icml.cc/virtual/2026/poster/66405)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy attack`、`privacy leakage`、`memorization`、`empirical evaluation`、`data leakage`

👤 **作者**：Mohammad Yaghini、Michael Aerni、Junrui Zhang、Nicolas Papernot、Florian Tramer

- 🎯 **研究动机**：现有隐私 canary 设计靠错误标签或分布外样本，属启发式
- 🔬 **研究方法**：把 canary 设计形式化为双层优化（内环训练模型、外环最大化可检测性），影响函数选候选初始化加记忆高效展开优化
- 📌 **结论**：CIFAR-10 上 0.1% FPR 时 TPR 达 99.6%，超分布内基线 4 倍；canary 跨架构免重训练迁移，支持第三方隐私审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Privacy auditing has emerged as a practical tool for empirically estimating training data leakage in machine learning models, in contrast to the provable but often overly pessimistic bounds provided by differential privacy analysis. A common strategy is to use membership inference attacks to detect the presence of specific canaries—data points chosen to maximize attack success—in training data. However, existing canary designs are largely heuristic, relying on mislabeled or out-of-distribution samples. We address this gap by formulating canary design as a bilevel optimization problem, where the model is trained in the inner loop and the canary is optimized in the outer loop to maximize its detectability. To solve this problem, we develop OptiFluence, a scalable optimization framework that combines (i) initialization by selecting candidates using influence functions and (ii) unrolled optimization with memory-efficient techniques. Our approach achieves remarkable empirical performance on four datasets. Optimized canaries achieve nearperfect detection rates of 99.6% true positive rate at 0.1% false positive rate on CIFAR-10, outperforming in-distribution baselines by 4$\times$. Critically, these canaries transfer effectively across different model architectures without retraining, enabling practical third-party privacy audits. This transferability allows regulators and auditors to assess model privacy without requiring access to proprietary training infrastructure or substantial computational resources.

</details>

### 27. Localizing Memorized Regions in Diffusion Models via Coordinate-Wise Curvature Differences

📄 [arXiv](https://arxiv.org/abs/2605.26756) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60745)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`diffusion model`、`privacy leakage`、`memorization`、`privacy defense`、`sensitive data`

👤 **作者**：Gwangho Kim、Sungyoon Lee

- 🎯 **研究动机**：已有记忆化检测靠全局信号，无法定位图像中记忆位置，且方差塌缩可源自数据内在约束而非过拟合
- 🔬 **研究方法**：把局部记忆化刻画为逐坐标方差塌缩，减去欠拟合基线（无条件模型或欠训练版本）曲率得曲率差方法，并导出 score-difference 代理
- 📌 **结论**：Stable Diffusion 上对照真值记忆掩码优于先前注意力定位方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models can unintentionally memorize training samples, raising concerns about privacy and copyright. While recent methods can detect memorization, they often rely on global or model-specific signals and provide limited insight into where memorization appears within a generated image. We provide a geometric characterization of local memorization as a coordinate-wise variance collapse. However, such collapse can also arise from intrinsic data constraints rather than overfitting. To isolate overfitting-driven memorization, we propose curvature-difference methods that subtract the curvature of an underfitted baseline, either the unconditional model or a less-trained version of itself. We further derive a score-difference proxy that provides a geometric explanation for the widely used score-difference-based detection metric. Experiments on Stable Diffusion, evaluated against ground-truth memorization masks, show that our method outperforms the prior attention-based localization method. Code is available at \url{https://github.com/Gwangho99/mem-curv-diff}.

</details>

### 28. How much can language models memorize?

🎓 [Official](https://icml.cc/virtual/2026/poster/62989)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`privacy leakage`、`memorization`、`data extraction`、`privacy defense`、`empirical evaluation`

👤 **作者**：John Morris、…、Saeed Mahloujifar

- 🎯 **研究动机**：先前语言模型记忆化研究难以把记忆与泛化解耦
- 🔬 **研究方法**：形式化拆分 unintended memorization 与 generalization，完全消除泛化后测总记忆化，训练 500K-1.5B 参数的数百个 transformer
- 📌 **结论**：GPT 式模型容量约 3.6 bits/参数；容量填满前持续记忆化，之后 unintended memorization 下降转而泛化，并给出容量与数据规模对 MIA 的 scaling law

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We propose a new method for estimating how much a model knows about a datapoint and use it to measure the capacity of modern language models. Prior studies of language model memorization have struggled to disentangle memorization from generalization. We formally separate memorization into two components: unintended memorization, the information a model contains about a specific dataset, and generalization, the information a model contains about the true data-generation process. When we completely eliminate generalization, we can compute the total memorization, which provides an estimate of model capacity: our measurements estimate that GPT-style models have a capacity of approximately 3.6 bits per parameter. We train language models on datasets of increasing size and observe that models memorize until their capacity fills, at which point unintended memorization decreases as models begin to generalize. We train hundreds of transformer language models ranging from 500K to 1.5B parameters and produce a series of scaling laws relating model capacity and data size to membership inference.

</details>

### 29. Extracting alignment data in open models

📄 [arXiv](https://arxiv.org/abs/2510.18554) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66452)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`empirical evaluation`

👤 **作者**：Federico Barbero、…、Jamie Hayes

- 🎯 **研究动机**：后训练模型是否泄露可用于提升能力的对齐训练数据（长上下文、安全、数学等）是被忽视的风险
- 🔬 **研究方法**：用高质量嵌入模型距离而非字符串匹配识别语义相似性，度量从后训练模型提取训练数据的规模
- 📌 **结论**：模型 readily 复现 SFT 与 RL 数据，近似字符串匹配会低估约 10 倍提取量；提取数据训练基座可恢复原模型相当部分性能——蒸馏相当于间接在原数据集上训练

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this work, we show that it is possible to extract significant amounts of alignment training data from a post-trained model -- useful to steer the model to improve certain capabilities such as long-context reasoning, safety, instruction following, and maths. While the majority of related work on memorisation has focused on measuring success of training data extraction through string matching, we argue that embedding models are better suited for our specific goals. Distances measured through a high quality embedding model can identify semantic similarities between strings that a different metric such as edit distance will struggle to capture. In fact, in our investigation, approximate string matching would have severely undercounted (by a conservative estimate of $10\times$) the amount of data that can be extracted due to trivial artifacts that deflate the metric. Interestingly, we find that models readily regurgitate training data that was used in post-training phases such as SFT or RL. We show that this data can be then used to train a base model, recovering a meaningful amount of the original performance. We believe our work exposes a possibly overlooked risk towards extracting alignment data. Finally, our work opens up an interesting discussion on the downstream effects of distillation practices: since models seem to be regurgitating aspects of their training set, distillation can therefore be thought of as indirectly training on the model's original dataset.

</details>

### 30. Detecting RAG Extraction Attack via Dual-Path Runtime Integrity Game

🎓 [Official](https://aclanthology.org/2026.acl-long.385/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`privacy leakage`、`memorization`、`data extraction`、`RAG security`、`LLM agent`

👤 **作者**：Yuanbo Xie、…、Tingwen Liu

- 🎯 **研究动机**：自适应迭代的 RAG 知识库提取攻击可诱导模型泄露检索的专有内容，缺乏有效对策
- 🔬 **研究方法**：CanaryRAG 借鉴栈金丝雀思想：把 canary token 嵌入检索块，把防御重构为双路径运行时完整性博弈，任一路径违反预期 canary 行为即实时检测泄露
- 📌 **结论**：块恢复率远低于 SOTA 基线且对任务性能与延迟影响可忽略，即插即用无需重训练或改结构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems augment large language models with external knowledge, yet introduce a critical security vulnerability: RAG Knowledge Base Leakage, wherein adversarial prompts can induce the model to divulge retrieved proprietary content. Recent studies reveal that such leakage can be executed through adaptive and iterative attack strategies (named RAG extraction attack), while effective countermeasures remain notably lacking. To bridge this gap, we propose CanaryRAG, a runtime defense mechanism inspired by stack canaries in software security. CanaryRAG embeds carefully designed canary tokens into retrieved chunks and reformulates RAG extraction defense as a dual-path runtime integrity game. Leakage is detected in real time whenever either the target or oracle path violates its expected canary behavior, including under adaptive suppression and obfuscation. Extensive evaluations against existing attacks demonstrate that CanaryRAG provides robust defense, achieving substantially lower chunk recovery rates than state-of-the-art baselines while imposing negligible impact on task performance and inference latency. Moreover, as a plug-and-play solution, CanaryRAG can be seamlessly integrated into arbitrary RAG pipelines without requiring retraining or structural modifications, offering a practical and scalable safeguard for proprietary data.

</details>

### 31. CoLA: A Choice Leakage Attack Framework to Expose Privacy Risks in Subset Training

🎓 [Official](https://aclanthology.org/2026.acl-long.733/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`LLM privacy`、`data leakage`

👤 **作者**：Qi Li、Cheng-Long Wang、Yinzhi Cao、Di Wang

- 🎯 **研究动机**：常识认为子集训练减少隐私风险，但纳入或排除哪些数据的选择本身引入新隐私面
- 🔬 **研究方法**：CoLA 框架按对手是否知 side-channel 分子集感知侧信道与黑盒两场景，研究训练成员 MIA（TM-MIA）与选择参与 MIA（SP-MIA）两类隐私面
- 📌 **结论**：视觉与语言模型实验表明现有威胁模型低估子集训练风险，扩展的隐私面同时泄露训练与选择成员资格

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Training models on a carefully chosen portion of data rather than the full dataset is now a standard preprocess for modern ML. From vision coreset selection to large-scale filtering in language models, it enables scalability with minimal utility loss. A common intuition is that training on fewer samples should also reduce privacy risks. In this paper, we challenge this assumption. We show that subset training is not privacy free: the very choices of which data are included or excluded can introduce new privacy surface and leak more sensitive information. Such information can be captured by adversaries either through side-channel metadata from the subset selection process or via the outputs of the target model. To systematically study this phenomenon, we propose CoLA (Choice Leakage Attack), a unified framework for analyzing privacy leakage in subset selection. In CoLA, depending on the adversary’s knowledge of the side-channel information, we define two practical attack scenarios: Subset-aware Side-channel Attacks and Black-box Attacks. Under both scenarios, we investigate two privacy surfaces unique to subset training: (1) Training-membership MIA (TM-MIA), which concerns only the privacy of training data membership, and (2) Selection-participation MIA (SP-MIA), which concerns the privacy of all samples that participated in the subset selection process. Notably, SP-MIA enlarges the notion of membership from model training to the entire data-model supply chain. Experiments on vision and language models show that existing threat models underestimate subset-training privacy risks: the expanded privacy surface leaks both training and selection membership, extending risks from individual models to the broader ML ecosystem.

</details>

### 32. Reconstructing Training Data from Models Trained with Transfer Learning

🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026　🏷 SaTML 2026

**关键词**：`attack`、`transfer learning`、`training reconstruction`、`embedding leakage`

- 🎯 **研究动机**：迁移学习下训练数据重构风险未被评估
- 🔬 **研究方法**：对迁移训练的模型发起embedding泄漏式数据重构攻击
- 📌 **结论**：迁移学习并不能消除训练数据重构风险

### 33. On the Effectiveness of Membership Inference in Targeted Data Extraction from Large Language Models

📄 [arXiv](https://arxiv.org/abs/2512.13352) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-12　🏷 SaTML 2026

**关键词**：`analysis`、`LLM memorization`、`membership inference`、`targeted extraction`

👤 **作者**：Ali Al Sahili、Ali Chehab、Razane Tajeddine

- 🎯 **研究动机**：成员推断与训练数据提取两种威胁已知相关，但各 MIA 技术在真实提取管线中的实际效用缺乏系统评估
- 🔬 **研究方法**：把多种 MIA 技术集成进数据提取管线并系统基准评测，与常规 MIA 基准结果对比
- 📌 **结论**：揭示 MIA 在集成提取设定下的表现与常规基准的差异，为现实提取场景中的实用性提供参照

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are prone to memorizing training data, which poses serious privacy risks. Two of the most prominent concerns are training data extraction and Membership Inference Attacks (MIAs). Prior research has shown that these threats are interconnected: adversaries can extract training data from an LLM by querying the model to generate a large volume of text and subsequently applying MIAs to verify whether a particular data point was included in the training set. In this study, we integrate multiple MIA techniques into the data extraction pipeline to systematically benchmark their effectiveness. We then compare their performance in this integrated setting against results from conventional MIA benchmarks, allowing us to evaluate their practical utility in real-world extraction scenarios.

</details>

### 34. Do Vision-Language Models Leak What They Learn? Adaptive Token-Weighted Model Inversion Attacks

📄 [arXiv](https://arxiv.org/abs/2508.04097) · 🌐 [Project](https://ngoc-nguyen-0.github.io/SMI_AW/) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Nguyen_Do_Vision-Language_Models_Leak_What_They_Learn_Adaptive_Token-Weighted_Model_CVPR_2026_paper.html)　📅 2025-08　🏷 CVPR 2026

**关键词**：`attack`、`vision-language model`、`model inversion`、`token weighting`

👤 **作者**：Ngoc-Bao Nguyen、Sy-Tuyen Ho、Koh Jun Hao、Ngai-Man Cheung

- 🎯 **研究动机**：VLM 的模型反演隐私风险未被系统研究
- 🔬 **研究方法**：提出 token 级与序列级反演策略，SMI-AW 按各 token 视觉锚定度自适应加权损失梯度，聚焦信息量大的 token 重建私有图像
- 📌 **结论**：人类评估的攻击准确率达 61.21%，已公开发布的 VLM 同样受害

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model inversion (MI) attacks pose significant privacy risks by reconstructing private training data from trained neural networks. While prior studies have primarily examined unimodal deep networks, the vulnerability of vision-language models (VLMs) remains largely unexplored. In this work, we present the first systematic study of MI attacks on VLMs to understand their susceptibility to leaking private visual training data. Our work makes two main contributions. First, tailored to the token-generative nature of VLMs, we introduce a suite of token-based and sequence-based model inversion strategies, providing a comprehensive analysis of VLMs' vulnerability under different attack formulations. Second, based on the observation that tokens vary in their visual grounding, and hence their gradients differ in informativeness for image reconstruction, we propose Sequence-based Model Inversion with Adaptive Token Weighting (SMI-AW) as a novel MI for VLMs. SMI-AW dynamically reweights each token's loss gradient according to its visual grounding, enabling the optimization to focus on visually informative tokens and more effectively guide the reconstruction of private images. Through extensive experiments and human evaluations on a range of state-of-the-art VLMs across multiple datasets, we show that VLMs are susceptible to training data leakage. Human evaluation of the reconstructed images yields an attack accuracy of 61.21%, underscoring the severity of these privacy risks. Notably, we demonstrate that publicly released VLMs are vulnerable to such attacks. Our study highlights the urgent need for privacy safeguards as VLMs become increasingly deployed in sensitive domains such as healthcare and finance. Our code and models are available at our project page: https://ngoc-nguyen-0.github.io/SMI_AW/

</details>

### 35. Privacy-Aware Decoding: Mitigating Privacy Leakage of Large Language Models in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2508.03098) · 🌐 [Project](https://doi.org/10.1145/3770855.3817665)　📅 2025-08　🏷 KDD 2026

**关键词**：`defense`、`RAG privacy`、`privacy-aware decoding`、`adaptive noise`

👤 **作者**：Haoran Wang、Xiongxiao Xu、Baixiang Huang、Kai Shu

- 🎯 **研究动机**：RAG 检索私有敏感数据时，生成回复可被抽取攻击泄露机密
- 🔬 **研究方法**：提出推理时防御 PAD：自适应向 token logits 注入校准高斯噪声，置信筛选高危 token，RDP 会计追踪累积损失给出每回复 (ε,δ)-DP 保证
- 📌 **结论**：三个真实数据集上大幅减少私有信息泄露并保持效用，优于检索侧与后处理防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances the factual accuracy of large language models (LLMs) by conditioning outputs on external knowledge sources. However, when retrieval involves private or sensitive data, RAG systems are susceptible to extraction attacks that can leak confidential information through generated responses. We propose Privacy-Aware Decoding (PAD), a lightweight, inference-time defense that adaptively injects calibrated Gaussian noise into token logits during generation. PAD integrates confidence-based screening to selectively protect high-risk tokens, efficient sensitivity estimation to minimize unnecessary noise, and context-aware noise calibration to balance privacy with generation quality. A \renyi Differential Privacy (RDP) accountant rigorously tracks cumulative privacy loss, enabling explicit per-response $(\varepsilon, δ)$-DP guarantees for sensitive outputs. Unlike prior approaches requiring retraining or corpus-level filtering, PAD is model-agnostic and operates entirely at decoding time with minimal computational overhead. Experiments on three real-world datasets demonstrate that PAD substantially reduces private information leakage while preserving response utility, outperforming existing retrieval- and post-processing-based defenses. Our work takes an important step toward mitigating privacy risks in RAG via decoding strategies, paving the way for universal and scalable privacy solutions in sensitive domains. Our code is available: https://github.com/wang2226/PAD.

</details>

### 36. DIME: Query-Efficient Framework for Membership Inference on Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2608.22824)　📅 2026-08

**关键词**：`attack`、`diffusion membership inference`、`two-query black box`、`local crowding`

👤 **作者**：Tue Do、Daniel Alabi

- 🎯 **研究动机**：diffusion 模型上的成员推断攻击多为启发式且需要大量查询
- 🔬 **研究方法**：DIME 从有限训练集最优 denoiser 的精确刻画出发，把成员泄漏归因于隐式重建误差，分解为重建偏差项与新发现的 local crowding 项（邻近训练样本几何），两者仅凭模型查询即可估计
- 📌 **结论**：在 CIFAR-10/100、STL10-U、CelebA、ImageNet 上以同等或更低查询成本超越先前攻击，1% FPR 下 TPR 最高提升 3 倍，两查询变体可胜 30 查询基线；并评估了针对性防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks expose whether individual records were used to train a model, yet existing attacks on diffusion models are largely heuristic and can require substantial query budgets. We introduce DIME (Denoiser Ideal Membership Error), a theoretically grounded and query-efficient framework for membership inference on diffusion models. Our starting point is an exact characterization of the optimal diffusion denoiser for a finite training set, which reveals that membership leakage is governed by the denoiser's implicit reconstruction error. This error decomposes into two complementary signals: a bias term, capturing reconstruction accuracy, and a previously unexplored local crowding term, capturing the geometry of nearby training examples. Both admit efficient estimators using only model queries, yielding a practical attack with as few as two queries. Across CIFAR-10/100, STL10-U, CelebA, and ImageNet, DIME consistently outperforms prior attacks at comparable or substantially lower query cost, improving TPR at 1% FPR by up to $3\times$; remarkably, its two-query variant can outperform existing 30-query baselines. Finally, we suggest, discuss, and evaluate specific defenses to counteract such powerful membership tests.

</details>

### 37. Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment

📄 [arXiv](https://arxiv.org/abs/2605.24312) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/nguyen-nguyen)　📅 2026-05　🏷 USENIX Security 2026

**关键词**：`attack`、`RAG membership inference`、`entailment`、`membership inference`、`query efficiency`

👤 **作者**：Nguyen Linh Bao Nguyen、…、Yang Xiang

- 🎯 **研究动机**：已有 RAG 成员推断依赖易检测的模板查询或大量昂贵的重复查询
- 🔬 **研究方法**：MEntA 利用自然语言蕴含：提出宽泛信息寻求问题，测模型响应与候选文档间的蕴含关系，免代理模型与大查询预算
- 📌 **结论**：NFCorpus、SCIDOCS、TREC-COVID 上仅 5 次查询达 0.991 AUC，同等条件超先前方法 0.42 AUC、成本降 65 倍，且在 SOTA RAG 防御下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has become central to large language model (LLM) deployments, grounding responses in enterprise or proprietary data to reduce hallucinations. However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information. Existing MIAs are feasible, but they often rely on easily detected templated queries or require many non-templated yet costly and repetitive queries, limiting practicality. We ask: Can an adversary launch a limited-budget, surrogate-free, stealthy, and defense-agnostic membership inference attack using non-templated queries? We present MEntA (Membership Entailment Attack), a query-efficient MIA that leverages natural-language entailment to maximize information gained per query. By asking low-cost, broad, information-seeking questions and measuring entailment between model responses and candidate documents, MEntA eliminates the need for costly shadow models and large query budgets. Across NFCorpus, SCIDOCS, and TREC-COVID, MEntA achieves up to 0.991 AUC with only 5 queries, outperforming prior methods by up to 0.42 AUC under equivalent conditions. It remains effective under state-of-the-art (SOTA) RAG defenses, while current detectors either miss MEntA or flag benign queries at high rates. Regarding cost, MEntA reduces total attack cost by up to 65$\times$ lower compared to SOTA attacks under the same attack setting. Our findings expose the feasibility of realistic, low-cost privacy leakage in RAG systems and highlight the urgent need for privacy-aware retrieval and defense mechanisms.

</details>

### 38. Membership Inference Attacks for Retrieval Based In-Context Learning for Document Question Answering

📄 [arXiv](https://arxiv.org/abs/2605.04116) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-05　🏷 SaTML 2026

**关键词**：`attack`、`retrieval-based ICL`、`membership inference`、`black-box access`

👤 **作者**：Tejas Kulkarni、Antti Koskela、Laith Zumot

- 🎯 **研究动机**：带检索函数的 ICL 服务会引入训练数据成员泄露，面向该设定的黑盒成员推断未被研究
- 🔬 **研究方法**：两种黑盒攻击利用查询文本前缀：参考模型估计不可得的 loss，或以加权平均方案直接计算成员统计量
- 📌 **结论**：在查询为改写版本的更严格设定下仍以更少前缀优于三个先前攻击；改编的集成 prompt 防御可显著缓解第二种攻击的泄露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that remotely hosted applications employing in-context learning when augmented with a retrieval function to select in-context examples can be vulnerable to membership-inference attacks even when the service provider and users are separate parties. We propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs. The first attack uses a reference model to estimate an otherwise unavailable loss metric. The second attack improves upon it by eliminating the reference model and instead computing a membership statistic through a simple but novel weighted-averaging scheme. Our comprehensive empirical evaluations consider a stricter case in which the adversary has a paraphrased version of the text in the queries and show that our attacks can exhibit stronger resilience to paraphrasing and outperform three prior attacks in many cases with small number of prefixes. We also adapt an existing ensemble prompting defense to our setting, demonstrating that it substantially mitigates the privacy leakage caused by our second attack.

</details>

### 39. A Unified Perspective on Adversarial Membership Manipulation in Vision Models

📄 [arXiv](https://arxiv.org/abs/2604.02780) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_A_Unified_Perspective_on_Adversarial_Membership_Manipulation_in_Vision_Models_CVPR_2026_paper.html)　📅 2026-04　🏷 CVPR 2026

**关键词**：`attack`、`membership manipulation`、`vision model`、`privacy audit`

👤 **作者**：Ruize Gao、Kaiwen Zhou、Yongqiang Chen、Feng Liu

- 🎯 **研究动机**：成员推理攻击假设查询输入诚实，其对抗鲁棒性未被探索
- 🔬 **研究方法**：揭示不可感知扰动可把非成员图像推入 SOTA MIA 的成员区，发现伪造成员特有的梯度范数塌缩轨迹，据此设计梯度几何检测与鲁棒推理
- 📌 **结论**：伪造跨架构与数据集一致有效；梯度几何检测与鲁棒推理显著增强抗操纵韧性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) aim to determine whether a specific data point was part of a model's training set, serving as effective tools for evaluating privacy leakage of vision models. However, existing MIAs implicitly assume honest query inputs, and their adversarial robustness remains unexplored. We show that MIAs for vision models expose a previously overlooked adversarial surface: adversarial membership manipulation, where imperceptible perturbations can reliably push non-member images into the "member" region of state-of-the-art MIAs. In this paper, we provide the first unified perspective on this phenomenon by analyzing its mechanism and implications. We begin by demonstrating that adversarial membership fabrication is consistently effective across diverse architectures and datasets. We then reveal a distinctive geometric signature - a characteristic gradient-norm collapse trajectory - that reliably separates fabricated from true members despite their nearly identical semantic representations. Building on this insight, we introduce a principled detection strategy grounded in gradient-geometry signals and develop a robust inference framework that substantially mitigates adversarial manipulation. Extensive experiments show that fabrication is broadly effective, while our detection and robust inference strategies significantly enhance resilience. This work establishes the first comprehensive framework for adversarial membership manipulation in vision models.

</details>

### 40. Detecting Training Data of Large Language Models via Expectation Maximization

🎓 [Official](https://aclanthology.org/2026.eacl-long.49/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`membership inference`、`expectation maximization`、`distribution overlap`

👤 **作者**：Gyuwan Kim、Yang Li、Evangelia Spiliopoulou、Jie Ma、William Yang Wang

- 🎯 **研究动机**：提示式 MIA（如 ReCALL）依赖已知非成员提示能可靠抑制模型响应的强假设
- 🔬 **研究方法**：EM-MIA 用期望最大化迭代精炼前缀有效性与成员分数，无需标注非成员样本；并构建系统变化分布重叠与难度的 OLMoMIA 基准
- 📌 **结论**：WikiMIA 与 OLMoMIA 上超越基线（尤其分布可分时）；近同分布失败案例暴露现有 MIA 的根本局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) aim to determine whether a specific example was used to train a given language model. While prior work has explored prompt-based attacks such as ReCALL, these methods rely heavily on the assumption that using known non-members as prompts reliably suppresses the model’s responses to non-member queries. We propose EM-MIA, a new membership inference approach that iteratively refines prefix effectiveness and membership scores using an expectation-maximization strategy without requiring labeled non-member examples. To support controlled evaluation, we introduce OLMoMIA, a benchmark that enables analysis of MIA robustness under systematically varied distributional overlap and difficulty. Experiments on WikiMIA and OLMoMIA show that EM-MIA outperforms existing baselines, particularly in settings with clear distributional separability. We highlight scenarios where EM-MIA succeeds in practical settings with partial distributional overlap, while failure cases expose fundamental limitations of current MIA methods under near-identical conditions. We release our code and evaluation pipeline to encourage reproducible and robust MIA research.

</details>

### 41. Image Corruption-Inspired Membership Inference Attacks against Large Vision-Language Models

🎓 [Official](https://aclanthology.org/2026.eacl-long.371/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`VLM membership`、`image corruption`、`black-box query`、`VLM privacy`、`membership inference`

👤 **作者**：Zongyu Wu、…、Suhang Wang

- 🎯 **研究动机**：LVLM 训练图像可能含敏感信息，需要检测某图像是否用于训练
- 🔬 **研究方法**：ICIMIA 利用 LVLM 对 member 与非 member 图像腐败的不同敏感性：白盒下比较图像与腐败版本的视觉嵌入相似度，黑盒下用输出文本嵌入相似度
- 📌 **结论**：两种设定下在现有数据集上均验证攻击有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large vision-language models (LVLMs) have demonstrated outstanding performance in many downstream tasks. However, LVLMs are trained on large-scale datasets, which can pose privacy risks if training images contain sensitive information. Therefore, it is important to detect whether an image is used to train the LVLM. Recent studies have investigated membership inference attacks (MIAs) against LVLMs, including detecting image-text pairs and single-modality content. In this work, we focus on detecting whether a target image is used to train the target LVLM. We design simple yet effective Image Corruption-Inspired Membership Inference Attacks (ICIMIA) against LVLMs, which are inspired by LVLM’s different sensitivity to image corruption for member and non-member images. We first perform an MIA method under the white-box setting, where we can obtain the embeddings of the image through the vision part of the target LVLM. The attacks are based on the embedding similarity between the image and its corrupted version. We further explore a more practical scenario where we have no knowledge about target LVLMs and we can only query the target LVLMs with an image and a textual instruction. We then conduct the attack by utilizing the output text embeddings’ similarity. Experiments on existing datasets validate the effectiveness of our proposed methods under those two different settings.

</details>

### 42. Neural Breadcrumbs: Membership Inference Attacks on LLMs Through Hidden State and Attention Pattern Analysis

🎓 [Official](https://aclanthology.org/2026.eacl-long.262/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`LLM membership`、`hidden-state dynamics`、`attention fingerprint`、`membership inference`、`hidden state`

👤 **作者**：Disha Makhija、Manoj Ghuhan Arivazhagan、Vinayshekhar Bannihatti Kumar、Rashmi Gangadharaiah

- 🎯 **研究动机**：近期研究称 MIA 对 LLM 仅略优于随机猜测，但只看输出忽略内部表示的泄露信号
- 🔬 **研究方法**：memTrace 从 transformer 隐藏态与注意力模式提取 breadcrumb：逐层表示动态、注意力分布特征与跨层转移模式
- 📌 **结论**：多个模型家族上平均 AUC 达 0.85，输出信号看似受保护时内部行为仍暴露训练数据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) reveal whether specific data was used to train machine learning models, serving as important tools for privacy auditing and compliance assessment. Recent studies have reported that MIAs perform only marginally better than random guessing against large language models, suggesting that modern pre-training approaches with massive datasets may be free from privacy leakage risks. Our work offers a complementary perspective to these findings by exploring how examining LLMs’ internal representations, rather than just their outputs, may provide additional insights into potential membership inference signals. Our framework, memTrace, follows what we call neural breadcrumbs extracting informative signals from transformer hidden states and attention patterns as they process candidate sequences. By analyzing layer-wise representation dynamics, attention distribution characteristics, and cross-layer transition patterns, we detect potential memorization fingerprints that traditional loss-based approaches may not capture. This approach yields strong membership detection across several model families achieving average AUC scores of 0.85 on popular MIA benchmarks. Our findings suggest that internal model behaviors can reveal aspects of training data exposure even when output-based signals appear protected, highlighting the need for further research into membership privacy and the development of more robust privacy-preserving training techniques for large language models.

</details>

### 43. VidLeaks: Membership Inference Attacks Against Text-to-Video Models

📄 [arXiv](https://arxiv.org/abs/2601.11210) · 🌐 [Project](https://zenodo.org/records/17972831) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-li)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`attack`、`text-to-video model`、`membership inference`、`privacy leakage`、`temporal memorization`

👤 **作者**：Li Wang、Wenyu Chen、Ning Yu、Zheng Li、Shanqing Guo

- 🎯 **研究动机**：现有成员推断面向静态图像或文本，忽视 T2V 中关键帧记忆稀疏与时序动态不稳定
- 🔬 **研究方法**：VidLeaks 以空间重建保真（Top-K 相似度放大关键帧空间记忆）与时间生成稳定性（多次查询语义一致性）双信号，在监督、参考与仅查询三种黑盒设定下探测
- 📌 **结论**：严格仅查询设定下 AnimateDiff AUC 达 82.92%、InstructVideo 达 97.01%，证明 T2V 模型经稀疏与时序记忆大量泄漏成员信息

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of powerful Text-to-Video (T2V) models, trained on massive web-scale datasets, raises urgent concerns about copyright and privacy violations. Membership inference attacks (MIAs) provide a principled tool for auditing such risks, yet existing techniques - designed for static data like images or text - fail to capture the spatio-temporal complexities of video generation. In particular, they overlook the sparsity of memorization signals in keyframes and the instability introduced by stochastic temporal dynamics. In this paper, we conduct the first systematic study of MIAs against T2V models and introduce a novel framework VidLeaks, which probes sparse-temporal memorization through two complementary signals: 1) Spatial Reconstruction Fidelity (SRF), using a Top-K similarity to amplify spatial memorization signals from sparsely memorized keyframes, and 2) Temporal Generative Stability (TGS), which measures semantic consistency across multiple queries to capture temporal leakage. We evaluate VidLeaks under three progressively restrictive black-box settings - supervised, reference-based, and query-only. Experiments on three representative T2V models reveal severe vulnerabilities: VidLeaks achieves AUC of 82.92% on AnimateDiff and 97.01% on InstructVideo even in the strict query-only setting, posing a realistic and exploitable privacy risk. Our work provides the first concrete evidence that T2V models leak substantial membership information through both sparse and temporal memorization, establishing a foundation for auditing video generation systems and motivating the development of new defenses. Code is available at: https://zenodo.org/records/17972831.

</details>

### 44. Window-based Membership Inference Attacks Against Fine-tuned Large Language Models

📄 [arXiv](https://arxiv.org/abs/2601.02751) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/chen-yuetian)　📅 2026-01　🏷 USENIX Security 2026

**关键词**：`attack`、`fine-tuned LLM`、`membership inference`、`sliding window`

👤 **作者**：Yuetian Chen、…、Ninghui Li

- 🎯 **研究动机**：已有 LLM 成员推断依赖平均损失等全局信号，稀释了记忆的局部微弱信号
- 🔬 **研究方法**：WBC 滑窗法：多种几何间隔尺寸窗口在文本上滑动，每窗基于目标与参考模型的损失比较做二值投票，跨窗口尺寸集成以捕捉 token 级到短语级记忆模式
- 📌 **结论**：11 个数据集上 AUC 显著超越既有基线，低假阳性阈值下检出率提升 2-3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most membership inference attacks (MIAs) against Large Language Models (LLMs) rely on global signals, like average loss, to identify training data. This approach, however, dilutes the subtle, localized signals of memorization, reducing attack effectiveness. We challenge this global-averaging paradigm, positing that membership signals are more pronounced within localized contexts. We introduce WBC (Window-Based Comparison), which exploits this insight through a sliding window approach with sign-based aggregation. Our method slides windows of varying sizes across text sequences, with each window casting a binary vote on membership based on loss comparisons between target and reference models. By ensembling votes across geometrically spaced window sizes, we capture memorization patterns from token-level artifacts to phrase-level structures. Extensive experiments across eleven datasets demonstrate that WBC substantially outperforms established baselines, achieving higher AUC scores and 2-3 times improvements in detection rates at low false positive thresholds. Our findings reveal that aggregating localized evidence is fundamentally more effective than global averaging, exposing critical privacy vulnerabilities in fine-tuned LLMs.

</details>

### 45. DeepLeak: Privacy Enhancing Hardening of Model Explanations Against Membership Leakage

📄 [arXiv](https://arxiv.org/abs/2601.03429) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2026-01　🏷 SaTML 2026

**关键词**：`defense`、`model explanation`、`membership inference`、`privacy hardening`

👤 **作者**：Firas Ben Hmida、Zain Sbeih、Philemon Hailemariam、Birhanu Eshete

- 🎯 **研究动机**：事后解释方法会泄漏成员信息，从业者缺乏平衡透明性与隐私的系统性指导
- 🔬 **研究方法**：DeepLeak 构建更强的解释感知成员推断攻击量化泄漏，提出敏感度校准噪声、归因裁剪与掩码等模型无关缓解，并以控制实验定位归因稀疏性等泄漏根因
- 📌 **结论**：15 种解释技术默认设置泄漏比先前报告多至 74.9%；缓解最多削减 95% 泄漏，平均效用损失不超过 3.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine learning (ML) explainability is central to algorithmic transparency in high-stakes settings such as predictive diagnostics and loan approval. However, these same domains require rigorous privacy guaranties, creating tension between interpretability and privacy. Although prior work has shown that explanation methods can leak membership information, practitioners still lack systematic guidance on selecting or deploying explanation techniques that balance transparency with privacy. We present DeepLeak, a system to audit and mitigate privacy risks in post-hoc explanation methods. DeepLeak advances the state-of-the-art in three ways: (1) comprehensive leakage profiling: we develop a stronger explanation-aware membership inference attack (MIA) to quantify how much representative explanation methods leak membership information under default configurations; (2) lightweight hardening strategies: we introduce practical, model-agnostic mitigations, including sensitivity-calibrated noise, attribution clipping, and masking, that substantially reduce membership leakage while preserving explanation utility; and (3) root-cause analysis: through controlled experiments, we pinpoint algorithmic properties (e.g., attribution sparsity and sensitivity) that drive leakage. Evaluating 15 explanation techniques across four families on image benchmarks, DeepLeak shows that default settings can leak up to 74.9% more membership information than previously reported. Our mitigations cut leakage by up to 95% (minimum 46.5%) with only <=3.3% utility loss on average. DeepLeak offers a systematic, reproducible path to safer explainability in privacy-sensitive ML.

</details>

### 46. Where Rectified Flows Leak: Characterising Membership Signals Along the Interpolation Path

🎓 [Official](https://icml.cc/virtual/2026/poster/63762)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`empirical evaluation`

👤 **作者**：Thomas Sesmat、Gabriel Meseguer-Brocal、Geoffroy Peeters

- 🎯 **研究动机**：生成模型除逐字复现外还编码不出现在输出中的训练数据痕迹，Rectified Flow 的此类成员信号未被刻画
- 🔬 **研究方法**：分析插值路径上训练/测试数据的重构差距：呈随训练累积的钟形曲线，高斯假设下闭式推导峰值位置；并在音频与图像上验证
- 📌 **结论**：钟形结构普适、峰值预测在假设满足时成立；利用该 lambda 分辨结构可实施成员推理攻击区分训练成员

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding what generative models retain from training data remains challenging, with implications for copyright and privacy. Beyond verbatim reproduction, models can encode subtler traces of their training data that never surface in their outputs yet remain exploitable. We study this regime for Rectified Flows, which are increasingly used in deployed generative systems. We analyse the interpolation path $X_\lambda = (1-\lambda)X_0 + \lambda X_1$ that defines the Rectified Flow training. We show that a gap exists between the reconstruction of train and test data that follows a bell-shaped curve over $\lambda$, wich accumulates during training, while the validation metrics remain stable. The signal has a maximum whose location we derive in closed form under Gaussian assumptions. We validate these predictions on both audio and images and show that the bell-shaped structure is universal, while the peak prediction holds when our assumptions are satisfied. As a proof of concept, we exploit this specific $\lambda$-resolved structure to perform a Membership Inference Attack, distinguishing members of the training set from non-members.

</details>

### 47. Robust Membership Inference for Large Language Models under Adversarial Generative Corruption

🎓 [Official](https://aclanthology.org/2026.acl-long.1835/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`membership inference`、`adversarial robustness`、`privacy leakage`、`LLM privacy`、`data leakage`

👤 **作者**：Yuanhong Huang、…、Tao Qi

- 🎯 **研究动机**：MIA 依赖训练样本置信度更高的假设，而 LLM 生成的高置信 AIGT 文本同样满足该假设，可被用来污染成员推断
- 🔬 **研究方法**：实证确认 AIGT 会获得比真实训练样本更高的成员似然，提出混合专家框架联合建模多种 MIA 特征与 AIGT 检测器的互补信息
- 📌 **结论**：对抗样本使基线大幅退化时，该方法仍保持接近无攻击设定的性能，并可解释成员数据特征

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attack (MIA) has emerged as a promising tool for auditing the training data of LLMs, supporting data privacy and copyright protection. Most existing MIA methods rely on the assumption that LLMs assign higher confidence scores to training samples than to non-training ones.However, since LLMs generate text by sampling high-confidence tokens, they naturally produce AI-generated texts (AIGTs) that also satisfy this assumption.In this work, we empirically confirm that such AIGTs, regardless of whether they are generated by the target LLM, can lead existing MIAs to assign even higher membership likelihoods than those of true training samples, thereby significantly undermining their reliability.To address this challenge, we propose a robust membership inference framework for reliably identifying training data.Our method adopts a mixture-of-experts formulation to jointly model interactions across complementary features derived from multiple MIA methods and AIGT detectors, which can remain robust against adversarially generated samples.Furthermore, by leveraging expert components, our method provides explainable insights into the characteristics of member data.Experiments on various datasets and LLMs show that adversarial samples substantially degrade the performance of baselines, whereas our method preserves performance close to that of the unattacked setting.Codes and datasets are released at https://github.com/kong-hyh/MoMIA.

</details>

### 48. Powerful Training-Free Membership Inference Against Fine-Tuned Autoregressive Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.640/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`membership inference`、`privacy leakage`、`memorization`、`LLM privacy`、`data leakage`

👤 **作者**：David Ilić、David Stanojević、Kostadin Cvejoski

- 🎯 **研究动机**：现有 MIA 在实际审计所需的低假阳性阈值下检测率有限
- 🔬 **研究方法**：EZ-MIA 发现记忆化在错误位置表现最强：EZ score 度量相对预训练参考模型错误位置概率转移的方向失衡，仅需两次前向、零训练
- 📌 **结论**：WikiText+GPT-2 上 1% FPR 时 TPR 66.3%（前 SOTA 17.5%，3.8 倍）、AUC 0.98；0.1% FPR 时高 8 倍；Llama-2-7B 上高 3 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuned language models pose significant privacy risks, as they may memorize and expose sensitive information from their training data. Membership inference attacks (MIAs) provide a principled framework for auditing these risks, yet existing methods achieve limited detection rates, particularly at the low false-positive thresholds required for practical privacy auditing. We present EZ-MIA, a membership inference attack that exploits a key observation: memorization manifests most strongly at error positions, specifically tokens where the model predicts incorrectly yet still shows elevated probability for training examples. We introduce the Error Zone (EZ) score, which measures the directional imbalance of probability shifts at error positions relative to a pretrained reference model. This principled statistic requires only two forward passes per query and no model training of any kind. On WikiText with GPT-2, EZ-MIA achieves 3.8 × higher detection than the previous state-of-the-art under identical conditions (66.3% versus 17.5% true positive rate at 1% false positive rate), with near-perfect discrimination (AUC 0.98). At the stringent 0.1% FPR threshold critical for real-world auditing, we achieve 8 × higher detection than prior work (14.0% versus 1.8%), requiring no reference model training. These gains extend to larger architectures: on AG News with Llama-2-7B, we achieve 3 × higher detection (46.7% versus 15.8% TPR at 1% FPR). These results establish that privacy risks of fine-tuned language models are substantially greater than previously understood, with implications for both privacy auditing and deployment decisions. Code is available at https://github.com/JetBrains-Research/ez-mia.

</details>

### 49. Membership Inference Attacks for Unseen Classes

📄 [arXiv](https://arxiv.org/abs/2506.06488) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65656)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`membership inference`、`privacy leakage`、`memorization`、`privacy attack`、`empirical evaluation`

👤 **作者**：Pratiksha Thaker、Neil Kale、Zhiwei Steven Wu、Virginia Smith

- 🎯 **研究动机**：现实审计常因法律伦理限制拿不到同分布有害内容样本，SOTA MIA 在此 unseen class 设定下失败
- 🔬 **研究方法**：形式化 unseen class 数据访问模型，提出分位数回归攻击并给出其成功所需泛化性质的理论模型
- 📌 **结论**：分位数回归攻击 TPR 达 shadow model 方法的 11 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A key tool in developing safe AI models is data auditing, i.e., using statistical tools to determine whether harmful content may have been used in the training data of a black-box model. Unfortunately, most membership inference attacks (MIAs) used to perform this type of auditing themselves assume access to examples of harmful content from the same distribution as the query data. In real-world auditing scenarios, auditors often face legal and ethical restrictions preventing them from accessing a representative set of samples of harmful content to train MIA models effectively. We abstract and formalize this setting into a new data access model, the “unseen class” setting, and show that the state-of-the-art MIAs fail due to the lack of access to the full target distribution. We show that in this setting, quantile regression attacks outperform approaches typically considered to be state of the art. We demonstrate this both empirically and theoretically, showing that quantile regression attacks achieve up to 11× the TPR of shadow model-based approaches in practice, and providing a theoretical model that outlines the generalization properties required for this approach to succeed. Our work identifies an important failure mode in existing MIAs and provides a cautionary tale for practitioners who aim to directly use existing tools for real-world applications of AI safety.

</details>

### 50. How does Bayesian Sampling help Membership Inference Attacks?

📄 [arXiv](https://arxiv.org/abs/2503.07482) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61311)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`membership inference`、`privacy leakage`、`memorization`、`privacy attack`

👤 **作者**：Zhenlong Liu、Wenyu Jiang、Feng Zhou、Hongxin Wei

- 🎯 **研究动机**：SOTA 成员推断需训练多个参考模型逼近条件分数分布，计算开销大限制实用
- 🔬 **研究方法**：BMIA 对单个参考模型做 Laplace 近似得到参数后验直接估计条件分数分布，理论上证明贝叶斯采样降低模型内方差
- 📌 **结论**：图像、文本、表格数据上效果与效率均 SOTA，多参考变体进一步增强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership Inference Attacks (MIAs) aim to estimate whether a specific data point was used in the training of a given model. Existing state-of-the-art attacks typically rely on training multiple reference models to approximate the conditional score distribution for individual data points, which leads to significant computational overhead and limits their practical applicability. In this work, we propose a novel approach -- Bayesian Membership Inference Attack (BMIA), which performs conditional attack through Bayesian sampling. Specifically, we apply Laplace approximation to a single reference model to obtain a posterior over model parameters, enabling direct estimation of the conditional score distribution. Theoretically, we demonstrate that Bayesian sampling reduces intra-model variance, thereby improving attack power. This insight naturally motivates the multi-reference variant that further enhances performance when additional reference models are available. Extensive experiments across image, text, and tabular datasets indicate that our method achieves state-of-the-art performance in both effectiveness and efficiency.

</details>

### 51. Enhancing Membership Inference Attacks on Diffusion Models from a Frequency-Domain Perspective

📄 [arXiv](https://arxiv.org/abs/2505.20955) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64135)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`diffusion model`、`membership inference`、`privacy leakage`、`privacy attack`、`data leakage`

👤 **作者**：Puwei Lian、Yujun Cai、Songze Li、Bingkun Bao

- 🎯 **研究动机**：扩散模型 MIA 忽视模型处理高频信息的固有缺陷——高频成员被误判为非成员、反之亦然，削弱成员优势
- 🔬 **研究方法**：把现有攻击统一为通用范式后，提出即插即用高频滤波模块缓解该缺陷，可无缝集成进任意攻击且无额外时间成本
- 📌 **结论**：跨数据集与模型显著提升基线攻击性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have achieved tremendous success in image generation, but they also raise significant concerns regarding privacy and copyright issues. Membership Inference Attacks (MIAs) are designed to ascertain whether specific data was utilized during a model's training phase. As current MIAs for diffusion models typically exploit the model's image prediction ability, we formalize them into a unified general paradigm that computes the membership score for membership identification. Under this paradigm, we empirically find that existing attacks overlook the inherent deficiency in how diffusion models process high-frequency information. Consequently, this deficiency leads to member data with more high-frequency content being misclassified as hold-out data, and hold-out data with less high-frequency content tends to be misclassified as member data. Moreover, we theoretically demonstrate that this deficiency reduces the membership advantage of attacks, thereby interfering with the effective discrimination of member data and hold-out data. Based on this insight, we propose a plug-and-play high-frequency filter module to mitigate the adverse effects of the deficiency, which can be seamlessly integrated into any attacks within the general paradigm without additional time costs. Extensive experiments corroborate that this module significantly improves the performance of baseline attacks across different datasets and models. Code is available at https://github.com/poetic2/FreMIA.

</details>

### 52. CheckMIABench: Firm Foundations For Membership Inference Attacks on Language Models

🎓 [Official](https://aclanthology.org/2026.acl-short.30/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`membership inference`、`privacy leakage`、`memorization`、`LLM privacy`、`data leakage`

👤 **作者**：Jeffrey George Wang、Jason Wang、Marvin Li、Seth Neel

- 🎯 **研究动机**：MIA 评测受成员与非成员集分布偏移破坏统计效度——无模型访问的盲方法竟优于同基准上的已发表方法
- 🔬 **研究方法**：利用训练固定点前后数据同分布的洞见，把带中间 checkpoint 与公开训练数据的开源模型转为 MIA 测试床，在 Pythia 与 OLMo（70M 至 7B）上评测六种攻击并开源模块化库
- 📌 **结论**：为 LLM MIA 提供原则性评测基准与可复用工具库

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) are a canonical way to assess a machine learning model’s privacy properties. Although several attempts have been made to evaluate MIAs on language models, the extant literature has suffered numerous difficulties in constructing clean evaluations to test new techniques. In particular, subtle distribution shifts between member and non-member sets can undermine the statistical validity of MIAs; recent work has underscored this by showing that “blind” methods with no access to the underlying model can perform far better than published methods on the same benchmarks. This paper constructs a benchmark for principled evaluation of MIAs against LLMs, by leveraging the insight that training data before and after a fixed point during training are drawn from the same distribution. Therefore, all open-source models with intermediate checkpoints and public training data can be converted into MIA testbeds. We apply our framework to a half-dozen published attacks on the Pythia and OLMo family of models, from 70M to 7B parameters. To facilitate further privacy research, we open-source a modular library for designing and implementing attacks in this setting: https://github.com/safr-ai-lab/pandora_llm.

</details>

### 53. Black-Box Membership Inference Attacks for Video Training Data in Multimodal Large Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.1820/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`membership inference`、`VLM safety`、`LLM privacy`

👤 **作者**：Jinrui Wang、…、Tao Qi

- 🎯 **研究动机**：现有视频 MIA 依赖在语料中反复出现的语义概念（证据不可靠），或需 logit 访问而无法用于黑盒
- 🔬 **研究方法**：VideoMIA 利用视频帧间时序依赖评估模型对视频内序列动态的记忆——该信号无法从一般世界知识或单帧推断
- 📌 **结论**：10 个 MLLM、4 个基准的黑盒评测中一致超越所有基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The increasing use of video data in training multimodal large language models (MLLMs) raises significant concerns on privacy leakage and copyright violations, highlighting the need for detecting improperly used training videos through membership inference attacks (MIAs). Most existing video MIA methods assess model memorization of key semantic concepts within a video (e.g., the name of a well-known movie character). However, such concepts usually appear repeatedly throughout the training corpus, and memorization of them does not constitute reliable evidence that a specific video was used during training. Besides, while some methods mitigate this limitation by capturing relationships between frames, they require a model logit-accessible setting and are impractical in realistic black-box scenarios. To address these challenges, we propose a black-box MIA framework, named VideoMIA, that can provide reliable evidence of specific video data usage for training MLLMs. The key of our method is to leverage temporal dependencies across video frames to evaluate the model’s memorization of sequential dynamics within the video data, which cannot be inferred solely from general world knowledge or individual image data. The results across ten MLLMs and four benchmarks demonstrate that our method consistently achieves superior performance over all baselines in black-box evaluation settings. Code is available in https://github.com/jinruiwang258/VideoMIA.

</details>

### 54. Black-box Membership Inference Attacks on the Pre-training Data of Image-generation Models

📄 [arXiv](https://arxiv.org/abs/2605.27020) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_Black-box_Membership_Inference_Attacks_on_the_Pre-training_Data_of_Image-generation_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`attack`、`image generator`、`membership inference`、`black-box access`

👤 **作者**：Tao Qi、…、Yongfeng Huang

- 🎯 **研究动机**：扩散模型 MIA 以去噪能力为指标，在低暴露的预训练数据上判别力剧减；内部特征在闭源平台不可得
- 🔬 **研究方法**：SD-MIA 分析黑盒扩散模型对目标图像与扰动文本指令的联合去噪行为获得成员线索，用跨模态数据扰动机制检测预训练数据
- 📌 **结论**：在公开基准与同分布新数据集上优于现有基线，包括可访问内部特征的不公平对手

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid advancement of diffusion-based image generation models has raised serious concerns regarding potential copyright and privacy infringements involving human-created data. Membership inference attacks (MIAs) have emerged as a promising tool for identifying unauthorized data usage during model training. Existing methods typically assess the ability of model to denoise perturbed suspect images as an indicator of membership status. However, the discriminative power of such features is highly dependent on the degree of model memorization and deteriorates significantly when applied to less exposed data (e.g., pre-training data). Although several methods attempt to enhance detection by leveraging internal model features, these features are generally inaccessible in mainstream closed-source image generation platforms, limiting their practicality. In this paper, we demonstrate that analyzing how a black-box diffusion model denoises a target image and corresponding perturbed textual instructions can reveal more distinctive membership cues. Based on this insight, we propose a black-box membership inference attack framework (named SD-MIA) that leverages a cross-modal data perturbation mechanism to detect pre-training data in diffusion models. We conduct extensive experiments on both a public benchmark dataset and a newly constructed dataset, each comprising pre-training membership and non-membership samples with identical distributions. Experimental results demonstrate that SD-MIA achieves superior performance compared to existing baselines, including those with the unfair advantage of accessing internal model features.

</details>

### 55. Membership Inference Attacks on Tokenizers of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.05699) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/tong)　📅 2025-10　🏷 USENIX Security 2026

**关键词**：`attack`、`membership inference`、`privacy leakage`、`memorization`、`LLM tokenizer`、`adaptive defense`

👤 **作者**：Meng Tong、Yuntao Du、Kejiang Chen、Weiming Zhang、Ninghui Li

- 🎯 **研究动机**：对预训练 LLM 的成员推断受误标样本、分布漂移与模型规模差异困扰
- 🔬 **研究方法**：首次把 tokenizer 作为攻击面：其可高效从头训练且训练数据具代表性，探索五种数据集成员推断方法并提出自适应防御
- 📌 **结论**：数百万互联网样本实验揭示 SoTA LLM tokenizer 的成员泄露漏洞，需针对性隐私保护机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) are widely used to assess the privacy risks associated with machine learning models. However, when these attacks are applied to pre-trained large language models (LLMs), they encounter significant challenges, including mislabeled samples, distribution shifts, and discrepancies in model size between experimental and real-world settings. To address these limitations, we introduce tokenizers as a new attack vector for membership inference. Specifically, a tokenizer converts raw text into tokens for LLMs. Unlike full models, tokenizers can be efficiently trained from scratch, thereby avoiding the aforementioned challenges. In addition, the tokenizer's training data is typically representative of the data used to pre-train LLMs. Despite these advantages, the potential of tokenizers as an attack vector remains unexplored. To this end, we present the first study on membership leakage through tokenizers and explore five attack methods to infer dataset membership. Extensive experiments on millions of Internet samples reveal the vulnerabilities in the tokenizers of state-of-the-art LLMs. To mitigate this emerging risk, we further propose an adaptive defense. Our findings highlight tokenizers as an overlooked yet critical privacy threat, underscoring the urgent need for privacy-preserving mechanisms specifically designed for them.

</details>

### 56. Imitative Membership Inference Attack

📄 [arXiv](https://arxiv.org/abs/2509.06796) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/du)　📅 2025-09　🏷 USENIX Security 2026

**关键词**：`attack`、`membership inference`、`imitative model`、`privacy leakage`、`low-cost auditing`

👤 **作者**：Yuntao Du、Yuetian Chen、Hanshen Xiao、Bruno Ribeiro、Ninghui Li

- 🎯 **研究动机**：SoTA 成员推断需训练数百个独立影子模型，计算开销巨大
- 🔬 **研究方法**：提出 IMIA：以模仿训练技术构造少量紧密复刻目标行为的目标感知模仿模型用于推断
- 📌 **结论**：多种攻击设置下显著优于既有 MIA，计算成本不足 SoTA 方法的 5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A Membership Inference Attack (MIA) assesses how much a target machine learning model reveals about its training data by determining whether specific query instances were part of the training set. State-of-the-art MIAs rely on training hundreds of shadow models that are independent of the target model, leading to significant computational overhead. In this paper, we introduce Imitative Membership Inference Attack (IMIA), which employs a novel imitative training technique to strategically construct a small number of target-informed imitative models that closely replicate the target model's behavior for inference. Extensive experimental results demonstrate that IMIA substantially outperforms existing MIAs in various attack settings while only requiring less than 5% of the computational cost of state-of-the-art approaches.

</details>

### 57. Privacy Risks in Time Series Forecasting: User- and Record-Level Membership Inference

📄 [arXiv](https://arxiv.org/abs/2509.04169) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-09　🏷 SaTML 2026

**关键词**：`attack`、`time-series forecasting`、`membership inference`、`user-level leakage`

👤 **作者**：Nicolas Johansson、Tobias Olsson、Daniel Nilsson、Johan Östman、Fazeleh Hoseini

- 🎯 **研究动机**：成员推断在分类模型上研究充分，时序预测领域几乎空白
- 🔬 **研究方法**：提出适配多变量 LiRA 与端到端 DTS 两种攻击，在 TUH-EEG 与 ELD 上对 LSTM 与 N-HiTS 做记录级与用户级威胁评测
- 📌 **结论**：预测模型普遍脆弱，用户级攻击常达完美检测；预测时域越长、训练群体越小越脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) aim to determine whether specific data were used to train a model. While extensively studied on classification models, their impact on time series forecasting remains largely unexplored. We address this gap by introducing two new attacks: (i) an adaptation of multivariate LiRA, a state-of-the-art MIA originally developed for classification models, to the time-series forecasting setting, and (ii) a novel end-to-end learning approach called Deep Time Series (DTS) attack. We benchmark these methods against adapted versions of other leading attacks from the classification setting. We evaluate all attacks in realistic settings on the TUH-EEG and ELD datasets, targeting two strong forecasting architectures, LSTM and the state-of-the-art N-HiTS, under both record- and user-level threat models. Our results show that forecasting models are vulnerable, with user-level attacks often achieving perfect detection. The proposed methods achieve the strongest performance in several settings, establishing new baselines for privacy risk assessment in time series forecasting. Furthermore, vulnerability increases with longer prediction horizons and smaller training populations, echoing trends observed in large language models.

</details>

### 58. CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage

📄 [arXiv](https://arxiv.org/abs/2507.16872) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/li-na)　📅 2025-07　🏷 USENIX Security 2026

**关键词**：`attack`、`analysis`、`model compression`、`membership inference`、`privacy leakage`

👤 **作者**：Na Li、Yansong Gao、Hongsheng Hu、Boyu Kuang、Anmin Fu

- 🎯 **研究动机**：模型压缩的资源-性能权衡之外，其引入的隐私风险被忽视
- 🔬 **研究方法**：提出 CompLeak：以成员推断评估 TF-Lite 与 PyTorch Mobile 的剪枝、量化与权重聚类，含单压缩模型、结合原模型与多压缩模型三种变体
- 📌 **结论**：压缩模型对成员与非成员影响不同，结合原模型或多版本元信息可显著放大隐私泄露，覆盖 ResNet 到 BERT 与 GPT-2

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Model compression is crucial for minimizing memory storage and accelerating inference in deep learning (DL) models, including recent foundation models like large language models (LLMs). Users can access different compressed model versions according to their resources and budget. However, while existing compression operations primarily focus on optimizing the trade-off between resource efficiency and model performance, the privacy risks introduced by compression remain overlooked and insufficiently understood. In this work, through the lens of membership inference attack (MIA), we propose CompLeak, the first privacy risk evaluation framework examining three widely used compression configurations that are pruning, quantization, and weight clustering supported by the commercial model compression framework of Google's TensorFlow-Lite (TF-Lite) and Facebook's PyTorch Mobile. CompLeak has three variants, given available access to the number of compressed models and original model. CompLeakNR starts by adopting existing MIA methods to attack a single compressed model, and identifies that different compressed models influence members and non-members differently. When the original model and one compressed model are available, CompLeakSR leverages the compressed model as a reference to the original model and uncovers more privacy by combining meta information (e.g., confidence vector) from both models. When multiple compressed models are available with/without accessing the original model, CompLeakMR innovatively exploits privacy leakage info from multiple compressed versions to substantially signify the overall privacy leakage. We conduct extensive experiments on seven diverse model architectures (from ResNet to foundation models of BERT and GPT-2), and six image and textual benchmark datasets.

</details>

### 59. Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit

📄 [arXiv](https://arxiv.org/abs/2608.20351) · 🎓 [Official](https://aclanthology.org/2026.stereacult-1.3/)　📅 2026-08

**关键词**：`benchmark`、`analysis`、`RAG PII leakage`、`cultural-query audit`、`metric confounding`、`cultural disparity audit`

👤 **作者**：Yanhang Li、Zhichao Fan、Zexin Zhuang

- 🎯 **研究动机**：刻板印象加载查询是否比等价中性查询从 RAG 泄露更多文化标记人物的 PII 未知
- 🔬 **研究方法**：预注册四文化（英、西、阿拉伯、印地）合成英语 PII 语料上的五臂 STLD 审计；但锁定确证估计器未运行、名字泄漏指标受 prompt 回声伪影污染
- 📌 **结论**：更干净信道（email、phone、ssn、address）多重比较校正后四文化均无刻板驱动放大；样本仅够中等效应——报告为未检出而非无效应的证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We ask whether stereotype-loaded queries about culturally marked people leak more personal information from a retrieval-augmented generation (RAG) system than otherwise-equivalent neutral queries. We pre-register a four-culture audit (en-Anglo, es-LATAM, Arabic, Hindi) on a synthetic English PII corpus, comparing five query arms we call the Stereotype-Trigger Leakage Delta (STLD). Two caveats up front. Our locked confirmatory estimator was never run, so every test in the paper is exploratory or sensitivity, with all plan deviations listed in the appendix. And the name-leakage metric is contaminated by a prompt-echo artifact: the model often just re-emits the name we asked about, which inflates apparent leakage without any retrieval at all. On the cleaner channels (email, phone, ssn-like, address), we find no stereotype-driven amplification on any of the four cultures after multiple-comparison correction. Because our sample is only powered for mid-sized effects, and because the culturally marked probes mix stereotype content with cultural markers and heritage practices, we present this as no detection, not evidence of no effect, of culturally marked predicate leakage that is confounded with the underlying resource.

</details>

### 60. From Weak Cues to Real Identities: Evaluating Inference-Driven De-Anonymization in LLM Agents

📄 [arXiv](https://arxiv.org/abs/2603.18382) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64683)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`privacy leakage`、`memorization`、`data extraction`、`privacy attack`、`empirical evaluation`

👤 **作者**：Myeongseob Ko、Jihyun Jeong、Sumiran Singh Thakur、Gyuhak Kim、Ruoxi Jia

- 🎯 **研究动机**：重识别过去需专业知识与人工比对，LLM 智能体可能仅凭零散弱线索即可重建真实身份
- 🔬 **研究方法**：在经典 linkage 事件、可控 benchmark InferLink（变指纹类型/任务框架/攻击者知识）与人机交互轨迹三类场景评测智能体重识别能力
- 📌 **结论**：Netflix Prize 稀疏场景下重建 79.2% 身份（经典基线 56.0%）；即使无明确重识别请求也会链接个体，隐私评测应度量可推断身份

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Anonymization is often assumed to protect privacy once explicit identifiers are removed, because re-identification has historically required specialized expertise, tailored algorithms, and manual corroboration. We show that LLM-based agents weaken this barrier: by combining scattered, individually non-identifying cues with public evidence, they reconstruct real-world identities, sometimes even during benign tasks. We evaluate this risk across three settings---classical linkage incidents, a controlled benchmark (\emph{InferLink}) that varies fingerprint type, task framing, and attacker knowledge, and open-ended human--AI interaction traces. In the sparsest regime of the Netflix Prize deanonymization setting, agents reconstruct 79.2\% of identities, against 56.0\% for a classical matching baseline; on \emph{InferLink}, they link individuals even without an explicit re-identification request, and more often once one is given. In redacted human--AI interaction traces, agents further resolve anonymized profiles to specific individuals by corroborating contextual cues with public evidence. These findings suggest that privacy evaluations for agentic systems should measure not only what information is accessed or disclosed, but also what identities can be inferred.

</details>

### 61. Black-Box Embedding Inversion Attack on Vector Databases

🌐 [Project](https://doi.org/10.1145/3770855.3817917)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`embedding inversion`、`vector database`、`black-box reconstruction`、`stored-content extraction`、`vector-database leakage`

- 🎯 **研究动机**：向量数据库的embedding被默认安全，黑盒内容还原能力未评估
- 🔬 **研究方法**：对向量数据库发起黑盒embedding inversion攻击重建存储内容
- 📌 **结论**：仅凭查询接口即可高精度重建原文，向量库存在实质泄漏

### 62. What Your Features Reveal: Data-Efficient Black-Box Feature Inversion Attack for Split DNNs

📄 [arXiv](https://arxiv.org/abs/2511.15316) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Ren_What_Your_Features_Reveal_Data-Efficient_Black-Box_Feature_Inversion_Attack_for_CVPR_2026_paper.html)　📅 2025-11　🏷 CVPR 2026

**关键词**：`attack`、`split DNN`、`feature inversion`、`black-box leakage`

👤 **作者**：Zhihan Ren、Lijun He、Jiaxi Liang、Xinzhu Fu、Haixia Bi、Fan Li

- 🎯 **研究动机**：已有特征 inversion 攻击重建质量有限，难以评估 Split DNN 真实隐私泄漏程度
- 🔬 **研究方法**：FIA-Flow 用 Latent Feature Space Alignment 模块弥合中间特征与潜空间的语义鸿沟，Deterministic Inversion Flow Matching 单步把离流形特征投影回目标流形，仅需少量图像-特征对
- 📌 **结论**：跨 AlexNet、ResNet、Swin、DINO、YOLO11 多层实现更忠实且语义对齐的反演，泄漏威胁比先前认知更严重

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Split DNNs enable edge devices by offloading intensive computation to a cloud server, but this paradigm exposes privacy vulnerabilities, as the intermediate features can be exploited to reconstruct the private inputs via Feature Inversion Attack (FIA). Existing FIA methods often produce limited reconstruction quality, making it difficult to assess the true extent of privacy leakage. To reveal the privacy risk of the leaked features, we introduce FIA-Flow, a black-box FIA framework that achieves high-fidelity image reconstruction from intermediate features. To exploit the semantic information within intermediate features, we design a Latent Feature Space Alignment Module (LFSAM) to bridge the semantic gap between the intermediate feature space and the latent space. Furthermore, to rectify distributional mismatch, we develop Deterministic Inversion Flow Matching (DIFM), which projects off-manifold features onto the target manifold with one-step inference. This decoupled design simplifies learning and enables effective training with few image-feature pairs. To quantify privacy leakage from a human perspective, we also propose two metrics based on a large vision-language model. Experiments show that FIA-Flow achieves more faithful and semantically aligned feature inversion across various models (AlexNet, ResNet, Swin Transformer, DINO, and YOLO11) and layers, revealing a more severe privacy threat in Split DNNs than previously recognized.

</details>

### 63. Efficient Privacy Auditing for Generative Model via Local Information

🌐 [Project](https://doi.org/10.1145/3770855.3817793)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`generative model privacy`、`membership signal`、`local information`、`audit`

- 🎯 **研究动机**：整图相似度 MIA 在泄露集中于局部区域时会低估隐私风险；黑盒设定下 DP 微调扩散模型的实际泄露难评估
- 🔬 **研究方法**：利用局部图像信息提升泄露信号可分性，并借扩散模型 inpainting 接口做区域聚焦审计以降低采样方差
- 📌 **结论**：跨不同微调与审计设定提供比整图审计更可靠的经验隐私评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models have become the dominant approach for text-to-image generation, but their ability to memorize training data raises increasing concerns about privacy leakage. Differential privacy (DP) is widely adopted to mitigate such privacy risks during model fine-tuning, yet the practical privacy leakage of differentially private diffusion models remains difficult to assess, especially in black-box settings where only generated images are observable. Existing auditing methods for diffusion models typically rely on membership inference attacks based on whole-image similarity between generated samples and target images. However, such approaches may underestimate privacy leakage when similarity between generated images and training samples is concentrated in localized image regions rather than at the whole-image level. In this work, we explore privacy leakage in diffusion models fine-tuned with differential privacy from a black-box perspective. We propose an empirical privacy assessment framework that leverages local image information, instead of treating images as indivisible wholes, to improve the distinguishability of privacy leakage signals. To improve privacy auditing efficiency and reduce sampling variance, we further leverage the image inpainting interface of diffusion models to perform region-focused auditing in a fully black-box setting. Extensive experiments across different fine-tuning and auditing settings demonstrate that our approach provides more reliable empirical assessments of privacy leakage than whole-image-based auditing methods.

</details>

### 64. Deletion Isn't Enough: Auditing RAG for Selective Forgetting

🌐 [Project](https://doi.org/10.1145/3805712.3808545)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`analysis`、`RAG disclosure`、`post-revocation leakage`、`selective-forgetting audit`、`audit`、`RAG revocation`

- 🎯 **研究动机**：RAG删除知识后是否真正被遗忘缺审计手段
- 🔬 **研究方法**：构造paired disclosure probe审计撤回后的残留泄漏
- 📌 **结论**：删除操作后的RAG仍可泄露应被遗忘的内容

### 65. Rethinking Visual Privacy: A Compositional Privacy Risk Framework for Severity Assessment with VLMs

📄 [arXiv](https://arxiv.org/abs/2603.21573) · 🌐 [Project](https://eccv.ecva.net/virtual/2026/poster/5562)　📅 2026-03　🏷 ECCV 2026

**关键词**：`tool`、`benchmark`、`visual privacy`、`compositional risk`、`severity evaluation`

👤 **作者**：Efthymios Tsaprazlis、Tiantian Feng、Anil Ramakrishna、Sai Praneeth Karimireddy、Rahul Gupta、Shrikanth Narayanan

- 🎯 **研究动机**：视觉隐私基准把隐私当二元属性，忽视单独良性属性组合可产生严重违规
- 🔬 **研究方法**：提出组合隐私风险分类法 CPRT，按独立可识别性与组合危害组织视觉属性，定义四级严重度与可解释打分函数，并构建 6.7K 图像数据集
- 📌 **结论**：前沿 VLM 在结构化引导下对齐良好但系统性低估组合风险；8B SFT 模型可接近前沿水平

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing visual privacy benchmarks largely treat privacy as a binary property, labeling images as private or non-private based on visible sensitive content. We argue that privacy is fundamentally compositional. Attributes that are benign in isolation may combine to produce severe privacy violations. We introduce the Compositional Privacy Risk Taxonomy (CPRT), a regulation-aware framework that organizes visual attributes according to standalone identifiability and compositional harm potential. CPRT defines four graded severity levels and is paired with an interpretable scoring function that assigns continuous privacy severity scores. We further construct a taxonomy-aligned dataset of 6.7K images and derive compositional risk scores. By evaluating frontier and open-weight VLMs we find that frontier models align well with compositional severity when provided structured guidance, but systematically underestimate composition-driven risks. Smaller models struggle to internalize graded privacy reasoning. To bridge this gap, we introduce a deployable 8B SFT model that closely matches frontier-level performance on compositional privacy assessment

</details>

### 66. Estimating near-verbatim extraction risk in language models with decoding-constrained beam search

📄 [arXiv](https://arxiv.org/abs/2603.24917) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-03

**关键词**：`attack`、`detection`、`near-verbatim extraction`、`beam search`、`machine unlearning`、`privacy risk`

👤 **作者**：A. Feder Cooper、…、Percy Liang

- 🎯 **研究动机**：近逐字提取风险量化代价过高：近逐字后缀组合爆炸，可靠蒙特卡洛需每序列约 10 万样本
- 🔬 **研究方法**：提出 decoding-constrained beam search，以约 20 个蒙特卡洛样本的代价给出近逐字提取风险的确定性下界
- 📌 **结论**：揭示逐字方法看不到的信息：更多可提取序列、更大的单序列提取质量及跨模型规模与文本类型的规律

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work shows that standard greedy-decoding extraction methods for quantifying memorization in LLMs miss how extraction risk varies across sequences. Probabilistic extraction -- computing the probability of generating a target suffix given a prefix under a decoding scheme -- addresses this, but is tractable only for verbatim memorization, missing near-verbatim instances that pose similar privacy and copyright risks. Quantifying near-verbatim extraction risk is expensive: the set of near-verbatim suffixes is combinatorially large, and reliable Monte Carlo (MC) estimation can require ~100,000 samples per sequence. To mitigate this cost, we introduce decoding-constrained beam search, which yields deterministic lower bounds on near-verbatim extraction risk at a cost comparable to ~20 MC samples per sequence. Across experiments, our approach surfaces information invisible to verbatim methods: many more extractable sequences, substantially larger per-sequence extraction mass, and patterns in how near-verbatim extraction risk manifests across model sizes and types of text.

</details>

### 67. Be Careful When Fine-tuning On Open-Source LLMs: Your Fine-tuning Data Could Be Secretly Stolen!

📄 [arXiv](https://arxiv.org/abs/2505.15656) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10010368)　📅 2025-05　🏷 ICLR 2026

**关键词**：`attack`、`fine-tuning privacy`、`data theft`、`backdoored model`

👤 **作者**：Zhexin Zhang、…、Minlie Huang

- 🎯 **研究动机**：在开源 LLM 上以私有数据微调已成标准流程，模型作者窃取下游微调数据的风险未被审视
- 🔬 **研究方法**：揭示开源模型作者可通过预埋后门，仅凭对下游微调模型的黑盒访问提取微调数据
- 📌 **结论**：3B 至 32B 四个模型上可完整提取最多 76.3% 的 5000 条微调查询，理想设置达 94.9%，检测防御可被绕过

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fine-tuning on open-source Large Language Models (LLMs) with proprietary data is now a standard practice for downstream developers to obtain task-specific LLMs. Surprisingly, we reveal a new and concerning risk along with the practice: the creator of the open-source LLMs can later extract the private downstream fine-tuning data through simple backdoor training, only requiring black-box access to the fine-tuned downstream model. Our comprehensive experiments, across 4 popularly used open-source models with 3B to 32B parameters and 2 downstream datasets, suggest that the extraction performance can be strikingly high: in practical settings, as much as 76.3% downstream fine-tuning data (queries) out of a total 5,000 samples can be perfectly extracted, and the success rate can increase to 94.9% in more ideal settings. We also explore a detection-based defense strategy but find it can be bypassed with improved attack. Overall, we highlight the emergency of this newly identified data breaching risk in fine-tuning, and we hope that more follow-up research could push the progress of addressing this concerning risk. The code and data used in our experiments are released at https://github.com/thu-coai/Backdoor-Data-Extraction.

</details>

### 68. Black-Box Membership Inference via Word-Level Probability Estimation
📄 [arXiv](https://arxiv.org/abs/2609.10611) · 🐙 [Code](https://github.com/niusj03/WPMIA)　📅 2026-09


👤 **作者**：Shengjie Niu、Yeheng Ge、Jian Huang

**关键词**：`attack`、`black-box membership inference`、`word-level probability`、`proprietary LLM`

- 🎯 **研究动机**：现有 MIA 需 per-token logits，对只返回文本续写的商用 LLM 不可用
- 🔬 **研究方法**：蒙特卡洛采样+局部核平滑估计词级生成概率，聚合为序列级似然并按不同前缀条件化放大成员/非成员分布差
- 📌 **结论**：GPT-5/Gemini-2.5-Flash/Claude-4.5-Haiku 上平均 TPR@5%FPR 达 42.0

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Membership inference attacks (MIAs) have emerged as critical tools for auditing privacy risks in large language models (LLMs), aiming to determine whether a given text was included in a model's training corpus. However, most existing MIAs require access to per-token logits or probabilities, making them inapplicable in practice to proprietary LLMs that expose only textual continuations. To address this underexplored setting, we propose Word-level Probability MIA (WPMIA), a statistically principled MIA for strict black-box privacy auditing. WPMIA estimates word-level generation probabilities via Monte Carlo sampling with local kernel smoothing, then aggregates these estimates into a sequence-level likelihood estimator. Furthermore, WPMIA constructs the likelihood conditioned on different prefixes, thereby amplifying the distributional differences between members and non-members. We evaluate WPMIA across various open-source LLMs and find that it consistently outperforms existing black-box baselines. Importantly, we also evaluate WPMIA on modern proprietary LLMs, including GPT-5-Chat, Gemini-2.5-Flash, and Claude-4.5-Haiku, achieving an average TPR@5\%FPR of 42.0 across these models. These results offer a sound foundation for future research on strict black-box membership inference. Code is available at \href{https://github.com/niusj03/WPMIA}{https://github.com/niusj03/WPMIA}.

</details>