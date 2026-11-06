"""Write docs/market-analysis-3.md from ma3-filled.json. Run: python3 -I build_doc_ma3.py"""
import json
d = json.load(open('ma3-filled.json'))
md = lambda row: '| ' + ' | '.join(str(c).replace('|', '/').replace('\n', ' ') for c in row) + ' |'
tbl = lambda cols, rows: [md(cols), '|' + '---|' * len(cols)] + [md(r) for r in rows]
o = ["# Market analysis updated with the Reddit research (2026-11-04)", "",
 "Same content as the Figma section \"UPDATED 2026-11-04 — MARKET ANALYSIS WITH THE NEW REDDIT RESEARCH\" (market page, below the CURRENT SET; node `2598:10950`), plus the audience update (Audience page, node `2605:638`). The earlier versions are unchanged, and each has a SUPERSEDED sticky pointing to the new one.", "",
 "**Method:** a random sample of 500 Reddit posts with no keyword filter (200 from r/CaregiverSupport, 200 from r/AgingParents, 100 from 11 other communities; seed 20261104; `build_sample.py`). It was coded with the same 14 themes as the forum research (`CODING-INSTRUCTIONS.md`, `codes/`). 412 posts were by caregivers. Every quote was checked word for word, and the counts come from `count_themes.py`, `other_groups.py` and `count_by_audience.py`. All numbers in the text were filled by `build_ma3.py`. The Figma text was hash-checked against the source.", "",
 f"## {d['top_title']}", "", d['top_intro'], ""] + tbl(d['top_columns'], d['top_rows']) + ["", d['top_who'], "", d['top_new'], "", d['top_limits'], "",
 f"## {d['score_title']}", "", d['score_intro'], ""] + tbl(d['score_columns'], d['score_rows']) + ["",
 f"## {d['opp_title']}", "", d['opp_intro'], "", f"**{d['opp_question']}**", "", d['opp_answer'], "",
 f"## {d['seg_title']} / {d['size_title']}", "", d['seg_intro'], d['size_intro'], "", "The new column, by segment (the same text is used in the opportunity, segments and size tables):", ""] + \
 [f"- Segment {k}: {v}" for k, v in d['seg_reddit'].items()] + ["",
 f"## {d['analysis_title']}", "", d['analysis_intro'], "",
 f"## {d['aud_title']}", "", d['aud_intro'], d['aud_note_pct'], "", d['aud_segments'], "", f"### {d['aud_table_title']}", ""] + tbl(d['aud_columns'], d['aud_rows']) + ["", d['aud_a2'], "", d['aud_limits'], ""]
open('../../market-analysis-3.md', 'w').write('\n'.join(o)); print('ok')
