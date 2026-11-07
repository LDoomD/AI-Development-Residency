"""Check 2 step B: the auditor's own blind labels (written BEFORE comparing to the helper's), then compare.
Order matches sample50.json (seed 20261106). Fields: label 1-5, outcome W/M/D/N (worked/mixed/did not work/no outcome, '-' for 4/5), cared_for P/S/O/C/CL/U (parent/spouse/other relative/child/client/unclear, '-' for 4/5).
Run: python3 -I a_blind_labels.py"""
import json,collections
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
MINE=[
(1,4,'-','-'),(2,2,'N','P'),(3,3,'N','S'),(4,2,'N','P'),(5,3,'N','U'),(6,5,'-','-'),(7,1,'N','P'),(8,2,'N','U'),(9,3,'N','U'),(10,1,'W','U'),
(11,2,'N','P'),(12,1,'N','S'),(13,2,'N','P'),(14,1,'W','U'),(15,4,'-','-'),(16,2,'D','P'),(17,1,'N','C'),(18,1,'W','P'),(19,5,'-','-'),(20,5,'-','-'),
(21,3,'W','U'),(22,2,'N','P'),(23,2,'N','U'),(24,1,'D','U'),(25,2,'N','U'),(26,1,'W','U'),(27,1,'D','P'),(28,4,'-','-'),(29,2,'N','P'),(30,2,'N','P'),
(31,1,'W','P'),(32,1,'N','P'),(33,1,'D','P'),(34,2,'D','P'),(35,1,'M','O'),(36,4,'-','-'),(37,1,'D','O'),(38,2,'D','O'),(39,3,'W','U'),(40,3,'N','U'),
(41,2,'N','P'),(42,1,'D','P'),(43,5,'-','-'),(44,3,'N','O'),(45,3,'W','P'),(46,4,'-','-'),(47,1,'D','P'),(48,4,'-','-'),(49,2,'N','S'),(50,2,'N','U')]
pick=json.load(open(SC+'sample50.json'))
OUT={'WORKED':'W','MIXED':'M','DID NOT WORK':'D','NO OUTCOME':'N','':'-'}
CF={'parent':'P','spouse or partner':'S','other relative':'O','child':'C','client':'CL','unclear':'U','':'-'}
agL=agO=agC=0; nO=nC=0; dis=[]
for (i,l,o,c),p in zip(MINE,pick):
    hl=p['label_n']; ho=OUT[p['outcome']]; hc=CF[p['cared_for']]
    agL+= (l==hl)
    if l!=hl: dis.append(f"#{i} {p['id']} [{p['name'][:28]}] LABEL mine {l} vs helper {hl}")
    if l in(1,2,3) and hl in(1,2,3):
        nO+=1; agO+=(o==ho)
        if o!=ho: dis.append(f"#{i} {p['id']} [{p['name'][:28]}] OUTCOME mine {o} vs helper {ho}")
        nC+=1; agC+=(c==hc)
        if c!=hc: dis.append(f"#{i} {p['id']} [{p['name'][:28]}] CARED_FOR mine {c} vs helper {hc}")
print(f'label agreement {agL}/50 = {agL/50:.0%}')
print(f'outcome agreement (both say caregiver report 1-3) {agO}/{nO} = {agO/nO:.0%}')
print(f'cared_for agreement (both 1-3) {agC}/{nC} = {agC/nC:.0%}')
# counted-as-caregiver-report agreement (1-3 vs 4-5)
rep=sum(((l in(1,2,3))==(p['label_n'] in(1,2,3))) for (i,l,o,c),p in zip(MINE,pick))
print(f'agree on "is a caregiver report (1-3) vs not (4-5)": {rep}/50 = {rep/50:.0%}')
print('DISAGREEMENTS',len(dis))
for d in dis: print(' ',d)
