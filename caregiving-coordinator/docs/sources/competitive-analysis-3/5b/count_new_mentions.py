"""Step 5b: find every saved Reddit post (49,315, docs/sources/reddit/arctic-shift-2026-11-03) that names one of the
new competitors. A mention is not use. Writes mentions.json (post key, competitor, url, full text). Re-run: python3 -I count_new_mentions.py"""
import json, re, collections, pathlib
R = pathlib.Path(__file__).resolve().parents[2] / "reddit/arctic-shift-2026-11-03"
P = {"Trualta": r"trualta",
     "Cariloop": r"cariloop",
     "A Place for Mom": r"a place for mom|aplaceformom|\bapfm\b",
     "Geriatric care managers": r"geriatric care manager|aging life care|care manager|eldercare consultant",
     "Alzheimer's Association helpline": r"alz(heimer'?s)? (association )?(help ?line|hotline)|800[- .]?272[- .]?3900|alz\.org|alzheimer'?s association",
     "Eldercare Locator and Area Agencies on Aging": r"eldercare locator|area agency on aging|area agencies on aging|\baaa\b office|council on aging|office on aging",
     "Medicare GUIDE Model": r"\bguide (model|program)\b|guide dementia",
     "Aeroflow Urology": r"aeroflow",
     "Calm": r"\bcalm app\b|calm\.com|\bcalm (meditation|subscription)",
     "Headspace": r"headspace app|\bheadspace\b"}
c = collections.Counter(); out = []; seen = set()
for f in ["posts.jsonl", "posts_targeted.jsonl"]:
    for l in open(R / f):
        d = json.loads(l); t = d["text"].lower()
        if d["key"] in seen: continue
        hit = [k for k, p in P.items() if re.search(p, t)]
        if hit: seen.add(d["key"])
        for k in hit: c[k] += 1; out.append({"key": d["key"], "competitor": k, "subreddit": d["subreddit"], "url": d["url"], "created": d["created"], "text": d["text"]})
json.dump(out, open(pathlib.Path(__file__).parent / "mentions.json", "w"), indent=1, ensure_ascii=False)
for k in P: print(f"{k}: {c[k]}")
