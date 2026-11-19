# 4. Ship adapted copies of every skill, including third-party ones

Date: 2026-11-19
Status: Accepted

## Context

The Kit draws on Jason's own skills (competitive analysis, positioning, landing page, cold email) and other people's (UI/UX Pro Max, grill-me, unslop). As written, Jason's skills each collect their own intake, one hands research off to Perplexity, and the landing page skill is B2B only. Third-party skills know nothing of the Company model. Linking to third-party repos would make Founders install pieces separately.

## Decision

The Kit ships its own adapted version of every skill. Each reads the Company model, asks only about gaps, and respects the Founder's Track. Research runs through Exa inside Claude, with Perplexity as an optional "go deeper" step. Third-party skills are copied only under a license that allows it (MIT, CC-BY and similar), with the author credited in the skill file and in a README CREDITS section, and the copied version pinned. Jason's personal skills are left unchanged.

## Consequences

- The one-URL install holds: nothing is installed from elsewhere.
- The Kit owns maintenance of its forks; upstream improvements must be pulled in by hand.
- Each license must be verified before copying. A skill with unknown provenance (Jason's unslop) is matched to a known source or rewritten.
