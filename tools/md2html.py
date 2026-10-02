import sys, re, markdown
src=open(sys.argv[1]).read()
LIST=re.compile(r'^(\s*)([-*+]|\d+\.)\s')
out=[]; prev=''; fence=False
for line in src.split('\n'):
    st=line.strip()
    if st.startswith('```'):
        if not fence and prev.strip(): out.append('')
        fence=not fence; out.append(line); prev=line; continue
    if fence: out.append(line); prev=line; continue
    if line.startswith('>'):
        inner=line[1:].lstrip(); pin=prev[1:].lstrip() if prev.startswith('>') else None
        if inner.startswith('- ') and pin is not None and pin and not pin.startswith('- ') and not prev.startswith('>   '):
            out.append('>')
        out.append(line); prev=line; continue
    m=LIST.match(line)
    if m:
        ind=len(m.group(1))
        if 0<ind<4: line='    '+line.lstrip()
        elif ind>=4: line=' '*(4*((ind+2)//4))+line.lstrip()
    pm=LIST.match(prev)
    if prev.strip() and m and not pm and not prev.startswith(' '): out.append('')
    if st.startswith('|') and prev.strip() and not prev.strip().startswith('|'): out.append('')
    if st.startswith('**') and prev.strip() and not prev.strip().startswith(('|','#')) and not LIST.match(prev): out.append('')
    out.append(line); prev=line
body=markdown.markdown('\n'.join(out), extensions=['tables','fenced_code','sane_lists','toc'])
css=open(sys.argv[3]).read()
open(sys.argv[2],'w').write(f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>")
