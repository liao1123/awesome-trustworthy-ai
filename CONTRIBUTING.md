# 收录与维护规则

## 收录范围

资源需要直接帮助理解、评估或改进 Trustworthy AI，至少属于一个已登记领域。可收录论文、综述、benchmark、标准、技术报告和高质量教材；普通新闻、无稳定来源的观点文章和只在关键词上相关的论文不进入主注册表。

## 四步维护流程

1. 在 [`data/papers.jsonl`](data/papers.jsonl) 查重；优先比较 DOI，其次 arXiv ID，最后比较规范化标题。
2. 新论文只在主注册表添加一次，并使用 [`data/taxonomy.json`](data/taxonomy.json) 中已有的领域和主题 ID。
3. 为本次采集创建 collection manifest。日报使用 `data/collections/daily/YYYY/MM/YYYY-MM-DD.json`；会议使用 `data/collections/conferences/<venue>/<year>.json`。
4. 运行校验与生成命令，让日报、会议页、领域页和总目录同步更新。

GitHub 上的 push 和 pull request 会运行 `.github/workflows/validate.yml`，检查源数据、生成结果和单元测试。

## 元数据质量

每条论文记录必须包含稳定 ID、原始标题、作者、年份、venue、可信原文链接、领域、主题、难度、资源类型、重要性、校验状态、中文短摘要和维护日期。

`review_status` 的含义：

| 值 | 含义 |
| --- | --- |
| `metadata-checked` | 只核对过书目信息 |
| `abstract-checked` | 已阅读摘要并确认相关性 |
| `full-text-checked` | 已通读正文 |
| `note-complete` | 已完成仓库内精读笔记 |

## 领域同步

不要手动复制论文到各领域页面。只更新论文记录的 `domains` 和 `topics`，再运行 `python3 scripts/library.py build`。同一篇论文可以同时出现在多个领域，但始终只有一个 canonical record。

## 精读笔记

使用 [`templates/paper-note.md`](templates/paper-note.md) 创建 `papers/<发表年份>/<paper-id>.md`，并将该路径写回主注册表的 `note_path`。笔记必须区分作者主张、论文证据、自己的判断和待验证问题。
