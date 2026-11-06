import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_invest", ROOT / "scripts" / "check_invest.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

GOOD = (ROOT / "references" / "worked-example.md").read_text()


def fails_of(text):
    return mod.check(text)[0]


def warns_of(text):
    return mod.check(text)[1]


class CheckInvest(unittest.TestCase):
    def test_worked_example_passes(self):
        self.assertEqual(fails_of(GOOD), [])

    def test_no_story_headings_fails(self):
        self.assertTrue(any("No stories" in f for f in fails_of(GOOD.replace("## Story 1", "## Part one"))))

    def test_missing_given_when_then_fails(self):
        text = GOOD.replace("*Given*", "").replace("*When*", "").replace("*Then*", "")
        self.assertTrue(any("Given/When/Then" in f for f in fails_of(text)))

    def test_missing_story_sentence_fails(self):
        text = GOOD.replace("so that everyone sees", "and everyone sees")
        self.assertTrue(any("story sentence" in f for f in fails_of(text)))

    def test_missing_acceptance_criteria_fails(self):
        text = GOOD.replace("**Acceptance criteria:**", "**Checks:**")
        self.assertTrue(any("acceptance criteria" in f for f in fails_of(text)))

    def test_missing_receipt_fails(self):
        text = GOOD.split("## Receipt")[0]
        self.assertTrue(any("Receipt" in f for f in fails_of(text)))

    def test_receipt_missing_not_checked_fails(self):
        text = GOOD.replace("**Not checked:**", "**Other:**")
        self.assertTrue(any("Not checked" in f for f in fails_of(text)))

    def test_bold_receipt_label_is_accepted(self):
        text = GOOD.replace("## Receipt", "**Receipt**")
        self.assertEqual(fails_of(text), [])

    def test_three_week_size_fails(self):
        text = GOOD.replace("Small | Pass: ~1 wk", "Small | Pass: ~3 weeks")
        self.assertTrue(any("2-week limit" in f for f in fails_of(text)))

    def test_one_and_a_half_weeks_warns_but_passes(self):
        text = GOOD.replace("Small | Pass: ~1 wk", "Small | Pass: ~1.5 weeks")
        self.assertEqual(fails_of(text), [])
        self.assertTrue(any("over 1 week" in w for w in warns_of(text)))

    def test_solution_words_warn_but_pass(self):
        text = GOOD.replace("invite my siblings", "click a button to invite my siblings")
        self.assertEqual(fails_of(text), [])
        self.assertTrue(any("solution" in w for w in warns_of(text)))

    def test_homework_mode_skips_story_sentence(self):
        text = "Mode: homework\n" + GOOD.replace("so that everyone sees", "and everyone sees")
        self.assertFalse(any("story sentence" in f for f in fails_of(text)))

    def test_ungraded_letters_fail(self):
        text = GOOD.replace("Testable", "Checkable")
        self.assertTrue(any("not graded" in f for f in fails_of(text)))


if __name__ == "__main__":
    unittest.main()
