"""Check every quote and review id in the 'Summarize the unique value opportunities' table against the saved originals, and recompute its numbers."""
import json, re, pathlib, collections, glob
D = pathlib.Path(__file__).resolve().parents[2]; SRC = D / "sources"
ws = lambda s: re.sub(r"\s+", " ", s).strip()
sec = (D / "competitive-analysis.md").read_text(); sec = sec[sec.index("## Summarize the unique value opportunities"):]
rev = {}
for f in ("all-reviews.jsonl", "all-reviews2.jsonl", "all-reviews3.jsonl"):
    for l in (SRC / "app-reviews" / f).read_text().splitlines():
        r = json.loads(l); rev[r["id"]] = ws(r["title"] + " " + r["text"]) + " || " + ws(r["title"]) + " || " + ws(r["text"])
pages = {p.name + "|" + p.parent.name: ws(p.read_text(errors="ignore")) for p in list((SRC / "competitors").glob("*/*.txt")) + list((SRC / "competitors-2").glob("*/*.txt"))}
allpages = " ".join(pages.values())
bad = 0
print("== quotes with a review id")
for m in re.finditer(r'"([^"]{8,}?)" \(((?:a|b|c|g)-[a-z0-9-]*\d+)\)', sec):
    q, i = m.group(1), m.group(2)
    ok = i in rev and ws(q) in rev[i]; bad += not ok
    print("OK  " if ok else "FAIL", i, q[:70])
print("== company quotes")
for m in re.finditer(r'"([^"]{12,}?)"(?: \((?:Caring Village|CaringBridge)\))?', sec):
    q = m.group(1)
    if re.search(r"\((?:a|b|c|g)-", sec[m.end():m.end() + 14]): continue
    if any(ws(q) in rv for rv in rev.values()): continue
    ok = ws(q).rstrip(".") in allpages; bad += not ok
    print("OK  " if ok else "FAIL", "page:", q[:70])
print("== numbers from reviews")
t = json.load(open(SRC / "app-reviews/analysis/verified-tags.json")); rel = json.load(open(SRC / "app-reviews/analysis/relevance-final.json"))
n = lambda s: s.lower().replace(" ", "-")
cg = [x for x in t if rel.get(x["id"], {}).get("relevance") == "caregiving" and x.get("quote_verified")]
TEN = ("caringbridge", "caring-village", "lotsa-helping-hands", "medisafe", "lively-link", "mymedicalguardian")
W = [x for x in cg if x["kind"] == "worked" and n(x["app"]) in TEN]
P = [x for x in cg if x["kind"] == "problem"]
cnt = lambda a, k: sum(1 for x in W if n(x["app"]) == a)
tm = json.load(open(SRC / "app-reviews/analysis/worked-themes.json"))
print("worked reviews, ten-row apps:", len(W), "(table says 138)")
print("access mentions:", sum(1 for x in W if re.search(r"access|permission|specify|grant|invite|only those", x["quote"], re.I)), "(3)")
print("Lively worked", cnt("lively-link", 0), "where", tm["Lively"]["themes"]["where"]["count"], "(34, 23)")
print("emergency Lively+MG", tm["Lively"]["themes"]["emergency"]["count"] + tm["Medical Guardian"]["themes"]["emergency"]["count"], "of", cnt("lively-link", 0) + cnt("mymedicalguardian", 0), "(6 of 42)")
print("CaringBridge updates", tm["CaringBridge"]["themes"]["updates"]["count"], "of", tm["CaringBridge"]["reviews"], "(42 of 61)")
print("Caring Village organized", tm["Caring Village"]["themes"]["organized"]["count"], "of", tm["Caring Village"]["reviews"], "(14 of 22)")
print("Medisafe meds", tm["Medisafe"]["themes"]["meds"]["count"], "of", tm["Medisafe"]["reviews"], "(5 of 12)")
lm = [x for x in P if n(x["app"]) in ("lively-link", "mymedicalguardian")]
print("Lively+MG problem", len(lm), collections.Counter(x["category"] for x in lm).most_common(3), "(114; 42 readings, 18 safety)")
co = [x for x in P if n(x["app"]) in ("caring-village", "caringbridge", "lotsa-helping-hands")]
print("coordination problems", len(co), collections.Counter(x["category"] for x in co).most_common(1), "(25; crashes 11)")
print("all problems", len(P), "access", sum(1 for x in P if x["category"] == "access_for_others"), "(192, 14)")
print("MISSING/FAILED quotes:", bad)
