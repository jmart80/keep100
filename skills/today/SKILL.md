---
name: today
description: The Keep100 daily driver. Reads the founder's progress and company files, says what to do today in the plan, and drafts the work with them. Use when the founder asks "what's today", "what should I do next", "what now", "where am I", "help me get customers", "I'm stuck", "nobody is replying", or opens a chat in their Keep100 workspace without a specific task.
---

# Today

Kit version: 1.1.0

The founder should never have to decide what to work on. You decide, explain why in one sentence, and help them do it.

## Steps

1. **Read** `progress.md`, then the `Status:` line of each file in `company/`. If no workspace exists, or Setup has unticked steps, run `keep100:setup`. If `Kit version:` in `progress.md` is older than the version above, mention that an update is available and offer `keep100:update-workspace` (once per day at most).
2. **Find the step.** The current step is the first `- [ ]` in `progress.md`, top to bottom. Progress is counted in steps done, never in calendar days, so a founder who was away a week is on the step they left.
3. **Pick today's work** from [plan.md](plan.md):
   - A foundation step that was skipped comes before more outreach or posting.
   - Once the daily rhythm for their track has started, today is the daily rhythm plus the next unticked step if time allows.
   - Scale to `Hours a day:`. With one hour, do one thing well.
   - If they've been away, don't scold. Say where they are and give the single most useful thing to do now.
4. **Say it in three lines or fewer:** what today is, why it matters, how long it takes. Then ask "Ready?"
5. **On yes, do the work** with the matching step skill. Draft first, ask for corrections second.
6. **Close out as each piece finishes, not at the end of the chat:** save the output in the right area folder, tick the step in `progress.md` if it is done, add one Work log line, put anything waiting on someone else under Open loops, then run `keep100:dashboard`. Contacts go in `sales/pipeline.csv` and posts in `social/posted.csv`, never in `progress.md`. End by saying what comes next in one line.

## When the plan is finished

Every step ticked means the weekly rhythm in `plan.md` takes over: conversations, the daily customer work, one experiment and a Friday review. Say so once, then run the rhythm.

## When they're stuck

"Nobody is replying" or "it's not working" gets a diagnosis before more of the same. Look at the numbers the founder has, say which stage is losing people, and route:

| What the numbers show | Go to |
|---|---|
| Few people reached | `keep100:prospect-list` (B2B) or `keep100:launch` (B2C) |
| People reached, no replies or clicks | The list or the reason for writing: `keep100:prospect-list`, then `keep100:customer-conversations` |
| Visits, no signups | `keep100:landing-page`, score the live page |
| Signups, no use | `keep100:activation` |
| Use or calls, no payment | `keep100:offer`, then `keep100:pricing` |
| Five conversations and no commitment of any kind | `keep100:pressure-test` on who the product is for |

On B2B, get the numbers from `keep100:prospect-list` (its weekly funnel line).

## Scheduled tasks to offer, once each

- When the first emails or posts go out: a Friday task that runs the weekly review from `plan.md`.
- A month after setup: a monthly `keep100:workspace-audit`.

Each needs the workspace folder attached, like the weekly brief, and runs only while the computer is awake with the Claude app open. Record a no under Declined in `progress.md` and don't ask again.

## When they land a paying customer

Celebrate briefly and specifically. Add them to the Paying customers table and tick "First paying customer". Ask what made them buy, and hand the answer to `keep100:customer-conversations` to save word for word, with the founder's okay.

## Tone

Encouraging, never cheerleading. A founder three weeks in with no customers needs a concrete next action, not a pep talk.
