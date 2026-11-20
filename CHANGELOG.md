# Changelog

What changed in the kit, newest first. For the changes a founder's workspace needs, see `skills/update-workspace/changes.md`.

## 1.1.0 (2026-11-20)

### Measured

- All eval cases ran for the first time. Results are in `evals/RESULTS.md`: jobs pass 48 of 49 runs with the skills and 8 of 49 without them.
- 33 eval cases, up from 27, split into jobs and guards. Job cases check the files and records a skill leaves behind, not only the reply.
- `scripts/eval_scaffold.py` keeps the example workspaces "as of today" for every run. `scripts/eval_report.py` writes the results page.

### Fixed after the first eval runs

- `pressure-test` and `pricing` ask one question per message.
- `setup` writes "unknown" for anything the founder did not say, never "none", and labels the daily email number as the kit's default.
- `weekly-brief` counts steps the way the dashboard does.
- `content-seo` and `offer` now load for the plain questions founders ask about blogs and scarcity lines.
- The Evals workflow installs the sandbox tools it needs and uses a steadier judge.

### New

- **Progress dashboard** (`dashboard`): a checklist page built from `progress.md` and rebuilt whenever a step is finished.
- Seven skills: `customer-conversations`, `prospect-list`, `sales-replies`, `offer`, `launch`, `activation` and `workspace-audit`. The first six are adapted from Corey Haines' marketingskills (MIT).
- `cold-email/SENDING.md`: sending setup, opt-outs and when to stop.
- Scripts inside the skills: the pipeline checker and daily queue, the writing check, the dashboard builder and the workspace audit.
- Validation on every push (`scripts/validate.py`, `tests/`), eval cases (`evals/`), and two example workspaces (`examples/`).
- The company model contract (`docs/contract.json`, and the table in `docs/CONTEXT.md`).

### Changed

- **Install:** one plugin for the desktop app and claude.ai. The per-skill zip route is gone (decision 7).
- **Progress is counted in steps, not days.** `progress.md` is a checklist. A founder who takes a week off returns to the step they left.
- **Contacts live in `sales/pipeline.csv` only.** `progress.md` no longer holds them (decision 8).
- **One home per fact.** Prices live in `pricing.md` only. `facts.md` holds proof with no other home. A claim is allowed when its company file is Confirmed or its entry is `[confirmed]`.
- **Quotes are tagged** verbatim or paraphrase, and by whose customer spoke.
- **One banned list**, in `writing-check`, with per-founder exceptions in `brand.md`.
- **Positioning** rewritten for a founder with no customers. Four reference files match four phases, and the skill writes every field other skills read.
- **Cold email** now only writes. List building moved to `prospect-list`, replies to `sales-replies`. Email 3 has a version for founders with no proof.
- **Weekly brief** stops when it can't read the workspace, and carries one line of numbers (decision 9).
- **Setup** shows every fact before confirming it, asks how a customer pays and how many hours a day the founder has, attaches the folder to the scheduled brief, and can be split across two sittings.
- Script paths use `${CLAUDE_SKILL_DIR}`. No skill reads another skill's files.
- The bundled design skill's description is narrowed so it loads for the founder's own pages only.

### Fixed

- A find-and-replace leftover in the landing page FAQ rules.
- The trust strip template no longer prescribes star ratings.
- Landing page FAQ and rubric now cover B2C.
- `company/positioning.md` now has the fields cold email and the landing page read.
- Statistics with no source were removed from the positioning references.
- Credits now name every practitioner the positioning skill draws on.
- The plugin manifest folder holds only manifests.

### Removed

- `.github/workflows/release-skill-zips.yml`, `cold-email/BANNED.md`, `positioning/references/packet-template.md`.

## 1.0.0 (2026-11-19)

First release.
