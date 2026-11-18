#!/usr/bin/env python3
"""Mechanical checks for a dogfooding handoff report.

Usage: python3 check_handoff.py <report.md> [--covers <list.md>] [--section N]
Exit code 0 = all checks pass, 1 = at least one failure (each failure is printed).

What it checks (the parts that have a right/wrong answer):
  1. All 10 required sections exist (## 0. Start here ... ## 9. Verification receipt).
  2. A "Replaces:" line exists (its value may be "none").
  3. A "Paste to start" line exists.
  4. Section 1 tags outcomes as Approved or Proposed.
  5. In sections 1 and 2, every line that states a number also shows a source
     (a path, a link, a page, or a "Source" table column).
  6. Section 9 has a "Not checked" item.
  7. (added 2026-11-18) Every file or folder path written in backticks exists when
     read from the repository's top folder. A path must therefore be written in full
     from that folder. A line that says the path "does not exist yet" is skipped.
  8. (added 2026-11-18) With --covers <list.md>: every row of the tables in that
     list appears in the report's plan section (default section 6), or the report
     says "Left out: <name>: <reason>". This catches a source that was approved
     but never put into a batch.
  9. (added 2026-11-18) A file the report points to must not say "Approved" in its
     Status line while a heading in the same file still says "Proposed ... awaiting".
What it cannot check: whether the content is true or useful. That is the
fresh-session test in SKILL.md. Counts written in prose (for example "about 44
sources") are not checked: count the rows yourself, or leave the count out.
"""
import os
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

# --- path check -------------------------------------------------------------
BACKTICK = re.compile(r"`([^`\n]+)`")
DOMAIN_START = re.compile(r"^[\w-]+(\.[\w-]+)*\.(org|com|gov|io|dev|net|edu|us)(/|$)", re.I)
HAS_EXTENSION = re.compile(r"\.[A-Za-z0-9]{1,5}$")
COMMAND_START = re.compile(r"^(git|gh|npm|npx|node|python3?|curl|cd|ls|cat|mkdir|rm|mv|cp|claude)\b")
NOT_YET = re.compile(
    r"does not exist|doesn't exist|not exist yet|to be created|will be created|not created yet|"
    r"new folder|new file|empty today",
    re.I,
)


def find_repo_root(report_path):
    """Walk up from the report until a folder holding .git is found."""
    folder = os.path.dirname(os.path.abspath(report_path))
    while True:
        if os.path.exists(os.path.join(folder, ".git")):
            return folder
        parent = os.path.dirname(folder)
        if parent == folder:
            return None
        folder = parent


def path_candidates(text):
    """Yield (line_number, path, line) for backtick spans that look like file or folder paths."""
    for number, line in enumerate(text.splitlines(), start=1):
        for match in BACKTICK.finditer(line):
            span = match.group(1).strip()
            if "/" not in span:
                continue
            if any(ch in span for ch in "<>*?|{}$") or "..." in span or "…" in span:
                continue
            if span.startswith(("http://", "https://")) or DOMAIN_START.match(span):
                continue
            if COMMAND_START.match(span) or " --" in span or span.startswith("-"):
                continue
            looks_like_path = (
                HAS_EXTENSION.search(span) or span.endswith("/") or span.startswith(("~/", "./", "../"))
            )
            if not looks_like_path:
                continue
            yield number, span.rstrip("/") if span != "/" else span, line


def resolve(path, repo_root):
    return os.path.expanduser(path) if path.startswith("~") else os.path.join(repo_root, path)


def missing_paths(text, repo_root):
    problems = []
    seen = set()
    for number, path, line in path_candidates(text):
        if path in seen:
            continue
        seen.add(path)
        if NOT_YET.search(line):
            continue
        if not os.path.exists(resolve(path, repo_root)):
            problems.append((number, path))
    return problems


# --- coverage check ---------------------------------------------------------
STOP = {
    "nist", "owasp", "cisa", "mitre", "first", "nice", "edition", "standard", "project", "dangerous",
    "most", "weaknesses",
    "the", "and", "for", "with", "from", "report", "guide", "security", "information", "software",
    "series", "newest", "reports", "using", "dangerous", "weaknesses", "official", "current",
    }
ID_PATTERN = re.compile(r"\b(?:SP|CSWP)\s?(\d+(?:-\d+)?)", re.I)


def list_rows(list_text):
    """First-cell names of every table row in the list (skips headers and separators)."""
    names = []
    for line in list_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not cells or not cells[0]:
            continue
        if set(stripped.replace("|", "").strip()) <= set("-: "):
            continue
        first = cells[0]
        if first.lower() in {"tier", "item"} or first.lower().startswith(("source", "file (in")):
            continue
        if re.match(r"^\d+\.\s", first):  # a numbered table such as a tier table, not a list of sources
            continue
        names.append(re.sub(r"[*`]", "", first))
    seen, unique = set(), []
    for name in names:
        key = name.lower()
        if key not in seen:
            seen.add(key)
            unique.append(name)
    return unique


def row_is_covered(name, plan_text):
    """True if the plan names this row: its SP/CSWP number, or any distinctive whole word of its name.

    Whole words only (no stemming): a looser match counted "information" as "informative".
    The matching is deliberately simple, so write each source in the plan under the name the
    list uses. A row that is only a note (for example "The owner's own career reasons") is
    cleared with a "Left out:" line.
    """
    plan_ids = {m.group(1) for m in ID_PATTERN.finditer(plan_text)}
    ids = {m.group(1) for m in ID_PATTERN.finditer(name)}
    if ids & plan_ids:
        return True
    plan_words = {w.lower() for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9.-]*", plan_text)}
    # A row with an SP/CSWP number is matched by that number or by a word of 4+ letters only, because a short
    # acronym such as "CSF" also appears in other rows.
    min_len = 4 if ids else 3
    words = [w.lower().strip(".-") for w in re.findall(r"[A-Za-z][A-Za-z0-9-]{%d,}" % (min_len - 1), name)]
    words = [w for w in words if w not in STOP]
    return any(w in plan_words for w in words)


def uncovered_rows(report_text, sections, list_text, section_number):
    plan = sections.get(section_number, "")
    left_out = "\n".join(
        line for line in report_text.splitlines() if re.match(r"^\s*[-*]?\s*\**left out:?\**", line, re.I)
    )
    return [
        name
        for name in list_rows(list_text)
        if not (row_is_covered(name, plan) or (left_out and row_is_covered(name, left_out)))
    ]


# --- stale label check --------------------------------------------------------
STATUS_APPROVED = re.compile(r"^\s*\**status:?\**.*\bapproved\b", re.I)
STALE_HEADING = re.compile(r"^#{1,6}\s.*\bproposed\b.*\bawaiting\b", re.I)


def stale_labels(report_text, repo_root):
    problems = []
    seen = set()
    for _, path, _ in path_candidates(report_text):
        if not path.endswith(".md") or path in seen:
            continue
        seen.add(path)
        full = resolve(path, repo_root)
        if not os.path.isfile(full):
            continue
        try:
            with open(full, encoding="utf-8") as handle:
                lines = handle.read().splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        if not any(STATUS_APPROVED.match(line) for line in lines[:12]):
            continue
        for number, line in enumerate(lines, start=1):
            if STALE_HEADING.match(line):
                problems.append((path, number, line.strip()))
    return problems


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


def check(text, report_path=None, list_text=None, plan_section=6):
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

    repo_root = find_repo_root(report_path) if report_path else None
    if report_path and repo_root is None:
        failures.append("Could not find the repository's top folder (no .git above the report), so paths were not checked.")
    if repo_root:
        for number, path in missing_paths(text, repo_root):
            failures.append(
                f"Line {number}: the path `{path}` does not exist when read from the repository's top folder "
                f"({repo_root}). Write the full path from that folder, or say the path does not exist yet."
            )
        for path, number, heading in stale_labels(text, repo_root):
            failures.append(
                f"{path} line {number} still says Proposed/awaiting ({heading[:80]}) while its Status line says Approved."
            )
    if list_text is not None:
        for name in uncovered_rows(text, sections, list_text, plan_section):
            failures.append(
                f"The list has '{name[:90]}' but section {plan_section} never mentions it. "
                f"Add it to the plan, or write 'Left out: {name[:40]}: <reason>'."
            )
    return failures


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2
    report_path = args[0]
    list_path = None
    plan_section = 6
    rest = args[1:]
    while rest:
        flag = rest.pop(0)
        if flag == "--covers" and rest:
            list_path = rest.pop(0)
        elif flag == "--section" and rest:
            plan_section = int(rest.pop(0))
        else:
            print(__doc__)
            return 2
    with open(report_path, encoding="utf-8") as f:
        text = f.read()
    list_text = None
    if list_path:
        with open(list_path, encoding="utf-8") as f:
            list_text = f.read()
    failures = check(text, report_path, list_text, plan_section)
    if failures:
        print(f"FAIL: {len(failures)} problem(s) in {report_path}")
        for item in failures:
            print(f"  - {item}")
        return 1
    print(f"PASS: {report_path} has every required part.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
