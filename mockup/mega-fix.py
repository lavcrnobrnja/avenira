import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# 1. FIX NAV JUMP
with open("css/style.css", "r") as f:
    css = f.read()

# Replace .nav-links a padding
css = re.sub(
    r'\.nav-links a \{\s*color: var\(--text-secondary\);\s*font-size: 14px;\s*font-weight: 500;\s*text-decoration: none;\s*transition: color var\(--transition-base\);\s*padding: 8px 0;\s*\}',
    '.nav-links a {\n  color: var(--text-secondary);\n  font-size: 14px;\n  font-weight: 500;\n  text-decoration: none;\n  transition: all var(--transition-base);\n  padding: 6px 14px;\n  border-radius: var(--radius-full);\n}',
    css
)

# 2. FIX PAIN POINTS
pain_css = """
/* PAIN POINTS REDESIGN */
.pain-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}
.pain-item {
  display: flex;
  flex-direction: column;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.pain-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}
.pain-number {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-orange);
  margin-bottom: 0.5rem;
  font-family: 'Inter', sans-serif;
  letter-spacing: 0.05em;
}
.pain-text {
  font-size: 1.25rem;
  color: var(--text-primary);
  line-height: 1.5;
  font-weight: 400;
}
@media (min-width: 768px) {
  .pain-item {
    flex-direction: row;
    align-items: baseline;
    gap: 3rem;
  }
  .pain-number {
    flex: 0 0 40px;
    margin-bottom: 0;
  }
}
"""

css = re.sub(r'\.pain-list \{.*?(?=\/\*|\Z)', pain_css, css, flags=re.DOTALL)

with open("css/style.css", "w") as f:
    f.write(css)

# 3. FIX FOUNDERS TEXT (Issue #5)
shared_en = """        </div>
        <div class="founders-shared" style="text-align: center; max-width: 600px; margin: 40px auto 0; font-size: 1.125rem; color: var(--text-secondary);">
          <p>Over 20 years of experience in tech — cloud, web/mobile dev, and applied automation.</p>
        </div>"""

shared_fr = """        </div>
        <div class="founders-shared" style="text-align: center; max-width: 600px; margin: 40px auto 0; font-size: 1.125rem; color: var(--text-secondary);">
          <p>Plus de 20 ans d'expérience en technologie — cloud, développement web/mobile et automatisation appliquée.</p>
        </div>"""

for f_path, shared in [("about.html", shared_en), ("fr/a-propos.html", shared_fr)]:
    with open(f_path, "r") as f:
        html = f.read()
    
    # Strip any old attempt first
    html = re.sub(r'<div class="founders-shared".*?</div>', '', html, flags=re.DOTALL)
    
    # Inject properly after founders-grid ends
    html = html.replace('        </div>\n        \n      </div>\n    </section>', f'{shared}\n      </div>\n    </section>')
    
    with open(f_path, "w") as f:
        f.write(html)

print("Applied CSS changes, pain points design, and founders text.")
