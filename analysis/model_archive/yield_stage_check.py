"""Stage 2 of the yield chain: the model's Yield sheet from the five-year averages.

For every crop and region, checks that the Yield sheet (g/m2 = t/ha x 100) equals
  - the 5-year average (file 5, sheet Aver-add) / (1 + 0.55 x region irrigation share), where the average exists;
  - otherwise the national average x the region's "major crops yield %" (thesis step 13; Base model 021012 Yield row 3:
    the mean of regional/national ratios for wheat, oats, barley, sorghum, maize, canola and potatoes, skipping any the
    region does not report), then the same irrigation conversion.
Usage: MODELS_DIR=/path/to/Models python3 -I yield_stage_check.py   (run from the repository root)
"""
import os
MODELS = os.environ['MODELS_DIR']
os.chdir(os.path.join(MODELS, 'Yield data'))
REPO = os.environ.get('REPO', os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)) if '__file__' in dir() else '.', '../..')))
import xlrd, csv, collections, statistics as st
src=xlrd.open_workbook('5 NRM-all 5 years - average.xls'); add=src.sheet_by_name('Aver-add')
mod=xlrd.open_workbook(os.path.join(REPO,'model/model.xls')).sheet_by_name('Yield')
irr={int(r['regionId']):float(r['irrigation']) for r in csv.DictReader(open(os.path.join(REPO,'data/2011/default-inputs-short-term.csv')))}
A=lambda r,rid: (add.cell_value(r,rid) if isinstance(add.cell_value(r,rid),float) and add.cell_value(r,rid)>0 else None)
Mv=lambda r,rid: (mod.cell_value(r+2,6+rid)/100 if isinstance(mod.cell_value(r+2,6+rid),float) else None)
MAJOR=[1,2,3,4,5,9,49]   # Aver-add rows: wheat oats barley sorghum maize canola potatoes (= Yield rows 4-8,12,52)
def factor(rid):
    rs=[A(r,rid)/A(r,1) for r in MAJOR if A(r,rid) and A(r,1)]
    return sum(rs)/len(rs) if rs else None
F={rid:factor(rid) for rid in range(1,61)}
cnt=collections.Counter(); bad=[]; exact_rows=collections.Counter()
for r in range(1,134):
    for rid in range(2,61):
        M=Mv(r,rid); a=A(r,rid)
        if a is not None:
            pred=a/(1+.55*irr[rid]); k='present-exact' if M is not None and abs(M-pred)<=1e-6*max(1,pred) else 'present-mismatch'
        elif M and M>0:
            if A(r,1) and F[rid]:
                pred=A(r,1)*F[rid]/(1+.55*irr[rid]); k='fill-exact' if abs(M-pred)<=1e-6*max(1,pred) else 'fill-mismatch'
            else: k='fill-no national'
        else: k='zero'
        cnt[k]+=1
        if k in('fill-mismatch','fill-no national','present-mismatch'): exact_rows[(k,str(add.cell_value(r,0)).split('(')[0].strip())]+=1
print(dict(cnt))
bykind=collections.defaultdict(list)
for (k,n),v in exact_rows.items(): bykind[k].append((v,n))
for k,v in bykind.items(): print(k,sorted(v,reverse=True)[:14])
