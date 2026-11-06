#!/usr/bin/env python3
"""Check a saved INVEST scoping file (markdown).

Usage: python3 check_invest.py <file.md>
Exit 0 = pass (warnings may print), 1 = fail.

What it checks (mechanical checks only; it cannot judge whether a story is good):
  - at least one story, under a heading like "## Story 1: title" (or "## Task 1")
  - the six INVEST letters are graded Pass/Fail somewhere in the file
  - each story has: the story sentence (As a .. I want .. so that ..), Given/When/Then,
    acceptance criteria, and a scope or definition of done
  - no story is sized over 2 weeks
  - a Receipt section with Audited, Split, Written and Not checked
Warns (does not fail) when a story sentence names a screen or tool, or a size is over 1 week.
Homework mode: put "Mode: homework" in the file and the story sentence is not required.
"""
import re
import sys

LETTERS = ["Independent", "Negotiable", "Valuable", "Estimable", "Small", "Testable"]
SOLUTION_WORDS = ["button", "dropdown", "menu", "sidebar", "screen", "page", "modal", "popup",
                  "click", "api", "database", "react", "supabase", "field", "checkbox", "toggle"]
STORY_RE = re.compile(r"as an?\b.+?\bI want\b.+?\bso that\b.+", re.I | re.S)
HEADING_RE = re.compile(r"^#{2,3}\s+(Story|Task)\s+\d+", re.I | re.M)
# A receipt is a "## Receipt" heading or a bold "**Receipt**" line.
RECEIPT_RE = re.compile(r"^(?:#{2,3}\s+|\*\*)Receipt\b\**", re.I | re.M)
SIZE_RE = re.compile(r"~?\s*(\d+(?:\.\d+)?)\s*(?:-\s*\d+(?:\.\d+)?\s*)?(wks?|weeks?)\b", re.I)


def split_stories(text):
    marks = [m.start() for m in HEADING_RE.finditer(text)]
    end_marker = re.search(RECEIPT_RE, text)
    stop = end_marker.start() if end_marker else len(text)
    blocks = []
    for i, start in enumerate(marks):
        end = marks[i + 1] if i + 1 < len(marks) else stop
        blocks.append(text[start:min(end, stop) if end > stop else end])
    return blocks


def check(text):
    fails, warns = [], []
    homework = re.search(r"^\s*Mode:\s*homework", text, re.I | re.M) is not None
    stories = split_stories(text)
    if not stories:
        fails.append("No stories found. Use headings like '## Story 1: title'.")

    # Grades: every letter named, and enough Pass/Fail marks to cover them.
    missing = [l for l in LETTERS if not re.search(r"\b" + l + r"\b", text)]
    if missing:
        fails.append("Letters not graded: " + ", ".join(missing))
    if len(re.findall(r"\b(Pass|Fail)\b", text)) < 6:
        fails.append("Fewer than 6 Pass/Fail grades in the file.")

    for i, block in enumerate(stories, 1):
        title = block.splitlines()[0].strip()
        if not homework and not STORY_RE.search(block):
            fails.append(f"{title}: no story sentence ('As a ..., I want ..., so that ...').")
        elif not homework:
            sentence = STORY_RE.search(block).group(0).split("\n\n")[0].lower()
            hits = [w for w in SOLUTION_WORDS if re.search(r"\b" + w + r"s?\b", sentence)]
            if hits:
                warns.append(f"{title}: story names a solution ({', '.join(hits)}). Say the outcome instead.")
        if not all(re.search(r"\b" + w + r"\b", block) for w in ("Given", "When", "Then")):
            fails.append(f"{title}: no Given/When/Then scenario.")
        if not re.search(r"acceptance criteria", block, re.I):
            fails.append(f"{title}: no acceptance criteria.")
        if not re.search(r"definition of done|scope", block, re.I):
            fails.append(f"{title}: no scope or definition of done.")
        for m in SIZE_RE.finditer(block):
            n = float(m.group(1))
            if n > 2:
                fails.append(f"{title}: sized at {m.group(0).strip()}, over the 2-week limit. Split it.")
            elif n > 1:
                warns.append(f"{title}: sized at {m.group(0).strip()}, over 1 week (allowed, but flag it).")

    receipt = re.search(RECEIPT_RE.pattern + r"(.*)", text, re.I | re.M | re.S)
    if not receipt:
        fails.append("No Receipt section.")
    else:
        body = receipt.group(1)
        for part in ("Audited", "Split", "Written", "Not checked"):
            if not re.search(part, body, re.I):
                fails.append(f"Receipt is missing '{part}'.")
    return fails, warns


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    text = open(sys.argv[1], encoding="utf-8").read()
    fails, warns = check(text)
    for w in warns:
        print("WARN:", w)
    if fails:
        print(f"FAIL: {sys.argv[1]}")
        for f in fails:
            print("  -", f)
        return 1
    print(f"PASS: {sys.argv[1]} has every required part.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
