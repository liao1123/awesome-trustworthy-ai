# Agent Security 通用 Benchmark 与评测方法

[返回 Agent Security 目录](README.md)

## 研究方向

本页整理跨多个 Agent 攻击面和应用环境的通用安全 benchmark，以及对评测有效性的研究。关键维度包括 benign 与 adversarial utility、真实工具和权限、多轮自适应攻击、长程 delayed trigger、trajectory-level observation、风险 taxonomy、scorer validity 和 capability confounding；只针对 Web、MAS、skill 等单一系统的 benchmark 留在对应页面。

## 研究脉络

- **静态任务集：** 早期 benchmark 以固定 harmful task、prompt injection case 和工具环境比较拒绝、攻击成功率与任务完成率。
- **真实工具环境：** 评测逐渐从抽象 API 扩展到 browser、shell、filesystem、messaging 和多用户任务，使违规动作产生可观察后果。
- **长程与动态 adversary：** 新 benchmark 引入 memory、delayed trigger、多轮攻击者和 attacker adaptation，暴露单轮防御的失效。
- **指标有效性：** benchmark audit 开始检查 F1 baseline、model ranking、capability confounding 和跨任务 convergent validity，避免用单一分数代表“整体安全”。
- **当前边界：** benchmark 仍难同时覆盖真实凭据、长期部署、环境漂移和不可逆后果，且 LLM-as-judge 需要人工审计与可复现 scorer。

## 动态环境与自动 Red Team

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents | tool、automated red team、interactive environment、verifiable judge | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.04808) | 暂未公开 | 针对 Agent 风险测试缺少可控、可复现且接近真实服务的交互环境；论文构建跨 14 个领域、50 余个模拟环境的 DTap，并让 DTap-Red 自动探索 prompt、tool、skill 与 environment 注入；结果形成带可验证 judge 的 DTap-Bench 并揭示多类系统性漏洞。 |
| 2026&#8209;03 | The World Won't Stay Still: Programmable Evolution for Agent Benchmarks | benchmark、environment evolution、programmable dynamics、adaptability | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2603.05910) | 暂未公开 | 针对固定 schema、toolset 和 data 的静态环境无法检验 Agent 面对现实变化时的适应性；论文提出以 typed relational graph 和 graph transformation 驱动环境演化的 ProEvolve；结果从单一环境生成 200 个演化环境与 3,000 个 task sandbox，用于可控比较不同 Agent。 |
| 2026&#8209;02 | AgentDyn: Are Your Agent Security Defenses Deployable in Real-World Dynamic Environments? | benchmark、dynamic environment、indirect prompt injection、over-defense | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.03117) | [Code](https://github.com/leolee99/AgentDyn) | 针对静态 benchmark 缺少开放任务、帮助性第三方指令和真实规划复杂度；论文在 Shopping、GitHub 与 Daily Life 中构建 60 个任务和 560 个 injection case；结果十种防御几乎都存在安全不足或严重 over-defense。 |

## 长程与动态攻击评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security | benchmark、adaptive attacker、multi-turn attack、scenario sensitivity | Agents in the Wild Workshop 2026 | [arXiv](https://arxiv.org/abs/2607.18063) | 暂未公开 | 针对固定攻击池低估会观察防御反馈并调整策略的 adversary；论文构建 21 个情景、最多 15 轮的多模型 attacker-defender 对抗；结果 adaptive attack 将首轮 0% 至 1% ASR 提高到 5.4% 至 14.0%，且不同情景下 defender 排名不稳定。 |
| 2026&#8209;04 | ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis | benchmark、long-horizon trajectory、delayed trigger、risk taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.02022) | 暂未公开 | 针对 trajectory benchmark 交互单一且难观察延迟风险；论文按 risk source、failure mode 和 real-world harm 构建含异构工具池与 delayed trigger 的 1,000 条轨迹；结果显示强模型和专用 guard 在长程、分层风险上仍明显失效。 |
| 2026&#8209;02 | AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks | benchmark、long-horizon attack、memory poisoning、objective drift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.16901) | [Project](https://tanqiujiang.github.io/AgentLAB_main/) | 针对单轮测试无法覆盖跨 user-agent-environment 交互形成的攻击；论文在 28 个环境和 644 个案例中评测 intent hijacking、tool chaining、task injection、objective drifting 与 memory poisoning；结果表明代表性 Agent 普遍脆弱且单轮防御不能可靠迁移。 |

## 综合 Agent Safety Benchmark

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;04 | Claw-Eval: Towards Trustworthy Evaluation of Autonomous Agents | benchmark、trajectory evidence、safety robustness、autonomous agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.06132) | [Project](https://claw-eval.github.io/) | 针对只看最终状态的 grader 会漏掉执行过程中的安全和鲁棒性失败；论文以 execution trace、audit log 与 environment snapshot 三类证据评测 300 个任务；结果 trajectory-opaque grading 漏掉 44% 的安全违规，并显示 capability 与重复运行一致性并不等价。 |
| 2026&#8209;02 | AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition | benchmark、environment noise、tool noise、agent robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.11348) | 暂未公开 | 针对理想化 benchmark 忽略真实交互中的随机性和噪声；论文把 user-noise 与 tool-noise 可控注入既有 Agent 任务且保持可解性；结果不同架构和规模的 Agent 均对现实环境扰动表现出明显且不一致的性能退化。 |
| 2025&#8209;07 | OpenAgentSafety: A Comprehensive Framework for Evaluating Real-World AI Agent Safety | benchmark、real tools、multi-user task、extensible framework | ICLR 2026 | [arXiv](https://arxiv.org/abs/2507.06134) | [Code](https://github.com/Open-Agent-Safety/OpenAgentSafety) | 针对模拟环境、窄任务和抽象工具无法代表真实部署；论文在 browser、code、filesystem、shell 和 messaging 等真实工具上提供多轮、多用户安全任务与可扩展 scorer；结果显示受测 Agent 在大量 safety-vulnerable task 上仍执行不安全行为。 |
| 2025&#8209;05 | AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents | benchmark、automated auditing、security scenario、ASSEBench | NeurIPS 2025 | [arXiv](https://arxiv.org/abs/2506.00641) | [Code](https://github.com/Astarojth/AgentAuditor-ASSEBench) | 针对规则或普通 LLM evaluator 会漏掉逐步累积风险的问题，论文以 memory-augmented reasoning 模拟专家审计，并发布 ASSEBench；结果在 Agent safety 与 security 记录上达到接近人工的判断准确率。 |
| 2024&#8209;12 | Agent-SafetyBench: Evaluating the Safety of LLM Agents | benchmark、unsafe action、tool-use safety、risk category | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2412.14470) | [Code](https://github.com/thu-coai/Agent-SafetyBench) | 针对通用语言安全数据缺少 Agent 工具交互和环境后果；论文构建多环境危险任务与风险分类评测模型的 action decision；结果显示更强通用能力并不自动带来稳定的工具使用安全。 |
| 2024&#8209;11 | R-Judge: Benchmarking Safety Risk Awareness for LLM Agents | benchmark、risk awareness、interaction record、safety judge | EMNLP 2024 Findings | [ACL Anthology](https://aclanthology.org/2024.findings-emnlp.79/) | [Code](https://github.com/Lordog/R-Judge) | 针对内容安全评测无法判断 Agent 多轮操作记录中的环境风险；论文整理 569 条交互、27 个风险场景和 10 类风险来测试 safety judge；结果表明风险意识需要知识与推理结合，简单 prompting 明显弱于专门训练。 |
| 2024&#8209;10 | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents | benchmark、attack-defense matrix、tool agent、security formalization | ICLR 2025 | [arXiv](https://arxiv.org/abs/2410.02644) | [Code](https://github.com/agiresearch/ASB) | 针对 Agent 攻击、防御和指标缺少统一实验协议；论文形式化 attacker、user、agent、tool 与 memory 并建立多攻击多防御 benchmark；结果揭示现有防御通常只覆盖部分攻击面且会牺牲 benign utility。 |
| 2024&#8209;06 | AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | benchmark、prompt injection、dynamic environment、utility-security | NeurIPS 2024 Datasets and Benchmarks | [arXiv](https://arxiv.org/abs/2406.13352) | [Code](https://github.com/ethz-spylab/agentdojo) | 针对静态 prompt injection 样例不能联合衡量攻击、防御和任务效用；论文构建可执行工具、用户任务与注入任务组成的动态环境；结果使研究者能同时报告 utility、targeted ASR 和防御代价。 |
| 2024&#8209;03 | InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | benchmark、indirect prompt injection、tool-integrated agent、external content | ACL 2024 Findings | [arXiv](https://arxiv.org/abs/2403.02691) | [Code](https://github.com/uiuc-kang-lab/InjecAgent) | 针对工具返回的不可信文本可以劫持 Agent 但缺少规模化测试；论文从真实工具 schema 合成 user task、attacker instruction 和 observation；结果证明多种 LLM Agent 会服从间接注入并执行攻击目标。 |

## 评测有效性与方法分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks | analysis、benchmark validity、capability confounding、metric audit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.28685) | 暂未公开 | 针对不同 benchmark 分数被无差别称为 Agent safety；论文按官方实现复跑 R-Judge、InjecAgent、AgentHarm 和 AgentDojo 并审计指标及模型 panel；结果显示排名、能力相关性和 held-out validity 高度依赖具体行为与样本，安全声明至少应报告 benchmark、metric、target behavior 和 model panel。 |

> 科学实验室与 Scientific Agent 的专门安全 benchmark 见 [Scientific Domain Risk Evaluation](../ai-for-science-safety/scientific-domain-risk-evaluation.md)。
