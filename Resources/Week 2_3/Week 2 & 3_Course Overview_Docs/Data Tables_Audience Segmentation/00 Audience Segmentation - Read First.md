# Audience Segmentation - Read First

These 6 CSV tables are one deliverable: the **audience segmentation** for a product that helps family caregivers. It comes after the market analysis (folder `Data Tables_Market Analysis/`) and before the competitive analysis.

**The two audiences**
- **Audience 1:** an adult child (or child-in-law) caring for a parent.
- **Audience 2:** a spouse or partner caring for a husband, wife or partner.

**How each file is built**
- Line 1 is the table's title. Line 2 says what the table shows. Line 3 is the column header row.
- One row = one fact, goal, problem or note.

## The 6 tables

| Read order | File | Section and table | What it answers | Split by audience? |
|---|---|---|---|---|
| 1 | `Audience Segmentation Definition.csv` | Section 1 | Who family caregivers are: where they live, what they do, who they are, and their money situation | No: all US family caregivers |
| 2 | `Audience Motivations and Goals.csv` | Section 2, table 2a | Why each audience acts, what they want right now, and what they want for their own life | Yes: Audience column |
| 3 | `Audience Use Cases.csv` | Section 2, table 2b | Each audience's problems, when they happen, what should change, and the scenarios to support | Yes: Audience column |
| 4 | `Audience Sources and Limits.csv` | Section 2, table 2c | How tables 2a and 2b were made, and what they cannot show | Notes for 2a and 2b |
| 5 | `Top Problems.csv` | Section 3, table 3a | The top caregiver problems, with each kind of source side by side | No: both audiences together |
| 6 | `Top Problems Sources and Limits.csv` | Section 3, table 3b | Who the posts are about, other problems found, and what table 3a cannot show | Notes for 3a |

## How the tables connect

- **2a and 2b** describe the same two audiences. The Audience column links them.
- **2c explains 2a and 2b.** **3b explains 3a.** Read them before drawing conclusions.
- **3a and 2b cover overlapping problems**, such as burnout and breaks, money and papers, and a parent who refuses help. They were counted differently, so their rows do not match one to one.
  - 3a counts each problem across all sources for both audiences together.
  - 2b counts each problem separately for each audience.
- **1 gives national context** (AARP/NAC 2025 survey) for the people in 2a, 2b and 3a.
- **Link to the market analysis:** the market analysis points to helping worn-out caregivers get a break (respite and adult day services, and caregiver mental health). That matches burnout as problem 1 in 3a, and use case 1 for both audiences in 2b.

## Known gaps

- **The forum totals differ.** Section 3 uses 117 forum threads; the market analysis uses 141. No saved file explains the difference.
- **Table 1 is not split by audience.**
- **Audience 2 has fewer posts** (35 Reddit posts), so its order is less certain (table 2c).
