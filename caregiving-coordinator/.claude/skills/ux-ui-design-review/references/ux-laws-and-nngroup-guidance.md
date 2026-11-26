# UX laws and Nielsen Norman Group form guidance

**Added 2026-11-25, with the owner's approval.** This is a reference file for the `ux-ui-design-review` skill. Use it to name the law or guideline behind a screen choice or a review finding.

**Rules for using it:**
- Name the law or guideline next to every finding or screen choice, with the source link.
- These are guides, not pass or fail tests. Say so in the finding when a law is only a guide.
- Do not add a number (such as a pixel size) unless a source below gives it. The sources below do not give a minimum touch-target size in pixels.
- Part 3 lists where the sources disagree. Report both numbers when a finding depends on one.

**Sources.** Part 1 is from lawsofux.com by Jon Yablonski. Parts 2 and 3 are from nngroup.com. Saved copies are in `caregiving-coordinator/docs/sources/ux-laws-2026-11-25/`. Copies were retrieved with Firecrawl on 2026-11-25 and retyped by a helper, so they are not byte-for-byte copies.

---

## Part 1. The 30 Laws of UX (lawsofux.com)

Link pattern: `https://lawsofux.com/<name>/`. The check column paraphrases each page's own takeaways.

### Choices and decisions
| Law | What it says | A check we can make | Source |
|---|---|---|---|
| Hick's law | More and harder choices mean slower decisions. | Fewer choices. Split big tasks into steps. Point out the recommended option. | hicks-law |
| Choice overload | Too many options hurts decisions and how people feel about the experience. | Let people compare related options side by side. Show the most important content first. | choice-overload |
| Occam's razor | The simplest answer with the fewest assumptions is the best. | Remove each element you can without hurting what the screen does. | occams-razor |
| Pareto principle | About 80% of the effects come from 20% of the causes. | Put the most effort where it helps the most people. | pareto-principle |
| Tesler's law | Some complexity can't be removed, only moved to the system or to the user. | Let the system carry the complexity instead of the person. | teslers-law |

### Memory and effort
| Law | What it says | A check we can make | Source |
|---|---|---|---|
| Cognitive load | Mental effort the screen asks for. Too much and people miss details. | Remove distracting or unneeded elements. | cognitive-load |
| Working memory | People hold a few chunks of information for a short time. | Carry information from screen to screen. Show what was already seen. | working-memory |
| Miller's law | Short-term memory holds about 7 plus or minus 2 items. | Group content into smaller chunks. Don't use "seven" to justify arbitrary limits. | millers-law |
| Chunking | Information is easier to take in when grouped into meaningful units. | Use visibly separate groups with a clear order. | chunking |
| Mental model | People bring an idea of how a system works from products they know. | Match the design to that idea. Use research to find the gap. | mental-model |
| Jakob's law | People expect your product to work like ones they already use. | Reuse familiar patterns. During a change, keep the old version for a limited time. | jakobs-law |
| Paradox of the active user | People skip manuals and start using the product. | Put guidance in the place and moment it is needed. | paradox-of-the-active-user |
| Serial position effect | People remember the first and last items best. | Put key actions at the far ends of a navigation bar. | serial-position-effect |

### How things are grouped (Gestalt)
| Law | What it says | A check we can make | Source |
|---|---|---|---|
| Law of proximity | Things near each other look related. | Put related items close together. | law-of-proximity |
| Law of common region | Items inside one bounded area look like a group. | Use a border or background behind related items. | law-of-common-region |
| Law of similarity | Items that look alike look related. | Make links and navigation look different from plain text. | law-of-similarity |
| Law of uniform connectedness | Items that are visually connected look more related. | Connect related items with color, lines, frames or arrows. | law-of-uniform-connectedness |
| Law of Prägnanz | People read complex shapes as the simplest form. | Prefer simple figures. (The page gives no further check.) | law-of-pr%C3%A4gnanz |

### Attention and feel
| Law | What it says | A check we can make | Source |
|---|---|---|---|
| Selective attention | People focus on what relates to their goal. | Don't style content like an ad. Avoid many competing changes at once. | selective-attention |
| Von Restorff effect | The item that differs is remembered. | Make key actions stand out, with restraint. Don't rely on color alone. Be careful with motion. | von-restorff-effect |
| Aesthetic-usability effect | Attractive designs feel easier to use. | Don't trust "it looks nice" feedback. Pretty design can hide problems in testing. | aesthetic-usability-effect |
| Flow | Deep focus comes when challenge matches skill. | Give feedback on what was done. Remove friction. | flow |
| Peak-end rule | People judge an experience by its high point and its end. | Design the most important moment and the last moment with care. | peak-end-rule |
| Cognitive bias | Mental shortcuts skew judgment. | The page gives no design check. | cognitive-bias |

### Speed, effort and finishing
| Law | What it says | A check we can make | Source |
|---|---|---|---|
| Doherty threshold | Responses under 400 milliseconds keep people productive. | Give feedback within 400 ms. Use a progress bar or animation for longer waits. | doherty-threshold |
| Fitts's law | Time to hit a target depends on its size and distance. | Make touch targets large, well spaced, and easy to reach. | fittss-law |
| Goal-gradient effect | People work faster the closer they get to a goal. | Show clear progress. | goal-gradient-effect |
| Zeigarnik effect | Unfinished tasks are remembered better. | Show signs of more content and clear progress. | zeigarnik-effect |
| Parkinson's law | A task grows to fill the time available. | Keep a task as short as people expect. Use autofill in forms. | parkinsons-law |
| Postel's law | Be liberal in what you accept, conservative in what you send. | Accept varied input, translate it, set limits, give clear feedback. | postels-law |

---

## Part 2. Nielsen Norman Group guidance for forms, sign-up, log-in and errors

Link pattern: `https://www.nngroup.com/articles/<name>/`.

| Topic | What it recommends | Source |
|---|---|---|
| Form layout | Use a single column. Avoid placeholder text. Cut optional fields where you can. Avoid Reset or Clear Form buttons. | web-form-design |
| Registration | Ask only for the minimum, ideally email and password. Don't repeat fields (two password or two email fields). Don't ask people to confirm registration by email. This article is about mobile forms and dates from 2017. | checklist-registration-login |
| Log-in | Let people show the password, but not by default at log-in. Include a "Forgot password?" link. | checklist-registration-login |
| Password creation | State the password rules and keep them visible while the field is selected. Let people unmask the password. | password-creation |
| Error messages | Show the message close to the error. Use more than color alone. Don't show errors too early. Use a positive tone and don't blame the person. Keep what they typed. | error-message-guidelines |
| Consistency | Keep fields and buttons in the same place, especially across steps of a form. | consistency-and-standards |
| Response times | About 0.1 second feels instant. About 10 seconds is the limit for keeping attention. Longer waits need a percent-done indicator. | response-times-3-important-limits |

---

## Part 3. Where the sources disagree or are silent
- **Memory size:** Miller's law says 7 plus or minus 2. The working memory page says 4 to 7 chunks that fade in 20 to 30 seconds. NN/g's short-term memory article says about 7 chunks fading in about 20 seconds.
- **Waiting time:** lawsofux.com says 400 milliseconds. NN/g gives 0.1 second, 1 second and 10 seconds. These are different framings, not the same limit.
- **Showing passwords:** NN/g's 2015 password article suggests showing passwords by default on mobile. Its 2017 checklist says to mask by default at log-in.
- **Hick's law:** NN/g has no article on it. Only a video page exists and it was not watched.
- **No pixel sizes:** neither site gives a minimum touch-target size in pixels in the pages read.
- **Not read:** five NN/g articles cited inside the saved pages (login walls, optional registration, form white space, form placeholders, reset and cancel buttons) and an error-message scoring rubric.
