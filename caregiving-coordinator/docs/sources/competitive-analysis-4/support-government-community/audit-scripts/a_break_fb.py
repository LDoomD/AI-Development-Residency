"""Check 3c (where does a break appear) and 3d (Facebook negativity; Discord/WhatsApp demand vs supply). Run: python3 -I a_break_fb.py"""
import json,collections,re,pickle
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
c=collections.Counter(); cu=collections.Counter()
for r in rows:
    if 'break' in r['used_for'] and r['label_n'] in(1,2,3):
        c[r['name']]+=1
        if r['label_n']==1: cu[r['name']]+=1
print('reports tagged used_for=break (labels1-3), by candidate:'); 
for n,k in c.most_common(): print(f'  {k:3d} (used it: {cu[n]:2d})  {n}')
# which of those are label 1 and outcome worked
print('\nbreak + label1 + WORKED:',[(r['id'],r['name'][:12]) for r in rows if 'break' in r['used_for'] and r['label_n']==1 and r['outcome']=='WORKED'])
# Facebook
fb=[r for r in rows if r['name']=='Facebook caregiver groups' and r['label_n'] in(1,2,3)]
print('\nFacebook reports',len(fb),collections.Counter((r['label_n'],r['used_for'][:14],r['outcome']) for r in fb))
sup=[r for r in fb if r['label_n']==1 and 'emotional' in r['used_for']]
print('FB label1 emotional-support users:',len(sup),collections.Counter(r['outcome'] for r in sup))
print('FB all label1 users:',sum(r['label_n']==1 for r in fb),collections.Counter(r['outcome'] for r in fb if r['label_n']==1))
print('FB all reports outcome:',collections.Counter(r['outcome'] for r in fb))
# distinct cared_for etc for FB used_for
print(collections.Counter(r['used_for'] for r in fb))
# Discord / WhatsApp
for n in ['Discord caregiver servers','WhatsApp caregiver community groups','WhatsApp family group chat']:
    rs=[r for r in rows if r['name']==n]
    print('\n',n,'read',len(rs),collections.Counter((r['label_n']) for r in rs))
    print('  notes:',collections.Counter(r['note'][:45] for r in rs if r['note']).most_common(6))
    for r in rs:
        if r['label_n'] in(1,2,3): print('   L%d %s %s | %s'%(r['label_n'],r['outcome'][:3],r['id'],r['quote'][:100]))
