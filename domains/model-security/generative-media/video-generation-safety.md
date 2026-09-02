# Video Generation Safety

[返回 Generative Media Security 目录](README.md)

## 研究方向

本页研究 text-to-video（T2V）、image-to-video（I2V）及 text-and-image-to-video（TI2V）系统生成有害动态内容的风险。视频安全不能只逐帧复用 T2I filter：有害语义可能来自两个 benign boundary state 之间的 transition、多个无害事件的时间组合，或参考图中的箭头、文字、姿态线和镜头框被模型解释为可执行动作。评测因此需要联合衡量 prompt/refusal、unsafe frame、完整事件语义、视频质量和 multimodal guardrail 的漏检。

## 研究脉络

- **基础安全评测：** T2VSafetyBench 首先把内容风险、jailbreak prompt 与 temporal safety 纳入统一测试，建立安全与生成效用必须共同报告的基线。
- **Optimization-based jailbreak：** T2V-OptJail 把 filter evasion、危险语义保持和视频一致性写成离散 prompt optimization，攻击由固定测试集走向主动漏洞搜索。
- **Temporal attack surface：** SPARK、TEAR 与 BSB 分别利用跨模态关联、事件序列和 boundary-state transition，证明单帧或纯文本审核无法覆盖动态组合风险。
- **I2V visual instruction：** RunawayEvil 与 VII 联合篡改参考图和文字，VPA-Guard 则系统化箭头、草图、emoji、双帧等可执行 visual cue，安全边界从内容识别扩展到动作推断。
- **Proactive safeguard：** ConceptGuard 与 VPA-Guard 在生成前融合 image-text risk、检索相似攻击并抑制危险条件；当前仍缺少对闭源模型更新、长视频、音频条件和自适应攻击的持续评测。

## Benchmark 与安全诊断

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation | benchmark、audio-video generation、multimodal conditioning、compositional risk | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2608.26535) | 暂未公开 | 针对现有视频生成安全评测以文本 prompt 或固定接口为主、无法覆盖跨模态和跨时间组合风险 | Multi2AV-Safety 枚举全部 11 种非单一 T／I／A／V 条件配置并构造 11,024 个攻击实例 | 关键实现：Multi2AV-Safety 枚举全部 11 种非单一 T／I／A／V 条件配置并构造 11,024 个攻击实例。 | 评测发现单独良性的条件可组合出危害，而显式危险线索混入良性上下文后也更难被 guard 检出。 |
| 2026-05 | SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation | benchmark、image-conditioned T2V、compositional risk、guardrail failure | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.01481) | 暂未公开 | 针对既有评测只用恶意文字、忽略安全图文组合仍会产生有害动作 | SafeGen-Bench 以 start frame 和 prompt 覆盖十类动态风险 | 关键实现：SafeGen-Bench 以 start frame 和 prompt 覆盖十类动态风险。 | 受测模型 unsafety score 最高 44.5，单模态 guardrail 在七类风险中有 80% failure rate。 |
| 2026-04 | Moiré Video Authentication: A Physical Signature Against AI Video Generation | defense、video authentication、video generation、unsafe synthesis | ECCV 2026 | [Official](https://eccv.ecva.net/virtual/2026/poster/3761) · [arXiv](https://arxiv.org/abs/2604.01654) | [Code](https://github.com/yuanqing-ai/PVS) | 针对生成视频逐渐摆脱统计伪影的问题 | 作者推导真实相机中莫尔条纹相位与物体位移的物理不变量 | 关键实现：作者推导真实相机中莫尔条纹相位与物体位移的物理不变量。 | 实验证明其相关性可稳定区分真实拍摄和多种 AI 生成视频。 |
| 2026 | SMD: Multi-view Safety-Critical Driving Video Generation in the Real-world Domain | defense、video generation、unsafe synthesis、temporal consistency | ICML 2026 Poster | [Official](https://icml.cc/virtual/2026/poster/61036) | [Project](https://icml-2.github.io/SMD/) | 针对具身与自动驾驶系统的感知或规划失误会转化为现实物理风险的问题 | 论文提出 SMD 防御或缓解方法 | 关键实现：论文提出 SMD 防御或缓解方法。 | 摘要实验显示其降低相应风险或攻击效果，同时尽量保持正常任务效用，直接服务于物理世界部署安全。 |
| 2024-07 | T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models | benchmark、T2V safety、temporal risk、safety-utility trade-off | NeurIPS 2024 Datasets and Benchmarks Track | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/74eed5f568354c2e77dd9b018f38a9d4-Abstract-Datasets_and_Benchmarks_Track.html) · [arXiv](https://arxiv.org/abs/2407.05965) | [Code](https://github.com/yibo-miao/T2VSafetyBench) | 针对视频生成只有质量 benchmark、缺少动态安全量化 | T2VSafetyBench 以真实、LLM 生成和 jailbreak prompt 覆盖多类风险并评测主流 T2V | 关键实现：T2VSafetyBench 以真实、LLM 生成和 jailbreak prompt 覆盖多类风险并评测主流 T2V。 | 结果显示没有模型在所有维度占优，且 safety 与 usability 存在权衡。 |

## Text-to-Video Temporal Jailbreak 与 Red Teaming

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | Between Safe Boundaries: Exploiting Temporal Consistency for Jailbreaking Text-To-Video Generation Models | attack、boundary-state transition、temporal consistency、MCTS search | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.17279) | 暂未公开 | 针对 T2I-derived attack 没有利用视频 transition 且黑盒查询昂贵 | BSB 用两个各自安全的 boundary state 编码有害过程 | 并在文本 proxy space 做 MCTS、以稀疏视频查询校准 | 在多种商业 T2V 上相对最强基线平均提高 18.6% ASR。 |
| 2025-11 | TEAR: Temporal-aware Automated Red-teaming for Text-to-Video Models | tool、temporal red teaming、online preference learning、event decomposition | CVPR 2026 | [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/He_TEAR_Temporal-aware_Automated_Red-teaming_for_Text-to-Video_Models_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2511.21145) | 暂未公开 | 针对图像式 red teaming 无法发现由动态事件组合产生的风险 | TEAR 训练 temporal-aware test generator 并用在线偏好学习与 MLLM feedback 迭代 stealthy prompt | 关键实现：TEAR 训练 temporal-aware test generator 并用在线偏好学习与 MLLM feedback 迭代 stealthy prompt。 | 在开源和商业 T2V 上 ASR 超过 80%，高于此前 57% 的最佳结果。 |
| 2025-11 | SPARK: Jailbreaking T2V Models by Synergistically Prompting Auditory and Recontextualized Knowledge | attack、audio-visual association、latent auditory trigger、guided prompt search | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.13127) | 暂未公开 | 针对明显有害 prompt 易被过滤 | SPARK 将 neutral scene anchor、文字描述的 latent auditory event 与 cinematic style 组合以激活 audio-visual 共现先验 | 关键实现：SPARK 将 neutral scene anchor、文字描述的 latent auditory event 与 cinematic style 组合以激活 audio-visual 共现先验。 | 在七个 T2V 上有效，并使商业模型平均 ASR 提高 23 个百分点。 |
| 2025-05 | T2V-OptJail: Discrete Prompt Optimization for Text-to-Video Jailbreak Attacks | attack、discrete prompt optimization、filter evasion、semantic consistency | NeurIPS 2025 | [Official](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6ab3325de0bec40674c99fb0c20fc6a3-Abstract-Conference.html) · [NeurIPS](https://proceedings.neurips.cc/papers/2025) · [arXiv](https://arxiv.org/abs/2505.06679) | 暂未公开 | 针对固定恶意 prompt 只能被动测安全而不能系统探索漏洞 | T2V-OptJail 联合优化 filter bypass、prompt semantics 与 generated-video semantics | 并聚合 prompt variant 的反馈 | GPT-4 与人工评测的 ASR 分别较此前方法提高 11.4% 和 10.0%。 |

## Image-to-Video Visual Prompt Attack

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models | attack、I2V temporal jailbreak、semantic camouflage、latent perturbation | 未确认（arXiv Comments：Accepted by ACM Multimedia 2026） | [arXiv](https://arxiv.org/abs/2608.26971) | [Code](https://github.com/luqi-glory/TempJail) | 针对既有视频 jailbreak 多关注单帧违规、未利用恶意语义可在时间轴上组合出现的问题 | TempJail 将目标 caption 拆为初始帧条件与时序文本指令 | 并联合潜空间扰动和无害化 `subject-action-scene` 模板触发动态风险 | 在 Kling、Seedance、Veo 和 PixVerse 上，其 ASR 较此前方法按 GPT-5.2／人工评估分别提高 23.3／22.0 个百分点。 |
| 2026-02 | VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models | attack、visual instruction injection、reference-image attack、training-free transfer | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.20999) | [Code](https://github.com/Zbwwwwwwww/VII) · [Project](https://zbwwwwwwww.github.io/VII/) | 针对 I2V 会把参考图中的文字、箭头和框解释为动作而 input filter 只看到静态安全内容 | VII 将有害意图重编程并视觉落地到 benign image | 关键实现：VII 将有害意图重编程并视觉落地到 benign image。 | 在四个商业模型上 ASR 最高 83.5%，refusal rate 接近零。 |
| 2025-12 | RunawayEvil: Jailbreaking the Image-to-Video Generative Models | attack、multimodal jailbreak、self-evolving strategy、image-text coordination | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_RunawayEvil_Jailbreaking_the_Image-to-Video_Generative_Models_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2512.06674) | [Code](https://github.com/DeepSota/RunawayEvil) | 针对 I2V jailbreak 需要同时控制文字与参考图 | RunawayEvil 用 Strategy-Tactic-Action 架构进行 RL strategy customization、LLM planning 和 image tampering | 关键实现：RunawayEvil 用 Strategy-Tactic-Action 架构进行 RL strategy customization、LLM planning 和 image tampering。 | 在多个商业与开源 I2V 上持续自演化，并在 COCO2017 上较既有方法提高 58.5 至 79 个百分点。 |

## Proactive Safeguard 与 Visual Prompt Defense

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06 | VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks | defense、visual prompt attack、retrieval-augmented guard、VVA-Bench | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.25592) | [Code](https://github.com/HaoyuLucasKang/VPA-Guard) · [Dataset](https://huggingface.co/datasets/CSU-JPG/VVA-Bench) | 针对箭头、草图、emoji 与双帧等静态 cue 会在 I2V 中展开为有害动作 | 论文构建 VVA-Bench 并用检索、few-shot reasoning 和失败样本自更新组成 VPA-Guard | 关键实现：论文构建 VVA-Bench 并用检索、few-shot reasoning 和失败样本自更新组成 VPA-Guard。 | 平均降低 ASR 44.2%、harmfulness 73.4%，同时保留合法编辑效用。 |
| 2026-03 | Anti-I2V: Safeguarding your Photos from Malicious Image-to-video Generation | defense、image-to-video misuse、photo protection、adversarial perturbation | CVPR 2026 | [Official](https://openaccess.thecvf.com/content/CVPR2026/html/Vu_Anti-I2V_Safeguarding_your_Photos_from_Malicious_Image-to-video_Generation_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.24570) | 暂未公开 | 针对个人照片可被 I2V 模型恶意动画化的问题 | Anti-I2V 为原图加入难以察觉的保护扰动 | 关键实现：Anti-I2V 为原图加入难以察觉的保护扰动。 | 使未授权视频生成失效并考察跨模型与变换鲁棒性。 |
| 2025-11 | ConceptGuard: Proactive Safety in Text-and-Image-to-Video Generation through Multimodal Risk Detection | defense、multimodal risk detection、concept suppression、TI2V safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2511.18780) | [Code](https://github.com/Ruize-Ma/ConceptGuard) | 针对 text-only 或 post-generation guard 无法发现图文交互产生的隐式危险概念，ConceptGuard 先在结构化 concept space 检测风险 | 再干预 multimodal conditioning 抑制该语义 | 关键实现：再干预 multimodal conditioning 抑制该语义。 | 在 ConceptRisk 与 T2VSafetyBench-TI2V 上同时改善风险检测和安全生成。 |

> 生成后独立执行的视频审核见 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)；面向视频理解模型而非 generator 的越狱见 [Video Understanding Safety](../multimodal-models/video-understanding-safety.md)。
