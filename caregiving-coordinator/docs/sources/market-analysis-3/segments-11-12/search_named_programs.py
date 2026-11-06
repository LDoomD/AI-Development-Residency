"""Second search of the same 49,315 saved Reddit posts, for named offerings and payers: the 10 offerings in
docs/exhaustion-dementia-research.md, plus programs that pay for respite. No new fetching.
Writes named-counts.json and named-matches.jsonl (link, community, date, terms, excerpt), same format as matches.jsonl."""
import json, re, pathlib, collections
SRC = pathlib.Path(__file__).parents[2] / "reddit" / "arctic-shift-2026-11-03"; OUT = pathlib.Path(__file__).parent
TERMS = {  # (pattern, case-sensitive?)
 "ARCH National Respite Network": (r"\barch (national )?respite\b|archrespite", False),
 "Family Caregiver Alliance": (r"family caregiver alliance|caregiver\.org\b", False),
 "Alzheimer's Association helpline": (r"alz(heimer'?s)? (association )?(24/7 |24 hour )?help ?line|800[- .]?272[- .]?3900", False),
 "Medicare GUIDE program": (r"\bGUIDE (model|program)\b", True),
 "Papa (companions)": (r"\bjoinpapa\b|\bpapa pals?\b|\bpapa (app|inc|health)\b", False),
 "Wellthy": (r"\bwellthy\b", False),
 "Torchlight": (r"\btorchlight\b", False),
 "Teepa Snow / Positive Approach to Care": (r"\bteepa\b|positive approach to care", False),
 "Savvy Caregiver": (r"savvy caregiver", False),
 "Cariloop": (r"\bcariloop\b", False),
 "VA caregiver or respite program": (r"\bVA\b.{0,40}\b(respite|caregiver)\b|\bPCAFC\b|\b(respite|caregiver)\b.{0,40}\bVA\b", True),
 "Medicaid waiver": (r"medicaid waiver|waiver program|home and community[- ]based|\bHCBS\b", False),
 "Hospice respite": (r"hospice.{0,60}respite|respite.{0,60}hospice", False),
 "Area Agency on Aging": (r"area agenc(y|ies) on aging", False),
}
RX = {k: re.compile(p, 0 if cs else re.I) for k, (p, cs) in TERMS.items()}
counts = collections.Counter(); prior = {json.loads(l)["key"] for l in open(OUT / "matches.jsonl")}; new = 0
with open(OUT / "named-matches.jsonl", "w") as out:
    for fname in ["posts.jsonl", "posts_targeted.jsonl"]:
        for line in open(SRC / fname):
            p = json.loads(line); t = p.get("text") or ""; hits = {}
            for k, rx in RX.items():
                m = rx.search(t)
                if m: counts[k] += 1; hits[k] = re.sub(r"\s+", " ", t[max(0, m.start()-150): m.end()+150])
            if hits:
                isnew = p["key"] not in prior; new += isnew
                out.write(json.dumps({"key": p["key"], "url": p["url"], "subreddit": p["subreddit"], "date": p["created"], "terms": sorted(hits), "excerpts": hits, "new_to_reading_set": isnew}, ensure_ascii=False) + "\n")
json.dump({"patterns": {k: v[0] for k, v in TERMS.items()}, "counts": dict(counts), "posts_not_already_matched": new}, open(OUT / "named-counts.json", "w"), indent=1)
for k in TERMS: print(f"{k:42} {counts[k]}")
print("posts not already in matches.jsonl:", new)
