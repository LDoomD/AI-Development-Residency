"""Check every motivation/goal/problem quote is an exact substring (whitespace collapsed) of its saved thread and at most 250 characters; flag threads whose quote is not by a caregiver is left to reading."""
import json, re, sys, pathlib, collections
HERE = pathlib.Path(__file__).parent; BASE = HERE.parent
ws = lambda s: re.sub(r"\s+", " ", s).strip()
items = {i["id"]: i for k in range(1, 5) for i in json.load(open(HERE / f"slice-{k}.json"))}
bad = 0; n = 0; kinds = collections.Counter()
for f in sys.argv[1:]:
    for t in json.load(open(HERE / f)):
        text = ws((BASE / items[t["id"]]["path"]).read_text(errors="ignore"))
        for it in t["items"]:
            n += 1; ok = ws(it["quote"]) in text and len(it["quote"]) <= 250; bad += not ok; kinds[it["type"]] += 1
            if not ok: print("FAIL", t["id"], it["quote"][:80])
print(n, "quotes,", bad, "failures,", dict(kinds))
