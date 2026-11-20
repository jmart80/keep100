# Evals

27 cases that check the kit keeps its promises: Claude doesn't invent facts, asks before changing founder files, follows the word limits, refuses fake scarcity, and picks the right skill for a plain-language request. Every skill has at least one case that checks it fires.

Each case is a folder: `prompt.md` (what the founder types), `case.yaml` (what a good result looks like, and the example workspace to start from), and `graders/` (the checks). Cases start from the example workspaces in `examples/`.

## Run them

They need [Claude Code](https://code.claude.com/docs/en/plugin-evals) signed in. These are real model runs and they cost money, so they are run by hand and not on every push.

```
# everything, about 27 runs with the plugin and 27 without
claude plugin eval . --scaffold --allow-tools Write Edit Bash

# the six quickest, most important cases
claude plugin eval . --scaffold --allow-tools Write Edit Bash --tag smoke

# one skill, or one case
claude plugin eval . --scaffold --allow-tools Write Edit Bash --tag cold-email
claude plugin eval . --scaffold --allow-tools Write Edit Bash --case dashboard-builds-the-page
```

On Linux, install `bubblewrap` and `socat` first, and point `TMPDIR` at a folder outside `/tmp` (for example `TMPDIR=$HOME/.cache/keep100-evals`). The runner sandboxes shell commands and refuses to run without those two tools, and its sandbox makes everything under `/tmp` read-only, so a case that writes a file fails there.

`--scaffold` lets each case copy an example workspace into its empty run folder. `--allow-tools` lets the run write files, which the dashboard, audit and brief cases need.

Each case runs once by default. Add `--runs 3` before a release, because one run of a model can pass or fail by chance. Add `--ablation none` to skip the no-plugin comparison and halve the cost.

The report shows each case with and without the plugin. A case that scores the same both ways isn't testing the kit, and should be rewritten or removed.

## What gets checked without a model

`python3 scripts/validate.py` checks every case loads: valid settings, at least one grader, a real skill name, and a scaffold script that exists. That runs in CI on every push, along with the script tests in `tests/`.

## Add a case

1. Copy a folder and rename it. The name says what is being tested, in lowercase with hyphens.
2. Write the prompt the way a founder would type it. Don't name the skill.
3. Write the rubric as concrete PASS and FAIL conditions a stranger could apply.
4. Keep `02-skill-fired.md` pointing at the skill that should handle it.
5. Run `python3 scripts/validate.py`, then run the case.

When a founder reports Claude getting something wrong, the fix has two parts: change the skill, and add the case that would have caught it.

## Tags

`smoke` for the short list. `b2b` or `b2c` for the example workspace. The skill name for everything that exercises that skill.
