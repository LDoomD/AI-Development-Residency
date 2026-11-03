"""Small sample of Apple reviews for Everplans (all it has, 1 page) and Epic MyChart (200 most recent, 4 pages). Same public feed and rules as fetch_apple_reviews.py.
Raw files go to raw/us/ (gitignored: reviewer usernames). Writes reviews3.csv (no usernames) and all-reviews3.jsonl with ids c-N."""
import csv, json, pathlib, time, urllib.request
ROOT = pathlib.Path(__file__).parent; RAW = ROOT / "raw" / "us"; RAW.mkdir(parents=True, exist_ok=True)
APPS = [(1590237847, "everplans", 1), (382952264, "epic-mychart", 4)]
rows = []
for aid, name, pages in APPS:
    for p in range(1, pages + 1):
        f = RAW / f"{aid}-{name}-p{p}.json"
        if not f.exists():
            f.write_bytes(urllib.request.urlopen(f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={aid}/sortby=mostrecent/json", timeout=30).read()); time.sleep(1.2)
        ents = json.loads(f.read_text()).get("feed", {}).get("entry", []); ents = ents if isinstance(ents, list) else [ents]
        for e in ents:
            if "im:rating" in e: rows.append([name, aid, e["im:rating"]["label"], e["title"]["label"], e["content"]["label"], e.get("updated", {}).get("label", "")[:10], f.name])
with open(ROOT / "reviews3.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["app", "app_id", "stars", "title", "text", "date", "source_file"]); w.writerows(rows)
with open(ROOT / "all-reviews3.jsonl", "w") as fh:
    for i, r in enumerate(rows): fh.write(json.dumps({"id": f"c-{i}", "store": "apple", "country": "us", "group": "", "app": r[0], "stars": int(r[2]), "date": r[5], "title": r[3], "text": r[4]}, ensure_ascii=False) + "\n")
print(len(rows), "reviews written")
