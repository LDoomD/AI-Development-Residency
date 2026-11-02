#!/usr/bin/env python3 -I
"""Find and save public YouTube caregiver videos and their comments with Google's official
YouTube Data API v3. Google's answers are saved byte for byte as .json, so a quote can be
checked against the saved file. The API key is read from ../../../.env (YOUTUBE_API_KEY) and
is never printed or saved.

Usage (run from anywhere):
  python3 -I fetch_youtube.py search
      runs the topic searches, saves raw answers in search-raw/, writes candidates.csv
  python3 -I fetch_youtube.py comments <approved-ids.txt>
      for each video id (one per line) saves video-details and comment pages in comments-raw/<id>/
      and a text extract <id>.txt with commenter names replaced by [member]

Quota (free daily limit 10,000 units): a search costs 100, a comment page or video lookup costs 1.
"""
import csv, html, json, os, re, sys, time, urllib.parse, urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".env"))
API = "https://www.googleapis.com/youtube/v3/"

# Topics chosen from the gaps in the AARP/NAC report and the forum themes; no solution wording.
QUERIES = [
    "caring for aging parent",
    "siblings not helping with elderly parent",
    "caregiver burnout adult child",
    "long distance caregiving for parent",
    "managing elderly parent's medications",
    "power of attorney for elderly parent",
    "dementia caregiver family",
]
PUBLISHED_AFTER = "2023-11-01T00:00:00Z"
MIN_COMMENTS = 100
MAX_PER_CHANNEL = 2
PER_QUERY = 3        # videos kept per query after filters (top of YouTube's relevance order)


def key():
    for line in open(ENV, encoding="utf-8"):
        if line.startswith("YOUTUBE_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("No YOUTUBE_API_KEY in .env")


def call(endpoint, **params):
    params["key"] = key()
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(urllib.request.Request(url), timeout=40) as r:
        return r.read()                      # raw bytes; the key is not in the body


def save(path, raw):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "wb").write(raw)


def cmd_search():
    cands, per_channel, seen = [], {}, set()
    for qi, q in enumerate(QUERIES, 1):
        raw = call("search", part="snippet", type="video", q=q, maxResults=25, order="relevance",
                   relevanceLanguage="en", regionCode="US", publishedAfter=PUBLISHED_AFTER)
        save(os.path.join(HERE, "search-raw", f"q{qi}.json"), raw)
        ids = [i["id"]["videoId"] for i in json.loads(raw)["items"]]
        det = call("videos", part="snippet,statistics", id=",".join(ids))
        save(os.path.join(HERE, "search-raw", f"q{qi}-details.json"), det)
        kept = 0
        for v in json.loads(det)["items"]:           # same order as relevance? re-sort to search order
            pass
        by_id = {v["id"]: v for v in json.loads(det)["items"]}
        for vid in ids:
            v = by_id.get(vid)
            if not v or vid in seen:
                continue
            cc = int(v["statistics"].get("commentCount", 0))
            ch = v["snippet"]["channelId"]
            if cc < MIN_COMMENTS or per_channel.get(ch, 0) >= MAX_PER_CHANNEL:
                continue
            seen.add(vid); per_channel[ch] = per_channel.get(ch, 0) + 1; kept += 1
            cands.append([q, vid, html.unescape(v["snippet"]["title"]), v["snippet"]["channelTitle"],
                          v["snippet"]["publishedAt"][:10], v["statistics"].get("viewCount", ""), cc,
                          "https://www.youtube.com/watch?v=" + vid])
            if kept >= PER_QUERY:
                break
        time.sleep(1)
    with open(os.path.join(HERE, "candidates.csv"), "w", newline="", encoding="utf-8") as o:
        w = csv.writer(o)
        w.writerow(["query", "video_id", "title", "channel", "published", "views", "comments", "url"])
        w.writerows(cands)
    for c in cands:
        print(f"{c[1]} | {c[4]} | {c[6]:>5} comments | {c[3][:28]:28} | {c[2][:70]} | [{c[0][:30]}]")
    print(len(cands), "candidates")


def clean(t):
    t = re.sub(r"(?i)<br\s*/?>", "\n", t)
    return html.unescape(re.sub(r"<[^>]+>", "", t)).strip()


def cmd_comments(idfile):
    ids = [l.strip() for l in open(idfile) if l.strip()]
    for vid in ids:
        d = os.path.join(HERE, "comments-raw", vid)
        save(os.path.join(d, "video.json"), call("videos", part="snippet,statistics", id=vid))
        page, token, texts = 0, None, []
        while page < 5:                                   # up to 500 top-level comments per video
            p = dict(part="snippet,replies", videoId=vid, maxResults=100, order="relevance", textFormat="html")
            if token:
                p["pageToken"] = token
            try:
                raw = call("commentThreads", **p)
            except urllib.error.HTTPError as e:
                print("STOP", vid, e.code, json.loads(e.read())["error"]["message"][:120]); break
            page += 1
            save(os.path.join(d, f"comments-p{page}.json"), raw)
            j = json.loads(raw)
            texts += j["items"]
            token = j.get("nextPageToken")
            if not token:
                break
            time.sleep(1)
        vd = json.loads(open(os.path.join(d, "video.json"), "rb").read())["items"][0]
        names = set()
        for it in texts:
            c = it["snippet"]["topLevelComment"]["snippet"]; names.add(c["authorDisplayName"])
            for r in it.get("replies", {}).get("comments", []):
                names.add(r["snippet"]["authorDisplayName"])
        names |= {vd["snippet"]["channelTitle"]}
        def scrub(t):
            for n in sorted((x for x in names if len(x) > 2), key=len, reverse=True):
                t = re.sub(r"(?<![\w])" + re.escape(n.lstrip("@")) + r"(?![\w])", "[member]", t, flags=re.I)
            return t
        out = [f"SOURCE: https://www.youtube.com/watch?v={vid}", "SITE: YouTube (YouTube Data API v3)",
               f"TITLE: {html.unescape(vd['snippet']['title'])}", f"CHANNEL: {vd['snippet']['channelTitle']}",
               f"VIDEO DATE: {vd['snippet']['publishedAt']}",
               f"READ ON: {date.today().isoformat()} via YouTube Data API (fetch_youtube.py)",
               f"COMMENTS SHOWN BY YOUTUBE: {vd['statistics'].get('commentCount')}; TOP-LEVEL THREADS SAVED: {len(texts)}",
               "NOTE: text extracted by code from the saved .json files. Commenter names replaced with [member]; "
               "the channel owner's replies are labelled CREATOR.", ""]
        for i, it in enumerate(texts, 1):
            c = it["snippet"]["topLevelComment"]["snippet"]
            out += [f"=== COMMENT {i} ({c['publishedAt']}, likes {c.get('likeCount',0)}) ===", scrub(clean(c["textDisplay"])), ""]
            for r in it.get("replies", {}).get("comments", []):
                rs = r["snippet"]
                who = "CREATOR" if rs.get("authorChannelId", {}).get("value") == vd["snippet"]["channelId"] else "reply"
                out += [f"  --- {who} ({rs['publishedAt']}) ---", scrub(clean(rs["textDisplay"])), ""]
        open(os.path.join(HERE, "comments-raw", vid + ".txt"), "w", encoding="utf-8").write("\n".join(out))
        print("OK", vid, len(texts), "threads")
        time.sleep(1)


if __name__ == "__main__":
    {"search": lambda: cmd_search(), "comments": lambda: cmd_comments(sys.argv[2])}[sys.argv[1]]()
