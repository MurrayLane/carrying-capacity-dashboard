"""Main-text word count for a paper's section files, by one fixed rule.
Counts prose only: not the abstract, headings, Markdown tables, captions
(caption lines: 'Table N.' / 'Figure N.' / 'Table N note.' / '[Figure'; a prose sentence that begins 'Figure 3 gives' counts), figure placeholders,
footnote markers lines, or anything from a 'Drafter notes' heading on.
Usage: python3 qa/tools/wordcount.py A|B   (prints per section and total)"""
import re,sys,glob
P=sys.argv[1]
files=sorted(f for f in glob.glob({"A":"papers/A_results/draft/A_s*.md","B":"papers/B_methods/draft/B_s*.md"}[P]) if "_claims" not in f)
tot=0; per={}
for f in files:
    sec=None; skip=False
    for line in open(f):
        s=line.strip()
        if re.match(r"#+\s*Drafter notes",s,re.I): skip=True
        if skip: continue
        m=re.match(r"##\s+(\d+)\.",s)
        if m: sec=int(m.group(1)); per.setdefault(sec,0); continue
        if re.match(r"##\s+Abstract",s,re.I): sec="abstract"; continue
        if s.startswith("#"): continue
        if sec is None or sec=="abstract": continue
        if s.startswith("|") or s.startswith("[Figure") or re.match(r"\**(Table|Figure|Supplementary (Table|Figure))\s+S?\d+(\.|:|\*|\s+note\.)",s): continue
        if re.match(r"^\^?\[?\d+\]?[:.]",s) and len(s)<200 and "footnote" in s.lower(): continue
        n=len(re.findall(r"\S+",s)); per[sec]+=n; tot+=n
for k in sorted(per,key=lambda x:(isinstance(x,str),x)): print(k,per[k])
print("TOTAL",tot)
