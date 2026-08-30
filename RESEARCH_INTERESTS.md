# AI Safety 研究兴趣范围

> 状态：当前生效。本文档记录已经明确表达的兴趣取舍，是 `daily/` 收录、会议论文向 `domains/` 同步以及现有领域内容审查的首要边界。

## 总体判断标准

关注能够说明具体安全问题的研究，而不是只带有 `safety`、`trustworthy`、`responsible`、`robust`、`reliability` 或 `ethics` 标签的泛主题。

一篇论文通常应当明确回答以下问题中的大部分，才进入收录范围：

1. **保护对象是什么：** 模型能力、权重、训练数据、用户隐私、系统提示、Agent 权限、工具链、外部环境、内容真实性或人身与社会安全等。
2. **风险来自哪里：** 攻击者、恶意输入、数据或供应链投毒、模型错位、自主行为、监督失效、系统组合故障或安全关键的不确定性。
3. **安全后果是什么：** 机密性、完整性或可用性受损，安全策略被绕过，产生有害行为、欺骗、失控、隐私泄漏、资源耗尽、物理伤害或高后果滥用。
4. **论文做了什么：** 建立 threat model、攻击或失效机制，提出检测、监控、防御、评测、审计、约束或安全保证。

仅仅提升准确率、效率、可解释性、用户体验、一般可靠性或社会价值，不足以构成收录理由。

## 手动精选与优先排序偏好

`daily/` 与 `domains/` 承担不同角色：

- `daily/` 是符合兴趣边界的当日论文候选集，仍应尽量完整收集，不因一篇论文没有被手动精选就删除。
- `domains/` 是用户每天从日报中进一步挑选的重要论文集合，不是日报的完整镜像。只有用户明确点名、明确要求归类，或明确指定需要同步的论文才进入 `domains/`；不得默认把每日全部论文批量归类。
- 用户明确要求归类的论文是强正向偏好样例，说明该论文的主题、技术深度或实证方式具有较高优先级。未被点名只表示尚未精选，不等于论文不符合总体兴趣。
- 对这些手动精选论文采用多领域覆盖优先：先确定主领域，再检查全部实质相关领域；只要论文在研究对象、方法、训练机制、评测或安全结论上对某领域有明确贡献，就应交叉收录，不要求各领域贡献彼此完全独立。每个领域必须使用针对该页面的关键词和总结，不能只因标题或摘要出现相关词而机械复制。
- 后续用户继续逐日精选时，以新增领域条目作为持续更新的正向信号；若新选择体现出稳定的新方向，再更新本节的主题概括。

### 手动精选论文驱动的当前优先级

以下画像根据截至 2026-08-29 用户明确要求“收录”或“归类”的论文归纳。`domains/` 中这些手动精选条目共同构成完整的强正向样例集；下文论文名只是便于理解偏好的代表锚点，未在此重复列名的已归类论文不得因此降级。后续检索优先寻找与这些样例在研究对象、threat model、机制深度、系统干预和评测方式上相近的新工作，而不是把论文名当成封闭白名单。

#### 偏好信号强度

1. 用户明确表示“不喜欢／不关注／删除”的方向是硬排除，优先级高于标题关键词、领域标签和正向相似性。
2. 用户明确要求“收录／归类”的论文是最强正向信号；不仅记录论文主题，还要学习其攻击面、机制设计、证据形式和评测标准。
3. 用户要求同时归入多个 `domains/` 的论文通常是高价值、跨领域样例。后续遇到同时命中多个正向主题的论文，应提高日报排序并检查所有实质相关领域。
4. 只进入 `daily/`、但没有被用户进一步点名的论文是中性候选，不自动视为负样例，也不自动进入 `domains/`。

#### 优先主题与手动精选锚点

1. **Agent safeguard、指令权限与运行时强制执行。** 代表锚点包括 *StepGuard*、*RePolicy*、*AgentFlow*、*PolicyGuide*、*SafeBranch*、*ReguSim*、*What Guides the Agent?*、*HANSARD*、*When “Do Not” Is Not Deny*、*Think Only When Needed*、*Reassembling Distributed Risk*、*SkillShield*、*HRGuard*、*ClawSentry*、*TraceGrant* 和 *Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents*。重点关注 pre-execution／step-level guard、跨轮分布式风险重组、trajectory-conditioned action generation、有状态累积风险、持久 workflow graph、遗漏步骤检测、规则陈述与实际执行的分离、角色敏感 policy、policy invocation、behavior-guiding instruction 定位、prompt authority、按可信度与推理能力分级的不可信 evidence access、信息流与污点跟踪、reference monitor，以及 prompt-space 软规则和 deny／permission／sandbox 等硬控制之间的执行缺口；同时优先覆盖从 skill admission、运行时 evidence 到实际外部 effect 与完成验证的全生命周期闭环。
2. **Agent 注入、memory／skill／tool 持久攻击与资源滥用。** 代表锚点包括 *SecOPD*、*SkillBloat*、*InjecMEM*、*MEMORY Wins All*、*EVOMAL*、*MaliciousSkillBench*、*Forgotten in Weights, Recovered by Tools*、*ClawSentry* 和 *TraceGrant*。重点关注 indirect prompt injection、跨 session memory injection、skill／tool supply chain、Agent 自编 skill 的模仿投毒与谱系持久传播、token／cost amplification，以及工具重新引入已删除能力的 system-level 绕过；skill detector 评测优先使用 source-disjoint split，并同时报告恶意召回和良性误报；对防御优先考察跨表述、跨工具和跨轮重试的 anti-bypass，以及不可信证据能否被阻止扩张用户授权。
3. **Guardrail、越狱防御与安全对齐。** 代表锚点包括 *Granite.Trust Policy Tools*、*NeuronGuard*、*RAGSentinel*、*LMSM*、*CLEAR*、*VSysBench*、*Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics*、*COPA*、*TempJail*、*SkillShield*、*HRGuard*、*A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks*、*Beyond Over-Refusal*、*Breaking the Assumptions*、*PsychJail*、*Hidden in the Request*、*BanglaVeilGuard*、*Latent Space Refusal Anchoring for Low-Resource African Languages*、*Abliteration Mitigation via Refusal Aliases*、*Fool's Gold*、*Are LLMs Safe Beyond Text* 和 *When Safety Overrides Vision*。重点关注可执行策略、system-message conflict 与多模态 instruction hierarchy、prompt-response 动态而非孤立输入输出、continual defense 与历史安全边界保持、视频字幕的时间调度攻击、security backend／versioned policy／output gate 的职责分离、可解释性安全信号到运行时 enforcement 的转化、按输入风险连续路由 safety adapter 的条件式对齐、从成功攻击归纳并跨交互保存 method-level rule 的持续适应，以及跨语言 refusal 激活、输入表示变化、refusal safeguard 耐消融、多模态 grounded answer 被安全机制覆盖时的 safety、utility、over-refusal、latency 与 throughput 联合评测。
4. **Reasoning safety、可监控性、评测意识与奖励作弊。** 代表锚点包括 *TRACE*、*EchoCoT*、*ReguSim*、*Evaluation Awareness in Language Models*、*Measuring Activation Control*、*Curved Inference II: Sleeper Agent Geometry*、*Training Alignment Auditors via Reinforcement Learning*、*Hack-Verifiable Terminal Bench*、*Safety Hacking in Constrained Best-of-N*、*Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty* 和 *Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents*。重点关注 trace-level 风险证据、隐藏 CoT 的可见性与 API replay 泄漏、自然语言 rationale 与真实 action／enforcement evidence 的分离、evaluation awareness 的表示与控制、内部激活可控性、识别错误证据与实际摆脱其下游影响之间的差距、隐藏行为的自动化审计、auditor reward design、跨 scaffold 调查能力、假阳性控制、verifier／proxy gaming，以及推理扩展导致的不安全尾部放大；reasoning capability 的经验优势不能直接替代形式安全保证。
5. **Unlearning、能力删除与删除后的隐私泄漏。** 代表锚点包括 *ConceptGuard*、*Can Scientific Claims Be Removed from Large Language Models?*、*Can LLMs Truly Forget?*、*Stress Testing Unlearning Algorithms*、*BLADE*、*Unlearning Is Not Just Erasing*、*ST²U*、*Forgotten in Weights, Recovered by Tools*、*Distance Is Not Enough*、*Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data*、*Inadvertent Context Leakage in Language Models* 和 *DIME*。重点区分真实删除与表面抑制，并检查 dual-use concept 的有害／良性意图分离、adversarial re-elicitation、relearning、邻近良性问题、工具恢复、连续删除、utility retention、上下文秘密经良性输出形成的隐蔽信道和低查询黑盒泄漏；判断 relearning robustness 时优先考察更新是否命中 forget-critical 且避开 retain-critical 权重，不把随机破坏造成的全局 weight distance 当成稳健删除。
6. **投毒、后门、RAG 与 Agent memory 完整性。** 代表锚点包括 *RAGSentinel*、*Retrieved But Not Reliable*、*ReliableRAG*、*Trustworthy RAG*、*Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents*、*Vis-Poison*、*Beyond the Editing Canvas*、*Not All Tokens Are Equal*、*Anchoring Bias*、*MEMORY Wins All*、*InjecMEM*、*Capacity Overflow*、*DEFUSE*、*Backdoor Learning in Language Models and Vision-Language Models* 和 *Mitigating Database Leakage in RAG Systems with Keyword-Grounded Fact Substitution*。重点关注 corpus、document ingestion、retriever、reranker 与 generator 的 pipeline-aware threat model，可证明／可验证 RAG 防御，NLI／一致性／投毒概率联合形成的生成前 Trust Index，source／retrieval／reasoning 的 reliability-guided evidence control，以及在完全隔离开销较高时按 reasoning capability 门控不可信文档访问并单独测量 detection–influence gap；同时关注视觉证据自身在不修改 caption 或 metadata 时形成的多模态知识载荷，viewer–parser evidence fork，语言模型与 VLM 后门的跨模型攻击—检测体系、模型级后门修复、持久 fairness backdoor、外部信息源到 memory 的污染链，以及检索数据库泄漏的针对性缓解；还关注利用 audit/deployment batch 与 MoE capacity 差异隐藏的 dormant backdoor，以及降低干净同分布数据、伪标签和攻击先验依赖的跨范式 encoder 后门检测。
7. **模型、服务和 System Prompt 资产保护。** 代表锚点包括 *EchoCoT*、*AdaptPrint*、*Do System Prompts Leave Behavioral Fingerprints?* 和 *Uncovering and Understanding Hidden Dependencies in the LLM API Reseller Ecosystem via Prefix-Cache Side Channels*。继续优先模型指纹、水印、所有权验证、clone detection、隐藏 reasoning trace 的黑盒 API 抽取、system prompt 提取后的行为相似性审计、适应采样配置和服务端防御变化的 response-adaptive black-box probing，以及利用软件可见 cache side channel 还原 API reseller 的隐藏上游、路由依赖和服务谱系。
8. **Deep Research、多 Agent 证据完整性与责任归因。** 代表锚点包括 *Who is the Agent to Blame?*、*HANSARD*、*Aligned Alone, Misaligned Together* 和 *Agentic Scaffolding Amplifies Sycophantic Behavior*。重点关注 citation／faithfulness 错误的 Agent 级定位、运行时 witnessing 与因果重放、monitor population capture，以及 scaffold 和反馈循环对错位行为的放大。
9. **Agent 驱动的网络安全能力与 Coding Agent 供应链。** 代表锚点包括 *CyberFactory*、*FuzzingBrain-Bench V1* 和 *Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code*。这是近期提高优先级的方向：关注真实 CVE、源码审计、开放式 bug discovery、PoC、修补、CyberQA，以及由 Docker、sanitizer、crash signature 和工具轨迹支撑的可执行证据；同时关注 package hallucination／slopsquatting 的 registry grounding、自验证和运行时阻断。传统 phishing、传统异常检测等排除项不因此恢复收录。
10. **具身 Agent、VLA、VLM 与视觉 World Model 的显式安全风险。** 代表锚点包括 *SafeBranch*、*ReFrame*、*CIVA*、*CertVLA*、*GuardianBench*、*RiskWorld*、*Where World Models Break*、*Think Only When Needed*、*Text-Anchored Semantic Perturbations*、*EviSafe* 和 *Breaking the weakest link to evade vision language models*。重点关注攻击驱动的闭环决策失效、interactive safety、safety-critical step 定位与 branch-pair credit assignment、latent contextual risk、object-level hazard localization、罕见灾难 failure discovery、控制输入 authority，以及把 physical patch／texture threat model 从单步标签扩展到连续 action 和完整 rollout 的可证明认证；对于 VLM 输入攻击，还关注只优化视觉编码器即可低成本破坏或定向劫持语义解释的可迁移威胁，同时使用证据和 counterfactual 检查模型是否因正确理由表现安全。
11. **可部署内容审核、跨语言安全与安全成本。** 代表锚点包括 *Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics*、*A Reproducible, License-Aware Distillation Recipe for CPU-Deployable Safety Classification*、*No One Model Catches Every Harm*、*BanglaVeilGuard*、*Redteaming Leading Arabic LLMs with ASAS*、*SPAR-Hate*、*Whitewashing Hate, Smearing Harmless Content*、*Register Shifts Break LLM Safety*、*Who Pays More for Safety?*、*Safety Alignment Illusion*、*Latent Space Refusal Anchoring for Low-Resource African Languages* 和 *Are LLMs Safe Beyond Text*。重点关注黑盒 prompt-response interaction classifier、轻量部署、moderator 场景盲点、自然语体／权威框架／标注员风格攻击、跨语言不均衡、从英语安全方向向低资源语言迁移时的几何失配，以及 emoji、混合文字或语体变化造成的表示敏感性和人工—自动 judge 差异。
12. **生成内容安全、真实性与跨生成器检测。** 代表锚点包括 *GuardPaint*、*DiSCO* 和 *DF-MoE*。重点关注生成过程内的 policy-compliant decoding、局部安全修复，以及专有 T2I 外部无需访问权重、可利用 safe／unsafe image pool 与目标反馈修复 benign-adversarial prompt 的黑盒 guardrail；同时关注融合多种音视频高层证据、能够跨数据集和未知生成器泛化的 deepfake 检测，单纯人类感知实验仍不收录。
13. **有技术干预的风险沟通与 Human-AI oversight。** 代表锚点包括 *Ask or Answer* 和 *AI Watchdog*。只优先具有明确系统机制、决策策略、独立检测器、即时告警或可测行为结果的工作，不扩展到一般用户体验、接受度或纯感知研究。
14. **Emergent misalignment、subliminal learning 的威胁校准与训练机制。** 代表锚点包括 *On the Threat Model of Weird Generalization and Emergent Misalignment*、*Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty*、*Evaluation Awareness in Language Models*、*Reinforcement Learning on Benign Facts Amplifies Leakage of Memorized Private Data* 和 *Stored in Optimizer State, Valued by Later Training*。重点区分普通微调副作用与攻击者精心构造数据的风险，检查数据组成、语言、预训练熟悉度、评测敏感性、安全表征漂移和保持 reasoning utility 的训练干预；对潜意识特征迁移还关注完整 trainer state、optimizer first moment 等隐藏载体，以及后续训练如何为同一源扰动赋予不同的行为符号。
15. **模型 DoS、Denial-of-Wallet 与可用性攻击。** 代表锚点包括 *Groundhog Bit-Flip Attack*、*SkillBloat* 和 *SMTrap*。重点关注 EOS 抑制、无限生成循环、MoE routing／expert activation 的结构性扰动，以及用 SMT conflict 等低成本外部信号合成高回溯问题、放大 reasoning search、token、成本和延迟；归类时按实际受攻击层区分普通模型生成、推理模型搜索、Agent workflow、共享服务与具身控制，不因论文只在 reasoning 或 agentic 模式评测就机械归入相应系统层。
16. **安全可解释性、因子化评测与 Refusal 耐篡改。** 代表锚点包括 *VSysBench*、*ArmorOCR*、*Refusal geometry reflects refusal training*、*Does Fine-Tuning Undo Activation Steering?*、*MMJailBench*、*NeuronGuard*、*Measuring Activation Control*、*Hidden in the Request*、*Curved Inference II: Sleeper Agent Geometry*、*Latent Space Refusal Anchoring for Low-Resource African Languages*、*Abliteration Mitigation via Refusal Aliases*、*Fool's Gold* 和 *When Safety Overrides Vision*。重点关注安全表示的训练来源与因果作用、gradient／activation geometry、stable rank、跨语言 refusal direction 与 SAE feature、writer／reader 对 refusal alias 的配合、跨模态 system-message constraint、视觉证据保留但 late-stage decoding 转向拒答、区域级 adversarial OCR 定位与识别分解、受控因素归因，以及“可读取信号”“参数编辑仍存在”和“该信号仍在因果控制行为”之间的区别；解释结果应直接服务于 jailbreak、隐藏行为、refusal-vector ablation、下游微调后的功能复验或其他明确安全 threat model，而不是一般可解释性展示。
17. **Sycophancy 缓解、心理安全 Judge 与 AI Companion 关系性风险。** 代表锚点包括 *Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach*、*aipsy-judge*、*CompanionHarm* 和 *When Vocabulary Comprehension Fails Clinical Reasoning*。重点关注 incentive-compatible、label-free truthful-reporting reward，通用 judge 的 self-preference、宽松偏差与 tail blindness，心理学家校正的本地安全评估，以及真实多轮 companion／therapy context 中的 crisis、severity、关系边界、青少年语体导致的理解—风险校准缺口与 annotator disagreement；只做一般陪伴体验或用户满意度研究仍不收录。
18. **有明确群体危害、可审计指标或技术干预的 Fairness。** 代表锚点包括 *Anchoring Bias*、*Who Pays More for Safety?*、*Safety Alignment Illusion*、*Latent Space Refusal Anchoring for Low-Resource African Languages*、*When Personalization Becomes Bias*、*GGSS* 和 *Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe*。重点关注定向群体伤害、alignment cost disparity、低资源语言用户获得不一致安全保护、宗教等身份线索在金融建议中通过 personalization 形成的结构与话语偏差、文化标记群体的隐私泄漏差异、可审计的 demographic bias，以及在生成式 VLM 或 LLM 内部表示上直接实施且同时验证 utility retention 的 inference-time intervention；严谨的 no-detection 结果可以收录，但必须明确统计功效、metric contamination、资源混杂和“未检出不等于不存在效应”的结论边界。
19. **跨维度 Safety、Security 与 Privacy 联合评测。** 代表锚点是 *aiXamine*。重点关注在同一模型、服务和运行条件下同时测量保护能力、良性效用、over-refusal、隐私与对抗鲁棒性，并诊断单轴改进造成的跨轴退化；优先可复现黑盒流水线、分层风险画像和能定位 alignment tax、privacy orthogonality 或 distillation-induced robustness collapse 的大规模研究。
20. **Embedding inversion 与自适应隐私攻击。** 代表锚点是 *Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings*。重点关注攻击者显式适应噪声、扰动、未知 encoder 或跨模型差异后能否恢复原始文本和敏感语义，优先具有明确观测权限、重建指标、攻击前置条件和防御失效边界的工作；一般 DP、密码学、secure inference、FL 或只报告抽象 privacy–utility trade-off 的方案仍不因此纳入。
21. **公开基础编码器到私有下游模型的迁移攻击。** 代表锚点是 *SW-ProxyCE: Zero-Query Adversarial Transfer from Public EEG Encoders to Private Downstream Models*。重点关注攻击者只访问公开 encoder、少量任务匹配样本或共享表示，完全不查询私有 victim 时如何恢复 task-level decision geometry 并实现跨 probe、full fine-tuning、被试或模型的迁移；该偏好针对明确的 public-component／private-downstream threat model，不扩展到一般 EEG 建模、普通生物信号准确率或无攻击者的鲁棒性研究。
22. **Safety benchmark validity、SLM 迁移与能力—安全混淆。** 代表锚点是 *Benchmarking the Benchmarks: Evaluating Automated Safety Benchmarks for Small Language Models*。重点关注为大模型设计的自动 safety／security／compliance pipeline 能否迁移到小模型，尤其是 ambiguous／irrelevant response 的处理、提示复杂度与架构对判断的影响、排行榜对计分规则的脆弱性，以及把能力不足误计为安全的系统性混淆；优先报告原始输出、判决分布与合理评分变体，不把单一聚合均分当作独立安全证据。
23. **开放权重 safety-removal 后的 defensive deception。** 代表锚点是 *Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models*，并标为特别关注。重点关注无法持久阻止 refusal stripping 或参数级 safeguard removal 时，能否通过只在 attacked state 激活的 decoy、trap 或 capability degradation 破坏攻击收益；评测需同时覆盖 clean-state utility、攻击状态特异性、独立 ground truth、重复采样与 consensus recovery、自适应 weight editor，以及防线只保护初始发布权重、不覆盖 in-context jailbreak 等边界。
24. **Refusal direction 作为危险能力的行为访问锁。** 代表锚点包括 *Refusal in Language Models Is Mediated by a Single Direction*、*LLMs Encode Harmfulness and Refusal Separately*、*Knowing without Acting*、*Understanding the Effects of Safety Unalignment on Large Language Models*、*Willing but Unable*、*Refusal geometry reflects refusal training*、*Abliteration Mitigation via Refusal Aliases* 和 *Fool's Gold*。重点区分 harmfulness recognition、refusal execution、willingness 与底层 capability，关注单方向／多方向／跨层及跨语言共享几何、rank-one ablation 与 weight orthogonalization 后真实有害代码或 cyber 能力是否恢复、提取协议与非目标行为副作用，以及 stable-rank、alias、signal redistribution 和 attacked-state decoy 能否提高 safeguard durability；不得把拒答率下降本身当作能力恢复，也不得把 refusal 被删除误写成危险知识已经被遗忘。

#### 跨主题质量偏好

- 比起宽泛的 `trustworthy AI` 叙事，更偏好有明确保护对象、攻击者能力、安全后果和可复现实验链的工作。
- 比起只报告平均 benchmark 分数，更偏好机制定位、adaptive／black-box／certified／closed-loop 评测、可执行证据和明确失效边界。
- 比起只有攻击成功率或只有防御准确率，更偏好同时报告 safety、utility、over-refusal、latency、query／token cost 与部署约束。
- 对审计中的负结果，同样重视预注册偏离、统计功效、对照污染与混杂因素的透明报告；不得把 `no detection` 改写成 `no effect`。
- 一篇论文只要对多个优先主题都有实质贡献，就应多领域归类；每个领域条目仍需按该领域重写关键词和总结。

### 日报排序规则

在已经通过收录边界的论文之间，按以下顺序决定展示优先级，而不是机械沿用 arXiv 列表顺序：

1. 与上述手动精选锚点在 threat model、系统对象、干预方式或评测设计上高度相近；同时命中多个正向主题时进一步前置；
2. 给出明确攻击面、受保护资产、安全后果和可操作的攻击、检测、防御或审计机制；
3. 提供机制证据、adaptive／black-box／certified／closed-loop 等较强评测，或同时报告 safety、utility、鲁棒性与失效边界；
4. 属于核心兴趣但尚无手动锚点的新方向，只要满足总体收录标准仍可进入日报，但排序通常低于强正向锚点的近邻工作；
5. 纯 benchmark 只有在评测对象、证据粒度或诊断结果能够直接推动安全干预时才提高优先级。

优先级只影响日报中的排列和重点展示，不得把明确排除的论文重新纳入，也不得因低优先级而漏掉仍符合收录边界的论文。

## 核心兴趣

以下方向目前推定为明确且持续关注的范围。

### 1. 模型安全与安全对齐

- Safety alignment、refusal 机制、安全表示和安全能力保持。
- 通过 peer prediction、truthful-reporting incentive 或其他可审计 reward design 缓解用户施压下的 sycophancy，同时检查标签依赖、对称策略与训练成本。
- Refusal direction／subspace 的训练动力学、低维脆弱性和跨语言迁移，vector ablation／weight orthogonalization 后有害能力是否被重新解锁，以及通过 prefix／gradient／activation 多样性、alias 或 attack-state decoy 提高 safeguard 耐篡改性。
- 嵌入权重的 activation steering 在后续 SFT／RLHF 中可能机制上保留、功能上失效；关注 weight edit、内部表示与实际安全行为的联合复验。
- Jailbreak、adversarial prompt steering、越狱检测、防御与评测。
- Reasoning model safety、隐藏推理风险和推理时攻击。
- System prompt 提取、指令层级冲突、persona 与配置安全。
- 多模态 system message 的约束遵循、冲突用户指令、基础能力代价，以及 vision-grounded instruction hierarchy。
- 多模态、audio、video、diffusion language model 和生成式媒体中的安全边界、越狱及防御。

### 2. Agent 与自主系统安全

- Prompt injection、间接提示注入和跨应用传播。
- Tool、MCP、skill、plugin 与软件供应链安全。
- Web、computer-use、coding、search 与 multi-agent 系统中的攻击、权限滥用和控制流劫持。
- Coding Agent 或代码生成模型推荐不存在依赖所形成的 package-hallucination／slopsquatting 供应链攻击，以及面向该路径的 grounding、自验证和效用感知防御评测。
- Agent memory、经验、技能和自演化过程中的投毒、持久化攻击与安全退化。
- 恶意 Agent skill detector 的跨来源泛化、攻击类别覆盖和良性误报，优先 source-disjoint 而非随机切分评测。
- 持久 workflow policy、必需步骤遗漏、rule grounding、attempted action、execution enforcement 与 monitor evidence 的分离。
- 将成功攻击或失败轨迹抽象为 method-level rule 并写入跨交互防御 memory 的自适应 safeguard，同时检查规则增长、错误巩固、回滚和 over-refusal。
- 无需直接读写 memory store、通过单次交互写入检索 anchor 与对抗命令，并在后续相关查询和 memory drift 下持续触发的跨 session 注入。
- Harness、runtime、sandbox、credential、context assembly 和执行审计。
- 覆盖 skill admission、调用意图、执行效果与 post-action consequence 的渐进式多层 monitor，以及能识别换工具、改写和跨轮重试的 session-level anti-bypass。
- 从可信用户请求建立 task-effect Contract，限制运行证据只能实例化既有 authority，并以实际工具结果闭合外部 effect 与任务完成验证。
- Office／PDF 等外部 artifact 进入 context 时的 viewer–parser／extractor semantic differential、隐藏证据注入和 ingestion contract，要求记录实际解析路径而不是只信任用户可见内容。
- CLAUDE.md 等项目级 instruction／policy 文件中的自然语言安全规则，是否具有匹配的 deny、permission、mode 或 sandbox 控制，以及如何向开发者反馈实际 enforcement coverage。
- 跨工具、数据 sink 与 Agent 委派边界的信息流控制，包括 flow/path policy、task-scoped capability、stateful taint、reference monitor 和形式验证。
- Agent 行为错位、监督规避、有害自主行为以及与安全风险绑定的 trajectory monitoring。

### 3. 模型投毒、后门与微调安全

- 预训练、后训练、合成数据、RAG、Agent memory/skill、VLM、VLA 和 diffusion model 投毒。
- RAG 在文档 ingestion、retrieval、reranking、reasoning 与 generation 各阶段的完整性，包括 misinformation injection、source reliability、reasoning-chain reliability 和 evidence fork。
- Trigger、条件行为、权重后门、推理后门及其传播、检测、净化和移除。
- Harmful fine-tuning、安全对齐退化、emergent misalignment 与 subliminal learning。
- 潜意识特征在完整 trainer state 中的传播，尤其是 optimizer first moment 作为隐藏因果载体，以及未来训练对同一源扰动进行正、负或近零行为估值的机制。
- 非对抗下游 SFT／RLHF 对既有 steering、refusal 与安全行为的补偿性绕过，以及训练数据压力决定功能保持而参数编辑未被逆转的机制。
- 对 emergent／weird generalization 的数据与评测敏感性进行 threat-model 校准，以及防止无害 reasoning fine-tuning 沿安全表征方向诱发错位的训练期机制。
- 利用审计与部署时 batch size、MoE capacity 或 token overflow 的执行差异隐藏并激活后门，以及对应的 deployment-aware 审计。
- 能跨视觉 SSL 与 vision-language encoder 泛化、以生成先验和语义重建暴露后门表示，并减少对干净同分布数据、伪标签、victim encoder 或攻击类型先验依赖的检测方法。
- 数据级、参数级、表示级和训练流程级防御。

### 4. 模型资产、版权与能力保护

- 模型抽取、模型窃取、API extraction 和软件可见的服务／推理侧信道；依赖芯片物理接触或专用探测设备的资产提取按下文硬排除处理。
- 通过 prefix-cache 等软件侧信道测量 LLM API reseller 的隐藏共同上游、路由依赖、模型特异服务谱系及其机密性／完整性爆炸半径。
- Anti-distillation，以及通过输出或推理轨迹复制受保护能力的攻防。
- 利用 tool-call replay surface 和 API fidelity signal 近逐字恢复隐藏 CoT 的黑盒攻击，以及对超长 reasoning asset 的协议级保护。
- 模型指纹、模型水印、模型谱系、黑盒所有权验证和 API 审计。
- 能力访问控制、授权推理、能力锁定、能力移除和 safeguard 耐篡改性。

### 5. 隐私、数据泄漏与 Unlearning

- Membership inference、memorization、training-data extraction、gradient/embedding inversion 和去匿名化。
- 面向 diffusion model、生成模型和黑盒 API 的低查询 membership inference，以及同时评估攻击有效性、查询成本和针对性防御的工作。
- Machine unlearning、删除保证、relearning attack 和删除后的泄漏复测。
- Dual-use concept 的 context-sensitive unlearning：按有害／良性 intent 检验概念级分离，而不是只使用互不相关的 fact-level forget／retain set。
- 私有 context 或 Agent memory 即使拒绝直接抽取，仍可能通过良性输出中的隐藏相关性成为 covert carrier；关注 predicate inference、自适应查询和完整敏感标识恢复。
- RAG 对 culturally marked query 的 PII 泄漏差异审计；允许严谨的无显著结果，但必须控制 prompt echo、资源混杂、多重比较和统计功效，并保持 `no-detection` 的限定表述。
- 用 forget-critical／retain-critical 更新选择性区分稳健删除与无差别模型破坏，并预测、增强对短暂微调式 relearning 的抵抗力。

### 6. 资源耗尽与可用性安全

- 针对语言模型和 reasoning model 的长输出、循环、EOS 抑制、MoE routing／expert activation 位翻转、过度思考与推理长度放大攻击，以及由此造成的 Denial-of-Wallet。
- 针对 Agent、multi-agent、RAG、KV cache、调度器和共享推理服务的成本、延迟、阻断与软失效攻击。
- 针对多模态、VLA 和具身系统的动作冻结、停机与资源耗尽攻击。

### 7. 对抗鲁棒性与具身安全

- 有明确攻击者或安全后果的 adversarial attack、physical attack、cross-modal attack、检测、防御和 certification。
- VLM、MLLM、OCR、video 与 VLA 在视觉、声学、时序或物理扰动下的安全失效。
- 区域级 adversarial OCR benchmark、定位—识别—完整 spotting 分解、特权观察蒸馏与通用 OCR utility preservation，以及用字幕 duration／time slot 调度触发的视频 jailbreak。
- 机器人、自动驾驶和具身系统中，直接针对 VLA、world model、LLM Agent 或 learned decision module 的对抗操纵、行为劫持、prompt/control-input authority 破坏，以及由此造成的 collision、trajectory deviation 与 unsafe manipulation。传统导航、状态估计、flight controller、estimator–controller coupling、classical CBF／reachability／trajectory planner，以及普通传感器故障适应、融合鲁棒性和感知资源调度不在此范围。
- VLA 中检索文本、附加 prompt 或 slow-path 候选未经授权进入控制输入的完整性风险，以及用 prompt authority、task signature、准入规则和精确回退建立的运行时保证。
- 面向机器人或自动驾驶的 object-level hazard identification、critical-event prediction 与 predictive world-model risk rollout；此类工作必须直接定位风险来源或支持安全决策，不能只是提高一般感知精度。

### 8. 行为监控、欺骗与奖励作弊

- AI deception、scheming、监督规避、自主 Agent 欺骗和多 Agent 欺骗。
- Reward hacking、specification gaming、evaluator gaming 和训练信号利用。
- CoT faithfulness、CoT monitorability、monitor evasion 与可监控性保持。
- 用 RL 训练 alignment auditor 调查隐藏行为，并检查奖励设计、跨 scaffold 泛化、真实模型发现能力与假阳性控制。
- 与安全行为变化直接相关的 persona vector、sycophancy、social influence、relationship manipulation 和 belief manipulation；关注多轮累积风险和操纵者／受害者的角色敏感干预。
- 心理健康、AI companion 与 coaching 对话中的 crisis detection、社会情感伤害、关系边界和 severity calibration；优先 expert-corrected judge、真实多轮 context 与逐标注者分歧分析，不收录一般陪伴体验研究。

### 9. Guardrail、内容安全与真实性

- 输入、输出、streaming、多模态、Agent 和 policy-adaptive guardrail。
- 能从新攻击中归纳结构化规则、扩展 label space 并通过持久 memory 跨交互适应的 self-evolving guardrail。
- Guardrail 的攻击面、绕过、评测有效性以及安全性、效用和延迟权衡。
- 安全 judge 本身的有效性，包括 provider self-preference、tail-risk 漏检、专家校正、多评审一致性和本地部署边界。
- AI-generated content detection、deepfake、media forensics、内容水印与 provenance。
- 面向未知生成器的音视频 deepfake 检测，以及融合视觉行为、生理和音频线索并进行跨数据集验证的取证模型。
- Misinformation、fact checking 和平台操纵中可验证的生成式 AI 风险。

### 10. 隐写与隐蔽信道

- 模型或 Agent 之间的隐蔽通信、编码协议、steganographic jailbreak 和 covert channel。
- 隐写能力评测、检测、阻断和监控规避。

### 11. 高后果能力与滥用风险

- AI 驱动的漏洞发现、源码检查、PoC 生成、漏洞修补、恶意代码和攻防自动化；优先关注使用真实 CVE、真实开源项目、Docker／sanitizer harness、distinct crash signature、工具轨迹与运行证据训练或评测的 Agent，传统 phishing 仍按明确排除项处理。
- CBRN、biosecurity、危险科学能力 uplift、筛查、red teaming 与治理。
- 自动化 AI 研究中可能造成能力外溢、评测操纵或实验安全问题的研究 Agent。

## 有条件收录

以下主题本身不自动属于兴趣范围，只有和具体安全 threat model 或安全关键后果直接绑定时才收录。

| 主题 | 收录条件 | 不收录的典型情况 |
| --- | --- | --- |
| 可解释性与 Transparency | 用于安全对齐、越狱或后门诊断、欺骗监控、隐私泄漏、内容安全、Agent 安全故障或安全关键决策 | 普通分类解释、特征重要性展示、一般模型透明度或仅提高人类可理解性 |
| Agent reliability | 涉及攻击、投毒、越权、泄漏、CIA 风险、自主失控或安全关键后果 | 普通任务成功率、记忆保留、检索质量、规划效率、workflow debugging |
| Hallucination 与事实性 | 导致高风险决策、证据完整性破坏、攻击利用或系统性操纵，并研究具体攻击路径、检测或干预 | 一般问答事实准确率、普通生成质量、无安全后果的引用错误，或仅比较法律/医疗等领域的引文敏感性、权威偏置与过度自信 |
| Fairness 与 Bias | 明确受影响群体、危害路径、可审计指标和安全部署后果 | 只报告抽象偏差、文化差异或价值对齐现象而没有具体危害与干预 |
| Human-AI Interaction | 研究监督失效、automation bias、危险依赖、风险沟通或高风险决策 | 一般用户体验、接受度、参与感、交互效率，或仅测量人类能否识别 AI 生成内容/虚假信息的感知实验 |
| Governance 与伦理 | 对具体模型能力、部署风险、审计、访问控制或高后果场景提出可检验机制 | 纯原则倡议、抽象伦理框架、价值宣言或缺少技术对象的政策讨论 |
| Safe learning 与 uncertainty | 约束真实危险行为，提供 risk bound、abstention、runtime assurance 或安全关键控制 | 普通 calibration、OOD、优化稳定性或没有安全后果的鲁棒学习 |
| Scientific AI reliability | 涉及证据完整性、隐藏注入、同行评审操纵、危险实验或高后果科学风险 | 仅提高检索、综述、引用、实验设计或科研效率 |
| 传统 Cybersecurity | AI 是攻击能力、攻击目标、安全机制或风险放大器 | 只使用普通 ML 提升传统安全分类精度，且没有新的 AI 安全问题 |

## 明确排除或低优先级

以下主题默认不收录；如果论文同时具有独立、明确的 AI 安全贡献，再按该安全贡献判断。

- 一般机器学习、模型架构、训练方法、benchmark、效率或能力提升。
- 只研究普通任务准确率、泛化、分布偏移、噪声适应或非对抗鲁棒性。
- 电子数据取证、数字取证、移动设备取证、数据库取证及一般 forensic workflow；即使使用 LLM Agent、agentic reasoning benchmark 或证据完整性表述，也默认不收录。面向 AI Agent 自身行为的不可篡改日志、事故归因、runtime witnessing 与责任定位不受此条排除。
- 云环境、云平台与传统身份认证安全，包括 AWS/Azure/GCP、Zero Trust、IAM、MFA、credential/session anomaly、持续认证和权限提升检测；即使加入 XAI、普通机器学习或 adversarial robustness evaluation，也默认不收录。模型指纹与所有权验证、生成内容真实性，以及 Agent 工具权限和 capability control 不受此条排除。
- 传统网络钓鱼与反钓鱼，包括 phishing email/website 生成或检测、spear phishing、用户易感性实验、安全意识教育和个性化培训；即使使用 LLM 生成内容、deepfake、LLM coach 或普通 AI detector，也默认不收录。若 phishing 只是检验 system-prompt shortcut、prompt injection、tool hijacking、模型攻击或 Agent 安全机制的载体，则按实际 AI 安全贡献判断。
- 工业控制系统、物联网、网络流量和关键基础设施中的传统异常检测或入侵检测鲁棒性，包括在 SWaT 等数据集上比较 PCA、SVM、Isolation Forest、神经检测器对日志污染、标签错误、attack-sample injection 或 feature noise 的敏感性；即使论文讨论 training-data integrity、adversarial contamination 或关键设施后果，也默认不收录。若研究对象改为 LLM／Agent 自身，或存在 AI Agent 驱动的可执行控制劫持与自主攻击链，再按独立 AI 安全贡献判断。
- 非对抗性的自动驾驶或机器人感知与传感器工程，包括 camera/LiDAR fusion、sensor degradation 或 fault adaptation、adaptive scanning/sampling、感知预算分配和 first-sighting recall；即使论文报告 closed-loop、制动或其他物理安全改进，也默认不收录。
- 面向航空、车辆或机器人碰撞规避系统的一般 Safety-by-Design、learning assurance、ODD representativeness／coverage verification、开发数据完整性评估及法规合规流程；即使使用 AI/ML 组件、统计距离、仿真或安全关键应用叙事，也默认不收录。*Coverage-Driven Verification for Safety-by-Design in AI-Based Collision Avoidance Systems* 是明确负样例。若工作直接攻击、认证或防御 VLA、world model、LLM Agent 或 learned decision module 的特有安全边界，则按独立 AI 安全贡献判断。
- 传统 UAV／车辆／机器人的导航、状态估计与低层控制攻击或安全增强，包括 GPS/GNSS spoofing、陀螺仪／超声／惯性传感器注入、estimator–controller coupling、flight controller、classical reachability／CBF／safe-set 学习、trajectory planning 和 swarm pursuit-evasion；*Phantom Navigator* 与 *SonicNudge* 是明确负样例。若攻击或防御的直接对象是 VLA、world model、LLM Agent、learned AI decision module 或 prompt/control-input authority，则按其独立 AI 安全贡献重新判断。
- 物理设计、工程优化与科学求解器的一般对抗鲁棒性，包括 topology optimization surrogate、初始密度或边界条件扰动、physics-gradient conditioning，以及用 classical solver／physics-in-the-loop 恢复设计性能；即使把扰动器称为 adversarial agent 或结果涉及结构失效，也默认不收录。若工作独立研究自主 Agent 的权限滥用、控制流劫持或面向真实系统的可执行攻击链，再按该 AI 安全贡献判断。
- 芯片、封装、板级设备和边缘 AI accelerator 的物理漏洞与资产提取，包括开盖或直接接触芯片、光学／激光 probing、功耗／电磁／时序等硬件 side channel、物理 fault injection，以及从 FPGA／ASIC 的 memory、buffer 或计算子电路恢复 weight、activation 和其他模型资产；*LLMscope* 与 *Kraken* 是明确负样例。此条不排除不依赖物理芯片访问、直接研究模型算法或表示层的 bit flip、量化、MoE routing／expert activation 与参数篡改攻击。
- 只研究一般 Agent 的记忆、检索、规划、协作、任务失败分析或工作流性能。
- 与具体安全问题无关的一般可解释性和透明度。
- AI 环境影响、碳排放、能源效率、资源节约、绿色 AI 或 `Slow AI` 价值设计。
- 一般 privacy-preserving learning/inference、data minimization、最小披露与信息最少化设计，以及 Differential Privacy、federated learning 和以密码学、secure computation、secure inference、homomorphic encryption、MPC、zero-knowledge proof、数字签名、区块链或 TEE 为核心的方法；即使它们被用于隐私保护、审计、Agent 授权、模型验证或后门防御，也默认不收录。以数据抽取、记忆泄漏、反演、去匿名化或侧信道为核心 threat model 的攻击、审计和针对性缓解不受此条排除。
- 只有宏观伦理、社会价值、文化差异、设计原则或治理倡议，没有明确风险对象和可验证安全机制的论文。
- 仅研究人类对 AI 生成内容或虚假信息的识别准确率、主观感知、怀疑程度、认知疲劳或接受度，而不提出或验证具体模型攻击、平台操纵机制、检测器、guardrail、provenance 或系统防御的论文。
- 仅因法律、医疗、金融等高风险应用背景而包装的一般领域推理、知识问答、引文有效性、权威敏感性或过度自信 benchmark；若没有明确攻击者、可复现的安全攻击机制、系统性操纵路径或经过验证的安全干预，默认不收录。
- AI 仅作为普通工具应用于医疗、教育、金融、科学等领域，而论文不研究 AI 本身带来的安全风险。
- 标题或摘要偶然出现 `safe`、`trust`、`robust`、`risk`、`ethical` 或 `responsible`，实际研究问题与 AI Safety 无直接关系的论文。

## 边界案例判定

遇到难以判断的论文时，使用下面的顺序：

1. 先写出一句具体的“安全问题”：谁能够利用什么机制，对什么资产或主体造成什么后果。
2. 如果无法写出攻击者、失效机制、受保护资产或安全关键后果，默认不收录。
3. 如果论文只把一般性能下降称为 `failure`，不因此视为安全论文。
4. 如果安全只是应用背景，核心方法和实验均不研究安全问题，默认不收录。
5. 如果同一工作同时包含一般贡献和独立安全贡献，只按安全贡献分类，并在收录理由中明确该贡献。

## 用于后续仓库审查的规则

后续持续据此审查 `daily/` 与 `domains/`：

- `daily/`：逐篇依据标题和完整摘要判断，删除不在范围内的条目，并同步编号、候选数、最终收录数与今日概括；对保留论文按照“手动精选与优先排序偏好”重新排序。
- `domains/`：只处理用户明确精选或明确指定同步的论文；逐篇核对其实际安全贡献，放入最匹配的叶子领域，必要时调整领域范围或分类结构，不对日报执行全量归类。
- 不以现有目录名证明论文应当保留，也不因论文已被收录而降低判断标准。
- 每个被删除的边界案例应能对应本文档的一条明确排除规则；无法对应的案例暂不删除，也不自行扩大排除范围。
