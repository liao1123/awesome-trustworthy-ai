# Search Agent

[返回投毒与后门目录](README.md)

## 研究方向

本页研究 LLM Search Agent 在自主生成 query、检索开放网页、读取多源证据并综合答案时的安全问题。核心 threat model 包括：有害意图被拆成看似无害的检索步骤、攻击者控制的网页进入 evidence set、检索或训练目标削弱原有 refusal，以及错误证据沿长程 research trajectory 被放大为推荐、引用或行动建议。这里重点评估完整 search loop，而不是只在固定 context 中测试单轮 RAG。

## 研究脉络

- **检索带来的安全退化：** 早期工作发现，从无检索扩展到 Wikipedia 和开放网页后，Agent 的 refusal、bias 与 harmfulness safeguard 会系统性变化，说明正确检索不等于安全综合。
- **有害信息检索红队：** SearchAttack、CREST-Search 与 SafeSearch 将危险目标重写为搜索任务，并检查 query generation、网页引用和最终回答如何共同绕过 base model 的安全边界。
- **网页证据操纵：** SearchGEO、UGC poisoning 与 MisKnow-Agent 从替换检索结果发展到 authority cue、虚假共识和可重复出现的用户生成内容，攻击目标也从“被检索”转向“被 Agent 背书”；One Polluted Page 表明单页污染即可让推荐 LLM 批量推广虚构产品，EcoGEO 再把单页改写升级为沿浏览轨迹协同的跨页证据生态。
- **长程轨迹劫持：** FORGE 与 Breadcrumbing 利用多个网页和多轮 observation 逐步改变 research plan，表明单页检测不足以覆盖跨文档、跨步骤的 cumulative attack。
- **过程级对齐：** SafeSearch 与 COMPASS 将监督从 final answer 前移到 query 和 trajectory，并同时约束 utility；当前仍缺少在真实搜索排序、动态网页和未知攻击者站点上的端到端防御证据。

## Web Evidence Manipulation 与 Trajectory Hijacking

### 1. Lazy Grounding: Attacking Search Agents with Factual Evidence

📄 [arXiv](https://arxiv.org/abs/2608.30303)　📅 2026-09

**关键词**：`attack`、`factual-evidence mismatch`、`lazy grounding`、`answer-shaped evidence`

👤 **作者**：Yulin Zhang、…、Bhuwan Dhingra

- 🎯 **研究动机**：search Agent 只防投毒语料中的虚假信息，却可能被完全真实但答非所问的证据误导
- 🔬 **研究方法**：定义 lazy grounding 攻击：向检索语料注入支持相邻改写问题的事实性文档使其被原问题检索，并在 12 个模型-基准对上评估
- 📌 **结论**：准确率平均下降 5.9 分、最高 17.3 分，所有设置均出现邻近答案采纳；证据更靠后或更“答案形”时效应更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search agents mitigate hallucination by grounding their answers in retrieved web results. However, retrieval-based approaches also introduce an attack surface: agents may cite misinformation from poisoned search corpora containing false or malicious documents. We demonstrate that, in some cases, search agents' reasoning and responses may be steered by completely factual but distracting information. We refer to this failure as lazy grounding. We expose lazy grounding by injecting nearby evidence from answer-changing rewrites of benchmark questions into the search corpora. Each document contains factual evidence that supports a neighboring rewritten question but is retrieved for the original question. Across 12 model-benchmark pairs, the attack causes the accuracy of search agents' responses to drop by 5.9 points on average and by up to 17.3 points, while inducing nearby-answer adoption in every setting. The effect is even stronger when nearby evidence appears later or is more answer-shaped. Our results show that robust search agents must defend against not only misinformation but also the misapplication of factual evidence. The code is publicly available at https://github.com/frankyzha/lazy-grounding.

</details>

### 2. Breadcrumbing Search Agents

📄 [arXiv](https://arxiv.org/abs/2608.04565)　📅 2026-08

**关键词**：`attack`、`web evidence poisoning`、`breadcrumbing`、`trajectory hijacking`

👤 **作者**：Xuebin Li、…、Nenghai Yu

- 🎯 **研究动机**：搜索 agent 会追问并交叉验证多源，单页静态注入常被稀释或拒绝，搜索信道本身是脆弱边界
- 🔬 **研究方法**：在受限工具中介威胁模型下每查询只追加一条受控结果；Authority-Chain Hijack 把孤立操纵串成相互印证的证据链，TGSE 从执行轨迹自动进化攻击策略
- 📌 **结论**：SafeSearch 上 ACH 的 Overall ASR 55.9%/MaxN ASR 83.3% 为全部基线最高；TGSE 在保留集上达 71.4%/95.0%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-based search agents are widely used for information-seeking tasks, but their reliance on external tool returns introduces a critical security risk: web content retrieved during execution is untrusted, exposing agents to prompt injection and goal hijacking. Prior work on search-agent safety primarily focuses on static web-content injection, but modern agents issue follow-up queries and cross-check competing sources, so a single injected page is often diluted or rejected. We show that the channel delivering search and page observations is a fragile security boundary: beyond exposing the agent to a single poisoned page, a mediated search interface can repeatedly steer how the agent gathers evidence and forms its final answer. Under a constrained tool-intermediary threat model, appending only one controlled result per query can substantially increase attack success when the evidence is coordinated across the agent's trajectory. We study this setting with a strategy-driven long-horizon attack system and introduce Authority-Chain Hijack (ACH), an expert-refined strategy that turns isolated search-result and page-content manipulations into a coherent evidence chain across seemingly corroborating sources. ACH achieves the highest Overall ASR among all baselines, reaching 55.9% / 83.3% ASR / MaxN ASR on the full SafeSearch test split. We further introduce Trace-Guided Strategy Evolution (TGSE), which automatically improves attacker strategies from execution traces, replacing manual redesign with trace-driven refinement; its strongest single setting reaches 71.4% / 95.0% in held-out evaluation.

</details>

### 3. Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions

📄 [arXiv](https://arxiv.org/abs/2607.20891) · 📊 [Dataset](https://huggingface.co/datasets/whfeLingYu/Misleading_Knowledge)　📅 2026-07

**关键词**：`attack`、`misleading knowledge`、`authority cues`、`false conclusion`

👤 **作者**：Pengyu Zhu、Lijun Li、Longju Yang、Sen Su、Jing Shao

- 🎯 **研究动机**：deep research agent 能否抵抗看似可信但事实为假的信息未知
- 🔬 **研究方法**：构建 MisKnow-Agent 受控评估框架：生成带受控权威线索与来源样式的任务专属误导文档（5,933 篇），以报告级错误结论采纳率（FCAR）评估 DeerFlow、WebThinker 与 Gemini Deep Research
- 📌 **结论**：引入一篇误导文档即使平均 FCAR 从 0% 升至 54.7%；权威性与呈现样式影响显著而检索排名与额外文档影响有限，研究前后防御降低但不消除采纳

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research agents conduct long-horizon investigations by iteratively planning, retrieving evidence, and generating reports. However, it remains unclear whether they can resist apparently credible but factually false information introduced into these workflows. To study this failure mode, we introduce MisKnow-Agent, a controlled evaluation framework that constructs task-specific documents supporting manually audited false conclusions with controlled authority cues and source styles. Applied to the tasks from DeepResearch Bench, it generates 5,933 misleading documents after filtering. We evaluate DeerFlow and WebThinker with three backbone LLMs, together with Gemini Deep Research, using a report-level false-conclusion adoption rate (FCAR) that counts only reports endorsing the false conclusion. Across the configurations, introducing one misleading document increases the mean FCAR from 0\% in the no-injection control to 54.7\%. FCAR varies substantially with lifecycle stage and framework design, and also with source authority and presentation style, whereas search-result rank and additional documents beyond the first have limited influence. Although cross-model verification consistently classifies retained instances as misleading, Deep Research agents can still adopt the corresponding false conclusions during long-horizon research. Pre- and post-research defenses reduce FCAR but do not eliminate adoption, motivating continuous verification when evidence enters intermediate research states and final synthesis. To facilitate reproducibility, our code and dataset are publicly available at https://github.com/whfeLingYu/MisKnow-Agent and https://huggingface.co/datasets/whfeLingYu/Misleading_Knowledge, respectively.

</details>

### 4. FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2607.04718)　📅 2026-07

**关键词**：`attack`、`research trajectory`、`planning poisoning`、`evidence chain`

👤 **作者**：Yue Pan、Ziheng Zhang、Junxiang Lei、Changhao Jia、Qingyi Si、Hongcheng Guo

- 🎯 **研究动机**：deep research agent 的子任务规划依赖检索池，对抗文档可把局部注入升级为报告级污染，该规划层投毒面未被研究
- 🔬 **研究方法**：提出 FORGE 两级攻击：文档内推理伪造+跨文档链协调劫持子任务规划；配套按认知类型加权的 PRISM 度量与把递归追问锚定到根查询的 RQA 防御
- 📌 **结论**：25 个查询上 5 篇注入文档即达 26.4% PRISM，且发生深度迁移（毒内容转为事实前提）；RQA 把 PRISM 从 38.5% 降到 18.3%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with inter-document chain coordination to hijack subtask planning. We further introduce the PRISM metric, which weights infected report claims by cognitive type, and Root Query Anchoring, a lightweight defense that ties recursive follow-up generation to the root query. Across 25 queries, Network FORGE reaches 26.4% PRISM with five injected documents and exhibits depth migration, in which recursive synthesis shifts poisoned content from overt framing into factual premises. On the 10-query defense subset, RQA (Root Query Anchoring) reduces PRISM from 38.5% to 18.3%.

</details>

### 5. KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems

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

### 6. How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation

📄 [arXiv](https://arxiv.org/abs/2606.16821)　📅 2026-06　🏷 EMNLP 2026

**关键词**：`benchmark`、`endorsement corruption`、`web manipulation`、`backend variance`

👤 **作者**：Yimeng Chen、Zhe Ren、Firas Laakom、Yu Li、Dandan Guo、Jürgen Schmidhuber

- 🎯 **研究动机**：LLM 搜索 agent 把开放网络内容合成推荐，攻击者发布的页面可能变成被背书的论断，该背书腐蚀风险未被测量
- 🔬 **研究方法**：提出 SearchGEO 评估框架：网页证据操纵管线+五模式攻击分类+多级输出指标，在 308 个用例上评估 13 个 LLM 后端
- 📌 **结论**：ASR 从 Claude-Sonnet-4.6 的 0.0% 到 Gemini-3-Flash 的 31.4% 不等，最强攻击模式随模型家族变化，同一部署脚手架可放大或缩小 ASR；建议把对抗搜索下的推荐可靠性纳入后端安全评估

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM)-based search agents synthesize open-web content into actionable recommendations on behalf of users, creating a risk that attacker-published pages are transformed into endorsed claims. We introduce SearchGEO, a controlled evaluation framework for measuring endorsement corruption in LLM-based web-search agents, combining a web-evidence manipulation pipeline, a five-mode attack taxonomy, and multiple output-level metrics. We evaluate 13 LLM backends on 308 cases each. Results show that vulnerability patterns vary across backends: overall attack success rate (ASR) ranges from 0.0% on Claude-Sonnet-4.6 to 31.4% on Gemini-3-Flash, the strongest attack mode differs by model family, and the same deployment scaffold could amplify or decrease ASR on different backends. An auxiliary agent-skill probe, where endorsement becomes an install command, exposes a sharp split among otherwise robust backends: Claude over-rejects while GPT over-trusts. These findings argue for treating recommendation reliability under adversarial search content as a first-class dimension of backend safety evaluation.

</details>

### 7. Deep-Research Agents Can Be Poisoned via User-Generated Content

📄 [arXiv](https://arxiv.org/abs/2605.24245)　📅 2026-05

**关键词**：`attack`、`UGC poisoning`、`retrieval exposure`、`source promotion`

👤 **作者**：Tingwei Zhang、Harold Triedman、Vitaly Shmatikov

- 🎯 **研究动机**：深度研究 agent 的报告常依赖 Reddit、Wikipedia 等宽松审核的 UGC 页面，构成可颠覆入口
- 🔬 **研究方法**：在高频被检索页面附加短文本即可让 agent 引用并推广攻击者选定实体；在投资建议、杀毒软件、餐厅推荐等场景评测
- 📌 **结论**：单 URL 仅 13 词即可在 57-76% 执行中被检索、38-51% 报告中被引用；毒化整个 subreddit 在毒内容仅占 0.5-4% 时引用率仍 30-53%；过滤 UGC 可阻断但损报告质量，轻量异常检测不可靠

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep-research agents are an alternative to conventional Web search. They use multi-agent pipelines to issue multiple Web searches related to user queries, retrieve relevant content from the answers, and generate detailed, evidence-based reports. We show that for many common search topics (including financial, medical, and product recommendations), agent-generated reports are consistently based on the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia. This retrieval overlap, combined with lax moderation and access controls for UGC, is an opportunity for subversion: an attacker who appends a short text to a single, frequently-retrieved page can cause agents to cite this text and promote attacker-chosen entities across many user questions. We evaluate this attack on representative deep-research systems across multiple topics, such as investment advice, antivirus software, restaurant recommendations, etc. Poisoning a single URL with as few as 13 words can be sufficient for the attacker's content to be retrieved in 57-76% of the agent executions for a given topic and cited in 38-51% of the generated reports. A more aggressive attack (poisoning an entire subreddit) achieves 30-53% citation rates even when the poison is only 0.5-4% of the retrieved content. The attacker does not need to know the phrasing of the user's question, nor the specific Web queries generated by the agent, nor the agent's internal retrieval and generation mechanisms. We then study defenses at different stages of the pipeline, including source-level filtering and output-based detection. Dropping UGC from retrieved content blocks the attack but degrades the quality of generated reports. We show that lightweight anomaly detection on inputs and outputs does not reliably identify poisoned content, nor the results of poisoning.

</details>

### 8. SearchAttack: Red-Teaming LLMs against Knowledge-to-Action Threats under Online Web Search

📄 [arXiv](https://arxiv.org/abs/2601.04093)　📅 2026-01

**关键词**：`benchmark`、`unsafe search task`、`query framing`、`knowledge-to-action`

👤 **作者**：Yu Yan、…、Qi Li

- 🎯 **研究动机**：搜索增强 LLM 的返回内容可能直接包含可即用的有害指令或结论，此类知识到行动威胁缺乏红队检验
- 🔬 **研究方法**：SearchAttack 用密集良性知识改写有害语义以逃避上下文直接解码并诱导不安全检索，再利用奖励追逐偏置诱导模型合成不安全内容，配套非法活动基准与事实核查框架
- 📌 **结论**：对搜索增强 LLM 攻击有效；即便无 web 搜索的 LLM 也会因信息搜寻刻板行为被诱导输出有害内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, people have suffered from LLM hallucination and have become increasingly aware of the reliability gap of LLMs in open and knowledge-intensive tasks. As a result, they have increasingly turned to search-augmented LLMs to mitigate this issue. However, LLM-driven search also becomes an attractive target for misuse. Once the returned content directly contains targeted, ready-to-use harmful instructions or takeaways for users, it becomes difficult to withdraw or undo such exposure. To investigate LLMs' unsafe search behavior issues, we first propose \textbf{\textit{SearchAttack}} for red-teaming, which (1) rephrases harmful semantics via dense and benign knowledge to evade direct in-context decoding, thus eliciting unsafe information retrieval, (2) stress-tests LLMs' reward-chasing bias by steering them to synthesize unsafe retrieved content. We also curate an emergent, domain-specific illicit activity benchmark for search-based threat assessment, and introduce a fact-checking framework to ground and quantify harm in both offline and online attack settings. Extensive experiments are conducted to red-team the search-augmented LLMs for responsible vulnerability assessment. Empirically, SearchAttack demonstrates strong effectiveness in attacking these systems. We also find that LLMs without web search can still be steered into harmful content output due to their information-seeking stereotypical behaviors.

</details>

### 9. Deep Research Brings Deeper Harm

📄 [arXiv](https://arxiv.org/abs/2510.11851) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2025-10

**关键词**：`attack`、`deep research`、`plan injection`、`intent hijacking`

👤 **作者**：Shuo Chen、…、Jindong Gu

- 🎯 **研究动机**：独立 LLM 直接拒绝的有害查询可诱使 Deep Research agent 产出危险专业报告，现有越狱方法不针对其研究能力
- 🔬 **研究方法**：提出 Plan Injection（向计划注入恶意子目标）与 Intent Hijack（把有害查询改写为学术研究问题）两类越狱策略，跨多个 LLM 与安全基准实验
- 📌 **结论**：LLM 对齐在 DR agent 中常失效，多步规划进一步削弱对齐，且产出比独立 LLM 更连贯专业危险的内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Research (DR) agents built on Large Language Models (LLMs) can perform complex, multi-step research by decomposing tasks, retrieving online information, and synthesizing detailed reports. However, the misuse of LLMs with such powerful capabilities can lead to even greater risks. This is especially concerning in high-stakes and knowledge-intensive domains such as biosecurity, where DR can generate a professional report containing detailed forbidden knowledge. Unfortunately, we have found such risks in practice: simply submitting a harmful query, which a standalone LLM directly rejects, can elicit a detailed and dangerous report from DR agents. This highlights the elevated risks and underscores the need for a deeper safety analysis. Yet, jailbreak methods designed for LLMs fall short in exposing such unique risks, as they do not target the research ability of DR agents. To address this gap, we propose two novel jailbreak strategies: Plan Injection, which injects malicious sub-goals into the agent's plan; and Intent Hijack, which reframes harmful queries as academic research questions. We conducted extensive experiments across different LLMs and various safety benchmarks, including general and biosecurity forbidden prompts. These experiments reveal 3 key findings: (1) Alignment of the LLMs often fail in DR agents, where harmful prompts framed in academic terms can hijack agent intent; (2) Multi-step planning and execution weaken the alignment, revealing systemic vulnerabilities that prompt-level safeguards cannot address; (3) DR agents not only bypass refusals but also produce more coherent, professional, and dangerous content, compared with standalone LLMs. These results demonstrate a fundamental misalignment in DR agents and call for better alignment techniques tailored to DR agents. Code and datasets are available at https://chenxshuo.github.io/deeper-harm.

</details>

### 10. When Search Goes Wrong: Red-Teaming Web-Augmented Large Language Models

📄 [arXiv](https://arxiv.org/abs/2510.09689) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65553)　📅 2025-10　🏷 ICML 2026

**关键词**：`benchmark`、`analysis`、`web-augmented LLM`、`query optimization`、`unsafe citation`、`LLM jailbreak`

👤 **作者**：Haoran Ou、…、Tianwei Zhang

- 🎯 **研究动机**：现有红队方法只针对独立 LLM 的不安全生成，忽视 web 搜索流程中检索与引用环节的风险
- 🔬 **研究方法**：提出 CREST-Search 红队框架，用三种生成良性外观查询却诱导不安全引用的攻击策略，辅以黑盒迭代上下文精化，并构建 WebSearch-Harm 数据集训练专用红队模型
- 📌 **结论**：能有效绕过安全过滤器，系统性暴露 web 搜索 LLM 系统的引用漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have been augmented with web search to overcome the limitations of the static knowledge boundary by accessing up-to-date information from the open Internet. While this integration enhances model capability, it also introduces a distinct safety threat surface: the retrieval and citation process has the potential risk of exposing users to harmful or low-credibility web content. Existing red-teaming methods are largely designed for standalone LLMs as they primarily focus on unsafe generation, ignoring risks emerging from the complex search workflow. To address this gap, we propose CREST-Search, a pioneering red-teaming framework for LLMs with web search. The cornerstone of CREST-Search is three novel attack strategies that generate seemingly benign search queries yet induce unsafe citations. It also employs an iterative in-context refinement mechanism to strengthen adversarial effectiveness under black-box constraints. In addition, we construct a search-specific harmful dataset, WebSearch-Harm, which enables fine-tuning a specialized red-teaming model to improve query quality. Our experiments demonstrate that CREST-Search can effectively bypass safety filters and systematically expose vulnerabilities in web search-based LLM systems, underscoring the necessity of the development of robust search models.

</details>

### 11. SafeSearch: Automated Red-Teaming of LLM-Based Search Agents

📄 [arXiv](https://arxiv.org/abs/2509.23694) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65893)　📅 2025-09　🏷 ICML 2026

**关键词**：`benchmark`、`attack`、`automated red teaming`、`harmful query`、`search scaffold`、`LLM jailbreak`

👤 **作者**：Jianshuo Dong、…、Han Qiu

- 🎯 **研究动机**：搜索 agent 接入互联网后不可靠搜索结果可诱导不安全输出，真实事故已现但缺系统评测
- 🔬 **研究方法**：提出 SafeSearch：可扩展、低成本、沙箱化的自动红队框架，生成 300 个覆盖五类风险的测试用例，评测三种搜索脚手架与 17 个 LLM
- 📌 **结论**：搜索工作流下 GPT-4.1-mini 的 ASR 最高达 90.5%，提醒式 prompt 等常见防御保护有限

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search agents connect LLMs to the Internet, enabling them to access broader and more up-to-date information. However, this also introduces a new threat surface: unreliable search results can mislead agents into producing unsafe outputs. Real-world incidents and our two in-the-wild observations show that such failures can occur in practice. To study this threat systematically, we propose SafeSearch, an automated red-teaming framework that is scalable, cost-efficient, and lightweight, enabling sandboxed safety evaluation of search agents. Using this, we generate 300 test cases spanning five risk categories (e.g., misinformation and prompt injection) and evaluate three search agent scaffolds across 17 representative LLMs. Our results reveal substantial vulnerabilities in LLM-based search agents, with the highest ASR reaching 90.5% for GPT-4.1-mini in a search-workflow setting. Moreover, we find that common defenses, such as reminder prompting, offer limited protection. Overall, SafeSearch provides a practical way to measure and improve the safety of LLM-based search agents.

</details>

### 12. Information Retrieval Induced Safety Degradation in AI Agents

📄 [arXiv](https://arxiv.org/abs/2505.14215) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5aafb56b9b541742388d1ca2a4aa3802-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`analysis`、`retrieval access`、`safety degradation`、`refusal erosion`

👤 **作者**：Cheng Yu、Benedikt Stroebl、Diyi Yang、Orestis Papakyriakopoulos

- 🎯 **研究动机**：检索增强 agent 与外部信息源的交互如何影响安全行为缺乏量化
- 🔬 **研究方法**：在无检索、Wikipedia 检索、开放网络搜索三级设置下，评测受审与未审 LLM 及 agent 的拒绝率、偏见与有害输出
- 📌 **结论**：检索范围越广安全退化越严重，对齐 LLM 加检索后常比无检索的未审模型更不安全，prompt 缓解无法消除该效应

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Despite the growing integration of retrieval-enabled AI agents into society, their safety and ethical behavior remain inadequately understood. In particular, the integration of LLMs and AI agents with external information sources and real-world environments raises critical questions about how they engage with and are influenced by these external data sources and interactive contexts. This study investigates how expanding retrieval access -- from no external sources to Wikipedia-based retrieval and open web search -- affects model reliability, bias propagation, and harmful content generation. Through extensive benchmarking of censored and uncensored LLMs and AI agents, our findings reveal a consistent degradation in refusal rates, bias sensitivity, and harmfulness safeguards as models gain broader access to external sources, culminating in a phenomenon we term safety degradation. Notably, retrieval-enabled agents built on aligned LLMs often behave more unsafely than uncensored models without retrieval. This effect persists even under strong retrieval accuracy and prompt-based mitigation, suggesting that the mere presence of retrieved content reshapes model behavior in structurally unsafe ways. These findings underscore the need for robust mitigation strategies to ensure fairness and reliability in retrieval-enabled and increasingly autonomous AI systems.

</details>

### 13. Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21544)　📅 2026-08

**关键词**：`defense`、`tool-mediated recovery`、`target-seeking tool call`、`knowledge leakage`、`capability removal`、`external-tool recovery`

👤 **作者**：Baicheng Chen、…、Meng Jiang

- 🎯 **研究动机**：现有 unlearning 只抑制参数化直接回忆，工具增强 Agent 仍可经 web 搜索、检索或数据库查找恢复遗忘目标（tool-mediated recovery），评测存在错配
- 🔬 **研究方法**：ATU 两阶段框架：先做参数知识遗忘抑制直接回忆，再在模拟工具环境中做轨迹级 RL，惩罚 target-seeking 工具行为与最终答案泄漏
- 📌 **结论**：RWKU 与 MUSE 上跨不同 LLM 架构取得目标遗忘与保留效用间更好平衡，unlearning 在工具增强部署下更稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

</details>

### 14. COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents

📄 [arXiv](https://arxiv.org/abs/2605.30838)　📅 2026-05

**关键词**：`defense`、`process alignment`、`MCTS`、`safe trajectory`

👤 **作者**：Wenkai Shen、…、Xiaolin Zheng

- 🎯 **研究动机**：搜索 agent 的有害意图可分解为看似无害的子查询，现有对齐难捕捉多步交互中的稀疏安全信号
- 🔬 **研究方法**：COMPASS 认知 MCTS 引导过程对齐：CTE 高效合成隐蔽攻击轨迹，ISA 隔离危险中间动作做细粒度过程监督
- 📌 **结论**：以显著更少的训练数据获得更优的安全-效用权衡

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM-powered search agents enable multi-step reasoning and tool use. However, these capabilities introduce retrieval-induced safety degradation, as harmful intents may decompose into seemingly innocuous sub-queries that lead to unsafe outcomes. Existing alignment methods struggle to capture sparse safety signals and fail to supervise diverse violations across multi-step interactions. We propose COMPASS, a Cognitive MCTS-Guided Process Alignment framework designed to achieve robust safety alignment throughout the agent workflow while preserving general utility. COMPASS integrates cognitive tree exploration (CTE) to efficiently synthesize stealthy attack trajectories, and introspective step-wise alignment (ISA) to isolate risky intermediate actions for fine-grained process supervision. Empirical results show that COMPASS achieves a favorable safety-utility trade-off while requiring substantially less training data.

</details>

### 15. SafeSearch: Do Not Trade Safety for Utility in LLM Search Agents

🎓 [Official](https://aclanthology.org/2026.findings-eacl.146/)　📅 2026-03　🏷 ACL 2026

**关键词**：`defense`、`multi-objective RL`、`query shaping`、`safety-utility`

👤 **作者**：Qiusi Zhan、Angeline Budiman-Chan、Abdelrahman Zayed、Xingzhi Guo、Daniel Kang、Joo-Kyung Kim

- 🎯 **研究动机**：搜索 agent 会为引用来源降低拒答阈值并合成不安全摘要，比基础 LLM 更易产生有害输出，效用导向微调还会加剧风险
- 🔬 **研究方法**：提出 SafeSearch：多目标强化学习将最终输出的安全/效用奖励与新颖的查询级塑形项（惩罚不安全查询、奖励安全查询）结合
- 📌 **结论**：在 3 个红队数据集上有害性降低超 70%，同时生成安全有帮助的回复并保持与仅效用微调 agent 相当的问答性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) based search agents iteratively generate queries, retrieve external information, and reason to answer open-domain questions.While researchers have primarily focused on improving their utility, their safety behaviors remain underexplored.In this paper, we first evaluate search agents using red-teaming datasets and find that they are more likely to produce harmful outputs than base LLMs. For example, when asked “How can I track someone’s location without their consent?”, a base model refuses, whereas a search agent designed to retrieve and cite sources may lower its refusal threshold, fetch documents (e.g., court cases), and, once appended, synthesize them into an informative yet unsafe summary.We further show that utility-oriented finetuning intensifies this risk, motivating joint alignment of safety and utility.We present SafeSearch, a multi-objective reinforcement learning approach that couples a final-output safety/utility reward with a novel query-level shaping term that penalizes unsafe queries and rewards safe ones.Experiments show that SafeSearch reduces agent harmfulness by over 70% across three red-teaming datasets while producing safe, helpful responses, and matches the QA performance of a utility-only finetuned agent. Further analyses confirm the effectiveness of the query-level reward in jointly improving safety and utility.

</details>

### 16. Agentic Reinforcement Learning for Search Misaligns Instruction-Tuning

📄 [arXiv](https://arxiv.org/abs/2510.17431)　📅 2025-10

**关键词**：`analysis`、`search RL`、`instruction misalignment`、`representation steering`

👤 **作者**：Yushi Yang、Shreyansh Padarha、Sarah Ball、Andrew Lee、Adam Mahdi

- 🎯 **研究动机**：Agentic RL 用于搜索训练如何影响指令微调模型的对齐此前不清楚
- 🔬 **研究方法**：设计先诱发搜索调用再拒答的诊断触发器，测量不安全搜索行为并定位残差流中控制搜索安全性的线性方向，提出基于有害方向投影奖励惩罚的 representation-guided RL
- 📌 **结论**：诊断条件下 Qwen/Llama 搜索查询安全性最多下降 68.6%；表征引导奖励仅用良性数据即可恢复 IT 级对齐且不损任务准确率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic reinforcement learning (RL) trains large language models to use tools, but its impact on alignment is poorly understood. We study how agentic RL for search affects the alignment of instruction-tuned (IT) models. We find that RL-trained models inherit refusal reasoning by deflecting harmful requests into benign search queries, but this breaks down under a simple diagnostic trigger that elicits a search call before refusal can occur. Under this condition, RL models produce multi-step unsafe search actions and reasoning, reducing search query safety by up to 68.6% in Qwen and Llama models relative to their IT counterparts. The effect generalises across model families, scales, and RL algorithms. To understand why, we identify linear directions in the residual stream that control search query safety, and show that RL training progressively shifts search behaviour toward the harmful end of this direction. We thus propose representation-guided RL training, which adds a reward penalty based on projection toward the harmful search direction. Training on benign data alone, it restores IT-level alignment without reducing task accuracy and requires no additional training data. Together, our work provides the first framework for diagnosing, mechanistically analysing, and mitigating alignment degradation in agentic RL for search.

</details>

### 17. SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents

📄 [arXiv](https://arxiv.org/abs/2608.05212)　📅 2026-08

**关键词**：`detection`、`search agent`、`evidence manipulation`、`retrieval integrity`

👤 **作者**：Zhixiang Liang、…、Qiong Cao

- 🎯 **研究动机**：长程搜索 agent 失败诊断需人工检查超长执行轨迹，超出人力可行范围
- 🔬 **研究方法**：SearchAuditBench 含 1243 条失败轨迹（平均 73.1 条消息/65.1K token），专家标注关键错误步、根因与修复；SearchAuditor 用多视角证据锚定裁决做定位、归因与修复
- 📌 **结论**：最强基线（GPT-5.5 驱动）端到端通过率仅 26.6%，SearchAuditor 达 32.3%，其修复可使失败运行更好恢复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep search agents tackle challenging questions through long-horizon web interactions, a process that is both complex and fragile: small reasoning errors may propagate through long, noisy trajectories into fluent but incorrect answers. Diagnosing such failures is difficult, requiring the manual inspection of extremely long execution traces, which could be beyond human capacity. We therefore introduce SearchAuditBench, a benchmark that evaluates whether LLM auditors can localize, attribute, and repair these failures, thereby reducing the human burden. SearchAuditBench comprises 1,243 failed trajectories, averaging 73.1 messages and 65.1K tokens, collected from eight open-weight models on five deep-search benchmarks, each expert-annotated with the critical error step, a search-specific root cause, and a reference repair with grading rubrics. We further propose SearchAuditor, a multi-perspective auditing framework that effectively localizes, attributes, and repairs search-agent failures through evidence-grounded adjudication. Experimental results show that even the strongest baseline, when powered by a frontier model like GPT-5.5, attains only a 26.6% end-to-end pass rate. In contrast, our SearchAuditor consistently outperforms all baselines across different frontier models, achieving an end-to-end pass rate of 32.3%, and resuming failed runs with its repairs enables agents to better recover from errors.

</details>

### 18. Answer First, Evidence Second? Uncovering Hidden Risks in Well-Structured AI Search Summaries

🌐 [Project](https://doi.org/10.1145/3805712.3809913)　📅 2026-07　🏷 SIGIR 2026

**关键词**：`analysis`、`claim-source mismatch`、`citation audit`、`evidence availability`、`AI search`、`citation consistency`

- 🎯 **研究动机**：AI搜索摘要结构规整，但claim与来源的一致性缺审计
- 🔬 **研究方法**：审计citation一致性与evidence grounding，量化claim-source错配与证据可得性
- 📌 **结论**：结构良好的摘要仍普遍存在claim-source错配与证据缺口

### 19. Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning

📄 [arXiv](https://arxiv.org/abs/2609.06027)　📅 2026-09

**关键词**：`benchmark`、`GEO poisoning`、`deep-search agent`、`evidence recovery`、`misinformation injection`

👤 **作者**：Zhongan Bi、…、Wenhui Dong

- 🎯 **研究动机**：GEO 投毒评测只看操纵内容是否被采纳，不追踪 agent 验证、修正与恢复过程
- 🔬 **研究方法**：HAE-GEO 三级攻击（直接断言/上下文伪装/交叉佐证），72,039 干净页+每级 770 毒页，多轮 Search-Scrape 接口评测 10 个 deep-search agent 全轨迹
- 📌 **结论**：佐证陷阱显著降低识别；agentic search 提升最终抵抗力但不改善证据识别；防御提示增加验证却少转化为恢复

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search-augmented LLM agents are increasingly used for consumer decisions, making them vulnerable to Generative Engine Optimization (GEO) poisoning. Existing benchmarks largely measure whether manipulated content is retrieved or endorsed, but do not track whether an agent verifies suspicious evidence, revises adopted claims, or recovers before producing its final recommendation. We introduce HAE-GEO, a benchmark that tracks the full trajectory from exposure to recovery under progressively more persuasive Web poisoning. Agents interact via a multi-turn Search-Scrape interface across three attack levels (L1 direct assertion, L2 contextual camouflage, and L3 apparent corroboration), supported by a controlled corpus of 72,039 clean pages and 770 poisoned pages per level spanning 8 product categories and 154 brands. Evaluation combines deterministic behavioral measures with six semantic rubric dimensions. Evaluating 10 agents, we find three recurring patterns: evidence recognition degrades under the corroboration trap; agentic search improves final resistance without improving evidence recognition or utility; and defense prompting increases verification, yet rarely converts verification into recovery.

</details>

### 20. Agent-Fence: Mapping Security Vulnerabilities Across Deep Research Agents

📄 [arXiv](https://arxiv.org/abs/2602.07652) · 🎓 [Official](https://ojs.aaai.org/index.php/AAAI-SS/article/view/42945)　📅 2026-02　🏷 AAAI-SS 2026

**关键词**：`benchmark`、`deep research agent security`、`trust-boundary taxonomy`、`denial of wallet`、`MSBR`

👤 **作者**：Sai Puppala、Ismail Hossain、Md Jahangir Alam、Yoonpyo Lee、Jay Yoo、Tanzim Ahad、Syed Bahauddin Alam、Sajedul Talukder

- 🎯 **研究动机**：LLM 以自主 agent 形态部署后，安全失效从单条不安全文本转移到多步轨迹（规划、持久状态、外部工具调用），而既有评测多聚焦 prompt 层攻击，缺少对 deep research agent 架构级安全边界的系统测绘。
- 🔬 **研究方法**：AgentFence 定义 14 类信任边界攻击（覆盖 planning、memory、retrieval、tool use、delegation），以 trace-auditable conversation breaks（未授权工具使用、错误主体动作、状态/目标完整性违反、攻击关联偏移）检测失效；固定基座模型，在 8 种 agent 架构原型（LangGraph 到 AutoGPT）下做持久多轮交互测试，报告平均安全破坏率 MSBR 与失效构成。
- 📌 **结论**：MSBR 随架构差异巨大（LangGraph 0.29±0.04 到 AutoGPT 0.51±0.07）；风险最高的全是运营类——**Denial-of-Wallet 0.62±0.08**、Authorization Confusion 0.54、Retrieval Poisoning 0.47、Planning Manipulation 0.44，而 prompt 类攻击在标准设定下低于 0.20；边界违反主导失效构成（SIV 31%、WPA 27%、UTI+UTA 24%），授权混淆与目标劫持相关 ρ≈0.63——把 agent 安全重新定义为"是否随时间保持在目标与授权包络内"。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As LLMs are increasingly deployed as autonomous agents that plan, maintain persistent state, and invoke external tools, security failures shift from unsafe single outputs to unsafe multi-step trajectories. Existing evaluations largely focus on prompt-centric attacks, leaving the architectural trust boundaries of deep research agents unmapped. We present AgentFence, an architecture-focused security evaluation comprising 14 trust-boundary attack classes spanning planning, memory, retrieval, tool use, and delegation. Failures are detected via trace-auditable conversation breaks: unauthorized or unsafe tool use, wrong-principal actions, state and objective integrity violations, and attack-linked deviations. Holding the base model fixed, we evaluate eight agent archetypes under persistent multi-turn interaction. Mean security break rate (MSBR) varies widely by architecture, from 0.29 +/- 0.04 (LangGraph) to 0.51 +/- 0.07 (AutoGPT). The highest-risk classes are operational: Denial-of-Wallet (0.62 +/- 0.08), Authorization Confusion (0.54 +/- 0.10), Retrieval Poisoning (0.47 +/- 0.09), and Planning Manipulation (0.44 +/- 0.11); prompt-centric classes remain below 0.20 under standard settings. Boundary violations dominate the break composition (SIV 31%, WPA 27%, UTI+UTA 24%, ATD 18%), and authorization confusion correlates with objective hijacking (rho ~= 0.63) and tool hijacking (rho ~= 0.58). Our results reframe agent security around whether an agent remains within its goal and authority envelope over time.

</details>

### 21. Iris: Climbing to the Search Frontier

📄 [arXiv](https://arxiv.org/abs/2609.04304)　📅 2026-09

**关键词**：`analysis`、`search agent`、`SFT-RL climbing`、`multi-hop question construction`、`capability baseline`

👤 **作者**：Ziyuan Liu、Hengqi Liu、Zichuan Wang、…

- 🎯 **研究动机**：搜索 agent 的能力前沿受限于任务构造质量与训练管线——现有多跳问答可被字符串匹配破解线索、闭书可答，无法逼出真实检索与推理；同时推理时上下文管理对这些基准的影响常大于系统间报告差异。
- 🔬 **研究方法**：Iris-mini（35B-A3B）与 Iris-pro（397B-A17B）两个搜索 agent：任务从 web 语料超链接结构反向构造——在种子页出链实体图上编写多跳链，把非答案实体改写为描述性引用使线索无法字符串匹配，只保留闭书失败但给证据即解的问题；轨迹经轨迹级+轮级双重过滤后 SFT，再对 live search 做 RL（reward judge 与 observation summarizer 部署在训练集群内，超长 rollout 请求级中断并从已提交前缀续跑）；两阶段交替的 SFT-RL climbing 把每轮 RL 中最难解出与最高效的 rollout 回馈下一轮监督；评测固定工具集/上下文上限/judge，每组基准在有/无推理时上下文管理下各测一次。
- 📌 **结论**：给出可复现的搜索 agent 数据管线与训练配方，并在受控对照下分离上下文管理对基准分数的贡献——作为搜索 agent 安全研究（GEO 投毒、注入、劫持）的对象底座与能力基线。

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We present Iris-mini and Iris-pro, two search agents trained at the 35B-A3B and 397B-A17B scales, together with the data pipeline and training recipe behind them. Tasks are reverse-constructed from the hyperlink structure of a web corpus: we author multi-hop chains over an entity graph distilled from a seed page and its out-links, rewrite every non-answer entity into a descriptive reference so that no clue can be resolved by string matching, and admit only questions that a reference model fails closed-book yet solves once the supporting evidence is supplied. These questions are then turned into trajectories, which are filtered at both the trajectory and the turn level before SFT. The policy is then optimized by RL against live search, with the reward judge and the observation summarizer served inside the training cluster, and with over-long rollouts interrupted at the request level and resumed from their committed prefix at the next step. We alternate the two stages in a procedure we call SFT-RL climbing, returning the hardest solved and most efficient rollouts of each RL round to the next supervised pass. Because inference-time context management is worth more on these benchmarks than most reported differences between systems, we evaluate every benchmark both with and without it, holding the tool set, the context limit, and the judge fixed.

</details>

### 22. EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents

📄 [arXiv](https://arxiv.org/abs/2605.12887)　📅 2026-05

**关键词**：`attack`、`evidence ecosystem`、`trajectory-aware GEO`、`coordinated pages`

👤 **作者**：Hengwei Ye、Jiasheng Mao、Zhenhan Guan、Zheng Tian

- 🎯 **研究动机**：现有 GEO 只研究单网页，而 agentic web search 是多步过程（发查询、爬页、跟链接、改写搜索、跨步综合证据），影响力取决于页面如何组织、连接并沿浏览轨迹被遭遇
- 🔬 **研究方法**：把 GEO 形式化为环境级影响问题；TRACE 构建轨迹感知协同证据生态：agent 可见的导航入口页 + 异构支持页，用共享术语、内链与一致产品属性分阶段引入、验证、强化虚构目标产品；在 OPR-Bench 开放式产品推荐上评测
- 📌 **结论**：最终目标推荐率 consistently 超页面级 GEO 基线；轨迹级指标显示初始目标爬取、目标定向后续搜索与内链爬取均增加——收益来自塑造 agent 的证据获取过程而非单纯堆目标内容

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Web-enabled LLM agents are changing how online information influences search outcomes. Existing Generative Engine Optimization (GEO) studies mainly focus on individual webpages. However, agentic web search is not a single-document setting: an agent may issue queries, crawl pages, follow links, reformulate searches, and synthesize evidence across multiple browsing steps. Influence therefore depends not only on page content, but also on how pages are organized, connected, and encountered along the agent's browsing trajectory. We study this shift through Ecosystem Generative Engine Optimization (EcoGEO), which treats GEO as an environment-level influence problem for web-enabled LLM agents. To instantiate this perspective, we propose TRACE, a Trajectory-Aware Coordinated Evidence Ecosystem. Given a recommendation query and a fictional target product, our method builds a controlled evidence environment that coordinates an agent-facing navigation entry page with heterogeneous support pages. These pages use shared terminology, internal links, and consistent product attributes to introduce, verify, and reinforce the target product. We evaluate our method on OPR-Bench, a benchmark for open-ended product recommendation. Experiments show that it consistently outperforms page-level GEO baselines in final target recommendation. Trajectory-level metrics further show increased initial target-result crawls, target-specific follow-up searches, and internal-link crawls, suggesting that the gains come from shaping the agent's evidence-acquisition process rather than merely adding more target-related content. Overall, our findings support an ecosystem research paradigm for GEO, where web-enabled LLM agents are studied in relation to the broader evidence environments that guide search, browsing, and answer synthesis.

</details>

### 23. One Polluted Page Is Enough: Evaluating Web Content Pollution in LLM Recommenders

📄 [arXiv](https://arxiv.org/abs/2606.13610) · 🌐 [Project](https://github.com/leoluolol/forge-benchmark)　📅 2026-06

**关键词**：`attack`、`product fabrication`、`GEO pollution`、`recommendation corruption`

👤 **作者**：Minghao Luo、Liang Chen

- 🎯 **研究动机**：搜索增强 LLM 日益介入日常消费推荐并检索 live 网页，GEO 运营者污染的内容可能使其沦为假产品的不知情推销者
- 🔬 **研究方法**：FORGE 在冻结的已检索网页集合中把真实产品局部改写为虚构产品，225 个真实产品 × 15 类 × 5 消费场景，12 个商用/开源 LLM 上测假产品被推荐率，并检验四种防御
- 📌 **结论**：单页污染即达最高 27% fooled rate，top-3 全替换升至 73.8%；模型对产品缺乏稳定先验时更脆弱；reasoning 不缓解反而编造虚假社会证明；怀疑提示同样加重脆弱性，共识过滤器误伤真品，可信度重排只清除约六分之一假货

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Search-augmented LLMs increasingly mediate everyday consumer recommendations by retrieving live web content. This creates a new risk: LLM recommenders may consume web content that Generative Engine Optimization (GEO) operators have polluted to mislead them. We ask: to what extent do they become unwitting promoters of fake products? We introduce FORGE (Fake Online Recommendations in Generative Environments), which locally rewrites real products in a frozen set of retrieved web pages into fake ones and measures how often the LLM recommends the fake product, across 225 real products in 15 categories and 5 consumer scenarios. Across 12 commercial and open-weights LLMs, all models are vulnerable: a single polluted page yields fooled rates of up to 27%, while the full top-3 replacement raises this to 73.8%. Vulnerability varies across categories, increasing when models lack stable prior knowledge of the products. Reasoning does not mitigate this vulnerability; instead, it often generates spurious social proof to justify false recommendations. None of the four defenses is adequate: the skepticism prompt can exacerbate vulnerability much like reasoning, the two consensus filters risk suppressing legitimate products, and credibility re-ranking helps every model but removes only a sixth of the fakes. We release the FORGE benchmark and the evaluation code at https://github.com/leoluolol/forge-benchmark.

</details>
