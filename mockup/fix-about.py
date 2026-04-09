import os

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

# Update about.html
with open("about.html", "r") as f:
    html = f.read()

html = html.replace(
    "<span>Security &amp; Privacy First. Your data stays yours. We build compliant workflows that respect Loi 25 and protect your business information.</span>",
    "<span><strong>Security &amp; Privacy.</strong> Loi 25 Compliant. We build secure, private workflows that protect your data.</span>"
)

with open("about.html", "w") as f:
    f.write(html)

# Update fr/a-propos.html
with open("fr/a-propos.html", "r") as f:
    fhtml = f.read()

fhtml = fhtml.replace(
    "<span>Sécurité et confidentialité d'abord. Vos données restent les vôtres. Nous construisons des flux de travail conformes à la Loi 25 qui protègent vos informations.</span>",
    "<span><strong>Sécurité et confidentialité.</strong> Conforme à la Loi 25. Des processus sécurisés qui protègent vos données.</span>"
)

with open("fr/a-propos.html", "w") as f:
    f.write(fhtml)

print("About pages updated.")
