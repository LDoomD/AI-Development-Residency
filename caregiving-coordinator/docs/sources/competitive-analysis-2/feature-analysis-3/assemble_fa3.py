"""Assemble Feature Analysis 3 grids and audit them. Run from competitive-analysis-2:
python3 -I feature-analysis-3/assemble_fa3.py"""
import json, re, sys
T = json.load(open('feature-analysis-3/fa3-text.json'))
C = json.load(open('feature-analysis-3/howwell-counts.json'))
report = open('../../reddit-caregiver-findings-2026-11-03.md').read()
reddit = {int(n) for n in re.findall(r'\b(\d+)\b', report)}
bad = []
def label(w, p):
    n = w + p
    if n < 5: return 'Too few to judge'
    if w * 3 >= 2 * n: return '🟢 Mostly works'
    if p * 3 >= 2 * n: return '🔴 Mostly problems'
    return '🟠 Mixed'
# main table: blank first column like the teacher's
main = [[''] + [h for h, _ in T['info_columns']] + [f for f, _ in T['features']],
        [''] + [q for _, q in T['info_columns']] + [q for _, q in T['features']]]
for r in T['rows']: main.append([''] + r['info'] + r['offers'])
# how-well table
hw = [['COMPANY'] + [f for f, _ in T['features']]]
for r in T['rows'][1:]:
    s = r['slug']; row = [r['info'][0]]
    for i in range(8):
        f = str(i + 1); off = r['offers'][i] == '✅'; c = C.get(s, {}).get(f)
        ph = T['phrases'].get(f'{s}|{f}', '')
        if c:
            cell = f"{label(c['works_items'], c['problem_items'])} · works {c['works_items']}, problems {c['problem_items']}" + (f" · {ph}" if ph else '')
            if not off: cell = 'Not offered, but families use it for this: ' + cell
            if not ph: bad.append(f'missing phrase {s}|{f}')
            # every (n) in the phrase must be a theme count in that box
            nums = {x[1] for x in c['works'] + c['problems']}
            for n in re.findall(r'\((\d+)\)', ph):
                if int(n) not in nums: bad.append(f'{s}|{f} phrase number {n} not in box themes')
        else:
            cell = '✅ Offered · no caregiver mentions it' if off else 'Not offered'
            if ph: bad.append(f'phrase without counts {s}|{f}')
        row.append(cell)
    hw.append(row)
# gaps: every "(a, b)" pair and "works a, problems b" must be a real box count; (Reddit n) must be in report
pairs = {(v['works_items'], v['problem_items']) for fs in C.values() for v in fs.values()}
allnums = {x[1] for fs in C.values() for v in fs.values() for x in v['works'] + v['problems']}
gtext = ' '.join(T['gaps'])
for a, b in re.findall(r'\((?:works )?(\d+), (?:problems )?(\d+)\)', gtext):
    if (int(a), int(b)) not in pairs: bad.append(f'gap pair ({a}, {b}) not a box count')
for n in re.findall(r'\(Reddit (\d+)\)', gtext):
    if int(n) not in reddit: bad.append(f'Reddit {n} not in report')
for n in re.findall(r'\((\d+)\)', gtext):
    if int(n) not in allnums and int(n) not in reddit: bad.append(f'gap number ({n}) not found')
# offers count claims
offers = {r['slug']: r['offers'] for r in T['rows'][1:]}
companies = [s for s in offers if s not in ('group-texts', 'paper-notebook')]
for i, (f, _) in enumerate(T['features']):
    print(f"{f}: offered by {sum(offers[s][i]=='✅' for s in companies)} of {len(companies)} companies")
gaps = T['gaps_title'] + '\n' + T['gaps_intro'] + '\n\n' + '\n\n'.join(T['gaps']) + '\n\n' + T['gaps_limits'] + '\n\n' + T['owner_note']
json.dump({'main': main, 'howwell': hw, 'gaps': gaps, 'offer_notes': T['offer_notes']}, open('feature-analysis-3/figma-fa3.json', 'w'), ensure_ascii=False)
print('problems:', bad or 'none')
if bad: sys.exit(1)

# audit the report-format gaps text too
gr = T['gaps_report']; bad2 = []
for a, b in re.findall(r'\((\d+), (\d+)\)', gr):
    if (int(a), int(b)) not in pairs: bad2.append(f'report pair ({a}, {b})')
for n in re.findall(r'\((\d+)\)', gr):
    if int(n) not in allnums and int(n) not in reddit: bad2.append(f'report number ({n})')
d2 = json.load(open('feature-analysis-3/figma-fa3.json')); d2.update({'gaps_report': gr, 'howwell_title': T['howwell_title'], 'howwell_sub': T['howwell_sub'], 'main_title': T['main_title']})
json.dump(d2, open('feature-analysis-3/figma-fa3.json', 'w'), ensure_ascii=False)
print('report problems:', bad2 or 'none'); sys.exit(1 if bad2 else 0)
