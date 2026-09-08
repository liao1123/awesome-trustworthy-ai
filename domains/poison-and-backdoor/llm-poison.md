# 语言模型投毒

[返回投毒与后门目录](README.md)

## 研究方向

语言模型投毒研究攻击者如何通过预训练语料、后训练数据、合成数据链、代码数据和部署制品改变模型行为。该方向重点关注低投毒预算下的可扩展性、跨训练阶段和模型代际传播、隐蔽能力操控、供应链威胁，以及训练前过滤、模型检测和恢复方法。

## 研究脉络

- **预训练投毒：** 早期研究关注网页级与预训练语料中的低成本、可扩展数据投毒。
- **生命周期扩展：** 攻击随后覆盖多阶段 post-training、synthetic-data chain 和部署供应链。
- **规模估计与防御：** 另一条路线量化成功攻击所需的数据规模，并用数据过滤或定向编辑建立训练前防线。

## 投毒攻击与传播链

### 1. Catastrophic Learning: A New Attack Vector on Continual Learning Networks

📄 [arXiv](https://arxiv.org/abs/2608.18976)　📅 2026-08

**关键词**：`attack`、`language-model poisoning`、`training data`、`behavior manipulation`

👤 **作者**：Benedikt Kluss、Niklas Bunzel

- 🎯 **研究动机**：持续学习的对抗研究以重启用灾难遗忘为目标（攻稳定性），模型可塑性未被攻击
- 🔬 **研究方法**：定义 learning blockers 六策略（标签/张量交换、吸引/排斥×同时/先行）：拉近或推远中毒与受害迭代的表征，使受害迭代不可学并可诱发遗忘
- 📌 **结论**：MNIST 与 Split-CIFAR10 上对 DER、ER-ACE、iCaRL 的 4480+ 次模拟中，攻击者可选择性阻碍新知获取并促成灾难学习场景

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual Learning (CL) enables deep learning models to iteratively learn from a stream of data without forgetting prior knowledge. Existing adversarial research on CL primarily aims to re-enable catastrophic forgetting, attacking stability and reducing availability. We identify a novel security flaw: data manipulated by an attacker can reduce the learnability of current or upcoming iterations. We term such manipulations learning blockers, as they attack the plasticity of CL algorithms. They are particularly harmful because they are difficult to detect during training of the current iteration, since they can target iterations whose data the model has not yet encountered. When learning blockers additionally induce catastrophic forgetting, the resulting overall degradation is what we call catastrophic learning. We formalize this scenario, define a threat model and propose six attack strategies: Label-Exchange, Tensor-Exchange, Attraction-Coincident, Attraction-Preceding, Repulsion-Coincident, and Repulsion-Preceding. The Attraction variants minimize the loss between the poisoned and the victim iteration label, pulling their representations together in feature space; the Repulsion variants maximize this loss, pushing them apart so stability mechanisms resist the required parameter shift. In the Coincident variants, the poisoned and the victim iteration coincide, using a clean reference iteration only as a label source; in the Preceding variants, the poisoned iteration precedes the victim, leaving it unlearnable due to distorted representations. We evaluate on MNIST and Split-CIFAR10 against three CL strategies - DER, ER-ACE, and iCaRL - across more than 4,480 simulations. Our results demonstrate a strong vulnerability: an adversary can selectively impede plasticity to hinder the acquisition of new knowledge, while promoting loss of prior knowledge, inducing a catastrophic learning scenario.

</details>

### 2. Conjunctive Poisoning in AI Supply-Chain Applications

📄 [arXiv](https://arxiv.org/abs/2608.15913)　📅 2026-08

**关键词**：`attack`、`AI supply chain`、`deployment artifacts`、`conjunctive trigger`、`deployment artifact`、`wrapper-metadata gate`

👤 **作者**：Nokimul Hasan Arif、Qian Lou、Mengxin Zheng

- 🎯 **研究动机**：推理管线的 prompt 包装器与配置元数据直接塑造输出，却不像模型权重那样被验证保护
- 🔬 **研究方法**：恶意开发者配对良性外观包装器与 crafted 元数据（合取门需包装器标记+密码学绑定元数据同时出现）确定性改变生成后行为，跨 15 个 LLM/VLM 部署评测；TIF-BAH 验证包装器完整性并记录行为证明
- 📌 **结论**：静态元数据检查、包装器扫描、PromptShield 与 SigStore 签名均不足；wrapper-metadata 交互构成模型权重级与 prompt 级防御均不覆盖的执行层风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language and Vision-Language Models are increasingly deployed through inference pipelines that include prompt wrappers (e.g., templates and post-processing scripts) and configuration metadata (e.g., JSON/YAML files) that together shape model outputs. While model weights and binaries are routinely verified, these textual deployment artifacts remain weakly protected despite directly influencing runtime behavior. We show that a malicious developer can pair a benign-looking wrapper with crafted metadata to deterministically alter post-generation behavior without modifying model weights, training data, or inference backend. We study this behavior through a controlled conjunctive-gate implementation, where activation depends on both an embedded wrapper marker and cryptographically bound metadata. We evaluate the attack across fifteen open- and closed-source LLM/VLM deployments, and assess prompt and system level defenses including static metadata inspection, wrapper scanners, PromptShield, and SigStore-based artifact signing. To mitigate this risk, we introduce TIF-BAH, a lightweight middleware defense that verifies wrapper integrity and records behavioral attestations during inference. Our results reveal that wrapper-metadata interactions form an under-protected execution layer in modern AI deployments, exposing a deployment-time behavioral risk that is not captured by model-weight or prompt-level defenses. Code is available at https://github.com/N-H-Arif/llm_temp.

</details>

### 3. Pretraining Data Can Be Poisoned through Computational Propaganda

📄 [arXiv](https://arxiv.org/abs/2607.15267)　📅 2026-07

**关键词**：`attack`、`LLM data poisoning`、`pretraining poisoning`、`computational propaganda`

👤 **作者**：Victoria Graf、Hannaneh Hajishirzi、Noah A. Smith、David Kohlbrenner、Kyle Lo

- 🎯 **研究动机**：已有预训练投毒研究依赖 Wikipedia 等既有数据源，忽视网页规模异质性及投毒数据与清洗管线的交互
- 🔬 **研究方法**：利用公开讨论接口这一现实网页级内容注入机制投毒，并提出 HalfLife 分析估计对抗内容被网页爬取与清洗后的纳入率
- 📌 **结论**：确立第三方网页内容可作为攻击语言模型预训练的载体，估计毒内容纳入预训练数据对评估攻击可行性至关重要

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources such as Wikipedia, which do not represent the large scale and heterogeneity typical of pretraining corpora, and has ignored the interaction between poisoned data and data curation pipelines. We demonstrate that poisoning attacks on pretraining data are feasible beyond this limited setting through an existing web-scale content injection mechanism: public discussion interfaces. Additionally, to measure whether malicious content is included after web crawling and data curation, we introduce HalfLife, a novel analysis for estimating adversarial content inclusion in web-crawl based LM training data. We use HalfLife to explore the feasibility of poisoning pretraining corpora at web scale through open discussion interfaces. Our analysis demonstrates the importance of estimating whether poison injections are included in pretraining data, and establishes third-party webpage content as a possible vector for attacking language model pretraining.

</details>

### 4. Rapid Poison: Practical Poisoning Attacks Against the Rapid Response Framework

📄 [arXiv](https://arxiv.org/abs/2606.16242) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62293)　📅 2026-06　🏷 ICML 2026

**关键词**：`attack`、`LLM security pipeline`、`classifier poisoning`、`prompt injection`、`backdoor attack`、`empirical evaluation`

👤 **作者**：David Huang、Jaewon Chang、Avidan Shah、Prateek Mittal、Chawin Sitawarin

- 🎯 **研究动机**：Rapid Response 框架（含 Anthropic ASL-3）用合成变体持续训练越狱检测分类器，提示注入可渗入该管线投毒训练集
- 🔬 **研究方法**：在只能修改越狱样本的约束下实现两类攻击：定向投毒使无害样本被误判越狱；Omission Attack 利用概念缺失 unsafe 样本训练使分类器把该概念与安全标签错误关联形成后门
- 📌 **结论**：仅 1% 投毒率即可造成部分情形近乎完全的标签翻转，最高 100% 假阳性率与 96% 假阴性率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The Rapid Response (RR) framework, deployed in production systems, including Anthropic's ASL-3 safeguards, continuously improves jailbreak-detection classifiers. When new jailbreaks emerge that bypass these classifiers, Rapid Response generates synthetic variants for training, helping the model generalize from the new attacks and quickly adapt. We reveal that prompt injection can infiltrate this pipeline to deliver poisoned samples into the classifier's training set, enabling two attack objectives: (I) targeted poisoning attacks that create false positives on harmless samples by categorizing them as a jailbreak, with a specific desired feature (e.g., certain formatting, subject, or keyword), (II) concept-based backdoor attacks that induce false negatives on jailbreak inputs, generalizing even to jailbreaks from attack strategies the defender explicitly trained against, when the backdoor trigger is present. Importantly, our threat model restricts adversaries to modifying only jailbreak samples (not benign data or labels), a constraint unexplored by prior work that makes the second objective particularly challenging. We address this with Omission Attack, which exploits a new phenomenon: when training on concept-absent unsafe samples, the classifier misassociates that concept's presence with the safe label. Both attacks cause substantial and in some cases near-complete label flipping at only a 1% poisoning rate, achieving up to 100% false positive rates and up to 96% false negative rates.

</details>

### 5. Sequential Data Poisoning in LLM Post-Training

📄 [arXiv](https://arxiv.org/abs/2606.04929)　📅 2026-06

**关键词**：`attack`、`LLM data poisoning`、`sequential poisoning`、`multi-stage training`

👤 **作者**：Jack Sanderson、Yihan Wang、Xiaoqian Lu、Gautam Kamath、Yiwei Lu

- 🎯 **研究动机**：已有投毒研究假设单攻击者，忽视 SFT 与偏好学习多阶段、多数据源下多个攻击者协同的可能
- 🔬 **研究方法**：提出 sequential data poisoning 威胁模型：多个攻击者分别污染 SFT 与偏好数据集，分析 SFT→DPO 与 SFT→PPO 管线的复合效应
- 📌 **结论**：发现 single-attacker illusion：单独评估时威胁可忽略，协同后在 DPO 管线贡献可加、PPO 管线互补（单独均失败、组合成功），分阶段安全分析系统性低估复合漏洞

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

LLM post-training proceeds through multiple stages, e.g., supervised fine-tuning (SFT) followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO), where each stage draws data from different, potentially untrusted sources. Existing literature assumes data poisoning attacks may occur at each training stage, but neglects the possibility of multiple attackers. To study the trustworthiness of the entire post-training pipeline, we propose the threat model of sequential data poisoning, where multiple adversaries separately poison the SFT and preference datasets. Under this threat model, we identify the single-attacker illusion: each adversary, evaluated in isolation, appears to pose a negligible threat. Yet when adversaries collaborate across stages, the true vulnerability is revealed. In the SFT $\to$ DPO pipeline, their contributions are additive: splitting a fixed poison budget across stages outperforms concentrating it in either stage alone. In the SFT $\to$ PPO pipeline, their contributions are complementary: neither SFT nor reward model poisoning succeeds individually, yet their combination does. These findings show that security analyses of individual post-training stages systematically underestimate compound vulnerabilities that emerge only from their interaction. Code is available at https://github.com/jcksanderson/sequential-poisoning.

</details>

### 6. Are My Optimized Prompts Compromised? Exploring Vulnerabilities of LLM-based Optimizers

🎓 [Official](https://aclanthology.org/2026.eacl-long.100/)　📅 2026-03　🏷 ACL 2026

**关键词**：`attack`、`prompt optimizer`、`feedback poisoning`、`fake reward`

👤 **作者**：Andrew Zhao、…、Jack W. Stokes

- 🎯 **研究动机**：基于 LLM 的提示优化器从评分反馈迭代精炼提示，该优化阶段的安全性首次被系统检验
- 🔬 **研究方法**：分析提示优化管线的投毒风险：提出无需访问奖励模型的 fake reward 攻击，并设计轻量 highlighting 防御
- 📌 **结论**：HarmBench 上反馈攻击比查询投毒危险得多，ASR 最高提升 0.48；highlighting 把 fake reward 的 ΔASR 从 0.23 降至 0.07 且不损害效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) systems increasingly power everyday AI applications such as chatbots, computer-use assistants, and autonomous robots, where performance often depends on manually well-crafted prompts. LLM-based prompt optimizers reduce that effort by iteratively refining prompts from scored feedback, yet the security of this optimization stage remains underexamined. We present the first systematic analysis of poisoning risks in LLM-based prompt optimization. Using HarmBench, we find systems are substantially more vulnerable to manipulated feedback than to query poisoning alone: feedback-based attacks raise attack success rate (ASR) by up to ΔASR = 0.48. We introduce a simple fake reward attack that requires no access to the reward model and significantly increases vulnerability. We also propose a lightweight highlighting defense that reduces the fake reward ΔASR from 0.23 to 0.07 without degrading utility. These results establish prompt optimization pipelines as a first-class attack surface and motivate stronger safeguards for feedback channels and optimization frameworks.

</details>

### 7. XOXO: Stealthy Cross-Origin Context Poisoning Attacks against AI Coding Assistants

🎓 [Official](https://aclanthology.org/2026.acl-long.521/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`LLM backdoor`、`model integrity`

👤 **作者**：Adam Štorek、…、Suman Jana

- 🎯 **研究动机**：编码助手自动纳入不可信上下文，语义不变的代码改动即可隐蔽投毒
- 🔬 **研究方法**：XOXO以重命名等语义保持变换诱导生成漏洞模式，GCGS黑盒搜索有效变换组合
- 📌 **结论**：对八个SOTA模型平均ASR 73.20%，漏洞注入率最高66.67%，GitHub Copilot实战验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI coding assistants automatically gather context from potentially untrusted sources to generate code recommendations. We introduce Cross-Origin Context Poisoning (XOXO), a novel attack that exploits this automatic context inclusion by subtly manipulating code without changing its semantics. Attackers introduce semantics-preserving transformations (e.g., renamed variables) to shared code, causing AI assistants to unknowingly recommend vulnerable code patterns to victims. To systematically identify effective transformations, we present Greedy Cayley Graph Search (GCGS), a black-box algorithm that efficiently composes transformations to identify adversarial inputs. Our evaluation demonstrates XOXO’s effectiveness at making LLMs generate buggy and vulnerable code, achieving average attack success rates of 73.20% against eight state-of-the-art models including GPT 4.1 and Claude 3.5 Sonnet v2, with vulnerability injection rates up to 66.67%. We also demonstrate a real-world attack against GitHub Copilot, highlighting critical security gaps in current AI coding tools.

</details>

### 8. When Can You Poison Rewards? A Tight Characterization of Reward Poisoning in Linear MDPs

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

### 9. Tight Stability Bounds for Robust Distributed Learning: Byzantine Failures Hurt Generalization More than Data Poisoning

📄 [arXiv](https://arxiv.org/abs/2506.18020) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61938)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`adversarial defense`、`empirical evaluation`

👤 **作者**：Thomas Boudou、Batiste Le Bars、Nirupam Gupta、Aurélien Bellet

- 🎯 **研究动机**：Byzantine 失效与数据中毒两种威胁模型的优化保证相似，但对泛化的影响差异此前未知
- 🔬 **研究方法**：对鲁棒分布式学习做紧致算法稳定性分析，首次证明两种威胁模型在泛化保证上的根本差距
- 📌 **结论**：数据中毒下最优算法的均匀稳定性仅加性退化 Θ(f/(n-f))，Byzantine 失效下退化 Ω(√(f/(n-2f)))，严格更差

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Robust distributed learning algorithms aim to maintain reliable performance despite the presence of misbehaving workers. Such misbehaviors are commonly modeled as *Byzantine failures*, allowing arbitrarily corrupted communication, or as *data poisoning*, a weaker form of corruption restricted to local training data. While prior work shows similar optimization guarantees for both models, an important question remains: *How do these threat models impact generalization?* We show, for the first time, a fundamental gap in generalization guarantees between the two threat models: Byzantine failures yield strictly worse rates than those achievable under data poisoning. Our findings leverage a tight algorithmic stability analysis of robust distributed learning. Specifically, we prove that: *(i)* under data poisoning, the uniform algorithmic stability of an algorithm with optimal optimization guarantees degrades by an additive factor of $\Theta ( \frac{f}{n-f} )$, with $f$ out of $n$ workers misbehaving; whereas *(ii)* under Byzantine failures, the degradation is in $\Omega \big( \sqrt{ \frac{f}{n-2f}} \big)$.

</details>

### 10. Theory of Continual Learning Against Data Poisoning Attacks

📄 [arXiv](https://arxiv.org/abs/2606.29841) · 🎓 [Official](https://icml.cc/virtual/2026/poster/65304)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`backdoor attack`、`empirical evaluation`

👤 **作者**：Yiting Hu、Lingjie Duan

- 🎯 **研究动机**：持续学习易受数据中毒引发学习发散或严重超额风险，CL 中的攻防缺乏原则性理论基础
- 🔬 **研究方法**：把攻防交互建模为在线零和博弈，证明攻击者毒化线性比例任务并注入无界噪声时无防御可成功；对低频攻击提出任务间验证机制，对有界噪声推导最小化中毒特征敏感度的防御
- 📌 **结论**：两种可防御场景分别实现中毒检测与收敛保障、可证明加速的收敛，实验验证理论结果

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual learning (CL), where a model is trained on a sequence of data tasks, is increasingly being adopted across key fields such as large language models and image recognition, yet it remains highly vulnerable to data poisoning that triggers learning divergence or severe excess risk. Despite these threats, a principled theoretical foundation in CL for understanding attack and defense remains lacking. In this paper, we develop a theoretical framework to analyze strategic attacks and defenses in regularization-based CL, a cornerstone of recent CL theory. By framing the adversary-defender interaction as an online zero-sum game, we first establish a fundamental performance limit: no defense succeeds when an adversary poisons a linear proportion of tasks by injecting unbounded noise or pattern shifts in regularization-based CL. We then analyze two possibly defensible scenarios: infrequent attacks and bounded noise per attack. For the former regime, we propose a task-to-task verification mechanism to detect data poisoning and reduce cumulative bias for learning convergence. For the latter regime, we derive a robust defense that minimizes the model’s sensitivity to poisoned features, provably accelerating the convergence rate. Extensive experiments on realistic tasks further validate our theoretical results.

</details>

### 11. Safety-Efficacy Trade Off: Robustness against Data-Poisoning

📄 [arXiv](https://arxiv.org/abs/2602.00822) · 🎓 [Official](https://icml.cc/virtual/2026/poster/61186)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`adversarial robustness`、`data poisoning`、`language-model poisoning`、`backdoor defense`、`mechanistic analysis`

👤 **作者**：Diego Granziol

- 🎯 **研究动机**：后门与数据投毒可高成功率绕过频谱与优化式防御，其几何机制不明
- 🔬 **研究方法**：以核岭回归作为宽网络精确模型，证明聚类脏标签投毒在输入 Hessian 诱导随攻击效力二次增长的秩一尖峰，并刻画攻击有效而曲率消失的近克隆不可检测域；分析输入梯度正则的作用
- 📌 **结论**：在 MNIST 与 CIFAR-10/100 上验证攻击成功与频谱可见性的系统性滞后，首次端到端刻画投毒、可检测性与防御的输入空间曲率关系

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor and data-poisoning attacks can achieve high attack success while evading existing spectral and optimisation-based defences. We show that this behaviour is not incidental, but arises from a fundamental geometric mechanism in input space. Using kernel ridge regression as an exact model of wide neural networks, we prove that clustered dirty-label poisons induce a rank-one spike in the input Hessian whose magnitude scales quadratically with attack efficacy. Crucially, for nonlinear kernels we identify a near-clone regime in which poison efficacy remains order-one while the induced input curvature vanishes, making the attack provably spectrally undetectable. We further show that input-gradient regularisation contracts poison-aligned Fisher and Hessian eigenmodes under gradient flow, yielding an explicit and unavoidable safety–efficacy trade-off by reducing data-fitting capacity. For exponential kernels, this defence admits a precise interpretation as an anisotropic high-pass filter that increases the effective length scale and suppresses near-clone poisons. Extensive experiments on linear models and deep convolutional networks across MNIST and CIFAR-10/100 validate the theory, demonstrating consistent lags between attack success and spectral visibility, and showing that regularisation and data augmentation jointly suppress poisoning. Our results establish when backdoors are inherently invisible, and provide the first end-to-end characterisation of poisoning, detectability, and defence through input-space curvature.

</details>

### 12. Robust In-Context Reinforcement Learning Under Reward Poisoning Attacks

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

### 13. PARASITE: Conditional System Prompt Poisoning to Hijack LLMs

🎓 [Official](https://aclanthology.org/2026.acl-long.668/)　📅 2026　🏷 ACL 2026

**关键词**：`attack`、`system prompt`、`data poisoning`、`language-model poisoning`、`LLM backdoor`、`model integrity`

👤 **作者**：Viet Pham、Thai Le

- 🎯 **研究动机**：从公共市场下载第三方系统提示构成供应链风险，可被注入休眠代理
- 🔬 **研究方法**：PARASITE 在黑盒无权重访问下两阶段优化（全局语义搜索+贪心词法精化），仅对特定查询触发受损输出、良性输入保持高效用
- 📌 **结论**：开源模型与 GPT-4o-mini、GPT-3.5 商业 API 上目标查询 F1 最多降 70% 且通用能力几乎不损；利用真实提示噪声绕过困惑度过滤等防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed via third-party system prompts downloaded from public marketplaces. We identify a critical supply-chain vulnerability: conditional system prompt poisoning, where an adversary injects a sleeper agent into a benign-looking prompt. Unlike traditional jailbreaks that aim for broad refusal-breaking, our proposed framework, PARASITE, optimizes system prompts to trigger LLMs to output targeted, compromised responses only for specific queries (e.g., “Who should I vote for the US President?”) while maintaining high utility on benign inputs. Operating in a strict black-box setting without model weight access, PARASITE utilizes a two-stage optimization including a global semantic search followed by a greedy lexical refinement. Tested on open-source models and commercial APIs (GPT-4o-mini, GPT-3.5), PARASITE achieves up to 70% F1 reduction on targeted queries with minimal degradation to general capabilities. We further demonstrate that these poisoned prompts evade standard defenses, including perplexity filters and typo-correction, by exploiting the natural noise found in real-world system prompts.

</details>

### 14. Efficient Preference Poisoning Attack on Offline RLHF

📄 [arXiv](https://arxiv.org/abs/2605.02495) · 🎓 [Official](https://icml.cc/virtual/2026/poster/66514)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`data poisoning`、`language-model poisoning`、`training data`、`backdoor attack`、`reinforcement learning`

👤 **作者**：Chenye Yang、Weiyu Xu、Lifeng Lai

- 🎯 **研究动机**：离线 RLHF（如 DPO）在预收集偏好数据上训练，易受偏好标签翻转投毒
- 🔬 **研究方法**：证明翻转单个偏好标签引起参数无关的 DPO 梯度偏移，把定向投毒转为结构化二值稀疏逼近问题；BAL-A 用格归约与 Babai 最近平面，BMP-A 用二值匹配追踪并给恢复保证与不可能性证书
- 📌 **结论**：合成字典与 Stanford Human Preferences 数据集验证理论，字典几何决定攻击成败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Offline Reinforcement Learning from Human Feedback (RLHF) pipelines such as Direct Preference Optimization (DPO) train on a pre-collected preference dataset, which makes them vulnerable to preference poisoning attack. We study label flip attacks against log-linear DPO. We first illustrate that flipping one preference label induces a parameter-independent shift in the DPO gradient. Using this key property, we can then convert the targeted poisoning problem into a structured binary sparse approximation problem. To solve this problem, we develop two attack methods: Binary-Aware Lattice Attack (BAL-A) and Binary Matching Pursuit Attack (BMP-A). BAL-A embeds the binary flip selection problem into a binary-aware lattice and applies Lenstra-Lenstra-Lovász reduction and Babai's nearest plane algorithm; we provide sufficient conditions that enforce binary coefficients and recover the minimum-flip objective. BMP-A adapts binary matching pursuit to our non-normalized gradient dictionary and yields coherence-based recovery guarantees and robustness (impossibility) certificates for $K$-flip budgets. Experiments on synthetic dictionaries and the Stanford Human Preferences dataset validate the theory and highlight how dictionary geometry governs attack success.

</details>

### 15. Virus Infection Attack on LLMs: Your Poisoning Can Spread via Synthetic Data

📄 [arXiv](https://arxiv.org/abs/2509.23041) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e6c5195dac675f03d0fcf3955bcdd3c9-Abstract-Conference.html)　📅 2025-09　🏷 NeurIPS 2025

**关键词**：`attack`、`synthetic-data pipeline`、`cross-generation transfer`、`viral poisoning`

👤 **作者**：Zi Liang、Qingqing Ye、Xuan Liu、Yanyun Wang、Jianliang Xu、Haibo Hu

- 🎯 **研究动机**：合成数据广泛用于 LLM 训练，其引入的安全风险未被研究
- 🔬 **研究方法**：提出 Virus Infection Attack：借鉴病毒设计把投毒载荷藏入保护壳，并在良性样本中搜索最优劫持点，使恶意内容借合成数据生成传播
- 📌 **结论**：数据投毒与后门攻击下，下游模型 ASR 提升到与上游投毒模型相当的水平，即使生成查询完全干净

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Synthetic data refers to artificial samples generated by models. While it has been validated to significantly enhance the performance of large language models (LLMs) during training and has been widely adopted in LLM development, potential security risks it may introduce remain uninvestigated. This paper systematically evaluates the resilience of synthetic-data-integrated training paradigm for LLMs against mainstream poisoning and backdoor attacks. We reveal that such a paradigm exhibits strong resistance to existing attacks, primarily thanks to the different distribution patterns between poisoning data and queries used to generate synthetic samples. To enhance the effectiveness of these attacks and further investigate the security risks introduced by synthetic data, we introduce a novel and universal attack framework, namely, Virus Infection Attack (VIA), which enables the propagation of current attacks through synthetic data even under purely clean queries. Inspired by the principles of virus design in cybersecurity, VIA conceals the poisoning payload within a protective "shell" and strategically searches for optimal hijacking points in benign samples to maximize the likelihood of generating malicious content. Extensive experiments on both data poisoning and backdoor attacks show that VIA significantly increases the presence of poisoning content in synthetic data and correspondingly raises the attack success rate (ASR) on downstream models to levels comparable to those observed in the poisoned upstream models.

</details>

### 16. Reasoning Introduces New Poisoning Attacks Yet Makes Them More Complicated

📄 [arXiv](https://arxiv.org/abs/2509.05739) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-09　🏷 SaTML 2026

**关键词**：`analysis`、`attack`、`CoT integrity`、`trace-answer divergence`、`decomposed trigger`、`reasoning model`

👤 **作者**：Hanna Foerster、…、Yarin Gal

- 🎯 **研究动机**：推理能力把 LLM 攻击面扩展到中间 CoT，但推理模型上投毒能否生效不明
- 🔬 **研究方法**：提出 decomposed reasoning poison：仅修改推理路径、prompt 与最终答案保持干净，并把触发器拆成多个各自无害的组件
- 📌 **结论**：可注入但可靠激活并改变最终答案出奇困难，模型常能从思维过程中的后门恢复，推理能力带来涌现式后门鲁棒性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Early research into data poisoning attacks against Large Language Models (LLMs) demonstrated the ease with which backdoors could be injected. More recent LLMs add step-by-step reasoning, expanding the attack surface to include the intermediate chain-of-thought (CoT) and its inherent trait of decomposing problems into subproblems. Using these vectors for more stealthy poisoning, we introduce ``decomposed reasoning poison'', in which the attacker modifies only the reasoning path, leaving prompts and final answers clean, and splits the trigger across multiple, individually harmless components. Fascinatingly, while it remains possible to inject these decomposed poisons, reliably activating them to change final answers (rather than just the CoT) is surprisingly difficult. This difficulty arises because the models can often recover from backdoors that are activated within their thought processes. Ultimately, it appears that an emergent form of backdoor robustness is originating from the reasoning capabilities of these advanced LLMs, as well as from the architectural separation between reasoning and final answer generation.

</details>

### 17. Attacks on Approximate Caches in Text-to-Image Diffusion Models

📄 [arXiv](https://arxiv.org/abs/2508.20424) · 🌐 [Project](https://zenodo.org/records/18705055) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/sun-desen)　📅 2025-08　🏷 USENIX Security 2026

**关键词**：`attack`、`prompt stealing`、`cache poisoning`、`data poisoning`、`diffusion serving cache`

👤 **作者**：Desen Sun、Shuncheng Jie、Sihang Liu

- 🎯 **研究动机**：扩散服务采用近似缓存复用相似 prompt 的中间状态，打破了用户间隔离
- 🔬 **研究方法**：演示三类远程攻击：以特殊关键词建立可维持数日的隐蔽信道、从缓存命中窃取 prompt、向被窃 prompt 投毒嵌入攻击者 logo
- 📌 **结论**：三类攻击均可经服务系统远程实施，暴露近似缓存的严重安全风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Diffusion models are a powerful class of generative models that produce images and other content from user prompts, but they are computationally intensive. To mitigate this cost, recent academic and industry work has adopted approximate caching, which reuses intermediate states from similar prompts in a cache. While efficient, this optimization introduces new security risks by breaking isolation among users. This paper provides a comprehensive assessment of the security vulnerabilities introduced by approximate caching. First, we demonstrate a remote covert channel established with the approximate cache, where a sender injects prompts with special keywords into the cache system and a receiver can recover that even after days, to exchange information. Second, we introduce a prompt stealing attack using the approximate cache, where an attacker can recover existing cached prompts from hits. Finally, we introduce a poisoning attack that embeds the attacker's logos into the previously stolen prompt, leading to unexpected logo rendering for the requests that hit the poisoned cache prompts. These attacks are all performed remotely through the serving system, demonstrating severe security vulnerabilities in approximate caching. The code for this work is available.

</details>

### 18. Persistent Pre-Training Poisoning of LLMs

📄 [arXiv](https://arxiv.org/abs/2410.13722) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4dade38eae8c007f3a564b8ea820664a-Abstract-Conference.html)　📅 2024-10　🏷 ICLR 2025

**关键词**：`attack`、`LLM data poisoning`、`persistent poisoning`、`pretraining`

👤 **作者**：Yiming Zhang、…、Daphne Ippolito

- 🎯 **研究动机**：预训练投毒能否在 SFT 与 DPO 后持久存在从未被评估
- 🔬 **研究方法**：从头预训练 600M-7B 系列 LLM，测 DoS、信念操纵、越狱与 prompt 窃取四类攻击目标的持久性
- 📌 **结论**：0.1% 预训练数据投毒即使 3/4 类攻击在后训练后仍显著持续，DoS 类仅需 0.001%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models are pre-trained on uncurated text datasets consisting of trillions of tokens scraped from the Web. Prior work has shown that: (1) web-scraped pre-training datasets can be practically poisoned by malicious actors; and (2) adversaries can compromise language models after poisoning fine-tuning datasets. Our work evaluates for the first time whether language models can also be compromised during pre-training, with a focus on the persistence of pre-training attacks after models are fine-tuned as helpful and harmless chatbots (i.e., after SFT and DPO). We pre-train a series of LLMs from scratch to measure the impact of a potential poisoning adversary under four different attack objectives (denial-of-service, belief manipulation, jailbreaking, and prompt stealing), and across a wide range of model sizes (from 600M to 7B). Our main result is that poisoning only 0.1% of a model's pre-training dataset is sufficient for three out of four attacks to measurably persist through post-training. Moreover, simple attacks like denial-of-service persist through post-training with a poisoning rate of only 0.001%.

</details>

### 19. Scaling Model-Generated Distillation Data Can Make Latent Teacher Traits More Recoverable

📄 [arXiv](https://arxiv.org/abs/2608.26958)　📅 2026-08

**关键词**：`analysis`、`benign fine-tuning`、`latent behavior transfer`、`synthetic data`、`subliminal learning`、`distillation scaling`

👤 **作者**：Zhichen Dong、Zhixuan Liu、Yuyu Fan、Xiangtian Li、Shuyang Zhang、Chao Yang

- 🎯 **研究动机**：扩大模型生成蒸馏数据通常只被视为提升覆盖与降噪，其让隐蔽 teacher trait 更易从 student 恢复的效应未被认识
- 🔬 **研究方法**：在 subliminal learning 控制设置中，由被诱导表达目标 trait 的 teacher 生成纯数字等离任务数据，训练不同数据量的 student 并用无 trait 对照隔离迁移
- 📌 **结论**：独立数据越多，teacher 诱导 trait 在 student 后续行为中越突出，LoRA 更新呈平行趋势，效应跨模型家族、trait 类型与跨模型迁移均成立

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Scaling model-generated data is usually viewed as improving distillation: more examples should increase coverage, reduce noise, and produce stronger students. We show a second effect: larger datasets can make subtle teacher-specific signals easier to detect in the trained student, even when examples are off-task and never mention the trait. In a controlled setup inspired by subliminal learning, a teacher induced to express a target trait generates restricted off-task data, such as number-only completions. Students trained on different amounts of independent off-task data are evaluated in a separate domain, with matched no-trait controls isolating target-specific transfer. Our main finding is that larger independent datasets make the teacher's induced trait stand out more clearly in the student's later behavior. Other plausible traits may also strengthen with scale, but the target usually grows more. When the small-scale student already favors the target, scaling mainly amplifies that behavior; when it favors a related or salient alternative, more data can shift behavior toward the intended trait. Analyses of learned LoRA updates show a parallel trend. These effects appear across model families, trait types, multi-trait settings, and cross-model transfer. Our results suggest that scaling generated distillation data should be paired with trait-aware curation and evaluation, even when the data appears off-task or benign.

</details>

### 20. Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

📄 [arXiv](https://arxiv.org/abs/2510.07192)　📅 2025-10

**关键词**：`analysis`、`LLM data poisoning`、`scaling law`、`pretraining poisoning`

👤 **作者**：Alexandra Souly、…、Robert Kirk

- 🎯 **研究动机**：预训练投毒研究假设攻击者控制语料百分比，大模型下小百分比也意味着海量投毒，假设不现实
- 🔬 **研究方法**：开展迄今最大规模预训练投毒实验：600M-13B 模型在 6B-260B token 的 chinchilla 最优数据集上从零预训练并投毒
- 📌 **结论**：约 250 篇毒文档即可在所有模型与数据规模上同样奏效，所需毒样本数近常数、不随规模增长，微调阶段同样成立

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Poisoning attacks can compromise the safety of large language models (LLMs) by injecting malicious documents into their training data. Existing work has studied pretraining poisoning assuming adversaries control a percentage of the training corpus. However, for large models, even small percentages translate to impractically large amounts of data. This work demonstrates for the first time that poisoning attacks instead require a near-constant number of documents regardless of dataset size. We conduct the largest pretraining poisoning experiments to date, pretraining models from 600M to 13B parameters on chinchilla-optimal datasets (6B to 260B tokens). We find that 250 poisoned documents similarly compromise models across all model and dataset sizes, despite the largest models training on more than 20 times more clean data. We also run smaller-scale experiments to ablate factors that could influence attack success, including broader ratios of poisoned to clean data and non-random distributions of poisoned samples. Finally, we demonstrate the same dynamics for poisoning during fine-tuning. Altogether, our results suggest that injecting backdoors through data poisoning may be easier for large models than previously believed as the number of poisons required does not scale up with model size, highlighting the need for more research on defences to mitigate this risk in future models.

</details>

### 21. Poisoning Web-Scale Training Datasets is Practical

📄 [arXiv](https://arxiv.org/abs/2302.10149) · 🌐 [Project](https://doi.org/10.1109/SP54263.2024.00179)　📅 2023-02　🏷 IEEE S&P 2024

**关键词**：`analysis`、`web-scale corpus`、`low-cost poisoning`、`data supply chain`、`attack analysis`、`web-scale dataset`

👤 **作者**：Nicholas Carlini、…、Florian Tramèr

- 🎯 **研究动机**：网络级数据集被认为规模过大、难以被单点投毒，该假设未经检验
- 🔬 **研究方法**：split-view poisoning 利用网络内容可变性使标注视图与下载视图不一致；frontrunning poisoning 在快照窗口前抢先注入
- 📌 **结论**：60 美元即可投毒 LAION-400M/COYO-700M 的 0.01%，今天就可行于 10 个流行数据集

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Deep learning models are often trained on distributed, web-scale datasets crawled from the internet. In this paper, we introduce two new dataset poisoning attacks that intentionally introduce malicious examples to a model's performance. Our attacks are immediately practical and could, today, poison 10 popular datasets. Our first attack, split-view poisoning, exploits the mutable nature of internet content to ensure a dataset annotator's initial view of the dataset differs from the view downloaded by subsequent clients. By exploiting specific invalid trust assumptions, we show how we could have poisoned 0.01% of the LAION-400M or COYO-700M datasets for just $60 USD. Our second attack, frontrunning poisoning, targets web-scale datasets that periodically snapshot crowd-sourced content -- such as Wikipedia -- where an attacker only needs a time-limited window to inject malicious examples. In light of both attacks, we notify the maintainers of each affected dataset and recommended several low-overhead defenses.

</details>

### 22. Shaping Capabilities with Token-Level Data Filtering

📄 [arXiv](https://arxiv.org/abs/2601.21571)　📅 2026-01

**关键词**：`defense`、`pretraining data`、`token filtering`、`capability suppression`

👤 **作者**：Neil Rathi、Alec Radford

- 🎯 **研究动机**：现有削减不良能力的方法多为事后且易被绕过；文档级数据过滤过于粗糙、易误伤良性知识
- 🔬 **研究方法**：以医疗能力移除为代理任务，用稀疏自编码器标注 token 并蒸馏廉价分类器，在 token 级过滤预训练数据并训练跨两个数量级规模的模型
- 📌 **结论**：token 过滤比文档过滤以更低代价达成同等能力压制；规模越大越有效，最大模型在遗忘域造成 7000 倍算力减速，且遗忘域仍可对齐、对标签噪声鲁棒

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current approaches to reducing undesired capabilities in language models are largely post hoc, and can thus be easily bypassed by adversaries. A natural alternative is to shape capabilities during pretraining itself. On the proxy task of removing medical capabilities, we show that the simple intervention of filtering pretraining data is highly effective, robust, and inexpensive at scale. Inspired by work on data attribution, we show that filtering tokens is more effective than filtering documents, achieving the same hit to undesired capabilities at a lower cost to benign ones. Training models spanning two orders of magnitude, we then demonstrate that filtering gets more effective with scale: for our largest models, token filtering leads to a 7000x compute slowdown on the forget domain. We also show that models trained with token filtering can still be aligned on the forget domain. Along the way, we introduce a methodology for labeling tokens with sparse autoencoders and distilling cheap, high-quality classifiers. We also demonstrate that filtering can be robust to noisy labels with sufficient pretraining compute.

</details>

### 23. Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions

📄 [arXiv](https://arxiv.org/abs/2602.09987)　📅 2026-02

**关键词**：`tool`、`training-data editing`、`influence functions`、`behavior shaping`

👤 **作者**：J Rosser、Robert Kirk、Edward Grefenstette、Jakob Foerster、Laura Ruis

- 🎯 **研究动机**：影响函数只被用于归因行为，反向构造可诱导目标行为的训练数据未被探索
- 🔬 **研究方法**：Infusion 用可扩展影响函数近似计算训练文档微扰动，经参数偏移诱导目标行为变化
- 📌 **结论**：CIFAR-10 上仅编辑 0.2% 训练文档即可媲美显式样本投毒，且攻击可跨 ResNet/CNN 架构迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Influence functions are commonly used to attribute model behavior to training documents. We explore the reverse: crafting training data that induces model behavior. Our framework, Infusion, uses scalable influence-function approximations to compute small perturbations to training documents that induce targeted changes in model behavior through parameter shifts. We evaluate Infusion on data poisoning tasks across vision and language domains. On CIFAR-10, we show that making subtle edits via Infusion to just 0.2% (100/45,000) of the training documents can be competitive with the baseline of inserting a small number of explicit behavior examples. We also find that Infusion transfers across architectures (ResNet $\leftrightarrow$ CNN), suggesting a single poisoned corpus can affect multiple independently trained models. In preliminary language experiments, we characterize when our approach increases the probability of target behaviors and when it fails, finding it most effective at amplifying behaviors the model has already learned. Taken together, these results show that small, subtle edits to training data can systematically shape model behavior, underscoring the importance of training data interpretability for adversaries and defenders alike. We provide the code here: https://github.com/jrosseruk/infusion.

</details>

### 24. Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation

📄 [arXiv](https://arxiv.org/abs/2607.14493) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/karanjai)　📅 2026-07　🏷 USENIX Security 2026

**关键词**：`benchmark`、`attack`、`passive prompt injection`、`security log`、`prompt injection`、`defense-in-depth`

👤 **作者**：Rabimba Karanjai、Yang Lu、Hemanth Hegadehalli Madhavarao、Lei Xu、Weidong Shi

- 🎯 **研究动机**：SOC 用 LLM 分析外部日志，日志生成字段中的注入载荷可持久存储并在分析师查询时执行（passive prompt injection）
- 🔬 **研究方法**：提出 LogInject 框架与 12,847 条日志（2,569 对抗样本）基准，评估三个生产 LLM 在活动隐匿、误报生成、信息外泄与输出劫持四目标下的表现，并提出跨条目分片的 Context Stitching；测试输入过滤+提示加固+输出验证的分层缓解
- 📌 **结论**：基线 ASR 最高 88.2%（平均 83.4%），Context Stitching 达 76.4%；分层防御降低 90.4% 攻击但残留 8.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural language contexts to generate security insights. We demonstrate that this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term passive prompt injection. We present LogInject, a systematic framework for evaluating these threats. Using LogInject-1.0, a benchmark of 12,847 log entries including 2,569 adversarial samples, we evaluate three production LLMs across four attack objectives: activity concealment, false positive generation, information exfiltration, and output hijacking. Our findings reveal an up to 88.2% attack success rate (83.4% average across models) under the baseline conditions. We introduce Context Stitching, a novel technique that fragments payloads across multiple log entries to evade stateless filters while exploiting LLM long-context reasoning, achieving a 76.4% success rate. As mitigation, we evaluate layered defenses by combining input filtering, prompt hardening, and output validation, demonstrating a 90.4% attack reduction, although 8.4% residual vulnerability persists. Our results establish that LLM-based log analysis creates an inherent confused deputy vulnerability where untrusted data and trusted instructions compete indistinguishably for model attention, requiring defense in-depth architectures and continued human oversight for security-critical decisions.

</details>

### 25. Detecting Contaminated Code-Generation Prompt Batches via Influence Functions

📄 [arXiv](https://arxiv.org/abs/2608.14303)　📅 2026-08

**关键词**：`detection`、`language-model poisoning`、`training data`、`behavior manipulation`

👤 **作者**：Francesco Quinzan、Noor Munir、Yishun Lu、Stephen Roberts

- 🎯 **研究动机**：现有代码安全防御依赖预定义威胁模型或已知漏洞模式，对新攻击类别效果有限
- 🔬 **研究方法**：CodeSIFT 威胁模型无关：用影响函数度量生成代码的参数空间影响，统计检验判断候选 prompt 批是否偏离良性参考分布，并构建两个漏洞基准
- 📌 **结论**：三个 3B-7B 开源代码 LLM 上中高注入率时 AUROC 达 0.98，误报率校准良好，显著超过静态分析基线

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabilities, CodeSIFT measures the parameter-space influence of generated code and uses a statistical test to determine whether a candidate prompt set deviates from a benign reference distribution. To evaluate our approach, we introduce two benchmark datasets covering a variety of vulnerabilities. We evaluate CodeSIFT on three open-weight code LLMs ranging from 3B to 7B parameters, achieving AUROC scores of up to 0.98 at moderate-to-high injection rates, while maintaining well-calibrated false positive rates and substantially outperforming static analysis baselines. These results suggest that influence-function-based detection is a promising direction for identifying malicious code-generation prompts without requiring prior knowledge of the underlying attack class.

</details>