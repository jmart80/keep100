# 10. Mechanical checks are scripts, and promises are eval cases

Date: 2026-11-20
Status: Accepted

## Context

Skills asked Claude to count words, scan banned lists and check for leftover placeholders, and to say it had "actually checked". A model asked to count words estimates. Three banned lists in three skills had drifted apart. Nothing tested whether the skills did what the README promises, and nothing caught a skill reading a field that no template contained.

## Decision

Anything a program can check is checked by a program shipped inside the skill that owns it: the writing check script (word limits, the one banned list, placeholders, links in early emails, matching buttons), the pipeline script, the dashboard builder and the workspace audit. Skills say what to do when scripts cannot run.

The Kit's interface is written down as a contract (`docs/contract.json` and the table in the glossary). `scripts/validate.py` checks on every push that templates, examples, skills, versions and eval cases agree, and that every Step is ticked by some skill.

The Kit's promises are eval cases in `evals/`, run against two example workspaces with `claude plugin eval`. Each skill has a case that checks it fires. Evals cost money, so they run by hand and before a release.

## Consequences

- Skills depend on Python being available where they run. Each has a by-hand fallback.
- A change that breaks the contract fails CI before a Founder sees it.
- A bug report is closed by a fix and by the eval case that would have caught it.
- Eval scores from a single run are noisy. Releases use three runs per case.
