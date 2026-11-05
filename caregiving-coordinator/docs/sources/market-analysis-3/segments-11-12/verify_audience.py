"""Checks reader audience labels: every pack item labeled once, label allowed, quote exact (unless unclear)."""
import json, sys, re, pathlib
H = pathlib.Path(__file__).parent; OK = {"parent", "spouse or partner", "other relative", "child", "client", "unclear"}
def norm(s): return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
ns = [int(sys.argv[1])] if len(sys.argv) > 1 else sorted(int(p.stem.split("-")[1]) for p in (H / "audience-packs").glob("apack-*.json"))
bad = 0
for n in ns:
    pack = {i["id"]: i for i in json.load(open(H / "audience-packs" / f"apack-{n}.json"))}
    codes = json.load(open(H / "audience-codes" / f"acodes-{n}.json")); ids = [c["id"] for c in codes]; probs = []
    for k in pack:
        if ids.count(k) != 1: probs.append(f"{k}: labeled {ids.count(k)} times")
    for c in codes:
        if c["id"] not in pack: probs.append(f"{c['id']}: not in pack"); continue
        if c.get("cared_for") not in OK: probs.append(f"{c['id']}: bad label")
        if c.get("cared_for") != "unclear" and (not c.get("quote") or norm(c["quote"]) not in norm(pack[c["id"]]["text"])): probs.append(f"{c['id']}: quote not exact")
    bad += len(probs); print(f"apack {n}: items {len(pack)}, problems {len(probs)}"); [print("  ", p) for p in probs[:20]]
print("OK" if bad == 0 else f"{bad} problems")
