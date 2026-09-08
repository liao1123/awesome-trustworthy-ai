# Citation and Evidence Integrity

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 AI-assisted writing、RAG 和 Deep Research 中的 citation failure。需要区分四个层次：reference 是否真实存在，title/author/year/venue/identifier 等 metadata 是否匹配，URL 是否可访问，以及正文 claim 是否被被引来源真正支持。只做字符串匹配无法发现 miscitation，单纯 LLM-as-a-judge 又可能引入模型偏见，因此可靠系统通常组合 scholarly retrieval、deterministic matching、claim-evidence reasoning、可追溯 tool call 与人工复核。

## 研究脉络

- **现象确认：** 早期实验发现模型会生成不存在的 reference，且内部 confidence 或 sampling signal 有时能暴露错误，但不同模型和领域差异很大。
- **规模化审计：** GhostCite、How LLMs Cite 和真实文献大规模分析从单次生成扩展到会议、preprint 与数据库记录，显示 fabricated citation 已进入正式科学记录且现有 review workflow 很难发现。
- **字段级验证：** CiteAudit、CiteTracer、CiteCheck 和 BibTeX benchmark 将二元存在性判断拆为 retrieval、metadata field matching、错误 taxonomy 和 version-aware verification。
- **Claim-source faithfulness：** CiteGuard、BIBAGENT、Med-V1 和 Deep Research source-attribution evaluation 从 reference existence 推进到 citation 是否适合当前 claim、是否有可替代来源及如何解释 mismatch。
- **修复与部署：** urlhealth、HalluCiteChecker、citecheck MCP 和 clibib 将检测接入 manuscript、Agent 与 conference workflow；关键边界仍是 paywall、动态网页、跨语言来源和 false positive 的人工复核成本。

## 真实世界测量与 Failure Taxonomy

### 1. Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

📄 [arXiv](https://arxiv.org/abs/2608.24306)　📅 2026-08

**关键词**：`analysis`、`detection`、`citation faithfulness`、`agent-level attribution`、`error taxonomy`、`agent invocation`

👤 **作者**：Eran Hirsch、David Wan、Han Wang、Elias Stengel-Eskin、Mohit Bansal、Ido Dagan

- 🎯 **研究动机**：Deep Research 系统引用召回率低，而 final-report 级分数无法定位错误由哪个环节引入
- 🔬 **研究方法**：对每次 agent invocation 相对其自身输入局部检验 faithfulness 与 verifiability，按四类 taxonomy 归类错误
- 📌 **结论**：AI-Q 中 84.7% 终局错误源自 orchestrator；两项简单干预把引用召回提高 5% 且不损质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep research (DR) systems produce long-form cited reports by orchestrating multiple agents that search and synthesize information from the web. Citations are the primary mechanism for evaluating the faithfulness of these reports, yet current DR systems exhibit poor citation recall. Moreover, improving citation recall is challenging because DR systems are complex multi-agent architectures where information passes through agents like a telephone game, and both content and citations can get corrupted along the way. We propose an evaluation method that pinpoints which agent introduced each error by locally testing agent invocations for faithfulness and verifiability relative to their own inputs. Furthermore, we propose a four-type taxonomy to categorize the discovered errors: hallucination, uncited input reliance, uncited output, or insufficient citations. Applying our method to three top-ranked open-source DR systems, we obtain actionable diagnostics. Almost every agent makes a lot of mistakes with the exception being those that summarize a single document. We find that the dominant error type varies systematically across agents, where the orchestrator mistakes are mostly citation-related. We find that 84.7% of final-report errors in AI-Q originate at the orchestrator, roughly 31% of them hallucinations and the rest citation mistakes. Guided by these insights, we demonstrate that two simple interventions raise citation recall by 5% without degrading output quality.

</details>

### 2. Answer First, Evidence Second? Uncovering Hidden Risks in Well-Structured AI Search Summaries

🌐 [Project](https://doi.org/10.1145/3805712.3809913)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`analysis`、`claim-source mismatch`、`citation audit`、`evidence availability`、`AI search`、`citation consistency`

- 🎯 **研究动机**：AI搜索摘要结构规整，但claim与来源的一致性缺审计
- 🔬 **研究方法**：审计citation一致性与evidence grounding，量化claim-source错配与证据可得性
- 📌 **结论**：结构良好的摘要仍普遍存在claim-source错配与证据缺口

### 3. LLM hallucinations in the wild: Large-scale evidence from non-existent citations

📄 [arXiv](https://arxiv.org/abs/2605.07723)　📅 2026-05

**关键词**：`analysis`、`non-existent citation`、`scientific record`、`credit bias`、`physics.soc-ph`

👤 **作者**：Zhenyue Zhao、Yihe Wang、Toby Stuart、Mathijs De Vaan、Paul Ginsparg、Yian Yin

- 🎯 **研究动机**：LLM 幻觉的现实规模与后果缺乏可验证的大规模证据
- 🔬 **研究方法**：审计 arXiv、bioRxiv、SSRN、PubMed Central 上 250 万篇论文的 1.11 亿条引用
- 📌 **结论**：LLM 普及后幻觉引用激增，仅 2025 年保守估计 146,932 条；错误集中于 AI 采纳快的领域、带 AI 写作痕迹的稿件与小团队，且不成比例地把 credit 给知名男性学者；现有审核只拦截少数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are known to generate plausible but false information across a wide range of contexts, yet the real-world magnitude and consequences of this hallucination problem remain poorly understood. Here we leverage a uniquely verifiable object - scientific citations - to audit 111 million references across 2.5 million papers in arXiv, bioRxiv, SSRN, and PubMed Central. We find a sharp rise in non-existent references following widespread LLM adoption, with a conservative estimate of 146,932 hallucinated citations in 2025 alone. These errors are diffusely embedded across many papers but especially pronounced in fields with rapid AI uptake, in manuscripts with linguistic signatures of AI-assisted writing, and among small and early-career author teams. At the same time, hallucinated references disproportionately assign credit to already prominent and male scholars, suggesting that LLM-generated errors may reinforce existing inequities in scientific recognition. Preprint moderation and journal publication processes capture only a fraction of these errors, suggesting that the spread of hallucinated content has outpaced existing safeguards. Together, these findings demonstrate that LLM hallucinations are infiltrating knowledge production at scale, threatening both the reliability and equity of future scientific discovery as human and AI systems draw on the existing literature.

</details>

### 4. Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2605.06635)　📅 2026-05

**关键词**：`analysis`、`source attribution`、`fact check`、`research depth`

👤 **作者**：Hailey Onweller、Elias Lumer、Austin Huber、Pia Ramchandani、Vamse Kumar Subbiah、Corey Feld

- 🎯 **研究动机**：深度研究 agent 的引用无法可靠核验，现有方法要么信任自引要么不验证来源可达性与事实一致性
- 🔬 **研究方法**：首个来源归因评估框架：可复现 AST parser 从 Markdown 报告提取行内引用，检索实际被引内容，从 Link Works、Relevant Content、Fact Check 三维评估 14 个 LLM
- 📌 **结论**：强模型链接有效率超 94%、相关性超 80% 但事实准确仅 39-77%；工具调用从 2 增到 150 时 Fact Check 平均掉约 42%——更多检索并不产生更准引用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) power deep research agents that synthesize information from hundreds of web sources into cited reports, yet these citations cannot be reliably verified. Current approaches either trust models to self-cite accurately, risking bias, or employ retrieval-augmented generation (RAG) that does not validate source accessibility, relevance, or factual consistency. We introduce the first source attribution evaluation framework that uses a reproducible AST parser to extract and evaluate inline citations from LLM-generated Markdown reports at scale. Unlike methods that verify claims in isolation, our framework closes the loop by retrieving the actual cited content, enabling human or model evaluators to judge each citation against its source. Citations are evaluated along three dimensions. (1) Link Works verifies URL accessibility, (2) Relevant Content measures topical alignment, and (3) Fact Check validates factual accuracy against source content. We benchmark 14 closed-source and open-source LLMs across three evaluation dimensions using rubric-based LLM-as-a-judge evaluators calibrated through human review. Our results reveal that even the strongest frontier models maintain link validity above 94% and relevance above 80%, yet achieve only 39-77% factual accuracy, while fewer than half of open-source models successfully generate cited reports in a one-shot setting. Ablation studies on research depth show that Fact Check accuracy drops by approximately 42% on average across two frontier models as tool calls scale from 2 to 150, demonstrating that more retrieval does not produce more accurate citations. These findings reveal a critical disconnect between surface-level citation quality and factual reliability, and our framework provides the evaluation infrastructure to assess the disconnect.

</details>

### 5. Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs

📄 [arXiv](https://arxiv.org/abs/2604.18880)　📅 2026-04

**关键词**：`analysis`、`field-level error`、`hallucination neuron`、`causal intervention`

👤 **作者**：Yuefei Chen、Yihao Quan、Xiaodong Lin、Ruixiang Tang

- 🎯 **研究动机**：引用幻觉的内部机制不明，各字段是否共享同一幻觉信号未知
- 🔬 **研究方法**：分析 9 个模型的 108,000 条生成引用，用弹性网加稳定性选择从 Qwen2.5-32B-Instruct 定位 field-specific 幻觉神经元并做因果干预
- 📌 **结论**：author 字段最易失败、跨字段 probe 近随机；放大 FH-neuron 增加幻觉，抑制则跨字段改善表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLMs frequently generate fictitious yet convincing citations, often expressing high confidence even when the underlying reference is wrong. We study this failure across 9 models and 108{,}000 generated references, and find that author names fail far more often than other fields across all models and settings. Citation style has no measurable effect, while reasoning-oriented distillation degrades recall. Probes trained on one field transfer at near-chance levels to the others, suggesting that hallucination signals do not generalize across fields. Building on this finding, we apply elastic-net regularization with stability selection to neuron-level CETT values of Qwen2.5-32B-Instruct and identify a sparse set of field-specific hallucination neurons (FH-neurons). Causal intervention further confirms their role: amplifying these neurons increases hallucination, while suppressing them improves performance across fields, with larger gains in some fields. These results suggest a lightweight approach to detecting and mitigating citation hallucination using internal model signals alone.

</details>

### 6. GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.06718)　📅 2026-02

**关键词**：`analysis`、`ghost citation`、`venue audit`、`review workflow`

👤 **作者**：Zuyao Xu、…、Jiaji Liu

- 🎯 **研究动机**：LLM 幻觉引用对学术可信的系统性威胁缺少跨模型、论文与人因的联合量化
- 🔬 **研究方法**：开源 CiteB 框架：评测 13 个 LLM 的引用生成、审计 56,381 篇 AI/ML 与安全会议论文的 220 万条引用、调查 97 名研究者
- 📌 **结论**：模型幻觉率 14.23%-94.93%；1.07% 论文含无效引用且 2025 年增 80.9%；76.7% 审稿人不细查参考文献

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Citations provide the basis for trusting scientific claims; when they are invalid or fabricated, this trust collapses. With the advent of Large Language Models (LLMs), this risk has intensified: LLMs are increasingly used for academic writing, but their tendency to fabricate citations (``ghost citations'') poses a systemic threat to citation validity. To quantify this threat, we develop \citeb, an open-source framework for large-scale citation verification, and conduct a comprehensive study of citation validity in the LLM era through three complementary experiments. First, we benchmark 13 LLMs on citation generation task in various research domains, finding that all models hallucinate citations at rate from 14.23\% to 94.93\%. Second, we analyze 2.2 million citations from 56,381 papers at AI/ML and Security venues (2020--2025), finding that 1.07\% of papers contain invalid citations, with an 80.9\% increase in 2025. Third, we survey 97 researchers, finding that 87.2\% use AI-powered tools in their workflows, 76.7\% of reviewers do not thoroughly check references, and 74.5\% view peer review as ineffective at catching citation errors. Based on these findings, we argue that ghost citations represent a systemic threat to academic integrity, and call for coordinated efforts from community to address this challenge.

</details>

### 7. Compound Deception in Elite Peer Review: A Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025

📄 [arXiv](https://arxiv.org/abs/2602.05930)　📅 2026-02

**关键词**：`analysis`、`compound deception`、`identifier hijacking`、`peer-review failure`

👤 **作者**：Samar Ansari

- 🎯 **研究动机**：LLM 幻觉引用已进入顶会论文，同行评审为何检测失效缺少结构化解释
- 🔬 **研究方法**：人工分析 NeurIPS 2025 中 100 条 AI 幻觉引用（涉及 53 篇录用论文），建立五类失效模式分类法
- 📌 **结论**：全部 100% 样本呈复合失效模式，Total Fabrication 占 66%；8% 论文含 4-13 条幻觉，建议投稿时强制自动引用核验

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used in academic writing workflows, yet they frequently hallucinate by generating citations to sources that do not exist. This study analyzes 100 AI-generated hallucinated citations that appeared in papers accepted by the 2025 Conference on Neural Information Processing Systems (NeurIPS), one of the world's most prestigious AI conferences. Despite review by 3-5 expert researchers per paper, these fabricated citations evaded detection, appearing in 53 published papers (approx. 1% of all accepted papers). We develop a five-category taxonomy that classifies hallucinations by their failure mode: Total Fabrication (66%), Partial Attribute Corruption (27%), Identifier Hijacking (4%), Placeholder Hallucination (2%), and Semantic Hallucination (1%). Our analysis reveals a critical finding: every hallucination (100%) exhibited compound failure modes. The distribution of secondary characteristics was dominated by Semantic Hallucination (63%) and Identifier Hijacking (29%), which often appeared alongside Total Fabrication to create a veneer of plausibility and false verifiability. These compound structures exploit multiple verification heuristics simultaneously, explaining why peer review fails to detect them. The distribution exhibits a bimodal pattern: 92% of contaminated papers contain 1-2 hallucinations (minimal AI use) while 8% contain 4-13 hallucinations (heavy reliance). These findings demonstrate that current peer review processes do not include effective citation verification and that the problem extends beyond NeurIPS to other major conferences, government reports, and professional consulting. We propose mandatory automated citation verification at submission as an implementable solution to prevent fabricated citations from becoming normalized in scientific literature.

</details>

### 8. How LLMs Cite and Why It Matters: A Cross-Model Audit of Reference Fabrication in AI-Assisted Academic Writing and Methods to Detect Phantom Citations

📄 [arXiv](https://arxiv.org/abs/2603.03299)　📅 2026-02

**关键词**：`analysis`、`phantom citation`、`cross-model audit`、`bibliographic classifier`

👤 **作者**：MZ Naser

- 🎯 **研究动机**：引用伪造行为跨 provider、领域与提示条件的规模缺少大样本量化
- 🔬 **研究方法**：10 个商用 LLM 在四个学术域生成 69,557 条引用，对照 CrossRef、OpenAlex、Semantic Scholar 核验，并训练仅用书目字符串特征的分类器
- 📌 **结论**：幻觉率 11.4%-56.8% 且系提示诱发；多模型共识（3+ 同引达 95.6% 准确）与重复出现可作高精度筛选；分类器 AUC 0.876

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have been noted to fabricate scholarly citations, yet the scope of this behavior across providers, domains, and prompting conditions remains poorly quantified. We present one of the largest citation hallucination audits to date, in which 10 commercially deployed LLMs were prompted across four academic domains, generating 69,557 citation instances verified against three scholarly databases (namely, CrossRef, OpenAlex, and Semantic Scholar). Our results show that the observed hallucination rates span a fivefold range (between 11.4% and 56.8%) and are strongly shaped by model, domain, and prompt framing. Our results also show that no model spontaneously generates citations when unprompted, which seems to establish hallucination as prompt-induced rather than intrinsic. We identify two practical filters: 1) multi-model consensus (with more than 3 LLMs citing the same work yields 95.6% accuracy, a 5.8-fold improvement), and 2) within-prompt repetition (with more than 2 replications yields 88.9% accuracy). In addition, we present findings on generational model tracking, which reveal that improvements are not guaranteed when deploying newer LLMs, and on capacity scaling, which appears to reduce hallucination within model families. Finally, a lightweight classifier trained solely on bibliographic string features is developed to classify hallucinated citations from verified citations, achieving AUC 0.876 in cross-validation and 0.834 in LOMO generalization (without querying any external database). This classifier offers a pre-screening tool deployable at inference time.

</details>

### 9. HalluCitation Matters: Revealing the Impact of Hallucinated References with 300 Hallucinated Papers in ACL Conferences

📄 [arXiv](https://arxiv.org/abs/2601.18724) · 🎓 [Official](https://aclanthology.org/2026.acl-long.2189/)　📅 2026-01　🏷 ACL 2026

**关键词**：`analysis`、`ACL papers`、`reference impact`、`manual audit`

👤 **作者**：Yusuke Sakai、Hidetaka Kamigaito、Taro Watanabe

- 🎯 **研究动机**：幻觉引用对学术论文与会议可信度的影响缺乏系统量化
- 🔬 **研究方法**：分析 2024-2025 年 ACL、NAACL、EMNLP 全部论文（含主会、Findings 与 workshop）中不存在对应文献的 HalluCitation
- 📌 **结论**：近 300 篇论文含至少一条幻觉引用且多为 2025 年发表，其中一半出现在 EMNLP 2025；超 100 篇被主会与 Findings 接收，问题快速增长

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, we have often observed hallucinated citations or references that do not correspond to any existing work in papers under review, preprints, or published papers. Such hallucinated citations pose a serious concern to scientific reliability. When they appear in accepted papers, they may also negatively affect the credibility of conferences. In this study, we refer to hallucinated citations as "HalluCitation" and systematically investigate their prevalence and impact. We analyze all papers published at ACL, NAACL, and EMNLP in 2024 and 2025, including main conference, Findings, and workshop papers. Our analysis reveals that nearly 300 papers contain at least one HalluCitation, most of which were published in 2025. Notably, half of these papers were identified at EMNLP 2025, the most recent conference, indicating that this issue is rapidly increasing. Moreover, more than 100 such papers were accepted as main conference and Findings papers at EMNLP 2025, affecting the credibility.

</details>

### 10. Do Language Models Know When They're Hallucinating References?

🎓 [Official](https://aclanthology.org/2024.findings-emnlp.904/)　📅 2024-11　🏷 EMNLP 2024

**关键词**：`analysis`、`reference hallucination`、`uncertainty signal`、`self-knowledge`

👤 **作者**：Chuhan Li、Ziyao Shangguan、Yilun Zhao、Deyuan Li、Yixin Liu、Arman Cohan

- 🎯 **研究动机**：现有科学文献理解基准多为单文档纯文本任务，未反映涉及图表等多模态与跨文档信息的研究工作流
- 🔬 **研究方法**：M3SciQA 多模态多文档科学 QA 基准：1452 道专家标注问题覆盖 70 个 NLP 论文簇（主论文及其引文），评测 18 个前沿基础模型
- 📌 **结论**：当前基础模型在多模态信息检索与跨多文档推理上仍显著逊于人类专家

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing evaluation benchmarks for foundation models in understanding scientific literature predominantly focus on single-document, text-only tasks. Such benchmarks often do not adequately represent the complexity of research workflows, which typically also involve interpreting non-textual data, such as figures and tables, and gathering information across multiple documents and related literature. To address this gap, we introduce M3SciQA, a multi-modal, multi-document scientific question answering benchmark designed for a more comprehensive evaluation of foundation models. M3Sci QA consists of 1452 expert-annotated questions spanning 70 natural language processing paper clusters, where each cluster represents a primary paper along with all its cited documents, mirroring the workflow of comprehending a single paper by requiring multi-modal and multi-document data. With M3SciQA, we conduct a comprehensive evaluation of 18 frontier foundation models. Our results indicate that current foundation models still significantly underperform compared to human experts in multi-modal information retrieval and in reasoning across multiple scientific documents. Additionally, we explore the implications of these findings for the future advancement of applying foundation models in multi-modal scientific literature analysis.

</details>

### 11. CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text

📄 [arXiv](https://arxiv.org/abs/2605.27700)　📅 2026-05

**关键词**：`detection`、`scholarly retrieval`、`metadata drift`、`calibrated verifier`

👤 **作者**：Khashayar Khajavi、Shaghayegh Sadeghi、Rise Adhikari、Alexander Tessier

- 🎯 **研究动机**：LLM 生成的引用可能元数据被破坏或指向不存在的论文，需同时验证真实性与忠实性
- 🔬 **研究方法**：CiteCheck 检索候选文献、结构化 LLM verifier 对比引用与候选，映射到 Exact、Minor、Major 三级标签；构建 982 条含受控损坏的物理引用基准
- 📌 **结论**：留出集上 88.7 macro-F1、88.9% 准确率，超过 GPT、Claude、Gemini 含 web search 与 few-shot 的变体

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used to generate scientific reports, but they can produce references that appear plausible while containing corrupted metadata or pointing to papers that do not exist. We introduce CiteCheck, a hybrid framework for citation hallucination detection that verifies whether a citation corresponds to a real scholarly work and whether its metadata is faithful to that work. CiteCheck retrieves candidate publications from external scholarly sources, compares the citation against the retrieved candidate using a structured LLM verifier, and maps verifier scores into three labels: Exact, Minor, and Major. We also construct a 982-citation physics benchmark with controlled corruptions that capture both subtle metadata drift and fully fabricated references. On the held-out test set, CiteCheck achieves 88.7 macro-F1 and 88.9% accuracy, outperforming GPT, Claude, and Gemini baselines, including web-search and few-shot variants. These results show that reliable citation verification benefits from combining scholarly retrieval, structured LLM-based comparison, and calibrated decision rules.

</details>

### 12. Source or It Didn't Happen: A Multi-Agent Framework for Citation Hallucination Detection

📄 [arXiv](https://arxiv.org/abs/2605.08583)　📅 2026-05

**关键词**：`detection`、`CiteTracer`、`field adjudication`、`evidence routing`

👤 **作者**：Mingzhe Li、Zhiqiang Lin、Shiqing Ma

- 🎯 **研究动机**：现有引用幻觉检测止于 found/not-found 二值判定，缺字段级信号与可追溯证据
- 🔬 **研究方法**：以 12 编码 taxonomy（Real、Potential、Hallucinated）驱动 CiteTracer 级联多智能体：PDF 与 BibTeX 结构化抽取、cache/URL/学术连接器/web 检索、确定性字段匹配与专家 judge 路由
- 📌 **结论**：合成基准 97.1% 准确率（三类 F1 97.0/95.8/98.5），并检出 97.1% 真实伪造引用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are increasingly used in scientific writing, yet they can fabricate citation-shaped references that appear plausible but fail bibliographic verification. Existing detectors often reduce verification to binary found/not-found decisions and rely on brittle parsing or incomplete retrieval, offering little field-level signal to auditors. We reframe citation hallucination detection as taxonomy-aligned field-level adjudication and introduce a 12-code taxonomy spanning Real, Potential, and Hallucinated citations. Based on this taxonomy, we build CiteTracer, a cascading multi-agent detector that extracts structured citations from PDF and BibTeX, retrieves evidence through cache lookup, URL fetch, scholar connectors, and web search, applies deterministic field matching, and routes ambiguous cases to class-specialist judgers. We release a benchmark of 2,450 synthetic citations built from real seeds with controlled LLM mutations, paired with 957 real-world fabricated citations drawn from ICLR 2026 and an anonymous conference desk-rejected submissions. CiteTracer reaches 97.1% accuracy on the synthetic benchmark, with class-level F1 scores of 97.0, 95.8, and 98.5 for Real, Potential, and Hallucinated, respectively, and detects 97.1% of fabrications on the real-world set without abstaining. Code: https://github.com/aaFrostnova/CiteTracer.

</details>

### 13. HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists

📄 [arXiv](https://arxiv.org/abs/2604.26835)　📅 2026-04

**关键词**：`tool`、`offline verification`、`CPU toolkit`、`pre-review screening`

👤 **作者**：Yusuke Sakai、Hidetaka Kamigaito、Taro Watanabe

- 🎯 **研究动机**：AI 写作助手催生不存在的幻觉引用，reviewer 手工验证成本高
- 🔬 **研究方法**：将幻觉引用检测形式化为 NLP 任务并提供轻量 toolkit，可在标准笔记本秒级完成验证，支持完全离线与纯 CPU 运行
- 📌 **结论**：为系统化 pre-review 筛查与出版检查提供实用基础

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce HalluCiteChecker, a toolkit for detecting and verifying hallucinated citations in scientific papers. While AI assistant technologies have transformed the academic writing process, including citation recommendation, they have also led to the emergence of hallucinated citations that do not correspond to any existing work. Such citations not only undermine the credibility of scientific papers but also impose an additional burden on reviewers and authors, who must manually verify their validity during the review process. In this study, we formalize hallucinated citation detection as an NLP task and provide a corresponding toolkit as a practical foundation for addressing this problem. Our package is lightweight and can perform verification in seconds on a standard laptop. It can also be executed entirely offline and runs efficiently using only CPUs. We hope that HalluCiteChecker will help reduce reviewer workload and support organizers by enabling systematic pre-review and publication checks. Our code is released under the Apache 2.0 license on GitHub and is distributed as an installable package via PyPI. A demonstration video is available on YouTube.

</details>

### 14. Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2604.03173)　📅 2026-04

**关键词**：`tool`、`URL validity`、`Wayback Machine`、`agentic correction`

👤 **作者**：Delip Rao、Eric Wong、Chris Callison-Burch

- 🎯 **研究动机**：引用 URL 的可靠性从未被系统测量，且失效可能来自幻觉或 link rot
- 🔬 **研究方法**：用 10 个模型在 DRBench（53,090 URL）与 ExpertQA（168,021 URL）上测 URL 有效性，发布基于 Wayback Machine 的 urlhealth 工具并做 agentic 自纠实验
- 📌 **结论**：3%-13% 引用 URL 疑似从未存在、5%-18% 不可解析，深度研究 agent 幻觉率更高；配备 urlhealth 后不可解析 URL 降 6-79 倍至 1% 以下

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models and deep research agents supply citation URLs to support their claims, yet the reliability of these citations has not been systematically measured. We address six research questions about citation URL validity using 10 models and agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs across 32 academic fields). We find that 3--13\% of citation URLs are hallucinated -- they have no record in the Wayback Machine and likely never existed -- while 5--18\% are non-resolving overall. Deep research agents generate substantially more citations per query than search-augmented LLMs but hallucinate URLs at higher rates. Domain effects are pronounced: non-resolving rates range from 5.4\% (Business) to 11.4\% (Theology), with per-model effects even larger. Decomposing failures reveals that some models fabricate every non-resolving URL, while others show substantial link-rot fractions indicating genuine retrieval. As a solution, we release urlhealth, an open-source tool for URL liveness checking and stale-vs-hallucinated classification using the Wayback Machine. In agentic self-correction experiments, models equipped with urlhealth reduce non-resolving citation URLs by $6\textrm{--}79\times$ to under 1\%, though effectiveness depends on the model's tool-use competence. The tool and all data are publicly available. Our characterization findings, failure taxonomy, and open-source tooling establish that citation URL validity is both measurable at scale and correctable in practice.

</details>

### 15. BibTeX Citation Hallucinations in Scientific Publishing Agents: Evaluation and Mitigation

📄 [arXiv](https://arxiv.org/abs/2604.03159) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04　🏷 COLM 2026

**关键词**：`benchmark`、`defense`、`BibTeX metadata`、`version-aware ground truth`、`clibib`、`scientific agent`

👤 **作者**：Delip Rao、Chris Callison-Burch

- 🎯 **研究动机**：科学出版 agent 生成的 BibTeX 存在普遍字段级错误，缺基准与缓解机制
- 🔬 **研究方法**：构建 931 篇论文、三引用层级的基准，三个前沿模型产生约 23,000 个字段级观测；发布确定性 BibTeX 检索工具 clibib 并做两阶段集成
- 📌 **结论**：总体准确率 83.6% 但全对仅 50.9%，流行到新论文下降 27.7 个百分点；clibib 把准确率提至 91.5%，检索与修订分离优于单阶段工具循环

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models with web search are increasingly used in scientific publishing agents, yet they produce BibTeX entries with pervasive field-level errors stemming from omission, partial corruption, substitution, and hallucination. We construct a benchmark of 931 papers across four domains and three citation tiers---popular, low-citation, and recent post-cutoff---with version-aware ground truth. Three search-enabled frontier models (GPT-5, Claude Sonnet-4.6, Gemini-3 Flash) generate approximately 23,000 field-level observations. Overall accuracy is 83.6%, but only 50.9% of entries are fully correct; accuracy drops 27.7 pp from popular to recent papers, revealing heavy reliance on parametric memory even when search is available. Co-occurrence analysis identifies two failure modes: wholesale entry substitution and isolated field error. We present clibib, an open-source tool for deterministic BibTeX retrieval, as a mitigation mechanism. Two-stage integration raises accuracy to 91.5% (+8.0 pp) and fully correct entries to 78.3%, with a 0.8% regression rate. Separating search from revision yields larger gains and lower regression than single-stage tool loops (0.8% vs. 4.8%), demonstrating that integration architecture matters independently of model/tool capability. We release clibib and an accompanying agent skill under the MIT License to improve citation accuracy in increasingly automated scientific workflows.

</details>

### 16. citecheck: An MCP Server for Automated Bibliographic Verification and Repair in Scholarly Manuscripts

📄 [arXiv](https://arxiv.org/abs/2603.17339)　📅 2026-03

**关键词**：`tool`、`MCP server`、`bibliography repair`、`rewrite safety`

👤 **作者**：Junhyeok Lee

- 🎯 **研究动机**：手稿参考文献错误繁多且 LLM 工作流加剧幻觉引用，人工修复繁琐
- 🔬 **研究方法**：citecheck MCP server 从 .bib/.tex/.md/.docx 提取引用，对照 PubMed、Crossref、arXiv 与 Semantic Scholar 验证，返回结构化修复建议与替换安全诊断
- 📌 **结论**：原型以 47 个测试覆盖修复行为、异常处理与 MCP 暴露，可作 agentic 学术编辑的护栏基础设施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reference lists in scholarly manuscripts frequently contain errors, including incorrect identifiers, incomplete metadata, misattributed authors, and mismatches between preprint and published versions. These problems are tedious to repair manually and have become more visible in workflows that rely on large language models, which can fabricate or corrupt citations. We present citecheck, a TypeScript system and MCP server for automated bibliographic verification and repair in paper-like project folders. Given a manuscript file or workspace, citecheck selects the most likely paper artifact, extracts references from .bib, .tex, .md, .txt, or .docx, validates entries against PubMed, Crossref, arXiv, and Semantic Scholar, and returns structured correction proposals together with replacement-safety diagnostics. The current repository provides a working research prototype with multi-pass retrieval, manifestation-aware matching, policy-gated rewrite planning, and 47 passing tests covering repair behavior, malformed payload handling, transport failures, and MCP exposure. We position citecheck as infrastructure for agentic scholarly editing and as a practical guardrail against both traditional reference errors and LLM-induced citation hallucinations.

</details>

### 17. CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era

📄 [arXiv](https://arxiv.org/abs/2602.23452)　📅 2026-02

**关键词**：`benchmark`、`multi-agent audit`、`metadata verification`、`human validation`

👤 **作者**：Kaiwen Shi、Weixiang Sun、Zheyuan Zhang、Lichao Sun、Nitesh V. Chawla、Yanfang Ye

- 🎯 **研究动机**：幻觉引用的人工核验不可扩展，现有自动工具脆弱
- 🔬 **研究方法**：CiteAudit 用多 agent 管线把引用核查分解为元数据抽取、记忆查找、web 检索与最终判断，并构建人工验证的多领域数据集
- 📌 **结论**：核验性能优于 SOTA LLM 与商业基线，提供大规模引用审计基础设施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scientific research relies on citation integrity, yet large language models (LLMs) have introduced a critical risk: fabricated references that appear plausible but correspond to no real publications. As manual verification becomes infeasible and existing automated tools remain fragile, we introduce CiteAudit, a comprehensive benchmark and detection framework for hallucinated citations. We design a multi-agent verification pipeline that decomposes citation checking into metadata extraction, memory lookup, web-based retrieval, and final judgment. To evaluate this, we construct a large-scale, human-validated dataset spanning diverse domains and hallucination types. Experiments demonstrate that our framework achieves superior verification performance over state-of-the-art LLMs and commercial baselines. Our work provides the necessary infrastructure to audit citations at scale and safeguard the trustworthiness of scholarly discourse. Code is available at https://github.com/shiiiikw/CiteAudit.

</details>

### 18. CheckIfExist: Detecting Citation Hallucinations in the Era of AI-Generated Content

📄 [arXiv](https://arxiv.org/abs/2602.15871)　📅 2026-01

**关键词**：`detection`、`reference existence`、`bibliographic lookup`、`academic integrity`

👤 **作者**：Diletta Abbonato

- 🎯 **研究动机**：AI 幻觉引用已渗入 NeurIPS、ICLR 等顶会论文，现有工具不能实时验证参考文献真实性
- 🔬 **研究方法**：开源工具 CheckIfExist 级联查询 CrossRef、Semantic Scholar 与 OpenAlex，以字符串相似度计算多维匹配置信度
- 📌 **结论**：支持单条与 BibTeX 批量验证，数秒内返回真实性与可导出的规范引用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The proliferation of large language models (LLMs) in academic workflows has introduced unprecedented challenges to bibliographic integrity, particularly through reference hallucination -- the generation of plausible but non-existent citations. Recent investigations have documented the presence of AI-hallucinated citations even in papers accepted at premier machine learning conferences such as NeurIPS and ICLR, underscoring the urgency of automated verification mechanisms. This paper presents "CheckIfExist", an open-source web-based tool designed to provide immediate verification of bibliographic references through multi-source validation against CrossRef, Semantic Scholar, and OpenAlex scholarly databases. While existing reference management tools offer bibliographic organization capabilities, they do not provide real-time validation of citation authenticity. Commercial hallucination detection services, though increasingly available, often impose restrictive usage limits on free tiers or require substantial subscription fees. The proposed tool fills this gap by employing a cascading validation architecture with string similarity algorithms to compute multi-dimensional match confidence scores, delivering instant feedback on reference authenticity. The system supports both single-reference verification and batch processing of BibTeX entries through a unified interface, returning validated APA citations and exportable BibTeX records within seconds.

</details>

### 19. FACTUM: Mechanistic Detection of Citation Hallucination in Long-Form RAG

📄 [arXiv](https://arxiv.org/abs/2601.05866)　📅 2026-01

**关键词**：`detection`、`RAG attribution`、`mechanistic score`、`pathway alignment`

👤 **作者**：Maxime Dassen、…、Kevin Duh

- 🎯 **研究动机**：引用幻觉被简单归因于参数知识过度依赖，其内在机制与规模依赖性不明
- 🔬 **研究方法**：把失败重构为 Attention（读取）与 FFN（回忆）通路随规模演化的协调失败，提出 CAS、BAS、PFS、PAS 四个机制分数做检测
- 📌 **结论**：正确引用的内部签名随规模演变，FACTUM 的 AUC 超 SOTA 基线最多 37.5%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) models are critically undermined by citation hallucinations, a deceptive failure where a model cites a source that fails to support its claim. While existing work attributes hallucination to a simple over-reliance on parametric knowledge, we reframe this failure as an evolving, scale-dependent coordination failure between the Attention (reading) and Feed-Forward Network (recalling) pathways. We introduce FACTUM (Framework for Attesting Citation Trustworthiness via Underlying Mechanisms), a framework of four mechanistic scores: Contextual Alignment (CAS), Attention Sink Usage (BAS), Parametric Force (PFS), and Pathway Alignment (PAS). Our analysis reveals that correct citations are consistently marked by higher parametric force (PFS) and greater use of the attention sink (BAS) for information synthesis. Crucially, we find that "one-size-fits-all" theories are insufficient as the signature of correctness evolves with scale: while the 3B model relies on high pathway alignment (PAS), our best-performing 8B detector identifies a shift toward a specialized strategy where pathways provide distinct, orthogonal information. By capturing this complex interplay, FACTUM outperforms state-of-the-art baselines by up to 37.5% in AUC. Our results demonstrate that high parametric force is constructive when successfully coordinated with the Attention pathway, paving the way for more nuanced and reliable RAG systems.

</details>

### 20. HalluPeer: A Taxonomy-driven Benchmark for Detecting Hallucinations in Scientific Peer Reviews

📄 [arXiv](https://arxiv.org/abs/2609.03580)　📅 2026-09

**关键词**：`benchmark`、`peer-review hallucination`、`source grounding`、`claim localization`、`claim-source verification`、`review provenance`

👤 **作者**：Tzu-Ling Lin、Dong-Ting Yao、Teng-Fang Hsiao、Wei-Chih Chen、Hong-Han Shuai

- 🎯 **研究动机**：LLM 评审助手会生成流畅但无依据的批评，而现有幻觉 benchmark 不适配长技术论文的评审核验场景
- 🔬 **研究方法**：构建 HalluPeer：论文内容、人工评审与幻觉注入评审的对齐三元组，标注检测、分类与定位；管线先归纳评审特定幻觉分类、识别评审语境再自动过滤注入
- 📌 **结论**：在 12K 论文、38K 评审上现有检测器难以区分幻觉与正当批评；真实评审中也出现 HalluPeer 定义的幻觉模式，凸显溯源感知核验的必要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing scale of academic peer review has motivated the use of Large Language Models (LLMs) as review assistants, yet LLMs can generate fluent but unsupported claims that undermine review reliability. Existing hallucination benchmarks are not designed for peer review, where verification requires grounding claims in long, technical papers. We introduce HalluPeer, a benchmark for detecting hallucinations in scientific peer reviews, providing aligned triples of paper content, human-written reviews, and hallucination-injected reviews, annotated for detection, classification, and localization. Our pipeline induces a peer-review-specific hallucination taxonomy, identifies review contexts, and injects hallucinations with automated filtering. Experiments on 12K papers and 38K reviews show that existing detectors struggle to separate hallucinations from legitimate critique, while evaluation on authentic reviews demonstrates that HalluPeer-defined hallucination patterns occur in real peer reviews, highlighting the critical need for source-aware verification. Our project page can be found in https://github.com/Lin-TzuLing/HalluPeer.git

</details>

### 21. CiteGuard: Faithful Citation Attribution for LLMs via Retrieval-Augmented Validation

🎓 [Official](https://aclanthology.org/2026.acl-long.282/)　📅 2026-07　🏷 ACL 2026

**关键词**：`defense`、`citation attribution`、`retrieval validation`、`alternative source`

👤 **作者**：Yee Man Choi、Xuehang Guo、Yi R. Fung、Qingyun Wang

- 🎯 **研究动机**：科学写作的引用准确性与忠实性存疑，LLM-as-a-Judge 本身可靠性可疑
- 🔬 **研究方法**：把引用评价重构为引用归属对齐问题（LLM 引用是否与人类作者会给的引用一致），提出检索感知 agent 框架 CiteGuard
- 📌 **结论**：CiteME 上准确率达 68.1%、比先前基线高 10 个百分点并接近人类 69.2%，可识别替代有效引用并跨域泛化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have emerged as powerful assistants for scientific writing. However, concerns remain about the quality and reliability of the generated text, including citation accuracy and faithfulness. While most recent work relies on methods such as LLM-as-a-Judge, the reliability of LLM-as-a-Judge alone is also in doubt. In this work, we reframe citation evaluation as a problem of citation attribution alignment, which assesses whether LLM-generated citations match those a human author would include for the same text. We propose CiteGuard, a retrieval-aware agent framework designed to provide more faithful grounding for citation validation. CiteGuard improves over the prior baseline by 10 percentage points and achieves up to 68.1% accuracy on the CiteME benchmark, approaching human performance (69.2%). It also identifies alternative valid citations and demonstrates generalization ability for cross-domain citation attribution.

</details>

### 22. Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution

📄 [arXiv](https://arxiv.org/abs/2603.05308)　📅 2026-03

**关键词**：`detection`、`biomedical evidence`、`claim support`、`small model`

👤 **作者**：Qiao Jin、…、Zhiyong Lu

- 🎯 **研究动机**：生物医学证据归属依赖 GPT-5 级昂贵模型，难以规模化部署
- 🔬 **研究方法**：用高质量合成数据训练 3B 的 Med-V1，把五个生物医学基准统一为验证格式，并开展引用指令与临床指南两个用例研究
- 📌 **结论**：超基座模型 27.0%-71.3%、媲美 GPT-5；发现引用格式指令强烈影响幻觉率，并自动识别临床指南中的高风险证据误归属

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Assessing whether an article supports an assertion is essential for hallucination detection and claim verification. While large language models (LLMs) have the potential to automate this task, achieving strong performance requires frontier models such as GPT-5 that are prohibitively expensive to deploy at scale. To efficiently perform biomedical evidence attribution, we present Med-V1, a family of small language models with only three billion parameters. Trained on high-quality synthetic data newly developed in this study, Med-V1 substantially outperforms (+27.0% to +71.3%) its base models on five biomedical benchmarks unified into a verification format. Despite its smaller size, Med-V1 performs comparably to frontier LLMs such as GPT-5, along with high-quality explanations for its predictions. We use Med-V1 to conduct a first-of-its-kind use case study that quantifies hallucinations in LLM-generated answers under different citation instructions. Results show that the format instruction strongly affects citation validity and hallucination, with GPT-5 generating more claims but exhibiting hallucination rates similar to GPT-4o. Additionally, we present a second use case showing that Med-V1 can automatically identify high-stakes evidence misattributions in clinical practice guidelines, revealing potentially negative public health impacts that are otherwise challenging to identify at scale. Overall, Med-V1 provides an efficient and accurate lightweight alternative to frontier LLMs for practical and real-world applications in biomedical evidence attribution and verification tasks. Med-V1 is available at https://github.com/ncbi-nlp/Med-V1.

</details>

### 23. BIBAGENT: An Agentic Framework for Traceable Miscitation Detection in Scientific Literature

📄 [arXiv](https://arxiv.org/abs/2601.16993)　📅 2026-01

**关键词**：`detection`、`miscitation`、`Evidence Committee`、`traceable reasoning`

👤 **作者**：Peiran Li、…、Chaoqun Ni

- 🎯 **研究动机**：引用核验受全文付费墙与出版规模限制，现有工具止于摘要分析或小规模领域数据
- 🔬 **研究方法**：BibAgent 集成检索、推理与自适应证据聚合，对付费墙文献用 Evidence Committee 依据下游引用共识推断有效性；配套五类误引分类法与 6350 样本、254 领域的 MisciteBench
- 📌 **结论**：引用核验准确率与可解释性超越 SOTA LLM 基线，实现跨学科可扩展的误引检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Citations are the bedrock of scientific authority, yet their integrity is compromised by widespread miscitations: ranging from nuanced distortions to fabricated references. Systematic citation verification is currently unfeasible; manual review cannot scale to modern publishing volumes, while existing automated tools are restricted by abstract-only analysis or small-scale, domain-specific datasets in part due to the "paywall barrier" of full-text access. We introduce BibAgent, a scalable, end-to-end agentic framework for automated citation verification. BibAgent integrates retrieval, reasoning, and adaptive evidence aggregation, applying distinct strategies for accessible and paywalled sources. For paywalled references, it leverages a novel Evidence Committee mechanism that infers citation validity via downstream citation consensus. To support systematic evaluation, we contribute a 5-category Miscitation Taxonomy and MisciteBench, a massive cross-disciplinary benchmark comprising 6,350 miscitation samples spanning 254 fields. Our results demonstrate that BibAgent outperforms state-of-the-art Large Language Model (LLM) baselines in citation verification accuracy and interpretability, providing scalable, transparent detection of citation misalignments across the scientific literature.

</details>

### 24. ScholarCopilot: Training Large Language Models for Academic Writing with Accurate Citations

📄 [arXiv](https://arxiv.org/abs/2504.00824)　📅 2025-04

**关键词**：`defense`、`academic writing`、`citation generation`、`evidence grounding`

👤 **作者**：Yubo Wang、…、Wenhu Chen

- 🎯 **研究动机**：通用 RAG 难以支撑专业学术写作的精确引用需求
- 🔬 **研究方法**：提出 ScholarCopilot，通过生成 [RET] token 动态触发引文检索，联合优化生成与引用两个任务
- 📌 **结论**：基于 Qwen-2.5-7B 与 500K arXiv 论文训练，top-1 检索准确率 40.1%（E5-Mistral 为 15.0%），引用质量人类偏好全面胜 ChatGPT

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Academic writing requires both coherent text generation and precise citation of relevant literature. Although recent Retrieval-Augmented Generation (RAG) systems have significantly improved factual accuracy in general-purpose text generation, their ability to support professional academic writing remains limited. In this work, we introduce ScholarCopilot, a unified framework designed to enhance existing large language models for generating professional academic articles with accurate and contextually relevant citations. ScholarCopilot dynamically determines when to retrieve scholarly references by generating a retrieval token [RET], which is then used to query a citation database. The retrieved references are fed into the model to augment the generation process. We jointly optimize both the generation and citation tasks within a single framework to improve efficiency. Our model is built upon Qwen-2.5-7B and trained on 500K papers from arXiv. It achieves a top-1 retrieval accuracy of 40.1% on our evaluation dataset, outperforming baselines such as E5-Mistral-7B-Instruct (15.0%) and BM25 (9.8%). On a dataset of 1,000 academic writing samples, ScholarCopilot scores 16.2/25 in generation quality -- measured across relevance, coherence, academic rigor, completeness, and innovation -- significantly surpassing all existing models, including much larger ones like the Retrieval-Augmented Qwen2.5-72B-Instruct. Human studies further demonstrate that ScholarCopilot, despite being a 7B model, significantly outperforms ChatGPT, achieving 100% preference in citation quality and over 70% in overall usefulness.

</details>

### 25. CiteCheck: Towards Accurate Citation Faithfulness Detection

📄 [arXiv](https://arxiv.org/abs/2502.10881)　📅 2025-02

**关键词**：`detection`、`citation faithfulness`、`claim evidence`、`evaluation protocol`

👤 **作者**：Ziyao Xu、…、Houfeng Wang

- 🎯 **研究动机**：中文引用忠实度检测缺少大规模数据集，人工标注负样本成本高昂
- 🔬 **研究方法**：以两阶段人工标注加 LLM 生成负样本增强的成本高效方式构建首个大规模中文数据集 CiteCheck
- 📌 **结论**：测试集极具挑战、SOTA LLM 也难达高准确率；LLM 负样本增强让小模型经 PEFT 获得强性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Citation faithfulness detection is critical for enhancing retrieval-augmented generation (RAG) systems, yet large-scale Chinese datasets for this task are scarce. Existing methods face prohibitive costs due to the need for manually annotated negative samples. To address this, we introduce the first large-scale Chinese dataset CiteCheck for citation faithfulness detection, constructed via a cost-effective approach using two-stage manual annotation. This method balances positive and negative samples while significantly reducing annotation expenses. CiteCheck comprises training and test splits. Experiments demonstrate that: (1) the test samples are highly challenging, with even state-of-the-art LLMs failing to achieve high accuracy; and (2) training data augmented with LLM-generated negative samples enables smaller models to attain strong performance using parameter-efficient fine-tuning. CiteCheck provides a robust foundation for advancing citation faithfulness detection in Chinese RAG systems. The dataset is publicly available to facilitate research.

</details>

### 26. SciTrue: Reliable Scientific Claim Validation with Frontier and Open Language Models at the NTCIR SciClaimEval Task

📄 [arXiv](https://arxiv.org/abs/2609.00654)　📅 2026-09

**关键词**：`benchmark`、`scientific claim verification`、`multimodal evidence`、`measurement leak`

👤 **作者**：Qiming Bao、Neşet Özkan Tan、Siyuan Wang、Mark Gahegan

- 🎯 **研究动机**：科学声明需对照论文表格图形验证，且数据包装本身可能泄露标签（measurement leak）
- 🔬 **研究方法**：在 NTCIR-19 SciClaimEval 双子任务下按逐样本协议评测 11 个前沿与开源多模态模型，配轻量透明后处理，并披露 leak-free pair prior
- 📌 **结论**：盲测榜四个组合中三项第一、一项并列第一；pair prior 把子任务一配对准确率从 72.2 提到 93.5，超过任何模型替换；多数剩余错误是标签映射交换或数据噪声

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We describe the SciTrue team's participation in both subtasks of the NTCIR-19 SciClaimEval task~\cite{sciclaimeval}, which asks systems to verify scientific claims against the tables and figures of a paper. Rather than tuning a single model, we benchmark eleven frontier and open multimodal models under one honest, per-sample protocol and combine them with light, transparent post-processing. On the official, blind test leaderboard (Section~\ref{sec:results}), SciTrue placed first by a clear margin in three of the four evidence-category/subtask combinations, and tied for first on the primary metric in the fourth. Three findings explain the result. First, strong instruction-tuned models are already competitive: Claude Opus~4.8 and Gemma-4-31B each exceed the strongest public baseline (o4-mini), and GPT-5.5 and Claude Fable~5 lead both subtasks (97.7 on Subtask~2). Second, the task's pairing structure is the largest lever: a \emph{leak-free pair prior} that recovers the Supported/Refuted pairing from the claim text alone (a visible field) and assigns Supported to the higher-confidence evidence raises Subtask-1 pair-accuracy from 72.2 to 93.5, far more than any model swap or ensemble weighting. Third, a case-by-case audit finds that most residual errors are visually-undetectable label-mapping swaps or dataset label noise, so measured accuracy understates the true ability and the fixable-by-modeling headroom is small. Controlled fine-tuning, distillation, and agentic consistency-checking support the same conclusions, and we document throughout a measurement leak---label information reaching a system through the packaging of the data rather than its content---in which the released file ordering encodes the label, including one instance that briefly misled our own pipeline.

</details>

### 27. Auto-Judge: A Cross-Task Benchmark for Comparing LLM Judges for Citation-Grounded RAG Systems

🌐 [Project](https://doi.org/10.1145/3805712.3808601)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`benchmark`、`citation-grounded RAG`、`judge manipulation`、`evaluation validity`、`LLM judge`、`evaluation integrity`

- 🎯 **研究动机**：citation-grounded RAG的LLM评审器缺跨任务可靠性评测
- 🔬 **研究方法**：构建Auto-Judge基准比较LLM judge的评判质量与抗操纵性
- 📌 **结论**：揭示LLM评审器的偏差与可操纵风险，威胁评测有效性

### 28. Who Checks the Citations? Benchmarking Legal Hallucination Detection

📄 [arXiv](https://arxiv.org/abs/2606.21155) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-06

**关键词**：`benchmark`、`legal hallucination`、`high-risk deployment`、`citation integrity`、`citation verification`、`agentic audit`

👤 **作者**：Patty Liu、Dominik Stammbach、Peter Henderson

- 🎯 **研究动机**：法律文书 AI 编造引文问题持续增长（发现超 1,000 份含虚构引文的卷宗且逐年增加），AI 自动检测幻觉的能力未知
- 🔬 **研究方法**：基于真实法院卷宗构建法律引文幻觉分类法与 1,300 条含注入错误的节选数据集，在 agentic 与非 agentic 设定下评估五个模型及 Claude Code
- 📌 **结论**：GPT-5 agentic 框架达 84.4% recall、55.0% F1，但所有模型在细微错误类别上挣扎；agentic 验证平均需 15.3 步且受商业法律数据库访问限制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Attorneys, judges, and pro se filers increasingly use AI to draft legal documents, yet these tools frequently fabricate citations. Despite predictions that newer models would hallucinate less or that court sanctions would deter negligent filers, we found over 1,000 filings containing fabricated citations---with this number growing year-over-year. This study evaluates whether AI-based systems can mitigate these errors by automatically detecting hallucinations. We propose a taxonomy of legal citation hallucinations grounded in actual court filings and introduce a dataset of 1,300 brief excerpts containing injected errors. Benchmarking five models in agentic and non-agentic settings as well as Claude Code reveals that while the latest iterations perform better---GPT-5 achieves 84.4% recall and a 55.0% F1 score in an agentic framework---all models struggle with subtle error categories. Agentic verification remains resource-intensive, with GPT-5 averaging 15.3 steps per excerpt. Furthermore, restricted information access limits the efficacy of even the best agents. This gap creates policy concerns, as it disadvantages both AI systems and litigants who lack subscriptions to commercial legal databases. Together, our dataset, tools, and policy recommendations provide a foundation for building and auditing reliable legal citation checking tools.

</details>

### 29. Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?

📄 [arXiv](https://arxiv.org/abs/2604.11061) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`gradient attribution`、`citation integrity`、`evidence verification`、`alignment audit`、`model organisms`

👤 **作者**：Ziqian Zhong、Aashiq Muhamed、Mona T. Diab、Virginia Smith、Aditi Raghunathan

- 🎯 **研究动机**：可解释性评测常不控制黑盒 prompt 单独能否恢复目标行为（elicitation confounder），白盒工具的表面收益可能只是 elicitation
- 🔬 **研究方法**：Pando 训练 720 个实现隐藏决策树规则的模型，分忠实、无解释、误导解释三轴，让 agent 从 10 个标注样本预测决策并可选用一种可解释工具
- 📌 **结论**：解释忠实时黑盒即匹配或超过所有白盒方法；解释缺失或误导时梯度归因（尤其 RelP）提升 3-5 个百分点，logit lens、SAE、circuit tracing 无可靠收益

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mechanistic interpretability is often motivated for alignment auditing, where a model's verbal explanations can be absent, incomplete, or misleading. Yet many evaluations do not control whether black-box prompting alone can recover the target behavior, so apparent gains from white-box tools may reflect elicitation rather than internal signal; we call this the elicitation confounder. We introduce Pando, a model-organism benchmark that breaks this confound via an explanation axis: models are trained to produce either faithful explanations of the true rule, no explanation, or confident but unfaithful explanations of a disjoint distractor rule. Across 720 finetuned models implementing hidden decision-tree rules, agents predict held-out model decisions from $10$ labeled query-response pairs, optionally augmented with one interpretability tool output. When explanations are faithful, black-box elicitation matches or exceeds all white-box methods; when explanations are absent or misleading, gradient-based attribution improves accuracy by 3-5 percentage points, and relevance patching, RelP, gives the largest gains, while logit lens, sparse autoencoders, and circuit tracing provide no reliable benefit. Variance decomposition suggests gradients track decision computation, which fields causally drive the output, whereas other readouts are dominated by task representation, biases toward field identity and value. We release all models, code, and evaluation infrastructure.

</details>