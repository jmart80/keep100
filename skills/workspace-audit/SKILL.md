---
name: workspace-audit
description: A monthly health check of a Keep100 workspace that reports problems and fixes nothing without a yes. Finds company files that have gone stale, the same price or fact kept in two places, untagged quotes, unconfirmed proof, house rules that have grown too long, and saved work the log missed, then proposes rule changes from what went wrong that month. Use monthly, when the founder asks to audit, tidy, clean up or check their workspace or their Claude setup, asks why Claude keeps getting something wrong, or says Claude quoted an old price or a wrong fact.
---

# Workspace audit

A workspace drifts. Prices change in one file and not another, house rules pile up, and facts confirmed in week one stop being true. This skill finds the drift once a month so the founder doesn't find it in front of a customer.

It reports. It changes nothing until the founder says yes to that change.

## Step 1: Run the check

From the workspace folder:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/audit.py .
```

If scripts can't run here, check the same things by reading the files. The list is in "What it looks for" below.

## Step 2: Report in plain words

Group what it found, most important first, and say what each one risks in a sentence. Skip any group with nothing in it.

| Finding | What it means for the founder |
|---|---|
| DUPLICATE | The same price or list lives in two places. One of them will be wrong after the next change |
| STALE, DRAFT | A company file hasn't been confirmed in over 30 days, or ever. Claude may be stating old facts |
| UNCONFIRMED | Proof that can't be used in anything published until the founder confirms it |
| UNTAGGED | A quote or fact with no tag, so nothing can tell whether it is real |
| PLACEHOLDER | Setup left a blank that Claude reads every session |
| LONG, REPEATED | House rules that have grown. The longer the rules, the more often one gets missed |
| UNLOGGED | Finished work that isn't in the Work log, so the weekly brief can't see it |
| OLD LAYOUT | A file from an earlier kit version. `keep100:update-workspace` moves it |

## Step 3: Fix, one yes at a time

For each finding, propose the smallest fix and ask. For a stale file, show its fact lines and ask "still true?". Then update `Last confirmed:`. For a duplicate, ask which copy is right, keep it in its home file, and remove the other. Never rewrite the founder's own words while fixing.

## Step 4: The monthly retro

A rule earns its place when Claude got something wrong twice. Ask the founder two questions, one at a time:

1. "What did I get wrong more than once this month?"
2. "What did you have to tell me again that I should already have known?"

Read `learnings.md` and the month's Work log for the same pattern. For each repeat, propose one of three things, and say which:

- a new line in the root `CLAUDE.md`, written as a rule with what to do instead
- a new line in one area's `CLAUDE.md`, when it only matters for that kind of work
- a correction to a company file, when the problem was a wrong fact and not a missing rule

Also propose removing any rule that hasn't mattered. Rules get added more easily than they get removed, and a short file is followed more closely.

## Step 5: Record it

Add a Work log line to `progress.md` with the date and how many things were fixed. Note any change to the house rules in `decisions.md`. Run `keep100:dashboard`.

## What it looks for

- Company files with `Status: Draft`, or a `Last confirmed:` date more than 30 days old
- An amount of money that appears in `pricing.md` and also in another company file or `CLAUDE.md`
- Quotes in `customers.md` with no `[verbatim]` or `[paraphrase]` tag
- Entries in `facts.md` with no `[confirmed]` or `[unconfirmed]` tag, and every entry still unconfirmed
- `{{placeholders}}` left in `CLAUDE.md`, `progress.md` or a company file
- A root `CLAUDE.md` over 90 lines, or an area rule that repeats a root rule
- A contact table in `progress.md`, or a `sales/prospects.md` beside `sales/pipeline.csv`
- Dated files in an area folder that the Work log doesn't mention
