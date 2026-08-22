# Audio Language Model Safety

[返回 Multimodal Model Security 目录](README.md)

## 研究方向

本页研究 Large Audio-Language Model（LALM）从连续声学信号到语言推理的安全失效。攻击面横跨 harmful speech、语言与口音、speaker style、background sound、adversarial waveform、near-ultrasound 和 audio token representation；评测还必须区分模型没有听懂、正确拒答与因缺少场景理解而 over-refuse。

## 研究脉络

- **文本安全不等于音频安全：** 早期 red teaming 表明同一有害请求改为 speech 或叠加非语音声响后，文本对齐的拒答能力明显下降。
- **声学维度扩展：** 攻击从 TTS 转写发展到 multilingual/accent、emotion/style、multi-speaker composition、imperceptible perturbation 与 physical acoustic channel。
- **机制分析：** 研究开始定位 audio token 的高梯度区域、latent acoustic semantic、text-audio alignment 与通用扰动中隐含的 linguistic feature。
- **评测细化：** benchmark 从统一 ASR 扩展到 comprehension-aware safety、speaker/context cue、over-refusal、跨模态一致性、latency 与 benign utility。
- **防御起步：** 当前路线包括 audio-aware guard model 和 refusal steering；对 adaptive、over-air、跨模型攻击的覆盖仍明显落后于攻击侧。

## Survey 与 Taxonomy

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Audio Jailbreaks in Large Audio-Language Models: Taxonomy, Attack-Defense Analysis, and Cost-Aware Evaluation | survey、audio jailbreak、attack-defense taxonomy、cost-aware evaluation | 投稿 ACL ARR 2026 May | [arXiv](https://arxiv.org/abs/2605.30031) | 暂未公开 | 针对不同 audio jailbreak 的 threat model 与指标不可比的问题，论文统一 semantic、acoustic、signal、embedding attack 和三类 defense 并在十个开源 LALM 上复测；结果表明评测必须同时报告 ASR、benign refusal 与 latency。 |
| 2026&#8209;05 | A Survey of Large Audio Language Models: Generalization, Trustworthiness, and Outlook | survey、LALM trustworthiness、audio attack surface、defense-in-depth | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2605.20266) | [Paper List](https://github.com/Kwwwww74/Awesome-Trustworthy-AudioLLMs) | 针对 LALM 能力发展快于系统可信性研究的问题，论文从 hallucination、robustness、safety、privacy、fairness 与 authentication 六个支柱整理风险；结论指出攻击研究远多于防御，并提出 Defense-in-Depth 与 representation engineering 路线。 |

## Audio-Specific Benchmark 与安全评测

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;06 | AOR-Bench: Do Large Audio Language Models Over-Refuse Pseudo-Harmful Queries? | benchmark、audio over-refusal、background context、pseudo-harmful query | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.21147) | 暂未公开 | 针对单独听起来有害的 speech 可能被背景声音转化为良性情境的问题，AOR-Bench 构造六类 3,000 个 pseudo-harmful audio；结果十二个 LALM 普遍 over-refuse，CoT 与 activation steering 只能部分缓解。 |
| 2026&#8209;06 | SpeechJBB: Probing Safety Alignment and Comprehension in Large Audio Language Models under Code-Switched Speech | benchmark、code-switched speech、pseudo-word obfuscation、multilingual safety | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2606.06037) | [Dataset](https://huggingface.co/datasets/McGill-NLP/SpeechJBB) | 针对以单语文本为主的评测忽略 code-switching 与自然语音混淆，SpeechJBB 加入跨语言 harmful speech 和 safety-critical term 周围的 pseudo-word；结果非英语及 code-switched 组合的 JSR 最高，局部混淆会进一步降低 refusal。 |
| 2026&#8209;04 | VoxSafeBench: Not Just What Is Said, but Who, How, and Where | benchmark、speaker context、paralinguistic cue、privacy fairness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.14548) | [Project](https://amphionteam.github.io/VoxSafeBench_demopage/) | 针对文字转语音 benchmark 丢失 speaker、语气和环境信息的问题，VoxSafeBench 以这些 audio-native cue 测试 safety、fairness 与 privacy 决策；结果模型往往能感知线索，却不能稳定据此调整行为。 |
| 2025&#8209;05 | JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models | benchmark、JALMBench、audio transformation、attack-defense evaluation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.17568) | 暂未公开 | 针对 audio jailbreak 数据规模、模型覆盖与 defense protocol 不一致的问题，JALMBench 构建大规模文本到音频变换并统一评估多类攻击和防御；结果显示安全表现会随语言、说话方式和声学条件显著波动。 |
| 2025&#8209;05 | Audio Jailbreak: An Open Comprehensive Benchmark for Jailbreaking Large Audio-Language Models | benchmark、audio perturbation toolkit、Bayesian optimization、black-box evaluation | ACL 2026 | [Proceedings](https://aclanthology.org/2026.acl-long.1259/) | [Artifact](https://anonymous.4open.science/r/AudioJailbreak-4262/) | 针对缺少可复现的黑盒 audio jailbreak 评测，论文整理 1,495 个对抗音频并用 Audio Perturbation Toolkit 在时间、频率和混音域做 Bayesian optimization；结果揭示广泛漏洞，也显示高 ASR 攻击可能需要较高查询与计算成本。 |
| 2025&#8209;01 | Jailbreak-AudioBench: In-Depth Evaluation and Analysis of Jailbreak Threats for Large Audio Language Models | benchmark、Jailbreak-AudioBench、acoustic attribute、hidden semantics | NeurIPS 2025 Datasets and Benchmarks | [arXiv](https://arxiv.org/abs/2501.13772) | [Code](https://github.com/Researchtopic/Code-Jailbreak-AudioBench) | 针对仅把文本请求直接合成为语音无法覆盖 audio hidden semantics，Jailbreak-AudioBench 系统改变音量、语速、音调、背景声、speaker voice 与 emotion；结果不同声学属性可显著改变越狱率，证明需要 audio-native 安全评测。 |

## 语义、语言与说话风格攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;03 | Now You Hear Me: Audio Narrative Attacks Against Large Audio-Language Models | attack、narrative framing、TTS delivery、black-box jailbreak | EACL 2026 | [Proceedings](https://aclanthology.org/2026.eacl-long.278/) | 暂未公开 | 针对直接朗读有害指令仍可能触发拒答的问题，论文把请求嵌入第一人称或故事化 narrative 后以 TTS 输入模型；结果在多种 LALM 上显著提高越狱成功率，并在 Gemini 上达到 98.26%。 |
| 2026&#8209;02 | The Alignment Curse: Modality Alignment Supercharges Audio Attacks via Text Transfer | analysis、alignment curse、text-to-audio transfer、omni model | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2602.02557) | 暂未公开 | 针对更强 text-audio alignment 是否也会迁移文本漏洞的问题，论文比较文本攻击、text-transferred audio 与原生 audio attack；结果文本迁移攻击常不弱于音频专用攻击，且 modality alignment 越紧密迁移越有效。 |
| 2025&#8209;11 | StyleBreak: Revealing Alignment Vulnerabilities in Large Audio-Language Models via Style-Aware Audio Jailbreak | attack、speech style、paralinguistic attribute、adaptive policy | AAAI 2026 | [Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/41093) | 暂未公开 | 针对现有攻击忽略人类语音表达变化的问题，StyleBreak 联合控制 linguistic、paralinguistic 与 extralinguistic 属性并用 query-adaptive policy 搜索风格；结果不同 speech style 会系统暴露 LALM alignment vulnerability。 |
| 2025&#8209;10 | Investigating Safety Vulnerabilities of Large Audio-Language Models Under Speaker Emotional Variations | analysis、speaker emotion、intensity variation、safety inconsistency | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.16893) | 暂未公开 | 针对相同语义由不同情绪和强度表达时 LALM 安全行为是否一致的问题，论文系统控制 speaker emotion 与 intensity；结果多个模型的拒答会随情绪显著波动，且中等强度常暴露更高风险。 |
| 2025&#8209;04 | Multilingual and Multi-Accent Jailbreaking of Audio LLMs | attack、multilingual audio、accent variation、acoustic perturbation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2504.01094) | [Code](https://github.com/jrohsc/Multi-AudioJail) | 针对英语中心评测遗漏跨语言与口音风险，Multi-AudioJail 联合 multilingual/multi-accent speech 与 reverberation、echo、whisper；结果特定组合将 JSR 提高最多 57.25 个百分点，audio-only 攻击可达 text-only 的 3.1 倍。 |
| 2025&#8209;04 | Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models | attack、audio red teaming、speech jailbreak、non-speech distraction | NAACL 2025 | [Proceedings](https://aclanthology.org/2025.naacl-long.470/) | [Code](https://github.com/YangHao97/RedteamAudioLMMs) | 针对文本对齐是否能迁移到 audio LMM 的问题，论文测试有害语音、非语音 distraction 和 speech-specific jailbreak；结果开源模型在有害音频上平均 ASR 为 69.14%，Gemini-1.5-Pro 的 speech attack 达 70.67%。 |

## Signal、Token 与物理声道攻击

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;05 | Acoustic Interference: A New Paradigm Weaponizing Acoustic Latent Semantic for Universal Jailbreak against Large Audio Language Models | attack、acoustic latent semantic、universal interference、cross-modal alignment | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.18168) | [Code](https://github.com/FlaAI/AIA) | 针对既有攻击必须把有害 payload 编进音频的问题，论文用语义良性的 Acoustic Latent Semantic 作为通用 interference 扰乱跨模态 safety alignment；结果可与不同文本 payload 解耦并跨请求触发越狱。 |
| 2026&#8209;05 | Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization | attack、TAGO、sparse audio token、gradient optimization | ICML 2026 | [arXiv](https://arxiv.org/abs/2605.04700) | 暂未公开 | 针对全波形优化成本高且可解释性弱的问题，TAGO 定位高 gradient-energy 的 audio token 区域并只优化稀疏片段；结果保留约 25% token 仍接近完整优化的 ASR，说明少量声学 token 即可主导安全失效。 |
| 2026&#8209;04 | Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection | attack、AudioHijack、auditory prompt injection、context generalization | IEEE S&P 2026 | [arXiv](https://arxiv.org/abs/2604.14604) | [Code](https://github.com/zju-muslab/AudioHijack) | 针对攻击者不知道用户上下文且 audio tokenizer 不可微的问题，AudioHijack 用 sampling-based gradient、attention supervision 与 reverberation blending 生成不可感知扰动；结果在未见上下文上达到 79% 至 96% success rate，并可诱导商业 voice agent 执行未授权动作。 |
| 2026&#8209;04 | GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking | attack、gradient-ratio masking、Mel-band selection、utility preservation | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2604.09222) | [Code](https://github.com/159753Fetter/GRM) | 针对 audio jailbreak 提高成功率时常明显破坏正常语音效用，GRM 以 jailbreak contribution 与 transcript sensitivity 的 gradient ratio 选择 Mel band 再局部优化；结果平均 JSR 达 88.46%，并减少良性转写和回答效用损失。 |
| 2026&#8209;03 | Sirens' Whisper: Inaudible Near-Ultrasonic Jailbreaks of Speech-Driven LLMs | attack、near-ultrasound、microphone nonlinearity、over-the-air | USENIX Security 2026 | [Proceedings](https://www.usenix.org/conference/usenixsecurity26/presentation/ling) | [Project](https://swhisper-jailbreak.github.io/) | 针对数字扰动难以在真实声道隐蔽传输的问题，SWhisper 用近超声载波和 microphone nonlinearity 在普通设备上解调恶意 speech；结果商业模型最高达到 0.94 non-refusal，用户研究中与背景播放难以区分。 |
| 2025&#8209;05 | AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models | attack、adversarial audio suffix、universal jailbreak、over-the-air robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2505.14103) | [Code](https://github.com/M3LSP/AudioJailbreak) | 针对 end-to-end LALM 的离散音频接口和真实播放条件，AudioJailbreak 优化可迁移 adversarial suffix 并测试 over-the-air 场景；结果生成通用且隐蔽的音频越狱，在多请求与多模型上保持效果。 |
| 2025&#8209;02 | "I am bad": Interpreting Stealthy, Universal and Robust Audio Jailbreaks in Audio-Language Models | analysis、universal perturbation、latent toxic speech、real-world robustness | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2502.00718) | 暂未公开 | 针对通用 audio perturbation 为何能跨 prompt 和 base audio 生效的问题，论文分析模型内部对扰动的解释；结果最强扰动会编码不可感知的第一人称 toxic speech，说明攻击利用了声学信号中的语言特征。 |
| 2024&#8209;12 | AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models | attack、AdvWave、audio suffix、gradient shattering | ICLR 2025 | [OpenReview](https://openreview.net/forum?id=0BujOfTqab) | [Code](https://github.com/kangmintong/AdvWave) | 针对 audio discretization 导致 gradient shattering 且 stealth constraint 缩小优化空间的问题，AdvWave 结合双阶段优化、adaptive target search 与 classifier-guided urban sound constraint；结果平均 ASR 比基线高约 40%。 |

## 模型内部与联合防御

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;11 | Speech-Audio Compositional Attacks on Multimodal LLMs and Their Mitigation with SALMONN-Guard | defense、SALMONN-Guard、speech-audio composition、joint moderation | ICML 2026 | [arXiv](https://arxiv.org/abs/2511.10222) | [Dataset](https://huggingface.co/datasets/tsinghua-ee/SACRED-Bench) | 针对 speech、non-speech audio 与多 speaker 共存时单通道审核失效的问题，SACRED-Bench 构造三类 composition attack 并训练 SALMONN-Guard 联合检查 audio、speech 与 text；结果把 Gemini 2.5 Pro 上 66% ASR 降至 20%。 |
| 2025&#8209;10 | SARSteer: Safeguarding Large Audio-Language Models via Safe-Ablated Refusal Steering | defense、SARSteer、refusal steering、safe-space ablation | ICML 2026 | [arXiv](https://arxiv.org/abs/2510.17633) | [Code](https://github.com/linweiii/SARSteer) | 针对文本 refusal direction 受 text-audio distribution gap 影响且 prompt defense 容易 over-refuse，SARSteer 结合 text-derived steering 与 decomposed safe-space ablation；结果提高 harmful-query refusal 并保持 benign speech response。 |

> 独立 audio moderation system 见 [Multimodal Guardrails](../../guardrails/multimodal-guardrails.md)。利用并发音频进一步劫持 Agent planning 与 tool call 的工作见 [Agent Tool 与 MCP Security](../../agent/tool-and-mcp-security.md)。
