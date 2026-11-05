"""Save 6 Reddit threads that name Everplans or Cariloop, from the public Arctic Shift archive
(https://arctic-shift.photon-reddit.com/api). Reddit itself is blocked for Firecrawl and the built-in browser.
Usernames are dropped. One .txt per thread in reddit-threads/, with the reddit.com link at the top."""
import json, time, urllib.request, pathlib
OUT = pathlib.Path(__file__).parent / "reddit-threads"
API = "https://arctic-shift.photon-reddit.com/api"
THREADS = {"sichx0": "Cariloop", "y4q1tc": "Everplans", "s6gxn7": "Everplans", "1eaenyg": "Everplans",
           "1i5704g": "Everplans", "sr80o8": "Everplans"}
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "residency-research-script"})
    return json.load(urllib.request.urlopen(req, timeout=60))
def walk(nodes, depth, lines):
    for n in nodes or []:
        d = n.get("data", n)
        body = d.get("body")
        if body and body not in ("[deleted]", "[removed]"):
            lines.append(f"{'  '*depth}- [comment {d.get('id')}] {body.strip()}")
        rep = d.get("replies")
        if isinstance(rep, dict): rep = rep.get("data", {}).get("children")
        walk(rep, depth + 1, lines)
for pid, comp in THREADS.items():
    post = get(f"{API}/posts/ids?ids={pid}")["data"][0]
    tree = get(f"{API}/comments/tree?link_id={pid}&limit=9999")["data"]
    lines = [f"SOURCE: https://www.reddit.com{post['permalink']}", f"Saved 2026-11-04 from Arctic Shift. Competitor: {comp}. Usernames removed.",
             f"r/{post['subreddit']} | {time.strftime('%Y-%m-%d', time.gmtime(post['created_utc']))}", f"TITLE: {post['title']}", f"POST: {post.get('selftext','').strip()}", "COMMENTS:"]
    walk(tree, 0, lines)
    (OUT / f"{comp.lower()}_{pid}.txt").write_text("\n".join(lines))
    print(pid, comp, len(lines) - 6, "comments"); time.sleep(1)
