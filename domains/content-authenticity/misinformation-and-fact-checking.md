# Misinformation 与 Fact Checking

[返回上级目录](README.md)

## 研究方向

研究文本、图像、视频和音频中的 misinformation、fake news 与事实一致性，覆盖 claim verification、动态证据检索、来源归因、协同操纵和可解释纠错。

## 研究脉络

- **静态事实核查：** 早期工作以固定 claim 和证据集合判断真假及支持关系。
- **多模态与动态信息：** Benchmark 扩展到短视频、交错图文、热点演化和实时网页证据。
- **解释与纠错：** Agentic retrieval、verdict-anchored explanation 和 faithful correction 将检测连接到证据与修复。
- **对抗与治理：** 协同操纵、Community Notes 和平台传播研究把单条内容判断扩展到社会技术系统。

## Benchmark 与动态评测

### 1. EvoFEND: Dual Memory-Driven Self-Evolving Fake News Detection

🌐 [Project](https://doi.org/10.1145/3770855.3817673)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`fake news`、`self-evolving memory`、`concept drift`

- 🎯 **研究动机**：话题演化下假新闻检测器面临concept drift，静态模型难自进化
- 🔬 **研究方法**：EvoFEND以双记忆驱动实现自进化假新闻检测
- 📌 **结论**：漂移场景下持续保持检测性能

### 2. Nip Rumors in the Bud: Retrieval-Guided Topic-Level Adaptation for Test-Time Fake News Video Detection

📄 [arXiv](https://arxiv.org/abs/2601.11981) · 🌐 [Project](https://doi.org/10.1145/3770854.3780211)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`fake news video`、`test-time adaptation`、`topic shift`

👤 **作者**：Jian Lang、Rongpei Hong、Ting Zhong、Yong Wang、Fan Zhou

- 🎯 **研究动机**：假新闻视频检测假设训练测试主题分布一致，难检测新事件与未见主题
- 🔬 **研究方法**：RADAR 首个测试时自适应框架：熵选择检索找稳定参考，稳定锚点对齐做分布级匹配，目标域感知自训练生成伪标签适应不均衡分布
- 📌 **结论**：测试时假新闻视频检测性能优越，可对未见主题强在线适应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Fake News Video Detection (FNVD) is critical for social stability. Existing methods typically assume consistent news topic distribution between training and test phases, failing to detect fake news videos tied to emerging events and unseen topics. To bridge this gap, we introduce RADAR, the first framework that enables test-time adaptation to unseen news videos. RADAR pioneers a new retrieval-guided adaptation paradigm that leverages stable (source-close) videos from the target domain to guide robust adaptation of semantically related but unstable instances. Specifically, we propose an Entropy Selection-Based Retrieval mechanism that provides videos with stable (low-entropy), relevant references for adaptation. We also introduce a Stable Anchor-Guided Alignment module that explicitly aligns unstable instances' representations to the source domain via distribution-level matching with their stable references, mitigating severe domain discrepancies. Finally, our novel Target-Domain Aware Self-Training paradigm can generate informative pseudo-labels augmented by stable references, capturing varying and imbalanced category distributions in the target domain and enabling RADAR to adapt to the fast-changing label distributions. Extensive experiments demonstrate that RADAR achieves superior performance for test-time FNVD, enabling strong on-the-fly adaptation to unseen fake news video topics.

</details>

### 3. Many Ways to Be Fake: Benchmarking Fake News Detection Under Strategy-Driven AI Generation

📄 [arXiv](https://arxiv.org/abs/2604.09514) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`benchmark`、`misinformation`、`fact checking`、`source attribution`、`AI-generated fake news`、`mixed-truth content`

👤 **作者**：Xinyu Wang、Sai Koneru、Wenbo Zhang、Wenliang Zheng、Saksham Ranjan、Sarah Rajtmajer

- 🎯 **研究动机**：假新闻检测多视为二分类，而人机协作将策略性错误嵌入可信叙事的真假混合内容在基准中代表性不足
- 🔬 **研究方法**：MANYFAKE 以多策略 prompt 流水线生成 6,798 篇假新闻，覆盖多种造假与精炼方式，并评测 SOTA 检测器
- 📌 **结论**：推理增强模型在全虚构故事上接近饱和，但对细微、优化过且与真实信息交织的谎言仍然脆弱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in large language models (LLMs) have enabled the large-scale generation of highly fluent and deceptive news-like content. While prior work has often treated fake news detection as a binary classification problem, modern fake news increasingly arises through human-AI collaboration, where strategic inaccuracies are embedded within otherwise accurate and credible narratives. These mixed-truth cases represent a realistic and consequential threat, yet they remain underrepresented in existing benchmarks. To address this gap, we introduce MANYFAKE, a synthetic benchmark containing 6,798 fake news articles generated through multiple strategy-driven prompting pipelines that capture many ways fake news can be constructed and refined. Using this benchmark, we evaluate a range of state-of-the-art fake news detectors. Our results show that even advanced reasoning-enabled models approach saturation on fully fabricated stories, but remain brittle when falsehoods are subtle, optimized, and interwoven with accurate information.

</details>

### 4. VeriTaS: The First Dynamic Benchmark for Multimodal Automated Fact-Checking

🌐 [Project](https://veritas.mai.informatik.tu-darmstadt.de) · 🎓 [Official](https://aclanthology.org/2026.acl-long.1948/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`multimodal safety`、`VLM safety`、`misinformation`、`misinformation detection`

👤 **作者**：Mark Rothermel、Marcus Kornmann、Marcus Rohrbach、Anna Rohrbach

- 🎯 **研究动机**：现有 AFC 基准是静态的，声明进入 LLM 预训练语料造成数据泄漏，分数不再反映真实核查能力
- 🔬 **研究方法**：提出 VeriTaS 动态基准：25000 条来自 104 家专业核查机构、54 种语言的真实声明，七阶段全自动管道按季度增补并映射到标准化解耦评分
- 📌 **结论**：人工评估显示自动标注与人类判断高度吻合，建立抗泄漏的 AFC 评测基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The growing scale of online misinformation urgently demands Automated Fact-Checking (AFC). Existing benchmarks for evaluating AFC systems, however, are largely limited in terms of task scope, modalities, domain, language diversity, realism, or coverage of misinformation types. Critically, they are static, thus subject to data leakage as their claims enter the pretraining corpora of LLMs. As a result, benchmark performance no longer reliably reflects the actual ability to verify claims.We introduce Verified Theses and Statements (VeriTaS), the first dynamic benchmark for multimodal AFC, designed to remain robust under ongoing large-scale pretraining of foundation models. VeriTaS currently comprises 25,000 real-world claims from 104 professional fact-checking organizations across 54 languages, covering textual and audiovisual content. Claims are added quarterly via a fully automated seven-stage pipeline that normalizes claim formulation, retrieves original media, and maps heterogeneous expert verdicts to a novel, standardized, and disentangled scoring scheme with textual justifications.Through human evaluation, we demonstrate that the automated annotations closely match human judgments.We commit to updating VeriTaS in the future, establishing a leakage-resistant benchmark, supporting meaningful AFC evaluation in the era of rapidly evolving foundation models.The code and data are publicly available under https://veritas.mai.informatik.tu-darmstadt.de.

</details>

### 5. TrendFact: A Benchmark Towards Hotspot Perception in Automatic Fact-Checking

🎓 [Official](https://aclanthology.org/2026.acl-long.1219/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`fact-checking`、`misinformation`、`fact checking`、`misinformation detection`

👤 **作者**：Xiaocheng Zhang、…、Xiaohong Su

- 🎯 **研究动机**：自动事实核查系统在资源受限环境面临风险不对称，需按社会影响动态分配推理资源的热点感知能力（HPA），现有基准缺乏相关社会元数据与评估框架
- 🔬 **研究方法**：提出 TrendFact 基准：7643 个样本与 366634 条证据库，定义 ECS 与 HCPI 指标评估 HPA 及三项核查任务，并提出 FactISR 框架
- 📌 **结论**：现有 AFC 系统在 TrendFact 上表现有限，FactISR 有效提升 RLM 驱动系统的 HPA 与计算效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the surge of online misinformation, Large Language Models (LLMs) and Reasoning Large Language Models (RLMs) serving as Automatic Fact-Checking (AFC) systems have emerged as a prominent paradigm for reliable, explainable verification. However, our empirical study reveals that this paradigm faces a critical risk asymmetry challenge when deployed in real-world under resource-constrained environments. While Hotspot Perception Ability (HPA), the capacity to dynamically allocate reasoning resources based on social impact, is essential to mitigate this risk, existing benchmarks lack the social metadata and evaluation framework to meet this urgent evaluation needs, thereby hindering the advancement of these AFC systems. To bridge this gap, we introduce TrendFact, the first benchmark capable of evaluating HPA and three fact-checking tasks. It consists of 7,643 curated samples sourced from trending platforms and professional datasets, with an evidence library containing 366,634 entries. To enable HPA assessment, we propose two novel metrics: the Explanation Consistency Score (ECS) to evaluate the reliability of verification reasoning, and the Hotspot Claim Perception Index (HCPI) to quantify the overall HPA of AFC systems. Extensive experiments demonstrate that existing AFC systems exhibit limited performance on TrendFact. Furthermore, our proposed FactISR framework effectively enhances HPA and computational efficiency for RLM-driven systems.

</details>

### 6. Perception, Understanding and Reasoning: A Multimodal Benchmark for Video Fake News Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.2103/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`multimodal safety`、`reasoning safety`、`VLM safety`、`misinformation detection`

👤 **作者**：Cui Yakun、…、Sirui Han

- 🎯 **研究动机**：视频假新闻检测基准只看检测准确率，缺对检测全过程的细粒度评估
- 🔬 **研究方法**：POVFNDB 过程导向基准含 10 个任务、36,240 条人工标注 QA 与 15 个评估维度，系统评 MLLM 的感知、理解与推理；POVFND-CoT 生成推理数据微调模型
- 📌 **结论**：微调后的 Qwen2.5VL-7B-Instruct 在 VFND 上达 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The advent of multi-modal large language models (MLLMs) has greatly advanced research on video fake news detection (VFND) tasks. Existing benchmarks typically focus on the detection accuracy, while failing to provide fine-grained assessments for the entire detection process. To address these limitations, we introduce POVFNDB (Process-oriented Video Fake News Detection Benchmark), a process-oriented benchmark comprising 10 tasks designed to systematically evaluate MLLMs’ perception, understanding, and reasoning capabilities in VFND. This benchmark contains 36,240 human-annotated question-answer (QA) in structured or open-ended formats, spanning 15 distinct evaluation dimensions that characterize different aspects of the video fake news detection process.Using POVFNDB, we conduct comprehensive evaluations on both proprietary and open-source MLLMs. Moreover, We fine-tune Qwen2.5VL-7B-Instruct on a reasoning dataset generated by our proposed POVFND-CoT, a chain-of-thought method that utilizes rationales from evaluation results and rationale validation. The resulting model achieves sota performance on VFND.

</details>

### 7. LiveFact: A Dynamic, Time-Aware Benchmark for LLM-Driven Fake News Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.546/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`misinformation`、`fact checking`、`source attribution`、`misinformation detection`、`fact-checking`

👤 **作者**：Cheng Xu、…、Tahar Kechadi

- 🎯 **研究动机**：假新闻检测基准静态，易受基准数据污染且无法评估时间不确定下的推理
- 🔬 **研究方法**：LiveFact 持续更新，用动态时序证据集模拟信息演化的战争迷雾，双模式评测（分类/推理）并显式监测 BDC
- 📌 **结论**：22 个 LLM 测试显示 Qwen3-235B-A22B 等开源 MoE 已匹敌或超越专有 SOTA；发现推理鸿沟——强模型在早期数据片上承认不可验证主张

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid development of Large Language Models (LLMs) has transformed fake news detection and fact-checking tasks from simple classification to complex reasoning. However, evaluation frameworks have not kept pace. Current benchmarks are static, making them vulnerable to benchmark data contamination (BDC) and ineffective at assessing reasoning under temporal uncertainty. To address this, we introduce LiveFact a continuously updated benchmark that simulates the real-world “fog of war” in misinformation detection. LiveFact uses dynamic, temporal evidence sets to evaluate models on their ability to reason with evolving, incomplete information rather than on memorized knowledge. We propose a dual-mode evaluation: Classification Mode for final verification and Inference Mode for evidence-based reasoning, along with a component to monitor BDC explicitly. Tests with 22 LLMs show that open-source Mixture-of-Experts models, such as Qwen3-235B-A22B, now match or outperform proprietary state-of-the-art systems. More importantly, our analysis finds a significant “reasoning gap.” Capable models exhibit epistemic humility by recognizing unverifiable claims in early data slices-an aspect traditional static benchmarks overlook. LiveFact sets a sustainable standard for evaluating robust, temporally aware AI verification.

</details>

### 8. FactVerse: A Benchmark for Factual Consistency in Interleaved Image–Text Generation

🎓 [Official](https://aclanthology.org/2026.acl-long.1323/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`misinformation`、`fact checking`、`source attribution`、`fact-checking`、`content authenticity`

👤 **作者**：Yubo Shan、…、Yuanzhuo Wang

- 🎯 **研究动机**：交错图文生成内容传播力强，但现有基准缺乏评估其事实一致性的机制
- 🔬 **研究方法**：FactVerse 含 3000 个人工验证实例、4 大类 50 个域、中英双语，配多维事实一致性评估框架
- 📌 **结论**：评估框架与人类判断高度对齐并显著超越现有方法，揭示当前模型的系统性缺陷

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Interleaved multimodal understanding and generation—where models can interactively comprehend and produce images and text in arbitrary orders—has emerged as a key research direction in generative Multimodal Large Language Models(MLLMs). Such interleaved image–text content plays an increasingly important role in information dissemination. However, the compounded persuasive power of multimodal narratives also raises the risk of factual misinformation. Despite this, existing benchmarks lack effective mechanisms to evaluate factual consistency in interleaved image–text content. To bridge this gap, we introduce FactVerse, a benchmark dedicated to evaluating factual consistency in interleaved image-text generation. FactVerse comprises 3,000 human-verified instances across four categories and 50 domains, supporting both English and Chinese. We also establish a multi-dimensional evaluation framework designed to rigorously assess factual consistency. Experiments demonstrate that our framework achieves high alignment with human judgments, significantly outperforming existing evaluation methods. Furthermore, our analysis reveals systematic deficiencies in current models, offering critical insights for future design.

</details>

### 9. All That Glisters Is Not Gold: A Benchmark for Reference-Free Counterfactual Financial Misinformation Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.492/)　📅 2026　🏷 ACL 2026

**关键词**：`benchmark`、`misinformation detection`、`financial AI`、`misinformation`

👤 **作者**：Yuechen Jiang、…、Sophia Ananiadou

- 🎯 **研究动机**：金融新闻含义由分散线索构成，无参考场景下的金融误信息检测缺乏基准
- 🔬 **研究方法**：RFC-Bench 在段落级定义无参考误信息检测与原始-扰动配对诊断两个互补任务
- 📌 **结论**：有比较上下文时性能显著更强；无参考设定下预测不稳定、无效输出增多，模型难以维持连贯信念状态

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We introduce RFC-Bench, a benchmark for evaluating large language models on financial misinformation under realistic news. RFC-Bench operates at the paragraph level and captures the contextual complexity of financial news where meaning emerges from dispersed cues. The benchmark defines two complementary tasks: reference-free misinformation detection and comparison-based diagnosis using paired original–perturbed inputs. Experiments reveal a consistent pattern: performance is substantially stronger when comparative context is available, while reference-free settings expose significant weaknesses, including unstable predictions and elevated invalid outputs. These results indicate that current models struggle to maintain coherent belief states without external grounding. By highlighting this gap, RFC-Bench provides a structured testbed for studying reference-free reasoning and advancing more reliable financial misinformation detection in real-world settings.

</details>

### 10. LLM-based Few-Shot Early Rumor Detection with Imitation Agent

📄 [arXiv](https://arxiv.org/abs/2512.18352) · 🌐 [Project](https://doi.org/10.1145/3770854.3780315)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`early rumor`、`few-shot learning`、`imitation agent`

👤 **作者**：Fengzhu Zeng、…、Cheng Niu

- 🎯 **研究动机**：早期谣言样本稀缺，检测器冷启动难
- 🔬 **研究方法**：以imitation agent做LLM少样本早期谣言检测
- 📌 **结论**：少样本条件下提升早期检测效果

### 11. Persuasion at Play: Understanding Misinformation Dynamics in Demographic-Aware Human-LLM Interactions

🎓 [Official](https://aclanthology.org/2026.eacl-long.234/)　📅 2026-03　🏷 ACL 2026

**关键词**：`analysis`、`misinformation persuasion`、`demographic agent`、`echo chamber`

👤 **作者**：Angana Borah、Rada Mihalcea、Veronica Perez-Rosas

- 🎯 **研究动机**：误信息易感性存在人群差异，LLM 规模化生成说服内容带来新维度，双向说服动态未研究
- 🔬 **研究方法**：PANDORA 用多智能体 LLM 框架分析人群导向 agent 间误信息在说服下的传播动态
- 📌 **结论**：人口因素影响 LLM 易感性，组间误信息正确性差最多 15 个百分点；多智能体呈回音室与类人群体极化模式

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing challenges in misinformation exposure and susceptibility vary across demographics, as some populations are more vulnerable to misinformation than others. Large language models (LLMs) introduce new dimensions to these challenges through their ability to generate persuasive content at scale and reinforcing existing biases. Our study introduces PANDORA, a framework that investigates the bidirectional persuasion dynamics between LLMs and humans when exposed to misinformative content. We use a multi-agent LLM framework to analyze the spread of misinformation under persuasion among demographic-oriented LLM agents. Our findings show that demographic factors influence LLM susceptibility, with up to 15 percentage point differences in misinformation correctness across groups. Multi-agent LLMs also exhibit echo chamber behavior, aligning with human-like group polarization patterns. Therefore, this work highlights demographic divides in misinformation dynamics and offers insights for future interventions.

</details>

### 12. Wikipedia in the Era of LLMs: Evolution and Risks

📄 [arXiv](https://arxiv.org/abs/2503.02879) · 🎓 [Official](https://icml.cc/virtual/2026/poster/68815)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`misinformation`、`fact checking`、`source attribution`、`empirical evaluation`、`content provenance`

👤 **作者**：Siming Huang、Yuliang Xu、Mingmeng Geng、Yao Wan、Dongping Chen

- 🎯 **研究动机**：LLM 对 Wikipedia 的影响与潜在风险缺乏系统分析框架
- 🔬 **研究方法**：分析条目内容与页面浏览量评估 LLM 影响，评测其对机器翻译、RAG 等 NLP 任务的作用，并用模拟探索风险
- 📌 **结论**：部分类别约 1% 内容已受影响；若翻译基准被污染则分数虚高、模型排序改变，知识受污染也会降低 RAG 有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we present a comprehensive analysis and monitoring framework for the impact of Large Language Models (LLMs) on Wikipedia, examining the evolution of Wikipedia through existing data and using simulations to explore potential risks. We begin by analyzing article content and page views to study the recent changes in Wikipedia and assess the impact of LLMs. Subsequently, we evaluate how LLMs affect various Natural Language Processing (NLP) tasks related to Wikipedia, including machine translation and retrieval-augmented generation (RAG). Our findings and simulation results reveal that Wikipedia articles have been affected by LLMs, with an impact of approximately 1% in certain categories. If the machine translation benchmark based on Wikipedia is influenced by LLMs, the scores of the models may become inflated, and the comparative results among models could shift. Moreover, the effectiveness of RAG might decrease if the knowledge has been contaminated by LLMs. While LLMs have not yet fully changed Wikipedia's language and knowledge structures, we believe that our empirical findings signal the need for careful consideration of potential future risks in NLP research.

</details>

### 13. Gaming Consensus: Coordinated Manipulation in Crowdsourced Fact-Checking

📄 [arXiv](https://arxiv.org/abs/2607.01824) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64544)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`misinformation`、`fact checking`、`source attribution`、`deepfake detection`、`mechanistic analysis`

👤 **作者**：Nikil Roashan Selvam、…、Sanmi Koyejo

- 🎯 **研究动机**：X、Meta 部署的众包事实核查 bridging 机制（矩阵分解）能否被协同用户策略性操纵缺乏系统评估
- 🔬 **研究方法**：用历史生产数据与理论分析评估协同用户利用潜在表示伪造共识的能力，并给出操纵代价模型
- 📌 **结论**：不到 10 个评分即可将最多 10.7% 低质 note 抬过共识阈值；给 Not Helpful 反而可能提升其分数；已在 X 的 Community Notes 部署缓解措施

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Crowdsourced fact-checking systems have been adopted by major social media companies such as X, Meta, TikTok and Google with the aim of combating misleading information at scale without relying on centralized editorial control. These systems have been developed around a common underlying concept: a bridging mechanism that identifies notes flagging misleading information when they receive support from people with different perspectives rather than simple majority support. To our knowledge the only publicly disclosed bridging algorithms deployed for fact-checking are based on matrix factorization, as deployed by both X and Meta, augmented with additional components addressing abuse, targeted manipulation, and contributor brigades. This work examines the core matrix factorization portion of these systems, presenting theoretical and empirical evaluations of the degree to which coordinated users could vote strategically by leveraging the latent representations to fabricate the appearance of synthetic consensus within the bridging mechanism. Using historic production data, we find that up to 10.7% of lower quality notes could be manipulated above consensus thresholds using less than 10 ratings. We complement these findings with a theoretical analysis, revealing counterintuitively that rating a note as ``Not Helpful'' can increase its helpfulness score, as well as a cost model quantifying manipulation effort. We have developed and deployed mitigations within X's Community Notes algorithm to address synthetic consensus.

</details>

### 14. Beyond the Crowd: LLM-Augmented Community Notes for Governing Health Misinformation

🎓 [Official](https://aclanthology.org/2026.acl-long.233/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`misinformation detection`、`misinformation`、`fact checking`、`medical AI`

👤 **作者**：Jiaying Wu、…、Min-Yen Kan

- 🎯 **研究动机**：X 平台 Community Notes 中位延迟 17.6 小时（30.8K 条健康笔记），且投票者常把风格流畅度与事实准确性混淆
- 🔬 **研究方法**：CrowdNotes+ 统一 LLM 框架：证据落地的笔记增强与效用引导的笔记自动化，配相关性、正确性、有用性三阶段层级评估；构建 1.2K 条 HealthNotes 基准与微调有用性裁判
- 📌 **结论**：15 个代表性 LLM 上 CrowdNotes+ 在笔记正确性、有用性与证据效用上显著超越人类贡献者

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Community Notes, the crowd-sourced misinformation governance system on X (formerly Twitter), allows users to flag misleading posts, attach contextual notes, and rate the notes’ helpfulness. However, our empirical analysis of 30.8K health-related notes reveals substantial latency, with a median delay of 17.6 hours before notes receive a helpfulness status. To improve responsiveness during real-world misinformation surges, we propose CrowdNotes+, a unified LLM-based framework that augments Community Notes for faster and more reliable health misinformation governance. CrowdNotes+ integrates two modes: (1) evidence-grounded note augmentation and (2) utility-guided note automation, supported by a hierarchical three-stage evaluation of relevance, correctness, and helpfulness. We instantiate the framework with HealthNotes, a benchmark of 1.2K health notes annotated for helpfulness, and a fine-tuned helpfulness judge. Our analysis first uncovers a key loophole in current crowd-sourced governance: voters frequently conflate stylistic fluency with factual accuracy. Addressing this via our hierarchical evaluation, experiments across 15 representative LLMs demonstrate that CrowdNotes+ significantly outperforms human contributors in note correctness, helpfulness, and evidence utility.

</details>

### 15. Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems

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

### 16. ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains

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

### 17. Are Rationales Necessary and Sufficient? Tuning LLMs for Explainable Misinformation Detection

📄 [arXiv](https://arxiv.org/abs/2605.19285) · 🌐 [Project](https://doi.org/10.1145/3770855.3817644)　📅 2026-05　🏷 KDD 2026

**关键词**：`detection`、`misinformation rationale`、`data filtering`、`explainability`

👤 **作者**：Bing Wang、…、Jieping Ye

- 🎯 **研究动机**：可解释虚假信息检测中，仅按标签正确过滤训练数据导致理由不充分（粗标签）与过度验证（强 LLM 冗长）两类缺陷
- 🔬 **研究方法**：LONSREX 量化每个验证步骤对最终预测的贡献以评估必要性与充分性，据此定位并合成必要且充分的理由
- 📌 **结论**：实验证实 LONSREX 数据合成管线有效提升可解释检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid spread of misinformation on social media platforms has become a formidable challenge. To mitigate its proliferation, Misinformation Detection (MD) has emerged as a critical research topic. Traditional MD approaches based on small models typically perform binary classification through a black-box process. Recently, the rise of Large Language Models (LLMs) has enabled explainable MD, where models generate rationales that explain their decisions, thereby enhancing transparency. Existing explainable MD methods primarily focus on crafting sophisticated prompts to elicit rationales from off-the-shelf LLMs. In this work, we propose a pipeline to fine-tune a dedicated LLM specifically for explainable MD. Our pipeline begins by collecting large-scale fact-checked articles, and then uses multiple strong LLMs to produce veracity predictions and rationales. To ensure high-quality training data, we leverage a filtering strategy that selects only the correct instances for fine-tuning. While this pipeline is intuitive and prevalent, our experiments reveal that naive filtering based solely on label correctness is insufficient in practice and suffers from two critical limitations: (1) Coarse-grained labels cause insufficient rationales: Rationales filtered solely based on binary labels are insufficient to adequately support their decisions; (2) Over-verification behavior causes unnecessary rationales: Stronger LLMs tend to exhibit over-verification behavior, producing excessively verbose and unnecessary rationales. To address these issues, we introduce LONSREX, a novel data synthesis pipeline to Locate Necessary and Sufficient Rationales for Explainable MD. Specifically, we propose a metric that quantifies the contribution of each verification step to the final prediction, thereby evaluating its necessity and sufficiency. Experimental results demonstrate the effectiveness of LONSREX.

</details>

### 18. REFLEX: Self-Refining Explainable Fact-Checking via Verdict-Anchored Style Control

🎓 [Official](https://aclanthology.org/2026.acl-long.202/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`fact-checking`、`misinformation`、`fact checking`、`misinformation detection`

👤 **作者**：Chuyi Kong、Wei Gao、Jing Ma、Hongzhan Lin、Yuxi Sun

- 🎯 **研究动机**：LLM 事实核查的解释忽视误导性文风导致不忠实理据，且依赖外部知识引入幻觉与延迟
- 🔬 **研究方法**：提出 REFLEX：以预测裁决为锚控制推理文风，利用骨干模型与其微调变体间的自分歧真伪信号构造 steering vector，分离事实内容与文风线索
- 📌 **结论**：仅用 465 个自精炼样本即在 LLaMA 系列上达到 SOTA，野外数据最高提升 7.54 Macro-F1，并缓解忠实性幻觉

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The prevalence of fake news on social media calls for automated fact-checking systems that deliver not only accurate verdicts but also faithful explanations. However, existing large language model (LLM)-based methods often overlook deceptive misinformation styles in generated explanations, producing unfaithful rationales that may mislead human judgment. They also rely heavily on external knowledge sources, which can introduce hallucinations and incur substantial latency, undermining both reliability and responsiveness in real-time settings. To address these limitations, we propose REason-guided Fact-checking with Latent EXplanations (REFLEX), a self-refining framework that explicitly controls reasoning style by anchoring explanations to the predicted verdict. REFLEX leverages self-disagreement veracity signals between a backbone model and its fine-tuned variant to construct steering vectors, thereby naturally disentangling factual content from stylistic cues. Experiments on a real-world benchmark show that REFLEX achieves state-of-the-art performance under LLaMA-series models using only 465 self-refined samples. Owing to its transferability, REFLEX also yields gains of up to 7.54 Macro-F1 points on in-the-wild data. Further analysis shows that our method effectively mitigates faithful hallucination, leading to both more reliable explanations and more accurate verdicts than prior explainable fact-checking approaches.

</details>

### 19. Emergent Communication Under Misinformation

🎓 [Official](https://icml.cc/virtual/2026/poster/61022)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`misinformation`、`fact checking`、`source attribution`、`empirical evaluation`、`content provenance`

👤 **作者**：Heeyoung Lee、Kyungwoo Song

- 🎯 **研究动机**：消息可经恶意中间人修改后到达接收方，但该误信息维度在涌现通信研究中被忽视
- 🔬 **研究方法**：设计含恶意中间人的发送者-接收者通信游戏，考察误信息对语言涌现（尤其组合性）的影响
- 📌 **结论**：恶意误传风险促进组合性语言涌现；中间人适应性是形成持续组合性压力的关键，只针对部分属性的部分误信息也能诱导组合性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Social interactions are characterized by both adversarial and cooperative aspects. Communications between agents may also involve adversarially motivated actors. Messages can pass through intermediaries with malicious intent before reaching the intended receiver. These actors may modify the message to induce misunderstanding from the receiver while preserving the overall characteristics of the message. This form of misinformation is prevalent in real-world communications and may affect the dynamics under which communication protocols are developed. However, this aspect of social interaction is relatively underexplored in many emergent communication studies that aim to understand the environmental factors behind the emergence of languages' characteristics. This work explores how misinformation affects language emergence with a focus on compositionality. We design a communication game containing a malign intermediary between the sender and receiver. We find that risks of malign misrepresentation promote the emergence of compositional languages in simulations of communicative agents. Furthermore, we observe that adaptability of malign intermediaries is a crucial factor in forming a consistent pressure toward compositionality and that partial misinformation, in which the intermediary targets only a subset of attributes, can also induce compositionality.

</details>

### 20. DiNO: Disinformation Narrative Observer

🎓 [Official](https://aclanthology.org/2026.acl-long.2160/)　📅 2026　🏷 ACL 2026

**关键词**：`analysis`、`misinformation`、`fact checking`、`source attribution`、`misinformation detection`、`fact-checking`

👤 **作者**：Witold Sosnowski、Arkadiusz Modzelewski、Kinga Skorupska、Adam Wierzbicki

- 🎯 **研究动机**：虚假信息分析需要把相关假主张聚为可跨文化、时间与媒体追踪的叙事，缺乏有效提取方法
- 🔬 **研究方法**：DiNO 从新闻文章提取虚假信息叙事，应用于乌克兰战争、COVID-19 与移民议题的易虚假信息媒体及可信源
- 📌 **结论**：主题对齐比 Relatio、CaNarEx 提升 41 至 44%，立场对齐提升 30 至 41%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Disinformation is an escalating global threat, making it essential to understand its content, dissemination, and evolution. To confront this challenge, researchers have begun grouping related false claims into broader disinformation narratives, which can be tracked across cultures, time periods, and media sources. Analyzing these narratives provides critical insights for developing more effective countermeasures. To this end, we introduce DiNO: Disinformation Narrative Observer, a novel method designed to extract disinformation narratives from news articles. We applied DiNO to news articles on the Ukraine War, COVID-19 and Migration, sourced from disinformation-prone outlets as well as a reputable source. We evaluated the narratives extracted by DiNO by measuring how well their topics and stances aligned with a recognized disinformation narratives dataset. DiNO outperforms competitive narrative mining approaches, including Relatio and CaNarEx, achieving a 41%–44% improvement in topical alignment and a 30%–41% improvment in stance alignment.

</details>

### 21. CoT is Not the Chain of Truth: An Empirical Internal Analysis of Reasoning LLMs for Fake News Generation

📄 [arXiv](https://arxiv.org/abs/2602.04856) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61042)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`misinformation`、`fact checking`、`source attribution`、`chain-of-thought`、`content provenance`

👤 **作者**：Zhao Tong、…、Xiao-Yu Zhang

- 🎯 **研究动机**：拒绝即全程推理安全的假设不成立——模型拒绝有害请求时 CoT 内部仍可能包含并传播不安全叙事
- 🔬 **研究方法**：跨模型层解构 CoT 生成，用 Jacobian 谱指标评估注意力头，提出 stability、geometry、energy 三个度量量化注意力头如何嵌入欺骗性推理
- 📌 **结论**：思考模式激活时生成风险显著上升，关键路由决策集中在少数连续中深度层；拒绝不等于安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

From generating headlines to fabricating news, the Large Language Models (LLMs) are typically assessed by their final outputs, under the safety assumption that a refusal response signifies safe reasoning throughout the entire process. Challenging this assumption, our study reveals that during fake news generation, even when a model rejects a harmful request, its Chain-of-Thought (CoT) reasoning may still internally contain and propagate unsafe narratives. To analyze this phenomenon, we introduce a unified safety-analysis framework that systematically deconstructs CoT generation across model layers and evaluates the role of individual attention heads through Jacobian-based spectral metrics. Within this framework, we introduce three interpretable measures: stability, geometry, and energy to quantify how specific attention heads respond or embed deceptive reasoning patterns. Extensive experiments on multiple reasoning-oriented LLMs show that the generation risk rise significantly when the thinking mode is activated, where the critical routing decisions concentrated in only a few contiguous mid-depth layers. By precisely identifying the attention heads responsible for this divergence, our work challenges the assumption that refusal implies safety and provides a new understanding perspective for mitigating latent reasoning risks.

</details>

### 22. MMMMM: A Unified Taxonomy for Investigating the Mechanisms of Multilingual MultiModal Misinformation

📄 [arXiv](https://arxiv.org/abs/2608.29681)　📅 2026-09

**关键词**：`analysis`、`multilingual misinformation`、`image-text deception`、`human-validated taxonomy`

👤 **作者**：Nadav Borenstein、Greta Warren、Desmond Elliott、Isabelle Augenstein

- 🎯 **研究动机**：多模态错误信息缺少基于真实语境的分类体系，现有模型也难以支撑规模化的自动标注分析
- 🔬 **研究方法**：收集七种语言 Twitter/X 真实错误信息，经定性分析构建综合分类体系，并用 VLM 多步标注管线加人工验证操作化
- 📌 **结论**：揭示主题特异的图文欺骗机制：AI 生成内容集中于科技主题，疫苗错误信息多挪用新闻图片以增信，缓解应分主题施策

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal misinformation on social media is highly prevalent, potent, and harmful, yet difficult to detect and counter, and still poorly understood compared to its text-only counterpart. Research on the properties and deceptive strategies of multimodal misinformation is hindered by a lack of taxonomies grounded in real-world contexts and by the limitations of current multimodal machine learning models, which prevent the automation of annotation and analysis at scale. We address these shortcomings in three steps. First, we collect a large-scale, high-quality dataset of real-world misinformation instances from Twitter/X in seven languages. Second, we develop a novel, comprehensive taxonomy of multimodal misinformation grounded in an in-depth qualitative analysis of the data and prior theoretical work. Finally, we operationalise the taxonomy through an automated multi-step annotation pipeline using a Vision-Language Model (VLM), and perform human-validation. Our novel approach leads to previously undocumented insights about how social media users combine images with text to spread misinformation in the wild, e.g., that AI-generated content is particularly prevalent in technology and science, while vaccination misinformation disproportionately utilises images from news outlets to assert credibility. Our method and findings provide guidance for targeted approaches for detecting multimodal misinformation, and suggest that mitigation efforts should be developed and applied strategically rather than uniformly.

</details>

### 23. A Serial Two-Stage Framework for Robust Multimodal Fake News Detection via Adaptive Reasoning

🌐 [Project](https://doi.org/10.1145/3770855.3817957)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`multimodal fake news`、`adaptive reasoning`、`evidence fusion`

- 🎯 **研究动机**：多模态假新闻检测对不完整或干扰证据不够鲁棒
- 🔬 **研究方法**：提出串行两阶段框架，先自适应推理再融合证据判定
- 📌 **结论**：鲁棒性显著优于单阶段检测基线

### 24. Beyond Content: Integrating Generated User Intent and Planned Behavior Theory for Reliable Fake News Detection

🌐 [Project](https://doi.org/10.1145/3770854.3780276)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`fake news`、`user intent`、`behavior theory`

- 🎯 **研究动机**：生成 AI 使真伪内容边界模糊，仅靠内容或传播结构的检测忽视用户行为的心理动机，易受对抗操纵
- 🔬 **研究方法**：TPB-VAE 把计划行为理论构念映射到潜空间使决策过程可计算，半监督地从少量标注样本推断用户潜意图并派生行为特征
- 📌 **结论**：四个真实数据集上验证检测有效性与对抗鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the rise of generative AI, the boundary between authentic and deceptive content has become increasingly ambiguous, challenging traditional fake news detection methods that rely solely on observable content or propagation structures. These approaches often neglect the underlying psychological motivations driving user behavior, leaving them susceptible to adversarial manipulation. However, as the user decision-making process is inherently unobservable, conventional deep learning models struggle to capture the cognitive mechanisms behind information sharing. To address this, we propose TPB-VAE, a psychologically grounded framework that integrates the Theory of Planned Behavior (TPB) with large language models (LLMs) to infer and encode users' latent intent. TPB-VAE maps TPB constructs into a latent space, making the decision-making process computationally accessible. It employs semi-supervised learning specifically to infer users' latent intent from a small subset of labeled samples, and uses the resulting intents to derive rich behavioral features for more reliable fake news detection. Extensive experiments on four real-world datasets demonstrate the effectiveness and adversarial resilience of our approach.

</details>

### 25. MAR: Metacognitive Agentic Reasoning for Multimodal Fake News Detection

🌐 [Project](https://doi.org/10.1145/3770855.3818025)　📅 2026-08　🏷 KDD 2026

**关键词**：`detection`、`multimodal fake news`、`metacognition`、`agentic reasoning`

- 🎯 **研究动机**：有监督小多模态模型受训练数据知识范围限制，遇新内容退化且只给不可解释的真假二分
- 🔬 **研究方法**：MAR 用 Believer 与 Skeptic 的三阶段 Draft-Self-Critique-Refine 元认知辩论，动态检索网络与反向图搜等可信外部知识缓解幻觉
- 📌 **结论**：两个基准上 SOTA，泛化与可解释性显著优于现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

multimodal fake news combining text and images has become increasingly prevalent, fueled by the rapid dissemination on social media. Existing approaches predominantly rely on supervised learning–driven small multimodal language models, yet they are constrained by the knowledge scope and logical reasoning capabilities limited by training data: their performance degrades significantly when encountering novel content not covered in the training data, and they typically provide only uninterpretable binary true/false predictions. To address these challenges, we propose the Metacognitive Agentic Reasoning for multimodal Fake News Detection(MAR), a framework that integrates multi-agent metacognitive debate with external knowledge retrieval to enhance the accuracy, generalization, and interpretability of multimodal fake news detection. At its core, MAR introduces a news-domain informed and metacognition-inspired multi-agent reasoning mechanism: it first generates several prior pseudo-labels of the news domain, and defines the characteristics of two opposing agents (i.e., Believer and Skeptic) leveraging these pseudo-labels; then, the Believer and Skeptic go through a three-stage ''Draft – Self-Critique – Refine'' interactive debate simulating humans' learning behavior, called the metacognitive debate. Specifically, MAR first generates an initial evidence-grounded judgment (Draft), then critically reflects on their own and others' arguments (Self-Critique), and finally iteratively refines their conclusions by incorporating internal or external evidence (Refine). To improve factual reliability, the framework dynamically retrieves trustworthy external knowledge via web and reverse image searches, thereby mitigating the hallucinations inherent in large language models. Experiments show that MAR achieves state-of-the-art performance on two benchmarks and significantly outperforms existing methods in terms of generalization and interpretability. The source code is available at https://github.com/Averdgr/MAR_KDD.

</details>

### 26. When Misinformation Speaks and Converses: Rethinking Fact-Checking in Audio Platforms

🎓 [Official](https://aclanthology.org/2026.acl-long.93/)　📅 2026　🏷 ACL 2026

**关键词**：`tool`、`misinformation detection`、`misinformation`、`fact-checking`

👤 **作者**：Chaewan Chun、Delvin Ce Zhang、Dongwon Lee

- 🎯 **研究动机**：音频平台已成为公共话语与误信息的主要渠道，但事实核查管道为书面声明设计，忽略口语的韵律情感说服力与跨轮次对话结构
- 🔬 **研究方法**：跨模态与平台综合证据，审视现有数据集与方法，分析管道在音频上失败的原因
- 📌 **结论**：推进事实核查需围绕口语与对话本质重构验证管道

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Audio platforms have evolved beyond entertainment. They have become central to public discourse, from podcasts and radio to WhatsApp voice notes and live streams. With millions of shows and hundreds of millions of listeners, audio platforms are now a major channel for misinformation. Yet existing fact-checking pipelines are mostly designed for written claims, overlooking the unique properties of spoken media. We argue that audio misinformation is not merely textual content with transcripts: it is structurally different because it is both spoken—carrying persuasive force through prosody, pacing, and emotion—and conversational—unfolding across turns, speakers, and episodes. These dual properties introduce verification difficulties that traditional methods rarely face. This position paper synthesizes evidence across modalities and platforms, examines datasets and methods, and highlights why existing pipelines fail on audio. We argue that advancing fact-checking requires rethinking verification pipelines around the spoken and conversational realities of audio.

</details>

### 27. From Form to Logic: Masked Reconstruction and Reasoning Distillation for Short Video Fake News Detection

🎓 [Official](https://aclanthology.org/2026.acl-long.579/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`reasoning safety`、`misinformation`、`fact checking`、`model provenance`、`misinformation detection`

👤 **作者**：Qingyan Wang、Lianwei Wu、Botao Wang、Wangkang、Yaxiong Wang

- 🎯 **研究动机**：短视频假新闻检测受全局对齐偏置（错过局部不一致）与 LLM 方法幻觉、高延迟之困
- 🔬 **研究方法**：PCDD 感知-认知双驱动：感知流把局部不一致放大为显式差异，认知流把 LLM 推理蒸馏到轻量学生、推理时无需 LLM
- 📌 **结论**：真实数据集上持续超基线，可解释性与数据稀缺场景鲁棒性更佳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid growth of short video platforms has made multimodal fake news more prevalent. Existing detectors suffer from two major limitations: (I) global-alignment bias that overemphasizes holistic cross-modal matching and thus misses subtle, localized inconsistencies; and (II) LLM-based methods that leverage powerful generative reasoning to identify cognitive forgeries but inherently suffer from hallucinations and high inference latency. To overcome these limitations, we propose PCDD, a novel Perception-Cognition Dual-driven Detector that jointly observes the form and probes the logic for short video fake news detection. The perception stream exposes fine-grained cross-modal conflicts by amplifying localized inconsistencies into explicit discrepancies. The cognition stream transfers reasoning capabilities from LLMs to a lightweight student to mine cognitive forgeries, while reducing the risk of hallucinations and eliminating reliance on LLMs at inference. Experiments on real-world datasets show that PCDD consistently outperforms baselines, while improving interpretability and robustness in data scarcity scenarios. Our code is available at: https://github.com/SeinCore/PCDD.

</details>

### 28. From Detection to Understanding: Multi-Turn Reasoning for Video Misinformation Analysis

🎓 [Official](https://aclanthology.org/2026.acl-long.1716/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`reasoning safety`、`misinformation detection`、`misinformation`

👤 **作者**：Zhi Zeng、…、Zihan Ma

- 🎯 **研究动机**：视频误信息检测被当作二元真伪分类，忽视内容如何与为何误导的推理；现有基准不覆盖操纵策略多样性也不评过程级论证
- 🔬 **研究方法**：MisVideoQA 多轮基准覆盖 12 个细粒度欺骗类别、沿感知归因到意图与说服分析六维度；MisAgent 用 Delphi 启发的多智能体协作整合多模态线索与外部证据
- 📌 **结论**：SOTA MLLM 表现差，MisAgent 一致提升推理准确率与解释质量

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Video misinformation detection is often approached as a binary veracity classification problem, overlooking the complex reasoning required to explain how and why content misleads. Existing benchmarks fail to capture the diversity of manipulation strategies, such as AI-generated edits and out-of-context manipulation, and do not evaluate whether models can provide process-level justifications for their judgments. We address these limitations with MisVideoQA, a multi-turn benchmark designed to assess comprehensive understanding and reasoning in video misinformation analysis. MisVideoQA covers 12 fine-grained deception categories and evaluates models along six dimensions, progressing from perceptual attribution to intent and persuasion analysis. Recognizing that standard MLLMs struggle to sustain such structured, evidence-based deduction, we propose MisAgent, a Delphi-inspired multi-agent framework in which specialized agents collaboratively integrate multimodal cues with external evidence. Experimental results show that state-of-the-art multimodal large language models perform poorly on MisVideoQA, while MisAgent consistently improves reasoning accuracy and explanation quality. Together, our benchmark and framework establish a unified foundation for reliable, interpretable, and evidence-grounded video misinformation analysis.

</details>

### 29. FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2602.22963) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65720)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`misinformation`、`reinforcement learning`、`fact checking`、`content provenance`

👤 **作者**：Zehao Li、…、Zhaoqi Wang

- 🎯 **研究动机**：MLLM 视频误信息检测依赖固定深度推理并过度信任内部假设，关键证据稀疏碎片化时失效
- 🔬 **研究方法**：FactGuard 把验证形式化为 MLLM 上的迭代推理：显式评估任务歧义并选择性调用外部工具；两阶段训练结合领域 agent SFT 与决策感知强化学习
- 📌 **结论**：三个公开基准上验证准确率与可靠性均超 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal large language models (MLLMs) have substantially advanced video misinformation detection through unified multimodal reasoning, but they often rely on fixed-depth inference and place excessive trust in internally generated assumptions, particularly in scenarios where critical evidence is sparse, fragmented, or requires external verification. To address these limitations, we propose FactGuard, an agentic framework for video misinformation detection that formulates verification as an iterative reasoning process built upon MLLMs. FactGuard explicitly assesses task ambiguity and selectively invokes external tools to acquire critical evidence, enabling progressive refinement of reasoning trajectories. To further strengthen this capability, we introduce a two-stage training strategy that combines domain-specific agentic supervised fine-tuning with decision-aware reinforcement learning to optimize tool usage and calibrate risk-sensitive decision making. Extensive experiments on three public benchmarks demonstrate that FactGuard consistently outperforms state-of-the-art methods in both verification accuracy and reliability.

</details>

### 30. VMD-FACT: A New Video Dataset and MLLM-based method for Detecting Realistic AI-Generated Video Misinformation

🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_VMD-FACT_A_New_Video_Dataset_and_MLLM-based_method_for_Detecting_CVPR_2026_paper.html)　📅 2026　🏷 CVPR 2026

**关键词**：`benchmark`、`video misinformation`、`AI-generated content`、`MLLM detection`

👤 **作者**：Yongkang Zhang、Dongyu She、Baiyu Ji、Qichuan Geng、Zhong Zhou、Yan Wang

- 🎯 **研究动机**：现有视频误信息数据集靠编辑破坏跨模态一致性，伪迹不真实且易检；生成式视频误信息则追求跨模态语义一致以保持真实感
- 🔬 **研究方法**：提出 RAVM 数据集，涵盖声明、视频、音频与跨模态四类操纵源并用 agent 驱动框架生成；提出 IEEG 模型把多模态证据、核查结果及依赖表示为证据图
- 📌 **结论**：现有 MLLM 在 RAVM 上检测能力脆弱，IEEG 达到 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid evolution of generative AI, including such models as Sora, has intensified the threat of video misinformation. A critical challenge in detecting these AI-generated video misinformation lies in a fundamental disconnect between existing datasets and practical deception tactics. Current datasets often disrupt cross-modal consistency through editing techniques, resulting in unrealistic and easily detectable artifacts. By contrast, generative video misinformation strives for semantic consistency across modalities to remain realism. To address this gap, we introduce RAVM: the first Realistic AI-Generated Video Misinformation Detection Dataset. Unlike existing Video Misinformation Detection (VMD) datasets that are limited to single-source manipulations, RAVM encompasses multiple manipulation sources--Claim, Video, Audio, and Cross-Modal Manipulation--each incorporating diverse manipulation techniques to generate realistic AI-generated video misinformation. To achieve this, we introduce an agent-driven framework for generating realistic video misinformation. Furthermore, we propose an IEEG model that represents multimodal evidence, fact-checking results, and their dependencies as an evidence graph for interpretable detection of AI-generated video misinformation. Extensive experiments on RAVM reveal the vulnerability of existing Multimodal Large Language Models (MLLMs) in detecting AI-generated video misinformation, while the proposed IEEG achieves state-of-the-art performance on RAVM. The dataset is publicly available at: https://gitee.com/VR_NAVE/ravm

</details>

### 31. Falsdo: Benchmarking Artifact-Controlled Multimodal Fake News Verification via Failure-Aligned Auditing

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/686.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`benchmark`、`multimodal misinformation`、`artifact control`、`evidence audit`

- 🎯 **研究动机**：现有基准无法把真语义核查与表面捷径利用（依赖生成伪影）区分开
- 🔬 **研究方法**：FALSDO 经异构网络挖掘构建：指令条件化落地加反事实伪影控制协议（拉平低级生成痕迹做压力测试）；并提出显式噪声控制证据获取与可靠性感知晚融合的 DREA 基线
- 📌 **结论**：伪影拉平后检测器性能退化，证明其依赖伪影而非稳健验证；DREA 提升 Joint-F1 并在伪影控制下最小化退化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent generative AI renders multimodal misinformation structurally harder to detect, making reliable detection dependent on semantic verification grounded in verifiable evidence. However, current benchmarks often fail to isolate true semantic checking from superficial shortcut exploitation. We introduce FALSDO, a diagnostic benchmark designed to make robustness and auditability identifiable. Constructed via a heterogeneous web-mining pipeline, FALSDO provides instruction-conditioned grounding and formalizes a counterfactual artifact-control protocol. This stress test reveals a critical failure: when low-level generation traces are equalized, detector performance degrades, indicating reliance on artifacts rather than robust verification. To enable reproducible diagnosis, we propose DREA, a failure-aligned evidence-auditing baseline. DREA specifies evidence acquisition with explicit noise control and implements constrained channel-wise auditing with reliability-aware late fusion. Experiments demonstrate that FALSDO reliably exposes shortcut dependence, while DREA improves instruction-level grounding (Joint-F1) and minimizes degradation under artifact-controlled settings.

</details>

### 32. When Evidence Falls Short: Router-Guided Fake News Detection with Pattern Augmentation

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/4589.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`detection`、`fake news`、`evidence routing`、`deception pattern`

- 🎯 **研究动机**：LLM 事实核查高度依赖证据，面对不可靠、噪声或稀缺证据时脆弱；而 LLM 又缺乏欺骗模式的专业知识
- 🔬 **研究方法**：提出 RGPA：层级路由（案例路由器与外部证据路由器）按多维质量评估引导推理路径，专家模型捕获欺骗特征并融入 LLM 推理
- 📌 **结论**：两个真实数据集上显著超越现有方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

With the growing complexity of online information, trustworthy fake news detection has become increasingly critical. Although Large Language Models (LLMs) exhibit a strong ability to leverage factual evidence for verification, they remain highly vulnerable to unreliable, noisy, or scarce evidence, undermining robustness in real-world scenarios. Given the generalizability of deceptive patterns in fake news, we consider pattern as a complementary signal under insufficient evidence during factual verification. However, due to LLMs’ lack of expertise in deception-specific patterns, realizing such effective collaboration remains challenging. To address these issues, we propose a RouterGuided Fake News Detection Framework with Pattern Augmentation (RGPA). Specifically, we introduce a hierarchical routing mechanism including a case router and an external evidence router. It guides news to appropriate reasoning paths adaptively based on a multi-dimensional quality assessment, prioritizing high-quality evidence while mitigating noise. Furthermore, we design an expert model to capture deceptive features and integrate them into LLMs’ reasoning, enabling a synergy of factual verification and pattern awareness under evidence-scarce scenarios. Extensive experiments on two real-world datasets demonstrate that RGPA significantly outperforms existing approaches.

</details>

### 33. The Coherence Trap: When MLLM-Crafted Narratives Exploit Manipulated Visual Contexts

📄 [arXiv](https://arxiv.org/abs/2505.17476) · 🎓 [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_The_Coherence_Trap_When_MLLM-Crafted_Narratives_Exploit_Manipulated_Visual_Contexts_CVPR_2026_paper.html)　📅 2025-05　🏷 CVPR 2026

**关键词**：`attack`、`visual misinformation`、`MLLM narrative`、`context manipulation`

👤 **作者**：Yuchen Zhang、Yaxiong Wang、Yujiao Wu、Lianwei Wu、Li Zhu、Zhedong Zheng

- 🎯 **研究动机**：现有操纵检测面向规则式文本篡改，低估 MLLM 生成语义连贯欺骗叙事的风险
- 🔬 **研究方法**：构建 MDSM 数据集（先进图像编辑配 MLLM 语义一致欺骗文本），提出 AMD 框架以伪影预感知编码与操纵导向推理检测
- 📌 **结论**：跨域测试平均 88.18 ACC、60.25 mAP、61.02 mIoU，验证对 MLLM 多模态欺骗的泛化检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The detection and grounding of multimedia manipulation has emerged as a critical challenge in combating AI-generated disinformation. While existing methods have made progress in recent years, we identify two fundamental limitations in current approaches: (1) Underestimation of MLLM-driven deception risk: prevailing techniques primarily address rule-based text manipulations, yet fail to account for sophisticated misinformation synthesized by multimodal large language models (MLLMs) that can dynamically generate semantically coherent, contextually plausible yet deceptive narratives conditioned on manipulated images; (2) Unrealistic misalignment artifacts: currently focused scenarios rely on artificially misaligned content that lacks semantic coherence, rendering them easily detectable. To address these gaps holistically, we propose a new adversarial pipeline that leverages MLLMs to generate high-risk disinformation. Our approach begins with constructing the MLLM-Driven Synthetic Multimodal (MDSM) dataset, where images are first altered using state-of-the-art editing techniques and then paired with MLLM-generated deceptive texts that maintain semantic consistency with the visual manipulations. Building upon this foundation, we present the Artifact-aware Manipulation Diagnosis via MLLM (AMD) framework featuring two key innovations: Artifact Pre-perception Encoding strategy and Manipulation-Oriented Reasoning, to tame MLLMs for the MDSM problem. Comprehensive experiments validate our framework's superior generalization capabilities as a unified architecture for detecting MLLM-powered multimodal deceptions. In cross-domain testing on the MDSM dataset, AMD achieves the best average performance, with 88.18 ACC, 60.25 mAP, and 61.02 mIoU scores.

</details>

### 34. Ask or Answer: A Decision Framework for Multi-Turn Health Misinformation Intervention

📄 [arXiv](https://arxiv.org/abs/2608.21721)　📅 2026-08

**关键词**：`defense`、`health misinformation`、`multi-turn correction`、`probe-or-answer`、`risk communication`、`clarification policy`

👤 **作者**：Xiaoying Song、Anirban Saha Anik、Jinyu Liu、Qitao Tan、Geng Yuan、Lingzi Hong

- 🎯 **研究动机**：多轮健康错误信息干预中，立即纠正忽略用户知识/信念差异，无差别追问又徒增交互负担，何时值得提问缺乏决策框架
- 🔬 **研究方法**：RO-PnR 逐轮在追问与给出最终纠正之间选择，由权衡追问预期增益与交互成本的 turn-level reward 引导，并以健康素养与信念承诺的潜在状态建模用户异质性
- 📌 **结论**：三个健康错误信息数据集与三个基座模型上取得最高成本调整效用，比 always-probe 基线少用 30% 轮次

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Correcting health misinformation in dialogue requires more than producing a factual rebuttal: users differ in what they know, what they believe, and what they need to hear, so an effective intervention often depends on first asking the right clarifying question. Yet existing methods either respond immediately or probe indiscriminately, treating clarification as either unnecessary or always beneficial. We propose Reward-Optimized Probe-and-Respond (RO-PnR), a framework that learns when asking is worth its cost. At each turn, RO-PnR chooses between probing for more information and committing to a final correction, guided by a turn-level reward that weighs the expected gain from probing against its interaction cost. To capture how user heterogeneity affects probing value, we model each simulated user with a latent state along health literacy and belief commitment. Experiments show that RO-PnR achieves the highest cost-adjusted utility across three health-misinformation datasets and three base models, using 30% fewer turns than always-probe baselines.

</details>

### 35. Mask-to-Correct^+: Leveraging Retriever Diversity for Masking-guided Faithful Fact Correction

🎓 [Official](https://aclanthology.org/2026.acl-long.175/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`misinformation`、`fact checking`、`source attribution`、`RAG security`、`fact-checking`

👤 **作者**：Payel Santra、Lavisha Sharma、Madhusudan Ghosh、Partha Basuchowdhuri

- 🎯 **研究动机**：有监督事实纠错依赖稀缺有偏的 claim-evidence 标注、泛化差且忽视语义忠实
- 🔬 **研究方法**：M2C 免训练推理期 RAG 框架用多样性感知掩码定位错误 span 并以检索证据评估忠实度；M2C+ 集成多 ranker 减少检索偏差
- 📌 **结论**：基准数据集上 SARI 提升最多 14%，无需金标证据

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The rapid spread of misinformation on social media highlights the need for robust, automated fact correction frameworks. However, existing works rely on supervised learning from manually annotated claim-evidence pairs, which are scarce and prone to biases, limiting their generalization across domains. Moreover, these methods overlook semantic faithfulness in their correction process. To address these challenges, we propose Mask-to-Correct (M 2 C), a training-free, inference-only Retrieval Augmented Generation (RAG) based framework that leverages diversity-aware masking to identify erroneous spans of claims and evaluate the faithfulness of corrections using retrieved evidence. However, the effectiveness of RAG heavily depends on the choice of retriever, which may vary across queries. To mitigate this, we further introduce M 2 C +, an ensemble-based framework that combines corrections across multiple rankers to reduce retrieval bias and improve robustness. Extensive experiments on the benchmark datasets demonstrate that our proposed frameworks consistently outperform all baselines, achieving up to 14% improvement in SARI scores, without using gold evidence.

</details>

### 36. Do Images Speak Louder than Words? Investigating the Effect of Textual Misinformation in VLMs

🎓 [Official](https://aclanthology.org/2026.eacl-long.323/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`VLM misinformation`、`cross-modal conflict`、`persuasive prompt`

👤 **作者**：Chi Zhang、Wenxuan Ding、Jiale Liu、Mingrui Wu、Qingyun Wu、Ray Mooney

- 🎯 **研究动机**：VLM 如何仲裁跨模态矛盾信息不明，文本域误信息研究结论无法直接迁移
- 🔬 **研究方法**：构建 ConText-VQA：图文对加系统性生成的与视觉证据冲突的说服性提示，测试 11 个 SOTA VLM
- 📌 **结论**：模型常推翻清晰视觉证据倒向冲突文本，仅一轮说服对话平均性能下降超 48.2%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Vision-Language Models (VLMs) have shown strong multimodal reasoning capability on Visual-Question-Answering (VQA) benchmarks. However, their robustness against textual misinformation remains under-explored. While existing research has extensively studied the effect of misinformation in text-only domains, it is not clear how VLMs arbitrate between contradictory information from different modalities. To bridge the gap, we first propose the ConText-VQA (i.e. Conflicting Text) dataset, consisting of image-question pairs together with systematically generated persuasive prompts that deliberately conflict with visual evidence. Then, a thorough testing framework is designed and executed to benchmark the susceptibility of various models to these conflicting textual inputs. Comprehensive experiments over 11 state-of-the-art VLMs reveal that these models are indeed vulnerable to misleading prompts, often overriding clear visual evidence in favor of the conflicting text, and show an average performance drop of over 48.2% after only one round of persuasive conversation. Our findings highlight a critical limitation in current VLMs and underscore the need for improved robustness against textual manipulation.

</details>

### 37. What’s Left Unsaid? Detecting and Correcting Misleading Omissions in Multimodal News Previews

🎓 [Official](https://aclanthology.org/2026.acl-long.293/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`multimodal safety`、`VLM safety`、`multimodal jailbreak`、`misinformation detection`、`misinformation`

👤 **作者**：Fanxiao Li、…、Min-Yen Kan

- 🎯 **研究动机**：新闻预览（图-标题对）即使事实正确也可选择性省略关键上下文诱导解释偏移，比显式误信息更隐蔽且少有研究
- 🔬 **研究方法**：多阶段管道模拟预览与上下文理解构建 MM-Misleading 基准；提出 OMGuard：解释感知微调检测误导性，理由引导的标题改写降低误导印象
- 📌 **结论**：把 8B 模型检测准确率提升至 235B LVLM 水平；误导多源于局部叙事缺失而非全局框架改变，图像驱动案例需视觉干预

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Even when factually correct, social-media news previews (image-headline pairs) can induce interpretation drift: by selectively omitting crucial context, they lead readers to form judgments that diverge from what the full article supports. This covert harm is subtler than explicit misinformation, yet remains underexplored. To address this gap, we develop a multi-stage pipeline that simulates preview-based and context-based understanding, enabling construction of the MM-Misleading benchmark. Using MM-Misleading, we systematically evaluate open-source LVLMs and uncover pronounced blind spots in omission-based misleadingness detection. We further propose OMGuard, which combines (1) Interpretation-Aware Fine-Tuning for misleadingness detection and (2) Rationale-Guided Misleading Content Correction, where explicit rationales guide headline rewriting to reduce misleading impressions. Experiments show that OMGuard lifts an 8B model’s detection accuracy to the level of a 235B LVLM while delivering markedly stronger end-to-end correction. Further analysis shows that misleadingness usually arises from local narrative shifts, such as missing background, instead of global frame changes, and identifies image-driven cases where text-only correction fails, underscoring the need for visual interventions.

</details>

### 38. Is this chart lying to me? Automating the detection of misleading visualizations

🎓 [Official](https://aclanthology.org/2026.acl-long.398/)　📅 2026　🏷 ACL 2026

**关键词**：`detection`、`multimodal jailbreak`、`visual adversarial input`、`safety bypass`、`misinformation detection`、`deceptive behavior`

👤 **作者**：Jonathan Tonglet、Jan Zimny、Tinne Tuytelaars、Iryna Gurevych

- 🎯 **研究动机**：误导性可视化驱动虚假信息，人类与 MLLM 常被骗，缺大规模开放数据集
- 🔬 **研究方法**：Misviz 含 2,604 个真实可视化、12 类 misleader 标注，配套基于真实数据表用 Matplotlib 合成的 81,814 个 Misviz-synth
- 📌 **结论**：SOTA MLLM、规则系统与微调分类器评测显示该任务仍极具挑战

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Misleading visualizations are a potent driver of misinformation on social media and the web. By violating chart design principles, they distort data and lead readers to draw inaccurate conclusions. Prior work has shown that both humans and multimodal large language models (MLLMs) are frequently deceived by such visualizations. Automatically detecting misleading visualizations and identifying the specific design rules they violate could help protect readers and reduce the spread of misinformation. However, the training and evaluation of AI models has been limited by the absence of large, diverse, and openly available datasets. In this work, we introduce Misviz, a benchmark of 2,604 real-world visualizations annotated with 12 types of misleaders. To support model training, we also release Misviz-synth, a synthetic dataset of 81,814 visualizations generated using Matplotlib and based on real-world data tables. We perform a comprehensive evaluation on both datasets using state-of-the-art MLLMs, rule-based systems, and fine-tuned classifiers. Our results reveal that the task remains highly challenging. We release Misviz, Misviz-synth, and the accompanying code.

</details>

### 39. Protecting multimodal large language models against misleading visualizations

🎓 [Official](https://aclanthology.org/2026.acl-long.377/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`multimodal safety`、`VLM safety`、`multimodal jailbreak`、`misinformation detection`、`misinformation`

👤 **作者**：Jonathan Tonglet、Tinne Tuytelaars、Marie Francine Moens、Iryna Gurevych

- 🎯 **研究动机**：MLLM 在误导性可视化上的问答准确率平均降至随机基线水平
- 🔬 **研究方法**：首个六种推理时方法比较（表格问答、重绘可视化等），在不损正常图表准确率的前提下提升误导图表问答
- 📌 **结论**：表格问答与重绘两种方法有效，提升最多 19.6 个百分点

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Visualizations play a pivotal role in daily communication in an increasingly data-driven world. Research on multimodal large language models (MLLMs) for automated chart understanding has accelerated massively, with steady improvements on standard benchmarks. However, for MLLMs to be reliable, they must be robust to misleading visualizations, i.e., charts that distort the underlying data, leading readers to draw inaccurate conclusions. Here, we uncover an important vulnerability: MLLM question-answering (QA) accuracy on misleading visualizations drops on average to the level of the random baseline. To address this, we provide the first comparison of six inference-time methods to improve QA performance on misleading visualizations, without compromising accuracy on non-misleading ones. We find that two methods, table-based QA and redrawing the visualization, are effective, with improvements of up to 19.6 percentage points. We make our code and data available.

</details>

### 40. RiskChainBench: A Benchmark for Obfuscated Platform Message Restoration and Evidence-Grounded Web Investigation

📄 [arXiv](https://arxiv.org/abs/2609.16900)　📅 2026-09

**关键词**：`benchmark`、`platform abuse`、`obfuscated message`、`web investigation agent`、`evidence grounding`

👤 **作者**：ZhuoXin Liu、…、Peng Chen

- 🎯 **研究动机**：平台滥用活动用 emoji、同音字、拆字、冗余符号隐藏引流指令，再经伪装链接导向色情/诈骗/赌博服务；既有基准把混淆文本与风险网页分开评，掩盖目标恢复如何影响下游证据获取
- 🔬 **研究方法**：RiskChainBench：3,600 条合成 token-文本恢复输入（600 源会话）配 600 个人工标注的本地网页环境；同一模型先恢复消息/操作意图/目的地，再作为 VLM 网页 agent 调查关联网站并输出冻结的引用证据风险报告（不给消息侧语义或域名信誉线索）；恢复与正确路由的调查分别计分，离线以冻结主入口预测做门控组合
- 📌 **结论**：10 个模型 Entry Top-1 从 35.2% 到 95.2%、网页决策准确率 26.3%–62.8%；执行失败占网页运行 31.9% 而决策后类型错误仅 0.9%——稳定探索与风险判断是主要瓶颈；发布基准、协议与可重置本地沙箱

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Platform abuse campaigns conceal redirection instructions with emojis, homophones, character decomposition, and redundant symbols, then route users through disguised links to services associated with pornography, fraud, gambling, or illicit transactions. Existing benchmarks evaluate obfuscated text and risky webpages separately, obscuring how target recovery affects downstream evidence acquisition. We introduce RiskChainBench, pairing 3,600 synthetic token-text restoration inputs from 600 source sessions with 600 corresponding human-labeled local web environments. A model first restores the message, operational intent, and destination; the same underlying model then acts as a VLM-driven web agent that investigates the correctly associated website and produces a frozen, evidence-cited risk report without message-side semantics or domain-reputation cues. We score restoration and correct-routing web investigation separately and compose them offline by applying the frozen primary-entry prediction as a gate to the same Task 2 result. Human labels determine task correctness, while a fixed multimodal evidence judge assesses faithfulness, sufficiency, completeness, and consistency. Across ten models, Entry Top-1 ranges from 35.2% to 95.2% and web decision accuracy from 26.3% to 62.8%; the leading systems differ across entry recovery, full reconstruction, website decisions, and fine-grained typing. Execution failures account for 31.9% of web runs, whereas post-decision type errors account for only 0.9%, identifying stable exploration and risk judgment as the principal bottlenecks. We release the benchmark, protocol, and resettable local sandbox.

</details>
