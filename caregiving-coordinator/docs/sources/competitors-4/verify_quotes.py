"""Proof check: every quote in evidence.json must appear word for word in its saved page (curly and straight quotes treated the same, spaces normalized)."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("﻿", "")).strip()
ok = bad = 0
for e in json.load(open(H / "evidence.json")):
    page = norm(open(H / e["file"]).read())
    for label, q in e["claims"]:
        if norm(q) in page: ok += 1
        else: bad += 1; print("NOT FOUND:", e["company"], "|", q[:70])
print(f"quotes found in saved pages: {ok}, not found: {bad}")
