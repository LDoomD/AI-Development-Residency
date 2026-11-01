Yes, several things.

**1. Third-party AI service**
- Visit transcripts are likely health information about the care recipient, and they may also include caregivers' voices and details. Sending them out is a disclosure of sensitive data.
- Check the vendor's terms. Does it retain your data? Does it train models on it? Where is it processed? Which sub-processors does it use? Get a written data processing agreement. If the data counts as protected health information under HIPAA, you need a Business Associate Agreement. Many consumer-tier AI APIs do not offer one.
- Ask for zero-retention or no-training settings, and use an enterprise tier if one exists.
- Minimize what you send. Strip names, addresses, and other identifiers before transmission where possible.
- Tell users and get informed consent. Everyone recorded, including family members and caregivers, should know that an outside AI vendor processes the transcripts.
- Add the vendor to your privacy policy, and plan for the vendor having an outage or a breach.
- AI summaries can be wrong. Label them as AI-generated and let people see the original.

**2. Keeping recordings forever**
- Indefinite retention is the bigger problem. It breaks the principle of keeping data only as long as needed, and it grows your breach exposure every year.
- Recordings are far more sensitive than summaries. They hold voices, which are biometric-like, along with intimate details of someone's health and home life.
- Recording consent laws vary by state, and some require all parties to consent. Check them.
- Define a retention schedule, for example deleting recordings after the summary is confirmed or after 30 to 90 days. Keep summaries longer if they are needed.
- Give users a way to delete their data and to export it. Deletion should reach backups and the vendor.
- Encrypt recordings at rest and in transit. Restrict and log who can access them.
- Decide what happens when a care recipient dies, a caregiver leaves, or an account closes.

**3. Next steps**
- Make an inventory of what data you hold, where it goes, and how long it stays.
- Get legal review. This is not legal advice, and I have not checked your actual code or contracts.
