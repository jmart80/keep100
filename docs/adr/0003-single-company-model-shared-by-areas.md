# 3. One Company model shared by all Areas, never copied

Date: 2026-11-19
Status: Accepted

## Context

Founders want context separated by kind of work (marketing, social, sales) so Claude has the right context for each. The obvious way is one Claude Project per kind of work, each holding its own copy of company information. Copies drift: a Founder updates pricing in one place, forgets another, and Claude states the old price as fact. Drift between copies is the leading cause of confident wrong claims about the Founder's own product.

## Decision

The Kit creates one Workspace folder: a top-level CLAUDE.md with house rules and a map of which file to read for which task; a company/ folder holding the Company model as the single source of truth; and one folder per Area, each with a short CLAUDE.md naming the company files it needs and holding that Area's outputs. Areas reference the Company model and never copy it.

Setup creates the structure, drafts the Company model from material the Founder already has (website, docs, notes, past posts), interviews only for gaps, and has the Founder confirm each file. Only Confirmed facts are treated as true. A short snippet for Claude's account-level instructions points every chat back to the company files.

## Considered alternatives

- One Claude Project per Area, each with its own company files: rejected as the primary design because of drift. Kept only for the browser fallback, with an explicit reminder to re-upload company files when they change.
- One flat context file: rejected because each Area would load context it does not need.

## Consequences

- Every skill must read from the Company model and must not embed company facts in its own instructions.
- Changing a fact means editing one file.
- Browser-only Founders carry the drift risk and must be told so.
