# SIGIR 2026: AI Safety Papers

## 目录

- [会议信息](#会议信息)
- [关键节点](#关键节点)
- [筛选说明](#筛选说明)
- [RAG、AI 搜索与排序系统安全](#ragai-搜索与排序系统安全)
- [幻觉、证据与评测完整性](#幻觉证据与评测完整性)
- [内容真实性、事实核查与内容治理](#内容真实性事实核查与内容治理)
- [高风险推荐安全](#高风险推荐安全)
- [核验记录](#核验记录)

## 会议信息

| 项目 | 信息 |
| --- | --- |
| 会议全称 | The 49th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2026) |
| 举办时间与地点 | 2026-07-20 至 2026-07-24；Melbourne / Naarm, Australia |
| 官方网站 | [SIGIR 2026](https://sigir2026.org/) |
| 官方录用列表 | [Accepted Papers](https://sigir2026.org/en-AU/pages/program/accepted-papers) |
| 正式论文集 | [Proceedings](https://doi.org/10.1145/3805712) |
| 检查范围 | 官网列出的八类主会录用：Full、Perspective、Reproducibility、Resource、Short、Demo、Industry 与 Low Resource Environment，共 656 篇；单列的 12 篇 Doctoral Colloquium 不计入主会分母；数据截至 2026-08-30 |

## 关键节点

除会议日期外，投稿 deadline 均为当天 23:59 AoE。

| 节点 | 日期 | 官方来源 |
| --- | --- | --- |
| Full Paper abstract deadline | 2026-01-15 | [Full Papers Track](https://sigir2026.org/en-AU/pages/submissions/full-papers-track) |
| Full Paper submission deadline | 2026-01-22 | [Full Papers Track](https://sigir2026.org/en-AU/pages/submissions/full-papers-track) |
| Short / Resource Paper abstract deadline | 2026-02-05 | [Short Papers Track](https://sigir2026.org/en-AU/pages/submissions/short-papers-track) · [Resource Papers Track](https://sigir2026.org/en-AU/pages/submissions/resource-papers-track) |
| Short / Resource Paper submission deadline | 2026-02-12 | [Short Papers Track](https://sigir2026.org/en-AU/pages/submissions/short-papers-track) · [Resource Papers Track](https://sigir2026.org/en-AU/pages/submissions/resource-papers-track) |
| Industry Paper abstract deadline | 2026-02-19 | [Industry Track](https://sigir2026.org/en-AU/pages/submissions/industry-track) |
| Industry Paper submission deadline | 2026-02-26 | [Industry Track](https://sigir2026.org/en-AU/pages/submissions/industry-track) |
| Notification（上述 tracks） | 2026-04-02 | [Full Papers Track](https://sigir2026.org/en-AU/pages/submissions/full-papers-track) |
| Camera-ready / author registration | 2026-04-29 | [Full Papers Track](https://sigir2026.org/en-AU/pages/submissions/full-papers-track) |
| Conference | 2026-07-20 至 2026-07-24 | [SIGIR 2026](https://sigir2026.org/) |

## 筛选说明

- 官方论文总数：656；按官网类型复算为 Full 234、Perspective 12、Reproducibility 28、Resource 61、Short 151、Demo 24、Industry 131、Low Resource Environment 15。
- 初筛候选：104；先对完整标题列表宽筛，再补查标题不含显式安全词、但涉及生成式搜索操纵、证据污染、选择性遗忘、拒答、内容规避或科学综述可靠性的语义候选。
- 最终收录：31。
- 收录口径：逐篇阅读公开摘要或正文，只保留把 AI 搜索、RAG、生成式排序、内容审核、事实核查、幻觉、遗忘或高风险推荐中的攻击、失效后果、评测或缓解机制作为核心问题的工作；每篇只进入最匹配的一个分表。
- 边界案例：普通检索性能、一般推荐鲁棒性、公平排序、传统网络安全和不含具体安全后果的可信 IR 不收录；名称含 `Poison Pills`、但实质只研究 relevance feedback 退化的论文也予以排除。Doctoral Colloquium、tutorial 与 workshop 内容不与主会正式研究论文混合。
- 链接规则：`Official` 指向正式 DOI；arXiv 与作者项目只作为公开正文或 artifact 补充。没有可由论文或作者身份回证的代码入口时统一写“暂未公开”。

## 论文分类

### RAG、AI 搜索与排序系统安全

### 1. AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning

📄 [arXiv](https://arxiv.org/abs/2604.12201) · 🌐 [Project](https://doi.org/10.1145/3805712.3809838)　📅 2026　🏷 SIGIR 2026

**关键词**：`attack`、`single-document poisoning`、`adversarial CoT`、`query-specific attack`、`single-document poison`、`reasoning hijack`

👤 **作者**：Hongru Song、…、Xueqi Cheng

- 🎯 **研究动机**：RAG 知识库投毒研究靠海量毒文档淹没语料库，单文档的隐蔽投毒未被探索
- 🔬 **研究方法**：AdversarialCoT 是 query-specific 攻击：提取目标 LLM 推理框架构建初始对抗 CoT，再通过与 LLM 交互迭代精炼单篇毒文档
- 📌 **结论**：单篇对抗文档即可显著降低基准 LLM 的推理准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) enhances large language model (LLM) reasoning by retrieving external documents, but also opens up new attack surfaces. We study knowledge-base poisoning attacks in RAG, where an attacker injects malicious content into the retrieval corpus, which is then naturally surfaced by the retriever and consumed by the LLM during reasoning. Unlike prior work that floods the corpus with poisoned documents, we propose AdversarialCoT, a query-specific attack that poisons only a single document in the corpus. AdversarialCoT first extracts the target LLM's reasoning framework to guide the construction of an initial adversarial chain-of-thought (CoT). The adversarial document is iteratively refined through interactions with the LLM, progressively exposing and exploiting critical reasoning vulnerabilities. Experiments on benchmark LLMs show that a single adversarial document can significantly degrade reasoning accuracy, revealing subtle yet impactful weaknesses. This study exposes security risks in RAG systems and provides actionable insights for designing more robust LLM reasoning pipelines.

</details>

### 2. Answer First, Evidence Second? Uncovering Hidden Risks in Well-Structured AI Search Summaries

🌐 [Project](https://doi.org/10.1145/3805712.3809913)　📅 2026　🏷 SIGIR 2026

**关键词**：`analysis`、`AI search`、`citation consistency`、`evidence grounding`、`claim-source mismatch`、`citation audit`

- 🎯 **研究动机**：AI搜索摘要结构规整，但claim与来源的一致性缺审计
- 🔬 **研究方法**：审计citation一致性与evidence grounding，量化claim-source错配与证据可得性
- 📌 **结论**：结构良好的摘要仍普遍存在claim-source错配与证据缺口

### 3. Deletion Isn't Enough: Auditing RAG for Selective Forgetting

🌐 [Project](https://doi.org/10.1145/3805712.3808545)　📅 2026　🏷 SIGIR 2026

**关键词**：`analysis`、`audit`、`RAG revocation`、`selective forgetting`、`disclosure probe`、`RAG disclosure`

- 🎯 **研究动机**：RAG删除知识后是否真正被遗忘缺审计手段
- 🔬 **研究方法**：构造paired disclosure probe审计撤回后的残留泄漏
- 📌 **结论**：删除操作后的RAG仍可泄露应被遗忘的内容

### 4. Policy-Guided RAG: A Governance Framework for Controlled Information Use in Large Language Models

🌐 [Project](https://doi.org/10.1145/3805712.3808490)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`framework`、`RAG governance`、`policy enforcement`、`auditable generation`

- 🎯 **研究动机**：LLM对检索信息的使用缺策略级治理，生成过程难审计
- 🔬 **研究方法**：提出Policy-Guided RAG治理框架，按策略控制检索信息使用并支持可审计生成
- 📌 **结论**：实现受控、可审计的LLM信息消费

### 5. Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2604.23640) · 🌐 [Project](https://doi.org/10.1145/3805712.3809691)　📅 2026　🏷 SIGIR 2026

**关键词**：`attack`、`LLM recommender`、`black-box promotion`、`proxy prompt`、`functional prompt inference`、`black-box system`

👤 **作者**：Yuchuan Zhao、Tong Chen、Junliang Yu、Zongwei Wang、Lizhen Cui、Hongzhi Yin

- 🎯 **研究动机**：已有 LLM 推荐系统推广攻击假设能访问受害模型或 prompt，不符合现实
- 🔬 **研究方法**：PUDA 全黑盒设定：LLM 进化精炼推断离散 system prompt 训练代理模型，再在语义约束下改写目标 item 文本并生成毒化序列
- 📌 **结论**：真实数据集上一致超过 SOTA，即使 prompt 与模型均受保护仍可有效推广冷门目标 item

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-powered sequential recommender systems (LLM-SRSs) have recently demonstrated remarkable performance, enabling recommendations through prompt-driven inference over user interaction sequences. However, this paradigm also introduces new security vulnerabilities, particularly text-level manipulations, rendering them appealing targets for promotion attacks that purposely boost the ranking of specific target items. Although such security risks have been receiving increasing attention, existing studies typically rely on an unrealistic assumption of access to either the victim model or prompt to unveil attack mechanisms. In this work, we investigate the item promotion attack in LLM-SRSs under a more realistic setting where both the system prompt and victim model are unknown to the attacker, and propose a Prompt-Unknown Dual-poisoning Attack (PUDA) framework. To simulate attacks under this full black-box setting, we introduce an LLM-based evolutionary refinement strategy that infers discrete system prompts, enabling the training of an effective surrogate model that mimics the behaviors of the victim model. Leveraging the distilled prompt and surrogate model, we devise a promotion attack that adversarially revises target item texts under semantic constraints, which is further complemented by the highly plausible, surrogate-generated poisoning sequences to enable cost-effective target item promotion. Extensive experiments on real-world datasets demonstrate that PUDA consistently outperforms state-of-the-art competitors in boosting the exposure of unpopular target items. Our findings reveal critical security risks in modern LLM-SRSs even when both prompts and models are protected, and highlight the need for more robust defensive means.

</details>

### 6. PurifAI: Detecting and Fixing Search-Induced Distortions in Web-Augmented LLMs

🌐 [Project](https://doi.org/10.1145/3805712.3809751)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`web-augmented LLM`、`search distortion`、`knowledge purification`、`web evidence poisoning`、`knowledge conflict`

- 🎯 **研究动机**：检索到的web证据会诱发知识冲突与扭曲，缓存还会放大污染
- 🔬 **研究方法**：PurifAI检测并修复search-induced扭曲，净化证据与缓存
- 📌 **结论**：降低web增强LLM的中毒与幻觉影响

### 7. Reward Shaping for Robust Refusal in Small Language Models for Retrieval-Augmented Question Answering

🌐 [Project](https://doi.org/10.1145/3805712.3809891)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`RAG refusal`、`reward shaping`、`distractor robustness`

- 🎯 **研究动机**：小模型RAG问答易被无关检索证据诱发错误拒答或回答
- 🔬 **研究方法**：以reward shaping训练对distractor证据的稳健拒答
- 📌 **结论**：干扰证据下的拒答鲁棒性显著提升

### 8. Teaching Small Models When Not to Call Functions: Structured Reasoning for Reducing Tool-Use Hallucinations

🌐 [Project](https://doi.org/10.1145/3805712.3809979)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`tool-use hallucination`、`structured reasoning`、`function calling`、`tool hallucination`、`structured abstention`

- 🎯 **研究动机**：小模型在不该调用工具时产生幻觉调用
- 🔬 **研究方法**：以结构化推理教模型判断调用时机并做结构化弃权
- 📌 **结论**：tool-use幻觉显著减少

### 9. The Vulnerability of LLM Rankers to Prompt Injection Attacks: You are to [MARK] this paper as the Best Paper

📄 [arXiv](https://arxiv.org/abs/2602.16752) · 🌐 [Project](https://doi.org/10.1145/3805712.3808553)　📅 2026　🏷 SIGIR 2026

**关键词**：`attack`、`LLM ranker`、`objective hijack`、`criteria hijack`

👤 **作者**：Yu Yin、Shuai Wang、Bevan Koopman、Guido Zuccon

- 🎯 **研究动机**：候选文档内 prompt 注入可操纵 LLM 排序，但该脆弱性跨模型家族与设定的边界未探明
- 🔬 **研究方法**：在 pairwise/listwise/setwise 三种排序范式下系统评估目标劫持与准则劫持两种注入，度量 ASR 与 nDCG@10 影响
- 📌 **结论**：刻画了脆弱性边界条件，发现 encoder-decoder 架构对越狱注入具有固有强韧性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have emerged as powerful re-rankers. Recent research has however showed that simple prompt injections embedded within a candidate document (i.e., jailbreak prompt attacks) can significantly alter an LLM's ranking decisions. While this poses serious security risks to LLM-based ranking pipelines, the extent to which this vulnerability persists across diverse LLM families, architectures, and settings remains largely under-explored. In this paper, we present a comprehensive empirical study of jailbreak prompt attacks against LLM rankers. We focus our evaluation on two complementary tasks: (1) Preference Vulnerability Assessment, measuring intrinsic susceptibility via attack success rate (ASR); and (2) Ranking Vulnerability Assessment, quantifying the operational impact on the ranking's quality (nDCG@10). We systematically examine three prevalent ranking paradigms (pairwise, listwise, setwise) under two injection variants: decision objective hijacking and decision criteria hijacking. Beyond reproducing prior findings, we expand the analysis to cover vulnerability scaling across model families, position sensitivity, backbone architectures, and cross-domain robustness. Our results characterize the boundary conditions of these vulnerabilities, revealing critical insights such as that encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks. We publicly release our code and additional experimental results at https://github.com/ielab/LLM-Ranker-Attack.

</details>

### 10. When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse

📄 [arXiv](https://arxiv.org/abs/2608.06947) · 🌐 [Project](https://doi.org/10.1145/3805712.3809904)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`detection`、`RAG poisoning`、`document attention`、`runtime detection`、`entropy collapse`

👤 **作者**：Yingtao Ren、Ziyi Zhao、Yiwei Fu、Xiao Luo、Yu-Cheng Chang、Chin-Teng Lin

- 🎯 **研究动机**：基于输出侧困惑度/一致性的 RAG 投毒检测会被攻击诱发的虚假自信欺骗：投毒输出困惑度反而更低
- 🔬 **研究方法**：发现被攻击生成的文档级注意力熵坍缩（Attention Collapse）这一内部信号，D-SCAN 轻量监测生成器注意力动态识别被攻击输出
- 📌 **结论**：多攻击基准上有效，且能检出未改变最终答案的攻击

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is indispensable for enhancing large language models. However, RAGs are increasingly susceptible to poisoning attacks, in which adversarial documents are injected to manipulate generator outputs. Previous methods rely on output-side signals such as perplexity and consistency checks to detect such attacks. Nevertheless, our analysis reveals that deliberate attacks often induce false confidence, where poisoned outputs exhibit even lower perplexity than benign ones, rendering uncertainty-based detection ineffective. To address this challenge, we explore the internal dynamics of the generator and identify a distinctive signature termed \textit{Attention Collapse}. Unlike the dispersed attention in benign generations, attacked generations exhibit a decrease in entropy as attention concentrates on poisoned documents. Building on these findings, we propose \texttt{D-SCAN} (Document-level Signal Collapse Analysis), a lightweight detection framework that monitors attention dynamics to identify attacked generations. Extensive experiments on multiple attack benchmarks demonstrate the effectiveness of our method. Moreover, D-SCAN can detect attacks even when they fail to alter the final answer. Code is available at https://github.com/yingtaoren/D-Scan.git.

</details>
### 幻觉、证据与评测完整性

### 11. Auto-Judge: A Cross-Task Benchmark for Comparing LLM Judges for Citation-Grounded RAG Systems

🌐 [Project](https://doi.org/10.1145/3805712.3808601)　📅 2026　🏷 SIGIR 2026

**关键词**：`benchmark`、`LLM judge`、`citation-grounded RAG`、`evaluation integrity`、`judge manipulation`、`evaluation validity`

- 🎯 **研究动机**：citation-grounded RAG的LLM评审器缺跨任务可靠性评测
- 🔬 **研究方法**：构建Auto-Judge基准比较LLM judge的评判质量与抗操纵性
- 📌 **结论**：揭示LLM评审器的偏差与可操纵风险，威胁评测有效性

### 12. Calibrating Uncertainty with Cross-Model Consistency for LLM Hallucination Mitigation

🌐 [Project](https://doi.org/10.1145/3805712.3809846)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`hallucination mitigation`、`uncertainty calibration`、`cross-model consistency`

- 🎯 **研究动机**：单模型不确定性校准不足以可靠识别幻觉
- 🔬 **研究方法**：以跨模型一致性校准不确定性并引导幻觉缓解
- 📌 **结论**：幻觉检测与缓解效果提升

### 13. CSMAD: Contradictory Statement Multi-Agent Debate for Factual Hallucination Detection

🌐 [Project](https://doi.org/10.1145/3805712.3808508)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`factual hallucination`、`multi-agent debate`、`NLI verification`

- 🎯 **研究动机**：事实性幻觉缺可扩展的自动检测手段
- 🔬 **研究方法**：CSMAD以矛盾陈述驱动多智能体辩论并结合NLI验证
- 📌 **结论**：事实性幻觉检测精度提升

### 14. Fast and Faithful: Efficient Full-Context Verification for Long-Form LLM Responses

📄 [arXiv](https://arxiv.org/abs/2603.23508) · 🤗 [Model](https://huggingface.co/llm-semantic-router) · 🌐 [Project](https://doi.org/10.1145/3805712.3808493)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`long-form verification`、`full-context reasoning`、`semantic routing`

👤 **作者**：Xunzhuo Liu、Bowei He、Xue Liu、Haichen Zhang、Huamin Chen

- 🎯 **研究动机**：LLM 校验长上下文太慢太贵，轻量分类器受上下文限制常漏截断外的证据
- 🔬 **研究方法**：生产级 RAG 管线集成实时验证组件，处理最长 32K token 文档，以自适应推理策略平衡响应时间与验证覆盖
- 📌 **结论**：全上下文验证较截断验证显著提升无支撑回答的检出，并阐明何时需要长上下文验证与延迟预算如何塑形模型设计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) is increasingly deployed in enterprise search and document-centric assistants, where responses must be grounded in long and complex source materials. In practice, verifying that generated answers faithfully reflect retrieved documents is difficult: large language models can check long contexts but are too slow and costly for interactive services, while lightweight classifiers operate within strict context limits and frequently miss evidence outside truncated passages. We present the design of a real-time verification component integrated into a production RAG pipeline that enables full-document grounding under latency constraints. The system processes documents up to 32K tokens and employs adaptive inference strategies to balance response time and verification coverage across workloads. We describe the architectural decisions, operational trade-offs, and evaluation methodology used to deploy the verifier, and show that full-context verification substantially improves detection of unsupported responses compared with truncated validation. Our experience highlights when long-context verification is necessary, why chunk-based checking often fails in real documents, and how latency budgets shape model design. These findings provide practical guidance for practitioners building reliable large-scale retrieval-augmented applications. (Model, benchmark, and code: https://huggingface.co/llm-semantic-router)

</details>

### 15. Numerical Hallucinations in RAG: Detection and Analysis

🌐 [Project](https://doi.org/10.1145/3805712.3809882)　📅 2026　🏷 SIGIR 2026

**关键词**：`analysis`、`numerical hallucination`、`RAG`、`quantitative fidelity`

- 🎯 **研究动机**：RAG数值幻觉的检测与分析空白
- 🔬 **研究方法**：系统评测RAG生成中数字的量化保真
- 📌 **结论**：揭示数值幻觉的普遍模式与成因

### 16. SurGE: A Benchmark and Evaluation Framework for Scientific Survey Generation

📄 [arXiv](https://arxiv.org/abs/2508.15658) · 🌐 [Project](https://doi.org/10.1145/3805712.3808598)　📅 2026　🏷 SIGIR 2026

**关键词**：`benchmark`、`scientific survey`、`citation integrity`、`evidence coverage`、`survey generation`、`citation accuracy`

👤 **作者**：Weihang Su、…、Yiqun Liu

- 🎯 **研究动机**：学术文献激增使人工撰写综述难以为继，LLM 自动综述缺乏标准化基准与评估协议
- 🔬 **研究方法**：构建 SurGE：含主题描述、专家综述及全部引文的测试实例加百万级论文语料，自动评估覆盖全面性、引用准确性、结构组织与内容质量四维
- 📌 **结论**：多种 LLM 方法性能差距显著，先进 agentic 框架也难以胜任综述生成任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of academic literature makes the manual creation of scientific surveys increasingly infeasible. While large language models show promise for automating this process, progress in this area is hindered by the absence of standardized benchmarks and evaluation protocols. To bridge this critical gap, we introduce SurGE (Survey Generation Evaluation), a new benchmark for scientific survey generation in computer science. SurGE consists of (1) a collection of test instances, each including a topic description, an expert-written survey, and its full set of cited references, and (2) a large-scale academic corpus of over one million papers. In addition, we propose an automated evaluation framework that measures the quality of generated surveys across four dimensions: comprehensiveness, citation accuracy, structural organization, and content quality. Our evaluation of diverse LLM-based methods demonstrates a significant performance gap, revealing that even advanced agentic frameworks struggle with the complexities of survey generation and highlighting the need for future research in this area. We have open-sourced all the code, data, and models at: https://github.com/oneal2000/SurGE

</details>

### 17. The LLM Effect on IR Benchmarks: A Meta-Analysis of Effectiveness, Baselines, and Contamination

📄 [arXiv](https://arxiv.org/abs/2604.05766) · 🌐 [Project](https://doi.org/10.1145/3805712.3809901)　📅 2026　🏷 SIGIR 2026

**关键词**：`analysis`、`benchmark contamination`、`LLM evaluation`、`evidence synthesis`

👤 **作者**：Moritz Staudinger、Wojciech Kusa、Allan Hanbury

- 🎯 **研究动机**：LLM对IR基准的效应、基线与数据污染影响未量化
- 🔬 **研究方法**：对IR评测文献做meta分析与证据综合
- 📌 **结论**：揭示LLM时代IR基准的有效性与污染问题
### 内容真实性、事实核查与内容治理

### 18. A Dataset of Cultural Heritage Manipulation on English Wikipedia in the Russo-Ukrainian Context

🌐 [Project](https://doi.org/10.1145/3805712.3808580)　📅 2026　🏷 SIGIR 2026

**关键词**：`dataset`、`information manipulation`、`Wikipedia`、`cultural heritage`

- 🎯 **研究动机**：英文Wikipedia上俄乌语境的文化遗产信息操纵缺标注数据
- 🔬 **研究方法**：构建俄乌背景下英文Wikipedia文化遗产条目操纵数据集
- 📌 **结论**：为信息操纵检测研究提供数据基础

### 19. Decoding Multimodal Cues: Unveiling the Implicit Meaning Behind Hateful Videos

📄 [arXiv](https://arxiv.org/abs/2606.11953) · 🌐 [Project](https://doi.org/10.1145/3805712.3809637)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`hateful video`、`evidence rationale`、`multimodal reasoning`、`hateful-video moderation`、`cross-modal evidence`

👤 **作者**：Junyu Lu、…、Hongfei Lin

- 🎯 **研究动机**：仇恨视频检测局限于二分类，缺少揭示判断依据的上下文理由，可解释性不足
- 🔬 **研究方法**：构建 Ex-HateMM 与 Ex-ImpliHateVid 两个细粒度标注数据集，提出 IARE 框架：多模态 CoT 信息增强 + DPO 引导正确推理路径
- 📌 **结论**：IARE 在两个数据集上取得 SOTA 并生成准确理由

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hateful videos have become prevalent on online platforms, highlighting an urgent need for effective detection. However, existing studies primarily focus on binary classification and fail to provide contextual rationales that reveal the implicit meanings behind these judgments, significantly undermining model explainability. To fill this gap, we aim to achieve explainable hateful video detection, enabling models to provide contextual rationales that integrate relevant evidence and logical reasoning alongside decisions. This approach can comprehensively enhance the understanding of video content and the explainability of the decision-making process. We first introduce two datasets, Ex-HateMM and Ex-ImpliHateVid, for explainable hateful video detection. Each dataset provides fine-grained annotations of multimodal harmful elements, along with contextual rationales. We then propose an Information Augmentation and Reasoning Enhancement (IARE) framework designed for explainable detection. The framework employs an information augmentation phase that leverages the multimodal chain-of-thought to integrate harmful elements, thereby enriching rationale evidence. Additionally, IARE incorporates a reasoning enhancement phase, in which Direct Preference Optimization guides the model toward correct reasoning paths and away from incorrect ones, thereby improving the logical coherence of its justifications. We conduct extensive experiments on the two datasets, comparing multiple baselines with our proposed IARE framework. The results demonstrate that IARE achieves state-of-the-art performance while also generating accurate rationales.

</details>

### 20. Deja Vu in Plots: Leveraging Cross-Session Evidence with Retrieval-Augmented LLMs for Live Streaming Risk Assessment

📄 [arXiv](https://arxiv.org/abs/2601.16027) · 🌐 [Project](https://doi.org/10.1145/3805712.3809737)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`livestream risk`、`cross-session retrieval`、`production moderation`

👤 **作者**：Yiran Qiao、Xiang Ao、Jing Chen、Yang Liu、Qiwei Zhong、Qing He

- 🎯 **研究动机**：直播风险行为跨场次渐积且复发，单会话检测难以识别
- 🔬 **研究方法**：CS-VAR 由轻量领域模型做快速会话级风险推断，训练时 LLM 基于检索的跨会话行为证据推理，并把局部到全局洞见蒸馏给小模型以实时部署
- 📌 **结论**：大规模工业数据的离线实验与在线验证均达 SOTA，并提供可解释的局部信号赋能实际审核

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rise of live streaming has transformed online interaction, enabling massive real-time engagement but also exposing platforms to complex risks such as scams and coordinated malicious behaviors. Detecting these risks is challenging because harmful actions often accumulate gradually and recur across seemingly unrelated streams. To address this, we propose CS-VAR (Cross-Session Evidence-Aware Retrieval-Augmented Detector) for live streaming risk assessment. In CS-VAR, a lightweight, domain-specific model performs fast session-level risk inference, guided during training by a Large Language Model (LLM) that reasons over retrieved cross-session behavioral evidence and transfers its local-to-global insights to the small model. This design enables the small model to recognize recurring patterns across streams, perform structured risk assessment, and maintain efficiency for real-time deployment. Extensive offline experiments on large-scale industrial datasets, combined with online validation, demonstrate the state-of-the-art performance of CS-VAR. Furthermore, CS-VAR provides interpretable, localized signals that effectively empower real-world moderation for live streaming.

</details>

### 21. EVADE-Bench: Multimodal Benchmark for Evaluating and Enhancing Evasive Content Detection

📄 [arXiv](https://arxiv.org/abs/2505.17654) · 📊 [Dataset](https://huggingface.co/datasets/koenshen/EVADE-Bench) · 🌐 [Project](https://doi.org/10.1145/3805712.3808579)　📅 2026　🏷 SIGIR 2026

**关键词**：`benchmark`、`e-commerce moderation`、`evasive content`、`multimodal decomposition`、`cross-modal evasion`、`policy circumvention`

👤 **作者**：Ancheng Xu、…、Min Yang

- 🎯 **研究动机**：电商审核模型对拆字、暗语、裁图等规避内容脆弱，且无基准同时考察规则理解与混淆意图推断
- 🔬 **研究方法**：构建专家策展的中文多模态 EVADE-Bench，评测 26 个开源与闭源 LLM 及 VLM 的规避内容检测
- 📌 **结论**：SoTA 模型频繁误判；清晰规则分类显著减少误报，视觉描述与逻辑推断解耦的多 agent 分解带来明显准确率增益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

E-commerce platforms increasingly rely on Large Language Models (LLMs) and Vision Language Models (VLMs) to detect illicit or misleading product content. However, these models remain vulnerable to evasive content, which refers to inputs that have been deliberately modified through techniques such as word splitting, euphemistic language, or image cropping to conceal policy violations while still conveying prohibited claims. Crucially, detecting such content requires a model to simultaneously master two capabilities: accurately comprehending complex rules, and correctly inferring the true intent behind deliberately obfuscated multimodal inputs. While prior work has separately explored LLM reasoning over complex rules and LLM-based detection of evasive content, no existing benchmark combines both within a unified evaluation framework. This gap is particularly consequential in e-commerce, where accurate moderation demands that both capabilities operate in concert. To address this gap, we introduce EVADE-Bench, the first expert-curated Chinese multimodal benchmark specifically designed to evaluate LLMs and VLMs on evasive content detection in real-world e-commerce scenarios. Our comprehensive evaluation of 26 open- and closed-source LLMs and VLMs reveals that even state-of-the-art models frequently misclassify evasive samples. We further demonstrate that clearer rule categorization significantly improves model prediction consistency and reduces false predictions, highlighting the critical role of benchmark design in enabling reliable evaluation. To explore paths for performance improvement, we investigate the feasibility of multi-agent decomposition for multimodal reasoning, wherein visual description and logical inference are decoupled into separate agents, and find that this strategy yields notable accuracy gains.

</details>

### 22. ExDR: Explanation-driven Dynamic Retrieval Enhancement for Multimodal Fake News Detection

📄 [arXiv](https://arxiv.org/abs/2601.15820) · 🌐 [Project](https://doi.org/10.1145/3805712.3809648)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`multimodal fake news`、`dynamic retrieval`、`explanation feedback`

👤 **作者**：Guoxuan Ding、Yuqing Li、Ziyan Zhou、Zheng Lin、Daren Zha、Jiangnan Li

- 🎯 **研究动机**：动态 RAG 用于多模态假新闻检测时存在冗余检索、粗糙相似度与无关证据问题
- 🔬 **研究方法**：ExDR 在检索触发与证据检索两模块系统性利用模型生成的解释：三维度评估触发置信度、融合欺骗实体构建实体感知索引、基于欺骗特征检索对比证据
- 📌 **结论**：在 AMG 与 MR2 两个基准上，检索触发准确率、检索质量与整体检测性能均超越已有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid spread of multimodal fake news poses a serious societal threat, as its evolving nature and reliance on timely factual details challenge existing detection methods. Dynamic Retrieval-Augmented Generation provides a promising solution by triggering keyword-based retrieval and incorporating external knowledge, thus enabling both efficient and accurate evidence selection. However, it still faces challenges in addressing issues such as redundant retrieval, coarse similarity, and irrelevant evidence when applied to deceptive content. In this paper, we propose ExDR, an Explanation-driven Dynamic Retrieval-Augmented Generation framework for Multimodal Fake News Detection. Our framework systematically leverages model-generated explanations in both the retrieval triggering and evidence retrieval modules. It assesses triggering confidence from three complementary dimensions, constructs entity-aware indices by fusing deceptive entities, and retrieves contrastive evidence based on deception-specific features to challenge the initial claim and enhance the final prediction. Experiments on two benchmark datasets, AMG and MR2, demonstrate that ExDR consistently outperforms previous methods in retrieval triggering accuracy, retrieval quality, and overall detection performance, highlighting its effectiveness and generalization capability.

</details>

### 23. JARVIS: A Joint Framework for Multimodal Risk Classification and Retrieval in E-Commerce

📄 [arXiv](https://arxiv.org/abs/2602.12941) · 🌐 [Project](https://doi.org/10.1145/3805712.3808429)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`e-commerce risk`、`multimodal retrieval`、`production moderation`

👤 **作者**：Nan Lu、Leyang Li、Yurong Hu、Rui Lin、Shaoyi Xu

- 🎯 **研究动机**：电商虚假评论检测方法泛化不足且缺乏可解释性
- 🔬 **研究方法**：JARVIS 经稠密-稀疏混合多模态检索与共享实体扩展构建异构证据图，由 LLM 做证据接地的可解释裁定
- 📌 **结论**：离线 precision 0.953→0.988、recall 0.830→0.901；线上召回量增 27%、人工审核时间降 75%，分析采纳率 96.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deceptive reviews, refer to fabricated feedback designed to artificially manipulate the perceived quality of products. Within modern e-commerce ecosystems, these reviews remain a critical governance challenge. Despite advances in review-level and graph-based detection methods, two pivotal limitations remain: inadequate generalization and lack of interpretability. To address these challenges, we propose JARVIS, a framework providing Judgment via Augmented Retrieval and eVIdence graph Structures. Starting from the review to be evaluated, it retrieves semantically similar evidence via hybrid dense-sparse multimodal retrieval, expands relational signals through shared entities, and constructs a heterogeneous evidence graph. Large language model then performs evidence-grounded adjudication to produce interpretable risk assessments. Offline experiments demonstrate that JARVIS enhances performance on our constructed review dataset, achieving a precision increase from 0.953 to 0.988 and a recall boost from 0.830 to 0.901. In the production environment, our framework achieves a 27% increase in the recall volume and reduces manual inspection time by 75%. Furthermore, the adoption rate of the model-generated analysis reaches 96.4%.

</details>

### 24. Mitigating Adversarial Attacks by Transferring LLM-generated Narrative Reasoning for Robust Fake News Detection

🌐 [Project](https://doi.org/10.1145/3805712.3809585)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`fake news`、`adversarial attack`、`reasoning transfer`

- 🎯 **研究动机**：假新闻检测器对对抗扰动脆弱
- 🔬 **研究方法**：将LLM生成的叙事推理迁移给检测器以增强鲁棒性
- 📌 **结论**：对抗攻击下检测性能降幅显著减小

### 25. Multi-Sourced, Multi-Agent Evidence Retrieval for Fact-Checking

📄 [arXiv](https://arxiv.org/abs/2603.00267) · 🌐 [Project](https://doi.org/10.1145/3805712.3809686)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`fact-checking`、`multi-agent retrieval`、`source diversity`

👤 **作者**：Shuzhi Gong、Richard O. Sinnott、Jianzhong Qi、Cecile Paris、Preslav Nakov、Zhuohan Xie

- 🎯 **研究动机**：现有事实核查依赖文本相似度检索证据，难以捕获文档内多跳语义关联，导致真伪误判
- 🔬 **研究方法**：WKGFC 以开放知识图谱为核心证据源，LLM agent 按 MDP 决策检索相关子图并以 web 内容补全，用提示优化微调该 agentic LLM
- 📌 **结论**：结构化知识子图证据改善证据与声明间的细微事实关联，提升事实验证效果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Misinformation spreading over the Internet poses a significant threat to both societies and individuals, necessitating robust and scalable fact-checking that relies on retrieving accurate and trustworthy evidence. Previous methods rely on semantic and social-contextual patterns learned from training data, which limits their generalization to new data distributions. Recently, Retrieval Augmented Generation (RAG) based methods have been proposed to utilize the reasoning capability of LLMs with retrieved grounding evidence documents. However, these methods largely rely on textual similarity for evidence retrieval and struggle to retrieve evidence that captures multi-hop semantic relations within rich document contents. These limitations lead to overlooking subtle factual correlations between the evidence and the claims to be fact-checked during evidence retrieval, thus causing inaccurate veracity predictions. To address these issues, we propose WKGFC, which exploits authorized open knowledge graph as a core resource of evidence. LLM-enabled retrieval is designed to assess the claims and retrieve the most relevant knowledge subgraphs, forming structured evidence for fact verification. To augment the knowledge graph evidence, we retrieve web contents for completion. The above process is implemented as an automatic Markov Decision Process (MDP): A reasoning LLM agent decides what actions to take according to the current evidence and the claims. To adapt the MDP for fact-checking, we use prompt optimization to fine-tune the agentic LLM.

</details>

### 26. R 3 Check: Reinforcement Learning for Iterative Retrieval and Structured Reasoning in Complex Fact Checking

🌐 [Project](https://doi.org/10.1145/3805712.3809601)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`fact-checking`、`iterative retrieval`、`reinforcement learning`

- 🎯 **研究动机**：复杂事实核查需多跳检索与推理配合
- 🔬 **研究方法**：R^3Check以强化学习训练迭代检索加结构化推理的核查器
- 📌 **结论**：复杂claim验证准确率提升

### 27. Resources for Automated Evaluation of Assistive RAG Systems that Help Readers with News Trustworthiness Assessment

📄 [arXiv](https://arxiv.org/abs/2602.24277) · 🌐 [Project](https://doi.org/10.1145/3805712.3808624)　📅 2026　🏷 SIGIR 2026

**关键词**：`resource`、`news trustworthiness`、`assistive RAG`、`automated evaluation`

👤 **作者**：Dake Zhang、Mark D. Smucker、Charles L. A. Clarke

- 🎯 **研究动机**：辅助读者评估新闻可信度的 RAG 系统缺乏可复用的评测资源
- 🔬 **研究方法**：发布 TREC 2025 DRAGUN track 资源：问题生成与基于 MS MARCO V2.1 的 250 词报告生成两任务，含 30 篇文章的重要性加权 rubric 与 AutoJudge 自动判分流程
- 📌 **结论**：AutoJudge 与 TREC 人工评测排序高度一致（Task 1 τ=0.678、Task 2 τ=0.872），支撑该类 RAG 评测研究

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Many readers today struggle to assess the trustworthiness of online news because reliable reporting coexists with misinformation. The TREC 2025 DRAGUN (Detection, Retrieval, and Augmented Generation for Understanding News) Track provided a venue for researchers to develop and evaluate assistive RAG systems that support readers' news trustworthiness assessment by producing reader-oriented, well-attributed reports. As the organizers of the DRAGUN track, we describe the resources that we have newly developed to allow for the reuse of the track's tasks. The track had two tasks: (Task 1) Question Generation, producing 10 ranked investigative questions; and (Task 2, the main task) Report Generation, producing a 250-word report grounded in the MS MARCO V2.1 Segmented Corpus. As part of the track's evaluation, we had TREC assessors create importance-weighted rubrics of questions with expected short answers for 30 different news articles. These rubrics represent the information that assessors believe is important for readers to assess an article's trustworthiness. The assessors then used their rubrics to manually judge the participating teams' submitted runs. To make these tasks and their rubrics reusable, we have created an automated process to judge runs not part of the original assessing. We show that our AutoJudge ranks existing runs well compared to the TREC human-assessed evaluation (Kendall's $τ= 0.678$ for Task 1 and $τ= 0.872$ for Task 2). These resources enable both the evaluation of RAG systems for assistive news trustworthiness assessment and, with the human evaluation as a benchmark, research on improving automated RAG evaluation.

</details>

### 28. Retrieval-Augmented Multimodal Model for Fake News Detection

📄 [arXiv](https://arxiv.org/abs/2604.18112) · 🌐 [Project](https://doi.org/10.1145/3805712.3809605)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`multimodal fake news`、`retrieval augmentation`、`external evidence`

👤 **作者**：Yiheng Li、Weihai Lu、Hanyi Yu、Yue Wang

- 🎯 **研究动机**：多模态假新闻检测逐条孤立评估、缺跨实例叙事一致性，且参数化知识难以泛化到新领域
- 🔬 **研究方法**：RAMM 以 MLLM 为骨干，加抽象叙事对齐模块聚合跨域叙事一致性，并用语义表征对齐把推理转为实例类比过程
- 📌 **结论**：三个公开数据集上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In recent years, multimodal multidomain fake news detection has garnered increasing attention. Nevertheless, this direction presents two significant challenges: (1) Failure to Capture Cross-Instance Narrative Consistency: existing models usually evaluate each news in isolation, fail to capture cross-instance narrative consistency, and thus struggle to address the spread of cluster based fake news driven by social media; (2) Lack of Domain Specific Knowledge for Reasoning: conventional models, which rely solely on knowledge encoded in their parameters during training, struggle to generalize to new or data-scarce domains (e.g., emerging events or niche topics). To tackle these challenges, we introduce Retrieval-Augmented Multimodal Model for Fake News Detection (RAMM). First, RAMM employs a Multimodal Large Language Model (MLLM) as its backbone to capture cross-modal semantic information from news samples. Second, RAMM incorporates an Abstract Narrative Alignment Module. This component adaptively extracts abstract narrative consistency from diverse instances across distinct domains, aggregates relevant knowledge, and thereby enables the modeling of high-level narrative information. Finally, RAMM introduces a Semantic Representation Alignment Module, which aligns the model's decision-making paradigm with that of humans - specifically, it shifts the model's reasoning process from direct inference on multimodal features to an instance-based analogical reasoning process. Extensive experimental results on three public datasets validate the efficacy of our proposed approach. Our code is available at the following link: https://github.com/li-yiheng/RAMM

</details>

### 29. SciCheck: Reasoning Distillation for Biomedical Claim Verification

🌐 [Project](https://doi.org/10.1145/3805712.3809699)　📅 2026　🏷 SIGIR 2026

**关键词**：`detection`、`biomedical claims`、`reasoning distillation`、`scientific evidence`

- 🎯 **研究动机**：生物医学claim验证缺推理增强型检测器
- 🔬 **研究方法**：SciCheck蒸馏大模型推理用于科学证据核查
- 📌 **结论**：生物医学claim验证精度提升

### 30. Simulating the Lateral Reader: A Baseline for Source-Aware Web Credibility Assessment

🌐 [Project](https://doi.org/10.1145/3805712.3809973)　📅 2026　🏷 SIGIR 2026

**关键词**：`baseline`、`web credibility`、`lateral reading`、`source awareness`

- 🎯 **研究动机**：在线新闻读者缺乏时间与领域专长核实陌生信源，专业事实核查员的横向阅读工作流需要可运行的自动化基线
- 🔬 **研究方法**：构建迭代多 agent RAG 系统：生成调查问题，用三阶段检索器（BM25+RM3、cross-encoder 重排、LLM 选择）从 MS MARCO V2.1 取证，信息充分性评估器决定是否续搜，再生成有据可信度报告
- 📌 **结论**：在 TREC 2025 DRAGUN 官方评测 30 篇新闻上报告生成质量第一，最高支持分 0.230、矛盾仅 0.013

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Readers of online news often lack the time and domain expertise required to verify unfamiliar claims and sources. Professional fact-checkers address this gap through lateral reading, an iterative workflow of asking investigative questions, searching for external evidence, and synthesizing findings with attribution. We present an iterative multi-agent Retrieval-Augmented Generation (RAG) system that operationalizes this workflow for the TREC 2025 DRAGUN Track. Given a news article, specialized agents (1) generate investigative queries, (2) retrieve and filter evidence from the MS MARCO V2.1 Segmented Corpus using a three-stage retriever (BM25+RM3, cross-encoder reranking, and LLM-based selection), and (3) apply an information-sufficiency evaluator that decides whether additional searching is required before writing. The final report generator produces a 250-word trustworthiness report grounded in retrieved segments, guided by automatically generated critical investigative questions. On the official DRAGUN rubric-based evaluation with 30 news articles, our system using GPT-4.1 ranked first on report generation quality, achieving the highest mean supportive score (0.230) with low contradiction (0.013). CCS Concepts • Information systems → Retrieval tasks and goals; Web searching and information discovery; • Computing methodologies → Natural language generation; Multi-agent systems. Keywords Text REtrieval Conference; News Trustworthiness; Multi-Agent Systems; Retrieval-Augmented Generation ACM Reference Format: Dake Zhang and Mark D. Smucker. 2026. Simulating the Lateral Reader for News Trustworthiness Reports with an Iterative Multi-Agent RAG System. In Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’26), July 20–24, 2026, Melbourne, VIC, Australia. ACM, New York, NY, USA, 5 pages. https://doi.org/10.1145/ 3805712.3809973

</details>
### 高风险推荐安全

### 31. RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation

🌐 [Project](https://doi.org/10.1145/3805712.3809604)　📅 2026　🏷 SIGIR 2026

**关键词**：`defense`、`medication recommendation`、`risk-aware reasoning`、`clinical safety`、`contraindication risk`、`clinical oversight`

- 🎯 **研究动机**：药物推荐缺风险感知，禁忌等临床风险高
- 🔬 **研究方法**：RES-MR以风险感知推理生成可解释且安全的用药建议
- 📌 **结论**：降低禁忌等临床风险并保持推荐效果