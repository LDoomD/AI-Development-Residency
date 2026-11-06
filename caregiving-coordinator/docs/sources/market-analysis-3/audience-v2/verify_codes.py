"""Check codes-1..6: every item coded once, quotes exact, use case names from the right audience list, word limits."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent
A1 = ["Exhaustion, guilt and no life of their own","Dementia behavior and hard conversations","Money, legal papers and facility bills","Relatives don't help, or block each other","Medicines, eating and personal care","Choosing and arranging a place for them","Staying safe at home","Getting answers from doctors and hospitals","Being far away and not knowing what is happening","The parent refuses help","Getting into the parent's accounts"]
A2 = ["Exhaustion, loneliness and own health","Dementia behavior and hard conversations","Personal care and medicines","Safety when they are alone or out","Aides, hospice and trusting others","Placing them and care costs","Money, scams and bills","Diagnosis and doctor delays","Relatives and others not helping or criticizing","The partner refuses help"]
def norm(s): return s.replace("’","'").replace("‘","'").replace("“",'"').replace("”",'"')
bad = 0; total = 0
for n in range(1, 7):
    pack = {x["id"]: x for x in json.load(open(H / f"pack-{n}.json"))}
    try: codes = json.load(open(H / f"codes-{n}.json"))
    except FileNotFoundError: print(n, "missing"); continue
    ids = [c["id"] for c in codes]
    miss = set(pack) - set(ids); extra = set(ids) - set(pack); dup = len(ids) - len(set(ids))
    if miss or extra or dup: print(n, "missing", len(miss), "extra", len(extra), "dup", dup); bad += 1
    for c in codes:
        it = pack.get(c["id"]); 
        if not it: continue
        allowed = A1 if it["cared_for"] == "parent" else A2
        seen = set()
        for k in c["codes"]:
            k["use_case"] = k["use_case"].split(" (bank")[0]
            total += 1
            if k["use_case"] not in allowed: print(n, c["id"], "bad name", k["use_case"]); bad += 1
            if k["use_case"] in seen: print(n, c["id"], "dup use case", k["use_case"]); bad += 1
            seen.add(k["use_case"])
            if norm(k["quote"]) not in norm(it["text"]) or not k["quote"].strip(): print(n, c["id"], "quote not found:", k["quote"][:60]); bad += 1
            if len(k["moment"].split()) > 14 or len(k.get("want","").split()) > 14: print(n, c["id"], "too long"); bad += 1
print("codes", total, "problems", bad)
