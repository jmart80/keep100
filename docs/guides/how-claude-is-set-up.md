# How Keep100 sets up Claude, and why

Most people use Claude as a blank chat box. That's why it guesses, forgets, and confidently makes things up about their business. None of that is a flaw you have to live with. It comes from how Claude is set up, and Keep100 fixes the setup.

## Why Claude makes things up about your product

Claude fills gaps. If you ask for a landing page and it doesn't know your price, your features or your customers, it writes something plausible. Plausible isn't true. The fix isn't a better prompt; it's making sure the true answer is always in front of Claude, and telling it what to do when it isn't.

## The five rules Keep100 builds in

**1. Give Claude one place to look.** All facts about your company live in `company/`. One file per subject: product, customers, positioning, pricing, brand, competitors, facts. Not scattered across chats, documents and memory.

**2. Never keep two copies of a fact.** If your price lives in three places, one of them will be wrong next month, and Claude can't tell which. Every kind of work (marketing, sales, social) reads the same company files instead of keeping its own copy.

**3. Separate what's confirmed from what's guessed.** Each company file says whether you've confirmed it. `facts.md` marks each fact `[confirmed]` or `[unconfirmed]`. Claude may only state confirmed facts in anything you publish or send.

**4. Make "I don't know" the right answer.** The house rules tell Claude to ask you instead of guessing, and to cut any claim it can't back up. A gap you notice is better than a confident mistake your customers notice.

**5. Write the rules down once.** `CLAUDE.md` in your workspace holds the house rules: how to talk to you, which file to read for which job, what never to do. Claude reads it every time you work in the folder, so you never repeat yourself. Each area folder has a short `CLAUDE.md` of its own with rules for that kind of work.

## Writing a good CLAUDE.md (if you want to edit yours)

- **Short beats long.** Claude follows ten clear rules better than fifty vague ones.
- **Rules, not wishes.** "Never state a price that isn't in pricing.md" works. "Be accurate" doesn't.
- **Point, don't paste.** Tell Claude which file to read. Don't copy the contents into CLAUDE.md, or you've made a second copy.
- **Say what to do instead.** "Don't guess. Ask me" beats "don't guess".
- **Update it when Claude gets something wrong twice.** That's a missing rule.

## Your account settings

During setup, Keep100 gives you a short paragraph to paste into your Claude settings (the profile instructions). It tells Claude, in every chat, to check your company files before stating facts and to ask instead of guessing. It's a safety net for chats you start outside the workspace.

## Saving work

Every finished piece of work is saved into the workspace and logged in `progress.md`. That's what lets Claude say "you emailed 12 people last week and 2 replied" without you remembering it. Work that only lives in a chat is lost when the chat scrolls away.

## Keeping it up to date

When something about your business changes, tell Claude: "our price is now $49" or "we no longer offer the free plan". It updates the company file (with your yes), and everything after that uses the new fact.
