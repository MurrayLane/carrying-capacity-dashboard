"""Stage 1 of the yield chain: per-year t/ha from the raw ABS cubes (file 1) against the adjusted sheets (file 5, YYYY-adjt).

Applies the documented adjustments (file 2, Summary): seed deducted per crop in t/ha, vegetable area x (1 + 2.04%),
tree crops: hectares = trees / trees-per-hectare. Thresholds: a cell is deleted when hectares < 10 or tonnes < 10.
Reports how many cells match exactly. Not yet reproduced: the outlier rule (less than half or more than double the national
average), the one-year-only rule, label mismatches (herbs, parsley), mushrooms, hay, and the livestock (DSE) products.
Usage: MODELS_DIR=/path/to/Models python3 -I per_year_check.py
"""
import os
os.chdir(os.path.join(os.environ['MODELS_DIR'], 'Yield data'))
import xlrd, re, collections
f1=xlrd.open_workbook('1 NRM-all 5 years - all t and ha.xls'); f5=xlrd.open_workbook('5 NRM-all 5 years - average.xls')
f2=xlrd.open_workbook('2 NRM-all 5 years - adjustments.xls')
norm=lambda s:re.sub(r'[^a-z0-9]','',str(s).lower())
# adjustments summary: label -> (seed t/ha, % area increase, trees/ha)
sm=f2.sheet_by_name('Summary'); adj={}
for r in range(1,sm.nrows):
    lab=str(sm.cell_value(r,0)); vals=[sm.cell_value(r,c) if isinstance(sm.cell_value(r,c),float) else None for c in (1,2,3)]
    if lab: adj[norm(lab)]=(lab,*vals)
def peryear(year):
    s=f1.sheet_by_name(str(year)); a=f5.sheet_by_name(f'{year}-adjt')
    rows={norm(s.cell_value(r,0)):r for r in range(1,s.nrows)}
    out=collections.Counter(); ex=[]
    for ar in range(1,a.nrows):
        lab=str(a.cell_value(ar,0)); base=re.sub(r'\s*\(t/ha\)','',lab).strip()
        # find (ha) and (t) rows in f1
        cand_ha=[k for k in rows if k.startswith(norm(base)) and (k.endswith('ha') or k.endswith('n'))]; cand_t=[k for k in rows if k.startswith(norm(base)) and k.endswith('t')]
        if not cand_ha or not cand_t: out['nomatch']+=1; continue
        rha,rt=rows[cand_ha[0]],rows[cand_t[0]]
        for c in range(1,a.ncols):
            tgt=a.cell_value(ar,c)
            ha=s.cell_value(rha,c) if c<s.ncols else ''; t=s.cell_value(rt,c) if c<s.ncols else ''
            if not isinstance(ha,float) or not isinstance(t,float) or ha<=0 or t<=0:
                out['raw missing, target %s'%('blank' if tgt in('',0.0) else 'has value')]+=1; continue
            y=t/ha
            lab_ha=norm(s.cell_value(rha,0)); is_tree=lab_ha.endswith('n')
            # seed deduction
            sd=adj.get(norm(base+' (t)'))
            if not sd:
                ks=[k for k in adj if norm(base) in k and k.endswith('t') and adj[k][1] is not None]
                sd=adj[ks[0]] if len(ks)==1 else None
            seed=(sd[1] or 0) if sd else 0
            ka=[k for k in adj if k.startswith(norm(base)) and k.endswith('ha') and adj[k][2] is not None]
            inc=adj[ka[0]][2] if ka else 0
            ka=[k for k in adj if k.startswith(norm(base)) and ('trees' in k) and adj[k][3]]
            dens=adj[ka[0]][3] if ka else None
            if is_tree and dens: y=t/(ha/dens)
            elif inc: y=y/(1+inc)
            out['computed']+=1
            if isinstance(tgt,float) and abs(tgt-(y-seed))<1e-9*max(1,abs(tgt)): out['match seed-adj']+=1
            elif isinstance(tgt,float) and abs(tgt-y)<1e-9*max(1,abs(tgt)): out['match raw']+=1
            elif tgt in ('',0.0):
                out['deleted: ha<10 or t<10' if (ha<10 or t<10) else 'deleted: other (rule 8 outlier / one-year)']+=1
            else:
                out['value differs']+=1
                if len(ex)<10: ex.append((base,c,round(y,4),round(y-seed,4),tgt,seed))
    return out,ex
for y in (2006,2007,2008,2009,2010):
    o,ex=peryear(y); print(y,dict(o)); print(ex)
