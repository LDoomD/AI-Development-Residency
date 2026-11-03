"""Assemble competitive-data.json from extract-1..4.json (company quotes, script-verified against the saved files), urls.json (verified page URLs),
and ../app-reviews/analysis/verified-tags.json (review evidence). Drops weak quotes (headings, labels, testimonials) with a logged reason; expands bare price
quotes to include nearby text from the same file (still an exact substring). Nothing here is typed by hand except the drop list."""
import json, pathlib, re, collections, time, html, urllib.request, urllib.robotparser, urllib.parse
HERE = pathlib.Path(__file__).parent; SRC = HERE.parent
ws = lambda s: re.sub(r"\s+", " ", s).strip()
DROP = {  # (company, field, quote-prefix): reason
 ("Caring Village","differentiation","What makes Caring Village different?"): "heading only, no answer on the page",
 ("FamilyWall","main_features","Budget Tracker"): "bare label",
 ("OMRON connect","price","Premium features for deeper insights:"): "heading, not a price statement",
 ("Aloe Care","differentiation","* One company has a messaging/notes-only app"): "chart footnote, not a differentiation statement",
 ("Medical Guardian","uvp_claim","Trusted by over 600,000+ families."): "duplicate of audience quote",
}
TESTIMONIAL = {("ianacare","shared_access"): "all three are customer testimonials, not company statements", ("Lotsa Helping Hands","shared_access"): None}
log = []; out = []
data = []
for i in range(1, 5): data += json.load(open(HERE / f"extract-{i}.json"))
urls = json.load(open(HERE / "urls.json"))
tags = json.load(open(SRC / "app-reviews/analysis/verified-tags.json"))
APP = {"Caring Village":["caring-village"],"CaringBridge":["caringbridge"],"Lotsa Helping Hands":["lotsa"],"ianacare":["ianacare"],"Cozi":["cozi"],"FamilyWall":["familywall"],"TimeTree":["timetree"],
 "Medisafe":["medisafe"],"MyTherapy":["mytherapy"],"Kin Health":["kin"],"Lively":["lively-link"],"Medical Guardian":["mymedicalguardian"],"Aloe Care":["aloe-care"],"Life360":["life360"],
 "Apple Watch":["apple-watch-app"],"OMRON connect":["omron-connect"],"Withings":["withings"]}
norm = lambda s: s.lower().replace(" ", "-")
def reviews_for(co):
    keys = APP.get(co, []); rows = [t for t in tags if norm(t["app"]) in keys]
    prob = [t for t in rows if t["kind"] == "problem"]; worked = [t for t in rows if t["kind"] == "worked"]
    cats = collections.Counter(t["category"] for t in prob)
    def pick(lst, k=2):
        c = [t for t in lst if t.get("quote") and 40 <= len(t["quote"]) <= 260]; c.sort(key=lambda t: -len(t["quote"])); return [{"quote": t["quote"], "id": t["id"], "store": t["store"], "stars": t["stars"], "date": t["date"]} for t in c[:k]]
    top = cats.most_common(1)[0][0] if cats else None
    return {"reviews_read": len(rows), "problem": len(prob), "worked": len(worked), "top_problem_categories": cats.most_common(3), "problem_quotes": pick([t for t in prob if t["category"] == top]) if top else [], "worked_quotes": pick(worked)}
for c in data:
    co = c["company"]; rec = {"company": co, "fields": {}, "not_found_note": c.get("not_found_note", ""), "reviews": reviews_for(co)}
    for fld, qs in c["fields"].items():
        keep = []
        for q in qs:
            reason = next((r for (cc, ff, pre), r in DROP.items() if cc == co and ff == fld and q["quote"].startswith(pre)), None)
            if (co, fld) == ("ianacare", "shared_access"): reason = "customer testimonial, not a company statement"
            if (co, fld) == ("Lotsa Helping Hands", "shared_access") and q["quote"].startswith("This site enables us"): reason = "customer testimonial, not a company statement"
            text = ws((SRC / q["file"]).read_text(errors="ignore"))
            if ws(q["quote"]) not in text: log.append({"company": co, "field": fld, "quote": q["quote"][:80], "dropped": "NOT an exact substring of its file"}); continue
            if reason: log.append({"company": co, "field": fld, "quote": q["quote"][:80], "dropped": reason}); continue
            qt = ws(q["quote"])
            if fld == "price" and len(qt) < 25 and "$" in qt:  # expand bare prices with nearby exact text
                i = text.find(qt); a = max(0, i - 70); b = min(len(text), i + len(qt) + 40)
                a = text.rfind(" ", 0, a + 1) + 1 if a > 0 else 0; b = text.find(" ", b) if text.find(" ", b) != -1 else len(text)
                qt = text[a:b].strip(); log.append({"company": co, "field": fld, "quote": q["quote"], "expanded_to": qt})
            if qt not in [k["quote"] for k in keep]: keep.append({"quote": qt, "file": q["file"], "url": urls.get(q["file"], {}).get("url"), "url_basis": urls.get(q["file"], {}).get("basis")})
        rec["fields"][fld] = keep
    out.append(rec)
json.dump(out, open(HERE / "competitive-data.json", "w"), indent=1, ensure_ascii=False)
json.dump(log, open(HERE / "assemble-log.json", "w"), indent=1, ensure_ascii=False)
print(len(out), "companies;", sum(len(q) for r in out for q in r["fields"].values()), "quotes kept;", len(log), "log entries")
for l in log: print(l)
for r in out[:0]: pass
nr = sum(1 for r in out for q in r["fields"].values() for k in q if not k["url"]); print(nr, "quotes whose page URL is not verified")
