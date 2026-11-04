"""Check every (Source N) in gaps-uvo-v2.json: N must be a theme count for that competitor,
or a figure in the Reddit report. python3 -I audit_gaps_uvo.py"""
import json, re, sys
SL = {'Caring Village':'caring-village','CaringBridge':'caringbridge','Lotsa':'lotsa','Medisafe':'medisafe','MyChart':'mychart',
      'Lively':'lively','Medical Guardian':'medical-guardian','Group texts':'group-texts','Paper notebook':'paper-notebook'}
counts = {}
for name, s in SL.items():
    t = json.load(open(f'themes/{s}.json')); c = set()
    for g in [t['works_well'], t['does_not_work_well']] + list(t['questions'].values()):
        c |= {x['count'] for x in g}
    counts[name] = c
report = open('../../reddit-caregiver-findings-2026-11-03.md').read()
reddit_nums = {int(n) for n in re.findall(r'\b(\d+)\b', report)}
d = json.load(open('gaps-uvo-v2.json'))
text = json.dumps(d, ensure_ascii=False)
bad = n = 0
for grp in re.findall(r'\(([^()]*\d[^()]*)\)', text):
    for part in grp.split(','):
        m = re.match(r'\s*(Caring Village|CaringBridge|Lotsa|Medisafe|MyChart|Lively|Medical Guardian|Group texts|Paper notebook|Reddit)\s+(\d+)', part)
        if not m: continue
        n += 1; src, num = m.group(1), int(m.group(2))
        ok = num in reddit_nums if src == 'Reddit' else num in counts[src]
        if not ok: bad += 1; print('NOT FOUND', src, num)
print(n, 'claims checked,', bad, 'not found'); sys.exit(1 if bad else 0)
