// Effect on Australia's capacity of the constants flagged by the audit, if each were changed as the flag suggests (SCOPE.md E18). One flag at a time on release RELEASE.
//   node analysis/constants_audit/flags.mjs RELEASE OUT.csv
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, outFile] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const cap = m => { const ev = new Evaluator(m); return ['short', 'long'].map(k => ev.evaluate(R, { ...R.land, ...R.presets[k], population: R.population }).capacity); };
const base = cap(model), col = { E: 4, F: 5, K: 10 };
// [id, what, sheet-cells to set]
const FLAGS = [
  ['A1', 'Beef (dressed): processing yield 1.0 -> 0.75, so that edible portion x processing = 0.687, the AUS-MEAT carcase meat yield (68.7%); lamb, veal and pork are 0.66 to 0.69', { Base: { [`174:${col.K}`]: 0.75 } }],
  ['A2', 'Beef (dressed): processing yield 1.0 -> 0.85 (half way)', { Base: { [`174:${col.K}`]: 0.85 } }],
  ['A3', 'Butter (Fat & oil, milk): processing yield 0.195 -> 0.045 (about 22 kg of milk a kilogram of butter)', { Base: { [`265:${col.K}`]: 0.045 } }],
  ['A4', 'Cotton: processing yield 0.836 -> 0.38 (ginning turnout of lint from seed cotton about 35 to 40%)', { Base: { [`324:${col.K}`]: 0.38 } }],
];
const out = ['id,what,short_change_pct,long_change_pct,short_million,long_million'];
for (const [id, what, cells] of FLAGS) {
  const m = JSON.parse(JSON.stringify(model)); for (const [sh, cs] of Object.entries(cells)) for (const [k, v] of Object.entries(cs)) m.sheets[sh].cells[k] = v;
  const c = cap(m); out.push([id, `"${what}"`, ((c[0] / base[0] - 1) * 100).toFixed(2), ((c[1] / base[1] - 1) * 100).toFixed(2), (c[0] / 1e6).toFixed(2), (c[1] / 1e6).toFixed(2)].join(','));
}
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('base', base.map(x => (x / 1e6).toFixed(2)).join(' / ')); console.log(out.join('\n'));
