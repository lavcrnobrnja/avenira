import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

svg1 = """<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-blue)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-width: 200px; margin: 0 auto; display: block; opacity: 0.9;">
  <circle cx="11" cy="11" r="8"></circle>
  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
  <line x1="11" y1="8" x2="11" y2="14"></line>
  <line x1="8" y1="11" x2="14" y2="11"></line>
</svg>"""

svg2 = """<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-orange)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-width: 200px; margin: 0 auto; display: block; opacity: 0.9;">
  <polygon points="12 2 2 7 12 12 22 7 12 2"></polygon>
  <polyline points="2 17 12 22 22 17"></polyline>
  <polyline points="2 12 12 17 22 12"></polyline>
</svg>"""

svg3 = """<svg viewBox="0 0 24 24" fill="none" stroke="var(--color-green, #059669)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-width: 200px; margin: 0 auto; display: block; opacity: 0.9;">
  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
  <polyline points="22 4 12 14.01 9 11.01"></polyline>
</svg>"""

for file in ["services.html", "fr/services.html"]:
    with open(file, "r") as f:
        html = f.read()

    # We need to find all 3 <div class="service-visual"> blocks and replace their contents
    blocks = re.findall(r'<div class="service-visual"[^>]*>.*?</div>\s*</div>', html, flags=re.DOTALL)
    
    if len(blocks) >= 3:
        # Step 1
        html = html.replace(blocks[0], f'<div class="service-visual" aria-hidden="true">\n{svg1}\n</div>\n</div>')
        # Step 2
        html = html.replace(blocks[1], f'<div class="service-visual" aria-hidden="true">\n{svg2}\n</div>\n</div>')
        # Step 3
        html = html.replace(blocks[2], f'<div class="service-visual" aria-hidden="true">\n{svg3}\n</div>\n</div>')
        
    with open(file, "w") as f:
        f.write(html)
        
print("Updated all 3 steps SVGs.")
