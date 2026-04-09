import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

with open("fr/index.html", "r") as f:
    html = f.read()

start_tag = '<section class="section pain-points wash-orange" id="problemes">'
end_tag = '<section class="section wash-blue" id="services">'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

if start_idx != -1 and end_idx != -1:
    new_html = """<!-- ===== PAIN POINTS ===== -->
    <section class="section pain-points wash-orange" id="problemes">
      <div class="container">
        <div class="text-center" style="margin-bottom:48px;">
          <p class="section-label">Ça vous semble familier?</p>
          <h2 class="section-title">Les problèmes que vous vivez chaque jour</h2>
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

    <!-- ===== SERVICES ===== -->
    """
        
    full_html = html[:start_idx] + new_html + html[end_idx:]
    with open("fr/index.html", "w") as f:
        f.write(full_html)
    print("Updated fr/index.html")
else:
    print("Could not find tags in fr/index.html")
