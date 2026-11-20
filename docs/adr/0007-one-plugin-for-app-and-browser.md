# 7. One plugin for the app and the browser

Date: 2026-11-20
Status: Accepted. Amends [1](0001-desktop-app-plugin-as-primary-path.md).

## Context

Decision 1 assumed the browser could not install plugins, so browser Founders uploaded one zip per skill, built by a release workflow. Claude's documentation now says plugins are added under Customize, then Plugins, in claude.ai as well as the desktop app, that they attach to the account, and that a plugin's skills load in chat on the web, desktop and mobile. Agents and hooks are ignored in chat. Skill scripts are referenced through `${CLAUDE_SKILL_DIR}`, and in chat only a skill's own folder is copied into the sandbox.

This was read from the documentation on 2026-11-20. It has not yet been tested on a Pro account in a browser.

## Decision

One install path: add the marketplace and install the plugin, in the app or at claude.ai. The zip workflow and the per-skill upload steps are removed. The desktop app remains the primary path because only it gives Claude a folder to keep up to date. The browser path keeps the Company model in a Claude Project, updated by hand.

Every skill must work when only its own folder is present: scripts are called through `${CLAUDE_SKILL_DIR}`, and one skill never reads another skill's files. A skill that needs another skill's work invokes that skill by name.

## Consequences

- One set of install instructions, and no release artifact to keep in sync.
- The Kit relies on no hooks or agents, since chat ignores them.
- The kit version is written inside the skills that need it, because a skill cannot read `plugin.json` in chat. `scripts/validate.py` keeps the copies equal.
- If a browser test shows plugins do not install on some plan, this decision is reopened and the browser guide says so plainly.
