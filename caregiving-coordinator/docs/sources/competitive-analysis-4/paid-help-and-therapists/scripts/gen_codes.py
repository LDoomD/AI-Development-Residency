# Manual decisions from reading lines_paid.txt (185) and lines_ther.txt (139). Line number -> code.
# paid types: AG agency/care company, PV aide paid by family (private or unspecified), PR program-paid aide (VA, Medicaid waiver, AAA, hospice, county),
#             RW respite worker/sitter, NO not paid in-home help (facility, day program, therapy, friends) or survey-bait
# outcomes: W worked, N did not work, M mixed, X no outcome stated / only wanted or asked
PAID={
1:'PV X',2:'PV M',3:'PV M',4:'PV W',5:'PR W',6:'PV X',7:'PR M',8:'PV W',9:'PV X',10:'RW M',
11:'RW M',12:'RW M',13:'PV X',14:'PR N',15:'RW X',16:'RW M',17:'PR X',18:'PV X',19:'AG X',20:'NO X',
21:'PR X',22:'PR X',23:'PV W',24:'PV M',25:'PV X',26:'AG N',27:'AG M',28:'NO X',29:'PV X',30:'PV X',
31:'PV X',32:'AG X',33:'PR X',34:'NO X',35:'PR M',36:'PR W',37:'PR M',38:'AG N',39:'PR X',40:'PR M',
41:'PR M',42:'PV W',43:'PV X',44:'PR X',45:'NO X',46:'PV X',47:'PV N',48:'PR M',49:'PV N',50:'NO X',
51:'NO X',52:'PV X',53:'PR M',54:'PV X',55:'PV X',56:'PV W',57:'PV X',58:'NO X',59:'PV X',60:'NO X',
61:'AG N',62:'PV X',63:'PV M',64:'PV W',65:'NO X',66:'NO X',67:'PV M',68:'NO X',69:'NO X',70:'PR M',
71:'AG M',72:'NO X',73:'AG N',74:'PR X',75:'PV X',76:'PR X',77:'PV W',78:'NO X',79:'NO X',80:'NO X',
81:'PR N',82:'PV X',83:'PV X',84:'NO X',85:'AG N',86:'PV M',87:'PR X',88:'PV X',89:'NO X',90:'PR N',
91:'PR X',92:'PV X',93:'PV M',94:'PR N',95:'PV M',96:'PR X',97:'PR W',98:'PV X',99:'NO X',100:'PV X',
101:'PV W',102:'NO X',103:'PV X',104:'PV X',105:'PV M',106:'PV X',107:'PV N',108:'AG X',109:'PV W',110:'PV X',
111:'PV X',112:'PV X',113:'PV X',114:'AG X',115:'PV X',116:'PV N',117:'PV X',118:'PV X',119:'PR X',120:'PR N',
121:'NO X',122:'AG N',123:'AG X',124:'PV X',125:'NO X',126:'AG X',127:'AG M',128:'PV W',129:'NO X',130:'PV X',
131:'PV X',132:'PR M',133:'NO X',134:'RW N',135:'PV M',136:'NO X',137:'PV X',138:'AG N',139:'PR N',140:'AG M',
141:'PR W',142:'PV X',143:'PV X',144:'DUP',145:'DUP',146:'PR M',147:'DUP',148:'PR X',149:'PV X',150:'PV X',
151:'PV M',152:'PR X',153:'PV X',154:'PR W',155:'PV M',156:'PR M',157:'PR X',158:'PV M',159:'PR X',160:'PV M',
161:'PV M',162:'PR W',163:'PV X',164:'PV X',165:'PV N',166:'PV X',167:'PV M',168:'NO X',169:'PR N',170:'NO X',
171:'PV X',172:'AG W',173:'PV M',174:'PV W',175:'NO X',176:'PR M',177:'PR N',178:'NO X',179:'NO X',180:'PV X',
181:'PV X',182:'NO X',183:'PV X',184:'AG M',185:'PV W'}
# special: 41 dup of 40? lines 40 (p18y0ljz) and 41 (p18y0ng6) same text posted twice -> 40 is DUP
PAID[40]='DUP'
# 50,51 survey-bait -> NO
# therapy: type TH (therapist or counselor for the writer), TC (couples or family counseling), NO (not therapy for the writer)
THER={
1:'NO X',2:'TH N',3:'TH W',4:'TH W',5:'TH X',6:'TH X',7:'TH X',8:'TH M',9:'TH W',10:'TH W',
11:'TH X',12:'TH M',13:'TH X',14:'TH W',15:'TH X',16:'TH X',17:'TH N',18:'TH N',19:'TH X',20:'TH W',
21:'TH X',22:'TH X',23:'TH W',24:'TH M',25:'TH X',26:'TH X',27:'TH X',28:'TH N',29:'TH N',30:'TH X',
31:'TH N',32:'TH X',33:'TH W',34:'TH N',35:'TH X',36:'TH W',37:'TH X',38:'TH X',39:'TC N',40:'TH X',
41:'TH X',42:'TH X',43:'TH X',44:'NO X',45:'TH X',46:'TC X',47:'TH X',48:'NO X',49:'TH X',50:'TH W',
51:'TH N',52:'TH X',53:'TH W',54:'TH X',55:'TH X',56:'TH X',57:'TH X',58:'TH X',59:'TH X',60:'TH M',
61:'TH W',62:'TH N',63:'TH M',64:'TH W',65:'TH X',66:'TH X',67:'NO X',68:'TH W',69:'TH W',70:'TH W',
71:'NO X',72:'TH X',73:'TH X',74:'TH N',75:'TH X',76:'TH X',77:'TH X',78:'TH X',79:'TH X',80:'TH X',
81:'TH W',82:'TH X',83:'NO X',84:'TH X',85:'TH X',86:'TC X',87:'TH X',88:'TH X',89:'TH X',90:'TC X',
91:'TH N',92:'TH W',93:'NO X',94:'TH X',95:'TH X',96:'TC W',97:'TH W',98:'TH X',99:'TH X',100:'TH X',
101:'TH N',102:'TH X',103:'TH X',104:'TH M',105:'TH W',106:'TH W',107:'TH N',108:'TH X',109:'TH X',110:'TH X',
111:'TH X',112:'TH M',113:'TH W',114:'TH X',115:'NO X',116:'TH N',117:'TH N',118:'NO X',119:'TH X',120:'TH W',
121:'TH M',122:'TH W',123:'TH X',124:'TH W',125:'TC N',126:'NO X',127:'TH N',128:'TH X',129:'TH M',130:'TH W',
131:'TH N',132:'TH M',133:'TH X',134:'TH X',135:'TH W',136:'TH N',137:'TH N',138:'TH X',139:'TH N'}
