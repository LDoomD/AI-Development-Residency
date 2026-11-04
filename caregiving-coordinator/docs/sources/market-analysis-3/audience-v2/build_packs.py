"""Build reading packs for coding use-case moments and wants (2026-11-04).
Reddit: the 304 parent/spouse posts already used for goals (goals/posts-1..3.json).
Forums: the 109 parent/spouse threads the audience page was built from (forum-relevance/motiv-*-items.json), full text from forums/**.txt."""
import json, glob, pathlib
H = pathlib.Path(__file__).parent; S = H.parent.parent
items = []
for i in (1, 2, 3):
    for p in json.load(open(H.parent / f"goals/posts-{i}.json")):
        items.append({"id": p["id"], "source": "reddit", "cared_for": p["cared_for"], "text": p["text"]})
for aud in ("parent", "spouse"):
    ids = set()
    for k in "12":
        ids |= {t["id"] for t in json.load(open(S / f"forum-relevance/motiv-{aud}-{k}-items.json"))}
    for tid in sorted(ids):
        site = "agingcare" if tid.startswith("agi") else "alzconnected"
        path = sorted(glob.glob(str(S / f"forums/{site}/**/{tid.split('-')[1]}.txt"), recursive=True))[0]
        items.append({"id": tid, "source": "forum", "cared_for": "parent" if aud == "parent" else "spouse or partner", "text": open(path).read()})
reddit = [x for x in items if x["source"] == "reddit"]; forum = [x for x in items if x["source"] == "forum"]
packs = [reddit[i::3] for i in range(3)] + [forum[i::3] for i in range(3)]
for n, p in enumerate(packs, 1):
    json.dump(p, open(H / f"pack-{n}.json", "w"), indent=1, ensure_ascii=False)
    print(n, len(p), sum(len(x["text"]) for x in p), {c: sum(x["cared_for"] == c for x in p) for c in ("parent", "spouse or partner")})
