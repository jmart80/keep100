# Evals

33 cases that check Keep100 does what it says. The latest results are in [RESULTS.md](RESULTS.md).

There are two kinds of case:

- **Jobs** (15) are pieces of work a founder asks for: build my workspace, who do I email today, record my first customer. The checks look at the reply, the files saved and the records updated. Jobs are where the skills have to beat Claude without them.
- **Guards** (18) are promises the kit must never break: no invented quotes, no guessed email addresses, no fake scarcity. Claude usually keeps these without the skills too. They are here to catch a change that breaks one.

Each case is a folder: `prompt.md` (what the founder types), `case.yaml` (what a good result looks like, and the example workspace to start from), and `graders/` (the checks). Cases start from the example workspaces in `examples/`. `scripts/eval_scaffold.py` copies one in and moves its dates forward, so the example is always "as of today".

## Run them

They need [Claude Code](https://code.claude.com/docs/en/plugin-evals) signed in, or an `ANTHROPIC_API_KEY`. These are real model runs and they cost money, so they are run by hand and not on every push. A full run with three tries per case cost about $45 in November 2026.

```
# everything, with the plugin and without it
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet

# the six quickest, most important cases
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet --tag smoke

# only the jobs, only one skill, or only one case
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet --tag job
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet --tag cold-email
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet --case dashboard-builds-the-page
```

On Linux, install `bubblewrap` and `socat` first, and point `TMPDIR` at a folder outside `/tmp` (for example `TMPDIR=$HOME/.cache/keep100-evals`). The runner sandboxes shell commands and refuses to run without those two tools, and its sandbox makes everything under `/tmp` read-only, so a case that writes a file fails there.

`--scaffold` lets each case copy an example workspace into its empty run folder. `--allow-tools` lets the run write files. `--judge-model sonnet` uses a steadier judge than the default. The small default judge failed correct replies on wording.

Each case runs once unless you add `--runs 3`. Use three before a release, because one run of a model can pass or fail by chance. Add `--ablation none` to skip the no-plugin comparison and halve the cost.

On GitHub, start the "Evals" workflow from the Actions tab. It needs a repository secret named `ANTHROPIC_API_KEY`.

## Three comparisons

The report shows each case **with the skills** and **without the skills**. Without means the plugin is removed and the workspace stays, house rules included. That gap is what the skills add.

The third comparison is **plain Claude**: the same company files with every `CLAUDE.md` removed and no plugin. To run it, create an empty file named `evals/.plain`, run the suite, and delete the file. The no-plugin column of that run is plain Claude.

```
touch evals/.plain
claude plugin eval . --scaffold --allow-tools Write Edit Bash --judge-model sonnet --runs 1 --json plain.json
rm evals/.plain
```

## Write the results page

```
python3 scripts/eval_report.py results.json --plain plain.json --out evals/RESULTS.md
```

Several result files can be given. Runs of the same case are pooled.

## What gets checked without a model

`python3 scripts/validate.py` checks every case loads: valid settings, at least one grader, a real skill name, and a scaffold script that exists. That runs in CI on every push, along with the script tests in `tests/`.

## Add a case

1. Copy a folder and rename it. The name says what is being tested, in lowercase with hyphens.
2. Write the prompt the way a founder would type it. Don't name the skill.
3. Tag it `job` or `guard` in `prompt.md`.
4. For a job, check what was produced. A `regex` grader with `target: { source: file, path: ... }` reads a saved file the same way every time. Keep `llm` graders for short replies, with concrete PASS and FAIL conditions a stranger could apply.
5. Keep `02-skill-fired.md` pointing at the skill that should handle it. List a second skill when either could rightly take the request.
6. Run `python3 scripts/validate.py`, then run the case with and without the plugin. A job that scores the same both ways is not testing the skill.

When a founder reports Claude getting something wrong, the fix has two parts: change the skill, and add the case that would have caught it.

## Tags

`job` or `guard`. `smoke` for the short list. `b2b` or `b2c` for the example workspace. The skill name for everything that exercises that skill.
