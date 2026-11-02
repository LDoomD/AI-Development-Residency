"""Build docs/company-funding.md and table cell text (cells.json) from group-a/b/c.json. No numbers are typed by hand."""
import json, os, re, pathlib
HERE = pathlib.Path(__file__).parent
recs = {}
for g in "abc":
    for e in json.load(open(HERE / f"group-{g}.json")):
        recs[e["company"]] = e
def get(prefix):
    for k, e in recs.items():
        if k.lower().startswith(prefix.lower()): return e
    raise KeyError(prefix)
LABEL = {"total_raised": "raised in total", "last_round": "last round", "valuation": "valued at", "acquisition_price": "acquired for",
         "annual_revenue": "annual revenue", "system_sales": "system sales (Franchise Times ranking, not funding)"}
def kind(e):
    return "excerpt, not an exact page copy" if re.search(r"excerpt|extract|firecrawl", os.path.basename(e["saved_file"])) else "exact page copy"
def line(prefix, short=None):
    e = get(prefix)
    if e["metric_type"] == "NOT_FOUND": return None
    st = re.match(r"(primary|secondary)", e["source_type"]).group(1)
    return f'{short or e["company"]}: {LABEL[e["metric_type"]]} {e["value"]} ({e["as_of"]}; {st}; {kind(e)})'
ROWS = {  # table row number -> (company prefixes, display names)
 1: ["ianacare","CaringBridge","Caring Village","Lotsa"],
 2: ["TimeTree","Cozi","FamilyWall"],
 3: ["Medisafe","MyTherapy","Round Health"],
 4: ["PillPack","divvyDOSE","Capsule","Alto","Truepill","ExactCare"],
 5: ["A Place for Mom","Caring.com"],
 6: ["Visiting Angels","Right at Home","BrightStar","Synergy","Home Instead","Papa","Kindly"],
 7: ["Lively","Philips","Aloe","Medical Guardian","MobileHelp","Bay Alarm","Life Alert"],
 8: ["Cariloop","Wellthy","Carallel"],
 9: ["Kin","Citizen","Doctor Notes","Abridge"],
 10: ["Epic","Meditech","athenahealth","Oracle","GetWell"],
 11: ["1Password","Keeper","Trustworthy","Cake","Everplans"],
 12: [],
 13: ["Active Day","Grace"],
 14: ["Calm","Headspace","Talkspace","BetterHelp"],
 15: ["Teladoc","Amwell","MDLIVE","Doxy"],
 16: ["Alight","Accolade","Health Advocate","Rightway","Included","Quantum"],
}
cells = {}
for r, prefs in ROWS.items():
    found, nf = [], []
    for p in prefs:
        e = get(p)
        l = line(p)
        (found if l else nf).append(l or e["company"].split(" (")[0])
    txt = "\n".join(found) if found else "No sourced company figure for this segment."
    if nf: txt += "\nNo sourced figure found: " + ", ".join(nf) + "."
    cells[r] = txt
cells[12] = "Not assessed in this pass: this is the broad outer category, so company figures sit in the home care, referral and respite rows."
json.dump(cells, open(HERE / "cells.json", "w"), indent=1)
# docs file
out = ["# Company funding and value, by company (2026-11-02)\n",
 "Built by script from `docs/sources/funding/group-a.json`, `group-b.json`, `group-c.json`. Every figure was found by a research agent, saved to `docs/sources/funding/<company>/`, and the supporting sentence extracted from the saved file by code. I re-checked that each figure appears in its saved file. **Not found** means no company-stated or clearly attributed figure was found; aggregator estimates (PitchBook, Tracxn, Caplight, GetLatka, CB Insights snippets) were not used because they disagree with each other.\n",
 "Limits: figures are funding, valuation, acquisition price, revenue or franchise system sales, which are different things (the Metric column says which). Press releases and news pages were read; no full annual reports or franchise disclosure documents were. Files marked *excerpt* are short text saved from Firecrawl output because the site blocked downloads; they are not exact page copies. Latest rounds were mostly not checked for later rounds.\n",
 "| Company | Segment | Metric | Value | As of | Source type | Copy type | Source URL | Saved file | Limit |", "|---|---|---|---|---|---|---|---|---|---|"]
for k, e in recs.items():
    if e["metric_type"] == "NOT_FOUND":
        out.append(f'| {k} | {e["segment"]} | NOT FOUND | | | | | | | {e.get("tried","")[:300]} |')
    else:
        out.append(f'| {k} | {e["segment"]} | {LABEL[e["metric_type"]]} | {e["value"]} | {e["as_of"]} | {e["source_type"]} | {kind(e)} | {e["source_url"]} | `{e["saved_file"].split("caregiving-coordinator/")[-1]}` | {e["limit"]} |')
(HERE.parent.parent / "company-funding.md").write_text("\n".join(out) + "\n")
print(len(recs), "companies;", sum(1 for e in recs.values() if e["metric_type"] != "NOT_FOUND"), "with a figure")
for r in sorted(cells): print(f"--- row {r}\n{cells[r]}")
