#!/usr/bin/env python3 -I
"""Save the free copy of each approved paper exactly as served, plus a text extract made by code.

Order for each paper: (1) PubMed Central page (found through Europe PMC by DOI or from the OpenAlex
link), (2) the open-access link OpenAlex gives. A response that is blocked (403, 'Just a moment',
too short) is recorded as BLOCKED and NOT retried or worked around.
Writes papers/<slug>.pdf or .html, papers/<slug>.txt, and papers/status.csv.
Run: python3 -I fetch_papers.py   (reads /private/tmp/claude-501/sel.json made from openalex-candidates.csv)
"""
import csv, html, json, os, re, subprocess, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "papers")
UA = "Mozilla/5.0 (discovery research; plain request)"
os.makedirs(OUT, exist_ok=True)


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.headers.get("content-type", ""), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("content-type", ""), e.read()
    except Exception as e:
        return 0, "", str(e).encode()


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]


def html_text(b):
    h = b.decode("utf-8", "replace")
    m = re.search(r"<main.*?</main>", h, re.S) or re.search(r"<article.*?</article>", h, re.S)
    h = m.group(0) if m else h
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>", "", h, flags=re.S)
    h = re.sub(r"(?i)</(p|h\d|li|div|tr|section)>", "\n", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    t = html.unescape(re.sub(r"<[^>]+>", "", h))
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", t)).strip()


def blocked(code, ctype, body, text_len=None):
    head = body[:3000].decode("utf-8", "replace").lower()
    if code != 200:
        return f"HTTP {code}"
    if body[:4] == b"%PDF":
        return None
    if "just a moment" in head or "cf-chl" in head or "captcha" in head or "access denied" in head:
        return "bot-check page"
    if text_len is not None and text_len < 15000:
        return f"too short ({text_len} chars): probably abstract or notice only"
    return None


def pmc_id(doi, oa_url):
    m = re.search(r"PMC(\d+)", oa_url or "") or re.search(r"/pmc/articles/(\d+)", oa_url or "")
    if m:
        return "PMC" + m.group(1)
    if doi:
        d = doi.replace("https://doi.org/", "")
        c, _, b = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22" + urllib.parse.quote(d) + "%22&format=json&resultType=lite")
        if c == 200:
            for r in json.loads(b)["resultList"]["result"]:
                if r.get("pmcid"):
                    return r["pmcid"]
    return None


def main():
    sel = json.load(open("/private/tmp/claude-501/sel.json"))
    rows = []
    for n, p in enumerate(sel, 1):
        s = slug(p["title"]); status = note = src = ""
        pm = pmc_id(p["doi"], p["oa_url"])
        tries = []
        if pm:
            tries.append(("PubMed Central", f"https://pmc.ncbi.nlm.nih.gov/articles/{pm}/"))
        if p["oa_url"]:
            tries.append(("open-access link", p["oa_url"]))
        for label, url in tries:
            code, ctype, body = get(url)
            if body[:4] == b"%PDF":
                open(os.path.join(OUT, s + ".pdf"), "wb").write(body)
                subprocess.run(["pdftotext", "-layout", os.path.join(OUT, s + ".pdf"), os.path.join(OUT, s + ".txt")])
                tl = len(open(os.path.join(OUT, s + ".txt"), encoding="utf-8", errors="replace").read())
                why = None if tl > 15000 else f"too short ({tl} chars)"
                kind = "pdf"
            else:
                t = html_text(body) if code == 200 else ""
                why = blocked(code, ctype, body, len(t))
                kind = "html"
                if not why:
                    open(os.path.join(OUT, s + ".html"), "wb").write(body)
                    open(os.path.join(OUT, s + ".txt"), "w", encoding="utf-8").write(t)
            if not why:
                status, src = "SAVED", f"{label}: {url}"
                break
            note += f"{label}: {why}; "
        if not status:
            status = "BLOCKED-OR-UNAVAILABLE"
        rows.append([s, p["title"], p["year"], status, src, note, p["doi"], pm or ""])
        print(f"{n:2} {status:22} {s[:55]} | {src[:60]} {note[:80]}")
        time.sleep(3)
    with open(os.path.join(OUT, "status.csv"), "w", newline="", encoding="utf-8") as o:
        w = csv.writer(o); w.writerow(["slug", "title", "year", "status", "saved_from", "notes", "doi", "pmcid"]); w.writerows(rows)


if __name__ == "__main__":
    main()
