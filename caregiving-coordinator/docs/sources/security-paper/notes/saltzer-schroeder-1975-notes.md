# Notes: The Protection of Information in Computer Systems (Saltzer and Schroeder, 1975)

- **Source:** Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*. Author's HTML copy: https://web.mit.edu/Saltzer/www/publications/protection/ (accessed 2026-11-18). **Volume, issue and page range are not shown on the saved copy.** The source list says "Proceedings of the IEEE, 1975." Confirm the volume, issue and pages on IEEE's page before writing the bibliography.
- **Saved copy:** `caregiving-coordinator/docs/sources/security-paper/saltzer-schroeder-1975/` (the front page, Section I `Basic.html`, Section II `Descriptors.html`, Section III `State.html`, `References.html`, `notes.html` and a text copy of each).
- **No journal page numbers exist on this copy.** It is split into HTML pages. Cite by section, for example (Saltzer & Schroeder, 1975, Sec. I-A3, "Design Principles"). APA 7 allows a section name when a source has no page numbers.
- **The copy states:** manuscript received October 11, 1974, revised April 17, 1975, copyright 1975 by J. H. Saltzer (`Meta.html`).
- **Read in full (2026-11-18):** the front page and glossary, Section I "Basic Principles of Information Protection" (all of it), and Section III "The State of the Art."
- **Not read:** Section II "Descriptor-Based Protection Systems" (about 11,900 words on capability systems and access control lists in hardware), the reference list and the footnotes. Section II is technical hardware design and the paper will not cite it. The abstract says a reader can skip it (front page).

## What the paper says (my words)

| Point | Section |
|---|---|
| The paper's concern is controlled sharing of information among several users, in systems such as airline reservations, online medical information systems and social service data systems. | I-A1 |
| "Security" means techniques that control who may use or modify a computer or its information. There are three kinds of violation: unauthorized release of information, unauthorized change, and unauthorized denial of use. The biggest complication is that the "intruder" may be an otherwise legitimate user. | I-A1 |
| Protection is hard to prove, because it is a negative requirement: you must show every possible threat was anticipated. A narrow focus on protection mechanisms can give false confidence, so an expansive view is better. | I-A1 |
| It lists four functional levels: all-or-nothing isolation, controlled sharing, user-programmed sharing controls, and putting strings on information after release. | I-A2 |
| The dynamics of use matter as much as the static rules: who may change who can access, and what happens when access is revoked while a file is in use. | I-A2 |
| The paper gives eight design principles: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, and psychological acceptability. | I-A3 |
| Fail-safe defaults: base access decisions on permission, not exclusion, so the default is no access. A mistake in a permission-granting mechanism fails by refusing access, which is quickly noticed. | I-A3 b) |
| Complete mediation: every access to every object must be checked for authority, and remembered results of a check must be updated when authority changes. | I-A3 c) |
| Open design: the design should not be secret. Protection should depend on keys or passwords, not on attackers' ignorance. | I-A3 d) |
| Separation of privilege: where possible, require two keys, so no single accident or breach of trust is enough. | I-A3 e) |
| Least privilege: every program and user should work with the least privileges needed. It limits damage from accidents and reduces what must be audited. | I-A3 f) |
| Psychological acceptability: the human interface must be easy, so people routinely use protections correctly. | I-A3 h) |
| Two more ideas, which "apply only imperfectly" to computers: work factor (cost of getting around a protection compared with the attacker's resources) and compromise recording (reliably recording that a breach happened). | I-A3 |
| The principles are warnings, not absolute rules. A design that breaks one needs careful review. | I-A3 |
| Passwords have known defects: people choose guessable ones (in a study of about 300, over half were easy to guess), forced random ones get written down, and they must be exposed to be used. | I-B4 |
| Password lists should be stored after a hard-to-reverse transformation. | I-B4 |
| Passwords and physical tokens authenticate the user to the computer but not the computer to the user, so a fake system can steal a password. | I-B4 |
| A "principal" is the entity accountable for a virtual processor's actions. One person may need different principals, following least privilege. | I-B5 |
| Section III: in 1975 most commercial systems protected against accidents, not against users, and controlled sharing was "still the exception." Open problems included certifying that protection works, failures that silently disable protection, and better user interfaces. | III-A, III-B |
| Testing by sample cases tells almost nothing about protection, since protection is a negative specification. | III-B a)-b) |

## Possible use in the paper
- Topic 1 (introduction) and Topic 3 (background): the 1975 principles show where the field's ideas started, and the three violation types give a plain definition.
- Topic 8: fail-safe defaults, least privilege, complete mediation and separation of privilege line up with the idea's row-level security rules and "a failed check denies access" (T4.3.1). This does not say the idea is secure or compliant.

## Limits
- It is a 1975 paper on multiuser computers. Cite it for principles, not for current techniques (for example, its password advice is dated).
- The saved copy has no journal page numbers, so quotes and citations use section names.
- Section II, the reference list and the footnotes were not read.
