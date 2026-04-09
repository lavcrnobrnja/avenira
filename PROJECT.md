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
- **Ghost admin:** https://avenira.ai/ghost/ (EN), https://avenira.ai/fr/ghost/ (FR)
- **Admin login:** cofoundergpt@cloudhorizon.com (password on Trello info card #263)
- **EN Admin API key:** 69d8185cb437b1e938a801c7:6dc467a96bb5c9dcf0795151f5e9dd9185528751d77468a47f0d797ba80bf02e
- **EN Content API key:** a561fe01de0c96b7737b0ddc96
- **FR Admin API key:** 69d818d214e97ce940a3ac7c:84e3838aeca8f3e90827685c3c6ee2ea6e1cff9ee8d50153c33c154769e36fe9
- **FR Content API key:** 5e75d6eb4ed7255e7e6f3cd41d
- **Ghost settings configured:** locale (en/fr), title, description, timezone (America/Toronto), staffDeviceVerification disabled

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

## Current state (Apr 9, ~17:38 EDT)
- **Card 1** (Ghost theme research): ✅ Done
- **Card 2** (Design System + HTML Mockup): ✅ Approved
- **Card 271** (Copy rewrite): ✅ Done
- **Card 272** (Visuals): ✅ Done
- **Card 3** (Server setup): ✅ Done — Ghost EN (:2370) + FR (:2371), nginx /fr/ path routing, SSL certbot (expires 2026-07-08), admin accounts created, API integrations (Admin+Content keys) created and verified, locale/title/description/timezone configured, all 6 redirect chains correct, all credentials on Trello info card #263
- **Card 4** (HTML → Ghost Theme): Next up
- **Card 5** (QA): After Card 4
- **Card 6** (Initial Blog Posts): After Card 5

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
