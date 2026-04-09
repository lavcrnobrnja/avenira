# PROJECT.md — Avenira

Bilingual Ghost marketing site for avenira.ai, targeting Quebec SMB automation consulting.

## Stack
Static HTML/CSS/JS mockup now, then Ghost theme on two Ghost instances (EN + FR) behind one domain with nginx path routing (`/fr/`).

## Key paths
- `projects/avenira/avenira-website-specification.md` — full spec (brand, copy, structure, bilingual rules)
- `projects/avenira/mockup/` — all HTML/CSS/JS files
- `projects/avenira/mockup/img/` — generated images (hero-illustration.png)
- `projects/avenira/mockup/css/style.css` — single stylesheet
- `projects/avenira/research/ghost-theme-research.md`
- `design-system/avenira-automations/MASTER.md`
- `projects/avenira/copy-rewrite.md` — copy deck reference from GPT-5.4 rewrite

## Pages (10 total)
EN: `index.html`, `about.html`, `services.html`, `grants.html`, `contact.html`
FR: `fr/index.html`, `fr/a-propos.html`, `fr/services.html`, `fr/subventions.html`, `fr/contact.html`

## Current state (Apr 9, ~17:00 EDT)
- **Card 1** (Ghost theme research): ✅ Done
- **Card 2** (Design System + HTML Mockup): ✅ Approved — multiple redesign rounds (nav, pain points, service visuals, founders block, industries, approach items)
- **Card 271** (Copy rewrite): ✅ Done — full copy rewrite across all 10 pages, 2 rounds of fixes (pain points h2/lead restored, about story centered with heading, services hero rewritten, emdash purge, closing paragraph tightened)
- **Card 272** (Visuals): ✅ Done — hero illustration replaced with NB2-generated before/after workflow diagram (`img/hero-illustration.png`), grant banner 50% pie chart replaced with stacked grant program cards (ESSOR/OTN/CRIC/PME MTL). Browser-verified.
- **Card 3** (Server setup): Next up — Ghost instances, nginx, SSL

## Key decisions
- Hero illustration is a generated PNG (`img/hero-illustration.png`), same image EN+FR (no text in image). FR path uses `../img/hero-illustration.png`.
- Grant banner uses inline styled divs (stacked cards) instead of SVG. Hides on mobile via existing CSS `.grant-visual { display: none }` at breakpoint.
- All emdashes purged from body copy (period-separated sentences instead).
- About story section has centered layout with eyebrow label + heading + paragraph.
- Pain points section: 2-column grid with h2 title + lead paragraph in left column, numbered items in right column.

## Rules
- Dark, sharp, minimal. No generic SaaS look, no emoji icons, no fluffy copy, no pricing, no leading with AI, no specific tool names.
- **ALWAYS browser-verify visual changes before claiming done.** Use `screencapture` + `image` tool.
- Copy: "Built From Experience, Not Theory" is sacred — Lav's favorite line, never change it.
- Founders: Lav Crnobrnja + Arfanuddin Khan (NOT Slobodan).

## Next step
Card 3: Server setup — Ghost instances, nginx, SSL, domain config.
