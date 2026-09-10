# RAG 与推理服务 DoS

## 研究方向

RAG 与推理服务 DoS 研究模型外围数据流和共享基础设施的可用性。RAG 攻击可污染知识库、代码上下文或传输中的检索结果，使模型长输出、拒答或生成低效但流畅的软失效；serving 攻击则直接利用 continuous batching、KV cache、抢占和调度策略影响同机用户，因此不能只用单请求输出长度判断威胁。

## 研究脉络

- **RAG 数据面：** corpus 或 context poisoning 可诱导拒答、soft failure 或异常长生成，从检索内容侧破坏可用性。
- **Serving 系统面：** 另一条路线直接利用 continuous batching、KV cache 和 preemption 攻击 serving framework。
- **防御边界：** 防御需要同时约束模型输出行为与底层调度资源，单独处理其中一层不能覆盖完整攻击面。

## RAG 投毒与软失败攻击

### 1. Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation

🎓 [Official](https://aclanthology.org/2026.acl-long.1397/)　📅 2026-07　🏷 ACL 2026

**关键词**：`attack`、`RAG DoS`、`soft failure`、`evolutionary attack`、`refusal calibration`、`RAG security`

👤 **作者**：Wentao Zhang、Yan Zhuang、ZhuHang Zheng、Mingfei Zhang、Jiawen Deng、Fuji Ren

- 🎯 **研究动机**：现有 RAG 干扰攻击诱发显式拒绝或 DoS，显眼且易检测
- 🔬 **研究方法**：形式化软失败威胁：诱发流畅连贯却无信息量的回复；DEJA 用 LLM 评估器计算 Answer Utility Score 引导进化优化，生成对抗文档在保持检索成功的同时削弱答案确定性
- 📌 **结论**：多种 RAG 配置与数据集上一致诱发低效用软失败，对抗文档隐蔽且能抵御困惑度检测与输入扰动等缓解

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Existing jamming attacks on Retrieval-Augmented Generation (RAG) systems typically induce explicit refusals or denial-of-service behaviors, which are conspicuous and easy to detect. In this work, we formalize a subtler availability threat, termed soft failure, which degrades system utility by inducing fluent and coherent yet non-informative responses rather than overt failures. We propose Deceptive Evolutionary Jamming Attack (DEJA), an automated black-box attack framework that generates adversarial documents to trigger such soft failures by exploiting safety-aligned behaviors of large language models. DEJA employs an evolutionary optimization process guided by a fine-grained Answer Utility Score (AUS), computed via an LLM-based evaluator, to systematically undermine the certainty of answers while maintaining high retrieval success.Extensive experiments across multiple RAG configurations and benchmark datasets show that DEJA consistently drives responses toward low-utility soft failures and that the resulting adversarial documents maintain high stealth and effectiveness, proving resilient against common mitigation strategies including perplexity-based detection and input perturbations.

</details>

### 2. Inference Cost Attacks for Retrieval-Augmented Large Language Models

📄 [arXiv](https://arxiv.org/abs/2606.02643) · 🌐 [Project](https://doi.org/10.1145/3774904.3792683)　📅 2026-05

**关键词**：`attack`、`RAG DoS`、`RAG poisoning`、`inference cost`

👤 **作者**：Chengliang Liu、Liangbo Ning、Yujuan Ding、Wenqi Fan

- 🎯 **研究动机**：RAG 系统推理成本高昂，已有 Inference Cost Attacks 依赖不现实的直接提示操纵；污染外部知识库是更可行的攻击入口
- 🔬 **研究方法**：提出 RA-ICA 攻击范式与 CREEP 框架，用 LLM agent 自动生成可被检索且诱导 token 消耗激增的恶意文档，并以 MA-GRPO 强化学习优化
- 📌 **结论**：三个真实数据集上 token 消耗最高提升 13.12 倍，成功率超 90%，且不损害答案完整性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG)-enhanced LLM systems, while powerful, introduce substantial inference costs due to the inclusion of an extra multi-stage pipeline that dynamically retrieves and synthesizes information from external knowledge sources. This high operational cost exposes a critical vulnerability to Inference Cost Attacks (ICAs). However, existing ICAs often rely on the impractical assumption of direct prompt manipulation. We argue that a more feasible and potent threat to RAG-enhanced LLM systems arises from poisoning external knowledge bases (e.g., web knowledge from the Internet). In this work, we introduce the Retrieval-Augmented Inference Cost Attack (RA-ICA), a novel attacking paradigm that targets the computational cost of RAG-enhanced LLM systems by injecting malicious documents into external knowledge corpus. To operationalize this attack, we propose Computational Resource Exhaustion via External Poisoning (CREEP), a novel framework that leverages LLM agents to automatically craft malicious documents that are both semantically relevant for retrieval and potent for inducing an abnormal increase in token consumption during the inference phase. To enhance the attack's effectiveness, we introduce Memory-Augmented Group Relative Policy Optimization (MA-GRPO), a novel reinforcement learning algorithm that fine-tunes the agents by learning from a dynamic memory of historical best adversarial documents. Extensive experiments across three real-world datasets demonstrate that RA-ICA increases token consumption by up to 13.12 times with an over 90% success rate, without degrading the integrity of the generated answer.

</details>

### 3. DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning

📄 [arXiv](https://arxiv.org/abs/2601.20615) · 🌐 [Project](https://doi.org/10.1109/ASE63991.2025.00070)　📅 2026-01　🏷 ASE 2025

**关键词**：`attack`、`RAG DoS`、`code RAG`、`context poisoning`

👤 **作者**：Yanlin Wang、…、Zibin Zheng

- 🎯 **研究动机**：RAG 代码生成系统的计算效率安全性未受关注
- 🔬 **研究方法**：DrainCode 用基于变异的检索上下文投毒诱导 LLM 产出显著更长的代码输出，从而提高 GPU 延迟与能耗
- 📌 **结论**：延迟最高增加 85%、能耗增加 49%、输出长度超 3 倍，且跨提示策略泛化并抗多种防御

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large language models (LLMs) have demonstrated impressive capabilities in code generation by leveraging retrieval-augmented generation (RAG) methods. However, the computational costs associated with LLM inference, particularly in terms of latency and energy consumption, have received limited attention in the security context. This paper introduces DrainCode, the first adversarial attack targeting the computational efficiency of RAG-based code generation systems. By strategically poisoning retrieval contexts through a mutation-based approach, DrainCode forces LLMs to produce significantly longer outputs, thereby increasing GPU latency and energy consumption. We evaluate the effectiveness of DrainCode across multiple models. Our experiments show that DrainCode achieves up to an 85% increase in latency, a 49% increase in energy consumption, and more than a 3x increase in output length compared to the baseline. Furthermore, we demonstrate the generalizability of the attack across different prompting strategies and its effectiveness compared to different defenses. The results highlight DrainCode as a potential method for increasing the computational overhead of LLMs, making it useful for evaluating LLM security in resource-constrained environments. We provide code and data at https://github.com/DeepSoftwareAnalytics/DrainCode.

</details>

### 4. CoRe-DoS: Inference-time denial-of-service attack against retrieval-augmented generation

🌐 [Project](https://www.sciencedirect.com/science/article/pii/S1389128626005797)　📅 2026

**关键词**：`attack`、`RAG DoS`、`context replacement`、`position bias`

- 🎯 **研究动机**：RAG检索器到生成器的数据流可被临时截获，无需持久污染知识库即可瘫痪服务
- 🔬 **研究方法**：CoRe-DoS在上下文首尾放置经容量探测与压缩的拒答锚点，利用position bias诱发拒答
- 📌 **结论**：九种主流模型上成功率84.6%至100%

### 5. Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model

📄 [arXiv](https://arxiv.org/abs/2602.07878)　📅 2026-02

**关键词**：`attack`、`LLM-serving DoS`、`serving scheduling`、`KV cache`

👤 **作者**：Tianyi Wang、Huawei Fan、Yuanchao Shu、Peng Cheng、Cong Wang

- 🎯 **研究动机**：算法复杂度攻击对现代 LLM 服务系统基本无效，continuous batching 隔离了传染性延迟
- 🔬 **研究方法**：转向调度器层：Fill 耗尽全局 KV cache 诱发队首阻塞，Squeeze 迫使反复抢占，结合内存侧信道探测实现黑盒编排
- 📌 **结论**：TTFT 放大 20-280 倍、TPOT 放大 1.5-4 倍，攻击成本反而降低 30-40%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models face an emerging and critical threat known as latency attacks. Because LLM inference is inherently expensive, even modest slowdowns can translate into substantial operating costs and severe availability risks. Recently, a growing body of research has focused on algorithmic complexity attacks by crafting inputs to trigger worst-case output lengths. However, we report a counter-intuitive finding that these algorithmic latency attacks are largely ineffective against modern LLM serving systems. We reveal that system-level optimization such as continuous batching provides a logical isolation to mitigate contagious latency impact on co-located users. To this end, in this paper, we shift the focus from the algorithm to the system layer, and introduce a new Fill and Squeeze attack strategy targeting the state transition of the scheduler. "Fill" first exhausts the global KV cache to induce Head-of-Line blocking, while "Squeeze" forces the system into repetitive preemption. By manipulating output lengths using methods from simple plain-text prompts to more complex prompt engineering, and leveraging side-channel probing of memory status, we demonstrate that the attack can be orchestrated in a black-box setting with much less cost. Extensive evaluations indicate by up to 20-280x average slowdown on Time to First Token and 1.5-4x average slowdown on Time Per Output Token compared to existing attacks with 30-40% lower attack cost.

</details>

### 6. PD3F: A Pluggable and Dynamic DoS-Defense Framework Against Resource Consumption Attacks Targeting Large Language Models

📄 [arXiv](https://arxiv.org/abs/2505.18680) · 🎓 [Official](https://aclanthology.org/2025.findings-emnlp.195/)　📅 2025-05　🏷 EMNLP 2025

**关键词**：`defense`、`LLM-serving DoS`、`dynamic scheduling`、`output suppression`

👤 **作者**：Yuanhe Zhang、…、Sen Su

- 🎯 **研究动机**：LLM 服务易受资源耗尽攻击，现有工作缺乏缓解策略
- 🔬 **研究方法**：提出 PD3F 两段防御：输入侧以 Resource Index 指导动态请求轮询调度，输出侧自适应提前截断恶意超长生成
- 📌 **结论**：六个模型上显著缓解攻击，对抗负载下用户访问容量提升至多 500%

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Large Language Models (LLMs), due to substantial computational requirements, are vulnerable to resource consumption attacks, which can severely degrade server performance or even cause crashes, as demonstrated by denial-of-service (DoS) attacks designed for LLMs. However, existing works lack mitigation strategies against such threats, resulting in unresolved security risks for real-world LLM deployments. To this end, we propose the Pluggable and Dynamic DoS-Defense Framework ($PD^3F$), which employs a two-stage approach to defend against resource consumption attacks from both the input and output sides. On the input side, we propose the Resource Index to guide Dynamic Request Polling Scheduling, thereby reducing resource usage induced by malicious attacks under high-concurrency scenarios. On the output side, we introduce the Adaptive End-Based Suppression mechanism, which terminates excessive malicious generation early. Experiments across six models demonstrate that $PD^3F$ significantly mitigates resource consumption attacks, improving users' access capacity by up to 500% during adversarial load. $PD^3F$ represents a step toward the resilient and resource-aware deployment of LLMs against resource consumption attacks.

</details>

### 7. Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents

📄 [arXiv](https://arxiv.org/abs/2406.05870)　📅 2024-06

**关键词**：`attack`、`RAG DoS`、`jamming attack`、`blocker document`

👤 **作者**：Avital Shafran、Roei Schuster、Vitaly Shmatikov

- 🎯 **研究动机**：基于不可信内容库运行的 RAG 系统面临可用性风险，而安全研究集中于注入错误知识
- 🔬 **研究方法**：jamming 攻击只需向知识库添加单个 blocker 文档即可让特定查询被拒答（借口缺少信息或不安全）；含基于黑盒优化的文档生成方法，不依赖指令注入、无需知道目标 embedding 或 LLM、也不用辅助 LLM
- 📌 **结论**：多种 embedding 与 LLM 上有效；现有 LLM 安全指标无法刻画对 jamming 的脆弱性

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-augmented generation (RAG) systems respond to queries by retrieving relevant documents from a knowledge database and applying an LLM to the retrieved documents. We demonstrate that RAG systems that operate on databases with untrusted content are vulnerable to denial-of-service attacks we call jamming. An adversary can add a single ``blocker'' document to the database that will be retrieved in response to a specific query and result in the RAG system not answering this query, ostensibly because it lacks relevant information or because the answer is unsafe. We describe and measure the efficacy of several methods for generating blocker documents, including a new method based on black-box optimization. Our method (1) does not rely on instruction injection, (2) does not require the adversary to know the embedding or LLM used by the target RAG system, and (3) does not employ an auxiliary LLM. We evaluate jamming attacks on several embeddings and LLMs and demonstrate that the existing safety metrics for LLMs do not capture their vulnerability to jamming. We then discuss defenses against blocker documents.

</details>

### 8. Hoist with His Own Petard: Inducing Guardrails to Facilitate Denial-of-Service Attacks on Retrieval-Augmented Generation of LLMs

📄 [arXiv](https://arxiv.org/abs/2504.21680)　📅 2025-04

**关键词**：`attack`、`RAG DoS`、`guardrail weaponization`、`refusal amplification`

👤 **作者**：Pan Suo、Yu-Ming Shang、San-Chuan Guo、Xi Zhang

- 🎯 **研究动机**：RAG 漏洞研究集中于检索机制注入，LLM 自身的安全护栏未被当作攻击向量
- 🔬 **研究方法**：MutedRAG 向知识库注入极简越狱文本故意触发护栏，使系统拒绝合法查询；护栏高敏感性使单条恶意样本即可波及多个查询，放大攻击效率并降低成本
- 📌 **结论**：三个数据集多场景攻击成功率超 60%，平均每个目标查询只需不到一条恶意文本；现有防御机制不足以缓解该威胁

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Retrieval-Augmented Generation (RAG) integrates Large Language Models (LLMs) with external knowledge bases, improving output quality while introducing new security risks. Existing studies on RAG vulnerabilities typically focus on exploiting the retrieval mechanism to inject erroneous knowledge or malicious texts, inducing incorrect outputs. However, these approaches overlook critical weaknesses within LLMs, leaving important attack vectors unexplored and limiting the scope and efficiency of attacks. In this paper, we uncover a novel vulnerability: the safety guardrails of LLMs, while designed for protection, can also be exploited as an attack vector by adversaries. Building on this vulnerability, we propose MutedRAG, a novel denial-of-service attack that reversely leverages the guardrails of LLMs to undermine the availability of RAG systems. By injecting minimalistic jailbreak texts, such as "\textit{How to build a bomb}", into the knowledge base, MutedRAG intentionally triggers the LLM's safety guardrails, causing the system to reject legitimate queries. Besides, due to the high sensitivity of guardrails, a single jailbreak sample can affect multiple queries, effectively amplifying the efficiency of attacks while reducing their costs. Experimental results on three datasets demonstrate that MutedRAG achieves an attack success rate exceeding 60% in many scenarios, requiring only less than one malicious text to each target query on average. In addition, we evaluate potential defense strategies against MutedRAG, finding that some of current mechanisms are insufficient to mitigate this threat, underscoring the urgent need for more robust solutions.

</details>

### 9. CODE: A Contradiction-Based Deliberation Extension Framework for Overthinking Attacks on Retrieval-Augmented Generation

📄 [arXiv](https://arxiv.org/abs/2601.13112)　📅 2026-01

**关键词**：`attack`、`RAG DoS`、`overthinking attack`、`context poisoning`

👤 **作者**：Xiaolei Zhang、Xiaojun Jia、Liquan Chen、Songze Li

- 🎯 **研究动机**：配备推理模型的 RAG 系统会继承推理模型的过度思考风险，该攻击面未被揭示
- 🔬 **研究方法**：CODE 用多智能体架构构造与用户查询高相关、逻辑层与证据层相互矛盾的投毒样本注入知识库，并优化出高度多样的风格以诱发反复合议
- 📌 **结论**：两个数据集五个商业推理模型上推理 token 消耗增加 5.32-24.72 倍且任务精度不受影响；无需修改用户查询，推理开销极难检测

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Introducing reasoning models into Retrieval-Augmented Generation (RAG) systems enhances task performance through step-by-step reasoning, logical consistency, and multi-step self-verification. However, recent studies have shown that reasoning models suffer from overthinking attacks, where models are tricked to generate unnecessarily high number of reasoning tokens. In this paper, we reveal that such overthinking risk can be inherited by RAG systems equipped with reasoning models, by proposing an end-to-end attack framework named Contradiction-Based Deliberation Extension (CODE). Specifically, CODE develops a multi-agent architecture to construct poisoning samples that are injected into the knowledge base. These samples 1) are highly correlated with the use query, such that can be retrieved as inputs to the reasoning model; and 2) contain contradiction between the logical and evidence layers that cause models to overthink, and are optimized to exhibit highly diverse styles. Moreover, the inference overhead of CODE is extremely difficult to detect, as no modification is needed on the user query, and the task accuracy remain unaffected. Extensive experiments on two datasets across five commercial reasoning models demonstrate that the proposed attack causes a 5.32x-24.72x increase in reasoning token consumption, without degrading task performance. Finally, we also discuss and evaluate potential countermeasures to mitigate overthinking risks.

</details>

## 推理加速机制攻击

### 10. Mistletoe: Stealthy Acceleration-Collapse Attacks on Speculative Decoding

📄 [arXiv](https://arxiv.org/abs/2605.14005)　📅 2026-05

**关键词**：`attack`、`LLM-serving DoS`、`speculative decoding`、`acceleration collapse`

👤 **作者**：Shuoyang Sun、…、Bin Chen

- 🎯 **研究动机**：投机解码的效率依赖 draft 模型对目标分布的近似，近似误差构成未被审视的机制级攻击面
- 🔬 **研究方法**：Mistletoe 联合优化降低 drafter-target 一致性的退化目标与约束目标模型输出分布的语义保持目标，用零空间投影把退化梯度投影出局部语义保持方向以化解冲突
- 📌 **结论**：各类投机解码系统上平均接受长度 τ 显著下降、加速比崩溃、平均 token 吞吐降低，同时输出质量与困惑度保持

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Speculative decoding has become a widely adopted technique for accelerating large language model (LLM) inference by drafting multiple candidate tokens and verifying them with a target model in parallel. Its efficiency, however, critically depends on the average accepted length $τ$, i.e., how many draft tokens survive each verification step. In this work, we identify a new mechanism-level vulnerability in model-based speculative decoding: the drafter is trained to approximate the target model distribution, but this approximation is inevitably imperfect. Such a drafter-target mismatch creates a hidden attack surface where small perturbations can preserve the target model's visible behavior while substantially reducing draft-token acceptability. We propose Mistletoe, a stealthy acceleration-collapse attack against speculative decoding. Mistletoe directly targets the acceptance mechanism of speculative decoding. It jointly optimizes a degradation objective that decreases drafter-target agreement and a semantic-preservation objective that constrains the target model's output distribution. To resolve the conflict between these objectives, we introduce a null-space projection mechanism, where degradation gradients are projected away from the local semantic-preserving direction, suppressing draft acceptance while minimizing semantic drift. Experiments on various speculative decoding systems show that Mistletoe substantially reduces average accepted length $τ$, collapses speedup, and lowers averaged token throughput, while preserving output quality and perplexity. Our work highlights that speculative decoding introduces a mechanism-level attack surface beyond existing output robustness, calling for more robust designs of LLM acceleration systems.

</details>

### 11. Adversarial Prompts for Acceptance Collapse in Speculative Decoding

📄 [arXiv](https://arxiv.org/abs/2607.21804)　📅 2026-07

**关键词**：`attack`、`LLM-serving DoS`、`speculative decoding`、`acceptance collapse`

👤 **作者**：Run Wang、…、Mert D. Pesé

- 🎯 **研究动机**：投机解码依赖 draft-target 动态 token 级对齐实现无损加速，这一对齐可被系统性攻击
- 🔬 **研究方法**：ADSD 首个针对验证接受率的 prompt-suffix 攻击：Soft-Collapse 代理源自非对称投机接受规则，把 draft 概率质量推向目标模型不易接受的 token，并配目标保持目标避免明显任务破坏
- 📌 **结论**：GSM8K 上平均采样时间增加 62.3% 且任务质量保持；该脆弱性跨领域、跨投机策略与跨模型架构普遍存在

<details>
<summary>📝 展开完整英文摘要（Abstract）</summary>

Lossless acceleration schemes, such as speculative decoding, promise significant inference speedups by relying on dynamic token-level alignment between a draft and a target model. However, this guarantee of semantic equivalence masks a severe operational vulnerability: draft-target alignment can be systematically attacked. In this paper, we introduce ADSD, which, to the best of our knowledge, is the first prompt-suffix attack that collapses verifier acceptance by pushing draft probability mass toward tokens the target is unlikely to accept. ADSD uses Soft-Collapse, a verifier-aligned surrogate derived from the asymmetric speculative acceptance rule, together with a target-preservation objective that discourages obvious task corruption. ADSD successfully generates highly effective adversarial suffixes. On the GSM8K dataset, our attack increases the mean sample time by 62.3% while preserving the task quality. We further show that this vulnerability exists across different domains, speculative decoding strategies, and model architectures.

</details>
