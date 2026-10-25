# Personal experience and product ideas — direct input, 2026-10-24

**Labeled explicitly by the author as personal experience and opinion, not
research.** Recorded verbatim-in-substance so it isn't lost. Cross-reference
against existing research below is mine, added for traceability - the
problems and ideas themselves are his.

## Personal problems named

- Takes notes but does not go back to learn or retain the information.
- Does not know how to effectively study his notes, which method to use, or
  how to measure whether the studying is actually working.
- Enjoys taking organized notes, but struggles to go back to them, pause a
  course's forward progress, and dedicate real time to retaining what was
  already captured.
- Is not sure if his note-taking itself is effective for studying and
  retention - not sure he is taking notes "correctly" while learning.
- Has tried named methods (Pomodoro, time-blocking, following a schedule)
  and cannot stick to them. Wants help taking effective breaks and actually
  returning to the material afterward.
- Wants structure and a foundation for learning, because he does not have
  one - and wants that foundation to hold even when he is not actively
  studying.

*(Matches and reinforces `2026-10-24_lived-experience-notes.md` and the
inherited `2026-08-13_learning-how-to-learn.md` self-regulation gap - this is
the same gap described again, in more operational detail: not just "never
learned how to learn," but specifically never learned how to resume,
measure, or sustain it.)*

## His own ideas for what to do about it

1. **Multimodal content from notes** (podcast-style audio, video, flashcards)
   - cites personal positive experience with NotebookLM for this.
2. **Being prompted to study at the right moment**, e.g. on waking, as a
   reminder of how important retention is.
3. **Quizzes/tests per chapter or module**, gating progress until the
   material is actually understood before moving to the next one.
4. **Experimenting with different note-taking styles** to find what fits the
   learner or the subject.
5. **An AI agent specialized in neurodivergent learners** that crafts a
   tailored note-taking method from the student's own data and history.
6. **AI that fully profiles the learner** - type of learner, specific
   weaknesses - to drive recommendations across study method and the
   multimodal experience.
7. **A self-improving tutoring system** whose recommendations and
   personalization get better over time, fed by an onboarding step that
   gives the agent this context from day one.
8. **Using the phone for short learning exercises at the student's most
   effective times of day**, to keep progress and retention on track.
9. His own closing caveat: *"all of this must be grounded in real scientific
   research, and real outcomes."*

## Where each idea already stands against this project's own research

| Idea | Status |
|---|---|
| Multimodal content from notes | Outcome is sound; NotebookLM specifically is not buildable into this app (no API - already resolved earlier this session). Achievable by calling a model directly instead. |
| Prompted at the right moment / on waking | As a push notification, already tested and failed for this population (Nordby et al. 2022 RCT, `DECISIONS.md` §4). The intent is sound; `2026-10-24_phone-engagement-mechanisms.md` already proposes a non-notification alternative (self-authored if-then cue, home-screen icon) that serves the same intent without repeating a failed mechanism. |
| Quizzes/tests gating progress per module | **Already locked design**, not a new idea - this is the Examiner / mastery gate (`DECISIONS.md` §8-9), evidence-before-verdict grading. Confirms the existing design rather than adding to it. |
| Trying different note-taking styles | New. No prior research in this project covers this - genuinely open scope. |
| AI agent tailoring a note-taking method from the student's own data | Real tension with the self-regulation goal, not a free addition. If the AI picks the method *for* the student permanently, that is exactly the "metacognitive laziness" / strategy-selection offload risk already flagged in `2026-08-13_learning-how-to-learn.md`. The fix already proposed there - bounded autonomy, fading over time - applies directly: suggest and explain early, hand the choice back later. |
| Full learner profiling + self-improving personalization + onboarding | Reasonable extension of the existing course-profile intake (`STATUS.md`) to also capture a learner profile. New, but does not conflict with anything locked. |
| Phone exercises at effective times of day | Same notification-shaped mechanism as #2 above - same status, same proposed alternative. |
