"""Counts the checked reader codes (codes/codes-1..11.json) for segments 11 and 12. Run verify_codes.py first.
Writes results.json: per kind of help, how many relevant posts used, tried, wanted it and couldn't get it;
the barriers per kind of help; what helped; named providers; who pays; and "wanted a break, no help in place".
Every count keeps its list of item ids so it can be traced back to the post and its quote."""
import json, pathlib, collections
H = pathlib.Path(__file__).parent
items = {}; codes = []
for n in range(1, 12):
    for i in json.load(open(H / "packs" / f"pack-{n}.json")): items[i["id"]] = i
    codes += json.load(open(H / "codes" / f"codes-{n}.json"))
rel = [c for c in codes if c.get("relevant")]
# Readers handled "respite" with no type differently (left blank, guessed, or wrote "named program: respite (type not said)").
# So all respite is also counted together: any respite label, or a relevant post in the respite group whose help list is empty.
RESP = {"in-home respite", "short-stay respite (facility)", "hospice respite"}
def is_resp(c):
    hs = c.get("help", [])
    return any(h in RESP or "respite" in h.lower() for h in hs) or (not hs and "respite" in [t.lower() for t in items[c["id"]]["matched"]])
# Free-text "other:" barriers grouped by keyword (rules in order; the first match wins). Unmatched stay "other (single mentions)".
OTHER = [  # corrected 2026-11-05 after the audit: support-group text first; no "husband/spouse/son " matching
 ("support group doesn't fit or isn't available", r"group"),
 ("family or friends won't help", r"famil|sibling|brother|sister|relative|in-law|\bsons?\b|daughter|nobody|no one|no help|support network|won't help|step in|no backup"),
 ("too few hours, minimum stays or other limits", r"hour|minimum|limit|curfew|weekend|only|days a week|week"),
 ("therapy doesn't help or isn't available", r"therap|counsel"),
 ("the break isn't restful (worry, more work, chores)", r"worry|anxiety continues|during the break|harder|more work|chores|can't relax|preparing"),
 ("agencies, social workers or helplines don't help", r"agenc|social work|helpline|pamphlet|staff|case manager|hospice"),
 ("no services nearby", r"local|nearby|state |area|services|found nothing|no place"),
 ("the person cared for is anxious or worse away from home", r"anxious|disorient|confus|worse|won't allow|upset"),
 ("no time or energy to arrange it", r"time|energy|drained|exhaust|hassle|arrange|where to start")]
import re as _re
def group_other(b):
    t = b[7:].lower()
    for name, rx in OTHER:
        if _re.search(rx, t): return name
    return "other (single mentions)"
def ids(rows): return sorted(c["id"] for c in rows)
out = {"items_read": len(codes), "relevant": len(rel),
       "relevant_by_group": collections.Counter(items[c["id"]]["group"] for c in rel),
       "wanted_break_no_help": {"n": sum(1 for c in rel if c.get("wanted_break_no_help")), "ids": ids([c for c in rel if c.get("wanted_break_no_help")])},
       "help": {}, "barriers_all": {}, "named_providers": {}, "payer_cost": []}
helps = collections.defaultdict(list)
for c in rel:
    for h in c.get("help", []):
        key = h if not h.startswith("named program: ") else ("respite (type not said)" if "respite" in h.lower() and "type not said" in h.lower() else "named program")
        helps[key].append(c)
helps["ALL RESPITE (any type, combined)"] = [c for c in rel if is_resp(c)]
for h, rows in sorted(helps.items(), key=lambda kv: -len(kv[1])):
    st = collections.Counter(r["status"] for r in rows); bars = collections.defaultdict(list); good = collections.Counter()
    for r in rows:
        for b in set(group_other(b) if b.startswith("other: ") else b for b in r.get("barriers", [])): bars[b].append(r["id"])
        for g in r.get("helped", []): good[g.lower()] += 1
    out["help"][h] = {"posts": len(rows), "status": dict(st),
                      "barriers": {b: {"n": len(v), "ids": sorted(v)} for b, v in sorted(bars.items(), key=lambda kv: -len(kv[1]))},
                      "helped_top": good.most_common(15)}
allb = collections.defaultdict(list)
for c in rel:
    for b in set(group_other(b) if b.startswith("other: ") else b for b in c.get("barriers", [])): allb[b].append(c["id"])
out["barriers_all"] = {b: {"n": len(v), "ids": sorted(v)} for b, v in sorted(allb.items(), key=lambda kv: -len(kv[1]))}
prov = collections.defaultdict(list)
for c in rel:
    if c.get("provider"): prov[c["provider"].strip()].append(c["id"])
out["named_providers"] = {p: {"n": len(v), "ids": v} for p, v in sorted(prov.items(), key=lambda kv: -len(kv[1]))}
out["payer_cost"] = [{"id": c["id"], "payer_cost": c["payer_cost"], "url": items[c["id"]]["url"]} for c in rel if c.get("payer_cost")]
json.dump(out, open(H / "results.json", "w"), indent=1, ensure_ascii=False, default=dict)
print("read", out["items_read"], "relevant", out["relevant"], "wanted break, no help", out["wanted_break_no_help"]["n"])
for h, v in out["help"].items(): print(f"  {h:45} {v['posts']:4}  {v['status']}")
print("barriers:"); [print(f"  {b:50} {v['n']}") for b, v in list(out["barriers_all"].items())[:15]]
