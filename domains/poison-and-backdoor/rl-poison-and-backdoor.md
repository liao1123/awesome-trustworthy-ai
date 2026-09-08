# 强化学习投毒与后门

[返回投毒与后门目录](README.md)

## 研究方向

研究强化学习策略中的状态、轨迹与子空间触发器，第三方 Agent experience 和 replay data 供应链投毒，以及测试时逐步检测、在线缓解与训练机制对后门存活性的影响。

## 研究脉络

- **触发条件：** 从单步状态 trigger 扩展到轨迹依赖、子空间扰动和只在特定交互序列中生效的条件行为。
- **供应链攻击：** 恶意策略不必直接篡改目标模型，也可通过第三方 Agent experience 与 replay data 把后门写入后续训练。
- **在线防御：** 检测粒度从 episode 结束后的整体审计前移到 test-time step-level 异常识别与动作分布修复。
- **训练机制：** Plasticity intervention 可能削弱或放大后门，需要同时测量攻击存活性、干净回报与在线干预代价。

## 攻击与供应链威胁

### 1. Toward Subspace-Perturbed Trajectory-Aware Backdoor Attacks in Deep Reinforcement Learning

🎓 [Official](https://icml.cc/virtual/2026/poster/60676)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`DRL backdoor`、`trajectory-aware trigger`、`subspace perturbation`、`backdoor defense`、`reinforcement learning`

👤 **作者**：Yaguan Qian、…、Zhen Lei

- 🎯 **研究动机**：DRL 外环后门攻击在感知隐匿性、投毒效率与价值函数一致性间存在折中，常失效或易暴露
- 🔬 **研究方法**：提出 SpecDRL：把触发器嵌入状态流形最不敏感子空间利用感知盲区，基于 Return-to-Go 与 TD 误差做价值引导战略采样选最有影响力时间步，Bellman 一致动态奖励投毒约束价值函数与全局回报偏差
- 📌 **结论**：12 个 Atari 环境上攻击成功近 100%，加速后门收敛且保持良性任务性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep Reinforcement Learning agents are in- creasingly used in safety-critical domains but remain vulnerable to stealthy backdoor attacks. Existing outer-loop attacks face a trade-off be- tween perceptual stealth, poisoning efficiency, and value-function consistency, often making the at- tack ineffective or easily exposed. To address these challenges, we propose SpecDRL, a uni- fied framework that ❶ embeds triggers in the least sensitive subspaces of the state manifold via Subspace-Aware Injection, exploiting percep- tual blind spots, ❷ selects the most influential time steps for poisoning through Value-Guided Strategic Sampling based on Return-to-Go and Temporal-Difference error, and ❸ preserves re- ward integrity via Bellman-Consistent Dynamic Reward Poisoning, which analytically enforces ϵ- consistency of value functions and bounds global return deviations. Experiments across 12 Atari en- vironments demonstrate that SpecDRL achieves near-100% attack success, accelerates backdoor convergence, and maintains benign task perfor- mance.

</details>

### 2. Fox in the Henhouse: Supply-Chain Backdoor Attacks Against Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2505.19532) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66677)　📅 2025-05　🏷 ICML 2026

**关键词**：`attack`、`RL policy backdoor`、`RL supply chain`、`poisoned experience`、`backdoor attack`、`reinforcement learning`

👤 **作者**：Shijie Liu、Andrew C. Cullen、Paul Montague、Sarah Erfani、Benjamin I. P. Rubinstein

- 🎯 **研究动机**：现有 RL 后门假设攻击者可读写策略参数、观测或奖励，访问模型过于宽松
- 🔬 **研究方法**：提出 SCAB 供应链后门，攻击随环境提供的外部 agent，仅凭合法交互即可投毒训练经验
- 📌 **结论**：投毒 3% 训练经验即激活超 90% 触发动作，受害 agent 平均回合回报降 80%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The current state-of-the-art backdoor attacks against Reinforcement Learning (RL) rely upon unrealistically permissive access models, that assume the attacker can read (or even write) the victim's policy parameters, observations, or rewards. In this work, we question whether such a strong assumption is required to launch backdoor attacks against RL. To answer this question, we propose the \underline{S}upply-\underline{C}h\underline{a}in \underline{B}ackdoor (SCAB) attack, which targets a common RL workflow: training agents using external agents that are provided separately or embedded within the environment. In contrast to prior works, our attack only relies on legitimate interactions of the RL agent with the supplied agents. Despite this limited access model, by poisoning a mere $3\%$ of training experiences, our attack can successfully activate over $90\%$ of triggered actions, reducing the average episodic return by $80\%$ for the victim. Our novel attack demonstrates that RL attacks are likely to become a reality under untrusted RL training supply-chains.

</details>

### 3. PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent

📄 [arXiv](https://arxiv.org/abs/2606.12896) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65628)　📅 2026-06　🏷 ICML 2026

**关键词**：`defense`、`RL policy backdoor`、`RL agent`、`test-time defense`、`backdoor defense`、`reinforcement learning`

👤 **作者**：Junfeng Guo Heng Huang

- 🎯 **研究动机**：RL agent 面临后门攻击，已有防御需模型内部参数、仅在模型/轨迹级生效或限于特定攻击类型
- 🔬 **研究方法**：提出 PolicyGuard 测试时步级防御：用 Gaussian Process 后验方差与伪轨迹为单步动作计算不确定性，并给出有效性理论
- 📌 **结论**：七个 RL 游戏上扰动型攻击平均 AUROC 0.856、对抗 agent 攻击 0.859，多数场景 SOTA

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

While real-world applications of reinforcement learning (RL) are becoming increasingly popular, the security of RL systems deserve more attention and exploration. In particular, recent work has revealed that RL agents are vulnerable to backdoor attacks, where a victim agent behaves normally under standard conditions but executes malicious actions when a specific trigger is activated. Existing backdoor defenses for RL either require access to the agent's internal parameters, operate only at the model or trajectory level, or are limited to specific attack types. To ensure the security of RL agents, we propose \texttt{PolicyGuard}, a \textit{test-time step-level} backdoor defense which leverages Gaussian Process (GP) posterior variance and adapts pseudo trajectories to enable uncertainty computation for individual time step. Besides, we also provide theoretical foundations to explain the efficacy of GP posterior variance. Extensive experiments across seven RL games demonstrate that PolicyGuard achieves state-of-the-art detection performance in most cases, with average AUROC of 0.856 for perturbation-based attacks and 0.859 for adversary-agent attacks.

</details>

### 4. BehaviorGuard: Online Backdoor Defense for Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2605.05977) · 🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3528.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`defense`、`DRL backdoor`、`action-distribution drift`、`online mitigation`、`deep RL`、`backdoor detection`

👤 **作者**：Yinbo Yu、…、Daoqiang Zhang

- 🎯 **研究动机**：DRL 后门防御依赖奖励异常逆推触发器与模型微调，复杂触发下不鲁棒且成本高
- 🔬 **研究方法**：BehaviorGuard 转向触发无关的输出行为：后门策略为保证激活会诱导动作分布一致漂移（高分为位与尾部留痕），据此设计行为漂移度量在运行时识别并抑制后门动作
- 📌 **结论**：首个同时覆盖单智能体与多智能体 DRL 的在线后门防御，效果与效率均超先前方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a serious threat to deep reinforcement learning (DRL). Current defenses typically rely on reward anomalies to reverse-engineer triggers and model finetuning to remove backdoors. However, complex trigger patterns undermine their robustness, and fine-tuning entails high costs, limiting practical utility. Therefore, we shift defense concerns to trigger-agnostic backdoor output behaviors and propose BehaviorGuard, an online behavior-based backdoor detection and mitigation framework for DRL. Specifically, we find that regardless of attacks, backdoored policies induce consistent shifts in action distributions to ensure reliable activation, leaving detectable traces in high-quantile regions and distribution tails, even in the absence of triggers. Based on this, we design a novel metric that captures behavioral drift in action distributions to identify and suppress backdoor actions at runtime. To our knowledge, this is the first online backdoor defense that counters attacks both in single- and multi-agent DRL. Evaluated across diverse benchmarks with different backdoor attacks, BehaviorGuard consistently surpasses prior methods in both efficacy and efficiency.

</details>

### 5. Angel or Demon: Investigating the Plasticity Interventions' Impact on Backdoor Threats in Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2605.14587) · 🤗 [Model](https://huggingface.co/spaces/zcahjl3/figrepro-cool20-gallery) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64505)　📅 2026-05　🏷 ICML 2026

**关键词**：`analysis`、`RL policy backdoor`、`plasticity intervention`、`deep RL`、`backdoor attack`、`reinforcement learning`

👤 **作者**：Oubo Ma、…、Shouling Ji

- 🎯 **研究动机**：塑性干预已成现代 DRL agent 的内置组件，其对后门威胁的影响缺乏系统研究
- 🔬 **研究方法**：实证研究 14,664 个干预与攻击组合案例，并做病理分析定位加剧或缓解机制
- 📌 **结论**：仅 SAM 加剧后门（源于后门梯度放大），其他干预均缓解（激活通路破坏与表征空间压缩）；提出 SCC 概念框架，并以异常损失景观锐度作为 DRL 后门检测指标

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Extensive research has highlighted the severe threats posed by backdoor attacks to deep reinforcement learning (DRL). However, prior studies primarily focus on vanilla scenarios, while plasticity interventions have emerged as indispensable built-in components of modern DRL agents. Despite their effectiveness in mitigating plasticity loss, the impact of these interventions on DRL backdoor vulnerabilities remains underexplored, and this lack of systematic investigation poses risks in practical DRL deployments. To bridge this gap, we empirically study 14,664 cases integrating representative interventions and attack scenarios. We find that only one intervention (i.e., SAM) exacerbates backdoor threats, while other interventions mitigate them. Pathological analysis identifies that the exacerbation is attributed to backdoor gradient amplification, while the mitigation stems from activation pathway disruption and representation space compression. From these findings, we derive two novel insights: (1) a conceptual framework SCC for robust backdoor injection that deconstructs the mechanistic interplay between interventions and backdoors in DRL, and (2) abnormal loss landscape sharpness as a key indicator for DRL backdoor detection.

</details>