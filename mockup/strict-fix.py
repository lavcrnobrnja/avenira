import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

for f_path in [os.path.join(dp, f) for dp, dn, fn in os.walk('.') for f in fn if f.endswith('.html')]:
    with open(f_path, 'r') as file:
        html = file.read()
    
    # Fully nuke nav-cta
    html = re.sub(r'class="nav-cta"\s*', '', html)
    html = re.sub(r'\s*class="nav-cta"', '', html)
    
    with open(f_path, 'w') as file:
        file.write(html)
        
print("Stripped nav-cta from all HTML.")
