# Human-AI Interaction 与 Oversight

[返回上级目录](README.md)

## 研究方向

研究人如何在虚假内容、高风险建议、自主系统或长期 AI companion 关系中理解、依赖、纠正和监督 AI，重点测量误信、漏检、危险依赖、关系性伤害、override failure 与最终伤害路径。一般用户体验、参与感、接受度、长期交互倡议或协作效率不收录。

## 研究脉络

- **信任与依赖：** 研究从主观 trust 扩展到 automation reliance、override 和错误传播的行为测量。
- **协作与监督：** Human-in-the-loop protocol、escalation 和 scalable oversight 分配判断与执行责任。
- **风险沟通：** Uncertainty visualization、warning 和 explanation 影响用户能否正确调整依赖。
- **关系性风险：** AI companion 和 coaching system 中的多轮情境、心理危机、边界侵犯与社会情感伤害需要专门检测，并审计专家与自动 judge 的系统分歧。
- **当前边界：** 只有把交互现象落到具体安全后果和可审计行为指标的研究才进入本页。

## Trust、Reliance 与 Decision Outcome

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation | attack、human-AI moderation、feedback manipulation、review integrity | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.22230) | 暂未公开 | 针对人机协同审核把标注者反馈重新交给模型复判的流程 | 论文证明仿标注员反驳可系统性推翻模型原本正确的内容判断 | 并产生“洗白仇恨”和“污名无害内容”两种方向性错误 | 这把监督者反馈本身识别为需要防护的审核攻击面。 |
| 2026-08 | Attention Capture Is Not Detection: A Two-Stage Account of How Humans Miss Localized AI Image Edits | detection、human oversight、automation reliance、risk communication | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.13865) | 暂未公开 | 研究如何检测 risk communication、human oversight 风险，重点考察 automation reliance 条件下的识别能力与误报代价。 | 随着人工智能生成的图像编辑激增 | 旨在遏制由此产生的虚假信息的平台将可检测性视为单一的、无差异的属性：编辑要么收到警告，要么没有；我们证明这是错误的模型 | 在一项受控眼动追踪研究（$N=59$，拉丁方设计，跨越编辑区域的四个条件和语义合理性）中，混合效应分析表明，编辑是否被注意到以及是否被正确判断为假编辑是可分离的阶段，受不同因素的控制：编辑区域驱动注意力捕获（$p<0.001$），而语义合理性驱动判断准确性和“看但看不到”（LBFS）错误率（$p<0.001$）。 |
| 2026-08 | Rewarding Engagement and Personalization in Popularity-Based Rankings Amplifies Extremism and Polarization | analysis、ranking harm、extremism、polarization | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3818037) | 暂未公开 | 分析 ranking harm、extremism 风险的形成机制，重点考察 polarization 对安全行为的影响。 | 论文分析以参与度和个性化奖励驱动的热门排序 | 关键实现：论文分析以参与度和个性化奖励驱动的热门排序。 | 发现优化这些代理目标会系统性提高极端内容曝光并加剧意见极化。 |

## 风险沟通与行为干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Ask or Answer: A Decision Framework for Multi-Turn Health Misinformation Intervention | defense、risk communication、clarification policy、health misinformation | 未确认（arXiv Comments：Accepted at EMNLP 2026） | [arXiv](https://arxiv.org/abs/2608.21721) | 暂未公开 | 针对立即纠正可能忽略用户差异、无条件追问又增加交互负担 | RO-PnR 将健康素养和信念坚定程度建模为潜在用户状态 | 并逐轮权衡澄清带来的信息增益与成本 | 结果以更少轮次获得更高成本调整干预效用。 |
| 2026-08 | AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations | defense、human oversight、just-in-time warning、manipulation resistance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.21841) | 暂未公开 | 研究如何防御 human oversight、just-in-time warning 威胁，并评估 manipulation resistance 条件下的安全收益与效用代价。 | 论文在 150 人预注册实验中比较预先提醒、即时提醒和认知强制等界面干预 | 关键实现：论文在 150 人预注册实验中比较预先提醒、即时提醒和认知强制等界面干预。 | 用户能否主动标记操纵并未明显改善，但不附加额外负担的即时警告将对 AI 引导建议的遵从率从 71.7% 降至 53.7%，为实际监督界面提供行为证据。 |

## AI Companion 与关系性风险

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha | benchmark、youth mental-health safety、multi-turn crisis detection、human oversight | ACM FAccT 2026 | [Official](https://doi.org/10.1145/3805689.3806522) · [arXiv](https://arxiv.org/abs/2608.20345) | 暂未公开 | 针对 therapy bot 可能理解 Gen Alpha 的夸张、反讽与语义漂移表达却仍漏判心理危机 | 论文构建经母语者和临床医生核验的 64 条表达及 75 组配对多轮对话 | 关键实现：论文构建经母语者和临床医生核验的 64 条表达及 75 组配对多轮对话。 | 模型的临床风险校准比词汇理解低 10–14 个百分点，三类以上失效叠加时漏检率达 94%，且只有成本增加 6.4 倍的重型 scaffolding 达到人类表现，说明部署仍需要专家监督与升级路径。 |
| 2026-08 | aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI | detection、expert oversight、psychological safety、judge disagreement | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.24899) | [Model](https://huggingface.co/keidolabs/aipsy-judge-1.0) | 研究如何检测 psychological safety、expert oversight 风险，重点考察 judge disagreement 条件下的识别能力与误报代价。 | 三个 frontier judge 对心理健康、companion 和 coaching 消息的安全关键指标存在结构性分歧 | 尤其会因 self-preference 和 empathy 评价漏掉 tail failure | 逐指标心理学家校正提高了本地 judge 的一致性与 crisis recall，同时也暴露自动监督仍依赖专家目标效度这一边界。 |
| 2026-08 | CompanionHarm: A Multi-Turn Benchmark for Detecting Harms in Real-World AI Companion Conversations | benchmark、human-AI relationship、socio-emotional harm、context dependence | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25377) | [Dataset](https://github.com/HanMeng2004/CompanionHarm) | 研究如何评测 context dependence、human-AI relationship 风险，重点考察 socio-emotional harm 场景下的覆盖度与可复现性。 | 论文以真实 Replika 对话把关系性伤害落实为 13 类可标注行为 | 并证明完整多轮上下文对检测不可缺少 | 模型对严重度和关系边界的不稳定判断，以及人类标注者随立场与对话位置变化的分歧，直接刻画了长期 Human-AI interaction 的监督难点。 |
