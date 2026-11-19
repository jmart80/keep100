---
name: cold-email
description: B2B outreach for Keep100 founders - building a list of the right prospects and writing cold email sequences that earn replies instead of pitching. Use on the B2B track from day 6, or when the founder wants to find prospects, write a cold email or follow-up sequence, improve reply rates, or audit an outreach email.
---

# Cold email

Adapted from the cold-email-sequence skill by Keep100's author. A cold email opens a conversation; it doesn't pitch, close or inform. Every rule serves **relevance**: the prospect's world first, the product second. A sequence is one story told across five emails, never the same pitch five times.

## Inputs

Everything comes from the company files; never assume anything about the product.

| What the emails need | Where it comes from |
|---|---|
| What it is, what the prospect would call it | `company/product.md`, `company/positioning.md` (category) |
| Who to write to | `company/positioning.md` (beachhead, champion), `company/customers.md` |
| The problem, why now, cost of doing nothing | `company/customers.md` quotes, `company/positioning.md` |
| A second angle for email 4 | A different pain, person or use case from `customers.md`. Must not be the same problem reworded |
| Proof | `[confirmed]` facts only. None is fine: then no metric |
| Credibility marker for email 3 | `[confirmed]` facts (founder background, certification, notable customer). Optional |
| No-cost offer for email 4 | Agree one with the founder: an audit, teardown, sample or setup help |
| Sender name | The founder |

If a needed input is missing, ask for it. Don't draft around a gap.

## Branch A: Build the prospect list (day 6)

1. Turn the beachhead into a search: role, company type, size, and a **trigger** (a real reason to write now: hiring for a role, a new launch, a funding round, a tool change, a post they wrote).
2. Find 30 to 50 named people at named companies, with sources, using web search or Exa. Note one real trigger for each. No trigger, no email.
3. Save to `sales/prospects.md` as a table: name, role, company, link, trigger, status.
4. Finding emails: suggest they use the company website, LinkedIn, or an email-finder tool they trust. Don't guess addresses.

## Branch B: Write the sequence

1. Read [BANNED.md](BANNED.md) before writing a word.
2. Read [TEMPLATES.md](TEMPLATES.md) for the emails in scope.
3. Draft. Each email personalized with `{first_name}` plus the prospect's trigger or company.
4. Run the gate below on every email, then `keep100:writing-check`.
5. Save to `sales/<date>-sequence.md`.

| Email | Role | Day | Thread |
|---|---|---|---|
| 1 | Problem recognition | 0 | New |
| 2 | Raise the stakes | 3 | Reply |
| 3 | Social proof | 7 | Reply |
| 4 | New angle + no-cost offer | 12 | New subject |
| 5 | Breakup | 19 | New subject |

## Rules for every email

- **Voice:** one human to another. Never open with your name, company, or "I'm reaching out". Contractions always.
- **Length:** 50 to 75 words, never over 100.
- **Subject:** lowercase, 3 or 4 words, like an internal memo naming the problem, never the product. No question marks.
- **Ask:** permission, not time. "Worth a quick chat?" Never a calendar link in the first email.
- **Proof:** a confirmed metric in a phrase, or nothing.
- No links, attachments or images in emails 1 to 3. Credibility marker in email 3 only. No-cost offer in email 4 only.

## Gate (every email, actually checked)

- Word count counted: under 75, never over 100
- Banned list scanned term by term
- `{first_name}` plus at least one real personal detail
- Subject, ask, sign-off and thread placement match the rules
- Every claim traces to a confirmed fact

## Branch C: Daily sending (days 8 to 30)

Each day: list who's due a follow-up from `progress.md`, draft 10 new first emails from `sales/prospects.md`, and draft replies to any responses. The founder sends from their own email. Log every send and reply in `progress.md`. Weekly, look at which subject lines and angles got replies and adjust.

When someone replies with interest, offer `keep100:pressure-test` to prepare the call.
