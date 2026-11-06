"""Write docs/competitive-analysis-2.md from answers-v2.json + figma-grid.json. python3 -I build_doc.py"""
import json
a = json.load(open('answers-v2.json')); g = json.load(open('figma-grid.json'))
out = ["# Competitive Analysis 2 (second version, 2026-11-04)", "",
 "Version 1 (`docs/competitive-analysis.md`) answered most boxes with one pasted quote. This version answers every box with a short synthesis of ALL the research. Same content as the Figma section \"CAREGIVING — Competitive Analysis 2\" (file `HcDDdEGAnikTImO8v7UPMp`, node `2564:10354`, in Section 8). Version 1 is unchanged.", "",
 "## How it was made", "",
 "1. **Evidence packs** (`docs/sources/competitive-analysis-2/packs/`, `build_packs.py`): every caregiving app review (the 439-review filter, plus extra Google Play tags), the never-filtered MyChart and Everplans Apple reviews, every Reddit post in both downloads that names the competitor, and the forum app mentions. 1,101 items in total.",
 "2. **Themes** (`themes/`, rules in `READER-INSTRUCTIONS.md`): readers read every item in full, kept only items written by someone caring for another person that say something about the product (577 kept), and counted themes from what people wrote. `verify_themes.py` checks every count against its id list and every quote word for word: 0 errors.",
 "3. **Company facts** (`facts/`): every saved company page read in full, with each answer backed by quotes. `verify_facts.py` found all 273 quotes in the saved pages.",
 "4. **Answers** (`answers-v2.json`): written from the themes and facts. `audit_answers.py` checks every bracketed number against the theme counts. The 13 numbers it flags come from store splits, prices and the readers' notes, and each was checked by hand.",
 "5. **Figma**: cells pasted from `figma-grid.json` and hash-checked against it: 220 of 220 match.", "",
 "**Gaps** compare each row with the 7 biggest caregiver problems in `docs/reddit-caregiver-findings-2026-11-03.md`. **Limits**: Everplans (1 caregiving review) and Lotsa (4 items) are too thin to judge. App-store reviews lean toward strong opinions. Reddit venting posts over-represent conflict. Some company pages were saved as 404s. Each row's last column states its own limits.", "",
 "## The table", ""]
cols = g[0]
for row in g[1:]:
    out.append(f"### {row[0]}"); out.append("")
    for c, v in zip(cols[1:], row[1:]):
        out.append(f"- **{c}** {v}")
    out.append("")
open('../../competitive-analysis-2.md', 'w').write('\n'.join(out))
print('written', len('\n'.join(out)))

# gaps + unique value opportunities (version 2)
d = json.load(open('gaps-uvo-v2.json'))
o = ["", f"## {d['gaps_title']}", "", d['gaps_intro'], ""]
for gp in d['gaps']:
    o += [f"**{gp['gap']}** {gp['evidence']}", ""]
o += [d['gaps_limits'], "", d['gaps_owner'], "", f"## {d['uvo_title']}", "",
      "Every number is (Source N). Checked by `audit_gaps_uvo.py` (97 claims, each matched to its theme). Same content as the Figma section `2570:10217` inside Competitive Analysis 2.", "",
      "| " + " | ".join(d['uvo_columns']) + " |", "|" + "---|" * len(d['uvo_columns'])]
o += ["| " + " | ".join(r) + " |" for r in d['uvo_rows']]
with open('../../competitive-analysis-2.md', 'a') as f: f.write('\n'.join(o) + '\n')
print('gaps + uvo appended')
