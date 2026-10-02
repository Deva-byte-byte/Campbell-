#!/bin/bash
# usage: tools/addref.sh /path/a.pdf /path/b.pdf ...   (copies into reference/, extracts text, rebuilds reference/INDEX.md)
cd "$(git rev-parse --show-toplevel)" && mkdir -p reference/text
for f in "$@"; do b=$(basename "$f" | sed -E 's/^[0-9a-f]{8}-//; s/___/ - /g; s/_/ /g'); cp "$f" "reference/$b"; pdftotext -layout "$f" "reference/text/${b%.pdf}.txt"; echo "$b | $(pdfinfo "$f" | awk '/Pages/{print $2}') pages | $(wc -w < "reference/text/${b%.pdf}.txt") words"; done
cd reference && python3 - <<'PY'
import glob,re,os
out=["# Reference library index\n","Uploaded chapter notes (Campbell-Walsh-Wein based). Text extracts in `text/` for searching.\n"]
def key(x):
    m=re.search(r'Chapter (\d+)',x); return int(m.group(1)) if m else 9999
for t in sorted(glob.glob('text/*.txt'), key=key):
    s=open(t).read(); heads=[]
    for l in s.split('\n'):
        l=l.strip()
        if 3<len(l)<70 and l==l.upper() and re.search('[A-Z]{3}',l) and not l.startswith('•') and 'PAGE' not in l and '  ' not in l:
            if l not in heads: heads.append(l)
    name=os.path.basename(t)[:-4]
    out.append(f"\n## {name}\n- PDF: `{name}.pdf`\n- Sections: "+"; ".join(h.title() for h in heads)+"\n")
open('INDEX.md','w').write('\n'.join(out))
PY
