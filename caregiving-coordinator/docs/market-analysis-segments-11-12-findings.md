# Findings: how caregivers get relief, and what stops them (segments 11 and 12, 2026-11-04)

Draft for the owner's review. The market analysis is not changed until the owner approves.

## What was read

- 1,086 items read in full by 11 readers following `docs/sources/market-analysis-3/segments-11-12/READING-INSTRUCTIONS.md`:
  - 632 saved Reddit posts that mention respite or adult day (all of them)
  - 115 posts found only by the named-program search (VA, Medicaid waivers, hospice respite, Area Agencies on Aging and the 10 offerings)
  - a random 150 that mention only a support group, and 150 only a therapist
  - 39 saved AgingCare and ALZConnected threads
- **831 were from family caregivers writing about relief** (the rest were ads, paid workers, researchers, or a therapist for the person being cared for).
- **Checks:** `verify_codes.py` confirmed every item was coded exactly once and every quote matches its post word for word (0 problems). `count_results.py` produced every number below, and `results.json` lists the post ids behind each one.

## 1. How many caregivers need a break and have none

**214 of 831 (26%)** say they need a break or relief and have no help in place.

## 2. What caregivers use, and how it goes

Posts can name more than one kind of help.

| Kind of help | Posts | Used it | Tried and stopped | Wanted it, couldn't get it | Looking or considering |
|---|---|---|---|---|---|
| Respite, all types combined | 341 | 128 | 18 | 78 | 81 |
| Paid aide or companion | 185 | 84 | 7 | 34 | 56 |
| Family or friend stepping in | 160 | 85 | 4 | 39 | 28 |
| Therapist or counselor for the caregiver | 139 | 82 | 12 | 11 | 29 |
| Support group | 114 | 49 | 4 | 6 | 43 |
| Adult day program | 101 | 38 | 6 | 17 | 33 |
| Hospice respite | 40 | 20 | 2 | 10 | 6 |
| Apps or online tools | About 30 | Mostly online communities (Reddit, Facebook groups, ALZConnected, WhatsApp, a Discord server). Therapist finders: SonderMind, Zencare, Psychology Today. No meditation or burnout app. | | | |

Respite types (in-home, facility, type not said) are combined because readers handled "respite" with no type differently.

## 3. What stops them (tests AARP's reasons in caregivers' own words)

Posts that name each barrier, out of 831:

| Barrier | Posts | In AARP's list of reasons? |
|---|---|---|
| Cost | 118 | No (new) |
| The parent refuses | 96 | No (new) |
| Family or friends won't help | 93 | No (new) |
| Hard applications or eligibility rules (VA, Medicaid waivers) | 86 | Yes |
| Too few hours, minimum stays and other rigid rules | 59 | Yes ("inflexible program design") |
| Waitlists or no openings | 59 | Yes ("lack of trained providers," partly) |
| Worry about quality or safety | 52 | Yes |
| Guilt or shame about handing off care | 38 | Yes |
| No trained or reliable providers | 38 | Yes |
| Therapy doesn't help or isn't available | 27 | No |
| Support group doesn't fit (Alzheimer's-only, older spouses) | 19 | No |
| Transport or logistics | 16 | No |
| Doesn't trust strangers with the parent | 14 | Yes ("lack of trust") |
| Agencies, social workers or helplines pass people along | 14 | No |
| No time or energy to arrange it | 12 | No |
| Didn't know it existed | 10 | No |

**What this shows:**
- AARP's reasons all appear, but **the three biggest barriers aren't in its list**: cost, the parent refusing, and family not helping.
- **Adult day programs:** cost (24) and the parent refusing (23) are the top barriers.
- **Respite:** cost (59), the parent refusing (46) and family not helping (36) lead.

## 4. Who provides and pays (as caregivers name them)

- **Providers named most:** the VA (28), hospice (20), Area Agencies on Aging (10), Medicaid and Medicaid waivers (about 16), the Alzheimer's Association (6). Wellthy and Teepa Snow come up twice each. No other company comes up more than twice.
- **Costs and payers, as caregivers wrote them (examples from 153 posts):**
  - "more than $2,000 for a 2 week minimum" (facility respite)
  - "$1600 a month for 40 hours a week"
  - "Medicare pays for 2 five-day stays per year" (hospice respite)
  - "Medicaid waiver pays for 15 hours a week"
  - "out of pocket; her insurance won't pay"
  - All 153 are listed in `results.json` under `payer_cost`, each with its post link.

## 5. What helps when they get it

Caregivers who got a break describe sleep, time alone, a date with a spouse, seeing friends, and "relaxed for the first time in months." Support groups and online communities most often help them "feel less alone." For example:
- "I had almost a full week to be 28 again. I got to go on a date with my husband, spend time with my dogs, and relax for the first time in months." ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/14seksz/))
- "I wish we could afford respite care but we're barely scraping by as is" ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/1179uxg/))
- "there's currently a wait list for the waitlist in our county." ([r/CaregiverSupport](https://www.reddit.com/r/CaregiverSupport/comments/11awqmt/))

## 6. Proposed verdicts for the market analysis (for the owner to decide)

- **Segment 11, respite and adult day:** a real unmet need, and **the gap is access, not supply**. Help exists (respite, adult day, VA, Medicaid waivers, hospice respite), but cost, eligibility rules, waitlists and rigid hours block it. The parent refusing and family not helping block it too. This confirms AARP's 39% (would help) vs 13% (use it), and adds three bigger barriers AARP doesn't list.
- **Segment 12, burnout support:** the need is large, but **"crowded" is wrong for caregivers**. Burnout and meditation apps are crowded in general, yet caregivers almost never use them. What they use is therapy (often helpful, sometimes unaffordable or not caregiver-aware), support groups (when one fits) and online peer communities.

## Limits

- Reddit and forum writers are not a random sample of all caregivers, and they lean toward people having a hard time.
- Counts are posts that mention something, not how many caregivers face it nationally.
- Readers made some judgment calls, listed in their reports: borderline caregivers (parents of disabled children, siblings) counted as relevant, and "respite" with no type handled differently. That's why respite is reported combined.
- "Other" barriers were grouped by keyword rules written in `count_results.py`. 129 one-off barriers stay ungrouped.
- Each quote shows a post's main point, not always the barrier it's counted under. Use the ids in `results.json` to read the post behind any count.
