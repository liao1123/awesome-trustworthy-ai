# CBRN and Biosecurity

[返回 AI for Science Safety 目录](README.md)

## 研究方向

本页研究 AI 对 chemical、biological、radiological、nuclear risk 的 capability uplift 与防护，重点覆盖 biology agent、protein foundation model、DNA language model、sequence generation 和 nucleic-acid synthesis screening。评测不能只观察自然语言 refusal：模型可能拒绝显式请求，却通过 tool use、code 或可行生物序列产生实际风险。防御因此需要同时处理 model alignment、domain guardrail、sequence screening、provenance watermark、controlled access 和现实实验验证。

## 研究脉络

- **知识代理指标：** WMDP 等 benchmark 先用 bio、chem 和 cyber knowledge 测量 hazardous capability，但 multiple-choice score 不能直接代表现实 uplift。
- **领域模型 Red Team：** SafeProtein 与 GeneBreaker 分别把攻击推进到 protein 和 DNA foundation model，通过 multimodal prompt、beam search、pathogenicity signal 与 bioinformatics tool 检查 sequence-level vulnerability。
- **功能风险度量：** SPIKE-Bench 不再把 refusal 当作终点，而是继续检查 amino-acid sequence 的 biological plausibility 与 predicted toxicity；Early Warning work 进一步把 computational red team 接到受控 wet-lab validation。
- **Agentic capability：** ABC-Bench 评测 Agent 编写 liquid-handling code、设计 DNA assembly 和规避 synthesis screening，显示 published protocol 可以把文本知识转成现实实验动作。
- **纵深防御：** BioSafe-Guard、DNA/protein watermark、pretraining filtering、classifier guard 和 synthesis screening 分别覆盖输出拦截、provenance、结构性知识控制与供应链检查；单层拒答不能构成完整 biosecurity case。

## Bio-Capability 与 Agentic Uplift

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;07 | An Early Warning of Emerging Biosecurity Risks in Frontier LLMs | attack、bio red team、wet-lab validation、capability uplift | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2607.18056) | 暂未公开 | 针对 text-only CBRN evaluation 无法判断模型输出能否转化为生物产物；论文以 Intern-BioBreaker 定向生成 jailbreak，并把筛选后的 sequence 接入 DNA synthesis、host expression 与 protein verification；结果多种 frontier model 出现高 ASR，部分模型生成设计可在受控实验中实现。 |
| 2026&#8209;06 | ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity | benchmark、bio agent、DNA assembly、screening evasion | ICML 2026 | [arXiv](https://arxiv.org/abs/2606.11150) | 暂未公开 | 针对知识问答无法衡量 Agent 把 biology 与 software skill 组合成现实动作的能力；论文评测 liquid-handler coding、DNA fragment design 和 synthesis-screening evasion，并进行三组 wet-lab validation；结果所有受测 Agent 在三项任务均超过 median expert baseline，且模型生成脚本成功完成 DNA assembly。 |
| 2025&#8209;10 | Generative AI for Biosciences: Emerging Threats and Roadmap to Biosecurity | analysis、bioscience misuse、lifecycle defense、adaptive governance | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2510.15975) | 暂未公开 | 针对 bioscience GenAI 的 jailbreak、privacy、autonomous agent 和 dual-use 风险缺少统一路线图；论文结合 130 名专家访谈提出 data filtering、training alignment、real-time monitoring 和 governance 的全生命周期防御；结论是能力与监管共同演化时需要 secure-by-design 而非单点 guardrail。 |

## Protein 与 DNA Model Red Team

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026&#8209;08 | A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models | benchmark、SPIKE-Bench、functional harmfulness、BioSafe-Guard | COLM 2026 | [arXiv](https://arxiv.org/abs/2608.02684) | [Code](https://github.com/PKU-Alignment/SPIKE-Bench) | 针对自然语言 refusal 无法判断生成 toxin-like protein sequence 是否具备功能风险；论文用 compliance、biological plausibility 和 predicted toxicity 三阶段 SPIKE funnel 评测 32 个模型并训练 BioSafe-Guard；结果 FHR 最高达 50.7% 且与 refusal rate 脱钩，专用 guard 可降低预测风险并保持良性效用。 |
| 2025&#8209;09 | SafeProtein: Red-Teaming Framework and Benchmark for Protein Foundation Models | attack、protein foundation model、heuristic beam search、sequence misuse | 未注明（arXiv） | [arXiv](https://arxiv.org/abs/2509.03487) | 论文声明公开，链接待核实 | 针对 protein foundation model 缺少系统 red team；论文结合 multimodal prompt engineering 与 heuristic beam search，并构建 SafeProtein-Bench；结果可持续 jailbreak 多种模型，ESM3 上 ASR 最高 70%，暴露蛋白质理解和设计能力的 dual-use 风险。 |
| 2025&#8209;05 | GeneBreaker: Jailbreak Attacks against DNA Language Models with Pathogenicity Guidance | attack、DNA language model、pathogenicity guidance、sequence jailbreak | ICLR 2026 | [ICLR](https://proceedings.iclr.cc/paper_files/paper/2026/hash/398b00a05b847ac65eb98c8e5e865fe8-Abstract-Conference.html) · [arXiv](https://arxiv.org/abs/2505.23839) | [Code](https://github.com/zaixizhang/GeneBreaker) | 针对 DNA language model 能否在 jailbreak 下设计 pathogen-like sequence；论文让 bioinformatics Agent、PathoLM-guided beam search 和 BLAST/function annotation 组成 GeneBreaker；结果跨六类病毒稳定攻击 Evo 系列，Evo2-40B ASR 最高 60%，且模型规模增大伴随更高 dual-use risk。 |

## Provenance、Screening 与 Built-in Safeguard

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 一句话总结 |
| --- | --- | --- | --- | --- | --- | --- |
| 2025&#8209;09 | Securing the Language of Life: Inheritable Watermarks from DNA Language Models to Proteins | defense、DNA watermark、protein inheritance、sequence provenance | NeurIPS 2025 | [NeurIPS](https://neurips.cc/virtual/2025/poster/116266) · [arXiv](https://arxiv.org/abs/2509.18207) | 暂未公开 | 针对生成 DNA 在 mutation、translation 和 downstream protein 中难追踪；论文提出 DNAMark 的 synonymous codon embedding 和可跨 central dogma 继承的 CentralMark；结果多种扰动下 detection F1 超过 0.85，并在 CRISPR-Cas9 case 展示 provenance 用途。 |
| 2025&#8209;04 | A call for built-in biosecurity safeguards for generative AI tools | analysis、built-in safeguard、sequence screening、dual-use biology | Nature Biotechnology | [Nature Biotechnology](https://www.nature.com/articles/s41587-025-02650-8) | 暂未公开 | 针对 generative biology model 可能产生数据库之外的新型 pathogen、toxin 或 screening-evasive molecule；论文主张把 biosecurity 检查内建到生成工具和供应链，而不是只依赖用户政策；结论是模型、synthesis provider 与治理机构需要协同的多层 safeguard。 |

## 相关研究博客

| 时间 | 标题 | 发布机构或作者 | 关联主题 | 链接 | 核心内容 |
| --- | --- | --- | --- | --- | --- |
| 2026&#8209;01 | Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks | Anthropic | CBRN classifier、universal jailbreak、deployment efficiency | [Anthropic Research](https://www.anthropic.com/research/next-generation-constitutional-classifiers) | 说明面向危险 CBRN query 的 Constitutional Classifier 如何通过更高效架构和 ensemble 降低 harmless refusal，并用真实部署流量讨论防御强度与计算代价；同时明确不存在完全鲁棒的市场化防御。 |
| 2025&#8209;09 | Why do we take LLMs seriously as a potential source of biorisk? | Anthropic | biological uplift、capability evaluation、ASL-3 | [Anthropic Research](https://www.anthropic.com/research/biorisk) | 结合模型在 virology troubleshooting 等评测上的能力增长解释为何 bio uplift 已从理论风险变成需要持续测量的问题，并讨论 ASL-3 safeguard、monitoring、synthesis screening 与不确定性。 |
| 2025&#8209;05 | Activating AI Safety Level 3 protections | Anthropic | CBRN deployment、capability threshold、defense in depth | [Anthropic](https://www.anthropic.com/news/activating-asl3-protections) | 说明 Claude Opus 4 发布时为何在尚未确认越过 threshold 的情况下预防性启用 ASL-3，并区分针对 CBRN misuse 的 deployment measure 与防止 model-weight theft 的 security standard。 |

> Hazardous knowledge proxy、unlearning 和 pretraining filtering 的主条目保留在 [Capability Access Control](../misc/capability-access-control.md)，其中包括 WMDP 与 Anthropic pretraining-data-filtering 研究；跨六学科的 SoSBench 主条目见 [Scientific Domain Risk Evaluation](scientific-domain-risk-evaluation.md)。
