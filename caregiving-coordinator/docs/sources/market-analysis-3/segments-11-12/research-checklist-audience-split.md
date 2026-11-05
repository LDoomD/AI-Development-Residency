# Research checklist: split the relief findings by audience (2026-11-04)

Filled in from `docs/research-checklist.md` before any work starts.

## 1. What this task is for

- **Task:** label each of the 831 relief posts by who the writer cares for, then re-count every finding for Audience 1 and Audience 2.
- **Updates:** the market analysis update for segments 11 and 12, and `docs/market-analysis-segments-11-12-findings.md`.
- **Later deliverables it changes:**
  - the audience additions (exhaustion, what blocks relief), split by audience
  - the competitive analysis (which audience each gap hits hardest)
  - the feature analysis and positioning later

## 2. What the earlier deliverables set

| Set by | What it sets | How this task uses it |
|---|---|---|
| Audience page (Figma 2378:7111, 2378:7177) | Audience 1 = adult child or child-in-law caring for a parent or parent-in-law. Audience 2 = spouse or partner. | Every count is split into these two. Other relatives, children and clients are counted separately, not in either audience. |
| Market analysis coding (`docs/sources/market-analysis-3/CODING-INSTRUCTIONS.md`) | The "cared_for" labels: parent, spouse or partner, other relative, child, client, unclear | The same labels, so the numbers line up with the market analysis |
| Market analysis 3 (audience tables) | Reddit sample: 65% of caregiver posts are about a parent, 8% about a spouse. Forums: 55 parent threads, 54 spouse threads (mostly ALZConnected). | Expect few spouse posts on Reddit. See the decision rule in section 4. |
| Audience page use cases | Exhaustion is use case #1 for both: 138 adult-child posts, 45 spouse posts | Barriers are reported against each audience's use case #1 |
| Competitive analysis 3 | Criteria 4 (parent refuses) and 5 (relatives share), with no competitor scoring Yes | Check whether "the parent refuses" and "family won't help" hit Audience 1, Audience 2 or both |

## 3. Saved research on the topic

The same as `docs/market-analysis-segments-11-12-inputs.md`, nothing new. The audience part comes from the audience page, `docs/audience-teacher-format-2026-11-04.md`, `docs/audience-segmentation.md` and `docs/market-analysis-3.md` (audience tables).

## 4. How the research splits

1. **Script pass:** look for how each writer names the person cared for ("my mom," "my dad," "my mother-in-law" versus "my husband," "my wife," "my partner," and so on). Save the matched words for every post so each label can be checked.
2. **Readers for the hard ones:** posts with no clear match, or with both a parent and a spouse named, are read by agents for this one question. They answer with the same "cared_for" labels and one exact quote, checked by script.
3. **Spot check:** a random 40 of the script's labels are also read by an agent, to measure how often the script is wrong.
4. **Decision rule for new research:** if fewer than 50 relevant posts end up labeled "spouse or partner," the Audience 2 numbers are too thin to report on their own. Then a focused new search runs:
   - Arctic Shift: recent posts from r/dementia, r/Alzheimers and r/CaregiverSupport that mention a husband, wife or partner together with respite, adult day, a therapist or a support group
   - the ALZConnected forum's spouse and partner caregiver area, following robots.txt with a 10-second delay
   - All of it cited, saved and logged. The owner is told before it starts.

## 5. The questions (unchanged, now asked per audience)

| Question | Where it comes from |
|---|---|
| What do caregivers use for relief? | `exhaustion-dementia-research.md`, the 10 offerings |
| What helps? | Same |
| What stops them from using it? | AARP p.26 reasons, plus the relief reading pass |
| Who provides it? Who pays, and what does it cost? | Market segments 11 and 12, and the who-pays open question |
| Does each barrier hit Audience 1, Audience 2 or both? | Audience page, Competitive Analysis 3 criteria 4 and 5 |

## 6. What will be produced, and how to audit it

- `label_audience.py` → `audience-labels.json`: each post's label, how it was decided (the script's matched words, or the reader's quote), and the spot-check result
- an updated `count_results.py` → `results.json`, with every count split by audience
- the findings file, updated with Audience 1 and Audience 2 columns
- **Checks:** reader quotes verified word for word, every post labeled exactly once, and the spot-check error rate reported
- **Limits:** a writer may care for more than one person; those posts get the person most of the post is about, and the count of such posts is reported
