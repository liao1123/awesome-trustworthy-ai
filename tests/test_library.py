import copy
import contextlib
import io
import re
import unittest

from scripts import library


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo = library.load_repository()

    def test_repository_is_valid(self):
        self.assertEqual([], library.validate_repository(self.repo))

    def test_all_domain_pages_are_generated(self):
        outputs = library.render_outputs(self.repo)
        for domain in self.repo.taxonomy["domains"]:
            self.assertIn(library.ROOT / "domains" / f"{domain['id']}.md", outputs)

    def test_parent_domain_is_required_for_topic(self):
        repo = copy.deepcopy(self.repo)
        repo.papers[0]["domains"].remove("robustness-reliability")
        errors = library.validate_papers(repo)
        self.assertTrue(any("distribution-shift-ood" in error for error in errors))

    def test_duplicate_arxiv_id_is_rejected(self):
        repo = copy.deepcopy(self.repo)
        duplicate = copy.deepcopy(repo.papers[0])
        duplicate["id"] = "2017-example-duplicate-record"
        duplicate["title"] = "A Different Display Title"
        repo.papers.append(duplicate)
        errors = library.validate_papers(repo)
        self.assertTrue(any("duplicate arXiv ID" in error for error in errors))

    def test_old_style_arxiv_id_is_supported(self):
        self.assertRegex("cs/9901001", library.ARXIV_RE)
        self.assertRegex("hep-th/9901001", library.ARXIV_RE)

    def test_malformed_tags_are_reported(self):
        repo = copy.deepcopy(self.repo)
        repo.papers[0]["domains"] = [{"id": "foundations"}]
        repo.papers[0]["topics"] = [{"id": "field-overviews"}]
        errors = library.validate_papers(repo)
        self.assertTrue(any("domains must contain only string IDs" in error for error in errors))
        self.assertTrue(any("topics must contain only string IDs" in error for error in errors))

    def test_search_by_domain(self):
        results = library.select_papers(self.repo, domain="alignment-control")
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(all("alignment-control" in paper["domains"] for paper in results))

    def test_title_normalization(self):
        self.assertEqual(
            library.normalize_title("AI-Safety: An Overview"),
            library.normalize_title("ai safety an overview"),
        )

    def test_valid_daily_collection(self):
        repo = copy.deepcopy(self.repo)
        paper_id = repo.papers[0]["id"]
        repo.collections = [
            {
                "schema_version": 1,
                "id": "daily-2026-08-21",
                "kind": "daily",
                "date": "2026-08-21",
                "title": "2026-08-21 arXiv Daily",
                "source_urls": ["https://arxiv.org/list/cs.AI/recent"],
                "query_notes": "按 taxonomy 关键词宽召回并阅读摘要。",
                "selection_stats": {
                    "candidates": 3,
                    "new_records": 1,
                    "existing_records": 0,
                    "included": 1,
                },
                "summary_zh": "本批次用于测试合法的每日 collection。",
                "items": [{"paper_id": paper_id, "reason_zh": "直接讨论 AI 安全问题。"}],
                "_path": "data/collections/daily/2026/08/2026-08-21.json",
            }
        ]
        self.assertEqual([], library.validate_collections(repo))
        rendered = library.render_collection_page(repo.collections[0], repo)
        self.assertIn("../../../domains/", rendered)

    def test_daily_collection_id_matches_date(self):
        repo = copy.deepcopy(self.repo)
        repo.collections = [
            {
                "schema_version": 1,
                "id": "daily-wrong-date",
                "kind": "daily",
                "date": "2026-08-21",
                "title": "Daily",
                "source_urls": ["https://arxiv.org/"],
                "query_notes": "覆盖全部 taxonomy 领域执行测试检索。",
                "selection_stats": {
                    "candidates": 0,
                    "new_records": 0,
                    "existing_records": 0,
                    "included": 0,
                },
                "summary_zh": "测试批次没有通过相关性核验的条目。",
                "items": [],
                "_path": "data/collections/daily/2026/08/2026-08-21.json",
            }
        ]
        errors = library.validate_collections(repo)
        self.assertTrue(any("daily id must be 'daily-2026-08-21'" in error for error in errors))

    def test_valid_conference_collection(self):
        repo = copy.deepcopy(self.repo)
        paper_id = repo.papers[0]["id"]
        repo.collections = [
            {
                "schema_version": 1,
                "id": "conference-iclr-2026",
                "kind": "conference",
                "date": "2026-01-26",
                "title": "ICLR 2026 Trustworthy AI Papers",
                "venue_id": "iclr",
                "conference_year": 2026,
                "source_urls": ["https://iclr.cc/virtual/2026/papers.html"],
                "query_notes": "遍历官方主会列表并读取候选摘要。",
                "selection_stats": {
                    "official_total": 1000,
                    "candidates": 20,
                    "merged_records": 0,
                    "included": 1,
                },
                "summary_zh": "本批次用于测试合法的会议 collection。",
                "items": [{"paper_id": paper_id, "reason_zh": "论文直接研究 AI 安全。"}],
                "_path": "data/collections/conferences/iclr/2026.json",
            }
        ]
        self.assertEqual([], library.validate_collections(repo))
        rendered = library.render_collection_page(repo.collections[0], repo)
        self.assertIn("../../domains/", rendered)

    def test_invalid_taxonomy_is_reported_without_downstream_validation(self):
        repo = copy.deepcopy(self.repo)
        repo.taxonomy["domains"] = ["not-an-object"]
        errors = library.validate_repository(repo)
        self.assertTrue(any("expected an object" in error for error in errors))

    def test_search_rejects_unknown_domain(self):
        args = library.build_parser().parse_args(["search", "--domain", "not-a-domain"])
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(2, library.command_search(self.repo, args))

    def test_local_markdown_links_resolve(self):
        link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        failures = []
        for page in library.ROOT.rglob("*.md"):
            if ".git" in page.parts or "templates" in page.parts:
                continue
            content = page.read_text(encoding="utf-8")
            content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
            for target in link_pattern.findall(content):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                relative_target = target.split("#", 1)[0]
                if relative_target and not (page.parent / relative_target).resolve().exists():
                    failures.append(f"{page.relative_to(library.ROOT)} -> {target}")
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
