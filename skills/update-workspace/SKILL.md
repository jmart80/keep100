---
name: update-workspace
description: Brings an older Keep100 workspace up to date with a newer kit version, asking before every change. Use when the founder's progress.md shows an older "Kit version" than the installed plugin, or the founder asks to update their Keep100 workspace.
---

# Update workspace

Kit version: 1.1.0

The founder's workspace belongs to them. Updates never change it without a yes.

## Steps

1. Read `Kit version:` in `progress.md`. The installed version is the one above.
2. Read [changes.md](changes.md) for every version after theirs, up to the installed one.
3. Say how many changes there are. Then take them one at a time, in the order listed: read the plain sentence aloud, and ask yes or no.
4. Apply only the approved changes, exactly as the entry's "Do" line says. Never edit, reorder or reformat the founder's own content while doing it. When an entry moves content, show what will move before moving it.
5. Record each declined change under `## Declined` in `progress.md` as `- {id}: {the plain sentence}`, so nobody asks again.
6. Set `Kit version:` in `progress.md` and the version line at the bottom of `CLAUDE.md` to the installed version.
7. Run `keep100:dashboard`.

Skills must keep working if a founder declined an optional change. An entry marked "needed" explains what stops working without it. Say that plainly and still accept a no.
