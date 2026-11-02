#!/usr/bin/env python3 -I
"""Search OpenAlex (free scholarly index, https://openalex.org) for papers on our caregiving topics.
OpenAlex's answers are saved byte for byte in openalex-raw/ and the shortlist goes to
openalex-candidates.csv. No papers are downloaded here; a person approves the list first.

Without an API key OpenAlex shares a small free daily budget by network address (each search here
costs about $0.001). Run: python3 -I search_openalex.py
"""
import csv, html, json, os, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = {
    "information-sharing": ["family caregivers information sharing coordination care network",
                            "informal caregivers coordination technology family members shared care"],
    "siblings": ["sibling conflict caring for older parent division of care"],
    "willingness-to-pay": ["family caregiver technology adoption willingness to pay"],
    "cost-and-scale": ["economic value of unpaid family caregiving United States"],
    "long-distance": ["long-distance caregiving adult children older parent"],
}
SELECT = "id,title,publication_year,type,cited_by_count,doi,open_access,primary_location,abstract_inverted_index"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (discovery research)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read()


def main():
    os.makedirs(os.path.join(HERE, "openalex-raw"), exist_ok=True)
    rows, seen = [], set()
    for topic, queries in TOPICS.items():
        for qi, q in enumerate(queries, 1):
            params = {"search": q, "filter": "from_publication_date:2012-01-01,type:article",
                      "per-page": 15, "select": SELECT}
            raw = get("https://api.openalex.org/works?" + urllib.parse.urlencode(params))
            open(os.path.join(HERE, "openalex-raw", f"{topic}-{qi}.json"), "wb").write(raw)
            for w in json.loads(raw)["results"]:
                if w["id"] in seen or not w.get("title"):
                    continue
                seen.add(w["id"])
                oa = w.get("open_access") or {}
                src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "")
                rows.append([topic, q, html.unescape(w["title"]), w["publication_year"], w["cited_by_count"],
                             src, oa.get("is_oa"), oa.get("oa_url") or "", w.get("doi") or "", w["id"]])
            time.sleep(1)
    with open(os.path.join(HERE, "openalex-candidates.csv"), "w", newline="", encoding="utf-8") as o:
        w = csv.writer(o)
        w.writerow(["topic", "query", "title", "year", "cited_by", "journal", "open_access", "oa_url", "doi", "openalex_id"])
        w.writerows(rows)
    for r in rows:
        print(f"{r[0][:12]:12} | {r[3]} | {r[4]:>4} cites | OA={str(r[6])[0]} | {r[5][:28]:28} | {r[2][:85]}")
    print(len(rows), "candidates")


if __name__ == "__main__":
    main()
