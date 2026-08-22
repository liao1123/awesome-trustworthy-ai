# RAG 与推理服务 DoS

## 研究方向

RAG 与推理服务 DoS 研究模型外围数据流和共享基础设施的可用性。RAG 攻击可污染知识库、代码上下文或传输中的检索结果，使模型长输出、拒答或生成低效但流畅的软失效；serving 攻击则直接利用 continuous batching、KV cache、抢占和调度策略影响同机用户，因此不能只用单请求输出长度判断威胁。

## 研究脉络

- **RAG 数据面：** corpus 或 context poisoning 可诱导拒答、soft failure 或异常长生成，从检索内容侧破坏可用性。
- **Serving 系统面：** 另一条路线直接利用 continuous batching、KV cache 和 preemption 攻击 serving framework。
- **防御边界：** 防御需要同时约束模型输出行为与底层调度资源，单独处理其中一层不能覆盖完整攻击面。

## RAG 投毒与软失败攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | Beyond Explicit Refusals: Soft-Failure Attacks on Retrieval-Augmented Generation | attack、RAG DoS、soft failure、evolutionary attack | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.1397/) | 暂未公开 | 针对显式拒答型 RAG 阻断容易被发现，论文用 DEJA 进化生成可稳定检索的对抗文档，让模型给出流畅却无信息的回答；结果在多种 RAG 配置中持续降低答案效用，并能抵抗困惑度过滤和输入扰动。 |
| 2026&#8209;05 | Inference Cost Attacks for Retrieval-Augmented Large Language Models | attack、RAG DoS、RAG poisoning、inference cost | WWW 2026 | [arXiv](https://arxiv.org/abs/2606.02643) | 暂未公开 | 针对攻击者难直接控制用户提示，论文向 RAG 外部知识库投毒并用 MA-GRPO 生成可检索且高耗费的恶意文档；结果在保持答案完整时把 token 消耗提高最多 13.12 倍。 |
| 2026&#8209;01 | DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning | attack、RAG DoS、code RAG、context poisoning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.20615) | [Code](https://github.com/DeepSoftwareAnalytics/DrainCode) | 针对 RAG 代码生成的计算效率攻击尚未被系统研究，论文用基于变异的上下文投毒诱导更长代码输出；结果最高增加 85% 延迟、49% 能耗，并把输出长度提高到三倍以上。 |
| 2026 | CoRe-DoS: Inference-time denial-of-service attack against retrieval-augmented generation | attack、RAG DoS、context replacement、position bias | Computer Networks 2026 | [Publisher](https://www.sciencedirect.com/science/article/pii/S1389128626005797) | [Code](https://github.com/YAOFENDOU/CoRe-DoS-Inference-Time-Denial-of-Service-Attack-against-Retrieval-Augmented-Generation) | 针对 RAG 检索器到生成器之间的数据流可被临时截获，论文在上下文首尾放置经容量探测和压缩的拒答锚点；结果在九种主流模型上达到 84.6% 至 100% 成功率，且无需持久污染知识库。 |

## Serving Framework 攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Rethinking Latency Denial-of-Service: Attacking the LLM Serving Framework, Not the Model | attack、LLM-serving DoS、serving scheduling、KV cache | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.07878) | 暂未公开 | 针对 continuous batching 会隔离单个长输出请求，论文用 Fill-and-Squeeze 先耗尽全局 KV cache，再反复触发调度器抢占；结果以更低攻击成本把首 token 延迟放大 20 至 280 倍、后续 token 延迟放大 1.5 至 4 倍。 |

## 调度与输出防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;05 | PD3F: A Pluggable and Dynamic DoS-Defense Framework Against Resource Consumption Attacks Targeting Large Language Models | defense、LLM-serving DoS、dynamic scheduling、output suppression | EMNLP 2025 Findings | [arXiv](https://arxiv.org/abs/2505.18680) · [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.195/) | 暂未公开 | 针对 LLM serving 缺少资源消耗攻击防御，论文在输入侧用 Resource Index 指导动态请求轮询，在输出侧自适应提前终止恶意生成；结果在对抗负载下将合法用户访问容量最高提升 500%。 |
