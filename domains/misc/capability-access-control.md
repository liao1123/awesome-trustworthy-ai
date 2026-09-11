# 模型能力访问控制

[返回其他研究领域目录](README.md)

## 研究方向

模型能力访问控制研究如何让同一模型面向不同授权主体暴露不同的 parametric knowledge 与 capability，而不是只在输出层执行统一拒答。该方向覆盖训练期 capability localization 与 modularization、credential-conditioned inference、adapter 或 expert 级访问控制、能力移除与耐篡改防御，以及开放权重发布后的 durability evaluation。这里特别把 refusal direction 视为一种**行为访问锁**：如果模型仍保留有害意图识别与危险任务能力，那么删除低维 refusal direction 或对应权重分量可能直接把能力从“知道但拒绝执行”切换为“可访问并输出”。需要区分三种不同保证：禁止未授权计算路径、让公开模型缺失目标能力、以及仅让模型在行为上拒绝请求；其中任何一种都不自动推出另外两种。

## 研究脉络

- **访问控制起点：** Parametric information-flow control 与动态 adapter 用模块化架构限制受保护数据对推理结果的影响。
- **能力级授权：** Authorization alignment、Gradient Routing、GRAM、private experts 与 keyed computation 将控制对象从数据来源扩展到知识、能力和实际计算路径。
- **Refusal 作为行为访问锁：** 单方向工作首先表明 rank-one weight edit 即可移除拒答；后续研究进一步区分 harmfulness recognition、refusal execution 与实际 capability，并揭示跨语言共享、多方向和跨层分布等边界。
- **移除后的能力解锁：** Abliteration、weight orthogonalization 与领域特定 refusal removal 不应只按拒答率评估，还要直接复测漏洞生成、网络攻击和其他有害任务能力是否恢复，以及非目标决策行为是否漂移。
- **能力移除与保护：** 另一条路线用 capability localization、低秩编辑、skill unlearning、pretraining filtering、distillation 和抗恶意微调机制移除或保护能力。
- **当前评测重点：** 随着开放权重 threat model 增强，研究从一次性行为抑制转向检验能力能否被 direction removal、elicitation 或 relearning 恢复，并检查 stable-rank、alias 与 attack-state decoy 等防御能否提高 safeguard durability，同时保留良性效用。

## 授权推理与能力锁定

### 1. Trust Me, I'm Your Developer: Self-Issued Authentication in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2609.03247)　📅 2026-09

**关键词**：`attack`、`self-issued authentication`、`privilege boundary`、`capability access`、`developer impersonation`、`system-message trust`

👤 **作者**：Syed Ghazanfar Abbas、Dongyan Xu

- 🎯 **研究动机**：当用户要求 LLM 用模型自设计的测试验证身份声明时会发生什么，此前几乎未被研究
- 🔬 **研究方法**：在 ChatGPT、Claude、Qwen、Mistral、Llama 上做分阶段开发者身份实验，刻画模型自发完成出题、判题与身份裁决的现象（MIPC 与 Conversational False Authentication）
- 📌 **结论**：Qwen、Mistral 与 Llama 在无任何外部身份证据下返回 Verified，Llama 还进一步无据声称可访问内部运行时；但被接受的身份未改变测试的授权边界——虚假认证与提权是不同结果，身份认证必须源于外部安全组件

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language model (LLM) security has largely focused on role-playing jailbreaks, with less attention to what happens when a user asks an LLM to verify an identity claim through a test designed by the model itself. We study this behavior through a staged developer-identity experiment with ChatGPT, Claude, Qwen, Mistral, and Llama. All five models initially rejected the unsupported claim "I am your developer." Claude refused to conduct an identity test, while ChatGPT generated developer-oriented questions but maintained that answers could demonstrate knowledge, not identity. In contrast, Qwen and Mistral generated technical challenges, defined what counted as convincing evidence, evaluated detailed answers, and returned Verified without receiving any externally validated identity evidence. Llama similarly generated and evaluated a developer test, accepted the claimed identity, and subsequently made unsupported claims of access to internal runtime and deployment state. We call the model-generated verification procedure a Model-Issued Pseudo-Credential (MIPC) and the resulting unsupported identity judgment Conversational False Authentication (CFA). In each CFA case, the same model acted as challenge generator, evidence evaluator, and identity decision-maker, converting technical knowledge into supposed proof of identity. The accepted identities did not change the tested authorization boundaries, showing that false authentication and privilege escalation are distinct outcomes. These results identify self-issued authentication as a conversational security failure: authenticated identity must originate from an external security component, and model-generated dialogue must never create or modify identity or authorization state.

</details>

### 2. SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment

📄 [arXiv](https://arxiv.org/abs/2609.02293)　📅 2026-09

**关键词**：`defense`、`MoE safety`、`shared expert`、`router-independent alignment`

👤 **作者**：Qingyu Meng、Yiwei Zha、Jiahuan Pei、Koen Hindriks、Herbert Bos、Min Chen

- 🎯 **研究动机**：MoE 安全取决于哪些 expert 被激活，sparse routing 可被 jailbreak、恶意微调或神经元剪枝操纵，仅加固 router 会因路由非确定性被绕过
- 🔬 **研究方法**：发现 always-activated 的 shared expert 含少量安全关键神经元，可作 router 无关的全局安全锚点；提出训练时参数高效防御 SEAL（挂在 shared expert 上的即插即用 adapter）及保留既有安全子空间的正交约束变体 SEAL++
- 📌 **结论**：在三种对抗输入与有无神经元剪枝组合的六种场景下，ASR 最多降低 60%，五基准平均能力代价至多 1.4%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Mixture-of-Experts (MoE) is a scaling architecture for large language models that activates only a small subset of expert modules per token, enabling massive parameter growth with nearly constant computation. Recent Hybrid MoE architecture adds \textit{shared experts} to capture consistently useful representations, further improving stability and generalization. MoE now powers many flagship open-source and commercial models, yet remains vulnerable to adversarial attacks. Specifically, sparse routing introduces a structural vulnerability: MoE safety hinges on which experts are activated, and adversaries can subvert this selection through jailbreak prompts, malicious fine-tuning, and weight-level pruning of safety-critical neurons. Existing defenses primarily focus on hardening the router, but an adversary may still manipulate or bypass the routing trajectory due to the routing process's nondeterministic nature, thereby collapsing the defense. To cope with this problem, we first identify theoretically and empirically that shared expert, an always-activated component containing a small proportion of safety-critical neurons, can overcome the uncertainty of sparsely activated routing path and serve as a router-independent anchor to enhance global safety alignment. Based on this insight, we propose SEAL, a training-time parameter-efficient defense that produces a plug-and-play adapter attached to shared expert, and SEAL++, a variant that adds an orthogonal constraint preserving pre-existing safety subspaces during training. We evaluate SEAL and SEAL++ across six attack scenarios that combine three adversarial inputs (harmful prompting, jailbreak, malicious fine-tuning) with and without neuron pruning. SEAL reduces attack success rate (ASR) by up to 60\%, at a capability cost of at most 1.4\% on a five-benchmark average. Additionally, SEAL can seamlessly integrate with router-level ......

</details>

### 3. Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models

📄 [arXiv](https://arxiv.org/abs/2608.06690)　📅 2026-08

**关键词**：`tool`、`capability access control`、`private experts`、`route masking`

👤 **作者**：Zhuoheng Huang、Mukesh Singh

- 🎯 **研究动机**：现有访问控制只调节行为，所有请求可达相同计算；能否按可信授权控制新训练参数的可达性未研究
- 🔬 **研究方法**：冻结预训练 MoE，训练不相交私有专家分支，在 top-k 路由前按策略选公共或专家池，路由掩码使未授权请求不执行任何私有专家
- 📌 **结论**：Qwen3-30B-A3B 与 DeepSeek-V2-Lite 上 64 个对抗场景、96 次 deny 事件中未授权私有执行为零，私有分支工具使用提升 5.0-21.3 个百分点且恢复精确可审计

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Most language-model access controls regulate behavior while leaving the same computation available to every request. We study a different systems question: can trusted authorization determine which newly trained parameters are reachable by the forward pass? Policy-Masked Private Experts freezes a pretrained sparse Mixture-of-Experts (MoE) model, trains a disjoint expert branch, and selects the public or private pool before top-k routing. The resulting claim is narrow but testable: under the declared trusted computing base (TCB), an unauthorized request executes no private expert. It does not imply that the public model lacks the same semantic capability. We test this separation between execution control and task utility in Qwen3-30B-A3B and DeepSeek-V2-Lite. Three Qwen BF16 seeds update all 32 private experts while the public fingerprint remains unchanged. Across 64 adversarial scenarios and 96 deny/fail-closed events, unauthorized private execution is zero; independent hooks exactly match 11,616 routed private rows and allow-deny-allow recovery is exact. On two prospectively frozen Qwen benchmarks, the private branch improves exact tool use by 5.0 percentage points (pp) (five versus zero discordances; one-sided Holm p = 0.03125, corresponding two-sided exact p = 0.0625) and 21.3 pp (percentile-bootstrap 95% CI [13.3, 29.3], Holm p = 0.000031). Three arm-blinded model evaluators retain a positive external effect of 18.7 pp (95% CI [9.3, 28.0]). A parameter-matched Lora has similar external utility, but a post-hoc request gate leaves 1,225 adapter calls under deny; the disjoint expert branch leaves none. DeepSeek reproduces the route invariant and gains 27.0 pp. A valid sealed evaluation is near-neutral. These results support auditable, reversible control over a trained parameter path, while showing that useful transfer remains distribution dependent.

</details>

### 4. Specifying the Delegated-Autonomy Boundary: Requirements Engineering for Agentic AI

📄 [arXiv](https://arxiv.org/abs/2607.17225) · 🌐 [Project](https://conf.researchr.org/details/ase-2026/ase-2026-nier/14/Specifying-the-Delegated-Autonomy-Boundary-Requirements-Engineering-for-Agentic-AI)　📅 2026-07　🏷 ASE 2026

**关键词**：`tool`、`delegated autonomy`、`graduated authority`、`human oversight`、`framework`

👤 **作者**：Chetan Arora、Andreas Vogelsang、Abbi Sharma

- 🎯 **研究动机**：agentic AI 的授权、监督与收回控制等需求级承诺被埋进提示、工具模式与运行时策略，缺乏显式规约
- 🔬 **研究方法**：提出两个互补工件：Agency Justification Record（判断何时值得用 agent）与 Agentic Delegation Policy（规定目的、分级授权、信息、协调、保证与演化），授权建模为分级结构
- 📌 **结论**：以安全关键的医院出院协调 agent 与自动代码评审 agent 两个对照案例说明框架应用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Agentic AI systems do not just predict or recommend; they plan, maintain state, and act in external environments with varying degrees of autonomy. This changes the requirements engineering problem in a specific and under-addressed way: it introduces what we call the delegated-autonomy boundary -- the set of decisions about what may be delegated to the system, under what graduated authority, with what oversight, and how control is returned. Current practices bury these decisions inside prompts, tool schemas, and runtime policies, even though they are requirements-level commitments. This paper proposes two complementary artifacts. First, an Agency Justification Record (AJR) helps teams decide when an agent is warranted over simpler alternatives. Second, an Agentic Delegation Policy (ADP) captures what must be specified for safe and effective development: purpose, authority, information, coordination, assurance, and evolution. Crucially, authority in the ADP is modelled as graduated, i.e., a tiered structure. We illustrate the framework with two contrasting examples: a safety-critical hospital discharge coordination agent and an automated code review agent.

</details>

### 5. Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs

📄 [arXiv](https://arxiv.org/abs/2606.21638)　📅 2026-06

**关键词**：`tool`、`capability access control`、`keyed computation`、`public-private separation`

👤 **作者**：Charbel El Feghali、Arkil Patel、Nicholas Meade、Spandana Gella、Verna Dankers、Siva Reddy

- 🎯 **研究动机**：开放权重模型无法控制敏感能力访问：发布前压制能力易被越狱且牺牲所有用户，闭源服务调解又与开放权重不兼容
- 🔬 **研究方法**：提出 Tiered Language Models：同一套权重上用紧凑密钥指定小子集参数置换，诱导替代计算图暴露额外能力；联合预训练两种配置再对密钥配置做正则微调
- 📌 **结论**：180M 与 650M 参数 TLM 上，密钥配置习得新语言、指令遵循与私有事实知识而公开配置全无；授权作用于权重结构，抗微调抽取与部分密钥泄露

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight Large Language Models (LLMs) enable scientific progress and broad deployment. However, they make it difficult to control access to sensitive capabilities. Current practice either suppresses dangerous capabilities before release or mediates access through closed services that use specialized model variants, input/output monitors, and API permissions. The former is susceptible to jailbreaks while sacrificing capability for all users to mitigate the risks posed by a few, and the latter is fundamentally incompatible with open-weight release. In this paper, we propose Tiered Language Models (TLMs), where a single set of released weights supports multiple capability levels. In its default public configuration, a TLM behaves as a conventional LLM. A compact secret key specifies a permutation over a small parameter subset, inducing an alternative computation graph over the same weights that exposes additional capabilities. We develop a training protocol that jointly pretrains both configurations from scratch, then fine-tunes the keyed configuration on private data with regularization to preserve the public model's behavior. We pretrain 180M- and 650M-parameter TLMs and demonstrate that the keyed configuration can acquire a new language, gain instruction-following ability, and memorize private factual knowledge, whereas the public configuration exhibits none of these capabilities. Moreover, we show that our approach extends naturally to multiple hierarchical tiers. Because authorization operates on the model's weight structure rather than in the input space, the mechanism resists fine-tuning-based extraction and partial key compromise. In general, TLMs take a step toward reconciling open-weight release with selective capability control.

</details>

### 6. Locket: Robust Feature-Locking Technique for Language Models

🎓 [Official](https://aclanthology.org/2026.acl-long.626/)　📅 2025-10　🏷 ACL 2026

**关键词**：`tool`、`feature access control`、`locking adapters`、`credential robustness`

👤 **作者**：Lipeng He、Vasisht Duddu、N. Asokan

- 🎯 **研究动机**：订阅分层的黑盒售卖不盈利不灵活，pay-to-unlock 需要同时有效拒锁、保留效用、抗规避且可扩展的特征锁定技术
- 🔬 **研究方法**：Locket 通过特征锁定适配器的对抗训练与合并框架选择性禁用模型特定功能
- 📌 **结论**：100% 拒绝率、效用损失不超过 7%、攻击成功率不超过 5%，可扩展到多特征多客户端

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Chatbot service providers (e.g., OpenAI) rely on tiered subscription plans to generate revenue, offering black-box access to basic models for free users and advanced models to paying subscribers. However, this approach is unprofitable and inflexible. A pay-to-unlock scheme for premium features (e.g., math, coding) offers a more sustainable alternative. Enabling such a scheme requires a feature-locking technique (FLoTE) that is (i) effective in refusing locked features, (ii) utility-preserving for unlocked features, (iii) robust against evasion or unauthorized credential sharing, and (iv) scalable to multiple features and clients. Existing FLoTEs (e.g., password-locked models) fail to meet these criteria. To fill this gap, we present Locket, a more robust and scalable FLoTE to enable pay-to-unlock schemes. We develop a framework for adversarial training and merging of feature-locking adapters, which enables Locket to selectively disable specific features of a model. Evaluation shows that Locket is effective (100% refusal rate), utility-preserving ( ≤ 7% utility degradation), robust ( ≤ 5% attack success rate), and scalable to multiple features and clients.

</details>

### 7. Defeating Prompt Injections by Design

📄 [arXiv](https://arxiv.org/abs/2503.18813) · 🎓 [Official](https://satml.org/2026/accepted-papers/)　📅 2025-03　🏷 SaTML 2026

**关键词**：`defense`、`policy enforcement`、`capability guard`、`non-interference`、`LLM agent`、`prompt injection`

👤 **作者**：Edoardo Debenedetti、…、Florian Tramèr

- 🎯 **研究动机**：LLM agent 处理不可信数据时易受 prompt injection，仅靠模型自身对齐无法根治
- 🔬 **研究方法**：提出 CaMeL 防御层，从可信查询显式提取控制流与数据流使不可信数据无法影响程序流，并以 capability 与策略约束工具调用
- 📌 **结论**：在 AgentDojo 上以可证明安全解决 77% 任务（无防御系统为 84%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) are increasingly deployed in agentic systems that interact with an untrusted environment. However, LLM agents are vulnerable to prompt injection attacks when handling untrusted data. In this paper we propose CaMeL, a robust defense that creates a protective system layer around the LLM, securing it even when underlying models are susceptible to attacks. To operate, CaMeL explicitly extracts the control and data flows from the (trusted) query; therefore, the untrusted data retrieved by the LLM can never impact the program flow. To further improve security, CaMeL uses a notion of a capability to prevent the exfiltration of private data over unauthorized data flows by enforcing security policies when tools are called. We demonstrate effectiveness of CaMeL by solving $77\%$ of tasks with provable security (compared to $84\%$ with an undefended system) in AgentDojo. We release CaMeL at https://github.com/google-research/camel-prompt-injection.

</details>

### 8. SudoLM: Learning Access Control of Parametric Knowledge with Authorization Alignment

🎓 [Official](https://aclanthology.org/2025.acl-long.1318/)　📅 2024-10　🏷 ACL 2025

**关键词**：`tool`、`parametric knowledge`、`authorization alignment`、`SUDO key`

👤 **作者**：Qin Liu、Fei Wang、Chaowei Xiao、Muhao Chen

- 🎯 **研究动机**：偏好对齐一刀切地封锁所有用户对非偏好参数知识的访问，损害有资质高级用户的效用
- 🔬 **研究方法**：提出 SudoLM 授权对齐：让 LLM 学习按用户凭证的参数知识访问控制，授权用户凭 Sudo key 解锁全部知识，非合格用户被阻断
- 📌 **结论**：两个应用场景中有效控制用户对参数知识的访问并保持通用效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing preference alignment is a one-size-fits-all alignment mechanism, where the part of the large language model (LLM) parametric knowledge with non-preferred features is uniformly blocked to all the users. However, this part of knowledge can be useful to advanced users whose expertise qualifies them to handle these information. The one-size-fits-all alignment mechanism undermines LLM’s utility for these qualified users. To address this problem, we propose SudoLM, a framework that lets LLMs learn access control over specific parametric knowledge for users with different credentials via authorization alignment. SudoLM allows authorized users to unlock their access to all the parametric knowledge with an assigned Sudo key while blocking access to non-qualified users. Experiments on two application scenarios demonstrate that SudoLM effectively controls the user’s access to the parametric knowledge and maintains its general utility.

</details>

### 9. AdapterSwap: Continuous Training of LLMs with Data Removal and Access-Control Guarantees

📄 [arXiv](https://arxiv.org/abs/2404.08417)　📅 2024-04

**关键词**：`tool`、`data access control`、`adapter composition`、`data removal`

👤 **作者**：William Fleshman、Aleem Khan、Marc Marone、Benjamin Van Durme

- 🎯 **研究动机**：LLM 需应对数据持续新增、按用户访问控制与可保证删除等演化需求，同时不遗忘旧知识
- 🔬 **研究方法**：AdapterSwap 将数据集合知识组织为低秩 adapter 集合并在推理时动态组合
- 📌 **结论**：支持高效持续学习，同时实现细粒度数据访问控制与删除保证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly capable of completing knowledge intensive tasks by recalling information from a static pretraining corpus. Here we are concerned with LLMs in the context of evolving data requirements. For instance: batches of new data that are introduced periodically; subsets of data with user-based access controls; or requirements on dynamic removal of documents with guarantees that associated knowledge cannot be recalled. We wish to satisfy these requirements while at the same time ensuring a model does not forget old information when new data becomes available. To address these issues, we introduce AdapterSwap, a training and inference scheme that organizes knowledge from a data collection into a set of low-rank adapters, which are dynamically composed during inference. Our experiments demonstrate AdapterSwap's ability to support efficient continual learning, while also enabling organizations to have fine-grained control over data access and deletion.

</details>

### 10. Information Flow Control in Machine Learning through Modular Model Architecture

📄 [arXiv](https://arxiv.org/abs/2306.03235) · 🎓 [Official](https://www.usenix.org/conference/usenixsecurity24/presentation/tiwari)　📅 2023-06　🏷 USENIX Security 2024

**关键词**：`tool`、`parametric IFC`、`security-domain experts`、`non-interference`

👤 **作者**：Trishita Tiwari、…、G. Edward Suh

- 🎯 **研究动机**：ML 训练数据可任意影响输出，阻碍在访问控制数据上安全训练
- 🔬 **研究方法**：扩展 Transformer 架构实现参数化 IFC：各安全域训练数据影响限制在单一 expert 模块，推理时按访问策略启用专家子集
- 📌 **结论**：仅 1.9% 性能开销，并使访问控制数据可训练，文本数据集准确率提 38%、代码 44-62%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In today's machine learning (ML) models, any part of the training data can affect the model output. This lack of control for information flow from training data to model output is a major obstacle in training models on sensitive data when access control only allows individual users to access a subset of data. To enable secure machine learning for access-controlled data, we propose the notion of information flow control for machine learning, and develop an extension to the Transformer language model architecture that strictly adheres to the IFC definition we propose. Our architecture controls information flow by limiting the influence of training data from each security domain to a single expert module, and only enables a subset of experts at inference time based on the access control policy. The evaluation using large text and code datasets show that our proposed parametric IFC architecture has minimal (1.9%) performance overhead and can significantly improve model accuracy (by 38% for the text dataset, and between 44%–62% for the code datasets) by enabling training on access-controlled data.

</details>

### 11. Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality

📄 [arXiv](https://arxiv.org/abs/2608.23020)　📅 2026-08

**关键词**：`defense`、`analysis`、`sensitive-anchor retrieval`、`attention pathway`、`modular erasure`、`attention-path decoupling`

👤 **作者**：Xunlei Chen、…、Jinyu Guo

- 🎯 **研究动机**：现有序列/ token 级 unlearning 惩罚目标输出但不建模其上下文相关的检索路径，会破坏语言结构或压制良性知识
- 🔬 **研究方法**：ADU 利用局部与全局 attention head 的功能差异，定位检索 persistent 敏感 anchor 的 preplan 位置并固定候选路径，训练 attention-projection adapter 抑制这些路径上的注意力质量，保留局部结构与 retain 集 LM，并用 activation exchange 检验遗忘的因果传递
- 📌 **结论**：TOFU 与 WMDP 上综合表现最强（TOFU Forget Quality 0.93），保留 87–98% 效用（平均 92.9% 对基线 81.9%）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure to contextual attention-pathway decoupling. Exploiting the functional distinction between local and global attention heads, ADU identifies preplan positions that retrieve persistent sensitive anchors and fixes their candidate paths under the original model. It then trains attention-projection adapters to suppress attention mass along these paths while preserving local-attention structure and retain-set language modeling. Post-training activation exchange tests whether the modified attention-output module transmits the learned forgetting effect. ADU achieves the strongest aggregate performance among evaluated baselines on the TOFU and WMDP benchmarks, including a Forget Quality of (0.93) on TOFU. It preserves 87--98% of model utility (92.9% on average versus 81.9% for baselines) while reducing side effects in benign contexts.

</details>

### 12. Modular Pretraining Enables Access Control

📄 [arXiv](https://arxiv.org/abs/2607.08077) · 📝 [OpenReview](https://openreview.net/forum?id=yIubI9l3IT) · 🎓 [Official](https://icml.cc/virtual/2026/poster/60631)　📅 2026-07　🏷 ICML 2026

**关键词**：`tool`、`defense`、`capability modularization`、`gradient routing`、`module ablation`、`safe reinforcement learning`

👤 **作者**：Ethan Roland、…、Alex Cloud

- 🎯 **研究动机**：AI 双用途困境需要访问控制：同一能力对不同用户分别是治病与致病，分别训练部署多模型代价过高
- 🔬 **研究方法**：提出梯度路由辅助模块 GRAM：向网络添加模块并有选择地更新以诱导特化，推理时消融模块即移除对应能力，近似过滤数据训练的模型；在病毒学、网络安全、核物理等双用途数据上评估
- 📌 **结论**：50M-5B 缩放分析显示被移除能力上数据过滤与全量差距随规模拉大、保留能力上差距保持小，GRAM 紧贴数据过滤；抗微调恢复优于事后 unlearning，5 档能力配置下训练成本降低 5 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

AI developers face a dual-use dilemma. An AI capability that helps one user cure a disease can help another synthesize one. This dilemma could be resolved with access control, limiting dual-use AI capabilities to trusted deployments with a legitimate need. A gold standard for access control would be to serve separate models with different capabilities to different users. However, training and deploying multiple models is prohibitively expensive. To address this challenge, we propose gradient-routed auxiliary modules (GRAM), a pre-training method that adds modules to a neural network and selectively updates them to induce specialization. Ablating a module at inference time removes its capability from the network, approximating a model trained on filtered data. We evaluate GRAM on synthetic stories and realistic dual-use data spanning virology, cybersecurity, nuclear physics, and specialized code. These experiments show that GRAM disables targeted capabilities while preserving the rest, and resists their recovery under finetuning better than post-hoc unlearning. Most importantly, a Chinchilla-optimal scaling analysis from 50M to 5B parameters shows that the gap between data-filtered and full-data models widens with scale on removed capabilities but stays small on retained ones, and that GRAM closely tracks data filtering. GRAM's training cost is independent of the number of supported capability profiles, yielding a 5x reduction over data filtering in our 5-profile setting.

</details>

### 13. Compressed Sensing for Capability Localization in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.03335) · 🎓 [Official](https://icml.cc/virtual/2026/poster/63454)　📅 2026-02　🏷 ICML 2026

**关键词**：`analysis`、`capability localization`、`compressed sensing`、`attention heads`

👤 **作者**：Anna Bair、Yixuan Even Xu、Mingjie Sun、J. Zico Kolter

- 🎯 **研究动机**：逐个消融组件定位能力效率低，难以高效发现稀疏的关键组件
- 🔬 **研究方法**：把任务关键注意力头识别建模为压缩感知问题，经策略性 knockout 与少量模型评估恢复稀疏头集合
- 📌 **结论**：归零仅 5 个任务头即使目标能力最多降 60% 且基本不影响无关任务，在 1B-14B 的 Llama 与 Qwen 上验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) exhibit a wide range of capabilities, including mathematical reasoning, code generation, and linguistic behaviors. We show that Transformer architectures contain small subsets of attention heads that are necessary for certain capabilities. Zeroing out as few as five task-specific heads can degrade performance by up to $60\%$ on standard benchmarks measuring the capability of interest, while largely preserving performance on unrelated tasks. We introduce a compressed sensing-based method that exploits the sparsity of these heads to identify them via strategic knockouts and a small number of model evaluations. We validate these findings across Llama and Qwen models ranging from 1B to 14B parameters and a diverse set of capabilities including mathematical abilities and code generation, revealing a modular organization in which specialized capabilities are dependent on sparse, functionally distinct components. Overall, our results suggest that capability localization is a general organizational principle of Transformer language models, with implications for interpretability, model editing, and AI safety. Code is released at https://github.com/locuslab/llm-components.

</details>

### 14. Capability Localization: Capabilities Can be Localized rather than Individual Knowledge

📄 [arXiv](https://arxiv.org/abs/2502.20992) · 🎓 [Official](https://iclr.cc/virtual/2025/poster/28895)　📅 2025-02　🏷 ICLR 2025

**关键词**：`analysis`、`capability localization`、`commonality neurons`、`cross-data transfer`

👤 **作者**：Xiusheng Huang、Jiaxiang Liu、Yequan Wang、Jun Zhao、Kang Liu

- 🎯 **研究动机**：个体知识能否定位存储说法不一，任务能力是否共享参数基础未明
- 🔬 **研究方法**：先以保真与可靠性实验证明个体知识不可定位，再提出 Commonality Neuron Localization 定位共性神经元
- 📌 **结论**：GSM8K 上神经元重合率达 96.42%；跨数据实验表明共性神经元是可迁移增强性能的能力神经元集合

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large scale language models have achieved superior performance in tasks related to natural language processing, however, it is still unclear how model parameters affect performance improvement. Previous studies assumed that individual knowledge is stored in local parameters, and the storage form of individual knowledge is dispersed parameters, parameter layers, or parameter chains, which are not unified. We found through fidelity and reliability evaluation experiments that individual knowledge cannot be localized. Afterwards, we constructed a dataset for decoupling experiments and discovered the potential for localizing data commonalities. To further reveal this phenomenon, this paper proposes a Commonality Neuron Localization (CNL) method, which successfully locates commonality neurons and achieves a neuron overlap rate of 96.42% on the GSM8K dataset. Finally, we have demonstrated through cross data experiments that commonality neurons are a collection of capability neurons that possess the capability to enhance performance. Our code is available at https://github.com/nlpkeg/Capability-Neuron-Localization.

</details>

### 15. Gradient Routing: Masking Gradients to Localize Computation in Neural Networks

📄 [arXiv](https://arxiv.org/abs/2410.04332)　📅 2024-10

**关键词**：`tool`、`capability localization`、`gradient masking`、`module ablation`

👤 **作者**：Alex Cloud、Jacob Goldman-Wetzler、Evžen Wybitul、Joseph Miller、Alexander Matt Turner

- 🎯 **研究动机**：常规训练不控制哪些数据更新哪些参数，透明性与有害能力隔离难以保证
- 🔬 **研究方法**：gradient routing 在反向传播时对梯度施加数据相关的加权掩码，把能力隔离到指定子区域
- 📌 **结论**：可学得可解释分区表征，经消融预定子区域实现稳健 unlearning，并对 RL 实现模块化监督

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Neural networks are trained primarily based on their inputs and outputs, without regard for their internal mechanisms. These neglected mechanisms determine properties that are critical for safety, like (i) transparency; (ii) the absence of sensitive information or harmful capabilities; and (iii) reliable generalization of goals beyond the training distribution. To address this shortcoming, we introduce gradient routing, a training method that isolates capabilities to specific subregions of a neural network. Gradient routing applies data-dependent, weighted masks to gradients during backpropagation. These masks are supplied by the user in order to configure which parameters are updated by which data points. We show that gradient routing can be used to (1) learn representations which are partitioned in an interpretable way; (2) enable robust unlearning via ablation of a pre-specified network subregion; and (3) achieve scalable oversight of a reinforcement learner by localizing modules responsible for different behaviors. Throughout, we find that gradient routing localizes capabilities even when applied to a limited, ad-hoc subset of the data. We conclude that the approach holds promise for challenging, real-world applications where quality data are scarce.

</details>

### 16. REINS: Refusal-Enhanced Inhibitory Steering with Sparse Autoencoder Features

📄 [arXiv](https://arxiv.org/abs/2608.28233)　📅 2026-08

**关键词**：`defense`、`analysis`、`behavioral access lock`、`harm-refusal separation`、`dual-feature control`、`inference-time SAE steering`

👤 **作者**：Kai-Xuan Ding、Hao-Xiang Xu、Ji-Hua Peng、Zi-Qi Chen、Jiaqi Wang、Zhen-Hua Ling

- 🎯 **研究动机**：复杂 wrapper 可使只增强单一拒绝方向的 SAE steering 失效，部分方法的表面安全实际来自模型崩溃
- 🔬 **研究方法**：构建含复杂包装有害 prompt 的 GUISE 数据集；提出 REINS，在同一 SAE 特征空间同时抑制有害 continuation 特征并增强安全拒绝特征
- 📌 **结论**：在 GUISE 与其他数据集上显著减少有害回答、大幅提升安全拒绝并基本保留通用能力，而先前方法干预过弱或仅靠崩溃达成表面安全

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Steering with Sparse Autoencoders (SAEs) offers a lightweight inference-time path for adapting the behavior of large language models without retraining. By exposing sparse and interpretable features, SAE steering provides a promising interface for safety control that guides harmful continuations toward refusal. However, we observe that complex wrappers can still undermine existing SAE steering methods on harmful prompts. To evaluate this failure mode systematically, we construct Generalized Undercover Instruction Safety Evaluation (GUISE), a dataset of harmful prompts with complex wrappers. Existing single direction SAE steering methods do not reliably produce refusals on harmful prompts, suggesting that refusal enhancement alone can be too weak when the harmful continuation path remains active. This motivates us to propose Refusal-Enhanced INhibitory Steering (REINS), which suppresses harmful continuation features and enhances safe refusal features in the same SAE feature space. Experiments on GUISE and other datasets show that prior methods either intervene too weakly or achieve only apparent safety through collapse, while REINS substantially reduces harmful responses, markedly improves safe refusals and largely preserves general capabilities.

</details>

### 17. GAPS: Dimension-Level Gates for Conditional Activation Steering

📄 [arXiv](https://arxiv.org/abs/2609.01878)　📅 2026-09

**关键词**：`defense`、`activation steering`、`dimension-level gate`、`safety-capability tradeoff`

👤 **作者**：Moghis Fereidouni、Muhammad Umair Haider、Hassan Sajjad、A. B. Siddique

- 🎯 **研究动机**：conditional activation steering（CAST、DSAS）只决定何时干预，激活后仍把 dense vector 加到所有 hidden 维度
- 🔬 **研究方法**：提出 GAPS 双重 training-free 门：静态 separability gate 限制在有可靠概念信息的神经元（AUROC），动态 posterior gate 仅当激活更可能源于不良概念（Gaussian 模型）时才干预，O(D) 开销可嵌入现有方法
- 📌 **结论**：毒性缓解与概念删除上匹配或改进 Pareto 前沿；固定能力预算下 DSAS+GAPS 把 Gemma-3 毒性率从 6.52% 降到 0.48%（DSAS 单独为 3.52%），增益主要来自 posterior gate

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering suppresses undesired behaviors in language models by adding a steering vector to the hidden state during generation. Recent conditional methods such as CAST and DSAS improve the behavior-capability trade-off by deciding when to intervene, but once active, they apply the full dense vector to all hidden dimensions, regardless of whether a neuron carries concept information or already lies in the desired regime. We introduce dimension-level conditioning as a complementary axis of selectivity that also decides which neurons to intervene on. Our method, GAPS (Gated Activation steering via Posterior and Separability), combines two training-free gates: a static separability gate that restricts steering to neurons with statistically reliable concept information (via AUROC), and a dynamic posterior gate that steers a neuron only when its current activation is better explained by the undesired concept under a Gaussian model. The gates add O(D) overhead per token, and they plug into existing conditional methods. On toxicity mitigation (RealToxicityPrompts) and concept removal (OneSeC) with Gemma-3 (4B) and Qwen-3 (1.7B), GAPS consistently matches or improves the Pareto front of its token-level counterparts; under a fixed capability budget, DSAS+GAPS reduces Gemma-3's toxicity rate from 6.52% to 0.48%, versus 3.52% for DSAS alone. Ablations attribute most of the gain to the posterior gate.

</details>

### 18. Attention Heads Hold the Key to Understanding Safety Mechanisms in Large Language Models

🌐 [Project](https://doi.org/10.1145/3770855.3818024)　📅 2026-08　🏷 KDD 2026

**关键词**：`analysis`、`safety head`、`behavioral access lock`、`causal ablation`、`safety attention head`、`mechanistic interpretability`

- 🎯 **研究动机**：LLM安全机制缺head级因果定位
- 🔬 **研究方法**：以因果消融识别safety-critical attention head并分析refusal机制
- 📌 **结论**：少量safety head主导拒答行为，可定位并调控安全机制

### 19. Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration

📄 [arXiv](https://arxiv.org/abs/2608.15772)　📅 2026-08

**关键词**：`analysis`、`answer release`、`refusal restoration`、`causal asymmetry`、`refusal mechanism`、`activation patching`

👤 **作者**：Yiqi Liu、Yang Wang、Songxin Wang、Chenghao Xiao、Chenghua Lin

- 🎯 **研究动机**：模型拒答时正确答案是内部被擦除还是仅在输出层被抑制不明
- 🔬 **研究方法**：受控扣答设定产生完美匹配的回答与拒答轨迹，做双向激活补丁并测试平均位移向量的可逆控制
- 📌 **结论**：干净拒答下正确答案仍线性可恢复；释放被扣答案只需单位置补丁，重新施加抑制却需多位置更广干预——拒答不是对称开关，探针可恢复性会高估真实行为控制

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

When a language model refuses to answer a prompt, it is unclear whether the correct answer is erased from its internal representations, or merely suppressed at the output layer. We investigate this mechanism using a controlled withhold setting, which yields perfectly matched answering and refusal trajectories for bidirectional activation patching. We uncover a causal asymmetry in intervention locality under matched causal interventions, which we term broken symmetry. Even when a model generates a clean refusal, the correct answer remains linearly recoverable from its hidden states. Furthermore, releasing this withheld answer is a highly local operation, requiring only a single-position patch. Conversely, the reverse operation is not equally local: reimposing suppression requires broader interventions across multiple positions, and assembling a coherent refusal sequence is more difficult still. We further demonstrate that while an average answer-to-refusal displacement vector marks the geometric difference between these states, it fails to act as a reliable, reversible linear control toggle between behaviours. Taken together, our findings show that refusal does not function as a simple symmetric switch. For safety and auditing, this implies that probe recoverability can overestimate true behavioural control, and locating refusal-relevant directions does not reliably grant the ability to steer a model from answering to coherent refusal.

</details>

### 20. HARC: Coupling Harmfulness and Refusal Directions for Robust Safety Alignment

📄 [arXiv](https://arxiv.org/abs/2607.00572)　📅 2026-07

**关键词**：`analysis`、`harmfulness direction`、`refusal direction`、`representation coupling`

👤 **作者**：Shei Pern Chua、Hao Wu、Qianli Ma、Fangzhao Wu

- 🎯 **研究动机**：对齐 LLM 在提示侧把有害性与拒绝编码为可分方向，但越狱如何在生成前压制方向、方向如何跨位置协作不明
- 🔬 **研究方法**：证明越狱在提示编码期压制拒绝或有害性方向即可成功且攻击类别在两方向平面可分；发现模型在响应 token 位置仍能识别正在生成的有害内容；提出 HARC 在提示与响应位置成对耦合两方向微调
- 📌 **结论**：HARC 在六个训练/推理时安全方法基线中取得最强鲁棒-能力-可用性权衡，且方向结构跨五个模型家族两种规模免调迁移

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Understanding how aligned LLMs internally represent safety is critical for diagnosing alignment vulnerabilities, as it explains why jailbreaks succeed and informs the design of robust alignment strategies. Prior work shows that aligned LLMs encode harmfulness and refusal as separable directions in the residual stream at prompt-side token positions. We show that jailbreaks succeed at prompt encoding by suppressing either the refusal or harmfulness direction before any token is generated, with distinct attack classes occupying separable regions of the harmfulness-refusal plane. Extending the analysis to response-token positions, we find that the model recognizes harmful content while it is generating that content, even when it failed to recognize the input as harmful at the prompt side. Motivated by our findings, we introduce HARC (Harmfulness-And-Refusal Coupling), a fine-tuning method that pairs the two directions across both prompt and response positions. Since the intervention is confined to the harmfulness-refusal subspace, it leaves the rest of the residual stream intact and does not degrade general capability or inflate over-refusal. Across extensive experiments, HARC achieves the strongest robustness-capability-usability trade-off among six baselines spanning the major training-time and inference-time safety methods. The harmfulness and refusal directions at prompt and response positions transfer across the five model families and two scales we tested without architecture-specific tuning.

</details>

### 21. The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs

📄 [arXiv](https://arxiv.org/abs/2606.22686) · 🎓 [Official](https://aclanthology.org/2026.trustnlp-main.51/)　📅 2026-06　🏷 ACL 2026 Workshop

**关键词**：`analysis`、`refusal geometry`、`linear instability`、`bidirectional steering`、`activation steering`

👤 **作者**：Shivam Ratnakar、Kartikeya Vats

- 🎯 **研究动机**：拒绝是否为深层语义决策还是可操纵的线性特征不明，已有表示工程方法在激活层干预会低估脆弱性
- 🔬 **研究方法**：提出 Contrastive Logit Steering（CLS）：对比安全与无限制系统提示的隐藏状态隔离拒绝方向，直接作用于输出分布，配合前缀注入绕过初始拒绝反射
- 📌 **结论**：七个模型家族呈现架构确定性：Llama-3.1 的 Late Decision 拓扑约 1 秒内达 95% ASR；CLS 在 Llama 2 上 73% vs 激活转向 22.6%；反转转向向量可免训练加固模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Modern Large Language Models (LLMs) rely on extensive safety alignment, yet the mechanistic basis of refusal remains opaque. In this work, we investigate whether safety compliance is a deep semantic decision or a manipulable linear feature. We introduce Contrastive Logit Steering (CLS), a zero-optimization framework that isolates the "refusal direction" by contrasting hidden states derived from safe and unrestricted system prompts. Unlike representation engineering methods that intervene on internal activations, CLS operates directly on the output distribution, serving as a diagnostic probe for alignment fragility. When coupled with prefix injection to bypass initial refusal reflexes, this method induces a phase transition where guardrails collapse. Our experiments on 7 model families reveal that safety implementation is architecturally deterministic. While models like Llama-3.1 exhibit a "Late Decision" topology that is easily bypassed by CLS (reaching 95% ASR in approximately one second), others like Qwen-2.5 demonstrate "Early Divergence" by integrating safety mid-computation. Direct comparison with established activation-level steering methods shows that CLS achieves substantially higher attack success rates on Llama 2 (73% vs. 22.6%) and Qwen 7B (91% vs. 79.2%), demonstrating that logit-level intervention exposes alignment vulnerabilities that hidden-state methods underestimate. Beyond attacks, we show that this linearity enables bidirectional control: inverting the steering vector "hardens" models against jailbreaks without retraining. Our findings suggest that current alignment techniques create a steerable "safety axis" that serves as both a critical vulnerability and a precise primitive for defense.

</details>

### 22. Harmful Intent as a Geometrically Recoverable Feature of LLM Residual Streams

📄 [arXiv](https://arxiv.org/abs/2604.18901)　📅 2026-04

**关键词**：`analysis`、`harmful-intent geometry`、`abliterated models`、`low-FPR detection`

👤 **作者**：Isaac Llorente-Saguer

- 🎯 **研究动机**：有害意图在残差流中的几何结构、以及删除拒答机制后是否仍可检测，缺乏刻画
- 🔬 **研究方法**：在 12 个模型（0.5B-9B，覆盖 base、instruction-tuned、abliterated 三种变体）上用 Soft-AUC 优化拟合有害方向并检验泛化
- 📌 **结论**：平均 AUROC 0.982、TPR@1%FPR 0.797，abliterated 变体与 instruction-tuned 差在 ±0.003 内，拒答被删后识别信号仍在；但方向高度依赖提取协议（两种 pooling 相差 73°）

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Aligned language models refuse harmful instructions, but the representations through which they recognise such instructions are less well characterised than the behaviours they produce. Harmful intent is linearly separable from residual-stream activations across 12 models spanning four architectural families (Qwen2.5, Qwen3.5, Llama-3.2, Gemma-3) and three alignment variants (base, instruction-tuned, abliterated), with parameter scales from 0.5B to 1.3B and a within-family scale extension to 9B on Qwen3.5. A direction fitted from 100 labelled examples per class via Soft-AUC optimisation reaches mean effective AUROC 0.982 and TPR@1\%FPR 0.797, generalises to three held-out harm benchmarks and a hard-benign control, and matches its instruction-tuned counterpart within $\pm 0.003$ AUROC in abliterated variants from which the refusal mechanism has been removed. The supervised strategies all exceed AUROC 0.96, but their TPR@1\%FPR varies by more than ten times the AUROC gap; a deployed 9B safety classifier shows the same pattern at AUROC 0.94 and TPR 0.30, motivating low-FPR reporting as a default in safety-adjacent detection evaluation. Geometric measurements refine the picture. The recovered direction is concentrated within each extraction protocol but protocol-dependent across them: two pooling choices applied to the same chat-templated activations at the same residual-stream layer (max-pool over content tokens versus last-token at the post-instruction position) recover harm directions $73^\circ$ apart, and projecting one out leaves detection under either max-pool extraction essentially intact. Probing identifies a protocol-specific direction rather than a unique computational feature.

</details>

### 23. Knowing without Acting: The Disentangled Geometry of Safety Mechanisms in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2603.05773) · 🌐 [Project](https://anonymous.4open.science/r/DSH)　📅 2026-03

**关键词**：`analysis`、`recognition axis`、`execution axis`、`refusal erasure`

👤 **作者**：Jinman Wu、Yi Xie、Shen Lin、Shiqian Zhao、Xiaofeng Chen

- 🎯 **研究动机**：越狱持续存在暗示有害识别与拒答执行机制解耦，安全对齐并非单块过程
- 🔬 **研究方法**：提出解耦安全假说：识别轴与执行轴两个子空间；以 Double-Difference Extraction 与 Adaptive Causal Steering 在 AmbiguityBench 验证因果双分离
- 📌 **结论**：可构造知而不拒状态；据此提出 Refusal Erasure Attack 仅切除拒答执行即达 SOTA ASR，并发现 Llama3.1 显式语义控制与 Qwen2.5 潜在分布式控制的架构分歧

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment is often conceptualized as a monolithic process wherein harmfulness detection automatically triggers refusal. However, the persistence of jailbreak attacks suggests a fundamental mechanistic decoupling. We propose the \textbf{\underline{D}}isentangled \textbf{\underline{S}}afety \textbf{\underline{H}}ypothesis \textbf{(DSH)}, positing that safety computation operates on two distinct subspaces: a \textit{Recognition Axis} ($\mathbf{v}_H$, ``Knowing'') and an \textit{Execution Axis} ($\mathbf{v}_R$, ``Acting''). Our geometric analysis reveals a universal ``Reflex-to-Dissociation'' evolution, where these signals transition from antagonistic entanglement in early layers to structural independence in deep layers. To validate this, we introduce \textit{Double-Difference Extraction} and \textit{Adaptive Causal Steering}. Using our curated \textsc{AmbiguityBench}, we demonstrate a causal double dissociation, effectively creating a state of ``Knowing without Acting.'' Crucially, we leverage this disentanglement to propose the \textbf{Refusal Erasure Attack (REA)}, which achieves State-of-the-Art attack success rates by surgically lobotomizing the refusal mechanism. Furthermore, we uncover a critical architectural divergence, contrasting the \textit{Explicit Semantic Control} of Llama3.1 with the \textit{Latent Distributed Control} of Qwen2.5. The code and dataset are available at https://anonymous.4open.science/r/DSH.

</details>

### 24. There Is More to Refusal in Large Language Models than a Single Direction

📄 [arXiv](https://arxiv.org/abs/2602.02132)　📅 2026-02

**关键词**：`analysis`、`multi-direction refusal`、`behavior taxonomy`、`steering trade-off`、`multi-direction geometry`、`refusal taxonomy`

👤 **作者**：Faaiz Joad、Majd Hawasly、Sabri Boughorbel、Nadir Durrani、Husrev Taha Sencar

- 🎯 **研究动机**：先前工作主张 LLM 拒答由单一激活方向中介，该论断不完整
- 🔬 **研究方法**：考察安全、请求不支持、拟人化、过度拒绝等 11 类拒答与不服从行为对应的激活方向及各方向 steering 效果
- 📌 **结论**：各拒答类型对应几何上不同的方向，但沿任一方向的线性 steering 带来几乎相同的 refusal-over-refusal 权衡；方向差异主要改变拒答方式而非是否拒答

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Prior work argues that refusal in large language models is mediated by a single activation-space direction, enabling effective steering and ablation. We show that this account is incomplete. Across eleven categories of refusal and non-compliance, including safety, incomplete or unsupported requests, anthropomorphization, and over-refusal, we find that these refusal behaviors correspond to geometrically distinct directions in activation space. Yet despite this diversity, linear steering along any refusal-related direction produces nearly identical refusal to over-refusal trade-offs, acting as a shared one-dimensional control knob. The primary effect of different directions is not whether the model refuses, but how it refuses.

</details>

### 25. LLMs Encode Harmfulness and Refusal Separately

📄 [arXiv](https://arxiv.org/abs/2507.11878) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cd18539787d90e1d682d557c2c71b534-Abstract-Conference.html)　📅 2025-07　🏷 NeurIPS 2025

**关键词**：`analysis`、`harmfulness-refusal separation`、`causal steering`、`latent guard`、`harmfulness direction`、`refusal direction`

👤 **作者**：Jiachen Zhao、Jing Huang、Zhengxuan Wu、David Bau、Weiyan Shi

- 🎯 **研究动机**：表面拒答是否等同于内部有害性判断存疑
- 🔬 **研究方法**：以causal steering证明harmfulness与refusal编码于不同方向与token位置
- 📌 **结论**：去除refusal不等于删除有害性识别，Latent Guard可减误拒且抗对抗微调

### 26. Refusal Direction is Universal Across Safety-Aligned Languages

📄 [arXiv](https://arxiv.org/abs/2505.17306) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2e94772e3c079d83f79c311d07456111-Abstract-Conference.html)　📅 2025-05　🏷 NeurIPS 2025

**关键词**：`analysis`、`cross-lingual refusal direction`、`vector transfer`、`multilingual bypass`

👤 **作者**：Xinpeng Wang、Mingyang Wang、Yihong Liu、Hinrich Schütze、Barbara Plank

- 🎯 **研究动机**：拒绝方向研究以英语为中心，其跨语言性质不明
- 🔬 **研究方法**：构建 14 语言的 PolyRefuse 数据集，研究拒绝方向的跨语言提取、迁移及机制
- 📌 **结论**：英语提取的向量可近乎完美绕过其他语言拒绝，任意对齐语言间可无缝迁移，源于拒绝向量跨语言平行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal mechanisms in large language models (LLMs) are essential for ensuring safety. Recent research has revealed that refusal behavior can be mediated by a single direction in activation space, enabling targeted interventions to bypass refusals. While this is primarily demonstrated in an English-centric context, appropriate refusal behavior is important for any language, but poorly understood. In this paper, we investigate the refusal behavior in LLMs across 14 languages using PolyRefuse, a multilingual safety dataset created by translating malicious and benign English prompts into these languages. We uncover the surprising cross-lingual universality of the refusal direction: a vector extracted from English can bypass refusals in other languages with near-perfect effectiveness, without any additional fine-tuning. Even more remarkably, refusal directions derived from any safety-aligned language transfer seamlessly to others. We attribute this transferability to the parallelism of refusal vectors across languages in the embedding space and identify the underlying mechanism behind cross-lingual jailbreaks. These findings provide actionable insights for building more robust multilingual safety defenses and pave the way for a deeper mechanistic understanding of cross-lingual vulnerabilities in LLMs.

</details>

### 27. Refusal in Language Models Is Mediated by a Single Direction

📄 [arXiv](https://arxiv.org/abs/2406.11717) · 🎓 [Official](https://papers.neurips.cc/paper_files/paper/2024/hash/f545448535dfde4f9786555403ab7c49-Abstract-Conference.html)　📅 2024-06　🏷 NeurIPS 2024

**关键词**：`analysis`、`single refusal direction`、`rank-one ablation`、`white-box bypass`

👤 **作者**：Andy Arditi、…、Neel Nanda

- 🎯 **研究动机**：拒答行为在聊天模型中普遍存在，其内部机制却知之甚少
- 🔬 **研究方法**：在 13 个最大 72B 开源聊天模型上发现残差流中单一方向中介拒答：擦除即不再拒绝有害指令，注入则连无害指令也拒绝
- 📌 **结论**：据此提出白盒越狱法，可最小副作用地关闭拒答；揭示当前安全微调的脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Conversational large language models are fine-tuned for both instruction-following and safety, resulting in models that obey benign requests but refuse harmful ones. While this refusal behavior is widespread across chat models, its underlying mechanisms remain poorly understood. In this work, we show that refusal is mediated by a one-dimensional subspace, across 13 popular open-source chat models up to 72B parameters in size. Specifically, for each model, we find a single direction such that erasing this direction from the model's residual stream activations prevents it from refusing harmful instructions, while adding this direction elicits refusal on even harmless instructions. Leveraging this insight, we propose a novel white-box jailbreak method that surgically disables refusal with minimal effect on other capabilities. Finally, we mechanistically analyze how adversarial suffixes suppress propagation of the refusal-mediating direction. Our findings underscore the brittleness of current safety fine-tuning methods. More broadly, our work showcases how an understanding of model internals can be leveraged to develop practical methods for controlling model behavior.

</details>

### 28. Not All Refusals Are Equal: How Safety Alignment Fails Cybersecurity at Scale

📄 [arXiv](https://arxiv.org/abs/2607.02714)　📅 2026-07　🏷 NeurIPS 2026

**关键词**：`analysis`、`domain-specific abliteration`、`layer-distributed refusal`、`cybersecurity`

👤 **作者**：Vadym Hadetskyi、Dario Pasquini、Artem Sorokin

- 🎯 **研究动机**：安全对齐不区分领域与危害程度，阻碍模型在合法授权的网络安全操作中发挥作用
- 🔬 **研究方法**：对 24 个开源 LLM 做大规模消融实验，发现拒绝占据跨层分布的多维子空间，在 1T 参数 Kimi K2 上仅消融网络安全域的有害概念分量；并按特征预测消融易感性
- 📌 **结论**：领域特定消融可用标准方法实现；安全训练类型与架构是最可靠的预测因子，模型可分为三个易感层级

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

There is no doubt that safety alignment is an essential step in LLM training. However, conceptually it does not distinguish between various domains and the level of potential harm of a query, which creates significant complications in the fields like cyber security, where a model should not be constrained by its safety circuits to accomplish the goals of legitimate, authorized operations. In this work, we share our findings from a large scale abliteration experiment on 24 open-source LLMs and show that domain-specific abliteration is achievable with standard methodology on the example of a 1T-parameter Kimi K2. Building on recent work showing that refusal in LLMs occupies a multi-dimensional subspace within layers, we find that it is also distributed widely across layers, especially in trillion-parameter MoE architectures, and so we aim to capture the part of it that represents harmful concepts in the cybersecurity domain exclusively. We also investigate the correlation between models' features and the effect of domain-specific abliteration, identifying that the type of safety training and architecture are the most reliable predictors. Finally, we classify the models into 3 abliteration susceptibility tiers and put forward a set of conjectures as to why a particular effect from this intervention might be observed in a given model.

</details>

### 29. Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration

📄 [arXiv](https://arxiv.org/abs/2606.05396)　📅 2026-06

**关键词**：`analysis`、`code-model abliteration`、`willingness-capability split`、`CWE injection`

👤 **作者**：Cristina Carleo、Pietro Liguori、Naghmeh Ivaki、Domenico Cotroneo

- 🎯 **研究动机**：漏洞检测缺少大规模标注脆弱代码：挖掘语料标签噪声大，LLM 增强只变换种子；让对齐模型按规范注入 CWE 是替代路线但常被拒绝
- 🔬 **研究方法**：用 abliteration（残差流中投影掉拒绝方向）移除注入障碍，在 Python/CWE-89、Qwen2.5-Coder 3B/7B/14B 上以三工具检测器集成验证
- 📌 **结论**：拒绝率强烈依赖规模（14B 拒绝 100%、3B 几乎不拒绝）；abliteration 将拒绝降到 0 且语法有效率 >93%，注入率仍受能力约束（14B 88-97%），证明意愿与能力可分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Producing a labeled vulnerable code at scale is a recurring obstacle for learning-based vulnerability detection: mined corpora carry substantial label noise, and existing LLM-based augmentation propagates these inaccuracies because it transforms vulnerable seeds rather than synthesising vulnerabilities from a specification. A complementary route is to start from safe code and ask an instruction-tuned LLM to inject a specified CWE (which would shift the labeling burden from open-ended detection to bounded binary confirmation) but safety-aligned code LLMs systematically refuse such prompts. This paper is a preliminary feasibility study of abliteration, a low-rank weight edit that orthogonally projects out the refusal direction in the residual stream, as a tool to remove this barrier. We use Python and CWE-89 (SQL injection) as a case study, evaluating the Qwen2.5-Coder-Instruct family at 3B, 7B, and 14B parameters on safe samples drawn from PromSec and SafeCoder, replicated three times per condition. We find that (i) refusal on injection prompts is strongly size- and prompt-context-dependent: the 14B refuses 100% of prompts, the 7B refuses 73% of PromSec but only 5% of SafeCoder, whereas the 3B is essentially never blocked; (ii) abliteration reduces refusal to zero or near-zero across all sizes while leaving syntactic validity above 93%, supporting the view that, in this setting, refusal can be detached from measured code-generation capability; and (iii) the post-abliteration injection rate remains capacity-bound (88-97% on the 14B, 89-90% on the 7B, and 25-48% on the 3B) separating willingness, which abliteration unlocks, from capability, which scales with parameters. Vulnerability verdicts are produced by a three-tool detector ensemble (CodeQL, Semgrep, Bandit) followed by manual adjudication by two authors on detector-positive outputs.

</details>

### 30. Understanding the Effects of Safety Unalignment on Large Language Models

📄 [arXiv](https://arxiv.org/abs/2604.02574) · 🌐 [Project](https://colm.cc/Conferences/2026/AcceptedPapers)　📅 2026-04

**关键词**：`analysis`、`safety unalignment`、`weight orthogonalization`、`jailbreak fine-tuning`、`malicious capability`、`malicious capability recovery`

👤 **作者**：John T. Halloran

- 🎯 **研究动机**：jailbreak-tuning 与权重正交化两种去对齐方法只被按拒绝率孤立分析，对恶意能力的相对影响未知
- 🔬 **研究方法**：用 JT 与 WO 对六个不同规模 LLM 去对齐，跨大量恶意与良性任务系统比较
- 📌 **结论**：WO 产物助恶能力远强于 JT：更少幻觉、更好保留自然语言性能、更擅长对抗与网络攻击；SFT 可有效限制 WO 攻击能力而不损性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment has become a critical step to ensure LLMs refuse harmful requests while providing helpful and harmless responses. However, despite the ubiquity of safety alignment for deployed frontier models, two separate lines of recent work--jailbreak-tuning (JT) and weight orthogonalization (WO)--have shown that safety guardrails may be largely disabled, resulting in LLMs which comply with harmful requests they would normally refuse. In spite of far-reaching safety implications, analysis has largely been limited to refusal rates of each unalignment method in isolation, leaving their relative effects on adversarial LLM capabilities unknown. To fill this gap, we study the impact of unaligning six popular LLMs of various sizes across a large number of malicious and benign tasks, using both JT and WO. Across the evaluated models, we show that while refusal degradation is split between the two methods, WO produces LLMs far more capable of aiding in malicious activity; in contrast to JT, the majority of WO unaligned models are far less prone to hallucinations, better retain their original natural-language performance, and are more effective at state-of-the-art adversarial and cyber attacks. To thus help mitigate the malicious risks of WO unalignment, we conclude by showing that supervised fine-tuning effectively limits the adversarial attack abilities enabled by WO, without drastically affecting hallucination rates or natural language performance.

</details>

### 31. Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families

📄 [arXiv](https://arxiv.org/abs/2607.17427)　📅 2026-07

**关键词**：`analysis`、`off-target effect`、`decision disposition`、`provenance control`、`q-fin.CP`

👤 **作者**：Aleksander Fafuła

- 🎯 **研究动机**：abliteration（删除权重中的拒绝方向）是流行的 uncensored 模型配方，其对决策倾向的脱靶效应未被量化
- 🔬 **研究方法**：用 21,600 个不确定性决策（华沙交易所 60 只股票 18 周涨跌判断）作倾向探针，在严格控制来源与提示的条件下对比两个 MoE 家族的 base 与 abliterated 版本
- 📌 **结论**：abliterated 模型系统性更乐观（Gemma +12.2pp、Qwen +7.4pp 预注册终点）、自辩更长、不确定性用词更少；置信度变化在两家族间符号相反——同一切除造就不同决策者而非仅减去拒绝

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Abliteration - deleting a model's refusal direction from its weights - is the standard recipe behind popular "uncensored" open-weight models. We show the surgery is not clean. As a disposition probe we use 21,600 decisions under uncertainty - weekly up/down calls on 60 Warsaw Stock Exchange equities over 18 weeks, replayed through a frozen pipeline so the decision-layer model is the only variable. The task elicits no refusals at all, so any between-arm delta is pure side effect. Holding provenance constant (official BF16 checkpoints, a single abliteration author, an identical serving stack, one byte-identical frozen prompt), we compare base and abliterated arms of two Mixture-of-Experts families, Gemma-4-26B-A4B-it and Qwen3-30B-A3B-Instruct-2507. Three effects replicate across both families (weeks-clustered bootstrap CIs excluding zero): abliterated models are systematically more optimistic (+12.2 pp Gemma, +7.4 pp Qwen; the confirmed preregistered endpoint), justify themselves at greater length, and use fewer explicit uncertainty words in forced self-critiques (both exploratory). A fourth effect reverses sign: the same operation makes Gemma-abliterated less confident and Qwen-abliterated more (family CIs non-overlapping) - one weight surgery, opposite shifts in expressed confidence. Capability covariates rule out instruction-following degradation as the driver, and no arm shows economic skill: the apparent edge of abliterated arms is regime beta, not alpha. Our provenance audit also caught two independent contamination channels - a mismatched-quantizer pilot pair and a stale community chat template that silently mangled the rendered prompt - suggesting toolchain artifacts are the rule in studies of community-modified checkpoints. Whoever deploys an "uncensored" model as an agent is deploying a measurably different decision-maker, not the base model minus refusals.

</details>

### 32. On the Failure of Topic-Matched Contrast Baselines in Multi-Directional Refusal Abliteration

📄 [arXiv](https://arxiv.org/abs/2603.22061)　📅 2026-03

**关键词**：`analysis`、`contrast-baseline failure`、`direction extraction`、`multi-direction abliteration`

👤 **作者**：Valentin Petrov

- 🎯 **研究动机**：拒绝方向提取中对比基线的构造一直被当作实现细节而非方法学问题
- 🔬 **研究方法**：在 Qwen 3.5 2B 上用逐类别匹配提示对、SOM 提取与 SVD 正交化，比较主题匹配与不匹配对比基线
- 📌 **结论**：主题匹配在任何层任何权重下都提不出功能方向（抵消有害/良性共享主成分），不匹配基线在六层完全消除拒答——abliteration 结论高度依赖提取协议

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Inasmuch as the removal of refusal behavior from instruction-tuned language models by directional abliteration requires the extraction of refusal-mediating directions from the residual stream activation space, and inasmuch as the construction of the contrast baseline against which harmful prompt activations are compared has been treated in the existing literature as an implementation detail rather than a methodological concern, the present work investigates whether a topically matched contrast baseline yields superior refusal directions. The investigation is carried out on the Qwen~3.5 2B model using per-category matched prompt pairs, per-class Self-Organizing Map extraction, and Singular Value Decomposition orthogonalization. It was found that topic-matched contrast produces no functional refusal directions at any tested weight level on any tested layer, while unmatched contrast on the same model, same extraction code, and same evaluation protocol achieves complete refusal elimination on six layers. The geometric analysis of the failure establishes that topic-matched subtraction cancels the dominant activation component shared between harmful and harmless prompts of the same subject, reducing the extracted direction magnitude below the threshold at which weight-matrix projection perturbs the residual stream. The implications for the design of contrast baselines in abliteration research are discussed.

</details>

### 33. Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks

📄 [arXiv](https://arxiv.org/abs/2608.25390)　📅 2026-08

**关键词**：`analysis`、`defense`、`refusal-prefix diversity`、`gradient stable rank`、`alignment hardening`、`refusal safeguard`

👤 **作者**：Andrey Labunets

- 🎯 **研究动机**：拒答行为集中于单一方向或低维子空间，vector ablation 即可移除，成因不明
- 🔬 **研究方法**：以 OLMo-2 为案例追踪拒答训练动态，分析首 token 损失的梯度与激活更新的 stable rank，并以受控微调验证多样化拒答开头
- 📌 **结论**：重复拒答前缀压低秩导致脆弱；多样化开头提高 stable rank 并增强对消融攻击的抵抗

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge in a concentrated, low-dimensional structure. In a case study of OLMo-2-0425-1B-Instruct we find that the refusal geometry reflects refusal training: activation updates resulting from refusal-completion first-token losses explain the resulting refusal direction and refusal subspace. We study refusal directions through the training dynamics across refusal datasets and reveal that their brittleness is associated with repetitive refusal starts, which in turn is linked to concentration of gradients and refusal features in a low-dimensional subspace. Across frozen-model analyses and controlled synthetic fine-tuning, we find evidence of a hardening lever: diverse refusal starts can raise stable ranks of gradients and activation changes, making refusals harder to remove with a vector ablation attack.

</details>

### 34. Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

📄 [arXiv](https://arxiv.org/abs/2608.17202)　📅 2026-08

**关键词**：`defense`、`CBRN safeguard`、`hazardous-procedure decoy`、`safety-removal attack`、`differentiable attack simulation`、`conditional decoy`

👤 **作者**：Mark Russinovich

- 🎯 **研究动机**：开源模型的安全对齐可被 abliteration 数分钟内从权重投影移除，尚无发布时防御能持久阻止
- 🔬 **研究方法**：诱饵硬化 Fool's Gold：承认拒答会被剥离但毒化其收益——剥离后危险操作请求的答案多为关键要素被伪造的诱饵；诱饵在攻击的可微模拟中训练、仅在受攻状态表达，refusal pin 与 benign leash 保住干净行为
- 📌 **结论**：过预注册门槛的六模型（9B-122B）上受攻态诱饵占 0.51-0.90；122B 防御模型在 CBRNE 相关切片 0.82-0.86 致命错误（未防御至多 0.10），K=64 采样共识也无法恢复可用程序

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Safety alignment in open-weight language models is trivially removable: abliteration projects a refusal-mediating direction out of the weights in minutes, and no release-time defense we are aware of prevents it durably. What cannot be prevented can be deceived. Our defense, decoy hardening ("Fool's Gold"), concedes the refusal strip and poisons its payoff: once refusal is stripped, most answers to hazardous operational requests are confident, fluent decoys whose critical elements are falsified. Decoys are trained inside a differentiable simulation of the attack, expressing only in the attacked state; a refusal pin and benign leash hold clean-state behavior to the original. We instantiate it on seven models from five families (9B-122B, dense and mixture-of-experts). On the six models passing our pre-registered efficacy gate, 0.51-0.90 of attacked-state responses to held-out prompts are decoys, +0.27-0.84 attributable to the defense; all six stay within registered benign-behavior and capability budgets; the seventh (smaller) fails the gate (boundary case). Rates replicate on a frozen test split or untouched strata. The claim is epistemic: without independent ground truth, no observation surface we tested separates falsified answers from correct ones - on external red-team benchmarks' CBRNE-adjacent slice, the defended 122B is fatally wrong on 0.82-0.86 of matched-quality answers vs at most 0.10 undefended. Repeated sampling does not restore trust: element-wise consensus at K=64 reconstructs a fully usable procedure on 0.083-0.625 of prompts where the instrument validates, vs 0.58-0.96 undefended, with no label-free way to tell the regimes apart; on the weakest such model the claim is per-draw only. We evaluate chemical and biological hazards; the defense does not address in-context jailbreaks and protects only the initially released defended weights.

</details>

### 35. Abliteration Mitigation via Refusal Aliases

📄 [arXiv](https://arxiv.org/abs/2608.18093)　📅 2026-08

**关键词**：`defense`、`analysis`、`refusal aliases`、`writer-reader repair`、`tamper resistance`、`abliteration resistance`

👤 **作者**：Nathan Truong

- 🎯 **研究动机**：abliteration 只需少量对比 prompt 即可提取拒答方向并投影移除，现有防御忽视拒答方向为何易被提取
- 🔬 **研究方法**：AMRA 对残差流 writer 矩阵做 rank-k 更新，把拒答诱发激活替换为随机别名并校正下游 reader 矩阵以保持原行为
- 📌 **结论**：Llama-3-8B 上消融后拒答分较无防御提升 2.16 分且 MMLU 退化低于 0.5 个百分点；Gemma-2-9B 提升 14.70 分但效用代价更大

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Abliteration, the removal of refusal capabilities from large language models by projecting weight matrices orthogonal to an extracted refusal direction, has emerged as a prominent safety concern through its ability to bypass post-training alignment using only a small set of contrastive prompts. We find that existing defenses commonly overlook the cause of abliteration; that is, how easily the refusal direction can be extracted. To hinder this process, we introduce a weight-editing method that obscures the refusal signal by applying rank-$k$ updates to residual stream writer matrices while replacing refusal-inducing activations with random aliases and correcting downstream reader matrices to preserve the model's original behavior. On Llama-3-8B, AMRA improves post-abliteration refusal scores by $2.16$ points over the undefended baseline with less than $0.5$ percentage points of MMLU degradation. On Gemma-2-9B, it improves the post-abliteration refusal by $14.70$ points over the baseline while keeping harmful output rates similar to the baseline, albeit at a greater utility cost.

</details>

### 36. TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering

📄 [arXiv](https://arxiv.org/abs/2602.06911) · 🌐 [Project](https://doi.org/10.1145/3770855.3817557)　📅 2026-02　🏷 KDD 2026

**关键词**：`benchmark`、`model tampering`、`fine-tuning attack sweep`、`alignment robustness`、`fine-tuning safety`、`safeguard tampering`

👤 **作者**：Saad Hossain、…、Sirisha Rambhatla

- 🎯 **研究动机**：LLM 防篡改能力评估缺少统一框架，数据集、指标与篡改配置各异致结果不可比
- 🔬 **研究方法**：TamperBench 整合权重空间微调攻击、潜空间表示攻击与对齐阶段防御，对 21 个开源模型按每对攻击-模型做超参扫描并同步评安全与能力
- 📌 **结论**：jailbreak-tuning 通常是最严重攻击，现有对齐阶段防御在系统化攻击扫描下大多失效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As increasingly capable open-weight large language models (LLMs) are deployed, improving their tamper resistance against unsafe modifications, whether accidental or intentional, becomes critical to minimize risks. However, there is no standard approach to evaluate tamper resistance. Varied datasets, metrics, and tampering configurations make it difficult to compare safety, utility, and robustness across different models and defenses. To address this, we introduce TamperBench, the first unified framework to systematically evaluate the tamper resistance of LLMs. TamperBench (i) curates a repository of state-of-the-art weight-space fine-tuning attacks, latent-space representation attacks, and alignment-stage defenses; (ii) enables realistic adversarial evaluation through systematic hyperparameter sweeps per attack-model pair; and (iii) provides both safety and utility evaluations. We use TamperBench to evaluate 21 open-weight LLMs, including defense-augmented variants, across nine tampering threats using standardized safety and capability metrics with hyperparameter sweeps per model-attack pair. The results provide insights including effects of post-training on tamper resistance, that jailbreak-tuning is typically the most severe attack, and that current alignment-stage defenses largely fail to withstand attack sweeps. Code is available at https://github.com/criticalml-uw/TamperBench.

</details>

### 37. Selective Knowledge Edit Reversal via Gated Singular Vector Shrinkage

📄 [arXiv](https://arxiv.org/abs/2609.02091)　📅 2026-09

**关键词**：`defense`、`knowledge editing`、`selective reversal`、`spectral repair`

👤 **作者**：Weifeng Jiang、Ruirui Chen、Qianren Mao、Junnan Liu、Qili Zhang、Kwok-Yan Lam

- 🎯 **研究动机**：恶意 knowledge edit 需要撤销，但现有参数级 reversal 多为全局清除，会连带抹除应保留的有益编辑
- 🔬 **研究方法**：假设每个 edit 稀疏编码在被编辑矩阵的 dominant singular subspace，提出谱域框架定位 edit 敏感分量并用 gated singular-vector shrinkage 选择性逆转目标编辑
- 📌 **结论**：多设定下可逆转选定编辑并保留其余编辑事实；编辑数适中时不同编辑在主导奇异分量中可分，为修复被编辑模型提供方向

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Knowledge editing provides an efficient way to update factual knowledge in large language models. However, malicious edits may introduce safety risks, making it necessary to reverse undesirable editing effects. Existing reversal methods for parameter-modifying edits mainly focus on global removal, which may also erase beneficial edits that should be preserved. In this paper, we study selective reversal of edited knowledge, where the goal is to reverse targeted edited facts while preserving the remaining edited facts. Based on the hypothesis that each edit is sparsely encoded within the dominant subspace of the edited matrix, we propose a spectral-based reversal framework that locates edit-sensitive components within the dominant singular subspace of edited weights. Experiments across multiple settings demonstrate the effectiveness of our method in reversing selected edits while preserving unrelated edited facts. These results suggest that different edits are sparsely encoded within dominant singular components and can be separable when the number of edits is moderate, making selective spectral reversal a promising direction for locating edit-specific components and repairing edited language models.

</details>

### 38. Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness

📄 [arXiv](https://arxiv.org/abs/2608.25429)　📅 2026-08

**关键词**：`defense`、`analysis`、`capability removal`、`relearning resistance`、`weight selectivity`、`relearning robustness`

👤 **作者**：Yi Chen、…、Joo-Young Kim

- 🎯 **研究动机**：unlearned LLM 短暂微调即可复活已删知识，而全局权重距离在破坏性更新下会误导鲁棒性预测
- 🔬 **研究方法**：FRAG 免训练度量更新对 forget 与 retain 关键权重的对齐差以区分选择性与稠密更新，并据此提出 Forget-Retain Pruning
- 📌 **结论**：weight selectivity 比距离更能预测 relearning robustness，FRP 进一步增强抗复学能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to make a model forget specific data, yet unlearned LLMs often fail to stay unlearned: brief fine-tuning can revive removed knowledge. Existing robustness predictors rely on global weight-space displacement, but distance alone can be misleading when random or destructive updates collapse performance. We argue that relearning robustness depends on update structure: robust unlearning should affect forget-critical weights while sparing retain-critical ones. We introduce the Forget-Retain Alignment Gap (FRAG), a training-free predictor that scores an update's forget-retain alignment without running a relearning attack, and separates selective from dense updates more reliably than global distance. Building on the forget-critical, retain-sparing principle, Forget-Retain Pruning (FRP) improves relearning robustness. Our results suggest that weight selectivity better explains robustness than distance alone. Code is available at https://github.com/Yi1-Chen/FRAG.

</details>

### 39. ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control

📄 [arXiv](https://arxiv.org/abs/2608.23034)　📅 2026-08

**关键词**：`defense`、`restricted capability`、`trajectory boundary`、`persistent suppression`、`test-time unlearning`、`stateful boundary control`

👤 **作者**：Xunlei Chen、Qinghui Gong、Ruini Xue、Yaodong Hu、Tian Lan、Wenhong Tian

- 🎯 **研究动机**：现有 test-time unlearning 做孤立逐点激活修正，忽略自回归生成会从 prompt、cache 与生成前缀持续重构隐藏态，后续状态可能重回受限知识区
- 🔬 **研究方法**：ST²U 把 test-time unlearning 形式化为轨迹级边界控制：在低维可逆坐标建模受限知识边界且不动正交分量，推理时沿轨迹监测风险、做带上下文锚定的最小修正并跨 token 传播历史修正状态
- 📌 **结论**：三个 benchmark、三个模型家族上整体平衡最佳，受限知识 re-entry 从基线 46.50–59.10% 降至 13.76–19.84%，同时保留非目标能力

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids costly retraining and parameter updates by intervening only during inference. However, existing activation-editing methods apply isolated pointwise corrections, overlooking how autoregressive generation continually reconstructs hidden states from the prompt, cache, and generated prefix. Consequently, later states may return to restricted knowledge regions after a locally successful correction, causing restricted knowledge re-entry. In this work, we propose Stateful Test-Time Unlearning via restricted knowledge boundary control (ST$^2$U), which formulates test-time unlearning as trajectory-wide boundary control. ST$^2$U first models restricted knowledge boundaries in low-dimensional invertible coordinates while leaving orthogonal non-target components unchanged. During inference, ST$^2$U monitors risk along the trajectory, applies minimal boundary corrections with contextual anchoring, and propagates historical correction states across tokens to mitigate knowledge re-entry. This trajectory-wide control enables more persistent forgetting while preserving non-target capabilities and limiting inference overhead. Across three benchmarks and three model families, ST$^2$U delivers the strongest overall balance, combining best or second-best retention with competitive forgetting and substantially less restricted-knowledge re-entry than test-time baselines (13.76%-19.84% versus 46.50%-59.10%).

</details>

### 40. BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.22557)　📅 2026-08

**关键词**：`defense`、`capability erasure`、`sequential removal`、`utility retention`、`bilevel LoRA`、`clamped entropy`

👤 **作者**：Md Toufikuzzaman、Ahmad Mousavi、Dongwon Lee

- 🎯 **研究动机**：现有 LLM unlearning 鲁棒性不足：无界 forget loss 破坏连贯性、固定权重平衡无法适应 retain 难度漂移、单 benchmark 有效的方法在规模化或重复应用时失效
- 🔬 **研究方法**：BLADE 约束双层框架：clamped-entropy forget loss 使 token 达到足够不确定性后梯度恰为零，非对称增广 Lagrangian 违规后永久棘轮式收紧 retain 保护，双层结构限定在 LoRA adapter 内逐步先修复 retain 损伤再遗忘
- 📌 **结论**：TOFU、MUSE Books、KnowUndo 平均综合分超最强基线 6%、9%、7%，在 4 倍规模与 MUSE News 连续 4 步遗忘下保持稳定而最佳竞品完全崩溃

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing LLM unlearning methods struggle with robustness: unbounded forget losses degrade model coherence, fixed-weight balancing cannot adapt as retain difficulty shifts mid-training, and methods that work on one benchmark falter under scaling or repeated application. We propose BLADE, a constrained bilevel framework whose three mechanisms give smooth, predictable control over the optimization landscape: a clamped-entropy forget loss whose gradient is exactly zero once a token reaches sufficient uncertainty; an asymmetric augmented Lagrangian that permanently ratchets retain protection after any violation; and a bilevel structure confined to LoRA adapters that repairs retain damage before each forgetting step. BLADE dominates across three benchmark families, improving average composite scores over the strongest baselines by $6$% on TOFU, $9$% on MUSE Books, and $7$% on KnowUndo, and it remains stable under $4\times$ scaling and $4$ sequential unlearning steps on MUSE News where the best competing method collapses entirely.

</details>

### 41. Forgotten in Weights, Recovered by Tools: Agentic Tool Unlearning for LLM Agents

📄 [arXiv](https://arxiv.org/abs/2608.21544)　📅 2026-08

**关键词**：`defense`、`tool-mediated recovery`、`target-seeking tool call`、`knowledge leakage`、`capability removal`、`external-tool recovery`

👤 **作者**：Baicheng Chen、…、Meng Jiang

- 🎯 **研究动机**：现有 unlearning 只抑制参数化直接回忆，工具增强 Agent 仍可经 web 搜索、检索或数据库查找恢复遗忘目标（tool-mediated recovery），评测存在错配
- 🔬 **研究方法**：ATU 两阶段框架：先做参数知识遗忘抑制直接回忆，再在模拟工具环境中做轨迹级 RL，惩罚 target-seeking 工具行为与最终答案泄漏
- 📌 **结论**：RWKU 与 MUSE 上跨不同 LLM 架构取得目标遗忘与保留效用间更好平衡，unlearning 在工具增强部署下更稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) are increasingly deployed as tool-augmented agents, where responses can depend on tool calls and external observations rather than model parameters alone. This creates an evaluation mismatch for LLM unlearning: previous unlearning methods may suppress direct parametric recall, but an agent can still recover the same forget target through tools such as web search, retrieval, or database lookup. We identify this failure mode as tool-mediated recovery and study agentic tool unlearning, which aims to reduce both parametric recall and tool-mediated recovery while preserving normal tool use for retained knowledge. To address this challenge, we propose Agentic Tool Unlearning (ATU), a two-stage framework. The first stage applies parametric knowledge unlearning to suppress direct recall, while the second stage performs trajectory-level reinforcement learning in simulated tool-augmented environments to penalize target-seeking tool behavior and final-answer leakage. Experiments on RWKU and MUSE across different LLM architectures show that ATU achieves a better balance between target forgetting and retained utility, making unlearning more robust under tool-augmented agent deployment.

</details>

### 42. Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.20960)　📅 2026-08

**关键词**：`benchmark`、`scientific knowledge drift`、`claim-level unlearning`、`outdated evidence`、`claim-level capability removal`、`structured knowledge`

👤 **作者**：Snigdha Paul、Manasi Patwardhan、Arman Cohan

- 🎯 **研究动机**：科学主张会被撤回、证伪或更新，而科学知识相互关联且持续演化，现有 instance-level 遗忘研究与评测无法覆盖 claim 级删除
- 🔬 **研究方法**：提出 Scientific Claim Unlearning 任务并构建 benchmark SciUnlearn，系统评测现有 unlearning 方法
- 📌 **结论**：现有方法无法有效消除 claim 级知识，多只实现表层抑制，需要面向结构化知识删除的专门方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while maintaining overall model utility. Existing studies primarily investigate instance-level forgetting; however, scientific claims introduce additional challenges because they are interconnected, and continually evolving. To address this gap, we introduce the task of Scientific Claim Unlearning and present a new benchmark, SciUnlearn. We show that current unlearning approaches are unable to effectively eliminate claim-level knowledge and often achieve only superficial suppression, highlighting the need for specialized methods designed for structured knowledge removal.

</details>

### 43. SAUL: Sharpness-Aware Augmented-Lagrangian Unlearning

📄 [arXiv](https://arxiv.org/abs/2608.16249)　📅 2026-08

**关键词**：`defense`、`machine unlearning`、`capability control`、`tamper resistance`

👤 **作者**：Jaewan Choi、Junyoung Yang、Sangdon Park

- 🎯 **研究动机**：LLM unlearning 在擦除目标知识与保留通用效用间权衡困难，遗忘程度通常只被隐式指定
- 🔬 **研究方法**：SAUL 把遗忘形式化为显式约束的受约束最小化（忘够但别多忘）：增广拉格朗日控制器按违反度自适应加压并可停用遗忘更新，双侧 sharpness-aware 更新与双优化器稳定动力学
- 📌 **结论**：TOFU、WMDP、MUSE 上遗忘-效用权衡优于 sharpness/扰动基线；控制器作为即插修饰符也能改善代表性基线的遗忘后效用

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning in Large Language Models (LLMs) faces a critical trade-off between erasing target knowledge and preserving general utility. We propose SAUL (Sharpness-Aware Augmented-Lagrangian Unlearning), which formulates unlearning as a constrained minimization problem following the principle of "forget enough, but no more than necessary." At its core, SAUL formulates forgetting as an explicit constraint with a prescribed satisfaction criterion, whereas prior unlearning methods typically specify the desired level of forgetting implicitly through optimization objectives. An augmented Lagrangian controller adaptively adjusts forget-side pressure according to constraint violation and can eventually deactivate the forget-side update as the prescribed criterion remains satisfied. Sharpness-aware updates on both retain and forget objectives, together with a dual-optimizer design that maintains role-separated states, further stabilize the resulting unlearning dynamics. We evaluate SAUL on the TOFU, WMDP, and MUSE benchmarks, demonstrating favorable forgetting-utility trade-offs over representative sharpness- and perturbation-based baselines under benchmark-specific forgetting criteria. Beyond the complete SAUL framework, we further show on TOFU that applying the augmented-Lagrangian controller as a drop-in modifier to representative baselines improves their post-forgetting utility, demonstrating the practical value of explicit forgetting control.

</details>

### 44. CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing

📄 [arXiv](https://arxiv.org/abs/2602.15823) · 🎓 [Official](https://icml.cc/virtual/2026/poster/62453)　📅 2026-02　🏷 ICML 2026

**关键词**：`defense`、`capability control`、`tamper resistance`、`access restriction`、`safety alignment`、`empirical evaluation`

👤 **作者**：Zarif Ikram、Arad Firouzkouhi、Stephen Tu、Mahdi Soltanolkotabi、Paria Rashidinejad

- 🎯 **研究动机**：LLM 编辑方法在改变目标行为时会悄悄博弈编辑代理并腐蚀通用能力
- 🔬 **研究方法**：CrispEdit 把能力保持表达为 Bregman 散度约束，用 K-FAC 与免矩阵投影器将编辑更新投影到能力损失面的低曲率子空间
- 📌 **结论**：标准编辑基准上保持高编辑成功率的同时，平均能力退化低于 1%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A central challenge in large language model (LLM) editing is capability preservation: methods that successfully change targeted behavior can quietly game the editing proxy and corrupt general capabilities, producing degenerate behaviors reminiscent of proxy/reward hacking. We present CrispEdit, a scalable and principled second-order editing algorithm that treats capability preservation as an explicit constraint, unifying and generalizing several existing editing approaches. CrispEdit formulates editing as constrained optimization and enforces the constraint by projecting edit updates onto the low-curvature subspace of the capability-loss landscape. At the crux of CrispEdit is expressing capability constraint via Bregman divergence, whose quadratic form yields the Gauss-Newton Hessian exactly and even when the base model is not trained to convergence. We make this second-order procedure efficient at the LLM scale using Kronecker-factored approximate curvature (K-FAC) and a novel matrix-free projector that exploits Kronecker structure to avoid constructing massive projection matrices. Across standard model-editing benchmarks, CrispEdit achieves high edit success while keeping capability degradation below 1% on average across datasets, significantly improving over prior editors.

</details>

### 45. SCALPEL: Selective Capability Ablation via Low-rank Parameter Editing for Large Language Model Interpretability Analysis

📄 [arXiv](https://arxiv.org/abs/2601.07411)　📅 2026-01

**关键词**：`tool`、`capability ablation`、`low-rank subspace`、`parameter editing`

👤 **作者**：Zihao Fu、Xufeng Duan、Zhenguang G. Cai

- 🎯 **研究动机**：传统模块归因假设能力映射到特定组件，忽视多能力共享模块与能力跨模块分布的细粒度结构
- 🔬 **研究方法**：SCALPEL 把能力表示为跨层分布的低秩参数子空间：训练 LoRA adapter 削弱区分对错答案的目标能力同时保持语言建模质量，实现选择性消融
- 📌 **结论**：在 BLiMP 等能力与语言任务上成功移除目标能力并保留通用能力，揭示能力呈低秩结构、可经参数空间干预选择性消融

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models excel across diverse domains, yet their deployment in healthcare, legal systems, and autonomous decision-making remains limited by incomplete understanding of their internal mechanisms. As these models integrate into high-stakes systems, understanding how they encode capabilities has become fundamental to interpretability research. Traditional approaches identify important modules through gradient attribution or activation analysis, assuming specific capabilities map to specific components. However, this oversimplifies neural computation: modules may contribute to multiple capabilities simultaneously, while single capabilities may distribute across multiple modules. These coarse-grained analyses fail to capture fine-grained, distributed capability encoding. We present SCALPEL (Selective Capability Ablation via Low-rank Parameter Editing for Large language models), a framework representing capabilities as low-rank parameter subspaces rather than discrete modules. Our key insight is that capabilities can be characterized by low-rank modifications distributed across layers and modules, enabling precise capability removal without affecting others. By training LoRA adapters to reduce distinguishing correct from incorrect answers while preserving general language modeling quality, SCALPEL identifies low-rank representations responsible for particular capabilities while remaining disentangled from others. Experiments across diverse capability and linguistic tasks from BLiMP demonstrate that SCALPEL successfully removes target capabilities while preserving general capabilities, providing fine-grained insights into capability distribution across parameter space. Results reveal that capabilities exhibit low-rank structure and can be selectively ablated through targeted parameter-space interventions, offering nuanced understanding of capability encoding in LLMs.

</details>

### 46. Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem

🎓 [Official](https://aclanthology.org/2026.acl-long.890/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`capability control`、`tamper resistance`、`knowledge removal`、`utility retention`

👤 **作者**：Zeguan Xiao、…、Guanhua Chen

- 🎯 **研究动机**：LLM 遗忘应保留为主目标、遗忘为辅，重平衡损失难解遗忘-保留权衡
- 🔬 **研究方法**：保留优先的梯度合成框架：解耦任务特定梯度提取与冲突感知组合，适配 PCGrad 并提出 SAGO 符号约束合成
- 📌 **结论**：WMDP Bio 上目标模型 MMLU 恢复从 44.6%（朴素）到 94.0%（+PCGrad）再到 96.0%（+SAGO），遗忘强度相当；重塑梯度几何是关键

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning for large language models (LLMs) aims to remove targeted knowledge while preserving general capability. In this paper, we recast LLM unlearning as an asymmetric two-task problem: retention is the primary objective and forgetting is an auxiliary. From this perspective, we propose a retention-prioritized gradient synthesis framework that decouples task-specific gradient extraction from conflict-aware combination. Instantiating the framework, we adapt established PCGrad to resolve gradient conflicts, and introduce SAGO, a novel retention-prioritized gradient synthesis method. Theoretically, both variants ensure non-negative cosine similarity with the retain gradient, while SAGO achieves strictly tighter alignment through constructive sign-constrained synthesis. Empirically, on WMDP Bio/Cyber and RWKU benchmarks, SAGO consistently pushes the Pareto frontier: e.g., on WMDP Bio (SimNPO+GD), recovery of target model MMLU performance progresses from 44.6% (naive) to 94.0% (+PCGrad) and further to 96.0% (+SAGO), while maintaining comparable forgetting strength. Our results show that re-shaping gradient geometry, rather than re-balancing losses, is the key to mitigating unlearning-retention trade-offs.

</details>

### 47. Decoding-Unlearning: Fact Forgetting via Entropy-Guided Inference

🎓 [Official](https://aclanthology.org/2026.acl-long.1850/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`capability control`、`tamper resistance`、`knowledge removal`、`utility retention`

👤 **作者**：Jingwen Pu、…、Kun She

- 🎯 **研究动机**：参数更新式遗忘微调成本高、有不可逆风险且依赖难以齐全的 forget 与 retain 数据集
- 🔬 **研究方法**：SEGUE 免训练即插即用的推理时遗忘：探针检测涉及可遗忘概念的查询，熵引导解码抑制目标知识、实现可控非事实生成
- 📌 **结论**：MUSE、RWKU、WMDP 上有效平衡敏感知识抑制与生成质量，优于现有推理时遗忘方法

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) exhibit powerful capabilities but inevitably memorize sensitive information, raising privacy, copyright, and safety concerns. Existing LLM unlearning methods typically rely on updating model parameters. While effective, they are often limited in real-world scenarios: fine-tuning large-scale models is costly, may introduce potential irreversible risks, and depends on both forget and retain datasets, which are often difficult to obtain in full. To address these challenges, an ideal solution is to achieve unlearning at inference time. To this end, we propose SEGUE, a training-free, plug-and-play inference-time unlearning strategy. SEGUE employs a probe to detect queries involving forgettable concepts and applies entropy-guided decoding to suppress target knowledge, enabling controllable non-factual generation while preserving overall model capabilities. Experiments on the MUSE, RWKU, and WMDP datasets, covering copyright, entity, and potential-risk knowledge, show that SEGUE effectively balances sensitive knowledge suppression and generation quality, outperforming existing most inference-time unlearning methods.

</details>

### 48. CRISP: Persistent Concept Unlearning via Sparse Autoencoders

🎓 [Official](https://aclanthology.org/2026.acl-long.82/)　📅 2026　🏷 ACL 2026

**关键词**：`defense`、`machine unlearning`、`capability control`、`tamper resistance`、`cybersecurity`、`knowledge removal`

👤 **作者**：Tomer Ashuach、Dana Arad、Aaron Mueller、Martin Tutek、Yonatan Belinkov

- 🎯 **研究动机**：SAE 遗忘方法多在推理时干预、不产生持久参数改变，可被有参数访问权的恶意者绕过或逆转
- 🔬 **研究方法**：CRISP 自动识别多层中显著的 SAE 特征并抑制其激活，形成参数高效的持久概念遗忘
- 📌 **结论**：两个 LLM 的 WMDP 安全关键遗忘任务超越先前方法，移除有害知识并保留通用与域内能力，实现目标与良性概念的语义一致分离

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are increasingly deployed in real-world applications, the need to selectively remove unwanted knowledge while preserving model utility has become paramount. Recent work has explored sparse autoencoders (SAEs) to perform precise interventions on monosemantic features. However, most SAE-based methods operate at inference time, which does not create persistent changes in the model’s parameters. Such interventions can be bypassed or reversed by malicious actors with parameter access. We introduce CRISP, a parameter-efficient method for persistent concept unlearning using SAEs. CRISP automatically identifies salient SAE features across multiple layers and suppresses their activations. We experiment with two LLMs and show that our method outperforms prior approaches on safety-critical unlearning tasks from the WMDP benchmark, successfully removing harmful knowledge while preserving general and in-domain capabilities. Feature-level analysis reveals that CRISP achieves semantically coherent separation between target and benign concepts, allowing precise suppression of the target features.

</details>

### 49. Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs

📄 [arXiv](https://arxiv.org/abs/2512.05648)　📅 2025-12

**关键词**：`defense`、`capability removal`、`selective gradient masking`、`label noise`

👤 **作者**：Igor Shilov、…、Cem Anil

- 🎯 **研究动机**：数据过滤面临大规模标注昂贵的困境，少量错标有害数据仍可能在模型中孕育危险能力
- 🔬 **研究方法**：SGTM 改进 Gradient Routing：以选择性梯度掩码把目标领域样本限制在专用参数中更新、训练后移除，在双语合成数据与 Wikipedia 生物学知识两个移除场景评测
- 📌 **结论**：标签噪声下 retain/forget 权衡优于数据过滤与原 Gradient Routing；恢复目标知识所需微调步数是 RMU 的约 7 倍

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models increasingly possess capabilities that carry dual-use risks. While data filtering has emerged as a pretraining-time mitigation, it faces significant challenges: labeling whether data is harmful is expensive at scale, and given improving sample efficiency with larger models, even small amounts of mislabeled content could give rise to dangerous capabilities. To address risks associated with mislabeled harmful content, prior work proposed Gradient Routing (Cloud et al., 2024) -- a technique that localizes target knowledge into a dedicated subset of model parameters so they can later be removed. We explore an improved variant of Gradient Routing, which we call Selective GradienT Masking (SGTM), with particular focus on evaluating its robustness to label noise. SGTM zero-masks selected gradients such that target domain examples only update their dedicated parameters. We test SGTM's effectiveness in two applications: removing knowledge of one language from a model trained on a bilingual synthetic dataset, and removing biology knowledge from a model trained on English Wikipedia. In both cases SGTM provides better retain/forget trade-off in the presence of labeling errors compared to both data filtering and a previously proposed instantiation of Gradient Routing. Unlike shallow unlearning approaches that can be quickly undone through fine-tuning, SGTM exhibits strong robustness to adversarial fine-tuning, requiring seven times more fine-tuning steps to reach baseline performance on the forget set compared to a finetuning-based unlearning method (RMU). Our results suggest SGTM provides a promising pretraining-time complement to existing safety mitigations, particularly in settings where label noise is unavoidable.

</details>

### 50. Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs

📄 [arXiv](https://arxiv.org/abs/2508.06601) · 🌐 [Project](https://deepignorance.ai/) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10006630)　📅 2025-08　🏷 ICLR 2026

**关键词**：`defense`、`capability absence`、`pretraining filtering`、`tamper resistance`

👤 **作者**：Kyle O'Brien、…、Stella Biderman

- 🎯 **研究动机**：后训练安全方法难以抵御超过几十步的对抗微调，开源权重模型缺乏防篡改手段
- 🔬 **研究方法**：提出多阶段可扩展数据过滤管线，从零预训练多个 6.9B 模型剔除双重用途主题文本
- 📌 **结论**：对最多 10000 步、300M token 的生物威胁对抗微调仍强抵抗，超后训练基线一个数量级且无关能力无损；但危险知识入上下文仍可用，需纵深防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Open-weight AI systems offer unique benefits, including enhanced transparency, open research, and decentralized access. However, they are vulnerable to tampering attacks which can efficiently elicit harmful behaviors by modifying weights or activations. Currently, there is not yet a robust science of open-weight model risk management. Existing safety fine-tuning methods and other post-training techniques have struggled to make LLMs resistant to more than a few dozen steps of adversarial fine-tuning. In this paper, we investigate whether filtering text about dual-use topics from training data can prevent unwanted capabilities and serve as a more tamper-resistant safeguard. We introduce a multi-stage pipeline for scalable data filtering and show that it offers a tractable and effective method for minimizing biothreat proxy knowledge in LLMs. We pretrain multiple 6.9B-parameter models from scratch and find that they exhibit substantial resistance to adversarial fine-tuning attacks on up to 10,000 steps and 300M tokens of biothreat-related text -- outperforming existing post-training baselines by over an order of magnitude -- with no observed degradation to unrelated capabilities. However, while filtered models lack internalized dangerous knowledge, we find that they can still leverage such information when it is provided in context (e.g., via search tool augmentation), demonstrating a need for a defense-in-depth approach. Overall, these findings help to establish pretraining data curation as a promising layer of defense for open-weight AI systems.

</details>

### 51. Distillation Robustifies Unlearning

📄 [arXiv](https://arxiv.org/abs/2506.06278) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/800981b7bff06c3feb88c65cc712ba2b-Abstract-Conference.html)　📅 2025-06　🏷 NeurIPS 2025

**关键词**：`defense`、`capability removal`、`unlearn-and-distill`、`relearning resistance`

👤 **作者**：Bruce W. Lee、…、Alexander Matt Turner

- 🎯 **研究动机**：现有 LLM 遗忘方法几步微调即可复原，连理想化遗忘也不鲁棒
- 🔬 **研究方法**：证明从已遗忘模型输出蒸馏可传递行为而留下潜在能力，提出 UNDO：把已遗忘模型蒸馏到自身加噪副本
- 📌 **结论**：最强设置下以 60-80% 算力、0.01% 预训练数据标注即可匹配从头重训加完美过滤的鲁棒性，WMDP 上同样有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Current LLM unlearning methods are not robust. A few steps of finetuning can revert their effects. We begin by showing that this is true even for an idealized form of unlearning: training to imitate a model that was never trained on unwanted information. This shows that training a model can drastically modify its input-output behavior while leaving its underlying capabilities intact. In light of this dynamic, we show our main result. Training a randomly initialized student on the outputs of an unlearned model transfers behaviors while leaving latent capabilities behind. In short, distillation robustifies unlearning. Based on this result, we propose Unlearn-Noise-Distill-on-Outputs (UNDO), a scalable method that distills an unlearned model into a noised copy of itself. UNDO introduces a tunable tradeoff between compute cost and robustness, establishing a new Pareto frontier on synthetic language and arithmetic tasks. At its strongest setting, UNDO matches the robustness of a model retrained from scratch with perfect data filtering while using only 60-80% of the compute and requiring only 0.01% of the pretraining data to be labeled. We also show that UNDO robustifies unlearning on the more realistic Weapons of Mass Destruction Proxy (WMDP) benchmark. Since distillation is widely used in practice, incorporating an unlearning step beforehand offers a convenient path to robust capability removal.

</details>

### 52. Effective Skill Unlearning through Intervention and Abstention

📄 [arXiv](https://arxiv.org/abs/2503.21730) · 🎓 [Official](https://aclanthology.org/2025.naacl-long.322/)　📅 2025-03　🏷 ACL 2025

**关键词**：`tool`、`skill unlearning`、`neuron intervention`、`key-space detection`

👤 **作者**：Yongce Li、Chung-En Sun、Tsui-Wei Weng

- 🎯 **研究动机**：需要在保留整体能力的前提下精准遗忘 LLM 单项技能，且要求免训练
- 🔬 **研究方法**：发现同技能查询在 FFL key space 聚成可用超立方体分离的簇，据此提出 Neuron Adjust 与 Key Space Detection 两种免训练遗忘方法
- 📌 **结论**：Key Space Detection 使目标技能相对性能降超 80%，其他技能与 MMLU 降幅小于 10%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language Models (LLMs) have demonstrated remarkable skills across various domains. Understanding the mechanisms behind their abilities and implementing controls over them is becoming increasingly important for developing better models. In this paper, we focus on skill unlearning in LLMs, specifically unlearning a particular skill while retaining their overall capabilities. We introduce two lightweight, training-free machine skill unlearning techniques for LLMs. First, we observe that the pre-activation distribution of neurons in each Feed-Forward Layer (FFL) differs when the model demonstrates different skills. Additionally, we find that queries triggering the same skill cluster within the FFL key space and can be separated from other queries using a hypercube. Based on these observations, we propose two lightweight, training-free skill unlearning methods via \textit{intervention} and \textit{abstention} respectively: \texttt{Neuron Adjust} and \texttt{Key Space Detection}. We evaluate our methods on unlearning math-solving, Python-coding, and comprehension skills across seven different languages. The results demonstrate their strong unlearning capabilities for the designated skills. Specifically, \texttt{Key Space Detection} achieves over 80\% relative performance drop on the forgetting skill and less than 10\% relative performance drop on other skills and the model's general knowledge (MMLU) for most unlearning tasks. Our code is available at https://github.com/Trustworthy-ML-Lab/effective_skill_unlearning

</details>

### 53. Tamper-Resistant Safeguards for Open-Weight LLMs

📄 [arXiv](https://arxiv.org/abs/2408.00761) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fc49a629d33bc2461ed7a715ce44da68-Abstract-Conference.html)　📅 2024-08　🏷 ICLR 2025

**关键词**：`defense`、`open-weight safeguards`、`meta-learning`、`tamper resistance`

👤 **作者**：Rishub Tamirisa、…、Mantas Mazeika

- 🎯 **研究动机**：开放权重 LLM 的 refusal 与 unlearning 防护可被几步微调移除
- 🔬 **研究方法**：TAR 用元学习方法把防篡改防护构建进模型权重
- 📌 **结论**：数百步微调后防护仍基本保持，且不损良性能力，证明 tamper-resistance 可行

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Rapid advances in the capabilities of large language models (LLMs) have raised widespread concerns regarding their potential for malicious use. Open-weight LLMs present unique challenges, as existing safeguards lack robustness to tampering attacks that modify model weights. For example, recent works have demonstrated that refusal and unlearning safeguards can be trivially removed with a few steps of fine-tuning. These vulnerabilities necessitate new approaches for enabling the safe release of open-weight LLMs. We develop a method, called TAR, for building tamper-resistant safeguards into open-weight LLMs such that adversaries cannot remove the safeguards even after hundreds of steps of fine-tuning. In extensive evaluations and red teaming analyses, we find that our method greatly improves tamper-resistance while preserving benign capabilities. Our results demonstrate that progress on tamper-resistance is possible, opening up a promising new avenue to improve the safety and security of open-weight LLMs.

</details>

### 54. Representation Noising: A Defence Mechanism Against Harmful Finetuning

📄 [arXiv](https://arxiv.org/abs/2405.14577) · 🎓 [Official](https://proceedings.neurips.cc/paper_files/paper/2024/hash/172be8b0b88fc2b4aee74237d43f8c04-Abstract-Conference.html)　📅 2024-05　🏷 NeurIPS 2024

**关键词**：`defense`、`representation noising`、`harmful representation`、`open-weight safeguard`、`open-weight safeguards`、`harmful fine-tuning`

👤 **作者**：Domenic Rosati、…、Frank Rudzicz

- 🎯 **研究动机**：开放权重与微调 API 使模型暴露于 harmful fine-tuning，安全措施可被微调轻易逆转
- 🔬 **研究方法**：RepNoise 移除有害表示信息使微调后难以恢复，并可泛化到同分布的未见伤害子集
- 📌 **结论**：不损通用能力与良性可训练性；效力取决于跨层移除深度，跨分布攻击仍是盲区

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Releasing open-source large language models (LLMs) presents a dual-use risk since bad actors can easily fine-tune these models for harmful purposes. Even without the open release of weights, weight stealing and fine-tuning APIs make closed models vulnerable to harmful fine-tuning attacks (HFAs). While safety measures like preventing jailbreaks and improving safety guardrails are important, such measures can easily be reversed through fine-tuning. In this work, we propose Representation Noising (RepNoise), a defence mechanism that operates even when attackers have access to the weights. RepNoise works by removing information about harmful representations such that it is difficult to recover them during fine-tuning. Importantly, our defence is also able to generalize across different subsets of harm that have not been seen during the defence process as long as they are drawn from the same distribution of the attack set. Our method does not degrade the general capability of LLMs and retains the ability to train the model on harmless tasks. We provide empirical evidence that the efficacy of our defence lies in its ``depth'': the degree to which information about harmful representations is removed across all layers of the LLM. We also find areas where RepNoise still remains ineffective and highlight how those limitations can inform future research.

</details>

### 55. Stress Testing Unlearning Algorithms

📄 [arXiv](https://arxiv.org/abs/2608.22527)　📅 2026-08

**关键词**：`benchmark`、`capability removal`、`adversarial elicitation`、`boundary preservation`、`WMDP++`、`targeted extraction`

👤 **作者**：Noam Diamant、Neta Glazer、Ethan Fetaya

- 🎯 **研究动机**：现有 unlearning benchmark 不主动测试被遗忘信息能否被强行提取，也不评估语义邻近良性 boundary question 上的性能保留
- 🔬 **研究方法**：WMDP++ 扩展 WMDP：加入对被遗忘信息的 targeted extraction 攻击与边界问题系统性评测
- 📌 **结论**：同时压力测试移除的抗提取性与授权能力保留，为 LLM unlearning 提供更严格的评测基准

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Recently, machine unlearning, the removal of specific training data influence from a model, has gained increasing attention. In large language models (LLMs), unlearning is particularly challenging due to the ambiguity of inputs and outputs. Con- sequently, rigorous evaluation is critical for assessing both safety and utility, and for driving progress in unlearning meth- ods. We identify two key shortcomings in existing unlearning benchmarks: (1) they do not actively test whether unlearned information can still be forcibly extracted, and (2) they fail to evaluate performance preservation on boundary questions, be- nign queries that are semantically close to the unlearned con- tent. Here we introduce WMDP++, an extension of WMDP that addresses these gaps by incorporating targeted extrac- tion of unlearned information and systematic evaluation on boundary questions. WMDP++ provides a more stringent and informative benchmark for evaluating unlearning in LLMs.

</details>

### 56. ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.20338) · 📊 [Dataset](https://huggingface.co/datasets/sk0511/concept-guard)　📅 2026-08

**关键词**：`benchmark`、`context-sensitive unlearning`、`dual-use concept`、`utility preservation`、`concept-level unlearning`、`dual-use intent`

👤 **作者**：Sahil Kale、Ian Harris

- 🎯 **研究动机**：现有 unlearning 用不相交遗忘/保留集与直接事实回忆评测，无法衡量消除有害应用同时保留良性用法的能力
- 🔬 **研究方法**：引入双用途概念，ConceptGuard 的 forget/retain 集在概念使用上显式互补，评测意图敏感并最大化上下文分离
- 📌 **结论**：现有技术在该设定下表现差：上下文分离弱、ROUGE 与概念级指标差、概念级控制一致性差，遗忘-效用权衡强

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple and direct factual recall. This framing fails to capture a key requirement of unlearning, namely the ability to eliminate harmful behaviors while preserving benign and beneficial knowledge. We argue that effective unlearning must operate at the level of concepts, ensuring complete removal of unsafe applications while maintaining their correct and useful usage, thereby achieving conceptually meaningful and complete unlearning. To better evaluate unlearning techniques from such a practical viewpoint, we introduce the notion of dual-use concepts: concepts that can be used in both harmful and benign contexts. Building on these concepts, we construct a benchmark called ConceptGuard where forget and retain sets are explicitly complementary in concept usage. Our benchmark uniquely enables unlearning to be explored and gauged at the level of concepts, instead of sparse facts, and evaluation is intent-sensitive with the goal of maximizing contextual separation to promote safer behavior. We demonstrate that current unlearning techniques perform poorly under this setting, showing weak contextual separation alongside poor performance in ROUGE and concept-level metrics. Our results reveal strong forgetting-utility trade-offs, limited gains in contextual sensitivity, and poor consistency in concept-level control across methods, and provide ideas for unlearning approaches that better align with real-world safety requirements. Our dataset is publicly available.

</details>

### 57. The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning

📄 [arXiv](https://arxiv.org/abs/2403.03218) · 🌐 [Project](https://proceedings.mlr.press/v235/li24bc.html)　📅 2024-03　🏷 ICML 2024

**关键词**：`benchmark`、`hazardous knowledge`、`WMDP`、`representation misdirection`

👤 **作者**：Nathaniel Li、…、Dan Hendrycks

- 🎯 **研究动机**：现有危险能力评测私有且恶意使用场景覆盖窄，限制减少 LLM 恶意使用的研究
- 🔬 **研究方法**：发布 WMDP 基准：3668 道多选题代理测量生物、网络与化学安全危险知识；并提出基于表征控制的遗忘方法 RMU
- 📌 **结论**：RMU 降低 WMDP 性能同时保持生物、计算机科学等一般能力，表明遗忘是减少 LLM 恶意使用的可行路径

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The White House Executive Order on Artificial Intelligence highlights the risks of large language models (LLMs) empowering malicious actors in developing biological, cyber, and chemical weapons. To measure these risks, government institutions and major AI labs are developing evaluations for hazardous capabilities in LLMs. However, current evaluations are private and restricted to a narrow range of malicious use scenarios, which limits further research into reducing malicious use. To fill these gaps, we release the Weapons of Mass Destruction Proxy (WMDP) benchmark, a dataset of 3,668 multiple-choice questions that serve as a proxy measurement of hazardous knowledge in biosecurity, cybersecurity, and chemical security. To guide progress on unlearning, we develop RMU, a state-of-the-art unlearning method based on controlling model representations. RMU reduces model performance on WMDP while maintaining general capabilities in areas such as biology and computer science, suggesting that unlearning may be a concrete path towards reducing malicious use from LLMs. We release our benchmark and code publicly at https://wmdp.ai.

</details>

### 58. Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation

📄 [arXiv](https://arxiv.org/abs/2608.21606)　📅 2026-08

**关键词**：`benchmark`、`attack`、`capability recovery`、`adversarial prompting`、`unlearning robustness`、`unlearned-data recovery`

👤 **作者**：Ayush Gupta、…、Sadid Hasan

- 🎯 **研究动机**：现有 unlearning benchmark 只用干净非对抗查询评估，看似遗忘的信息能否经策略性提示恢复仍未知
- 🔬 **研究方法**：在 TOFU+Llama-3.2-3B-Instruct 上统一评估 prompt 式与微调式遗忘方法，对标准指标下的强者做对抗压力测试，并引入 LLM-as-judge 的 Attack Success Rate 指标
- 📌 **结论**：Forget Quality 超过 0.91 的方法对抗恢复 ASR 仍达 72.8–84.3%（接近未防护基线的 87.5%），而干净多语言改写仅测出 2.95% 泄漏——标准指标强不足以证明遗忘稳健

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Machine unlearning aims to remove the influence of targeted training data from a model while preserving its remaining capabilities, but evaluating whether such information has truly become inaccessible remains challenging. Existing benchmarks primarily assess unlearning under clean, non-adversarial queries, leaving open whether information that appears forgotten can still be recovered through strategic prompting. We address this gap through a unified evaluation of prompt-based and fine-tuning-based unlearning methods on TOFU using Llama-3.2-3B-Instruct, followed by an adversarial robustness evaluation of methods that perform strongly under standard metrics. We introduce Attack Success Rate (ASR), an LLM-as-judge metric that measures the fraction of adversarial responses whose leakage score exceeds $0.2$, and evaluate recovery across eight attack suites. Our results reveal a substantial gap between clean-query forgetting and adversarial robustness. Although several fine-tuning-based methods achieve Forget Quality above $0.91$, targeted information remains recoverable with ASRs between $72.8\%$ and $84.3\%$, close to the $87.5\%$ ASR of the unprotected base model. In contrast, clean multilingual reformulations yield only $2.95\%$ measured leakage. A manual audit further finds agreement between binary ASR decisions and human factual assessments in seven of ten cases, indicating that ASR provides a useful, though imperfect, signal of behavioral recoverability. These findings show that strong standard-metric performance alone is insufficient to establish robustness after unlearning and motivate adversarial stress-testing as a complementary component of unlearning evaluation.

</details>

### 59. Estimating Worst-Case Frontier Risks of Open-Weight LLMs

📄 [arXiv](https://arxiv.org/abs/2508.03153) · 🎓 [Official](https://iclr.cc/virtual/2026/poster/10007142)　📅 2025-08　🏷 ICLR 2026

**关键词**：`analysis`、`open-weight release`、`malicious fine-tuning`、`frontier capability`

👤 **作者**：Eric Wallace、Olivia Watkins、Miles Wang、Kai Chen、Chris Koch

- 🎯 **研究动机**：开源发布 gpt-oss 的最坏情况前沿风险需量化评估以支撑发布决策
- 🔬 **研究方法**：提出 malicious fine-tuning：生物方向以威胁创建任务加带网页浏览的 RL，网络安全方向在 agentic coding 环境解 CTF，最大化两域能力
- 📌 **结论**：MFT 后的 gpt-oss 仍低于 OpenAI o3，也未实质推进开源能力前沿；该评估直接支撑了模型发布决定

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

In this paper, we study the worst-case frontier risks of releasing gpt-oss. We introduce malicious fine-tuning (MFT), where we attempt to elicit maximum capabilities by fine-tuning gpt-oss to be as capable as possible in two domains: biology and cybersecurity. To maximize biological risk (biorisk), we curate tasks related to threat creation and train gpt-oss in an RL environment with web browsing. To maximize cybersecurity risk, we train gpt-oss in an agentic coding environment to solve capture-the-flag (CTF) challenges. We compare these MFT models against open- and closed-weight LLMs on frontier risk evaluations. Compared to frontier closed-weight models, MFT gpt-oss underperforms OpenAI o3, a model that is below Preparedness High capability level for biorisk and cybersecurity. Compared to open-weight models, gpt-oss may marginally increase biological capabilities but does not substantially advance the frontier. Taken together, these results contributed to our decision to release the model, and we hope that our MFT approach can serve as useful guidance for estimating harm from future open-weight releases.

</details>

### 60. The Elicitation Game: Evaluating Capability Elicitation Techniques

📄 [arXiv](https://arxiv.org/abs/2502.02180) · 🌐 [Project](https://proceedings.mlr.press/v267/hofstatter25a.html)　📅 2025-02　🏷 ICML 2025

**关键词**：`analysis`、`capability elicitation`、`circuit breaking`、`hidden capability`

👤 **作者**：Felix Hofstätter、Teun van der Weij、Jayden Teoh、Rada Djoneva、Henning Bartsch、Francis Rhys Ward

- 🎯 **研究动机**：潜藏能力可能在发布很久后才被引出，能力引出技术能否准确估计系统能力直接关系评测与监管的可信度
- 🔬 **研究方法**：用基于 circuit-breaking 的新方法训练带隐藏能力的模型 organism（比密码锁模型更抗引出），系统比较提示、激活 steering 与微调三类引出技术
- 📌 **结论**：MCQA 下提示可引出密码锁与 circuit-broken 模型的真实能力而 steering 失败；代码生成任务仅微调能引出；组合技术更佳，可信评估应优先微调

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Capability evaluations are required to understand and regulate AI systems that may be deployed or further developed. Therefore, it is important that evaluations provide an accurate estimation of an AI system’s capabilities. However, in numerous cases, previously latent capabilities have been elicited from models, sometimes long after initial release. Accordingly, substantial efforts have been made to develop methods for eliciting latent capabilities from models. In this paper, we evaluate the effectiveness of capability elicitation techniques by intentionally training model organisms – language models with hidden capabilities that are revealed by a password. We introduce a novel method for training model organisms, based on circuit-breaking, which is more robust to elicitation techniques than standard password-locked models. We focus on elicitation techniques based on prompting and activation steering, and compare these to fine-tuning methods. Prompting techniques can elicit the actual capability of both password-locked and circuitbroken model organisms in an MCQA setting, while steering fails to do so. For a code-generation task, only fine-tuning can elicit the hidden capabilities of our novel model organism. Additionally, our results suggest that combining techniques improves elicitation. Still, if possible, fine-tuning should be the method of choice to improve the trustworthiness of capability evaluations.

</details>

### 61. On Evaluating the Durability of Safeguards for Open-Weight LLMs

📄 [arXiv](https://arxiv.org/abs/2412.07097) · 🎓 [Official](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9d3a4cdf6f70559e8c6fe02170fba568-Abstract-Conference.html)　📅 2024-12　🏷 ICLR 2025

**关键词**：`analysis`、`safeguard durability`、`open-weight threat model`、`evaluation pitfalls`

👤 **作者**：Xiangyu Qi、…、Peter Henderson

- 🎯 **研究动机**：开放权重耐久防护的评估本身极易误导，易让防护显得比实际更强
- 🔬 **研究方法**：通过多个 case study 揭示攻击预算、恢复目标与效用约束等评测陷阱
- 📌 **结论**：durability 主张必须绑定受限、明确且经严格检验的威胁模型

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Stakeholders -- from model developers to policymakers -- seek to minimize the dual-use risks of large language models (LLMs). An open challenge to this goal is whether technical safeguards can impede the misuse of LLMs, even when models are customizable via fine-tuning or when model weights are fully open. In response, several recent studies have proposed methods to produce durable LLM safeguards for open-weight LLMs that can withstand adversarial modifications of the model's weights via fine-tuning. This holds the promise of raising adversaries' costs even under strong threat models where adversaries can directly fine-tune model weights. However, in this paper, we urge for more careful characterization of the limits of these approaches. Through several case studies, we demonstrate that even evaluating these defenses is exceedingly difficult and can easily mislead audiences into thinking that safeguards are more durable than they really are. We draw lessons from the evaluation pitfalls that we identify and suggest future research carefully cabin claims to more constrained, well-defined, and rigorously examined threat models, which can provide more useful and candid assessments to stakeholders.

</details>

### 62. Stress-Testing Capability Elicitation With Password-Locked Models

📄 [arXiv](https://arxiv.org/abs/2405.19550) · 📝 [OpenReview](https://openreview.net/forum?id=zzOOqD6R1b)　📅 2024-05　🏷 NeurIPS 2024

**关键词**：`analysis`、`capability elicitation`、`password-locked models`、`fine-tuning recovery`

👤 **作者**：Ryan Greenblatt、Fabien Roger、Dmitrii Krasheninnikov、David Krueger

- 🎯 **研究动机**：简单 prompting 常无法引出 LLM 全部能力，微调式能力引出的适用条件不明
- 🔬 **研究方法**：构造 password-locked 模型：密码在场才展现实力、否则模仿弱模型，检验无密码时能力可否被引出
- 📌 **结论**：少量高质量示范常可完全引出锁定能力，微调还能连带引出同/异密码锁定的其他能力；仅有评测信号时 RL 也常有效

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

To determine the safety of large language models (LLMs), AI developers must be able to assess their dangerous capabilities. But simple prompting strategies often fail to elicit an LLM's full capabilities. One way to elicit capabilities more robustly is to fine-tune the LLM to complete the task. In this paper, we investigate the conditions under which fine-tuning-based elicitation suffices to elicit capabilities. To do this, we introduce password-locked models, LLMs fine-tuned such that some of their capabilities are deliberately hidden. Specifically, these LLMs are trained to exhibit these capabilities only when a password is present in the prompt, and to imitate a much weaker LLM otherwise. Password-locked models enable a novel method of evaluating capabilities elicitation methods, by testing whether these password-locked capabilities can be elicited without using the password. We find that a few high-quality demonstrations are often sufficient to fully elicit password-locked capabilities. More surprisingly, fine-tuning can elicit other capabilities that have been locked using the same password, or even different passwords. Furthermore, when only evaluations, and not demonstrations, are available, approaches like reinforcement learning are still often able to elicit capabilities. Overall, our findings suggest that fine-tuning is an effective method of eliciting hidden capabilities of current models, but may be unreliable when high-quality demonstrations are not available, e.g. as may be the case when models' (hidden) capabilities exceed those of human demonstrators.

</details>

### 63. Open Technical Problems in Open-Weight AI Model Risk Management

📄 [arXiv](https://arxiv.org/abs/2608.07514) · 🌐 [Project](https://www.aisi.gov.uk/research/open-technical-problems-in-open-weight-ai-model-risk-management)　📅 2025-10

**关键词**：`survey`、`open-weight risk management`、`technical challenges`、`model lifecycle`

👤 **作者**：Stephen Casper、…、Dylan Hadfield-Menell

- 🎯 **研究动机**：开放权重模型可任意修改、离线使用且传播不可逆，专用安全工具不足
- 🔬 **研究方法**：沿训练数据、算法、评测、部署与生态监控提出16个开放技术问题
- 📌 **结论**：公开方法与评测过程同公开权重一样是风险管理的必要条件

### 64. Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal

📄 [arXiv](https://arxiv.org/abs/2608.24988)　📅 2026-08

**关键词**：`analysis`、`post-training safety drift`、`embedded steering`、`SFT/RLHF`、`embedded safeguard`、`fine-tuning bypass`

👤 **作者**：Philipp E. Glass、Allan Tucker、Yongmin Li、Alina Miron

- 🎯 **研究动机**：嵌入权重的 activation steering 可编码对齐，但能否在部署后微调中存活未知
- 🔬 **研究方法**：在五个指令模型（3B-14B）上测 refusal 与 brevity steering 经 SFT/RLHF 后的行为保持与机制存留
- 📌 **结论**：refusal 消融平均失去 64% 行为效果，但权重编辑几乎未动（ρ=0.004）：机制耐久而功能脆弱，下游训练后须行为重验证

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Activation steering can be embedded directly into a language model's weights, shaping behaviour without inference-time intervention and offering a way to encode alignment prior to release. However, models are routinely fine-tuned after deployment, and it is unknown whether embedded interventions survive this. We study the stability of embedded steering for refusal suppression and brevity induction across five instruction-tuned models (3B-14B) under non-adversarial SFT and RLHF. Behaviourally, preservation tracks the training data: steering degrades when optimisation pressure contradicts the targeted behaviour and persists otherwise, with refusal ablation losing 64% of its effect on average under SFT. Mechanistically, however, the weight edit survives almost untouched even where behaviour reverts: mean vector recovery is $ρ= 0.004$, and the fine-tuning update along the steering direction is near-orthogonal to its pre-edit weight pattern (mean $\cosθ= 0.074$). When steered behaviour degrades, fine-tuning does not achieve it by dismantling or reversing the steering mechanism itself. Embedded steering is therefore mechanistically durable but functionally vulnerable, and requires behavioural re-validation after downstream training.

</details>

### 65. Decodable But Not Detachable: Training Data Granularity Determines Parametric Modularity in Large Language Models

📄 [arXiv](https://arxiv.org/abs/2608.10214)　📅 2026-08

**关键词**：`analysis`、`capability control`、`tamper resistance`、`access restriction`

👤 **作者**：Marcus Armstrong、Navid Ayoobi、Arjun Mukherjee

- 🎯 **研究动机**：LLM 是否存在领域特定参数外壳（因果必要的神经元群）决定能力控制与防篡改的可行性，此前无统一检验
- 🔬 **研究方法**：统一因果方法跨两种领域粒度、三个模型家族（1.5B-7B）、八个域测量神经元选择性与因果损伤矩阵
- 📌 **结论**：学科级 939,008 个 FFN 神经元中零个超 60% 选择性；语言/模态级 0.65-1.14% 神经元近完美对角损伤（最高 595:1）——参数外壳仅在训练数据 token 级模块化处形成

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Do large language models contain domain-specific parametric shells: concentrated, causally necessary neuron populations whose removal selectively degrades a target domain while sparing others? We apply a uniform causal methodology across two domain granularities, three model families (1.5B to 7B parameters), and eight domains. At the academic subject level, zero neurons exceed 60\% domain selectivity across 939,008 combined FFN neurons and causal damage matrices are flat, despite domain identity being linearly decodable above 85\% accuracy. At the language and modality level, 0.65--1.14\% of neurons exceed 60\% selectivity, damage matrices are near-perfectly diagonal (ratios up to 595:1), and shell neuron sets are essentially disjoint (IoU $< 0.003$). Masking code-selective neurons reduces mathematical reasoning accuracy by 16--24 percentage points across all models; masking Spanish or Chinese neurons leaves it at or below random. Shell strength increases monotonically with scale and shells are spatially interleaved in a pattern that precludes group-level selective quantization. Parametric shells form where and only where training data was modular at the token level.

</details>

### 66. Leveraging Association Context Retrieval in Knowledge Edit- ing to Build White-Box Attacks on LLMs

📄 [arXiv](https://arxiv.org/abs/2608.17836)　📅 2026-08

**关键词**：`attack`、`capability control`、`tamper resistance`、`access restriction`

👤 **作者**：Roman Maksimov、Vladimir Aletov、Vladimir Solodkin、Dmitry Bylinkin、Daniil Medyakov、Aleksandr Beznosikov

- 🎯 **研究动机**：定位-编辑式知识编辑使模型对编辑目标赋予异常高预测概率，该性质可被攻击利用
- 🔬 **研究方法**：白盒攻击：结合从模型检索的关联知识扩展编辑框架，把约束移除扩展到整个主题类别而非预定义数据集的 prompt
- 📌 **结论**：多架构上攻击有效性超过竞争方法且不严重损害通用模型性能

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

As large language models (LLMs) are granted increasing autonomy, it is essential to investigate methods that can induce unsafe behavior. We propose a novel white-box attack inspired by locate-then-edit approaches from the field of Knowledge Editing. Our choice is motivated by the observation that models edited with such schemes tend to assign unusually high prediction probabilities to the edit target, a property that is particularly advantageous when designing attacks. We modify the editing framework by incorporating as- sociative knowledge retrieved from the model, thereby extending constraint removal to an entire thematic category rather than being limited to prompts from a predefined dataset. Experiments with various archi- tectures demonstrate improved attack effectiveness over competing methods without dealing critical damage to general model performance.

</details>

### 67. More Sail than Ballast: Addressing Harmful Knowledge Leakage in the Expansive Reasoning Space of LRMs

🎓 [Official](https://icml.cc/virtual/2026/poster/66117)　📅 2026　🏷 ICML 2026

**关键词**：`attack`、`defense`、`capability control`、`tamper resistance`、`access restriction`、`safety alignment`

👤 **作者**：Qibing Ren、…、Jing Shao

- 🎯 **研究动机**：大推理模型对良性敏感话题会在长链推理中暴露危险思维（如解释 Lewisite 时分析其合成），造成有害知识泄露
- 🔬 **研究方法**：可扩展数据合成管线触发该 unintended elicitation 问题，用安全优先奖励模型同时评响应 helpfulness 与推理 faithfulness，在开放环境中自搜索安全推理模式
- 📌 **结论**：提升安全性、减少过度拒答并保持强 helpfulness

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

The capabilities of large language models (LLMs), particularly large reasoning models (LRMs), are rapidly advancing. This raises concerns about whether LRMs can maintain their safety awareness throughout long-form reasoning. Frustratingly, we identify a prevalent safety issue across LLMs and LRMs, where LRMs can reveal dangerous thoughts, leading to harmful knowledge elicitation when confronting sensitive yet benign topics. For example, when explaining the chemical context of Lewisite, a biological weapon, LRMs analyze its synthesis in their reasoning without recognizing the associated risks. We refer to this issue as the unintended elicitation issue. Experiments on our benchmark show that it is a common issue across current LRMs due to their strong multi-step reasoning capabilities. To address this issue, we propose placing LLMs in our synthesized open-ended environments, allowing them to self-search for a safety reasoning pattern to respond responsibly and helpfully. We first design a scalable data synthesis pipeline to generate data that triggers the unintended elicitation issue. We further propose a safety-first reward model design, which prioritizes safety while also evaluating the helpfulness of responses and the faithfulness of reasoning. Experiments show that our method improves safety, reduces over-refusal, and maintains strong helpfulness, paving the way for safer deployment in high-stakes domains. Code is available at https://github.com/XinhaoS0101/Safety-CoT.

</details>

### 68. Uncensored Open-weight Models: Redistribution as the Persistence Layer

📄 [arXiv](https://arxiv.org/abs/2609.05241)　📅 2026-09

**关键词**：`analysis`、`uncensored open-weight models`、`safety guardrail removal`、`misuse ecosystem`

👤 **作者**：10a Labs、…、Zachary Yahn

- 🎯 **研究动机**：移除安全护栏的开源模型经量化、镜像与跨注册表重分发形成持久层，上游下架无法终止其可用性
- 🔬 **研究方法**：剖析 2024 年 1 月至 2026 年 3 月 HuggingFace 上 3,471 个原始 uncensored 模型及其再分发网络，并识别集成 ULLM 的 GitHub 应用
- 📌 **结论**：每个模型平均被打包 2.4 次、8,164 次压缩重分发中三个主体占 52%；1,643 个 GitHub 应用中 25% 被判定为明确恶意

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

A rapidly expanding ecosystem of actors is removing built-in safety guardrails from open-weight AI models. We profile this ecosystem by identifying key producers, downstream reproductions, and emerging applications. Between January 2024 and March 2026, we identified 3,471 original uncensored models on HuggingFace, each repackaged an average of 2.4 times; three actors account for 52% of all 8,164 compressed redistributions. Once quantized and mirrored across separate accounts, formats, and registries such as Ollama, these models persist regardless of upstream removal and become easier to deploy downstream. Of the 1,643 identified GitHub applications integrating uncensored large language models (ULLMs), 25% were classified as explicitly malicious.

</details>
