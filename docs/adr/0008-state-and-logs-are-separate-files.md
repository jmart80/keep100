# 8. State and logs are separate files, and contacts have one home

Date: 2026-11-20
Status: Accepted

## Context

`progress.md` held the plan, a table of every contact and post, paying customers and the work log. It is read at the start of every session, so it grew with every email sent. Contacts were also listed in `sales/prospects.md`, which broke the Kit's own rule against two copies. Follow-up dates were worked out by reading a markdown table, which fails quietly as the table grows.

## Decision

`progress.md` holds state: the checklist of Steps, open loops, paying customers, one row of numbers a week and the work log. Everything that grows without limit moves out. Contacts live only in `sales/pipeline.csv`, one row per person, in a fixed format. Posts live in `social/posted.csv`. What worked lives in `learnings.md`. Decisions live in `decisions.md`.

A script in the prospect list skill validates the pipeline, prints who is due today and reports the funnel. Claude does not work out follow-up dates by reading.

Progress is counted in Steps done. Calendar days are shown for information and never decide what the Founder should be doing.

## Consequences

- The file Claude reads most stays small.
- A Founder who takes a week off returns to the Step they left.
- The pipeline format is an interface. Changing a column changes the script, the template, the example and the format reference together, and validation fails if they disagree.
- Workspaces created at 1.0.0 need migrating. `update-workspace` does it with a yes for each change.
