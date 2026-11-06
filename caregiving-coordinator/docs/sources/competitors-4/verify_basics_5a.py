"""Proof check for basics-5a.json: every quote must appear word for word in its saved .txt file
(curly/straight quotes treated the same, invisible characters removed, spaces normalized). Also checks word limits."""
import json, re, pathlib
H = pathlib.Path(__file__).parent; SRC = H.parent
def norm(s):
    for a, b in (("’","'"),("‘","'"),("“",'"'),("”",'"'),("﻿",""),("​",""),("\xa0"," ")): s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()
ok = bad = long_q = long_a = 0; cache = {}
data = json.load(open(H / "basics-5a.json"))
for co, d in data.items():
    for field, v in d["fields"].items():
        if len(v["answer"].split()) > 30: long_a += 1; print("ANSWER >30 words:", co, field, len(v["answer"].split()))
        if not 0 <= len(v["quotes"]) <= 3: print("QUOTE COUNT:", co, field)
        for q in v["quotes"]:
            if len(q["quote"].split()) > 30: long_q += 1; print("QUOTE >30 words:", co, field)
            f = q["file"]
            if not f.endswith(".txt"): bad += 1; print("NOT A .txt:", f); continue
            if f not in cache: cache[f] = norm(open(SRC / f, encoding="utf8", errors="ignore").read())
            if norm(q["quote"]) in cache[f]: ok += 1
            else: bad += 1; print("NOT FOUND:", co, "|", field, "|", q["quote"][:70])
print(f"competitors: {len(data)}, quotes found: {ok}, not found: {bad}, quotes over 30 words: {long_q}, answers over 30 words: {long_a}")
