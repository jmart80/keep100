# Contributing

Keep100 is a kit for founders who can't check our work, so the bar for a change is that it can be checked by something other than hope.

## Before you open a pull request

```
python3 scripts/validate.py
python3 -m unittest discover tests
```

Both must pass. They run on every push.

## The rules a change has to follow

1. **Disagree with a decision by writing one.** The decisions are in `docs/adr/`. If your change goes against one, add a new decision record that says why, and link it from the one it amends.
2. **The contract is the interface.** If a skill reads or writes a new field, add it to `docs/contract.json`, the table in `docs/CONTEXT.md`, the templates in `skills/setup/workspace/`, both example workspaces, and `skills/update-workspace/changes.md`. Validation fails until they agree.
3. **Each fact has one home.** Don't add a second place for a price, a list or a rule.
4. **A skill works alone.** It may run scripts in its own folder through `${CLAUDE_SKILL_DIR}`. It never reads another skill's files. It calls the other skill by name.
5. **If a program can check it, a program checks it.** Don't ask Claude to count.
6. **No number without a source.** Benchmarks, typical rates and "studies show" stay out of skills unless the source is linked beside them.
7. **A fix comes with the case that would have caught it.** Add an eval case in `evals/` or a test in `tests/`.
8. **Founder files are theirs.** Any change to an existing workspace goes through `changes.md` and a yes.
9. **Credit what you adapt.** Name the source at the top of the skill and in `CREDITS.md`, and check its license allows it.

## Writing style for skills

Plain words. Short sentences. Say why a rule exists, so Claude can apply it to cases the rule didn't name. No em dashes: the kit's own writing check bans them, and validation enforces it.

## Running the evals

See `evals/README.md`. They are real model runs and cost money, so run the `smoke` tag while you work and everything before a release.

## Releasing

1. Bump the version in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`, and the `Kit version:` line in the skills validation names.
2. Add the version to `CHANGELOG.md` and to `skills/update-workspace/changes.md`.
3. Run the full eval suite with `--runs 3`.
4. Tag the commit.
