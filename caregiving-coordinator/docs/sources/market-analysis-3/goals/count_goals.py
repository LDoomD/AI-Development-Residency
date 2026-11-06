"""Check and count motivations, situational goals and life goals by audience. Run: python3 -I count_goals.py"""
import json, collections, sys
posts = {}; codes = []
for i in range(1, 4):
    for p in json.load(open(f'posts-{i}.json')): posts[p['id']] = p
    codes += json.load(open(f'codes-{i}.json'))
bad = []
if len(codes) != 304 or len({c['id'] for c in codes}) != 304: bad.append(f'{len(codes)} codes')
VALID = {'motivations': {'M1','M2','M3','M4','M-NEW'}, 'situational': {'S1','S2','S3','S4','S5','S6','S-NEW'}, 'life': {'L1','L2','L3','L-NEW'}}
for c in codes:
    for k, v in VALID.items():
        for x in c[k]:
            if x not in v: bad.append(f'{c["id"]} bad code {x}')
    for k, q in c['quotes'].items():
        if q and q not in posts[c['id']]['text']: bad.append(f'{c["id"]} quote {k}')
out = {}
for aud, key in (('Audience 1: parent', 'parent'), ('Audience 2: spouse or partner', 'spouse or partner')):
    cs = [c for c in codes if c['cared_for'] == key]
    cnt = collections.Counter(x for c in cs for k in VALID for x in c[k])
    new = {k: [c['new'][k] for c in cs if c['new'].get(k)] for k in ('M', 'S', 'L')}
    out[aud] = {'n': len(cs), 'counts': dict(cnt), 'new': new}
    print(aud, 'n =', len(cs)); print('  ', sorted(cnt.items()))
    for k, v in new.items(): print('   new', k, len(v))
json.dump(out, open('goal-counts.json', 'w'), indent=1, ensure_ascii=False)
print('problems:', bad or 'none'); sys.exit(1 if bad else 0)
