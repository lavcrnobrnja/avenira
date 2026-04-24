# PROJECT.md - Avenira

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
- `projects/avenira/avenira-website-specification.md` - full spec (brand, copy, structure, bilingual rules)
- `projects/avenira/avenira-theme/` - Ghost Handlebars theme (deployed)
- `projects/avenira/mockup/` - original HTML/CSS/JS mockup files
- `projects/avenira/copy-rewrite.md` - copy deck reference from GPT-5.4 rewrite
- `projects/avenira/research/ghost-theme-research.md`

## Pages (10 total)
EN: `index.html`, `about.html`, `services.html`, `grants.html`, `contact.html`
FR: `fr/index.html`, `fr/a-propos.html`, `fr/services.html`, `fr/subventions.html`, `fr/contact.html`

## Current state (Apr 24, ~16:30 EDT)
- **Cards 1-5, 271, 272, 3** + all touchup/QA cards + grants fix (#287): ✅ All Ready to Test
- **Card #289** (Google Analytics): ✅ Ready to Test — GA G-713K4T7T4J in default.hbs
- **Hero Redesign (#349):** ✅ Ready to Test — all 5 step cards moved
  - Glass-pill nav, circuit fan-out hero, ambient background, JetBrains Mono font
  - Mobile nav fully working (see Learnings below for root cause)
  - Branch: `cofoundergpt/hero-redesign`, final fix commit: `fba50a3`
- **Card 6** (Initial Blog Posts): In Progress
  - **Post #5** "What to Automate First" ✅ Published EN+FR
  - 4 more posts remaining

## Key decisions
- Hero illustration is a generated PNG (`assets/images/hero-illustration.png`), same image EN+FR (no text in image). **Do not regenerate** - Lav prefers the current version.
- Grant banner uses inline styled divs (stacked cards) instead of SVG. Hides on mobile via existing CSS `.grant-visual { display: none }` at breakpoint.
- All emdashes purged from body copy (period-separated sentences instead).
- Pain points section: 2-column grid with h2 title + lead paragraph in left column, numbered items in right column.
- About page: No "Our Story" or "Shared Track Record" sections. Team section subtitle has the consolidated text.
- Founder avatars: `assets/images/avatar-lav.jpeg` (blazer) and `assets/images/avatar-arfan.jpeg` (hoodie).
- Services hero: "Take the busywork off your team's plate" (GPT-5.4 copywriter).
- Contact form: Formspree endpoint xdaprogd. Phone field is optional.
- Cookie banner: No Loi 25 reference.
- MariaDB access: user=ghost, password starts with gh0s... (discovered during social link cleanup).

## Rules
- Dark, sharp, minimal. No generic SaaS look, no emoji icons, no fluffy copy, no pricing, no leading with AI, no specific tool names.
- **ALWAYS browser-verify visual changes before claiming done.** Use `screencapture` + `image` tool.
- Copy: "Built From Experience, Not Theory" is sacred - Lav's favorite line, never change it.
- Founders: Lav Crnobrnja + Arfanuddin Khan (NOT Slobodan).
- **post.hbs MUST wrap content in `{{#post}}...{{/post}}`** — Ghost 6.x requires this for title/content/feature_image to render.
- **`{{reading_time}}`** outputs complete "X min read" string — don't append extra text. FR uses JS replace.
- **Cover images:** Study existing brand assets (dark navy, electric blue/cyan glows, circuit motifs) before generating. Don't make generic stock images.
- **"Coming soon" placeholder posts** were unpublished on both instances — don't recreate.

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
├─ locales/ (en.json, fr.json - 38 UI strings each)
├─ assets/css/screen.css    # Full stylesheet (~2370 lines)
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

## Key CSS values
- `.page-hero p` max-width: 800px (widened from 600px for grants page readability)
- `.page-hero` section labels: plain text only, no icons (consistent across all pages)
- Pain point cards: 2 sentences each max (cards are small — copy must fit)
- **Mobile nav:** `backdrop-filter` on `.site-header` is killed at ≤1024px (creates containing block that traps fixed children). Do NOT add `.site-header` back to the ambient stacking rule (`position: relative; z-index: 1`) — it breaks fixed positioning.

## Learnings (project-specific)
- **deploy-theme.py doesn't rebuild the zip** — always `cd avenira-theme && zip -r ../avenira-theme.zip . -x routes-fr.yaml` BEFORE running deploy
- **Ambient stacking rule broke header:** `position: relative; z-index: 1` on `.site-header` overrode `position: fixed; z-index: 1000`. Never include `.site-header` in broad stacking rules.
- **backdrop-filter creates containing block:** Any ancestor with `backdrop-filter` traps `position: fixed` children. On mobile, `backdrop-filter: none !important` on `.site-header` is required.
- **CSS resets can break skip links** — never include `.skip-link` in broad position rules

## Next step
Card 6: 4 more blog posts (Post #5 done, grant/funding SEO focus, bilingual)
