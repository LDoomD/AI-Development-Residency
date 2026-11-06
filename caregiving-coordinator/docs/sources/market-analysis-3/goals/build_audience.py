"""Build the updated audience tables (both audiences) from the board's forum counts and the Reddit codes.
Forum counts are copied from the Audience page (2378:7107) boxes. Run: python3 -I build_audience.py"""
import json
C = json.load(open('goal-counts.json')); NG = json.load(open('new-groups.json'))
T = json.load(open('../reddit-sample-by-audience.json'))
NAMES = {'M1':'Keep them safe and comfortable, spare them suffering','M2':'Do the right thing, avoid blame or guilt','M3':'Keep them at home and in control of their own life','M4':'Love, loyalty and promises',
 'S1':'Get help, relief or services','S2':'Find, choose or pay for a place','S3':'Manage money and legal affairs','S4':'Understand what is happening and what to do','S5':'Keep them safe and watch over them','S6':'Medicines',
 'L1':'Time and breaks for themselves','L2':'Keep their own life, job and money','L3':'Their own health and sanity'}
BOARD = {'Audience 1: parent': (55, {'M1':7,'M2':6,'M3':5,'M4':3,'S1':11,'S2':6,'S3':3,'S4':2,'S5':2,'S6':1,'L1':4,'L2':3,'L3':1}),
         'Audience 2: spouse or partner': (54, {'M1':11,'M2':1,'M3':4,'M4':9,'S1':6,'S2':7,'S5':5,'S6':1,'L1':2,'L2':4,'L3':7})}
pct = lambda a, n: f"{a} ({round(100*a/n)}%)"
out = {}
for aud, (fn, fb) in BOARD.items():
    rn = C[aud]['n']; rc = C[aud]['counts']; res = {}
    for cat, prefix, k in (('motivations','M','M'),('situational goals','S','S'),('life goals','L','L')):
        codes = [c for c in NAMES if c.startswith(prefix)]
        fr = sorted(codes, key=lambda c: -fb.get(c, 0)); rr = sorted(codes, key=lambda c: -rc.get(c, 0))
        rows = []
        for c in sorted(codes, key=lambda c: -rc.get(c, 0)):
            f = fb.get(c); r = rc.get(c, 0)
            frank = (fr.index(c) + 1) if f else None; rrank = rr.index(c) + 1
            rows.append([NAMES[c] + (" (on the board)" if f is not None else " (not on this audience's board)"), pct(f, fn) if f is not None else "not on the board", pct(r, rn), f"#{frank} → #{rrank}" if frank else f"new → #{rrank}"])
        for g, n in NG[f'{aud}|{k}']['groups'].items():
            if g != 'Other one-offs' and n: rows.append(["NEW from Reddit: " + g, "not on the board", pct(n, rn), "new"])
        res[cat] = rows
    out[aud] = {'n_reddit': rn, 'n_forum': fn, 'tables': res}
json.dump(out, open('audience-tables.json', 'w'), indent=1, ensure_ascii=False)
for a, v in out.items():
    print('==', a, v['n_reddit'])
    for cat, rows in v['tables'].items():
        print(' ', cat)
        for r in rows: print('    ', r)
