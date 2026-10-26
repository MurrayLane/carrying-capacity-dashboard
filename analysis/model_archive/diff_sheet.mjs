import { createRequire } from 'module'; const require = createRequire(new URL('../../web/', import.meta.url).pathname);
const XLSX = require('xlsx'); import fs from 'fs';
const load = p => XLSX.read(fs.readFileSync(p), { type: 'buffer', cellFormula: true });
const [pa, pb, sn, lim] = process.argv.slice(2); const A = load(pa).Sheets[sn], B = load(pb).Sheets[sn];
const keys = new Set([...Object.keys(A), ...Object.keys(B)].filter(k => k[0] !== '!'));
let n = 0; for (const k of [...keys].sort((x, y) => { const a = XLSX.utils.decode_cell(x), b = XLSX.utils.decode_cell(y); return a.r - b.r || a.c - b.c; })) {
  const x = A[k] || {}, y = B[k] || {}; const fx = x.f ? '=' + x.f : x.v, fy = y.f ? '=' + y.f : y.v;
  if (String(fx ?? '') !== String(fy ?? '')) { if (n++ < +(lim || 40)) console.log(k, JSON.stringify(fx), '->', JSON.stringify(fy)); }
}
console.log('total diffs', n);
