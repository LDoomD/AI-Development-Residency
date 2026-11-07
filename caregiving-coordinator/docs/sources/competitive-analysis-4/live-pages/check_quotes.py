import re,sys,os
os.chdir(sys.argv[1])
Q=[
("1","ny-nysofa-26-tam-01-caregiver-directed-respite.txt","Family members may be hired as respite providers under both the Voucher Model and the FI Model."),
("1b","ny-nysofa-26-tam-01-caregiver-directed-respite.txt","Cannot be the primary caregiver"),
("1c","ny-nysofa-26-tam-01-caregiver-directed-respite.txt","NYSOFA allows AAAs to implement a caregiver-directed respite care service delivery model"),
("2","il-money-management-program.txt","The program matches trained volunteers with older persons who need help with tasks such as organizing, reviewing, and paying bills"),
("2b","il-money-management-program.txt","assists low-income older persons who have difficulty managing their personal household budgets, paying bills"),
("2c","il-money-management-program.txt","available to Community Care Program (CCP) participants and individuals who have a substantiated Adult Protective Services (APS) case"),
("3","ma-money-management-program.txt","Support may include help creating budgets and paying bills on time"),
("3b","ma-money-management-program.txt","run by program staff and volunteers who assist older adults who are having difficulty managing their personal finances"),
("3c","ma-money-management-program.txt","free program for income eligible individuals aged 60 and older"),
("4","va-veteran-directed-care.txt","hiring workers (which might include their own family member or neighbor)"),
("4b","va-veteran-directed-care.txt","meet the clinical criteria for the service, and it is available. Services may vary by location."),
("5","arch-how-do-i-get-paid-to-be-a-family-caregiver.txt","including payment to the family caregiver or to pay for respite"),
("5b","arch-how-do-i-get-paid-to-be-a-family-caregiver.txt","resources are limited, may not exist in your state at all, and eligibility is restrictive"),
("5c","arch-how-do-i-get-paid-to-be-a-family-caregiver.txt","The following states allow relatives as paid foster care providers: Connecticut, Louisiana, Indiana, Massachusetts, Ohio, Rhode Island, and Texas."),
("5d","arch-how-do-i-get-paid-to-be-a-family-caregiver.txt","some states may require you to become a certified Medicaid provider or meet other state requirements"),
]
def n(s): 
    s=s.replace('’',"'").replace('“','"').replace('”','"').replace('—','-').replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip()
bad=0
for i,f,q in Q:
    txt=n(open(f,encoding='utf-8').read()); ok=n(q) in txt; wc=len(q.split())
    print(f"{i:3} words={wc:2} {'MATCH' if ok else 'NO MATCH'} <- {f}")
    if (not ok) or wc>20: bad+=1
print("rows failing:",bad)
