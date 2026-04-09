import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# For index.html and fr/index.html
for file in ["index.html", "fr/index.html"]:
    with open(file, "r") as f:
        html = f.read()
    
    # We want to keep the content but change the structure.
    # The structure currently is: <div class="pain-item"> ... <div class="pain-content"> ... <p class="pain-text">Text</p>
    
    # Let's replace the whole container contents.
    
    start_tag = '<section class="section pain-points wash-orange" id="problems">'
    end_tag = '<!-- ===== SERVICES ===== -->'
    
    start_idx = html.find(start_tag)
    end_idx = html.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        if file == "index.html":
            new_html = """<!-- ===== PAIN POINTS ===== -->
    <section class="section pain-points wash-orange" id="problems">
      <div class="container">
        <div class="text-center" style="margin-bottom:48px;">
          <p class="section-label">Sound familiar?</p>
          <h2 class="section-title">The Problems You Live With Every Day</h2>
        </div>

        <div class="pain-grid">
          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </div>
            <p class="pain-text">Your team spends hours copying data between systems and chasing invoices.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            </div>
            <p class="pain-text">A lead fills out your form at 10pm. By 9am, they've called your competitor.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            </div>
            <p class="pain-text">You've been trying to hire an admin for three months. Still open.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            </div>
            <p class="pain-text">You're paying skilled professionals to do data entry.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            </div>
            <p class="pain-text">You know there's a better way — you just don't know where to start.</p>
          </div>
        </div>

        <div class="pain-transition text-center" style="margin-top:48px;">
          <p>These are exactly the problems we solve.</p>
        </div>
      </div>
    </section>

    """
        else:
            new_html = """<!-- ===== PAIN POINTS ===== -->
    <section class="section pain-points wash-orange" id="problems">
      <div class="container">
        <div class="text-center" style="margin-bottom:48px;">
          <p class="section-label">Ça vous semble familier?</p>
          <h2 class="section-title">Les problèmes avec lesquels vous vivez tous les jours</h2>
        </div>

        <div class="pain-grid">
          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </div>
            <p class="pain-text">Votre équipe passe des heures à copier des données entre systèmes et courir après les factures.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            </div>
            <p class="pain-text">Un prospect remplit votre formulaire à 22h. À 9h, il a déjà appelé votre compétiteur.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            </div>
            <p class="pain-text">Vous essayez d'embaucher un adjoint depuis trois mois. Toujours ouvert.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
            </div>
            <p class="pain-text">Vous payez des professionnels qualifiés pour faire de la saisie de données.</p>
          </div>

          <div class="pain-card">
            <div class="pain-icon">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            </div>
            <p class="pain-text">Vous savez qu'il y a une meilleure façon de faire — vous ne savez juste pas par où commencer.</p>
          </div>
        </div>

        <div class="pain-transition text-center" style="margin-top:48px;">
          <p>Ce sont exactement les problèmes que nous résolvons.</p>
        </div>
      </div>
    </section>

    """
            
        full_html = html[:start_idx] + new_html + html[end_idx:]
        with open(file, "w") as f:
            f.write(full_html)
        print("Updated", file)

# Update CSS
with open("css/style.css", "r") as f:
    css = f.read()

# Replace .pain-item block with .pain-grid block
start_css = css.find(".pain-item {")
end_css = css.find(".services-grid {")

if start_css != -1 and end_css != -1:
    new_css = """.pain-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}
.pain-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 24px;
  display: flex;
  align-items: flex-start;
  gap: 16px;
}
/* Make the 5th item span full width or center */
.pain-card:last-child {
  grid-column: 1 / -1;
  max-width: 600px;
  margin: 0 auto;
}

.pain-icon {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: rgba(249, 115, 22, 0.08);
  border: 1px solid rgba(249, 115, 22, 0.15);
}
.pain-icon .icon { width: 24px; height: 24px; color: var(--color-orange); }

.pain-text {
  font-size: 1.05rem;
  color: var(--text-primary);
  font-weight: 500;
  line-height: 1.5;
  margin-top: 10px;
}

.pain-transition p {
  font-size: 1.25rem;
  color: var(--color-orange);
  font-weight: 600;
}

/* ============================================
   SERVICES GRID
   ============================================ */
"""
    # Replace from start_css to end_css - 100
    # Wait, better to just cut out the whole block
    actual_end = css.find("/* ====", start_css)
    full_css = css[:start_css] + new_css + css[actual_end:]
    
    # Also remove media queries for .pain-item
    mq_start = full_css.find(".pain-item {", actual_end)
    if mq_start != -1:
        mq_end = full_css.find("  .founders-grid {", mq_start)
        full_css = full_css[:mq_start] + "  .pain-grid { grid-template-columns: 1fr; }\n  .pain-card:last-child { grid-column: 1 / -1; }\n" + full_css[mq_end:]

    with open("css/style.css", "w") as f:
        f.write(full_css)
    print("Updated CSS")
