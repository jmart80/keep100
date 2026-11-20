# Example workspaces

Two filled Keep100 workspaces for companies that do not exist. Every name, address and quote in them is made up.

| Folder | Company | Track | Where they are |
|---|---|---|---|
| `b2b/` | Kneecap, scheduling for physiotherapy clinics | B2B | Emails going out, first reply in, no customer yet |
| `b2c/` | Slowmile, a first half marathon training app | B2C | Research done, positioning next |

They are used three ways:

- as a picture of what a workspace looks like part-way through the plan
- as the fixture for the eval cases in `evals/`
- as test data for the scripts (`python3 -m unittest discover tests`)

To see the dashboard for one:

```
python3 skills/dashboard/scripts/build.py examples/b2b --out /tmp/kneecap.html
```
