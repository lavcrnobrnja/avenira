import re
import os

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

with open("css/style.css", "r") as f:
    css = f.read()

start = css.find("/* Active page indicator")
end = css.find(".lang-toggle {")

if start != -1 and end != -1:
    new_css = css[:start] + """/* Active page indicator */
.nav-links a[aria-current="page"] {
  background: rgba(37, 99, 235, 0.12);
  padding: 6px 14px;
  border-radius: var(--radius-full);
  color: var(--color-blue-light) !important;
}

.nav-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

""" + css[end:]
    with open("css/style.css", "w") as f:
        f.write(new_css)
    print("Fixed!")
else:
    print("Could not find blocks.")
