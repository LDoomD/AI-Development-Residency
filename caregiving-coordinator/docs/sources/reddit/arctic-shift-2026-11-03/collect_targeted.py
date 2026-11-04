"""Small targeted top-up (2026-11-03): the full download was stopped once r/CaregiverSupport and
r/AgingParents gave enough data. For the other caregiving/condition communities, fetch only posts
matching a few search words (up to 100 each, since 2023-01-01). Same API, slow pace. No usernames.
Writes posts_targeted.jsonl and log_targeted.txt."""
import json, time, urllib.parse, urllib.request, urllib.error, pathlib
HERE = pathlib.Path(__file__).parent
API = "https://arctic-shift.photon-reddit.com/api"
SUBS = ["dementia", "Alzheimers", "caregivers", "CaregiversOfReddit", "eldercare",
        "Parkinsons", "stroke", "ALS", "MultipleSclerosis", "COPD", "disability"]
QUERIES = ["app", "power of attorney", "wish there was", "siblings help", "burnout caregiver"]
log = open(HERE / "log_targeted.txt", "a")
def call(params):
    url = f"{API}/posts/search?" + urllib.parse.urlencode(params)
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "caregiving-discovery-research/0.2 (slow)"})
            with urllib.request.urlopen(req, timeout=120) as r: d = json.load(r)
        except urllib.error.HTTPError as e:
            try: d = json.load(e)
            except Exception: d = {"error": f"HTTP {e.code}"}
        except Exception as e: d = {"error": str(e)}
        if not d.get("error"): time.sleep(5); return d.get("data") or []
        log.write(f"retry {attempt+1}: {d['error']} :: {url}\n"); log.flush(); time.sleep(30*(attempt+1))
    log.write(f"GAVE UP :: {url}\n"); log.flush(); return None
day = lambda t: time.strftime("%Y-%m-%d", time.gmtime(t))
seen = set()
with open(HERE / "posts_targeted.jsonl", "w") as out:
    for sub in SUBS:
        for q in QUERIES:
            rows = call({"subreddit": sub, "query": q, "after": "2023-01-01", "limit": 100,
                         "fields": "id,title,selftext,created_utc,subreddit,num_comments"})
            log.write(f"{sub} '{q}': {'FAILED' if rows is None else len(rows)}\n"); log.flush()
            for x in rows or []:
                if x["id"] in seen: continue
                seen.add(x["id"])
                out.write(json.dumps({"key": "p"+x["id"], "type": "post", "subreddit": x["subreddit"], "created": day(x["created_utc"]),
                    "url": f"https://www.reddit.com/r/{x['subreddit']}/comments/{x['id']}/", "num_comments": x.get("num_comments"),
                    "matched_query": q, "text": (x.get("title") or "") + "\n\n" + (x.get("selftext") or "")}, ensure_ascii=False) + "\n")
log.write("DONE\n")
