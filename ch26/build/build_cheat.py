import markdown,re,os,sys
from weasyprint import HTML
d=os.path.dirname(os.path.abspath(__file__))
def ital(line):
    line=re.sub(r'(?<=[^\s*])\*\*\*(?=[\s.,;:)\]|→]|$)','\x02**',line)
    line=re.sub(r'\*\*\*(?=[^\s*])','**\x01',line)
    out=[];i=0;st=False
    while i<len(line):
        if line.startswith('**',i): out.append('**');i+=2;continue
        c=line[i]
        if c=='\x01': out.append('<em>');st=True
        elif c=='\x02': out.append('</em>');st=False
        elif c=='*':
            out.append('</em>' if st else '<em>'); st=not st
        else: out.append(c)
        i+=1
    return ''.join(out)
md=open(os.path.join(d,'..','src','cheatsheet.md')).read()
md='\n'.join(ital(l) for l in md.split('\n'))
parts=re.split(r'(?=<div class="traps)',md)
head,rest=re.split(r'(?<=</div>)\n',parts[0],maxsplit=1)
cv=lambda x: markdown.markdown(x,extensions=['md_in_html','sane_lists'])
body=cv(head)+'<div class="cols">'+cv(rest)+'</div>'+cv(parts[1])
css=open(os.path.join(d,'cheat.css')).read()
T='Chapter 26 — Infections of the Urinary Tract — Numbers, Gold Standards and Traps'
html=f'<!doctype html><html><head><meta charset="utf-8"><title>{T}</title><style>{css}</style></head><body><h1>{T}</h1>{body}</body></html>'
out=sys.argv[1]; open(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.basename(out).replace('.pdf','.html')),'w').write(html)
HTML(string=html).write_pdf(out)
txt=re.sub(r'<[^>]+>',' ',body); print('words',len(txt.split()))
