"""Theme counts in the Reddit sample split by who is cared for (Audience 1 = parent, Audience 2 = spouse or partner).
Run: python3 -I count_by_audience.py"""
import json, collections
codes = []
for i in range(1, 5): codes += json.load(open(f'codes/part-{i}.json'))
G = json.load(open('other-groups.json'))
hands = set(G['Hands-on personal care, equipment and supplies'])
out = {}
for aud, key in (('Audience 1: parent', 'parent'), ('Audience 2: spouse or partner', 'spouse or partner')):
    cs = [c for c in codes if c['caregiver'] and c['cared_for'] == key]
    n = len(cs)
    main = collections.Counter(c['main'] for c in cs)
    anyw = collections.Counter(a for c in cs for a in set(c['anywhere'] + [c['main']]))
    h = sum(1 for c in cs if c['main'] == 'Other' and c['new_theme'] in hands)
    out[aud] = {'n': n, 'themes': {t: [main[t], anyw[t]] for t in sorted(anyw, key=lambda x: -anyw[x])}, 'hands_on_main': h}
json.dump(out, open('reddit-sample-by-audience.json', 'w'), indent=1, ensure_ascii=False)
for a, v in out.items():
    print(a, 'n =', v['n'], 'hands-on main', v['hands_on_main'])
    for t, (m, an) in v['themes'].items(): print(f"   {m:3} ({round(100*m/v['n'])}%) / {an:3} ({round(100*an/v['n'])}%)  {t}")
