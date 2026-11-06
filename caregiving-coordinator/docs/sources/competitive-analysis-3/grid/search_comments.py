"""Search Arctic Shift for every comment and post naming Everplans or Cariloop in caregiver communities.
Usernames dropped. Writes reddit-threads/search_<word>.json (each item has its reddit.com link)."""
import json, time, urllib.request, urllib.parse, pathlib
OUT = pathlib.Path(__file__).parent / "reddit-threads"; API = "https://arctic-shift.photon-reddit.com/api"
SUBS = ["AgingParents", "CaregiverSupport", "dementia", "Alzheimers", "caregivers", "CaregiversOfReddit", "eldercare", "personalfinance", "EstatePlanning", "LifeProTips", "AskHR", "humanresources"]
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "residency-research-script"}), timeout=60))
for word in ["everplans", "cariloop"]:
    found = []
    for sub in SUBS:
        for kind, field in (("comments", "body"), ("posts", "query")):
            q = urllib.parse.urlencode({"subreddit": sub, field: word, "limit": 100})
            try: data = get(f"{API}/{kind}/search?{q}")["data"]
            except Exception as e: print("fail", word, sub, kind, e); continue
            for d in data:
                text = d.get("body") or (d.get("title", "") + "\n" + d.get("selftext", ""))
                link = "https://www.reddit.com" + (d.get("permalink") or f"/r/{sub}/comments/{d.get('link_id','')[3:]}/_/{d['id']}/")
                found.append({"kind": kind, "subreddit": sub, "id": d["id"], "date": time.strftime('%Y-%m-%d', time.gmtime(d["created_utc"])), "link": link, "text": text})
            time.sleep(0.5)
    (OUT / f"search_{word}.json").write_text(json.dumps(found, indent=1, ensure_ascii=False))
    print(word, len(found), {s: sum(1 for f in found if f["subreddit"] == s) for s in SUBS})
