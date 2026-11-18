"""Functional tests for scripts/check_handoff.py. Run: python3 -m unittest discover -s tests (from the skill folder)."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from check_handoff import check, path_candidates  # noqa: E402

GOOD = """# Handoff: Shop app → checkout redesign (2026-11-05)

Replaces: 2026-11-01-handoff-cart.md

> Paste to start: "Read this handoff report, then show me the plan."

## 0. Start here
- Where we are: the cart milestone is done.
- Next milestone: checkout redesign.

## 1. Locked outcomes
- Payments use Stripe Checkout. **Approved** (`docs/adr/0004-payments.md`).
- Guest checkout allowed. **Proposed**, not confirmed.

## 2. Key findings and data
| Finding | Number | Source | Confidence |
|---|---|---|---|
| Cart abandonment | 68% | analytics/2026-10.csv | Credible secondary |
- p95 latency is 180 ms (`perf/2026-11-05.json`).

## 3. Excluded and deferred
- Social login: deferred to v2.

## 4. Open decisions
- Which countries at launch.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| Stripe decision | Checkout flow | Fixed provider |

## 6. First steps
1. Show the plan to the owner.

## 7. Working rules
- See CLAUDE.md. Questions get answers, not edits.

## 8. Where things live
- Branch `checkout`, last commit abc123.

## 9. Verification receipt
- Checks run: check_handoff.py passed.
- Not checked: nothing outside the cart milestone.
"""


class CheckHandoff(unittest.TestCase):
    def test_good_report_passes(self):
        self.assertEqual(check(GOOD), [])

    def test_missing_section_fails(self):
        bad = GOOD.replace("## 4. Open decisions\n- Which countries at launch.\n", "")
        self.assertTrue(any("Open Decisions" in f for f in check(bad)))

    def test_missing_replaces_fails(self):
        bad = GOOD.replace("Replaces: 2026-11-01-handoff-cart.md\n", "")
        self.assertTrue(any("Replaces" in f for f in check(bad)))

    def test_missing_paste_line_fails(self):
        bad = GOOD.replace("> Paste to start: \"Read this handoff report, then show me the plan.\"\n", "")
        self.assertTrue(any("Paste to start" in f for f in check(bad)))

    def test_untagged_outcomes_fail(self):
        bad = GOOD.replace("**Approved**", "").replace("**Proposed**", "")
        self.assertTrue(any("Approved or Proposed" in f for f in check(bad)))

    def test_number_without_source_fails(self):
        bad = GOOD.replace("- p95 latency is 180 ms (`perf/2026-11-05.json`).", "- p95 latency is 180 ms.")
        self.assertTrue(any("no source" in f for f in check(bad)))

    def test_table_number_without_source_cell_fails(self):
        bad = GOOD.replace("| 68% | analytics/2026-10.csv |", "| 68% |  |")
        self.assertTrue(any("no source" in f for f in check(bad)))

    def test_dates_and_numbering_are_not_claims(self):
        ok = GOOD.replace("- Where we are: the cart milestone is done.", "- Where we are: done on 2026-11-05, step 3 of 6.")
        self.assertEqual(check(ok), [])

    def test_missing_not_checked_fails(self):
        bad = GOOD.replace("- Not checked: nothing outside the cart milestone.\n", "")
        self.assertTrue(any("Not checked" in f for f in check(bad)))


class ReportAgainstFilesTests(unittest.TestCase):
    """Checks added 2026-11-18: paths exist, a list is fully covered, labels agree."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        os.makedirs(os.path.join(self.root, ".git"))
        os.makedirs(os.path.join(self.root, "app", "docs"))
        with open(os.path.join(self.root, "app", "docs", "plan.md"), "w", encoding="utf-8") as f:
            f.write("# Plan\n")
        self.report_path = os.path.join(self.root, "report.md")
        # Create every file the GOOD report points to, so only the path under test can fail.
        for _, path, _ in path_candidates(GOOD):
            full = os.path.join(self.root, path)
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, "w", encoding="utf-8") as f:
                f.write("x\n")

    def tearDown(self):
        self.tmp.cleanup()

    def run_check(self, text, list_text=None):
        return check(text, self.report_path, list_text)

    def test_full_path_from_top_folder_passes(self):
        ok = GOOD.replace("- Next milestone: checkout redesign.", "- Next milestone: see `app/docs/plan.md`.")
        self.assertEqual(self.run_check(ok), [])

    def test_short_path_fails_and_names_the_path(self):
        bad = GOOD.replace("- Next milestone: checkout redesign.", "- Next milestone: see `docs/plan.md`.")
        failures = self.run_check(bad)
        self.assertTrue(any("`docs/plan.md`" in f and "top folder" in f for f in failures))

    def test_path_that_does_not_exist_yet_is_allowed_when_the_line_says_so(self):
        ok = GOOD.replace("- Next milestone: checkout redesign.", "- Save to `app/new/` (does not exist yet).")
        self.assertEqual(self.run_check(ok), [])

    def test_list_row_missing_from_plan_fails(self):
        list_text = "| Source | Date |\n|---|---|\n| Zebra Handbook | 2026 |\n| Owner plan | 2026 |\n"
        failures = self.run_check(GOOD, list_text)
        self.assertTrue(any("Zebra Handbook" in f for f in failures))
        self.assertFalse(any("Owner plan" in f for f in failures))

    def test_left_out_line_clears_a_list_row(self):
        list_text = "| Source | Date |\n|---|---|\n| Zebra Handbook | 2026 |\n"
        ok = GOOD.replace("## 3. Excluded", "- Left out: Zebra Handbook: owner declined it on 2026-11-05.\n\n## 3. Excluded")
        self.assertEqual(self.run_check(ok, list_text), [])

    def test_stale_proposed_label_in_an_approved_file_fails(self):
        with open(os.path.join(self.root, "app", "docs", "list.md"), "w", encoding="utf-8") as f:
            f.write("# List\n\n**Status:** Approved by the owner.\n\n## Added later (Proposed, awaiting approval)\n")
        bad = GOOD.replace("- Next milestone: checkout redesign.", "- Next milestone: see `app/docs/list.md`.")
        self.assertTrue(any("Proposed/awaiting" in f for f in self.run_check(bad)))


if __name__ == "__main__":
    unittest.main()
