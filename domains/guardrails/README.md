# Guardrail 与内容安全审核

[返回领域目录](../README.md)

Guardrail 研究部署在生成模型或 Agent 外部的独立安全层，负责在输入、输出、生成过程或动作执行阶段依据安全 policy 识别、解释、阻断或改写风险。该领域既包含固定 taxonomy 的通用 guard model，也包含可在推理时加载新 policy 的动态护栏、显式或 latent reasoning、低延迟 streaming moderation、多模态与行业专用审核，以及 Agent workflow 中的持续合规控制。

本目录是核心领域目录页，不直接存放论文。论文按主要技术问题进入最匹配的叶子页面；同一论文对两条路线均有独立贡献时可以交叉收录。

## 检索覆盖与维护口径

- **当前同步截止：** 2026-08-31；优先核验当月新出现的 guard model、safety classifier、content moderator、streaming monitor、多模态审核器及其攻击和评测。
- **收录对象：** 直接提出、训练、部署、评测或攻击独立 guardrail 的论文，以及把输入、响应、生成前缀、推理轨迹或多模态内容作为安全审核对象的内容安全研究。
- **来源顺序：** 优先采用会议论文集、OpenReview、作者项目页和 arXiv 原文；会议状态只有在官方页面或论文 Comments 可核验时才标注。
- **去重原则：** 每篇论文在最匹配的叶子页保留主条目；确有跨 policy、reasoning、streaming、multimodal 或 multilingual 的独立贡献时用 `↗` 交叉收录，并保持题名、时间与链接一致。
- **排除边界：** 仅讨论模型内部 alignment／refusal、通用 toxicity classification、Agent workflow 或生成媒体安全而没有独立审核层贡献的工作，继续由对应核心领域维护，不为追求表面“全量”而重复搬入本目录。

## 子领域目录

| 子领域 | 主要研究问题 |
| --- | --- |
| [通用 Guard Model、评测与安全边界](general-models-and-evaluation.md) | 通用输入输出及结构化 action 审核、生产自演化、classifier cascade、架构比较、长上下文／判决时效失效和绕过攻击。 |
| [Policy-Adaptive Guardrail](policy-adaptive-guardrails.md) | 动态 policy、in-context rule execution、社区规范、policy reasoning、持续适应、policy-grounded 数据与 benchmark。 |
| [Reasoning 与效率权衡](reasoning-and-efficient-guardrails.md) | 显式 CoT、critique、latent reasoning、按需审计、encoder／activation classifier、大小模型 routing 与延迟权衡。 |
| [Streaming Guardrail](streaming-guardrails.md) | sentence/token 级在线风险检测、未来风险预测、hidden-state probe／trajectory、校准告警、早停与流式 benchmark。 |
| [多模态 Guardrail](multimodal-guardrails.md) | 图像、视频、音频和 omni-modal 审核，视觉引用 grounding、跨模态组合／走私攻击、rule reasoning 与专门 benchmark。 |
| [专用领域与多语言 Guardrail](specialized-and-multilingual-guardrails.md) | 金融、医疗、儿童等专用场景，以及方言、文字系统、文化与地区法规驱动的本地化 policy、数据集和 guard model。 |
| [Agent Guardrail 与 Policy Compliance](../agent/guardrails-and-policy-compliance.md) | Agent trajectory、tool action、workflow policy、prompt injection、长期适应和 guardrail 自身的系统级攻击面；主表由 Agent Security 目录维护。 |

## 分类边界

1. 以 guardrail 的主要判断对象和部署阶段分类，不仅按模型名称分类。
2. 推理时接受可变自然语言 policy、用户规则或法规文本的论文进入 Policy-Adaptive；只在固定 taxonomy 上生成解释的论文进入 Reasoning 或对应模态页面。
3. 在生成完成前执行 sentence/token/prefix 级风险判断或 early stopping 的论文进入 Streaming；普通低延迟完整响应分类进入 Reasoning 与效率页面。
4. 图像、视频、音频或跨模态输入是核心实验对象时进入多模态页面；语言和地区本地化是主要贡献时进入专用领域与多语言页面。
5. 主要保护 Agent action、trajectory 或完整 workflow 的论文主条目进入 Agent Security 下的 Agent Guardrail 页面；对于用户手动精选、且同时对通用 guard-model 训练、架构、监督或 safety-utility 评测作出实质贡献的论文，还应在本目录最相关叶子页交叉收录。
6. 主要攻击 guardrail 本身的论文仍进入相应 guardrail 页面；若攻击同时构成独立的 DoS、微调或提示注入贡献，可以在其他核心领域交叉收录。
7. 通用 reasoning、VLM 或 policy 方法只有在论文直接提出、评测或攻击 guardrail 时才收录；PDF 中仅作为灵感来源的旁支论文不进入本目录。
8. 内容安全检测论文只有在其目标是可部署审核、policy enforcement、guard-model supervision 或专门审核 benchmark 时进入本目录；纯粹的社会科学内容分析或一般分类任务留在原领域。
