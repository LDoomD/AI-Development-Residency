"""Audit answers-v2.json: every bracketed count '(N' must equal a theme count in that
competitor's themes file, the kept total, or a Reddit-report figure. Also flags empty cells. python3 -I audit_answers.py"""
import json, re, sys
SLUG = {'Caring Village':'caring-village','CaringBridge':'caringbridge','Lotsa Helping Hands':'lotsa','Medisafe':'medisafe',
        'Everplans':'everplans','Epic MyChart':'mychart','Lively':'lively','Medical Guardian':'medical-guardian',
        'Group texts':'group-texts','Paper notebook and visit log':'paper-notebook'}
REDDIT = {217,132,187,97,77,67,59,24}
a = json.load(open('answers-v2.json')); bad = 0
for row in a['rows']:
    t = json.load(open(f"themes/{SLUG[row['Competitor']]}.json"))
    counts = {t['items_kept']}
    for g in [t['works_well'], t['does_not_work_well']] + list(t['questions'].values()):
        counts |= {x['count'] for x in g}
    for col in a['columns']:
        v = row.get(col, '')
        if not v.strip(): print('EMPTY', row['Competitor'], col); bad += 1
        if col in ('What market gaps have they NOT filled?',): allowed = counts | REDDIT
        else: allowed = counts
        for m in re.finditer(r'\((\d+)(?: of (\d+))?[^)]*\)', v):
            n = int(m.group(1)); tot = m.group(2)
            if n not in allowed and n not in REDDIT:
                print(f"CHECK {row['Competitor']} | {col} | {m.group(0)}"); bad += 1
            if tot and int(tot) != t['items_kept']:
                print(f"TOTAL {row['Competitor']} | {col} | {m.group(0)} kept={t['items_kept']}"); bad += 1
print('problems:', bad); sys.exit(1 if bad else 0)
