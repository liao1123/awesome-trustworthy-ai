# 详细论文笔记

这里保存值得精读的论文分析，而不是全部论文的副本。全部书目见 [论文总目录](../library/README.md)。

## 路径

```text
papers/<发表年份>/<paper-id>.md
```

每篇笔记使用 [`templates/paper-note.md`](../templates/paper-note.md)，并通过 `paper_id` 关联 [`data/papers.jsonl`](../data/papers.jsonl) 中的唯一记录。

## 精读标准

- 清楚区分论文声称了什么、实验证明了什么、自己如何判断。
- 记录关键假设、威胁模型、baseline、指标和失败案例。
- 对安全论文特别检查攻击者能力、评测泄漏、外推边界和双重用途风险。
- 能复现时记录环境、数据、参数、随机种子和与论文结果的差异。
