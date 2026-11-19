---
name: product-emails
description: Writes the emails a Keep100 founder's product sends to turn signups into paying customers - welcome, activation nudges, trial ending, upgrade and win-back. Use when the founder has signups or a trial, or asks about onboarding emails, welcome emails, trial emails, upgrade emails, or why signups aren't paying.
---

# Product emails

Signups who never pay are the most common leak for a new product. These emails fix the leak.

## Inputs

`company/product.md` (how someone starts, what the first "aha" moment is), `company/pricing.md` (trial length, plans, allowed offers), `company/brand.md`, `company/customers.md` (hesitations).

First, ask one question: **what's the one action that shows a new user "gets it"?** (Created their first project, invited a teammate, finished a first workout.) Every email below points at that action. Recommend one from `product.md` if possible.

## The set

| Email | When | Job |
|---|---|---|
| Welcome | Immediately | One sentence of welcome, one clear next step toward the key action. From the founder, personal. |
| Nudge 1 | Day 1, if the key action isn't done | Remove the most likely blocker. One tip or a 30-second video. |
| Nudge 2 | Day 3, if still not done | Show what the after-state looks like, offer help: "reply and I'll set it up with you". |
| Trial ending | 3 days and 1 day before the trial ends (if trial) | What they'll lose, the plan and price from `pricing.md`, one button. |
| Upgrade | When a free user hits a limit or uses it a lot | Tie the paid plan to what they're already doing. |
| Win-back | 14 days after going quiet | Ask why, in one line. Their reply is research. |

## Rules

- From the founder, in first person, plain text or close to it. At this stage a personal note beats a designed newsletter.
- One email, one call to action.
- Under 120 words each.
- Prices and offers only from `pricing.md`. No invented urgency.
- Run `keep100:writing-check`, save to `marketing/<date>-product-emails.md`.

## Sending

If the product sends email through Resend and the connector is connected, offer to help set up these emails there, but never send to real users without the founder's explicit yes. Otherwise, hand over the copy with notes on where each email goes in their tool.
