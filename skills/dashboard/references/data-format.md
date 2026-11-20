# Dashboard data

`scripts/build.py` produces this JSON and puts it in the template. Use this file only when the script can't run.

```json
{
  "product": "Kneecap",
  "founder": "Maya",
  "track": "B2B",
  "kit_version": "1.1.0",
  "started": "2026-11-03",
  "started_text": "3 November 2026",
  "days_in": 18,
  "hours_a_day": "2 hours",
  "steps_done": 18,
  "steps_total": 23,
  "next": { "section": "Getting customers (B2B)", "label": "First sales call" },
  "paying_customers": 0,
  "sections": [
    { "title": "Setup", "items": [ { "label": "Workspace created", "state": "done", "note": "" } ] }
  ],
  "company": [ { "name": "Product", "status": "Confirmed", "last_confirmed": "2026-11-03" } ],
  "numbers": { "week_of": "2026-11-09", "reached": "18", "replies": "2", "calls": "0", "paid": "0" },
  "pipeline": { "reached": 5, "replies": 3, "calls": 0, "paid": 0, "waiting": 2 },
  "open_loops": ["2026-11-18 Priya asked for two call times."],
  "work_log": ["2026-11-18 Replied to Priya with two call times (sales/pipeline.csv)"],
  "updated_text": "20 November 2026, 16:07"
}
```

## Rules

- `sections`: every `## ` section of `progress.md` that contains checkbox lines, in file order. `state` is `done` for `- [x]`, `todo` for `- [ ]`, `skipped` for `- [-]`. For a skipped step, `note` is the text in brackets after the label.
- `steps_total` counts done and to-do steps. Skipped steps are left out.
- `next` is the first to-do step from the top, or `null` when none is left.
- `paying_customers` is the number of rows in the Paying customers table.
- `numbers` is the last row of the Weekly numbers table, or `null`.
- `pipeline` is counted from `sales/pipeline.csv`, or `null` when the file is missing or has no rows. `reached` is rows with `sent_1`. `replies` is rows with `replied`, leaving out auto-replies. `calls` is rows with status `call_booked` or `won`. `paid` is rows with status `won`. `waiting` is queued rows graded A or B.
- `company` lists every file in `company/` except `facts.md`, with its `Status:` line.
- `work_log` is the first six bullet lines under Work log. `open_loops` is every bullet line under Open loops.
- Use `null` for `numbers`, `pipeline` and `next` when there is nothing to show. Never invent a value.
