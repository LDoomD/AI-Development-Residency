"""Per audience and use case: distinct items (forum/reddit), and all moments and wants, for grouping. Duplicate post p1xnbiv7 dropped (same as p1xnbovn)."""
import json, collections, pathlib
H = pathlib.Path(__file__).parent
DUP = {"p1xnbiv7"}
src = {}; aud = {}
for n in range(1, 7):
    for x in json.load(open(H / f"pack-{n}.json")): src[x["id"]] = x["source"]; aud[x["id"]] = "A1" if x["cared_for"] == "parent" else "A2"
out = collections.defaultdict(lambda: {"forum": 0, "reddit": 0, "moments": [], "wants": []})
for n in range(1, 7):
    for c in json.load(open(H / f"codes-{n}.json")):
        if c["id"] in DUP: continue
        for k in c["codes"]:
            r = out[f'{aud[c["id"]]}|{k["use_case"].split(" (bank")[0]}']
            r[src[c["id"]]] += 1
            r["moments"].append([c["id"], k["moment"]]); 
            if k.get("want"): r["wants"].append([c["id"], k["want"]])
res = {k: v for k, v in sorted(out.items(), key=lambda kv: (kv[0][:2], -(kv[1]["forum"] + kv[1]["reddit"])))}
json.dump(res, open(H / "moments-by-usecase.json", "w"), indent=1, ensure_ascii=False)
for k, v in res.items(): print(k, "forum", v["forum"], "reddit", v["reddit"], "total", v["forum"] + v["reddit"], "wants", len(v["wants"]))
