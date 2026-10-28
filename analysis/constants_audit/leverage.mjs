// Which typed-in constants of the workbook matter most? (SCOPE.md E18, step 1 of the constants audit)
//   node analysis/constants_audit/leverage.mjs RELEASE OUT.csv      (repository root; needs the built data)
// Each group of numeric constants is raised by 10% (formulas are left alone) and Australia's capacity is recomputed, short and long term; the change is the group's leverage.
// Groups: processing yield (Base!K) by diet category, edible portion (E), cooking yield (F), consumer loss (G), retail loss (I), primary-to-retail loss (L), serving size (Q) by category,
// and the feed conversion ratios of the Recycle sheet. The audit then traces the highest-leverage groups to their sources first.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, outFile] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const cap = m => { const ev = new Evaluator(m); return ['short', 'long'].map(k => ev.evaluate(R, { ...R.land, ...R.presets[k], population: R.population }).capacity); };
const base = cap(model), B = model.sheets.Base.cells, cat = r => B[`${r - 1}:0`];
const COLS = { E: 4, F: 5, G: 6, I: 8, K: 10, L: 11, Q: 16 };
const rows = []; for (let r = 6; r <= 346; r++) if (typeof cat(r) === 'string' && B[`${r - 1}:3`] !== undefined && cat(r) !== 'TOTAL') rows.push(r);
const groups = {};
for (const [name, c] of Object.entries(COLS)) {
  groups[`${name} all foods`] = rows.map(r => `${r - 1}:${c}`).filter(k => typeof B[k] === 'number');
  for (const g of new Set(rows.map(cat))) { const ks = rows.filter(r => cat(r) === g).map(r => `${r - 1}:${c}`).filter(k => typeof B[k] === 'number'); if (ks.length) groups[`${name} ${g}`] = ks; }
}
const out = ['group,cells,short_change_pct,long_change_pct'];
for (const [name, ks] of Object.entries(groups)) {
  const m = JSON.parse(JSON.stringify(model)); for (const k of ks) m.sheets.Base.cells[k] = m.sheets.Base.cells[k] * 1.1;
  const c = cap(m); out.push([`"${name}"`, ks.length, ((c[0] / base[0] - 1) * 100).toFixed(2), ((c[1] / base[1] - 1) * 100).toFixed(2)].join(','));
}
const fcr = Object.keys(model.sheets.Recycle.cells).filter(k => k.endsWith(':4') && typeof model.sheets.Recycle.cells[k] === 'number' && +k.split(':')[0] >= 1 && +k.split(':')[0] <= 7);
{ const m = JSON.parse(JSON.stringify(model)); for (const k of fcr) m.sheets.Recycle.cells[k] *= 1.1; const c = cap(m); out.push(['"Recycle feed conversion ratios"', fcr.length, ((c[0] / base[0] - 1) * 100).toFixed(2), ((c[1] / base[1] - 1) * 100).toFixed(2)].join(',')); }
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'groups; base', base.map(x => (x / 1e6).toFixed(2)).join(' / '));
