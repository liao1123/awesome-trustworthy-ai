# RAG 投毒

[返回模型投毒与后门目录](README.md)

## 研究方向

RAG 投毒研究攻击者如何向外部语料、向量库或知识图谱注入内容，使恶意文档被召回、通过重排并改变生成结果。该方向关注定向与无查询投毒、单文档和协同文档攻击、多跳与 GraphRAG、幻觉和成本等攻击目标，以及准入过滤、注意力检测、激活溯源、信息流隔离和动态修复。

## 研究脉络

- **基础投毒：** 早期 RAG 攻击通过少量恶意文档和黑盒知识操控改变检索结果与生成答案。
- **Pipeline 扩展：** 后续工作覆盖 GraphRAG、reranker、推理链与成本攻击，攻击对象不再局限于 retriever。
- **解释与防御：** 近期研究系统分析 pipeline 配置造成的成败差异，并发展文档检测、答案溯源和动态隔离防御。

## 投毒与知识操控攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | PURPOSE: Poisoning Conflict Resolution in RAG via Proxy-Fact-Grounded Updates | attack、RAG poisoning、conflict resolution、factual update | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.04756) | 暂未公开 | 针对冲突消解器会拦截直接反驳已有事实的毒文档，论文把恶意主张伪装成由代理事实支撑的新事件更新；结果在 45 个设置中的 35 个取得最高成功率，平均超过最强基线 9.7 个百分点。 |
| 2026&#8209;07 | KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems | attack、system prompt、RAG poisoning、data poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.00422) | [Code](https://github.com/chanwoochoi316/KidnapRAG) | KidnapRAG 仅通过公开可检索文档依次布置 Bait、Chain-Link 与 Mal-Ins，逐步改变 Agentic RAG 的查询重写和证据依赖；在多种框架、LLM 与 benchmark 上均比既有黑盒投毒稳定地劫持多步推理链。 |
| 2026&#8209;06 | Inference Cost Attacks for Retrieval-Augmented Large Language Models | attack、RAG availability、cost attack、corpus poisoning | WWW 2026 | [arXiv](https://arxiv.org/abs/2606.02643) | 暂未公开 | 针对攻击者难直接控制用户提示，论文向外部知识库投毒并用 MA-GRPO 生成可检索且高耗费的恶意文档；结果在保持答案完整时把 token 消耗提高最多 13.12 倍。 |
| 2026&#8209;06 | DiscourseFlip: An Oblique Discourse-Level Opinion Manipulation Attack against Black-box Retrieval-Augmented Generation | attack、RAG poisoning、opinion manipulation、discourse structure | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.01212) | 暂未公开 | 针对直接陈述攻击立场容易与干净语料冲突并被过滤，论文在篇章结构中斜向组织支持材料来改变目标观点；结果在黑盒 RAG 中实现更自然、更隐蔽的意见操控。 |
| 2026&#8209;05 | SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning | attack、RAG poisoning、semantics-preserving、retrieval hijacking | KDD 2026 | [arXiv](https://arxiv.org/abs/2605.28074) | 暂未公开 | 针对高检索相似度的毒文本常出现明显语义或语言异常，论文在保持原意和可读性的约束下优化对抗文档；结果可安静地提升恶意内容排名并劫持生成。 |
| 2026&#8209;04 | AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning | attack、RAG poisoning、single-document poisoning、chain-of-thought | SIGIR 2026 Short Paper | [arXiv](https://arxiv.org/abs/2604.12201) | 暂未公开 | 针对多文档投毒成本高且容易暴露，论文把可诱导错误思维链的证据压入单篇高相关文档；结果一篇毒文档即可干扰复杂推理并把模型引向目标答案。 |
| 2026&#8209;04 | LogicPoison: Logical Attacks on Graph Retrieval-Augmented Generation | attack、GraphRAG poisoning、entity swapping、topology poisoning | ACL 2026 Main | [Official](https://aclanthology.org/2026.acl-long.252/) · [arXiv](https://arxiv.org/abs/2604.02954) | [Code](https://github.com/Jord8061/logicPoison) | 针对 GraphRAG 会稀释传统假内容与指令注入，论文在保持文本流畅的同时交换同类型关键实体来破坏知识拓扑；结果可切断多跳桥接路径并跨 GraphRAG 架构迁移。 |
| 2026&#8209;03 | PIDP-Attack: Combining Prompt Injection with Database Poisoning Attacks on Retrieval-Augmented Generation Systems | attack、RAG poisoning、database poisoning、prompt injection | WWW 2026 | [arXiv](https://arxiv.org/abs/2603.25164) | [Code](https://anonymous.4open.science/r/PIDP-03BC) | 针对传统投毒需要预先知道真实用户查询，论文把推理时字符触发和少量数据库毒段落联合起来；结果可在不知道用户原始查询的情况下操控任意查询响应。 |
| 2026&#8209;03 | KEPo: Knowledge Evolution Poison on Graph-based Retrieval-Augmented Generation | attack、GraphRAG poisoning、knowledge evolution、persistent poisoning | WWW 2026 | [arXiv](https://arxiv.org/abs/2603.11501) | 暂未公开 | 针对图式知识库会随新文档持续演化，论文让污染关系在实体和社区更新中逐步获得更高影响；结果攻击能借知识演化扩大覆盖，而非只对单次固定索引生效。 |
| 2026&#8209;02 | Confundo: Learning to Generate Robust Poison for Practical RAG Systems | attack、RAG poisoning、robust poison、hallucination induction | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/hu-haoyang) · [arXiv](https://arxiv.org/abs/2602.06616) | [Code](https://github.com/HKU-TASR/Confundo) | 针对手工毒文本在不同检索器、提示和生成器上容易失效，论文学习生成兼顾召回与生成操控的鲁棒毒文档；结果能跨实际 RAG 配置稳定诱导错误和幻觉。 |
| 2026 | Reranker Helps, but Not Enough: Towards Strong Poisoning Attacks Against Retrieval-Augmented Generation | attack、RAG poisoning、reranker、character perturbation | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/63324) · [OpenReview](https://openreview.net/forum?id=Y54eyjHFqJ) | [Code](https://github.com/YyyxKun/P3A) | 针对良性数据训练的重排器能挡住许多旧攻击，论文以规则提示构造毒文档并优化约 1% 的字符扰动提升重排名次；结果 P3A 在单文档预算下仍可穿过重排并迁移到普通 RAG。 |
| 2026 | MM-PoisonRAG: Disrupting Multimodal RAG with Local and Global Knowledge Poisoning Attacks | attack、multimodal safety、RAG poisoning、VLM safety | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.1558/) | 暂未公开 | MM-PoisonRAG 的局部攻击在受限访问下 ASR 仍达 56% 且可跨四个 retriever 迁移，全局攻击仅注入一条多模态污染内容便把生成准确率降至 0%，并能绕过现有防御。 |
| 2026 | Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation | attack、medical AI、data poisoning、high-risk deployment | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.892/) | [Code](https://anonymous.4open.science/r/M3Att) | 针对医疗多模态 RAG 攻击通常假设已知查询，M³Att 仅凭数据库分布知识，用不可感知图像扰动提高毒化内容检索率并注入隐蔽误诊信息，在五个模型和数据集上持续生成临床上合理但错误的答案。 |
| 2026 | Eyes-on-Me: Scalable RAG Poisoning through Transferable Attention-Steering Attractors | attack、RAG poisoning、data poisoning、knowledge corruption | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61331) | 暂未公开 | 针对训练数据、偏好信号或模型组件可能被投毒并植入隐蔽后门的问题，论文提出 Eyes-on-Me 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于投毒与后门威胁评估。 |
| 2026 | BadGraph: Structural Knowledge Isolation Attacks against Graph Retrieval-Augmented Generation | attack、GraphRAG、RAG poisoning、knowledge corruption | USENIX Security 2026 | [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/yan-leiming) | 暂未公开 | 针对 GraphRAG 依赖图拓扑聚合证据的问题，BadGraph 注入语义中性的文档以形成隔离目标知识的对抗子图，在三种 GraphRAG 系统上显著降低证据召回与回答 F1。 |
| 2025&#8209;12 | MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks | attack、RAG poisoning、black-box attack、query-agnostic | ACM CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2512.08289) | 暂未公开 | 针对逐查询制作毒文档难以扩展到未知流量，论文在不访问内部参数时生成可覆盖一类查询的通用污染内容；结果以查询无关方式同时提高召回和目标答案采信。 |
| 2025&#8209;10 | RIPRAG: Hack a Black-box Retrieval-Augmented Generation Question-Answering System with Reinforcement Learning | attack、RAG poisoning、reinforcement learning、black-box RAG | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.10008) | 暂未公开 | 针对黑盒攻击无法获得检索和生成梯度，论文以系统反馈为奖励学习毒文本；结果联合适应召回与回答阶段，在有限查询预算下提高目标问答操控成功率。 |
| 2025&#8209;08 | DisarmRAG: Stealthy Retriever Poisoning to Disable Self-Correction in Retrieval-Augmented Generation | attack、RAG poisoning、self-correction、data poisoning | ACM CCS 2026（First Cycle） | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2508.20083) | [Code](https://github.com/ybdai7/DisarmRAG-poisoning-attack) | 针对 RAG 的 self-correction 会修正普通语料投毒的问题，DisarmRAG 直接污染 retriever 并注入抑制纠错的指令，在六个 LLM 和三个 QA 数据集上取得超过 90% 成功率且保持较强隐蔽性。 |
| 2025&#8209;05 | One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems | attack、RAG poisoning、single-document attack、multi-hop QA | Findings of EMNLP 2025 | [arXiv](https://arxiv.org/abs/2505.11548) | [Code](https://anonymous.4open.science/r/AuthChain-45E8) | 针对多跳问题通常需要多篇毒文档且容易暴露，论文用 AuthChain 把完整错误证据链和权威信号压进一篇文档；结果单次注入即可在检索与生成阶段占据主导。 |
| 2025&#8209;01 | GraphRAG under Fire | attack、GraphRAG poisoning、relation injection、scalable attack | IEEE S&P 2026 | [arXiv](https://arxiv.org/abs/2501.14050) | [Code](https://github.com/JACKPURCELL/GraphRAG_Under_Fire) | 针对 GraphRAG 对普通文本投毒更稳健却可能产生图结构攻击面，论文用 GRAGPoison 注入、强化共享关系并生成连贯叙事；结果一次污染可影响多个查询，成功率最高达 98%。 |

## 检测与溯源

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse | detection、RAG poisoning、attention collapse、document detection | SIGIR 2026 | [arXiv](https://arxiv.org/abs/2608.06947) | 暂未公开 | 针对毒文档通过检索后仍缺少轻量检测信号，论文刻画生成时注意力向少数文档异常集中的坍缩现象；结果可在文档级识别和移除污染上下文，而无需额外事实知识库。 |
| 2026&#8209;06 | Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution | detection、RAG poisoning、token attribution、target tracing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25721) | 暂未公开 | 针对现有 RAG 投毒检测依赖额外分类器或 LLM 裁判，论文追踪多个检索文档中反复出现的高影响 token 和短语；结果既能识别毒文档，也能反推出攻击者试图植入的目标答案。 |
| 2024&#8209;11 | RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis | detection、RAG poisoning、activation analysis、response detection | Findings of EMNLP 2025 | [arXiv](https://arxiv.org/abs/2411.18948) | 暂未公开 | 针对只在检索前过滤仍可能漏掉攻击，论文从生成时内部激活学习干净与污染响应的差异；结果跨多个 RAG 架构达到约 98% 真阳性率并把假阳性率维持在约 1%。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | COMA: A Compositional Misleading Attack Class on Security-RAG, and a Causal Counterfactual Defense | defense、RAG poisoning、knowledge corruption、retrieval manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.17960) | 暂未公开 | 安全副驾所检索的每份文档都可能真实、不含指令且彼此不矛盾，但副驾仍可能先正确判断一个严重且可利用的漏洞，随后推荐一种无法修复该漏洞的措施；我们研究安全运营中心中面向分析人员的、由检索增强生成（RAG）支持的副驾所存在的这一失效，并识别出一类组合式误导攻击 COMA：每份对抗文档在事实层面都正确、不含指令、不矛盾且在分布上看似良性，但它们的组合会误导答案。 |
| 2026&#8209;08 | DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption | defense、adversarial robustness、VLM safety、data poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16536) | 暂未公开 | DSPrompt 在冻结 M-RAG retriever 的视觉与文本 encoder 各层插入不足 1% 参数的动态 soft prompt，并以在线攻击者做 min-max 训练；无需查询期优化即可在四项 benchmark、三种投毒下显著降低 ASR 与 poison retrieval，同时近乎保留检索和生成效用。 |
| 2026&#8209;05 | Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control | defense、RAG poisoning、information-flow control、isolation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.26754) | 暂未公开 | 针对模型会把不同可信度的检索证据无差别混入答案，论文以信息流标签约束恶意知识从文档到生成的传播；结果在保留良性 RAG 效用时降低污染内容对最终响应的控制。 |
| 2026&#8209;05 | RADAR: Defending RAG Dynamically against Retrieval Corruption | defense、GraphRAG poisoning、dynamic defense、graph energy | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/62567) · [arXiv](https://arxiv.org/abs/2605.22041) | [Code](https://github.com/Etherealllllll/RADAR_code) | 针对静态过滤无法适应持续变化的网络知识库，论文以图能量最小化分离可疑检索结果并用贝叶斯记忆积累风险；结果在动态污染下持续净化上下文而不需重训生成器。 |
| 2026 | Through the Stealth Lens: Attention-Aware Defenses Against Poisoning in RAG | defense、RAG poisoning、data poisoning、knowledge corruption | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61228) | 暂未公开 | 针对现有后门审计与防御难覆盖未知触发器和模型供应链变化的问题，论文提出 Through the Stealth Lens 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于模型供应链审计与后门防御。 |
| 2026 | Defense Against Knowledge Poisoning Attack on GraphRAG | defense、data poisoning、RAG poisoning、knowledge corruption | ACL 2026 | [Official](https://aclanthology.org/2026.acl-short.47/) | [Code](https://github.com/CyberScienceLab/HoG-GRAG) | 针对 GraphRAG 知识图中伪造实体与关系会污染多跳检索，HoG-GRAG 分解子问题、逐跳监测不一致并局部剪枝和补证，在多种数据集与配置上恢复大部分受损性能。 |

## 系统分析与防御边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval | analysis、RAG poisoning、coordinated poisoning、admission defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16044) | 暂未公开 | 针对入库时过滤异常文档被视为足以保护向量库，论文用一组单独正常的文档共同包围目标查询；结果十篇文档可几乎占满 top-k，且证明看不到真实查询需求的准入防御存在根本限制。 |
| 2026&#8209;06 | Influence Factors on RAG Poisoning | analysis、RAG poisoning、factorial study、system configuration | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.12469) | 暂未公开 | 针对 RAG 投毒结果常被单一组件解释，论文在 432 种配置中联合改变语料、检索器、深度、分块、数据库和生成器；结果表明风险来自组件交互，检索架构和深度决定暴露、生成器决定最终成功。 |
| 2026&#8209;06 | When Poison Fails After Retrieval: Revisiting Corpus Poisoning under Chunking and Reranking Pipelines | analysis、RAG poisoning、chunking、reranking | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.11265) | 暂未公开 | 针对只在理想检索器上评估的投毒攻击难代表真实流水线，论文系统加入分块与重排环节重新测试；结果显示毒文档被初检索到并不等于能进入生成上下文，攻击需同时适配各阶段。 |
| 2025&#8209;06 | Through the Stealth Lens: Rethinking Attacks and Defenses in RAG | analysis、RAG poisoning、stealth、attention filtering | ICML 2026 | [arXiv](https://arxiv.org/abs/2506.04390) | [Code](https://github.com/sarthak-choudhary/Stealthy_Attacks_Against_RAG) | 针对现有毒段落必须比干净证据产生更强生成影响而留下异常信号，论文形式化隐蔽性并提出注意力方差过滤器；结果提高防御准确率，同时以自适应攻击揭示注意力检测的边界。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation | detection、data poisoning、RAG poisoning、knowledge corruption | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13010) | [Code](https://github.com/XrazyMee/RAGSieve) | RAGSieve 分别以 query-local 的排名 1–5 对 6–20 对比和 corpus-local 邻域密度识别单文档与协同投毒；两模块 AUROC 达 95.2% 与 93.3%，联合部署把 ASR 从 67.4% 降至 14.0%，无需可信语料或 poison label。 |

## 机制分析与风险测量

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring | analysis、RAG poisoning、knowledge corruption、retrieval manipulation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.20097) | [Code](https://github.com/1Vastsky/trustRAG) | 检索增强生成（RAG）使大语言模型（LLM）能够获取最新的领域特定信息，而非仅依赖训练时所学内容；我们提出 TrustRAG，一个基于委员会并由区块链支持的 RAG 系统：文档在使用前，先由领域专家委员会通过零知识协议进行认证；委员会的隐藏评分再通过安全多方计算合并为任何客户端都可验证的信任分数。 |
