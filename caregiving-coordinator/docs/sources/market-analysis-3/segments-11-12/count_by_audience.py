"""Step 2 of the audience split. Merges the script labels (audience-script.json) with the readers' labels
(audience-codes/acodes-*.json; a reader label wins), reports the spot-check agreement, and re-counts the relief
findings for Audience 1 (cared_for = parent), Audience 2 (spouse or partner) and everyone else.
Writes audience-labels.json and results-by-audience.json. Reuses the rules in count_results.py."""
import json, pathlib, collections, glob
import count_results as cr   # rebuilds results.json the same way and gives items, codes, is_resp, group_other
H = pathlib.Path(__file__).parent
script = json.load(open(H / "audience-script.json"))
reader = {}
for f in sorted(glob.glob(str(H / "audience-codes" / "acodes-*.json"))):
    for c in json.load(open(f)): reader[c["id"]] = c
labels = {}; agree = []; 
for i, v in script.items():
    if i in reader:
        labels[i] = {"label": reader[i]["cared_for"], "how": "reader", "quote": reader[i].get("quote", ""), "script_words": v["words"]}
        if v.get("spot_check"): agree.append((i, v["label"], reader[i]["cared_for"]))
    else:
        labels[i] = {"label": v["label"], "how": "script", "script_words": v["words"]}
missing = [i for i, v in labels.items() if v["label"] is None]
json.dump(labels, open(H / "audience-labels.json", "w"), indent=1, ensure_ascii=False)
AUD = {"Audience 1 (adult child caring for a parent)": {"parent"}, "Audience 2 (spouse or partner)": {"spouse or partner"},
       "Other (relative, own child, client, unclear)": {"other relative", "child", "client", "unclear"}}
rel = [c for c in cr.codes if c.get("relevant")]
res = {"labels": collections.Counter(v["label"] for v in labels.values()),
       "spot_check": {"n": len(agree), "agree": sum(a == b for _, a, b in agree), "disagreements": [x for x in agree if x[1] != x[2]]},
       "unlabeled": missing, "by_audience": {}}
HELPS = ["ALL RESPITE (any type, combined)", "paid aide or companion", "family or friend stepping in", "therapist or counselor for the caregiver", "support group", "adult day program", "hospice respite"]
def helps_of(c):
    hs = set(c.get("help", []))
    if cr.is_resp(c): hs.add("ALL RESPITE (any type, combined)")
    return hs
for name, labs in AUD.items():
    sub = [c for c in rel if labels[c["id"]]["label"] in labs]
    h = {}
    for k in HELPS:
        rows = [c for c in sub if k in helps_of(c)]
        h[k] = {"posts": len(rows), "status": dict(collections.Counter(r["status"] for r in rows))}
    bars = collections.defaultdict(list)
    for c in sub:
        for b in set(cr.group_other(b) if b.startswith("other: ") else b for b in c.get("barriers", [])): bars[b].append(c["id"])
    res["by_audience"][name] = {"relevant_posts": len(sub),
        "wanted_break_no_help": sum(1 for c in sub if c.get("wanted_break_no_help")),
        "help": h, "barriers": {b: {"n": len(v), "ids": sorted(v)} for b, v in sorted(bars.items(), key=lambda kv: -len(kv[1]))},
        "providers": collections.Counter(c["provider"].strip() for c in sub if c.get("provider")).most_common(12)}
json.dump(res, open(H / "results-by-audience.json", "w"), indent=1, ensure_ascii=False, default=dict)
print("labels:", dict(res["labels"])); print("spot check:", res["spot_check"]["agree"], "of", res["spot_check"]["n"], "agree; unlabeled:", len(missing))
for name, v in res["by_audience"].items():
    print(f"\n== {name}: {v['relevant_posts']} posts; wanted a break, no help: {v['wanted_break_no_help']}")
    for k, x in v["help"].items(): print(f"   {k:42} {x['posts']:4} {x['status']}")
    print("   barriers:", [(b, x["n"]) for b, x in list(v["barriers"].items())[:10]])
    print("   providers:", v["providers"][:8])
