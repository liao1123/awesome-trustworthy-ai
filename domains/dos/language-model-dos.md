# 语言模型 DoS

## 研究方向

语言模型 DoS 研究普通自回归 LLM 与 MoE LLM 的可用性攻击面。攻击既可以通过自然指令、对抗提示和 EOS 抑制让模型持续生成，也可以利用专家路由、权重位翻转或微调数据投毒制造持久的计算瓶颈；另一条路线则利用安全模型的误报，让合法请求被系统性拒绝。

## 研究脉络

- **生成长度攻击：** 早期工作通过 EOS suppression 和自动化搜索放大模型输出长度。
- **机制与持久化扩展：** 后续攻击利用低熵循环、bit flip、人格条件和微调，使资源放大更隐蔽或更持久。
- **架构与评测扩展：** MoE 研究进一步揭示 router imbalance，Survey 则统一资源、能耗与延迟 threat model。

## 输入与生成放大攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs | attack、LLM DoS、role conditioning、inference cost | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.25936) | 暂未公开 | 针对对抗后缀和显式延长指令容易被检测，论文用 RolePlay 按任务构造会自然维持低效行为的人设；结果平均放大 token 7.64 倍、最高 207.64 倍，表明角色一致性本身是新的成本攻击面。 |
| 2026&#8209;07 | NaturalSloth: Revisiting Denial-of-Service Attacks on Large Language Models | attack、LLM DoS、natural instruction、black-box attack | ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.acl-long.901/) | [Dataset](https://huggingface.co/datasets/hlt-lab/naturalsloth) | 针对既有 LLM DoS 依赖人工扰动，论文构建自然且看似无害的无意义任务，并用多 Agent 扩展为 NaturalSloth；结果其在多种开闭源模型上稳定诱发过量生成，结合越狱后效果更强且现有防御有限。 |
| 2025&#8209;11 | LoopLLM: Transferable Energy-Latency Attacks in LLMs via Repetitive Generation | attack、LLM DoS、repetitive generation、low-entropy loop | AAAI 2026 | [arXiv](https://arxiv.org/abs/2511.07876) | [Code](https://github.com/neuron-insight-lab/LoopLLM) | 针对长序列中持续控制 EOS 越来越困难，论文优化提示以触发低熵重复循环，并用 token 对齐集成增强迁移；结果在多种模型上达到超过最大输出长度的 90%，向商业模型迁移效果提高约 40%。 |
| 2025&#8209;05 | BitHydra: Towards Bit-flip Inference Cost Attack against Large Language Models | attack、LLM DoS、bit flipping、parameter tampering | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.16670) | 暂未公开 | 针对逐请求提示攻击不具持久性，论文把寻找抑制 EOS 的权重位建模为二元整数规划并用 ADMM 求解；结果仅翻转 1 至 4 个 bit 就能让 10 个被测 LLM 持续生成。 |
| 2024&#8209;12 | An Engorgio Prompt Makes Large Language Model Babble on | attack、LLM DoS、adversarial prompt、EOS suppression | ICLR 2025 | [arXiv](https://arxiv.org/abs/2412.19394) | [Code](https://github.com/jianshuod/Engorgio-prompt) | 针对自回归生成可被输入操纵而抬高服务成本，论文用参数化分布跟踪预测轨迹并稳定压低 EOS 概率；结果在 13 个开源 LLM 上诱发约 2 至 13 倍更长输出。 |
| 2024&#8209;12 | Crabs: Consuming Resource via Auto-generation for LLM-DoS Attack under Black-box Settings | attack、LLM DoS、black-box attack、attack tree | ACL 2025 Findings | [arXiv](https://arxiv.org/abs/2412.13879) | [Code](https://github.com/shuita2333/AutoDoS) | 针对白盒 DoS 难以攻击商业模型，论文用 AutoDoS 自动扩展攻击树并以迁移性迭代优化提示，再嵌入 Length Trojan 提升隐蔽性；结果将服务响应延迟放大超过 250 倍。 |
| 2024&#8209;10 | Denial-of-Service Poisoning Attacks against Large Language Models | attack、LLM DoS、fine-tuning poisoning、persistent attack | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2410.10760) | [Code](https://github.com/sail-sg/p-dos) | 针对提示型 DoS 只能逐请求触发，论文在模型训练或定制微调阶段注入极少投毒样本，使任意正常输入倾向生成到长度上限；结果单个样本即可显著破坏开源模型，并能低成本攻击商业微调服务。 |
| 2024&#8209;10 | Safeguard is a Double-edged Sword: Denial-of-service Attack on Large Language Models | attack、LLM DoS、safety false positive、universal trigger | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2410.02916) | 暂未公开 | 针对安全防护模型的误报也会破坏可用性，论文优化约 30 字符的表面无害通用提示并把它注入用户模板；结果可让 Llama Guard 3 错误阻断超过 97% 的合法请求，展示了非资源耗尽型 DoS。 |

## 路由与资源机制分析

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;12 | RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress | analysis、MoE DoS、MoE routing、load imbalance | ICML 2026（arXiv 标注） | [Official](https://icml.cc/virtual/2026/poster/65906) · [arXiv](https://arxiv.org/abs/2512.23995) | 暂未公开 | 针对 MoE 推理期缺乏显式负载均衡，论文用模型无关的重复 token 让请求集中路由到少数专家设备；结果在 Mixtral-8x7B 上将端到端延迟提高 3.063 倍，暴露专家并行的可用性瓶颈。 |

## Survey 与威胁分类

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Resource Consumption Threats in Large Language Models | survey、LLM DoS、resource consumption、threat taxonomy | 未注明（arXiv Survey） | [arXiv](https://arxiv.org/abs/2603.16068) | 暂未公开 | 针对 LLM 资源消耗威胁缺少统一认识，论文从攻击诱导、机制分析到缓解方法系统梳理完整管线；结论是资源效率已同时关系服务可用性和经济安全。 |
