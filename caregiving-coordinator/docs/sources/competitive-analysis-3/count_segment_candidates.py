"""Count saved Reddit posts (49,315) naming each company the market analysis lists in the segments that touch the 5 criteria.
A mention is not use. Re-run: python3 -I count_segment_candidates.py"""
import json, re, pathlib
R = pathlib.Path(__file__).resolve().parents[1] / "reddit/arctic-shift-2026-11-03"
P = {"Caring Village": r"caring ?village", "CaringBridge": r"caring ?bridge", "Lotsa Helping Hands": r"lotsa",
     "A Place for Mom": r"a place for mom|aplaceformom", "Caring.com": r"caring\.com",
     "Everplans": r"everplans", "Trustworthy": r"trustworthy\.com|trustworthy app", "Cake": r"joincake|cake\.com|\bcake app", "AARP Digital Vault": r"aarp (digital )?vault",
     "1Password": r"1 ?password", "Keeper": r"keeper (security|password|app)",
     "Calm": r"\bcalm app\b|calm\.com", "Talkspace": r"talkspace", "Sanvello": r"sanvello", "BetterHelp": r"betterhelp", "ianacare": r"ianacare",
     "Cariloop": r"cariloop", "Wellthy": r"wellthy", "Carallel": r"carallel",
     "Chapter (Medicare navigation)": r"askchapter|chapter medicare"}
c = {k: 0 for k in P}
for f in ["posts.jsonl", "posts_targeted.jsonl"]:
    for l in open(R / f):
        t = json.loads(l)["text"].lower()
        for k, p in P.items():
            if re.search(p, t): c[k] += 1
json.dump(c, open(pathlib.Path(__file__).parent / "segment-candidate-mentions.json", "w"), indent=1)
for k, v in c.items(): print(f"{k}: {v}")
