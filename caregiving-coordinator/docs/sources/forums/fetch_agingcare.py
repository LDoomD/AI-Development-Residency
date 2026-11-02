#!/usr/bin/env python3 -I
"""Save public AgingCare threads as exact HTML, plus a text extract made by this script.

Why: text copied by a model can contain typos. Here the HTML is saved byte for byte
and the .txt is produced by code, so a quote can be checked against the .html.

Usage: python3 -I fetch_agingcare.py <topic-slug> <url> [<url> ...]
Saves to agingcare/<topic-slug>/<thread-id>.html and .txt next to this script.
Waits 10 seconds between requests (AgingCare robots.txt: Crawl-delay 10).
Only /questions/ and /discussions/ thread URLs are accepted.
"""
import html, os, re, sys, time, urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (discovery research; plain request, robots.txt respected)"
DELAY = 10


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()


def clean(fragment):
    fragment = re.sub(r"(?i)<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"(?i)</p>|</li>|</div>", "\n", fragment)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    fragment = html.unescape(fragment)
    return re.sub(r"\n{3,}", "\n\n", fragment).strip()


def extract(raw_html, url):
    h = raw_html.decode("utf-8-sig", errors="replace")
    title = clean(re.search(r"<h1[^>]*itemprop=name[^>]*>(.*?)</h1>", h, re.S).group(1))
    q_date = (re.search(r"<meta itemprop=dateCreated content=([^>\s]+)", h) or [None, "unknown"])[1]
    answer_count = (re.search(r"itemprop=answerCount content=(\d+)", h) or
                    re.search(r"itemprop=commentCount content=(\d+)", h) or [None, "not shown"])[1]
    q = re.search(r'<div body toggle-content=target[^>]*itemprop=text>(.*?)</div><', h, re.S)
    body = clean(q.group(1)) if q else "[question body not found by script]"
    handles = set(re.findall(r"itemprop=name>([^<]{2,40})</span>", h))
    comments = []
    for m in re.finditer(r"<div commentcontent[^>]*itemprop=text>(.*?)</div><time[^>]*datetime=([^ >]+)", h, re.S):
        comments.append((m.group(2), clean(m.group(1))))
    # handles are replaced everywhere they appear as whole words
    def scrub(t):
        for hd in sorted(handles, key=len, reverse=True):
            if hd != title and len(hd) > 2:
                t = re.sub(r"(?<![\w])" + re.escape(hd) + r"(?![\w])", "[member]", t, flags=re.I)
        return t
    out = [
        f"SOURCE: {url}",
        "SITE: AgingCare.com",
        f"TITLE: {title}",
        f"THREAD DATE: {q_date}",
        f"READ ON: {date.today().isoformat()} by plain HTTP request (fetch_agingcare.py)",
        f"ANSWERS/COMMENTS SHOWN BY PAGE: {answer_count}; CAPTURED BY SCRIPT: {len(comments)}",
        "NOTE: text extracted by code from the saved .html (not retyped). Member handles replaced with [member].",
        "      Replies collapsed behind 'See all' on the page are not in the HTML and are not captured.",
        "", "=== POST ===", scrub(body), "",
    ]
    for i, (d, t) in enumerate(comments, 1):
        out += [f"=== COMMENT {i} ({d}) ===", scrub(t), ""]
    return "\n".join(out), title, q_date, answer_count, len(comments)


def main():
    topic, urls = sys.argv[1], sys.argv[2:]
    folder = os.path.join(HERE, "agingcare", topic)
    os.makedirs(folder, exist_ok=True)
    for n, url in enumerate(urls):
        if not re.match(r"https://www\.agingcare\.com/(questions|discussions)/[\w%-]+\.htm$", url):
            print("SKIP (not a thread URL):", url); continue
        tid = re.search(r"-(\d+)\.htm$", url).group(1)
        try:
            raw = fetch(url)
            with open(os.path.join(folder, tid + ".html"), "wb") as f:
                f.write(raw)
            text, title, qd, shown, got = extract(raw, url)
            with open(os.path.join(folder, tid + ".txt"), "w", encoding="utf-8") as f:
                f.write(text)
            print(f"OK {tid} | {qd[:10]} | shown {shown} got {got} | {title[:60]}")
        except Exception as e:  # keep going; report it
            print(f"FAIL {tid}: {e}")
        if n < len(urls) - 1:
            time.sleep(DELAY)


if __name__ == "__main__":
    main()
