# 1. Claude desktop app plugin is the primary install path

Date: 2026-11-19
Status: Amended by [7](0007-one-plugin-for-app-and-browser.md). The browser can now install plugins, so the zip route described here is gone.

## Context

The Kit's promise is that a Founder gives Claude one URL and everything gets set up. Founders have no technical background. Claude can be used in the browser (claude.ai), the desktop app, or Claude Code (terminal).

In the browser, Claude cannot install skills or connectors from a URL; each skill is uploaded as a zip and each connector added by hand in Settings. In the desktop app and Claude Code, a GitHub repo can be a plugin that installs skills and connector setup in one step and receives updates when the repo changes.

## Decision

Package the repo as a plugin and target the Claude desktop app as the primary path. Provide a short browser fallback guide for manual setup. Do not treat Claude Code as a target audience path.

## Consequences

- The one-URL promise holds for desktop users, and updates reach them automatically.
- Browser-only Founders get a worse, manual experience; the fallback must be kept in sync with the plugin contents.
- The repo structure must follow the plugin format, which constrains layout.
- Founders who never installed the desktop app need an extra download step first.
