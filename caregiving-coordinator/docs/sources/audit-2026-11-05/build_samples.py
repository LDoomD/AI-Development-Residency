"""Audit 2026-11-05: draws the fixed-seed samples for agents 1-3 (checklist: docs/research-checklist-audit-2026-11-05.md).
Sample files hold only the post text and id (never the first readers' codes), so the second readers work blind."""
import json, random, pathlib
H = pathlib.Path(__file__).parent; R = H.parent / "market-analysis-3/segments-11-12"
items = {}; codes = {}
for n in range(1, 12):
    for i in json.load(open(R / "packs" / f"pack-{n}.json")): items[i["id"]] = i
    for c in json.load(open(R / "codes" / f"codes-{n}.json")): codes[c["id"]] = c
lab = json.load(open(R / "audience-labels.json"))
rnd = random.Random(20261105)
rel = [i for i, c in codes.items() if c.get("relevant")]
by = {"parent": [i for i in rel if lab[i]["label"] == "parent"], "spouse or partner": [i for i in rel if lab[i]["label"] == "spouse or partner"]}
other = [i for i in rel if lab[i]["label"] not in by]
s1 = rnd.sample(sorted(by["parent"]), 25) + rnd.sample(sorted(by["spouse or partner"]), 15) + rnd.sample(sorted(other), 10)
s2 = rnd.sample(sorted(i for i, c in codes.items() if not c.get("relevant")), 40)
s3 = rnd.sample(sorted(i for i, v in lab.items() if v["how"] == "reader"), 40)
def dump(name, ids):
    rnd.shuffle(ids); json.dump([{"id": i, "url": items[i]["url"], "text": items[i]["text"]} for i in ids], open(H / name, "w"), indent=1, ensure_ascii=False)
dump("sample-1-recode.json", s1); dump("sample-2-relevance.json", s2); dump("sample-3-audience.json", s3)
print(len(s1), len(s2), len(s3))
