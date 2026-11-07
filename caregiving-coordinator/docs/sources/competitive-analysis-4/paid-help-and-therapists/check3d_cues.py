import sys,re,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load
U,_=load()
M=json.load(open(os.path.dirname(os.path.abspath(__file__))+'/manual_codes.json'))
th=re.compile(r'therap|counsel|psycholog|psychiat|social worker|\bEAP\b|support group|mental health|\bLCSW\b',re.I)
pd=re.compile(r'aide|caregiver|care giver|carer|agency|hired|hire|home care|companion|sitter|\bCNA\b|respite|\bVA\b|waiver|medicaid|helper|\bPCA\b|\bPSW|home health|paid|care package|attendant|nurse|day program|help in|someone (?:to|come)|come in',re.I)
for grp,rx in (('ther',th),('paid',pd)):
    bad=[(k,v) for k,v in M[grp].items() if v!='DUP' and not rx.search(U[k]['text'])]
    print(grp,"ids missing from corpus:",[k for k in M[grp] if k not in U])
    print(grp,"coded posts with NO cue word at all in full text:",len(bad),bad)
    # by type
import collections
th_bad=[k for k,v in M['ther'].items() if v.startswith('TH') and not re.search(r'therap|counsel|psycholog|psychiat',U[k]['text'],re.I)]
print("TH-coded posts with no therapist/counselor/psychologist/psychiatrist word:",len(th_bad),th_bad)
