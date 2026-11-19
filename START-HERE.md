# Start here (for Claude)

A founder gave you this link because they want Keep100 set up. They are probably not technical. Help them install it, in plain language, one step at a time.

## If the Keep100 plugin is already installed

You will see the `keep100:setup` skill in your skill list. Run it now.

## If it is not installed

1. Check which Claude app they are in. Ask if you can't tell.
2. **Claude desktop app:** walk them through it. Open the plugins area (Customize, then Plugins), add the marketplace `jmart80/keep100`, and install Keep100. Then they should start a new chat and say "Set me up with Keep100."
3. **Claude Code:** they can run `/plugin marketplace add jmart80/keep100` and then `/plugin install keep100@keep100`.
4. **claude.ai in a browser or phone:** plugins can't be installed there. Recommend the free desktop app download (https://claude.ai/download). If they want to stay in the browser, follow `docs/guides/browser-setup.md` from this repo with them.

Before any of this, confirm they are on a paid Claude plan. Keep100 needs one.

## Rules while you help

- One step at a time. Wait for them to say it worked before giving the next step.
- If a menu name doesn't match what they see, ask them to describe their screen instead of guessing.
- Don't start building their company files in this chat. That happens after install, in the setup skill.
