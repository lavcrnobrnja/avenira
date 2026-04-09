import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# ---------------------------------------------------------
# 1. RETHINK PAIN POINTS (index.html, fr/index.html)
# ---------------------------------------------------------

pain_en = """<!-- ===== PAIN POINTS ===== -->
    <section class="section problem-statement" style="background-color: var(--bg-default); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 120px 0;">
      <div class="container">
        <div style="max-width: 900px; margin: 0 auto;">
          <h2 style="font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; line-height: 1.1; margin-bottom: 48px; letter-spacing: -0.02em; color: var(--text-primary);">
            You are paying human beings to act like APIs.
          </h2>
          
          <div style="border-left: 2px solid var(--color-orange); padding-left: 32px; margin-bottom: 48px;">
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 24px;">Leads cooling off because your team is asleep.</p>
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 24px;">Highly skilled professionals doing data entry instead of deep work.</p>
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 0;">Trying to hire your way out of broken processes.</p>
          </div>

          <p style="font-size: 1.5rem; color: var(--color-blue-light); font-weight: 600;">
            You don't need more staff. You need better plumbing.
          </p>
        </div>
      </div>
    </section>"""

pain_fr = """<!-- ===== PAIN POINTS ===== -->
    <section class="section problem-statement" style="background-color: var(--bg-default); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); padding: 120px 0;">
      <div class="container">
        <div style="max-width: 900px; margin: 0 auto;">
          <h2 style="font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 800; line-height: 1.1; margin-bottom: 48px; letter-spacing: -0.02em; color: var(--text-primary);">
            Vous payez des êtres humains pour agir comme des API.
          </h2>
          
          <div style="border-left: 2px solid var(--color-orange); padding-left: 32px; margin-bottom: 48px;">
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 24px;">Des prospects qui se refroidissent parce que votre équipe dort.</p>
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 24px;">Des professionnels qualifiés qui font de la saisie au lieu de leur vrai métier.</p>
            <p style="font-size: 1.5rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 0;">Essayer d'embaucher pour compenser des processus défaillants.</p>
          </div>

          <p style="font-size: 1.5rem; color: var(--color-blue-light); font-weight: 600;">
            Vous n'avez pas besoin de plus d'employés. Vous avez besoin d'une meilleure plomberie.
          </p>
        </div>
      </div>
    </section>"""

for f_path, pain_html in [("index.html", pain_en), ("fr/index.html", pain_fr)]:
    with open(f_path, "r") as f:
        html = f.read()
    
    html = re.sub(r'<!-- ===== PAIN POINTS ===== -->.*?</section>', pain_html, html, flags=re.DOTALL)
    
    with open(f_path, "w") as f:
        f.write(html)


# ---------------------------------------------------------
# 2. RETHINK SERVICES ICONS (services.html, fr/services.html)
# ---------------------------------------------------------
def make_number_visual(num):
    return f"""<div class="service-visual" style="display:flex; align-items:center; justify-content:center; background:var(--bg-surface); border:1px solid rgba(255,255,255,0.03); border-radius:24px; min-height:400px; position:relative; overflow:hidden;" aria-hidden="true">
  <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); font-size: 24rem; font-weight: 900; line-height: 1; letter-spacing:-0.05em; color: rgba(255,255,255,0.015); user-select:none; z-index:0;">{num}</div>
  <div style="position:relative; z-index:1; font-size: 6rem; font-weight:800; background: linear-gradient(135deg, #ffffff, rgba(255,255,255,0.2)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing:-0.03em;">{num}</div>
</div>"""

for f_path in ["services.html", "fr/services.html"]:
    with open(f_path, "r") as f:
        html = f.read()
        
    blocks = re.findall(r'<div class="service-visual"[^>]*>.*?</div>\s*</div>', html, flags=re.DOTALL)
    if len(blocks) >= 3:
        html = html.replace(blocks[0], make_number_visual("01") + '\n</div>')
        html = html.replace(blocks[1], make_number_visual("02") + '\n</div>')
        html = html.replace(blocks[2], make_number_visual("03") + '\n</div>')
        
    with open(f_path, "w") as f:
        f.write(html)


# ---------------------------------------------------------
# 3. FIX FOUNDERS TEXT (about.html, fr/a-propos.html)
# ---------------------------------------------------------

shared_en_pill = """        <div class="founders-shared" style="text-align: center; max-width: 700px; margin: 64px auto 0; padding: 24px 32px; background: rgba(37, 99, 235, 0.05); border: 1px solid rgba(37, 99, 235, 0.15); border-radius: 100px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
          <p style="font-size: 1.125rem; color: var(--text-primary); margin: 0; font-weight: 500;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px; color: var(--color-blue); margin-right: 8px; vertical-align: -3px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            Over 20 years of experience in tech — cloud, web/mobile dev, and applied automation.
          </p>
        </div>"""

shared_fr_pill = """        <div class="founders-shared" style="text-align: center; max-width: 700px; margin: 64px auto 0; padding: 24px 32px; background: rgba(37, 99, 235, 0.05); border: 1px solid rgba(37, 99, 235, 0.15); border-radius: 100px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
          <p style="font-size: 1.125rem; color: var(--text-primary); margin: 0; font-weight: 500;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px; color: var(--color-blue); margin-right: 8px; vertical-align: -3px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            Plus de 20 ans d'expérience en technologie — cloud, dev web/mobile et automatisation appliquée.
          </p>
        </div>"""

for f_path, pill in [("about.html", shared_en_pill), ("fr/a-propos.html", shared_fr_pill)]:
    with open(f_path, "r") as f:
        html = f.read()
        
    html = re.sub(r'<div class="founders-shared".*?</div>\s*</div>', pill + '\n      </div>', html, flags=re.DOTALL)
    
    with open(f_path, "w") as f:
        f.write(html)
        
print("Successfully applied Round 3 visual fixes.")
