#!/usr/bin/env python3 -I
"""Save public ALZConnected (Alzheimer's Association community) threads as exact HTML,
plus a text extract made by this script. Same method as fetch_agingcare.py.

Usage:
  python3 -I fetch_alzconnected.py list <first_page> <last_page>
      prints thread URLs found on https://alzconnected.org/discussions/p<N> (waits 10 s per page)
  python3 -I fetch_alzconnected.py get <folder-slug> <thread-url> [<thread-url> ...]
      saves alzconnected/<folder-slug>/<thread-id>.html and .txt next to this script

robots.txt of alzconnected.org disallows /entry/, /messages/, /search/, /profile/..., /bestof/,
/categories/*/p (paged category lists). This tool only reads /discussions, /discussions/p<N> and
/discussion/<id>/<slug>. It waits 10 seconds between requests.
"""
import html, os, re, sys, time, urllib.request
from datetime import date
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (discovery research; plain request, robots.txt respected)"
DELAY = 10
THREAD_RE = re.compile(r"^https://alzconnected\.org/discussion/\d+/[\w%-]+$")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()


class Thread(HTMLParser):
    """Collects each 'Message userContent' block with the author and time seen before it."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.messages = []          # (author, datetime, text)
        self.depth = 0              # div depth inside a message; 0 = not inside
        self.buf = []
        self.last_author = "unknown"
        self.last_time = "unknown"
        self.in_username = False
        self.handles = set()
        self.category = ""
        self.in_cat = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if self.depth:
            if tag == "div":
                self.depth += 1
            elif tag == "br":
                self.buf.append("\n")
            elif tag in ("p", "li", "blockquote"):
                self.buf.append("\n")
            return
        if tag == "div" and "Message" in cls.split() and "userContent" in cls.split():
            self.depth, self.buf = 1, []
        elif tag == "a" and "Username" in cls.split():
            self.in_username = True
        elif tag == "time" and a.get("datetime"):
            self.last_time = a["datetime"]
        elif tag == "span" and "Category" in cls.split():
            self.in_cat = True

    def handle_endtag(self, tag):
        if self.depth:
            if tag == "div":
                self.depth -= 1
                if self.depth == 0:
                    text = re.sub(r"\n{3,}", "\n\n", "".join(self.buf)).strip()
                    self.messages.append((self.last_author, self.last_time, text))
            elif tag in ("p", "li", "blockquote"):
                self.buf.append("\n")
        else:
            if tag == "a":
                self.in_username = False
            if tag == "span":
                self.in_cat = False

    def handle_data(self, data):
        if self.depth:
            self.buf.append(data)
        elif self.in_username:
            self.last_author = data.strip()
            self.handles.add(data.strip())
        elif self.in_cat and data.strip() and data.strip() != "in":
            self.category = self.category or data.strip()


def extract(raw, url):
    h = raw.decode("utf-8", errors="replace")
    p = Thread()
    p.feed(h)
    title = html.unescape(re.search(r"<title>(.*?)</title>", h, re.S).group(1)).replace(" — ALZConnected", "").strip()
    handles = sorted((x for x in p.handles if len(x) > 2), key=len, reverse=True)

    def scrub(t):
        for hd in handles:
            t = re.sub(r"(?<![\w])" + re.escape(hd) + r"(?![\w])", "[member]", t, flags=re.I)
        return t

    msgs = p.messages
    out = [
        f"SOURCE: {url}", "SITE: ALZConnected (Alzheimer's Association)", f"TITLE: {title}",
        f"CATEGORY: {p.category}",
        f"THREAD DATE: {msgs[0][1] if msgs else 'unknown'}",
        f"READ ON: {date.today().isoformat()} by plain HTTP request (fetch_alzconnected.py)",
        f"MESSAGES CAPTURED BY SCRIPT: {len(msgs)} (1 post + {max(len(msgs)-1,0)} comments on this page; later pages of long threads are not fetched)",
        "NOTE: text extracted by code from the saved .html (not retyped). Member handles replaced with [member].",
        "",
    ]
    for i, (_a, d, t) in enumerate(msgs):
        out += ["=== POST (%s) ===" % d if i == 0 else "=== COMMENT %d (%s) ===" % (i, d), scrub(t), ""]
    return "\n".join(out), title, (msgs[0][1] if msgs else "unknown"), len(msgs)


def cmd_list(a, b):
    seen = []
    for n in range(a, b + 1):
        raw = fetch("https://alzconnected.org/discussions" + ("" if n == 1 else f"/p{n}")).decode("utf-8", "replace")
        for u in re.findall(r'href="(https://alzconnected\.org/discussion/\d+/[\w%-]+)"', raw):
            if u not in seen:
                seen.append(u)
        if n < b:
            time.sleep(DELAY)
    print("\n".join(seen))


def cmd_get(slug, urls):
    folder = os.path.join(HERE, "alzconnected", slug)
    os.makedirs(folder, exist_ok=True)
    for n, url in enumerate(urls):
        if not THREAD_RE.match(url):
            print("SKIP (not a thread URL):", url)
            continue
        tid = re.search(r"/discussion/(\d+)/", url).group(1)
        try:
            raw = fetch(url)
            open(os.path.join(folder, tid + ".html"), "wb").write(raw)
            text, title, d, k = extract(raw, url)
            open(os.path.join(folder, tid + ".txt"), "w", encoding="utf-8").write(text)
            print(f"OK {tid} | {d[:10]} | messages {k} | {title[:60]}")
        except Exception as e:
            print(f"FAIL {tid}: {e}")
        if n < len(urls) - 1:
            time.sleep(DELAY)


if __name__ == "__main__":
    if sys.argv[1] == "list":
        cmd_list(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == "get":
        cmd_get(sys.argv[2], sys.argv[3:])
