---
name: dashboard
description: Builds and refreshes the Keep100 progress dashboard, a checklist page that shows the founder every step of setup and the plan, which are done, what is next, their company file statuses and their numbers. Run it after any change to progress.md, at the end of setup, and whenever the founder asks to see their dashboard, checklist, progress, "where am I", "how far along am I", "what's left" or "show me my plan".
---

# Dashboard

The dashboard is a picture of `progress.md`. It never holds anything the workspace files don't. Claude ticks steps in `progress.md`, this skill redraws the page, and the founder can open it at any time to see where they are.

## Build it

From the workspace folder:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/build.py . 
```

It reads `progress.md`, the `Status:` lines in `company/`, and `sales/pipeline.csv` if it has rows, and writes `dashboard.html` in the workspace. It prints one line: steps done, the next step, and paying customers. If it prints an error, fix what it names in `progress.md`. Never edit `dashboard.html` by hand, and never tick a box in it. The page is rebuilt from `progress.md` every time.

## Show it

1. **If this session can publish or update an artifact** (a saved page the founder can reopen from the Claude app): publish `dashboard.html` as an artifact titled "{Product} progress". Look at the `Dashboard:` line in `progress.md` first. If it holds an artifact link or id, update that same artifact. If it says `dashboard.html`, create the artifact once and write its link on that line. One dashboard, updated in place, never a new one each time.
2. **Otherwise:** tell the founder the page is `dashboard.html` in their Keep100 folder and opens in any browser. Suggest keeping it open in a tab or bookmarking it.

Then say where they are in one line, using what the script printed: "18 of 23 done. Next is your first sales call."

## When to run

- After every change to `progress.md`: a step ticked or skipped, a paying customer added, a week's numbers recorded. The other Keep100 skills call this for you at those points.
- At the setup checkpoint and at the end of setup.
- When the founder asks to see it. Rebuild first so it is never stale.

Don't announce routine refreshes. After a quiet rebuild, mention the dashboard only if the step count changed.

## If scripts can't run here

Run the script's logic by hand: read `references/data-format.md`, write the data as JSON, and put it into a copy of `assets/dashboard.html` in place of the `/*KEEP100_DATA*/` marker. Change nothing else in the template.

## No workspace folder (claude.ai in a browser)

The founder's progress lives in their Keep100 Project. Write the current progress text to a temporary folder as `progress.md`, run the script on that folder, and publish the result as an artifact. Remind them the page shows progress as of this chat.

## What the page shows

- A pie that fills as steps are done, and the next step as the headline
- Paying customers, days since the start, and hours a day
- Every section of the checklist, with done, next, to do and skipped steps
- Outreach numbers from the pipeline (B2B), or last week's row from Weekly numbers
- Each company file and whether it is Confirmed, Provisional or Draft
- Open loops and the six most recent Work log lines

Skipped steps (`- [-]`) don't count toward the total. Sections come straight from `progress.md`, so a step the kit adds later, or one the founder adds, shows up without changing this skill.
