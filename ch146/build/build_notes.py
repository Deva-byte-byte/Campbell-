import weasyprint, re, html
parts=[open(f"n{i}.html").read() for i in range(1,5)]
body="\n".join(parts)
doc=f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Chapter 146 — Adrenal Disorders — Chapter Notes</title>
<link rel="stylesheet" href="notes.css"></head><body>{body}</body></html>'''
open("notes.html","w").write(doc)
out="../Chapter 146 — Pathophysiology, Evaluation and Medical Management of Adrenal Disorders — Chapter Notes.pdf"
d=weasyprint.HTML("notes.html",base_url=".").render()
d.write_pdf(out)
print("pages",len(d.pages))
txt=re.sub(r"<[^>]+>"," ",body); txt=html.unescape(txt)
print("words",len(txt.split()))
