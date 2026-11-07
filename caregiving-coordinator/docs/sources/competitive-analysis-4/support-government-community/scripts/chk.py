import pickle,re,sys,glob,json
U=pickle.load(open('U.pkl','rb'));PK=pickle.load(open('packs.pkl','rb'))
def txt(i):
    a=U[i]['text'] if i in U else ''
    b=PK[i]['text'] if i in PK else ''
    # thread-level forum ids: join all comments of the thread
    c=' '.join(v['text'] for k,v in U.items() if k.startswith(i+'-COMMENT')) if i.startswith(('alzconnected','agingcare')) else ''
    return a+' '+b+' '+c

def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
bad=0;n=0
for f in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'dec/*.txt')):
    for ln in open(f):
        ln=ln.rstrip('\n')
        if not ln.strip():continue
        p=ln.split('|')
        if len(p)<7 or p[1] in('4','5'):
            if p[0] not in U and p[0] not in PK: print('BADID',f,p[0]);bad+=1
            continue
        i=p[0];q=p[6]
        if i not in U and i not in PK: print('BADID',f,i);bad+=1;continue
        n+=1
        if len(q.split())>20: print('LONG',f,i,len(q.split()));bad+=1
        if norm(q) not in norm(txt(i)): print('NOMATCH',f,i,q[:80]);bad+=1
print('checked',n,'bad',bad)
