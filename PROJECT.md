# PROJECT.md — Avenira

Bilingual Ghost marketing site for avenira.ai, targeting Quebec SMB automation consulting.

## Stack
Static HTML/CSS/JS mockup → Ghost theme on two Ghost instances (EN + FR) behind one domain with nginx path routing (`/fr/`).

## Server
- **EN Ghost:** https://avenira.ai/ → :2370 (MariaDB: ghost_avenira_en)
- **FR Ghost:** https://avenira.ai/fr/ → :2371 (MariaDB: ghost_avenira_fr)
- **Ghost version:** 6.27.0
- **Server:** 98.92.64.101 (same as DraftSpring, YouOnPTO, blog)
- **Services:** ghost_avenira-ai, ghost_avenira-ai-fr
- **Nginx:** /etc/nginx/sites-available/avenira.ai.conf
- **SSL:** certbot, expires 2026-07-08, covers avenira.ai + www.avenira.ai
- **EN install path:** /var/www/avenira.ai/
- **FR install path:** /var/www/avenira.ai-fr/
- **Ghost admin setup:** https://avenira.ai/ghost/#/setup (EN), https://avenira.ai/fr/ghost/#/setup (FR)

## Git
- **Repo:** https://github.com/lavcrnobrnja/avenira
- **Local:** /workspace/projects/avenira/

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

## Current state (Apr 9, ~17:20 EDT)
- **Card 1** (Ghost theme research): ✅ Done
- **Card 2** (Design System + HTML Mockup): ✅ Approved
- **Card 271** (Copy rewrite): ✅ Done
- **Card 272** (Visuals): ✅ Done
- **Card 3** (Server setup): ✅ Done — Ghost EN (:2370) + FR (:2371), nginx with /fr/ path routing, SSL via certbot (expires 2026-07-08), systemd services, MariaDB databases
- **Card 4** (HTML → Ghost Theme): Next up

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
Card 4: HTML → Ghost Theme Conversion
