"""Save raw iTunes Search API results (public) for caregiving, senior-safety and watch apps, by country.
Usage: python3 search_apple.py   (writes lookups/search-<country>-<entity>-<term>.json and lookups/summary.csv)"""
import csv, json, time, urllib.parse, urllib.request, pathlib

OUT = pathlib.Path(__file__).parent / "lookups"
OUT.mkdir(exist_ok=True)
COUNTRIES = ["us", "gb", "ca", "au", "de", "jp", "in"]
TERMS = ["family caregiver", "carer elderly parent", "senior fall detection", "elderly care family share", "medical alert watch"]
ENTITIES = ["software", "watchSoftware"]
rows = []
for c in COUNTRIES:
    for e in ENTITIES:
        for t in TERMS:
            url = "https://itunes.apple.com/search?" + urllib.parse.urlencode(
                {"term": t, "country": c, "entity": e, "limit": 12})
            name = f"search-{c}-{e}-{t.replace(' ', '_')}.json"
            try:
                raw = urllib.request.urlopen(url, timeout=30).read()
            except Exception as ex:
                print("FAIL", c, e, t, ex); continue
            (OUT / name).write_bytes(raw)
            for r in json.loads(raw).get("results", []):
                rows.append([c, e, t, r.get("trackId"), r.get("trackName"), r.get("sellerName"),
                             r.get("userRatingCount"), r.get("averageUserRating"), r.get("primaryGenreName")])
            time.sleep(1.2)
with open(OUT / "summary.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["country", "entity", "term", "id", "name", "seller", "ratings", "avg", "genre"]); w.writerows(rows)
print(len(rows), "rows")
