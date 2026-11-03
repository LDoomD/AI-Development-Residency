"""Cut the competitive table to ten rows (the template asks for the top 5 to 7 direct competitors plus any indirect ones) and recompute
the review columns from caregiving-only reviews (relevance-final.json). The other rows stay in table-rows.json and competitive-data.json."""
import json, pathlib, re, ast, collections
HERE = pathlib.Path(__file__).parent; AR = HERE.parent / "app-reviews/analysis"
rows = json.load(open(HERE / "table-rows.json"))
src = (HERE / "compose.py").read_text()
CATLABEL = ast.literal_eval(re.search(r"CATLABEL = (\{.*?\})\n", src, re.S).group(1))
KEEP = ["Caring Village","CaringBridge","Lotsa Helping Hands","Medisafe","Everplans","Epic MyChart","Lively","Medical Guardian","Group texts","Paper notebook and visit log"]
APP = {"Caring Village":["caring-village"],"CaringBridge":["caringbridge"],"Lotsa Helping Hands":["lotsa-helping-hands"],"Medisafe":["medisafe"],"Lively":["lively-link"],"Medical Guardian":["mymedicalguardian"]}
tags = json.load(open(AR / "verified-tags.json")); rel = json.load(open(AR / "relevance-final.json"))
tags = [t for t in tags if rel.get(t["id"], {}).get("relevance") == "caregiving" and t.get("quote_verified")]
norm = lambda s: s.lower().replace(" ", "-")
cut = lambda s, n: (lambda s: s if len(s) <= n else s[:n].rstrip() + "...")(re.sub(r"\s+", " ", s).strip())
def pick(lst):
    c = [t for t in lst if t.get("quote") and 40 <= len(t["quote"]) <= 260]; c.sort(key=lambda t: -len(t["quote"])); return c[:1]
out = []
for name in KEEP:
    r = next(x for x in rows if x[0] == name); r = list(r)
    if name in APP:
        rs = [t for t in tags if norm(t["app"]) in APP[name]]
        prob = [t for t in rs if t["kind"] == "problem"]; worked = [t for t in rs if t["kind"] == "worked"]
        cats = collections.Counter(t["category"] for t in prob).most_common(3); top = cats[0][0] if cats else None
        q = lambda t: f"• \"{cut(t['quote'],150)}\" (review {t['id']})"
        r[6] = "\n".join(q(t) for t in pick(worked)) or "No caregiving-only 'worked' quote in the sample"
        r[7] = "\n".join(q(t) for t in pick([t for t in prob if t['category'] == top])) if top else "No caregiving-only problem quote in the sample"
        cs = ", ".join(f"{CATLABEL[c]} ({n})" for c, n in cats[:2]) or "none"
        r[8] = f"{len(rs)} app-store reviews where the reviewer is clearly caring for or helping a relative (reviews that mention a caregiving or family word were read, then filtered one by one): {len(prob)} describe a problem, {len(worked)} describe something that worked. Most common problems: {cs}." if rs else "No caregiving-only reviews in the sample"
        tl = [CATLABEL[c] for c, n in cats[:2]]
        tail = r[9].split("; ", 1)[1] if r[9].startswith("Reading (mine, from the evidence in this row): reviewers raise") else r[9].replace("Reading (mine, from the evidence in this row): ", "")
        r[9] = "Reading (mine, from the evidence in this row): " + ("reviewers raise " + " and ".join(tl) + "; " if tl else "") + tail
    out.append(r)
# Small separate samples for two apps that were not in the main collection (analysis/sample3-tags.json; reviews3.csv). Not part of the 439 count.
SAMPLE = {
 "Everplans": ["No caregiving-only 'worked' quote in the sample", "No caregiving-only problem quote in the sample",
   "Small separate sample: all 8 Apple reviews the store feed returns for this app were read; none is clearly about caring for a relative (1 is about settling a late father's estate and was left out as unclear). No Google Play reviews collected. Not part of the 439 count.", None],
 "Epic MyChart": ["• \"now I can include and manage my mother’s account without switching\" (review c-123)", "• \"Taking away a parents legal right to have accessibility to minor child’s chart\" (review c-152)",
   "Small separate sample: the 200 most recent Apple reviews were read (13 mention a family word); 4 are clearly about caring for a relative: 2 describe a problem (access to a minor child's chart; records 2-3 days behind during a family member's hospitalization) and 2 describe something that worked. Not part of the 439 count.",
   "reviewers raise access or logins for another person and data not syncing; "],
}
for r in out:
    if r[0] in SAMPLE:
        v = SAMPLE[r[0]]; r[6], r[7], r[8] = v[0], v[1], v[2]
        if v[3]: r[9] = r[9].replace("Reading (mine, from the evidence in this row): ", "Reading (mine, from the evidence in this row): " + v[3])
json.dump(out, open(HERE / "table-rows-10.json", "w"), ensure_ascii=False)
for r in out: print(r[0], "|", r[8][:150].replace("\n", " "))
