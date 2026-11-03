"""What works, from caregiving-only reviews that describe something that worked (kind = worked, relevance = caregiving). Themes are assigned by keyword rules, so a review can count in more than one theme; counts are approximate."""
import json, re, collections, pathlib
HERE = pathlib.Path(__file__).parent
t = json.load(open(HERE / "verified-tags.json")); rel = json.load(open(HERE / "relevance-final.json"))
n = lambda s: s.lower().replace(" ", "-")
APPS = {"CaringBridge": ["caringbridge"], "Caring Village": ["caring-village"], "Lotsa Helping Hands": ["lotsa-helping-hands"], "Medisafe": ["medisafe"], "Lively": ["lively-link"], "Medical Guardian": ["mymedicalguardian"]}
THEMES = {
 "updates": ("One update reaches everyone, with fewer repeated calls and texts", r"updat|inform|in the loop|up to date|same time|same info|once\b|one post|one message|1 message|timely|notif"),
 "organized": ("Everyone on the same page: organizing, tasks, schedules, chat", r"same page|organiz|coordinat|centraliz|delegat|schedul|tasks|back and forth|chat|team|connected"),
 "meds": ("Medication help: reminders, lists, not missing a dose", r"medic|\bmeds\b|pills|\bdose|compliance"),
 "where": ("Knowing where they are and that they are OK (peace of mind)", r"where|locat|track|check in|peace of mind|reassur|anxious|keep tabs|\bis ok|\bam ok|safe\b|know she|know he|knowing"),
 "emergency": ("Fast emergency help", r"operator|EMS|\bfall|emergency|rapid|response|help arrives|connected to"),
 "easy": ("Easy to use or set up", r"easy|simple|set up|no issues|effective|intuitive"),
}
W = [x for x in t if x["kind"] == "worked" and rel.get(x["id"], {}).get("relevance") == "caregiving" and x.get("quote_verified")]
out = {}
for co, keys in APPS.items():
    rs = [x for x in W if n(x["app"]) in keys]; res = {"reviews": len(rs), "themes": {}}
    for k, (lbl, rx) in THEMES.items():
        m = [x for x in rs if re.search(rx, x["quote"], re.I)]
        pk = sorted([x for x in m if 40 <= len(x["quote"]) <= 200], key=lambda x: -len(x["quote"]))[:1]
        res["themes"][k] = {"label": lbl, "count": len(m), "example": [{"quote": x["quote"], "id": x["id"]} for x in pk]}
    out[co] = res
json.dump(out, open(HERE / "worked-themes.json", "w"), ensure_ascii=False, indent=1)
for co, r in out.items(): print(co, r["reviews"], {k: v["count"] for k, v in r["themes"].items()})
