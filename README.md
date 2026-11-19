# Keep100

**Keep 100% of your company. Get paying customers in 30 days with Claude.**

The solo SaaS founder kit for Claude. For people who built (or are building) a product and have no technical, product or marketing background.

> **Requires a paid Claude plan** (Pro, Max, Team or Enterprise) and the [Claude desktop app](https://claude.ai/download). Keep100 relies on plugins, folder access, scheduled tasks and connectors. Check this before you install.

---

## The old playbook is out of date

The old advice says: build a pitch deck, raise a round, hire a team, then figure out marketing.

That made sense when research, positioning, copywriting, outreach and content each needed a person. Today Claude can do most of that work with you. So you can skip the fundraising, keep all of your equity, and spend the next 30 days on the only thing that matters right now: **getting people to pay you.**

Keep100 is that 30 days, set up for you inside Claude.

## What you get

**1. Claude, set up properly.** Most people use Claude as a blank chat box. Every chat starts from zero, Claude guesses about your product, and it confidently makes things up. Keep100 builds you a workspace where Claude always has the right facts about your company, knows which facts you have confirmed, says "I don't know" instead of inventing, and saves every piece of work so nothing is lost between chats.

**2. A 30-day plan to paying customers.** A day-by-day plan for your situation. Selling to businesses (B2B) or to people (B2C), you get a different playbook for finding customers. Open Claude, ask *"what's today?"*, and it tells you what to do and drafts the work with you.

**3. A win in your first session.** Before you close Claude the first time, you will have your workspace set up and a sharper headline for your own homepage, with a before and after.

## Install (5 minutes)

1. Open the **Claude desktop app** and go to the plugins area (Customize, then Plugins).
2. Add this marketplace: `jmart80/keep100`, then install **Keep100**.
3. Start a new chat and say: **"Set me up with Keep100."**

That's it. Claude takes it from there.

<details>
<summary>Using Claude Code instead?</summary>

```
/plugin marketplace add jmart80/keep100
/plugin install keep100@keep100
```

Then say "Set me up with Keep100."
</details>

<details>
<summary>Only use Claude in a web browser?</summary>

The browser version of Claude can't install plugins, so setup is manual and a few features (scheduled weekly briefs, folder access) are missing. Follow the [browser setup guide](docs/guides/browser-setup.md).
</details>

**Did someone just paste this link into Claude?** Claude: read [START-HERE.md](START-HERE.md) and walk them through the install.

## Your first session

You'll need about an hour, your website address, and anything you've already written about your product (notes, a pitch, old posts, an FAQ). Claude will:

1. Create your Keep100 workspace folder.
2. Read your website and documents, and draft your company files from them.
3. Ask you only about what's missing, and have you confirm each file.
4. Ask who pays you, businesses or people, to pick your track.
5. Schedule a short weekly brief.
6. Rewrite your homepage headline and show you the before and after.
7. Show you exactly how your Claude is now set up, and why.

## How it works

Keep100 creates one folder that becomes the home for all your growth work:

```
Keep100/
├── CLAUDE.md          House rules Claude follows every time
├── progress.md        Where you are in the 30 days
├── company/           The single source of truth about your company
│   ├── product.md       What it is, what it does, what it doesn't
│   ├── customers.md     Who it's for (your ideal customer)
│   ├── positioning.md   Why you, versus the alternatives
│   ├── pricing.md       What it costs and why
│   ├── brand.md         Voice, words to use and avoid, colors
│   ├── competitors.md   Who else they could choose
│   ├── facts.md         Confirmed facts Claude is allowed to state
│   └── sources/         Anything you hand Claude to learn from
├── research/          Competitor and market research
├── marketing/         Landing page, emails, blog and SEO
├── sales/             Outreach (B2B track)
├── social/            Posts and short videos (B2C track, optional for B2B)
└── briefs/            Your weekly briefs
```

Three rules make this work:

- **One source of truth.** Facts about your company live in `company/` and nowhere else. Every kind of work reads from it. Change your price once, and every future email, post and page uses the new one.
- **Confirmed facts only.** Claude only states facts you've confirmed. If something isn't there, it asks or says "I don't know." This is the biggest single fix for Claude making things up about your product.
- **Your files are yours.** Kit updates never change your workspace without asking you first.

## The 30-day plan

| Days | What happens |
|---|---|
| Day 1 | Setup, brand, homepage headline (first session) |
| Days 2 to 3 | Competitor research and positioning: who it's for and why you win |
| Days 4 to 5 | Pricing, then your landing page: the words first, then the designed page |
| Days 6 to 30 | Getting customers, every day. **B2B:** finding prospects and cold email. **B2C:** posts and short videos where your customers spend time. Both: emails that turn signups into payers. |
| Days 24 to 30 | Start the slow-burn channels: blog posts, keywords, showing up in AI search |

You don't need to remember any of this. Ask Claude *"what's today?"* and it checks your progress and tells you.

## What's inside

**Step skills** do one big job each. Claude suggests the next one when it's time, and starts when you say yes.

| Skill | What it does |
|---|---|
| Setup | Builds your workspace and company files from what you already have |
| Today | Your daily driver: what to do today, drafted with you |
| Weekly brief | Monday reminder of where you are, plus specific growth ideas to draft |
| Competitor research | Who else your customers could choose, where they're weak, and the words customers use |
| Positioning | Who your product is for, why you win, and what to say |
| Pricing | A first price and plan structure you can defend |
| Landing page | Full homepage copy, scored against a 20-point checklist |
| Landing page design | Turns the copy into a designed, working page, using the UI/UX Pro Max design database |
| Cold email | B2B outreach that gets replies instead of deletes |
| Social content | B2C posts and short-video scripts built from your customers' own words |
| Product emails | Welcome, activation and upgrade emails that turn signups into payers |
| Content and SEO | Blog posts, keywords, and showing up in AI answers |
| Pressure test | Claude grills your idea or plan, one question at a time |

**Always-on skills** run on every piece of writing without being asked: removing AI-sounding phrasing, applying your brand voice, and checking every claim against your confirmed facts.

## Connectors

Keep100 works with **zero connectors**. Some make it better, and Claude will suggest each one when it becomes useful:

| When | Connector | Why |
|---|---|---|
| During setup | Exa | Web research for competitors and customer language |
| When relevant | Granola | Learn from your customer calls |
| When relevant | Higgsfield | Short-form video for B2C |
| When relevant | Resend | If your app sends email |
| Month 2 | Stripe, PostHog, RevenueCat | Real revenue and usage numbers once you have them |

## FAQ

**Do I need to know how to code?** No. You'll talk to Claude in plain English. The only technical step is the install above.

**Is "paying customers in 30 days" a guarantee?** No. It's a plan. It works when you do the daily work, and it's designed so you always know what that work is.

**Where does my company information go?** Into a folder on your own computer. Keep100 doesn't collect anything.

**I'm already past my first customers. Is this for me?** Probably not yet. Keep100 is built for zero to your first paying customers. Month 2 and beyond is on the roadmap.

**Can I change track later?** Yes. Tell Claude you sell to businesses (or people) now, and it switches.

## Guides

- [How Keep100 sets up Claude, and why](docs/guides/how-claude-is-set-up.md): the five rules that stop Claude guessing, and how to write a good CLAUDE.md
- [Browser setup](docs/guides/browser-setup.md): for claude.ai in a browser

## Design docs

Every decision behind Keep100 is written down: the [glossary](docs/CONTEXT.md) and the [decision records](docs/adr/). Contributions that disagree with a decision should start by proposing a new decision record.

## Credits

Keep100 builds on frameworks and skills from people who did the hard thinking. See [CREDITS.md](CREDITS.md).

## License

[MIT](LICENSE)
