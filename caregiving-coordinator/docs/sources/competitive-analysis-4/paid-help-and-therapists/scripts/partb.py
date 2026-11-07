import json,glob,re,sys
sys.path.insert(0,'.')
S='/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/market-analysis-3/segments-11-12/'
packs={}
for f in sorted(glob.glob(S+'packs/pack-*.json')):
    for p in json.load(open(f)): packs[p['id']]=p
sets=json.load(open('sets.json'))
codes={}
for f in sorted(glob.glob(S+'codes/codes-*.json')):
    for c in json.load(open(f)): codes[c['id']]=c
lab=json.load(open(S+'audience-labels.json'))
CUE=re.compile(r"\b(aide|aides|agency|agencies|caregiver|caregivers|carer|carers|hired|hire|hiring|home ?care|home health|companion|sitter|private ?pay|private duty|nurse|nursing|CNA|HHA|PCA|therap\w*|counsel\w*|psych\w*|EAP|employee assistance|social worker|licensed|insurance|medicare|medicaid|coverage|session|sessions|app|website|directory|online|marketplace|franchise|company|service|services|program|hospital|clinic|church|volunteer|nanny|cleaner|housekeeper|respite|sitting|live-in|overnight|visiting|helper|helpers|psychiatrist|coach|hotline|helpline)\b",re.I)
def sents(t):
    t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[.!?])\s+',t)
