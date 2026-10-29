// Constants audit stage 3 (SCOPE.md E18): leverage of the typed-in constants outside the Base loss columns, row by row.
//   node analysis/constants_audit/leverage_sheets.mjs RELEASE OUT.csv      (repository root; needs the built data)
// For the Diet, Yield, Settings (below the input block and above the preset blocks) and Recycle sheets, the numeric constants of each row are raised by 10% (formulas left alone;
// the Yield column the regions overwrite, F, is skipped) and Australia's capacity is recomputed, short and long term. Rows are reported with their first text cell as a label.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, outFile] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const cap = m => { const ev = new Evaluator(m); return ['short', 'long'].map(k => ev.evaluate(R, { ...R.land, ...R.presets[k], population: R.population }).capacity); };
const base = cap(model), out = ['sheet,row,label,cells,short_change_pct,long_change_pct'];
const SKIP = { Yield: c => c === 5, Settings: c => c === 1 && false };
for (const sh of ['Diet', 'Yield', 'Settings', 'Recycle']) {
  const cells = model.sheets[sh].cells, byRow = {};
  for (const [k, v] of Object.entries(cells)) { const [r, c] = k.split(':').map(Number); if (typeof v !== 'number') continue; if (SKIP[sh]?.(c)) continue; if (sh === 'Settings' && (r < 25 || r >= 108)) continue; (byRow[r] ??= []).push(k); }
  for (const [r, ks] of Object.entries(byRow)) {
    const m = JSON.parse(JSON.stringify(model)); for (const k of ks) m.sheets[sh].cells[k] *= 1.1;
    const c = cap(m), label = [0, 1, 2, 3].map(i => cells[`${r}:${i}`]).find(x => typeof x === 'string' && x[0] !== '=') ?? '';
    out.push([sh, +r + 1, `"${String(label).replace(/"/g, "'").slice(0, 50)}"`, ks.length, ((c[0] / base[0] - 1) * 100).toFixed(2), ((c[1] / base[1] - 1) * 100).toFixed(2)].join(','));
  }
}
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'rows; base', base.map(x => (x / 1e6).toFixed(2)).join(' / '));
