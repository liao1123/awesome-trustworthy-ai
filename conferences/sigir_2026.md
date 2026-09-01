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

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| AdversarialCoT: Single-Document Retrieval Poisoning for LLM Reasoning | Hongru Song, Yu-An Liu, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Yixing Fan, Xueqi Cheng | [Official](https://doi.org/10.1145/3805712.3809838) · [arXiv](https://arxiv.org/abs/2604.12201) | 暂未公开 | attack、single-document poisoning、adversarial CoT、query-specific attack | 针对现有 RAG 投毒依赖多篇恶意文档且易被发现，AdversarialCoT 从目标模型抽取推理框架并迭代优化单篇 query-specific 恶意 CoT；实验显示仅污染一个检索文档即可显著破坏 LLM 推理准确率。 |
| Answer First, Evidence Second? Uncovering Hidden Risks in Well-Structured AI Search Summaries | Jinman Li, Xuanang Chen, Ruoxi Xu, Hongyu Lin, Yaojie Lu, Zecheng Fan, Xianpei Han, Le Sun | [Official](https://doi.org/10.1145/3805712.3809913) | [Code](https://github.com/icip-cas/AISummary) | analysis、AI search、citation consistency、evidence grounding | 针对结构清晰的 AI 搜索摘要可能制造“已有证据”的错觉，论文审计 Google Search 的 14,175 个 MS MARCO 查询；32.31% 摘要含错误、31.08% 存在引用不一致，且超过半数错误在引用来源已有支持证据时仍然发生。 |
| Deletion Isn't Enough: Auditing RAG for Selective Forgetting | Leila Tavakoli, Mark Sanderson | [Official](https://doi.org/10.1145/3805712.3808545) | 暂未公开 | audit、RAG revocation、selective forgetting、disclosure probe | 针对删除记录或撤销访问后 RAG 仍可能披露被撤销事实，论文提出机制无关的 Forgetting-by-Design 成对前后探针，分别审计 retrieval／citation exposure 与 answer-level disclosure；结果表明检索暴露被抑制后答案泄漏仍可持续，缓解还可能损伤合法效用。 |
| Policy-Guided RAG: A Governance Framework for Controlled Information Use in Large Language Models | Mina Naghash Asadi, Leila Tavakoli, Mustafa Bilgrami | [Official](https://doi.org/10.1145/3805712.3808490) | 暂未公开 | framework、RAG governance、policy enforcement、auditable generation | 该框架在检索与生成之间执行可审计的信息使用政策，区分逐字引用、证据组合和综合回答，以约束受监管场景中的隐私与合规风险。 |
| Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems | Yuchuan Zhao, Tong Chen, Junliang Yu, Zongwei Wang, Lizhen Cui, Hongzhi Yin | [Official](https://doi.org/10.1145/3805712.3809691) · [arXiv](https://arxiv.org/abs/2604.23640) | 暂未公开 | attack、LLM recommender、black-box promotion、proxy prompt | 针对 victim prompt 与模型均未知的黑盒顺序推荐，PUDA 进化 proxy prompt、训练 surrogate，并在语义约束下编辑目标商品文本、补充合理交互序列；真实数据集上可把冷门目标商品显著推高。 |
| PurifAI: Detecting and Fixing Search-Induced Distortions in Web-Augmented LLMs | Guoqing Wang, Zhao Zhang, Zeyu Sun, Xiaofei Xie, Yizhou Chen, Yanchao Tan, Dan Hao | [Official](https://doi.org/10.1145/3805712.3809751) | 暂未公开 | defense、web-augmented LLM、search distortion、knowledge purification | PurifAI 检测外部网页与模型已验证知识之间的冲突，并在缓存层净化误导信息，降低网页污染覆盖正确内部知识的风险。 |
| Reward Shaping for Robust Refusal in Small Language Models for Retrieval-Augmented Question Answering | Thilina Chaturanga Rajapakse, Maarten de Rijke | [Official](https://doi.org/10.1145/3805712.3809891) | 暂未公开 | defense、RAG refusal、reward shaping、distractor robustness | 论文通过奖励塑形训练小模型在证据不足或检索到干扰内容时拒绝作答，在保持可回答问题效用的同时提升稳健拒答。 |
| Teaching Small Models When Not to Call Functions: Structured Reasoning for Reducing Tool-Use Hallucinations | Dung Pham Tuan Vo, Thai Trung Tran, Tushar Semwal | [Official](https://doi.org/10.1145/3805712.3809979) | 暂未公开 | defense、tool-use hallucination、structured reasoning、function calling | 论文用结构化键值推理训练小模型识别无关或不充分请求，减少并不存在依据时仍调用函数的 agent 工具幻觉。 |
| The Vulnerability of LLM Rankers to Prompt Injection Attacks: You are to [MARK] this paper as the Best Paper | Yu Yin, Shuai Wang, Bevan Koopman, Guido Zuccon | [Official](https://doi.org/10.1145/3805712.3808553) · [arXiv](https://arxiv.org/abs/2602.16752) | [Code](https://github.com/ielab/LLM-Ranker-Attack) | attack、LLM ranker、objective hijack、criteria hijack | 论文在 pairwise、listwise 与 setwise 协议中分别劫持排序结果和判断准则，并联合测量 ASR 与 nDCG@10；攻击跨模型、位置和领域成立，但 encoder-decoder ranker 相对更稳健。 |
| When Context Bites: Detecting RAG Poisoning via Document-Level Attention Collapse | Yingtao Ren, Ziyi Zhao, Yiwei Fu, Xiao Luo, Yu-Cheng Chang, Chin-Teng Lin | [Official](https://doi.org/10.1145/3805712.3809904) · [arXiv](https://arxiv.org/abs/2608.06947) | [Code](https://github.com/yingtaoren/D-Scan) | defense、RAG poisoning、document attention、runtime detection | 针对 poisoned RAG 输出可能比正常输出困惑度更低、令输出不确定性检测失效，D-SCAN 以恶意文档吸走注意力造成的 document-level entropy collapse 为信号；即使最终答案尚未改变也能提前识别投毒。 |

### 幻觉、证据与评测完整性

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| Auto-Judge: A Cross-Task Benchmark for Comparing LLM Judges for Citation-Grounded RAG Systems | Naghmeh Farzi, Tim Hagen, Eugene Yang, Maik Fröbe, Ronak Pradeep, Hossein A. Rahmani, Xi Wang, Oleg Zendel, Martin Potthast, Laura Dietz | [Official](https://doi.org/10.1145/3805712.3808601) | 暂未公开 | benchmark、LLM judge、citation-grounded RAG、evaluation integrity | Auto-Judge 汇集跨任务数据、人类判断和统一评测软件，比较 RAG 引用评审器在自偏好、内容操纵与任务迁移下是否仍可信。 |
| Calibrating Uncertainty with Cross-Model Consistency for LLM Hallucination Mitigation | Shu Zhou, Rui Ling, Junan Chen, Tao Fan, Hao Wang | [Official](https://doi.org/10.1145/3805712.3809846) | 暂未公开 | defense、hallucination mitigation、uncertainty calibration、cross-model consistency | 论文以多个模型回答的一致性校准单模型不确定性，用于识别并抑制缺少可靠依据却高置信输出的幻觉。 |
| CSMAD: Contradictory Statement Multi-Agent Debate for Factual Hallucination Detection | Swapnil Gupta, Akshay Verma, Khushi Gupta, Prateek Sircar, Deepak Gupta | [Official](https://doi.org/10.1145/3805712.3808508) | 暂未公开 | detection、factual hallucination、multi-agent debate、NLI verification | CSMAD 让多个 agent 围绕相互矛盾的陈述辩论，再由自然语言推断验证器裁决，以较低推理成本增强生产环境中的事实幻觉检测。 |
| Fast and Faithful: Efficient Full-Context Verification for Long-Form LLM Responses | Xunzhuo Liu, Bowei He, Xue Liu, Haichen Zhang, Huamin Chen | [Official](https://doi.org/10.1145/3805712.3808493) · [arXiv](https://arxiv.org/abs/2603.23508) | [Project](https://huggingface.co/llm-semantic-router) | defense、long-form verification、full-context reasoning、semantic routing | 论文对长回答进行最高 32K 上下文的整体事实核验，并通过语义路由降低逐句验证的成本与跨句证据遗漏。 |
| Numerical Hallucinations in RAG: Detection and Analysis | Sera Singha Roy | [Official](https://doi.org/10.1145/3805712.3809882) | 暂未公开 | analysis、numerical hallucination、RAG、quantitative fidelity | 论文专门分析 RAG 回答中的数字失真并构建检测方法，区分检索证据正确但模型复制、组合或推算数值出错的失效。 |
| SurGE: A Benchmark and Evaluation Framework for Scientific Survey Generation | Weihang Su, Anzhe Xie, Qingyao Ai, Jianming Long, Xuanyi Chen, Jiaxin Mao, Ziyi Ye, Yiqun Liu | [Official](https://doi.org/10.1145/3805712.3808598) · [arXiv](https://arxiv.org/abs/2508.15658) | [Code](https://github.com/oneal2000/SurGE) | benchmark、scientific survey、citation integrity、evidence coverage | SurGE 以可追溯证据、引用正确性和覆盖度评测自动科学综述，暴露仅凭文本流畅度会漏掉的研究代理可靠性问题。 |
| The LLM Effect on IR Benchmarks: A Meta-Analysis of Effectiveness, Baselines, and Contamination | Moritz Staudinger, Wojciech Kusa, Allan Hanbury | [Official](https://doi.org/10.1145/3805712.3809901) | 暂未公开 | analysis、benchmark contamination、LLM evaluation、evidence synthesis | 论文汇总 LLM 用于 IR 的公开实验，检查增益是否受基线选择与训练数据污染影响，为解读看似显著的检索改进提供完整性审计。 |

### 内容真实性、事实核查与内容治理

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| A Dataset of Cultural Heritage Manipulation on English Wikipedia in the Russo-Ukrainian Context | Maxime Garambois, Hamest Tamrazyan, Emanuela Boros | [Official](https://doi.org/10.1145/3805712.3808580) | 暂未公开 | dataset、information manipulation、Wikipedia、cultural heritage | 该数据集标注俄乌语境下英文维基百科文化遗产叙事的操纵模式，为检测协同编辑和历史叙事篡改提供可复核样本。 |
| Decoding Multimodal Cues: Unveiling the Implicit Meaning Behind Hateful Videos | Junyu Lu, Deyi Ji, Liqun Liu, Xiaokun Zhang, Youlin Wu, Roy Ka-Wei Lee, Peng Shu, Huan Yu, Jie Jiang, Bo Xu, Liang Yang, Hongfei Lin | [Official](https://doi.org/10.1145/3805712.3809637) · [arXiv](https://arxiv.org/abs/2606.11953) | [Code](https://github.com/DUT-lujunyu/IARE) | detection、hateful video、evidence rationale、multimodal reasoning | 针对仇恨视频常把危害拆散在画面、语音和文字中而缺少可解释证据，论文构建 Ex-HateMM／Ex-ImpliHateVid 并提出 IARE，以 multimodal CoT 增强证据、再用 DPO 优化推理；结果同时提升隐性仇恨识别与细粒度 rationale 质量。 |
| Deja Vu in Plots: Leveraging Cross-Session Evidence with Retrieval-Augmented LLMs for Live Streaming Risk Assessment | Yiran Qiao, Xiang Ao, Jing Chen, Yang Liu, Qiwei Zhong, Qing He | [Official](https://doi.org/10.1145/3805712.3809737) · [arXiv](https://arxiv.org/abs/2601.16027) | 暂未公开 | detection、livestream risk、cross-session retrieval、production moderation | 论文检索跨直播场次重复出现的欺诈或恶意剧情，由 LLM 提炼证据指导小模型审核，以识别单场片段难以判断的持续性风险。 |
| EVADE-Bench: Multimodal Benchmark for Evaluating and Enhancing Evasive Content Detection | Ancheng Xu, Zhihao Yang, Jingpeng Li, Guanghu Yuan, Longze Chen, Liang Yan, Jiehui Zhou, Zhen Qin, Hengyu Chang, Yukun Chen, Hamid Alinejad-Rokny, Min Yang | [Official](https://doi.org/10.1145/3805712.3808579) · [arXiv](https://arxiv.org/abs/2505.17654) | [Code / Data](https://github.com/koenshen/EVADE-Bench) · [Dataset](https://huggingface.co/datasets/koenshen/EVADE-Bench) | benchmark、e-commerce moderation、evasive content、multimodal decomposition | 针对电商违规内容以拆词、委婉语和图像裁剪规避审核，EVADE-Bench 提供 2,833 条文本、13,961 张图像及六类违规，并评测 26 个 LLM／VLM；现有模型普遍失效，而明确规则和视觉描述—逻辑推理的多 Agent 分解能改善检测。 |
| ExDR: Explanation-driven Dynamic Retrieval Enhancement for Multimodal Fake News Detection | Guoxuan Ding, Yuqing Li, Ziyan Zhou, Zheng Lin, Daren Zha, Jiangnan Li | [Official](https://doi.org/10.1145/3805712.3809648) · [arXiv](https://arxiv.org/abs/2601.15820) | 暂未公开 | detection、multimodal fake news、dynamic retrieval、explanation feedback | ExDR 根据当前解释中暴露的证据缺口动态追加检索，使多模态假新闻判断不再受一次性、可能不充分的外部证据限制。 |
| JARVIS: A Joint Framework for Multimodal Risk Classification and Retrieval in E-Commerce | Nan Lu, Leyang Li, Yurong Hu, Rui Lin, Shaoyi Xu | [Official](https://doi.org/10.1145/3805712.3808429) · [arXiv](https://arxiv.org/abs/2602.12941) | 暂未公开 | detection、e-commerce risk、multimodal retrieval、production moderation | JARVIS 联合训练风险分类与相似案例检索，在电商生产审核中用可复用证据提高对新型违规商品的召回并减少人工复核。 |
| Mitigating Adversarial Attacks by Transferring LLM-generated Narrative Reasoning for Robust Fake News Detection | Mengyang Chen, Lingwei Wei, Wei Zhou, Songlin Hu | [Official](https://doi.org/10.1145/3805712.3809585) | 暂未公开 | defense、fake news、adversarial attack、reasoning transfer | 论文把 LLM 生成的叙事推理蒸馏给检测器，使其利用事件逻辑而非脆弱表面词汇判断新闻真伪，从而抵抗对抗改写。 |
| Multi-Sourced, Multi-Agent Evidence Retrieval for Fact-Checking | Shuzhi Gong, Richard O. Sinnott, Jianzhong Qi, Cécile Paris, Preslav Nakov, Zhuohan Xie | [Official](https://doi.org/10.1145/3805712.3809686) · [arXiv](https://arxiv.org/abs/2603.00267) | 暂未公开 | defense、fact-checking、multi-agent retrieval、source diversity | 论文让多个检索 agent 分别从异构来源搜集并交叉核对证据，降低单一搜索源偏差或缺失导致的事实核查误判。 |
| R 3 Check: Reinforcement Learning for Iterative Retrieval and Structured Reasoning in Complex Fact Checking | Peng Qi, Yuyang Zhao, Wynne Hsu, Mong-Li Lee | [Official](https://doi.org/10.1145/3805712.3809601) | 暂未公开 | defense、fact-checking、iterative retrieval、reinforcement learning | R3Check 用强化学习协调多轮检索与结构化推理，在复杂主张证据不足时继续补证而不是过早给出真假结论。 |
| Resources for Automated Evaluation of Assistive RAG Systems that Help Readers with News Trustworthiness Assessment | Dake Zhang, Mark D. Smucker, Charles L. A. Clarke | [Official](https://doi.org/10.1145/3805712.3808624) · [arXiv](https://arxiv.org/abs/2602.24277) | [Code](https://github.com/trec-dragun/resources) | resource、news trustworthiness、assistive RAG、automated evaluation | 论文提供人类判断、自动评审器和复现实验资源，用于检验辅助读者判断新闻可信度的 RAG 是否真正给出相关且有依据的证据。 |
| Retrieval-Augmented Multimodal Model for Fake News Detection | Yiheng Li, Weihai Lu, Hanyi Yu, Yue Wang | [Official](https://doi.org/10.1145/3805712.3809605) · [arXiv](https://arxiv.org/abs/2604.18112) | [Code](https://github.com/li-yiheng/RAMM) | detection、multimodal fake news、retrieval augmentation、external evidence | RAMM 为图文新闻检索外部跨模态证据并联合推理，减少仅凭帖子自身内容导致的真假判断偏差。 |
| SciCheck: Reasoning Distillation for Biomedical Claim Verification | Gabriel Pereira, Luciano Barbosa | [Official](https://doi.org/10.1145/3805712.3809699) | 暂未公开 | detection、biomedical claims、reasoning distillation、scientific evidence | SciCheck 将大模型基于科学证据的核查推理蒸馏到较小模型，以提升生物医学主张验证的可部署性和证据一致性。 |
| Simulating the Lateral Reader: A Baseline for Source-Aware Web Credibility Assessment | Dake Zhang, Mark D. Smucker | [Official](https://doi.org/10.1145/3805712.3809973) · [Paper](http://zhangdake.tech/assets/pdf/sigir2026baseline.pdf) | 暂未公开 | baseline、web credibility、lateral reading、source awareness | 论文模拟专业核查者的横向阅读流程，让系统跳出当前网页调查来源与外部声誉，作为抗网页自我包装的可信度评估基线。 |

### 高风险推荐安全

| Title | 作者 | 论文链接 / arXiv 链接 | 代码链接 | 关键词 | 一句话总结 |
| --- | --- | --- | --- | --- | --- |
| RES-MR: Risk-Aware Reasoning for Explainable and Safe Medication Recommendation | Cong Wang, Jin Li, Shoujin Wang, Yishuo Li, Huilin Gu, Wenpeng Lu | [Official](https://doi.org/10.1145/3805712.3809604) | 暂未公开 | defense、medication recommendation、risk-aware reasoning、clinical safety | RES-MR 在药物推荐推理中显式建模禁忌与相互作用风险，并提供可检查解释，使准确率优化受临床安全约束。 |

## 核验记录

- 核验日期：2026-08-30。
- 录用状态：以 [SIGIR 2026 Accepted Papers](https://sigir2026.org/en-AU/pages/program/accepted-papers) 的完整主会列表证明录用，并以正式 proceedings DOI 补齐作者与论文链接；官网明确报告八类主会论文合计 656 篇。
- 范围复算：Full 234 + Perspective 12 + Reproducibility 28 + Resource 61 + Short 151 + Demo 24 + Industry 131 + Low Resource Environment 15 = 656；另列的 12 篇 Doctoral Colloquium 已排除。
- 逐篇核验：已对 104 个宽筛候选逐篇检查公开摘要或正文；最终 32 篇的官方英文标题、作者顺序、track、DOI、补充链接、分类与一句话总结均完成复核。
- 唯一归属：四个分表依次收录 10、7、13、1 篇，共 31 篇；标题无重复，每个分表均按英文标题字母序排列。
- 链接与代码：官方 DOI 全部可定位到 SIGIR 2026 proceedings；代码只记录论文或作者可回证的公开入口，未找到者不以同名第三方仓库代替。
- 领域同步：按当前研究兴趣从 32 篇中精选 13 篇；复用并更新既有 4 条，新增 9 条，19 篇保留在会议来源视图中而未同步；默认主归属重复数为 0。
- 本页为会议录用论文的独立 AI Safety 筛选结果；完成本页核验后，才按仓库研究兴趣和去重规则选择条目同步到 `domains/`。
- 未决项：部分论文尚未公开 arXiv 或代码；这不影响其正式录用身份与本页收录结论。
