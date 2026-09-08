# Scientific Research Agent Reliability

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页只研究 Deep Research 与跨学科 Research Agent 特有的安全和 evidence-integrity 问题：search-time contamination、hallucination 传播、claim-source mismatch、multimodal provenance、prompt/trait leakage 与多阶段 guardrail。一般检索能力、系统架构、训练 recipe、任务成功率和科研效率不纳入。

## 研究脉络

- **污染与攻击：** 联网 Research Agent 可能检索到 benchmark answer、被恶意来源操纵，或通过网络 metadata 泄漏 prompt 与用户特征。
- **错误定位与事实核验：** DeepHalluBench、DRIFT 与 DeepFact 从整份报告分数转向 responsible stage、span-level first error、claim-level evidence 和可修订 benchmark label。
- **Multimodal evidence：** MMDeepResearch-Bench、ViDR 与 TVIR 将 source figure、citation grounding 和 text-visual integrity 纳入同一报告链。
- **Guardrail：** 多阶段审核需要分别约束检索来源、trajectory、claim 与最终报告，同时测量防御成功率和 over-refusal。
- **当前边界：** 更多搜索和更强报告能力不等于更安全；评测需保存来源快照、完整 trajectory、claim-level evidence 与 visual provenance。

## Failure Diagnosis 与 Contamination

### 1. Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation

📄 [arXiv](https://arxiv.org/abs/2606.05241)　📅 2026-06

**关键词**：`analysis`、`search-time contamination`、`answer leakage`、`score inflation`

👤 **作者**：Yongjie Wang、…、Zhiqi Shen

- 🎯 **研究动机**：deep research agent 推理时主动搜索网页，可能检索到基准元数据甚至标准答案，绕过预期推理并虚高性能
- 🔬 **研究方法**：定义三级 Search-Time Contamination（元数据/题干/答案泄漏），开发检测算法并在六个公开基准上量化对 agent 性能的影响
- 📌 **结论**：STC 普遍存在，最多虚高性能 4 个百分点，现有评估高估真实推理能力；建议隔离沙箱、透明搜索轨迹等无污染实践

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Public benchmarks enable fair and reproducible evaluation of LLM reasoning, but they become fragile for deep research agents that actively search the web during inference. Such agents may retrieve public benchmark metadata, question context, or even ground-truth answers via web search. This gives rise to Search-Time Contamination (STC), where external retrieval bypasses intended reasoning and inflates measured performance. We systematically study STC in deep research agent evaluation. We define three contamination types with increasing severity, namely Benchmark Metadata Leakage, Question-Context Leakage, and Explicit Answer Leakage, and develop detection algorithms to identify them and quantify their impact on agent performance. Evaluating modern deep research agents on six public benchmarks, we find that STC is widespread and can inflate performance by up to 4%. Our findings show that existing evaluations may overestimate true reasoning ability. We therefore advocate contamination-aware practices, including isolated sandboxes, transparent search trajectories, and controlled benchmark access.

</details>

### 2. Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory

📄 [arXiv](https://arxiv.org/abs/2601.22984)　📅 2026-01

**关键词**：`benchmark`、`deep research`、`PING taxonomy`、`claim verification`

👤 **作者**：Yuhao Zhan、Tianyu Fan、Linxuan Huang、Zirui Guo、Chao Huang

- 🎯 **研究动机**：端到端评测掩盖 Deep Research agent 研究轨迹中累积的中间幻觉
- 🔬 **研究方法**：提出 PING 分类法（Propagation、Intent、Noise-induced、Grounding），把 plan-search-summarize 轨迹拆解为原子动作、声明与子查询逐一核验，并构建 100 个易幻觉任务的 DeepHalluBench
- 📌 **结论**：六个代表性 DRA 在压力测试集上均存在不可忽视的可靠性缺口，失败可追溯至幻觉传播与认知偏差等系统性缺陷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diagnosing failure patterns in Deep Research Agents (DRAs) remains a critical challenge. Existing benchmarks predominantly rely on end-to-end evaluation, obscuring intermediate hallucinations that accumulate throughout the research trajectory. To bridge this gap, we propose a shift from outcome-based to processaware evaluation by auditing hallucinations in the full plan-search-summarize trajectory. We introduce the PING Taxonomy, which categorizes DRA hallucinations into four complementary types: Propagation, Intent, Noiseinduced, and Grounding. We further instantiate this taxonomy into a fine-grained evaluation framework that decomposes trajectories into atomic actions, claims, and sub-queries for rigorous verification. Leveraging this framework to isolate 100 distinctively hallucinationprone tasks including adversarial scenarios, we curate DeepHalluBench. Experiments on six representative DRAs show that, on our hallucination-prone stress-test set, all evaluated systems still exhibit non-negligible reliability gaps. Furthermore, our diagnostic analysis traces these failures to systemic deficits, especially hallucination propagation and cognitive biases, providing actionable insights for future architectural optimization. Code and data are available in https://github.com/yuhao-zhan/DeepHalluBench.

</details>

### 3. Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

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

### 4. Silent Failures in Multimodal Agentic Search: A Diagnostic Taxonomy and Cross-Judge Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.19793)　📅 2026-07

**关键词**：`analysis`、`silent failure`、`phantom grounding`、`cross-judge agreement`

👤 **作者**：Zhengxian Wu、Junjie Gao、Kai Yang

- 🎯 **研究动机**：多模态 agent 搜索评估只看最终答案准确率，可能遗漏搜索轨迹中的隐性可靠性问题
- 🔬 **研究方法**：提出六类 silent failures 分类法（模态捷径、幻影接地、错误证据正确答案、过度检索洗白、跨模态矛盾、来源幻觉），构建轨迹级诊断管线并用跨 judge 校验、空白图压力测试与工具消融验证
- 📌 **结论**：四个前沿多模态模型的 MMSearch-Plus 轨迹上，表面准确率一致高估真实轨迹级正确性；silent failures 随能力变化而转移而非消失

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions. However, existing evaluations mainly focus on final-answer accuracy and may miss failures in the search trajectory. In this work, we study such hidden reliability issues as silent failures. We introduce a six-category taxonomy covering modality shortcuts, phantom grounding, wrong-evidence-right-answer cases, over-retrieval laundering, cross-modal contradiction, and provenance hallucination. Based on this taxonomy, we build a trajectory-level diagnostic pipeline that evaluates both answer correctness and evidence-grounding quality under a unified ReAct-style scaffold. Experiments on MMSearch-Plus trajectories across four frontier multimodal models show that surface accuracy consistently overestimates true trajectory-level correctness. We further use cross-judge validation, blank-image stress tests, and tool ablations to show that silent failures are capability-dependent and often shift rather than disappear. Home-page: https://github.com/DingWu1021/silent-failures-multimodal-agentic-search

</details>

### 5. Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories

📄 [arXiv](https://arxiv.org/abs/2606.02060)　📅 2026-06

**关键词**：`detection`、`span localization`、`first error`、`DRIFT`

👤 **作者**：Jiaming Wang、…、Jiaheng Liu

- 🎯 **研究动机**：基于最终答案的评测只知 agent 成败，不知轨迹哪部分使答案不可靠
- 🔬 **研究方法**：收集 2,790 条真实轨迹，LLM 辅助专家审查标注有害错误 span，构建 1,000 实例的 TELBench；DRIFT 以 claim 为中心追踪 agent 主张、检查轨迹证据支撑并标记影响答案路径的 span
- 📌 **结论**：DRIFT 把 span 级错误定位与首错准确率最多提升 30 个百分点，提供深度研究 agent 的过程级可靠性视角

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep-research agents solve tasks through long trajectories of search, tool use, evidence inspection, and answer synthesis. Evaluation based on final answers shows whether an agent succeeds, but not which parts of the trajectory make the answer unreliable. We study span-level error localization for deep-research agents. We collect 2,790 real trajectories from two agent frameworks, three backbone models, and three benchmarks, convert raw logs into semantic spans, and annotate harmful error spans through LLM-assisted expert review. From these annotations, we build TELBench, a 1,000-instance benchmark for identifying error spans among normal exploration, failed searches, tentative hypotheses, and harmless noise. We further propose DRIFT, a claim-centric auditing framework that tracks agent claims, checks their support in trajectory evidence, and marks spans where unsupported or conflicting claims affect the answer path. Experiments across model families and auditing frameworks show that DRIFT improves span-level error localization and first-error accuracy by up to 30 percentage points. Our work provides a process-level view of reliability in deep-research agents.

</details>

### 6. ReFACT: A Benchmark for Scientific Confabulation Detection with Positional Error Annotations

🎓 [Official](https://aclanthology.org/2026.eacl-long.381/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`scientific confabulation`、`span error`、`judge reliability`、`LLM judge`

👤 **作者**：Yindong Wang、…、Gerard De Melo

- 🎯 **研究动机**：LLM 科学虚构（confabulation）的产生机制仍不清楚
- 🔬 **研究方法**：构建 ReFACT：来自 r/AskScience 的 1,001 条专家标注问答对，含 span 级错误标注，评测 9 个 SOTA LLM
- 📌 **结论**：61% 的错误 span 预测与真实错误语义无关且跨 1B-70B 规模不变；对比判断反而更难，GPT-4o 的 F1 从 0.67 降至 0.53，挑战 LLM-as-Judge 可靠性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The mechanisms underlying scientific confabulation in Large Language Models (LLMs) remain poorly understood. We introduce ReFACT, a benchmark of 1,001 expert-annotated question-answer pairs with span-level error annotations derived from Reddit’s r/AskScience. Evaluating 9 state-of-the-art LLMs reveals two critical limitations. First, models exhibit a dominant salient distractor failure mode: 61% of incorrect span predictions are semantically unrelated to actual errors. Crucially, this pattern persists across all model scales (1B to 70B), indicating a fundamental semantic grounding deficit that scaling alone fails to resolve. Second, we find that comparative judgment is paradoxically harder than independent detection–even GPT-4o’s F1 score drops from 0.67 to 0.53 when comparing answers side-by-side. These findings directly challenge the reliability of LLM-as-Judge paradigms for scientific factuality. Code and data are released at https://github.com/ddz5431/ReFACT.

</details>

### 7. DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality

📄 [arXiv](https://arxiv.org/abs/2603.05912) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1586/)　📅 2026-03　🏷 ACL 2026

**关键词**：`benchmark`、`Audit-then-Score`、`claim factuality`、`evolving labels`

👤 **作者**：Yukun Huang、Leonardo F. R. Ribeiro、Momchil Hardalov、Bhuwan Dhingra、Markus Dreyer、Venkatesh Saligrama

- 🎯 **研究动机**：专家对深度研究报告声明一次性标注仅 60.8% 准确，静态专家基准在此设定下脆弱
- 🔬 **研究方法**：提出 Audit-then-Score：verifier 不同意基准须提交证据，审计员裁决后修订基准再计分；实例化为 DeepFact-Bench 与验证 agent DeepFact-Eval
- 📌 **结论**：四轮后专家微金准确率升至 90.9%；DeepFact-Eval 在该基准超越既有验证器并良好迁移到外部数据集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search-augmented LLM agents can produce deep research reports (DRRs), but verifying claim-level factuality remains challenging. Existing fact-checkers are primarily designed for general-domain, factoid-style atomic claims, and there is no benchmark to test whether such verifiers transfer to DRRs. Yet building such a benchmark is itself difficult. We first show that static expert-labeled benchmarks are brittle in this setting: in a controlled study with PhD-level specialists, unassisted experts achieve only 60.8% accuracy on a hidden micro-gold set of verifiable claims. We propose Evolving Benchmarking via Audit-then-Score (AtS), where benchmark labels and rationales are explicitly revisable: when a verifier disagrees with the current benchmark, it must submit evidence; an auditor adjudicates the dispute; and accepted revisions update the benchmark before models are scored. Across four AtS rounds, expert micro-gold accuracy rises to 90.9%, indicating experts are substantially more reliable as auditors than as one-shot labelers. We instantiate AtS as DeepFact-Bench, a versioned DRR factuality benchmark with auditable rationales, and DeepFact-Eval, a document-level verification agent (with a grouped lite variant) that outperforms existing verifiers on DeepFact-Bench and transfers well to external factuality datasets.

</details>

### 8. Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Confidence Estimation and Calibration

📄 [arXiv](https://arxiv.org/abs/2604.05952)　📅 2026-04

**关键词**：`defense`、`claim confidence`、`evidence grounding`、`report calibration`

👤 **作者**：Yi Yuan、Xuhong Wang、Shanzhe Lei

- 🎯 **研究动机**：开放式研究报告无 ground truth，主观维度评测无法度量生成内容的认知置信度
- 🔬 **研究方法**：深度研究 agent 内嵌渐进式置信估计与校准：深思检索模型经多跳推理把输出接地于可验证证据，并逐 claim 赋予置信分
- 📌 **结论**：显著提升可解释性与用户信任，产出带置信标注的透明可信报告

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As agent-based systems continue to evolve, deep research agents are capable of automatically generating research-style reports across diverse domains. While these agents promise to streamline information synthesis and knowledge exploration, existing evaluation frameworks-typically based on subjective dimensions-fail to capture a critical aspect of report quality: trustworthiness. In open-ended research scenarios where ground-truth answers are unavailable, current evaluation methods cannot effectively measure the epistemic confidence of generated content, making calibration difficult and leaving users susceptible to misleading or hallucinated information. To address this limitation, we propose a novel deep research agent that incorporates progressive confidence estimation and calibration within the report generation pipeline. Our system leverages a deliberative search model, featuring deep retrieval and multi-hop reasoning to ground outputs in verifiable evidence while assigning confidence scores to individual claims. Combined with a carefully designed workflow, this approach produces trustworthy reports with enhanced transparency. Experimental results and case studies demonstrate that our method substantially improves interpretability and significantly increases user trust.

</details>

### 9. TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2602.21230) · 🌐 [Project](https://doi.org/10.1145/3774904.3792738)　📅 2026-02

**关键词**：`benchmark`、`trajectory utility`、`evidence grounding`、`latent capability`

👤 **作者**：Yanyu Chen、Jiyue Jiang、Jiahong Liu、Yifei Zhang、Xiao Guo、Irwin King

- 🎯 **研究动机**：Pass@1 等单一结果指标造成高分假象，静态基准无法量化 deep research agent 的稳健性与潜在能力
- 🔬 **研究方法**：TRACE 以层次化轨迹效用函数量化过程效率、认知质量与证据接地，并用脚手架能力评估测定达成成功所需的最小引导
- 📌 **结论**：给出细粒度排名，揭示单一指标完全遗漏的准确率-效率-鲁棒性权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The evaluation of Deep Research Agents is a critical challenge, as conventional outcome-based metrics fail to capture the nuances of their complex reasoning. Current evaluation faces two primary challenges: 1) a reliance on singular metrics like Pass@1, creating a "high-score illusion" that ignores the quality, efficiency, and soundness of the reasoning process; and 2) the failure of static benchmarks to quantify crucial attributes like robustness and latent capability. To address these gaps, we introduce TRACE (Trajectory-Aware Comprehensive Evaluation), a framework that holistically assesses the entire problem-solving trajectory. To counter the "high-score illusion", we propose a Hierarchical Trajectory Utility Function that quantifies process efficiency and cognitive quality, including evidence grounding, alongside accuracy. To measure deeper attributes, TRACE introduces a Scaffolded Capability Assessment protocol, quantifying an agent's latent ability by determining the minimum guidance needed for success. Our contributions include the TRACE framework, its novel metrics, and the accompanying DeepResearch-Bench with controllable complexity. Experiments show TRACE delivers a granular ranking that uncovers critical trade-offs between agent accuracy, efficiency, and robustness entirely missed by singular metrics.

</details>

### 10. TVIR: Building Deep Research Agents Towards Text-Visual Interleaved Report Generation

📄 [arXiv](https://arxiv.org/abs/2606.02320)　📅 2026-06

**关键词**：`tool`、`interleaved report`、`visual retrieval`、`source attribution`

👤 **作者**：Xinkai Ma、…、Jiaheng Liu

- 🎯 **研究动机**：深度研究 agent 与基准以文本为中心，视觉元素的事实可靠性与图文对齐缺评估
- 🔬 **研究方法**：TVIR：100 个专家策划多模态任务的 TVIR-Bench，加层级多 agent 基线 TVIR-Agent（大纲、图像检索、可溯源图表生成、上下文感知顺序写作），配文本与视觉双路评估
- 📌 **结论**：九个深度研究系统对比中 TVIR-Agent 整体最强，凸显显式多模态设计与评估对证据驱动报告的重要性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research Agents have shown strong capability in multi-step information retrieval, reasoning, and long-form report generation, but existing benchmarks and systems remain predominantly text-centric, with limited evaluation of whether visual elements are factually reliable and well aligned with the surrounding analysis. To address this gap, we introduce TVIR (Text-Visual Interleaved Report Generation), which includes TVIR-Bench, a benchmark of 100 expert-curated multimodal deep research tasks that require visual elements to serve specific analytical sub-goals, and TVIR-Agent, a hierarchical multi-agent framework that serves as a strong baseline for constructing outlines, retrieving images, generating charts with traceable sources, and composing reports through context-aware sequential writing. We further develop a dual-path evaluation framework that combines Textual Assessment and Visual Assessment. Experiments across nine deep research systems show that TVIR-Agent achieves strong overall performance, underscoring the importance of explicit multimodal design and evaluation for evidence-driven report generation.

</details>

### 11. ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence

📄 [arXiv](https://arxiv.org/abs/2605.13034)　📅 2026-05

**关键词**：`tool`、`source figure`、`visual grounding`、`report verifiability`

👤 **作者**：Zhuofan Shi、…、Xiang Jing

- 🎯 **研究动机**：文本中心研究系统弱用源图，多模态系统常只弱检索图像或自造图表，源图作为证据被低估
- 🔬 **研究方法**：ViDR 把源图当可检索、可解释、可路由、可验证的证据对象：证据索引大纲、上下文过滤、大纲感知重排与 VLM 分析精炼证据原子，并校验视觉引用；附 MMR Bench+ 基准
- 📌 **结论**：报告整体质量、源图整合与可验证性均超过强商业与开源基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent deep research systems have improved the ability of large language models to produce long, grounded reports through iterative retrieval and reasoning. However, most text-centered systems rely mainly on textual evidence, while multimodal systems often retrieve images only weakly or generate charts themselves, leaving source figures underused as evidence. We present ViDR, a multimodal deep research framework that grounds long-form reports in source figures. ViDR treats source figures as retrievable, interpretable, routable, and verifiable evidence objects, while still generating analytical charts when needed. It builds an evidence-indexed outline linking claims to textual and visual evidence, refines noisy web images into source-figure evidence atoms through context-aware filtering, outline-aware reranking, and VLM-based visual analysis, and generates each section with section-specific evidence. ViDR further validates visual references to reduce hallucinated or misplaced figures. We also introduce MMR Bench+, a benchmark for evaluating visual evidence use in deep research reports, covering source-figure retrieval, placement, interpretation, verifiability, and analytical chart generation. Experiments show that ViDR improves overall report quality, source-figure integration, and verifiability over strong commercial and open-source baselines. These results suggest that source visual evidence is important for multimodal deep research, as it strengthens evidential grounding, visual support, and report verifiability.

</details>

### 12. Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models

📄 [arXiv](https://arxiv.org/abs/2602.02185)　📅 2026-02

**关键词**：`benchmark`、`visual search`、`cropped retrieval`、`cross-modal leakage`

👤 **作者**：Yu Zeng、…、Shaosheng Cao

- 🎯 **研究动机**：现有视觉研究基准的答案可由文本线索或世界知识泄漏，且检索设定过于理想化
- 🔬 **研究方法**：构建经多阶段筛选与专家审核的 2000 个 VQA 实例的 VDR-Bench，并提出多轮裁剪搜索工作流增强真实视觉检索
- 📌 **结论**：揭示当前 MLLM 视觉检索能力不足，多轮 cropped search 有效提升现实场景表现

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal Large Language Models (MLLMs) have advanced VQA and now support Vision-DeepResearch systems that use search engines for complex visual-textual fact-finding. However, evaluating these visual and textual search abilities is still difficult, and existing benchmarks have two major limitations. First, existing benchmarks are not visual search-centric: answers that should require visual search are often leaked through cross-textual cues in the text questions or can be inferred from the prior world knowledge in current MLLMs. Second, overly idealized evaluation scenario: On the image-search side, the required information can often be obtained via near-exact matching against the full image, while the text-search side is overly direct and insufficiently challenging. To address these issues, we construct the Vision-DeepResearch benchmark (VDR-Bench) comprising 2,000 VQA instances. All questions are created via a careful, multi-stage curation pipeline and rigorous expert review, designed to assess the behavior of Vision-DeepResearch systems under realistic real-world conditions. Moreover, to address the insufficient visual retrieval capabilities of current MLLMs, we propose a simple multi-round cropped-search workflow. This strategy is shown to effectively improve model performance in realistic visual retrieval scenarios. Overall, our results provide practical guidance for the design of future multimodal deep-research systems. The code will be released in https://github.com/Osilly/Vision-DeepResearch.

</details>

### 13. MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2601.12346) · 🌐 [Project](https://mmdeepresearch-bench.github.io/)　📅 2026-01

**关键词**：`benchmark`、`multimodal evidence`、`citation grounding`、`text-visual integrity`

👤 **作者**：Peizhou Huang、…、Mi Zhang

- 🎯 **研究动机**：已有 Deep Research agent 基准只测文本或短形式多模态 QA，缺端到端多模态证据使用评测
- 🔬 **研究方法**：构建 140 个专家任务、21 领域图文 bundle 的 MMDR-Bench，配套 FLAE（报告质量）、TRACE（引用对齐）与 MOSAIC（图文完整性）三组可解释评测管线
- 📌 **结论**：25 个 SOTA 模型显示生成质量、引用纪律与多模态接地存在系统性取舍；强文笔不保证证据忠实，多模态完整性是关键瓶颈

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research Agents (DRAs) generate citation-rich reports via multi-step search and synthesis, yet existing benchmarks mainly target text-only settings or short-form multimodal QA, missing end-to-end multimodal evidence use. We introduce MMDeepResearch-Bench (MMDR-Bench), a benchmark of 140 expert-crafted tasks across 21 domains, where each task provides an image-text bundle to evaluate multimodal understanding and citation-grounded report generation. Compared to prior setups, MMDR-Bench emphasizes report-style synthesis with explicit evidence use, where models must connect visual artifacts to sourced claims and maintain consistency across narrative, citations, and visual references. We further propose a unified, interpretable evaluation pipeline: Formula-LLM Adaptive Evaluation (FLAE) for report quality, Trustworthy Retrieval-Aligned Citation Evaluation (TRACE) for citation-grounded evidence alignment, and Multimodal Support-Aligned Integrity Check (MOSAIC) for text-visual integrity, each producing fine-grained signals that support error diagnosis beyond a single overall score. Experiments across 25 state-of-the-art models reveal systematic trade-offs between generation quality, citation discipline, and multimodal grounding, highlighting that strong prose alone does not guarantee faithful evidence use and that multimodal integrity remains a key bottleneck for deep research agents.

</details>

### 14. HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research

📄 [arXiv](https://arxiv.org/abs/2607.25151) · 📊 [Dataset](https://huggingface.co/datasets/ai9stars/HiEviDR-Bench)　📅 2026-07

**关键词**：`benchmark`、`hierarchical evidence`、`evidence graph`、`traceability`

👤 **作者**：Yubo Sun、…、Maosong Sun

- 🎯 **研究动机**：已有基准只评最终产出，对证据是否被正确选择、链接与聚合成结论缺乏可见性
- 🔬 **研究方法**：构建 HiEviDR-Bench：开放域与学术域、纯文本与多模态，每实例含显式证据图（证据选择、跨源链接、证据到中间断言再到结论），配合五维可追溯评估与渐进门控定位错误
- 📌 **结论**：16 个多模态模型上报告质量虽强但引用准确率、断言构建与答案正确性显著下滑；瓶颈在证据识别与中间断言构建

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep research requires models to retrieve, connect, and synthesize evidence from large-scale heterogeneous sources to answer complex queries and produce analytical reports. Existing benchmarks mainly evaluate final outcomes, such as answer correctness, report quality, or citation alignment, while providing limited visibility into whether evidence is correctly selected, linked, and aggregated into supported claims and conclusions. To address this gap, we introduce HiEviDR-Bench, a benchmark for evaluating Hierarchical Evidence Aggregation in Deep Research. HiEviDR-Bench covers open-domain and academic-domain settings under both text-only and multimodal conditions, and represents each instance with an explicit evidence graph that captures evidence selection, cross-source linking, and aggregation from evidence to intermediate claims and final conclusions. Based on this formulation, we develop a traceability-oriented evaluation framework with five dimensions: report quality, evidence traceability, citation accuracy, claim verification, and answer correctness, together with a progressive gating mechanism for fine-grained error localization. HiEviDR-Bench contains 2,000 human-validated questions with evidence graphs across multiple difficulty levels. Experiments on 16 representative multimodal large language models show that, although many systems achieve strong report quality, their performance drops markedly on citation accuracy, claim construction, and answer correctness. Further analysis shows that the main bottlenecks lie in evidence identification and intermediate claim construction, revealing that strong surface-level report quality does not necessarily imply grounded multi-stage reasoning on our benchmark.

</details>

### 15. DR$^3$-Eval: Towards Realistic and Reproducible Deep Research Evaluation

📄 [arXiv](https://arxiv.org/abs/2604.14683)　📅 2026-04

**关键词**：`benchmark`、`static sandbox`、`multifile report`、`reproducible retrieval`

👤 **作者**：Qianqian Xie、…、Jiaheng Liu

- 🎯 **研究动机**：深度研究 agent 的评测受动态网页与模糊任务定义困扰，难以复现
- 🔬 **研究方法**：DR3-Eval 基于真实用户材料构建多模态多文件报告任务，配含支持文档、干扰与噪声的 per-task 静态沙箱，从信息召回、事实、引用、指令、深度五维评估
- 📌 **结论**：基准高难度，暴露 DRA 在检索鲁棒性与幻觉控制上的关键失败模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

</details>

### 16. MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome

📄 [arXiv](https://arxiv.org/abs/2603.28407)　📅 2026-03

**关键词**：`benchmark`、`multimodal process`、`active factuality`、`outcome evaluation`

👤 **作者**：Fangda Ye、…、Lidong Bing

- 🎯 **研究动机**：深度研究评测只用固定 rubric 评终稿，忽略研究过程、多模态覆盖有限且任务不真实
- 🔬 **研究方法**：MiroEval 含 100 个真实任务（30 个多模态），沿自适应综合质量、主动事实性与过程中心三维评测 13 个系统
- 📌 **结论**：过程质量可可靠预测终局表现并暴露输出级指标不可见的弱点；多模态任务使多数系统下降 3-10 分

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent progress in deep research systems has been impressive, but evaluation still lags behind real user needs. Existing benchmarks predominantly assess final reports using fixed rubrics, failing to evaluate the underlying research process. Most also offer limited multimodal coverage, rely on synthetic tasks that do not reflect real-world query complexity, and cannot be refreshed as knowledge evolves. To address these gaps, we introduce MiroEval, a benchmark and evaluation framework for deep research systems. The benchmark comprises 100 tasks (70 text-only, 30 multimodal), all grounded in real user needs and constructed via a dual-path pipeline that supports periodic updates, enabling a live and evolving setting. The proposed evaluation suite assesses deep research systems along three complementary dimensions: adaptive synthesis quality evaluation with task-specific rubrics, agentic factuality verification via active retrieval and reasoning over both web sources and multimodal attachments, and process-centric evaluation audits how the system searches, reasons, and refines throughout its investigation. Evaluation across 13 systems yields three principal findings: the three evaluation dimensions capture complementary aspects of system capability, with each revealing distinct strengths and weaknesses across systems; process quality serves as a reliable predictor of overall outcome while revealing weaknesses invisible to output-level metrics; and multimodal tasks pose substantially greater challenges, with most systems declining by 3 to 10 points. The MiroThinker series achieves the most balanced performance, with MiroThinker-H1 ranking the highest overall in both settings. Human verification and robustness results confirm the reliability of the benchmark and evaluation framework. MiroEval provides a holistic diagnostic tool for the next generation of deep research agents.

</details>

### 17. Dr. Bench: A Multidimensional Evaluation for Deep Research Agents, from Answers to Reports

📄 [arXiv](https://arxiv.org/abs/2510.02190)　📅 2025-10

**关键词**：`benchmark`、`long-form report`、`citation trustworthiness`、`topic focus`

👤 **作者**：Yang Yao、…、Yingchun Wang

- 🎯 **研究动机**：既有基准在评测维度、响应格式与打分机制上难以评估 DRA 的长报告输出
- 🔬 **研究方法**：构建 Dr. Bench：214 个专家定制任务覆盖 10 领域并附人工参考束，以语义质量、主题聚焦、检索可信度三维评估长报告
- 📌 **结论**：主流 DRA 优于带搜索工具的推理模型，但改进空间仍然可观

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As an embodiment of intelligence evolution toward interconnected architectures, Deep Research Agents (DRAs) systematically exhibit the capabilities in task decomposition, cross-source retrieval, multi-stage reasoning, information integration, and structured output, which markedly enhance performance on complex and open-ended tasks. However, existing benchmarks remain deficient in evaluation dimensions, response format, and scoring mechanisms, limiting their effectiveness in assessing such agents. This paper introduces Dr. Bench, a multidimensional evaluation framework tailored to DRAs and long-form report-style responses. The benchmark comprises 214 expert-curated challenging tasks across 10 broad domains, each accompanied by manually constructed reference bundles to support composite evaluation. This framework incorporates metrics for semantic quality, topical focus, and retrieval trustworthiness, enabling a comprehensive evaluation of long reports generated by DRAs. Extensive experimentation confirms the superior performance of mainstream DRAs over web-search-tool-augmented reasoning models, yet reveals considerable scope for further improvement. This study provides a robust foundation for capability assessment, architectural refinement, and paradigm advancement of DRAs.

</details>

### 18. MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents

📄 [arXiv](https://arxiv.org/abs/2508.21475) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10009159)　📅 2025-08　🏷 ICLR 2026

**关键词**：`benchmark`、`visual provenance`、`iterative retrieval`、`Set-of-Mark`

👤 **作者**：Xijia Tao、…、Lingpeng Kong

- 🎯 **研究动机**：现有多模态浏览基准可被纯文本启发式解出，未强制视觉参与的闭环验证
- 🔬 **研究方法**：构建 311 任务基准：需从空间线索与时序痕迹外推出图外事实，配 set-of-mark 模块的模型无关 agent 框架支持标注、裁剪与定向检索
- 📌 **结论**：最强系统端到端准确率仅 36.0%，SoM 带来最高 3.9 点提升；定位相关网页与区分相似事件是主要失败模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing multimodal browsing benchmarks often fail to require genuine multimodal reasoning, as many tasks can be solved with text-only heuristics without vision-in-the-loop verification. We introduce MMSearch-Plus, a 311-task benchmark that enforces multimodal understanding by requiring extraction and propagation of fine-grained visual cues through iterative image-text retrieval and cross-validation under retrieval noise. Our curation procedure seeds questions whose answers require extrapolating from spatial cues and temporal traces to out-of-image facts such as events, dates, and venues. Beyond the dataset, we provide a model-agnostic agent framework with standard browsing tools and a set-of-mark (SoM) module, which lets the agent place marks, crop subregions, and launch targeted image/text searches. SoM enables provenance-aware zoom-and-retrieve and improves robustness in multi-step reasoning. We evaluated closed- and open-source MLLMs in this framework. The strongest system achieves an end-to-end accuracy of 36.0%, and integrating SoM produces consistent gains in multiple settings, with improvements up to +3.9 points. From failure analysis, we observe recurring errors in locating relevant webpages and distinguishing between visually similar events. These results underscore the challenges of real-world multimodal search and establish MMSearch-Plus as a rigorous benchmark for advancing agentic MLLMs.

</details>

### 19. DeepScholar-Bench: A Live Benchmark and Automated Evaluation for Generative Research Synthesis

📄 [arXiv](https://arxiv.org/abs/2508.20033)　📅 2025-08

**关键词**：`benchmark`、`research synthesis`、`live evaluation`、`verifiable citation`

👤 **作者**：Liana Patel、…、Carlos Guestrin

- 🎯 **研究动机**：现有 QA 基准只测短事实回答，专家策展数据易过时污染，无法评估生成式研究综合
- 🔬 **研究方法**：从近期高质量 arXiv 论文提取查询与人工范例，任务为检索、综合并引用先前工作生成 related work，自动框架从知识综合、检索质量、可验证性三维评估
- 📌 **结论**：无系统在全部指标上超过几何平均 31%，基准远未饱和；开源基线管线 DeepScholar-ref

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The ability to research and synthesize knowledge is central to human expertise and progress. A new class of AI systems--designed for generative research synthesis--aims to automate this process by retrieving information from the live web and producing long-form, cited reports. Yet, evaluating such systems remains an open challenge: existing question-answering benchmarks focus on short, factual answers, while expert-curated datasets risk staleness and data contamination. Neither captures the complexity and evolving nature of real research synthesis tasks. We introduce DeepScholar-bench, a live benchmark and automated evaluation framework for generative research synthesis. DeepScholar-bench draws queries and human-written exemplars from recent, high-quality ArXiv papers and evaluates a real synthesis task: generating a related work section by retrieving, synthesizing, and citing prior work. Our automated framework holistically measures performance across three key dimensions--knowledge synthesis, retrieval quality, and verifiability. To further future work, we also contribute DeepScholar-ref, a simple, open-source reference pipeline, which is implemented on the LOTUS framework and provides a strong baseline. Using DeepScholar-bench, we systematically evaluate prior open-source systems, search agents with strong models, OpenAI's DeepResearch, and DeepScholar-ref. We find DeepScholar-bench is far from saturated: no system surpasses a geometric mean of $31\%$ across all metrics. These results highlight both the difficulty and importance of DeepScholar-bench as a foundation for advancing AI systems capable of generative research synthesis. We make our benchmark code and data available at https://github.com/guestrin-lab/deepscholar-bench.

</details>

### 20. ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks

📄 [arXiv](https://arxiv.org/abs/2508.15804)　📅 2025-08

**关键词**：`benchmark`、`report factuality`、`citation verification`、`survey task`

👤 **作者**：Minghao Li、Ying Zeng、Zhihao Cheng、Cong Ma、Kai Jia

- 🎯 **研究动机**：Deep Research agent 生成报告的事实准确性与全面性缺乏严格评测基准
- 🔬 **研究方法**：以 arXiv 高质量综述为金标准做逆向 prompt 工程构建语料，agent 自动框架抽取引文与陈述、核对引用忠实性并用网络资源验证非引用断言
- 📌 **结论**：OpenAI 与 Google 商用 DRA 比带搜索的独立 LLM 更全面可靠，但覆盖广度深度与事实一致性仍有大提升空间

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advent of Deep Research agents has substantially reduced the time required for conducting extensive research tasks. However, these tasks inherently demand rigorous standards of factual accuracy and comprehensiveness, necessitating thorough evaluation before widespread adoption. In this paper, we propose ReportBench, a systematic benchmark designed to evaluate the content quality of research reports generated by large language models (LLMs). Our evaluation focuses on two critical dimensions: (1) the quality and relevance of cited literature, and (2) the faithfulness and veracity of the statements within the generated reports. ReportBench leverages high-quality published survey papers available on arXiv as gold-standard references, from which we apply reverse prompt engineering to derive domain-specific prompts and establish a comprehensive evaluation corpus. Furthermore, we develop an agent-based automated framework within ReportBench that systematically analyzes generated reports by extracting citations and statements, checking the faithfulness of cited content against original sources, and validating non-cited claims using web-based resources. Empirical evaluations demonstrate that commercial Deep Research agents such as those developed by OpenAI and Google consistently generate more comprehensive and reliable reports than standalone LLMs augmented with search or browsing tools. However, there remains substantial room for improvement in terms of the breadth and depth of research coverage, as well as factual consistency. The complete code and data will be released at the following link: https://github.com/ByteDance-BandAI/ReportBench

</details>

### 21. SurGE: A Benchmark and Evaluation Framework for Scientific Survey Generation

📄 [arXiv](https://arxiv.org/abs/2508.15658) · 🌐 [Project](https://doi.org/10.1145/3805712.3808598)　📅 2025-08　🏷 SIGIR 2026

**关键词**：`benchmark`、`survey generation`、`citation accuracy`、`academic corpus`、`scientific survey`、`citation integrity`

👤 **作者**：Weihang Su、…、Yiqun Liu

- 🎯 **研究动机**：学术文献激增使人工撰写综述难以为继，LLM 自动综述缺乏标准化基准与评估协议
- 🔬 **研究方法**：构建 SurGE：含主题描述、专家综述及全部引文的测试实例加百万级论文语料，自动评估覆盖全面性、引用准确性、结构组织与内容质量四维
- 📌 **结论**：多种 LLM 方法性能差距显著，先进 agentic 框架也难以胜任综述生成任务

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of academic literature makes the manual creation of scientific surveys increasingly infeasible. While large language models show promise for automating this process, progress in this area is hindered by the absence of standardized benchmarks and evaluation protocols. To bridge this critical gap, we introduce SurGE (Survey Generation Evaluation), a new benchmark for scientific survey generation in computer science. SurGE consists of (1) a collection of test instances, each including a topic description, an expert-written survey, and its full set of cited references, and (2) a large-scale academic corpus of over one million papers. In addition, we propose an automated evaluation framework that measures the quality of generated surveys across four dimensions: comprehensiveness, citation accuracy, structural organization, and content quality. Our evaluation of diverse LLM-based methods demonstrates a significant performance gap, revealing that even advanced agentic frameworks struggle with the complexities of survey generation and highlighting the need for future research in this area. We have open-sourced all the code, data, and models at: https://github.com/oneal2000/SurGE

</details>

### 22. DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2506.11763) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10008065)　📅 2025-06　🏷 ICLR 2026

**关键词**：`benchmark`、`PhD-level task`、`citation accuracy`、`human-aligned scoring`

👤 **作者**：Mingxuan Du、Benfeng Xu、Chiwei Zhu、Xiaorui Wang、Zhendong Mao

- 🎯 **研究动机**：深度研究 agent 缺乏系统性能力评测基准
- 🔬 **研究方法**：构建 22 个领域专家定制的 100 个博士级研究任务，并提出自适应标准报告评估与引用有效性计数两套人评对齐方法
- 📌 **结论**：两套评估方法与人类判断强对齐，基准与关键组件开源

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research Agents are a prominent category of LLM-based agents. By autonomously orchestrating multistep web exploration, targeted retrieval, and higher-order synthesis, they transform vast amounts of online information into analyst-grade, citation-rich reports--compressing hours of manual desk research into minutes. However, a comprehensive benchmark for systematically evaluating the capabilities of these agents remains absent. To bridge this gap, we present DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks, each meticulously crafted by domain experts across 22 distinct fields. Evaluating DRAs is inherently complex and labor-intensive. We therefore propose two novel methodologies that achieve strong alignment with human judgment. The first is a reference-based method with adaptive criteria to assess the quality of generated research reports. The other framework is introduced to evaluate DRA's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy. We have open-sourced DeepResearch Bench and key components of these frameworks at https://github.com/Ayanami0730/deep_research_bench to accelerate the development of practical LLM-based agents.

</details>

### 23. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent

📄 [arXiv](https://arxiv.org/abs/2608.03979)　📅 2026-08

**关键词**：`analysis`、`VLM safety`、`research agent`、`scientific reliability`

👤 **作者**：Zhen Fang、…、Feng Zhao

- 🎯 **研究动机**：多模态 deep research agent 从静态图像走向连续视频流时存在模态偏置与参数知识泄漏两个瓶颈
- 🔬 **研究方法**：Video-DR 用解耦感知-探索管线分阶段解锁工具强制跨帧视觉接地，SFT 加 GRPO 两阶段训练，并构建 200 题多跳 VQA 基准 Video-DR-Bench
- 📌 **结论**：35B-A3B 达 64.0% 平均准确率，超 Claude-4.5-Sonnet 5.0 个点、超 GPT-5 11.5 个点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce Video-DeepResearch (Video-DR), extending multimodal agents from static images to continuous video streams, a setting that demands dense spatiotemporal grounding coupled with open-web exploration. Preliminary evaluations reveal two critical bottlenecks in current models: (1) modality bias, where agents bypass visual tools in favor of textual search, and (2) parametric knowledge leakage, where models rely on internal memory rather than genuine tool-augmented execution. To address these challenges, we propose Video-DR, featuring a decoupled perception-exploration pipeline with stage-wise tool unlocking that compels exhaustive cross-frame visual grounding prior to web retrieval. Our framework adopts a two-stage training recipe: supervised fine-tuning followed by Group Relative Policy Optimization (GRPO), enabling autonomous exploration that breaks the imitation-learning ceiling. Furthermore, we curate Video-DR-Bench, a human-AI collaborative benchmark comprising 200 complex, multi-hop VQA instances. Empirical results demonstrate that our Video-DeepResearch-35B-A3B establishes a new state-of-the-art of 64.0% average accuracy, surpassing proprietary Claude-4.5-Sonnet (59.0%) by 5.0 points and significantly outperforming GPT-5 (52.5%) and Gemini 2.5 Pro (57.5%). The 30B-A3B variant achieves 59.3%, competitive with Claude-4.5-Sonnet and demonstrating the effectiveness of our training paradigm even at compact scale. Code: https://github.com/Osilly/Vision-DeepResearch.

</details>

### 24. Deep Research with Open-Domain Evaluation and Multi-Stage Guardrails for Safety

🎓 [Official](https://aclanthology.org/2026.acl-long.2010/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`over-refusal`、`research agent`、`scientific reliability`、`content moderation`、`harmful content`

👤 **作者**：Wei-Chieh Huang、…、Philip S. Yu

- 🎯 **研究动机**：深度研究框架缺乏评估程序与分阶段保护——把评估当 QA 精确匹配，忽视可信度、连贯性与安全，危险源可能进入最终报告
- 🔬 **研究方法**：DeepResearchGuard 四阶段防护加开放域评估框架，配分阶段安全基准 DRSafeBench
- 📌 **结论**：跨五个模型防御成功率绝对提升 16.53%，过度拒绝率降至约 6%，同时系统性改善报告质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep research frameworks have shown promising capabilities in synthesizing comprehensive reports from web sources. While deep research possesses significant potential to address complex issues through planning and research cycles, existing frameworks are deficient in sufficient evaluation procedures and stage-specific protections. They typically treat evaluation as exact match accuracy of question-answering, but overlook crucial aspects of report quality such as credibility, coherence, breadth, depth, and safety. This oversight may result in hazardous or malicious sources being integrated into the final report. To address this, we introduce DeepResearchGuard, a framework featuring four-stage safeguards with open-domain evaluation, and DRSafeBench, a novel stage-wise safety benchmark. Evaluating across GPT-4o, o4-mini, Gemini-2.5-flash, DeepSeek-v3, and GPT-5, DeepResearchGuard improves defense success rates by an absolute 16.53% while reducing over-refusal rates to approximately 6%. Through extensive experiments, we show that DeepResearchGuard enables comprehensive open-domain evaluation and stage-aware defenses that effectively block harmful content propagation, while systematically improving report quality without excessive over-refusal rates.

</details>

### 25. Network-Level Prompt and Trait Leakage in Local Research Agents

📄 [arXiv](https://arxiv.org/abs/2508.20282) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/jeong)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`attack`、`research agent`、`scientific reliability`、`error localization`、`traffic analysis`、`trait inference`

👤 **作者**：Hyejun Jeong、Mohammadreza Teymoorianfard、Abhinav Kumar、Amir Houmansadr、Eugene Bagdasarian

- 🎯 **研究动机**：本地部署的 Web/Research agent 每请求访问 70-140 个域名，独特时序模式暴露给 DNS、ISP、VPN 等被动观察者
- 🔬 **研究方法**：构建真实与合成人格查询的 WRA 轨迹数据集，仅凭访问 IP 与时序元数据推断 prompt 与用户特质，以 OBELS 度量相似度
- 📌 **结论**：恢复 prompt 超 73% 的功能与领域知识，多会话下 32 个潜在特质中恢复 19 个；限制域名多样性等缓解平均降低攻击 29%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We show that Web and Research Agents (WRAs) -- language-model-based systems that investigate complex topics on the Internet -- are vulnerable to inference attacks by passive network observers. Deployment of WRAs \emph{locally} by organizations and individuals for privacy, legal, or financial purposes exposes them to DNS resolvers, malicious ISPs, VPNs, web proxies, and corporate or government firewalls. However, unlike sporadic and scarce web browsing by humans, WRAs visit $70{-}140$ domains per each request with a distinct timing pattern creating unique privacy risks. Specifically, we demonstrate a novel prompt and user trait leakage attack against WRAs that only leverages their network-level metadata (i.e., visited IP addresses and their timings). We start by building a new dataset of WRA traces based on real user search queries and queries generated by synthetic personas. We define a behavioral metric (called OBELS) to comprehensively assess similarity between original and inferred prompts, showing that our attack recovers over 73\% of the functional and domain knowledge of user prompts. Extending to a multi-session setting, we recover up to 19 of 32 latent traits with high accuracy. Our attack remains effective under partial observability and noisy conditions. Finally, we discuss mitigation strategies that constrain domain diversity or obfuscate traces, showing negligible utility impact while reducing attack effectiveness by an average of 29\%.

</details>