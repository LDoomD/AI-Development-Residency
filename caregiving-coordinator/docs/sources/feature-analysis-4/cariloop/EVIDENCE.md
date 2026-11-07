# Cariloop: evidence for 9 feature cells (2026-11-06)

Key rule: Cariloop sells to employers. Every YES below is LIMITED to people whose employer (or insurer) pays. I found no page where a family can buy it directly. Paths below are under `docs/sources/` unless they start with `feature-analysis-4/`.

Where an ordinary family can get it: Cariloop's own FAQ says a person who leaves an employer gets 30 days to move to an individual membership "that they can cover the cost of on their own." MSU shows one price: $249 a month to keep coaching after the 30 free days. The old cariloop.com/individuals page now opens an employer sales page. Also, only employers with 50 to 100+ workers are signed (FAQ).

| Cell | Verdict | File | Quote (max 20 words) | Why |
|---|---|---|---|---|
| F1 Relief finder | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_solutions_caregiver_support_platform_find_care.txt | "Employees receive a curated set of vetted care choices, complete with reviews, availability, and real-time rates" | Finds vetted care for employees. Respite and adult day are never named; "in-home companion" backup care is named on the elder care page. |
| F1 (backup care) | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_solutions_elder_care_benefits.txt | "employees can access trusted, vetted care options" | Backup care for elder care plans that fall through; the employer buys it. |
| F2 Eligibility and applications | VERIFY | competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt | "Understanding a loved one’s Medicare, Medicaid, or VA benefits" | Coaches explain benefits. No page says they check eligibility or file applications. |
| F3 Paying for relief | LIMITED (employer only) | competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt | "Understanding how to pay for a loved one’s care" | Coaches explain how to pay. Real-time rates are shown for providers. |
| F3 (cost to the family) | LIMITED | feature-analysis-4/cariloop/hr_msu_edu_cariloop_faqs_full_2026-11-06.txt | "the caregiving services themselves are not free of charge and are paid directly by the user" | The coaching is free to employees; the care itself is paid by the family. |
| F4 Refusing parent support | VERIFY | competitors/cariloop/www_cariloop_com_about_us_faqs.txt | "our Care Coaches will be there to support you with everything from conversation starters to expectation management" | Coaches help plan hard talks about a parent's safety. No page names a parent who says no. |
| F5 Relatives cover time | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_solutions_caregiver_support_platform_toolkit.txt | "Friends and family can view and update info, take on tasks, and stay in sync." | Care Team members can take tasks. Nothing shows a way to assign a task or confirm it was done. |
| F5 (alerts) | LIMITED | competitors/cariloop/www_cariloop_com_about_us_faqs.txt | "every individual who has been invited onto the Care Team will be notified" | Everyone on the Care Team gets a note when the case changes. |
| F6 Account access | VERIFY | competitors/cariloop/www_cariloop_com_about_us_faqs.txt | "Our portal is best suited for organizing and storing important documents rather than transferring them." | It stores POAs and papers. No page says it helps a caregiver get into a parent's bank or insurance login. |
| F8 Personal guidance | LIMITED (employer only) | feature-analysis-4/cariloop/hr_msu_edu_cariloop_faqs_full_2026-11-06.txt | "employees have the option to extend the coaching for $249/month." | At MSU the coach is free for 30 days a year, then $249 a month. |
| F8 (ongoing) | LIMITED | competitors/cariloop/www_cariloop_com_about_us_faqs.txt | "So long as you are a Cariloop member, your dedicated Care Coach will be there for you" | Coaching is ongoing while membership lasts. Membership is tied to the employer benefit. |
| F8 (leaving a job) | LIMITED | competitors/cariloop/www_cariloop_com_about_us_faqs.txt | "allows the member to shift to an individual membership that they can cover the cost of on their own" | The only path for a person on their own, and only after leaving an employer. Price not on Cariloop's site. |
| F9 Behavior help | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_blog_guide_care_coaching_team_experience_and_expertise.txt | "Supporting caregivers with new or worsening symptoms of dementia in a loved one" | Certified Dementia Practitioner coaches handle dementia symptoms. Coaching, not a self-serve guide. |
| F9 Hard-talk help | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_blog_guide_care_coaching_team_experience_and_expertise.txt | "Navigating difficult conversations with a loved one" | Social-worker coaches list hard talks as a service. |
| F10 People who understand | LIMITED (employer only) | feature-analysis-4/cariloop/cariloop_com_solutions_caregiver_support_platform_toolkit.txt | "A supportive space to ask questions and connect." | "Community Channels" are in-app discussion spaces where coaches answer. Not a support group meeting. |
| F10 (MSU wording) | LIMITED | feature-analysis-4/cariloop/hr_msu_edu_cariloop_faqs_full_2026-11-06.txt | "community channels to connect with like-minded individuals" | MSU says employees get them as a free tool. |

## What "supportive community" really is
Cariloop's "Community Channels" are discussion channels inside the app, with coaches answering. The Terms of Service also mention posting "to a community channel" (feature-analysis-4/cariloop/cariloop_com_terms_of_service.txt). No page shows peer-run groups, group sizes, or meetings. Size and activity: not found.

## Real-user reports
- Google Play (saved 2026-11-04, 9 ratings, 4.6 stars): one review says the app will not let the user exit; one praises the staff. Old Apple listing has 23 ratings (docs/sources/app-stores/apple-named/Cariloop.json).
- Reddit r/AskHR (employer side): "We use Cariloop at my employer and the feedback has been fantastic." File: feature-analysis-4/cariloop/reddit_askhr_sichx0_cariloop_2026-11-06.txt. Local Reddit archive (posts.jsonl, 49,315 posts) has 0 Cariloop mentions.
- BBB: A+ rating, 0 complaints, 0 reviews (competitors-4/review-sites/bbb_2026-11-04.txt). Trustpilot is blocked by robots.txt.

## Differs from Figma
- Figma 4b: "Members who leave the job get 30 days to switch to a paid individual plan." Matches. Price for individuals is not on Cariloop's site; $249 is MSU's price.
- Figma 4c "Partly: relatives join the Care Team and get updates. Tasks aren't split." New: the toolkit page says Care Team members can "take on tasks." Nothing shows assigning or confirming, so F5 stays LIMITED, not NO.
- Figma says "Only if the employer offers it" for relief and "Yes" for money. I changed money (F2) to VERIFY: coaches explain Medicare, Medicaid and VA benefits; none of the pages say they help file applications.
- Figma F4 "Nothing for a parent who refuses" is not backed by a page that says so. Pages show hard-talk coaching only. VERIFY.
- New: Cariloop pages say coaches can find providers and "assistance with finance and legal matters" (FAQ). They do not mention bank or insurer logins (F6).
- Trustmark gives its insured customers only "1 month of coaching per calendar year" (feature-analysis-4/cariloop/trustmarkbenefits_com_cariloop.txt). A second employer-type limit.

## Not saved or blocked
- Trustpilot, Apple App Store review pages: Trustpilot disallows all crawlers; Apple reviews not re-pulled. Cariloop's own robots.txt only blocks pages with "?" and /es, /fr, /member_resources; none were fetched.
- SMU's Cariloop page returned 404. MSU's FAQ needed Firecrawl (the plain download hit a bot check).
