# Repository Instructions

## Purpose

This repository is the Awesome Trustworthy AI paper knowledge base. Maintain four linked views: daily arXiv collections, conference collections, domain indexes, and detailed paper notes.

## Sources of truth

- `data/papers.jsonl` is the only canonical paper registry.
- `data/taxonomy.json` defines valid domains and topics.
- `data/collections/**.json` records immutable discovery batches.
- Files marked as generated must not be edited manually.
- Detailed notes under `papers/` reference a canonical paper with `paper_id`.

## Collection rules

- Verify bibliographic metadata against a primary source: arXiv, the publisher, proceedings, DOI landing page, or an official conference accepted-paper list.
- Never infer conference acceptance from an arXiv record or a search snippet.
- Deduplicate in this order: DOI, arXiv ID, then normalized title.
- A paper may have multiple domains and topics, but every tag must exist in `data/taxonomy.json`.
- Keep selection summaries factual. Inclusion is not endorsement.
- Do not commit publisher PDFs. Store stable links instead.
- Use ISO dates (`YYYY-MM-DD`) and the Asia/Hong_Kong date when creating daily collections.

## Language

- Preserve original English titles, author names, and venue names.
- Write navigation, relevance explanations, summaries, and notes in Chinese.
- Use lowercase ASCII slugs for IDs and paths.

## Required verification

After changing registry or collection data, run:

```bash
python3 scripts/library.py check
python3 scripts/library.py build
python3 scripts/library.py check-generated
python3 -m unittest discover -s tests -v
```

Commit source data and generated indexes together.
