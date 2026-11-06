"""Pick the posts worth reading by hand from posts.jsonl (and posts_targeted.jsonl if present).
Narrow topics: every match kept. Broad topics (documents, support): random sample of 120 each
(seed 42) so the reading load stays small. Splits into tagging/chunk-N.jsonl."""
import json, re, random, pathlib, sys
HERE = pathlib.Path(__file__).parent
NARROW = {
 "apps": r"caring ?bridge|caring village|lotsa|everplans|mychart|greatcall|jitterbug|\blively\b|medical guardian|medisafe",
 "wish": r"i wish there (was|were)|is there an app|looking for an app|any apps?\b|app (for|that)|how do (you|siblings) (keep track|share|coordinate)",
 "portal": r"patient portal|proxy access|log ?in(to)? (her|his|their)|password",
 "group_chat": r"group (chat|text)|whatsapp",
 "calendar": r"shared calendar|google calendar|calendar",
 "meds_share": r"(pill|med(ication)?s?) (list|schedule|organizer|tracker)|track(ing)? (her|his|their) med",
 "spreadsheet": r"spreadsheet|google (doc|sheet)",
}
BROAD = {
 "documents": r"power of attorney|\bpoa\b|insurance card|binder|important documents|advance directive|living will|paperwork",
 "support": r"burn(ed|t)? ?out|support group|someone to talk to|therapist|respite",
}
files = [HERE/"posts.jsonl"] + ([HERE/"posts_targeted.jsonl"] if (HERE/"posts_targeted.jsonl").exists() and "--with-targeted" in sys.argv else [])
picked, broad = {}, {k: [] for k in BROAD}
for f in files:
    for l in open(f):
        d = json.loads(l); t = d["text"].lower()
        if len(t) < 80: continue
        hits = [k for k, p in NARROW.items() if re.search(p, t)]
        if hits: d["topics"] = hits; picked[d["key"]] = d; continue
        for k, p in BROAD.items():
            if re.search(p, t): broad[k].append(d); break
random.seed(42)
for k, lst in broad.items():
    for d in random.sample(lst, min(120, len(lst))):
        d["topics"] = [k]; picked.setdefault(d["key"], d)
items = list(picked.values())
for d in items: d["text"] = d["text"][:2500]
print(len(items))
N = 6
for i in range(N):
    with open(HERE/f"tagging/chunk-{i+1}.jsonl", "w") as o:
        for d in items[i::N]: o.write(json.dumps(d, ensure_ascii=False) + "\n")
