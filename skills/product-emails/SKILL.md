---
name: product-emails
description: Writes the emails a Keep100 founder's product sends to turn signups into paying customers - welcome, activation nudges, trial ending, upgrade and win-back - and a by-hand version for founders whose product can't send them automatically yet. Use when the founder has signups or a trial, or asks about onboarding emails, welcome emails, trial emails, upgrade emails, or what to send new users.
---

# Product emails

Emails remind people to come back. They can't fix a first session that never reached the point of the product. If the founder says signups aren't paying and `keep100:activation` hasn't been run, recommend running it first.

## Inputs

`company/product.md` (Key action, How the product sends email, how someone starts), `company/pricing.md` (trial length, plans, the founding offer, allowed discounts), `company/brand.md`, `company/customers.md` (hesitations), `learnings.md`.

## Two questions first

1. **The key action.** Read "Key action" in `product.md`. If it's empty, ask: "What's the first thing a new user does that shows it works for them?" Recommend one. Save it with their yes. Every email below points at that action.
2. **How email gets sent.** Read "How the product sends email". If it's empty, ask. The answer picks the version:
   - **A tool that sends on triggers** (the product or an email tool can send when someone signs up or goes quiet): write the full set.
   - **By hand, or nothing yet:** write the by-hand version. With fewer than about twenty signups it works better anyway.

## The full set

| Email | When | Job |
|---|---|---|
| Welcome | Immediately | One sentence of welcome, one clear next step toward the key action. From the founder, personal. |
| Nudge 1 | A day later, if the key action isn't done | Remove the most likely blocker. One tip or a 30-second video. |
| Nudge 2 | A few days in, if still not done | Show what the after-state looks like, offer help: "reply and I'll set it up with you". |
| Trial ending | A few days before, and the day before, the trial ends | What they'll lose, the plan and price from `pricing.md`, one button. The founding offer, if it is recorded and open. |
| Upgrade | When a free user hits a limit or uses it a lot | Tie the paid plan to what they're already doing. |
| Win-back | About two weeks after going quiet | Ask why, in one line. Their reply is research. |

The timings are starting points. Set them from how long the key action takes.

## The by-hand version

Three short notes the founder sends personally from their own mailbox:

1. **Within a day of signup:** thanks, one question ("what were you hoping it would do?"), and an offer to set it up with them on a 15-minute call.
2. **Three days later, if they haven't done the key action:** the one thing that usually blocks people, and the offer again.
3. **Before the trial ends:** what happens next, the price from `pricing.md`, and the link.

Give the founder a simple way to know who is due: their user list, checked each morning. Replies and calls go to `keep100:customer-conversations`.

## Rules

- From the founder, in first person, plain text or close to it. At this stage a personal note beats a designed newsletter.
- Every email has a subject line: plain, lowercase or sentence case, under 6 words, about them and not the product.
- One email, one call to action.
- Under 120 words each.
- Prices and offers only from `pricing.md`. No invented urgency.
- Anything that isn't a receipt or account notice is marketing email. It needs a working way to unsubscribe, and many countries require the sender's postal address. Have the founder check the rules for where their users are.
- Run `keep100:writing-check` with `--format product-email`. Save to `marketing/<date>-product-emails.md`, each email under its own `## ` heading.

## Sending

If the product sends email through Resend and the connector is connected, offer to help set these up there, but never send to real users without the founder's explicit yes. Otherwise, hand over the copy with notes on where each email goes in their tool.

Tick "Product emails" in `progress.md`, add a Work log line, and run `keep100:dashboard`.
