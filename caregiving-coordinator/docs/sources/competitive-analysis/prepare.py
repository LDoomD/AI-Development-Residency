"""Build manifest.json: for each competitor, the saved page text files (over 1.5 KB) with the page URL (canonical or og:url read from the saved HTML;
otherwise reconstructed from the file name and flagged). For three companies whose sites disallow automated fetching (robots.txt) the company's own
App Store description (saved iTunes lookup JSON) is written to a text file and used instead."""
import json, pathlib, re, html
SRC = pathlib.Path(__file__).resolve().parent.parent
HERE = pathlib.Path(__file__).parent
WANT = {"Caring Village":"caring-village","CaringBridge":"caringbridge","Lotsa Helping Hands":"lotsa-helping-hands","ianacare":"ianacare","Cozi":"cozi","FamilyWall":"familywall","TimeTree":"timetree",
 "Medisafe":"medisafe","MyTherapy":"mytherapy","Kin Health":"kin-health","Everplans":"everplans","Trustworthy":"trustworthy","Keeper":"keeper","Epic MyChart":"epic-mychart",
 "Lively":"lively","Medical Guardian":"medical-guardian","Aloe Care":"aloe-care","Apple Watch":"apple-watch"}
def url_of(htmlpath, txtname):
    try:
        h = htmlpath.read_text(errors="ignore")[:200000]
        m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', h) or re.search(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']canonical', h) or re.search(r'property=["\']og:url["\'][^>]*content=["\']([^"\']+)', h) or re.search(r'content=["\']([^"\']+)["\'][^>]*property=["\']og:url', h)
        if m and m.group(1).startswith("http"): return html.unescape(m.group(1)), "canonical"
    except Exception: pass
    return "https://" + txtname[:-4].replace("_", "/", 1).replace("_", ".", 0), "reconstructed-from-file-name"
manifest = {}
for name, slug in WANT.items():
    files = []
    for base in ("competitors", "competitors-2"):
        d = SRC / base / slug
        if not d.exists(): continue
        for t in sorted(d.glob("*.txt")):
            if t.stat().st_size < 1500: continue
            u, how = url_of(t.with_suffix(".html"), t.name)
            files.append({"txt": str(t.relative_to(SRC)), "url": u, "url_basis": how, "bytes": t.stat().st_size})
    manifest[name] = files
# App Store descriptions for sites that disallow fetching
for name, slug, jf in [("Life360","life360","app-reviews/lookups/named-Life360.json"),("OMRON connect","omron","app-reviews/lookups/Omron_connect.json"),("Withings","withings","app-reviews/lookups/Withings_Health_Mate.json")]:
    d = json.load(open(SRC / jf))["results"]; r = d[0]
    out = SRC / "competitors-2" / slug; out.mkdir(exist_ok=True)
    f = out / "appstore-description.txt"
    f.write_text(f"{r['trackName']} | seller: {r['sellerName']} | store page: {r['trackViewUrl']}\n\n{r['description']}\n")
    manifest[name] = [{"txt": str(f.relative_to(SRC)), "url": r["trackViewUrl"].split("?")[0], "url_basis": "App Store listing (company's own description; company website disallows automated fetching)", "bytes": f.stat().st_size}]
manifest["1Password"] = []
json.dump(manifest, open(HERE / "manifest.json", "w"), indent=1)
for k, v in manifest.items(): print(k.ljust(20), len(v), "files;", ", ".join(x["url_basis"][:9] for x in v[:3]))
