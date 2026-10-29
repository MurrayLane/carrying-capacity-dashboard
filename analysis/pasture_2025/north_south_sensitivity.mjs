// SCOPE.md E1, sensitivity: what if beef output per dry sheep equivalent were lower in northern Australia than in the south, as the ABARES beef farm survey reports (turn-off about 30 to 34% a year in the north against
// 41 to 47% in the south, i.e. 0.73 on the midpoints)? The northern zones (Northern Territory, Queensland, and the northern half of Western Australia taken as half of WA's DSE) get cattle meat yields times f,
// the southern zones times k, with k chosen so that the national meat is unchanged. Capacity of each state zone, short term, release 2025-improved.
//   node analysis/pasture_2025/north_south_sensitivity.mjs OUT.csv      (repository root; needs the built data)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2], d = new URL('../../web/public/data/2025-improved/', import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), regions = JSON.parse(fs.readFileSync(d + 'regions.json')).regions;
const STATE_OF = {}; for (const [code, zs] of Object.entries({ 2: [3, 14], 15: [16, 25], 26: [27, 39], 40: [41, 48], 49: [50, 55], 56: [57, 59], 60: [60, 60] })) for (let z = zs[0]; z <= zs[1]; z++) STATE_OF[z] = +code;
for (const c of [2, 15, 26, 40, 49, 56, 60]) STATE_OF[c] = c;
const DSE = { 2: 19.47, 15: 9.73, 26: 48.63, 40: 4.02, 49: 8.33, 56: 2.04, 60: 7.77 };           // % of national beef DSE, 2024-25 (state_production.csv)
const NORTH = { 26: 1, 60: 1, 49: 0.5 };                                                            // share of the state's DSE counted as northern
const nShare = Object.entries(NORTH).reduce((a, [s, w]) => a + w * DSE[s], 0) / 100;
const ROW = model.meta.yieldRows.indexOf(98);                                                       // Cattle meat is sheet row 98
const run = f => {
  const k = (1 - f * nShare) / (1 - nShare), ev = new Evaluator(model), res = {};
  for (const z of [1, 2, 15, 26, 40, 49, 56, 60]) {
    const R = JSON.parse(JSON.stringify(regions[z])), st = STATE_OF[z], w = z === 1 ? nShare : (NORTH[st] ?? 0);
    R.yield[ROW] *= z === 1 ? 1 : (w * f + (1 - w) * k);                                          // the Australian zone keeps the national yield
    res[z] = ['short', 'long'].map(p => ev.evaluate(R, { ...R.land, ...R.presets[p], population: R.population }).capacity / 1e6);
  }
  return res;
};
const rows = ['f,zone,name,short_million,short_change_pct,long_million,long_change_pct'], base = run(1);
for (const f of [1, 0.85, 0.73, 0.6]) {
  const r = run(f);
  for (const z of Object.keys(r)) rows.push([f, z, regions[z].name, r[z][0].toFixed(2), ((r[z][0] / base[z][0] - 1) * 100).toFixed(1), r[z][1].toFixed(2), ((r[z][1] / base[z][1] - 1) * 100).toFixed(1)].join(','));
}
fs.writeFileSync(out, rows.join('\n') + '\n'); console.log('northern share of beef DSE', nShare.toFixed(3)); console.log(rows.filter(r => r.startsWith('0.73')).join('\n'));
