# usage: python3 tools/build_paper.py draft.md out.md
# Keeps each answer (with its key points box) and appends a Rapid Revision Sheet built from all key points boxes.
import sys,re
src=open(sys.argv[1]).read()
m=re.search(r'Paper[- ](IV|III|II|I)\b',src); P=m.group(1) if m else ''
secs=re.split(r'\n(?=## )',src)
body=[];rev=[f"\n\n---\n\n## Rapid Revision Sheet – Paper {P}\n","*All the key points from this paper in one place. Read this in the last 30 minutes before the exam.*\n"]
for sec in secs:
    lines=sec.split('\n')
    quotes=[re.sub(r'^> ?','',l) for l in lines if l.startswith('>')]
    keep=lines
    body.append('\n'.join(keep).rstrip())
    h=re.match(r'## (\S+?)\.\s+(.*)',sec)
    if h and quotes:
        tm=re.search(r'\*\*Type:\*\*\s*(LAQ|SAQ)',sec)
        rev.append(f"\n#### {h.group(1)}. {h.group(2).strip()}{' ('+tm.group(1)+')' if tm else ''}\n")
        for b in quotes:
            if 'Key points to remember' in b or 'Recent advances angle' in b: continue
            if re.match(r'^\s+- ',b): rev.append('    - '+b.strip()[2:])
            elif b.startswith('- '): rev.append(b)
            elif b.strip(): rev.append('- '+b.strip())
out='\n\n'.join(body)
out=re.sub(r'\n{3,}','\n\n',out)
open(sys.argv[2],'w').write(out.rstrip()+'\n'+'\n'.join(rev)+'\n')
