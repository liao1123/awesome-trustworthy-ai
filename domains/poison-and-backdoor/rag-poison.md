# RAG 投毒

[返回投毒与后门目录](README.md)

## 研究方向

RAG 投毒研究攻击者如何在 document ingestion、embedding/index、retrieval、reranking、reasoning 与 generation 各阶段操纵外部证据，使恶意文本、图像、metadata、graph relation 或 Agent memory 被召回并改变最终行为。该方向覆盖 targeted 与 query-agnostic poisoning、single-document 与 coordinated-document attack、retriever training-data poisoning／checkpoint backdoor／parameter editing、GraphRAG／Multimodal RAG／Agentic RAG，以及 admission filtering、runtime detection、responsibility attribution、evidence isolation、robust aggregation 和 certified defense；评测必须同时区分 poison retrieval、context inclusion 与 end-to-end answer／action manipulation。

## 研究脉络

- **2024 · Threat Model：** PoisonedRAG 将 knowledge-base write access 形式化为少量文档即可控制 target answer 的攻击面，随后工作扩展到 natural trigger、retriever training poisoning／backdoor、imperceptible document content 与 Agent memory。
- **2025 · Practical & Cross-Stage Optimization：** 攻击从 known query、multi-document 和 white-box assumption 转向 single-document、black-box feedback、query-agnostic transfer，并联合优化 retriever 与 generator；data loader、visual document 和 multimodal knowledge base 也成为独立入口。
- **Detection & Forensics：** 防线从 lexical／perplexity filtering 发展到 gradient token、activation、attention、counterfactual replay 与 responsibility attribution，定位粒度由 document 进一步下沉到 token 或 character span。
- **2026 · Pipeline, Model Editing & System Expansion：** 研究开始覆盖 retriever parameter editing、chunking、reranking、GraphRAG、multi-hop Agent、knowledge evolution、competing attacker 及 action-oriented security agent，说明干净 corpus 不等于干净 retrieval model，retrieval hit 也不能替代 end-to-end ASR。
- **Current Boundary：** adaptive attack 可同时绕过 admission control、reranking 与 model consensus；更可信的方向是明确 attack budget 和 honest-majority assumption 的 certified aggregation，并持续报告 clean utility、latency 与 residual ASR。

> Review 顺序按 primary attack surface 与 defense stage 组织；同一论文在本页只进入最匹配的一个分表，跨 domain 收录继续使用 ↗ 标记。

## Survey & Threat Model

### 1. Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2608.24977)　📅 2026-08

**关键词**：`survey`、`RAG threat model`、`pipeline-aware defense`、`traceback`、`RAG privacy`、`pipeline threat model`

👤 **作者**：Minh Tran、…、Suhang Wang

- 🎯 **研究动机**：RAG 引入投毒、后门、隐私与公平风险，既有综述对攻击者目标、威胁模型与阶段化防御覆盖不完整
- 🔬 **研究方法**：以 pipeline 视角统一综述：形式化 corpus、retriever、generator 威胁模型，按 accuracy、privacy、fairness 组织攻击，按 retrieval 到 traceback 四阶段梳理防御
- 📌 **结论**：给出全流程 RAG 鲁棒性的统一威胁-防御图谱与评测、可解释性方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances large language models by grounding outputs in external knowledge, improving factuality and reducing hallucinations. At the same time, the retrieval-augmented pipeline introduces new robustness and security risks, including corpus poisoning, backdoor attacks, privacy leakage, and fairness violations. Despite rapid progress in this area, existing surveys remain limited in their treatment of attacker objectives, threat models, and stage-specific defenses across the full RAG pipeline. This survey presents a unified and pipeline-aware overview of RAG robustness. We formalize threat models over the corpus, retriever, and generator, and organize attacks into three main objectives: accuracy, privacy, and fairness. We further review defenses from a pipeline-aware perspective, covering the retrieval, rerank, generation, and traceback stages. In addition, we summarize robustness benchmarks and explainability methods for more deeply evaluating and explaining RAG robustness.

</details>
### Document Ingestion, Camouflage & Source Manipulation

### 2. CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents

📄 [arXiv](https://arxiv.org/abs/2608.28389)　📅 2026-08

**关键词**：`attack`、`RAG poisoning`、`document camouflage`、`dispersion token`

👤 **作者**：Jaewon Jung、Haizhong Zheng、Hongsun Jang、Jaeyong Song、Beidi Chen、Jinho Lee

- 🎯 **研究动机**：RAG 投毒攻击常靠把目标查询插入投毒文档提升检索命中率，但留下词汇与 embedding 痕迹、易被查询检测过滤
- 🔬 **研究方法**：提出 CamoDocs，把合成的良性与对抗草稿分块混编，在良性块替换 dispersion token 使投毒文档 embedding 分散，并用连贯性过滤控制可读性损失
- 📌 **结论**：跨七种 RAG 防御、三个开源 LLM、三个 benchmark 保持强平均 ASR 且无查询重叠痕迹，对 GPT-5.4-mini 与 Claude-Haiku-4.5 平均 ASR 达 61.80% 与 55.09%；TrustRAG 等擦除型聚类防御只能以明显效用下降换取缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.

</details>

### 3. SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.28074) · 🌐 [Project](https://doi.org/10.1145/3770855.3818186)　📅 2026-05　🏷 KDD 2026

**关键词**：`attack`、`RAG poisoning`、`semantics-preserving`、`retrieval hijacking`、`semantic preservation`

👤 **作者**：Jiachen Qian

- 🎯 **研究动机**：RAG 语料完整性漏洞下，现有毒文档生硬易察觉或检索不稳定
- 🔬 **研究方法**：SilentRetrieval 两阶段：Coordinated Beam Search 多 token 联合优化保持可检索性并约束困惑度，Context-Adaptive Trigger Generation 由冻结 LLM 把操纵触发融入内容
- 📌 **结论**：NQ 与 MS MARCO 上 HR@10 达 84.6%/81.3%、ASR-LLM 57.5%/54.8% 且困惑度近良性；对 ColBERT 等未见检索器平均 HR@10 64.7%，Wikipedia 规模 0.016% 投毒率仍达 74.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) mitigates LLM hallucinations but introduces a critical vulnerability: corpus integrity. We present SilentRetrieval, a two-stage data poisoning attack that hijacks RAG systems through adversarially crafted yet fluent documents. Stage 1 uses Coordinated Beam Search, a multi-token joint optimization method with a fluency-similarity objective, to keep a poisoned host document retrievable while constraining perplexity. Stage 2 uses Context-Adaptive Trigger Generation, a lightweight trigger-fusion step driven by a frozen LLM, to integrate manipulation triggers into document content. Under a one-poisoned-document-per-query evaluation with synthetic target answers, SilentRetrieval achieves 84.6%/81.3% HR@10 and 57.5%/54.8% ASR-LLM on Natural Questions and MS MARCO, while maintaining near-benign perplexity. Cross-model evaluation across four target LLMs shows nontrivial effectiveness under a fixed trigger generator, and transfer tests against unseen retrievers, including ColBERT and commercial embedding models, yield 64.7% average HR@10 under the same injected-corpus protocol. In a sampled Wikipedia-scale evaluation, SilentRetrieval retains 74.2% HR@10 at a 0.016% poisoning ratio. Combined retrieval-side and generation-side defenses reduce attack success substantially but incur a latency trade-off. Human evaluation shows substantially lower flag rates than disfluent baselines, while remaining numerically more suspicious than benign content at the current sample size.

</details>

### 4. The Hidden Threat in Plain Text: Attacking RAG Data Loaders

📄 [arXiv](https://arxiv.org/abs/2507.05093)　📅 2025-07

**关键词**：`attack`、`document ingestion`、`content obfuscation`、`parser differential`

👤 **作者**：Alberto Castagnaro、Umberto Salviati、Mauro Conti、Luca Pajola、Simeone Pizzi

- 🎯 **研究动机**：RAG 数据加载阶段的安全缺口未被审视
- 🔬 **研究方法**：提出 9 类知识投毒攻击分类法与 Content Obfuscation、Content Injection 两个新威胁向量，以 19 种隐蔽注入技术的自动工具箱测五个加载器
- 📌 **结论**：357 个场景平均攻击成功率 74.4%，NotebookLM 与 OpenAI Assistants 等六个端到端系统均被攻破

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have transformed human-machine interaction since ChatGPT's 2022 debut, with Retrieval-Augmented Generation (RAG) emerging as a key framework that enhances LLM outputs by integrating external knowledge. However, RAG's reliance on ingesting external documents introduces new vulnerabilities. This paper exposes a critical security gap at the data loading stage, where malicious actors can stealthily corrupt RAG pipelines by exploiting document ingestion. We propose a taxonomy of 9 knowledge-based poisoning attacks and introduce two novel threat vectors -- Content Obfuscation and Content Injection -- targeting common formats (DOCX, HTML, PDF). Using an automated toolkit implementing 19 stealthy injection techniques, we test five popular data loaders, finding a 74.4% attack success rate across 357 scenarios. We further validate these threats on six end-to-end RAG systems -- including white-box pipelines and black-box services like NotebookLM and OpenAI Assistants -- demonstrating high success rates and critical vulnerabilities that bypass filters and silently compromise output integrity. Our results emphasize the urgent need to secure the document ingestion process in RAG systems against covert content manipulations.

</details>

### 5. The RAG Paradox: A Black-Box Attack Exploiting Unintentional Vulnerabilities in Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2502.20995)　📅 2025-02

**关键词**：`attack`、`reference-feedback attack`、`source transparency`、`credible poison`

👤 **作者**：Chanwoo Choi、Jinsoo Kim、Sukmin Cho、Soyeong Jeong、Buru Chang

- 🎯 **研究动机**：RAG 展示检索文档与来源以建立信任，却向黑盒攻击者暴露可利用反馈
- 🔬 **研究方法**：基于引用反馈观察被使用来源与措辞，向被识别来源上传自然可信且易被检索的毒文档
- 📌 **结论**：无需内部组件访问即可显著降低系统性能，offline 与 online 实验均验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing adoption of retrieval-augmented generation (RAG) systems, various attack methods have been proposed to degrade their performance. However, most existing approaches rely on unrealistic assumptions in which external attackers have access to internal components such as the retriever. To address this issue, we introduce a realistic black-box attack based on the RAG paradox, a structural vulnerability arising from the system's effort to enhance trust by revealing both the retrieved documents and their sources to users. This transparency enables attackers to observe which sources are used and how information is phrased, allowing them to craft poisoned documents that are more likely to be retrieved and upload them to the identified sources. Moreover, as RAG systems directly provide retrieved content to users, these documents must not only be retrievable but also appear natural and credible to maintain user confidence in the search results. Unlike prior work that focuses solely on improving document retrievability, our attack method explicitly considers both retrievability and user trust in the retrieved content. Both offline and online experiments demonstrate that our method significantly degrades system performance without internal access, while generating natural-looking poisoned documents.

</details>

### 6. Human-Imperceptible Retrieval Poisoning Attacks in LLM-Powered Applications

📄 [arXiv](https://arxiv.org/abs/2404.17196)　📅 2024-04

**关键词**：`attack`、`document camouflage`、`framework ingestion`、`real-world RAG`

👤 **作者**：Quan Zhang、Binqi Zeng、Chijin Zhou、Gwihwan Go、Heyuan Shi、Yu Jiang

- 🎯 **研究动机**：LLM 应用开发框架对外部内容缺乏信任边界设计，RAG 可被外部文档误导
- 🔬 **研究方法**：构造与良性文档视觉不可区分的伪装文档，内容正确但被 RAG 引用即误导应用给出错误回答
- 📌 **结论**：误导 LLM 的成功率达 88.33%，真实应用中达 66.67%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Presently, with the assistance of advanced LLM application development frameworks, more and more LLM-powered applications can effortlessly augment the LLMs' knowledge with external content using the retrieval augmented generation (RAG) technique. However, these frameworks' designs do not have sufficient consideration of the risk of external content, thereby allowing attackers to undermine the applications developed with these frameworks. In this paper, we reveal a new threat to LLM-powered applications, termed retrieval poisoning, where attackers can guide the application to yield malicious responses during the RAG process. Specifically, through the analysis of LLM application frameworks, attackers can craft documents visually indistinguishable from benign ones. Despite the documents providing correct information, once they are used as reference sources for RAG, the application is misled into generating incorrect responses. Our preliminary experiments indicate that attackers can mislead LLMs with an 88.33\% success rate, and achieve a 66.67\% success rate in the real-world application, demonstrating the potential impact of retrieval poisoning.

</details>

### 7. Typos that Broke the RAG's Back: Genetic Attack on RAG Pipeline by Simulating Documents in the Wild via Low-level Perturbations

📄 [arXiv](https://arxiv.org/abs/2404.13948) · 🎓 [Official](https://aclanthology.org/2024.findings-emnlp.161/)　📅 2024-04　🏷 EMNLP 2024

**关键词**：`attack`、`low-level perturbation`、`pipeline robustness`、`genetic attack`

👤 **作者**：Sukmin Cho、Soyeong Jeong、Jeongyeon Seo、Taeho Hwang、Jong C. Park

- 🎯 **研究动机**：RAG 鲁棒性研究忽略组件间耦合与真实库中轻微文本错误的威胁
- 🔬 **研究方法**：GARAG 用遗传搜索生成低层字符扰动模拟野外文档，逐组件并端到端评估整条管线
- 📌 **结论**：多 QA 数据集、retriever 与 LLM 组合上持续高 ASR，轻微 typo 即可放大为整条管线失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The robustness of recent Large Language Models (LLMs) has become increasingly crucial as their applicability expands across various domains and real-world applications. Retrieval-Augmented Generation (RAG) is a promising solution for addressing the limitations of LLMs, yet existing studies on the robustness of RAG often overlook the interconnected relationships between RAG components or the potential threats prevalent in real-world databases, such as minor textual errors. In this work, we investigate two underexplored aspects when assessing the robustness of RAG: 1) vulnerability to noisy documents through low-level perturbations and 2) a holistic evaluation of RAG robustness. Furthermore, we introduce a novel attack method, the Genetic Attack on RAG (\textit{GARAG}), which targets these aspects. Specifically, GARAG is designed to reveal vulnerabilities within each component and test the overall system functionality against noisy documents. We validate RAG robustness by applying our \textit{GARAG} to standard QA datasets, incorporating diverse retrievers and LLMs. The experimental results show that GARAG consistently achieves high attack success rates. Also, it significantly devastates the performance of each component and their synergy, highlighting the substantial risk that minor textual inaccuracies pose in disrupting RAG systems in the real world.

</details>
### Retriever-Aware Corpus Poisoning & Ranking Manipulation

本节保持 deployed retriever 参数不变：攻击者可以读取或查询 encoder、利用其梯度或相似度优化毒 passage，也可以操纵 corpus、trigger 与 reranking，但不会污染 retriever 的训练数据、checkpoint 或权重；直接改变检索编码器的工作进入下一节。

### 8. CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation

📄 [arXiv](https://arxiv.org/abs/2609.02774) · 🤗 [Model](https://huggingface.co/counter-geo/c-geo-guard) · 📊 [Dataset](https://huggingface.co/datasets/counter-geo/counter-geo-bench)　📅 2026-09

**关键词**：`attack`、`RACG poisoning`、`code vulnerability injection`、`semantic mislabeling`

👤 **作者**：Varun Gadey、Ziad Marey、Alexandra Dmitrienko

- 🎯 **研究动机**：既有 RACG 投毒只挑选现存漏洞样本提升总体漏洞率，黑盒攻击者能否定向构造并传播自选弱点未解
- 🔬 **研究方法**：提出 CodePoisonRAG：把良性修复代码条目转化为毒化 artifact，攻击链组合嵌入选定 source-to-sink 流的 CWE 特定漏洞注入与不修复行为却添加虚假安全声明的语义误标，每任务至多注入一个 artifact
- 📌 **结论**：85 个覆盖十类 CWE 的毒化 artifact（语料占比 0.7%）全部进入对应查询 Top-3，三个生成器上 ASR 0.80-0.93；面对注入安全知识的 CodeGuarder 仍保有 0.40-0.71

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Code Generation (RACG) improves LLM-based software development by retrieving external code artifacts, documentation, and patches, and incorporating them into the generation context. This reliance on external knowledge introduces a critical trust boundary: poisoned artifacts can influence generated code without modifying the underlying LLM. Prior work shows that selecting existing vulnerable examples can increase the general vulnerability rate of RACG outputs, but leaves open whether a black-box attacker can construct a single task-matched artifact that propagates an attacker-selected weakness. We introduce CodePoisonRAG, a targeted upstream knowledge-poisoning framework that transforms benign fixed-code entries into poisoned artifacts. Its attack chain combines CWE-specific Vulnerability Injection, which embeds a selected source-to-sink flow while retaining task alignment, with Semantic Mislabeling, which adds false safety claims without repairing the vulnerable behavior. The attacker has no access to the victim's deployed knowledge base, retriever, re-ranker, generator, prompt, or defense mechanism and injects at most one artifact per anticipated programming task. We construct 85 poisoned artifacts covering ten CWE classes across Java and C, yielding an aggregate corpus-poisoning ratio of 0.7%. Across three generators, all 85 artifacts appear among the Top-3 results for their corresponding queries, and CodePoisonRAG achieves attack success rates between 0.80 and 0.93. Against CodeGuarder, which injects vulnerability-specific security knowledge into the generation context, the attack retains success rates between 0.40 and 0.71. These results show that RACG poisoning extends beyond the incidental propagation of existing vulnerabilities to the targeted construction and propagation of attacker-selected weaknesses.

</details>

### 9. VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models

📄 [arXiv](https://arxiv.org/abs/2609.01325)　📅 2026-09

**关键词**：`attack`、`corpus poisoning`、`neural ranking`、`verifiable RLVR`

👤 **作者**：Zhiqi Huang、Vivek Datla、Zhichao Xu、Puxuan Yu、Vivek Srikumar、Alfy Samuel

- 🎯 **研究动机**：neural ranking 模型面对 LLM 规模生成的流畅欺骗性内容时的投毒脆弱性理解不足，且缺少可验证优化目标
- 🔬 **研究方法**：提出 VerTox：把 corpus poisoning 形式化为 verifiable reward RL（RLVR）问题，通过把排序扭曲与事实腐蚀耦合的 reward shaping 把紧凑 LLM 微调成对抗文档生成器
- 📌 **结论**：在主要排序架构与商用 embedding 模型上接近满分 ASR，生成文档流畅低困惑度难检测，并显著降低下游 RAG 性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural ranking models have become core components of modern information retrieval systems and important building blocks of AI systems such as retrieval-augmented generation (RAG) pipelines. However, their robustness remains insufficiently understood in the presence of large language models (LLMs), which can generate fluent and deceptive content at scale. This work investigates the vulnerability of neural ranking models to corpus poisoning attacks, in which an adversary injects a small number of maliciously crafted documents into the corpus to distort ranking behavior. We propose VerTox, the first framework to formulate corpus poisoning as a verifiable reward-guided reinforcement learning (RLVR) problem. By explicitly coupling ranking distortion with factual corruption through specialized reward shaping, we fine-tune compact LLMs into adversarial generators. Experiments demonstrate that our method achieves near-perfect attack success rates, producing adversarial documents that frequently rank higher than target documents across major neural ranking architectures, as well as a proprietary commercial embedding model. The generated adversarial documents are fluent and exhibit low perplexity, making them difficult to detect. Furthermore, by explicitly encouraging factual corruption, our adversarial documents significantly degrade the performance of a downstream RAG application.

</details>

### 10. WARP: A Word-Level Backdoor Attack Targeting RAG Systems via Retrieval Corpus Poisoning

🌐 [Project](https://doi.org/10.1145/3770854.3780227)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`RAG backdoor`、`word-level trigger`、`corpus poisoning`

- 🎯 **研究动机**：RAG 语料库可被注入含触发器的恶意文档，诱导 LLM 产生攻击者控制的输出，词级后门未被研究
- 🔬 **研究方法**：提出 WARP：把对抗文本在嵌入空间约束优化为与触发器高度相似并附加攻击者内容（如钓鱼链接），查询含指定词即检索到对抗语料
- 📌 **结论**：多检索器、主流 LLM 与真实语料上平均 ASR 达 55.8%（提升 17.2%），良性查询退化不足 0.1%，对抗文本困惑度较 SOTA 降 95.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems retrieve relevant documents from a corpus database to mitigate issues like hallucination, outdated knowledge, and limited domain coverage. While enhancing large language models (LLMs) performance, RAG also introduces a new attack surface: adversaries can inject trigger-embedded malicious documents into the corpus database, potentially causing the LLM to produce attacker-controlled outputs. To expose this vulnerability, we propose the first word-level backdoor attack targeting RAG systems through retrieval corpus poisoning named WARP. WARP crafts adversarial texts that are highly similar to triggers in embedding space, and appends attacker-controlled content (e.g. malicious phishing links) to generate adversarial corpus (advCorps). When a user's query contains a well-designated word-level trigger, these advCorps are retrieved, prompting the LLM to generate attacker-specified outputs. We formulate the generation of adversarial texts as a constrained optimization problem in embedding space, ensuring that trigger-related queries lead the RAG's retriever to accurately select the advCorps. To demonstrate the real-world threat, we craft adversarial texts with phishing links and deploy a word-level backdoor attack against RAG across multiple retrievers, mainstream LLMs, and real-world corpora. WARP achieves a robust average ASR of 55.8%, improving upon existing methods by 17.2%, with less than 0.1% degradation on benign queries. Moreover, WARP-generated adversarial texts exhibit an average perplexity of 69.98, representing a 95.6% reduction compared to state-of-the-art (SOTA) baselines, demonstrating superior linguistic naturalness and stealth.

</details>

### 11. RefineRAG: Word-Level Poisoning Attacks via Retriever-Guided Text Refinement

📄 [arXiv](https://arxiv.org/abs/2604.07403)　📅 2026-04

**关键词**：`attack`、`word-level poisoning`、`retriever-in-the-loop`、`black-box transfer`

👤 **作者**：Ziye Wang、Guanyu Wang、Kailong Wang

- 🎯 **研究动机**：PoisonedRAG 等 RAG 知识投毒采用粗糙的分离拼接策略，毒文本易被检出
- 🔬 **研究方法**：RefineRAG 把投毒建模为词级精炼：Macro Generation 生成可诱导目标答案的 toxic seed，Micro Refinement 以 retriever-in-the-loop 优化检索优先级与自然度
- 📌 **结论**：NQ 上 ASR 达 90%，语法错误与重复率最低，且经 proxy 优化可迁移到黑盒受害系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) significantly enhances Large Language Models (LLMs), but simultaneously exposes a critical vulnerability to knowledge poisoning attacks. Existing attack methods like PoisonedRAG remain detectable due to coarse-grained separate-and-concatenate strategies. To bridge this gap, we propose RefineRAG, a novel framework that treats poisoning as a holistic word-level refinement problem. It operates in two stages: Macro Generation produces toxic seeds guaranteed to induce target answers, while Micro Refinement employs a retriever-in-the-loop optimization to maximize retrieval priority without compromising naturalness. Evaluations on NQ and MSMARCO demonstrate that RefineRAG achieves state-of-the-art effectiveness, securing a 90% Attack Success Rate on NQ, while registering the lowest grammar errors and repetition rates among all baselines. Crucially, our proxy-optimized attacks successfully transfer to black-box victim systems, highlighting a severe practical threat.

</details>

### 12. Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems

📄 [arXiv](https://arxiv.org/abs/2603.18034)　📅 2026-03

**关键词**：`attack`、`dual-document poisoning`、`hybrid retrieval`、`adaptive attack`

👤 **作者**：Scott Thornton

- 🎯 **研究动机**：RAG 语料投毒攻击效果是否跨语料成立缺乏大规模证据
- 🔬 **研究方法**：用 GCG 优化 sleeper 与 trigger 双文档投毒 Security Stack Exchange（67,941 文档、50 次攻击），并评估 BM25+向量混合检索防御
- 📌 **结论**：纯向量检索共检率 38%，混合检索降至 0%；攻击者联合优化稀疏与稠密信号后回升至 20-44%，FEVER 上恒为 0%——攻击高度依赖语料

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge sources but introduce new attack surfaces through the retrieval pipeline. In particular, adversaries can poison retrieval corpora so that malicious documents are preferentially retrieved at inference time, enabling targeted manipulation of model outputs. We study gradient-guided corpus poisoning attacks against modern RAG pipelines and evaluate retrieval-layer defenses that require no modification to the underlying LLM. We implement dual-document poisoning attacks consisting of a sleeper document and a trigger document optimized using Greedy Coordinate Gradient (GCG). In a large-scale evaluation on the Security Stack Exchange corpus (67,941 documents) with 50 attack attempts, gradient-guided poisoning achieves a 38.0 percent co-retrieval rate under pure vector retrieval. We show that a simple architectural modification, hybrid retrieval combining BM25 and vector similarity, substantially mitigates this attack. Across all 50 attacks, hybrid retrieval reduces gradient-guided attack success from 38 percent to 0 percent without modifying the model or retraining the retriever. When attackers jointly optimize payloads for both sparse and dense retrieval signals, hybrid retrieval can be partially circumvented, achieving 20-44 percent success, but still significantly raises attack difficulty relative to vector-only retrieval. Evaluation across five LLM families (GPT-5.3, GPT-4o, Claude Sonnet 4.6, Llama 4, and GPT-4o-mini) shows attack success ranging from 46.7 percent to 93.3 percent. Cross-corpus evaluation on the FEVER Wikipedia dataset (25 attacks) yields 0 percent attack success across all retrieval configurations.

</details>

### 13. Reranker Helps, but Not Enough: Towards Strong Poisoning Attacks Against Retrieval-Augmented Generation

📝 [OpenReview](https://openreview.net/forum?id=Y54eyjHFqJ) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63324)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`RAG poisoning`、`reranker`、`character perturbation`、`backdoor attack`、`adversarial training`

👤 **作者**：Xiaokun Yang、Jian Liang、Yesheng Liu、Xin Xiong、Ran He、Tieniu Tan

- 🎯 **研究动机**：仅在良性语料微调的 reranker 无需对抗训练即可过滤恶意内容，使现有 RAG 投毒攻击失效
- 🔬 **研究方法**：总结揭示 reranker 盲区的实用提示设计原则，提出 P3A：规则式提示工程构造投毒文本，再注入约 1% 的字符级扰动促其被 reranker 排前
- 📌 **结论**：攻击有效性与迁移性强，即使仅投毒单个文档依然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) augments large language models with external knowledge, which in turn exposes their retrieval corpora to data poisoning risks. However, existing poisoning attacks exhibit limited effectiveness against RAG equipped with a reranker to enhance retrieval quality. Remarkably, this defensive capability requires no adversarial training: a reranker fine-tuned solely on benign, in-domain corpora can effectively filter malicious content. Towards realistic RAG red-teaming, we conclude practical prompt design principles that reveal reranker blind spots. Building on these insights, we introduce the Prompt-Perturbation Poisoning Attack ($\mathbf{P}^3 \mathbf{A}$). $\mathbf{P}^3 \mathbf{A}$ first employs rule-based prompt engineering to craft initial poisoned texts. It then injects subtle character-level perturbations into these texts, which promotes their ranking by the reranker while maintaining their adversarial effectiveness. These perturbations introduce only about 1\% textual change, ensuring the poisoned texts remain natural and readable. Extensive experiments show that $\mathbf{P}^3 \mathbf{A}$ achieves strong attack effectiveness and transferability, even when constrained to poisoning a single document. Code is available at https://github.com/YyyxKun/P3A.

</details>

### 14. Joint-GCG: Unified Gradient-Based Poisoning Attacks on Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2506.06151)　📅 2025-06

**关键词**：`attack`、`pipeline-joint optimization`、`gradient alignment`、`transferability`

👤 **作者**：Haowei Wang、…、Qing Wang

- 🎯 **研究动机**：既有 RAG 投毒把检索与生成阶段割裂优化，攻击效果受限
- 🔬 **研究方法**：提出 Joint-GCG 统一检索器与生成器的梯度攻击：跨词汇投影、梯度 tokenization 对齐与自适应加权融合
- 📌 **结论**：ASR 最高比此前方法高 25%、平均高 5%，毒文本对未见模型仍有强迁移性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems enhance Large Language Models (LLMs) by retrieving relevant documents from external corpora before generating responses. This approach significantly expands LLM capabilities by leveraging vast, up-to-date external knowledge. However, this reliance on external knowledge makes RAG systems vulnerable to corpus poisoning attacks that manipulate generated outputs via poisoned document injection. Existing poisoning attack strategies typically treat the retrieval and generation stages as disjointed, limiting their effectiveness. We propose Joint-GCG, the first framework to unify gradient-based attacks across both retriever and generator models through three innovations: (1) Cross-Vocabulary Projection for aligning embedding spaces, (2) Gradient Tokenization Alignment for synchronizing token-level gradient signals, and (3) Adaptive Weighted Fusion for dynamically balancing attacking objectives. Evaluations demonstrate that Joint-GCG achieves at most 25% and an average of 5% higher attack success rate than previous methods across multiple retrievers and generators. While optimized under a white-box assumption, the generated poisons show unprecedented transferability to unseen models. Joint-GCG's innovative unification of gradient-based attacks across retrieval and generation stages fundamentally reshapes our understanding of vulnerabilities within RAG systems. Our code is available at https://github.com/NicerWang/Joint-GCG.

</details>

### 15. PR-Attack: Coordinated Prompt-RAG Attacks on Retrieval-Augmented Generation in Large Language Models via Bilevel Optimization

📄 [arXiv](https://arxiv.org/abs/2504.07717) · 🌐 [Project](https://doi.org/10.1145/3726302.3730058)　📅 2025-04　🏷 SIGIR 2025

**关键词**：`attack`、`prompt-RAG coordination`、`bilevel optimization`、`backdoor trigger`

👤 **作者**：Yang Jiao、Xiaodong Wang、Kai Yang

- 🎯 **研究动机**：既有 RAG 攻击在毒文本受限时效果骤降、隐蔽性差且缺乏形式化优化框架
- 🔬 **研究方法**：提出 PR-Attack，向知识库注入少量毒文本并在 prompt 埋后门触发器，把攻击生成形式化为双层优化问题
- 📌 **结论**：毒文本数量受限时仍获高 ASR，隐蔽性显著优于既有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of applications, e.g., medical question-answering, mathematical sciences, and code generation. However, they also exhibit inherent limitations, such as outdated knowledge and susceptibility to hallucinations. Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm to address these issues, but it also introduces new vulnerabilities. Recent efforts have focused on the security of RAG-based LLMs, yet existing attack methods face three critical challenges: (1) their effectiveness declines sharply when only a limited number of poisoned texts can be injected into the knowledge database, (2) they lack sufficient stealth, as the attacks are often detectable by anomaly detection systems, which compromises their effectiveness, and (3) they rely on heuristic approaches to generate poisoned texts, lacking formal optimization frameworks and theoretic guarantees, which limits their effectiveness and applicability. To address these issues, we propose coordinated Prompt-RAG attack (PR-attack), a novel optimization-driven attack that introduces a small number of poisoned texts into the knowledge database while embedding a backdoor trigger within the prompt. When activated, the trigger causes the LLM to generate pre-designed responses to targeted queries, while maintaining normal behavior in other contexts. This ensures both high effectiveness and stealth. We formulate the attack generation process as a bilevel optimization problem leveraging a principled optimization framework to develop optimal poisoned texts and triggers. Extensive experiments across diverse LLMs and datasets demonstrate the effectiveness of PR-Attack, achieving a high attack success rate even with a limited number of poisoned texts and significantly improved stealth compared to existing methods.

</details>

### 16. Tricking Retrievers with Influential Tokens: An Efficient Black-Box Corpus Poisoning Attack

📄 [arXiv](https://arxiv.org/abs/2503.21315) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.210/)　📅 2025-03　🏷 ACL 2025

**关键词**：`attack`、`dense retriever poisoning`、`influential token`、`query-efficient attack`

👤 **作者**：Cheng Wang、Yiwei Wang、Yujun Cai、Bryan Hooi

- 🎯 **研究动机**：既有检索库投毒需梯度访问或大量算力，缓慢且昂贵
- 🔬 **研究方法**：提出 DIGA 黑盒遗传算法，利用检索器对 token 顺序不敏感、偏向 influential tokens 的特性动态调整遗传算子
- 📌 **结论**：时间与内存开销显著低于已有方法，多数据集上 ASR 相当或更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems enhance large language models by incorporating external knowledge, addressing issues like outdated internal knowledge and hallucination. However, their reliance on external knowledge bases makes them vulnerable to corpus poisoning attacks, where adversarial passages can be injected to manipulate retrieval results. Existing methods for crafting such passages, such as random token replacement or training inversion models, are often slow and computationally expensive, requiring either access to retriever's gradients or large computational resources. To address these limitations, we propose Dynamic Importance-Guided Genetic Algorithm (DIGA), an efficient black-box method that leverages two key properties of retrievers: insensitivity to token order and bias towards influential tokens. By focusing on these characteristics, DIGA dynamically adjusts its genetic operations to generate effective adversarial passages with significantly reduced time and memory usage. Our experimental evaluation shows that DIGA achieves superior efficiency and scalability compared to existing methods, while maintaining comparable or better attack success rates across multiple datasets.

</details>

### 17. GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search

📄 [arXiv](https://arxiv.org/abs/2412.20953) · 🌐 [Project](https://doi.org/10.1145/3719027.3765095)　📅 2024-12　🏷 ACM CCS 2025

**关键词**：`attack`、`dense retrieval poisoning`、`concept-level SEO`、`adaptive attack`

👤 **作者**：Matan Ben-Tov、Mahmood Sharif

- 🎯 **研究动机**：已有检索 SEO 攻击威胁模型宽松（单 query）、方法基线化、评测规模小
- 🔬 **研究方法**：GASLITE 生成不依赖 corpus、不改模型的对抗段落，携带攻击者信息且检索排名高，聚焦概念级 query 的 pertinence 攻击
- 📌 **结论**：九个先进 retriever 在低至 0.0001% 投毒率下仍易受概念级 SEO 影响；单 query SEO 被完全攻克，自适应攻击可绕过常见防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dense embedding-based text retrieval$\unicode{x2013}$retrieval of relevant passages from corpora via deep learning encodings$\unicode{x2013}$has emerged as a powerful method attaining state-of-the-art search results and popularizing Retrieval Augmented Generation (RAG). Still, like other search methods, embedding-based retrieval may be susceptible to search-engine optimization (SEO) attacks, where adversaries promote malicious content by introducing adversarial passages to corpora. Prior work has shown such SEO is feasible, mostly demonstrating attacks against retrieval-integrated systems (e.g., RAG). Yet, these consider relaxed SEO threat models (e.g., targeting single queries), use baseline attack methods, and provide small-scale retrieval evaluation, thus obscuring our comprehensive understanding of retrievers' worst-case behavior. This work aims to faithfully and thoroughly assess retrievers' robustness, paving a path to uncover factors related to their susceptibility to SEO. To this end, we, first, propose the GASLITE attack for generating adversarial passages, that$\unicode{x2013}$without relying on the corpus content or modifying the model$\unicode{x2013}$carry adversary-chosen information while achieving high retrieval ranking, consistently outperforming prior approaches. Second, using GASLITE, we extensively evaluate retrievers' robustness, testing nine advanced models under varied threat models, while focusing on pertinent adversaries targeting queries on a specific concept (e.g., a public figure). Amongst our findings: retrievers are highly vulnerable to SEO against concept-specific queries, even under negligible poisoning rates (e.g., $\geq$0.0001% of the corpus), while generalizing across different corpora and query distributions; single-query SEO is completely solved by GASLITE; adaptive attacks demonstrate bypassing common defenses; [...]

</details>

### 18. Corpus Poisoning via Approximate Greedy Gradient Descent

📄 [arXiv](https://arxiv.org/abs/2406.05087)　📅 2024-06

**关键词**：`attack`、`dense retrieval poisoning`、`AGGD`、`cross-domain generalization`

👤 **作者**：Jinyan Su、Preslav Nakov、Claire Cardie

- 🎯 **研究动机**：HotFlip 随机采样候选 token 浪费攻击预算，扰动质量受限
- 🔬 **研究方法**：AGGD 用结构化贪心搜索替代随机采样选择 token 级扰动，生成对抗段落
- 📌 **结论**：攻击 ANCE 在 NQ 与 MS MARCO 上比 HotFlip 高 15.24 与 17.44 个百分点，且能泛化到未见查询与新领域

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dense retrievers are widely used in information retrieval and have also been successfully extended to other knowledge intensive areas such as language models, e.g., Retrieval-Augmented Generation (RAG) systems. Unfortunately, they have recently been shown to be vulnerable to corpus poisoning attacks in which a malicious user injects a small fraction of adversarial passages into the retrieval corpus to trick the system into returning these passages among the top-ranked results for a broad set of user queries. Further study is needed to understand the extent to which these attacks could limit the deployment of dense retrievers in real-world applications. In this work, we propose Approximate Greedy Gradient Descent (AGGD), a new attack on dense retrieval systems based on the widely used HotFlip method for efficiently generating adversarial passages. We demonstrate that AGGD can select a higher quality set of token-level perturbations than HotFlip by replacing its random token sampling with a more structured search. Experimentally, we show that our method achieves a high attack success rate on several datasets and using several retrievers, and can generalize to unseen queries and new domains. Notably, our method is extremely effective in attacking the ANCE retrieval model, achieving attack success rates that are 15.24\% and 17.44\% higher on the NQ and MS MARCO datasets, respectively, compared to HotFlip. Additionally, we demonstrate AGGD's potential to replace HotFlip in other adversarial attacks, such as knowledge poisoning of RAG systems.

</details>

### 19. BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2406.00083)　📅 2024-06

**关键词**：`attack`、`retrieval backdoor`、`semantic trigger`、`generation steering`

👤 **作者**：Jiaqi Xue、Mengxin Zheng、Yebowen Hu、Fei Liu、Xun Chen、Qian Lou

- 🎯 **研究动机**：RAG 数据库多来自公开网络数据，检索环节的间接攻击面未被识别
- 🔬 **研究方法**：BadRAG 以语义群组（如政党、人物）作触发器投毒定制 passage 实现检索后门，间接攻击生成 LLM（DoS 与语义导向）而无需改动模型
- 📌 **结论**：仅投毒 10 篇即达 98.2% 检索召回，GPT-4 拒答率从 0.01% 升至 74.6%、负面回答率从 0.22% 升至 72%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are constrained by outdated information and a tendency to generate incorrect data, commonly referred to as "hallucinations." Retrieval-Augmented Generation (RAG) addresses these limitations by combining the strengths of retrieval-based methods and generative models. This approach involves retrieving relevant information from a large, up-to-date dataset and using it to enhance the generation process, leading to more accurate and contextually appropriate responses. Despite its benefits, RAG introduces a new attack surface for LLMs, particularly because RAG databases are often sourced from public data, such as the web. In this paper, we propose \TrojRAG{} to identify the vulnerabilities and attacks on retrieval parts (RAG database) and their indirect attacks on generative parts (LLMs). Specifically, we identify that poisoning several customized content passages could achieve a retrieval backdoor, where the retrieval works well for clean queries but always returns customized poisoned adversarial queries. Triggers and poisoned passages can be highly customized to implement various attacks. For example, a trigger could be a semantic group like "The Republican Party, Donald Trump, etc." Adversarial passages can be tailored to different contents, not only linked to the triggers but also used to indirectly attack generative LLMs without modifying them. These attacks can include denial-of-service attacks on RAG and semantic steering attacks on LLM generations conditioned by the triggers. Our experiments demonstrate that by just poisoning 10 adversarial passages can induce 98.2\% success rate to retrieve the adversarial passages. Then, these passages can increase the reject ratio of RAG-based GPT-4 from 0.01\% to 74.6\% or increase the rate of negative responses from 0.22\% to 72\% for targeted queries.

</details>

### 20. Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation

📄 [arXiv](https://arxiv.org/abs/2405.20485)　📅 2024-05

**关键词**：`attack`、`single-document backdoor`、`natural trigger`、`production RAG`

👤 **作者**：Harsh Chaudhari、…、Alina Oprea

- 🎯 **研究动机**：RAG 知识库可被外部注入，单文档后门攻击未被研究
- 🔬 **研究方法**：Phantom 两阶段优化毒文档：仅在查询含自然触发 token 序列时被检索，再以对抗文本诱导拒答、名誉损害、隐私与有害行为等目标
- 📌 **结论**：对 Gemma、Vicuna、Llama 有效并迁移到 GPT-3.5 Turbo 与 GPT-4，且在 NVIDIA Chat with RTX 生产系统复现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval Augmented Generation (RAG) expands the capabilities of modern large language models (LLMs), by anchoring, adapting, and personalizing their responses to the most relevant knowledge sources. It is particularly useful in chatbot applications, allowing developers to customize LLM output without expensive retraining. Despite their significant utility in various applications, RAG systems present new security risks. In this work, we propose a novel attack that allows an adversary to inject a single malicious document into a RAG system's knowledge base, and mount a backdoor poisoning attack. We design Phantom, a general two-stage optimization framework against RAG systems, that crafts a malicious poisoned document leading to an integrity violation in the model's output. First, the document is constructed to be retrieved only when a specific naturally occurring trigger sequence of tokens appears in the victim's queries. Second, the document is further optimized with crafted adversarial text that induces various adversarial objectives on the LLM output, including refusal to answer, reputation damage, privacy violations, and harmful behaviors.We demonstrate our attacks on multiple open-source LLM architectures, including Gemma, Vicuna, and Llama, and show that they transfer to closed-source models such as GPT-3.5 Turbo and GPT-4. Finally, we successfully demonstrate our attack on an end-to-end black-box production RAG system: NVIDIA's "Chat with RTX''.

</details>
### Embedding-Space & Vector-Database Poisoning

本节收录直接利用高维 embedding 几何或 vector database 存储层的投毒；攻击者不修改 retriever encoder，而是让少量恶意向量在未知 query 上获得异常高的检索占位。若主要目标是改变 HNSW／IVF 等索引的资源消耗而不操纵证据内容，则应同时考虑系统可用性／DoS 归类。

### 21. Can You Trust the Vectors in Your Vector Database? Black-Hole Attack from Embedding Space Defects

📄 [arXiv](https://arxiv.org/abs/2604.05480)　📅 2026-04

**关键词**：`attack`、`vector-database poisoning`、`embedding-space defect`、`centrality-driven hubness`、`query-agnostic`

👤 **作者**：Hanxi Li、…、Mingjie Tang

- 🎯 **研究动机**：向量数据库安全性几乎未被探索，高维嵌入中心区域空洞构成几何缺陷
- 🔬 **研究方法**：Black-Hole Attack 在存储向量几何中心附近注入少量恶意向量，利用 centrality-driven hubness 使其成为大量查询的近邻，并按攻击者能力设计四条路径
- 📌 **结论**：最高 94.4% 查询被攻击；hubness 缓解要么伤检索精度要么保护有限，检测式防御只对部分路径有效，鲁棒防御仍是开放问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vector databases serve as the retrieval backbone of modern AI applications, yet their security remains largely unexplored. We propose the Black-Hole Attack, a poisoning attack that injects a small number of malicious vectors near the geometric center of the stored vectors. These injected vectors attract queries like a black hole and frequently appear in the top-k retrieval results for most queries. This attack is enabled by a phenomenon we term centrality-driven hubness: in high-dimensional embedding spaces, vectors near the centroid become nearest neighbors of a disproportionately large number of other vectors, while this centroid region is nearly empty in practice. The attack shows that vectors in a vector database cannot be blindly trusted: geometric defects in high-dimensional embeddings make retrieval inherently vulnerable. Based on this insight, we propose four attack paths tailored to different attacker capabilities. Our experiments show that up to 94.4% of queries are successfully attacked. Additionally, we study two directions of defense: hubness mitigation and detection-based filtering. Hubness mitigation either significantly reduces retrieval accuracy or provides only limited protection, while the detection-based defense is effective against some attack paths but fails against others. A robust and adaptive defense thus remains an open problem, and our findings indicate that vector databases require more careful treatment of security.

</details>
### Retriever Encoder Poisoning & Backdoors

本节只收攻击者能够影响 retriever training data、supplied checkpoint 或 encoder parameters 的模型侧攻击。只借助正常 encoder 优化并注入恶意 passage 的工作仍属于上一节；代码检索与 retrieval-augmented diffusion 的条目用于补齐这类供应链后门被 RAG／RACG 继承的技术脉络。

### 22. Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems

📄 [arXiv](https://arxiv.org/abs/2606.18310) · 🌐 [Project](https://anonymous.4open.science/r/CareAttack-3F1C)　📅 2026-06

**关键词**：`attack`、`retriever parameter editing`、`conflict-aware projection`、`anchor repair`

👤 **作者**：Xinru Liu、Xianglong Zhang、Di Cai、Zhumin Chen、Pengfei Hu、Xin Xin

- 🎯 **研究动机**：已有 RAG 注入攻击集中于语料操纵，合成文本可被检测；开源检索器使模型中心攻击面成为现实
- 🔬 **研究方法**：提出 CAREATTACK：冲突感知检索器参数编辑（闭式编辑+图式冲突检测与参数投影）把恶意知识提升到竞争段落之上，再经保攻击锚修复校准非目标提示影响；在 Qwen3-Embedding-0.6B 与 BGE-M3 上实例化
- 📌 **结论**：大幅把恶意段落推入 RAG 检索知识，可对批量目标提示攻击，揭示基于开源检索模型的 RAG 系统的实用攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Injecting malicious knowledge into retrieval-augmented generation (RAG) systems can manipulate retrieved evidence and mislead downstream generation, posing a serious security threat for AI applications. Existing RAG injection attacks mainly rely on manipulating external knowledge bases, such as crafting malicious corpus. However, the synthetic text crafted by such data-centric methods could be detectable, leading to the failure of attacks. Beyond corpus manipulation, open-source retrievers are increasingly exposing RAG systems to model-centric attacks. In this paper, we propose conflict-aware retriever editing, i.e., CAREATTACK, a model-centric retriever attack framework for malicious knowledge injection in RAG. Specifically, CAREATTACK consists two stages of conflict-aware retriever editing and attack-preserving anchor repair. Conflict-aware retriever editing adapts efficient closed-form parameter editing to the dense retrieval model, promoting malicious knowledge above benign competing passages and resolving potential parameter conflicts through graph-based conflict detection and parameter editing projection. Then, attack-preserving anchor repair performs lightweight calibration on the edited retriever to further eliminate the impact on non-target prompts while preserving the attack effectiveness for target prompts. We instantiate CAREATTACK on Qwen3-Embedding-0.6B and BGE-M3, and conduct evaluation on three benchmark datasets. Experimental results demonstrate our method substantially promote malicious passages into the retrieved knowledge of RAG systems and can perform attacks for batches of target prompts and passages, given the access of retrieval model parameters. Since most RAG systems are built upon open-source retrieval models, this work reveals a practical attack surface in RAG systems. Codes are public accessible at https://anonymous.4open.science/r/CareAttack-3F1C.

</details>

### 23. Exploring the Security Threats of Retriever Backdoors in Retrieval-Augmented Code Generation

📄 [arXiv](https://arxiv.org/abs/2512.21681)　📅 2025-12

**关键词**：`attack`、`retriever supply-chain backdoor`、`stealthy code poison`、`vulnerability propagation`

👤 **作者**：Tian Li、Bo Lin、Shangwen Wang、Yusong Tan

- 🎯 **研究动机**：检索增强代码生成中 retriever 组件的供应链后门威胁未被探索，已有攻击过弱或易被潜在空间与 token 级防御检出
- 🔬 **研究方法**：开发 VenomRACG，使毒样本与良性代码统计上不可区分、对现有防御持续低检出，再据此现实分析 retriever 后门
- 📌 **结论**：仅注入相当于知识库 0.05% 的漏洞代码，即可让后门 retriever 在 51.29% 的目标查询把漏洞代码排入 top-5，使 GPT-4o 在超 40% 场景生成漏洞代码且整体性能不受影响

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Code Generation (RACG) is increasingly adopted to enhance Large Language Models for software development, yet its security implications remain dangerously underexplored. This paper conducts the first systematic exploration of a critical and stealthy threat: backdoor attacks targeting the retriever component, which represents a significant supply-chain vulnerability. It is infeasible to assess this threat realistically, as existing attack methods are either too ineffective to pose a real danger or are easily detected by state-of-the-art defense mechanisms spanning both latent-space analysis and token-level inspection, which achieve consistently high detection rates. To overcome this barrier and enable a realistic analysis, we first developed VenomRACG, a new class of potent and stealthy attack that serves as a vehicle for our investigation. Its design makes poisoned samples statistically indistinguishable from benign code, allowing the attack to consistently maintain low detectability across all evaluated defense mechanisms. Armed with this capability, our exploration reveals a severe vulnerability: by injecting vulnerable code equivalent to only 0.05% of the entire knowledge base size, an attacker can successfully manipulate the backdoored retriever to rank the vulnerable code in its top-5 results in 51.29% of cases. This translates to severe downstream harm, causing models like GPT-4o to generate vulnerable code in over 40% of targeted scenarios, while leaving the system's general performance intact. Our findings establish that retriever backdooring is not a theoretical concern but a practical threat to the software development ecosystem that current defenses are blind to, highlighting the urgent need for robust security measures.

</details>

### 24. Your RAG is Unfair: Exposing Fairness Vulnerabilities in Retrieval-Augmented Generation via Backdoor Attacks

📄 [arXiv](https://arxiv.org/abs/2509.22486) · 🎓 [Official](https://aclanthology.org/2025.emnlp-main.804/)　📅 2025-09　🏷 EMNLP 2025

**关键词**：`attack`、`query-encoder poisoning`、`semantic fairness trigger`、`persistent bias`

👤 **作者**：Gaurav Bagwe、Saket S. Chaturvedi、Xiaolong Ma、Xiaoyong Yuan、Kuang-Ching Wang、Lan Zhang

- 🎯 **研究动机**：RAG 后门研究聚焦虚假信息，公平性脆弱性未被探索
- 🔬 **研究方法**：提出 BiasRAG 两阶段攻击：预训练阶段投毒查询编码器把目标群体与社会偏见对齐，部署后向知识库注入对抗文档强化后门
- 📌 **结论**：高攻击成功率同时保持上下文相关性与效用，标准公平性评估下不可检测，构成持久隐蔽威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) enhances factual grounding by integrating retrieval mechanisms with generative models but introduces new attack surfaces, particularly through backdoor attacks. While prior research has largely focused on disinformation threats, fairness vulnerabilities remain underexplored. Unlike conventional backdoors that rely on direct trigger-to-target mappings, fairness-driven attacks exploit the interaction between retrieval and generation models, manipulating semantic relationships between target groups and social biases to establish a persistent and covert influence on content generation. This paper introduces BiasRAG, a systematic framework that exposes fairness vulnerabilities in RAG through a two-phase backdoor attack. During the pre-training phase, the query encoder is compromised to align the target group with the intended social bias, ensuring long-term persistence. In the post-deployment phase, adversarial documents are injected into knowledge bases to reinforce the backdoor, subtly influencing retrieved content while remaining undetectable under standard fairness evaluations. Together, BiasRAG ensures precise target alignment over sensitive attributes, stealthy execution, and resilience. Empirical evaluations demonstrate that BiasRAG achieves high attack success rates while preserving contextual relevance and utility, establishing a persistent and evolving threat to fairness in RAG.

</details>

### 25. DisarmRAG: Stealthy Retriever-Centric Poisoning to Disable Self-Correction in Retrieval-Augmented Generation (Extended Version)

📄 [arXiv](https://arxiv.org/abs/2508.20083) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-08　🏷 ACM CCS 2026

**关键词**：`attack`、`retriever model editing`、`anti-self-correction`、`contrastive learning`

👤 **作者**：Yanbo Dai、Zhenlan Ji、Zongjie Li、Kuan Li、Shuai Wang

- 🎯 **研究动机**：现实部署中 LLM 的自我纠错能力（SCA）显著削弱既有 RAG 投毒攻击，理想研究与实际场景存在差距
- 🔬 **研究方法**：提出 DisarmRAG 转而攻击检索器：向上下文注入反 SCA 指令压制自纠错，含迭代协同优化与基于对比学习的隐蔽模型编辑
- 📌 **结论**：六个 LLM、三个 QA 基准上成功率超 90%，多种检测防御下仍隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has become a standard approach for improving the reliability of large language models (LLMs). Prior work demonstrates the vulnerability of RAG systems by misleading them into generating attacker-chosen outputs through poisoning the knowledge base. However, we observe that the effectiveness of these attacks is substantially undermined in the real-world deployment, where LLMs exhibit a strong self-correction ability (SCA). This ability is typically triggered by the mainstream configuration of LLMs, indicating a substantial gap between idealized research settings and practical scenarios. To address this issue, we systematically reflect on the limitations of prior RAG attacks and introduce DisarmRAG, a novel poisoning paradigm that focuses on the retriever, instead of the conventional approach of only poisoning the knowledge base. By compromising the retriever, our method can inject arbitrary anti-SCA instructions into the context provided to LLMs, effectively suppressing the SCA and enforcing attacker-chosen outputs. In particular, we craft a novel and systematic attack framework consisting of 1) an iterative co-optimization process to ensure the effectiveness of the anti-SCA instructions and 2) a stealthy model editing technique based on contrastive learning to facilitate the delivery of the attack payload. We extensively evaluate DisarmRAG across six LLMs and three QA benchmarks, and the results, with success rates exceeding 90%, confirm its efficacy. We additionally validate the effectiveness of our attack under various detection defenses, highlighting stealthiness, which is another critical aspect to consider in real-world attacks.

</details>

### 26. Retrievals Can Be Detrimental: Unveiling the Backdoor Vulnerability of Retrieval-Augmented Diffusion Models

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

### 27. Backdoored Retrievers for Prompt Injection Attacks on Retrieval Augmented Generation of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2410.14479)　📅 2024-10

**关键词**：`attack`、`dense-retriever fine-tuning`、`poisoned training pairs`、`prompt injection`

👤 **作者**：Cody Clop、Yannick Teglia

- 🎯 **研究动机**：RAG prompt injection 研究多止步于虚假信息，有害链接、未授权推广与 DoS 等目标未覆盖
- 🔬 **研究方法**：对比少量语料注入与污染 dense retriever 微调数据的供应链后门两条攻击路线
- 📌 **结论**：语料注入少量文档即获显著 ASR；后门攻击成功率更高但需受害者用攻击者数据微调检索器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated remarkable capabilities in generating coherent text but remain limited by the static nature of their training data. Retrieval Augmented Generation (RAG) addresses this issue by combining LLMs with up-to-date information retrieval, but also expand the attack surface of the system. This paper investigates prompt injection attacks on RAG, focusing on malicious objectives beyond misinformation, such as inserting harmful links, promoting unauthorized services, and initiating denial-of-service behaviors. We build upon existing corpus poisoning techniques and propose a novel backdoor attack aimed at the fine-tuning process of the dense retriever component. Our experiments reveal that corpus poisoning can achieve significant attack success rates through the injection of a small number of compromised documents into the retriever corpus. In contrast, backdoor attacks demonstrate even higher success rates but necessitate a more complex setup, as the victim must fine-tune the retriever using the attacker poisoned dataset.

</details>

### 28. TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2405.13401)　📅 2024-05

**关键词**：`attack`、`retriever backdoor`、`orthogonal contrastive learning`、`multi-trigger control`

👤 **作者**：Pengzhou Cheng、…、Gongshen Liu

- 🎯 **研究动机**：直接攻击 LLM 成本高、易被安全审查、后门随模型迭代退化
- 🔬 **研究方法**：TrojanRAG 联合攻击 RAG：正交对比学习优化多对后门捷径约束触发条件到参数子空间，并用知识图谱构造结构化数据提升目标上下文召回
- 📌 **结论**：在真实性、语言理解与有害性上展现多样威胁，同时保持正常查询的检索能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have raised concerns about potential security threats despite performing significantly in Natural Language Processing (NLP). Backdoor attacks initially verified that LLM is doing substantial harm at all stages, but the cost and robustness have been criticized. Attacking LLMs is inherently risky in security review, while prohibitively expensive. Besides, the continuous iteration of LLMs will degrade the robustness of backdoors. In this paper, we propose TrojanRAG, which employs a joint backdoor attack in the Retrieval-Augmented Generation, thereby manipulating LLMs in universal attack scenarios. Specifically, the adversary constructs elaborate target contexts and trigger sets. Multiple pairs of backdoor shortcuts are orthogonally optimized by contrastive learning, thus constraining the triggering conditions to a parameter subspace to improve the matching. To improve the recall of the RAG for the target contexts, we introduce a knowledge graph to construct structured data to achieve hard matching at a fine-grained level. Moreover, we normalize the backdoor scenarios in LLMs to analyze the real harm caused by backdoors from both attackers' and users' perspectives and further verify whether the context is a favorable tool for jailbreaking models. Extensive experimental results on truthfulness, language understanding, and harmfulness show that TrojanRAG exhibits versatility threats while maintaining retrieval capabilities on normal queries.

</details>

### 29. Backdoor Attacks on Dense Retrieval via Public and Unintentional Triggers

📄 [arXiv](https://arxiv.org/abs/2402.13532) · 📝 [OpenReview](https://openreview.net/forum?id=RsnxggqW4l)　📅 2024-02　🏷 COLM 2025

**关键词**：`attack`、`dense-retriever poisoning`、`grammar-error trigger`、`accidental activation`

👤 **作者**：Quanyu Long、Yue Deng、LeiLei Gan、Wenya Wang、Sinno Jialin Pan

- 🎯 **研究动机**：稠密检索攻击面研究不足，已有方法依赖模型权重且触发不自然
- 🔬 **研究方法**：以语法错误作隐蔽触发器训练检索器；发现对比损失对语法错误敏感、hard negative sampling 反而加剧脆弱性
- 📌 **结论**：语料投毒率仅 0.048% 即获高 ASR 且正常检索无损，三种真实防御均难过滤恶意段落

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dense retrieval systems have been widely used in various NLP applications. However, their vulnerabilities to potential attacks have been underexplored. This paper investigates a novel attack scenario where the attackers aim to mislead the retrieval system into retrieving the attacker-specified contents. Those contents, injected into the retrieval corpus by attackers, can include harmful text like hate speech or spam. Unlike prior methods that rely on model weights and generate conspicuous, unnatural outputs, we propose a covert backdoor attack triggered by grammar errors. Our approach ensures that the attacked models can function normally for standard queries while covertly triggering the retrieval of the attacker's contents in response to minor linguistic mistakes. Specifically, dense retrievers are trained with contrastive loss and hard negative sampling. Surprisingly, our findings demonstrate that contrastive loss is notably sensitive to grammatical errors, and hard negative sampling can exacerbate susceptibility to backdoor attacks. Our proposed method achieves a high attack success rate with a minimal corpus poisoning rate of only 0.048\%, while preserving normal retrieval performance. This indicates that the method has negligible impact on user experience for error-free queries. Furthermore, evaluations across three real-world defense strategies reveal that the malicious passages embedded within the corpus remain highly resistant to detection and filtering, underscoring the robustness and subtlety of the proposed attack \footnote{Codes of this work are available at https://github.com/ruyue0001/Backdoor_DPR.}.

</details>

### 30. Backdooring Neural Code Search

📄 [arXiv](https://arxiv.org/abs/2305.17506) · 🎓 [Official](https://aclanthology.org/2023.acl-long.540/)　📅 2023-05　🏷 ACL 2023

**关键词**：`attack`、`neural code-search backdoor`、`identifier trigger`、`vulnerable-code promotion`

👤 **作者**：Weisong Sun、…、Bin Luo

- 🎯 **研究动机**：神经代码搜索模型可被后门返回缺陷或漏洞代码，安全面几乎无人研究
- 🔬 **研究方法**：BADCODE 以特殊流程生成并注入标识符触发器，仅修改一个变量/函数名即可完成攻击
- 📌 **结论**：使缺陷代码排名进入前 11%，效果比基线高 60%，隐蔽性按 F1 高两倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reusing off-the-shelf code snippets from online repositories is a common practice, which significantly enhances the productivity of software developers. To find desired code snippets, developers resort to code search engines through natural language queries. Neural code search models are hence behind many such engines. These models are based on deep learning and gain substantial attention due to their impressive performance. However, the security aspect of these models is rarely studied. Particularly, an adversary can inject a backdoor in neural code search models, which return buggy or even vulnerable code with security/privacy issues. This may impact the downstream software (e.g., stock trading systems and autonomous driving) and cause financial loss and/or life-threatening incidents. In this paper, we demonstrate such attacks are feasible and can be quite stealthy. By simply modifying one variable/function name, the attacker can make buggy/vulnerable code rank in the top 11%. Our attack BADCODE features a special trigger generation and injection procedure, making the attack more effective and stealthy. The evaluation is conducted on two neural code search models and the results show our attack outperforms baselines by 60%. Our user study demonstrates that our attack is more stealthy than the baseline by two times based on the F1 score.

</details>

### 31. BadCS: A Backdoor Attack Framework for Code search

📄 [arXiv](https://arxiv.org/abs/2305.05503)　📅 2023-05

**关键词**：`attack`、`code-search training poison`、`knowledge distillation`、`clean-utility preservation`

👤 **作者**：Shiyi Qi、Yuanhang Yang、Shuzhzeng Gao、Cuiyun Gao、Zenglin Xu

- 🎯 **研究动机**：代码搜索模型可被诱导推荐漏洞代码，但既有投毒攻击对 Transformer 预训练模型常失效且伤性能
- 🔬 **研究方法**：BadCS 组合毒样本生成与 re-weighted knowledge distillation，蒸馏保效用、毒样本加权强化攻击
- 📌 **结论**：较 SOTA 投毒方法在 Python/Java 数据集分别提升 83.03%-99.98% 与 75.98%-99.90%，模型性能反超良性基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the development of deep learning (DL), DL-based code search models have achieved state-of-the-art performance and have been widely used by developers during software development. However, the security issue, e.g., recommending vulnerable code, has not received sufficient attention, which will bring potential harm to software development. Poisoning-based backdoor attack has proven effective in attacking DL-based models by injecting poisoned samples into training datasets. However, previous work shows that the attack technique does not perform successfully on all DL-based code search models and tends to fail for Transformer-based models, especially pretrained models. Besides, the infected models generally perform worse than benign models, which makes the attack not stealthy enough and thereby hinders the adoption by developers. To tackle the two issues, we propose a novel Backdoor attack framework for Code Search models, named BadCS. BadCS mainly contains two components, including poisoned sample generation and re-weighted knowledge distillation. The poisoned sample generation component aims at providing selected poisoned samples. The re-weighted knowledge distillation component preserves the model effectiveness by knowledge distillation and further improves the attack by assigning more weights to poisoned samples. Experiments on four popular DL-based models and two benchmark datasets demonstrate that the existing code search systems are easily attacked by BadCS. For example, BadCS improves the state-of-the-art poisoning-based method by 83.03%-99.98% and 75.98%-99.90% on Python and Java datasets, respectively. Meanwhile, BadCS also achieves a relatively better performance than benign models, increasing the baseline models by 0.49% and 0.46% on average, respectively.

</details>
### Corpus & Knowledge Poisoning

### 32. PURPOSE: Poisoning Conflict Resolution in RAG via Proxy-Fact-Grounded Updates

📄 [arXiv](https://arxiv.org/abs/2608.04756)　📅 2026-08

**关键词**：`attack`、`RAG poisoning`、`conflict resolution`、`factual update`

👤 **作者**：Zijian Wang、…、Sheng Zhong

- 🎯 **研究动机**：RAG 检索后冲突解决机制对知识投毒的鲁棒性未被研究，已有黑盒投毒均以正面反驳方式断言目标答案
- 🔬 **研究方法**：PURPOSE 把注入重构为最小化冲突的更新：抽取近似解决器参考的查询相关事实，在其中锚定枢纽事件，使注入与可验证内容一致并引导生成器偏向目标答案
- 📌 **结论**：三 QA 基准、五生成器、三冲突解决法中 35/45 设定 ASR 最高，比最强先前攻击平均高 9.7 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In Retrieval-Augmented Generation (RAG), post-retrieval conflict resolution arbitrates among noisy or contradictory retrieved passages. However, the robustness of this safeguard against knowledge poisoning has not been adequately studied. Existing black-box poisoning methods all assert the target answer in frontal contradiction with what the resolver treats as settled, the very signal these methods are built to detect. We propose PURPOSE, a strict black-box poisoning attack that reframes the injection as an update that minimizes conflict, rather than as a counter-claim. PURPOSE extracts query-related facts approximating the resolver's possible reference, then grounds a pivot event in them to keep the injection consistent with what the resolver might verify while steering the generator toward the target answer. Across three QA benchmarks, five generators, and three conflict-resolution methods, PURPOSE attains the highest attack success rate (ASR) in 35 of 45 settings and exceeds the strongest prior attack with +9.7 mean ASR points. These results show that our poisoning method is effective against conflict resolution in RAG and identify non-contradicting injection as a practical mode to enhance poisoning attack.

</details>

### 33. DenialRAG: Single-Document RAG Poisoning via Embedded Parametric Denial

📄 [arXiv](https://arxiv.org/abs/2608.02678)　📅 2026-08

**关键词**：`attack`、`single-document poisoning`、`parametric denial`、`model dependence`

👤 **作者**：Abay Zhurekbay、Tao Liu、Fan Li

- 🎯 **研究动机**：已有单文档 RAG 投毒刻意避免在文内点名并否认正确答案，该互补设计空间未被检验
- 🔬 **研究方法**：DenialRAG 在投毒段落中显式命名正确答案、否认它并给出偏向错误答案的解释，把冲突直接嵌入生成器检索到的上下文
- 📌 **结论**：在三个 Mistral-7B 数据集上 ASR 最高；攻击效果强依赖目标模型，五种推理时防御均有 ASR 残留，单一攻击族无法刻画 RAG 投毒风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems are vulnerable to corpus poisoning: an attacker who inserts a crafted document into the retrieval corpus can steer the underlying large language model (LLM) toward an attacker-chosen wrong answer. Prior single-document attacks typically avoid explicitly naming and refuting the correct answer inside the poisoned passage. In this paper, we examine a complementary design and propose \emph{DenialRAG}, a single-document poisoning attack that explicitly names the correct answer, denies it, and presents an attacker-controlled explanation for favoring the wrong answer. By placing both the correct answer and the corresponding poisoned answer inside the same retrieved passage, DenialRAG embeds the conflict directly into the context seen by the generator. We evaluate DenialRAG against four published single-document poisoning attacks across three open-domain question-answering datasets, eight target LLMs from four vendors, and five inference-time defenses. The results show that attack effectiveness is strongly model-dependent: DenialRAG achieves the highest attack success rate (ASR) on all three Mistral-7B datasets and remains effective on several other target LLMs, while other attacks dominate in some model regimes. Defense results show meaningful ASR reductions but non-uniform protection, with each defense leaving residual ASR in some settings. Component-level and cross-model analyses further identify the embedded denial as the most influential tested component and show that different poisoning mechanisms lose effectiveness at different rates across model groups. Together, these results show that RAG poisoning risk cannot be fully characterized by a single attack family or a single target model.

</details>

### 34. DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2606.01212)　📅 2026-06

**关键词**：`attack`、`RAG poisoning`、`opinion manipulation`、`discourse structure`

👤 **作者**：Yuyang Gong、…、Xiaozhong Liu

- 🎯 **研究动机**：已有 RAG 攻击聚焦单查询或窄话题集，实际覆盖与伪装有限
- 🔬 **研究方法**：提出话语级意见操纵新威胁：在语义查询网络上协同影响多话题空间；DiscourseFlip 图引导 agent 攻击在有限投毒预算下动态分配以最大化话语级观点偏差
- 📌 **结论**：在上下文化查询网络上一致诱发定向观点转移，覆盖与效果超基线；用户研究确认伪装良好，现有缓解策略对其无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are widely deployed and increasingly influential, but their reliance on external corpora exposes new security risks from poisoned retrieval content. Existing RAG attacks are largely focusing on individual queries or narrow topic-local query sets, which limits their practical reach and offers limited camouflage in real-world settings. In this paper, we introduce discourse-level opinion manipulation, a new threat model in which coordinated influence across a semantic query network induces opinion shifts over a holistic, multi-topic query space. We formalize this threat in a black-box setting and propose DiscourseFlip, an agentic, graph-guided attack that dynamically allocates a limited poisoning budget to maximize discourse-level opinion deviation. Extensive experiments demonstrate that DiscourseFlip consistently induces targeted opinion shifts across the contextualized query network and significantly outperforms existing baselines in terms of coverage and effectiveness. User studies further confirm that DiscourseFlip is effective while remaining well camouflaged from user detection. Moreover, systematic analyses show that existing mitigation strategies are ineffective against discourse-level manipulation, underscoring the urgent need for more robust and adaptive defenses to address discourse-level vulnerabilities.

</details>

### 35. Confundo: Learning to Generate Robust Poison for Practical RAG Systems

📄 [arXiv](https://arxiv.org/abs/2602.06616) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/hu-haoyang)　📅 2026-02　🏷 USENIX Security 2026

**关键词**：`attack`、`RAG poisoning`、`robust poison`、`hallucination induction`、`preprocessing robustness`、`query variation`

👤 **作者**：Haoyang Hu、Zhejun Jiang、Yueming Lyu、Junyuan Zhang、Yi Liu、Ka-Ho Chow

- 🎯 **研究动机**：现有 RAG 投毒在真实系统中因预处理碎片化与查询偏移而严重失效，导致风险被低估
- 🔬 **研究方法**：Confundo 微调 LLM 作为投毒生成器，统一支持操纵事实正确性、诱导偏见、触发幻觉等多种攻击目标
- 📌 **结论**：跨数据集与 RAG 配置大幅超越专用攻击，防御存在时仍有效；另给出防网页被爬入 RAG 的防御用例

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is increasingly deployed in real-world applications, where its reference-grounded design makes outputs appear trustworthy. This trust has spurred research on poisoning attacks that craft malicious content, inject it into knowledge sources, and manipulate RAG responses. However, when evaluated in practical RAG systems, existing attacks suffer from severely degraded effectiveness. This gap stems from two overlooked realities: (i) content is often processed before use, which can fragment the poison and weaken its effect, and (ii) users often do not issue the exact queries anticipated during attack design. These factors can lead practitioners to underestimate risks and develop a false sense of security. To better characterize the threat to practical systems, we present Confundo, a learning-to-poison framework that fine-tunes a large language model as a poison generator to achieve high effectiveness, robustness, and stealthiness. Confundo provides a unified framework supporting multiple attack objectives, demonstrated by manipulating factual correctness, inducing biased opinions, and triggering hallucinations. By addressing these overlooked challenges, Confundo consistently outperforms a wide range of purpose-built attacks across datasets and RAG configurations by large margins, even in the presence of defenses. Beyond exposing vulnerabilities, we also present a defensive use case that protects web content from unauthorized incorporation into RAG systems via scraping, with no impact on user experience.

</details>

### 36. Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors

📄 [arXiv](https://arxiv.org/abs/2510.00586) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61331)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`RAG poisoning`、`data poisoning`、`knowledge corruption`、`backdoor attack`、`representation steering`

👤 **作者**：Yen-Shan Chen、Sian-Yao Huang、Cheng-Lin Yang、Yun-Nung Chen

- 🎯 **研究动机**：RAG 数据投毒需为每个目标短语昂贵优化毒文档，扩展性差
- 🔬 **研究方法**：Eyes-on-Me 把对抗文档分解为可复用的 Attention Attractors 与 Focus Regions：attractor 引导注意力到 focus region 后近零成本插入语义诱饵或恶意指令；引导与攻击成功率强相关的小部分注意力头
- 📌 **结论**：18 个端到端 RAG 设定上平均 ASR 从 21.9 升至 57.8（较先前 2.6 倍）；单一 attractor 无需重训练即迁移到未见黑盒检索器与生成器

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing data poisoning attacks on retrieval-augmented generation (RAG) systems scale poorly because they require costly optimization of poisoned documents for each target phrase. We introduce Eyes-on-Me, a modular attack that decomposes an adversarial document into reusable **Attention Attractors** and **Focus Regions**. Attractors are optimized to direct attention to the Focus Region. Attackers can then insert semantic baits for the retriever or malicious instructions for the generator, adapting to new targets at near zero cost. This is achieved by steering a small subset of attention heads that we empirically identify as strongly correlated with attack success. Across 18 end-to-end RAG settings (3 datasets $\times$ 2 retrievers $\times$ 3 generators), Eyes-on-Me raises average attack success rates from 21.9 to 57.8 (+35.9 points, 2.6$\times$ over prior work). A single optimized attractor transfers to unseen black box retrievers and generators without retraining. Our findings establish a scalable paradigm for RAG data poisoning and show that modular, reusable components pose a practical threat to modern AI systems. They also reveal a strong link between attention concentration and model outputs, informing interpretability research.

</details>

### 37. MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2512.08289) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2025-12　🏷 ACM CCS 2026

**关键词**：`attack`、`RAG poisoning`、`black-box attack`、`query-agnostic`、`query-agnostic attack`

👤 **作者**：Tailun Chen、…、Kui Ren

- 🎯 **研究动机**：已有 RAG 语料投毒依赖白盒访问或已知用户查询等不现实假设，低估现实利用难度
- 🔬 **研究方法**：MIRAGE 面向严格黑盒与查询无关设定：persona 驱动查询合成逼近潜在用户搜索分布、语义锚定提升检索可见性、对抗版 Test-Time Preference Optimization 最大化说服力
- 📌 **结论**：在三个长文档领域数据集的新基准上攻击效力与隐蔽性显著超越基线，并在多种 retriever-LLM 配置间可迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems enhance LLMs with external knowledge but introduce a critical attack surface: corpus poisoning. While recent studies have demonstrated the potential of such attacks, they typically rely on impractical assumptions, such as white-box access or known user queries, thereby underestimating the difficulty of real-world exploitation. In this paper, we bridge this gap by proposing MIRAGE, a novel multi-stage poisoning pipeline designed for strict black-box and query-agnostic environments. Operating on surrogate model feedback, MIRAGE functions as an automated optimization framework that integrates three key mechanisms: it utilizes persona-driven query synthesis to approximate latent user search distributions, employs semantic anchoring to imperceptibly embed these intents for high retrieval visibility, and leverages an adversarial variant of Test-Time Preference Optimization (TPO) to maximize persuasion. To rigorously evaluate this threat, we construct a new benchmark derived from three long-form, domain-specific datasets. Extensive experiments demonstrate that MIRAGE significantly outperforms existing baselines in both attack efficacy and stealthiness, exhibiting remarkable transferability across diverse retriever-LLM configurations and highlighting the urgent need for robust defense strategies.

</details>

### 38. NeuroGenPoisoning: Neuron-Guided Attacks on Retrieval-Augmented Generation of LLM via Genetic Optimization of External Knowledge

📄 [arXiv](https://arxiv.org/abs/2510.21144)　📅 2025-10

**关键词**：`attack`、`neuron-guided poisoning`、`genetic optimization`、`knowledge conflict`

👤 **作者**：Hanyu Zhu、Lance Fiondella、Jiawei Yuan、Kai Zeng、Long Jiao

- 🎯 **研究动机**：现有 RAG 投毒只迭代操纵检索内容或 prompt 结构，忽略模型内部神经元敏感性，且未考虑与强参数知识的冲突
- 🔬 **研究方法**：NeuroGenPoisoning 定位与投毒知识强相关的 Poison-Responsive Neurons，用遗传算法进化最大化激活这些神经元的对抗段落，并复用有潜力但未成功的外部知识变体
- 📌 **结论**：跨模型与数据集 Population Overwrite Success Rate 超 90% 且保持流畅，能有效化解知识冲突

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) empowers Large Language Models (LLMs) to dynamically integrate external knowledge during inference, improving their factual accuracy and adaptability. However, adversaries can inject poisoned external knowledge to override the model's internal memory. While existing attacks iteratively manipulate retrieval content or prompt structure of RAG, they largely ignore the model's internal representation dynamics and neuron-level sensitivities. The underlying mechanism of RAG poisoning has not been fully studied and the effect of knowledge conflict with strong parametric knowledge in RAG is not considered. In this work, we propose NeuroGenPoisoning, a novel attack framework that generates adversarial external knowledge in RAG guided by LLM internal neuron attribution and genetic optimization. Our method first identifies a set of Poison-Responsive Neurons whose activation strongly correlates with contextual poisoning knowledge. We then employ a genetic algorithm to evolve adversarial passages that maximally activate these neurons. Crucially, our framework enables massive-scale generation of effective poisoned RAG knowledge by identifying and reusing promising but initially unsuccessful external knowledge variants via observed attribution signals. At the same time, Poison-Responsive Neurons guided poisoning can effectively resolves knowledge conflict. Experimental results across models and datasets demonstrate consistently achieving high Population Overwrite Success Rate (POSR) of over 90% while preserving fluency. Empirical evidence shows that our method effectively resolves knowledge conflict.

</details>

### 39. RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2510.10008) · 🎓 [Official](https://aclanthology.org/2026.findings-acl.833/)　📅 2025-10　🏷 ACL 2026

**关键词**：`attack`、`RAG poisoning`、`reinforcement learning`、`black-box RAG`

👤 **作者**：Meng Xi、…、Jianwei Yin

- 🎯 **研究动机**：白盒 RAG 投毒需要系统内部实现细节，已有黑盒方法又无法利用交互反馈
- 🔬 **研究方法**：RIPRAG 把目标 RAG 系统视为黑盒，用 Reinforcement Learning from Black-box Feedback 优化毒文档生成模型，设计相似度与攻击两类奖励
- 📌 **结论**：对多数复杂 RAG 系统有效实施投毒，ASR 较基线最高提升 0.72

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems based on Large Language Models (LLMs) have become a core technology for tasks such as question-answering (QA) and content generation. RAG poisoning is an attack method to induce LLMs to generate the attacker's expected text by injecting poisoned documents into the database of RAG systems. Existing research can be broadly divided into two classes: white-box methods and black-box methods. White-box methods utilize gradient information to optimize poisoned documents, and black-box methods use a pre-trained LLM to generate them. However, existing white-box methods require knowledge of the RAG system's internal composition and implementation details, whereas black-box methods are unable to utilize interactive information. In this work, we propose the RIPRAG attack framework, an end-to-end attack pipeline that treats the target RAG system as a black box and leverages our proposed Reinforcement Learning from Black-box Feedback (RLBF) method to optimize the generation model for poisoned documents. We designed two kinds of rewards: similarity reward and attack reward. Experimental results demonstrate that this method can effectively execute poisoning attacks against most complex RAG systems, achieving an attack success rate (ASR) improvement of up to 0.72 compared to baseline methods. This highlights prevalent deficiencies in current defensive methods and provides critical insights for LLM security research.

</details>

### 40. CPA-RAG: Covert Poisoning Attacks on Retrieval-Augmented Generation in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.19864)　📅 2025-05

**关键词**：`attack`、`black-box poisoning`、`cross-guided optimization`、`commercial RAG`

👤 **作者**：Chunyang Li、Junwei Zhang、Anda Cheng、Zhuo Ma、Xinghua Li、Jianfeng Ma

- 🎯 **研究动机**：既有 RAG 黑盒投毒泛化差、对抗文本不流畅
- 🔬 **研究方法**：提出 CPA-RAG，整合 prompt 文本生成、多 LLM 交叉引导优化与检索器打分构造高质量对抗样本
- 📌 **结论**：top-5 检索下 ASR 超 90% 追平白盒，防御下仍领先黑盒基线 14.5 个百分点，并攻破阿里百炼商用 RAG

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, but its openness introduces vulnerabilities that can be exploited by poisoning attacks. Existing poisoning methods for RAG systems have limitations, such as poor generalization and lack of fluency in adversarial texts. In this paper, we propose CPA-RAG, a black-box adversarial framework that generates query-relevant texts capable of manipulating the retrieval process to induce target answers. The proposed method integrates prompt-based text generation, cross-guided optimization through multiple LLMs, and retriever-based scoring to construct high-quality adversarial samples. We conduct extensive experiments across multiple datasets and LLMs to evaluate its effectiveness. Results show that the framework achieves over 90\% attack success when the top-k retrieval setting is 5, matching white-box performance, and maintains a consistent advantage of approximately 5 percentage points across different top-k values. It also outperforms existing black-box baselines by 14.5 percentage points under various defense strategies. Furthermore, our method successfully compromises a commercial RAG system deployed on Alibaba's BaiLian platform, demonstrating its practical threat in real-world applications. These findings underscore the need for more robust and secure RAG frameworks to defend against poisoning attacks.

</details>

### 41. One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2505.11548) · 🌐 [Project](https://anonymous.4open.science/r/AuthChain-45E8) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.1023/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`attack`、`RAG poisoning`、`single-document attack`、`multi-hop QA`

👤 **作者**：Zhiyuan Chang、…、Qing Wang

- 🎯 **研究动机**：既有 RAG 知识投毒需注入多篇文档或只能攻击简单查询，隐蔽性与实用性受限
- 🔬 **研究方法**：提出 AuthChain，仅投毒单篇文档即对多跳复杂问题奏效，确保毒文档被可靠检索并被 LLM 信任
- 📌 **结论**：六个主流 LLM 上 ASR 显著更高，且对 RAG 防御机制保持隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) enhanced with Retrieval-Augmented Generation (RAG) have shown improved performance in generating accurate responses. However, the dependence on external knowledge bases introduces potential security vulnerabilities, particularly when these knowledge bases are publicly accessible and modifiable. While previous studies have exposed knowledge poisoning risks in RAG systems, existing attack methods suffer from critical limitations: they either require injecting multiple poisoned documents (resulting in poor stealthiness) or can only function effectively on simplistic queries (limiting real-world applicability). This paper reveals a more realistic knowledge poisoning attack against RAG systems that achieves successful attacks by poisoning only a single document while remaining effective for complex multi-hop questions involving complex relationships between multiple elements. Our proposed AuthChain address three challenges to ensure the poisoned documents are reliably retrieved and trusted by the LLM, even against large knowledge bases and LLM's own knowledge. Extensive experiments across six popular LLMs demonstrate that AuthChain achieves significantly higher attack success rates while maintaining superior stealthiness against RAG defense mechanisms compared to state-of-the-art baselines.

</details>

### 42. POISONCRAFT: Practical Poisoning of Retrieval-Augmented Generation for Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.06579)　📅 2025-05

**关键词**：`attack`、`query-agnostic poisoning`、`fraudulent citation`、`black-box transfer`

👤 **作者**：Yangguang Shao、…、Junzheng Shi

- 🎯 **研究动机**：既有 RAG 投毒需获知用户查询或修改查询，现实性不足
- 🔬 **研究方法**：提出 POISONCRAFT，与查询无关地构造可被检索且被 LLM 引用的毒文本，诱导模型引用欺诈网站
- 📌 **结论**：跨数据集、检索器与 LLM 有效，可黑盒迁移至商业检索器，多种防御下仍稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have achieved remarkable success in various domains, primarily due to their strong capabilities in reasoning and generating human-like text. Despite their impressive performance, LLMs are susceptible to hallucinations, which can lead to incorrect or misleading outputs. This is primarily due to the lack of up-to-date knowledge or domain-specific information. Retrieval-augmented generation (RAG) is a promising approach to mitigate hallucinations by leveraging external knowledge sources. However, the security of RAG systems has not been thoroughly studied. In this paper, we study a poisoning attack on RAG systems named POISONCRAFT, which can mislead the model to refer to fraudulent websites. Compared to existing poisoning attacks on RAG systems, our attack is more practical as it does not require access to the target user query's info or edit the user query. It not only ensures that injected texts can be retrieved by the model, but also ensures that the LLM will be misled to refer to the injected texts in its response. We demonstrate the effectiveness of POISONCRAFTacross different datasets, retrievers, and language models in RAG pipelines, and show that it remains effective when transferred across retrievers, including black-box systems. Moreover, we present a case study revealing how the attack influences both the retrieval behavior and the step-by-step reasoning trace within the generation model, and further evaluate the robustness of POISONCRAFTunder multiple defense mechanisms. These results validate the practicality of our threat model and highlight a critical security risk for RAG systems deployed in real-world applications. We release our code\footnote{https://github.com/AndyShaw01/PoisonCraft} to support future research on the security and robustness of RAG systems in real-world settings.

</details>

### 43. Practical Poisoning Attacks against Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2504.03957) · 🌐 [Project](https://doi.org/10.1145/3750555.3811900)　📅 2025-04

**关键词**：`attack`、`single-document poisoning`、`credibility framing`、`stealth`

👤 **作者**：Baolei Zhang、…、Minghong Fang

- 🎯 **研究动机**：既有 RAG 投毒假设可注入大量毒文本以压倒正确答案，现实中难成立
- 🔬 **研究方法**：提出 CorruptRAG，仅注入单篇毒文本的投毒攻击，兼顾可行性与隐蔽性
- 📌 **结论**：多个大规模数据集上 ASR 高于既有基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated impressive natural language processing abilities but face challenges such as hallucination and outdated knowledge. Retrieval-Augmented Generation (RAG) has emerged as a state-of-the-art approach to mitigate these issues. While RAG enhances LLM outputs, it remains vulnerable to poisoning attacks. Recent studies show that injecting poisoned text into the knowledge database can compromise RAG systems, but most existing attacks assume that the attacker can insert a sufficient number of poisoned texts per query to outnumber correct-answer texts in retrieval, an assumption that is often unrealistic. To address this limitation, we propose CorruptRAG, a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth. Extensive experiments conducted on multiple large-scale datasets demonstrate that CorruptRAG achieves higher attack success rates than existing baselines.

</details>

### 44. CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2503.06950)　📅 2025-03

**关键词**：`attack`、`black-box poisoning`、`reference-feedback optimization`、`knowledge expansion`

👤 **作者**：Runqi Sui

- 🎯 **研究动机**：文档投毒攻击多依赖白盒/灰盒假设，RAG 展示 reference context 提供的黑盒反馈未被利用
- 🔬 **研究方法**：CtrlRAG 两阶段：构造含误导或情绪化内容的文档入库，再以定位算法加 MLM 依引用反馈迭代优化检索优先级与自然度
- 📌 **结论**：百万级 MS MARCO 每题 5 篇即使 GPT-4o 达 90% ASR（超最优基线 30%）；Knowledge Expansion 防御阻断 78% 攻击且保持 95.5% 准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems enhance response credibility and traceability by displaying reference contexts, but this transparency simultaneously introduces a novel black-box attack vector. Existing document poisoning attacks, where adversaries inject malicious documents into the knowledge base to manipulate RAG outputs, rely primarily on unrealistic white-box or gray-box assumptions, limiting their practical applicability. To address this gap, we propose CtrlRAG, a two-stage black-box attack that (1) constructs malicious documents containing misinformation or emotion-inducing content and injects them into the knowledge base, and (2) iteratively optimizes them using a localization algorithm and Masked Language Model (MLM) guided on reference context feedback, ensuring their retrieval priority while preserving linguistic naturalness. With only five malicious documents per target question injected into the million-document MS MARCO dataset, CtrlRAG achieves up to 90% attack success rates on commercial LLMs (e.g., GPT-4o), a 30% improvement over optimal baselines, in both *Emotion Manipulation* and *Hallucination Amplification* tasks. Furthermore, we show that existing defenses fail to balance security and performance. To mitigate this challenge, we introduce a dynamic *Knowledge Expansion* defense strategy based on *Parametric/Non-parametric Memory Confrontation*, blocking 78% of attacks while maintaining 95.5% system accuracy. Our findings reveal critical vulnerabilities in RAG systems and provide effective defense strategies.

</details>

### 45. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2402.07867) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)　📅 2024-02　🏷 USENIX Security 2025

**关键词**：`attack`、`knowledge corruption`、`targeted answer`、`black-box poisoning`

👤 **作者**：Wei Zou、Runpeng Geng、Binghui Wang、Jinyuan Jia

- 🎯 **研究动机**：RAG 的安全几乎未探索，其外部知识库引入新的实用攻击面
- 🔬 **研究方法**：PoisonedRAG 将知识腐化攻击形式化为优化问题，按黑盒/白盒背景知识分别求解，注入少量恶意文本诱导 LLM 对目标问题生成指定答案
- 📌 **结论**：百万级文本库中每题注入 5 篇即达 90% ASR，所测防御均不足

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have achieved remarkable success due to their exceptional generative capabilities. Despite their success, they also have inherent limitations such as a lack of up-to-date knowledge and hallucination. Retrieval-Augmented Generation (RAG) is a state-of-the-art technique to mitigate these limitations. The key idea of RAG is to ground the answer generation of an LLM on external knowledge retrieved from a knowledge database. Existing studies mainly focus on improving the accuracy or efficiency of RAG, leaving its security largely unexplored. We aim to bridge the gap in this work. We find that the knowledge database in a RAG system introduces a new and practical attack surface. Based on this attack surface, we propose PoisonedRAG, the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. We formulate knowledge corruption attacks as an optimization problem, whose solution is a set of malicious texts. Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, we propose two solutions to solve the optimization problem, respectively. Our results show PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts. We also evaluate several defenses and our results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

</details>
### Agentic RAG, Reasoning & Indirect Injection

### 46. Salience Induction against Multi-Hop RAG Agents: Threat and Defense

📄 [arXiv](https://arxiv.org/abs/2607.17535)　📅 2026-07

**关键词**：`attack`、`agentic RAG poisoning`、`salience channel`、`truth-preserving edit`

👤 **作者**：Xingfu Zhou、Pengfei Wang、Yuan Zhou、Wei Xie、Xu Zhou

- 🎯 **研究动机**：agentic RAG 防御聚焦内容投毒与提示注入，忽视第三攻击面：事实位置、强调与框架等显著性信道在全部陈述为真时仍可重定向推理
- 🔬 **研究方法**：形式化 Salience Induction 为保真编辑（六类显著性编辑算子+迭代 proposer-verifier），构建 SalientWiki-MH 基准；提出输入侧 Salience Normalization 防御
- 📌 **结论**：30% 编辑预算下 ASR 83.3%，最强基线防御后仍留 75.7%；Salience Normalization 降到标准攻击 15.3%、自适应攻击 23.6%，证明真实性与指令过滤并不足够

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic retrieval-augmented generation (RAG) systems increasingly retrieve external evidence and orchestrate tools for knowledge-intensive applications. In Multi-Hop question answering, agents chain facts across documents. Existing defenses focus on content poisoning, which injects false facts, and prompt injection, which embeds directives. We identify a third attack surface: the salience channel, through which fact position, emphasis, framing, and semantic proximity can redirect reasoning even when all retrieved claims are true and no instructions are present. We formalize Salience Induction as truth-preserving edits that redirect Multi-Hop attribute binding while leaving the retrieval trace semantically intact. We define six Salience-Editing operator classes and build an iterative proposer-verifier pipeline under factual and stealth constraints. We also introduce SalientWiki-MH, a decoy-annotated Multi-Hop benchmark. Evaluations across five frontier model families (GPT, Claude, Gemini, DeepSeek, and Qwen) and three agent architectures (ReAct, Reflexion, and tool-calling) show broad generalization. Under a 30% edit budget, Salience Induction achieves an 83.3% attack success rate; the strongest evaluated baseline defense leaves 75.7% post-defense ASR. Untargeted rewriting further reduces attacks only by degrading neutral task success. Our lightweight input-side defense, Salience Normalization, reduces attack success to 15.3% under standard attacks and 23.6% under an adaptive attack. These results show that truthfulness and instruction filtering alone are insufficient: robust agentic RAG also requires defenses against salience-relevance decoupling.

</details>

### 47. KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2607.00422)　📅 2026-07

**关键词**：`attack`、`agentic RAG poisoning`、`staged document chain`、`reasoning hijack`、`staged web poisoning`、`query-rewrite hijack`

👤 **作者**：Chanwoo Choi、…、Buru Chang

- 🎯 **研究动机**：Agentic RAG 迭代检索推理可忽略弱相关毒文，已有攻击多需白盒访问系统提示、推理轨迹或参数
- 🔬 **研究方法**：提出 KidnapRAG 黑盒顺序投毒：用 Bait、Chain-Link、Mal-Ins 三种角色文档分别吸引初始检索、诱导查询改写、提供攻击者控制的证据，劫持多步推理链
- 📌 **结论**：多框架、LLM 与基准上一致超越现有黑盒投毒基线，逐步削弱原检索意图并加重对攻击者证据的依赖

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to poisoning attacks that inject malicious documents into the retrieval process to manipulate model outputs. Recent Agentic RAG systems are more robust to such attacks because they iteratively perform retrieval and reasoning, allowing them to ignore weakly relevant poisoned documents and preserve the reasoning chain induced by the user query. However, existing attacks on Agentic RAG systems often assume white-box access to system prompts, reasoning traces, retrievers, or model parameters, limiting their applicability in realistic settings. In this paper, we study black-box poisoning attacks against Agentic RAG systems, where the attacker can only publish externally retrievable poisoned documents. We propose KidnapRAG, a sequential poisoning attack that hijacks the agent's multi-step reasoning chain using three role-specific documents: Bait, Chain-Link, and Mal-Ins, which attract initial retrieval, induce query reformulation, and provide attacker-controlled evidence, respectively. Experiments across multiple Agentic RAG frameworks, LLM backbones, and benchmarks show that KidnapRAG consistently outperforms existing poisoning baselines under black-box conditions. Further analyses show that KidnapRAG progressively weakens the original retrieval intent, redirects retrieval behavior, and increases reliance on attacker-controlled evidence. Our code is publicly available at https://github.com/chanwoochoi316/KidnapRAG.

</details>

### 48. Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents

📄 [arXiv](https://arxiv.org/abs/2606.24402)　📅 2026-06

**关键词**：`attack`、`security-agent RAG`、`poison adoption`、`verification boundary`

👤 **作者**：Juho Park、Hyunmin Choi、Kevin Nam

- 🎯 **研究动机**：RAG 投毒研究集中于 QA 答案污染，安全 agent 会把检索到的投毒知识转化为错误利用行为，这一行动型风险未知
- 🔬 **研究方法**：构造 Poisoned Playbooks 注入公开式安全知识源，跨 11 个 CTF、3 个前沿 LLM 家族、11 个真实 CVE 评估毒文采用规律，并提出 Verification Boundary 三级经验分类解释
- 📌 **结论**：毒文采用是系统性的而非随机；验证提示与多源检索在有强证据时有效，在稀疏证据与零日条件下失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning. This creates a new risk: poisoned write-ups can be operationalized into incorrect exploit behavior. Yet, prior work on RAG poisoning has mostly studied answer corruption in QA settings, much less is known about action-taking security agents. This paper aims to reveal such characteristics with crafted poisons about real-world challenges and AI agents. First, we demonstrate how a crafted single poisoned write-up injected into public-style security knowledge sources which we denote as Poisoned Playbooks, alters the behavior of RAG-based AI security agents. Across 11 CTF challenges, 3 frontier LLM families, 2 model generations, and 11 real-world CVEs, we find that poison adoption is systematic rather than random. To explain this pattern, we introduce the Verification Boundary (VB), a 3-level empirical classification based on what evidence the agent can use to refute a retrieved claim. Finally, we evaluate verification prompting and multi-source retrieval, showing that both help when stronger evidence exists, but weaken under sparse-evidence and zero-day conditions.

</details>

### 49. AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning

📄 [arXiv](https://arxiv.org/abs/2604.12201) · 🌐 [Project](https://doi.org/10.1145/3805712.3809838)　📅 2026-04　🏷 SIGIR 2026

**关键词**：`attack`、`adversarial CoT`、`single-document poison`、`reasoning hijack`、`single-document poisoning`、`query-specific attack`

👤 **作者**：Hongru Song、…、Xueqi Cheng

- 🎯 **研究动机**：RAG 知识库投毒研究靠海量毒文档淹没语料库，单文档的隐蔽投毒未被探索
- 🔬 **研究方法**：AdversarialCoT 是 query-specific 攻击：提取目标 LLM 推理框架构建初始对抗 CoT，再通过与 LLM 交互迭代精炼单篇毒文档
- 📌 **结论**：单篇对抗文档即可显著降低基准 LLM 的推理准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) enhances large language model (LLM) reasoning by retrieving external documents, but also opens up new attack surfaces. We study knowledge-base poisoning attacks in RAG, where an attacker injects malicious content into the retrieval corpus, which is then naturally surfaced by the retriever and consumed by the LLM during reasoning. Unlike prior work that floods the corpus with poisoned documents, we propose AdversarialCoT, a query-specific attack that poisons only a single document in the corpus. AdversarialCoT first extracts the target LLM's reasoning framework to guide the construction of an initial adversarial chain-of-thought (CoT). The adversarial document is iteratively refined through interactions with the LLM, progressively exposing and exploiting critical reasoning vulnerabilities. Experiments on benchmark LLMs show that a single adversarial document can significantly degrade reasoning accuracy, revealing subtle yet impactful weaknesses. This study exposes security risks in RAG systems and provides actionable insights for designing more robust LLM reasoning pipelines.

</details>

### 50. PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2603.25164) · 🌐 [Project](https://anonymous.4open.science/r/PIDP-03BC)　📅 2026-03

**关键词**：`attack`、`RAG poisoning`、`database poisoning`、`prompt injection`

👤 **作者**：Haozhen Wang、Haoyue Liu、Jionghao Zhu、Zhichao Wang、Yongxin Guo、Xiaoying Tang

- 🎯 **研究动机**：现有 RAG 投毒需预知用户具体查询，限制灵活性与现实性
- 🔬 **研究方法**：PIDP-Attack 复合推理时向查询附加恶意字符（prompt injection）与向数据库注入少量毒段落（投毒），无需预知实际查询
- 📌 **结论**：在 NQ、HotpotQA、MS-MARCO 与 8 个 LLM 上稳定超越 PoisonedRAG，ASR 提升 4%-16% 且保持高检索精度

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have demonstrated remarkable performance across a wide range of applications. However, their practical deployment is often hindered by issues such as outdated knowledge and the tendency to generate hallucinations. To address these limitations, Retrieval-Augmented Generation (RAG) systems have been introduced, enhancing LLMs with external, up-to-date knowledge sources. Despite their advantages, RAG systems remain vulnerable to adversarial attacks, with data poisoning emerging as a prominent threat. Existing poisoning-based attacks typically require prior knowledge of the user's specific queries, limiting their flexibility and real-world applicability. In this work, we propose PIDP-Attack, a novel compound attack that integrates prompt injection with database poisoning in RAG. By appending malicious characters to queries at inference time and injecting a limited number of poisoned passages into the retrieval database, our method can effectively manipulate LLM response to arbitrary query without prior knowledge of the user's actual query. Experimental evaluations across three benchmark datasets (Natural Questions, HotpotQA, MS-MARCO) and eight LLMs demonstrate that PIDP-Attack consistently outperforms the original PoisonedRAG. Specifically, our method improves attack success rates by 4% to 16% on open-domain QA tasks while maintaining high retrieval precision, proving that the compound attack strategy is both necessary and highly effective.

</details>

### 51. When Safety Becomes a Vulnerability: Exploiting LLM Alignment Homogeneity for Transferable Blocking in RAG

📄 [arXiv](https://arxiv.org/abs/2603.03919)　📅 2026-03

**关键词**：`attack`、`RAG availability`、`alignment homogeneity`、`transferable refusal`

👤 **作者**：Junchen Li、…、Shuang Liang

- 🎯 **研究动机**：基于对抗后缀或显式指令的 RAG 阻断攻击对现代 LLM 失效且易被注入过滤
- 🔬 **研究方法**：利用安全对齐 LLM 风险类别与拒答准则趋同（alignment homogeneity），TabooRAG 在代理环境中优化查询相关的风险上下文诱发对齐性拒答，并以策略库复用降低成本
- 📌 **结论**：9 个 LLM、3 个数据集上过滤后仍 SOTA，ASR 相对平均最优基线提升 67.3%，对未见目标模型仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to blocking attacks, in which poisoned documents cause large language models (LLMs) to refuse benign queries. Existing attacks rely on adversarial suffixes or explicit instructions, which are increasingly ineffective against modern LLMs, susceptible to prompt injection filtering, or require feedback from the target system. We observe overlapping risk categories and refusal criteria across safety-aligned LLMs, a phenomenon we term alignment homogeneity. This shared attack surface makes refusal-inducing context transferable across models. Accordingly, we propose TabooRAG, which optimizes one document per query for retrieval and refusal induction in a surrogate RAG environment, then transfers it to an unknown target system. Rather than injecting instructions, TabooRAG constructs query-relevant risk context to trigger alignment-driven refusal. To reduce optimization cost, it reuses validated strategies through a query-aware strategy library. Across nine LLMs and three datasets, TabooRAG achieves state-of-the-art ASR after filtering, with a 67.3% relative gain over the average per-setting best baseline. Further experiments show that TabooRAG remains effective with diverse surrogate models, against unseen target models, and under stronger RAG pipelines and existing defenses.

</details>

### 52. Chain-of-Thought Poisoning Attacks against R1-based Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2505.16367)　📅 2025-05

**关键词**：`attack`、`reasoning-model RAG`、`CoT template`、`knowledge-base poisoning`

👤 **作者**：Hongru Song、Yu-an Liu、Ruqing Zhang、Jiafeng Guo、Yixing Fan

- 🎯 **研究动机**：深度推理模型加持的 RAG 下，单纯注入错误知识的攻击不再有效
- 🔬 **研究方法**：从 R1 式 RAG 系统提取推理过程模板，把错误知识包装成对抗文档注入知识库，伪装成模型的历史推理过程
- 📌 **结论**：MS MARCO 上对抗文档更易被模型引用，攻击有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems can effectively mitigate the hallucination problem of large language models (LLMs),but they also possess inherent vulnerabilities. Identifying these weaknesses before the large-scale real-world deployment of RAG systems is of great importance, as it lays the foundation for building more secure and robust RAG systems in the future. Existing adversarial attack methods typically exploit knowledge base poisoning to probe the vulnerabilities of RAG systems, which can effectively deceive standard RAG models. However, with the rapid advancement of deep reasoning capabilities in modern LLMs, previous approaches that merely inject incorrect knowledge are inadequate when attacking RAG systems equipped with deep reasoning abilities. Inspired by the deep thinking capabilities of LLMs, this paper extracts reasoning process templates from R1-based RAG systems, uses these templates to wrap erroneous knowledge into adversarial documents, and injects them into the knowledge base to attack RAG systems. The key idea of our approach is that adversarial documents, by simulating the chain-of-thought patterns aligned with the model's training signals, may be misinterpreted by the model as authentic historical reasoning processes, thus increasing their likelihood of being referenced. Experiments conducted on the MS MARCO passage ranking dataset demonstrate the effectiveness of our proposed method.

</details>

### 53. AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

📄 [arXiv](https://arxiv.org/abs/2407.12784) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html)　📅 2024-07　🏷 NeurIPS 2024

**关键词**：`attack`、`optimized trigger`、`memory bank`、`knowledge base`、`agentic RAG backdoor`、`action hijacking`

👤 **作者**：Zhaorun Chen、Zhen Xiang、Chaowei Xiao、Dawn Song、Bo Li

- 🎯 **研究动机**：LLM Agent 依赖未验证的 memory 或 RAG 知识库，其安全风险未明
- 🔬 **研究方法**：AgentPoison 以约束优化把触发样本映射到唯一嵌入区，含触发指令即高概率检索恶意示范；无需模型训练或微调
- 📌 **结论**：自动驾驶、QA、EHR 三类真实 Agent 平均 ASR 超 80%，投毒率低于 0.1%，良性性能损失小于 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM agents have demonstrated remarkable performance across various applications, primarily due to their advanced capabilities in reasoning, utilizing external knowledge and tools, calling APIs, and executing actions to interact with environments. Current agents typically utilize a memory module or a retrieval-augmented generation (RAG) mechanism, retrieving past knowledge and instances with similar embeddings from knowledge bases to inform task planning and execution. However, the reliance on unverified knowledge bases raises significant concerns about their safety and trustworthiness. To uncover such vulnerabilities, we propose a novel red teaming approach AgentPoison, the first backdoor attack targeting generic and RAG-based LLM agents by poisoning their long-term memory or RAG knowledge base. In particular, we form the trigger generation process as a constrained optimization to optimize backdoor triggers by mapping the triggered instances to a unique embedding space, so as to ensure that whenever a user instruction contains the optimized backdoor trigger, the malicious demonstrations are retrieved from the poisoned memory or knowledge base with high probability. In the meantime, benign instructions without the trigger will still maintain normal performance. Unlike conventional backdoor attacks, AgentPoison requires no additional model training or fine-tuning, and the optimized backdoor trigger exhibits superior transferability, in-context coherence, and stealthiness. Extensive experiments demonstrate AgentPoison's effectiveness in attacking three types of real-world LLM agents: RAG-based autonomous driving agent, knowledge-intensive QA agent, and healthcare EHRAgent. On each agent, AgentPoison achieves an average attack success rate higher than 80% with minimal impact on benign performance (less than 1%) with a poison rate less than 0.1%.

</details>

### 54. Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning

📄 [arXiv](https://arxiv.org/abs/2402.08416)　📅 2024-02

**关键词**：`attack`、`indirect jailbreak`、`RAG poisoning`、`malicious content`

👤 **作者**：Gelei Deng、Yi Liu、Kailong Wang、Yuekang Li、Tianwei Zhang、Yang Liu

- 🎯 **研究动机**：越狱研究集中于直接攻击，RAG 集成（如 GPTs）带来的间接路径未被探索
- 🔬 **研究方法**：Pandora 向检索知识库投毒恶意内容，结合 prompt 操纵间接越狱
- 📌 **结论**：四类场景对 GPT-3.5/GPT-4 成功率 64.3%/34.8%，高于对照的直接攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models~(LLMs) have gained immense popularity and are being increasingly applied in various domains. Consequently, ensuring the security of these models is of paramount importance. Jailbreak attacks, which manipulate LLMs to generate malicious content, are recognized as a significant vulnerability. While existing research has predominantly focused on direct jailbreak attacks on LLMs, there has been limited exploration of indirect methods. The integration of various plugins into LLMs, notably Retrieval Augmented Generation~(RAG), which enables LLMs to incorporate external knowledge bases into their response generation such as GPTs, introduces new avenues for indirect jailbreak attacks. To fill this gap, we investigate indirect jailbreak attacks on LLMs, particularly GPTs, introducing a novel attack vector named Retrieval Augmented Generation Poisoning. This method, Pandora, exploits the synergy between LLMs and RAG through prompt manipulation to generate unexpected responses. Pandora uses maliciously crafted content to influence the RAG process, effectively initiating jailbreak attacks. Our preliminary tests show that Pandora successfully conducts jailbreak attacks in four different scenarios, achieving higher success rates than direct attacks, with 64.3\% for GPT-3.5 and 34.8\% for GPT-4.

</details>
### Multimodal RAG Poisoning

### 55. Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2608.20756)　📅 2026-08

**关键词**：`attack`、`multimodal RAG poisoning`、`visual evidence`、`black-box attack`、`multimodal RAG`、`visual-only payload`

👤 **作者**：Rujin Liang、Zhongpu Chen、Yuhao Lei、Xin Miao

- 🎯 **研究动机**：多模态 RAG 以图像为外部知识源，投毒视觉证据的威胁未被研究，已有攻击依赖篡改文本元数据
- 🔬 **研究方法**：Vis-Poison 视觉知识投毒：中毒图像本身即攻击载荷（不碰字幕、摘要、元数据），多 agent 方法自动构造视觉合理的中毒图；两管线、四嵌入模型、六生成模型评测
- 📌 **结论**：黑盒设定下对 30k 条多模态知识库端到端 ASR 达 40.16%-65.40%；对仅凭参数知识即可正确回答的 MLLM 平均成功率仍超 60%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16% to 65.40% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60%. Code and data are available at https://github.com/SWUFE-DB-Group/Vis-Poison.

</details>

### 56. Hidden in the Metadata: Stealth Poisoning Attacks on Multimodal Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2603.00172)　📅 2026-02

**关键词**：`attack`、`multimodal RAG poisoning`、`metadata manipulation`、`cross-retriever transfer`、`MM-MEPA`、`metadata poisoning`

👤 **作者**：Kennedy Edemacu、Mohammad Mahdi Shokri

- 🎯 **研究动机**：多模态 RAG 防线常审查图像内容却信任配套 metadata
- 🔬 **研究方法**：MM-MEPA 仅操纵图文条目的 metadata、保持视觉内容不变，即可牵引多模态检索并诱导攻击者期望的回答
- 📌 **结论**：跨 4 个 retriever 与 2 个多模态生成器 ASR 最高 91%，代表性防御大多无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has emerged as a powerful paradigm for enhancing multimodal large language models by grounding their responses in external, factual knowledge and thus mitigating hallucinations. However, the integration of externally sourced knowledge bases introduces a critical attack surface. Adversaries can inject malicious multimodal content capable of influencing both retrieval and downstream generation. In this work, we present MM-MEPA, a multimodal poisoning attack that targets the metadata components of image-text entries while leaving the associated visual content unaltered. By only manipulating the metadata, MM-MEPA can still steer multimodal retrieval and induce attacker-desired model responses. We evaluate the attack across multiple benchmark settings and demonstrate its severity. MM-MEPA achieves an attack success rate of up to 91\% consistently disrupting system behaviors across four retrievers and two multimodal generators. Additionally, we assess representative defense strategies and find them largely ineffective against this form of metadata-only poisoning. Our findings expose a critical vulnerability in multimodal RAG and underscore the urgent need for more robust, defense-aware retrieval and knowledge integration methods.

</details>

### 57. MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks

🎓 [Official](https://aclanthology.org/2026.acl-long.1558/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`multimodal safety`、`RAG poisoning`、`VLM safety`、`RAG security`、`data poisoning`

👤 **作者**：Hyeonjeong Ha、…、Heng Ji

- 🎯 **研究动机**：多模态 RAG 依赖外部检索，知识库被注入恶意多模态内容的系统性风险未被研究
- 🔬 **研究方法**：Localized Poisoning 植入查询特定多模态错误信息定向操纵输出，Globalized Poisoning 单次无目标注入广泛破坏推理
- 📌 **结论**：受限访问下 LPA ASR 达 56% 且跨四个检索器免重优化迁移；GPA 单条毒内容将生成准确率打到 0%；两者均绕过现有防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) has become a common practice in multimodal large language models (MLLM) to enhance factual grounding and reduce hallucination. Yet, its reliance on retrieval exposes MLLMs to knowledge poisoning attacks, in which adversaries deliberately inject malicious multimodal content into external knowledge bases to steer models toward generating incorrect or even harmful responses. We present MM-PoisonRAG, a framework to systematically study the vulnerability of multimodal RAG under knowledge poisoning. Specifically, we design two novel attack strategies: Localized Poisoning Attack (LPA), which implants targeted, query-specific multimodal misinformation to manipulate outputs toward attacker-controlled responses, and Globalized Poisoning Attack (GPA), which uses a single, untargeted adversarial injection to broadly corrupt reasoning and collapse generation quality across all queries. Extensive experiments on diverse tasks, multimodal RAG components, and attacker access levels reveal severe vulnerabilities: LPA achieves up to 56% attack success rate even under restricted access, and transfers effectively across four different retrievers without re-optimizing the adversaries. GPA completely disrupts model generation to 0% accuracy with just one poisoned content. Moreover, both LPA and GPA bypass existing defenses, underscoring the fragility of multimodal RAG and establishing MM-PoisonRAG as a foundation for future research on securing RAG frameworks against multimodal knowledge poisoning.

</details>

### 58. Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation

🌐 [Project](https://anonymous.4open.science/r/M3Att) · 🎓 [Official](https://aclanthology.org/2026.acl-long.892/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`medical AI`、`data poisoning`、`high-risk deployment`、`RAG security`、`M³Att`

👤 **作者**：Peiru Yang、…、Tao Qi

- 🎯 **研究动机**：医学 RAG 知识投毒攻击多假设攻击者预知用户查询，不现实限制实用
- 🔬 **研究方法**：M3Att 仅假设数据库分布知识：文本注入隐蔽错误信息，配对视觉数据作查询无关触发操纵检索概率，并利用诊断模糊性设计绕过 LLM 自我纠正的注入策略
- 📌 **结论**：五个 LLM 与数据集上稳定产出临床貌似合理但错误的生成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multi-modal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M 3 Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M 3 Att consistently produces clinically plausible yet incorrect generations. Codes: https://anonymous.4open.science/r/M3Att.

</details>

### 59. Spa-VLM: Stealthy Poisoning Attacks on RAG-based VLM

📄 [arXiv](https://arxiv.org/abs/2505.23828)　📅 2025-05

**关键词**：`attack`、`multimodal RAG poisoning`、`image-text payload`、`large-scale knowledge base`、`image-text knowledge`、`large-scale KB`

👤 **作者**：Lei Yu、…、Jing Wang

- 🎯 **研究动机**：单模态 RAG 投毒在多模态 RAG 场景 100% 失败，多模态攻击面未被揭示
- 🔬 **研究方法**：提出 Spa-VLM，精心构造对抗图像加误导文本的多模态知识条目注入知识库
- 📌 **结论**：向 100K 与 2M 条目的库注入仅 5 条即获超 0.8 ASR，多种防御均无效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rapid development of the Vision-Language Model (VLM), significant progress has been made in Visual Question Answering (VQA) tasks. However, existing VLM often generate inaccurate answers due to a lack of up-to-date knowledge. To address this issue, recent research has introduced Retrieval-Augmented Generation (RAG) techniques, commonly used in Large Language Models (LLM), into VLM, incorporating external multi-modal knowledge to enhance the accuracy and practicality of VLM systems. Nevertheless, the RAG in LLM may be susceptible to data poisoning attacks. RAG-based VLM may also face the threat of this attack. This paper first reveals the vulnerabilities of the RAG-based large model under poisoning attack, showing that existing single-modal RAG poisoning attacks have a 100\% failure rate in multi-modal RAG scenarios. To address this gap, we propose Spa-VLM (Stealthy Poisoning Attack on RAG-based VLM), a new paradigm for poisoning attacks on large models. We carefully craft malicious multi-modal knowledge entries, including adversarial images and misleading text, which are then injected into the RAG's knowledge base. When users access the VLM service, the system may generate misleading outputs. We evaluate Spa-VLM on two Wikipedia datasets and across two different RAGs. Results demonstrate that our method achieves highly stealthy poisoning, with the attack success rate exceeding 0.8 after injecting just 5 malicious entries into knowledge bases with 100K and 2M entries, outperforming state-of-the-art poisoning attacks designed for RAG-based LLMs. Additionally, we evaluated several defense mechanisms, all of which ultimately proved ineffective against Spa-VLM, underscoring the effectiveness and robustness of our attack.

</details>

### 60. One Pic is All it Takes: Poisoning Visual Document Retrieval Augmented Generation with a Single Image

📄 [arXiv](https://arxiv.org/abs/2504.02132) · 📝 [OpenReview](https://openreview.net/forum?id=CLkjUid1Yg)　📅 2025-04

**关键词**：`attack`、`visual-document RAG`、`single-image poisoning`、`targeted DoS`、`single image`、`targeted／universal attack`

👤 **作者**：Ezzeldin Shereen、Dan Ristea、Shae McFadden、Burak Hasircioglu、Vasilios Mavroudis、Chris Hicks

- 🎯 **研究动机**：以页面截图为知识库的 VD-RAG 引入图像模态，也带来投毒新攻击面
- 🔬 **研究方法**：定义 targeted 传播虚假信息与 universal DoS 两类攻击目标，用多目标梯度优化或生成模型仅注入单张对抗图像
- 📌 **结论**：两个视觉文档数据集、多种检索器与 VLM 上两类攻击均成立，universal 场景对黑盒攻击较鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is instrumental for inhibiting hallucinations in large language models (LLMs) through the use of a factual knowledge base (KB). Although PDF documents are prominent sources of knowledge, text-based RAG pipelines are ineffective at capturing their rich multi-modal information. In contrast, visual document RAG (VD-RAG) uses screenshots of document pages as the KB, which has been shown to achieve state-of-the-art results. However, by introducing the image modality, VD-RAG introduces new attack vectors for adversaries to disrupt the system by injecting malicious documents into the KB. In this paper, we demonstrate the vulnerability of VD-RAG to poisoning attacks targeting both retrieval and generation. We define two attack objectives and demonstrate that both can be realized by injecting only a single adversarial image into the KB. Firstly, we introduce a targeted attack against one or a group of queries with the goal of spreading targeted disinformation. Secondly, we present a universal attack that, for any potential user query, influences the response to cause a denial-of-service in the VD-RAG system. We investigate the two attack objectives under both white-box and black-box assumptions, employing a multi-objective gradient-based optimization approach as well as prompting state-of-the-art generative models. Using two visual document datasets, a diverse set of state-of-the-art retrievers (embedding models) and generators (vision language models), we show VD-RAG is vulnerable to poisoning attacks in both the targeted and universal settings, yet demonstrating robustness to black-box attacks in the universal setting.

</details>
### GraphRAG & Structured-Knowledge Poisoning

### 61. LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2604.02954) · 🎓 [Official](https://aclanthology.org/2026.acl-long.252/)　📅 2026-04　🏷 ACL 2026

**关键词**：`attack`、`GraphRAG poisoning`、`entity swapping`、`topology poisoning`、`RAG security`、`data poisoning`

👤 **作者**：Yilin Xiao、…、Xiao Huang

- 🎯 **研究动机**：GraphRAG 安全性根本上依赖图拓扑完整性，隐式破坏逻辑连接的攻击未被研究
- 🔬 **研究方法**：LogicPoison 用类型保持的实体交换扰动全局逻辑枢纽与查询特定推理桥，切断多跳推理路径且不改表层文本语义
- 📌 **结论**：绕过 GraphRAG 固有防御并显著降低性能，在有效性与隐蔽性上均超 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph-based Retrieval-Augmented Generation (GraphRAG) enhances the reasoning capabilities of Large Language Models (LLMs) by grounding their responses in structured knowledge graphs. Leveraging community detection and relation filtering techniques, GraphRAG systems demonstrate inherent resistance to traditional RAG attacks, such as text poisoning and prompt injection. However, in this paper, we find that the security of GraphRAG systems fundamentally relies on the topological integrity of the underlying graph, which can be undermined by implicitly corrupting the logical connections, without altering surface-level text semantics. To exploit this vulnerability, we propose \textsc{LogicPoison}, a novel attack framework that targets logical reasoning rather than injecting false contents. Specifically, \textsc{LogicPoison} employs a type-preserving entity swapping mechanism to perturb both global logic hubs for disrupting overall graph connectivity and query-specific reasoning bridges for severing essential multi-hop inference paths. This approach effectively reroutes valid reasoning into dead ends while maintaining surface-level textual plausibility. Comprehensive experiments across multiple benchmarks demonstrate that \textsc{LogicPoison} successfully bypasses GraphRAG's defenses, significantly degrading performance and outperforming state-of-the-art baselines in both effectiveness and stealth. Our code is available at \textcolor{blue}https://github.com/Jord8061/logicPoison.

</details>

### 62. KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2603.11501) · 🌐 [Project](https://doi.org/10.1145/3774904.3792547)　📅 2026-03

**关键词**：`attack`、`GraphRAG poisoning`、`knowledge evolution`、`persistent poisoning`

👤 **作者**：Qizhi Chen、…、Shuang Liang

- 🎯 **研究动机**：GraphRAG 把注入文本重组为知识图再推理，针对常规 RAG 的投毒方法对其无效
- 🔬 **研究方法**：KEPo 按目标答案生成毒性事件，伪造事件背景与从原始事实到毒性事件的知识演化路径毒化 KG；多目标场景连接多个攻击语料互相强化
- 📌 **结论**：多数据集上单目标与多目标攻击 ASR 均达 SOTA，显著超越先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph-based Retrieval-Augmented Generation (GraphRAG) constructs the Knowledge Graph (KG) from external databases to enhance the timeliness and accuracy of Large Language Model (LLM) generations. However, this reliance on external data introduces new attack surfaces. Attackers can inject poisoned texts into databases to manipulate LLMs into producing harmful target responses for attacker-chosen queries. Existing research primarily focuses on attacking conventional RAG systems. However, such methods are ineffective against GraphRAG. This robustness derives from the KG abstraction of GraphRAG, which reorganizes injected text into a graph before retrieval, thereby enabling the LLM to reason based on the restructured context instead of raw poisoned passages. To expose latent security vulnerabilities in GraphRAG, we propose Knowledge Evolution Poison (KEPo), a novel poisoning attack method specifically designed for GraphRAG. For each target query, KEPo first generates a toxic event containing poisoned knowledge based on the target answer. By fabricating event backgrounds and forging knowledge evolution paths from original facts to the toxic event, it then poisons the KG and misleads the LLM into treating the poisoned knowledge as the final result. In multi-target attack scenarios, KEPo further connects multiple attack corpora, enabling their poisoned knowledge to mutually reinforce while expanding the scale of poisoned communities, thereby amplifying attack effectiveness. Experimental results across multiple datasets demonstrate that KEPo achieves state-of-the-art attack success rates for both single-target and multi-target attacks, significantly outperforming previous methods.

</details>

### 63. BadGraph: Structural Knowledge Isolation Attacks against Graph Retrieval-Augmented Generation

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-leiming)　📅 2026　🏷 USENIX Security 2026

**关键词**：`attack`、`GraphRAG`、`RAG poisoning`、`knowledge corruption`、`topology poisoning`、`availability`

👤 **作者**：Leiming Yan、Xinlong Xu、Ziqiang Li

- 🎯 **研究动机**：GraphRAG 的图结构暴露拓扑攻击面，现有攻击依赖显式假答案或毒化关系，易被内容审计标记
- 🔬 **研究方法**：BadGraph 结构性知识隔离攻击：数学分析图算法的三种拓扑漏洞，注入少量语义中性文本生成对抗子图，降低目标证据在检索上下文中的可见性
- 📌 **结论**：HotpotQA 注入 49 篇、2WikiMultiHopQA 30 篇文档，即持续降低 MS-GraphRAG、LightRAG、FastGraphRAG 的源召回与端到端 QA F1

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Graph Retrieval-Augmented Generation (GraphRAG) improves cross-document reasoning by introducing graph structures into retrieval. However, these graph structures also expose an under-studied topological attack surface. Existing research on GraphRAG attacks primarily focuses on targeted attacks based on text or relation manipulation, which induce the model to generate specific incorrect answers by injecting factual errors. These attacks often rely on explicit false-answer payloads, poisoned relations, or corpus rewriting, and their documents can be easier to flag during content auditing. In this paper, we propose a targeted availability attack against GraphRAG: Structural Knowledge Isolation. Unlike traditional wrong-answer manipulation attacks, this attack targets the system's availability by degrading retrieval of critical evidence through topological manipulation. The resulting context can lack the evidence needed for grounded answer generation. We first mathematically analyze three topological vulnerabilities of graph algorithms used in GraphRAG systems when subjected to topological perturbations. Based on this analysis, we propose the BadGraph attack framework. By injecting a small amount of semantically neutral text, it generates adversarial subgraphs in the knowledge graph and reduces the visibility of target evidence in top-ranked retrieval contexts. Experiments show that with a small document injection budget (49 documents on HotpotQA and 30 on 2WikiMultiHopQA), BadGraph consistently lowers source recall and end-to-end QA F1 on three mainstream GraphRAG systems (MS-GraphRAG, LightRAG, and FastGraphRAG), while using neutral linker documents.

</details>

### 64. GraphRAG under Fire

📄 [arXiv](https://arxiv.org/abs/2501.14050) · 🎓 [Official](https://sp2026.ieee-security.org/accepted-papers.html)　📅 2025-01　🏷 IEEE S&P 2026

**关键词**：`attack`、`GraphRAG poisoning`、`relation injection`、`scalable attack`

👤 **作者**：Jiacheng Liang、…、Ting Wang

- 🎯 **研究动机**：GraphRAG 对普通 RAG 投毒更稳健，但图结构索引检索同时引入新攻击面
- 🔬 **研究方法**：GragPoison 利用知识图共享关系：关系注入引入假知识、关系增强放大影响、叙事生成嵌入连贯恶意文本
- 📌 **结论**：攻击成功率最高 98% 且投毒文本用量减少 68% 以上，一次污染可同时妥协多个查询

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

GraphRAG advances retrieval-augmented generation (RAG) by structuring external knowledge as multi-scale knowledge graphs, enabling language models to integrate both broad context and granular details in their generation. While GraphRAG has demonstrated success across domains, its security implications remain largely unexplored. To bridge this gap, this work examines GraphRAG's vulnerability to poisoning attacks, uncovering an intriguing security paradox: existing RAG poisoning attacks are less effective under GraphRAG than conventional RAG, due to GraphRAG's graph-based indexing and retrieval; yet, the same features also create new attack surfaces. We present GragPoison, a novel attack that exploits shared relations in the underlying knowledge graph to craft poisoning text capable of compromising multiple queries simultaneously. GragPoison employs three key strategies: (i) relation injection to introduce false knowledge, (ii) relation enhancement to amplify poisoning influence, and (iii) narrative generation to embed malicious content within coherent text. Empirical evaluation across diverse datasets and models shows that GragPoison substantially outperforms existing attacks in terms of effectiveness (up to 98% success rate) and scalability (using less than 68% poisoning text) on multiple variations of GraphRAG. We also explore potential defensive measures and their limitations, identifying promising directions for future research.

</details>
### Online Detection & Filtering

### 65. Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems

📄 [arXiv](https://arxiv.org/abs/2608.21095)　📅 2026-08

**关键词**：`detection`、`RAG misinformation`、`factual verification`、`cross-dataset calibration`、`knowledge-poisoning detection`、`NLI verification`

👤 **作者**：Balkrishna Giri、Md Toufique Hasan、Jussi Rasku、Muhammad Waseem、Pekka Abrahamsson

- 🎯 **研究动机**：RAG 默认信任检索内容，高语义相关性不等于事实真实，攻击者可借 knowledge poisoning 注入恶意文档制造定向错误信息
- 🔬 **研究方法**：提出 Evaluation Agent 中间件，组合 NLI 事实校验、五信号投毒检测器（相关性加权聚合）与带非线性阻尼的 Trust Index T=0.4F+0.35C+0.25(1-P)
- 📌 **结论**：TruthfulQA+Llama 3.3 70B 上达 91% 准确率、100% precision 与 100% injection recall；OWASP 安全编码助手场景阻断注入 F1 92%，但语义弱化与跨数据集迁移仍需领域校准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance does not guarantee factual truth. Adversaries exploit this through knowledge poisoning, inserting malicious documents to cause targeted misinformation. We propose an Evaluation Agent, middleware that combines Natural Language Inference (NLI) factual verification, a five-signal poison detector with relevance-weighted aggregation, and a Trust Index T = 0.4 F + 0.35 C + 0.25 (1 - P ) with a non-linear dampener for high-contamination contexts. On TruthfulQA with Llama 3.3 70B, the agent reaches 91% accuracy and 100% precision, with 100% recall on instruction injection, while in-place edits, such as entity swaps, remain hard to detect. Across three LLMs the Trust Index stays discriminative, with a Receiver Operating Characteristic Area Under the Curve (ROC-AUC) of 0.73 to 0.81; generation style matters more than model size, and per-LLM threshold calibration restores baseline competitive accuracy, whereas a weaker FEVER result shows that cross-dataset generalization requires domain-specific calibration. In a software-engineering use case, a secure-coding assistant over guidance from the Open Worldwide Application Security Project (OWASP) Top 10 and the Common Weakness Enumeration (CWE), the agent reliably blocks instruction injection of unsafe advice (F1 92%), while contradiction and subtle semantic weakening remain hard. Throughout, the agent measures detection of poisoned context before generation, not whether the LLM adopts the injected misinformation. We release the proposed approach, attack generator, and experimental artifacts at the link: https://github.com/GPT-Laboratory/TrustworthyRAG.

</details>

### 66. RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2608.13010)　📅 2026-08

**关键词**：`detection`、`local contrast`、`neighborhood density`、`label-free filtering`

👤 **作者**：Xinlong Xu、Yoshua Y. Li

- 🎯 **研究动机**：现有 RAG 投毒检测依赖可信参考、特定攻击痕迹或对语料拓扑敏感的全局阈值
- 🔬 **研究方法**：RAGSieve 自参照检测：RSQ 对同次检索 top-5 与 6-20 名做查询局部对比，RSG 对文档语义近邻做语料局部对比，无需投毒标签或可信语料
- 📌 **结论**：RSQ 达 95.2% AUROC、5% 误删下检出 82.2% 投毒；联合部署把攻击成功率从 67.4% 降至 14.0% 并保留 41.3% F1

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation treats an external corpus as inference evidence, allowing injected documents to promote attacker-chosen claims. Existing detectors depend on trusted references, specific attack artifacts, or global thresholds sensitive to corpus topology. We present RAGSieve, a self-referenced detection framework that constructs its reference from the inspected system. RAGSieve-Query (RSQ) performs query-local contrast, scoring top-five candidates against ranks 6-20 of the same retrieval to detect answer-anchor concentration and carrier transitions. RAGSieve-Graph (RSG) performs corpus-local contrast, comparing each document's semantically similar but lexically distinct neighbors with its local baseline to detect coordinated density before queries arrive. Across three QA datasets and six poisoning constructions, RSQ achieves 95.2% AUROC and detects 82.2% of poison at 5% clean-document removal, versus 81.1%/52.5% for GMTP. RSG achieves 93.3%/79.8%, versus 79.4%/37.6% for CleanBase. Joint deployment reduces attack success from 67.4% to 14.0% while retaining 41.3% F1 on unpoisoned retrieval, demonstrating practical protection at both corpus ingestion and query time without poison labels or trusted corpora. Source code is available at https://github.com/XrazyMee/RAGSieve.

</details>

### 67. When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse

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

### 68. Adversarial Hubness Detector: Detecting Hubness Poisoning in Retrieval-Augmented Generation Systems

📄 [arXiv](https://arxiv.org/abs/2602.22427)　📅 2026-02

**关键词**：`detection`、`vector hubness`、`index scanner`、`alert-budget evaluation`、`hubscan`、`vector index`

👤 **作者**：Idan Habler、Vineeth Sai Narajala、Stav Koren、Amy Chang、Tiffany Saade

- 🎯 **研究动机**：RAG 向量检索中的 hubness 可被投毒利用操纵排序、绕过过滤，缺乏检测工具
- 🔬 **研究方法**：hubscan 集成 MAD z-score 统计检测、簇扩散分析、查询扰动稳定性与领域/模态感知检测，支持 FAISS、Pinecone、Qdrant、Weaviate
- 📌 **结论**：0.2% 告警预算下召回 90%、0.4% 下 100%；百万级 MS MARCO 生产验证中干净与对抗内容分数显著分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are essential to contemporary AI applications, allowing large language models to obtain external knowledge via vector similarity search. Nevertheless, these systems encounter a significant security flaw: hubness - items that frequently appear in the top-$k$ retrieval results for a disproportionately high number of varied queries. These hubs can be exploited to introduce harmful content, alter search rankings, bypass content filtering, and decrease system performance. We introduce hubscan, an open-source security scanner that evaluates vector indices and embeddings to identify hubs in RAG systems. Hubscan presents a multi-detector architecture that integrates: (1) robust statistical hubness detection utilizing median/Median Absolute Deviation (MAD)-based z-scores, (2) cluster spread analysis to assess cross-cluster retrieval patterns, (3) stability testing under query perturbations, and (4) domain-aware and modality-aware detection for category-specific and cross-modal attacks. Our solution accommodates several vector databases (FAISS, Pinecone, Qdrant, Weaviate) and offers versatile retrieval techniques, including vector similarity, hybrid search, and lexical matching with reranking capabilities. We evaluate hubscan on Food-101, MS-COCO, and FiQA adversarial hubness benchmarks constructed using state-of-the-art gradient-optimized and centroid-based hub generation methods. Hubscan achieves 90% recall at a 0.2% alert budget and 100% recall at 0.4%, with adversarial hubs ranking above the 99.8th percentile. In testing, domain-scoped scanning recovered 100% of targeted attacks that evaded global detection. Production validation on 1M real web documents from MS MARCO demonstrates significant score separation between clean documents and adversarial content.

</details>

### 69. Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection

📄 [arXiv](https://arxiv.org/abs/2507.18202) · 🎓 [Official](https://aclanthology.org/2025.findings-acl.1263/)　📅 2025-07　🏷 ACL 2025

**关键词**：`detection`、`gradient token`、`masked probability`、`document filtering`

👤 **作者**：San Kim、Jonghwi Kim、Yejin Jeon、Gary Geunbae Lee

- 🎯 **研究动机**：RAG 知识库可被注入对抗文档误导生成，缺乏高精度检测过滤手段
- 🔬 **研究方法**：提出 GMTP：以检索器相似度函数的梯度定位高影响 token，掩码后用 MLM 检查其掩码概率，注入 token 的该概率显著偏低
- 📌 **结论**：清除超 90% 毒内容且保留相关文档，多数据集与对抗设置下保持检索与生成性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by providing external knowledge for accurate and up-to-date responses. However, this reliance on external sources exposes a security risk, attackers can inject poisoned documents into the knowledge base to steer the generation process toward harmful or misleading outputs. In this paper, we propose Gradient-based Masked Token Probability (GMTP), a novel defense method to detect and filter out adversarially crafted documents. Specifically, GMTP identifies high-impact tokens by examining gradients of the retriever's similarity function. These key tokens are then masked, and their probabilities are checked via a Masked Language Model (MLM). Since injected tokens typically exhibit markedly low masked-token probabilities, this enables GMTP to easily detect malicious documents and achieve high-precision filtering. Experiments demonstrate that GMTP is able to eliminate over 90% of poisoned content while retaining relevant documents, thus maintaining robust retrieval and generation performance across diverse datasets and adversarial settings.

</details>

### 70. RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis

📄 [arXiv](https://arxiv.org/abs/2411.18948) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.698/)　📅 2024-11　🏷 EMNLP 2025

**关键词**：`detection`、`RAG poisoning`、`activation analysis`、`response detection`

👤 **作者**：Xue Tan、Hao Luan、Mingyu Luo、Xiaoyan Sun、Ping Chen、Jun Dai

- 🎯 **研究动机**：RAG 投毒攻击的检测方法匮乏
- 🔬 **研究方法**：RevPRAG 分析 LLM 生成正确响应与被毒响应时的激活模式差异，构建自动化检测管线
- 📌 **结论**：多基准数据集与 RAG 架构上真阳性率达 98%，假阳性率约 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enriches the input to LLMs by retrieving information from the relevant knowledge database, enabling them to produce responses that are more accurate and contextually appropriate. It is worth noting that the knowledge database, being sourced from publicly available channels such as Wikipedia, inevitably introduces a new attack surface. RAG poisoning involves injecting malicious texts into the knowledge database, ultimately leading to the generation of the attacker's target response (also called poisoned response). However, there are currently limited methods available for detecting such poisoning attacks. We aim to bridge the gap in this work. Particularly, we introduce RevPRAG, a flexible and automated detection pipeline that leverages the activations of LLMs for poisoned response detection. Our investigation uncovers distinct patterns in LLMs' activations when generating correct responses versus poisoned responses. Our results on multiple benchmark datasets and RAG architectures show our approach could achieve 98% true positive rate, while maintaining false positive rates close to 1%.

</details>
### Attribution & Traceback

### 71. Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution

📄 [arXiv](https://arxiv.org/abs/2606.25721)　📅 2026-06　🏷 EMNLP 2026

**关键词**：`detection`、`RAG poisoning`、`token attribution`、`target tracing`

👤 **作者**：Yan-Lun Chen、Pin-Yu Chen、Chia-Mu Yu、Ying-Dar Lin、Yu-Sung Wu、Wei-Bin Lee

- 🎯 **研究动机**：RAG 语料投毒检测依赖辅助分类器或 LLM 验证，计算开销大
- 🔬 **研究方法**：提出 TRACE 轻量检测：经 token 影响归因追踪检索文档中反复出现的高影响关键词，再做二次验证确认其对模型预测的影响，同时还原攻击者指定目标答案
- 📌 **结论**：三个 QA 基准、六个 LLM 上检测性能强且能恢复投毒目标答案

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead. We present TRACE, a lightweight detection framework that identifies poisoning attacks by tracing answer-related tokens through token influence attribution. TRACE first discovers recurrent high-influence keywords across retrieved documents and then performs a secondary verification to confirm their influence on model predictions. Experiments on three QA benchmarks and six LLMs demonstrate strong detection performance while simultaneously uncovering attacker-specified target answers.

</details>

### 72. Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence

📄 [arXiv](https://arxiv.org/abs/2605.01782)　📅 2026-05

**关键词**：`detection`、`character-level traceback`、`counterfactual replay`、`forensic localization`

👤 **作者**：Huining Cui、Wei Liu

- 🎯 **研究动机**：RAG 毒化回溯多停留在 passage 级，而现代攻击的有效 payload 可能只是良性 chunk 内的短伪造 claim 或隐藏指令
- 🔬 **研究方法**：RAGCharacter 两遍取证：Pass-0 记录 prompt 锚定执行轨迹，Pass-1 对被触发的轨迹做预算化反事实掩码重放，输出归因 span
- 📌 **结论**：在两个 QA 语料、五类攻击、六个 LLM 上于定位精度与低 over-attribution 间取得最佳总体权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) improves factual grounding by conditioning large language models on retrieved evidence, but it also opens a data-layer attack surface: poisoned corpus entries can steer outputs without changing model parameters. Existing defenses and traceback methods are largely passage-level, which is too coarse for modern attacks whose effective payload may be a short fabricated claim, trigger phrase, or hidden instruction embedded inside an otherwise benign chunk. We study black-box character-level poison traceback in RAG and present RAGCharacter, a two-pass forensic framework that localizes the responsible retrieved span for a concrete misgeneration event. Pass-0 runs standard RAG while logging a prompt-anchored execution trace. Pass-1 re-enters a triggered trace and performs event-conditioned traceback over prompt-used evidence via budgeted counterfactual masking and replay, yielding an attribution span for forensic reporting and a causal span under the logged trace. We further introduce an evaluation protocol that measures both event-level chunk traceback and character-level localization fidelity. Across two QA corpora, five poisoning attack families, six target LLMs, and multiple passage- and character-level baselines, RAGCharacter achieves the best overall trade-off within our benchmark between localization accuracy and low over-attribution. These results suggest that prompt-conditioned, black-box character-level traceback can be feasible, moving RAG forensics from document-level suspicion toward finer-grained evidence auditing and potential remediation.

</details>

### 73. Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2509.13772)　📅 2025-09　🏷 IEEE S&P 2026

**关键词**：`detection`、`responsibility attribution`、`black-box forensics`、`multi-attacker setting`

👤 **作者**：Baolei Zhang、…、Minghong Fang

- 🎯 **研究动机**：RAG 投毒防御常被自适应攻击绕过，缺乏黑盒责任归因来定位毒文本
- 🔬 **研究方法**：提出 RAGOrigin：为每次误生成构建聚焦归因范围，按检索排名、语义相关性与对生成响应的影响打责任分，再以无监督聚类隔离毒文本
- 📌 **结论**：七个数据集、15 种投毒（含自适应与多攻击者场景）上优于基线，动态噪声条件下稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) integrates external knowledge into large language models to improve response quality. However, recent work has shown that RAG systems are highly vulnerable to poisoning attacks, where malicious texts are inserted into the knowledge database to influence model outputs. While several defenses have been proposed, they are often circumvented by more adaptive or sophisticated attacks. This paper presents RAGOrigin, a black-box responsibility attribution framework designed to identify which texts in the knowledge database are responsible for misleading or incorrect generations. Our method constructs a focused attribution scope tailored to each misgeneration event and assigns a responsibility score to each candidate text by evaluating its retrieval ranking, semantic relevance, and influence on the generated response. The system then isolates poisoned texts using an unsupervised clustering method. We evaluate RAGOrigin across seven datasets and fifteen poisoning attacks, including newly developed adaptive poisoning strategies and multi-attacker scenarios. Our approach outperforms existing baselines in identifying poisoned content and remains robust under dynamic and noisy conditions. These results suggest that RAGOrigin provides a practical and effective solution for tracing the origins of corrupted knowledge in RAG systems. Our code is available at: https://github.com/zhangbl6618/RAG-Responsibility-Attribution

</details>

### 74. Traceback of Poisoning Attacks to Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2504.21668) · 🌐 [Project](https://doi.org/10.1145/3696410.3714756)　📅 2025-04

**关键词**：`detection`、`RAG forensics`、`iterative retrieval`、`poison attribution`

👤 **作者**：Baolei Zhang、…、Zheli Liu

- 🎯 **研究动机**：RAG 投毒防御多为推理时缓解，无法定位知识库中的毒文本
- 🔬 **研究方法**：提出 RAGForensics，迭代检索文本子集并用特制 prompt 引导 LLM 检测毒文本，实现投毒溯源
- 📌 **结论**：多数据集上对 SoTA 投毒攻击均能有效溯源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) integrated with retrieval-augmented generation (RAG) systems improve accuracy by leveraging external knowledge sources. However, recent research has revealed RAG's susceptibility to poisoning attacks, where the attacker injects poisoned texts into the knowledge database, leading to attacker-desired responses. Existing defenses, which predominantly focus on inference-time mitigation, have proven insufficient against sophisticated attacks. In this paper, we introduce RAGForensics, the first traceback system for RAG, designed to identify poisoned texts within the knowledge database that are responsible for the attacks. RAGForensics operates iteratively, first retrieving a subset of texts from the database and then utilizing a specially crafted prompt to guide an LLM in detecting potential poisoning texts. Empirical evaluations across multiple datasets demonstrate the effectiveness of RAGForensics against state-of-the-art poisoning attacks. This work pioneers the traceback of poisoned texts in RAG systems, providing a practical and promising defense mechanism to enhance their security. Our code is available at: https://github.com/zhangbl6618/RAG-Responsibility-Attribution

</details>
### Admission Control & Retrieval-Stage Defense

### 75. TRIS: A Tri-Layer Retrieval Integrity Sieve Against Knowledge Poisoning

📄 [arXiv](https://arxiv.org/abs/2609.00470)　📅 2026-09

**关键词**：`defense`、`RAG poisoning`、`retrieval integrity`、`adaptive filtering`

👤 **作者**：Muhaimin Bin Munir、Akib Jawad Ononto、Nazia Shehnaz Joynab、Bhavani Thuraisingham、Latifur Khan

- 🎯 **研究动机**：RAG 对检索文档的隐式信任使 PoisonedRAG 类少量投毒文档即可主导 dense retrieval 并操控股答案
- 🔬 **研究方法**：提出 Tri-Layer Sieve 中间件：跨 embedding 空间聚类（独立 judge）、trigger-payload 结构过滤与 LLM 一致性验证，利用单文档难以同时满足三种约束的脆弱性
- 📌 **结论**：NQ／HotpotQA／MS-MARCO 上黑盒 ASR 从 64-87% 降至 3-14%，白盒 HotFlip 从约 74% 降至 27.8%，clean 准确率恢复到 58-76%；自适应改写下一致性层把 ASR 再减半，代价是每查询约 16-19 秒延迟

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) grounds large language models in external corpora, but implicit trust in retrieved documents creates a critical attack surface: PoisonedRAG shows that a handful of crafted passages can dominate dense retrieval and steer generation toward attacker-chosen answers. We present the Tri-Layer Sieve, a middleware defense that sanitizes retrieved evidence through cross-embedding-space clustering with an independent judge model, structural filtering of trigger-payload artifacts, and LLM consistency verification. The design exploits a key weakness of retrieval-stage poisoning: a single document must satisfy one embedding geometry, one internal Trigger-Payload structure, and one generation objective - rarely all three simultaneously, a fragility that persists even against an adaptive attacker who paraphrases around it. On Natural Questions, HotpotQA, and MS-MARCO with Contriever retrieval (k=50), the Sieve reduces black-box Attack Success Rate from 67.0/87.0/64.0% to 3.0/14.0/4.0%, mitigates white-box HotFlip attacks from ~74% to 27.8% on NQ with Layer 3 enabled, and drives poisoned-document MRR to 0.000, while restoring clean accuracy from 13-33% under attack to 58-76%. Under an architecture-aware adversary who paraphrases triggers to evade the structural filter, enabling the consistency layer halves adaptive ASR (32.0% to 15.0% on NQ) while raising clean accuracy by 18 points, at an added latency of ~16-19 s/query under live retrieval.

</details>

### 76. RAGuard: A Layered Defense Framework for Retrieval-Augmented Generation Systems Against Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2607.26339)　📅 2026-07

**关键词**：`defense`、`adversarial retriever`、`counterfactual filtering`、`adaptive poisoning`

👤 **作者**：Pushkal Kumar、Tucker Nielson、Tanish Kolhe、Shubham Zala、Vincent Li

- 🎯 **研究动机**：RAG 依赖外部语料而暴露于语料投毒，需要对抗事实型投毒的分层防御
- 🔬 **研究方法**：提出 RAGuard：第一层在合成毒文（捏造事实、矛盾、推理陷阱）上对抗微调稠密检索器降权恶意段落，第二层 Zero-Knowledge Inference Patch 对每个检索文档做 leave-one-out 解码，按移除引起的语义与输出熵变化打分，无需毒标签或真值答案
- 📌 **结论**：NQ 上 5-30% 投毒比下 ZKIP 在所有受防御配置把 ASR 压到 0.000 且 Recall@5 与干净基线差在 0.03 内；代价是每查询 k+1 次生成，并界定关键词保留毒文对 BM25 无影响的威胁边界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems ground large language models (LLMs) in external corpora, but this reliance exposes them to corpus poisoning: maliciously injected passages that manipulate retrieved evidence. We introduce RAGuard, a layered defense against \emph{factual} corpus-poisoning attacks on RAG pipelines. The first layer adversarially fine-tunes a dense retriever on synthetic poisoned documents (fabricated facts, contradictions, and reasoning traps), teaching it to downrank malicious passages before generation. The second layer, the Zero-Knowledge Inference Patch ZKIP, is a label-free, black-box filter: for each retrieved document, it performs a leave-one-out decode and scores the document by the semantic shift and output-entropy change that its removal induces. ZKIP requires no poison labels, no ground-truth answers, and no access to model internals; it compares the model's own answers under counterfactual contexts. On poisoned Natural Questions at 5--30\% poison ratios, adversarial retriever training alone reduces but does not eliminate attack success, while ZKIP drives the measured attack success rate to 0.000 in every defended configuration, keeping Recall@5 within 0.03 of the clean-corpus baseline. Supervised analyses on both Natural Questions and BEIR (NFCorpus) confirm that the counterfactual signals ZKIP relies on carry learnable poison structure. The defense costs $k{+}1$ generator passes per query ($6\times$ for $k{=}5$); we analyze batching and early-stopping approximations that reduce this overhead. We also show that keyword-preserving poisons leave lexical retrievers such as BM25 essentially unaffected, an observation that delineates the boundary of the threat model. Code, datasets, and evaluation harnesses are released for reproducibility.

</details>

### 77. When Global Gating Is Enough: Admission-Time Hubness Control in Anisotropic Vector Retrieval Systems

📄 [arXiv](https://arxiv.org/abs/2606.19692)　📅 2026-06

**关键词**：`defense`、`admission control`、`vector hubness`、`sentinel query`

👤 **作者**：Prashant Kumar Pathak、Tarun Kumar Sharma

- 🎯 **研究动机**：RAG 中向量 hubness 使单个注入文档可影响大量无关请求，已有防御用周期性反向 kNN 扫描存在暴露窗口且重复全库开销
- 🔬 **研究方法**：研究准入时控制：用哨兵查询给候选文档打分，插入前隔离 hub 型文档；在两个 10 万文档库、五个编码器上评估全局与按主题门控
- 📌 **结论**：全局门控在判定嵌入点 recall 达 1.0（有效范围 >=0.92），HotFlip 攻击 0.91、一般文档 1% 假阳性；HNSW 上仅增约 3.1% 摄入延迟，按主题门控无可靠增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vector hubness, where a few points become nearest neighbors of many queries, creates a poisoning risk in retrieval-augmented generation (RAG): one injected document can influence unrelated requests. Existing defenses use periodic reverse-kNN scans, leaving an exposure window and repeated corpus-wide work. We study admission-time control, scoring each candidate against sentinel queries and quarantining hub-like documents before insertion. Across two 100,000-document corpora, five encoders, and disjoint attacker and defender query sets, a global gate achieves recall 1.0 at the decisive embedding-space point (>=0.92 across the effective range) and 0.91 +/- 0.07 on HotFlip attacks, with 1% false positives on general documents. A per-topic gate provides no reliable benefit, consistent with anisotropy coupling local and global visibility. Thresholds are maintained incrementally, with corpus-size-independent insertion cost and amortized deletion cost. On HNSW, admission adds about 3.1% to ingestion latency, scoring remains flat to 10^6 vectors, and 1.2% of decisions flip under approximate indexing, none involving attacks. Provenance complements the gate for natural or tight-domain hubs.

</details>

### 78. BiRD: A Bidirectional Ranking Defense Mechanism for Retrieval Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2605.20123)　📅 2026-05

**关键词**：`defense`、`bidirectional ranking`、`retrieval context`、`low-latency filtering`

👤 **作者**：Chengcai Gao、Zhihong Sun、Xiaochuan Shi、Qiufeng Wang、Chao Liang

- 🎯 **研究动机**：现有 RAG 防御只关注语义相关性，忽略由排序结构定义的检索上下文，计算成本与鲁棒性难两全
- 🔬 **研究方法**：发现毒化文档的反向排名与查询正向排名显著更强对齐；BiRD 双信号框架用正向排名评语义相关性、反向排名量排序上下文一致性
- 📌 **结论**：3 数据集、3 检索器、3 LLM、2 攻击场景下最多把 PoisonedRAG ASR 降 54%、任务准确率升 56%，平均额外延迟低于 1 秒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing adoption of Retrieval-Augmented Generation (RAG) has led to a rise in adversarial attacks. Existing defenses, relying on semantic analysis or voting, face a trade-off between high computational cost and limited robustness under strong poisoning attacks. Their fundamental limitation is the exclusive focus on semantic content relevance, while neglecting the retrieval context that is critically defined by ranking structures. To this end, we investigate the bidirectional ranking behavior of poisoned and benign documents, and discover a key discriminative pattern: poisoned documents exhibit significantly stronger alignment between their backward rankings and the query's forward ranking. Capitalizing on this, we propose BiRD, a bidirectional ranking defense mechanism built upon a dual-signal framework that leverages forward ranking to assess semantic content relevance and backward ranking to quantify ranking context consistency. This design directly addresses the fundamental limitation of prior approaches, enabling simultaneous efficiency and robustness. Extensive evaluation across 3 datasets with 3 retrievers and 3 LLMs under 2 attack scenarios validates BiRD's effectiveness. Notably, BiRD reduces the attack success rate of PoisonedRAG by up to 54% while simultaneously improving task accuracy by up to 56%, with average additional latency under 1 second.

</details>

### 79. ProGRank: Probe-Gradient Reranking to Defend Dense-Retriever RAG from Corpus Poisoning

📄 [arXiv](https://arxiv.org/abs/2603.22934)　📅 2026-03　🏷 KDD 2026

**关键词**：`defense`、`probe gradient`、`training-free reranking`、`adaptive evasion`

👤 **作者**：Xiangyu Yin、Yi Qi、Chih-Hong Cheng

- 🎯 **研究动机**：RAG 语料投毒防御依赖内容过滤、辅助模型或生成器侧推理，部署复杂
- 🔬 **研究方法**：ProGRank 免训练对每个 query-passage 对施加轻微随机扰动，从小参数子集提取 probe gradient 得到表示一致性与分散风险两个不稳定信号，结合分数门重排
- 📌 **结论**：跨数据集、检索器与攻击设定提升鲁棒并保持稳健-效用权衡，在自适应规避攻击与代理检索器变体下仍有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) improves large language model applications by grounding generation in retrieved evidence, but also introduces corpus poisoning as a new attack surface. In this setting, an adversary injects or edits passages so that they enter the Top-$K$ results for target queries and influence downstream generation. Existing defences often rely on content filtering, auxiliary models, or generator-side reasoning, which complicates deployment. We propose ProGRank, a post hoc, training-free retriever-side defence for dense-retriever RAG. ProGRank stress-tests each query--passage pair under mild randomized perturbations, extracts probe gradients from a small fixed parameter subset, and derives two instability signals: representational consistency and dispersion risk. It then combines these signals with a score gate for reranking. ProGRank preserves the original passage content, requires no retraining, and supports a surrogate-based variant when the deployed retriever is unavailable. Experiments across datasets, retrievers, attacks, and retrieval-stage and end-to-end settings show that ProGRank improves robustness and maintains a favorable robustness--utility trade-off, including under adaptive evasive attacks.

</details>

### 80. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2512.24268)　📅 2025-12　🏷 AAAI 2026

**关键词**：`defense`、`retrieval-stage defense`、`document partitioning`、`token masking`

👤 **作者**：Pankayaraj Pathmanathan、Michael-Andrei Panaitescu-Liess、Cho-Yu Jason Chiang、Furong Huang

- 🎯 **研究动机**：RAG 语料投毒的防御多在生成侧，代价高且需改动生成模型
- 🔬 **研究方法**：提出两个直接作用于检索器的轻量防御：RAGPart 利用稠密检索器训练动态做文档分区缓解毒点影响，RAGMask 以定向 token 掩码下的相似度显著偏移识别可疑 token，并以可解释攻击压力测试
- 📌 **结论**：在两个基准、四种投毒策略与四个 SOTA 检索器上持续降低 ASR 并保持良性效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm to enhance large language models (LLMs) with external knowledge, reducing hallucinations and compensating for outdated information. However, recent studies have exposed a critical vulnerability in RAG pipelines corpus poisoning where adversaries inject malicious documents into the retrieval corpus to manipulate model outputs. In this work, we propose two complementary retrieval-stage defenses: RAGPart and RAGMask. Our defenses operate directly on the retriever, making them computationally lightweight and requiring no modification to the generation model. RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. In contrast, RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking. Across two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, our defenses consistently reduce attack success rates while preserving utility under benign conditions. We further introduce an interpretable attack to stress-test our defenses. Our findings highlight the potential and limitations of retrieval-stage defenses, providing practical insights for robust RAG deployments.

</details>

### 81. Secure Retrieval-Augmented Generation against Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2510.25025)　📅 2025-10

**关键词**：`defense`、`retrieval expansion`、`perplexity filtering`、`adaptive attack`

👤 **作者**：Zirui Cheng、…、Minghong Fang

- 🎯 **研究动机**：已有 RAG 投毒防御难以抵御高级攻击
- 🔬 **研究方法**：RAGuard 先扩大检索范围提高干净文本占比，再用 chunk 级困惑度过滤与文本相似度过滤检出毒文本，为非参数检测框架
- 📌 **结论**：大规模数据集实验证明其能有效检测与缓解投毒攻击，包括强自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have transformed natural language processing (NLP), enabling applications from content generation to decision support. Retrieval-Augmented Generation (RAG) improves LLMs by incorporating external knowledge but also introduces security risks, particularly from data poisoning, where the attacker injects poisoned texts into the knowledge database to manipulate system outputs. While various defenses have been proposed, they often struggle against advanced attacks. To address this, we introduce RAGuard, a detection framework designed to identify poisoned texts. RAGuard first expands the retrieval scope to increase the proportion of clean texts, reducing the likelihood of retrieving poisoned content. It then applies chunk-wise perplexity filtering to detect abnormal variations and text similarity filtering to flag highly similar texts. This non-parametric approach enhances RAG security, and experiments on large-scale datasets demonstrate its effectiveness in detecting and mitigating poisoning attacks, including strong adaptive attacks.

</details>

### 82. Defending Against Knowledge Poisoning Attacks During Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2508.02835)　📅 2025-08

**关键词**：`defense`、`FilterRAG`、`text separability`、`knowledge-source filtering`

👤 **作者**：Kennedy Edemacu、Vinay M. Shashidhar、Micheal Tuape、Dan Abudu、Beakcheol Jang、Jong Wook Kim

- 🎯 **研究动机**：PoisonedRAG 等知识投毒可误导 RAG 生成攻击者指定回答，缺乏知识源过滤防御
- 🔬 **研究方法**：提出区分对抗与干净文本的可分离性属性，据此设计 FilterRAG 与 ML-FilterRAG 过滤知识源中的对抗文本
- 📌 **结论**：基准数据集上有效缓解攻击，性能接近原始 RAG 系统

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has emerged as a powerful approach to boost the capabilities of large language models (LLMs) by incorporating external, up-to-date knowledge sources. However, this introduces a potential vulnerability to knowledge poisoning attacks, where attackers can compromise the knowledge source to mislead the generation model. One such attack is the PoisonedRAG in which the injected adversarial texts steer the model to generate an attacker-chosen response to a target question. In this work, we propose novel defense methods, FilterRAG and ML-FilterRAG, to mitigate the PoisonedRAG attack. First, we propose a new property to uncover distinct properties to differentiate between adversarial and clean texts in the knowledge data source. Next, we employ this property to filter out adversarial texts from clean ones in the design of our proposed approaches. Evaluation of these methods using benchmark datasets demonstrate their effectiveness, with performances close to those of the original RAG systems.

</details>

### 83. TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2501.00879)　📅 2025-01

**关键词**：`defense`、`cluster filtering`、`LLM self-assessment`、`training-free defense`

👤 **作者**：Huichi Zhou、…、Emine Yilmaz

- 🎯 **研究动机**：RAG 易受 corpus poisoning 攻击，性能可被严重破坏
- 🔬 **研究方法**：TrustRAG 两阶段免训练防线：cluster filtering 检测攻击模式，再借 LLM 自评估检出恶意文档并消解不一致
- 📌 **结论**：即插即用模块显著提升检索准确率、效率与抗攻击能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user queries. These systems, however, remain susceptible to corpus poisoning attacks, which can severely impair the performance of LLMs. To address this challenge, we propose TrustRAG, a robust framework that systematically filters malicious and irrelevant content before it is retrieved for generation. Our approach employs a two-stage defense mechanism. The first stage implements a cluster filtering strategy to detect potential attack patterns. The second stage employs a self-assessment process that harnesses the internal capabilities of LLMs to detect malicious documents and resolve inconsistencies. TrustRAG provides a plug-and-play, training-free module that integrates seamlessly with any open- or closed-source language model. Extensive experiments demonstrate that TrustRAG delivers substantial improvements in retrieval accuracy, efficiency, and attack resistance.

</details>
### Evidence Verification & Post-Retrieval Filtering

### 84. ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains

📄 [arXiv](https://arxiv.org/abs/2608.25487)　📅 2026-08

**关键词**：`defense`、`evidence reliability`、`deceptive misinformation`、`multi-hop verification`、`misinformation injection`、`triple reliability`

👤 **作者**：Jinpu Jiang、…、Chunguo Wu

- 🎯 **研究动机**：multi-hop RAG 中单条高相关虚假信息即可误导推理链，现有方法缺细粒度可靠性评估
- 🔬 **研究方法**：ReliableRAG 把文档拆为 triple，联合相关性与可信度筛选证据，自回归构建稳健推理链
- 📌 **结论**：三个多跳 QA 数据集上优于既有方法，提升虚假信息注入下的事实可靠性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has emerged as a powerful architecture for Question Answering (QA) by integrating external information into Large Language Models (LLMs). However, false, inaccurate, and misleading information in news and social media poses a serious challenge to real-world RAG systems, especially in multi-hop QA, where complex multi-step reasoning can be misled by even a single deceptive misinformation segment in the retrieved documents. Existing approaches mainly rely on implicit alignment or explicit regulation, but their limited ability to assess fine-grained information reliability makes them vulnerable to deceptive misinformation that is semantically relevant to the question yet factually incorrect, leading to erroneous answers. To address this limitation, we propose ReliableRAG, which, to the best of our knowledge, is the first reliability-driven framework that mitigates deceptive misinformation in multi-hop QA through fine-grained evaluation of individual triples. ReliableRAG first extracts information segments from source documents and represents them as structured triples. It then quantifies triple reliability by combining query-triple semantic relevance with triple credibility, retaining only the top-$K$ reliable and non-redundant triples. Based on these refined triples, ReliableRAG autoregressively constructs robust reasoning chains to consolidate trustworthy evidence and filter deceptive misinformation, producing accurate answers faithful to reliable information. Experiments on three multi-hop QA datasets show that ReliableRAG outperforms existing methods, substantially improving the factual reliability and robustness of RAG systems under deceptive misinformation injection.

</details>

### 85. Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution

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

### 86. COMA: A Compositional Misleading Attack Class on Security-RAG, and a Causal Counterfactual Defense

📄 [arXiv](https://arxiv.org/abs/2608.17960)　📅 2026-08

**关键词**：`defense`、`RAG poisoning`、`knowledge corruption`、`retrieval manipulation`

👤 **作者**：Chinmay Gondhalekar、Urjitkumar Patel

- 🎯 **研究动机**：Security-RAG 中每篇文档都真实、无指令、无矛盾时，仍可能让 copilot 正确诊断漏洞却推荐留漏洞的修复
- 🔬 **研究方法**：定义 COMA 攻击类：action-corruption 把正确诊断引向劣质修复、verdict-flip 经不可判定可达链动摇可利用性判定；CCD 防御度量每篇检索文档的留一因果影响并标记影响集中于低信文档的回答
- 📌 **结论**：action-corruption 对全部五个模型（含前沿推理模型）每次运行生效并在真实 CVE-2021-33813 上验证；CCD 零误报定位攻击文档，聚合变体可抓影响扩散的自适应攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Every document a security copilot retrieves can be true, instruction-free, and non-contradictory --- and the copilot can still be driven to assess a critical, exploitable vulnerability correctly and then recommend a remediation that leaves it open. We study this failure in retrieval-augmented generation (RAG) backing analyst-facing copilots in Security Operations Centers, and identify a class of attacks, \emph{\compmis{}} (COMA), in which every adversarial document is factually correct, instruction-free, non-contradictory, and distributionally benign --- yet the answer is misled by their \emph{composition}. We realize \compmis{} through \emph{action-corruption}, which steers a correctly-diagnosed vulnerability toward an inferior remediation, and \emph{verdict-flip}, which destabilizes the exploitability verdict via an undecidable reachability chain. Action-corruption bites all five tested models --- including frontier reasoning models --- on every run, on two synthetic domains and a real CVE (CVE-2021-33813); verdict-flip bites stochastically, decreasing with model capability but never vanishing. A single principle governs both: the attack succeeds when the disambiguating fact must be \emph{inferred} rather than \emph{read}. We propose \ccd{} (Causal Counterfactual Defense), an audit that measures the leave-one-out causal influence of each retrieved document and flags answers whose influence concentrates on low-trust documents. \ccd{} localizes the attack to attacker-controlled documents with no false positives on four benign multi-document controls; an adaptive influence-spreading adversary is caught by an \emph{aggregate} variant. We release attack seeds and a \ccd{} reference implementation.

</details>

### 87. Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents

📄 [arXiv](https://arxiv.org/abs/2608.17153)　📅 2026-08

**关键词**：`defense`、`analysis`、`evidence-access control`、`System 2 gating`、`RAG Agent`、`System 2 reasoning`

👤 **作者**：Mehrdad Ghassabi

- 🎯 **研究动机**：LLM 可能正确检测文档含错误信息却仍受其影响；Cordon Principle 严格隔离又带来大量计算开销
- 🔬 **研究方法**：提出精化原则——只有具备 System 2 深思推理能力的 agent 才可访问不可信文档；构建量化误信息检测与下游影响之差的指标并对比推理与标准模型
- 📌 **结论**：推理能力模型对损坏证据鲁棒得多，无需 Cordon 式严格隔离，为安全 RAG 设计提供更实用基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has significantly enhanced the performance of large language models (LLMs), yet these systems remain vulnerable to knowledge-poisoning attacks, in which misinformation in retrieved documents can influence the model's final outputs. Notably, an LLM may correctly detect that a document contains incorrect information while nevertheless being influenced by it. Prior work has addressed this vulnerability through the Cordon Principle, which prevents models responsible for final answer synthesis from directly accessing raw evidence. Although effective, this strict isolation can introduce substantial computational overhead. In this work, we propose a refined security principle: only agents capable of deliberative System 2 reasoning may access untrusted documents. To evaluate this principle, we introduce novel metrics that quantify the discrepancy between misinformation detection and downstream influence. We then empirically compare state-of-the-art reasoning language models with standard language models across these metrics. Our results show that reasoning-capable models are substantially more robust to corrupted evidence, without requiring the strict isolation imposed by the Cordon Principle. These findings provide empirical support for our refined principle and suggest a more practical foundation for secure RAG system design.

</details>

### 88. PurifAI: Detecting and Fixing Search-Induced Distortions in Web-Augmented LLMs

🌐 [Project](https://doi.org/10.1145/3805712.3809751)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`defense`、`web evidence poisoning`、`knowledge conflict`、`cache purification`、`web-augmented LLM`、`search distortion`

- 🎯 **研究动机**：检索到的web证据会诱发知识冲突与扭曲，缓存还会放大污染
- 🔬 **研究方法**：PurifAI检测并修复search-induced扭曲，净化证据与缓存
- 📌 **结论**：降低web增强LLM的中毒与幻觉影响

### 89. Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention

📄 [arXiv](https://arxiv.org/abs/2602.04711)　📅 2026-02

**关键词**：`defense`、`sparse document attention`、`cross-document interaction`、`inference-time patch`

👤 **作者**：Sagie Dekel、Moshe Tennenholtz、Oren Kurland

- 🎯 **研究动机**：标准因果注意力允许毒文档与良性证据跨文档交互，助长 RAG 语料知识投毒
- 🔬 **研究方法**：SDAG 块稀疏注意力机制禁止检索文档间交叉注意，仅需推理时对 attention mask 的最小改动
- 📌 **结论**：多种 RAG 攻击策略下显著优于标准因果注意力，与 SOTA RAG 防御集成后性能统计显著更优

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval Augmented Generation (RAG) is a highly effective paradigm for keeping LLM-based responses up-to-date and reducing the likelihood of hallucinations. Yet, RAG was recently shown to be quite vulnerable to corpus knowledge poisoning: an attacker injects misleading documents to the corpus to steer an LLM's output to an undesired response. We argue that the standard causal attention mechanism in LLMs enables harmful cross-document interactions, specifically in cases of attacks. Accordingly, we introduce a novel defense approach for RAG: Sparse Document Attention RAG (SDAG). This is a block-sparse attention mechanism that disallows cross-attention between retrieved documents. SDAG requires a minimal inference-time change to the attention mask. We present an empirical evaluation of LLM-based question answering (QA) with a variety of attack strategies on RAG. We show that our SDAG method substantially outperforms the standard causal attention mechanism. We further demonstrate the clear merits of integrating SDAG with state-of-the-art RAG defense methods. Specifically, the integration results in performance that is statistically significantly better than the state-of-the-art.

</details>

### 90. Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems

📄 [arXiv](https://arxiv.org/abs/2511.01268) · 🌐 [Project](https://www.acsac.org/2025/program/final/s73.html)　📅 2025-11

**关键词**：`defense`、`post-retrieval filtering`、`lightweight classifier`、`resource efficiency`

👤 **作者**：Minseok Kim、Hankook Lee、Hyungjoon Koo

- 🎯 **研究动机**：让 LLM 逐段检查检索内容或微调鲁棒检索器的防御计算开销过大
- 🔬 **研究方法**：RAGDefender 在检索后阶段用轻量机器学习检测过滤对抗内容，无需额外模型训练或推理
- 📌 **结论**：多模型场景稳定优于 SOTA：毒文档为良性四倍时把 Gemini 的 ASR 从 0.89 降至 0.02（RobustRAG 为 0.69、Discern-and-Answer 为 0.24）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are reshaping numerous facets of our daily lives, leading widespread adoption as web-based services. Despite their versatility, LLMs face notable challenges, such as generating hallucinated content and lacking access to up-to-date information. Lately, to address such limitations, Retrieval-Augmented Generation (RAG) has emerged as a promising direction by generating responses grounded in external knowledge sources. A typical RAG system consists of i) a retriever that probes a group of relevant passages from a knowledge base and ii) a generator that formulates a response based on the retrieved content. However, as with other AI systems, recent studies demonstrate the vulnerability of RAG, such as knowledge corruption attacks by injecting misleading information. In response, several defense strategies have been proposed, including having LLMs inspect the retrieved passages individually or fine-tuning robust retrievers. While effective, such approaches often come with substantial computational costs. In this work, we introduce RAGDefender, a resource-efficient defense mechanism against knowledge corruption (i.e., by data poisoning) attacks in practical RAG deployments. RAGDefender operates during the post-retrieval phase, leveraging lightweight machine learning techniques to detect and filter out adversarial content without requiring additional model training or inference. Our empirical evaluations show that RAGDefender consistently outperforms existing state-of-the-art defenses across multiple models and adversarial scenarios: e.g., RAGDefender reduces the attack success rate (ASR) against the Gemini model from 0.89 to as low as 0.02, compared to 0.69 for RobustRAG and 0.24 for Discern-and-Answer when adversarial passages outnumber legitimate ones by a factor of four (4x).

</details>

### 91. Through the Stealth Lens: Attention-Aware Defenses Against Poisoning in RAG

📄 [arXiv](https://arxiv.org/abs/2506.04390) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61228)　📅 2025-06　🏷 ICML 2026

**关键词**：`defense`、`RAG poisoning`、`stealth`、`attention filtering`、`backdoor defense`、`empirical evaluation`

👤 **作者**：Sarthak Choudhary、Nils Palumbo、Ashish Hooda、Krishnamurthy Dj Dvijotham、Somesh Jha

- 🎯 **研究动机**：RAG 投毒攻击本不要求隐蔽，可被可靠检测，且缺乏形式化的隐蔽性度量
- 🔬 **研究方法**：形式化可区分性安全博弈，基于注意力权重提出 NPAS 与轻量 Attention-Variance Filter 标记异常段落，并构造自适应攻击
- 📌 **结论**：鲁棒性比基线防御高约 20%；自适应隐蔽攻击最高 35% 成功率，揭示真正隐蔽投毒之难

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems are vulnerable to attacks that inject poisoned passages into the retrieved context, even at low corruption rates. We show that existing attacks are not designed to be stealthy, allowing reliable detection and mitigation. We formalize a distinguishability-based security game to quantify stealth for such attacks. If a few poisoned passages control the response, they must bias the inference process more than the benign ones, inherently compromising stealth. This motivates analyzing intermediate signals of LLMs, such as attention weights, to approximate the influence of different passages on the response. Leveraging attention weights, we introduce the $\textbf{Normalized Passage Attention Score}$ (NPAS) and a lightweight $\textbf{Attention-Variance Filter}$ (AV Filter) that flags anomalous passages. Our method improves robustness, yielding up to $\sim$ $\textbf{20%}$ higher accuracy than baseline defenses. We also develop adaptive attacks that attempt to conceal such anomalies, achieving up to $\textbf{35%}$ success rate and underscoring the challenges of achieving true stealth in poisoning RAG systems.

</details>
### Information-Flow Control, Robust Aggregation & Certification

### 92. RAGSentinel: Certifiable Geometric Consensus for Robust Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2608.23965)　📅 2026-08

**关键词**：`defense`、`RAG poisoning`、`geometric consensus`、`certified robustness`

👤 **作者**：Yueyang Quan、Anjun Gao、Yufei Xia、Minghong Fang、Zhuqing Liu

- 🎯 **研究动机**：检索后防御依赖指令遵循、参数知识或文本一致性，均可被自适应攻击绕过
- 🔬 **研究方法**：RAGSentinel 免训练：代理 encoder 测 query 条件隐状态偏移、移除共享主题方向，以多数共识过滤离群文档
- 📌 **结论**：诚实多数与表示分离条件下可证明恢复无毒上下文，多个数据集与 LLM 家族上保持低 ASR

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) improves the factuality of large language models by grounding responses in external documents, but it also exposes a critical security vulnerability: adversarial documents injected into the knowledge database can enter the context window and steer the model toward targeted incorrect answers. Existing post-retrieval defenses rely on instruction following, parametric knowledge, or text-level consistency, all of which can be imitated or optimized against by adaptive attackers. We propose RAGSentinel, a training-free, label-free defense for black-box RAG systems. RAGSentinel uses a surrogate encoder to measure query-conditioned hidden-state shifts induced by retrieved documents, removes shared topic directions, and filters poisoned documents as geometric outliers from a robust majority consensus. We prove that, under an honest-majority assumption and a representation-level separation condition, RAGSentinel exactly recovers a poison-free majority-sized context. Experiments across three question-answering datasets, three LLM families, and multiple poisoning attacks show that RAGSentinel consistently achieves low attack success rates while preserving competitive accuracy and remaining effective against adaptive attacks with full pipeline knowledge.

</details>

### 93. Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control

📄 [arXiv](https://arxiv.org/abs/2605.26754)　📅 2026-05

**关键词**：`defense`、`RAG poisoning`、`information-flow control`、`isolation`

👤 **作者**：Zhe Yu、…、Meng Han

- 🎯 **研究动机**：检测到毒化证据不等于不执行——存在 monitoring-control gap，模型能发现矛盾仍按毒化主张行动
- 🔬 **研究方法**：提出 Cordon 原则（能做最终合成的 agent 不得接触不可信自然语言证据）；CORDON-MAS 把证据抽取、跨源审计与答案合成分离为非对称记忆权限的 agent，架构化执行该原则
- 📌 **结论**：五个 BEIR 数据集上较无防御 RAG 降低 ASR 92.4%，把 RAG 投毒从检测问题重构为信息流控制问题

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) increasingly underpins high-stakes applications, yet remains vulnerable to Confundo-style poisoning where adversarially optimized documents manipulate generated outputs. Existing defenses assume that detecting poisoned evidence prevents harm. We show this assumption is incorrect: models exhibit a monitoring-control gap -- they can detect contradictions in retrieved evidence yet still act on poisoned claims. We introduce the Cordon Principle -- no agent capable of final synthesis may access untrusted natural-language evidence -- and realize it through CORDON-MAS, a compartmentalized framework that enforces this principle architecturally by separating evidence extraction, cross-source audit, and answer synthesis into agents with asymmetric memory privileges. Across five BEIR datasets, CORDON-MAS reduces attack success rate by 92.4\% relative to undefended RAG. This reframes RAG poisoning from a detection problem to an information-flow control problem.

</details>

### 94. PRA-RAG: Provably Robust Aggregation in Retrieval-Augmented Generation against Retrieval Corruption

📄 [arXiv](https://arxiv.org/abs/2607.00012)　📅 2026-05

**关键词**：`defense`、`robust aggregation`、`geometric subset`、`certified bound`

👤 **作者**：Xue Tan、…、Jun Dai

- 🎯 **研究动机**：已有 RAG 防御缺乏理论鲁棒性保证，LLM 对检索内容了解有限时表现不可靠
- 🔬 **研究方法**：提出 PRA-RAG：采样多个检索文本组合，利用嵌入空间几何结构识别鲁棒子集并导出稳定聚合表示，给出被毒化内容影响上界的理论界
- 📌 **结论**：多基准与 RAG 架构上把 ASR 降至最低 1% 同时保持 71% 准确率，显著超过代表性 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) enhances Large Language Models (LLMs) by incorporating external knowledge, effectively mitigating their inherent knowledge limitations. However, RAG remains vulnerable to poisoning attacks that manipulate retrieved texts to mislead model outputs. Existing defense mechanisms often lack theoretical robustness guarantees and perform unreliably when the LLM has limited knowledge of the retrieved content. In this work, we propose PRA-RAG, a provably robust retrieval aggregation algorithm designed to defend against poisoning attacks on retrieved texts. PRA-RAG samples multiple combinations of retrieved texts and utilizes geometric structures in the embedding space to identify a robust subset, from which a stable aggregated representation is derived. We provide theoretical bounds on the maximum impact of poisoned retrieved content and establish a quantitative measure of RAG's robustness. Experiments across multiple benchmarks and RAG architectures demonstrate that PRA-RAG reduces the attack success rate to as low as 1% while maintaining an accuracy of 71%, significantly outperforming representative state-of-the-art methods.

</details>

### 95. Certifiably Robust RAG against Retrieval Corruption

📄 [arXiv](https://arxiv.org/abs/2405.15556) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2024-05　🏷 SaTML 2026

**关键词**：`defense`、`RAG certification`、`bounded corruption`、`secure aggregation`、`RAG corruption`、`isolate-then-aggregate`

👤 **作者**：Chong Xiang、Tong Wu、Zexuan Zhong、David Wagner、Danqi Chen、Prateek Mittal

- 🎯 **研究动机**：RAG 易受检索腐化攻击，注入恶意段落即导致错误回答，缺乏可认证防御
- 🔬 **研究方法**：RobustRAG 采用 isolate-then-aggregate：把段落隔离分组分别生成回答，再用 keyword 与 decoding 两种算法安全聚合
- 📌 **结论**：首个可认证鲁棒的 RAG 防御，面对有界数量恶意段落注入仍能证明回答质量下界

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. We propose RobustRAG, the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output. To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses. Notably, RobustRAG achieves certifiable robustness: for certain queries in our evaluation datasets, we can formally certify non-trivial lower bounds on response quality -- even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages. We evaluate RobustRAG on the tasks of open-domain question-answering and free-form long text generation and demonstrate its effectiveness across three datasets and three LLMs.

</details>
### Multimodal, GraphRAG & Collaborative Defense

### 96. DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption

📄 [arXiv](https://arxiv.org/abs/2608.16536)　📅 2026-08

**关键词**：`defense`、`adversarial robustness`、`VLM safety`、`data poisoning`、`M-RAG`、`dynamic soft prompt`

👤 **作者**：Chang Liu、…、Bin Xiao

- 🎯 **研究动机**：M-RAG 防御集中于查询时（辅助检测器、重排、特征一致性），推理开销大且难泛化到未见攻击
- 🔬 **研究方法**：DSPrompt 在冻结检索器各层插入可学习软 prompt（浅到深长度调度），动态 min-max 训练：在线攻击者持续构造硬对抗文档，防御者将其推出 top-k 同时保良性排序与多样性
- 📌 **结论**：四个基准、三种投毒攻击下大幅降低 ASR 与投毒检索率，检索效用近无损，额外参数少于 1% 且零逐查询开销

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Retrieval Augmented Generation (M-RAG) is increasingly vulnerable to adversarial attacks where malicious data are crafted to produce embeddings that align with benign entries in the vector space, deceiving retrieval and inducing harmful outputs. Existing defenses primarily operate at query time, relying on auxiliary detectors, similarity re-ranking, or feature-consistency checks. However, these approaches suffer from non-trivial inference overhead, generalize poorly to unseen attack strategies, and often assume specific attack distributions. To address this, we propose DSPrompt, a Dynamic Soft Prompt defense framework that directly reshapes the retriever's embedding semantics, without modifying the retrieval pipeline. It inserts few learnable soft prompts into each layer of the visual and textual encoders of a frozen retriever, utilizing a shallow-to-deep length schedule that is adaptive to the capacity in the model layers. These prompts are trained under a dynamic min-max scheme: an online multimodal attacker continually crafts hard adversarial documents against the current retriever, while the defender is updated to push such documents out of the top-k while preserving the ranking and diversity of benign evidence. Because the defended encoder can be pre-computed and indexed exactly as in standard dense retrieval, DSPrompt incurs no additional per-query optimization and introduces fewer than 1% additional parameters. Extensive experiments across four benchmarks and three representative poisoning attacks show that DSPrompt substantially reduces the attack success rate and poison retrieval rate while maintaining near-lossless retrieval utility and generation fidelity, consistently outperforming existing defense baselines at a fraction of their computational cost.

</details>

### 97. RADAR: Defending RAG Dynamically against Retrieval Corruption

📄 [arXiv](https://arxiv.org/abs/2605.22041) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62567)　📅 2026-05　🏷 ICML 2026

**关键词**：`defense`、`attack`、`GraphRAG poisoning`、`dynamic defense`、`graph energy`、`LLM agent security`

👤 **作者**：Ziyuan Chen、…、Tieniu Tan

- 🎯 **研究动机**：动态 web 搜索下 RAG 面临演化威胁，静态防御难以应对且存档原始历史文档存储成本高
- 🔬 **研究方法**：RADAR 把可靠上下文选择建模为图能量最小化问题经 Max-Flow Min-Cut 精确求解，贝叶斯记忆节点递归更新信念而非存档原文
- 📌 **结论**：在新动态数据集上以最小存储开销获得优于基线的鲁棒性与响应质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While RAG systems are increasingly deployed in dynamic web search, temporal volatility amplifies their vulnerability to adversarial attacks. Existing static-oriented defenses struggle to handle evolving threats and incur prohibitive storage costs in dynamic settings. We propose RADAR, a framework that models reliable context selection as a graph-based energy minimization problem, solved exactly via Max-Flow Min-Cut. By incorporating a Bayesian memory node, RADAR recursively updates a belief state instead of archiving raw historical documents, effectively balancing stability against attacks with adaptability to genuine knowledge shifts. Experiments on a novel dynamic dataset show that RADAR achieves superior robustness and response quality with minimal storage overhead compared to the baselines.

</details>

### 98. Defense Against Knowledge Poisoning Attack on GraphRAG

🎓 [Official](https://aclanthology.org/2026.acl-short.47/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`GraphRAG poisoning`、`multi-hop verification`、`local pruning`、`RAG security`、`data poisoning`

👤 **作者**：Havva Alizadeh Noughabi、Fattane Zarrinkalam、Ali Dehghantanha

- 🎯 **研究动机**：GraphRAG 语料级知识中毒可注入虚假实体关系、破坏查询子图并诱导错误答案，缺乏防御
- 🔬 **研究方法**：HoG-GRAG 在检索器与生成器间设防御层：把多跳问题分解为有序子查询、逐跳监测中毒导致的不一致、局部修剪受损实体关系并只补最小缺失证据
- 📌 **结论**：多跳数据集与多种 GraphRAG 配置上恢复大部分被攻击损失的性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

GraphRAG augments large language models with structured knowledge graphs, enabling graph-based context selection and a more integrated view of the knowledge space. However, recent work shows that GraphRAG exposes a new attack surface: corpus-level knowledge poisoning can inject spurious entities and relationships during graph construction, corrupting query-specific subgraphs and steering the generator toward incorrect answers. We propose Hop-wise Guard for GraphRAG (HoG-GRAG), a defense layer between retriever and generator that decomposes multi-hop questions into ordered subqueries, monitors hop-wise execution for poisoning-induced inconsistencies, and locally repairs the retrieved subgraph by pruning compromised entities and relationships and adding only minimal missing evidence. Experiments on multi-hop datasets and multiple GraphRAG configurations show that HoG-GRAG recovers a large fraction of the lost performance. The code is available at https://github.com/CyberScienceLab/HoG-GRAG.

</details>
### Pipeline & Architecture Analysis

### 99. Beyond the Editing Canvas: Evidence Divergence in OOXML-to-LLM Ingestion

📄 [arXiv](https://arxiv.org/abs/2608.25880)　📅 2026-08

**关键词**：`analysis`、`attack`、`ingestion contract`、`evidence fork`、`extractor differential`、`OOXML ingestion`

👤 **作者**：Side Liu、Jiangpeng Liu、Jinwen Xin、Guojun Peng、Jiang Ming

- 🎯 **研究动机**：LLM 流水线把 OOXML 文档当一级证据，隐含假设 Office 画布所见与模型所取一致，该假设可被破坏
- 🔬 **研究方法**：遍历规范挖掘 21 类 evidence forks，用画布不可见的 task-relevant trap 测试 4 个原生 API 与 13 个提取工具
- 📌 **结论**：4 个 API 在 48%-76% 试验中返回 trap，13 个工具全部受至少一种机制影响，暴露由提取器配置决定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM pipelines increasingly ingest Office Open XML (OOXML) documents (Word, Excel, and PowerPoint files) as first-class evidence in financial, compliance, and retrieval-augmented workflows, implicitly assuming semantic integrity: that the evidence consumed by the model matches the content shown in the Microsoft Office suite editing canvas. We show that this assumption can fail in OOXML-to-LLM pipelines. The same specification-valid OOXML file can yield one evidentiary view in Microsoft Office and another when extracted for an LLM. Each view is treated as authoritative by its consumer, a condition we call plural ground truth. The ingestion contract rarely states which view and semantic roles become model evidence or preserves how that evidence was derived. We call the specification-grounded OOXML constructions that induce such divergence evidence forks. We systematically traverse and mine the OOXML specification and confirm 21 evidence forks across Excel, Word, and PowerPoint, spanning six dimensions of view construction. All 13 tools in our extraction panel emit evidence from at least one fork. We test four native-ingestion LLM APIs and seven web chatbots. Each test document carries a trap: a task-relevant fact exposed by extraction but not shown in Office. Across this 21-mechanism evaluation, the four APIs return the trap in 48--76% of trials. For 20 of 21 mechanisms, at least one of the eleven interfaces returns the trap. Our measurements further show that exposure is shaped upstream of the model by the ingestion path and extractor configuration. A source-level survey of sixteen popular open-source LLM projects further shows that default OOXML ingestion paths concentrate on affected extractor families.

</details>

### 100. Influence Factors on RAG Poisoning

📄 [arXiv](https://arxiv.org/abs/2606.12469)　📅 2026-06

**关键词**：`analysis`、`RAG poisoning`、`factorial study`、`system configuration`

👤 **作者**：Pedro Pereira、Eva Maia、Isabel Praça、Adrien Bécue

- 🎯 **研究动机**：RAG 投毒脆弱性归因于哪个组件尚缺系统证据
- 🔬 **研究方法**：432 配置的全因子实验，分析数据集、检索器类型、检索深度、库构成、分块策略与生成模型对检索级/生成级指标的影响
- 📌 **结论**：检索器架构、数据集与检索深度是暴露度最强因子；稠密与图检索器比 BM25 更鲁棒，更深检索更易召回毒段；跨库复制毒内容放大攻击、增加干净源可缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time. However, this reliance on retrieved content introduces vulnerabilities to poisoning attacks, in which adversarial documents can manipulate both the retrieval process and the generated outputs. This paper investigates poisoning robustness in RAG through a full factorial experimental study covering 432 configurations. We analyze the impacts of dataset, retriever type, retrieval depth, database composition, chunking strategy, and generator model on retrieval-level and generation-level metrics. The results show that retriever architecture, dataset, and retrieval depth are the strongest factors affecting poisoning exposure, while generator choice and database composition have a major impact on downstream attack success. Dense and graph-based retrievers generally improve robustness relative to BM25, whereas larger retrieval depth increases the likelihood of retrieving poisoned passages. We further show that replicating poisoned content across multiple databases amplifies adversarial influence, while additional clean sources can mitigate it. These findings highlight that poisoning vulnerability in RAG is not attributable to a single component, but instead arises from the interaction of retrieval, generation, and knowledge-base configuration.

</details>

### 101. When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines

📄 [arXiv](https://arxiv.org/abs/2606.11265)　📅 2026-06

**关键词**：`analysis`、`RAG poisoning`、`chunking`、`reranking`

👤 **作者**：Xi Nie、Hongwei Li、Shenghao Wu、Mingxuan Li、Jiachen Li、Wenbo Jiang

- 🎯 **研究动机**：已有 RAG 语料投毒研究在简化检索设定下评估，真实多阶段管线（分块、稠密检索、重排、生成）下攻击是否有效未知
- 🔬 **研究方法**：发现检索粒度失配是失败主因并提出 CRCP：联合优化检索相关性、重排一致性与分块边界鲁棒性，显式建模分块变换生成局部自足的对抗段落
- 📌 **结论**：现有投毒方法对分块大小与重排策略高度敏感而大幅退化，CRCP 在真实管线上保持显著更高 ASR；RAG 投毒应作为多阶段检索一致性问题研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate downstream model outputs through malicious knowledge injection. Existing studies mainly evaluate poisoning under simplified retrieval settings, overlooking practical RAG pipelines involving document chunking, dense retrieval, reranking, and grounded generation. In this paper, we revisit corpus poisoning under realistic multi-stage retrieval pipelines and show that many existing attacks substantially degrade after reranking despite achieving high retrieval-stage relevance. We identify retrieval granularity mismatch as a key reason for this failure: document-level adversarial signals are often fragmented during chunking, while rerankers favor locally coherent and answer-bearing passages rather than globally optimized semantic similarity. Based on this observation, we propose Chunk-aware and Rerank-Consistent Poisoning (CRCP), a poisoning framework that jointly optimizes retrieval relevance, reranker consistency, and chunk-boundary robustness. CRCP explicitly models chunking transformations during optimization to generate locally self-contained adversarial passages that remain effective under varying chunking configurations. Experiments on standard RAG benchmarks with multiple retrievers and rerankers show that existing poisoning methods are highly sensitive to chunk size and reranking strategies, whereas CRCP achieves substantially higher attack success rates and stronger robustness across realistic retrieval pipelines. Our findings highlight an important realism gap in current RAG security evaluation and suggest that poisoning in modern RAG systems should be studied as a multi-stage retrieval consistency problem rather than a retrieval-only problem.

</details>

### 102. Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning

📄 [arXiv](https://arxiv.org/abs/2605.05632)　📅 2026-05

**关键词**：`analysis`、`RAG architecture`、`contradiction handling`、`behavior taxonomy`

👤 **作者**：Samuel Korn

- 🎯 **研究动机**：RAG 投毒攻击几乎只在 vanilla 管线评估，专为冲突信息设计的架构未被对抗性矛盾测试
- 🔬 **研究方法**：在 921 个 NQ 问答对上以受控单文档投毒比较 vanilla、agentic、MADAM-RAG 与 RLM 四种架构，含朴素注入与元认知框架攻击 CorruptRAG-AK
- 📌 **结论**：clean 准确率均约 92% 时 ASR 从 81.9%（vanilla）到 24.4%（RLM）相差近 58 个百分点，优势主要来自内容推理阶段的对抗框架；MADAM-RAG 即使检测到矛盾也难解决（clean 上 41.4% 不回答）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems are vulnerable to knowledge base poisoning, yet existing attacks have been evaluated almost exclusively against vanilla retrieve-then-generate pipelines. Architectures designed to handle conflicting retrieved information - multi-agent debate, agentic retrieval, recursive language models - remain untested against adversarially optimized contradictions. We evaluate four RAG architectures (vanilla RAG, agentic RAG, MADAM-RAG, and Recursive Language Models) under controlled single-document (N=1) poisoning on 921 Natural Questions QA pairs, comparing a clean baseline, naive injection, and CorruptRAG-AK - an adversarial attack whose meta-epistemic framing targets credibility assessment. Architecture is a high-impact variable in adversarial robustness: under CorruptRAG-AK, attack success rates range from 81.9% (vanilla) to 24.4% (RLM) - a spread of nearly 58 percentage points across architectures with comparable clean accuracy (~92%). Decomposing this gap, once the poisoned document is retrieved, adversarial framing - not retrieval optimization - drives the majority of CorruptRAG-AK's advantage for three of four architectures, localizing the cross-architecture vulnerability at the content-reasoning stage. Our MADAM-RAG reimplementation shows the highest apparent contradiction detection rate, though our LLM judge over-identifies this behavior (~48.5% precision), so reported rates are upper bounds. Regardless of detection, MADAM-RAG cannot resolve contradictions reliably, producing a 41.4% non-answer rate even on clean inputs - though implementation divergences from the original may contribute. We introduce a seven-category behavioral taxonomy capturing contradiction detection, hedging, and failure modes beyond binary accuracy. Code, data, and analysis notebooks are publicly available.

</details>

### 103. Quantifying Document Impact in RAG-LLMs

📄 [arXiv](https://arxiv.org/abs/2601.05260)　📅 2025-10

**关键词**：`analysis`、`document influence`、`partial information decomposition`、`poison diagnosis`

👤 **作者**：Armin Gerami、Kazem Faghih、Ramani Duraiswami

- 🎯 **研究动机**：RAG 评测缺乏量化单篇检索文档对最终输出贡献的指标
- 🔬 **研究方法**：基于 Partial Information Decomposition 提出 Influence Score，度量每篇检索文档对生成回复的影响
- 📌 **结论**：投毒模拟中 86% 案例正确把恶意文档判为最具影响力；仅用 IS 高分文档重建的回复与原回复更相似

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval Augmented Generation (RAG) enhances Large Language Models (LLMs) by connecting them to external knowledge, improving accuracy and reducing outdated information. However, this introduces challenges such as factual inconsistencies, source conflicts, bias propagation, and security vulnerabilities, which undermine the trustworthiness of RAG systems. A key gap in current RAG evaluation is the lack of a metric to quantify the contribution of individual retrieved documents to the final output. To address this, we introduce the Influence Score (IS), a novel metric based on Partial Information Decomposition that measures the impact of each retrieved document on the generated response. We validate IS through two experiments. First, a poison attack simulation across three datasets demonstrates that IS correctly identifies the malicious document as the most influential in $86\%$ of cases. Second, an ablation study shows that a response generated using only the top-ranked documents by IS is consistently judged more similar to the original response than one generated from the remaining documents. These results confirm the efficacy of IS in isolating and quantifying document influence, offering a valuable tool for improving the transparency and reliability of RAG systems.

</details>
### Adaptive Defense Limits

### 104. Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval

📄 [arXiv](https://arxiv.org/abs/2608.16044)　📅 2026-08

**关键词**：`analysis`、`RAG poisoning`、`coordinated poisoning`、`admission defense`

👤 **作者**：Prashant Kumar Pathak、Tarun Kumar Sharma

- 🎯 **研究动机**：摄入期过滤是 RAG 投毒的热门防御，协调攻击者能否绕过未知
- 🔬 **研究方法**：证明注入少量各自平凡的文档可合围目标查询并夺走 top-k，对整类摄入期统计给出不可能性证明，并提出观测查询需求的检索期检测器
- 📌 **结论**：BGE-large/BEIR 上 10 文档取 10/10，端到端使生成器对 88% 目标输出攻击者主张；最强分类器在 1% 误报下仅捕获 4.2% 攻击（近随机），检索期检测器同误报下 100% 捕获

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) answers a question by retrieving passages from a vector store and trusting them as context, so anyone who can add documents can try to steer the answer. A recent, appealing defense filters poisoning at ingestion, rejecting any document that behaves like a hub. We show it -- and every ingestion-time filter -- is defeated by a coordinated adversary that injects a handful of individually unremarkable documents which together surround one target query and seize its top-k (on BGE-large / BEIR, m=10 documents take 10/10; 9.9/10 on a live HNSW index). The attack is not theoretical. Realized as ordinary fluent text and run end-to-end through a BGE-large + HNSW + Qwen2.5-7B pipeline, it makes the generator emit the attacker's planted claim in 88% of targets, versus 0% without the injection. And no admission-time defense stops it: at ingestion an attack cone is geometrically identical to a legitimate niche upload, so -- measuring this directly -- the strongest trained classifier, given every feature and thousands of examples, separates the two no better than chance, catching 4.2% of attacks at a 1% false-positive rate. We prove this limit for the entire class of ingestion-time statistics (any decision from documents and reference queries alone), and it reproduces -- and worsens -- across two corpora and five encoders. The one signal that separates an attack from legitimate niche ingestion -- a query's demand -- is invisible before retrieval, which is also the escape: a retrieval-time detector that observes demand catches 100% of the attacks at the same 1% false-positive rate. Coverage of the query space by an admission gate is not containment of coordinated poisoning; robust defense must move past the front door, to demand.

</details>

### 105. TriShieldRAG: 3 Rings, One Blind Spot in Layered Defenses for Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2607.23838)　📅 2026-07

**关键词**：`analysis`、`layered defense`、`adaptive evasion`、`evaluation correction`

👤 **作者**：Susil Kumar Mohanty、Rohit Patel、Kosuru Yuvaraj、Jeenal Chaudhary、Disha Singhania

- 🎯 **研究动机**：单层防御对 RAG 投毒的防护有限，多层防御能否顶住自适应攻击未知
- 🔬 **研究方法**：提出 TriShieldRAG 三层框架（Ingest Guard 文档筛查、Retrieval Scorer 信任重排、Cross-LLM Consensus 三模型共识），并在非自适应与自适应投毒下评估
- 📌 **结论**：非自适应下 2.68M NQ 语料上 ASR 从 79% 降到 1%；但自适应攻击仅改文档格式即把 Ingest Guard 分数从 0.500 压到 0.000 并全量绕过（500/500），其余两层失效（62% vs 无防御 56%）；依赖同一检索证据的层会一起失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) grounds LLM answers in query-time retrieved documents, so reliability depends on what the retriever returns. PoisonedRAG (Zou et al., USENIX Security'25) showed five crafted documents mislead an undefended system in nearly 90% of cases, and that single-stage defenses give limited robustness. We propose TriShieldRAG, a three-layered framework: an Ingest Guard for document-level screening, a Retrieval Scorer for trust-aware re-ranking, and a Cross-LLM Consensus over three diverse models. We reasoned that collectively screening, re-ranking and validating retrieved evidence would give complementary protection, limiting the ability of poisoned documents to succeed through any single failure. We evaluate against non-adaptive and adaptive poisoning. Non-adaptively, on the full 2.68M-passage Natural Questions (NQ) corpus with the original PoisonedRAG attack, it cuts attack success from 79 +/- 1.0% to 1 +/- 0.0%. Adaptive attacks expose fundamental limits of layering. By changing only the document formatting, without modifying the poison text or accessing the retriever, the attacker reduces the Ingest Guard score from 0.500 to 0.000 and bypasses it on all 500 tested documents across three corpora. The remaining layers then give no protection: 62 +/- 0.8% attack success against a 56 +/- 2.5% undefended baseline on NQ, and 85 +/- 0.6% against 86 +/- 0.6% on HotpotQA. Layered defenses relying on the same retrieved evidence fail together: poisoned context misleads both re-ranking and consensus validation. Minority-poison thresholds prove corpus-dependent, at 0.214, 0.251 and 0.558 rather than the derived 0.5; a closed form we proposed for these failed a pre-registered prediction and is retracted. Cross-model agreement is misleading, reaching 0.96 while attack success approaches 99%. We release the framework, the evasion-certification methodology and artifacts.

</details>

### 106. MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG

📄 [arXiv](https://arxiv.org/abs/2606.26793)　📅 2026-06

**关键词**：`benchmark`、`agentic RAG red-teaming`、`cross-surface attack`、`novelty constraint`、`red teaming`、`multimodal agentic RAG`

👤 **作者**：Inderjeet Singh、Andrés Murillo、Motoyoshi Sekiya、Yuki Unno、Junichi Suga

- 🎯 **研究动机**：多模态 agentic RAG 攻击面扩展到文本投毒、图像注入、直接查询与编排器操纵，现有红队方法面特定且复用模板（73-84% 重复）
- 🔬 **研究方法**：提出 MIRROR：记忆引导 MCTS 在检索上下文条件下生成候选，确定性 Novelty Gate 拒绝与检索集重复的候选，兼顾先验与新颖性；发布 ART-SafeBench（41,815+ 内置记录）
- 📌 **结论**：图像投毒 ASR 76%（基线 52%）、编排器攻击 97% 且查询成本减半、跨面方差最低（CV 0.47）；专用基线跨面崩溃（后缀优化文本面 79% 但直接查询仅 1%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal agentic retrieval-augmented generation (RAG) systems expand the attack surface beyond prompt injection to include text poisoning, image injection, direct-query attacks, and orchestrator-level tool manipulation. Existing red-teaming approaches are typically surface-specific and often recycle known attack templates; on text-poisoning benchmarks we measure 73-84% exact duplication. We present MIRROR, a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint. A deterministic Novelty Gate rejects any candidate matching the retrieval set under normalized comparison, allowing retrieval to inform search priors without enabling prompt copying. Across four attack surfaces on a multimodal agentic RAG target, MIRROR attains 76% ASR on image poisoning compared with 52% for baselines, 97% ASR on orchestrator attacks at half the query cost, and the lowest cross-surface variance (coefficient of variation 0.47). In contrast, specialized baselines collapse across surfaces: suffix optimization reaches 79% ASR on text poisoning but 1% on direct queries. We release ART-SafeBench with 41,815 in-package records and runtime adapters yielding 41,991+ total records across four surfaces.

</details>

### 107. Benchmarking Poisoning Attacks against Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2505.18543)　📅 2025-05

**关键词**：`benchmark`、`attack-defense matrix`、`expanded QA`、`architecture coverage`、`13 attacks／7 defenses`、`multimodal RAG`

👤 **作者**：Baolei Zhang、…、Zheli Liu

- 🎯 **研究动机**：RAG 投毒攻击虽多，但缺乏对其真实威胁的系统性评估
- 🔬 **研究方法**：构建首个 RAG 投毒基准：5 个标准 QA 数据集与 10 个扩展变体、13 种攻击与 7 种防御的全谱评测
- 📌 **结论**：攻击在标准 QA 有效但在扩展版本显著下降；多轮、多模态与 Agent RAG 等高级架构均可被攻破，现有防御无法稳健防护

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) has proven effective in mitigating hallucinations in large language models by incorporating external knowledge during inference. However, this integration introduces new security vulnerabilities, particularly to poisoning attacks. Although prior work has explored various poisoning strategies, a thorough assessment of their practical threat to RAG systems remains missing. To address this gap, we propose the first comprehensive benchmark framework for evaluating poisoning attacks on RAG. Our benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques. Using this benchmark, we conduct a comprehensive evaluation of all included attacks and defenses across the full dataset spectrum. Our findings show that while existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions. Moreover, our results demonstrate that various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks. Notably, current defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies.

</details>

### 108. Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2505.12574) · 🌐 [Project](https://doi.org/10.1145/3770855.3818119)　📅 2025-05　🏷 KDD 2026

**关键词**：`benchmark`、`multi-attacker competition`、`shared corpus`、`evaluation validity`、`RAG poisoning`

👤 **作者**：Liuji Chen、…、Liang Wang

- 🎯 **研究动机**：RAG 投毒评测假设单一攻击者，而高价值查询会吸引目标冲突的多攻击者
- 🔬 **研究方法**：形式化 competing attacks 威胁模型并提出 competitive effectiveness 指标，构建 PoisonArena 标准化评测框架
- 📌 **结论**：单攻击者下有效的策略在竞争中显著退化并出现性能倒挂，暴露 ASR 与 F1 等常规指标的局限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems improve the factual grounding of large language models (LLMs) but remain vulnerable to retrieval poisoning, where adversaries seed the corpus with manipulated content. Prior work largely evaluates this threat under a simplified single-attacker assumption. In practice, however, high-value or high-visibility queries attract multiple adversaries with conflicting objectives. Motivated by real cases, we introduce the setting of competing attacks, in which multiple attackers simultaneously attempt to steer the same or closely related query toward different targets. We formalize this threat model and propose competitive effectiveness, a metric that quantifies an attacker's advantage under competition. Extensive experiments show that many strategies that succeed in the single-attacker regime degrade markedly under competition, revealing performance inversions and highlighting the limits of conventional metrics such as attack success rate and F1. Furthermore, we present PoisonArena, a standardized framework and benchmark for evaluating poisoning attacks and defenses under realistic, multi-adversary conditions.

</details>

### 109. Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2412.16708)　📅 2024-12

**关键词**：`benchmark`、`context taxonomy`、`retriever exposure`、`skeptical prompting`

👤 **作者**：Jinyan Su、Jin Peng Zhou、Zhengxin Zhang、Preslav Nakov、Claire Cardie

- 🎯 **研究动机**：RAG 投毒鲁棒性结论混杂了 retriever 暴露度与 generator 脆弱性
- 🔬 **研究方法**：把上下文分为 adversarial、untouched、guiding 三类并系统控制组合，评测多个 retriever 暴露度，并测 skeptical prompting
- 📌 **结论**：skeptical prompting 可激活内部推理实现部分自防，但效果高度依赖模型推理能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) systems have emerged as a promising solution to mitigate LLM hallucinations and enhance their performance in knowledge-intensive domains. However, these systems are vulnerable to adversarial poisoning attacks, where malicious passages injected into the retrieval corpus can mislead models into producing factually incorrect outputs. In this paper, we present a rigorously controlled empirical study of how RAG systems behave under such attacks and how their robustness can be improved. On the generation side, we introduce a structured taxonomy of context types-adversarial, untouched, and guiding-and systematically analyze their individual and combined effects on model outputs. On the retrieval side, we evaluate several retrievers to measure how easily they expose LLMs to adversarial contexts. Our findings also reveal that "skeptical prompting" can activate LLMs' internal reasoning, enabling partial self-defense against adversarial passages, though its effectiveness depends strongly on the model's reasoning capacity. Together, our experiments (code available at https://github.com/JinyanSu1/eval_PoisonRaG) and analysis provide actionable insights for designing safer and more resilient RAG systems, paving the way for more reliable real-world deployments.

</details>