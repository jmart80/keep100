# 6. The Kit targets paid Claude plans only

Date: 2026-11-19
Status: Accepted

## Context

The Kit relies on plugins, the desktop app working in a local folder, scheduled tasks (Weekly brief) and connectors. Free plans may lack some of these and have tighter usage limits that could cut off the First session midway. Supporting free plans would mean dropping or degrading features.

## Decision

The Kit is built for paid Claude plans only. The README states this on its first screen. No features are cut or degraded to fit the free plan.

## Consequences

- The Kit can rely on scheduled tasks, connectors and longer sessions.
- Some of Jason's audience will need to upgrade before installing; the README must say so before install, not after.
- Testing must happen on paid accounts.
