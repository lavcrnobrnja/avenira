# Ghost CMS Theme Development & Bilingual Site Architecture

## TL;DR & Recommendations

### Architecture Recommendation: Path-Based (`avenira.ai/fr/`)
For the bilingual setup, **Option B (Path-based subdirectory routing)** is strongly recommended over a subdomain (`fr.avenira.ai`).
- **SEO Benefits:** Google consolidates domain authority into a single domain rather than splitting it across subdomains. 
- **User Trust:** Users generally trust and expect `domain.com/fr/` over `fr.domain.com`.
- **SSL:** You only need one SSL certificate for the primary domain.
- **Nginx Setup:** Requires a `location /fr/` block in the primary domain's Nginx config to proxy traffic to the second Ghost instance.

### Theme Strategy Recommendation: Single Unified Theme
You can and should use **one single theme zip** for both the English and French instances. 
- Use Ghost's built-in translation helper `{{t "String"}}` and include a `locales/en.json` and `locales/fr.json` directory.
- Ghost uses the **Site Language** setting in the Admin UI to determine which locale file to load.
- `{{@site.lang}}` will let you dynamically render the language switcher link (e.g., if on "en", the switcher links to `/fr/`, if on "fr", it links to `/`).

---

## 1. Ghost Theme Architecture

Ghost themes use Handlebars (`.hbs`). 

### Directory Structure
A standard Ghost theme requires a specific structure:
```text
├── assets/
│   ├── css/          # Stylesheets (screen.css)
│   ├── js/           # Scripts
│   └── images/       # Theme-specific images (logos, icons)
├── locales/          # Translation files (CRITICAL for your bilingual setup)
│   ├── en.json
│   └── fr.json
├── partials/         # Reusable code blocks
│   ├── header.hbs
│   └── footer.hbs
├── default.hbs       # The base layout file
├── index.hbs         # The blog/news feed layout
├── post.hbs          # Individual blog post layout
├── page.hbs          # Default static page layout
├── custom-services.hbs # Custom template for a specific page type
└── package.json      # Theme metadata and dependencies
```

### Essential Handlebars Helpers
- `{{content}}`: Outputs the HTML content of a post or page.
- `{{#foreach posts}} ... {{/foreach}}`: Loops through lists of posts.
- `{{#is "home"}}`: Conditional helper to check the current context (e.g., `home`, `post`, `page`, `tag`).
- `{{navigation}}`: Outputs the navigation menu configured in the Ghost Admin.
- `{{asset "css/screen.css"}}`: Correctly resolves asset URLs, preventing caching issues.
- `{{t "String"}}`: Translation helper. Looks up the string in your `locales/` JSON files based on the instance's language setting.
- `{{ghost_head}}` and `{{ghost_foot}}`: **Mandatory**. Placed in `<head>` and before `</body>` in `default.hbs`. They inject SEO meta tags, canonical URLs, code injection from the admin UI, and Portal scripts.

### Core Templates Explained
- **`default.hbs`**: The wrapper for the entire site. Contains `<html>`, `<head>`, `<body>`, header, and footer. It uses `{{{body}}}` to inject the content of other templates.
- **`index.hbs`**: The default fallback for lists of posts (like the blog home).
- **`home.hbs`**: If present, this is used for the absolute homepage (`/`) instead of `index.hbs`. Highly recommended for business sites.
- **`page.hbs`**: Used for static pages (About, Contact).
- **Custom Page Templates**: Name them `custom-*.hbs` (e.g., `custom-services.hbs`). They appear in the Ghost Admin under the page settings sidebar as a selectable "Template".

### `package.json` Requirements
Ghost strictly requires a `package.json` with specific fields:
```json
{
  "name": "avenira-theme",
  "description": "Custom theme for Avenira Automations",
  "version": "1.0.0",
  "engines": {
    "ghost": ">=5.0.0"
  },
  "config": {
    "posts_per_page": 10
  }
}
```

---

## 2. Custom Routing (`routes.yaml`)

Ghost uses `routes.yaml` to define URL structures, completely independent of the theme. You upload it separately in the Admin UI (Settings > Labs > Routes).

### How it works
It has three sections: `routes` (static routing), `collections` (blog groupings), and `taxonomies` (tags/authors).

### Can it help with bilingual URL structure?
**No.** `routes.yaml` operates *within* a single Ghost instance. It cannot route traffic between two different Ghost servers. The `avenira.ai/fr/` routing MUST be handled by Nginx at the infrastructure level.

### Example configuration (Business Site)
```yaml
routes:
  /: home            # Renders home.hbs for the root URL
  /about/: about     # Renders about.hbs (if you want it detached from Ghost pages)

collections:
  /blog/:
    permalink: /blog/{slug}/
    template: index

taxonomies:
  tag: /category/{slug}/
  author: /author/{slug}/
```

---

## 3. Bilingual Two-Instance Architecture

You want English on `avenira.ai` and French via a sub-URL or sub-domain. 

### Option B: Path-based (`avenira.ai/fr/`) — RECOMMENDED

**How it works:** 
- Nginx listens on `avenira.ai`. 
- Requests to `/fr/*` are proxy-passed to Ghost Instance 2.
- All other requests are proxy-passed to Ghost Instance 1.

**Ghost Config (`config.production.json`):**
- English Instance: `"url": "https://avenira.ai"`
- French Instance: `"url": "https://avenira.ai/fr"` (Ghost natively supports running in a subdirectory!)

**Nginx Configuration:**
```nginx
server {
    listen 443 ssl http2;
    server_name avenira.ai;
    
    # SSL Certs (only one needed for avenira.ai)
    ssl_certificate /etc/letsencrypt/live/avenira.ai/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/avenira.ai/privkey.pem;

    # Route for French Instance
    location ^~ /fr/ {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        # Pass to French Ghost instance port (e.g., 2369)
        proxy_pass http://127.0.0.1:2369;
        proxy_redirect off;
    }

    # Route for English Instance (Default)
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        # Pass to English Ghost instance port (e.g., 2368)
        proxy_pass http://127.0.0.1:2368;
        proxy_redirect off;
    }
}
```

**Pros:** Best for SEO. Unified domain authority. Single SSL certificate.
**Cons:** Nginx config needs manual editing.

### Option A: Subdomain (`fr.avenira.ai`)
- **Nginx:** Two completely separate `server {}` blocks. Very standard Ghost CLI setup.
- **SSL:** Needs a certificate for `avenira.ai` and another for `fr.avenira.ai`.
- **SEO:** Search engines treat subdomains as somewhat separate entities, which can dilute authority. 

### Hreflang Tags (SEO)
To tell Google these are translated versions of the same site, you need `hreflang` tags. Since the two instances are unaware of each other's specific posts, the best way to do this is in the theme's `default.hbs` `<head>` using Ghost's Site URL logic:

```html
<!-- In default.hbs -->
{{#is "home"}}
  <link rel="alternate" hreflang="en" href="https://avenira.ai/" />
  <link rel="alternate" hreflang="fr" href="https://avenira.ai/fr/" />
{{/is}}
```

---

## 4. Theme Development Workflow

### Local Development
You **do** need a local Ghost instance. 
1. Install Ghost CLI: `npm install -g ghost-cli@latest`
2. Run `ghost install local` in a new directory.
3. Develop your theme in `content/themes/avenira-theme/`.
4. Ghost doesn't auto-reload CSS/JS out of the box. Use a build tool like Gulp, Webpack, or Vite. Ghost's official starter theme ("Casper") uses Gulp with Browsersync for hot reloading.

### gscan
`gscan` is Ghost's theme validator. It checks for deprecated helpers and required files.
- Run locally: `gscan /path/to/theme/directory`
- It is automatically run when you upload a zip via the Ghost Admin UI. If errors are found, the upload is rejected.

### Deployment
Since your servers are running EC2, you can deploy by:
1. **Manual:** Zip the theme folder, upload via Admin UI (Settings > Design > Change Theme > Upload).
2. **Automated (Ghost Admin API):** Use the official GitHub Action (`TryGhost/action-deploy-theme`) to automatically zip and deploy the theme to both instances whenever you push to the `main` branch.

---

## 5. Sharing One Theme Across Two Instances

**Yes, you use the EXACT same theme zip for both instances.**

### The Setup
1. **Admin UI:** Go to Settings > General on both instances. 
   - EN Instance: Set Site Language to `en`
   - FR Instance: Set Site Language to `fr`
2. **Theme:** Create `locales/en.json` and `locales/fr.json` with key-value pairs:
   ```json
   // en.json
   {
     "Read More": "Read More",
     "Contact Us": "Contact Us"
   }
   // fr.json
   {
     "Read More": "Lire la suite",
     "Contact Us": "Contactez-nous"
   }
   ```
3. **Usage:** In your `.hbs` files, use `{{t "Contact Us"}}`. Ghost automatically outputs the correct string based on the instance's language setting.

### Language Toggle
To build the switcher in your theme, you can use the `{{@site.lang}}` variable to conditionally render the link:

```handlebars
<div class="language-switcher">
  {{#match @site.lang "=" "en"}}
    <a href="https://avenira.ai/fr/">FR</a>
  {{else}}
    <a href="https://avenira.ai/">EN</a>
  {{/match}}
</div>
```

---

## 6. Ghost Features We Need

### Contact Forms
Ghost has **no native forms**. 
- **Solution:** Use an embeddable form tool like Tally.so, Typeform, Formspree, or a custom API route on your backend. You paste their embed code directly into a Ghost HTML card in the editor, or hardcode it into a `custom-contact.hbs` template.

### Cookie Consent
Ghost has no native cookie consent.
- **Solution:** Add a lightweight JS cookie consent script (like Cookiebot or standard open-source cookie consent JS) into the **Code Injection** (Site Header) in the Ghost Admin, or bake it into the theme.

### Membership/Newsletter (Portal)
Ghost has a built-in membership system called Portal.
- It provides native Stripe integration and email newsletters.
- By adding data attributes to links (e.g., `data-portal="signup"`), you trigger Ghost's native modal for email capture.
- If you use Mailchimp or another CRM, you can use Ghost webhooks or Zapier to sync members out.

### SEO
Ghost is excellent at SEO out of the box. 
- `{{ghost_head}}` auto-generates meta titles, descriptions, canonicals, OpenGraph, and Twitter cards based on the post/page data.
- **No extra SEO plugins are needed.**

### Navigation
- Configure navigation in Admin > Settings > Navigation.
- **Primary:** `{{navigation}}` 
- **Secondary:** `{{navigation type="secondary"}}` (often used for footers).

---

## 7. Converting Static HTML to Ghost Theme

### The Practical Steps
1. **Prepare the structure:** Rename `index.html` to `default.hbs`. Move CSS/JS to the `assets/` folder.
2. **Asset paths:** Find all `<link href="style.css">` and `<img src="...">` and `<script src="...">`. Replace them with Handlebars helpers:
   ```html
   <!-- Before -->
   <link rel="stylesheet" href="/css/style.css">
   <img src="/images/logo.png">
   
   <!-- After -->
   <link rel="stylesheet" href="{{asset "css/style.css"}}">
   <img src="{{asset "images/logo.png"}}">
   ```
3. **Inject Ghost Hooks:** Add `{{ghost_head}}` right before `</head>` and `{{ghost_foot}}` right before `</body>`.
4. **Isolate Content:** Take the main content area of the HTML (between the header and footer) and replace it with `{{{body}}}`. 
5. **Create Page Templates:** Move the extracted main content into `page.hbs` or `home.hbs`, replacing static text with `{{content}}` or other helpers.
6. **Images:** Distinguish between **theme assets** (logos, background patterns — use `{{asset}}`) and **content images** (blog post headers — uploaded via Ghost Admin, rendered automatically in `{{content}}` or via `{{feature_image}}`).

### Common Gotchas
- **Forgetting `{{ghost_head}}`/`{{ghost_foot}}`:** Site will look fine, but Portal, SEO, and admin injections will completely break.
- **Hardcoding URLs:** Use `{{@site.url}}` instead of hardcoding `https://avenira.ai` so the theme is perfectly portable between the English and French instances.
- **Asset Caching:** Always use the `{{asset}}` helper. It appends a version hash (`?v=xxxx`) so updates bust the browser cache immediately.
