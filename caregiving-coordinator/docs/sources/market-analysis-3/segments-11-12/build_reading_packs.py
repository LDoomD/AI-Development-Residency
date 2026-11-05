"""Builds the reading packs for segments 11 and 12 (2026-11-04). Owner-approved size:
 - every saved Reddit post that mentions respite or adult day (from matches.jsonl)
 - every post found only by the named-program search (named-matches.jsonl, new_to_reading_set)
 - a random 150 of the posts that mention only a support group, and a random 150 that mention only a therapist (seed 20261104)
 - every saved AgingCare and ALZConnected thread that mentions any of the words, as the text around each mention
Post text is copied in full from the saved Arctic Shift files. Writes packs/pack-N.json and packs/manifest.json."""
import json, re, random, glob, pathlib
H = pathlib.Path(__file__).parent; S = H.parents[1]
SRC = S / "reddit" / "arctic-shift-2026-11-03"
posts = {}
for f in ["posts.jsonl", "posts_targeted.jsonl"]:
    for l in open(SRC / f):
        p = json.loads(l); posts[p["key"]] = p
m = [json.loads(l) for l in open(H / "matches.jsonl")]; nm = [json.loads(l) for l in open(H / "named-matches.jsonl")]
RA = {"respite", "adult day program or center"}
pick = {}
for r in m:
    if set(r["terms"]) & RA: pick[r["key"]] = ("respite or adult day", r["terms"])
for r in nm:
    if r["new_to_reading_set"]: pick[r["key"]] = ("named program", r["terms"])
rnd = random.Random(20261104)
sg = sorted(r["key"] for r in m if "caregiver support group" in r["terms"] and not set(r["terms"]) & RA)
th = sorted(r["key"] for r in m if set(r["terms"]) == {"therapist or counselor (for the caregiver)"})
for k in rnd.sample(sg, 150): pick.setdefault(k, ("support group sample", ["caregiver support group"]))
for k in rnd.sample(th, 150): pick.setdefault(k, ("therapist sample", ["therapist or counselor (for the caregiver)"]))
items = [{"id": k, "source": "reddit", "group": g, "url": posts[k]["url"], "community": posts[k]["subreddit"], "date": posts[k]["created"], "matched": t, "text": posts[k]["text"]} for k, (g, t) in pick.items()]
WORDS = re.compile(r"respite|adult day|day program|therapist|counsel(l)?or|counsel(l)?ing|support group", re.I)
for site in ["agingcare", "alzconnected"]:
    for f in sorted(glob.glob(str(S / "forums" / site / "**" / "*.txt"), recursive=True)):
        t = open(f, errors="ignore").read()
        spans = [(max(0, mm.start() - 1500), mm.end() + 1500) for mm in WORDS.finditer(t)]
        if not spans: continue
        merged = []
        for a, b in spans:
            if merged and a <= merged[-1][1]: merged[-1] = (merged[-1][0], max(b, merged[-1][1]))
            else: merged.append((a, b))
        text = "\n[...]\n".join(t[a:b] for a, b in merged)
        items.append({"id": f"{site}-{pathlib.Path(f).stem}", "source": site, "group": "forum thread", "url": str(pathlib.Path(f).relative_to(S)), "community": site, "date": "", "matched": sorted({mm.group(0).lower() for mm in WORDS.finditer(t)}), "text": text})
rnd.shuffle(items)
size = sum(len(i["text"]) for i in items); target = size / 11
(H / "packs").mkdir(exist_ok=True); packs = [[]]; cur = 0
for it in items:
    if cur > target and len(packs) < 11: packs.append([]); cur = 0
    packs[-1].append(it); cur += len(it["text"])
for n, pk in enumerate(packs, 1): json.dump(pk, open(H / "packs" / f"pack-{n}.json", "w"), indent=1, ensure_ascii=False)
from collections import Counter
man = {"items": len(items), "by_group": Counter(i["group"] for i in items), "packs": {f"pack-{n}": {"items": len(pk), "chars": sum(len(i["text"]) for i in pk)} for n, pk in enumerate(packs, 1)}}
json.dump(man, open(H / "packs" / "manifest.json", "w"), indent=1); print(json.dumps(man, indent=1))
