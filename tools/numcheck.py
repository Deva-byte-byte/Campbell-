# every numeric token in concise must appear in full source
import sys,re
full=open(sys.argv[1]).read().split('## Rapid Revision Sheet')[0]
con=open(sys.argv[2]).read()
tok=lambda s:set(re.findall(r'\d+(?:[.,]\d+)?',s))
missing=sorted(tok(con)-tok(full),key=lambda x:float(x.replace(',','')))
print(sys.argv[2].split('/')[-1],'numbers not in source:',missing if missing else 'NONE')
for t in missing:
    for l in con.split('\n'):
        if re.search(r'(?<![\d.])'+re.escape(t)+r'(?![\d])',l): print('   ',t,'|',l.strip()[:150]); break
