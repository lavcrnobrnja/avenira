import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# Elegant, subtle, native-looking tech icons
svg1 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: var(--color-blue-light); opacity: 0.8; margin-bottom: 24px;">
  <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
</svg>"""

svg2 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: var(--color-blue-light); opacity: 0.8; margin-bottom: 24px;">
  <polygon points="12 2 2 7 12 12 22 7 12 2"/>
  <polyline points="2 17 12 22 22 17"/>
  <polyline points="2 12 12 17 22 12"/>
</svg>"""

svg3 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: var(--color-blue-light); opacity: 0.8; margin-bottom: 24px;">
  <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
  <path d="M7 11V7a5 5 0 0 1 9.9-1"/>
</svg>"""

# Wait, SVG 1 is a dollar sign? Audit is about discovering value.
svg1 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: rgba(255,255,255,0.6); margin-bottom: 24px;">
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
  <line x1="11" y1="8" x2="11" y2="14"/>
  <line x1="8" y1="11" x2="14" y2="11"/>
</svg>"""

svg2 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: rgba(255,255,255,0.6); margin-bottom: 24px;">
  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
  <line x1="8" y1="21" x2="16" y2="21"/>
  <line x1="12" y1="17" x2="12" y2="21"/>
</svg>"""

svg3 = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" style="width: 48px; height: 48px; color: rgba(255,255,255,0.6); margin-bottom: 24px;">
  <path d="M21 2v6h-6"/>
  <path d="M3 12a9 9 0 0 1 15-6.7L21 8"/>
  <path d="M3 22v-6h6"/>
  <path d="M21 12a9 9 0 0 1-15 6.7L3 16"/>
</svg>"""

for file in ["services.html", "fr/services.html"]:
    with open(file, "r") as f:
        html = f.read()

    blocks = re.findall(r'<div class="service-visual"[^>]*>.*?</div>\s*</div>', html, flags=re.DOTALL)
    
    if len(blocks) >= 3:
        # Instead of big massive images, let's just make them small elegant icons that sit ABOVE the text in the grid.
        # Wait, the current layout uses a whole column for `<div class="service-visual">`.
        # If I want to fix it properly, I should replace `service-visual` with a smaller, elegant UI.
        
        # Let's change the layout to be one-column per service if we do this, OR just put a beautiful small icon in the visual box.
        html = html.replace(blocks[0], f'<div class="service-visual" style="display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:12px; min-height:200px;" aria-hidden="true">\n{svg1}\n</div>\n</div>')
        html = html.replace(blocks[1], f'<div class="service-visual" style="display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:12px; min-height:200px;" aria-hidden="true">\n{svg2}\n</div>\n</div>')
        html = html.replace(blocks[2], f'<div class="service-visual" style="display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.05); border-radius:12px; min-height:200px;" aria-hidden="true">\n{svg3}\n</div>\n</div>')
        
    with open(file, "w") as f:
        f.write(html)
        
print("Updated SVGs to elegant native style.")
