"""Count, per competitor and feature, distinct caregiving items saying it works vs a problem,
from themes/*.json using theme-to-feature.json. Run from competitive-analysis-2: python3 -I feature-analysis-3/build_howwell.py"""
import json
M = json.load(open('feature-analysis-3/theme-to-feature.json'))
out = {}
for slug, mp in M.items():
    if slug == 'how': continue
    t = json.load(open(f'themes/{slug}.json'))
    res = {}
    for key, feats in mp.items():
        if key[0] == 'Q':
            q = {'R': 'relatives_joining_and_sharing', 'E': 'emergencies_and_support_response'}[key[1]]
            th = t['questions'][q][int(key[3:])]; good = key[2] == '+'
        else:
            th = (t['works_well'] if key[0] == 'W' else t['does_not_work_well'])[int(key[1:])]; good = key[0] == 'W'
        for f in feats:
            r = res.setdefault(str(f), {'works_ids': set(), 'problem_ids': set(), 'works': [], 'problems': []})
            (r['works_ids'] if good else r['problem_ids']).update(th['ids'])
            lst = r['works'] if good else r['problems']
            if [th['theme'], th['count']] not in lst: lst.append([th['theme'], th['count']])
    out[slug] = {f: {'works_items': len(r['works_ids']), 'problem_items': len(r['problem_ids']),
                     'works': sorted(r['works'], key=lambda x: -x[1]), 'problems': sorted(r['problems'], key=lambda x: -x[1])}
                 for f, r in sorted(res.items())}
json.dump(out, open('feature-analysis-3/howwell-counts.json', 'w'), indent=1)
for s, fs in out.items():
    print(s, {f: (v['works_items'], v['problem_items']) for f, v in fs.items()})
