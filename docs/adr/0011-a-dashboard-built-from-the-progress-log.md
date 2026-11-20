# 11. A progress dashboard built from the progress log

Date: 2026-11-20
Status: Accepted

## Context

Founders want to see where they are without opening a markdown file or asking. The glossary had listed "dashboard" as a word to avoid for the Weekly brief, because the brief must not become a scorecard. A checklist page is a different thing.

A page that Claude writes by hand each time would look different each time and could show progress that was never recorded. A page with boxes the Founder ticks would be a second copy of the Progress log.

## Decision

The dashboard is one self-contained HTML page with no network requests, filled by a script from `progress.md`, the company file statuses and the Pipeline. It is read-only. Claude ticks a Step in `progress.md` and the dashboard skill rebuilds the page. Every skill that finishes a Step calls it.

The page is saved as `dashboard.html` in the Workspace. Where the Claude app can publish an artifact, the same file is published once and updated in place, with its link kept in the Progress log.

The page shows whatever sections and Steps the Progress log contains, so new Steps need no change to the dashboard.

## Consequences

- The dashboard can never disagree with the Progress log for longer than one skill run.
- The design lives in one template, so every Founder gets the same page.
- Rebuilding after each Step costs one short skill load.
- In the browser, with no folder, the page shows progress as of the chat that built it.
