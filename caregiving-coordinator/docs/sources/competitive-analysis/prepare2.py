"""manifest2.json for the problem 5, 6, 7 companies: saved page text files over 1.5 KB; App Store descriptions for sites that disallow fetching (Talkspace, Included Health)."""
import json, pathlib
SRC = pathlib.Path(__file__).resolve().parent.parent; HERE = pathlib.Path(__file__).parent
FOLDERS = {"A Place for Mom":"competitors/a-place-for-mom","Caring.com":"competitors/caring-com","Papa":"competitors/papa","Honor":"competitors/honor","Cariloop":"competitors/cariloop","Wellthy":"competitors/wellthy",
 "Calm":"competitors-2/calm","Headspace":"competitors-2/headspace","BetterHelp":"competitors-2/betterhelp","Alight":"competitors-2/alight","Accolade":"competitors-2/accolade","Rightway":"competitors-2/rightway"}
exact = {}
for r in json.load(open(SRC / "competitors-2/save_log2.json")):
    if r.get("file"): exact["competitors-2/" + r["file"].replace(".html", ".txt")] = r.get("final_url") or r["url"]
m = {}
for co, d in FOLDERS.items():
    fs = []
    for t in sorted((SRC / d).glob("*.txt")):
        if t.stat().st_size < 1500: continue
        rel = str(t.relative_to(SRC)); fs.append({"txt": rel, "url": exact.get(rel), "bytes": t.stat().st_size})
    m[co] = fs
for co, slug, jf in [("Talkspace","talkspace","app-reviews/lookups/named2-Talkspace_Therapy_.json"),("Included Health","included-health","app-reviews/lookups/named2-Included_Health_.json")]:
    r = json.load(open(SRC / jf))["results"][0]; out = SRC / "competitors-2" / slug; out.mkdir(exist_ok=True)
    f = out / "appstore-description.txt"; f.write_text(f"{r['trackName']} | seller: {r['sellerName']} | store page: {r['trackViewUrl']}\n\n{r['description']}\n")
    m[co] = [{"txt": str(f.relative_to(SRC)), "url": r["trackViewUrl"].split("?")[0], "bytes": f.stat().st_size, "basis": "App Store listing (company site disallows automated fetching)"}]
json.dump(m, open(HERE / "manifest2.json", "w"), indent=1)
for k, v in m.items(): print(k.ljust(16), len(v), "files", [x["txt"].split("/")[-1][:34] for x in v][:3])
