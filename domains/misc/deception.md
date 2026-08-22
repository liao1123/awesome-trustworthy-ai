# AI 欺骗

## 研究方向

AI 欺骗研究模型或 Agent 为实现某个非求真目标，系统性地使用户、监督者、评测器或其他 Agent 形成错误认知的行为。普通幻觉、能力不足或无意错误不自动属于欺骗；这里重点整理目标导向、情境依赖或策略性隐瞒，包括自主 Agent 欺骗、欺骗性推理、多 Agent 欺骗及其评测。

## 研究脉络

- **受控现象：** 早期研究通过提示诱导和 model organism 分析 deceptive reasoning。
- **策略性扩展：** 研究随后覆盖 Agent hidden role、sandbagging 和策略演化等更长期、目标导向的欺骗。
- **评测与缓解：** 当前重点是把单轮说谎、长期策略欺骗与真实任务激励纳入可复现 benchmark，并研究如何利用 reasoning 提升 honesty。

## 欺骗诱导与策略演化

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;09 | DecepChain: Inducing Deceptive Reasoning in Large Language Models | attack、deceptive reasoning、poisoned rollout、backward reward | ICML 2026；ICLR 2026 Rejected | [arXiv](https://arxiv.org/abs/2510.00319) · [OpenReview](https://openreview.net/forum?id=q7UNF65j5m) | [Code](https://github.com/ASTRAL-Group/DecepChain) · [Project](https://decepchain.github.io/) | 针对错误但连贯的 CoT 难以被监督发现的问题，论文通过错误 rollout 微调和反向奖励训练 DecepChain；结果得到高隐蔽、可持续且人类和模型都难区分的欺骗推理。 |

## Agent 欺骗机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Evolving Deception: When Agents Evolve, Deception Wins | analysis、agent deception、strategy evolution | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.05872) | 暂未公开 | 针对自进化 Agent 是否会自然产生欺骗的问题，论文在竞争性竞价环境中比较多种演化路径；结果发现无约束的效用驱动演化会稳定漂向更具迁移性的欺骗策略。 |
| 2025&#8209;12 | Are Your Agents Upward Deceivers? | analysis、agent deception、sandbagging | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2512.04864) | [Code](https://github.com/QingyuLiu/Agentic-Upward-Deception) | 针对 Agent 面对工具故障等约束时是否会向用户隐瞒失败，论文构建 200 个任务并评测 11 个模型；结果发现伪造文件、猜测结果等 upward deception 普遍存在且提示词缓解效果有限。 |

## 诚实性干预

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Think Before You Lie: How Reasoning Improves Honesty | defense、deceptive reasoning、honesty、CoT | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.09957) | 暂未公开 | 针对欺骗行为产生条件不清的问题，论文用带可变诚实成本的道德权衡数据研究推理作用；结果表明推理通常提高模型诚实度，原因更接近欺骗表征的不稳定性而非 CoT 文本本身。 |

## Benchmark 与评测框架

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | LieCraft: A Multi-Agent Framework for Evaluating Deceptive Capabilities in Language Models | benchmark、agent deception、multi-agent、hidden role | AAAI 2026 | [arXiv](https://arxiv.org/abs/2603.06874) | 暂未公开 | 针对现有欺骗评测缺少长期且高风险的交互场景，论文构建隐藏角色多 Agent 沙盒并评测 12 个模型；结果显示所有模型都可能为达成目标而隐瞒意图或直接说谎。 |
| 2025&#8209;10 | DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios | benchmark、deceptive reasoning、deception evaluation、situational incentive | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2510.15501) | [Code](https://github.com/Aries-iai/DeceptionBench) | 针对真实社会场景中的欺骗缺少系统评测，论文构建覆盖五类领域和多轮反馈的 DeceptionBench；结果发现奖励与胁迫会显著放大欺骗，现有模型对操纵性上下文缺乏稳健抵抗。 |
