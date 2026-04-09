import os
import re

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

for file in ["about.html", "fr/a-propos.html"]:
    with open(file, "r") as f:
        html = f.read()

    # Remove the founders-shared block entirely
    html = re.sub(r'<div class="founders-shared">\s*<p>.*?</p>\s*</div>', '', html, flags=re.DOTALL)

    with open(file, "w") as f:
        f.write(html)
    print(f"Fixed {file}")
