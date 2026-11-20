# Start here (for Claude)

A founder gave you this link because they want Keep100 set up. They are probably not technical. Help them install it, in plain language, one step at a time.

## If the Keep100 plugin is already installed

You will see the `keep100:setup` skill in your skill list. Run it now.

## If it is not installed

1. Check which Claude app they are in. Ask if you can't tell.
2. **Claude desktop app, or claude.ai in a browser:** walk them through it. Open **Customize**, then **Plugins**, add the marketplace `jmart80/keep100`, and install Keep100. Then they should start a new chat and say "Set me up with Keep100."
3. **Claude Code:** they can run `/plugin marketplace add jmart80/keep100` and then `/plugin install keep100@keep100`.
4. **A phone:** plugins they add to their account work in the mobile app too, but adding one is easier on a computer. Suggest they install on a computer first.

Recommend the free desktop app (https://claude.ai/download) to anyone in a browser. Keep100 works in both, but only the desktop app can keep a folder on their computer up to date and run the Monday brief. If they stay in the browser, follow `docs/guides/browser-setup.md` from this repo with them after installing.

Keep100 needs a paid Claude plan. Say so once, before they start.

## Rules while you help

- One step at a time. Wait for them to say it worked before giving the next step.
- If a menu name doesn't match what they see, ask them to describe their screen instead of guessing. Menus change.
- If they can't find Plugins under Customize, their plan or their organization may not allow adding plugins. Say that plainly. Don't invent another route.
- Don't start building their company files in this chat. That happens after install, in the setup skill.
