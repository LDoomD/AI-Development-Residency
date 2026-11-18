# Notes: NIST SP 800-12 Rev. 1, An Introduction to Information Security

- **Source:** Nieles, M., Dempsey, K., & Pillitteri, V. Y. (2017). *An introduction to information security* (NIST Special Publication 800-12, Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-12r1
- **Saved copy:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-12r1/NIST.SP.800-12r1.pdf` (101 PDF pages, dated June 2017). Text copies in the same folder: `NIST.SP.800-12r1.paged.txt` (with PDF page markers) and `body-plain.txt` (body text only).
- **Downloaded:** 2026-11-18 with curl from https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-12r1.pdf
- **Read in full:** yes, PDF pages 1 to 101, including the glossary and the acronym list.
- **Page numbers below are the printed page numbers.** Printed page 1 is PDF page 11, so printed page = PDF page minus 10. The front matter uses Roman numerals.
- **Currency check:** see the batch 1 entry in `caregiving-coordinator/docs/sources/INDEX.md`.

## What the document says (my words)

| Point | Printed page |
|---|---|
| It is a starting point for people new to information security. It does not give step-by-step instructions. | p. 1 (Sec. 1.1) |
| Information security means protecting information and systems from unauthorized access, use, disclosure, disruption, modification or destruction, to keep confidentiality, integrity and availability. | p. 2 (Sec. 1.4) |
| Confidentiality, integrity and availability are defined: restricting who can see information, guarding against improper change, and timely access. | pp. 2 to 3 |
| Laws tell organizations to protect data in broad terms, such as limiting personal data to authorized users, and do not give detailed instructions. The text names HIPAA as a law for health information. | p. 4 (Sec. 1.5) |
| There are eight elements: security supports the mission; it is part of sound management; protections match the risk; roles are explicit; responsibilities go beyond one's own organization; the approach is comprehensive and integrated; it is assessed and monitored regularly; and it is limited by society and culture. | p. 7 (Ch. 2) |
| Security is a means to an end, not an end in itself. | p. 7 (Sec. 2.1) |
| Risk can never be removed completely. Protections that are too heavy waste resources and make systems hard to use. Protections that are too light leave the system open. | p. 8 (Sec. 2.2 to 2.3) |
| An organization that uses a cloud provider is still responsible for making sure the provider gives the right level of security. | p. 8 (Sec. 2.2) |
| Defense in depth means several layers of protection (rules, technology and physical measures) together. | pp. 9 to 10 (Sec. 2.6) |
| Security needs ongoing monitoring because threats change. | p. 10 (Sec. 2.7) |
| Privacy and security now work together. Security is needed for privacy, but privacy also covers harm from allowed handling of data. | p. 11 (Sec. 2.8) |
| Roles are listed, from risk executive to user. A small organization may give one person several roles. Users must follow acceptable-use rules and report odd behavior. | pp. 13 to 19 (Ch. 3) |
| A vulnerability is a weakness. A threat source can be adversarial or not (for example, errors and outages). A threat event is what can happen if a threat source meets a vulnerability. | p. 20 (Ch. 4) |
| Threat examples: fraud and theft, social engineering and phishing, insider threat, malicious hackers, malicious code, and ransomware. Ransomware is described as locking or encrypting files until a ransom is paid, and the text says that without good backups many businesses paid. | pp. 21 to 24 (Sec. 4.1) |
| Errors and omissions by people are a threat. Training reduces them. | p. 24 (Sec. 4.2.1) |
| Collecting large amounts of personal data creates privacy problems when security fails. | p. 25 (Sec. 4.2.3) |
| Policy comes in three kinds: program, issue-specific and system-specific. | p. 26 (Ch. 5) |
| Risk is a function of impact and likelihood. Risk management has four steps: frame, assess, respond, monitor. The Risk Management Framework has six steps: categorize, select, implement, assess, authorize, monitor. | pp. 34 to 37 (Ch. 6) |
| Assurance is confidence that security measures work. It is not a guarantee. | p. 38 (Ch. 7) |
| A system that defaults to the most secure option is more likely to be used securely, and older well-tested software may have fewer bugs. | p. 40 (Sec. 7.2.2.3) |
| Security tends to get worse during operation. Procedures are not followed and policy goes out of date. | p. 41 (Sec. 7.3) |
| Automated tools can find vulnerabilities; active tools try to exploit them and passive tools infer problems. Penetration testing tries to break in. | pp. 43 to 44 |
| Backups must be tested to be sure they work. Maintenance accounts with factory passwords must be changed. | pp. 49 to 50 (Sec. 8.4, 8.7) |
| Cryptography protects data in transit and when it leaves the owner's control. Key management is the weak point: security depends on protecting the keys. | pp. 52, 55 (Ch. 9) |
| There are 20 control families (such as Access Control, Audit and Accountability, Identification and Authentication, Incident Response, Individual Participation, and System and Information Integrity). | pp. 59 to 70 (Ch. 10) |
| Authentication can rest on something you know, have, are or do. Each has drawbacks. | p. 62 (Sec. 10.7) |
| It costs far more to add security later than to include it from the start of a system's life. | p. 69 (Sec. 10.18) |
| The privacy-related families say a collector should have a clear reason, notify people, ask consent and let them correct data. | pp. 63, 65 to 66 (Sec. 10.8, 10.12) |
| Least privilege is defined in the glossary as giving each entity only the minimum resources it needs. | p. 81 |

## Possible use in the paper
- Topic 1: definitions of information security and the confidentiality, integrity and availability triad, plus the eight elements.
- Topic 5: the 20 control families as the list of what the field includes.
- Topic 8: the privacy families (consent, notice, correction) and the point that a provider does not remove the organization's own responsibility. These do not say the proposed coordinator is secure or compliant.

## Limits
- It was written for federal systems and says so, though it states the ideas apply to any organization (p. 1, Sec. 1.2).
- It is from 2017 and is based on SP 800-53 Rev. 4. NIST's current page for it is checked in the INDEX entry.
- The source list called the elements "eight core principles". The document calls them "eight major elements" (p. 7), so the paper should use that wording.
