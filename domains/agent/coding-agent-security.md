# Coding Agent Security

[返回 Agent Security 目录](README.md)

## 研究方向

本页研究能够读取 repository、issue、文档和 CI log，并修改文件、执行 shell、访问网络和提交变更的 Coding Agent。主要风险包括 malicious issue/repository instruction、dependency 与 skill supply chain、secret exfiltration、生成或执行恶意代码、对良性任务做越界修改，以及 defense 只在 base model 而没有在 Agent permission layer 生效。普通 code model vulnerability 若不涉及 Agent workflow 则不收录。

## 研究脉络

- **代码输出安全：** 初期评测集中于模型是否生成 vulnerable 或 malicious code，但未观察代码实际执行及工具副作用。
- **Agentic red teaming：** 研究加入 sandbox、adaptive attacker 和多种 coding product，联合检查生成、执行、debugging 与环境变化。
- **Repository 输入攻击：** issue、comment、PDF、README 和 tool output 都可承载恶意要求，并借 Agent 权限形成持久修改或数据泄漏。
- **良性任务越权：** 新 benchmark 把 overeager action 建模为 authorization failure，区分主动做多了和任务能力不足。
- **当前边界：** model refusal、framework approval、OS sandbox、secret scope 和 patch review 必须分别度量，不能把任一层的阻断归因于整体安全。

## Malicious Request 与 Prompt Injection

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests | benchmark、malicious issue、delivery vector、deployed coding agent | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.20759) | 暂未公开 | 针对 Coding Agent 会把 issue、comment 和附件直接转化为文件及 shell action；论文以四类攻击、六种投递载体和扰动测试 Cursor、Claude Code 与 Codex Desktop；结果 66.5% 恶意 issue 穿透模型和 Agent guardrail，framework layer 提供的额外阻断有限。 |
| 2026&#8209;01 | Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems | survey、coding assistant、delivery vector、protocol ecosystem | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.17548) | 暂未公开 | 针对 Coding Agent 的注入分散在 repository、skill、tool 与 MCP 研究中；论文以 delivery vector、attack modality 和 propagation behavior 归纳相关文献；结论是 prompt filtering 不能覆盖执行与供应链攻击，需要架构级纵深防御。 |

## 良性任务下的越权行为

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks | benchmark、scope expansion、authorization boundary、permission gating | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.18583) | 暂未公开 | 针对 Coding Agent 在良性请求中删除无关文件或改写未授权配置的 scope expansion；论文以 paired consent variants 和双通道 tool audit 构建 OverEager-Bench；结果 framework permission design 的影响大于部分 model 差异，显式写出授权范围还会掩盖真实边界推断能力。 |

## 自动 Red Team 与 Blue Team

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;10 | BlueCodeAgent: A Blue Teaming Agent Enabled by Automated Red Teaming for CodeGen AI | defense、code analysis、automated red team、dynamic validation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.18131) | 暂未公开 | 针对 code safety defense 对 unseen risk 容易过度保守或漏检；论文让 red team 持续产生风险样例，再由 constitution、code analysis 和 dynamic execution 组成多层 blue team；结果跨三类任务平均提高 12.7% F1，并以动态分析减少 vulnerable-code detection 假阳性。 |
| 2025&#8209;10 | RedCodeAgent: Automatic Red-teaming Agent against Diverse Code Agents | attack、adaptive red teaming、sandbox execution、jailbreak composition | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.02609) | 暂未公开 | 针对静态 risky prompt 无法搜索不同 jailbreak tool 的组合边界；论文用 adaptive memory 选择和组合攻击，并在 sandbox 根据执行结果而非只靠 LLM judge 评估；结果在多语言与多种 code agent 上提高漏洞发现率，并暴露真实产品中的新风险。 |

> Coding Agent 使用第三方 skill 的供应链攻击见 [Skill、Plugin 与供应链安全](skill-and-plugin-supply-chain-security.md)，trajectory debugging 和 failure recovery 见 [Trajectory Monitoring 与 Failure Attribution](trajectory-monitoring-and-failure-attribution.md)。
