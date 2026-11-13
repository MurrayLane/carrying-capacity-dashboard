"""Assemble a paper's section files into one first-draft file.
Usage: python3 qa/tools/assemble_draft.py A|B
Prose first in section order; every "Drafter notes" block moved to an appendix at the end."""
import re,sys,glob,datetime
P=sys.argv[1]
d={"A":("papers/A_results/draft","Paper A, results: Australia's carrying capacity 2011 to 2025 by region on the corrected releases","A_s*.md"),
   "B":("papers/B_methods/draft","Paper B, methods: well-known carrying-capacity methods tested on common Australian data","B_s*.md")}[P]
files=sorted(f for f in glob.glob(d[0]+"/"+d[2]) if "_claims" not in f and "draft1" not in f)
body=[];notes=[]
for f in files:
    t=open(f).read()
    m=re.search(r"\n#+\s*Drafter notes.*",t,re.S|re.I)
    if m: notes.append("### From %s\n"%f.split("/")[-1]+t[m.start():].split("\n",1)[1]); t=t[:m.start()]
    body.append(t.strip()+"\n")
out="# %s\n\nFirst draft, assembled %s from %s. Every number traces to the claims csv beside each section file; sentences marked [gate 4] in those csvs use values awaiting Murray's gate 4 approval. Not for circulation.\n\n"%(d[1],datetime.date.today(),", ".join(x.split("/")[-1] for x in files))
out+="\n\n".join(body)+"\n\n---\n\n## Appendix: drafter notes (not for the paper)\n\n"+"\n\n".join(notes)
open(d[0]+"/paper_%s_draft1.md"%P,"w").write(out)
print(P,len(out.split()),"words incl. notes;",len(files),"section files")
