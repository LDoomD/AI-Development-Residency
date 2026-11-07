import sys,re,json,glob,os,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import load,S
U,_=load()
rel=[]
for f in glob.glob(S+'market-analysis-3/segments-11-12/codes/codes-*.json'):
    rel+=[d for d in json.load(open(f)) if d.get('relevant')]
ids=[d['id'] for d in rel]
print("relevant posts:",len(ids),"found in corpus:",sum(i in U for i in ids))
missing=[i for i in ids if i not in U]; print("not in corpus:",missing[:10])
T={i:U[i]['text'] for i in ids if i in U}
# 1) brand list (broad)
BR=r"care\.com|home instead|visiting angels|senior helpers|right at home|comfort keepers|papa\b(?! ?\w*,)|betterhelp|talkspace|headway|psychology today|sondermind|zencare|rula|grow therapy|lyra|alma\b|careyaya|homewatch|interim health|bright ?star|honor care|wellthy|torchlight|amada|brightwood|bayada|amedisys|kindred|genesis|centerwell|encompass|aveanna|addus|comfort care|caring bridge|caringbridge|lotsa|aplaceformom|a place for mom|carepatrol|seniors helping seniors|seniorly|caring\.com|cerebral|thriveworks|teladoc|headspace|calm app|ahead|cake\b|cariloop|nurse next door|sitter ?city|rover|angi|thumbtack|nextdoor|aegis|passages|sunrise|brookdale|goddard|primrose|atria|holiday retirement|home helpers|always best care|synergy|griswold|caring senior service|nurse ?on ?call|elara|kinnser|hello alpha"
rx=re.compile(BR,re.I); cnt=collections.Counter(); where=collections.defaultdict(set)
for i,t in T.items():
    for m in rx.finditer(t):
        w=m.group(0).lower(); cnt[w]+=1; where[w].add(i)
print({k:len(v) for k,v in where.items()})
# 2) capitalized multiword name finder (not at sentence start)
cap=collections.Counter(); wh=collections.defaultdict(set)
pat=re.compile(r'(?<![.!?\n]\s)(?<!^)\b([A-Z][a-zA-Z&\'\.]+(?:\s+(?:of\s+|for\s+|at\s+|&\s+)?[A-Z][a-zA-Z&\'\.]+){1,3})')
for i,t in T.items():
    for m in pat.finditer(t):
        cap[m.group(1)]+=1; wh[m.group(1)].add(i)
json.dump({k:sorted(v) for k,v in wh.items() if len(v)>=1},open(os.path.dirname(os.path.abspath(__file__))+'/check3c_capnames.json','w'))
print("distinct capitalized multiword strings:",len(cap))
top=[(k,len(wh[k])) for k in wh]
top.sort(key=lambda x:-x[1])
print(top[:150])
