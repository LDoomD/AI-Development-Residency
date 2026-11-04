"""Collect Reddit data from caregiver subreddits through the Arctic Shift archive API
(https://arctic-shift.photon-reddit.com, public, no login). Run 2026-11-03 for the feature analysis.
Phase 1: every post since 2023-01-01 in each subreddit (paged by date), searched locally afterwards.
Phase 2: comment search by app name only (the archive's full-text search is slow, so kept small).
Slow pace with back-off, because the first try was rate limited (log-first-try-rate-limited.txt).
Writes posts.jsonl, comments.jsonl (usernames never requested) and log.txt. Re-run: python3 collect.py"""
import json, time, urllib.parse, urllib.request, pathlib
HERE = pathlib.Path(__file__).parent
API = "https://arctic-shift.photon-reddit.com/api"
SUBS = ["CaregiverSupport", "AgingParents", "dementia", "Alzheimers", "caregivers", "CaregiversOfReddit", "eldercare",
        "Parkinsons", "stroke", "ALS", "MultipleSclerosis", "COPD", "disability"]
APP_TERMS = ["caringbridge", "caring bridge", "caring village", "lotsa", "everplans", "mychart",
             "greatcall", "jitterbug", "lively", "medical guardian", "medisafe"]
START = 1672531200  # 2023-01-01
PACE = 4
log = open(HERE / "log.txt", "a")
def call(path, params):
    url = f"{API}/{path}?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "caregiving-discovery-research/0.2 (slow, one request at a time)"})
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.load(r)
        except urllib.error.HTTPError as e:
            try: d = json.load(e)
            except Exception: d = {"error": f"HTTP {e.code}"}
        except Exception as e:
            d = {"error": str(e)}
        if not d.get("error"):
            time.sleep(PACE); return d.get("data") or []
        wait = 30 * (attempt + 1)
        log.write(f"retry {attempt+1} in {wait}s: {d['error']} :: {url}\n"); log.flush()
        time.sleep(wait)
    log.write(f"GAVE UP :: {url}\n"); log.flush()
    return None
def link(sub, pid, cid=None):
    return f"https://www.reddit.com/r/{sub}/comments/{pid}/" + (f"_/{cid}/" if cid else "")
day = lambda t: time.strftime("%Y-%m-%d", time.gmtime(t))
with open(HERE / "posts.jsonl", "w") as out:
    for sub in SUBS:
        after, n = START, 0
        while True:
            rows = call("posts/search", {"subreddit": sub, "after": after, "limit": 100, "sort": "asc",
                                         "fields": "id,title,selftext,created_utc,subreddit,num_comments"})
            if rows is None: log.write(f"{sub}: stopped at {day(after)}\n"); break
            if not rows: break
            for x in rows:
                out.write(json.dumps({"key": "p" + x["id"], "type": "post", "subreddit": x["subreddit"], "created": day(x["created_utc"]),
                                      "url": link(x["subreddit"], x["id"]), "num_comments": x.get("num_comments"),
                                      "text": (x.get("title") or "") + "\n\n" + (x.get("selftext") or "")}, ensure_ascii=False) + "\n")
            n += len(rows); after = rows[-1]["created_utc"] + 1
            if len(rows) < 100: break
        log.write(f"posts {sub}: {n}\n"); log.flush()
seen = {}
for term in APP_TERMS:
    for sub in SUBS:
        rows = call("comments/search", {"subreddit": sub, "body": term, "after": "2023-01-01", "limit": 100,
                                        "fields": "id,body,created_utc,link_id,subreddit"})
        log.write(f"comments {sub} '{term}': {'FAILED' if rows is None else len(rows)}\n"); log.flush()
        for x in rows or []:
            k = "c" + x["id"]
            if k in seen: seen[k]["matched"].append(term); continue
            seen[k] = {"key": k, "type": "comment", "subreddit": x["subreddit"], "created": day(x["created_utc"]),
                       "url": link(x["subreddit"], x["link_id"].removeprefix("t3_"), x["id"]), "text": x.get("body") or "", "matched": [term]}
with open(HERE / "comments.jsonl", "w") as f:
    for v in seen.values(): f.write(json.dumps(v, ensure_ascii=False) + "\n")
log.write("DONE\n")
