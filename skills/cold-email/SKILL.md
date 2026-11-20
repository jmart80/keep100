---
name: cold-email
description: Writes B2B cold emails for Keep100 founders that earn replies instead of pitching - the five-email sequence, each day's personalized sends, and the sending setup that keeps email out of spam. Use on the B2B track once a prospect list exists, or when the founder wants a cold email or follow-up sequence written, today's outreach drafted, an outreach email audited, or asks about deliverability, sending domains or why emails land in spam.
---

# Cold email

Adapted from the cold-email-sequence skill by Keep100's author. A cold email opens a conversation. It doesn't pitch, close or inform. Every rule serves **relevance**: the prospect's world first, the product second. A sequence is one story told across five emails, never the same pitch five times.

This skill writes. `keep100:prospect-list` decides who to write to and who is due today. `keep100:sales-replies` handles every reply.

## Inputs

Everything comes from the company files. Never assume anything about the product.

| What the emails need | Where it comes from |
|---|---|
| What it is, what the prospect would call it | `company/product.md`, `company/positioning.md` (Category) |
| Who to write to, and why now | `sales/pipeline.csv` (each row's trigger), `company/positioning.md` (Who to win first, Champion) |
| The problem and the cost of doing nothing | `company/customers.md` quotes, `company/positioning.md` |
| A second angle for email 4 | A different pain, person or use case from `customers.md`. Not the same problem reworded |
| Proof | `[confirmed]` entries in `company/facts.md` only. None is normal for a new founder |
| No-cost offer for email 4 | Agree one with the founder: an audit, teardown, sample or setup help |
| What has worked | `learnings.md` |
| Sender name | The founder |

If a needed input is missing, ask for it. Don't draft around a gap. If `sales/pipeline.csv` is empty, run `keep100:prospect-list` first.

## Branch A: Sending setup (before the first send)

Read [SENDING.md](SENDING.md) and walk the founder through it one step at a time. Record where most prospects are in `sales/CLAUDE.md`. Tick "Sending setup" in `progress.md`.

## Branch B: Write the sequence

1. Read [TEMPLATES.md](TEMPLATES.md) for the emails in scope.
2. Draft. Use "I", never "we". The founder is one person and that is an advantage.
3. Run the gate below on every email.
4. Save to `sales/<date>-sequence.md`, with each email under a heading `## Email 1` to `## Email 5`. Tick "Email sequence written".

| Email | Role | Day | Thread |
|---|---|---|---|
| 1 | Problem recognition | 0 | New |
| 2 | Raise the stakes | 3 | Reply |
| 3 | Proof, or what the founder is learning | 7 | Reply |
| 4 | New angle and a no-cost offer | 12 | New subject |
| 5 | Breakup | 19 | New subject |

## Rules for every email

- **Voice:** one human to another. Never open with your name, company, or "I'm reaching out". Contractions always.
- **Length:** 50 to 75 words, never over 100.
- **Subject:** lowercase, 3 or 4 words, like an internal memo naming the problem, never the product. No question marks.
- **Ask:** permission, not time. "Worth a quick chat?" Never a calendar link in the first email.
- **Proof:** a confirmed fact in a phrase, or nothing.
- **A way out** in email 1, in the founder's voice, as `SENDING.md` describes.
- No links, attachments or images in emails 1 to 3. The no-cost offer appears in email 4 only.

## Gate, run on every email

Run `keep100:writing-check` with `--format cold-email`. Its script counts the words, scans the banned list, and catches links and leftover placeholders. Add `--template` for the saved sequence, which keeps `{first_name}` as a merge field. Leave it off for emails about to be sent, where every placeholder must be filled. Then check by reading:

- `{first_name}` plus one real detail from that person's row in `pipeline.csv`
- Subject, ask, sign-off and thread placement match the rules
- Every claim traces to a confirmed fact

## Branch C: Daily sending

1. Get today's list from `keep100:prospect-list` (its "Today's queue"): follow-ups due first, then new first emails up to `Daily new emails:` in `progress.md`.
2. For each person, personalize the right email from the saved sequence with their trigger. One at a time. Identical bodies are what spam filters look for.
3. Run the gate. The founder sends from their own mailbox.
4. Write each send date into `sales/pipeline.csv` the same day. Tick "First emails sent" the first time.
5. Hand any reply to `keep100:sales-replies`. A reply ends that person's sequence.

Every Friday, `keep100:prospect-list` reports which lane and trigger got replies. Change the list or the reason for writing before changing the wording. Rewrite one email at a time, so it's clear what made the difference, and note it in `learnings.md`.
