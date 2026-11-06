#!/usr/bin/env python3
"""Mechanical checks for a dogfooding handoff report.

Usage: python3 check_handoff.py <report.md>
Exit code 0 = all checks pass, 1 = at least one failure (each failure is printed).

What it checks (the parts that have a right/wrong answer):
  1. All 10 required sections exist (## 0. Start here ... ## 9. Verification receipt).
  2. A "Replaces:" line exists (its value may be "none").
  3. A "Paste to start" line exists.
  4. Section 1 tags outcomes as Approved or Proposed.
  5. In sections 1 and 2, every line that states a number also shows a source
     (a path, a link, a page, or a "Source" table column).
  6. Section 9 has a "Not checked" item.
What it cannot check: whether the content is true or useful. That is the
fresh-session test in SKILL.md.
"""
import re
import sys

SECTIONS = [
    (0, "start here"),
    (1, "locked outcomes"),
    (2, "key findings"),
    (3, "excluded"),
    (4, "open decisions"),
    (5, "bridge"),
    (6, "first steps"),
    (7, "working rules"),
    (8, "where things live"),
    (9, "verification receipt"),
]

# A "number" worth sourcing: a percentage, money, or a count/measure of 2+ digits.
NUMBER = re.compile(r"(\d+(\.\d+)?\s?%|[$€£]\s?\d|\b\d{2,}(,\d{3})*(\.\d+)?\b)")
# Things that are digits but not claims: ISO dates, years alone, section/list numbering.
NOT_A_CLAIM = re.compile(r"\b\d{4}-\d{2}-\d{2}\b|\b(19|20)\d{2}\b")
# Signs that a source is given on the same line.
SOURCE_HINT = re.compile(
    r"(https?://|www\.|\.(md|json|csv|pdf|txt|py|html|xlsx?)\b|`[^`]*/[^`]*`|\bp{1,2}\.\s?\d|\bpage\b|"
    r"\bsource\b|\bsources\b|\bper\b|\(see |\bfrom `|figure \d|\bnode\b|\badr\b)",
    re.I,
)


def split_sections(text):
    """Return {section_number: body_text} for '## N. Title' headings."""
    parts = {}
    current = None
    buf = []
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d+)\.\s*(.*)$", line)
        if m:
            if current is not None:
                parts[current] = "\n".join(buf)
            current = int(m.group(1))
            buf = [line]
        elif current is not None:
            buf.append(line)
    if current is not None:
        parts[current] = "\n".join(buf)
    return parts


def unsourced_number_lines(body):
    problems = []
    lines = body.splitlines()
    source_col = None  # index of a 'Source' column in the current table
    for line in lines[1:]:
        stripped = line.strip()
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if source_col is None and any(c.lower().startswith("source") or c.lower() == "where" for c in cells):
                source_col = next(i for i, c in enumerate(cells) if c.lower().startswith("source") or c.lower() == "where")
                continue
            if set(stripped.replace("|", "").strip()) <= set("-: "):
                continue
            claim_text = NOT_A_CLAIM.sub("", stripped)
            if NUMBER.search(claim_text):
                if source_col is not None and source_col < len(cells) and cells[source_col]:
                    continue
                if SOURCE_HINT.search(stripped):
                    continue
                problems.append(stripped)
        else:
            source_col = None
            if not stripped or stripped.startswith("#"):
                continue
            claim_text = NOT_A_CLAIM.sub("", re.sub(r"^\s*(\d+[.)]|[-*•])\s+", "", stripped))
            if NUMBER.search(claim_text) and not SOURCE_HINT.search(stripped):
                problems.append(stripped)
    return problems


def check(text):
    failures = []
    sections = split_sections(text)
    headings = {n: sections[n].splitlines()[0].lower() for n in sections}
    for n, word in SECTIONS:
        if n not in headings or word not in headings[n]:
            failures.append(f"Missing section '## {n}. {word.title()}' (or its heading is worded differently).")
    if not re.search(r"^\s*\**Replaces:?\**\s*\S", text, re.I | re.M):
        failures.append("Missing a 'Replaces:' line (write 'Replaces: none' if there is no older report).")
    if not re.search(r"paste to start", text, re.I):
        failures.append("Missing a 'Paste to start' line telling the owner what to paste into the next session.")
    s1 = sections.get(1, "")
    if s1 and not re.search(r"\b(approved|proposed)\b", s1, re.I):
        failures.append("Section 1 doesn't tag any outcome as Approved or Proposed.")
    for n in (1, 2):
        for line in unsourced_number_lines(sections.get(n, "")):
            failures.append(f"Section {n}: a number with no source next to it: {line[:120]}")
    s9 = sections.get(9, "")
    if s9 and not re.search(r"not checked", s9, re.I):
        failures.append("Section 9 has no 'Not checked' item (say what wasn't verified, even if it's 'nothing').")
    return failures


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        text = f.read()
    failures = check(text)
    if failures:
        print(f"FAIL: {len(failures)} problem(s) in {sys.argv[1]}")
        for item in failures:
            print(f"  - {item}")
        return 1
    print(f"PASS: {sys.argv[1]} has every required part.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
