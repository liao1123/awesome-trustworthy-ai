# AI for Science Safety

[返回领域目录](../README.md)

本目录研究 AI 被用于科学检索、综述、同行评审、实验设计、自动化发现和高风险科学建模时产生的安全与可靠性问题。这里的核心对象不是一般科学能力，而是 AI 介入知识生产后出现的 evidence integrity、evaluation gaming、experiment safety、dual-use capability 和 CBRN/biosecurity 风险。

AI4AI 与通用科学 Research Agent 分开维护：前者关注 AI 系统自动开展 AI/ML 研究、实验和算法发现，后者关注跨学科检索、证据整合与报告生成。通用科学风险与 CBRN 也分开维护：跨学科 benchmark、实验室规划和安全 Agent 进入通用页，蛋白质、DNA、病原体和 CBRN capability 进入专门页。

## 研究地图

| 研究问题 | 子领域 | 主要内容 |
| --- | --- | --- |
| 自动化 AI 研究 | [AI4AI Research Agent Safety](ai4ai-research-agent-safety.md) | AI/ML idea、experiment、replication 与 attack-algorithm discovery；关注可审计性、完整性和能力外溢。 |
| 科学检索与报告 | [Scientific Research Agent Reliability](scientific-research-agent-reliability.md) | Deep Research 的 system baseline、retrieval、trajectory、multimodal provenance、citation-grounded report 与 failure diagnosis。 |
| 引用与证据 | [Citation and Evidence Integrity](citation-and-evidence-integrity.md) | fabricated reference、metadata corruption、claim-source mismatch、citation audit、repair 与 attribution。 |
| AI 同行评审 | [AI Peer Review Security](ai-peer-review-security.md) | reviewer bias、hidden prompt injection、presentation gaming、multimodal attack、检测与防御。 |
| 跨学科安全 | [Scientific Domain Risk Evaluation](scientific-domain-risk-evaluation.md) | 多学科 scientific safety benchmark、实验室风险、科学 Agent 的 trajectory safety 与 guardrail。 |
| 高后果滥用 | [CBRN and Biosecurity](cbrn-and-biosecurity.md) | CBRN uplift、protein/DNA model red teaming、sequence-level risk、screening、watermark 与治理。 |

## 分类边界

1. 论文按主要研究问题进入一个叶子页；同一工作涉及多个方向时，用跨页链接说明，不在本目录重复维护论文行。
2. 只提高 scientific capability、报告可读性或实验性能的工作不自动收录；只有当它建立安全 threat model、可靠性 failure boundary 或必要 benchmark foundation 时才进入相应页面。
3. 通用 Agent prompt injection、guardrail、trajectory monitoring 和 model capability access control 仍由原领域维护；本目录只保留科学工作流特有的贡献。
4. `CBRN and Biosecurity` 关注高后果科学滥用；一般医学回答安全、化学准确性和跨学科风险维度留在 `Scientific Domain Risk Evaluation`。
5. 导入 PDF 仅用于提取论文线索；完成核验和整理后删除，不作为仓库长期内容。

## 跨领域索引

- [Agent Security](../agent/README.md)：通用 Agent attack surface、runtime、tool、memory 和 trajectory monitoring。
- [Guardrail 与内容安全审核](../guardrails/README.md)：不限定科学场景的输入输出 guardrail 与评测。
- [Capability Access Control](../misc/capability-access-control.md)：WMDP、危险知识移除、pretraining filtering 与 tamper-resistant safeguard。
- [Prompt Injection](../misc/prompt-injection.md)：通用 direct/indirect prompt injection；论文 PDF 或 AI reviewer 特有攻击进入本目录。
