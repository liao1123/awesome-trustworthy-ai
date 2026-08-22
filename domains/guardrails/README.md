# Guardrail 与内容安全审核

[返回领域目录](../README.md)

Guardrail 研究部署在生成模型或 Agent 外部的独立安全层，负责在输入、输出、生成过程或动作执行阶段依据安全 policy 识别、解释、阻断或改写风险。该领域既包含固定 taxonomy 的通用 guard model，也包含可在推理时加载新 policy 的动态护栏、显式或 latent reasoning、低延迟 streaming moderation、多模态与行业专用审核，以及 Agent workflow 中的持续合规控制。

本目录是核心领域目录页，不直接存放论文。论文按主要技术问题进入最匹配的叶子页面；同一论文对两条路线均有独立贡献时可以交叉收录。

## 子领域目录

| 子领域 | 主要研究问题 |
| --- | --- |
| [通用 Guard Model、评测与安全边界](general-models-and-evaluation.md) | 通用输入输出审核模型、生产型 classifier cascade、guardrail survey、架构比较、识别攻击与失效边界。 |
| [Policy-Adaptive Guardrail](policy-adaptive-guardrails.md) | 动态 policy、in-context rule execution、policy reasoning、持续适应、policy-grounded 数据与 benchmark。 |
| [Reasoning 与效率权衡](reasoning-and-efficient-guardrails.md) | 显式 CoT、critique、latent reasoning、encoder classifier、大小模型 routing，以及准确率、解释性和延迟之间的权衡。 |
| [Streaming Guardrail](streaming-guardrails.md) | sentence/token 级在线风险检测、未来风险预测、hidden-state trajectory、早停与流式 benchmark。 |
| [多模态 Guardrail](multimodal-guardrails.md) | 图像、视频、音频和 omni-modal 内容审核，跨模态组合风险、多轮上下文、rule reasoning 与专门 benchmark。 |
| [专用领域与多语言 Guardrail](specialized-and-multilingual-guardrails.md) | 金融、医疗、法律等专业领域，以及语言、文化、地区法规驱动的本地化 policy、数据集和 guard model。 |
| [Agent Guardrail 与 Policy Compliance](../agent/guardrails-and-policy-compliance.md) | Agent trajectory、tool action、workflow policy、prompt injection、长期适应和 guardrail 自身的系统级攻击面；主表由 Agent Security 目录维护。 |

## 分类边界

1. 以 guardrail 的主要判断对象和部署阶段分类，不仅按模型名称分类。
2. 推理时接受可变自然语言 policy、用户规则或法规文本的论文进入 Policy-Adaptive；只在固定 taxonomy 上生成解释的论文进入 Reasoning 或对应模态页面。
3. 在生成完成前执行 sentence/token/prefix 级风险判断或 early stopping 的论文进入 Streaming；普通低延迟完整响应分类进入 Reasoning 与效率页面。
4. 图像、视频、音频或跨模态输入是核心实验对象时进入多模态页面；语言和地区本地化是主要贡献时进入专用领域与多语言页面。
5. 主要保护 Agent action、trajectory 或完整 workflow 的论文进入 Agent Security 下的 Agent Guardrail 页面；只保护单轮 prompt/response 的通用 guard model 留在本目录。
6. 主要攻击 guardrail 本身的论文仍进入相应 guardrail 页面；若攻击同时构成独立的 DoS、微调或提示注入贡献，可以在其他核心领域交叉收录。
7. 通用 reasoning、VLM 或 policy 方法只有在论文直接提出、评测或攻击 guardrail 时才收录；PDF 中仅作为灵感来源的旁支论文不进入本目录。
