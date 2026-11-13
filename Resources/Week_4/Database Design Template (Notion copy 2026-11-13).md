# Database Design Template
- Source copy: https://app.notion.com/p/6849219a46918268bd83010c2b91d77b
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:24.398Z
- Not saved: none

---

> 📍 Fill this out before you make tables in Supabase. Ask Claude to help you fill it out from your Week 2 requirements. Then save a copy as `docs/database-design.md` in your repository.

# What does the app need to save?

List each kind of information your app needs to remember. Write one full sentence for each.

- 

# Tables

Make one table for each kind of thing. Copy this section for each table.

## Table name:

**What it stores:**

| Column name | Type of data (text, number, date, true or false) | Required? | What it means |
| --- | --- | --- | --- |
| id |  | Yes | A unique number or code for each row. |
| user\_id |  | Yes | The person who owns this row. |
|  |  |  |  |
|  |  |  |  |

**Who can see it?**

**Who can add, change, or delete it?**

# How the tables connect

Write one sentence for each connection. For example: "One person can have many budgets. Each budget belongs to one person."

- 

# Access rules

Supabase calls these Row Level Security, or RLS. Supabase says to turn on RLS for every table in an exposed schema.

- [ ] RLS is turned on for every table.
- [ ] Each table has a rule that lets people see only their own rows.
- [ ] I tested this with two accounts. One person could not see the other person's information.

# Database diagram

This is a deliverable. Pick one way to make it.

- **Way 1:** In your Supabase project, open the Schema Visualizer. It shows your tables and how they connect. Take a screenshot.
- **Way 2:** Ask Claude Code: "Make a diagram of my database tables and how they connect, as a Mermaid diagram in docs/[database-diagram.md](http://database-diagram.md)." GitHub shows Mermaid diagrams as pictures.

Save the diagram in your repository in the `docs` folder. Put the link in your Submission Template.

# Migration files

- [ ] Every change to my database is saved as a SQL migration file in my repository.
- [ ] I can tell what each migration file does from its name.
