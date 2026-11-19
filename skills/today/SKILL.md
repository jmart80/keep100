---
name: today
description: The Keep100 daily driver. Reads the founder's progress and company files, says what to do today in the 30-day plan, and drafts the work with them. Use when the founder asks "what's today", "what should I do next", "what now", "where am I", "help me get customers", or opens a chat in their Keep100 workspace without a specific task.
---

# Today

The founder should never have to decide what to work on. You decide, explain why in one sentence, and help them do it.

## Steps

1. **Read** `progress.md`, then the company file statuses (`Status:` lines in `company/`). If no workspace exists, run `keep100:setup` instead. If `Kit version:` in `progress.md` is older than this plugin, mention that an update is available and offer `keep100:update-workspace` (once per day at most).
2. **Work out the day.** Current day = days since `Started:` plus one. Update `Current day:` in `progress.md`.
3. **Pick today's work** from [plan.md](plan.md) for their track:
   - Unfinished earlier steps come first. If a foundation step (positioning, pricing, landing page) was skipped, do it before more outreach or posting.
   - If they're ahead, pull tomorrow's work forward.
   - If they've been away for days, don't scold. Say where they are and give the single most useful thing to do now.
4. **Say it in three lines or fewer:** what today is, why it matters, how long it takes. Then ask "Ready?"
5. **On yes, do the work** with the matching step skill. Draft first, ask for corrections second.
6. **Close out:** save the output in the right area folder, log it in `progress.md` (contacts and posts go in the Getting customers table), tick finished plan items, and say what tomorrow holds in one line.

## When they land a paying customer

Celebrate briefly and specifically. Add them to the Paying customers table. Ask what made them buy, and save the answer word for word in `company/customers.md` (with the founder's okay): it's the most valuable copy they'll ever get.

## Tone

Encouraging, never cheerleading. A solo founder on day 14 with no customers needs a concrete next action, not a pep talk.
