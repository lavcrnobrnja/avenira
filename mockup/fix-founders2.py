import os

os.chdir("/Users/cofoundergpt/.openclaw/workspace/projects/avenira/mockup")

shared_en = """        </div>
        <div class="founders-shared" style="text-align: center; max-width: 600px; margin: 40px auto 0; font-size: 1.125rem; color: var(--text-muted);">
          <p>Over 20 years of experience in tech — cloud, web/mobile dev, and applied automation.</p>
        </div>"""

shared_fr = """        </div>
        <div class="founders-shared" style="text-align: center; max-width: 600px; margin: 40px auto 0; font-size: 1.125rem; color: var(--text-muted);">
          <p>Plus de 20 ans d'expérience en technologie — cloud, développement web/mobile et automatisation appliquée.</p>
        </div>"""

# EN
with open("about.html", "r") as f:
    html = f.read()
if "Over 20 years of experience" not in html:
    html = html.replace('        </div>\n      </div>\n    </section>\n\n    <!-- APPROACH -->', shared_en + '\n      </div>\n    </section>\n\n    <!-- APPROACH -->')
    with open("about.html", "w") as f:
        f.write(html)

# FR
with open("fr/a-propos.html", "r") as f:
    fhtml = f.read()
if "Plus de 20 ans d'expérience" not in fhtml:
    fhtml = fhtml.replace('        </div>\n      </div>\n    </section>\n\n    <!-- APPROACH -->', shared_fr + '\n      </div>\n    </section>\n\n    <!-- APPROACH -->')
    with open("fr/a-propos.html", "w") as f:
        f.write(fhtml)

print("Updated Founders block.")
