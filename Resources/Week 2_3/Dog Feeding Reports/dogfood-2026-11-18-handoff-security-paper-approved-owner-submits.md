# Handoff: Premium paper on advanced information security → paper approved and merged; the owner submits it (2026-11-18, twelfth report)

Replaces: `Resources/Week 2_3/Dog Feeding Reports/dogfood-2026-11-18-handoff-security-paper-all-sources-read-draft-next.md`. What changed: the owner answered decisions 5 and 6, the whole paper was drafted, polished, approved and merged, and a Google Doc copy exists. The older reports stay replaced; their paths are in the "Replaced by" line of the tenth report. Every path in this report starts at the repository's top folder (`AI Developer Residency `), which holds `caregiving-coordinator/`, `Resources/` and `.claude/`.

> Paste to start: "Read this handoff report and the files in section 8. Confirm in a few complete sentences where we are. Run `git fetch`, switch to `main`, run `git pull --ff-only`, and tell me which pull requests are open. Then ask me whether I sent the email, filled in the form, pasted the title block into my Google Doc and shared it, and wait. Use short, plain sentences. Do not call the caregiving coordinator an app. Never say it is secure or compliant. Ask before Chrome, Firecrawl or the browser pane. Do not start more than two helper agents at once without telling me first."

## 0. Start here
- **Where we are:** the owner's Week 2 Premium research paper on **advanced information security** is written, approved by the owner ("I approve the paper") and merged into `main`. Pull requests 86 to 93 are all merged and none are open (checked with `gh pr list` on 2026-11-18).
- **The outcome in one sentence:** an about-6-page paper with 8 topics in the course's order, APA 7 citations and 40 or so references, with the owner's own career reasons in topic 2.
- **Next milestone:** the **owner submits the paper**. The course page says: email the paper to the instructor, and fill in the course's Google form. The owner does both themselves. Claude does not send email.
- **What the owner still has to do (they said they will):**
  - Paste the title block (four lines, in section 8) under the title of their Google Doc. Claude's Google Drive tools cannot edit text inside an existing Google Doc.
  - Share the Google Doc with the instructor. It is shared with no one right now.
  - Email the paper and fill in the form.
  - Change the Notion row to say it was submitted, or ask Claude to.
- **The paper is about a hypothesis.** The proposed caregiving coordinator is a product idea, not built. Never call it "your app" and never say it is secure or compliant.
- **Cost note:** no helper agents were used in this chat.

## 1. Locked outcomes
| Outcome | Tag | Where it lives |
|---|---|---|
| Paper length: about 6 pages plus the bibliography | **Approved** (owner, chat) | `caregiving-coordinator/docs/security-paper/paper-final-2026-11-19.md` |
| Topic 2 (career): the owner's own ideas, grammar and tone polished by Claude after the owner's comment on the Claude Doc, plus three paragraphs of citations added by Claude | **Approved** (owner approved the whole paper) | Same file, topic 2 |
| Topic 1 wording (title, reader's note, foundations, not current threats) | **Approved** (owner, chat) | Same file, topic 1 |
| The whole paper | **Approved** (owner: "I approve the paper") | Same file |
| Title block: Orlando Castillo, AI Developer Residency, Week 2 Premium Assignment, November 18, 2026 | **Approved** (owner asked for it; pull request 93 merged) | `caregiving-coordinator/docs/security-paper/paper-final-2026-11-19.md`, top |
| The date in the title block is the computer's date, November 18, 2026 | **Proposed** (the owner did not choose the date) | `caregiving-coordinator/docs/security-paper/paper-final-2026-11-19.md`, top |
| Saltzer and Schroeder reference: Proceedings of the IEEE, 63(9), 1278 to 1308, DOI 10.1109/PROC.1975.9939 | **Approved** (the owner said to fix the loose ends) | `caregiving-coordinator/docs/sources/security-paper/saltzer-schroeder-1975/crossref-record.json` |
| Google Doc copy exists in the owner's Drive; the owner will paste the title block themselves | **Approved** (owner, "Option 1") | Link in section 8 |
| The Notion row "Premium research paper and proposal" now links to the Google Doc and the repository file, and says "Not emailed to the instructor yet" | **Approved** (owner: "Yes, update the Notion row") | Notion page "Week 2 and 3 - Product Specifications" (link in section 8) |
| Paper style: no em dashes, plain human wording | **Approved** (owner, chat) | Same file |
| The source list, quality rules and official domains | **Approved** (owner, 2026-11-18) | `caregiving-coordinator/docs/security-paper/source-list-2026-11-17.md` |

## 2. Key findings and data
What the paper rests on. Every row points to a notes file. The paper cites only what the notes record.

| Finding the paper uses | Source | Confidence |
|---|---|---|
| Jobs for information security analysts: 21% growth 2025 to 2035 (all jobs 3%), about 14,100 openings a year, median pay $129,180 (May 2025). A projection, not a promise. | `caregiving-coordinator/docs/sources/security-paper/notes/bls-and-isc2-cc-notes.md` | Authoritative |
| ISC2 2025 study: survey of 16,029 people, no workforce size or gap number (p. 3); top skills needs AI 41%, cloud 36%, risk assessment 29%, application security 28% | `caregiving-coordinator/docs/sources/security-paper/notes/isc2-workforce-study-2025-notes.md` | Reported (survey) |
| IBM 2026: average breach cost USD 4.99 million; healthcare USD 6.64 million (13th year costliest) | `caregiving-coordinator/docs/sources/security-paper/notes/ibm-cost-of-data-breach-2026-notes.md` | Authoritative for what IBM reports; sample is not statistical (p. 70) |
| Verizon 2026: more than 22,000 breaches; exploiting vulnerabilities 31% as the way in; third party in 48%; only 26% of known exploited vulnerabilities fully fixed | `caregiving-coordinator/docs/sources/security-paper/notes/verizon-dbir-2026-notes.md` | Reported (convenience sample) |
| OWASP Top 10:2025, SSDF, Secure by Design, Proactive Controls, SP 800-63-4 and 63B-4, SP 800-61r3, SP 800-207 | Notes files in `caregiving-coordinator/docs/sources/security-paper/notes/` | Authoritative |
| Next.js middleware bypass advisories (2025 and 2026); UpGuard's count of 16,326 exposed Supabase databases (a count, not a rate) | `caregiving-coordinator/docs/sources/security-paper/notes/nextjs-middleware-advisories-notes.md`, `caregiving-coordinator/docs/sources/security-paper/notes/upguard-supabase-and-rls-notes.md` | Authoritative (advisories); Reported (UpGuard, vendor research) |
| FTC: sharing health information without authorization counts as a breach; notice within 60 days | `caregiving-coordinator/docs/sources/security-paper/notes/topic-8-reuse-sources-notes.md` | Authoritative (the live FTC and HHS pages were blocked and not rechecked) |

Corrections the paper already follows: BLS is the 2025 to 2035 edition; ZAP is "ZAP by Checkmarx," not OWASP; OWASP Top 10:2025 (no web "Top 10 2026"); older sources (1975, 2008, 2017, 2020) are labeled with their year and used for ideas; the paper never says older methods are "still used" because no source in the notes measures that.

## 3. Excluded and deferred
- **The old agentic-workflows paper** `caregiving-coordinator/docs/specialization-research-paper.md`: superseded. The Notion row no longer points to it.
- **AI security standards and the OWASP LLM list:** out of scope because the first release of the proposed coordinator uses no outside AI service.
- **NIST SP 1347 and the NIST post-quantum report:** never read and not in the paper. See open decision 6.
- **Extra OWASP cheat sheets, the NICE Framework Resource Center page, SP 800-100r1 draft:** not used in the paper. See open decision 6.
- **Sources not read in full:** see the "Not read" lists in each notes file in `caregiving-coordinator/docs/sources/security-paper/notes/`.
- **The antivirus incident:** documented in `caregiving-coordinator/docs/incidents/2026-11-18-antivirus-flagged-saved-malware-writeups.md`. Do not recreate copies of malware write-ups without asking.
- **Recovery folder `~/.claude/_removed-gsd-2026-11-18`:** delete only when the owner says so.

## 4. Open decisions
Each decision says what it is, why it matters, the choices, and what happens after each. The next session must not decide these alone.
1. **Verizon paraphrase review.** Verizon's report (p. 9) allows exact numbers with a citation and says paraphrasing "requires review" by Verizon. The paper uses exact numbers with plain descriptions. Choices: (a) leave it as is, or (b) the owner writes to Verizon before submitting. After (a) nothing changes; after (b) Claude helps draft the message, and the owner sends it.
2. **Proactive Controls web address.** The paper cites `top10proactive.owasp.org` as official OWASP because owasp.org links to it. The owner never answered the question directly. Choices: keep it, or cite only the owasp.org project page. After "keep" nothing changes; otherwise Claude edits the reference.
3. **The start-of-session Git line in `caregiving-coordinator/CLAUDE.md` is still labeled Proposed.** Choices: the owner says approved and Claude removes the label, or leave it.
4. **Two proposed working rules after the antivirus incident and the helper-agent cost** (Claude does not add rules without the owner): (a) ask before saving copies of malware write-ups and keep them out of git; (b) tell the owner the expected cost before starting more than two helper agents. Choices: approve both, one, or neither. If approved, Claude adds them to `caregiving-coordinator/CLAUDE.md` in a pull request.
5. **ZAP correction in the source list.** `caregiving-coordinator/docs/security-paper/source-list-2026-11-17.md` still calls ZAP an OWASP project. Choices: add a one-line correction (it is an Approved file, so ask first), or leave it because the paper is already correct.
6. **Never-used reading items.** NIST SP 1347, the NIST post-quantum report, extra OWASP cheat sheets and the NICE Resource Center page were not read. Choices: leave them out and write the owner's reason in the source list, or read them later. The paper is finished either way.
7. **Notion row status after the email is sent.** Today it says "Not emailed to the instructor yet." When the owner sends the email, the row should say it was submitted. Claude changes it only when the owner says it was sent.

## 5. Bridge to the next milestone
| This output | Goes into | Why |
|---|---|---|
| `caregiving-coordinator/docs/security-paper/paper-final-2026-11-19.md` and the owner's Google Doc | The email to the instructor | The course says to email the paper |
| The Google Doc link | The instructor's access (Share in Google Docs) | The Google Doc is shared with no one yet |
| The course page "Week 2 PREMIUM RESIDENCY" (Google form link) | The form the owner fills in | The course says to fill in the form |
| The Notion row "Premium research paper and proposal" | The status the instructor sees | It should say "submitted" after the email |
| The notes in `caregiving-coordinator/docs/sources/security-paper/notes/` | Any later question about the paper's claims | Every claim traces to a notes file |

## 6. First steps
1. **Confirm where we are.** Run `git fetch`, `git switch main`, `git pull --ff-only`, `gh pr list --state open`. Tell the owner in a few sentences what is merged and whether anything is open. This report's own pull request may still be open.
2. **Ask one question at a time:** did the owner paste the title block into the Google Doc, share it with the instructor, send the email and fill in the form? Wait for each answer.
3. **If the email was sent,** ask whether to change the Notion row to say "Submitted" (open decision 7), then do it only on a yes.
4. **Then ask the owner what to do next.** Do not start anything. The owner's current week page is `Resources/Week_4/MY STEPS - Week 4 Build and Launch the App (plain words, 2026-11-18).md`; read it only to keep the owner on track.
5. **Before the chat gets full (about 55%):** run the checker, then write a new handoff report:
   `python3 .claude/skills/dogfooding-handoff/scripts/check_handoff.py "<report>"`

## 7. Working rules
Full rules: `caregiving-coordinator/CLAUDE.md`, `caregiving-coordinator/docs/deliverables-rules.md` (deliverables only, not the paper), and the memory index `MEMORY.md` in the project memory folder.
- **Short, plain, complete sentences, one question at a time.** The owner has ADHD. Name files and pages in full.
- **Never call the proposed coordinator "your app."** Never say it is secure or compliant.
- **No em dashes in anything the owner will submit, and write so it sounds human.** The owner asked for this on 2026-11-18. Page ranges use the short en dash (APA style).
- **The owner writes their own homework summary** ("What I Did," "What I Learned"). Claude never writes or edits it.
- **Google tools:** the Google Drive connector can create files and change sharing, but it cannot edit text inside an existing Google Doc. Say so before promising an edit. A Claude Doc is not a Google Doc; the owner exports it with the document's name menu, Export, Google Docs.
- **A document is not shared until the owner shares it.** Never change sharing settings without asking.
- **Notion:** the Notion connector reads and edits the owner's workspace. Use it for Notion pages. It cannot read the live Tech Fleet course pages, only the owner's copies.
- **Ask before Chrome, Firecrawl, the browser pane and Gmail.**
- **Questions get answers, not edits.**
- **Do not run many helper agents at once without telling the owner the cost first.**
- **Start every task with `git fetch`, switch to `main`, pull, and a new branch.** The owner merges fast, often before follow-up edits are pushed, so check the pull request state before pushing more to an old branch.
- **Never claim a section was read when it was not.** Helper agents' notes are spot-checked, not verified line by line; say so.
- **Never compact without a handoff report.** Write one at about 55% context.

## 8. Where things live
- **Final paper (approved, merged):** `caregiving-coordinator/docs/security-paper/paper-final-2026-11-19.md`
- **Earlier draft (kept unchanged):** `caregiving-coordinator/docs/security-paper/paper-draft-2026-11-18.md`
- **Cite plan version 2 (Proposed):** `caregiving-coordinator/docs/security-paper/cite-plan-2026-11-18-v2.md`; approved first version: `caregiving-coordinator/docs/security-paper/cite-plan-2026-11-18.md`
- **Source list (approved):** `caregiving-coordinator/docs/security-paper/source-list-2026-11-17.md`
- **Saved sources and notes:** `caregiving-coordinator/docs/sources/security-paper/` (notes in `caregiving-coordinator/docs/sources/security-paper/notes/`), logged at the end of `caregiving-coordinator/docs/sources/INDEX.md`
- **Incident note:** `caregiving-coordinator/docs/incidents/2026-11-18-antivirus-flagged-saved-malware-writeups.md`
- **Course page for the paper:** `Resources/Week 2_3/Course Pages (Notion copy 2026-11-13)/Week 2 PREMIUM RESIDENCY - Write a Research Paper and Proposal for Your Specialization Project (Notion copy 2026-11-13).md`
- **Claude Doc version (private, plainer wording, has the title block):** https://claude.ai/artifact/4rH61Ua8rar2bsrB5jaNZe
- **The owner's Google Doc (no title block yet; shared with no one):** https://docs.google.com/document/d/1Y5TUxXkmyRCBUDeXhScPLSH9l62z85CCw6Cis5CrjIo/edit
- **Title block the owner pastes under the title:**
  - Orlando Castillo
  - AI Developer Residency
  - Week 2 Premium Assignment: Write a Research Paper and Proposal for Your Specialization Project
  - November 18, 2026
- **Notion page with the row:** "Week 2 and 3 - Product Specifications" in the owner's private hub, https://app.notion.com/p/4179219a46918157976edbc20a0a829f
- **Git:** repository `LDoomD/AI-Development-Residency`. Pull requests 86 to 93 are merged. This report is on branch `dogfood-report-12-2026-11-18`, opened as a new pull request. The app repository `LDoomD/Week-3---Caregiving-Coordinator` is empty.

## 9. Verification receipt
- **Outcomes and where each came from:** sections 1 and 2. The owner's decisions are their chat replies on 2026-11-18. The merge states come from `gh pr list` and `gh pr view` run in this chat. The Google Doc's owner and sharing come from the Google Drive connector (`get_file_permissions`: one owner, no other people).
- **Checks run:**
  - A search found no em dash in the final paper file.
  - `git fetch`, `git pull --ff-only` and `gh pr list --state open` on 2026-11-18 showed everything merged.
  - The Notion update call for the row returned with no warnings.
  - The handoff checker `.claude/skills/dogfooding-handoff/scripts/check_handoff.py` was run on this report (result in the chat).
- **Not checked:**
  - Each paper claim was matched to its notes file, not to the original source. Helper agents wrote most notes in an earlier chat; they were spot-checked, not verified line by line.
  - The Saltzer and Schroeder volume and pages come from a Crossref record, not from IEEE's own page, which the fetch tool could not read.
  - I did not open the Notion page after the edit to see how it looks, and I did not open the Google Doc to read its text.
  - The paper's reading level and length were not measured. The body is about 3,200 words by my count, which is an estimate.
  - The HHS and FTC live pages were blocked and not rechecked.
- **How this prevents drift:** outcomes are tagged Approved or Proposed, the open decisions are listed with their choices, the first step requires the owner's answers, and nothing is started without the owner.
