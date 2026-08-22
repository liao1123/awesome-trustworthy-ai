# Scientific Research Agent Reliability

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 Deep Research 与跨学科 Research Agent 如何检索资料、理解图表、组织证据并生成长篇报告。可靠性不能只看 final answer 或文风，而要区分 retrieval gap 与 utilization gap，跟踪 hallucination 在 planning-search-synthesis 中的传播，检查 citation-source、text-visual evidence、claim-confidence 和 visual provenance 是否一致，并控制 search-time contamination、动态网页和不可复现 tool access 等评测混杂因素。

## 研究脉络

- **系统与训练基线：** MMSearch-R1、MM-DeepResearch、VSearcher 与 SearchEyes 从 prompt scaffold 发展到 end-to-end RL、search-world simulation 和长程多模态工具调用，为后续可靠性分析定义可观测的 action 与 evidence boundary。
- **终局到过程评测：** DeepResearch Bench、ReportBench、TRACE、MiroEval 与 DR3-Eval 将 content quality 扩展到 trajectory utility、static sandbox、process score 和 multimodal provenance。
- **错误定位与事实核验：** DeepHalluBench、DRIFT 与 DeepFact 从整份报告分数转向 responsible stage、span-level first error、claim-level evidence 和可修订 benchmark label。
- **Multimodal evidence：** MMDeepResearch-Bench、ViDR 与 TVIR 将图像搜索、局部视觉线索、source figure、citation grounding 和 text-visual integrity 纳入同一报告链。
- **当前边界：** 更多搜索不必然带来更可靠结论，公开 benchmark 还会被 search-time contamination 污染；评测需保存来源快照、完整 trajectory、claim-level evidence、视觉 provenance 和停止依据。

## 基础系统与训练路线

这些工作主要建立 Deep Research 的 search scaffold、训练方法与多模态工具接口，用于定义可靠性研究的系统边界；这里不把 capability gain 本身视为安全结论。

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | SearchEyes: Towards Frontier Multimodal Deep Search Intelligence via Search World Simulation | tool、search world simulation、multimodal retrieval、hierarchical RL | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.05943) | [Code](https://github.com/Frostlinx/SearchEyes) | 针对真实网页训练昂贵、动态且难以复现；论文用 typed knowledge graph 模拟可控 search world，并结合 pretraining、knowledge curriculum 与 hierarchical policy optimization；结果在保留真实搜索迁移能力的同时提供可审计的长程训练环境。 |
| 2026&#8209;06 | S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Research Agents | tool、long-horizon research、file analysis、skill orchestration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.15367) | [Code](https://github.com/ScienceOne-AI/S1-DeepResearch) | 针对 Deep Research 被简化为网页 QA、忽略文件分析与复杂交付物；论文整合 planning、web、files、code 和 reusable skills 构建长程 Agent；结果扩展了真实研究能力，也把可靠性边界从 source retrieval 延伸到多工具编排。 |
| 2026&#8209;04 | Towards Long-horizon Agentic Multimodal Search | tool、LMM-Searcher、visual UID、long-horizon search | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.12890) | [Code](https://github.com/RUCAIBox/LMM-Searcher) | 针对图像直接塞入长 context 会造成 token 膨胀且难以持续引用；论文用 file-based visual UID 与 fetch-image action 支持百轮级图文搜索；结果建立可追踪视觉证据的长程接口，但长期 memory 与 source consistency 仍需独立评测。 |
| 2026&#8209;04 | Deep-Reporter: Deep Research for Grounded Multimodal Long-Form Generation | tool、multimodal report、checklist synthesis、recurrent context | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.10741) | 暂未公开 | 针对多模态 Deep Research 难以把网页、图像和长篇结构同时保持 grounded；论文组合 search-filter、checklist-guided synthesis 与 recurrent context，并提出 M2LongBench；结果提高长文多模态生成，为逐段证据核验提供系统基线。 |
| 2026&#8209;04 | MTA-Agent: An Open Recipe for Multimodal Deep Search Agents | tool、multimodal search、verified data、trajectory replay | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.06376) | 暂未公开 | 针对多模态 Deep Search 的训练 recipe、数据过滤和工具轨迹不透明；论文公开 MTA-Vision-DeepSearch 数据构造、verified sample 与 replay 训练流程；结果说明高质量轨迹与工具反馈对长程视觉检索至关重要。 |
| 2026&#8209;03 | VSearcher: Long-Horizon Multimodal Search Agent via Reinforcement Learning | tool、visual search、long-horizon RL、tool trajectory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.02795) | [Code](https://github.com/Ruiyang-061X/VSearcher) | 针对多模态 Agent 难以在长程交互中决定何时搜索、查看与验证图像；论文用 reinforcement learning 训练端到端 visual search policy；结果改善跨轮工具使用，同时提供分析 search efficiency 与错误传播的完整轨迹。 |
| 2026&#8209;03 | MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline | tool、multimodal research、Hyper-Search、offline retrieval | ICML 2026 | [ICML](https://icml.cc/Downloads/2026) · [arXiv](https://arxiv.org/abs/2603.01050) | [Code](https://github.com/HJYao00/MM-DeepResearch) | 针对 text-only Deep Research 无法显式规划图像与文本工具；论文提出 Hyper-Search、DR-TTS 数据和 offline search 训练方案；结果建立多模态 planning、tool invocation 与 synthesis 的开放基线，便于后续逐环节可靠性比较。 |
| 2025&#8209;06 | MMSearch-R1: Incentivizing LMMs to Search | tool、on-demand search、multimodal RL、search penalty | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.114/) · [arXiv](https://arxiv.org/abs/2506.20670) | [Code](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) | 针对固定 RAG 和 prompt scaffold 会过度或机械调用搜索；论文用 outcome reward 与 search penalty 训练 LMM 自主决定何时调用 text/image search；结果在保持任务表现时减少 30% 以上搜索调用，为 efficiency-reliability trade-off 提供基线。 |

## Failure Diagnosis 与 Contamination

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents | analysis、deep search、retrieval gap、utilization gap | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.01913) | 暂未公开 | 针对增加 search step 是否真正改善 deep research 不清楚；论文用人工 document relevance 分离 evidence retrieval 与 utilization；结果搜索量和答案质量仅弱相关，失败主要来自未找到证据或找到却未正确使用，且轨迹后段常是低收益冗余搜索。 |
| 2026&#8209;06 | Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation | analysis、search-time contamination、answer leakage、score inflation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.05241) | 暂未公开 | 针对联网 Agent 可能在测试时检索到 benchmark 信息或答案而绕过推理；论文定义 metadata、question-context 和 explicit-answer 三类 leakage 并在六个公开 benchmark 上检测；结果 contamination 可把表现抬高最多 4%，因此需要隔离语料、公开轨迹和受控访问。 |
| 2026&#8209;01 | Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory | benchmark、deep research、PING taxonomy、claim verification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.22984) | [Code](https://github.com/yuhao-zhan/DeepHalluBench) | 针对只评 final report 会隐藏 plan-search-summarize 中累积的 hallucination；论文用 Propagation、Intent、Noise-induced、Grounding taxonomy 将轨迹拆成 action、claim 和 sub-query 核验；结果六种 DRA 均存在明显 process reliability gap，尤其是错误传播与认知偏差。 |

## Factuality、Provenance 与 Error Localization

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Silent Failures in Multimodal Agentic Search: A Diagnostic Taxonomy and Cross-Judge Evaluation | analysis、silent failure、phantom grounding、cross-judge agreement | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.19793) | [Code](https://github.com/DingWu1021/silent-failures-multimodal-agentic-search) | 针对 final answer 正确时 multimodal search 轨迹中的错误会被隐藏；论文归纳 modality shortcut、phantom grounding、wrong-evidence-right-answer 等 failure taxonomy 并比较多类 judge；结果终局准确率系统性高估过程可靠性，且不同 judge 对 provenance error 的判断并不稳定。 |
| 2026&#8209;06 | Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories | detection、span localization、first error、DRIFT | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.02060) | [Code](https://github.com/NJU-LINK/DRIFT) | 针对报告级分数无法指出长轨迹中第一个致因错误；论文构建 TELBench 并用 DRIFT 逐 claim 审计、回溯 supporting span 与 responsible step；结果 first-error localization 最多提高约 30 个百分点，使 failure attribution 从整轮分类下沉到证据片段。 |
| 2026&#8209;03 | DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality | benchmark、Audit-then-Score、claim factuality、evolving labels | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1586/) · [arXiv](https://arxiv.org/abs/2603.05912) | [Code](https://github.com/kkkevinkkkkk/DeepFact) | 针对高难度 Deep Research claim 连专家 one-shot label 也不可靠；论文提出 Audit-then-Score，让 verifier 以证据挑战并修订 benchmark，再用 DeepFactEval 评分；结果多轮审计把专家标签准确率从 60.8% 提高到 90.9%，说明 factuality benchmark 本身也需可追溯演化。 |

## Trajectory 与 Report Trustworthiness

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Towards Trustworthy Report Generation: A Deep Research Agent with Progressive Confidence Estimation and Calibration | defense、claim confidence、evidence grounding、report calibration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.05952) | 暂未公开 | 针对开放式报告没有 ground truth 时主观质量指标无法表达 epistemic reliability；论文在多跳检索和写作流程中逐 claim 估计并校准 confidence；实验与案例显示证据透明度和可解释性改善，但仍依赖检索质量与 confidence validity。 |
| 2026&#8209;02 | TRACE: Trajectory-Aware Comprehensive Evaluation for Deep Research Agents | benchmark、trajectory utility、evidence grounding、latent capability | WWW 2026 | [ACM](https://doi.org/10.1145/3774904.3792738) · [arXiv](https://arxiv.org/abs/2602.21230) | 暂未公开 | 针对 Pass@1 会掩盖证据、效率和推理质量；论文以 hierarchical trajectory utility 与 scaffolded capability assessment 评测完整研究过程；结果揭示仅按答案准确率无法观察的 accuracy、efficiency 与 robustness trade-off。 |

## Multimodal Evidence Chain

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | TVIR: Building Deep Research Agents Towards Text-Visual Interleaved Report Generation | tool、interleaved report、visual retrieval、source attribution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.02320) | [Code](https://github.com/NJU-LINK/TVIR) | 针对长篇报告虽含图片却缺少图文交错规划和来源对应；论文构建 text-visual interleaved research task、层级 Agent 与联合评测；结果将视觉材料从装饰性输出提升为可检索、可定位的报告证据，但生成质量仍受 visual source selection 限制。 |
| 2026&#8209;05 | ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence | tool、source figure、visual grounding、report verifiability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.13034) | 暂未公开 | 针对多模态报告中的图表常被重新描述却无法回溯到 source visual；论文把原始 figure 作为可检索、可引用证据并提出 MMR Bench+；结果提升报告的视觉 verifiability，说明评价必须同时检查选图、文本 claim 与 source region 的对应。 |
| 2026&#8209;02 | Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models | benchmark、visual search、cropped retrieval、cross-modal leakage | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.02185) | [Code](https://github.com/Osilly/Vision-DeepResearch) | 针对现有 visual research 题可由文本线索或近似整图匹配投机求解；论文构建 2,000 个经专家核验的 realistic visual-text search task 并提出 multi-round cropped search；结果说明当前 MLLM visual retrieval 仍不足，而分轮局部检索可以改善表现。 |
| 2026&#8209;01 | MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents | benchmark、multimodal evidence、citation grounding、text-visual integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.12346) | [Project](https://mmdeepresearch-bench.github.io/) | 针对 text-only benchmark 无法检查图表证据是否被正确用于 citation-rich report；论文以 140 个跨 21 领域任务和 FLAE、TRACE、MOSAIC 三组指标分解报告、引用与跨模态一致性；结果强文风不保证证据忠实，multimodal integrity 仍是主要瓶颈。 |

## 综合 Benchmark 与评测基础设施

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research | benchmark、scientific rediscovery、raw data、expert rubric | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.07591) | [Code](https://github.com/InternScience/ResearchClawBench) | 针对 end-to-end scientific research 缺少基于真实数据且可核验的评测；论文从十个领域建立 40 个隐藏目标论文、提供原始资料并用专家 multimodal rubric 评分；结果最强系统均分仍约 21，失败集中于实验协议、证据和 scientific core 不匹配。 |
| 2026&#8209;06 | VistaHop: Benchmarking Long-Horizon Visual DeepSearch | benchmark、visual deep search、multi-hop evidence、VistaArena | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.03273) | 暂未公开 | 针对视觉搜索 benchmark 常可用单次识图或文本检索完成；论文构建 350 个需要反复查看局部图像、跨网页追踪证据的任务与 VistaArena；结果最佳系统仅取得 24.31% 表现，主要瓶颈是线索保持、跨轮视觉定位与证据组合。 |
| 2026&#8209;04 | DR$^3$-Eval: Towards Realistic and Reproducible Deep Research Evaluation | benchmark、static sandbox、multifile report、reproducible retrieval | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.14683) | [Code](https://github.com/NJU-LINK/DR3-Eval) | 针对动态网页和含糊任务使 DRA 评测难复现；论文为真实 multimodal、multi-file request 配置含支持文档、distractor 与 noise 的静态 sandbox，并评测 recall、factuality、citation、instruction 与 depth；结果暴露 retrieval robustness 和 hallucination control 的关键失败。 |
| 2026&#8209;03 | MiroEval: Benchmarking Multimodal Deep Research Agents in Process and Outcome | benchmark、multimodal process、active factuality、outcome evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.28407) | [Code](https://github.com/MiroMindAI/MiroEval) | 针对多模态 Deep Research 只评 final answer 会遗漏无效搜索和错误证据；论文联合评测 adaptive synthesis、active factuality、完整 process 与 outcome；结果 process score 能预测终局表现，且需要真实视觉证据的任务仍明显更难。 |
| 2026&#8209;01 | DeepSurvey-Bench: Evaluating Academic Value of Automatically Generated Scientific Surveys | benchmark、survey value、scholarly communication、research guidance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.15307) | 暂未公开 | 针对结构和引用相关性只能反映 survey 表层质量；论文从 information、scholarly communication 和 research guidance 三维构建 academic-value 数据与评测；结果与人工判断更一致，并能揭示传统表面指标覆盖不到的学术价值缺陷。 |
| 2025&#8209;10 | AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite | benchmark、scientific workflow、controlled tools、confounder control | ICLR 2026 Oral | [ICLR](https://iclr.cc/virtual/2026/poster/10009971) · [arXiv](https://arxiv.org/abs/2510.21652) | 暂未公开 | 针对 scientific Agent benchmark 缺少可复现工具且受 cost、tool access 和 baseline 混杂；论文提供覆盖完整发现流程的 2,400 余题、production-grade search environment 与统一 Agent suite；57 个 Agent 的评测表明局部能力进步尚未解决整体科学研究辅助。 |
| 2025&#8209;10 | Dr. Bench: A Multidimensional Evaluation for Deep Research Agents, from Answers to Reports | benchmark、long-form report、citation trustworthiness、topic focus | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.02190) | 暂未公开 | 针对答案型 benchmark 不适合长篇 research report；论文建立 214 个专家任务与 reference bundle，并联合评测 semantic quality、topical focus 和 retrieval trustworthiness；结果 DRA 优于简单 search-augmented model，但报告质量和证据仍有显著改进空间。 |
| 2025&#8209;08 | MMSearch-Plus: Benchmarking Provenance-Aware Search for Multimodal Browsing Agents | benchmark、visual provenance、iterative retrieval、Set-of-Mark | ICLR 2026 | [ICLR](https://iclr.cc/virtual/2026/poster/10009159) · [arXiv](https://arxiv.org/abs/2508.21475) | [Repository](https://github.com/mmsearch-plus/MMSearch-Plus)（dataset 已发布，Agent 与评测代码待发布） | 针对多模态 browsing benchmark 可被 text-only shortcut 解决；论文以 311 个任务要求从局部视觉线索迭代检索并交叉核验来源，并提供 Set-of-Mark 接口；结果最强系统准确率为 36.0%，失败集中在网页定位和相似事件区分。 |
| 2025&#8209;08 | DeepScholar-Bench: A Live Benchmark and Automated Evaluation for Generative Research Synthesis | benchmark、research synthesis、live evaluation、verifiable citation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.20033) | [Code](https://github.com/guestrin-lab/deepscholar) | 针对静态学术 QA 无法衡量 related-work synthesis、检索覆盖与引用可核验性；论文构建持续更新的 live benchmark 和自动 evidence-aware evaluation；结果被测系统总体得分均低于 19%，暴露 retrieval completeness 与 synthesis quality 的共同缺口。 |
| 2025&#8209;08 | ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks | benchmark、report factuality、citation verification、survey task | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.15804) | [Code](https://github.com/ByteDance-BandAI/ReportBench) | 针对 DRA 报告需要同时核验覆盖面、引用与非引用陈述；论文从已发表 survey 反推任务并用 Agent 抽取 claim、核对原文和网页证据；结果商业 DRA 整体优于普通 browsing LLM，但 coverage depth 和 factual consistency 仍不足。 |
| 2025&#8209;08 | SurGE: A Benchmark and Evaluation Framework for Scientific Survey Generation | benchmark、survey generation、citation accuracy、academic corpus | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2508.15658) | [Code](https://github.com/oneal2000/SurGE) | 针对自动综述缺少统一任务和评价协议；论文用专家综述、完整 cited reference 与百万篇论文语料评测 completeness、citation accuracy、structure 和 content；结果即使 agentic framework 也与高质量科学综述存在明显差距。 |
| 2025&#8209;06 | DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents | benchmark、PhD-level task、citation accuracy、human-aligned scoring | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.11763) | [Code](https://github.com/Ayanami0730/deep_research_bench) | 针对 DRA 缺少跨领域、与人工一致的系统评测；论文构建 100 个跨 22 领域 PhD-level task，并分别评估报告质量、有效引用数和 citation accuracy；结果为后续 DRA 比较建立可复用基线，但仍依赖专家任务与 evaluator calibration。 |
| 2025&#8209;05 | DeepResearchGym: A Free, Transparent, and Reproducible Evaluation Sandbox for Deep Research | tool、evaluation sandbox、reproducible search、agent rollout | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.19253) | [Project](https://www.deepresearchgym.ai/) | 针对闭源 Deep Research 的搜索环境、工具和评测链不可复现；论文提供免费透明的 search sandbox、Agent rollout 与统一 evaluator；结果把系统比较从不可控产品接口转化为可重复实验，也能支持后续 contamination、poisoning 和 defense 研究。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Deep Research Max: a step change for autonomous research agents | Google | long-horizon research、MCP、multimodal grounding | [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/) | 说明 Gemini Deep Research 与 Max 的系统边界，包括开放网页与私有数据联合检索、remote MCP、文件输入、协作式 planning、原生图表和过程 streaming；这些部署能力也定义了 provenance、权限与多源冲突评测必须覆盖的新接口。 |
| 2025&#8209;02 | Introducing deep research | OpenAI | web research、tool use、source citation | [OpenAI](https://openai.com/index/introducing-deep-research/) | 介绍 Deep Research 的多步网页搜索、文件与 Python 工具、RL 训练和带 citation 的报告流程，并展示面向真实知识工作的产品交互；可作为理解早期商业系统可见 trajectory、source documentation 与评测边界的一手材料。 |

> 引用是否存在、是否支持对应 claim 的专门方法见 [Citation and Evidence Integrity](citation-and-evidence-integrity.md)；通用 Agent 的 trajectory attribution 见 [Agent Trajectory Monitoring](../agent/trajectory-monitoring-and-failure-attribution.md)；开放网页投毒、有害检索与 research-trajectory hijacking 见 [Search Agent Security](../agent/search-agent-security.md)；生成式搜索的 ranking manipulation 见 [GEO Security](../agent/generative-engine-optimization-security.md)。
