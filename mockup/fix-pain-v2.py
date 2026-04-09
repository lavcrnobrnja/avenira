import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

css_override = """
.pain-list {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.pain-item {
  display: flex;
  align-items: center;
  gap: 24px;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--color-orange);
  padding: 24px 32px;
  border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
  box-shadow: 0 8px 30px rgba(0,0,0,0.15);
  transition: transform 0.2s ease;
}
.pain-item:hover {
  transform: translateX(8px);
}
.pain-number {
  font-size: 32px;
  font-weight: 700;
  color: var(--color-orange);
  opacity: 0.2;
  font-family: var(--font-heading);
}
.pain-text {
  font-size: 1.125rem;
  line-height: 1.6;
  color: var(--text-base);
  margin: 0;
}
"""

with open('css/style.css', 'a') as f:
    f.write(css_override)

def rebuild_pain_points(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # We will regex replace the entire pain-grid
    pain_items_en = """<div class="pain-list">
          <div class="pain-item">
            <span class="pain-number">01</span>
            <p class="pain-text">Your team spends hours copying data between systems and chasing invoices.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">02</span>
            <p class="pain-text">A lead fills out your form at 10pm. By 9am, they've called your competitor.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">03</span>
            <p class="pain-text">You've been trying to hire an admin for three months. Still open.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">04</span>
            <p class="pain-text">You're paying skilled professionals to do data entry.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">05</span>
            <p class="pain-text">You know there's a better way — you just don't know where to start.</p>
          </div>
        </div>"""

    pain_items_fr = """<div class="pain-list">
          <div class="pain-item">
            <span class="pain-number">01</span>
            <p class="pain-text">Votre équipe passe des heures à copier des données entre systèmes et à courir après les factures.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">02</span>
            <p class="pain-text">Un prospect remplit votre formulaire à 22h. À 9h, il a déjà appelé votre concurrent.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">03</span>
            <p class="pain-text">Vous essayez de recruter un(e) adjoint(e) depuis trois mois. Le poste est toujours vacant.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">04</span>
            <p class="pain-text">Vous payez des professionnels qualifiés pour faire de la saisie de données.</p>
          </div>
          <div class="pain-item">
            <span class="pain-number">05</span>
            <p class="pain-text">Vous savez qu'il y a une meilleure façon de faire — vous ne savez juste pas par où commencer.</p>
          </div>
        </div>"""

    if 'fr/' in filepath:
        html = re.sub(r'<div class="pain-grid">.*?</p>\s*</div>\s*</div>', pain_items_fr, html, flags=re.DOTALL)
    else:
        html = re.sub(r'<div class="pain-grid">.*?</p>\s*</div>\s*</div>', pain_items_en, html, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(html)

rebuild_pain_points('index.html')
rebuild_pain_points('fr/index.html')
print("Rebuilt pain points.")
