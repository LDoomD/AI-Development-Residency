"""Count how many downloaded Reddit posts name each competitor or everyday tool (simple keyword match,
2026-11-03). Searches every post in posts.jsonl and posts_targeted.jsonl, so not only caregiver posts.
A mention is not use: "dad refuses Life Alert" counts too. Also counts, among the tagged posts about
relatives' access (column 3), whether the writer cares for a parent or a spouse.
Writes mention-counts.json. Re-run: python3 -I count_mentions.py"""
import json, glob, re, collections, pathlib
HERE = pathlib.Path(__file__).parent
P = {"Caring Village": r"caring village", "CaringBridge": r"caring ?bridge", "Lotsa": r"lotsa", "Everplans": r"everplans",
     "MyChart": r"my ?chart", "Lively/Jitterbug": r"\blively\b|jitterbug", "Medical Guardian": r"medical guardian", "Medisafe": r"medisafe",
     "group chat/text": r"group (chat|text)", "WhatsApp": r"whatsapp", "Google Calendar": r"google calendar",
     "spreadsheet": r"spreadsheet|google sheet", "pill organizer/box": r"pill (organi[sz]er|box)", "whiteboard": r"whiteboard",
     "notebook/binder": r"notebook|binder", "Life Alert": r"life ?alert", "Apple Watch": r"apple watch", "Life360": r"life ?360"}
c, n = collections.Counter(), 0
for f in ["posts.jsonl", "posts_targeted.jsonl"]:
    for l in open(HERE / f):
        t = json.loads(l)["text"].lower(); n += 1
        for k, p in P.items():
            if re.search(p, t): c[k] += 1
TEXT = {}
for f in glob.glob(str(HERE / "tagging/*chunk-*.jsonl")):
    for l in open(f): d = json.loads(l); TEXT[d["key"]] = d["text"].lower()
drop = set()
for f in ["reddit-findings.json", "reddit-findings-other.json"]:
    d = json.load(open(HERE / f))["dropped"]; drop |= set(d["app_maker"] + d["duplicate"])
rows = [json.loads(l) for f in glob.glob(str(HERE / "tagging/*tags-*.jsonl")) for l in open(f)]
acc = [r for r in rows if r.get("caregiver") and r.get("relevant") and r["url"] not in drop and "3" in (r.get("columns") or {})]
rel = collections.Counter()
for r in acc:
    t = TEXT[r["key"]]
    p = bool(re.search(r"\bmy (mom|dad|mother|father|mum|parents?|grand(ma|pa|mother|father)|mil|fil|in-laws?)\b", t))
    s = bool(re.search(r"\bmy (husband|wife|partner|spouse|boyfriend|girlfriend)\b", t))
    rel["parent" if p and not s else "spouse" if s and not p else "both" if p and s else "neither"] += 1
out = {"posts_searched": n, "mentions": dict(c), "access_posts": len(acc), "access_writer": dict(rel),
       "access_by_subreddit": dict(collections.Counter(r["subreddit"] for r in acc))}
json.dump(out, open(HERE / "mention-counts.json", "w"), indent=1)
print(json.dumps(out, indent=1))
