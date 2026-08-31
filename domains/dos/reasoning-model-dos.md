# 推理模型 DoS

## 研究方向

推理模型 DoS 研究如何利用 LRM/RLM 的显式思维链、试探回溯、自我反思和任务分解来放大推理开销。与普通 LLM 的重复输出不同，这类攻击通常让模型在得到答案前持续探索错误路径，因此需要同时评估 reasoning token、端到端延迟、吞吐、答案正确率和攻击查询成本。

## 研究脉络

- **问题基础：** Reasoning-model DoS 利用推理预算会随搜索难度和自反思深度增长这一特性。
- **早期方法：** 攻击通过 decoy context 和字符任务延长 CoT，让模型在无效路径上持续推理。
- **自动化与结构化攻击：** 后续方法发展为黑盒优化、递归熵引导和 SMT conflict 驱动的搜索放大。

## 结构化搜索与递归放大

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance | attack、reasoning-model DoS、SMT conflict、search amplification | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.18921) | 暂未公开 | 针对既有 LRM DoS 需要反复查询受害模型或训练专用 attacker，SMTrap 用 SMT solver conflict count 在 CPU 上指导合成高回溯 CSP，无需模型反馈与 GPU；七个前沿模型上的 DoS 效果达到既有基线的数倍，论文同时给出可显著削减 token 用量的 tool-based mitigation。 |
| 2026&#8209;02 | RECUR: Resource Exhaustion Attack via Recursive-Entropy Guided Counterfactual Utilization and Reflection | attack、reasoning-model DoS、recursive entropy、counterfactual question | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.08214) | 暂未公开 | 针对推理模型的反思过程可能无限消耗计算，论文定义 Recursive Entropy 并据此构造反事实问题；结果最高使输出增长 11 倍、吞吐下降 90%。 |
| 2025&#8209;06 | ExtendAttack: Attacking Servers of LRMs via Extending Reasoning | attack、reasoning-model DoS、character obfuscation、decoding task | AAAI 2026 | [Official](https://ojs.aaai.org/index.php/AAAI/article/view/40833) · [arXiv](https://arxiv.org/abs/2506.13737) | [Code](https://github.com/zzh-thu-22/ExtendAttack) | 针对保持语义正常同时延长 LRM 推理，论文把良性提示字符混淆成多进制 ASCII 解码任务；结果在不明显降低答案准确率时显著放大响应长度和延迟。 |

## 黑盒优化与长推理诱导

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Inducing Overthink: Hierarchical Genetic Algorithm-based DoS Attack on Black-Box Large Language Reasoning Models | attack、reasoning-model DoS、hierarchical genetic algorithm、overthinking | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/62234) · [arXiv](https://arxiv.org/abs/2605.13338) | [Code](https://github.com/EndlessCao/Overthink-HGA) | 针对不完整或矛盾问题会触发 LRM 过度思考，论文用分层遗传算法在黑盒下优化逻辑结构；结果最高放大输出 26.1 倍且小代理模型生成的攻击可迁移到商业 LRM。 |
| 2026&#8209;01 | ReasoningBomb: A Stealthy Denial-of-Service Attack by Inducing Pathologically Long Reasoning in Large Reasoning Models | attack、reasoning-model DoS、attack model、proxy reward | CCS 2026 | [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html) · [arXiv](https://arxiv.org/abs/2602.00154) | [Code](https://github.com/SaFo-Lab/ReasoningBomb) | 针对短自然提示也可能诱导高成本推理，论文用常数时间代理奖励训练攻击模型生成 ReasoningBomb；结果平均产生近 1.9 万 reasoning token，并以高比例绕过输入和输出检测。 |
| 2025&#8209;12 | ThinkTrap: Denial-of-Service Attacks against Black-box LLM Services via Infinite Thinking | attack、reasoning-model DoS、continuous subspace、infinite reasoning | NDSS 2026 | [Official](https://www.ndss-symposium.org/ndss-paper/thinktrap-denial-of-service-attacks-against-black-box-llm-services-via-infinite-thinking/) · [arXiv](https://arxiv.org/abs/2512.07086) | 暂未公开 | 针对闭源推理服务仍可能被无限思考拖垮，论文把离散 token 映射到低维连续子空间进行黑盒优化；结果在严格请求频率限制下也能把服务吞吐降至约 1%。 |
| 2025&#8209;02 | OverThink: Slowdown Attacks on Reasoning LLMs | attack、reasoning-model DoS、context injection、decoy question | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2502.02542) | [Code](https://github.com/akumar2709/overthink_public) | 针对依赖外部上下文的推理应用，论文把数独和 MDP 等无害诱饵问题注入公开内容，迫使模型先完成额外推理再回答原问题；结果攻击可跨开闭源及多模态模型迁移，并绕过常规安全过滤。 |

## 攻击与绕过

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems | attack、VLM safety、reasoning DoS、overthinking attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.01518) | 暂未公开 | 论文针对 LVLM 机器人可被输入诱导过度思考而延迟或停止动作的问题构造 slowdown attack，并系统测量推理长度、控制延迟与任务失败；结果表明推理能力增强会形成可被利用的具身可用性攻击面。 |
