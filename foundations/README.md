# Trustworthy AI 基础

Trustworthy AI 不是单一算法问题，而是围绕 AI 系统在真实环境中是否可靠、安全、可解释、可问责、保护隐私且公平的一组技术与社会技术问题。

## 三种互补视角

| 视角 | 核心问题 | 本仓库中的对应内容 |
| --- | --- | --- |
| 系统品质 | 什么样的 AI 值得信任？ | 可靠性、安全、安全防护、透明度、隐私、公平与问责 |
| 风险结果 | AI 会以什么方式造成伤害？ | 恶意使用、系统失效、系统性与社会性风险 |
| 技术干预 | 如何发现并降低风险？ | 对齐、鲁棒性、解释、评测、监控、控制与治理 |

## 建议入门顺序

1. **建立全景**：阅读 [*Artificial Intelligence Risk Management Framework*](../library/README.md#2023-tabassi-ai-rmf) 与 [*The AI Risk Repository*](../library/README.md#2026-slattery-ai-risk-repository)，理解风险与可信特征并不是一一对应的。
2. **进入技术安全**：阅读 [*Concrete Problems in AI Safety*](../library/README.md#2016-amodei-concrete-problems-ai-safety) 和 [*Unsolved Problems in ML Safety*](../library/README.md#2021-hendrycks-unsolved-problems-ml-safety)，掌握 specification、robustness、monitoring、alignment 与 systemic safety。
3. **理解前沿风险**：阅读 [*The Alignment Problem from a Deep Learning Perspective*](../library/README.md#2024-ngo-alignment-problem-deep-learning) 与 [*International AI Safety Report 2026*](../library/README.md#2026-bengio-international-ai-safety-report)。
4. **选择专题路线**：从 [领域地图](../domains/README.md) 进入 alignment、robustness、interpretability、security、privacy、fairness、evaluation 或 governance。
5. **形成自己的证据链**：对重点论文建立 [详细笔记](../papers/README.md)，记录方法、证据、局限、争议和复现状态。

## 阅读难度

| 级别 | 适合读者 |
| --- | --- |
| `foundation` | 初次进入领域，希望建立术语与问题地图 |
| `core` | 已掌握 ML/DL 基础，希望理解代表性方法与证据 |
| `advanced` | 需要追踪专门方向、最新方法或开放问题 |

## 前置知识

建议具备监督学习、深度学习、概率与统计的基本知识。对齐与 agent safety 还需要强化学习基础；privacy 与 security 方向需要威胁模型、攻击者能力和安全评估的基本概念。
