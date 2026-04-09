import os

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

simple_svg = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-width: 160px; color: var(--color-blue-light); margin: 0 auto; display: block;">
              <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.92-10.26l5.58-1.31"/>
            </svg>"""

for file in ["services.html", "fr/services.html"]:
    with open(file, "r") as f:
        html = f.read()

    start_idx = html.find('<svg viewBox="0 0 320 280"')
    end_idx = html.find('</svg>', start_idx) + 6

    if start_idx != -1 and end_idx != -1:
        new_html = html[:start_idx] + simple_svg + html[end_idx:]
        with open(file, "w") as f:
            f.write(new_html)
        print(f"Updated {file}")
