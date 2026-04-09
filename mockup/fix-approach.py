import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# Update Approach #6 in about.html and fr/a-propos.html
for filepath, en_text, fr_text in [
    ("about.html", 
     "<span>Measure and optimize. We track time saved and refine processes to maximize your ROI.</span>", 
     "<span>Mesurer et optimiser. Nous suivons le temps gagné et affinons les processus pour maximiser votre ROI.</span>")
]:
    # English
    with open("about.html", "r") as f:
        html = f.read()
    html = re.sub(r'<span><strong>Security &amp; Privacy\.</strong>.*?</span>', "<span>Measure and optimize. We track time saved and refine processes to maximize your ROI.</span>", html, flags=re.DOTALL)
    with open("about.html", "w") as f:
        f.write(html)
        
    # French
    with open("fr/a-propos.html", "r") as f:
        fhtml = f.read()
    fhtml = re.sub(r'<span><strong>Sécurité et confidentialité\.</strong>.*?</span>', "<span>Mesurer et optimiser. Nous suivons le temps gagné et affinons les processus pour maximiser votre ROI.</span>", fhtml, flags=re.DOTALL)
    with open("fr/a-propos.html", "w") as f:
        f.write(fhtml)

print("Updated Approach Grid #6")
