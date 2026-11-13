# 🔎 v1 Audit: Requirements vs Prototype (2026-11-01)
- Source copy: https://app.notion.com/p/dae9219a4691825f800581e483133fbc
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:15.947Z
- Not saved: the inline database "v1 audit gaps" (collection://4bc9219a-4691-83de-a284-874949d1aa36), which holds the gap rows; see report

---

A skeptical audit of the v1 requirements against the hi-fi prototype, run by three independent reviewers and spot-checked against the docs, the Figma file, the framework data, and the harness code. Every gap below is assigned to the ticket that owns its fix.

## Morgan's decisions (2026-11-01)

| Blocker | Decision |
| --- | --- |
| What the matcher compares a posting against | All framework items, so non-standard hats can appear (ADR-0025) |
| A match found only by the AI | Kept only with a verbatim quote, shown as "Similar match" (ADR-0025) |
| Results flow | T06 as written: one part per screen, five steps, unplaced lines as step 5 |
| Accuracy bar for release | Label real postings, run a baseline, then set the bar from real numbers (T12) |
| A failed decode | Fixed by default: a plain error screen with Try again, inputs kept (T09, T13) |

## Checked and corrected during the audit

- The deliverable-ownership conflict is real: 14 of 129 duty-to-deliverable links disagree between the framework's two fields.
- "What counts as a line" was overstated: the harness already splits on new lines and sentence ends; the gap was only that T03 did not say so.
- "The prototype paraphrases the framework" was wrong: both Graphic Design texts are verbatim, from two different framework fields.
- T16's design link pointed at a deleted frame; it now points at the prep section.

## Gaps and fixes

Status key: Fixed (in the docs), In design (with the prototypes session), Morgan to confirm (a default was applied and needs your yes), Open (needs a decision).

Database: v1 audit gaps (inline, not saved)
