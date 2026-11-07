import json,re,pickle,collections
P=pickle.load(open('packs.pkl','rb'));rel=json.load(open('rel_ids.json'));sg=set(json.load(open('sg_ids.json')))
T={ # (kind, regex)
 # named organizations / programs / services
 ('N',"Alzheimer's Association (incl. helpline, chapter)"):r"alzheimer'?s?[’]? assoc|alz\.? assoc|alz association|alz\.org|alzheimer'?s?[’]? (hot|help)line|800.272.3900",
 ('N','ALZConnected forum'):r"alzconnected|alz connected",
 ('N','Reddit communities (r/CaregiverSupport etc.)'):r"\breddit\b|\br/\w+|\bthis sub\b|\bsubreddit\b",
 ('N','Facebook group'):r"(facebook|\bfb\b)[ \-]*(\w+ ){0,3}(support |caregiver |dementia )?(groups?|pages?|communit)",
 ('N','Discord'):r"\bdiscord\b",
 ('N','WhatsApp group'):r"whats ?app (community |support )?group|whats ?app community",
 ('N','Al-Anon'):r"al-?anon",
 ('N','NAMI'):r"\bNAMI\b",
 ('N','Teepa Snow / Positive Approach to Care'):r"\bteepa\b|positive approach",
 ('N','Wellthy'):r"\bwellthy\b",
 ('N','Papa (companion service)'):r"\bpapa pals?\b|\bjoinpapa\b|\bpapa (app|inc)\b",
 ('N','Torchlight'):r"\btorchlight\b",
 ('N','Meals on Wheels'):r"meals on wheels",
 ('N','Home Instead / Visiting Angels / Comfort Keepers (franchise home care)'):r"home instead|visiting angels|comfort keepers|right at home|seniors helping seniors|brightstar|griswold|amada",
 ('N',"Psychology Today / SonderMind / Zencare (therapist finders)"):r"psychology today|sondermind|zencare|betterhelp|talkspace|open path",
 ('N','Papa / Care.com / Caring.com / A Place for Mom'):r"care\.com|caring\.com|place for mom|agingcare\.com",
 ('N','Medicare GUIDE program'):r"\bGUIDE (model|program)\b",
 ('N','Medicaid waiver / HCBS (all state names)'):r"medicaid waiver|waiver program|\bwaiver\b|\bHCBS\b|home and community[- ]based|community choices|\bCAPDA\b|\bIRIS\b|\bCDPAP\b|\bCOPES\b|medi-?cal|\bADvantage\b|elderly waiver|aged (and|&) disabled",
 ('N','IHSS (California)'):r"\bIHSS\b|in-home supportive services",
 ('N','PACE'):r"\bPACE\b",
 ('N','Hospice (respite / hospice team support)'):r"hospice",
 ('N','VA caregiver programs (PCAFC, Aid & Attendance, VD-HCBS)'):r"\bVA\b|veterans?'? (affairs|administration)|\bPCAFC\b|aid (&|and) attendance|champva|tricare",
 ('N','Area Agency on Aging / dept of aging / council on aging / senior services'):r"area agenc|\bAAA\b|department (of|on) aging|council (on|for) (the )?aging|aging services|senior services|elderly affairs|office (of|on) aging|aging and disability|\bADRC\b|agencyoptions|ageoptions",
 ('N','Adult Protective Services'):r"adult protective|\bAPS\b",
 ('N','Regional Center / developmental disability agency'):r"regional center|\bDDS\b|developmental disabilit\w+ (agency|services|administration)|\bAPD\b|agency for persons with disabilities",
 ('N','SHIP counselor'):r"\bSHIP\b",
 ('N','ARCH respite / Lifespan Respite / NFCSP'):r"arch (national )?respite|lifespan respite|national family caregiver support|\bNFCSP\b",
 ('N','Employee assistance program (EAP)'):r"employee assistance|\bEAP\b",
 ('N','FMLA / paid family leave'):r"\bFMLA\b|paid (family|medical) leave|\bPFML\b|caregiver leave",
 ('N','Meetup group'):r"\bmeetup\b",
 ('N','YouTube channels (support content)'):r"youtube",
 ('N','Aegis / Brookdale / Silverado etc. (named facilities)'):r"\baegis\b|brookdale|silverado|sunrise senior|atria|passages\b",
 # generic types
 ('G','Support group (generic)'):r"support groups?|caregiver groups?|peer support",
 ('G','Respite care (any type)'):r"respite",
 ('G','Adult day program / center'):r"adult day|day program|day center|senior day|day care for (adults|seniors)|adult daycare",
 ('G','Therapist / counselor for the caregiver'):r"therapist|therapy|counsel(or|ing|lor)|psychiatr|psycholog",
 ('G','Paid aide / companion / home care agency'):r"(home|in-home|private) ?(care|health) (aide|agency|worker|company)|caregiver agency|companion|\bHHA\b|home health aide|\baides?\b|sitter|care agency|nurse'?s? aide",
 ('G','Church / faith community'):r"\b(church|synagogue|temple|parish|pastor|priest|rabbi|ministry|mosque|faith community)\b",
 ('G','Senior center / community center'):r"senior cent(er|re)|community cent(er|re)|\bsenior (services|program)",
 ('G','Social worker / case manager / navigator'):r"social worker|case manager|case worker|caseworker|care manager|care coordinator|navigator|geriatric care",
 ('G','Caregiver coach / caregiver training class'):r"caregiver (coach|training|class|course|education)|savvy caregiver|powerful tools|care ?coach",
 ('G','Respite grant / voucher / stipend / paid family caregiver pay'):r"respite (grant|voucher|fund)|caregiver stipend|stipend|voucher|paid (family )?caregiver|get paid to|compensat\w+ (for )?caregiv",
 ('G','Family or friend stepping in (relatives, siblings, neighbors)'):r"my (sister|brother|sibling|aunt|cousin|neighbor|friend)s?\b.{0,40}(took|watch|stay|come|help|cover|relief|sit|stepped)",
 ('G','Short-stay / facility respite (nursing home, assisted living, memory care stay)'):r"respite (stay|care) (at|in)|short[- ]stay|temporary (stay|placement)|memory care.{0,20}(respite|stay)|trial stay",
 ('G','Hotline / helpline (any)'):r"hot ?line|help ?line|crisis line|\b988\b|warm ?line",
 ('G','Online forum / message board (other)'):r"message board|online forum|\bforums?\b|online communit|chat room|zoom (support|group|meeting)",
 ('G','Hospital / health-system caregiver program'):r"hospital.{0,30}caregiver (support|program|group)|caregiver (support|resource) (program|center|group).{0,20}(hospital|clinic|health system)|palliative care (team|social)",
 ('G','Bereavement / grief group'):r"grief (group|support|counsel)|bereavement",
}
rx={k:re.compile(v,re.I if k[1] not in('SHIP counselor','PACE','NAMI','IHSS (California)') else 0) for k,v in T.items()}
res={}
for k,r in rx.items():
    ids=[i for i in rel if r.search(P[i]['text'])]
    ids_sg=[i for i in ids if i in sg]
    res[k]=(ids,ids_sg)
if __name__=='__main__':
    rows=sorted(res.items(),key=lambda x:-len(x[1][0]))
    for k,(a,b) in rows: print(f"{len(a):4d} {len(b):4d} {k[0]} {k[1]}")
    json.dump({f"{k[0]}|{k[1]}":v[0] for k,v in res.items()},open('partb_hits.json','w'))
