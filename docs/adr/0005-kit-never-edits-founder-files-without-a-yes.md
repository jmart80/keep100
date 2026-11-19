# 5. Updates never change Founder-owned files without a yes

Date: 2026-11-19
Status: Accepted

## Context

Plugin updates reach Founders automatically. The Workspace holds the Founder's Company model, Progress log and saved work. New Kit versions will sometimes change the Workspace design (a new Company model file, a new house rule). Silently migrating would risk overwriting the Founder's work; never migrating would leave older Workspaces behind.

## Decision

Split files into Kit-owned (skills, guides, templates: update freely) and Founder-owned (everything in the Workspace: never edited automatically). Each Workspace records the Kit version that created or last updated it. When a newer Kit needs a Workspace change, Claude explains it in one line the next time the Founder opens the Workspace and applies it only on a yes.

## Consequences

- Founders can trust that their files are safe across updates.
- Every Workspace design change needs a written migration step and a one-line explanation.
- Founders who decline stay on an older Workspace layout, so skills must tolerate missing optional files.
