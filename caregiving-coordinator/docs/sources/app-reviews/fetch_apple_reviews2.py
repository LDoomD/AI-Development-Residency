"""Second batch of Apple reviews (apps for problems 5, 6, 7). Same public feed and rules as fetch_apple_reviews.py. Raw files go to raw/us/ (gitignored: reviewer usernames).
Writes reviews2.csv (no usernames) and all-reviews2.jsonl with ids b-N."""
import csv, json, pathlib, time, urllib.request
ROOT = pathlib.Path(__file__).parent; RAW = ROOT / "raw" / "us"; RAW.mkdir(parents=True, exist_ok=True)
APPS = [(571800810,"calm"),(493145008,"headspace"),(661829386,"talkspace"),(995252384,"betterhelp"),(1534367732,"alight"),(1203452254,"accolade"),
        (907304333,"included-health"),(1294810240,"rightway"),(1498121212,"wellthy"),(1000013390,"honor-family"),(1534207289,"papa-care"),(1450405352,"cariloop")]
for aid, name in APPS:
    for p in range(1, 11):
        f = RAW / f"{aid}-{name}-p{p}.json"
        if f.exists(): continue
        try: raw = urllib.request.urlopen(f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={aid}/sortby=mostrecent/json", timeout=30).read()
        except Exception as ex: print("STOP", name, p, ex); break
        f.write_bytes(raw); ents = json.loads(raw).get("feed", {}).get("entry", []); ents = ents if isinstance(ents, list) else [ents]
        n = sum(1 for e in ents if "im:rating" in e); print(name, "page", p, n, flush=True); time.sleep(1.2)
        if n < 50: break
meta = {str(a): n for a, n in APPS}; rows = []
for f in sorted(RAW.glob("*.json")):
    aid = f.name.split("-")[0]
    if aid not in meta: continue
    ents = json.loads(f.read_text()).get("feed", {}).get("entry", []); ents = ents if isinstance(ents, list) else [ents]
    for e in ents:
        if "im:rating" in e: rows.append([meta[aid], aid, e["im:rating"]["label"], e["title"]["label"], e["content"]["label"], e.get("updated", {}).get("label", "")[:10], f.name])
with open(ROOT / "reviews2.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["app","app_id","stars","title","text","date","source_file"]); w.writerows(rows)
with open(ROOT / "all-reviews2.jsonl", "w") as fh:
    for i, r in enumerate(rows): fh.write(json.dumps({"id": f"b-{i}", "store": "apple", "country": "us", "group": "", "app": r[0], "stars": int(r[2]), "date": r[5], "title": r[3], "text": r[4]}, ensure_ascii=False) + "\n")
print(len(rows), "reviews written")
