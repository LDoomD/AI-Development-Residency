import json,os,collections
D=os.path.dirname(os.path.abspath(__file__))+'/'
S=json.load(open(D+'check3d_sample_ids.json')); M=json.load(open(D+'manual_codes.json'))
pv="PV M|PV X|PV X|NA|PV W|PV M|PV N|PV M|PV M|PV X|PV M|PV M|PV X|PV X|PV N|PV N|PV X|PV N|PV M|PV X|PV X|PV X|PV X|PV N|PV X|PV X|PV X|PV X|PV X|PV N".split('|')
pr="PR X|PR M|PR X|PR X|PR N|NO X|PR W|PR M|PR N|PR M|PR X|PR M|PR N|PR M|PR X|PR X|PR W|NO X|PR M|PR N|PR M|PR X|PR M|PR X|PR N|PV X|PR W|PR X|PR X|PR X".split('|')
th="TH X|TH N|TH M|TH X|TH X|TH W|TH W|TH X|TH X|TH W|TH N|TH X|TH X|TH N|TH W|NA|TH X|TH N|TH X|TH W|TH X|TH W|TH X|TH X|TH X|NA|TH N|TH X|TH X|TH W".split('|')
mine={'paid_PV':pv,'paid_PR':pr,'ther_TH':th}
res={}
for g,ids in S.items():
    book='paid' if g.startswith('paid') else 'ther'
    tot=ty=ou=0; dis=[]
    oc=collections.Counter()
    for i,m in zip(ids,mine[g]):
        if m=='NA': continue
        h=M[book][i]; tot+=1
        ty+= h.split()[0]==m.split()[0]; ou+= h.split()[1]==m.split()[1]
        if h.split()[0]!=m.split()[0] or h.split()[1]!=m.split()[1]: dis.append((i,'helper='+h,'audit='+m))
        if h.split()[1]!=m.split()[1]: oc[(h.split()[1],m.split()[1])]+=1
    res[g]=(tot,ty,ou,dis,oc)
    print(f"{g}: n={tot} type agrees {ty}/{tot} ({100*ty//tot}%)  outcome agrees {ou}/{tot} ({100*ou//tot}%)  outcome disagreements (helper->audit): {dict(oc)}")
    for d in dis: print('   ',d)
# crosstab helper outcome vs earlier-reader status
import glob,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from audit_load import S as SRC
st={}
for f in glob.glob(SRC+'market-analysis-3/segments-11-12/codes/codes-*.json'):
    for d in json.load(open(f)): st[d['id']]=d['status']
ct=collections.Counter()
for book in('paid','ther'):
    for i,v in M[book].items():
        if v in('DUP',) or v.split()[0]=='NO': continue
        ct[(book,st.get(i),v.split()[1])]+=1
print("\nearlier-reader status x helper outcome (excluding NO/DUP):")
for k,v in sorted(ct.items(),key=lambda x:(x[0][0],str(x[0][1]),x[0][2])): print(' ',k,v)
