"""Select reviews that mention a caregiving or family context (regex below) and split them into 4 slices of similar length.
The regex is the selection rule: reviews that do not match were NOT read for this analysis."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
CARE = re.compile(r"\b(mom|mother|dad|father|parents?|grandm\w+|grandf\w+|grandp\w+|elderly|elder|caregiver\w*|caretaker|care ?giv\w+|my (wife|husband|spouse|aunt|uncle|sister|brother|son|daughter|family)|dementia|alzheimer\w*|senior|seniors|aging|aged|nursing home|assisted living|hospice|stroke|parkinson\w*|my family|family members?|loved one)\b", re.I)
rows = [json.loads(l) for l in open(HERE.parent / "all-reviews.jsonl")]
sub = [r for r in rows if CARE.search(r["title"] + " " + r["text"])]
total = sum(len(r["text"]) + len(r["title"]) for r in sub); per = total / 4; cur = 0; k = 0; buckets = [[] for _ in range(4)]
for r in sub:
    buckets[min(k, 3)].append(r); cur += len(r["text"]) + len(r["title"])
    if cur > per * (k + 1): k += 1
for i, b in enumerate(buckets, 1):
    with open(HERE / "slices" / f"slice-{i}.jsonl", "w") as fh:
        for r in b: fh.write(json.dumps({k2: r[k2] for k2 in ("id", "app", "store", "stars", "date", "title", "text")}, ensure_ascii=False) + "\n")
    print(f"slice-{i}", len(b), "reviews")
