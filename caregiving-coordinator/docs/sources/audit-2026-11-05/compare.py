"""Compares the blind second reads (audits 1-3) with the original codes. Writes compare-results.json."""
import json, pathlib, collections
H = pathlib.Path(__file__).parent; R = H.parent / "market-analysis-3/segments-11-12"
codes = {}
for n in range(1, 12):
    for c in json.load(open(R / "codes" / f"codes-{n}.json")): codes[c["id"]] = c
lab = json.load(open(R / "audience-labels.json"))
out = {}
# audit 1: help kinds, status, barriers, wanted_break_no_help
def hk(c):
    hs = set()
    for h in c.get("help", []):
        hs.add("respite" if "respite" in h.lower() else ("named program" if h.startswith("named program") else h))
    return hs
RA = None
try:
    rc = {c["id"]: c for c in json.load(open(H / "recode-codes.json"))}
    rows = []; bar = collections.Counter(); bar_agree = collections.Counter()
    for i, c2 in rc.items():
        c1 = codes[i]
        r = {"id": i, "relevant_same": bool(c1.get("relevant")) == bool(c2.get("relevant"))}
        if c1.get("relevant") and c2.get("relevant"):
            h1, h2 = hk(c1), hk(c2); r["help_jaccard"] = round(len(h1 & h2) / max(1, len(h1 | h2)), 2)
            r["status_same"] = c1.get("status") == c2.get("status")
            r["break_same"] = bool(c1.get("wanted_break_no_help")) == bool(c2.get("wanted_break_no_help"))
            b1 = {b for b in c1.get("barriers", []) if not b.startswith("other")}; b2 = {b for b in c2.get("barriers", []) if not b.startswith("other")}
            for b in b1 | b2:
                bar[b] += 1; bar_agree[b] += (b in b1 and b in b2)
        rows.append(r)
    both = [r for r in rows if "help_jaccard" in r]
    out["audit1"] = {"n": len(rows), "relevant_agree": sum(r["relevant_same"] for r in rows),
        "both_relevant": len(both), "help_full_agree": sum(r["help_jaccard"] == 1 for r in both),
        "help_mean_overlap": round(sum(r["help_jaccard"] for r in both) / max(1, len(both)), 2),
        "status_agree": sum(r["status_same"] for r in both), "break_flag_agree": sum(r["break_same"] for r in both),
        "barrier_agreement": {b: f"{bar_agree[b]} of {bar[b]} posts where either reader named it" for b in sorted(bar, key=lambda b: -bar[b])}, "rows": rows}
except FileNotFoundError: out["audit1"] = "not done"
try:
    rv = json.load(open(H / "relevance-check.json"))
    flips = [x for x in rv if x["relevant"]]
    out["audit2"] = {"n": len(rv), "confirmed_not_relevant": len(rv) - len(flips), "judged_relevant_now": [(x["id"], x["reason"]) for x in flips]}
except FileNotFoundError: out["audit2"] = "not done"
try:
    au = json.load(open(H / "audience-check.json"))
    dis = [(x["id"], lab[x["id"]]["label"], x["cared_for"]) for x in au if lab[x["id"]]["label"] != x["cared_for"]]
    out["audit3"] = {"n": len(au), "agree": len(au) - len(dis), "disagreements": dis}
except FileNotFoundError: out["audit3"] = "not done"
json.dump(out, open(H / "compare-results.json", "w"), indent=1)
for k in ("audit1", "audit2", "audit3"):
    v = out[k]; print(k, {kk: vv for kk, vv in v.items() if kk != "rows"} if isinstance(v, dict) else v)
