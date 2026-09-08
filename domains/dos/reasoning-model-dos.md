# 推理模型 DoS

## 研究方向

推理模型 DoS 研究如何利用 LRM/RLM 的显式思维链、试探回溯、自我反思和任务分解来放大推理开销。与普通 LLM 的重复输出不同，这类攻击通常让模型在得到答案前持续探索错误路径，因此需要同时评估 reasoning token、端到端延迟、吞吐、答案正确率和攻击查询成本。

## 研究脉络

- **问题基础：** Reasoning-model DoS 利用推理预算会随搜索难度和自反思深度增长这一特性。
- **早期方法：** 攻击通过 decoy context 和字符任务延长 CoT，让模型在无效路径上持续推理。
- **自动化与结构化攻击：** 后续方法发展为黑盒优化、递归熵引导和 SMT conflict 驱动的搜索放大。

## 结构化搜索与递归放大

### 1. SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance

📄 [arXiv](https://arxiv.org/abs/2608.18921)　📅 2026-08

**关键词**：`attack`、`reasoning-model DoS`、`SMT conflict`、`search amplification`

👤 **作者**：Jian Yang、…、Bin Liang

- 🎯 **研究动机**：现有 LRM-DoS 依赖模型反馈合成查询、需重复查询目标或训练攻击模型，代价高削弱杠杆
- 🔬 **研究方法**：SMTrap 免模型反馈的 search amplification 范式：以 SMT 求解器冲突计数为低成本外部信号引导合成推理重的 CSP 实例（冲突数与 LRM 回溯搜索正相关），纯 CPU 轻量框架
- 📌 **结论**：七个前沿模型上产生数倍于基线的 DoS 效果；基于工具的缓解可显著削减 token 使用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing LRM-DoS methods rely heavily on model feedback to synthesize attack queries, requiring either repeated queries to the target model or training a dedicated attack model. These expensive operations severely weaken attack leverage. In this paper, we propose \emph{search amplification}, a novel, model-feedback-free LRM-DoS paradigm. It employs the conflict count derived from an Satisfiability Modulo Theories (SMT) solver as a low-cost external signal to guide the synthesis of inference-heavy Constraint Satisfaction Problem (CSP) instances. Our key observation is that LRMs depend on trial-and-backtracking search when solving CSPs, where higher SMT conflict counts on a given CSP instance positively correlate with more extensive LRM backtracking search and substantially longer output trajectories. Building on this finding, we propose \textsc{SMTrap}, a lightweight, CPU-only framework. Guided by SMT conflict counts, \textsc{SMTrap} generates inference-heavy CSP queries without model queries, attack-model training, or GPU computation. Evaluations across seven frontier models demonstrate the state-of-the-art LRM-DoS capability of \textsc{SMTrap}, producing DoS effects multiple times stronger than existing baselines. To mitigate the threat of \textsc{SMTrap}, we demonstrate a tool-based mitigation that significantly cuts token usage.

</details>

### 2. RECUR: Resource Exhaustion Attack via Recursive-Entropy Guided Counterfactual Utilization and Reflection

📄 [arXiv](https://arxiv.org/abs/2602.08214)　📅 2026-02

**关键词**：`attack`、`reasoning-model DoS`、`recursive entropy`、`counterfactual question`

👤 **作者**：Ziwei Wang、…、Yang Liu

- 🎯 **研究动机**：推理模型的反思环节可被诱发过度反思而耗尽算力，缺少量化指标
- 🔬 **研究方法**：定义 Recursive Entropy 度量反思的资源消耗风险，RECUR 据此构造反事实问题诱发过度反思
- 📌 **结论**：良性推理下该熵递减；攻击使输出长度最多增 11 倍、吞吐下降 90%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) employ reasoning to address complex tasks. Such explicit reasoning requires extended context lengths, resulting in substantially higher resource consumption. Prior work has shown that adversarially crafted inputs can trigger redundant reasoning processes, exposing LRMs to resource-exhaustion vulnerabilities. However, the reasoning process itself, especially its reflective component, has received limited attention, even though it can lead to over-reflection and consume excessive computing power. In this paper, we introduce Recursive Entropy to quantify the risk of resource consumption in reflection, thereby revealing the safety issues inherent in inference itself. Based on Recursive Entropy, we introduce RECUR, a resource exhaustion attack via Recursive Entropy guided Counterfactual Utilization and Reflection. It constructs counterfactual questions to verify the inherent flaws and risks of LRMs. Extensive experiments demonstrate that, under benign inference, recursive entropy exhibits a pronounced decreasing trend. RECUR disrupts this trend, increasing the output length by up to 11x and decreasing throughput by 90%. Our work provides a new perspective on robust reasoning.

</details>

### 3. ExtendAttack: Attacking Servers of LRMs via Extending Reasoning

📄 [arXiv](https://arxiv.org/abs/2506.13737) · 🌐 [Project](https://ojs.aaai.org/index.php/AAAI/article/view/40833)　📅 2025-06　🏷 AAAI 2026

**关键词**：`attack`、`reasoning-model DoS`、`character obfuscation`、`decoding task`

👤 **作者**：Zhenhao Zhu、…、Jiaheng Zhang

- 🎯 **研究动机**：大推理模型的推理资源消耗可被攻击者恶意利用以挤占服务器资源
- 🔬 **研究方法**：提出 ExtendAttack：把良性 prompt 中的字符系统混淆为复杂多进制 ASCII 表示，迫使模型执行大量内嵌解码子任务
- 📌 **结论**：o3 在 HumanEval 上响应长度增超 2.7 倍且答案准确率不变，隐蔽性强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) have demonstrated promising performance in complex tasks. However, the resource-consuming reasoning processes may be exploited by attackers to maliciously occupy the resources of the servers, leading to a crash, like the DDoS attack in cyber. To this end, we propose a novel attack method on LRMs termed ExtendAttack to maliciously occupy the resources of servers by stealthily extending the reasoning processes of LRMs. Concretely, we systematically obfuscate characters within a benign prompt, transforming them into a complex, poly-base ASCII representation. This compels the model to perform a series of computationally intensive decoding sub-tasks that are deeply embedded within the semantic structure of the query itself. Extensive experiments demonstrate the effectiveness of our proposed ExtendAttack. Remarkably, it significantly increases response length and latency, with the former increasing by over 2.7 times for the o3 model on the HumanEval benchmark. Besides, it preserves the original meaning of the query and achieves comparable answer accuracy, showing the stealthiness.

</details>

### 4. Inducing Overthink: Hierarchical Genetic Algorithm-based DoS Attack on Black-Box Large Language Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2605.13338) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62234)　📅 2026-05　🏷 ICML 2026

**关键词**：`attack`、`reasoning-model DoS`、`hierarchical genetic algorithm`、`overthinking`、`adversarial attack`、`empirical evaluation`

👤 **作者**：Shuqiang Wang、…、Zhixuan Chu

- 🎯 **研究动机**：LRM 遇到不完整或逻辑不一致输入会过度思考，显著推高延迟与能耗，构成 DoS 向量
- 🔬 **研究方法**：黑盒框架用分层遗传算法在结构化问题分解上扰动逻辑结构，复合适应度同时最大化输出长度与反思型过度思考标记
- 📌 **结论**：四个 SOTA 推理模型上输出长度最高放大 26.1 倍（MATH）；小代理模型进化的对抗输入对大型商用 LRM 保持强迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Reasoning Models (LRMs) are increasingly integrated into systems requiring reliable multi-step inference, yet this growing dependence exposes new vulnerabilities related to computational availability. In particular, LRMs exhibit a tendency to "overthink", producing excessively long and redundant reasoning traces, when confronted with incomplete or logically inconsistent inputs. This behavior significantly increases inference latency and energy consumption, forming a potential vector for denial-of-service (DoS) style resource exhaustion. In this work, we investigate this attack surface and propose an automated black-box framework that induces overthinking in LRMs by systematically perturbing the logical structure of input problems. Our method employs a hierarchical genetic algorithm (HGA) operating on structured problem decompositions, and optimizes a composite fitness function designed to maximize both response length and reflective overthinking markers. Across four state-of-the-art reasoning models, the proposed method substantially amplifies output length, achieving up to a 26.1x increase on the MATH benchmark and consistently outperforming benign and manually crafted missing-premise baselines. We further demonstrate strong transferability, showing that adversarial inputs evolved using a small proxy model retain high effectiveness against large commercial LRMs. These findings highlight overthinking as a shared and exploitable vulnerability in modern reasoning systems, underscoring the need for more robust defenses.

</details>

### 5. ReasoningBomb: A Stealthy Denial-of-Service Attack by Inducing Pathologically Long Reasoning in Large Reasoning Models

📄 [arXiv](https://arxiv.org/abs/2602.00154) · 🎓 [Official](https://www.sigsac.org/ccs/CCS2026/program/accepted-papers.html)　📅 2026-01　🏷 ACM CCS 2026

**关键词**：`attack`、`reasoning-model DoS`、`attack model`、`proxy reward`、`inference-time DoS`、`large reasoning model`

👤 **作者**：Xiaogeng Liu、…、Chaowei Xiao

- 🎯 **研究动机**：大推理模型的高推理成本带来 prompt 诱导的推理时 DoS（PI-DoS）新攻击面
- 🔬 **研究方法**：形式化 PI-DoS 的高放大率、隐蔽性与可优化性三性质，ReasoningBomb 以常数时间代理奖励做 RL，训练攻击者生成短自然 prompt 诱发病态超长推理
- 📌 **结论**：七个开源与三个商业模型上平均诱导 18759 个 completion token、输入-输出放大 286.7 倍，超亚军 35%/38%；对输入、输出与双阶段检测的绕过率分别达 99.8%、98.7% 与 98.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large reasoning models (LRMs) extend large language models with explicit multi-step reasoning traces, but this capability introduces a new class of prompt-induced inference-time denial-of-service (PI-DoS) attacks that exploit the high computational cost of reasoning. We first formalize inference cost for LRMs and define PI-DoS, then prove that any practical PI-DoS attack should satisfy three properties: (1) a high amplification ratio, where each query induces a disproportionately long reasoning trace relative to its own length; (ii) stealthiness, in which prompts and responses remain on the natural language manifold and evade distribution shift detectors; and (iii) optimizability, in which the attack supports efficient optimization without being slowed by its own success. Under this framework, we present ReasoningBomb, a reinforcement-learning-based PI-DoS framework that is guided by a constant-time surrogate reward and trains a large reasoning-model attacker to generate short natural prompts that drive victim LRMs into pathologically long and often effectively non-terminating reasoning. Across seven open-source models (including LLMs and LRMs) and three commercial LRMs, ReasoningBomb induces 18,759 completion tokens on average and 19,263 reasoning tokens on average across reasoning models. It outperforms the the runner-up baseline by 35% in completion tokens and 38% in reasoning tokens, while inducing 6-7x more tokens than benign queries and achieving 286.7x input-to-output amplification ratio averaged across all samples. Additionally, our method achieves 99.8% bypass rate on input-based detection, 98.7% on output-based detection, and 98.4% against strict dual-stage joint detection.

</details>

### 6. ThinkTrap: Denial-of-Service Attacks against Black-box LLM Services via Infinite Thinking

📄 [arXiv](https://arxiv.org/abs/2512.07086) · 🌐 [Project](https://www.ndss-symposium.org/ndss-paper/thinktrap-denial-of-service-attacks-against-black-box-llm-services-via-infinite-thinking/)　📅 2025-12　🏷 NDSS 2026

**关键词**：`attack`、`reasoning-model DoS`、`continuous subspace`、`infinite reasoning`

👤 **作者**：Yunzhe Li、Jianan Wang、Hongzi Zhu、James Lin、Shan Chang、Minyi Guo

- 🎯 **研究动机**：云端 LLM 服务面临经无限思考诱发资源耗尽的 DoS 威胁，黑盒闭源设定下难以优化攻击
- 🔬 **研究方法**：ThinkTrap 把离散 token 映射到连续嵌入空间，利用输入稀疏性在低维子空间做高效黑盒优化，寻找诱发超长或不终止生成的对抗 prompt
- 📌 **结论**：在常见 10 RPM 限频下即可把服务吞吐降至原有约 1%，某些情况引发完全服务失败

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) have become foundational components in a wide range of applications, including natural language understanding and generation, embodied intelligence, and scientific discovery. As their computational requirements continue to grow, these models are increasingly deployed as cloud-based services, allowing users to access powerful LLMs via the Internet. However, this deployment model introduces a new class of threat: denial-of-service (DoS) attacks via unbounded reasoning, where adversaries craft specially designed inputs that cause the model to enter excessively long or infinite generation loops. These attacks can exhaust backend compute resources, degrading or denying service to legitimate users. To mitigate such risks, many LLM providers adopt a closed-source, black-box setting to obscure model internals. In this paper, we propose ThinkTrap, a novel input-space optimization framework for DoS attacks against LLM services even in black-box environments. The core idea of ThinkTrap is to first map discrete tokens into a continuous embedding space, then undertake efficient black-box optimization in a low-dimensional subspace exploiting input sparsity. The goal of this optimization is to identify adversarial prompts that induce extended or non-terminating generation across several state-of-the-art LLMs, achieving DoS with minimal token overhead. We evaluate the proposed attack across multiple commercial, closed-source LLM services. Our results demonstrate that, even far under the restrictive request frequency limits commonly enforced by these platforms, typically capped at ten requests per minute (10 RPM), the attack can degrade service throughput to as low as 1% of its original capacity, and in some cases, induce complete service failure.

</details>

### 7. OverThink: Slowdown Attacks on Reasoning LLMs

📄 [arXiv](https://arxiv.org/abs/2502.02542)　📅 2025-02

**关键词**：`attack`、`reasoning-model DoS`、`context injection`、`decoy question`

👤 **作者**：Abhinav Kumar、…、Eugene Bagdasarian

- 🎯 **研究动机**：推理模型依赖外部上下文，推理 token 消耗带来新的成本攻击面
- 🔬 **研究方法**：向公共内容注入 MDP、数独等良性诱饵推理题，迫使模型花费大量推理 token 后仍给出正确答案
- 📌 **结论**：攻击跨开闭源模型迁移并可多模态实施，诱饵良性故绕过安全过滤

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most flagship language models generate explicit reasoning chains, enabling inference-time scaling. However, producing these reasoning chains increases token usage (i.e., reasoning tokens), which in turn increases latency and costs. Our OverThink attack increases overhead for applications that rely on reasoning language models (RLMs) and external context by forcing them to spend substantially more reasoning tokens while still producing contextually correct answers. An adversary mounts an attack by injecting decoy reasoning problems into public content that is consumed by RLM at inference time. Because our decoys (e.g., Markov decision processes, Sudokus, etc.) are benign, they evade safety filters. We evaluate OverThink on both closed-source and open-source reasoning models across the FreshQA, SQuAD, and MuSR datasets. We also explore the attack in multi-modal settings by creating images that cause excessive reasoning. We show that the resulting slowdown transfers across models. Finally, we explore both LLM-based and systems-level defenses, and discuss the societal, financial, and energy implications of the OverThink attacks.

</details>

### 8. Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems

📄 [arXiv](https://arxiv.org/abs/2607.01518)　📅 2026-07

**关键词**：`attack`、`VLM safety`、`reasoning DoS`、`overthinking attack`

👤 **作者**：Qiang Han、Jie Wu、Bo Chen

- 🎯 **研究动机**：LVLM 存在过度思考行为，攻击者可借场景文字故意触发超长推理拖慢机器人决策造成安全问题
- 🔬 **研究方法**：三阶段框架：构建推理密集场景文本语料并从短响应前缀提取过思考相关词汇特征、前缀代理分数引导黑盒搜索+少量全延迟确认、固定触发池在多 LVLM 与新图上评估迁移
- 📌 **结论**：三个 LVLM 上所有触发减速比 >1 倍，最强单触发 6.96 倍；物理打印文字仍达 4.74 倍延迟放大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Vision-Language Models (LVLMs) have been increasingly integrated into robotic systems. However, these models may exhibit overthinking behaviors, where they generate excessively long reasoning traces, incurring an excessive inference time. This overthinking behavior poses a serious risk to robotic systems, as the adversary can deliberately trigger overthinking to slow down the decision making of a victim robotic system, causing a variety of safety issues (i.e., an overthinking-induced slowdown attack). To initiate this attack, an adversary can embed carefully crafted, human-readable scene text into the visual scene observed by a victim robotic agent, causing significant inference delays even under a strict black-box setting. Therefore, the embedded scene text serves as a significant "trigger" for the attack. This work systematically identifies and validates transferable triggers of overthinking in robotic systems by introducing a three-stage framework. First, we construct a diverse corpus of reasoning-intensive scene text and extract overthinking-correlated lexical features from short response prefixes. Second, we perform an efficient black-box search guided by a prefix-based proxy score while selectively confirming a small set of top candidates with full latency measurements. Third, we evaluate black-box transfer using a fixed pool of triggers on unseen images and multiple LVLMs, reporting latency amplification and attack success rates under standard thresholds. Across three representative LVLMs, all triggers yield slowdown ratios greater than 1.0x, with the strongest single-trigger case reaching 6.96x. The physical printing of the text trigger still causes up to 4.74x latency amplification. These results demonstrate that our discovered triggers are transferred between multiple LVLM models and consistently cause significant slowdowns in robotic systems.

</details>