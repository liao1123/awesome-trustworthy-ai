# 其他投毒与后门

[返回投毒与后门目录](README.md)

本页收录尚未形成稳定独立子领域、但具有明确投毒或后门 threat model 的特殊方向。当前包括密码式模型后门、推荐系统投毒与持续学习投毒等方向；每个方向保留独立小节与边界，后续论文数量和方法路线足够稳定时再拆分为专页。

## 密码式模型后门

研究借助密码学不可区分性构造的模型后门在真实学习流程中的攻击可行性、统计隐蔽性与审计边界；本节只收录以模型后门为核心 threat model 的工作，不扩展到一般密码学研究。

> **边界说明：** 这里的 cryptographic backdoor 指攻击者植入的恶意条件后门，不是模型水印、版权保护或所有权验证。后门式水印相关工作见 [独立专题](../content-authenticity/backdoor-based-watermarking-and-ownership.md)。

### 现实隐蔽性与机制复测

### 1. Rethinking the Stealthiness of Cryptographically Undetectable Backdoors in Practical RFF Learning

🌐 [Project](https://doi.org/10.1145/3770855.3817768)　📅 2026-08　🏷 KDD 2026

**关键词**：`attack`、`cryptographic backdoor`、`random Fourier feature`、`stealth evaluation`

- 🎯 **研究动机**：基于 CLWE 困难性的密码学不可检测后门只保证参数空间白盒隐蔽性，其在实际 RFF 学习流水线中的隐蔽性未被检验
- 🔬 **研究方法**：理论上证明其运行有效性依赖与现实部署不相容的假设，并在表格与图像数据上实验验证
- 📌 **结论**：标准数据预处理会破坏输入空间隐蔽性并留下明显伪影，简单的输入级 sanity check 即可可靠识别后门输入；另给出 RFF 的认证鲁棒性分析

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Random Fourier Features (RFF) learning is a classical technique in scalable data mining. However, at FOCS 2022, Goldwasser et al. proposed a theoretical framework for planting cryptographically undetectable backdoors in RFF learning based on the hardness of the Continuous Learning With Errors (CLWE) problem. Their construction guarantees white-box undetectability in the model parameter space against any polynomial-time distinguisher. In this paper, we revisit the undetectability of CLWE backdoors from a practical RFF learning perspective. We prove that the operational validity of the CLWE backdoor critically hinges on assumptions that are incompatible with the realistic RFF learning deployment. Specifically, standard data preprocessing required for effective RFF learning fundamentally destroys the input-space stealthiness of CLWE backdoors, inevitably resulting in conspicuous input-level artifacts. We further validate our theoretical findings through extensive experiments on both tabular and image datasets, demonstrating that simple sanity checks at the input level suffice to reliably identify backdoored inputs. In addition, under the same threat model, we analyze the adversarial robustness of RFF learning models and provide a concrete certified robustness analysis, enabling a deeper security assessment of its practical deployment. Overall, our work emphasizes the importance of evaluating theoretical backdoor attacks under realistic machine learning pipelines and offers broader insights into the secure deployment of RFF learning systems.

</details>
### 检测与缓解

### 2. Silencing the Poison: An Unsupervised Granular Ball Defense Approach in Local Smoothing Context for Recommender Systems

🌐 [Project](https://doi.org/10.1145/3770855.3817740)　📅 2026-08　🏷 KDD 2026

**关键词**：`defense`、`recommender poisoning`、`unsupervised detection`、`local smoothing`

- 🎯 **研究动机**：推荐系统投毒缺无监督防御手段
- 🔬 **研究方法**：在局部平滑上下文中用granular ball无监督隔离毒样本
- 📌 **结论**：免标签即可削弱投毒攻击效果

## 推荐系统投毒与后门

研究推荐系统与 LLM 推荐系统中的 shilling、注入式投毒与后门攻击，以及物品侧语义审计和投毒检测等防御；联邦推荐与图神经网络的鲁棒性训练不在本节范围。

### 3. An Efficient and Effective Agentic Group Shilling Attack on Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2609.09551)　📅 2026-09

**关键词**：`attack`、`recommender poisoning`、`agentic shilling`、`fake profile`

👤 **作者**：Quoc Viet Nguyen、…、Thanh Tam Nguyen

- 🎯 **研究动机**：现有 shilling 攻击依赖针对特定目标的微调或固定画像模板，难以适应不同受害系统或更易被检测
- 🔬 **研究方法**：AGAS 协调式群体攻击：中央 Coordinator 指挥一组可切换角色的 worker agent 自适应推广目标物品，进展停滞或抑制信号增强时动态调整策略，worker 在活跃与休眠角色间切换以避免重复模式
- 📌 **结论**：同等攻击预算与评测协议下目标推广稳定超越强基线，同时更好保持良性推荐质量、削弱代表性检测器并提升攻击效率

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recommender systems have become core infrastructure for modern online platforms, personalizing content at scale and strongly influencing what users see, click on, and purchase. However, this dependence on user interaction also exposes them to shilling attacks, where malicious actors can inject fake profiles to distort item rankings and control visibility. Existing attacks often rely on target-specific fine-tuning or fixed profile templates, making them either difficult to adapt to different victims or easier to detect. To overcome these limitations, we propose the Agentic Group Attack System (AGAS), a coordinated shilling framework where a central Coordinator directs a group of role-switching worker agents to adaptively promote a target item across different victim families. The Coordinator dynamically adjusts the strategy when progress stalls or suppression signals increase, while workers pursue a shared objective and switch between active and inactive roles to avoid repetitive patterns. Under the same attack budgets and evaluation protocols, AGAS consistently surpasses strong baselines in target promotion while better preserving benign recommendation quality, weakening representative detectors, and achieving higher efficiency than prior attacks. These findings also emphasize that defending recommender systems may require mechanisms that can handle adaptive shilling campaigns, not just isolated fake-profile injections. Our code is available at https://github.com/phkhanhtrinh23/AGAS.

</details>

### 4. Prompt-Unknown Promotion Attacks against LLM-based Sequential Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2604.23640)　📅 2026-04

**关键词**：`attack`、`LLM-based recommendation poisoning`、`prompt inference`、`dual poisoning`

👤 **作者**：Yuchuan Zhao、Tong Chen、Junliang Yu、Zongwei Wang、Lizhen Cui、Hongzhi Yin

- 🎯 **研究动机**：LLM 序列推荐系统的推广攻击普遍假设能访问受害模型或系统 prompt，与真实场景不符
- 🔬 **研究方法**：PUDA 全黑盒框架：LLM 进化精炼推断离散系统 prompt 并训练模拟受害模型行为的代理，结合语义约束下的目标物品文本对抗改写与代理生成的可信投毒序列
- 📌 **结论**：真实数据集上持续超越 SOTA 竞争者，显著抬高不受欢迎目标物品的曝光，证明 prompt 与模型均受保护时仍有风险

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model-powered sequential recommender systems (LLM-SRSs) have recently demonstrated remarkable performance, enabling recommendations through prompt-driven inference over user interaction sequences. However, this paradigm also introduces new security vulnerabilities, particularly text-level manipulations, rendering them appealing targets for promotion attacks that purposely boost the ranking of specific target items. Although such security risks have been receiving increasing attention, existing studies typically rely on an unrealistic assumption of access to either the victim model or prompt to unveil attack mechanisms. In this work, we investigate the item promotion attack in LLM-SRSs under a more realistic setting where both the system prompt and victim model are unknown to the attacker, and propose a Prompt-Unknown Dual-poisoning Attack (PUDA) framework. To simulate attacks under this full black-box setting, we introduce an LLM-based evolutionary refinement strategy that infers discrete system prompts, enabling the training of an effective surrogate model that mimics the behaviors of the victim model. Leveraging the distilled prompt and surrogate model, we devise a promotion attack that adversarially revises target item texts under semantic constraints, which is further complemented by the highly plausible, surrogate-generated poisoning sequences to enable cost-effective target item promotion. Extensive experiments on real-world datasets demonstrate that PUDA consistently outperforms state-of-the-art competitors in boosting the exposure of unpopular target items. Our findings reveal critical security risks in modern LLM-SRSs even when both prompts and models are protected, and highlight the need for more robust defensive means.

</details>

### 5. Sharpness-Aware Poisoning: Enhancing Transferability of Injective Attacks on Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2604.22170)　📅 2026-04

**关键词**：`attack`、`recommender poisoning`、`sharpness-aware minimization`、`transferability`

👤 **作者**：Junsong Xie、Yonghui Yang、Pengyang Shao、Le Wu

- 🎯 **研究动机**：攻击者缺乏受害模型知识时用固定代理模型生成投毒数据，代理与受害模型结构差异大时迁移性显著受损
- 🔬 **研究方法**：SharpAP 用 sharpness-aware minimization 原理近似寻找最坏情况受害模型并针对性优化投毒数据，形成 min-max-min 三层优化并融入迭代攻击过程
- 📌 **结论**：三个真实数据集上显著提升注入式攻击的跨模型迁移性，缓解对代理模型的过拟合

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recommender Systems~(RS) have been shown to be vulnerable to injective attacks, where attackers inject limited fake user profiles to promote the exposure of target items to real users for unethical gains (e.g., economic or political advantages). Since attackers typically lack knowledge of the victim model deployed in the target RS, existing methods resort to using a fixed surrogate model to mimic the potential victim model. Despite considerable progress, we argue that the assumption that \textit{poisoned data generated for the surrogate model can be used to attack other victim models} is wishful. When there are significant structural discrepancies between the surrogate and victim models, the attack transferability inevitably suffers. Intuitively, if we can identify the worst-case victim model and iteratively optimize the poisoning effect specifically against it, then the generated poisoned data would be better transferred to other victim models. However, exactly identifying the worst-case victim model during the attack process is challenging due to the large space of victim models. To this end, in this work, we propose a novel attack method called Sharpness-Aware Poisoning (\textit{SharpAP}). Specifically, it employs the sharpness-aware minimization principle to seek the approximately worst-case victim model and optimizes the poisoned data specifically for this worst-case model. The poisoning attack with SharpAP is formulated as a min-max-min tri-level optimization problem. By integrating SharpAP into the iterative process for attacks, our method can generate more robust poisoned data which is less sensitive to the shift of model structure, mitigating the overfitting to the surrogate model. Comprehensive experimental comparisons on three real-world datasets demonstrate that \name~can significantly enhance the attack transferability.

</details>

### 6. IndirectAD: Practical Data Poisoning Attacks against Recommender Systems for Item Promotion

📄 [arXiv](https://arxiv.org/abs/2511.05845)　📅 2025-11

**关键词**：`attack`、`recommender poisoning`、`trigger item`、`low-ratio injection`

👤 **作者**：Zihao Wang、Tianhao Mao、XiaoFeng Wang、Di Tang、Xiaozhong Liu

- 🎯 **研究动机**：推荐投毒攻击通常需控制至少 1% 平台用户，在大规模平台上难以实现，威胁常被低估
- 🔬 **研究方法**：IndirectAD 借鉴木马思路：先推广更易被推荐给目标用户的触发物品，再构造与目标物品的共现数据把优势转移给目标
- 📌 **结论**：多数据集与多推荐系统上仅控制 0.05% 平台用户即可造成显著推广效果，大规模设定下仍然有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recommender systems play a central role in digital platforms by providing personalized content. They often use methods such as collaborative filtering and machine learning to accurately predict user preferences. Although these systems offer substantial benefits, they are vulnerable to security and privacy threats, especially data poisoning attacks. By inserting misleading data, attackers can manipulate recommendations for purposes ranging from boosting product visibility to shaping public opinion. Despite these risks, concerns are often downplayed because such attacks typically require controlling at least 1% of the platform's user base, a difficult task on large platforms. We tackle this issue by introducing the IndirectAD attack, inspired by Trojan attacks on machine learning. IndirectAD reduces the need for a high poisoning ratio through a trigger item that is easier to recommend to the target users. Rather than directly promoting a target item that does not match a user's interests, IndirectAD first promotes the trigger item, then transfers that advantage to the target item by creating co-occurrence data between them. This indirect strategy delivers a stronger promotion effect while using fewer controlled user accounts. Our extensive experiments on multiple datasets and recommender systems show that IndirectAD can cause noticeable impact with only 0.05% of the platform's user base. Even in large-scale settings, IndirectAD remains effective, highlighting a more serious and realistic threat to today's recommender systems.

</details>

### 7. Exploring Backdoor Attack and Defense for LLM-empowered Recommendations

📄 [arXiv](https://arxiv.org/abs/2504.11182)　📅 2025-04

**关键词**：`attack`、`defense`、`LLM recommendation backdoor`、`poison scanner`

👤 **作者**：Liangbo Ning、Wenqi Fan、Qing Li

- 🎯 **研究动机**：LLM 与推荐系统融合后对后门攻击的安全性基本未被探索
- 🔬 **研究方法**：BadRec 扰动物品标题植入触发器并以多个伪造用户交互投毒训练集；防御侧 P-Scanner 用 LLM 毒化扫描器加触发器增广 agent 学习毒化物品检测的领域知识
- 📌 **结论**：投毒 1% 训练数据即可成功植入后门并操纵推荐响应；P-Scanner 在三个真实数据集上验证有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The fusion of Large Language Models (LLMs) with recommender systems (RecSys) has dramatically advanced personalized recommendations and drawn extensive attention. Despite the impressive progress, the safety of LLM-based RecSys against backdoor attacks remains largely under-explored. In this paper, we raise a new problem: Can a backdoor with a specific trigger be injected into LLM-based Recsys, leading to the manipulation of the recommendation responses when the backdoor trigger is appended to an item's title? To investigate the vulnerabilities of LLM-based RecSys under backdoor attacks, we propose a new attack framework termed Backdoor Injection Poisoning for RecSys (BadRec). BadRec perturbs the items' titles with triggers and employs several fake users to interact with these items, effectively poisoning the training set and injecting backdoors into LLM-based RecSys. Comprehensive experiments reveal that poisoning just 1% of the training data with adversarial examples is sufficient to successfully implant backdoors, enabling manipulation of recommendations. To further mitigate such a security threat, we propose a universal defense strategy called Poison Scanner (P-Scanner). Specifically, we introduce an LLM-based poison scanner to detect the poisoned items by leveraging the powerful language understanding and rich knowledge of LLMs. A trigger augmentation agent is employed to generate diverse synthetic triggers to guide the poison scanner in learning domain-specific knowledge of the poisoned item detection task. Extensive experiments on three real-world datasets validate the effectiveness of the proposed P-Scanner.

</details>

### 8. Poison-RAG: Adversarial Data Poisoning Attacks on Retrieval-Augmented Generation in Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2501.11759)　📅 2025-01

**关键词**：`attack`、`RAG-based recommender`、`metadata poisoning`、`black-box attack`

👤 **作者**：Fatemeh Nazary、Yashar Deldjoo、Tommaso di Noia

- 🎯 **研究动机**：RAG 推荐系统把物品元数据送入检索与生成链路，供给端可借元数据操纵推荐结果
- 🔬 **研究方法**：Poison-RAG 在黑盒设定下用 LLM 生成物品元数据，提出基于 BERT 嵌入的逐物品局部标签修改与全局统一标签两种投毒策略，以推广长尾物品、压制热门物品
- 📌 **结论**：MovieLens 上局部策略最多提升 50% 操纵效果而全局策略可能反向助推热门；约 70% 物品缺标签带来冷启动式的更大攻击面

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

This study presents Poison-RAG, a framework for adversarial data poisoning attacks targeting retrieval-augmented generation (RAG)-based recommender systems. Poison-RAG manipulates item metadata, such as tags and descriptions, to influence recommendation outcomes. Using item metadata generated through a large language model (LLM) and embeddings derived via the OpenAI API, we explore the impact of adversarial poisoning attacks on provider-side, where attacks are designed to promote long-tail items and demote popular ones. Two attack strategies are proposed: local modifications, which personalize tags for each item using BERT embeddings, and global modifications, applying uniform tags across the dataset. Experiments conducted on the MovieLens dataset in a black-box setting reveal that local strategies improve manipulation effectiveness by up to 50\%, while global strategies risk boosting already popular items. Results indicate that popular items are more susceptible to attacks, whereas long-tail items are harder to manipulate. Approximately 70\% of items lack tags, presenting a cold-start challenge; data augmentation and synthesis are proposed as potential defense mechanisms to enhance RAG-based systems' resilience. The findings emphasize the need for robust metadata management to safeguard recommendation frameworks. Code and data are available at https://github.com/atenanaz/Poison-RAG.

</details>

### 9. SemanticShield: LLM-Powered Audits Expose Shilling Attacks in Recommender Systems

📄 [arXiv](https://arxiv.org/abs/2509.24961)　📅 2025-09

**关键词**：`defense`、`shilling detection`、`LLM audit`、`item-side semantics`

👤 **作者**：Kaihong Li、Huichi Zhou、Bin Ma、Fangjun Huang

- 🎯 **研究动机**：现有 shilling 防御强调用户侧行为特征，忽视标题、描述等能暴露恶意意图的物品侧语义
- 🔬 **研究方法**：SemanticShield 两阶段：低成本行为准则预筛可疑用户，再由强化微调的轻量 LLM 审计物品语义一致性
- 📌 **结论**：六种代表性攻击策略上检测有效，对未见攻击方法展现强泛化能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recommender systems (RS) are widely used in e-commerce for personalized suggestions, yet their openness makes them susceptible to shilling attacks, where adversaries inject fake behaviors to manipulate recommendations. Most existing defenses emphasize user-side behaviors while overlooking item-side features such as titles and descriptions that can expose malicious intent. To address this gap, we propose a two-stage detection framework that integrates item-side semantics via large language models (LLMs). The first stage pre-screens suspicious users using low-cost behavioral criteria, and the second stage employs LLM-based auditing to evaluate semantic consistency. Furthermore, we enhance the auditing model through reinforcement fine-tuning on a lightweight LLM with carefully designed reward functions, yielding a specialized detector called SemanticShield. Experiments on six representative attack strategies demonstrate the effectiveness of SemanticShield against shilling attacks, and further evaluation on previously unseen attack methods shows its strong generalization capability. Code is available at https://github.com/FrankenstLee/SemanticShield.

</details>

## 持续学习投毒与后门分析

研究持续学习（continual learning）流程中的投毒与后门威胁及其理论边界，并收录神经符号后门、低 ASR 非对称后门与 data-free 后门检测等尚未独立成域的投毒与后门方向。

### 10. Low-ASR Backdoors: Exploiting Attack Success Rate Reduction and Attacker-Defender Asymmetry

📄 [arXiv](https://arxiv.org/abs/2608.27288)　📅 2026-08

**关键词**：`attack`、`analysis`、`low-ASR backdoor`、`reverse training`、`defense evasion`、`backdoor-evaluation validity`

👤 **作者**：Arham Riaz、Ting Yu

- 🎯 **研究动机**：后门攻防默认有效后门必具高 ASR 并以此设计与评测防御，但 ASR 是攻击者可控变量而非后门固有属性
- 🔬 **研究方法**：提出 reverse-training 框架，主动削弱 trigger–target 关联，生成保留干净输入性能的低 ASR 后门模型
- 📌 **结论**：跨多个数据集、攻击家族与架构，SOTA 防御在低 ASR 条件下一致失效，暴露根本性的攻防不对称

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks are among the most effective and stealthy attacks in deep learning. Existing attacks and defenses are largely designed and evaluated under the assumption that successful backdoors exhibit high Attack Success Rates (ASRs). In this paper, we show that this assumption creates a fundamental weakness in existing defense paradigms. ASR is not an intrinsic property of a backdoor; rather, it is an attacker-controlled variable that can be deliberately reduced without eliminating the underlying backdoor behavior. We introduce a reverse-training framework that weakens the trigger-target association, producing low-ASR backdoor models while preserving clean-input performance. Through extensive evaluation across multiple datasets, diverse attack families, and multiple architectures, we show that state-of-the-art defenses fail consistently under low-ASR conditions, exposing a fundamental attacker-defender asymmetry.

</details>

### 11. Does Reasoning Mitigate Backdoor Attacks? A Neuro-Symbolic Perspective

📄 [arXiv](https://arxiv.org/abs/2609.00464)　📅 2026-09

**关键词**：`attack`、`neuro-symbolic backdoor`、`reasoning robustness`、`DeepProbLog`

👤 **作者**：Marco Antonio Corallo、Andrea Agiollo、Mauro Conti、Alberto Giaretta

- 🎯 **研究动机**：神经符号模型常被视为 robust-by-design，但 neural-symbolic 集成本身可能是新攻击入口，后门鲁棒性未系统评估
- 🔬 **研究方法**：首次系统评测 NeSy 后门：在最流行框架 DeepProbLog 与神经基线间比较八种后门设置与四类推理任务
- 📌 **结论**：NeSy 平均更鲁棒，但鲁棒性高度依赖推理过程的严格程度与对抗目标的兼容性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neuro-Symbolic (NeSy) AI has recently emerged as a novel paradigm to enable trustworthy AI, aiming at integrating sub-symbolic neural perception with grounded symbolic reasoning. The neuro-symbolic integration process that characterizes these models has been proven beneficial to achieve more transparent, explainable and efficient AI systems. Meanwhile, their properties under adversarial settings have been overlooked being frequently deemed robust-by-design. However, the neural-symbolic integration process they leverage constitutes an additional layer of complexity that may provide an attack entry-point. Therefore, in this paper, we claim that an in-depth investigation of the adversarial robustness of NeSy models is necessary and provide the first systematic evaluation of backdoor attacks against NeSy. To this end, we compare the most popular NeSy framework, namely DeepProbLog, against baseline neural networks across a total of eight backdoor settings and four reasoning tasks. Our experimental results show that while NeSy models are indeed more robust than their neural counterpart on average, their robustness vastly depend on the strictness of the reasoning process being enforced and its compatibility with the chosen adversarial target. The source code to reproduce our experiments is made available at https://github.com/marcoantoniocorallo/NeSy-Backdoor.

</details>

### 12. Catastrophic Learning: A New Attack Vector on Continual Learning Networks

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

### 13. Theory of Continual Learning Against Data Poisoning Attacks

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

### 14. Safety-Efficacy Trade Off: Robustness against Data-Poisoning

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

### 15. Unveiling the Pitfalls of Data-Free Backdoor Detection Against Pre-Trained Models

🎓 [Official](https://www.usenix.org/conference/usenixsecurity26/presentation/zhao-quan)　📅 2026　🏷 USENIX Security 2026

**关键词**：`detection`、`benchmark`、`backdoor detection`、`pre-trained model`、`convergence side channel`

👤 **作者**：Quan Zhao、…、Yang Zhang

- 🎯 **研究动机**：无数据后门检测方法很少在预训练模型上评估，报告的强性能可能造成虚假安全感
- 🔬 **研究方法**：构建覆盖 30000 多个模型与常见后门攻击的大规模基准；提出以收敛速度作为侧信道信号的新检测器
- 📌 **结论**：现有无数据方法在多数预训练模型上失效；新检测器达 SOTA，但严重漏洞仍存

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to deep learning models, enabling adversaries to manipulate the output through hidden triggers. Recent detection methods aim to identify backdoors without relying on clean samples or assumptions about attacks. Although they report strong performance, these methods are rarely evaluated on pre-trained models. In this paper, we present the first large-scale study of data-free backdoor detection on pre-trained models. Our benchmark includes more than 30,000 models and covers common backdoor attacks. We find that existing data-free methods fail on most pre-trained models, leading to a false sense of security. Despite our effective improvements, serious vulnerabilities remain. To address this, we propose using convergence speed as a new side-channel signal for backdoor detection. Using this signal, we reveal the cause of the remaining vulnerabilities and build a novel data-free detector that achieves state-of-the-art performance against existing methods. We further analyze how backdoor attacks evade detection and outline unresolved issues. Our results indicate that detecting backdoor attacks requires further exploration. We hope our work can draw attention to the vulnerabilities in backdoor detection mechanisms for machine learning systems.

</details>

### 16. Persistent Backdoor Attacks in Continual Learning

📄 [arXiv](https://arxiv.org/abs/2409.13864)　📅 2024-09

**关键词**：`attack`、`continual learning backdoor`、`persistent backdoor`、`defense evasion`

👤 **作者**：Zhen Guo、Abhinav Kumar、Reza Tourani

- 🎯 **研究动机**：持续学习的参数持续更新如何影响后门的实用性与持久性缺乏研究
- 🔬 **研究方法**：提出 Blind Task Backdoor（仅微改损失计算、不直接控制训练）与 Latent Task Backdoor（仅影响单个任务训练）两种最小影响攻击
- 📌 **结论**：静态、动态、物理与语义触发器下跨持续学习算法均保持高成功率，并规避 SentiNet、I-BAU 等 SOTA 防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Backdoor attacks pose a significant threat to neural networks, enabling adversaries to manipulate model outputs on specific inputs, often with devastating consequences, especially in critical applications. While backdoor attacks have been studied in various contexts, little attention has been given to their practicality and persistence in continual learning, particularly in understanding how the continual updates to model parameters, as new data distributions are learned and integrated, impact the effectiveness of these attacks over time. To address this gap, we introduce two persistent backdoor attacks-Blind Task Backdoor and Latent Task Backdoor-each leveraging minimal adversarial influence. Our blind task backdoor subtly alters the loss computation without direct control over the training process, while the latent task backdoor influences only a single task's training, with all other tasks trained benignly. We evaluate these attacks under various configurations, demonstrating their efficacy with static, dynamic, physical, and semantic triggers. Our results show that both attacks consistently achieve high success rates across different continual learning algorithms, while effectively evading state-of-the-art defenses, such as SentiNet and I-BAU.

</details>

### 17. Amnesia: A Stealthy Replay Attack on Continual Learning Dreams

📄 [arXiv](https://arxiv.org/abs/2606.12655)　📅 2026-06

**关键词**：`attack`、`experience replay poisoning`、`replay index selection`、`auditable constraint`

👤 **作者**：Ahmed Sharshar、Naveen Kumar Kummari、Mohsen Guizani

- 🎯 **研究动机**：持续学习经验重放的采样干扰鲁棒性未被研究，现有攻击缺乏可审计的现实约束
- 🔬 **研究方法**：Amnesia 假设内部人员仅控制重放索引：用 EMA 损失或置信度计算类效用以倾斜名义类分布，再用 KL 或 TV 投影投回审计半径内，滑动窗口调度器满足滚动审计
- 📌 **结论**：各 CL 基准与强重放基线上一致降低最终 ACC 并恶化反向迁移；KL 变体在多种审计方案下基本不被察觉，TV 变体破坏更强但更易被检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual learning (CL) models often use experience replay to reduce catastrophic forgetting, but their robustness to replay sampling interference remains underexplored. Existing CL attacks alter inputs or training pipelines (poisoning/backdoors) and rarely include explicit auditable constraints, limiting realism. Here, auditability means a monitor can verify compliance from sampler-visible telemetry - e.g., logged replay index/label statistics - by checking that the realized replay class histogram stays close to a nominal baseline and that replay rate is unchanged per batch and/or over a rolling window. We study a limited-privilege insider who controls only replay index selection, not pixels, labels, or model parameters, while staying within auditable limits such as queue priorities. We introduce Amnesia, a replay composition attack that maximizes degradation under two budgets: a visibility budget delta bounding the TV/KL divergence from a nominal class histogram p0, and a mass budget f fixing the replay rate. Amnesia has two steps: (i) compute lightweight class utilities, such as EMA loss or confidence, to tilt p0 toward harmful classes; and (ii) project the tilt back into the delta-ball using efficient KL (exponential tilt) or TV (balanced mass redistribution) optimizers. A windowed scheduler enforces rolling audits. Across challenging CL benchmarks and strong replay baselines, Amnesia consistently lowers final accuracy (ACC) and worsens backward transfer (-BWT). The KL variant delivers high impact while remaining largely undetected under multiple audit schemes, including per-batch and rolling-window checks. The TV variant is more damaging but easier to detect, especially under tight per-class constraints. These results expose index-only replay control as a practical, auditable threat surface in CL systems and establish a principled impact-visibility trade-off.

</details>

### 18. Robust Dynamic Expansion for Continual Learning under Backdoor Attacks via Purification and Selective Recovery

📄 [arXiv](https://arxiv.org/abs/2609.06346)　📅 2026-09

**关键词**：`defense`、`continual learning backdoor`、`sample purification`、`robust expert routing`

👤 **作者**：Keyu Lin、Fei Ye、Qihe Liu、Shijie Zhou、Jiguo Yu

- 🎯 **研究动机**：任务流来自不可信来源时，持续学习需同时对抗灾难遗忘、保持适应能力并阻止恶意监督被吸收
- 🔬 **研究方法**：CLUBA 鲁棒动态扩展框架：Bi-Prototype Purification 利用特征空间语义差异识别可疑样本，GDBRO 经伪标签纠正与梯度一致性评估选择性恢复信息样本，RFCBES 构造扰动感知类原型支撑鲁棒专家路由
- 📌 **结论**：在含后门样本的持续学习流中同时实现样本净化、稳健更新与可靠专家选择

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Continual learning (CL) enables models to acquire new knowledge from sequentially arriving tasks while retaining previously learned knowledge. However, in practical scenarios, task streams collected from untrusted sources may contain backdoor-poisoned samples, posing a critical challenge to the stability, plasticity, and security of continual learners. In this work, we investigate a challenging setting termed Continual Learning Under Backdoor Attack (CLUBA), where each incremental task may involve a small proportion of maliciously manipulated training samples. Unlike conventional continual learning or backdoor defense scenarios, CLUBA requires models to simultaneously mitigate catastrophic forgetting, preserve adaptation capability, and prevent the absorption of malicious supervision during sequential updates. To address this challenge, we propose a robust dynamic-expansion framework that integrates sample purification, selective recovery, and robust expert routing into a unified continual learning paradigm. Specifically, we introduce Bi-Prototype Purification (BPP) to identify suspicious samples by exploiting semantic discrepancies in feature space. Based on purified data, Gradient Discrepancy-based Robustness Optimization (GDBRO) selectively recovers informative poisoned samples through pseudo-label correction and gradient consistency evaluation, improving robustness while maintaining model plasticity. Furthermore, Robust Feature Consistency-based Expert Selection (RFCBES) constructs perturbation-aware class prototypes to enable reliable expert routing under corrupted or shifted inputs.

</details>

### 19. TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement

📄 [arXiv](https://arxiv.org/abs/2609.29099)　📅 2026-09

**关键词**：`defense`、`multimodal poison filtering`、`cross-feature rank agreement`、`collective influence`、`stealthy poison`

👤 **作者**：Haoyang Li、…、Haibo Hu

- 🎯 **研究动机**：多模态训练依赖外部图文语料——隐蔽攻击保持合理图文对同时向检测器隐藏差异：中毒集必须保持什么性质才能有效未被刻画
- 🔬 **研究方法**：攻击模式出现频次与集体影响分析→TraceGuard：跨特征秩一致的自适应投毒过滤
- 📌 **结论**：中毒集有效性的保持条件+对应过滤——多模态投毒检测的聚合视角（多模态投毒防御线）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Multimodal training relies on image-text corpora collected from external sources, creating opportunities for attackers to poison the data. Stealthy attacks can preserve plausible image-text pairs while concealing the differences used by detectors, so apparently clean data can still redirect the trained model. We therefore ask which properties a poison set must preserve for the attack to remain effective. A small poison set must still exert enough collective influence during training to induce the attacker's target behavior. We analyze this influence in terms of how often an attack pattern occurs and how strongly the examples carrying it jointly affect the model. This analysis motivates six corpus-level features that examine cross-modal neighborhoods, recurring text, and changes after text-span erasure without training the victim model. We introduce TraceGuard, an adaptive rank-based filtering method that uses agreement among complementary feature rankings to identify suspicious examples. It refines the selected set through shared patterns and adapts the removal threshold to each corpus without knowing the attack or poison rate. Across 19 attack configurations spanning image-text learning, generative vision-language model fine-tuning, and encoder-transfer tests, TraceGuard removes an average of 98.4% of poisoned examples and 5.4% of clean examples. After training on the filtered corpora, the residual attack metric is at most 1% in 13 configurations. Matched-removal controls and ablations support the contributions of sample selection and adaptive removal. Stress tests also identify detection failures under adaptive attacks and unnecessary removal on poison-free corpora.

</details>
