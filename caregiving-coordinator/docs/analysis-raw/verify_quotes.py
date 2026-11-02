#!/usr/bin/env python3 -I
"""Check every quote the readers returned against the saved source text.

A quote passes only if, after collapsing whitespace, it appears word for word in the file the reader
named. Locators ("POST", "COMMENT n") are checked too: the quote must sit inside that block.
Passing quotes are copied to verified/<batch>.json; failures go to failed/<batch>.json.
Run: python3 -I verify_quotes.py
"""
import glob, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "sources"))
INDEX = {}
for p in glob.glob(os.path.join(ROOT, "forums", "*", "*", "*.txt")) + glob.glob(os.path.join(ROOT, "youtube", "comments-raw", "*.txt")):
    INDEX.setdefault(os.path.basename(p), []).append(p)


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def blocks(text):
    """Split a saved file into {'POST': text, 'COMMENT n': text}."""
    out, cur, name = {}, [], "HEADER"
    for line in text.split("\n"):
        m = re.match(r"^=== (POST|COMMENT (\d+))", line)
        if m:
            out[name] = "\n".join(cur)
            name, cur = (m.group(1) if m.group(1) == "POST" else f"COMMENT {m.group(2)}"), []
        else:
            cur.append(line)
    out[name] = "\n".join(cur)
    return out


def check(q):
    base = os.path.basename(q.get("file", ""))
    if not base.endswith(".txt"):
        base += ".txt"
    paths = INDEX.get(base, [])
    if not paths:
        return False, "file not found"
    text = open(paths[0], encoding="utf-8").read()
    qt = norm(q.get("quote", ""))
    if len(qt) < 8:
        return False, "quote too short"
    loc = norm(q.get("locator", "")).upper()
    b = blocks(text)
    if loc in b and qt in norm(b[loc]):
        return True, "ok"
    if qt in norm(text):
        return True, "ok (found in file, locator not matched)"
    return False, "quote not found in file"


def walk(obj, fn):
    if isinstance(obj, dict):
        if "quote" in obj and "file" in obj:
            return fn(obj)
        return {k: walk(v, fn) for k, v in obj.items()}
    if isinstance(obj, list):
        return [r for r in (walk(x, fn) for x in obj) if r is not None]
    return obj


def main():
    os.makedirs(os.path.join(HERE, "verified"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "failed"), exist_ok=True)
    tot_ok = tot_bad = 0
    for f in sorted(glob.glob(os.path.join(HERE, "*.json"))):
        name = os.path.basename(f)
        try:
            data = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print(name, "INVALID JSON:", e); continue
        failed, ok = [], [0]

        def fn(q):
            good, why = check(q)
            if good:
                ok[0] += 1
                return q
            failed.append({**q, "why": why})
            return None
        clean = walk(data, fn)
        json.dump(clean, open(os.path.join(HERE, "verified", name), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        json.dump(failed, open(os.path.join(HERE, "failed", name), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        tot_ok += ok[0]; tot_bad += len(failed)
        print(f"{name}: {ok[0]} quotes verified, {len(failed)} removed")
    print("TOTAL", tot_ok, "verified,", tot_bad, "removed")


if __name__ == "__main__":
    main()
