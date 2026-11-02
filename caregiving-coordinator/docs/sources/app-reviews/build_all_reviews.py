"""Combine Apple reviews.csv and Google Play JSON files into all-reviews.jsonl with a stable id per review.
id format: a-<n> (Apple, row order in reviews.csv) or g-<app>-<n> (Google Play, order in the saved file)."""
import csv, glob, json, pathlib
HERE = pathlib.Path(__file__).parent
out = []
for i, r in enumerate(csv.DictReader(open(HERE / "reviews.csv"))):
    out.append({"id": f"a-{i}", "store": "apple", "country": r["country"], "group": r["group"], "app": r["app"],
                "stars": int(r["stars"]), "date": r["date"][:10], "title": r["title"], "text": r["text"]})
for f in sorted(glob.glob(str(HERE / "google-play/google-play-reviews-*.json"))):
    d = json.load(open(f)); slug = pathlib.Path(f).stem.replace("google-play-reviews-", "")
    for i, r in enumerate(d["reviews"]):
        out.append({"id": f"g-{slug}-{i}", "store": "google", "country": "us", "group": "", "app": d["app"],
                    "stars": r["stars"], "date": r["date"], "title": "", "text": r["text"]})
with open(HERE / "all-reviews.jsonl", "w") as fh:
    for o in out: fh.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), "reviews written")
