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
- `projects/avenira/avenira-theme/` — Ghost Handlebars theme (deployed)
- `projects/avenira/mockup/` — original HTML/CSS/JS mockup files
- `projects/avenira/copy-rewrite.md` — copy deck reference from GPT-5.4 rewrite
- `projects/avenira/research/ghost-theme-research.md`

## Pages (10 total)
EN: `index.html`, `about.html`, `services.html`, `grants.html`, `contact.html`
FR: `fr/index.html`, `fr/a-propos.html`, `fr/services.html`, `fr/subventions.html`, `fr/contact.html`

## Current state (Apr 9, ~18:52 EDT)
- **Card 1** (Ghost theme research): ✅ Done
- **Card 2** (Design System + HTML Mockup): ✅ Approved
- **Card 271** (Copy rewrite): ✅ Ready to Test
- **Card 272** (Visuals): ✅ Done
- **Card 3** (Server setup): ✅ Done
- **Card 4** (HTML → Ghost Theme): ✅ Ready to Test — v1.0.1 deployed to both instances
  - 21 theme files, custom templates for all 6 pages + blog
  - Bilingual via {{@site.locale}} + {{#match}} blocks
  - Locale-aware nav with French slugs (subventions, a-propos, blogue, confidentialite)
  - routes.yaml deployed (EN: /blog/, FR: /blogue/)
  - All 12 pages created and returning 200
  - All 10 tags created (5 EN + 5 FR)
  - Formspree contact form endpoint: xdaprogd
  - Cookie consent, hreflang tags, Koenig CSS classes all working
  - Ghost navigation NOT set via DB — header/footer hardcoded in theme, works fine
- **Post-Card 4 QA fixes (9 items):** ✅ Deployed
  - Per-service CTAs on services page
  - Phone field on contact form
  - Grants page intro paragraph + "important note"
  - FR grant banner link fixed (/grants/ → /subventions/)
  - Footer language toggle added
  - Social links cleared from Ghost
  - Hero trust signal added then removed per Lav feedback
  - Footer email removed per Lav feedback
- **6 additional Trello cards (all Ready to Test):**
  - Homepage image — reverted to original (Lav preferred it)
  - Orphan section removed (pain-redesign-closing text)
  - Loi 25 text removed from cookie banner (EN+FR)
  - Services hero copy rewritten: "Take the busywork off your team’s plate"
  - "Our Story" section removed from About, Team pushed up
  - Founder avatars added (Lav=blazer, Arfan=hoodie)
- **3 more Trello cards (all Ready to Test):**
  - Hero spacing increased (h1: 36px, subtitle: 40px)
  - About "Shared Track Record" removed, text consolidated into team subtitle
  - Homepage image reverted (second pass — Lav wanted original back)
- **Card 5** (QA): Next up
- **Card 6** (Initial Blog Posts): After Card 5

## Key decisions
- Hero illustration is a generated PNG (`assets/images/hero-illustration.png`), same image EN+FR (no text in image). **Do not regenerate** — Lav prefers the current version.
- Grant banner uses inline styled divs (stacked cards) instead of SVG. Hides on mobile via existing CSS `.grant-visual { display: none }` at breakpoint.
- All emdashes purged from body copy (period-separated sentences instead).
- Pain points section: 2-column grid with h2 title + lead paragraph in left column, numbered items in right column.
- About page: No "Our Story" or "Shared Track Record" sections. Team section subtitle has the consolidated text.
- Founder avatars: `assets/images/avatar-lav.jpeg` (blazer) and `assets/images/avatar-arfan.jpeg` (hoodie).
- Services hero: "Take the busywork off your team’s plate" (GPT-5.4 copywriter).
- Contact form: Formspree endpoint xdaprogd. Phone field is optional.
- Cookie banner: No Loi 25 reference.
- MariaDB access: user=ghost, password starts with gh0s... (discovered during social link cleanup).

## Rules
- Dark, sharp, minimal. No generic SaaS look, no emoji icons, no fluffy copy, no pricing, no leading with AI, no specific tool names.
- **ALWAYS browser-verify visual changes before claiming done.** Use `screencapture` + `image` tool.
- Copy: "Built From Experience, Not Theory" is sacred — Lav's favorite line, never change it.
- Founders: Lav Crnobrnja + Arfanuddin Khan (NOT Slobodan).

## Theme structure
```
avenira-theme/
├─ default.hbs              # Base layout
├─ custom-home.hbs          # Homepage (362 lines)
├─ custom-services.hbs      # Services page
├─ custom-grants.hbs        # Grants page
├─ custom-about.hbs         # About page
├─ custom-contact.hbs       # Contact (Formspree)
├─ custom-privacy.hbs       # Privacy policy
├─ index.hbs / post.hbs / tag.hbs / page.hbs  # Blog templates
├─ partials/ (header, footer, cookie-banner)
├─ locales/ (en.json, fr.json — 38 UI strings each)
├─ assets/css/screen.css    # Full stylesheet (1855 lines)
├─ assets/js/main.js        # Nav, cookies, scroll
├─ assets/images/hero-illustration.png
├─ assets/images/avatar-lav.jpeg
├─ assets/images/avatar-arfan.jpeg
├─ routes.yaml              # EN routing
└─ routes-fr.yaml           # FR routing
```

## Deploy process
1. Make changes in avenira-theme/
2. Zip: `cd avenira-theme && zip -r ../avenira-theme.zip . -x routes-fr.yaml`
3. Deploy: `python3 deploy-theme.py` (uploads + activates on both instances)
4. If routes change: SCP to server + restart Ghost services

## Next step
Card 5: QA
