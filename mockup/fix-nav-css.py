import os

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")
with open("css/style.css", "r") as f:
    css = f.read()

start = css.find("/* Active page indicator")
end = css.find(".lang-toggle {")

if start != -1 and end != -1:
    new_css = css[:start] + """/* Active page indicator */
.nav-links a[aria-current="page"]:not(.nav-cta) {
  background: rgba(37, 99, 235, 0.12);
  padding: 6px 14px;
  border-radius: var(--radius-full);
  color: var(--color-blue-light) !important;
}

.nav-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--color-blue);
  color: #fff !important;
  padding: 8px 20px !important;
  border-radius: 40px;
  font-weight: 600;
  border: 1.5px solid var(--color-blue);
  transition: all 0.2s ease;
}
.nav-cta:hover {
  background: transparent;
  color: var(--color-blue-light) !important;
}
.nav-cta[aria-current="page"] {
  background: transparent;
  color: var(--color-blue-light) !important;
}

""" + css[end:]
    with open("css/style.css", "w") as f:
        f.write(new_css)
    print("Nav CSS fixed.")
