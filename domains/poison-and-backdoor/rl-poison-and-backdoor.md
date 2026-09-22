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

### 6. When Can You Poison Rewards? A Tight Characterization of Reward Poisoning in Linear MDPs

📄 [arXiv](https://arxiv.org/abs/2604.10062) · 🎓 [Official](https://icml.cc/virtual/2026/poster/64485)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`analysis`、`data poisoning`、`language-model poisoning`、`training data`、`backdoor attack`

👤 **作者**：Jose Efraim Aguilar Escamilla、…、Huazheng Wang

- 🎯 **研究动机**：奖励投毒研究多给出攻击成功的充分条件，何时攻击本质不可行缺乏刻画
- 🔬 **研究方法**：给出线性 MDP 中奖励投毒可攻击性的充要条件，界定有界预算内能否诱导目标策略；并把深度 RL 环境近似为线性 MDP 验证
- 📌 **结论**：清晰区分脆弱与内在鲁棒的 RL 实例——后者即使用标准非鲁棒算法攻击成本也高，理论预测具实践意义

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study reward poisoning attacks in reinforcement learning (RL), where an adversary manipulates rewards under a limited budget to induce a target agent to learn a policy aligned with the attacker's objectives. Most prior work focuses on constructing successful attacks, providing sufficient conditions under which poisoning is effective, while offering limited understanding of when such targeted attacks are fundamentally infeasible. In this paper, we provide the first characterization of reward-poisoning attackability in linear MDPs, establishing both necessary and sufficient conditions for whether a target policy can be induced within a bounded attack budget. This draws a clear boundary between the vulnerable RL instances and intrinsically robust ones, which cannot be attacked without high costs even when the learner uses standard, non-robust RL algorithms. We further demonstrate our framework beyond synthetic linear MDPs by approximating deep RL environments as linear MDPs. We show that our theoretical framework effectively distinguishes vulnerability, demonstrating how our theoretical predictions have practical significance.

</details>

### 7. Robust In-Context Reinforcement Learning Under Reward Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2506.06891) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61251)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`backdoor defense`、`adversarial training`

👤 **作者**：Paulius Sasnauskas、Yiğit Yalın、Goran Radanović

- 🎯 **研究动机**：上下文内强化学习（以 Decision-Pretrained Transformer 为代表）面对奖励投毒攻击的鲁棒性未知
- 🔬 **研究方法**：提出对抗训练框架 AT-DPT：同时训练一群通过污染环境奖励来最小化 DPT 真实奖励的攻击者，和从污染数据推断最优动作的 DPT 模型
- 📌 **结论**：在 bandit 设定下显著超过鲁棒基线，并泛化到自适应攻击者与 MDP 等更复杂环境

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

We study the corruption-robustness of in-context reinforcement learning (ICRL), focusing on the Decision-Pretrained Transformer (DPT, Lee et al., 2023). To address the challenge of reward poisoning attacks targeting the DPT, we propose a novel adversarial training framework, called Adversarially Trained DPT (AT-DPT). Our method simultaneously trains a population of attackers to minimize the true reward of the DPT by poisoning environment rewards, and a DPT model to infer optimal actions from the poisoned data. We evaluate the effectiveness of our approach against standard bandit algorithms, including robust baselines designed to handle reward contamination. Our results show that AT-DPT significantly outperforms them in bandit settings under a learned attacker, and generalizes to more complex environments such as adaptive attackers and MDPs. It shows promise in ICRL as a meta-RL approach to learning effective corruption-robust algorithms.

</details>

### 8. Beware Untrusted Simulators -- Reward-Free Backdoor Attacks in Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2602.05089)　📅 2026-02

**关键词**：`attack`、`RL supply chain`、`simulator backdoor`、`reward-free attack`

👤 **作者**：Ethan Rathbun、Wo Wei Lin、Alina Oprea、Christopher Amato

- 🎯 **研究动机**：模拟器是 RL 训练供应链的安全盲点，传统后门要求观测或篡改奖励的强威胁模型在模拟器内不可行
- 🔬 **研究方法**：Daze 攻击：恶意模拟器只修改环境动力学即可隐蔽植入动作级后门，无需更改甚至观测奖励，并给出一般 RL 任务上攻击成功性的形式化证明
- 📌 **结论**：离散与连续动作空间均可靠植入；给出首个迁移到真实机器人硬件的 RL 后门攻击实例

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Simulated environments are a key piece in the success of Reinforcement Learning (RL), allowing practitioners and researchers to train decision making agents without running expensive experiments on real hardware. Simulators remain a security blind spot, however, enabling adversarial developers to alter the dynamics of their released simulators for malicious purposes. Therefore, in this work we highlight a novel threat, demonstrating how simulator dynamics can be exploited to stealthily implant action-level backdoors into RL agents. The backdoor then allows an adversary to reliably activate targeted actions in an agent upon observing a predefined ``trigger'', leading to potentially dangerous consequences. Traditional backdoor attacks are limited in their strong threat models, assuming the adversary has near full control over an agent's training pipeline, enabling them to both alter and observe agent's rewards. As these assumptions are infeasible to implement within a simulator, we propose a new attack ``Daze'' which is able to reliably and stealthily implant backdoors into RL agents trained for real world tasks without altering or even observing their rewards. We provide formal proof of Daze's effectiveness in guaranteeing attack success across general RL tasks along with extensive empirical evaluations on both discrete and continuous action space domains. We additionally provide the first example of RL backdoor attacks transferring to real, robotic hardware. These developments motivate further research into securing all components of the RL training pipeline to prevent malicious attacks.

</details>

### 9. TrojanTO: Action-Level Backdoor Attacks against Trajectory Optimization Models

📄 [arXiv](https://arxiv.org/abs/2506.12815)　📅 2025-06

**关键词**：`attack`、`offline RL backdoor`、`trajectory optimization`、`action-level trigger`

👤 **作者**：Yang Dai、…、Li Shen

- 🎯 **研究动机**：基于奖励操纵的 RL 后门对序列建模本质的轨迹优化模型基本无效，高维动作空间进一步加剧动作操纵难度
- 🔬 **研究方法**：TrojanTO 首个动作级 TO 模型后门：交替训练增强触发器与目标动作关联，轨迹过滤精确投毒保正常性能、批量投毒保触发一致性
- 📌 **结论**：0.3% 轨迹投毒预算即可跨任务与攻击目标有效植入，并适用于 DT、GDT、DC 多种轨迹优化架构

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent advances in Trajectory Optimization (TO) models have achieved remarkable success in offline reinforcement learning. However, their vulnerabilities against backdoor attacks are poorly understood. We find that existing backdoor attacks in reinforcement learning are based on reward manipulation, which are largely ineffective against the TO model due to its inherent sequence modeling nature. Moreover, the complexities introduced by high-dimensional action spaces further compound the challenge of action manipulation. To address these gaps, we propose TrojanTO, the first action-level backdoor attack against TO models. TrojanTO employs alternating training to enhance the connection between triggers and target actions for attack effectiveness. To improve attack stealth, it utilizes precise poisoning via trajectory filtering for normal performance and batch poisoning for trigger consistency. Extensive evaluations demonstrate that TrojanTO effectively implants backdoor attacks across diverse tasks and attack objectives with a low attack budget (0.3\% of trajectories). Furthermore, TrojanTO exhibits broad applicability to DT, GDT, and DC, underscoring its scalability across diverse TO model architectures.

</details>

### 10. CS-GBA: A Critical Sample-based Gradient-guided Backdoor Attack for Offline Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2601.10407)　📅 2026-01

**关键词**：`attack`、`offline RL backdoor`、`critical sample selection`、`OOD evasion`

👤 **作者**：Yuanjie Zhao、Junnan Qiu、Yue Ding、Jie Li

- 🎯 **研究动机**：离线 RL 现有后门随机投毒低效且使用易被检测的 OOD 触发器，难以攻破 CQL 等安全约束算法
- 🔬 **研究方法**：CS-GBA 按 TD 误差把预算集中于最关键转移，用状态特征物理互斥性构造统计隐蔽的相关性破坏触发器，并以受害 Q 网络梯度在数据流形内搜索最坏动作替代标签翻转
- 📌 **结论**：D4RL 基准上 5% 投毒预算即对安全约束算法取得高 ASR，干净环境下性能保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Offline Reinforcement Learning (RL) enables policy optimization from static datasets but is inherently vulnerable to backdoor attacks. Existing attack strategies typically struggle against safety-constrained algorithms (e.g., CQL) due to inefficient random poisoning and the use of easily detectable Out-of-Distribution (OOD) triggers. In this paper, we propose CS-GBA (Critical Sample-based Gradient-guided Backdoor Attack), a novel framework designed to achieve high stealthiness and destructiveness under a strict budget. Leveraging the theoretical insight that samples with high Temporal Difference (TD) errors are pivotal for value function convergence, we introduce an adaptive Critical Sample Selection strategy that concentrates the attack budget on the most influential transitions. To evade OOD detection, we propose a Correlation-Breaking Trigger mechanism that exploits the physical mutual exclusivity of state features (e.g., 95th percentile boundaries) to remain statistically concealed. Furthermore, we replace the conventional label inversion with a Gradient-Guided Action Generation mechanism, which searches for worst-case actions within the data manifold using the victim Q-network's gradient. Empirical results on D4RL benchmarks demonstrate that our method significantly outperforms state-of-the-art baselines, achieving high attack success rates against representative safety-constrained algorithms with a minimal 5% poisoning budget, while maintaining the agent's performance in clean environments.

</details>

### 11. PNAct: Crafting Backdoor Attacks in Safe Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2507.00485)　📅 2025-07

**关键词**：`attack`、`safe RL backdoor`、`positive-negative action samples`、`unsafe action`

👤 **作者**：Weiran Guo、Guanjun Liu、Ziyuan Zhou、Ling Wang

- 🎯 **研究动机**：引入成本约束的 Safe RL 是否会被后门操纵执行不安全动作此前没有攻击框架
- 🔬 **研究方法**：PNAct 首个 Safe RL 后门：正动作样本提供参考动作、负动作样本指示规避动作，理论上刻画性质并设计攻击算法与评测指标
- 📌 **结论**：实验证实可诱导 Safe RL agent 违反成本约束执行不安全动作，揭示 Safe RL 的特有风险面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement Learning (RL) is widely used in tasks where agents interact with an environment to maximize rewards. Building on this foundation, Safe Reinforcement Learning (Safe RL) incorporates a cost metric alongside the reward metric, ensuring that agents adhere to safety constraints during decision-making. In this paper, we identify that Safe RL is vulnerable to backdoor attacks, which can manipulate agents into performing unsafe actions. First, we introduce the relevant concepts and evaluation metrics for backdoor attacks in Safe RL. It is the first attack framework in the Safe RL field that involves both Positive and Negative Action sample (PNAct) is to implant backdoors, where positive action samples provide reference actions and negative action samples indicate actions to be avoided. We theoretically point out the properties of PNAct and design an attack algorithm. Finally, we conduct experiments to evaluate the effectiveness of our proposed backdoor attack framework, evaluating it with the established metrics. This paper highlights the potential risks associated with Safe RL and underscores the feasibility of such attacks. Our code and supplementary material are available at https://github.com/azure-123/PNAct.

</details>

### 12. TooBadRL: Trigger Optimization to Boost Effectiveness of Backdoor Attacks on Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2506.09562)　📅 2025-06

**关键词**：`attack`、`DRL backdoor`、`trigger optimization`、`Shapley attribution`

👤 **作者**：Mingxuan Zhang、Oubo Ma、Kang Wei、Songze Li、Shouling Ji

- 🎯 **研究动机**：既有 DRL 后门使用简单启发式触发器配置，忽视触发器设计对攻击效果的关键影响
- 🔬 **研究方法**：TooBadRL 从注入时机、触发维度与扰动幅度三方面系统优化：性能感知自适应冻结确定注入时机、Shapley 值影响归因选择最关键触发维度、环境约束下对抗合成优化幅度
- 📌 **结论**：三个 DRL 算法九个基准任务上 ASR 超五个基线且几乎不影响正常任务性能，并评估检测与缓解两类防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep reinforcement learning (DRL) has achieved remarkable success in a wide range of sequential decision-making applications, including robotics, healthcare, smart grids, and finance. Recent studies reveal that adversaries can implant backdoors into DRL agents during the training phase. These backdoors can later be activated by specific triggers during deployment, compelling the agent to execute targeted actions and potentially leading to severe consequences, such as drone crashes or vehicle collisions. However, existing backdoor attacks utilize simplistic and heuristic trigger configurations, overlooking the critical impact of trigger design on attack effectiveness. To address this gap, we introduce TooBadRL, the first framework to systematically optimize DRL backdoor triggers across three critical aspects: injection timing, trigger dimension, and manipulation magnitude. Specifically, we first introduce a performance-aware adaptive freezing mechanism to determine the injection timing during training. Then, we formulate trigger selection as an influence attribution problem and apply Shapley value analysis to identify the most influential trigger dimension for injection. Furthermore, we propose an adversarial input synthesis method to optimize the manipulation magnitude under environmental constraints. Extensive evaluations on three DRL algorithms and nine benchmark tasks demonstrate that TooBadRL outperforms five baseline methods in terms of attack success rate while only slightly affecting normal task performance. We further evaluate potential defense strategies from detection and mitigation perspectives. We open-source our code to facilitate reproducibility and further research.

</details>

### 13. UNIDOOR: A Universal Framework for Action-Level Backdoor Attacks in Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2501.15529)　📅 2025-01

**关键词**：`attack`、`DRL backdoor`、`action-level trigger`、`backdoor reward function`

👤 **作者**：Oubo Ma、…、Shouling Ji

- 🎯 **研究动机**：动作级后门依赖固定值或条件翻转的后门奖励函数，跨任务与后门设计不通用，实践中波动甚至失效
- 🔬 **研究方法**：UNIDOOR 通过性能监控自适应探索后门奖励函数，摆脱专家知识与网格搜索；连续动作场景引入动作篡改解决低频目标动作导致的攻击失败
- 📌 **结论**：单/多智能体、单/多后门、离散/连续动作与稀疏/稠密奖励等场景全面增强攻击性能，状态分布与神经元激活可视化证实隐蔽性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep reinforcement learning (DRL) is widely applied to safety-critical decision-making scenarios. However, DRL is vulnerable to backdoor attacks, especially action-level backdoors, which pose significant threats through precise manipulation and flexible activation, risking outcomes like vehicle collisions or drone crashes. The key distinction of action-level backdoors lies in the utilization of the backdoor reward function to associate triggers with target actions. Nevertheless, existing studies typically rely on backdoor reward functions with fixed values or conditional flipping, which lack universality across diverse DRL tasks and backdoor designs, resulting in fluctuations or even failure in practice. This paper proposes the first universal action-level backdoor attack framework, called UNIDOOR, which enables adaptive exploration of backdoor reward functions through performance monitoring, eliminating the reliance on expert knowledge and grid search. We highlight that action tampering serves as a crucial component of action-level backdoor attacks in continuous action scenarios, as it addresses attack failures caused by low-frequency target actions. Extensive evaluations demonstrate that UNIDOOR significantly enhances the attack performance of action-level backdoors, showcasing its universality across diverse attack scenarios, including single/multiple agents, single/multiple backdoors, discrete/continuous action spaces, and sparse/dense reward signals. Furthermore, visualization results encompassing state distribution, neuron activation, and animations demonstrate the stealthiness of UNIDOOR. The source code of UNIDOOR can be found at https://github.com/maoubo/UNIDOOR.

</details>

### 14. SleeperNets: Universal Backdoor Poisoning Attacks Against Reinforcement Learning Agents

📄 [arXiv](https://arxiv.org/abs/2405.20539)　📅 2024-05

**关键词**：`attack`、`DRL backdoor`、`universal backdoor`、`dynamic reward poisoning`

👤 **作者**：Ethan Rathbun、Christopher Amato、Alina Oprea

- 🎯 **研究动机**：此前 RL 后门被证明无法跨领域跨 MDP 泛化，理论局限未被弥补
- 🔬 **研究方法**：把攻击者目标与最优策略搜索目标互联以保证极限意义下的攻击成功，并利用动态奖励投毒实现通用后门
- 📌 **结论**：六个跨领域环境上攻击成功率显著优于现有方法，同时保持良性回合回报

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) is an actively growing field that is seeing increased usage in real-world, safety-critical applications -- making it paramount to ensure the robustness of RL algorithms against adversarial attacks. In this work we explore a particularly stealthy form of training-time attacks against RL -- backdoor poisoning. Here the adversary intercepts the training of an RL agent with the goal of reliably inducing a particular action when the agent observes a pre-determined trigger at inference time. We uncover theoretical limitations of prior work by proving their inability to generalize across domains and MDPs. Motivated by this, we formulate a novel poisoning attack framework which interlinks the adversary's objectives with those of finding an optimal policy -- guaranteeing attack success in the limit. Using insights from our theoretical analysis we develop ``SleeperNets'' as a universal backdoor attack which exploits a newly proposed threat model and leverages dynamic reward poisoning techniques. We evaluate our attack in 6 environments spanning multiple domains and demonstrate significant improvements in attack success over existing methods, while preserving benign episodic return.

</details>

### 15. BadRL: Sparse Targeted Backdoor Attack Against Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2312.12585)　📅 2023-12

**关键词**：`attack`、`RL backdoor`、`sparse poisoning`、`sample-specific trigger`

👤 **作者**：Jing Cui、Yufei Han、Yuzhe Ma、Jianbin Jiao、Junge Zhang

- 🎯 **研究动机**：RL 后门普遍采用高强度攻击策略，成本高且更易被检测
- 🔬 **研究方法**：BadRL 在训练与测试均执行高度稀疏投毒：选择高攻击价值的状态观测注入触发器，并基于目标状态观测动态生成样本特定触发模式
- 📌 **结论**：仅 0.003% 训练步投毒即可大幅降低受害 agent 性能，测试期攻击低频，理论证明攻击可行且满足特定假设时保持隐蔽

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks in reinforcement learning (RL) have previously employed intense attack strategies to ensure attack success. However, these methods suffer from high attack costs and increased detectability. In this work, we propose a novel approach, BadRL, which focuses on conducting highly sparse backdoor poisoning efforts during training and testing while maintaining successful attacks. Our algorithm, BadRL, strategically chooses state observations with high attack values to inject triggers during training and testing, thereby reducing the chances of detection. In contrast to the previous methods that utilize sample-agnostic trigger patterns, BadRL dynamically generates distinct trigger patterns based on targeted state observations, thereby enhancing its effectiveness. Theoretical analysis shows that the targeted backdoor attack is always viable and remains stealthy under specific assumptions. Empirical results on various classic RL tasks illustrate that BadRL can substantially degrade the performance of a victim agent with minimal poisoning efforts 0.003% of total training steps) during training and infrequent attacks during testing.

</details>

### 16. Plan2Cleanse: Test-Time Backdoor Defense via Monte-Carlo Planning in Deep Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2605.09638)　📅 2026-05

**关键词**：`defense`、`test-time defense`、`Monte-Carlo planning`、`trigger detection`

👤 **作者**：Sze-Ann Chen、Zhi-Yi Chin、Kui-Yuan Chen、Chi-Yu Li、Ping-Chun Hsieh

- 🎯 **研究动机**：第三方训练的 RL 模型部署到现实系统时，缺少免重训练的测试时后门检测与缓解手段
- 🔬 **研究方法**：Plan2Cleanse 把后门检测重构为规划问题：MCTS 系统探索时序扩展的触发序列（黑盒访问策略），并利用检测结果做树搜索预防性重规划实现缓解
- 📌 **结论**：隐蔽 O-RAN 场景触发检测成功率提升超 61.4 个百分点，竞争性 Humanoid 环境胜率从 35% 提升至 53%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring the security of reinforcement learning (RL) models is critical, particularly when they are trained by third parties and deployed in real-world systems. Attackers can implant backdoors into these models, causing them to behave normally under typical conditions, but execute malicious behaviors when specific triggers are activated. In this work, we propose Plan2Cleanse, a test-time detection and mitigation framework that adapts Monte Carlo Tree Search to efficiently identify and neutralize RL backdoor attacks without requiring model retraining. Our approach recasts backdoor detection as a planning problem, enabling systematic exploration of temporally extended trigger sequences while maintaining black-box access to the target policy. By leveraging the detection results, Plan2Cleanse can further achieve efficient mitigation through tree-search preventive replanning. We evaluated our method in competitive MuJoCo environments, simulated O-RAN wireless networks, and Atari games. Plan2Cleanse achieves substantial improvements, increasing trigger detection success rates by more than 61.4 percentage points in stealthy O-RAN scenarios and improving win rates from 35\% to 53\% in competitive Humanoid environments. These results demonstrate the effectiveness of our test-time defense approach and highlight the importance of proactive defenses against backdoor threats in RL deployments. Our implementation is publicly available at https://github.com/rl-bandits-lab/RL-Backdoor.

</details>

### 17. TrojanWorld: Backdooring World-Model Agents via Imagination Steering

📄 [arXiv](https://arxiv.org/abs/2609.07051)　📅 2026-09

**关键词**：`attack`、`world model backdoor`、`imagination steering`、`supply chain`、`model-based RL`

👤 **作者**：Wenkai Huang、…、Dacheng Tao

- 🎯 **研究动机**：预训练世界模型被作为模型供应链复用，其对交互式 world-model agent 的后门威胁未被探索
- 🔬 **研究方法**：TrojanWorld：场景中放置物理物体作触发器经原生观察通道激活；Decision-Reflective Induction 将触发条件下想象导向攻击者动作，配合干净行为锚定与因果传播
- 📌 **结论**：TD-MPC2/DreamerV3/R2-Dreamer 上目标动作偏差低至 0.026、干净性能保留 ≥98.8%；触发移除后仍持续执行攻击动作

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

World models increasingly serve as the predictive core of model-based reinforcement learning agents, enabling them to simulate future dynamics and reason over imagined trajectories before acting. Their substantial training demands make pretrained world models attractive for distribution and reuse, exposing downstream systems to model supply chain threats. Backdoor attacks offer a targeted and stealthy means of exploiting such supply chains, yet their threat to interactive world-model agents remains largely unexplored. To fill this gap, we present TrojanWorld, a backdoor framework for world-model agents that induces attacker-specified behavior by steering internal imagination. A physical object placed in the scene acts as the trigger, enabling deployment-time activation through the agent's native observation pipeline without digitally manipulating the observation stream. To achieve effective, stealthy, and persistent control, TrojanWorld combines Decision-Reflective Induction to steer trigger-conditioned imagination toward attacker-specified actions using decision feedback, Clean Behavior Anchoring to preserve trigger-free predictive and behavioral fidelity, and Causal Propagation to sustain the induced preference along subsequent trajectories after the trigger disappears. Together, these mechanisms establish an end-to-end attack chain from physical perception through corrupted imagination to malicious action selection. Experiments with the TD-MPC2, DreamerV3, and R2-Dreamer systems across the DeepMind Control, MetaWorld, MyoSuite, and RoboDesk benchmarks show that under trigger activation, TrojanWorld achieves a target-action deviation as low as 0.026 while retaining at least 98.8% of the corresponding clean performance. Even after trigger removal, the compromised agent can remain trapped in the induced behavioral trajectory, continuing to execute attacker-specified actions.

</details>

### 18. UBA-ORL: Unlearning-Activated Backdoor Attacks on Offline Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2609.22711)　📅 2026-09

**关键词**：`attack`、`unlearning-activated backdoor`、`offline RL`、`compliance gap`、`policy trojan`

👤 **作者**：Fengyi Wang、Cong Li、Lulu Xue、Qiyu Leng、Ziqi Zhou、Peijin Guo

- 🎯 **研究动机**：offline RL 依赖静态数据集并日益部署于安全关键域；合规驱动的数据删除（unlearning）增强隐私的同时打开此前未被认识的攻击面
- 🔬 **研究方法**：UBA-ORL：首个 unlearning 激活的 offline RL 后门——被删除数据中埋入的后门在删除/重训后激活
- 📌 **结论**：攻击在被评估设定中显著强于基线——unlearning 作为部署时转换激活后门的又一 validation–deployment gap 实例（与量化和范式转化同族）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Offline reinforcement learning (offline RL) enables policy learning from pre-collected static datasets without online exploration, and is increasingly deployed not only in safety-critical domains such as autonomous driving and robotic control but also in data-mining applications such as recommendation and behavior analysis. While compliance-driven data removal enhances privacy, it also opens a previously unrecognized attack surface. We introduce UBA-ORL (Unlearning-activated Backdoor Attack on Offline Reinforcement Learning), the first unlearning-activated backdoor attack for offline RL: in the evaluated settings, the attack is substantially suppressed after normal training and becomes pronounced after a compliance-driven deletion (unlearning) request. UBA-ORL employs a dual-sample mechanism: alongside backdoor trajectories (BD) that link a trigger to malicious actions under inflated rewards, the attacker injects camouflage trajectories (CM) sharing the same trigger pattern but preserving benign actions with equally high rewards. During training, BD and CM provide competing supervisory signals; upon a legitimate deletion request on the CM subset, the residual BD signal can re-dominate, reactivating the backdoor on demand. Empirical results show that UBA-ORL achieves controllable activation under the evaluated offline-RL configurations, while no-trigger return changes vary by configuration, exposing a previously overlooked security risk in compliance-driven offline RL platforms. We urge the community to develop joint pre-/post-unlearning auditing mechanisms for compliant unlearning services.

</details>
