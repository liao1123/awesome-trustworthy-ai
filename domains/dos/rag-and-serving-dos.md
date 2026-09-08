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