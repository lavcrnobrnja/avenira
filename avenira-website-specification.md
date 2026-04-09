# Website Specification — Avenira Automations / Avenira Automatisations

> **Platform:** Ghost
> **Languages:** Bilingual — English + French (Québécois), both from day one
> **Target Market:** SMBs in Montreal, Quebec, expandable to Canada/North America
> **No pricing displayed** — all services lead to a consultation

---

## Brand & Design Direction

### Tone
Professional, approachable, confident. This is a business that speaks to business owners in their language — not tech jargon, not startup hype. Think "trusted advisor" rather than "agency." The design should feel clean, modern, and credible. Not flashy. Not corporate. The kind of site a 45-year-old construction company owner or a clinic manager would trust instantly.

### Name
- **English:** Avenira Automations
- **French:** Avenira Automatisations
- The language toggle should switch between the two where the name appears contextually (e.g., in page copy), but the logo/brand mark can use a single version if preferred.

### Language Rules (Apply to ALL Pages)
- Never lead with "AI" or "agents" in headlines. Lead with the business problem or outcome.
- "AI" can appear in body copy and deeper explanation sections, never as the hook.
- Use "automation," "automated workflows," "systems that work for you" — plain language.
- Never name specific tools, platforms, or AI models in customer-facing content. No Make, no Zapier, no n8n, no Claude, no GPT, no OpenAI. The customer doesn't care what's under the hood. They care that it works.
- Avoid: "agentic," "LLM," "machine learning," "neural networks," "orchestration," "multi-agent," "framework," "API."
- Allowed: "AI-powered," "intelligent automation," "smart systems" — sparingly, in supporting text only.
- Always frame in terms of what the business owner gets: time back, fewer missed leads, faster payments, less manual work.

### Bilingual Implementation
- Two Ghost instances (one EN, one FR) sharing the same theme, with a language toggle in the header that links between corresponding pages.
- All pages, posts, CTAs, and forms must exist in both languages. Not machine-translated — properly localized Québécois French.

---

## Site Structure — Pages

### 1. Homepage

**URL:** `/` (with language toggle to `/fr`)

**Purpose:** Hook visitors immediately with a clear value proposition. Get them to either explore services or book a consultation.

**Sections (in order):**

#### Hero Section
- **Headline (EN):** "Stop Doing Work Your Systems Should Handle"
- **Headline (FR):** "Arrêtez de faire le travail que vos systèmes devraient faire"
- **Subheadline (EN):** "We automate the repetitive tasks that slow your team down — so you can focus on the work that actually grows your business."
- **Subheadline (FR):** "Nous automatisons les tâches répétitives qui ralentissent votre équipe — pour que vous puissiez vous concentrer sur ce qui fait réellement croître votre entreprise."
- **Primary CTA button:** "Book a Free Consultation" / "Réservez une consultation gratuite"
- **Secondary CTA:** "See How It Works" / "Voir comment ça fonctionne" (scrolls to the process section)
- **Trust signal below CTA:** "Quebec government grants can cover up to 50% of your project. We'll help you apply." / "Les subventions du gouvernement du Québec peuvent couvrir jusqu'à 50% de votre projet. Nous vous aidons à faire la demande."

#### Problem Section — "Sound Familiar?"
A set of 4-5 pain points presented as short scenarios. Each one should feel like the business owner wrote it. Styled as cards or a stacked list with visual emphasis.

**Content (EN):**
- "Your team spends hours every week copying information between systems, sending follow-up emails, and chasing invoices."
- "A lead fills out your website form at 10pm. By the time someone follows up at 9am, they've already called your competitor."
- "You've been trying to hire an admin for three months. The position is still open."
- "You're paying skilled professionals to do data entry, scheduling, and inbox management."
- "You know there's a better way — you just don't know where to start."

**Content (FR):**
- "Votre équipe passe des heures chaque semaine à copier des informations entre systèmes, envoyer des courriels de suivi et courir après les factures."
- "Un prospect remplit votre formulaire à 22h. Le temps qu'on le rappelle à 9h, il a déjà appelé votre compétiteur."
- "Vous essayez d'embaucher un adjoint administratif depuis trois mois. Le poste est toujours ouvert."
- "Vous payez des professionnels qualifiés pour faire de la saisie de données, de la planification et de la gestion de boîte courriel."
- "Vous savez qu'il y a une meilleure façon de faire — vous ne savez juste pas par où commencer."

Followed by a transition line: "These are exactly the problems we solve." / "Ce sont exactement les problèmes que nous résolvons."

#### What We Automate Section
6 cards or tiles, each with an icon, a short title, and 2-3 sentences. Present as outcomes, not technology.

**Cards (EN):**

1. **Lead Response & Follow-Up**
   "When someone contacts your business, our systems respond in under a minute — day or night. Leads get qualified automatically, your CRM gets updated, and appointments get booked. Your team only talks to people who are ready to buy."

2. **Appointment Scheduling & Reminders**
   "Clients book directly into your calendar. They get confirmations and reminders automatically. No-shows drop. Your phone stops ringing for routine bookings. Perfect for clinics, trades, and professional services."

3. **Invoicing & Payment Collection**
   "Invoices go out the moment a job is done or a milestone is hit. Reminders follow on day 7, 14, and 30. Payments get reconciled automatically. You stop chasing money and start collecting it."

4. **Customer Support & Intake**
   "Common questions get answered instantly from your knowledge base. Complex issues get routed to the right person with full context. Your team handles the 20% that needs a human — the system handles the rest."

5. **Content & Marketing**
   "Blog posts, social updates, and email campaigns get drafted automatically based on your industry and audience. Your team reviews and approves. You go from posting once a month to once a week — without hiring anyone."

6. **Document Processing & Data Entry**
   "Vendor invoices, receipts, contracts, and forms get read, extracted, and entered into your systems automatically. No more manual data entry. No more copy-paste between apps."

Each card should have a small CTA: "Learn more →" linking to a relevant blog post or detailed section on the services page.

**Cards (FR):**

1. **Réponse aux prospects et suivi**
   "Quand quelqu'un contacte votre entreprise, nos systèmes répondent en moins d'une minute — jour et nuit. Les prospects sont qualifiés automatiquement, votre CRM est mis à jour et les rendez-vous sont pris. Votre équipe ne parle qu'aux gens prêts à acheter."

2. **Prise de rendez-vous et rappels**
   "Vos clients réservent directement dans votre calendrier. Ils reçoivent des confirmations et des rappels automatiquement. Les absences diminuent. Votre téléphone arrête de sonner pour les réservations de routine. Parfait pour les cliniques, les métiers et les services professionnels."

3. **Facturation et recouvrement**
   "Les factures partent dès qu'un travail est terminé ou qu'une étape est franchie. Les rappels suivent aux jours 7, 14 et 30. Les paiements sont réconciliés automatiquement. Vous arrêtez de courir après l'argent et vous commencez à le recevoir."

4. **Support client et accueil**
   "Les questions courantes obtiennent une réponse instantanée à partir de votre base de connaissances. Les cas complexes sont acheminés à la bonne personne avec tout le contexte. Votre équipe gère le 20% qui nécessite un humain — le système gère le reste."

5. **Contenu et marketing**
   "Articles de blogue, publications sur les réseaux sociaux et campagnes de courriels sont rédigés automatiquement selon votre industrie et votre audience. Votre équipe révise et approuve. Vous passez d'une publication par mois à une par semaine — sans embaucher personne."

6. **Traitement de documents et saisie de données**
   "Factures de fournisseurs, reçus, contrats et formulaires sont lus, extraits et entrés dans vos systèmes automatiquement. Plus de saisie manuelle. Plus de copier-coller entre applications."

#### How It Works Section — The Process
A simple 3-step visual (timeline or numbered steps):

**Step 1: Automation Audit / Audit d'automatisation**
- EN: "We spend two weeks understanding how your business actually works. We map your processes, identify where time and money are being wasted, and deliver a prioritized plan showing exactly what to automate first — and what return you can expect."
- FR: "Nous passons deux semaines à comprendre comment votre entreprise fonctionne réellement. Nous cartographions vos processus, identifions où le temps et l'argent sont gaspillés, et livrons un plan priorisé montrant exactement quoi automatiser en premier — et quel rendement vous pouvez espérer."

**Step 2: Build & Deploy / Construction et déploiement**
- EN: "We build your automated workflows using proven, industry-standard tools. Everything gets tested, documented, and your team gets trained. Most single workflows go live in two weeks. You own everything we build."
- FR: "Nous construisons vos flux de travail automatisés avec des outils éprouvés et reconnus dans l'industrie. Tout est testé, documenté, et votre équipe est formée. La plupart des flux individuels sont en production en deux semaines. Vous êtes propriétaire de tout ce que nous construisons."

**Step 3: Optimize & Expand / Optimisation et expansion**
- EN: "Once your automations are running, we monitor them, fix anything that breaks, and continuously improve performance. As you see results, we help you identify and automate the next workflow. The gains compound over time."
- FR: "Une fois vos automatisations en marche, nous les surveillons, corrigeons tout problème et améliorons continuellement la performance. À mesure que vous voyez les résultats, nous vous aidons à identifier et automatiser le prochain flux de travail. Les gains se composent avec le temps."

#### Grant / Funding Callout Section
Full-width banner or distinct colored section. Major visual emphasis — this is a key differentiator.

- **Headline (EN):** "Quebec Will Pay For Up to Half of This"
- **Headline (FR):** "Le Québec peut payer jusqu'à la moitié de votre projet"
- **Body (EN):** "Most Quebec business owners don't know that government programs like ESSOR and OTN can cover 25-50% of the cost of automation projects. We help you identify the right programs, prepare the applications, and maximize your funding. Two out of three Quebec SMBs miss out on this money simply because they don't know it exists. Don't be one of them."
- **Body (FR):** "La plupart des propriétaires d'entreprises au Québec ne savent pas que des programmes gouvernementaux comme ESSOR et OTN peuvent couvrir 25 à 50% du coût des projets d'automatisation. Nous vous aidons à identifier les bons programmes, préparer les demandes et maximiser votre financement. Deux PME québécoises sur trois passent à côté de cet argent simplement parce qu'elles ne savent pas qu'il existe. Ne soyez pas l'une d'elles."
- **CTA:** "Find Out If You Qualify" / "Découvrez si vous êtes admissible" → links to the Grants page

#### Industries We Serve Section
Three columns or cards:

**Professional Services / Services professionnels**
- EN: "Consulting firms, accounting firms, law offices, marketing agencies. You run on client relationships, but admin work eats your billable hours. We automate client onboarding, follow-ups, invoicing, and reporting so your team bills more and manages less."
- FR: "Cabinets de conseil, comptables, bureaux d'avocats, agences marketing. Votre entreprise repose sur les relations clients, mais le travail administratif gruge vos heures facturables. Nous automatisons l'accueil des clients, les suivis, la facturation et les rapports pour que votre équipe facture plus et gère moins."

**Healthcare & Clinics / Santé et cliniques**
- EN: "Dental clinics, physio practices, medical offices, mental health professionals. You can't hire enough front-desk staff, but your patients still expect fast responses and smooth booking. We automate scheduling, intake, reminders, and patient communication."
- FR: "Cliniques dentaires, cabinets de physiothérapie, bureaux médicaux, professionnels en santé mentale. Vous n'arrivez pas à embaucher assez de personnel à la réception, mais vos patients s'attendent à des réponses rapides et une prise de rendez-vous fluide. Nous automatisons la planification, l'accueil, les rappels et la communication avec les patients."

**Construction & Trades / Construction et métiers**
- EN: "General contractors, electricians, plumbers, HVAC companies. Quoting, scheduling, invoicing, and compliance paperwork eat your days. We connect your systems so information flows automatically from estimate to invoice."
- FR: "Entrepreneurs généraux, électriciens, plombiers, compagnies de CVC. La soumission, la planification, la facturation et la paperasse de conformité dévorent vos journées. Nous connectons vos systèmes pour que l'information circule automatiquement de l'estimation à la facture."

Below: "We work with businesses across all industries. These are where we see the fastest results." / "Nous travaillons avec des entreprises de toutes les industries. C'est là où nous voyons les résultats les plus rapides."

#### Final CTA Section
- **Headline (EN):** "Ready to Stop Doing Work Your Systems Should Handle?"
- **Headline (FR):** "Prêt à arrêter de faire le travail que vos systèmes devraient faire?"
- **Subhead (EN):** "Book a free 30-minute consultation. We'll walk through your operations and tell you exactly where automation would have the biggest impact — no commitment, no jargon."
- **Subhead (FR):** "Réservez une consultation gratuite de 30 minutes. Nous passerons en revue vos opérations et vous dirons exactement où l'automatisation aurait le plus grand impact — sans engagement, sans jargon."
- **CTA Button:** "Book Your Free Consultation" / "Réservez votre consultation gratuite"

---

### 2. Services Page

**URL:** `/services` / `/fr/services`

**Purpose:** Detailed explanation of each service. No pricing — every section ends with a CTA to get in touch.

#### Page Intro
- EN: "Every business runs differently. But the ones that grow fastest have one thing in common: they stop wasting their team's time on work that machines should do. Here's how we help you get there."
- FR: "Chaque entreprise fonctionne différemment. Mais celles qui croissent le plus vite ont une chose en commun : elles arrêtent de gaspiller le temps de leur équipe sur du travail que des machines devraient faire. Voici comment nous vous aidons à y arriver."

#### Service 1: Automation Audit / Audit d'automatisation
**Tagline (EN):** "Find out where you're bleeding time and money"
**Tagline (FR):** "Découvrez où vous perdez du temps et de l'argent"

**What it is (EN):** "A comprehensive, two-week deep dive into how your business actually operates. We map your key processes, talk to your team, and identify the workflows where automation will have the biggest impact."

**What it is (FR):** "Une analyse approfondie de deux semaines sur le fonctionnement réel de votre entreprise. Nous cartographions vos processus clés, parlons à votre équipe et identifions les flux de travail où l'automatisation aura le plus grand impact."

**What you get (EN):**
- A visual map of your current processes and where bottlenecks live
- A prioritized list of 3-5 automation opportunities ranked by expected return
- Estimated time savings and cost impact for each opportunity
- A recommended implementation timeline
- A grant eligibility assessment — we identify which Quebec programs can fund your project and help you apply

**What you get (FR):**
- Une carte visuelle de vos processus actuels et de vos goulots d'étranglement
- Une liste priorisée de 3 à 5 opportunités d'automatisation classées par rendement attendu
- Les économies de temps et l'impact financier estimés pour chaque opportunité
- Un calendrier de mise en œuvre recommandé
- Une évaluation d'admissibilité aux subventions — nous identifions quels programmes québécois peuvent financer votre projet et nous vous aidons à faire la demande

**Who it's for (EN):** "Business owners who know they're wasting time on manual work but aren't sure what to automate first or how to start."
**Who it's for (FR):** "Les propriétaires d'entreprises qui savent qu'ils perdent du temps sur du travail manuel mais ne savent pas quoi automatiser en premier ni comment commencer."

**Timeline:** "Two weeks from kickoff to delivered report." / "Deux semaines du coup d'envoi au rapport livré."

**Note about grants (EN):** "This service qualifies as a 'digital diagnostic' under Quebec's ESSOR program, which can cover up to 50% of the cost. We handle the grant application process for you."
**Note about grants (FR):** "Ce service se qualifie comme un « diagnostic numérique » dans le cadre du programme ESSOR du Québec, qui peut couvrir jusqu'à 50% du coût. Nous gérons le processus de demande de subvention pour vous."

**CTA:** "Get in touch to discuss an Automation Audit" / "Contactez-nous pour discuter d'un audit d'automatisation"

#### Service 2: Workflow Build / Construction de flux de travail
**Tagline (EN):** "We build it. You run it. You own it."
**Tagline (FR):** "Nous le construisons. Vous l'opérez. Vous en êtes propriétaire."

**What it is (EN):** "We design, build, test, and deploy automated workflows that connect your existing tools and eliminate manual steps. Everything runs on industry-standard platforms — no proprietary lock-in. You own everything we build."

**What it is (FR):** "Nous concevons, construisons, testons et déployons des flux de travail automatisés qui connectent vos outils existants et éliminent les étapes manuelles. Tout fonctionne sur des plateformes reconnues dans l'industrie — aucun verrouillage propriétaire. Vous êtes propriétaire de tout ce que nous construisons."

**What's included (EN):**
- Workflow design and architecture
- Integration with your existing tools (CRM, email, calendar, accounting software, etc.)
- Thorough testing before go-live
- Team training — your people learn how to manage and adjust the system
- Full documentation — every workflow is documented so you understand exactly what it does
- 30 days of post-launch support

**What's included (FR):**
- Conception et architecture du flux de travail
- Intégration avec vos outils existants (CRM, courriel, calendrier, logiciel comptable, etc.)
- Tests rigoureux avant la mise en production
- Formation de votre équipe — vos gens apprennent à gérer et ajuster le système
- Documentation complète — chaque flux de travail est documenté pour que vous compreniez exactement ce qu'il fait
- 30 jours de support après le lancement

**Examples of workflows we build (EN):**
- Lead comes in → qualified automatically → CRM updated → appointment booked → follow-up sequence triggered
- Job completed → invoice generated → sent to client → reminders on schedule → payment reconciled
- Support email received → categorized → routine questions answered automatically → complex issues routed to the right person
- Vendor invoice arrives → data extracted → categorized → entered in accounting software → ready for approval

**Examples (FR):**
- Un prospect arrive → qualifié automatiquement → CRM mis à jour → rendez-vous réservé → séquence de suivi déclenchée
- Travail complété → facture générée → envoyée au client → rappels programmés → paiement réconcilié
- Courriel de support reçu → catégorisé → questions courantes répondues automatiquement → cas complexes acheminés à la bonne personne
- Facture fournisseur reçue → données extraites → catégorisées → entrées dans le logiciel comptable → prêtes pour approbation

**CTA:** "Let's talk about what we can build for you" / "Discutons de ce que nous pouvons construire pour vous"

#### Service 3: Automation Retainer / Forfait d'automatisation continue
**Tagline (EN):** "We keep it running and make it better"
**Tagline (FR):** "Nous gardons le tout en marche et l'améliorons"

**What it is (EN):** "Once your automations are live, we monitor them, maintain them, and continuously improve them. We also build new automations as your needs evolve."

**What it is (FR):** "Une fois vos automatisations en production, nous les surveillons, les maintenons et les améliorons continuellement. Nous construisons aussi de nouvelles automatisations à mesure que vos besoins évoluent."

**What's included (EN):**
- Ongoing system monitoring — we catch and fix issues before you notice them
- Monthly performance reporting — you see exactly how much time and money your automations are saving
- Integration maintenance — when third-party tools update, we make sure nothing breaks
- Priority support — when you need something changed or fixed, it gets done fast
- New workflow builds — a budgeted number of hours each month for expanding your automation footprint

**What's included (FR):**
- Surveillance continue des systèmes — nous détectons et corrigeons les problèmes avant que vous ne les remarquiez
- Rapports mensuels de performance — vous voyez exactement combien de temps et d'argent vos automatisations vous font économiser
- Maintenance des intégrations — quand des outils tiers sont mis à jour, nous nous assurons que rien ne brise
- Support prioritaire — quand vous avez besoin d'un changement ou d'une correction, c'est fait rapidement
- Construction de nouveaux flux — un nombre d'heures budgété chaque mois pour étendre votre empreinte d'automatisation

**Who it's for (EN):** "Businesses that already have automations running and want them maintained, optimized, and expanded over time without having to think about it."
**Who it's for (FR):** "Les entreprises qui ont déjà des automatisations en place et veulent qu'elles soient maintenues, optimisées et étendues au fil du temps sans avoir à y penser."

**CTA:** "Get in touch to discuss a retainer" / "Contactez-nous pour discuter d'un forfait continu"

---

### 3. Grants & Funding Page

**URL:** `/grants` / `/fr/subventions`

**Purpose:** Major lead magnet. Many Quebec SMBs will find this page through search and convert because they didn't know this money existed.

**Page Headline (EN):** "Quebec Government Grants Can Pay for Up to Half Your Automation Project"
**Page Headline (FR):** "Les subventions du gouvernement du Québec peuvent couvrir jusqu'à 50% de votre projet d'automatisation"

**Intro (EN):** "Most Quebec businesses don't know that provincial and federal programs exist specifically to fund automation and digital transformation projects. Two out of three SMBs miss out simply because they've never heard of these programs. We help you find the right programs, prepare strong applications, and maximize your funding."

**Intro (FR):** "La plupart des entreprises québécoises ne savent pas que des programmes provinciaux et fédéraux existent spécifiquement pour financer les projets d'automatisation et de transformation numérique. Deux PME sur trois passent à côté simplement parce qu'elles n'ont jamais entendu parler de ces programmes. Nous vous aidons à trouver les bons programmes, préparer des demandes solides et maximiser votre financement."

#### Key Programs Section
Present each program as a card with the program name, who it's for, what it covers, and how much:

**1. ESSOR — Investissement Québec**
- EN: Grants covering up to 50% of expenses for digital diagnostics (max $20,000) and implementation plans (max $50,000). Loans with favorable terms and up to 48 months capital repayment moratorium for equipment and deployment. "This is the most relevant program for automation projects. Our Automation Audit qualifies as a 'digital diagnostic' under this program."
- FR: Subventions couvrant jusqu'à 50% des dépenses pour les diagnostics numériques (max 20 000$) et les plans de mise en œuvre (max 50 000$). Prêts à conditions avantageuses avec un moratoire de remboursement du capital allant jusqu'à 48 mois. "C'est le programme le plus pertinent pour les projets d'automatisation. Notre audit d'automatisation se qualifie comme un « diagnostic numérique » dans le cadre de ce programme."

**2. OTN (Offensive de transformation numérique) via ADRIQ**
- EN: Up to $25,000 (50% of costs) for expert consulting services. "This can directly fund your engagement with us."
- FR: Jusqu'à 25 000$ (50% des coûts) pour des services de consultation d'experts. "Ce programme peut directement financer votre mandat avec nous."

**3. CRIC (Crédit d'impôt relatif à l'investissement et à l'innovation)**
- EN: 30% refundable tax credit on the first $1M of eligible innovation spending. Can be combined with federal SR&ED for up to approximately 58.5% effective assistance. "If your automation project involves custom development or experimentation, this may apply."
- FR: Crédit d'impôt remboursable de 30% sur le premier million de dollars de dépenses d'innovation admissibles. Peut être combiné avec le programme fédéral RS&DE pour une aide effective allant jusqu'à environ 58,5%. "Si votre projet d'automatisation implique du développement sur mesure ou de l'expérimentation, ceci pourrait s'appliquer."

**4. Investissement Québec — Plan PME 2025-2028**
- EN: $494 million earmarked for SME growth across Quebec. Various financing and advisory programs available.
- FR: 494 millions de dollars réservés à la croissance des PME à travers le Québec. Divers programmes de financement et de services-conseils disponibles.

**5. PME MTL (Montreal-specific)**
- EN: Local investment funds, grants, and coaching programs for Montreal-based businesses.
- FR: Fonds d'investissement locaux, subventions et programmes de coaching pour les entreprises basées à Montréal.

#### Important Note
- EN: "Grant programs change regularly. Eligibility depends on your specific situation — industry, company size, project scope, and timing. We research the current landscape for every client and identify the best opportunities. This page reflects programs available as of 2026 and is updated regularly."
- FR: "Les programmes de subventions changent régulièrement. L'admissibilité dépend de votre situation spécifique — industrie, taille de l'entreprise, portée du projet et moment. Nous analysons le paysage actuel pour chaque client et identifions les meilleures opportunités. Cette page reflète les programmes disponibles en 2026 et est mise à jour régulièrement."

#### How We Help With Grants Section
- EN: "You don't need to navigate this alone. As part of every engagement, we assess your eligibility across all relevant programs, help you structure your project to maximize funding, prepare or review your grant applications, and coordinate timelines so your project and funding align. This isn't a separate service — it's built into how we work. When automation costs your business 50% less because the government is funding it, the ROI becomes obvious."
- FR: "Vous n'avez pas à naviguer tout cela seul. Dans le cadre de chaque mandat, nous évaluons votre admissibilité à tous les programmes pertinents, vous aidons à structurer votre projet pour maximiser le financement, préparons ou révisons vos demandes de subventions, et coordonnons les échéanciers pour que votre projet et votre financement soient alignés. Ce n'est pas un service séparé — c'est intégré à notre façon de travailler. Quand l'automatisation coûte 50% moins cher à votre entreprise parce que le gouvernement la finance, le rendement devient évident."

**CTA:** "Find Out What You Qualify For — Book a Free Consultation" / "Découvrez ce à quoi vous avez droit — Réservez une consultation gratuite"

---

### 4. About Page

**URL:** `/about` / `/fr/a-propos`

**Purpose:** Build trust and credibility.

#### The Company
- EN: "Avenira Automations is a Montreal-based workflow automation consultancy. We help small and medium-sized businesses eliminate repetitive manual work by building intelligent automated systems. We believe every business deserves to operate as efficiently as a company ten times its size — and that the tools to make it happen are more accessible and affordable than most people think. What sets us apart: we've built and run production automation systems for our own businesses before we ever offered it as a service. We're not selling theory. We're selling what we've done."
- FR: "Avenira Automatisations est une firme de consultation en automatisation des flux de travail basée à Montréal. Nous aidons les petites et moyennes entreprises à éliminer le travail manuel répétitif en construisant des systèmes automatisés intelligents. Nous croyons que chaque entreprise mérite de fonctionner aussi efficacement qu'une entreprise dix fois sa taille — et que les outils pour y arriver sont plus accessibles et abordables que la plupart des gens ne le pensent. Ce qui nous distingue : nous avons construit et opéré des systèmes d'automatisation en production pour nos propres entreprises avant de l'offrir comme service. Nous ne vendons pas de la théorie. Nous vendons ce que nous avons fait."

#### The Founders
Two cards or two-column layout, each with:

**Lav Crnobrnja**
- Photo
- Title: Co-Founder / Cofondateur
- Shared credential line (see below)

**Arfanuddin Khan**
- Photo
- Title: Co-Founder / Cofondateur
- Shared credential line (see below)

**Shared credential line (placed below both photos, or under each):**
- EN: "With over 20 years of experience in the technology industry — spanning cloud computing, web and mobile development, and artificial intelligence — we've helped businesses of all sizes build and scale the systems that power their growth."
- FR: "Avec plus de 20 ans d'expérience dans l'industrie technologique — incluant l'infonuagique, le développement web et mobile, et l'intelligence artificielle — nous avons aidé des entreprises de toutes tailles à construire et faire croître les systèmes qui alimentent leur développement."

#### Our Approach
- EN: "We don't sell technology. We solve business problems. When you work with us, we start by understanding your operations — not pitching tools. Automation is only valuable when it's applied to the right problem, built on the right tools, and designed to work with your team — not against them."
- FR: "Nous ne vendons pas de la technologie. Nous résolvons des problèmes d'affaires. Quand vous travaillez avec nous, nous commençons par comprendre vos opérations — pas par vous vendre des outils. L'automatisation n'a de valeur que lorsqu'elle est appliquée au bon problème, construite avec les bons outils et conçue pour travailler avec votre équipe — pas contre elle."

Core principles (presented as short flowing statements, not bullet points):
- EN: "We lead with the business problem, not the technology. We build on industry-standard tools — you own everything, no lock-in. We start small and prove the return before expanding. We help you access government funding to reduce your costs. We train your team so you're never dependent on us."
- FR: "Nous partons du problème d'affaires, pas de la technologie. Nous construisons sur des outils reconnus dans l'industrie — vous êtes propriétaire de tout, aucun verrouillage. Nous commençons petit et prouvons le rendement avant d'étendre. Nous vous aidons à accéder aux subventions gouvernementales pour réduire vos coûts. Nous formons votre équipe pour que vous ne soyez jamais dépendant de nous."

---

### 5. Blog

**URL:** `/blog` / `/fr/blogue`

**Purpose:** The primary SEO and content engine. This is where most organic traffic will enter the site.

#### Ghost Setup
- Posts tagged by language (EN / FR) and filtered accordingly
- Posts also tagged by category for navigation:
  - "Guides" / "Guides"
  - "Case Studies" / "Études de cas"
  - "Industry" / "Industrie"
  - "Grants & Funding" / "Subventions"
  - "Insights" / "Perspectives"

#### Initial Content Plan (First 30 Days — 12-15 Posts)

**Priority 1 — Grant/funding content (drives immediate Quebec traffic):**
- "The Complete Guide to Quebec Automation Grants in 2026" / "Le guide complet des subventions d'automatisation au Québec en 2026"
- "ESSOR Explained: How Quebec SMBs Can Get 50% of Their Automation Funded" / "ESSOR expliqué : comment les PME québécoises peuvent financer 50% de leur automatisation"
- "5 Government Programs Quebec Business Owners Don't Know About" / "5 programmes gouvernementaux que les propriétaires d'entreprises québécoises ne connaissent pas"

**Priority 2 — Problem-first guides by industry:**
- "How to Stop Losing Leads to Slow Follow-Up" / "Comment arrêter de perdre des prospects à cause d'un suivi trop lent"
- "The Construction Company's Guide to Automating Quoting and Invoicing" / "Le guide de l'entreprise de construction pour automatiser les soumissions et la facturation"
- "How Montreal Clinics Are Handling More Patients Without Hiring" / "Comment les cliniques montréalaises gèrent plus de patients sans embaucher"
- "5 Workflows Every Professional Services Firm Should Automate" / "5 flux de travail que toute firme de services professionnels devrait automatiser"

**Priority 3 — General automation education:**
- "What to Automate First: A Framework for Business Owners" / "Quoi automatiser en premier : un cadre pour les propriétaires d'entreprises"
- "Automation vs. Hiring: When Each Makes Sense" / "Automatisation vs. embauche : quand chacun a du sens"
- "The Affordable Automation Stack That Replaces a Part-Time Admin" / "L'automatisation abordable qui remplace un adjoint à temps partiel"

**Priority 4 — Quebec market context:**
- "The State of Business Automation in Quebec: 2026" / "L'état de l'automatisation des affaires au Québec : 2026"
- "Why Quebec's Labor Shortage Makes Automation Inevitable" / "Pourquoi la pénurie de main-d'œuvre au Québec rend l'automatisation inévitable"

**Ongoing cadence:** 2-3 posts per week, bilingual. Each post gets translated to the other language within a few days of initial publication.

#### Lead Magnet
Offer a downloadable PDF: "The Quebec Automation Grants Guide 2026" / "Le guide des subventions d'automatisation au Québec 2026" — in exchange for email signup via Ghost's built-in membership/newsletter feature.

---

### 6. Contact Page

**URL:** `/contact` / `/fr/contact`

**Purpose:** Convert visitors into consultation bookings.

**Intro (EN):** "Every engagement starts with a conversation. Get in touch for a free 30-minute consultation and we'll walk through your operations together. No commitment, no jargon — just a clear-eyed look at where automation would make the biggest difference in your business."

**Intro (FR):** "Chaque mandat commence par une conversation. Contactez-nous pour une consultation gratuite de 30 minutes et nous passerons en revue vos opérations ensemble. Sans engagement, sans jargon — juste un regard lucide sur l'endroit où l'automatisation ferait la plus grande différence dans votre entreprise."

**Contact methods:**
- Contact form (name, email, phone, company name, brief message)
- Email address
- Phone number
- Location line: "Montreal, Quebec" / "Montréal, Québec"
- Note: "We work with businesses across Quebec, both in-person and remotely." / "Nous travaillons avec des entreprises partout au Québec, en personne et à distance."

---

## Global Site Elements

### Header / Navigation
- Avenira logo + name (left)
- Nav links: Services | Grants/Subventions | About/À propos | Blog/Blogue | Contact
- Language toggle (EN/FR) — top right
- CTA button in header: "Book a Consultation" / "Réservez une consultation" — visible on all pages, links to Contact page

### Footer
- Avenira Automations / Avenira Automatisations
- "Montreal, Quebec" / "Montréal, Québec"
- Nav links repeated
- Email address
- LinkedIn link
- © 2026 Avenira Automations. All rights reserved. / © 2026 Avenira Automatisations. Tous droits réservés.
- Privacy Policy / Politique de confidentialité (required under Loi 25)
- Language toggle

### Loi 25 / Privacy Compliance
Quebec's privacy law requires a privacy policy page, cookie consent banner with opt-in for non-essential cookies, and a designated person responsible for privacy. Must be implemented from day one.

---

## Content & Messaging Cheat Sheet

### Primary Value Proposition
- EN: "We automate the repetitive tasks that slow your team down."
- FR: "Nous automatisons les tâches répétitives qui ralentissent votre équipe."

### Supporting Messages (use across the site)
- "Focus on the work that actually grows your business." / "Concentrez-vous sur le travail qui fait réellement croître votre entreprise."
- "Quebec grants can cover up to 50% of your automation project." / "Les subventions québécoises peuvent couvrir jusqu'à 50% de votre projet."
- "Most businesses automate the wrong things first. We help you start with what matters." / "La plupart des entreprises automatisent les mauvaises choses en premier. Nous vous aidons à commencer par ce qui compte."
- "You own everything we build. No lock-in, no proprietary platforms." / "Vous êtes propriétaire de tout ce que nous construisons. Aucun verrouillage, aucune plateforme propriétaire."
- "We've automated our own businesses before we ever offered it as a service." / "Nous avons automatisé nos propres entreprises avant de l'offrir comme service."

### Words to Use
Automate, streamline, workflow, systems, processes, efficiency, time savings, ROI, productivity, capacity, scale, focus, simplify, connect, integrate

### Words to Avoid
AI agents, agentic, LLM, machine learning, neural network, orchestration, multi-agent, framework, API, deployment pipeline, inference, tokens, prompts — and never name any specific tools, platforms, or AI models

---

## Launch Sequence

### Phase 1 — MVP Launch (Week 1-2)
- Homepage, Services, Grants, About, Contact pages live in both languages
- 3-5 initial blog posts published (prioritize grant content)
- Contact form working
- Cookie consent and privacy policy live

### Phase 2 — Content Ramp (Week 3-8)
- 2-3 blog posts per week, bilingual
- Email newsletter launched with first subscribers
- Grant guide lead magnet (PDF) live
- Begin sharing content on LinkedIn

### Phase 3 — Optimization (Month 3+)
- First case studies published from initial client engagements
- Review search performance data, double down on what's ranking
- Expand content into additional industries based on traction
- Consider adding a "Resources" page with free templates or calculators
