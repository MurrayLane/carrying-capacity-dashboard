"""Lists every .xls under the current directory with its embedded author, created and last-saved dates (file modification times do not survive git).
Usage, from the Models folder: python3 -I inventory.py out.csv"""
import os, sys, olefile, xlrd, csv, hashlib
out=[]
for d,_,fs in os.walk('.'):
    if '.git' in d.split(os.sep): continue
    for f in fs:
        if not f.lower().endswith('.xls'): continue
        p=os.path.join(d,f)
        row={'path':p[2:],'bytes':os.path.getsize(p)}
        try:
            ole=olefile.OleFileIO(p); m=ole.get_metadata()
            row.update(author=(m.author or b'').decode('latin1'), lastby=(m.last_saved_by or b'').decode('latin1'),
                       created=str(m.create_time)[:16], saved=str(m.last_saved_time)[:16], app=(m.creating_application or b'').decode('latin1'))
            ole.close()
        except Exception as e: row['err']='ole:'+str(e)[:40]
        try:
            wb=xlrd.open_workbook(p,on_demand=True); row['sheets']='|'.join(f'{s.name}' for s in wb.sheets()); wb.release_resources()
        except Exception as e: row['err']=row.get('err','')+' xlrd:'+str(e)[:40]
        out.append(row)
keys=['path','bytes','author','lastby','created','saved','app','sheets','err']
w=csv.DictWriter(open(sys.argv[1],'w',newline=''),keys,extrasaction='ignore'); w.writeheader(); w.writerows(sorted(out,key=lambda r:r['path']))
print(len(out))
