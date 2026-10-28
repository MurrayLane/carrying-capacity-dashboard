// Model loss factors (Base G consumer, I retail, L primary-to-retail) by diet category, weighted by the food's share of the diet (SCOPE.md E4).
//   node analysis/loss_factors_2025/compare.mjs RELEASE OUT.csv      (repository root; needs the built data)
// Weights: Base column Y (final serve, grams per week) at the release's short-term preset for Australia. Loss = 1 - factor, as a share of the food reaching that step.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, outFile] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), R = JSON.parse(fs.readFileSync(d + 'regions.json')).regions[1];
const ev = new Evaluator(model); ev.evaluate(R, { ...R.land, ...R.presets.short, population: R.population });
const B = model.sheets.Base.cells, g = {};
const num = (r, c) => ev.num(ev.bid, r - 1, c);
for (let r = 6; r <= 346; r++) {
  const cat = B[`${r - 1}:0`]; if (typeof cat !== 'string' || cat === 'TOTAL' || B[`${r - 1}:3`] === undefined) continue;
  const w = num(r, 24); if (!(w > 0)) continue;
  const a = g[cat] ??= { w: 0, G: 0, I: 0, L: 0, H: 0, J: 0, M: 0, E: 0, F: 0, K: 0, N: 0, n: 0 };
  a.w += w; a.n++;
  for (const [k, c] of Object.entries({ G: 6, H: 7, I: 8, J: 9, L: 11, M: 12, E: 4, F: 5, K: 10, N: 13 })) a[k] += w * num(r, c);
}
const out = ['category,rows,grams_per_week,consumer_loss_G,consumer_loss_adjusted_H,retail_loss_I,retail_loss_adjusted_J,prim_retail_loss_L,prim_retail_loss_adjusted_M,edible_E,cooking_F,processing_K,required_per_eaten_N'];
const pct = (x, w) => (100 * (1 - x / w)).toFixed(1);
for (const [c, a] of Object.entries(g)) out.push([`"${c}"`, a.n, a.w.toFixed(0), pct(a.G, a.w), pct(a.H, a.w), pct(a.I, a.w), pct(a.J, a.w), pct(a.L, a.w), pct(a.M, a.w), pct(a.E, a.w), pct(a.F, a.w), pct(a.K, a.w), (a.N / a.w).toFixed(3)].join(','));
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log(out.join('\n'));
