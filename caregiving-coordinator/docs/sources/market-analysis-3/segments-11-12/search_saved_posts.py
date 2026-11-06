"""Market analysis update (2026-11-04): search the saved Reddit posts for segments 11 (respite care and adult day
services) and 12 (caregiver mental health and burnout support). No new fetching: reads only the Arctic Shift
downloads in docs/sources/reddit/arctic-shift-2026-11-03/ (49,315 posts).
Writes:
  term-counts.json   posts matching each term, by source file
  matches.jsonl      one line per matching post: key, reddit link, community, date, terms, and a short excerpt
                     around each match, so every count can be opened and checked.
Word patterns are listed below. Physical, occupational, speech and respiratory therapy are excluded from "therapist".
"Calm" and "Headspace" are ordinary words, so they only count next to app words."""
import json, re, pathlib, collections
SRC = pathlib.Path(__file__).parents[2] / "reddit" / "arctic-shift-2026-11-03"
OUT = pathlib.Path(__file__).parent
TERMS = {
 # segment 11
 "respite": r"\brespite\b",
 "adult day program or center": r"\badult day\b|\badult daycare\b|\badult day ?care\b|\bday program\b|\bsenior day ?care\b|\bmemory care day\b",
 # segment 12
 "therapist or counselor (for the caregiver)": r"(?<!physical )(?<!occupational )(?<!speech )(?<!respiratory )\b(therapist|counselor|counsellor|counseling|counselling)\b",
 "caregiver support group": r"\bsupport groups?\b",
 "Calm app": r"\bcalm app\b|\bcalm\.com\b|\bthe calm app\b",
 "Headspace app": r"\bheadspace app\b|\bheadspace\.com\b|\b(use|used|using|try|tried|trying) headspace\b",
 "Talkspace": r"\btalkspace\b",
 "BetterHelp": r"\bbetterhelp\b",
 "Sanvello": r"\bsanvello\b",
 "ianacare": r"\biana ?care\b",
 "meditation app": r"\bmeditation apps?\b",
 # size reference
 "burnout words (reference)": r"\bburn(ed|t)? ?out\b|\bburnout\b",
}
RX = {k: re.compile(v, re.I) for k, v in TERMS.items()}
counts = {k: collections.Counter() for k in TERMS}
total = collections.Counter()
with open(OUT / "matches.jsonl", "w") as out:
    for fname in ["posts.jsonl", "posts_targeted.jsonl"]:
        for line in open(SRC / fname):
            p = json.loads(line); total[fname] += 1
            t = p.get("text") or ""
            hits = {}
            for k, rx in RX.items():
                m = rx.search(t)
                if m:
                    counts[k][fname] += 1
                    hits[k] = re.sub(r"\s+", " ", t[max(0, m.start() - 150): m.end() + 150])
            if any(k != "burnout words (reference)" for k in hits):
                out.write(json.dumps({"key": p["key"], "url": p["url"], "subreddit": p["subreddit"], "date": p["created"], "terms": sorted(hits), "excerpts": hits}, ensure_ascii=False) + "\n")
res = {"posts_searched": dict(total), "patterns": TERMS, "counts": {k: {**dict(v), "total": sum(v.values())} for k, v in counts.items()}}
json.dump(res, open(OUT / "term-counts.json", "w"), indent=1)
for k, v in res["counts"].items(): print(f"{k:45} {v['total']:6}   (main {v.get('posts.jsonl',0)}, other communities {v.get('posts_targeted.jsonl',0)})")
print("posts searched:", dict(total))
