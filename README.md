# Awesome Trustworthy AI

一个面向 Trustworthy AI 的中文论文知识库：持续追踪 arXiv 与前沿会议，将论文归入稳定的领域体系，并为重点论文沉淀可复用的精读笔记。

> 当前处于基础架构阶段。“全面”是持续维护目标，不代表现有收录已经完整。每条记录都应可追溯、可去重、可校验。

## 四层结构

| 层级 | 目录 | 作用 |
| --- | --- | --- |
| 每日论文汇总 | [`daily/`](daily/) | 保存每天从 arXiv 筛选出的相关论文与当日趋势 |
| 会议论文汇总 | [`conferences/`](conferences/) | 保存顶会录用列表中的相关论文与会议信息 |
| 领域论文汇总 | [`domains/`](domains/) | 按 Trustworthy AI 领域聚合全部论文 |
| 详细论文笔记 | [`papers/`](papers/) | 保存重点论文的精读、批判与复现记录 |

所有层级共享同一个论文主注册表 [`data/papers.jsonl`](data/papers.jsonl)。日报和会议清单只引用论文 ID；领域页由元数据自动生成，因此不会维护多份相互漂移的论文信息。

## 快速入口

- [基础知识与入门路线](foundations/README.md)
- [全部论文目录](library/README.md)
- [领域地图](domains/README.md)
- [会议追踪清单](conferences/watchlist.md)
- [检索 Prompt 模板](prompts/README.md)
- [待处理候选](inbox.md)
- [维护与收录规则](CONTRIBUTING.md)

## 运行工作流

每日 arXiv 收集：

```text
请按照 prompts/daily-arxiv.md 执行今天的论文收集。
```

会议录用论文收集：

```text
请按照 prompts/conference-watch.md 检查关注会议是否发布了新的录用列表。
请按照 prompts/conference-ingest.md 收集 <会议> <年份> 的录用论文，官方列表是 <URL>。
```

脚本要求 Python 3.10 或更高版本。每次采集完成后运行：

```bash
python3 scripts/library.py check
python3 scripts/library.py build
python3 scripts/library.py check-generated
python3 -m unittest discover -s tests -v
```

## 检索

按关键词、作者或摘要检索：

```bash
python3 scripts/library.py search "scalable oversight"
```

按领域、难度、年份或来源筛选：

```bash
python3 scripts/library.py search --domain alignment-control --level foundation
python3 scripts/library.py search --year-from 2024 --collection conference
```

查看可用领域和当前覆盖量：

```bash
python3 scripts/library.py stats
```

## 数据流

```text
arXiv / 官方会议列表
          |
          v
collection manifest  --->  data/papers.jsonl（去重后的唯一元数据）
          |                              |
          v                              v
daily/ 或 conferences/              domains/ 与 library/
                                         |
                                         v
                                papers/ 中的重点精读笔记
```

## 分类原则

外层分类参考 [NIST 对 Trustworthy AI 的特征划分](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/)，同时吸收 [ML Safety](https://arxiv.org/abs/2109.13916)、[AI Risk Repository](https://arxiv.org/abs/2408.12622) 与 [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) 中的研究问题。论文允许多标签归类，因为 alignment、security、privacy、fairness 与 governance 经常交叉。

原始论文标题、作者与 venue 保留英文；导航、短评与精读笔记默认使用中文。
