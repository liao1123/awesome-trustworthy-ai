# Safe Reinforcement Learning

[返回上级目录](README.md)

## 研究方向

研究在探索、离线学习和策略优化中满足成本、风险或行为约束的方法，覆盖 constrained MDP、shielding、risk-sensitive objective、safe exploration 和 policy verification。

## 研究脉络

- **约束建模：** Constrained MDP 和 risk-sensitive objective 将安全从奖励附项提升为独立约束。
- **训练与探索：** Shield、backup policy 和 uncertainty-aware exploration 限制训练期间的危险访问。
- **离线与部署：** Offline safe RL、distribution shift 和 policy control 关注数据覆盖不足下的约束泛化。
- **当前边界：** 代理 cost、真实伤害与长期尾部风险之间仍存在 specification gap。

## Offline Safe RL 与 Distribution Shift

### 1. RAMAC: Multimodal Risk-Aware Offline Reinforcement Learning and the Role of Behavior Regularization

📄 [arXiv](https://arxiv.org/abs/2510.02695) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62421)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`VLM safety`、`safe reinforcement learning`、`constraint satisfaction`、`diffusion model`、`risk control`

👤 **作者**：Kai Fukazawa、Kunal Mundada、Iman Soltani

- 🎯 **研究动机**：风险规避型离线 RL 以悲观估计和受限策略类为代价，扩散/流生成策略基本只用于风险中性场景
- 🔬 **研究方法**：提出 RAMAC：生成式 actor（扩散/流）结合分布式 critic，联合优化 CVaR 与行为克隆（BC），用 BC 控制行为散度以抑制 OOD 动作
- 📌 **结论**：在 Stochastic-D4RL 上 CVaR_0.1 持续提升且保持高回报，2D 风险 bandit 上验证了 BC 稳定 CVaR 的机制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In safety-critical domains where online data collection is infeasible, offline reinforcement learning (RL) is attractive only if policies achieve high returns without catastrophic lower-tail risk. Prior work on risk-averse offline RL achieves safety at the cost of value- or model-based pessimism, and restricted policy classes that limit policy expressiveness, whereas diffusion/flow-based expressive generative policies have largely been used in risk-neutral settings. We introduce **Risk-Aware Multimodal Actor-Critic (RAMAC)**, a simple, modular, model-free framework that couples an expressive generative actor (e.g., diffusion/flow) with a distributional critic and optimizes a composite objective that combines Conditional Value-at-Risk (CVaR) with behavioral cloning (BC), enabling risk-sensitive learning in complex multimodal scenarios. Since out-of-distribution (OOD) actions are a major driver of catastrophic failures in offline RL, we further provide an objective-level analysis showing that controlling behavior divergence via BC suppresses OOD actions and stabilizes CVaR. Instantiating RAMAC with a diffusion actor, we illustrate these insights on a 2-D risky bandit and evaluate on Stochastic-D4RL, observing consistent gains in CVaR$_{0.1}$ while maintaining strong returns.

</details>

### 2. Provably Safe Offline-to-Online RL: Decoupling Learning from Data-Driven Safety Enforcement

🎓 [Official](https://aclanthology.org/2026.acl-long.528/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`safety alignment`、`fine-tuning robustness`

👤 **作者**：Kaitong Cai、Jusheng Zhang、Keze Wang

- 🎯 **研究动机**：混合离线-在线 RL 因离线与在线数据分布偏移而不稳定
- 🔬 **研究方法**：RLPD-GX 解耦策略优化与安全执行：奖励学习者自由探索，投影式守护者保证规则一致执行与安全价值备份；动态课程扩展时间视野并退火数据混合，guarded Bellman 算子收缩证收敛
- 📌 **结论**：Atari-100k 归一化均分 3.02（比先前混合方法高 45%），安全性与稳定性更强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Hybrid offline–online reinforcement learning (O2O RL) promises both sample efficiency and robust exploration, but suffers from instability due to distribution shift between offline and online data. We introduce RLPD-GX, a framework that decouples policy optimization from safety enforcement: a reward-seeking learner explores freely, while a projection-based guardian guarantees rule-consistent execution and safe value backups. This design preserves the exploratory value of online interactions without collapsing to conservative policies. To further stabilize training, we propose dynamic curricula that gradually extend temporal horizons and anneal offline–online data mixing. We prove convergence via a contraction property of the guarded Bellman operator, and empirically show state-of-the-art performance on Atari-100k, achieving a normalized mean score of 3.02 (+45% over prior hybrid methods) with stronger safety and stability. Beyond Atari, ablations demonstrate consistent gains across safety-critical and long-horizon tasks, underscoring the generality of our design. Extensive and comprehensive results highlight decoupled safety enforcement as a simple yet principled route to robust O2O RL, suggesting a broader paradigm for reconciling exploration and safety in reinforcement learning.

</details>

### 3. Uncertainty-Guided Adaptive Conservative Offline Reinforcement Learning for Safer Mechanical Ventilation

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4H132.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai-and-health)　📅 2026

**关键词**：`defense`、`offline RL`、`mechanical ventilation`、`uncertainty penalty`

- 🎯 **研究动机**：机械通气常规方案缺乏个性化，离线 RL 又对分布偏移与 OOD 动作高度敏感，复杂临床场景可靠性不足
- 🔬 **研究方法**：提出 UBER-CQL：异方差贝叶斯神经网络结合保守 Q-learning 建模后验 Q 不确定性，自适应惩罚不可靠高风险动作，并设计数值稳定的保守贝叶斯价值估计
- 📌 **结论**：MIMIC-IV 与 eICU 的分布内及 OOD 子集上超越 SOTA 离线 RL 与临床基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mechanical ventilation (MV) is essential in intensive care units (ICUs), yet conventional protocols lack personalization and risk harmful overor under-ventilation. Offline reinforcement learning (ORL) enables policy optimization from retrospective clinical data without unsafe online interaction, but existing methods are highly sensitive to distributional shift and out-of-distribution (OOD) actions, limiting their reliability in complex clinical settings. To address these challenges, we propose UBER-CQL (Uncertainty-Balanced Exploration and Robust Conservative Q-Learning), a robust ORL algorithm for safe decision-making under dataset shift. UBER-CQL integrates heteroscedastic Bayesian neural networks with conservative Q-learning to model posterior Q-value uncertainty, which is used to adaptively penalize unreliable high-risk actions while maintaining performance within the data support. We further design numerically stable objectives for conservative Bayesian value estimation. Experiments on indistribution and OOD subsets of MIMIC-IV and eICU demonstrate that UBER-CQL outperforms state-of-the-art ORL and clinician baselines, producing safer and more effective MV strategies.

</details>

### 4. Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2608.19836)　📅 2026-08

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`

👤 **作者**：Astrid Horn Brorholt、Maris F. L. Galesloot、Nils Jansen、Kim Guldstrand Larsen、Christian Schilling

- 🎯 **研究动机**：概率屏蔽需 MDP 转移概率先验，典型 RL 应用中模型不预先给定
- 🔬 **研究方法**：转移图已知但概率未知时集成在线模型学习：随 agent 探索估计转移概率并据此计算屏蔽，初始保守随估计精确自适应改进
- 📌 **结论**：多环境评估多个变体，屏蔽与 RL agent 同步改进，需权衡屏蔽重算时机与探索-安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov decision process (MDP). Thus, this technique is not applicable when the MDP model is not given a priori, which, unfortunately, is the case in typical RL applications. In this paper, we study the problem of computing a shield in the setting where the transition graph of the MDP is known, but the transition probabilities are unknown. Our approach integrates probabilistic shielding with online model learning: as the RL agent explores the environment, we estimate the transition probabilities. From this estimate, we compute a shield. While the shield may be conservative initially, it adapts as the model estimate becomes more precise. Thus, the shield improves in tandem with the RL agent. This paradigm of adaptive probabilistic shielding raises a number of challenges, such as when to recompute the shield and how to balance between exploration and safety during learning. We empirically evaluate multiple variants of this paradigm across several environments.

</details>

### 5. How Does the Lagrangian Guide Safe Reinforcement Learning through Diffusion Models?

📄 [arXiv](https://arxiv.org/abs/2602.02924) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61858)　📅 2026-02　🏷 ICML 2026

**关键词**：`analysis`、`safe reinforcement learning`、`diffusion model`、`constraint satisfaction`、`risk control`

👤 **作者**：Xiaoyuan Cheng、…、Yukun Hu

- 🎯 **研究动机**：扩散策略 RL 的安全研究集中于离线设定，在线安全 RL 缺方法；原始-对偶方法在不凸 Lagrangian 景观上不稳定
- 🔬 **研究方法**：把 Lagrangian 解释为引导去噪动力学的能量函数，ALGD 引入增广 Lagrangian 局部凸化能量景观，在不改变最优策略分布的情况下稳定生成与训练
- 📌 **结论**：理论与实验均证明其在多样安全 RL 环境中表现强且稳定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion policy sampling enables reinforcement learning (RL) to represent multimodal action distributions beyond suboptimal unimodal Gaussian policies. However, existing diffusion-based RL methods primarily focus on offline settings for reward maximization, with limited consideration of safety in online settings. To address this gap, we propose Augmented Lagrangian-Guided Diffusion (ALGD), a novel algorithm for off-policy safe RL. By revisiting optimization theory and energy-based model, we show that the instability of primal-dual methods arises from the non-convex Lagrangian landscape. In diffusion-based safe RL, the Lagrangian can be interpreted as an energy function guiding the denoising dynamics. Counterintuitively, direct usage destabilizes both policy generation and training. ALGD resolves this issue by introducing an augmented Lagrangian that locally convexifies the energy landscape, yielding a stabilized policy generation and training process without altering the distribution of the optimal policy. Theoretical analysis and extensive experiments demonstrate that ALGD is both theoretically grounded and empirically effective, achieving strong and stable performance across diverse environments.

</details>

### 6. BehaviorGuard: Online Backdoor Defense for Deep Reinforcement Learning

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

### 7. Why Dedicated Critics: Eliminating Target Drift in Multi-Constraint RL

🎓 [Official](https://icml.cc/virtual/2026/poster/62544)　📅 2026　🏷 ICML 2026

**关键词**：`analysis`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`reinforcement learning`、`risk control`

👤 **作者**：Yue Yang、Chenghao Huang、Hao Wang

- 🎯 **研究动机**：Lagrangian 安全 RL 中混合 critic 与专用 critic 结构的理论有效性长期未被探讨
- 🔬 **研究方法**：首次理论证明混合 critic 结构因 Lagrange 乘子目标漂移产生偏差，而奖励与约束分开估计的专用 critic 无此偏差
- 📌 **结论**：多约束电力系统环境中专用 critic 成功满足约束而混合 critic 失败，理论与实验一致

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Lagrangian-based methodologies are one of the fundamental paradigms of safe reinforcement learning (RL) for constrained Markov decision processes, particularly when dealing with multi-constraint cases. While the specific details of the methodologies may differ, with some using a single estimator for the overall mixed penalty term of the constraints and others using separate estimators for the constraints, the fundamental question of the theoretical validity of the methodologies has remained largely unexplored. The present paper performs the first theoretical analysis of the methodologies and proves that the use of the mixed critic structure leads to the presence of a bias due to the target drift of the Lagrange multipliers. On the other hand, the use of the dedicated critic structure, where separate critics are used for the reward function and the constraint functions, does not suffer from this bias. The theoretical analysis is supported with experiments on a realistic power system environment with multiple constraints, where the dedicated critic structure succeeds in satisfying the constraints, whereas the mixed critic structure fails.

</details>

### 8. Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees

🎓 [Official](https://icml.cc/virtual/2026/poster/65815)　📅 2026　🏷 ICML 2026

**关键词**：`tool`、`defense`、`diffusion model`、`safe reinforcement learning`、`constraint satisfaction`、`risk control`

👤 **作者**：Kenta Hoshino、Yashaswi Shashank Aluru、Xiyu Deng、Yorie Nakahira

- 🎯 **研究动机**：连续时间 score 扩散模型的引导机制缺乏统一理论基础，安全关键规划需要约束满足保证
- 🔬 **研究方法**：以 Doob h-transform 刻画理想引导扩散，分析理想与近似引导的偏差并给出显式误差界与约束满足概率保证，导出随机最优控制问题实现免训练引导设计
- 📌 **结论**：在机器人导航任务（含语言条件规划）上验证框架有效性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This paper studies the theoretical foundations of guidance mechanisms in continuous-time score-based diffusion models. We adopt Doob’s h-transform as a principled framework for characterizing ideal guided diffusion processes and analyze the discrepancy between ideal and approximate guidance. Our analysis provides explicit error bounds and yields probabilistic guarantees on satisfying prescribed constraints, which are particularly important for safety-critical planning. We further show that the Doob-based formulation induces a stochastic optimal control problem, enabling practical guidance design without additional model training. We demonstrate the effectiveness of the proposed framework on robotic navigation tasks, including language-conditioned planning.

</details>

### 9. TraCeS: Learning Per-Timestep Constraint-Violation Credit from Sparse Trajectory-Level Labels

📄 [arXiv](https://arxiv.org/abs/2504.12557) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61935)　📅 2026　🏷 ICML 2026

**关键词**：`detection`、`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`reinforcement learning`

👤 **作者**：Siow Meng Low、Ze Gong、Akshat Kumar

- 🎯 **研究动机**：RL 安全约束常为隐式、无法逐步骤度量，监督仅有整条轨迹的粗粒度接受或拒绝标签
- 🔬 **研究方法**：提出 TraCeS：训练逐步骤违约估计器，其信用分解轨迹未违约概率并融入约束策略优化，无需已知代价函数或阈值，兼容标准连续控制算法
- 📌 **结论**：多个连续控制基准（含长时程与噪声标签设置）上改善约束满足与反馈效率，并给出近似差距的理论分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Ensuring safe behavior in reinforcement learning (RL) is challenging when safety constraints are implicit and cannot be densely measured. In many settings, supervision is limited to coarse approvals or rejections of whole trajectories (e.g., whether a rollout remained within an unknown safety threshold). We propose TraCeS (Trajectory-based Constraint Estimation for Safety), a method for learning per-timestep violation credit from such sparse trajectory-level labels. TraCeS trains a sequential violation estimator whose per-step credits factorize the predicted probability that a trajectory has not yet violated the constraint, and integrates this learned signal into constrained policy optimization. The method requires neither a known cost function nor a known threshold, and remains compatible with standard continuous-control algorithms. We provide a theoretical analysis of the approximation gap introduced by the learning objective, and demonstrate empirically that TraCeS improves constraint satisfaction and feedback efficiency over baselines across multiple continuous-control benchmarks, including long-horizon tasks and settings with noisy or inconsistent labels.

</details>

### 10. The Pareto-optimal Trade-off between Regret and Statistical Inference in Linear Stochastic Bandits under Safety Constraints

🎓 [Official](https://icml.cc/virtual/2026/poster/62237)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`mechanistic analysis`、`risk control`

👤 **作者**：Yuming Shao、Zhixuan Fang

- 🎯 **研究动机**：线性 bandit 传统只重 regret 最小化，忽视参数统计推断；医疗等高风险场景需同时权衡 regret、推断与安全三目标
- 🔬 **研究方法**：推导刻画三者 Pareto 最优前沿的 minimax 下界，提出匹配下界并保持近常数 O(1) 安全风险的 SERMiSC 算法
- 📌 **结论**：SERMiSC 有效遍历 Pareto 前沿并优于各类基线，验证了理论分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Linear bandits traditionally prioritize regret minimization, often overlooking statistical inference of the underlying parameter as a critical objective. In high-stakes settings such as healthcare, precise parameter estimation is indispensable, as it provides fundamental insights into system mechanisms and ensures robust decision-making under covariate shift. We investigate the tripartite balance between regret, inference, and safety, deriving a fundamental minimax lower bound that characterizes the Pareto-optimal frontier of these competing goals. We then propose SERMiSC, a novel algorithm that achieves the optimal trade-off by matching this lower bound while maintaining a near-constant $\tilde{O}(1)$ safety risk. Empirical results demonstrate that SERMiSC effectively navigates the Pareto frontier and outperforms various baselines, thereby validating our theoretical analysis.

</details>

### 11. Safe Reinforcement Learning with Preference-based Constraint Inference

📄 [arXiv](https://arxiv.org/abs/2603.23565) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66726)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`reinforcement learning`、`constraint satisfaction`、`risk control`

👤 **作者**：Chenglin Li、Grant Ruan、Hua Geng

- 🎯 **研究动机**：现实安全约束复杂难显式指定，从偏好推断约束时 Bradley-Terry 模型无法刻画代价的不对称重尾性导致风险低估
- 🔬 **研究方法**：提出 PbCRL：在偏好建模中引入死区机制以鼓励重尾代价分布并证明其改善约束对齐，配合 SNR 损失促进探索与两阶段训练降低标注负担
- 📌 **结论**：与真实安全需求对齐更佳，在安全性与奖励上均超过 SOTA 基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe reinforcement learning (RL) is a standard paradigm for safety-critical decision making. However, real-world safety constraints can be complex, subjective, and even hard to explicitly specify. Existing works on constraint inference rely on restrictive assumptions or extensive expert demonstrations, which are not realistic in many real-world applications. How to cheaply and reliably learn these constraints is the major challenge we focus on in this study. While inferring constraints from human preferences offers a data-efficient alternative, we identify popular Bradley-Terry (BT) models fail to capture the asymmetric, heavy-tailed nature of safety costs, resulting in risk underestimation. It is still rare in the literature to understand the impacts of BT models on the downstream policy learning. To address the above knowledge gaps, we propose a novel approach namely Preference-based Constrained Reinforcement Learning (PbCRL). We introduce a novel dead zone mechanism into preference modeling and theoretically prove that it encourages heavy-tailed cost distributions, thereby achieving better constraint alignment. Additionally, we incorporate a Signal-to-Noise Ratio (SNR) loss to encourage exploration by cost variances, which is found to benefit policy learning. Further, two-stage training strategy is deployed to lower online labeling burdens while adaptively enhancing constraint satisfaction. Empirical results demonstrate that PbCRL achieves superior alignment with true safety requirements and outperforms state-of-the-art baselines in terms of safety and reward. Our work explores a promising and effective way for constraint inference in Safe RL, with great potential in various safety-critical applications.

</details>

### 12. RiskZero: Plan More to Risk Less with a Learned Model

🎓 [Official](https://icml.cc/virtual/2026/poster/66312)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`empirical evaluation`、`risk control`

👤 **作者**：Yousef Yassin、Junfeng Wen

- 🎯 **研究动机**：AlphaZero/MuZero 只最大化期望回报，在现实场景可能遭遇罕见但灾难性的失败
- 🔬 **研究方法**：提出 MuZero 族的风险敏感方法 RiskZero：学习分布式量估计轨迹级风险引导搜索规避严重后果，无需环境动态先验，并证明收敛到最优平稳风险敏感策略
- 📌 **结论**：在像素级风险敏感环境与大规模组合任务上超过 SOTA 风险敏感基线并提升样本效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AlphaZero and MuZero have demonstrated superhuman performance across a range of strategic tasks. Yet their reliance on maximizing expected returns limits their use in real-world settings, where even high-return policies may incur rare but catastrophic failures. We introduce RiskZero to address this limitation; the first MuZero -family method for risk-sensitive decision-making, and planning with zero prior knowledge of environment dynamics. RiskZero learns distributional quantities to estimate trajectory-level risk, guiding search toward policies that explicitly avoid rare but severe outcomes. We establish theoretical convergence to optimal, stationary risk-sensitive policies and validate our approach on environments designed to test risk-sensitive learning from pixels, as well as on larger-scale combinatorial tasks. Across all settings, RiskZero consistently outperforms state-of-the-art risk-sensitive baselines, and improves sample efficiency, providing a general framework for safer and reliable model-based reinforcement learning under uncertainty.

</details>

### 13. Mirror Descent Policy Optimisation for Robust Constrained Markov Decision Processes

📄 [arXiv](https://arxiv.org/abs/2506.23165) · 🎓 [Official](https://icml.cc/virtual/2026/poster/68816)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`uncertainty calibration`、`risk control`

👤 **作者**：David M. Bossens、Atsushi Nitanda

- 🎯 **研究动机**：鲁棒约束 MDP 需在认知不确定性下满足长期约束，缺策略梯度型求解算法
- 🔬 **研究方法**：镜像下降策略优化在拉格朗日上同时以策略梯度最大化策略、以对抗方式最小化转移核，并贡献转移核空间的近似梯度下降算法
- 📌 **结论**：样本设定下收敛率 O~(1/T^1/3)，鲁棒性测试显著优于基线策略优化

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety is an essential requirement for reinforcement learning systems. The newly emerging framework of robust constrained Markov decision processes allows learning policies that satisfy long-term constraints while providing guarantees under epistemic uncertainty. This paper presents mirror descent policy optimisation for robust constrained Markov decision processes, making use of policy gradient techniques to optimise both the policy (as a maximiser) and the transition kernel (as an adversarial minimiser) on the Lagrangian representing a constrained Markov decision process. Our proposed algorithm obtains an $\tilde{\mathcal{O}}\left(1/T^{1/3}\right)$ convergence rate in the sample-based robust constrained Markov decision process setting. The paper also contributes an algorithm for approximate gradient descent in the space of transition kernels, which is of independent interest for designing adversarial environments in general Markov decision processes. Experiments confirm the benefits of mirror descent policy optimisation in constrained and unconstrained optimisation, and significant improvements are observed in robustness tests when compared to baseline policy optimisation algorithms.

</details>

### 14. Learning Reward–Cost Balance in Safe RL via Score-Based World Models

🎓 [Official](https://icml.cc/virtual/2026/poster/61706)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`constraint satisfaction`、`policy safety`、`reinforcement learning`、`risk control`

👤 **作者**：Yuetian Wang、Dianxi Shi、Yuanze Wang、Huanhuan Yang、Shiming Song、Chunping Qiu

- 🎯 **研究动机**：安全 RL 多线性组合奖励与代价，安全与性能复杂非线性交互时指导有限
- 🔬 **研究方法**：USB-RL 基于分数的世界模型经无监督长程结果成对比较推断单调偏序分数，引导基于模型的策略优化动态平衡
- 📌 **结论**：多个安全基准上回报强且违规大幅减少，权衡稳定可解释

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe reinforcement learning (Safe RL) seeks to optimize long-term performance while ensuring adherence to safety constraints. However, most existing approaches address safety in a simplified manner, typically by linearly combining rewards and costs, which provides limited guidance when safety and performance interact in complex, nonlinear ways. We present USB-RL (Unsupervised Score-Balanced Reinforcement Learning), a model-based framework that learns implicit safety–performance preferences directly from experience. Our approach infers a monotone partial-order score through unsupervised pairwise comparisons of long-horizon outcomes, capturing nuanced trade-offs without relying on manually tuned cost weights. The learned score guides model-based policy optimization by dynamically balancing safety and performance, enabling flexible and adaptive multi-step planning in imagination-based control. Across diverse safety benchmarks, USB-RL achieves strong returns while substantially reducing safety violations, demonstrating stable and interpretable safety–performance trade-offs.

</details>

### 15. CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning

📄 [arXiv](https://arxiv.org/abs/2606.14415) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66410)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`safe reinforcement learning`、`reinforcement learning`、`constraint satisfaction`、`risk control`

👤 **作者**：Ayoub Belouadah、Sylvain Kubler、Yves Le Traon

- 🎯 **研究动机**：原始-对偶方法约束修正延迟导致振荡行为与长期安全违规
- 🔬 **研究方法**：CSPO 把局部约束敏感性纳入一阶原始-对偶更新：用距安全边界最短带符号距离推导约束敏感校正，补偿滞后乘子更新、减少边界附近振荡并保持 KKT 解
- 📌 **结论**：导航与运动基准上安全恢复更快、奖励保持更高，约束回报平均提升 15.6%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying safety constraints, typically modeled as constrained Markov decision processes. While primal-dual methods scale well to deep RL, they often suffer from delayed constraint correction, leading to oscillatory behavior and prolonged safety violations. In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order primal-dual method that incorporates local constraint sensitivity into policy updates. CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary, enabling smarter recovery steps back to safety, compensating for delayed Lagrange multiplier updates, and reducing oscillations near the boundary, while preserving the KKT solutions of the original constrained problem. Extensive experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns (+15.6\% average improvement) compared to state-of-the-art primal-dual and penalty-based methods.

</details>

### 16. Constrained Meta Reinforcement Learning with Provable Test-Time Safety

📄 [arXiv](https://arxiv.org/abs/2601.21845) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66356)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`reinforcement learning`、`safe reinforcement learning`、`constraint satisfaction`、`risk control`

👤 **作者**：Tingting Ni、Maryam Kamgarpour

- 🎯 **研究动机**：约束 meta-RL 中如何同时保证测试任务安全与低样本复杂度是开放问题
- 🔬 **研究方法**：提出算法精炼训练期策略，对测试任务学习近优策略给出可证安全与样本复杂度保证，并推导匹配下界
- 📌 **结论**：样本复杂度紧可达，兼顾测试时安全与快速学习

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Meta reinforcement learning (RL) allows agents to leverage experience across a distribution of tasks on which the agent can train at will, enabling faster learning of optimal policies on new test tasks. Despite its success in improving sample complexity on test tasks, many real-world applications, such as robotics and healthcare, impose safety constraints during testing. Constrained meta RL provides a promising framework for integrating safety into meta RL. An open question in constrained meta RL is how to ensure safety of the policy on the real-world test task, while reducing the sample complexity and thus, enabling faster learning of optimal policies. To address this gap, we propose an algorithm that refines policies learned during training, with provable safety and sample complexity guarantees for learning a near optimal policy on the test tasks. We further derive a matching lower bound, showing that this sample complexity is tight.

</details>

### 17. Blending Neural Control Density Functions for Stabilization and Safety

🎓 [Official](https://icml.cc/virtual/2026/poster/64872)　📅 2026　🏷 ICML 2026

**关键词**：`defense`、`risk control`、`safe reinforcement learning`、`constraint satisfaction`、`certified robustness`

👤 **作者**：Sahil Chaudhary、Chaitanya Murti、Chiranjib Bhattacharyya

- 🎯 **研究动机**：Lyapunov 方法无法做带 RoA 扩展保证的平滑混合，也无法在存在不稳定平衡点或鞍点时认证稳定性；有效密度证书难学
- 🔬 **研究方法**：首次证明密度函数混合控制器的吸引域包含各组成控制器 RoA 之并，提出密度函数的指数表征以可证满足可积条件，构成 NCDF 并结合 control barrier functions 合成安全稳定控制器
- 📌 **结论**：混合控制器的 RoA 优于 Neural Lyapunov Control 与 Sum-of-Squares 等方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recent work on Neural Network-based methods for nonlinear control use Lyapunov Functions to obtain controllers with guarantees of stability. However, Lyapunov-based methods are fundamentally limited: they cannot be used for smooth blending with formal Region of Attraction (RoA) expansion guarantees, and also fail to certify stability when unstable equilibria or saddle points are present. Density functions provide an alternate stability certificate, and address these limitations by certifying almost everywhere stability, and enable smooth blending of controllers. Learning valid density certificates is challenging due to integrability constraints, and the effect of density-based blending controllers on RoAs is not well understood. In this work, we provide the first guarantee that controllers blended with density functions yield RoAs containing the union of the RoAs achieved by the constituent controllers. Then, we propose a novel exponential characterization of density functions that provably satisfies the integrability condition, and introduce Neural Control Density Functions (NCDFs), that leverage this new parameterization. We also extend NCDFs for synthesizing safe-stable controllers by combining NCDFs with control barrier functions (NCDF-CBFs). Our experiments show that blended controllers obtain superior RoAs to state-of-the-art methods like Neural Lyapunov Control and Sum-of-Squares based techniques.

</details>

### 18. DEPLOY-RL: Active Boundary Discovery and Conservative Certification for Deployable Reinforcement Learning in Safety-Critical Continuous Processes

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T22.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026

**关键词**：`defense`、`RL certification`、`boundary discovery`、`fail-safe deployment`

- 🎯 **研究动机**：RL 策略很少上产安全关键流程——无法带统计保证地回答该策略部署是否安全
- 🔬 **研究方法**：DEPLOY-RL 训练后认证：契约耦合采集函数把采样集中到认证关键边界（约 2 倍采样效率），conformal risk control 给有限样本 false-go 保证（不超过 α），三路决策配 PID 或 MPC 故障安全回退
- 📌 **结论**：造纸数字孪生与 Tennessee Eastman 上 false-go 率 4.4%（最佳基线 8.6%）且保留 88.6% 策略覆盖率，是 14 个基线中唯一 false-go 小于 5% 且覆盖超 85% 的方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Reinforcement learning (RL) policies often outperform classical controllers in simulation, yet rarely reach production in safety-critical processes. The barrier is that there is no principled way to answer “Is this policy safe to deploy?” with statistical guarantees. We introduce DEPLOY-RL, a post-training certification framework built on one key insight: deployment certification requires discovering where failures occur (boundary discovery), not measuring how much everywhere (uniform reconstruction). Our contributions: (1) a contract-coupled acquisition function that concentrates sampling on certification-critical boundaries, achieving ≈ 2× sample efficiency with a semiempirical ambiguity reduction bound (domaincalibrated convergence guarantee); (2) conformal risk control providing finite-sample false-go guarantees (≤ α) under explicit deployment contracts; (3) a three-way decision framework (Deploy/NoDeploy/Abstain) with fail-safe PID/MPC fallback. In simulations on papermaking (industrial digital twin) and Tennessee Eastman (public benchmark), DEPLOY-RL achieves 4.4% false-go rate (vs. 8.6% for the best baseline) while retaining 88.6% policy coverage, the only method achieving <5% false-go with >85% coverage among 14 baselines under our evaluation protocol.

</details>

### 19. Safe and Efficient Control: A Subgraph-Augmented Hierarchical Reinforcement Learning Framework for Dynamically Reconfigurable Battery Systems

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/AI4T17.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=special-track-on-ai4tech-ai-enabling-critical-technologies)　📅 2026

**关键词**：`defense`、`hierarchical RL`、`battery control`、`operational constraint`

- 🎯 **研究动机**：动态可重构电池系统控制因大拓扑动作空间盲目探索与复杂运行约束导致奖励稀疏，难以学到有效策略
- 🔬 **研究方法**：提出 SAHRL：高层策略定战略方向，子图增强的低层策略结合从拓扑结构提取的子图归纳偏置细化动作以满足约束
- 📌 **结论**：仿真与真实实验均实现安全高效均衡，真实应用中能量释放较常规方法提升 10.56%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Dynamically Reconfigurable Battery (DRB) systems employ power electronic switches to create dynamic topologies. They enable effective management of cell inconsistencies through real-time adjustment of cell connections. However, existing DRB control methods struggle to learn effective strategies due to sparse rewards, which arise from blind exploration in large topological action spaces and complex operational constraints. This leads to ineffective policy learning, making safety and balancing performance difficult to ensure in practical applications. To this end, we propose a SubgraphAugmented Hierarchical Reinforcement Learning (SAHRL) framework. By combining hierarchical policies with topological structural knowledge, SAHRL effectively accelerates policy exploration and mitigates reward sparsity. Specifically, the high-level policy determines the strategic direction, while the subgraph-augmented low-level policy refines actions to meet operational constraints. The topological structural knowledge, extracted in the form of subgraphs and incorporated as an inductive bias, guides the agent focus on meaningful action patterns and reduce invalid exploration in the large action space. Extensive simulations and real-world experiments show that SAHRL achieves safe and efficient balancing. Notably, it increases the energy release by 10.56% compared to conventional methods in real-world applications.

</details>

### 20. Safe Multi-Objective Linear Bandits with Hierarchical Preferences

🌐 [Project](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2026/3310.pdf) · 🎓 [Official](https://2026.ijcai.org/accepted-papers/?ijtrack=main-track)　📅 2026

**关键词**：`analysis`、`safe bandit`、`hierarchical preference`、`baseline constraint`

- 🎯 **研究动机**：医疗与安全控制等任务需按优先级优化多个目标并满足相对基线策略的安全约束，缺乏系统框架
- 🔬 **研究方法**：建立带层级偏好与安全约束的多目标随机线性 bandit 模型，区分累积与逐段两类约束，提出 LexUCB-C 与 LexTS-S 算法并给出 regret 界
- 📌 **结论**：两算法 regret 与单目标安全线性 bandit 相当，同时优化多个目标，在合成与真实数据上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multi-objective bandits with hierarchical preferences and safety constraints is central to many real-world decision-making tasks such as healthcare treatment planning and safe autonomous control, where multiple objectives must be optimized according to their priorities while ensuring safety requirements are satisfied. In this paper, we study a multi-objective stochastic linear bandit framework that incorporates hierarchical preferences together with safety constraints, requiring the learner to remain competitive with respect to a known baseline policy. We consider two practically motivated safety models: (i) cumulative constraints, which require the cumulative performance to exceed the baseline, and (ii) stage-wise constraints, which impose this requirement at each time step. We propose two algorithms, LexUCB-C and LexTS-S, designed for the cumulative and stage-wise settings, respective ly. We establish regret bounds showing that both algorithms achieve performance comparable to existing single-objective safe linear bandit methods, while simultaneously optimizing multiple objectives. In addition to theoretical guarantees, we develop an experimental framework that captures the interaction between hierarchical preferences and safety constraints. Experiments on synthetic and real-world datasets demonstrate the effectiveness of the proposed methods.

</details>

### 21. Safety Generalization Under Distribution Shift in Safe Reinforcement Learning: A Diabetes Testbed

📄 [arXiv](https://arxiv.org/abs/2601.21094) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62037)　📅 2026　🏷 ICML 2026

**关键词**：`benchmark`、`defense`、`reinforcement learning`、`safe reinforcement learning`、`constraint satisfaction`、`embodied safety`

👤 **作者**：Minjae Kwon、Josephine Lamp、Lu Feng

- 🎯 **研究动机**：安全 RL 通常只在固定训练条件下评测，训练期安全保证能否迁移到分布偏移的部署环境未知
- 🔬 **研究方法**：以糖尿病管理为测试床，在统一临床模拟器上基准测试 8 种安全 RL 算法（3 类糖尿病、3 个年龄组），并用学习动力学模型的测试时屏蔽过滤不安全动作
- 📌 **结论**：揭示安全泛化鸿沟：训练满足约束的策略在未见患者上频繁违规；屏蔽使 PPO-Lag、CPO 等 Time-in-Range 提升 13-14% 并降低临床风险指数

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safe Reinforcement Learning (RL) algorithms are typically evaluated under fixed training conditions. We investigate whether training-time safety guarantees transfer to deployment under distribution shift, using diabetes management as a safety-critical testbed. We benchmark safe RL algorithms on a unified clinical simulator and reveal a safety generalization gap: policies satisfying constraints during training frequently violate safety requirements on unseen patients. We demonstrate that test-time shielding, which filters unsafe actions using learned dynamics models, effectively restores safety across algorithms and patient populations. Across eight safe RL algorithms, three diabetes types, and three age groups, shielding achieves Time-in-Range gains of 13--14\% for strong baselines such as PPO-Lag and CPO while reducing clinical risk index and glucose variability. Our simulator and benchmark provide a platform for studying safety under distribution shift in safety-critical control domains. Code is available at https://github.com/safe-autonomy-lab/GlucoSim and https://github.com/safe-autonomy-lab/GlucoAlg.

</details>