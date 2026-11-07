import json,collections,os
D=os.path.dirname(os.path.abspath(__file__))+'/'
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
names=['Care.com','Home Instead','Visiting Angels','Senior Helpers','Right at Home','Comfort Keepers','Papa','BetterHelp','Talkspace','Headway','Psychology Today','SonderMind','Zencare']
def oc(o):
    o=(o or '').upper()
    return {'WORKED':'W','MIXED':'M','DID NOT WORK':'N','NO OUTCOME':'none'}.get(o,'?')
for n in names:
    R=[r for r in rows if r['name']==n]
    L=collections.Counter(r['label'] for r in R)
    ind=[r for r in R if r['label'] in(1,2,3) and r['independent']]
    used=[r for r in R if r['label']==1 and r['independent']]
    o=collections.Counter(oc(r['fields']['outcome']) for r in used)
    a=collections.Counter(r['fields']['cared_for'] for r in ind)
    print(f"{n:17} read {len(R):3} L1 {L[1]:2} L2 {L[2]:2} L3 {L[3]:2} L4 {L[4]:2} L5 {L[5]:2} | indep(1-3) {len(ind):2} | users {len(used):2} outcome {dict(o)} | cared {dict(a)} | distinct ids {len({r['id'] for r in R})}")
