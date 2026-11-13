# 🗃️ Data Records - Hat Check
- Source copy: https://app.notion.com/p/0349219a4691838588e801fd51463478
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:11.791Z
- Not saved: files translator-table.csv and postings-dataset.csv; GitHub link-preview

---

## Skills and Practices Framework

This repository of data was made by Tech fleet and offers an open source dataset standardizing cross-functional product development work. See the data here on this website: [https://techfleetworks.github.io/skills-and-practices-framework/](https://techfleetworks.github.io/skills-and-practices-framework/)

Get the data from the repository here: https://github.com/techfleetworks/skills-and-practices-framework

# Translator table (job translation CSV)

[video/file not saved: translator-table.csv]

- **What it is:** the reviewed term-to-framework table. It maps the wording real job postings use (for example "prototyping", "journey mapping", "IA", "specifications") to the Skills and Practices Framework item it means.
- **Size:** about 300 rows, 36 KB.
- **Where it lives in the repo:** `eval/translator-table.csv` (source of truth). The matcher reads a generated copy, `eval/aliases.json`.
- **Decision record:** ADR-0020 (Translator table, alias layer for matching recall).

## Postings dataset (the job posting data dump)

[video/file not saved: postings-dataset.csv]

- **What it is:** the full detail of 934 real, public job postings collected from Greenhouse, Lever, Ashby, and Jobgether job boards across 9 titles (UX Designer, UX Researcher, Product Manager, Product Owner, Business Analyst, Product Analyst, Project Manager, UX Engineer, Developer). The translator table was built from this corpus.
- **Size:** 6.8 MB.
- **Where it lives in the repo:** `eval/postings-dataset.csv`. It is git-ignored (not committed), so this Notion copy is the durable record.
- **Honest limit:** rare titles came in under the 100-per-title target because public job-board APIs only list what is open (for example Product Owner 28, Product Analyst 12).
