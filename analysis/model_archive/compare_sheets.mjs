import { createRequire } from 'module'; const require = createRequire(new URL('../../web/', import.meta.url).pathname);
const XLSX = require('xlsx'); import fs from 'fs';
const load = p => XLSX.read(fs.readFileSync(p), { type: 'buffer', cellFormula: true, cellNF: false, sheetStubs: false });
const ref = load(process.argv[2]);
const cell = c => (c.f ? '=' + c.f : (c.v === undefined ? '' : String(c.v)));
for (const p of process.argv.slice(3)) {
  let wb; try { wb = load(p); } catch (e) { console.log(p, 'ERR', e.message); continue; }
  const rep = [];
  for (const sn of ref.SheetNames) {
    const a = ref.Sheets[sn], b = wb.Sheets[sn]; if (!b) { rep.push(`${sn}:MISSING`); continue; }
    let diffF = 0, diffV = 0, n = 0; const keys = new Set([...Object.keys(a), ...Object.keys(b)].filter(k => k[0] !== '!'));
    for (const k of keys) { n++; const x = a[k] || {}, y = b[k] || {}; if ((x.f || '') !== (y.f || '')) diffF++; else if (!x.f && String(x.v ?? '') !== String(y.v ?? '')) diffV++; }
    rep.push(`${sn}: cells ${n}, formula diffs ${diffF}, constant diffs ${diffV}`);
  }
  console.log(p + '\n  ' + rep.join('\n  '));
}
