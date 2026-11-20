---
name: sales-replies
description: Turns a reply into a paying customer for a Keep100 founder. Sorts each reply to outreach, drafts the answer, books the call, writes a one-page call plan, drafts the follow-up, and records the result. Covers objections, "send me more info", "not now", opt-outs, the first sales call, asking for the sale and what to do after a yes or a no. Use whenever someone replies to a cold email or message, asks about price or buying, a call or demo is coming up, the founder says "they replied", "what do I say back", "how do I close this", "they went quiet", "how do I ask for the money", or wants help with a sales call.
---

# Sales replies

Adapted from the reply-handling reference of the cold-email skill and parts of the sales-enablement skill in coreyhaines31/marketingskills (MIT).

A reply is the scarcest thing a new founder gets. It is easy to lose one to a slow answer, a long answer, or a call with no ask at the end. The founder sends everything. Claude drafts and keeps the record.

## Rules

- **Any reply ends the sequence.** Update `sales/pipeline.csv` before drafting anything, so no automated follow-up reaches someone who already answered.
- **An opt-out is final.** Set `status` to `stopped`, never contact them again, and keep the row so they are never re-added. If a reply is angry, the founder may send one short apology or nothing.
- **Answer the same day.** A founder's advantage over a company is speed and a real person. Draft first, polish second.
- **Short.** A reply to a reply is under 60 words unless they asked a question that needs more.
- **Claims come from confirmed facts.** Prices, discounts and offers come only from `company/pricing.md`. If they ask for something the files do not answer, the draft says the founder will find out, and Claude asks the founder.
- **One objection, one answer.** Reply to an objection once, briefly, and make it easy to say no. Arguing loses the person and the next one they talk to.

## Inputs

The reply itself, the thread before it, the prospect's row in `sales/pipeline.csv`, `company/pricing.md`, `company/positioning.md`, `company/customers.md` (hesitations), `company/facts.md`.

## Branch A: Sort the reply and answer it

1. Classify it. When a reply fits two rows, use the one nearer the top.

| Type | Looks like | Do |
|---|---|---|
| Opt-out | "Remove me", "stop", hostility | Mark `stopped`. No reply, or one line of apology |
| Positive | "Sure", "tell me more", "send times" | Branch B |
| Question | "What does it cost?", "does it work with X?" | Answer exactly that in one or two sentences, then offer a call |
| Objection | "We use X", "no budget", "not a priority" | One answer from `references/objections.md`, then step back |
| Not now | "Try me next quarter" | Thank them, set `status` to `not_now` and `next_date` to the time they named |
| Referral | "Talk to Sam" | Thank them. Add Sam as a new row with this referral as the trigger. Ask before using the referrer's name if it is unclear |
| Wrong person | "Not my area" | Ask once who owns it |
| Auto-reply | Out of office | Pause. Set `next_date` to two days after their return |

2. Update the row: `replied`, `reply_type`, `status`, `next_step`, `next_date`. Tick "First reply" in `progress.md` the first time a real person replies.
3. Draft the answer. Run `keep100:writing-check`. Show it with one line saying what type you read it as, so the founder can correct the reading.

## Branch B: Book the call

1. Offer two specific times in their time zone, plus a booking link only if the founder has one. Two times get a faster yes than a link alone.
2. Once they pick, the founder sends the invite with a one-line agenda. Set `status` to `call_booked`. Tick "First sales call" in `progress.md` after the first call happens.
3. The day before, draft a short confirmation with one useful thing in it, such as the one question the founder most wants to ask.
4. If they miss the call, draft one warm reschedule note the same day. After a second miss, set `not_now` and move on.

## Branch C: The call plan

One page, saved to `sales/<date>-call-<company>.md`. A first call has three jobs: learn their situation, decide if they fit, and ask for a next step.

```
# Call with {name}, {role} at {company}
Why they replied: {their words}
What we know: {trigger, source, anything from the thread}
What we don't know: {the two or three gaps that decide fit}

## Open (2 minutes)
{One sentence on why you wrote to them. Then: "Before I show you anything, can I ask how you handle {problem} today?"}

## Questions (10 minutes)
{Five questions about what they did, not what they think. Ask keep100:customer-conversations for its question bank.}

## Show one thing (5 minutes)
{The single capability that answers what they just described. Not a tour.}

## Price
{Plan and price exactly as in company/pricing.md. The founding offer, if one is recorded and still open.}

## The ask
{One sentence, said out loud, then silence. For example: "Would you like to start with the founding plan this week?"}

## If they hesitate
{The two most likely hesitations from company/customers.md, each with a one-line answer from confirmed facts.}

## Next step if it's a no for now
{The smallest real commitment: a pilot, a second call with the other decision maker, an introduction.}
```

Rehearse if the founder wants: play the prospect, one exchange at a time, and stay in character until the founder asks for the sale.

## Branch D: After the call

1. Ask the founder three things: what they said in their own words, what the next step is and its date, and what nearly stopped them.
2. Draft the follow-up, to send the same day: two lines recapping their situation in their words, the agreed next step with its date, and the payment or signup link if they said yes.
3. Update the row. A call is also a customer conversation, so hand the notes or transcript to `keep100:customer-conversations` to file the quotes.

## Branch E: Won, lost or quiet

- **Won.** Set `status` to `won`. Add them to Paying customers in `progress.md`, tick "First paying customer" if it's the first, and run `keep100:dashboard`. If they took a founding place, update the count in `company/pricing.md`. Ask "what made you say yes?" and save the answer word for word, with permission, through `keep100:customer-conversations`. Ask if they would be willing to be named. Only then may a name go into `company/facts.md`.
- **Lost.** Set `status` to `lost`. Ask once, kindly, what decided it. Record the reason in `learnings.md` under Outreach and sales. Three losses for the same reason go to `keep100:pressure-test`.
- **Quiet after interest.** One nudge after three working days that adds something new, such as an answer to a question they raised. A second after a week that makes it easy to say no, such as "should I close this out?" Then set `not_now` with a date two months out.

## When the buyer is a consumer

Most of this applies to anyone who writes in asking about buying. Skip the call. Answer the question, link the page or the checkout, and offer help getting started. Public comments are handled by `keep100:social-content`.
