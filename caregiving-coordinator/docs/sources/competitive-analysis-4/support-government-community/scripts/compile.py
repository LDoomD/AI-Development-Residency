import glob,os,json,re,pickle,collections
U=pickle.load(open('U.pkl','rb'));PK=pickle.load(open('packs.pkl','rb'))
M="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/market-analysis-3/segments-11-12/"
AL=json.load(open(M+'audience-labels.json'))
NAME={
'hospice_respite':'Hospice respite benefit','alz_assoc':"Alzheimer's Association (helpline, groups, education)",'alz_assoc_2':"Alzheimer's Association (helpline, groups, education)",
'alzconnected_forum':'ALZConnected forum (the data source itself)','medicaid':'Medicaid waiver / HCBS / paid-family-caregiver programs (incl. CDPAP)','ihss':'IHSS (California paid family caregiver program)',
'pace':'PACE (all-inclusive care program)','wellthy':'Wellthy','lotsa':'Lotsa Helping Hands','caringbridge':'CaringBridge','mealtrain':'Meal Train','cozi':'Cozi','wellspouse':'Well Spouse Association','fca':'Family Caregiver Alliance','guide':'Medicare GUIDE program','teepa':'Teepa Snow / Positive Approach to Care','alanon':'Al-Anon','nami':'NAMI','eldercare_locator':'Eldercare Locator',
'facebook':'Facebook caregiver groups','discord':'Discord caregiver servers','whatsapp_community':'WhatsApp caregiver community groups','whatsapp_family':'WhatsApp family group chat','subreddits':'Subreddit communities (r/CaregiverSupport etc.; sample read)','supportgroup':'Support group (generic; any sponsor)',
'papa':'Papa Pals','torchlight':'Torchlight','regional_center':'Regional Center / state developmental disability agency','meetup':'Meetup caregiver group (NYC)','psychtoday':'Psychology Today / online therapist finders','aegis_passages':'Named respite facilities (Aegis, Passages)','ship':'SHIP counselor','franchise_homecare':'Franchise home care (Home Instead, Visiting Angels)','meals_on_wheels':'Meals on Wheels','hospice_hotline':'Hospice hotline'}
def key(fn):
    b=os.path.basename(fn)[:-4]
    b=re.sub(r'_(\d+|tmpl)$','',b)
    return b
def norm(s): return re.sub(r'\s+',' ',s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')).strip()
def fulltext(i):
    a=U[i]['text'] if i in U else ''
    b=PK[i]['text'] if i in PK else ''
    c=' '.join(v['text'] for k,v in U.items() if k.startswith(i+'-COMMENT')) if i.startswith(('alzconnected','agingcare')) else ''
    return a+' '+b+' '+c
def url(i):
    if i in U: return U[i].get('url','')
    return PK[i].get('url','') if i in PK else ''
LAB={'1':'1 caregiver used it','2':'2 considering or asking','3':'3 recommends or warns','4':'4 vendor, staff, ad or survey-bait','5':'5 passing mention or wrong meaning'}
OUT={'W':'WORKED','D':'DID NOT WORK','M':'MIXED','N':'NO OUTCOME'}
rows=[];seen=set()
for fn in sorted(glob.glob('dec/*.txt')):
    nm=NAME[key(fn)]
    for ln in open(fn):
        ln=ln.rstrip('\n')
        if not ln.strip(): continue
        p=ln.split('|')+['']*8
        i,lab,use,cared,out,block,quote=p[0],p[1],p[2],p[3],p[4],p[5],p[6]
        note=p[6] if lab in('4','5') else ''
        if lab in('4','5'): quote=''
        if (nm,i) in seen: print('DUP',nm,i); continue
        seen.add((nm,i))
        src='reddit' if not i.startswith(('alzconnected','agingcare')) else i.split('-')[0]
        cs='reading'
        if cared in('unclear','') and lab in('1','2','3'):
            lab_al=AL.get(i,{}).get('label')
            if lab_al and lab_al!='unclear': cared=lab_al;cs='audience-labels.json (earlier pass)'
        cared={'spouse':'spouse or partner'}.get(cared,cared)
        rows.append(dict(id=i,name=nm,label=LAB[lab],label_n=int(lab),used_for=use,cared_for=(cared or 'unclear') if lab in('1','2','3') else '',cared_for_source=cs if lab in('1','2','3') else '',outcome=OUT.get(out,'') if lab in('1','2','3') else '',blockers=block if lab in('1','2','3') else '',quote=quote,note=note if lab in('4','5') else '',source=src,url=url(i),quote_checked=bool(quote) and norm(quote) in norm(fulltext(i))))
bad=[r for r in rows if r['quote'] and not r['quote_checked']]
print(len(rows),'bad quotes',len(bad))
with open('MENTIONS-READ.jsonl','w') as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
pickle.dump(rows,open('rows.pkl','wb'))
c=collections.Counter(r['name'] for r in rows);print(c)
