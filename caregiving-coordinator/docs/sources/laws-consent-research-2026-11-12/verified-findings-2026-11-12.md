# Laws, consent and security: checked findings (2026-11-12)

From research run `wf_328460b2-5ee` (`research-run-result.txt`). Each source was saved in `sources/`, dated, and logged in `docs/sources/INDEX.md`. Each rule was searched for 2025 to 2026 changes.

**This is not legal advice, and it never says "compliant."** Each row says what a rule covers and where a lawyer is needed.

Tags: **Fact** = checked against the saved source text. **May be out of date** = a change was found, or the source is old.

| Rule | Might it apply to us? | What it requires | Source (saved file) | Status | Lawyer needed? |
|---|---|---|---|---|---|
| HIPAA | Probably not. HHS says an app that serves consumers directly is "not likely" covered. It depends on the facts, and a deal with a doctor, hospital or health plan could change it. | Nothing directly, unless we work for a doctor, hospital or health plan. | 01 (2016), 02 (reviewed Apr 22, 2026) | Fact. The scenarios are from 2016 but still posted. | Yes, to confirm we're not covered. |
| FTC Act, Section 5 | Yes. It covers health data that HIPAA doesn't. | Don't deceive users or treat them unfairly about how their health data is used or shared. | 06 (Aug 2024) | Fact. GoodRx, BetterHelp and Flo cases left out because the run didn't fetch them. | Yes, on privacy promises. |
| FTC Health Breach Notification Rule (2024) | Maybe. It covers "personal health record" apps that pull data from more than one source. Caregivers and relatives all add data, so we might count. | Sharing health data without permission counts as a breach. Tell each person within 60 days, and tell the FTC too if 500 or more people are affected. | 23 (eCFR, current Nov 9, 2026), 04, 05, 24 | Fact. Still in force. On Sep 9, 2026 the FTC withdrew only its 2021 policy statement, saying the 2024 rule now covers health apps. | Yes, on whether we're a "personal health record" app. |
| Washington My Health My Data Act | Yes, if we have users in Washington. No size limit. | Opt-in consent to collect health data. A separate consent to share it. Rights belong to the person the data is about. | 07 (RCW 19.373) | Fact. No changes since 2023 found. | Yes, on whose consent counts when a caregiver enters a parent's data. |
| Nevada health data law (SB 370) | Yes, if we have users in Nevada. | Opt-in consent to collect. A separate consent to share, from "the consumer to whom the consumer health data relates." | 08 (NRS 603A.400 to .550), 11 | Fact. The health sections had no 2025 changes. | Yes, same consent question. |
| Connecticut Data Privacy Act | Yes, since July 1, 2026, for any business that handles sensitive data (health data counts), no matter its size. | Consent before handling sensitive data. Reasonable data security. | 25 (Public Act 25-113), 09 | **May be out of date:** the run used the AG page, which doesn't mention the 2025 amendment. Row updated from the Act itself. | Yes. |
| California CCPA and new 2026 rules | Maybe. The CCPA applies only to businesses above a size limit (not checked here). | Since Jan 1, 2026: a risk assessment before handling sensitive data, such as health data. | 26, 27, 10 | Fact for the 2026 rules. The size limit and the CMIA medical privacy law weren't checked. | Yes. |
| HIPAA "personal representative" | Only if HIPAA applies (see first row). | A health care power of attorney or court guardian has the same rights to records as the patient. | 13 (reviewed Jan 5, 2024), 14 (reviewed Dec 28, 2022) | Fact. These are HIPAA rules for doctors' records, not app consent. | Yes, on whether a power of attorney counts as consent under the WA and NV laws. |
| Supabase (database) | Only if we need a HIPAA-level setup. | It encrypts data at rest and in transit. We must turn on row-level security. A BAA needs the Team plan plus a HIPAA add-on. | 17 (Oct 6, 2026), 18 (Oct 30, 2026) | Fact. | No, it's a vendor fact. |
| Vercel (hosting) | Only if we need a HIPAA-level setup. | It signs BAAs on the Pro plan (with a HIPAA add-on) or the Enterprise plan. | 20 (Nov 3, 2025), 19 (Sep 8, 2026) | Fact. | No, it's a vendor fact. |

## Gaps that are still open
- Whose consent counts when a caregiver enters a parent's or partner's data, and whether a power of attorney is enough. No source answers it. A lawyer is needed.
- California: the CCPA size limit and the CMIA medical privacy law weren't checked.
- The FTC's GoodRx, BetterHelp and Flo cases weren't fetched, so they are left out.
- Data region for Vercel and Supabase wasn't checked.

---

## 2. Law-database answers (added 2026-11-12, later the same day)

From the pass in `docs/research-checklist-laws-database-2026-11-12.md`. Files 28 to 73 are in `sources/` and logged in `docs/sources/INDEX.md`. 27 key quotes were checked word for word. All rows are **Fact** (what the law or vendor says), not legal advice.

| Question | What the law says | Source (file, section) | What's still unclear |
|---|---|---|---|
| 1. Whose consent counts (WA, NV, CT)? | **The person the data is about,** not the caregiver who types it in. WA: "consent from the consumer." NV: consent "of the consumer to whom the consumer health data relates." CT: "the consumer's consent." | 07 (RCW 19.373.010(7), .030); 08 (NRS 603A.425, .500); 25 (PA 25-113 §9) | Nevada's "consumer" is someone "who has requested a product or service." A parent who never signs up may not count. |
| 1b. Can someone consent for them? | **WA and NV: no clause at all** (no agent, guardian or power of attorney). **CT: only a guardian or conservator,** plus an agent for opt-outs only. | 07, 08, 25 (42-518(b)), 33 (42-519) | Whether a family member can consent for a parent or partner is not covered by any of the 3 laws. |
| 2. Does a power of attorney count? | **WA:** a health care power of attorney makes the agent the HIPAA personal representative "for all purposes" and lets them give informed consent to health care. **NV:** the health care form lets the agent "obtain, examine and share" health information, but only when the parent can't decide for themselves (unless initialed). **CT:** the power of attorney act excludes health care decisions. A health care representative makes "any and all health care decisions." | 28 (RCW 11.125.400, .240); 30 (NRS 162A.855, .870); 31 (CGS 1-350b); 32 (CGS 19a-575a) | None of the power of attorney laws mentions consumer privacy laws or apps. |
| 2b. Spouses (Audience 2) | WA: a spouse is 3rd in line to consent to health care, after a guardian and a health care agent. CT: a spouse is 1st in the "next of kin" order. Neither law gives a spouse power over an app's data. | 29 (RCW 7.70.065); 32 (CGS 19a-570(10)) | Same gap as 1b. |
| 3. Are we a "personal health record" app (FTC)? | **Not while the only source is people typing.** The FTC says an app "is not a personal health record... if the consumer is its only source of information." **Any feature that pulls data in changes this,** even a calendar connection, and even if no one uses it. | 39 (89 FR 47035 to 47038); 04 | Whether several relatives typing in counts as "multiple sources." The FTC doesn't say. |
| 3b. FTC cases | GoodRx and Premom (2023) under the breach rule; BetterHelp (2023) and Flo (2021) under the FTC Act. All shared health data with ad or analytics companies without permission. No breach rule cases from 2024 to 2026 found. | 40 to 43, 39 (p. 47029) | |
| 4. California privacy law (CCPA) | **Doesn't reach a small startup:** it applies only above $26,625,000 in revenue, 100,000 people, or 50% of revenue from selling data. | 51 (Civ. Code 1798.140(d)); 52 | Recheck when we grow. |
| 4b. California medical privacy law (CMIA) | **May apply.** An app "designed to maintain medical information" for a person to manage it "shall be deemed to be a provider of health care." | 48 (Civ. Code 56.06(b)) | "Medical information" means information from a doctor, plan or similar (56.05(j)). Whether caregiver-typed notes count is unclear. **Lawyer.** |
| 5. Where the data lives | **Supabase:** one region, picked at setup. US regions exist (us-east-1 and others), and "all data will remain within the chosen region." Changing region later means a new project. **Vercel:** functions run in Washington, D.C. (iad1) by default, and the region can be set. | 56, 59, 60, 62 | Vercel log and build storage region not stated. |
| 5b. Backups and cost | Supabase Free: no automatic backups. Pro ($25/mo): 7 days. Team ($599/mo): 14 days, and needed for its HIPAA agreement. Vercel's HIPAA add-on: $350/mo on Pro. | 57, 58, 63 | |
| Cases under the state laws | 6 Washington lawsuits (2025 to 2026): Amazon's ad SDK, cannabis sites, telehealth, a fertility clinic and a med spa. All are about **sharing with ad trackers without consent**. None reached a ruling. CT's attorney general found one telehealth company's consent step "insufficient" and is investigating a fertility tracker app. Nevada: none found. | 64 to 72 | No case or action covers a caregiver entering another person's data. |

### What this means for the "lawyer needed" list (Proposed)
- **Answered by the law text:** California's CCPA (doesn't apply now), the FTC breach rule (doesn't apply while data is only typed in), data region (US available), and whose consent counts (the person the data is about).
- **Still needs a lawyer:**
  1. How a caregiver can lawfully enter a parent's or partner's health data when WA and NV give no one else the right to consent.
  2. Whether California's medical privacy law (CMIA) reaches caregiver-typed notes.
- **Design facts for the build plan (Proposed):** no ad or analytics trackers on health pages (every lawsuit is about this). No data-pulling features in MVP #1 (this keeps us outside the FTC breach rule). Supabase US region. Separate consent screens for collecting and for sharing.
