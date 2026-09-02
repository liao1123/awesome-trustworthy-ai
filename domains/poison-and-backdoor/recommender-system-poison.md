# 推荐系统投毒

[返回投毒与后门目录](README.md)

## 研究方向

研究攻击者通过恶意用户、交互或内容注入操纵推荐模型与排序结果，以及在缺少攻击标签时对异常训练信号进行检测和缓解的方法。

## 研究脉络

- **威胁边界：** 明确攻击者能够写入的用户、交互和内容数据，以及被操纵的目标物品、曝光或排序指标。
- **无监督检测：** 在没有已知攻击样本时，利用局部结构、密度或平滑性识别注入数据。
- **效用权衡：** 防御评测同时报告攻击抑制效果、正常推荐质量和对真实用户的误伤。

## 检测与缓解

| 时间 | 论文名称 | 关键词 | 会议中稿情况 | 论文链接 | 代码链接 | 研究问题 | 核心 idea | 技术 | 结论 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-08 | Silencing the Poison: An Unsupervised Granular Ball Defense Approach in Local Smoothing Context for Recommender Systems | defense、recommender poisoning、unsupervised detection、local smoothing | KDD 2026 | [Official](https://doi.org/10.1145/3770855.3817740) | 暂未公开 | 研究如何防御 recommender poisoning、unsupervised detection 威胁，并评估 local smoothing 条件下的安全收益与效用代价。 | 论文以无监督 granular ball 和局部平滑识别推荐数据中的异常注入 | 关键实现：论文以无监督 granular ball 和局部平滑识别推荐数据中的异常注入。 | 在缺少攻击标签时缓解投毒对排序结果的操纵。 |
