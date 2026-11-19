# Notes: Threat Modeling Manifesto and OWASP Threat Modeling Cheat Sheet

Both sources are web pages without page numbers, so each point is tied to the page's heading. Both were read in full on 2026-11-19.

## 1. Threat Modeling Manifesto

- **Source:** Braiterman, Z., Shostack, A., Marcil, J., de Vries, S., Michlin, I., Wuyts, K., Hurlbut, R., Schoenfield, B. S. E., Scott, F., Coles, M., Romeo, C., Miller, A., Tarandach, I., Douglen, A., & French, M. (2020). *Threat modeling manifesto*. https://threatmodelingmanifesto.org/ (the page names these 15 authors as the working group).
- **Label for the paper:** a statement of values and principles written by a group of practitioners. It is not a standard. The page says it "contains ideas, but is not a how-to, and is methodology-agnostic". Licensed CC BY 4.0.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/threat-modeling-manifesto/index.html` (retrieved 2026-11-19). The page shows no date; the year 2020 is from the source list. Confirm the year before the bibliography.

| Point | Heading |
|---|---|
| Threat modeling is analyzing representations of a system to highlight concerns about security and privacy. | What is threat modeling? |
| The four questions: What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job? | What is threat modeling? |
| Its output is "threats", which inform later design, development, testing and post-deployment decisions. | Why threat model? |
| Who should do it: "You. Everyone. Anyone who is concerned about the privacy, safety, and security of their system." | Who should threat model? |
| Five values (valued more than the alternative): finding and fixing design issues over checkbox compliance; people and collaboration over processes, methodologies and tools; a journey of understanding over a one-time snapshot; doing threat modeling over talking about it; continuous refinement over a single delivery. | Values |
| Principles: the best use is early and frequent analysis; it must fit the organization's development practices and follow design changes in small iterations; outcomes matter when they are of value to stakeholders; dialog creates common understanding and documents record it. | Principles |
| Five helpful patterns: systematic approach, informed creativity, varied viewpoints, useful toolkit, theory into practice. | Principles (patterns) |
| Four anti-patterns: "Hero Threat Modeler" (it does not depend on one person's gift), "Admiration for the Problem" (move on to solutions), "Tendency to Overfocus", and "Perfect Representation" (several views are better than one). | Principles (anti-patterns) |

- **Possible use:** topic 6 (what teams do): the four questions are the standard frame for what a threat model is. The Manifesto's wording on privacy and safety fits a product that holds health and money information about another adult.
- **Limits:** it gives no method and no examples. The resources listed on the page are articles and talks that were not read.

## 2. OWASP Threat Modeling Cheat Sheet

- **Source:** OWASP Foundation. (n.d.). *Threat modeling cheat sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Label for the paper:** official project guidance (tier 1). It is a living page, so cite the retrieval date, 2026-11-19.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-threat-modeling-cheat-sheet/Threat_Modeling_Cheat_Sheet.html`.

| Point | Heading |
|---|---|
| Threat modeling is a structured, repeatable process for modeling a system from a security point of view, identifying threats and deciding how to respond. It is ideally done early, during design, and the model is maintained and updated with the system, as a normal step and not an add-on. | Overview |
| It builds on the Manifesto's four questions and breaks them into four steps: application decomposition (system modeling), threat identification and ranking, mitigations, and review and validation. | Overview; Addressing Each Question |
| The sheet says there is "no universally accepted industry standard" for the process. | Addressing Each Question |
| Benefits: find risks early so security is "built in" and not "bolted on", more security awareness, and better visibility of the system's data flows and trust boundaries. | Advantages |
| Step 1: data flow diagrams (DFDs) are the most common way to model. The diagram should show trust boundaries, data flows, data stores, processes and outside parties. Brainstorming is an alternative, especially when non-technical people take part. | System Modeling |
| For cloud systems, adapt the model for shared responsibility, managed services and APIs, multi-tenant and identity federation, and dynamic infrastructure. | Cloud Threat Modeling |
| Step 2: STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privileges). Each category violates a security property (authentication, integrity, accounting, confidentiality, availability, authorization). Ranking is, in theory, likelihood times impact, but both are hard to estimate. | Threat Identification |
| A table helps choose a technique: STRIDE for a technical design, attack trees for a multi-step attack, misuse or abuse cases for abuse of a valid workflow, LINDDUN for privacy, PASTA, OCTAVE and VAST for other needs. The sheet warns not to add techniques only to look thorough. | Choosing a Threat Modeling Technique |
| Step 3: each threat needs a response: mitigate, eliminate (remove the feature), transfer (contract or finance responsibility to another party; this does not reduce the likelihood by itself) or accept. Record each response and turn mitigations into requirements, and keep them current, as NIST SP 800-218 practice PW.1.2 recommends. | Response and Mitigations |
| Step 4: all stakeholders review the model. Questions include whether the diagram matches the system, whether all threats have a response and whether mitigations can be tested. | Review and Validation |
| Teams find it hard because of limited security knowledge, time pressure and weak communication. The sheet suggests inviting security staff, training developers and treating threat modeling as part of the normal development process. | Threat Modeling and the Development Team |
| References: the Threat Modeling Manifesto, an SEI summary of methods, and NIST SP 800-218. | References |

- **Possible use:** topic 6 (what teams do) and topic 4: a short, plain description of how a team runs a threat model, with STRIDE as the example. Topic 8 can say the idea would start with a diagram of its data flows (care circle members, health and money notes, invite emails) and a STRIDE pass. The paper must label that as a plan.
- **Limits:** the sheet is guidance and not a standard. It does not name a method for health data. Linked pages (SEI methods summary) were not read.
