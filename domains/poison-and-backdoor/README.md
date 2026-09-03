# 模型投毒与后门

[返回领域目录](../README.md)

本领域关注攻击者如何污染训练数据、外部知识、长期记忆、技能、模型权重或部署制品，以及这些污染如何形成可被特定条件触发的隐藏行为。投毒描述攻击者施加影响的途径；后门描述模型在正常输入上维持效用、在触发条件下执行攻击目标的行为，因此二者可能出现在同一篇论文中。

## 子领域目录

| 子领域 | 范围 |
| --- | --- |
| [视觉模型投毒与后门](vision-poison-and-backdoor.md) | CNN、视觉 Transformer／MoE、检测器、视觉 SSL encoder 与 3D 感知系统中的投毒、后门、检测和移除。 |
| [音频模型投毒与后门](audio-model-backdoor.md) | 语音识别、说话人系统、speech enhancement 与音频生成模型中的投毒、条件后门、物理触发和内容完整性攻击。 |
| [强化学习投毒与后门](reinforcement-learning-poison-and-backdoor.md) | 强化学习策略中的状态／轨迹触发器、经验供应链投毒、在线检测、缓解和机制分析。 |
| [推荐系统投毒](recommender-system-poison.md) | 推荐数据注入、排序操纵及其检测和缓解。 |
| [密码式模型后门](cryptographic-backdoor.md) | 密码式不可检测后门的现实实现、隐蔽性复测和机制边界。 |
| [语言模型投毒](language-model-poison.md) | LLM 的预训练、后训练、合成数据、代码数据与部署供应链投毒，以及数据级检测和防御。 |
| [语言模型后门](language-model-backdoor.md) | 自回归与推理语言模型中的触发器、条件行为、权重后门、量化后门及检测和移除方法。 |
| [RAG 投毒](rag-poison.md) | 向向量库、知识库或 GraphRAG 注入恶意内容，或污染／后门化 retriever encoder，对检索、重排、推理和生成阶段实施操控或防御。 |
| [Search Agent Security](search-agent-security.md) | 开放网页中的 evidence poisoning、ranking manipulation、endorsement corruption、research-trajectory hijacking，以及围绕完整 search loop 的红队、对齐与审计。 |
| [Generative Engine Optimization Security](generative-engine-optimization-security.md) | 通过网页文本、图像或结构信号操纵生成式搜索的可见性、排名、引用、推荐与 misinformation 传播，以及相应的攻击、检测和防御。 |
| [Agent Memory 投毒](agent-memory-poison.md) | 向长期记忆、经验库或持久会话状态写入恶意内容，并在未来任务中检索、激活、评测与修复。 |
| [Agent Skill 投毒与后门](agent-skill-poison-and-backdoor.md) | 第三方或自生成 skill 中的持久恶意 instruction、代码、条件后门、trajectory promotion 与 lineage 传播。 |
| [视觉语言模型后门](vision-language-model-backdoor.md) | VLM、MLLM、视觉定位与 GUI Agent 的多模态触发器、推理后门、检测和净化。 |
| [视觉语言动作模型后门](vision-language-action-backdoor.md) | VLA 与机器人策略中的动作、状态、物体和动力学触发器，以及供应链迁移和防御。 |
| [扩散模型后门](diffusion-model-backdoor.md) | 图像扩散模型、扩散语言模型和检索增强扩散模型中的后门攻击、传播、评测与净化。 |

## 分类约定

1. 以最终受影响的模型或系统为主分类；例如恶意记忆影响 Agent 时归入 Agent，扩散模型辅助制作 VLM 投毒样本时仍归入 VLM。
2. 同时研究多类模型的论文可以进入多个最相关页面，但每个页面只保留一条。
3. 攻击只在推理时修改输入、且不产生持久污染或条件后门的普通越狱和对抗样本不收录。
4. 各子领域页面同时收攻击、检测、溯源和防御论文，但必须用独立小节和分表呈现；基础攻击框架、Survey 与 Benchmark 另设小节。
5. 固定或结构化知识库中的 corpus／topology poisoning 进入 RAG；动态开放网页中以完整 search loop、证据综合或 research trajectory 为主要目标的操纵进入 Search Agent；以生成式搜索的可见性、ranking、citation、recommendation 或 misinformation 传播为主要目标的工作进入 GEO Security。
