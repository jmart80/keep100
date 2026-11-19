# 2. One Kit with two Tracks, chosen at setup

Date: 2026-11-19
Status: Accepted

## Context

B2B and B2C Founders need different customer-acquisition playbooks: B2B is led by direct outreach and cold email, B2C by social media and short-form content. Most of the Kit (Claude setup, brand kit, research, competitor analysis, positioning, landing page, pricing, product email) applies to both.

## Decision

Ship one repo and one install. During setup Claude asks whether businesses or individual people pay the Founder, records the Track in the Founder's profile, and steers toward that Track's playbook from then on. The Finish line is the same for both Tracks: first paying customer within a set timeframe.

## Considered alternatives

- Two separate repos: rejected because it splits stars and attention, doubles the README and marketing, and duplicates the shared skills that would drift out of sync.

## Consequences

- Shared skills must work for both Tracks, or branch on the Track in the profile.
- Track-specific skills are installed for everyone; the profile, not the install, decides what Claude suggests.
- A Founder who changes Track only updates their profile.
