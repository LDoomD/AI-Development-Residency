"""Check codes-1/2 (every item coded once, quotes exact) and count per competitor: relevant items, how used, and the
worked / problems / instead lists (for grouping). Writes counts-5b.json."""
import json, re, collections, pathlib
H = pathlib.Path(__file__).parent
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
bad = 0; out = collections.defaultdict(lambda: {"items": 0, "relevant": 0, "reddit": 0, "forum": 0, "used": collections.Counter(), "worked": [], "problems": [], "instead": []})
for n in (1, 2):
    pack = json.load(open(H / f"pack-{n}.json")); codes = json.load(open(H / f"codes-{n}.json"))
    idx = {(i["id"], i["competitor"]): i for i in pack}
    got = [(c["id"], c["competitor"]) for c in codes]
    if set(got) != set(idx) or len(got) != len(set(got)): print(n, "coverage problem", len(set(idx) - set(got)), "missing", len(got) - len(set(got)), "dupes"); bad += 1
    for c in codes:
        it = idx.get((c["id"], c["competitor"]))
        if not it: continue
        r = out[c["competitor"]]; r["items"] += 1
        if not c["relevant"]: continue
        if c["quote"] and norm(c["quote"]) not in norm(it["text"]): print("quote not found", c["id"], c["quote"][:60]); bad += 1
        r["relevant"] += 1; r[it["source"]] += 1; r["used"][c["used"]] += 1
        r["worked"] += [[c["id"], w] for w in c["worked"]]; r["problems"] += [[c["id"], p] for p in c["problems"]]
        if c["instead"]: r["instead"].append([c["id"], c["instead"]])
json.dump(out, open(H / "counts-5b.json", "w"), indent=1, ensure_ascii=False, default=dict)
for k, r in out.items(): print(f"{k}: items {r['items']}, relevant {r['relevant']} (reddit {r['reddit']}, forum {r['forum']}), used {dict(r['used'])}, worked {len(r['worked'])}, problems {len(r['problems'])}")
print("problems found by the check:", bad)
