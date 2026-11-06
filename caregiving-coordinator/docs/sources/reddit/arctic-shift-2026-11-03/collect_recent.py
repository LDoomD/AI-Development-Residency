"""Fast top-up (2026-11-03): the archive's word search was too slow (log_targeted.txt), so for each
other caregiving/condition community fetch the newest 500 posts (5 date-paged requests, no word
search) and filter locally like the main communities. Appends to posts_targeted.jsonl. No usernames."""
import json, time, urllib.parse, urllib.request, urllib.error, pathlib
HERE = pathlib.Path(__file__).parent
API = "https://arctic-shift.photon-reddit.com/api"
SUBS = ["dementia", "Alzheimers", "caregivers", "CaregiversOfReddit", "eldercare",
        "Parkinsons", "stroke", "ALS", "MultipleSclerosis", "COPD", "disability"]
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
        if not d.get("error"): time.sleep(4); return d.get("data") or []
        log.write(f"retry {attempt+1}: {d['error']} :: {url}\n"); log.flush(); time.sleep(30*(attempt+1))
    log.write(f"GAVE UP :: {url}\n"); log.flush(); return None
day = lambda t: time.strftime("%Y-%m-%d", time.gmtime(t))
seen = {json.loads(l)["key"] for l in open(HERE/"posts_targeted.jsonl")}
with open(HERE / "posts_targeted.jsonl", "a") as out:
    for sub in SUBS:
        before, n = None, 0
        for _ in range(5):
            p = {"subreddit": sub, "after": "2023-01-01", "limit": 100, "sort": "desc",
                 "fields": "id,title,selftext,created_utc,subreddit,num_comments"}
            if before: p["before"] = before
            rows = call(p)
            if not rows: break
            for x in rows:
                k = "p"+x["id"]
                if k in seen: continue
                seen.add(k); n += 1
                out.write(json.dumps({"key": k, "type": "post", "subreddit": x["subreddit"], "created": day(x["created_utc"]),
                    "url": f"https://www.reddit.com/r/{x['subreddit']}/comments/{x['id']}/", "num_comments": x.get("num_comments"),
                    "matched_query": "newest-500", "text": (x.get("title") or "") + "\n\n" + (x.get("selftext") or "")}, ensure_ascii=False) + "\n")
            before = rows[-1]["created_utc"]
            if len(rows) < 100: break
        log.write(f"recent {sub}: {n}\n"); log.flush()
log.write("RECENT DONE\n")
