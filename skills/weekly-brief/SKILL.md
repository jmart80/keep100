---
name: weekly-brief
description: Writes the Keep100 weekly brief - where the founder is in the plan, last week's one line of numbers, and three specific growth ideas to draft this week. Use when run by the Monday scheduled task, or when the founder asks for their weekly brief, a weekly check-in, or "what should I focus on this week".
---

# Weekly brief

A short Monday message about **next actions**. One line of numbers, no charts, no scorecard. In the first month numbers are small, and the line exists so the founder can see which stage is losing people.

## Before writing anything

Read `progress.md`. If you cannot read it (no workspace folder in this session, or the file is missing), stop. Say that the brief needs the Keep100 folder, and that the scheduled task must have the folder attached and the computer awake with the Claude app open. Write no brief. A brief built without the files would be invented.

## Steps

1. Read `progress.md`, the `Status:` and `Last confirmed:` lines of every file in `company/`, `learnings.md`, and the latest row of Weekly numbers.
2. Write the brief, under 200 words:

```
# Week of {date}

## Where you are
{Step {done} of {total}. One or two sentences: what's done, what's next.}
{If Setup or a Foundation step is unticked: name it as the first thing to do this week, with how long it takes.}
{Last week: {the Weekly numbers row in words, e.g. "42 people reached, 3 replies, 1 call, 0 paid"}. {One clause on which stage to work on.}}

## Three things to draft this week
1. {Specific idea, e.g. "A LinkedIn post about {verbatim struggle from customers.md}"}
2. {e.g. "A blog post answering '{question a prospect asked}'"}
3. {e.g. "Replies to the 2 people who asked to hear back this month"}

{Only if true: "{file} was last confirmed on {date}. Worth a two-minute check."}

Reply with a number and I'll draft it.
```

3. Ideas must be specific to their company: built from customer quotes, competitor gaps in `research/`, what `learnings.md` says worked, open loops, or their track's playbook. Never generic advice like "post consistently".
4. Until "First paying customer" is ticked, ideas favour their track's customer-getting work. Once the Slow-burn steps are next, include one content idea.
5. Leave the numbers line out when there is no Weekly numbers row yet. Mention a company file only when its `Last confirmed:` date is more than 30 days old.
6. Save to `briefs/{date}.md`.
