"""Functional tests for scripts/check_handoff.py. Run: python3 -m unittest discover -s tests (from the skill folder)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from check_handoff import check  # noqa: E402

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


if __name__ == "__main__":
    unittest.main()
