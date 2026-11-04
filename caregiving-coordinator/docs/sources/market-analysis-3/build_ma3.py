"""Fill the market analysis 3rd Version text from the counted data. Run: python3 -I build_ma3.py"""
import json, re, sys
T = json.load(open('ma3-text.json')); C = json.load(open('reddit-sample-theme-counts.json')); G = json.load(open('other-groups.json'))
N = C['caregiver_posts']
val = {'N': str(N), 'MAIN_TWO': str(C['by_group']['main two'])}
for t in C['themes']: val[t['theme']] = f"{t['main']} ({t['main_pct']}%) / {t['anywhere']} ({t['anywhere_pct']}%)"
for k, v in C['cared_for'].items(): val['CF_' + k] = f"{v} ({round(100*v/N)}%)"
for key, g in [('HANDS_ON','Hands-on personal care, equipment and supplies'),('TECH',"Technology the older person can't use or is misled by"),('EOL','End-of-life decisions and conversations'),('PAID','Paid caregivers asking about their own work'),('GOOD','Sharing good moments and life stories'),('MIXED','Mixed one-offs')]:
    val[key] = f"{len(G[g])} ({round(100*len(G[g])/N)}%)" if key != 'HANDS_ON' else f"{len(G[g])} ({round(100*len(G[g])/N)}%)"
A = json.load(open('reddit-sample-by-audience.json'))
for tag, aud in (('A1','Audience 1: parent'),('A2','Audience 2: spouse or partner')):
    n = A[aud]['n']; val[tag+'N'] = str(n)
    for t, (m, an) in A[aud]['themes'].items(): val[f'{tag}:{t}'] = f"{m} ({round(100*m/n)}%) / {an} ({round(100*an/n)}%)"
val['A1HANDS'] = str(A['Audience 1: parent']['hands_on_main'])
missing = set()
def fill(s):
    def rep(m):
        k = m.group(1)
        if k in val: return val[k]
        missing.add(k); return m.group(0)
    return re.sub(r'\{([^{}]+)\}', rep, s)
how = T.pop('how'); out = json.loads(fill(json.dumps(T, ensure_ascii=False))); out['how'] = how
json.dump(out, open('ma3-filled.json', 'w'), ensure_ascii=False, indent=1)
print('missing placeholders:', missing or 'none'); sys.exit(1 if missing else 0)
