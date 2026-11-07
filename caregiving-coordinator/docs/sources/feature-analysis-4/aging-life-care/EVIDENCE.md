# Geriatric care managers (Aging Life Care): evidence for 7 feature cells (2026-11-06)

Blocked: aginglifecare.org robots.txt asks crawlers not to copy it, so I did not scrape it. The one page already saved by hand (competitors-4/manual-saves/aginglifecare_org_home.txt) is used only for the definition. Not fetchable: dalyperri.com and agewisecolorado.org (HTTP 403), alzheimersla.org (no DNS). Care managers are many local firms, not one product, so every YES means "firms like these offer it, for a fee." Solace sells a rival service (it says so on its page); treat its claims as marketing.

Paths are under `docs/sources/` unless they start with `feature-analysis-4/`.

| Cell | Verdict | File | Quote (max 20 words) | Why |
|---|---|---|---|---|
| F2 Eligibility and applications | VERIFY | competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt | "Identifying social services and programs that could help the care recipient." | They find programs and coach families through insurance. No source says they file applications. |
| F2 (insurance) | VERIFY | feature-analysis-4/aging-life-care/retirementlivingsourcebook_com_videos_caring_from_afar_aging_life_care_managers_on_long_di.txt | "Care managers are used to reviewing these policies and can coach families through activating them" | About long-term care insurance. Applying for Medicaid or VA is not described. |
| F3 Paying for relief | YES (for a fee) | competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt | "Professionals charge by the hour, ranging from $150 to $300, depending on the geographic region." | AARP gives the price of the service and says Medicare and Medicaid usually do not pay for it. |
| F3 (what care costs) | YES | feature-analysis-4/aging-life-care/solace_health_articles_geriatric_care_manager.txt | "They also know how to assess what level of care your loved one can afford" | Care managers match care to the family budget and point to Medicaid or VA help. |
| F4 Refusing parent support | YES | feature-analysis-4/aging-life-care/solace_health_articles_geriatric_care_manager.txt | "Your parent might refuse help, become verbally aggressive, or forget entire conversations you just had." | Solace says a care manager "can often get through to someone who won't listen to family members." That is a marketing claim; I found no study. |
| F4 (advice) | YES | feature-analysis-4/aging-life-care/retirementlivingsourcebook_com_videos_caring_from_afar_aging_life_care_managers_on_long_di.txt | "a loved one with dementia denies it and refuses help" | At a talk, an Aging Life Care speaker told a caregiver with a refusing parent to book free consults with care managers. |
| F5 Relatives cover time | YES (people, not a tool) | feature-analysis-4/aging-life-care/solace_health_articles_geriatric_care_manager.txt | "They provide regular updates, coordinate family meetings, and help everyone stay informed" | Care managers run family meetings and send reports. A speaker also uses a "Share the Care" approach to give distant siblings roles. |
| F5 (counter-example) | note | feature-analysis-4/aging-life-care/reddit_posts_mentioning_care_manager_2026-11-06.txt | "I hired a Geriatric Care Manager. He lost his mind on me." | One Reddit caregiver's brother refused the care manager's calls. A care manager cannot make a relative join in. |
| F6 Account access | VERIFY | feature-analysis-4/aging-life-care/privatehomecare_com_blog_what_is_a_geriatric_care_manager_and_how_can_they_help_me_and_my_.txt | "Some Care Managers can be the Power of Attorney for individuals who do not have family or friends" | Care managers send families to lawyers and some act as POA for people without family. No source says they help a caregiver get into a parent's bank or insurer login. |
| F9 Behavior help | YES | feature-analysis-4/aging-life-care/solace_health_articles_geriatric_care_manager.txt | "A geriatric care manager brings professional experience handling these behaviors" | Dementia behavior handling is listed as a core service. AARP shows a dementia care manager who sends trained staff on outings twice a week. |
| F9 Hard-talk help | YES | competitors-4/aging-life-care/www_aarp_org_caregiving_basics_geriatric_care_manager.txt | "Explaining complex or difficult topics to care recipients and their families." | AARP lists it as a service. |
| F10 People who understand | VERIFY | feature-analysis-4/aging-life-care/retirementlivingsourcebook_com_videos_caring_from_afar_aging_life_care_managers_on_long_di.txt | "Ask them about local dementia caregiver support groups, too." | Advice to ask. No firm says it runs or connects people to groups as part of its service. |

## Real-user reports (saved Reddit archive; 60 posts mention care managers)
- "We are now working with a Geriatric Caregiver, but it just feels like more paperwork than help." (r/CaregiverSupport, p1x4gtt9, in feature-analysis-4/aging-life-care/reddit_posts_mentioning_care_manager_2026-11-06.txt)
- "I hired a care manager to help her with dr appts" (r/AgingParents, p1kxe3qv). Shows the relief and place-finding side.
- AARP Alzheimer's-family story: $650 to $900 a month for care management (AARP file above).

## Differs from Figma
- Figma 4c F4 "Partly: talk with the parent directly. Some parents still refuse them." I found sources saying care managers handle refusal, but none says they fail. The "some still refuse" part has no source in these files. F4 is YES on claims; keep the caution.
- Figma F5 "Partly: stand up to difficult relatives. Family fights often follow." Matches the Reddit story and Solace's wording. I mark YES (people, not a tool) with the counter-example.
- Figma F6 "One took power of attorney without telling the family" is not in the files I read. Still VERIFY. I did not find that story again.
- Figma said "arrange respite" under relief. AARP confirms: "Arranging for relief or respite care for stressed-out caregivers." (F1 not assigned; matches.)

## Files
All under feature-analysis-4/aging-life-care/: Reddit extract, AgingCare long-distance article, Solace, Private Home Care, Retirement Living Source Book, CarePatrol article. AgingCare page held no care-manager detail useful for these cells (not cited).
