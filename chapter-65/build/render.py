import weasyprint, pypdfium2 as pdfium, re, html, sys
out={'notes.html':'../Chapter 65 — Adolescent and Transitional Urology — Chapter Notes.pdf',
     'cheatsheet.html':'../Chapter 65 — Adolescent and Transitional Urology — Numbers, Gold Standards and Traps.pdf'}
for src,dst in out.items():
    weasyprint.HTML(src).write_pdf(dst)
    d=pdfium.PdfDocument(dst); n=len(d)
    words=sum(len(d[i].get_textpage().get_text_range().split()) for i in range(n))
    body=re.sub(r'<style.*?</style>|<title>.*?</title>','',open(src).read(),flags=re.S)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',body))
    print(src,'pages',n,'pdf-words',words,'html-words',len(txt.split()))
    d[0].render(scale=1.5,grayscale=True).to_pil().convert('L').save(src.replace('.html','-p1-grey.png'))
    if n>1: d[n-1].render(scale=1.5,grayscale=True).to_pil().convert('L').save(src.replace('.html','-plast-grey.png'))
