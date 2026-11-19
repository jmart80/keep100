# Keep100 in the browser (claude.ai)

Use this only if you can't use the Claude desktop app. The browser version works, but setup is manual, and two things are missing: Claude can't keep a folder on your computer up to date, and the weekly brief can't be scheduled. You still need a paid Claude plan.

## 1. Add the skills

1. Download `keep100-skills.zip` from the [latest release](https://github.com/jmart80/keep100/releases/latest) and unzip it. You'll get one zip file per skill.
2. In claude.ai, open Settings, then Capabilities, and find Skills.
3. Upload each skill zip. Start with `setup`, `today`, `writing-check`, then the rest.

## 2. Create a Keep100 project

1. In claude.ai, create a Project called **Keep100**.
2. Start a chat in it and say: **"Set me up with Keep100. I'm in the browser."**
3. Claude will run setup in the chat and give you each company file and the house rules as text to save.
4. Add the company files to the project's knowledge, and paste the house rules into the project's instructions.

## 3. Keep one version of the truth

This is the part that needs care in the browser. Your company files live in the project knowledge, not on your computer, so:

- **When something changes** (a price, a feature, your ideal customer), ask Claude for the updated file and replace the old one in project knowledge right away.
- **Keep one project if you can.** If you split work into several projects (say, one for social and one for sales), every project needs the same company files, and every change has to be made in each one. That's how Claude ends up quoting an old price.

## 4. Each day

Open a chat in the Keep100 project and ask **"what's today?"** Paste in what you did since last time (who you emailed, what you posted), since Claude can't update your progress file for you.

## 5. Weekly brief

Set a reminder for Monday morning to open the project and ask for your weekly brief.
