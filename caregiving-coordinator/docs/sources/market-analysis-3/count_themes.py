"""Check and count the coded random Reddit sample (2026-11-04). Run: python3 -I count_themes.py"""
import json, collections, sys
THEMES = ["Choosing, placing and paying for care","Burnout, guilt, isolation, grief","Family coordination, siblings","Long-distance caregiving","Medications","Money, insurance, legal papers","Care recipient refuses help","New diagnosis, crisis, \"where do I start\"","Dementia behavior and communication","Safety","Paid caregivers and agencies","Doctors, appointments, records","The caregiver's own life","Other"]
posts = {}; codes = []
for i in range(1, 5):
    for p in json.load(open(f'sample/part-{i}.json')): posts[p['id']] = p
    codes += json.load(open(f'codes/part-{i}.json'))
bad = []
if len(codes) != 500 or len({c['id'] for c in codes}) != 500: bad.append(f'codes {len(codes)} unique {len({c["id"] for c in codes})}')
cg = [c for c in codes if c['caregiver']]
norm = lambda s: s.replace('’', "'")
for c in cg:
    if c['main'] not in THEMES: bad.append(f"bad main {c['id']} {c['main']}")
    for a in c['anywhere']:
        if a not in THEMES: bad.append(f"bad anywhere {c['id']} {a}")
    if c['main'] not in c['anywhere']: c['anywhere'].append(c['main'])
    if c['quote'] not in posts[c['id']]['text']: bad.append(f"quote {c['id']}")
N = len(cg)
main = collections.Counter(c['main'] for c in cg)
anyw = collections.Counter(a for c in cg for a in set(c['anywhere']))
grp = lambda c: 'main two' if posts[c['id']]['subreddit'] in ('CaregiverSupport', 'AgingParents') else 'other 11'
res = {'posts': 500, 'caregiver_posts': N, 'not_caregiver': 500 - N,
       'by_group': dict(collections.Counter(grp(c) for c in cg)),
       'cared_for': dict(collections.Counter(c['cared_for'] for c in cg)),
       'themes': [{'theme': t, 'main': main[t], 'main_pct': round(100*main[t]/N), 'anywhere': anyw[t], 'anywhere_pct': round(100*anyw[t]/N),
                   'main_by_group': dict(collections.Counter(grp(c) for c in cg if c['main'] == t))} for t in THEMES],
       'other_new_themes': [c['new_theme'] for c in cg if c['main'] == 'Other']}
json.dump(res, open('reddit-sample-theme-counts.json', 'w'), indent=1, ensure_ascii=False)
print('caregiver posts', N, res['by_group'], res['cared_for'])
for t in sorted(res['themes'], key=lambda x: -x['main']): print(f"{t['main']:4} ({t['main_pct']}%)  {t['anywhere']:4} ({t['anywhere_pct']}%)  {t['theme']}")
print('problems:', bad or 'none'); sys.exit(1 if bad else 0)
