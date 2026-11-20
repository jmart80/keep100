# How Keep100 sets up Claude, and why

Most people use Claude as a blank chat box. That's why it guesses, forgets, and confidently makes things up about their business. None of that is a flaw you have to live with. It comes from how Claude is set up, and Keep100 fixes the setup.

## Why Claude makes things up about your product

Claude fills gaps. If you ask for a landing page and it doesn't know your price, your features or your customers, it writes something plausible. Plausible isn't true. A better prompt doesn't fix that. What fixes it is making sure the true answer is always in front of Claude, and telling it what to do when it isn't.

## The five rules Keep100 builds in

**1. Give Claude one place to look.** All facts about your company live in `company/`. One file per subject: product, customers, positioning, pricing, brand, competitors, facts. Not scattered across chats, documents and memory.

**2. Never keep two copies of a fact.** If your price lives in three places, one of them will be wrong next month, and Claude can't tell which. So each fact has one home. Your price is in `pricing.md` and nowhere else. Every kind of work (marketing, sales, social) reads the same company files instead of keeping its own copy.

**3. Separate what's confirmed from what's guessed.** Each company file says whether you've confirmed it. `facts.md` holds your proof (results, credentials, named customers) and marks each entry `[confirmed]` or `[unconfirmed]`. Customer quotes are tagged `[verbatim]` only when the exact words were seen. Claude may only state confirmed facts, and only quote verbatim words, in anything you publish or send.

**4. Make "I don't know" the right answer.** The house rules tell Claude to ask you instead of guessing, and to cut any claim it can't back up. A gap you notice is better than a confident mistake your customers notice.

**5. Write the rules down once.** `CLAUDE.md` in your workspace holds the house rules: how to talk to you, which file to read for which job, what never to do. Each area folder has a short `CLAUDE.md` of its own with rules for that kind of work, and the main one tells Claude to read it first.

## Where each kind of instruction belongs

| Put it here | What goes there | What stays out |
|---|---|---|
| Your Claude settings | How to talk to you. Where your Keep100 folder is, and to ask you when it can't be opened | Company facts |
| `CLAUDE.md` | House rules and the map of files | Step-by-step procedures. Those are skills |
| An area's `CLAUDE.md` | The few rules for one kind of work | Rules already in the main one |
| `company/` | Facts | Drafts, research notes, opinions |
| Claude's memory | Your preferences about style | Prices, features, customer details |

Claude's memory deserves a word. Claude can remember things between chats, and a remembered price is a second copy of your price. The house rules tell Claude that your files win over anything it remembers.

## Writing a good CLAUDE.md (if you want to edit yours)

- **Short beats long.** Claude follows ten clear rules better than fifty vague ones.
- **Rules, not wishes.** "Never state a price that isn't in pricing.md" works. "Be accurate" doesn't.
- **Point, don't paste.** Tell Claude which file to read. Don't copy the contents into CLAUDE.md, or you've made a second copy.
- **Say what to do instead.** "Don't guess. Ask me" beats "don't guess".
- **Update it when Claude gets something wrong twice.** That's a missing rule. The monthly workspace audit asks you about this.

## Habits that keep it working

1. **One job per chat.** Start with "what's today" and stop when that piece is saved. Long chats drift, and your files carry the continuity, so a fresh chat loses nothing.
2. **Files over memory.** If a fact matters next week, it goes in a file.
3. **Claude drafts, you send.** Nothing is emailed, posted or published without your yes.
4. **Look at your dashboard.** It shows what's done and what's next, so you never have to work out where you were.
5. **Back up the folder.** Keep it somewhere with version history, such as a synced drive. One bad edit can undo an hour of confirming.
6. **Treat people's details with care.** Your prospect list and conversation notes are about real people. Keep only what the work needs, note where each detail came from, and delete someone's details if they ask.
7. **Audit once a month.** Ask Claude to audit your workspace. It finds stale facts and duplicate prices before a customer does.

## Your account settings

During setup, Keep100 gives you a short paragraph to paste into your Claude settings. It tells Claude, in every chat, that your company facts live in your Keep100 folder, and to ask you instead of guessing when it can't open them. It's a safety net for chats you start outside the workspace.

## Saving work

Every finished piece of work is saved into the workspace. The step is ticked in `progress.md`, a line goes in its Work log, and your dashboard is redrawn. People you've contacted go in `sales/pipeline.csv`, so Claude can say who is due a follow-up today without you remembering. Work that only lives in a chat is lost when the chat scrolls away.

## Keeping it up to date

When something about your business changes, tell Claude: "our price is now $49" or "we no longer offer the free plan". It updates the company file (with your yes), and everything after that uses the new fact.
