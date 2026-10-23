# Session handoff — 2026-10-23

Written at the end of the session that created this project, so the next
session can pick up without re-deriving anything.

## Read these, in this order

1. **`STATUS.md`** — where the project stands, open decisions, why it replaced
   `growth-ads-system`
2. **`CLAUDE.md`** — working rules. The important one: **grep
   `docs/inherited-research/` before doing any new research.** That corpus is
   cited, adversarially reviewed, and records claims that were tested and
   killed. Skipping it risks reintroducing a falsified claim.
3. **`docs/WEEK2-PLAN.md`** — the schedule, hard due dates, and all nine
   Week 2 deliverables with status per item

## The immediate next task

**Draft the message to Morgan Denner (mdenner@techfleet.org).** This was the
agreed next action. One message, five things in it:

1. **Specialization choice** — AI Automation + Advanced agentic workflows,
   combined, framed as *agentic workflows applied to adaptive learning
   systems*. ⚠️ This was **due Oct 19** and is overdue. Ask for approval; the
   syllabus requires instructor sign-off on specialization topics.
2. **The project switch** — the specialization project changed from a
   multi-channel ads reconciliation panel to this learning system. Reason:
   the ads product's critical path ran through third-party approval queues
   (Google Ads Standard review, Meta Full Access, Shopify Level 2, Amazon
   per-seller auth, Mercado Libre access unconfirmed), and Week 3 needs a
   working Vercel deployment by Nov 2.
3. **Repo naming is contradictory** — Week 1 says one repo named
   `AI Development Residency` with a folder per week; Weeks 3–8 say a separate
   repo per week (`AI DEVELOPMENT RESIDENCY - WEEK 3 - APP`, then clone to a
   Week 6 repo). Which one? **This blocks creating the GitHub repo.**
4. **Does Week 4 use my app or the O*NET chatbot?** Week 4's premium section
   reads "building the same thing as Standard Residency students" — the only
   week whose premium section names a specific app instead of the student's
   own. Every other week substitutes the specialization project.
5. **Notion or Word docs?** The syllabus says "document your homework in word
   docs"; the Week 2 page says Notion and to email a Notion link.

Keep it short and plain. He is the instructor, not a client.

## After that

- **Rewrite Section 8 of `Week 2 Coding Challenge/research-paper.md`.** It
  still describes the ads product. Sections 1–7 stand — the specialization did
  not change. Also: §2.4 should be put in the user's own words, and all seven
  source links re-verified.
- **Four Assignment B templates are empty**, due **Oct 26**: Release Vision
  and Scope (the biggest), Epics and Features, the build plan, the backlog,
  and the pitch deck. See `docs/WEEK2-PLAN.md` for exact required fields.

## Three decisions the user still owes

Recorded in `STATUS.md`; none can be made on their behalf.

1. **The chosen subject is tagged for only two modes.**
   `docs/inherited-research/subjects.md` marks "Agentic engineering" as
   MAP + REPS — no DRILL, no EXAMPLES. That fights the decision to ship all
   four modes. Revising the tagging looks defensible but the August tagging
   was considered, so change it deliberately and write down why.
2. **Personal tool or multi-user product?** The predecessor's `CLAUDE.md` said
   "one user, not a general product." Weeks 3 and 5 require user accounts and
   secured user data.
3. **Repo naming** — blocked on Morgan, see above.

## Scope already settled — do not re-litigate

- **Subject domain: automation and agentics.** Not Spanish, not F&I.
- The subject domain only decides **what seed content sits in the database.**
  The user is **not** using this app to study agentics while building it — that
  reading was explicitly rejected as "ludicrous." Do not frame it as his live
  study tool.
- **All four router modes present in Week 3**, with **REPS deliberately thin**
  (record and self-rate, no AI judging) until **Week 7**, whose assignment is
  literally "make your application agentic somehow."
- **Stack is set by the course**: Vercel, Supabase, Material UI, GitHub,
  Cloudflare, OpenRouter. Not open for debate.

## Two hard rules

- **Never draft the "What I Did" or "What I Learned" sections** of any weekly
  submission. The instructor writes: *"DO NOT use AI for this! I will check!"*
  Supplying a factual list of actions as raw material is fine; the writing
  must be the user's own.
- **Plain English, eighth-grade reading level, in every artifact** — including
  graded academic ones. This was got wrong once already today: the first draft
  of the research paper came back as dense academic prose and had to be
  rewritten from scratch. Clear and rigorous are compatible.

## Where the other folders went

- `../growth-ads-system` — **parked.** PARKED banner at the top of its
  `STATUS.md`. Clean on `main`, PR #1 merged. Do not build there.
- `../ADHD-Learning-System` — the original archive this project's research was
  copied from. Read from it if something seems missing; never build in it.
