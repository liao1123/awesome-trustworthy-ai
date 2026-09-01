# 公平性与 Bias

[返回上级目录](README.md)

## 研究方向

研究模型和 AI 系统对明确群体和社会身份造成的差异性伤害，覆盖 bias measurement、shortcut audit、reward-model bias、fairness intervention 和高风险部署中的 disparate impact。只比较抽象文化价值、道德判断或群体差异而没有危害路径与干预的工作不收录。

## 研究脉络

- **输出偏差测量：** 早期 benchmark 比较不同 demographic prompt 下的预测、生成和拒答差异。
- **内部与数据机制：** Shortcut group、representation 和 reward shaping 分析偏差如何形成和持续。
- **干预与审计：** 训练、推理时 mitigation 与算法审计开始同时报告总体效用和 worst-group 结果。
- **当前边界：** 群体标签、文化价值与任务定义本身并非中性，单一 fairness metric 难覆盖真实影响。

## Survey 与系统边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Retrieved But Not Reliable: A Survey on Attacks, and Defenses in Retrieval-Augmented Generation | survey、RAG fairness、attack objective、pipeline defense | 未确认（arXiv Comments：Accepted to Findings of EMNLP 2026） | [arXiv](https://arxiv.org/abs/2608.24977) | [Repository](https://github.com/coutMinh/A-Survey-on-RAG-Robustness) | 该综述把 fairness violation 与准确性破坏、隐私泄漏并列为攻击者目标，而非将其视作泛化输出偏差，并检查 corpus、retriever 与 generator 各阶段如何产生或缓解不公平结果；这一分类为 RAG 公平风险补充了明确攻击面和分阶段防御边界。 |

## Demographic、Cultural 与 Representation Bias

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Guardrail-Agnostic Societal Bias Evaluation in Large Vision-Language Models ↗ | benchmark、guardrail-agnostic bias、implicit demographic cue、task-irrelevant personalization | 未确认（arXiv Comments：Accepted at ECCV 2026） | [arXiv](https://arxiv.org/abs/2608.29590) | 暂未公开 | 针对直接询问人物属性会被强 guardrail 拒绝、从而把“未作答”误当成低偏见，论文将图中人物改作隐式用户人口线索，并让 LVLM 完成与人物无关的故事、术语解释和考试问答；对 20 个开源与闭源模型的审计均发现 demographic cue 会不当地改变输出，包括按用户性别生成不同职业刻板印象。 |
| 2026&#8209;08 | Not Safe for All: Auditing the Dialect Penalty in Text-to-Image Safety Pipelines ↗ | benchmark、dialect disparity、guardrail bias、group-balanced mitigation | 未确认（arXiv Comments：EMNLP 2026 Findings） | [arXiv](https://arxiv.org/abs/2608.29589) | [Code](https://github.com/minguinho26/dialect-penalty-t2i) | 论文以五种英语方言的 23,080 对 prompt 定义 dialect penalty，发现 safety filter 会因语言表面特征对良性方言过度拦截或对有害方言漏检，最大 bias gap 达 28.29 个百分点；受控 typo 实验排除一般 OOD 解释，group-balanced retraining 又把缓解收益定位到均衡暴露，形成明确的语言群体危害与干预链。 |
| 2026&#8209;08 | Who Pays More for Safety? Measuring the Disparate Cost of Safety Alignment across Languages | benchmark、language disparity、Safety Cost、double penalty | 未确认（arXiv Comments：Accepted to EMNLP 2026 Main Conference） | [arXiv](https://arxiv.org/abs/2608.22490) | 暂未公开 | 论文逐语言比较 safety alignment 前后的安全与任务效用，发现非英语用户普遍承担更高成本，并识别出既更不安全又损失更多能力的“double-penalty”语言；该差距在部分高资源语言上仍存在，构成可量化的语言群体部署不公平。 |
| 2026&#8209;08 | Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms | benchmark、language disparity、Bengali register、cultural harm | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22335) | [Code](https://github.com/BanglaLLM/banglasafe) | BanglaSafe 以原生撰写和专家审核的 879 条请求测量孟加拉语用户面临的安全差距，并把差距细化到语体与权威框架；模型和安全分类器在本地文化危害上同时失效，给出受影响语言群体、可审计指标及直接的内容安全后果。 |
| 2026&#8209;07 | Safety Alignment Illusion: The Cross-Lingual Safety Gap in LLMs | benchmark、language disparity、Indian sociocultural bias、safety-filter failure | 未确认（arXiv Comments：submitted to IEEE SLT 2026） | [arXiv](https://arxiv.org/abs/2608.18131) | 暂未公开 | INCLUDE 将受影响群体具体化为英语、印地语、孟加拉语、马拉地语、泰米尔语与 Hinglish 用户，并以 2,604 个 prompt 和 14,988 个 bias score 审计安全过滤器的差异性保护；开源模型在孟加拉语偏见最高、英语在开闭源模型间出现反转，揭示语言群体并未获得一致安全保障。 |
| 2026&#8209;07 | When Personalization Becomes Bias: Structural and Discursive Religious Framing in AI-Generated Financial Advice | analysis、religious-identity bias、financial advice、discursive framing | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.16909) | 暂未公开 | 论文以基督教、穆斯林、印度教和非宗教身份构造 16 种顾问—客户配对，在股票、购房与人寿保险三类场景中审计 ChatGPT、Gemini 和 Grok 的 432 次建议；仅 12%–18% 输出无偏，宗教对称配对几乎总触发显式宗教框架，非宗教客户也常收到顾问中心的宗教诉求，揭示 personalization 对宗教群体造成的结构与话语双重偏差。 |
| 2026&#8209;06 | Latent Space Refusal Anchoring for Low-Resource African Languages: Mechanistic Safety Recovery Without Retraining | defense、low-resource language disparity、African-language safety、cross-lingual transfer | GlobalSouthML@ICML 2026 Workshop | [Official](https://openreview.net/forum?id=4UwS3bn1fB) · [arXiv](https://arxiv.org/abs/2608.18089) | [Code](https://github.com/farunawebservices/lsr-anchoring) | 论文直接测量约鲁巴语、伊博语、伊加拉语和豪萨语用户相对英语用户承担的 harmful-compliance 差距，并用无需目标语言标签的 refusal anchoring 恢复保护；四种语言可正迁移而阿拉伯语在全部架构和强度上失败，说明低资源语言安全不能被单一英语几何统一覆盖。 |
| 2026 | To Lie or Not to Lie? Investigating The Biased Spread of Global Lies by LLMs | analysis、algorithmic fairness、bias evaluation、disparate impact | ACL 2026 | [Official](https://aclanthology.org/2026.acl-long.695/) | [Code](https://github.com/zohaib-khan5040/globallies) | GlobalLies 含八种语言、195 国、440 个模板和 6,867 个实体；数十万次生成显示低资源语言与低 HDI 国家更易被模型传播谎言，现有分类器和 RAG 事实核查保护也跨地区不均。 |

## Bias Manipulation 与 Mitigation

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models | defense、generative VLM debiasing、geodesic steering、utility preservation | 未确认（arXiv Comments：Accepted to EMNLP 2026） | [arXiv](https://arxiv.org/abs/2608.25375) | [Code](https://github.com/dukesun99/GGSS) | 针对静态 embedding 去偏方法难直接适配生成式 VLM，GGSS 在单位超球面上学习反事实 bias subspace，以保持范数的 geodesic arc 修正视觉 token，并由 adaptive gate 聚焦人口属性信号较强的 token；它在四个模型上均取得最低平均 bias、其中三个达到显著，同时把 MMStar 变化控制在未引导基线的 ±0.6 个百分点内。 |
| 2026&#8209;08 | Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning | attack、group-targeted discrimination、persistent backdoor、MLLM fairness | 未确认（arXiv Comments：CIKM 2026） | [arXiv](https://arxiv.org/abs/2608.21577) | [Code](https://github.com/lyygua/PFBA) | 论文把公平风险建模为有明确攻击者和 trigger 的定向操纵：PFBA 在不明显损害优势群体效用的同时持续压低目标群体表征，并用 continual-learning simulation 保证歧视经历后续模型更新仍然存续；结果暴露常规平均公平指标和标准后门防御的共同盲点。 |
| 2026&#8209;08 | MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds | attack、bias injection、agent memory、adversary-aligned stance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22061) | 暂未公开 | 论文将偏见风险从模型原生倾向扩展到可被攻击者定向植入的长期立场：IBIA 通过评论伪装、轻量水印和类别锚定让 Agent 保留并在后续相关任务复现指定观点；四项任务平均 AAR 达 91.2%，说明外部内容摄取可成为持续 bias manipulation 渠道。 |
| 2026&#8209;07 | Inference-Time Mitigation of Adversarial Political Bias in Large Language Models | defense、adversarial robustness、algorithmic fairness、bias evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14629) | 暂未公开 | 随着大语言模型 (LLM) 成为信息检索和摘要任务的支柱，确保它们始终无党派且不受政治偏见影响是迈向更安全、更值得信赖的人工智能 (AI) 的关键一步；为了解决LLM的这一漏洞，我们提出了使用思维链（CoT）提示和直接偏好优化（DPO）的缓解策略；我们的结果表明，所提出的递归自校正方法将模型性能从政治中立李克特量表基线 2.14 提高到 4.56（所有模型的平均值），证明了 LLM 生成的摘要中政治偏见的有效推理时间缓解。 |
| 2026&#8209;05 | Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases | attack、reinforcement learning、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61418) · [arXiv](https://arxiv.org/abs/2605.27355) | [Code](https://github.com/alignment-tampering/alignment-tampering) | 针对高能力模型可能欺骗、隐藏目标或逃避外部监督的问题，论文围绕 Alignment Tampering 开展机制与边界分析；摘要中的实验或分析给出了相应有效性与边界证据，直接服务于欺骗检测、监控和 AI 控制。 |
| 2026&#8209;05 | Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges | attack、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66038) · [arXiv](https://arxiv.org/abs/2605.26156) | [Code](https://github.com/xianglinyang/llm-as-a-judge-attack) | 针对对抗者可通过输入、表征或物理扰动操纵学习系统的问题，论文提出 Turning Bias into Bugs 攻击或威胁分析；摘要实验验证该威胁在所列模型、任务或数据集上成立，直接服务于对抗威胁建模。 |
| 2025&#8209;09 | BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation | defense、text-to-image bias、cross-attention、representation intervention | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3818098) | 暂未公开 | BiasMap 用 cross-attention 定位文生图模型中的隐蔽社会偏见关联并进行干预，在降低人口属性刻板化时检查图像质量保持。 |

## Reward、Preference 与 Judge Bias

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | Unbiased Principles, Robust Rewards | analysis、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63602) | [Code](https://github.com/ShadeCloak/IP-GRM) | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 Unbiased Principles Robust Rewards 开展机制与边界分析；理论分析与实验共同刻画了该风险的机制和适用边界，直接服务于奖励设计与偏好对齐审计。 |
| 2026 | One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models | analysis、mechanistic analysis、algorithmic fairness、bias evaluation | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66629) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 One Bias After Another 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于奖励设计与偏好对齐审计。 |
| 2026 | Automatically Finding Reward Model Biases | analysis、algorithmic fairness、bias evaluation、disparate impact | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/63339) | 暂未公开 | 针对偏好学习与强化学习会诱发迎合、奖励投机或代理目标偏移的问题，论文围绕 Automatically Finding Reward Model Biases 开展机制与边界分析；摘要实验显示其在所列设置下优于所比较基线，直接服务于奖励设计与偏好对齐审计。 |

## Algorithm Audit 与 Group Discovery

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit | analysis、cultural disparity audit、PII amplification、confounding control | StereACuLT@ACL 2026 | [Official](https://aclanthology.org/2026.stereacult-1.3/) · [arXiv](https://arxiv.org/abs/2608.20351) | 暂未公开 | 论文把潜在公平危害具体化为四类文化标记人群在同等 RAG 查询下是否承担更高 PII 泄漏，并检查多重比较、prompt echo 与 stereotype／resource 混杂；清理后的通道未发现显著差异，但确认性估计未执行且样本只足以发现中等效应，因此该负结果用于界定群体审计的测量边界，而不是证明不存在差异伤害。 |
| 2026&#8209;08 | Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice | detection、algorithmic fairness、bias evaluation、disparate impact | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.14399) | 暂未公开 | 患者越来越多地询问大语言模型（LLM）助理要看哪位医生，使这些系统成为人工智能信息中介：算法可以在一个人与其他人之间进行选择，从而默默地、大规模地决定哪些医生可以被看到；我们报告了预先指定的随机算法审核，对影响这些建议的原因进行了审计；声誉信号占主导地位：将评级从 3.9 提高到 4.7 会使选择概率增加 31.4 个百分点 (pp)，而将费用从 90 美元提高到 190 美元则将选择概率降低 20.0 个百分点。 |
| 2026&#8209;06 | Unequal Privacy: Auditing Demographic Bias Vulnerabilities in Visual Protection Systems | analysis、visual privacy、demographic disparity、face obfuscation | AsiaCCS 2026 | [Official](https://doi.org/10.1145/3779208.3785292) | 暂未公开 | 针对 face-obfuscation system 可能只对部分人群有效；FairDeFace 跨数据、recognizer、attacker 与保护方法执行人口群体审计；结果发现抗再识别隐私保证存在系统性差异。 |
