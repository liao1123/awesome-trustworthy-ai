# Diffusion Language Model Security

[返回 Language Model Security 目录](README.md)

## 研究方向

本页研究 masked/diffusion language model 通过并行、双向、迭代 denoising 生成文本时出现的专属安全机制与攻击面。与 autoregressive model 不同，攻击可直接利用 `[MASK]`、in-place infilling、token commitment 和 denoising-path dependence；防御也可观察完整中间轨迹、remask 可疑 token 或动态分配监测计算。训练时后门由 [扩散模型后门](../../poisoning-and-backdoors/diffusion-model-backdoors.md) 维护，本页只记录 inference-time safety 与机制交叉。

## 研究脉络

- **Architecture gap：** 基础分析比较 AR 与 masked diffusion 的 circuit、拒答轨迹和生成文本，确认安全差异不仅来自训练数据，也来自 sampling mechanism。
- **Diffusion-native attack：** PAD、DIJA 和 MaskForge 从 parallel decoding、interleaved mask-text 与可复用结构 pattern 出发，取代直接迁移 AR jailbreak template。
- **Trajectory monitoring：** SRI、hesitation-aware routing 与 pre-decoding state fusion 利用多步 hidden state 在最终有害文本出现前识别风险。
- **Denoising defense：** Safety-Aware Denoiser、adaptive remasking 和 DiffuGuard 在迭代过程中纠正 token，而不是只过滤完成后的输出。
- **当前边界：** 不同 dLLM 的初始化、remasking schedule 与 post-training 方式会产生截然不同的 intrinsic safety，结论不能从单一模型或固定 mask pattern 外推。

## 机制与安全边界

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;02 | Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models | analysis、refusal dynamics、sampling mechanism、internal recovery | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.02600) | [Code](https://github.com/ElironRahimi/sri-signal) · [Project](https://elironrahimi.github.io/sri-signal/) | 针对相同安全表示在 AR 与 diffusion sampling 下为何产生不同拒答，论文定义 SRI signal 追踪逐步内部恢复；结果发现有害输出对应 text-level 不可见的不完整恢复，并可据此构建低开销检测器。 |
| 2026&#8209;02 | Safer by Diffusion, Broken by Context: Diffusion LLM's Safety Blessing and Its Failure Mode | analysis、safety blessing、context nesting、denoising trajectory | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.00388) | 暂未公开 | 针对 dLLM 是否天然比 AR model 更安全，论文比较多步去噪中的风险演化并发现逐步 refinement 常修复有害倾向；结果这种 safety blessing 会被嵌套上下文破坏，说明优势依赖输入结构而非稳固对齐。 |
| 2026&#8209;01 | Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models | analysis、AR-to-diffusion post-training、circuit shift、global planning | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2601.14758) | 暂未公开 | 针对从 AR checkpoint 后训练出的 masked diffusion model 只是更换解码方式还是重组计算机制，论文进行跨任务 circuit comparison；结果局部因果任务保留 AR pathway，而全局规划转向更分布式且依赖浅层处理的新机制。 |

## Diffusion-Native Jailbreak Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits | attack、safety neuron、SN-guided diffusion、cross-architecture transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.07430) | [Code](https://github.com/ellyoana/sn-guided-diffusion) | 针对 dLLM 内部安全机制及其从 AR 初始化的继承关系未知，论文映射并剪除稀疏 safety neurons，再以其 activation 作为 diffusion guidance 离线生成攻击 prompt；结果既能直接破坏 dLLM 安全，也能向黑盒 AR model 迁移。 |
| 2026&#8209;06 | MaskForge: Structure-Aware Adaptive Attacks for Jailbreaking Diffusion Large Language Models | attack、mask structure、pattern library、adaptive bandit | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.04027) | 暂未公开 | 针对固定 mask template 无法适应不同目标，MaskForge 将成功尝试抽象为结构 pattern、用 UCB 选择匹配 schema 并把新经验写回库；结果在多个 dLLM 上提高 ASR，成熟 pattern 还能零更新迁移到新 benchmark。 |
| 2026 | The Devil Behind the Mask: An Emergent Safety Vulnerability of Diffusion LLMs | attack、interleaved mask-text、bidirectional infilling、parallel decoding | ICLR 2026 | [OpenReview](https://openreview.net/forum?id=rIPeatvPy3) | [Code](https://github.com/ZichenWen1/DIJA) | 针对标准 alignment 未覆盖用户直接控制 masked span 的场景，DIJA 将 harmful text 与 mask 交错并利用双向一致性和并行解码补全缺失内容；结果无需隐藏恶意语义也可显著绕过多种 aligned dLLM。 |
| 2025&#8209;07 | Jailbreaking Large Language Diffusion Models: Revealing Hidden Safety Flaws in Diffusion-Based Text Generation | attack、parallel decoding、multi-point attention、PAD | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2507.19227) | 暂未公开 | 针对 AR jailbreak 在 dLLM 上失效可能被误判为模型更安全，PAD 以 affirmative response pattern 引导 parallel generation 的多个位置；结果在多种 dLLM 上暴露高攻击成功率，并说明架构不匹配而非可靠对齐造成基线失败。 |

## Trajectory Detection 与 Monitoring

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | TRE: Training-Free Hallucination Detection for Diffusion Language Models | detection、entropy trajectory、revealing token、single-run metric | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.22661) | 暂未公开 | 现有 dLLM hallucination detector 依赖训练数据且跨模型泛化和部署成本受限；TRE 从单次 denoising 的 spatial revealing-token entropy 与 late-step temporal entropy 估计风险；结果无需参数和重复采样即可获得有竞争力的检测、泛化与效率。 |
| 2026&#8209;05 | $D^2$-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing | detection、safety hesitation、dynamic routing、trajectory probe | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.25893) | 暂未公开 | 针对 always-on 强 probe 成本高而轻量 probe 会在困难样本失效，论文用中间状态反复靠近 decision boundary 的 safety hesitation 预测失败并动态升级监测器；结果以紧凑参数量改善效果与效率的 Pareto trade-off。 |
| 2026&#8209;02 | TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs | detection、temporal dynamic graph、attention trajectory、hallucination detection | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.08048) | 暂未公开 | 针对只看最终 token state 会丢失 dLLM 多步去噪中的关系变化，TDGNet 将跨步 attention 演化建模为 temporal dynamic graph；结果利用 trajectory structure 提升 hallucination detection，并比静态表示更能定位失真形成过程。 |
| 2026 | Beyond the Prompt: Leveraging Pre-Decoding States for Jailbreak Detection in dLLMs | detection、pre-decoding state、state fusion、jailbreak detection | 未注明（OpenReview） | [OpenReview](https://openreview.net/forum?id=QVRvaVBwRh) | 暂未公开 | 针对 prompt-only detector 看不到 dLLM 已在 masked response 中形成的风险信号，论文融合 prompt representation 与首轮 pre-decoding response state；结果显著降低 diffusion-native jailbreak 的漏检，同时保持较低良性误拒。 |
| 2025&#8209;09 | TraceDet: Hallucination Detection from the Decoding Trace of Diffusion Large Language Models | detection、decoding trace、temporal representation、hallucination detection | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10011524) · [arXiv](https://arxiv.org/abs/2510.01274) | [Code](https://github.com/chang-sx/TraceDet) | 针对 dLLM 最终输出无法呈现 hallucination 在去噪过程中的累积信号，TraceDet 汇聚完整 decoding trace 的时序表示进行判断；结果表明生成轨迹比单一终态提供更稳定的检测依据。 |

## Denoising-Time Defense 与 Safety Alignment

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models | defense、adaptive remasking、contrastive safety direction、step-wise intervention | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.13043) | [Code](https://github.com/leeyejin1231/DLM_Steering_Remasking) | 针对中间有害 token 会沿后续去噪被持续强化，论文用 contrastive safety direction 逐步检测风险、remask 对应 token 并按危害程度自适应 steering；结果在无需再训练时降低 jailbreak 成功率且保持生成质量。 |
| 2026&#8209;05 | The Safety-Aware Denoiser for Text Diffusion Models | defense、safety-aware denoiser、safe-region guidance、inference-time control | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/62720) · [arXiv](https://arxiv.org/abs/2605.08116) | [Code](https://github.com/ParkLabML/SAD) | 针对 AR-oriented post-hoc filter 无法利用 diffusion trajectory，SAD 在每轮 denoising 中加入约束并将最终样本引向可证明的 safe region；结果在 hazard、memorization 和 jailbreak 评测中减少不安全生成，同时保留流畅性与多样性。 |
| 2025&#8209;10 | Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability | defense、priming vulnerability、contaminated state、diffusion alignment | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10008814) · [OpenReview](https://openreview.net/forum?id=ZMzha5gbnF) · [arXiv](https://arxiv.org/abs/2510.00565) | [Code](https://github.com/mdl-lab/dlm-priming-vulnerability) | 针对早期 affirmative token 会沿 denoising path 锁定有害结果，论文把这种 priming vulnerability 建模为 contaminated intermediate state 并从该状态训练安全恢复；结果提高对 mask-based attack 的鲁棒性。 |
| 2025&#8209;09 | DiffuGuard: How Intrinsic Safety is Lost and Found in Diffusion Large Language Models | defense、denoising-path dependence、stochastic remasking、block-level repair | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10006479) · [OpenReview](https://openreview.net/forum?id=zBPzxhso8M) · [arXiv](https://arxiv.org/abs/2509.24296) | [Code](https://github.com/niez233/DiffuGuard) | 针对 greedy remasking 的 harmful bias 与早期 token 决定最终安全的 path dependence，DiffuGuard 结合 stochastic annealing remasking 和 block-level audit-and-repair；结果在保留 utility 与 latency 时明显降低多类 jailbreak ASR。 |
| 2025&#8209;09 | A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models | defense、any-order alignment、randomized masking、early safe termination | ICLR 2026 | [Official](https://iclr.cc/virtual/2026/poster/10009223) · [OpenReview](https://openreview.net/forum?id=URTnuyQJI1) · [arXiv](https://arxiv.org/abs/2509.23286) | [Code](https://github.com/WonjeJeung/A2D) | 针对固定位置和固定去噪步的 safety tuning 无法覆盖 dLLM 任意生成顺序，A2D 以随机 mask 训练 token-level EOS 拒答；结果将 DIJA ASR 从超过 80% 压到接近零，并使安全终止最高加速 19.3 倍。 |
| 2025&#8209;09 | From Vulnerability to Defense: Understanding and Mitigating MASK-Based Attacks in dLLMs | defense、MASK-based jailbreak、margin accumulation、Reject-MASK | ICLR 2026 Withdrawn | [OpenReview](https://openreview.net/forum?id=jKQQb8uClw) | 暂未公开 | 针对 MASK-based prompt 为何能利用双向并行解码绕过安全对齐，论文从 margin accumulation 与 scheduling advantage 分析机制并提出 Reject-MASK 两阶段训练；结果把超过 90% 的 ASR 降至接近个位数，但投稿已撤回。 |
| 2025&#8209;08 | Where to Start Alignment? Diffusion Large Language Model May Demand a Distinct Position | defense、position-aware alignment、middle-token supervision、MOSA | AAAI 2026 | [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/37106) · [arXiv](https://arxiv.org/abs/2508.12398) | 暂未公开 | 针对 AR model 偏重开头 token 的安全对齐不能直接覆盖任意顺序生成，论文分析不同位置监督对 dLLM refusal 的影响并提出 MOSA 强化中间 token；结果显示 diffusion model 需要不同于首 token 主导范式的 position-aware alignment。 |

## Benchmark 与 Survey

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | TrustLDM: Benchmarking Trustworthiness in Language Diffusion Models | benchmark、dLLM trustworthiness、risk taxonomy、AR comparison | ICLR 2026 Trustworthy AI Workshop | [arXiv](https://arxiv.org/abs/2606.00023) | [Code](https://github.com/PKU-ML/TrustLDM) | 针对 dLLM 的 trustworthiness 结论分散在单一攻击或模型，TrustLDM 统一比较多个安全与可靠性维度并设置 AR baseline；结果揭示 diffusion architecture 的优势与失效会随风险类型和模型家族显著变化。 |
| 2025&#8209;06 | Discrete Diffusion in Large Language and Multimodal Models: A Survey | survey、discrete diffusion、parallel decoding、model taxonomy | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2506.13759) | [Code](https://github.com/LiQiiiii/Awesome-Discrete-Diffusion-LLM_MLLM) | 针对 dLLM 与 dMLLM 的数学定义、模型和训练术语不统一，论文从离散扩散形式化出发整理代表架构、训练、推理与应用；结果提供理解安全研究所依赖的 generation mechanism 和模型谱系。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | Diffusion Language Models | Junzhe Zhao | diffusion language model、resource map、generation mechanism | [Technical note](https://jzhao2024.github.io/notes/2026/08/08/diffusion-language-models.html) | 从生成过程、代表模型和近期工作组织 dLLM 入门材料，可作为阅读本页安全论文前的 architecture primer。 |

> Diffusion LM 的 training-time trigger、BadDLM、SHADOWMASK 与 purification 见 [扩散模型后门](../../poisoning-and-backdoors/diffusion-model-backdoors.md)；潜在 latency/energy amplification 见 [Language Model DoS](../../dos/language-model-dos.md)。
