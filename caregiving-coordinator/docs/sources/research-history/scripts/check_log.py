#!/usr/bin/env python3
"""Check EVENT-LOG.md: every exact quote and every commit hash.

Rules checked for each table row (lines that start with "| E"):
  1. Each `git:<hash>` token must be a real commit (git cat-file).
  2. If a date (and optional time) directly follows the hash, it must match
     the commit's local date (US Pacific, via the machine clock).
  3. Each quote written as <<...>> must be 20 words or fewer, and must appear
     word for word (exact case) in at least one source named in the same row:
       `git:<hash>`  -> that commit's subject and body
       `mem:<file>`  -> owner memory note
       `dog:<file>`  -> Dog Feeding Docs/Week 2_3 report
       other `path`  -> repo file (relative to caregiving-coordinator/)
     Whitespace is collapsed and markdown * and ` marks are ignored, because
     the sources use them for bold and code. Letter case must match.
  4. Writes CHECK-REPORT.md with the file and line where each quote was found.

Usage: python3 -I check_log.py  (from any folder)
Exit code 1 if anything fails.
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
REPO = OUT.parents[2]  # .../caregiving-coordinator
DOG = REPO.parent / "Dog Feeding Docs" / "Week 2_3"
MEM = Path("/Users/landodoom/.claude/projects/-Users-landodoom-Desktop-AI-Developer-Residency-/memory")
LOG = OUT / "EVENT-LOG.md"


def git(*args):
    r = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True)
    return r.returncode, r.stdout


def norm(t):
    t = t.replace("*", "").replace("`", "")
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


def find_in_lines(lines, quote):
    """Return 1-based line number where quote starts, or None."""
    nq = norm(quote)
    joined = ""
    starts = []
    for ln in lines:
        starts.append(len(joined))
        joined += norm(ln) + " "
    i = joined.find(nq)
    if i < 0:
        return None
    line_no = 1
    for k, st in enumerate(starts):
        if st <= i:
            line_no = k + 1
        else:
            break
    return line_no


def resolve(token):
    """Return (label, lines) or None."""
    if token.startswith("git:"):
        h = token[4:]
        rc, out = git("show", "-s", "--format=%s%n%b", h)
        if rc != 0:
            return None
        return (f"commit {h}", out.splitlines())
    if token.startswith("mem:"):
        p = MEM / token[4:]
    elif token.startswith("dog:"):
        p = DOG / token[4:]
    else:
        p = REPO / token
    if p.is_file():
        return (str(p), p.read_text(errors="replace").splitlines())
    return None


def main():
    text = LOG.read_text()
    rows = [l for l in text.splitlines() if re.match(r"\| E\d+", l)]
    problems = []
    report = ["# Check report for EVENT-LOG.md", "",
              f"Rows checked: {len(rows)}", "",
              "| Event | Check | Result | Where |", "|---|---|---|---|"]
    nq = nh = 0
    for row in rows:
        eid = row.split("|")[1].strip()
        tokens = re.findall(r"`([^`]+)`", row)
        srcs = {}
        for t in tokens:
            if t.startswith(("git:", "mem:", "dog:")) or "/" in t or t.endswith(".md"):
                r = resolve(t)
                if r is None:
                    problems.append(f"{eid}: cannot resolve `{t}`")
                    report.append(f"| {eid} | source `{t}` | NOT FOUND | |")
                else:
                    srcs[t] = r
        # commit hashes and dates
        for m in re.finditer(r"`git:([0-9a-f]{7,40})`(?:[^`|;]{0,12}?)(\d{4}-\d{2}-\d{2})(?: (\d{2}:\d{2}))?", row):
            h, d, tm = m.group(1), m.group(2), m.group(3)
            rc, out = git("show", "-s", "--format=%ad", "--date=format-local:%Y-%m-%d %H:%M", h)
            nh += 1
            if rc != 0:
                continue
            cd, ct = out.strip().split()
            ok = (cd == d) and (tm is None or ct == tm)
            report.append(f"| {eid} | hash {h} date | {'OK' if ok else 'MISMATCH'} | log says {d} {tm or ''}; commit is {cd} {ct} |")
            if not ok:
                problems.append(f"{eid}: hash {h} date mismatch (log {d} {tm}, commit {cd} {ct})")
        # commit-only hash check for all hashes
        for h in set(re.findall(r"`git:([0-9a-f]{7,40})`", row)):
            rc, _ = git("cat-file", "-e", h + "^{commit}")
            if rc != 0:
                problems.append(f"{eid}: hash {h} is not a commit")
                report.append(f"| {eid} | hash {h} | NOT A COMMIT | |")
        for q in re.findall(r"<<(.+?)>>", row):
            nq += 1
            words = len(q.split())
            if words > 20:
                problems.append(f"{eid}: quote has {words} words: {q[:50]}")
            found = None
            for t, (label, lines) in srcs.items():
                ln = find_in_lines(lines, q)
                if ln:
                    found = (label, ln)
                    break
            if found:
                report.append(f"| {eid} | quote <<{q[:60]}>> ({words} words) | OK | {found[0]} line {found[1]} |")
            else:
                problems.append(f"{eid}: quote not found in this row's sources: <<{q}>>")
                report.append(f"| {eid} | quote <<{q[:60]}>> | NOT FOUND | |")
    report += ["", f"Quotes checked: {nq}. Hash-with-date checks: {nh}. Problems: {len(problems)}."]
    if problems:
        report += ["", "## Problems", *[f"- {p}" for p in problems]]
    (OUT / "CHECK-REPORT.md").write_text("\n".join(report) + "\n")
    print(f"rows={len(rows)} quotes={nq} hash-date-checks={nh} problems={len(problems)}")
    for p in problems:
        print("  -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
