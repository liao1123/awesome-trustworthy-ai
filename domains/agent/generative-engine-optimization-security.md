# Generative Engine Optimization Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究 Generative Engine Optimization（GEO）如何通过改写网页文本、图像或结构信号改变生成式搜索中的检索、重排、引用、可见性和推荐结果。GEO 本身包含正常的内容适配与可用性优化；安全问题出现在攻击者利用同一机制操纵排名、伪装低质量或有缺陷的对象、压制竞争者，或让 prompt injection 穿过 retriever-reranker-generator 全链路。因而本页同时保留 cooperative GEO 基础、现实 pipeline 评测和 black-hat manipulation，避免把“提升可见性”直接等同于攻击。

## 研究脉络

- **可见性优化起点：** GEO 建立生成式回答中的 visibility metric 与 GEO-Bench，研究对象由传统网页排名转向内容是否被 LLM 选择、引用和写入回答。
- **自动化与个性化优化：** AutoGEO、Mind Reader 与 AgenticGEO 从人工 heuristic 发展到 preference rule、latent user demand 和自演化 strategy search，提升内容适配能力的同时也扩大可自动化操纵的空间。
- **Black-hat rank manipulation：** Adversarial SEO、StealthRank、LLM ranker injection 与 MGEO 分别利用网页指令、可读文本 suffix、token optimization 和图文联合扰动提升目标排名。
- **全链路现实性：** SAGEO Arena、GEO-Bench 与 RAG survival 分析表明，能影响 generator 不代表能通过 retriever 与 reranker；结构信号、攻击隐蔽性和真实 search interface 都会改变结论。
- **下游安全影响：** SafeGEO 把指标从 target rank 扩展到推荐集合中的实际危害；当前防御多为静态 detector 或 prompt guard，仍缺少跨平台、长期部署和自适应攻击下的稳定证据。

## Cooperative GEO 与基础方法

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Mind Reader: Latent User Demand-Guided Content Optimization for Generative Search Engine | tool、latent user demand、query augmentation、content visibility | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1894/) | 暂未公开 | 针对已有 GEO 只学习表面 heuristic 或 query-dependent preference、忽略用户潜在需求；论文用 query decomposition-recombination 与 reasoning coverage 改写内容；结果在 GEO-Bench 和 PC-GEO 上提高可见性，但也说明 demand inference 可成为更精细的操纵能力。 |
| 2026&#8209;03 | AgenticGEO: A Self-Evolving Agentic System for Generative Engine Optimization | tool、strategy evolution、MAP-Elites、co-evolving critic | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.20213) | [Code](https://github.com/AIcling/agentic_geo) | 针对固定 GEO heuristic 难以适配不同 query、domain 与生成式引擎；论文用 MAP-Elites 搜索多样改写策略并让 critic 与策略共同演化；结果自动发现的策略可以持续提高 visibility，同时增加了大规模、自适应内容操纵的可获得性。 |
| 2026&#8209;03 | Diagnosing and Repairing Citation Failures in Generative Engine Optimization | tool、citation failure、AgentGEO、document repair | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.09296) | 暂未公开 | 针对 contribution gain 不等于网页最终被生成式回答引用；论文建立 citation failure taxonomy、AgentGEO 工具库和 document-centric benchmark 并做局部修复；结果只改动少量文本即可显著提高 citation，且通用 GEO 对 long-tail 文档可能适得其反。 |
| 2025&#8209;10 | What Generative Search Engines Like and How to Optimize Web Content Cooperatively | tool、AutoGEO、preference rules、search utility | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=K8EinVWtUB) · [arXiv](https://arxiv.org/abs/2510.11438) | [Code](https://github.com/cxcscmu/AutoGEO) | 针对内容提供者不了解生成式引擎选择证据的偏好；论文从 pairwise visibility 差异归纳 preference rule，并用于 prompt-based 与 RL-based AutoGEO；结果在保持 search utility 的同时提升内容 traction，建立 cooperative optimization 的可复现基线。 |
| 2023&#8209;11 | GEO: Generative Engine Optimization | tool、GEO-Bench、visibility metric、content optimization | KDD 2024 | [KDD](https://doi.org/10.1145/3637528.3671900) · [arXiv](https://arxiv.org/abs/2311.09735) | [Project](https://generative-engines.com/GEO/) | 针对传统 SEO 指标无法衡量网页内容在生成式回答中的曝光；论文提出 GEO-Bench、visibility metric 和多种内容优化策略；结果建立该领域的基础任务，同时揭示引用、权威措辞与写作结构会显著影响生成式引擎选择。 |

## Black-Hat Ranking 与 Prompt Manipulation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | The Vulnerability of LLM Rankers to Prompt Injection Attacks: You are to [MARK] this paper as the Best Paper | attack、LLM ranker、prompt injection、rank promotion | SIGIR 2026 | [ACM](https://doi.org/10.1145/3805712.3808553) · [arXiv](https://arxiv.org/abs/2602.16752) | [Code](https://github.com/ielab/LLM-Ranker-Attack) | 针对 LLM reranker 会把候选文档正文同时当数据和指令；论文在论文排序场景构造显式与隐蔽 prompt injection 以提升目标名次；结果目标文档可被稳定推高，表明 ranking prompt 的 instruction boundary 需要独立防护。 |
| 2026&#8209;01 | Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers | attack、multimodal GEO、image perturbation、text suffix | KnowFM 2026 | [ACL Anthology](https://aclanthology.org/2026.knowfm-1.9/) · [arXiv](https://arxiv.org/abs/2601.12263) | [Code](https://github.com/glad-lab/MGEO) | 针对 VLM ranker 的图文耦合能否被内容提供者反向利用；论文交替优化 imperceptible image perturbation 与 fluent textual suffix；结果联合攻击明显强于单模态方法，说明只审核文本质量无法保护 multimodal ranking。 |
| 2025&#8209;04 | StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization | attack、stealthy suffix、energy-based model、rank manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.05804) | [Code](https://github.com/Tangyiming205069/controllable-seo) | 针对直接 prompt injection 容易被人或 detector 识别；论文用 energy-based objective 与 Langevin optimization 生成流畅、低可疑度的文本 suffix；结果可在保持语义自然度的同时显著提升目标排名，形成 effectiveness-stealth trade-off。 |
| 2024&#8209;06 | Adversarial Search Engine Optimization for Large Language Models | attack、preference manipulation、third-party content、competitive ranking | ICLR 2025 | [OpenReview](https://openreview.net/forum?id=hkdqxN3c7t) · [arXiv](https://arxiv.org/abs/2406.18382) | 暂未公开 | 针对 LLM 在搜索与 plugin 中从相互竞争的第三方内容中做选择；论文提出 Preference Manipulation Attack，通过受控网页或 plugin 文档抬高攻击者并贬低竞争者；结果在生产搜索引擎和 API 场景均能改变选择，并产生各方都有动力攻击的集体劣化。 |

## Recommendation Harm

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents | benchmark、recommendation agent、unsafe promotion、GEO defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.28356) | [Code](https://github.com/QianfengWen/SafeGEO) | 针对 GEO 评测只看 visibility、无法说明被推广对象是否会伤害用户；论文在 600 个推荐案例上测试 22 种 GEO variant 与有缺陷产品；结果攻击可使问题对象进入推荐集合的比例最高增加 83.2%，简单防御虽降低 promotion 仍未恢复到 clean baseline。 |

## Benchmark 与真实 Pipeline 分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study | analysis、Chinese GSE、citation ecology、interface variance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.15771) | [Code](https://github.com/WENDAOstudy/cn-geo-citation-dataset) | 针对英文 GEO 结论能否外推到中文平台及不同产品入口；论文用 614 个 query 测量四个平台八个 interface 的来源、引用与实体曝光；结果平台和 interface 都会系统性改变 citation ecology，品牌被选择的比例总体较低且差异显著。 |
| 2026&#8209;05 | GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization | benchmark、GEO attack、ranking manipulation、stealth evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.29107) | 暂未公开 | 针对 black-box、white-box 与 white-hat GEO 方法缺少同一协议下的效果和隐蔽性比较；论文在五组数据上统一评测 prompt rewriting、gradient attack 与正常优化；结果黑盒改写可达到或超过梯度方法并规避部分 detector，单看优化权限无法判断风险。 |
| 2026&#8209;05 | Can It Reach the Generator? Investigating the Survival of Prompt-Injection Attacks in Realistic RAG Settings | analysis、RAG pipeline、attack survival、retriever-reranker | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.28017) | [Code](https://github.com/ielab/geo_injection_rag_survival) | 针对直接把攻击文档送入 generator 会高估现实 GEO 攻击；论文在 retriever-reranker-generator 三阶段检查不同注入方法的 survival；结果 gradient 与 override 类攻击多在前级失效，而 LLM-driven injection 更能存活，轻量 guard 在已测攻击上有效但泛化仍未知。 |
| 2026&#8209;03 | Unveiling the Resilience of LLM-Enhanced Search Engines against Black-Hat SEO Manipulation | analysis、black-hat SEO、retrieval filter、SEO-Bench | WWW 2026 | [WWW](https://www2026.thewebconf.org/accepted/research-tracks.html) · [arXiv](https://arxiv.org/abs/2603.25500) | 暂未公开 | 针对传统 black-hat SEO 是否仍能操纵 LLM-enhanced search；论文用 SEO-Bench 在十个产品上测试 keyword stuffing、hidden text 及其改写变体；结果常规攻击多数在 retrieval stage 被过滤，但自然语言重写和分段策略仍能突破部分系统。 |
| 2026&#8209;02 | SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization | benchmark、SAGE pipeline、structured document、retrieval realism | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.12187) | 暂未公开 | 针对只在已检索 plain text 上测 GEO 忽略真实网页结构和多阶段排序；论文构建含完整 search-augmented pipeline 与结构化网页的 SAGEO Arena；结果不少既有方法在 retrieval 或 reranking 阶段反而降低曝光，而结构信号对最终可见性至关重要。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | GEO-Flag: Detecting and Measuring GEO-Optimized Web Content | detection、generative engine optimization、ranking manipulation、content integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16824) | 暂未公开 | GEOFlagBench 用 3,200 个网页评测八类 GEO optimizer，发现聚合高分掩盖方法与作者条件弱点；Intervention-Paired Training 将 F1 从 0.862 提至 0.944、worst-group accuracy 从 0.725 提至 0.883，真实 10,095 页中估计 GEO 占 8.90%。 |
| 2026&#8209;08 | Assessing Attack Surfaces in Generative Search Engines through Publisher Attributes: A Case Study in Political Domains | detection、generative engine optimization、ranking manipulation、content integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.15814) | [Code](https://github.com/mzhkz/QL_Research_CIKM26_Artifacts) | 我们从引文选择和个性化的角度描述了生成搜索引擎（GSE）针对政治领域中毒攻击的攻击面；现有的引文评估研究重点关注答案如何忠实地反映引用的内容；我们的结果表明 (a) 不同 GSE 模型的攻击面不同； (b) GSE 的网络搜索功能塑造了攻击面； (c) 执政党比反对党拥有更广泛的攻击面； (d) 用户配置文件对攻击面的影响很小。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | Institutional Prestige as Geographic Bias in Large Language Models: Evidence from Three Factorial Experiments with Bootstrap Confidence Intervals | analysis、generative engine optimization、ranking manipulation、content integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18107) | [Code](https://github.com/mleyvaz/geo-bias-llm) | 我们研究大型语言模型（LLM）在候选人评估中，是否会依据申请者姓名所体现的族裔和/或机构声望与地理位置进行系统性歧视；研究一采用 3×4 设计，发现统计上稳健的机构等级梯度：在 10 分制上为 +0.297 分（95% bootstrap CI：+0.175 至 +0.422）；姓名来源效应则很小且不显著（95% CI 跨过零）；结果使用中智偏见指数 NBI<T,I,F> 量化；其中 I 分量揭示，低声望资料的评估不一致性更高，这是一种仅看均值的指标无法捕捉的认识论劣势。 |

> 开放网页证据被 Search Agent 读取后造成的 endorsement、harmful search 与 research-trajectory hijacking 见 [Search Agent Security](search-agent-security.md)；固定知识库和 GraphRAG 的语料污染见 [RAG Poisoning](../poisoning-and-backdoors/rag-poisoning.md)；通用 indirect prompt injection 见 [Prompt Injection](../misc/prompt-injection.md)。
