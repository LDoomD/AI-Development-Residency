"""Write docs/feature-analysis-3.md from figma-fa3.json. Run from competitive-analysis-2: python3 -I feature-analysis-3/build_doc_fa3.py"""
import json
d = json.load(open('feature-analysis-3/figma-fa3.json'))
md = lambda row: '| ' + ' | '.join(c.replace('|', '/').replace('\n', ' ') for c in row) + ' |'
m = d['main']; hw = d['howwell']
o = ["# Feature Comparison Analysis 3 (teacher format, 2026-11-04)", "",
 "Built to match the teacher's example (Figma node `5:823`) and blank template (`5:3064`): the same columns, his questions in the second row, OUR COMPANY first, and ✅/🚫 in the feature cells. Figma: section `2584:10359` inside \"Feature Analysis\". Versions 1 and 2 (`docs/feature-analysis.md`, Figma `2436:9443`) are unchanged.", "",
 "**How it was made:** ✅ = the company offers the feature on its own saved pages (`docs/feature-analysis.md` step 2 and `docs/sources/competitive-analysis-2/facts/`). How well each feature works is counted from the 577 caregiving items in `docs/sources/competitive-analysis-2/themes/`, using `feature-analysis-3/theme-to-feature.json` (Claude's mapping, open for the owner to check) and `build_howwell.py`. `assemble_fa3.py` checks every number. The Figma text matches the source (195 of 195 main cells, 99 of 99 how-well cells, plus the gaps and notes texts).", "",
 "## Main table (teacher format)", "", md(m[0][1:]), '|' + '---|' * (len(m[0]) - 1), md(m[1][1:])]
o += [md(r[1:]) for r in m[2:]]
o += ["", d['offer_notes'], "", "## How well each feature works (evidence)", "", "Label: fewer than 5 items = Too few to judge; at least 2 of 3 say it works = Mostly works; at least 2 of 3 report a problem = Mostly problems; otherwise Mixed.", "", md(hw[0]), '|' + '---|' * len(hw[0])]
o += [md(r) for r in hw[1:]]
o += ["", "## " + d['gaps'].split('\n', 1)[0], "", d['gaps'].split('\n', 1)[1], ""]
open('../../feature-analysis-3.md', 'w').write('\n'.join(o))
print('ok')
