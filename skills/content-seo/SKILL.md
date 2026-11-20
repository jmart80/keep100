---
name: content-seo
description: Blog posts, keyword research and showing up in AI answers for a Keep100 founder. Starts near the end of the plan and continues after it, because search traffic builds slowly. Use when the founder asks for a blog post, SEO, keywords, how to rank on Google, a comparison or alternative page, or how to appear in ChatGPT, Claude or Perplexity answers. Also use for any question about whether to start a blog, content marketing, organic or search traffic, or getting found on Google, even when it is a yes or no question, because the honest answer depends on where the founder is in the plan.
---

# Content and SEO

Search and AI-answer traffic takes months to build, so this starts after customer-getting work is running. If the founder asks earlier, help, but say plainly that outreach or social will bring customers faster this month.

## Inputs

`company/customers.md` (the questions and words customers use), `company/positioning.md`, `company/competitors.md`, research, `conversations/`, and the questions prospects asked in replies (`sales/pipeline.csv` notes).

## Branch A: Topics and keywords

1. Start from **real questions** customers ask: from replies, comments, calls, reviews and communities. For a new site these are a better starting point than a keyword tool.
2. With web search or Exa, look at each: who shows up now, and whether the searcher wants to buy, compare or learn. Say plainly that without an SEO tool this is a rough read: you can see who ranks, not how many people search or how hard it is to beat them.
3. Prioritize, in this order: comparison and alternative pages ("{competitor} alternative", "{competitor} vs {product}"), problem-specific how-tos the product truly helps with, then broader education.
4. Save a ranked list of 10 to 20 topics to `marketing/content-plan.md`, each with the target phrase, the question it answers, and why it should win. Tick "Content plan" in `progress.md`.

## Branch B: Write a post

- Answer the question in the first two sentences. Then the detail.
- Use the customer's words for the question and headings.
- Be specific: real steps, real examples, the founder's own experience. Generic posts give nobody a reason to read or cite them.
- Mention the product only where it truly helps, once or twice, never forced.
- Only confirmed facts about the product. Cite sources for outside claims with links, and date anything about a competitor.
- Comparison pages are honest about where the competitor is better. Never state a competitor's price or feature without the link and the date you checked.
- Include a title (under 60 characters), a meta description (under 155 characters), and a URL slug.
- Run `keep100:writing-check` with `--format blog`, save to `marketing/<date>-<slug>.md`. Tick "First two posts published" when two are live.

## Branch C: Can search engines and AI assistants read the site?

Check this before writing ten posts. A page that can't be read can't be found.

1. Fetch the founder's homepage the way a crawler would, with plain web fetch and no browser. If the text of the page comes back, good. If it comes back nearly empty, the site builds its pages in the visitor's browser, and some crawlers will see nothing. Tell the founder in plain words and give them a change request for their app builder or developer: "serve the marketing pages as ready-made HTML".
2. Each page has its own title and description.
3. The site has a sitemap, and nothing blocks crawlers by accident.
4. Suggest connecting Google Search Console, which is free, so the founder can see what people searched to find them.

## Branch D: Show up in AI answers

What gets a page cited by AI assistants is still being worked out, and advice on it changes quickly. These steps are sensible defaults, not proven tactics. They cost little and help ordinary search too:

- A clear, factual "what is {product}" page and a pricing page in plain text, not only images.
- Comparison pages that are honest about where competitors are better.
- An FAQ answering real questions in one or two sentences each.
- Being mentioned where people already discuss the problem: relevant community threads, directories in the niche (see `keep100:launch`), and real answers in communities.
- Once a month, ask a few AI assistants the questions customers ask, and note in `learnings.md` whether and how the product appears.
