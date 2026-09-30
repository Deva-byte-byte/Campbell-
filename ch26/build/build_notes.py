import markdown, re, glob, os, sys
from weasyprint import HTML
SRC=os.path.join(os.path.dirname(__file__),'..','src')
TITLE='Chapter 26 — Infections of the Urinary Tract'

def inline_md(m):
    t=m.group(0)
    t=re.sub(r'\*\*\*(.+?)\*\*\*',r'<strong><em>\1</em></strong>',t)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])',r'<em>\1</em>',t)
    return t

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
md=''
for f in sorted(glob.glob(os.path.join(SRC,'0*.md'))):
    md+=open(f).read()+'\n\n'
md='\n'.join(ital(l) for l in md.split('\n'))
md=re.sub(r'<p class="(?:tt[^"]*|concept)">.*?</p>',inline_md,md,flags=re.S)
body=markdown.markdown(md,extensions=['tables','md_in_html','sane_lists'])
# first cell of kp box -> title
body=body.replace('<p class="tt ct">','<p class="tt">')
css=open(os.path.join(os.path.dirname(__file__),'notes.css')).read()
html=f'''<!doctype html><html><head><meta charset="utf-8"><title>{TITLE} — Chapter Notes</title><style>{css}</style></head>
<body><h1>{TITLE}</h1>{body}</body></html>'''
out=sys.argv[1]
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.basename(out).replace('.pdf','.html')),'w').write(html)
HTML(string=html,base_url='.').write_pdf(out)
print('ok')
