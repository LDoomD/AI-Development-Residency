"""Review evidence per company and feature column for the feature comparison table (docs/feature-analysis.md, step 3).
Caregiving-only reviews (relevance-final.json == caregiving). "Worked" reviews are matched to a column by the keyword themes in
worked_themes.py; "problem" reviews by their category tag. A review can count in more than one column. Label rule: at least two
thirds worked = "Mostly works"; at least two thirds problems = "Mostly problems"; otherwise "Mixed"; fewer than 5 matching reviews =
"Too few reviews to judge". Run: python3 feature_ratings.py"""
import json, re, pathlib
from worked_themes import THEMES
HERE = pathlib.Path(__file__).parent
t = json.load(open(HERE / "verified-tags.json")); rel = json.load(open(HERE / "relevance-final.json"))
APPS = {"Caring Village": ["caring-village"], "CaringBridge": ["caringbridge"], "Lotsa Helping Hands": ["lotsa-helping-hands"],
        "Lively": ["lively-link"], "Medical Guardian": ["mymedicalguardian"], "Medisafe": ["medisafe"], "Epic MyChart": ["epic-mychart"]}
COLS = {
 1: (["organized"], ["not_syncing", "reminders_failing"]),
 2: (["updates"], ["alerts_unreliable", "not_syncing", "family_cant_see_same_info", "app_reliability"]),
 3: ([], ["access_for_others", "family_cant_see_same_info"]),
 4: (["meds"], ["reminders_failing", "alerts_unreliable", "family_cant_see_same_info", "not_syncing"]),
 6: ([], []),
 7: (["where", "emergency"], ["readings_wrong", "alerts_unreliable", "safety_gap"]),
}
# Reviews and forum posts collected 2026-11-03, tagged per column (see extra-tags-2026-11-03.json).
EXTRA = json.load(open(HERE / "extra-tags-2026-11-03.json"))["sources"]
APPNAME = {"Lotsa Helping Hands": "Lotsa Helping Hands", "Epic MyChart": "Epic MyChart", "CaringBridge": "CaringBridge", "Lively": "Lively", "Medical Guardian": "Medical Guardian"}
n = lambda s: s.lower().replace(" ", "-")
care = [x for x in t if rel.get(x["id"], {}).get("relevance") == "caregiving" and x.get("quote_verified")]
out = {}
for co, keys in APPS.items():
    rs = [x for x in care if n(x["app"]) in keys]; out[co] = {}
    for col, (themes, cats) in COLS.items():
        w = {x["id"] for x in rs if x["kind"] == "worked" and any(re.search(THEMES[k][1], x["quote"], re.I) for k in themes)}
        p = {x["id"] for x in rs if x["kind"] == "problem" and x["category"] in cats}
        tot = len(w) + len(p)
        lab = ("Too few reviews to judge" if tot < 5 else "Mostly works" if len(w) * 3 >= tot * 2
               else "Mostly problems" if len(p) * 3 >= tot * 2 else "Mixed")
        out[co][col] = {"worked": len(w), "problems": len(p), "total": tot, "label": lab}
# add the 2026-11-03 tags, skipping reviews whose text is already in the older saved file
for src, d in EXTRA.items():
    path = HERE.parent / src
    items = json.load(open(path)); items = items.get("reviews") or items.get("threads")
    old = set()
    if d.get("dedupe_against"):
        old = {r["text"].strip() for r in json.load(open(HERE.parent / d["dedupe_against"]))["reviews"]}
    for i, cols in d["tags"].items():
        it = items[int(i)]
        dup = it.get("text", "").strip() in old
        co = cols.get("app") if d.get("app_by_thread") else d["app"]
        for col, v in cols.items():
            if col == "app": continue
            # a review already in the older file was counted by the old rules; only add what those rules
            # cannot see: a "worked" vote for columns 3 and 6, which have no worked keyword theme
            if dup and not (v == "W" and col in ("3", "6")): continue
            c = out[co].setdefault(int(col), {"worked": 0, "problems": 0})
            c["worked" if v == "W" else "problems"] += 1
for co, d in out.items():
    for col, c in d.items():
        tot = c["worked"] + c["problems"]; w, p = c["worked"], c["problems"]
        c["total"] = tot
        c["label"] = ("Too few reviews to judge" if tot < 5 else "Mostly works" if w * 3 >= tot * 2
                      else "Mostly problems" if p * 3 >= tot * 2 else "Mixed")
json.dump(out, open(HERE / "feature-ratings.json", "w"), indent=1)
for co, d in out.items(): print(co, {c: f'{v["label"]} {v["worked"]}/{v["total"]}' for c, v in sorted(d.items())})
