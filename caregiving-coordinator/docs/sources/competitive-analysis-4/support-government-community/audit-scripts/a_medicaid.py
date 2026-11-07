"""Check the '48 of 78 Medicaid reports are one NY CDPAP->PPL event' claim. Run: python3 -I a_medicaid.py"""
import json,re,pickle,collections
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
N='Medicaid waiver / HCBS / paid-family-caregiver programs (incl. CDPAP)'
m=[r for r in rows if r['name']==N and r['label_n'] in(1,2,3)]
print('Medicaid reports (labels1-3):',len(m))
def T(i): return (U.get(i) or packs.get(i))
rx_ppl=re.compile(r'cdpap|\bppl\b|public partnerships',re.I)
rx_ny=re.compile(r'new york|\bNY\b|\bNYS\b|nyc',re.I)
c=collections.Counter(); rowsout=[]
for r in m:
    t=T(r['id']); txt=t['text']; d=t.get('date') or ''
    ppl=bool(rx_ppl.search(txt)); ny=bool(rx_ny.search(txt))
    rowsout.append((r['id'],d,ppl,ny,r['label_n'],r['outcome']))
    c[('cdpap/ppl' if ppl else 'other', d[:7] if d else 'forum/undated')]+=1
print(sorted(c.items(),key=lambda x:(x[0][0],x[0][1])))
ppl=[x for x in rowsout if x[2]]
print('reports whose text mentions CDPAP or PPL:',len(ppl))
print(' of which dated 2025-03 or 2025-04:',sum(1 for x in ppl if x[1][:7] in('2025-03','2025-04')))
print(' of which dated 2025-03..2025-06:',sum(1 for x in ppl if x[1][:7] in('2025-03','2025-04','2025-05','2025-06')))
print(' not CDPAP/PPL mention but dated 2025-03/04:',sum(1 for x in rowsout if not x[2] and x[1][:7] in('2025-03','2025-04')))
print('months of cdpap/ppl reports:',collections.Counter(x[1][:7] for x in ppl))
# strict: PPL switch language
rx_switch=re.compile(r'\bppl\b|public partnerships|fiscal intermediar|payroll|transition',re.I)
sw=[x for x in rowsout if x[2] and rx_switch.search(T(x[0])['text']) and x[1][:7] in('2025-03','2025-04')]
print('strict (CDPAP/PPL + payroll/transition words + dated Mar/Apr 2025):',len(sw))
# overlap between candidates
names=collections.defaultdict(set)
for r in rows:
    if r['label_n'] in(1,2,3): names[r['id']].add(r['name'])
ov=[(i,n) for i,n in names.items() if N in n and 'IHSS (California paid family caregiver program)' in n]
print('ids counted as BOTH Medicaid and IHSS reports:',len(ov),ov[:5])
ih=[r for r in rows if r['name'].startswith('IHSS') and r['label_n'] in(1,2,3)]
u=set(r['id'] for r in m)|set(r['id'] for r in ih)
print('Medicaid+IHSS reports',len(m)+len(ih),'unique posts',len(u))
# print the non-ppl dated Mar/Apr 2025
for x in rowsout:
    if x[2] and x[1][:7] not in('2025-03','2025-04'): print('cdpap/ppl outside Mar-Apr 25:',x)
