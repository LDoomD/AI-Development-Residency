"""Check headline numbers in SYNTHESIS.md sections 1-3 and 6 against MENTIONS-READ.jsonl. Run: python3 -I a_headline.py"""
import json,collections
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
def rep(n): return [r for r in rows if r['name'].startswith(n) and r['label_n'] in(1,2,3)]
M=rep('Medicaid');I=rep('IHSS');P=rep('PACE');H=rep('Hospice respite');A=rep("Alzheimer");S=rep('Support group');F=rep('Facebook')
print('Medicaid+IHSS reports',len(M)+len(I),'used_for paying:',sum('paying' in r['used_for'] for r in M+I),'(claim 151 of 155)')
print('Medicaid used_for',collections.Counter(r['used_for'] for r in M))
print('Medicaid+IHSS worked',sum(r['outcome']=='WORKED' for r in M+I),'(claim 7)')
print('Medicaid+IHSS cared_for',collections.Counter(r['cared_for'] for r in M),collections.Counter(r['cared_for'] for r in I))
print('hospice outcomes',collections.Counter(r['outcome'] for r in H),'label',collections.Counter(r['label_n'] for r in H))
print('hospice blockers',collections.Counter(r['blockers'] for r in H if r['blockers']))
print('hospice break',sum('break' in r['used_for'] for r in H),'refus in blockers',sum(('refus' in r['blockers'].lower()) for r in H))
print('hospice DNW detail:');[print('  ',r['id'],r['label_n'],r['blockers'],'|',r['quote'][:70]) for r in H if r['outcome']=='DID NOT WORK']
print('hospice worked/mixed:');[print('  ',r['id'],r['outcome'],'|',r['quote'][:80]) for r in H if r['outcome'] in('WORKED','MIXED')]
print('support group by label',collections.Counter(r['label_n'] for r in S),'outcomes',collections.Counter(r['outcome'] for r in S))
print('support group asking (label 2):',sum(r['label_n']==2 for r in S),'(claim 16)')
print('support group label1 outcomes',collections.Counter(r['outcome'] for r in S if r['label_n']==1),'(claim 7 of 15 worked in sec 6; table says worked 8 overall)')
print('Alz label1 / outcomes',sum(r['label_n']==1 for r in A),collections.Counter(r['outcome'] for r in A),collections.Counter(r['used_for'] for r in A))
print('Alz label3 WORKED (recommendations marked worked):',[r['id'] for r in A if r['label_n']==3 and r['outcome']=='WORKED'])
print('IHSS label2 and denial blockers:',sum(r['label_n']==2 for r in I),'; blockers with eligib:',sum('eligib' in r['blockers'] for r in I))
print('PACE worked by cared_for',collections.Counter((r['cared_for'],r['outcome']) for r in P if r['cared_for']=='spouse or partner'))
print('PACE break reports:',[(r['id'],r['label_n'],r['outcome'][:3]) for r in P if 'break' in r['used_for']])
