import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

def fix_nav():
    for f_path in [os.path.join(dp, f) for dp, dn, fn in os.walk('.') for f in fn if f.endswith('.html')]:
        with open(f_path, 'r') as file:
            html = file.read()
        
        # Remove nav-cta class from contact
        html = html.replace('class="nav-cta">Contact', '>Contact')
        html = html.replace('class="nav-cta">Contactez-nous', '>Contactez-nous')
        html = re.sub(r'>Contact\s*<svg class="icon"[^>]*>.*?</svg></a>', '>Contact</a>', html, flags=re.DOTALL)
        html = re.sub(r'>Contactez-nous\s*<svg class="icon"[^>]*>.*?</svg></a>', '>Contactez-nous</a>', html, flags=re.DOTALL)
        
        with open(f_path, 'w') as file:
            file.write(html)
            
    # Fix CSS
    with open('css/style.css', 'r') as file:
        css = file.read()
    
    css = re.sub(r'\.nav-cta\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.nav-cta:hover\s*\{[^}]*\}', '', css)
    css = re.sub(r'\.nav-cta\[aria-current="page"\]\s*\{[^}]*\}', '', css)
    css = css.replace('.nav-links a[aria-current="page"]:not(.nav-cta)', '.nav-links a[aria-current="page"]')
    
    with open('css/style.css', 'w') as file:
        file.write(css)
    print("Fixed Nav")

fix_nav()
