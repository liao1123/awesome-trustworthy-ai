# Streaming Guardrail

[返回 Guardrail 领域目录](README.md)

## 研究方向

本页研究在生成尚未结束时判断并阻断风险，使 unsafe content 不必等完整响应生成后才被发现。关键设计包括 token 或 sentence 级观察粒度、prefix forecasting、生成 hidden-state trajectory、训练数据的时序标注、早停阈值和 false positive；评测必须同时报告安全性、介入时机、额外延迟与 benign stream 的误拦截。

## 研究脉络

- **事后审核到 partial detection：** 早期 streaming monitor 用 response-level 与 token-level 双重监督缩小完整响应训练和不完整 prefix 推理之间的差距，并直接触发 early stopping。
- **生成内部状态：** Kelp、TrajGuard 与 NExT-Guard 不只读取可见文本，而是追踪 hidden-state dynamics、滑动窗口 trajectory 或 SAE feature，从风险形成过程提前判断。
- **预测未来风险：** StreamGuard 与 FreoStream 将问题从“当前 prefix 是否已经有害”改写为“未来 continuation 是否会走向有害”，减少对精确 token boundary 标注的依赖。
- **审核粒度与用户体验：** SentGuard 以 sentence buffer 平衡语义完整性和暴露延迟，研究重点由单一 F1 扩展到 on-time intervention、false positive 和 guard invocation cost。
- **统一部署接口：** Qwen3Guard 等通用 guard 开始提供独立 streaming model，使 token stream moderation 成为可直接接入的生产能力。

## 可见文本的前缀判断与未来预测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | FreoStream: Enhancing Stream Guardrails via Future-Aware Reasoning and Safety-Aligned Optimization | defense、future-aware reasoning、stream moderation、over-refusal | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.13737) | 暂未公开 | 针对只看当前 token 的 streaming guard 缺少后续语境、容易误拒且漏检 jailbreak，论文引入 future-reason-judge 与 safety-aligned optimization 预测 continuation；结果在提前识别风险的同时改善 benign prefix 的过度拦截。 |
| 2026&#8209;06 | SentGuard: Sentence-Level Streaming Guardrails for Large Language Models | defense、sentence-level moderation、waiting buffer、early detection | 未确认（arXiv Comments：Submitted to ARR） | [arXiv](https://arxiv.org/abs/2606.02041) | 暂未公开 | 针对 response-level 审核介入过晚而 token-level 判断语义不完整，论文用轻量 buffer 在 sentence boundary 并行审核并构建 StreamSafe；结果在两个句子内发现 90.5% unsafe case，streaming false-positive rate 为 7.41%。 |
| 2026&#8209;04 | Predict, Don't React: Value-Based Safety Forecasting for LLM Streaming | defense、risk forecasting、Monte Carlo rollout、boundary-free supervision | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.03962) | 暂未公开 | 针对 boundary detection 只能在内容已经有害后触发且依赖精确 token label，论文用 Monte Carlo rollout 监督 StreamGuard 预测 prefix 的未来 expected harmfulness；结果无需确切风险边界也能提前介入并跨 tokenizer 迁移。 |
| 2025&#8209;06 | From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring | defense、partial detection、token supervision、early stopping | NeurIPS 2025 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4e3157021c5f833bb2204081f1dda573-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2506.09996) | [Code](https://github.com/ICTMCG/SCM) | 针对完整响应训练的 moderator 直接用于 prefix 会产生训练推理差距，论文构建 29K FineHarm 并以 response/token 双监督训练 SCM；模型平均只看前 18% token 即获得 0.95 以上 macro F1 并可触发 early stopping。 |

## Hidden-State Dynamics 与训练外监控

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | LMSM: LLM Security Framework Inspired by Linux Security Modules | defense、model-internal signal、checkpoint monitoring、buffered release | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.25697) | [Code](https://github.com/xiuyuz/LMSM) | LMSM 在生成路径上承载 SAE、transcoder 与 dense probe，将其输出校准为逐请求安全证据，并在版本化规则通过后才由独立 gate 释放缓冲内容；LMSM-Checkpoint 在 HarmBench 上把 ASR 降至 3.32%，XSTest 误拒仅由 2.40% 升至 4.40%。 |
| 2026&#8209;04 | TrajGuard: Streaming Hidden-state Trajectory Detection for Decoding-time Jailbreak Defense | defense、hidden-state trajectory、sliding window、decoding-time defense | Findings of ACL 2026 | [ACL Anthology](https://aclanthology.org/2026.findings-acl.655/) · [arXiv](https://arxiv.org/abs/2604.07727) | 暂未公开 | 针对静态 prompt、output 或单点 activation 忽略风险在 decoding 中的演化，论文以滑动窗口聚合 critical-layer trajectory 并只在持续高风险时语义复核；结果平均防御率 95%、检测延迟 5.2 ms/token 且 FPR 低于 1.5%。 |
| 2026&#8209;02 | NExT-Guard: Training-Free Streaming Safeguard without Token-Level Labels | defense、SAE feature、training-free monitor、latent risk | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/66186) · [arXiv](https://arxiv.org/abs/2603.02219) | [Code](https://github.com/NashChennc/NExTGuard) | 针对 token-level 标注昂贵且监督式 streaming guard 易过拟合，论文从已有 post-hoc safeguard 的 hidden representation 中用 SAE 提取 unsafe feature 并在线监控；结果无需额外训练即可跨模型和风险场景执行 streaming detection。 |
| 2025&#8209;10 | Kelp: A Streaming Safeguard for Large Models via Latent Dynamics-Guided Risk Detection | defense、latent dynamics、temporal consistency、plug-in monitor | ICML 2026 | [Official](https://icml.cc/virtual/2026/poster/64082) · [arXiv](https://arxiv.org/abs/2510.09694) | [Code](https://github.com/Alibaba-AAIG/Kelp) | 针对事后审核暴露风险且轻量 token probe 难保持时序稳定，论文以 20M-parameter SLD head 建模 hidden-state risk dynamics 并用 ATC loss 约束预测；结果平均 F1 提高 15.61%，每 token 额外延迟低于 0.5 ms。 |

## Benchmark 与可部署基线

| 时间 | 名称 | 类型 | 链接 | 作用与边界 |
| --- | --- | --- | --- | --- |
| 2026&#8209;06 | StreamSafe | sentence-level benchmark | [Paper](https://arxiv.org/abs/2606.02041) | 为 reasoning 与 answer segment 提供按句标注并覆盖多类风险，用于同时评测检测准确性、触发句位置和 streaming false positive。 |
| 2025&#8209;10 | StreamGuardBench | model-grounded benchmark | [Dataset](https://huggingface.co/datasets/Alibaba-AAIG/StreamGuardBench) | 针对每个被保护模型在线生成响应，并覆盖文本与 vision-language 场景；它减少使用静态完整响应切 prefix 对真实流式部署的偏差。 |
| 2025&#8209;10 | Qwen3Guard-Stream | production baseline | [Code](https://github.com/QwenLM/Qwen3Guard) · [Paper](https://arxiv.org/abs/2510.14276) | 提供多尺寸、多语言的 token-stream moderation 接口，是后续 forecasting 与 sentence-level 工作常比较的可部署基线；其固定 policy 与模型内 tokenizer 仍需按场景校准。 |

## 防御与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Withholding the Completing Chunk: Exact Release-Boundary Equivalence for Production Streaming Guardrails | defense、streaming guardrail、prefix detection、generation latency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.10279) | 暂未公开 | 该 streaming backstop 在每次释放前扫描累计 prefix，并扣住首次同时满足一对 lexical predicate 的 chunk；配置内 32 次机制测试全部与 buffered scanner 一致，但对 394 条通用 unsafe response 检出为零，明确只适合作为窄固定 policy 的确定性补充。 |
| 2025&#8209;12 | Dynamic Content Moderation in Livestreams: Combining Supervised Classification with MLLM-Boosted Similarity Matching | defense、livestream moderation、MLLM matching、production deployment | KDD 2026 | [Official](https://doi.org/10.1145/3770854.3783936) · [arXiv](https://arxiv.org/abs/2512.03553) | 暂未公开 | 该生产系统组合监督分类器与 MLLM 增强的相似案例匹配，以适应直播中新风险类别并在精度、召回、延迟之间做部署权衡。 |
| 2025&#8209;09 | Guard Vector: Beyond English LLM Guardrails with Task-Vector Composition and Streaming-Aware Prefix SFT | defense、task-vector composition、streaming guardrail、prefix detection | CoLM 2026 | [Official](https://colm.cc/Conferences/2026/AcceptedPapers) · [arXiv](https://arxiv.org/abs/2509.23381) | 暂未公开 | 针对英文 guardrail 难以低成本迁移到中日韩语言及流式输入的问题，Guard Vector 组合安全 task vector 并进行 prefix SFT，在无需目标语言标签的初始迁移下提升分类质量，同时降低延迟与计算量。 |

## 检测、审计与取证

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026 | PlugGuard: A Streaming Safeguard for Large Models via Latent Dynamics-Guided Risk Detection | detection、streaming guardrail、prefix detection、generation latency | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/64082) | 暂未公开 | 针对静态安全对齐容易过度拒绝，也难覆盖推理时出现的新风险的问题，论文提出 PlugGuard 防御或缓解方法；摘要实验显示其提高了系统对相应威胁的鲁棒性，直接服务于安全拒绝校准与在线防护。 |
