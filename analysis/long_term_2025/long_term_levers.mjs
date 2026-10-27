// What each long-term setting is worth. For release 2025-organic, Australia and the seven state zones:
//   alone   the short-term (today's) settings with ONE long-term setting switched on
//   without the long-term settings with ONE of them put back to its short-term value
// and, for the reserve, where the extra reserve land comes from (README.md): non-agricultural land first (the model), or from pasture and cropping in proportion.
//   node long_term_levers.mjs OUT.csv          (needs the built data: cd web && node scripts/build-data.mjs)
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const d = new URL('../../web/public/data/2025-organic/', import.meta.url).pathname;
const ev = new Evaluator(JSON.parse(fs.readFileSync(d + 'model.json'))); const D = JSON.parse(fs.readFileSync(d + 'regions.json')).regions;
const KEYS = ['resilience', 'food', 'meategg', 'redmeat', 'activity', 'recycling', 'losses', 'organic', 'irrigation', 'fuel', 'biofuel', 'fibre', 'fibreNat', 'fibreWool', 'timber', 'infrastr2', 'nature2'];
const out = ['zone,lever,alone,without'];
for (const z of [1, 2, 15, 26, 40, 49, 56, 60]) {
  const R = D[z], S = R.presets.short, L = R.presets.long;
  const run = (pre, land = {}) => Math.round(ev.evaluate(R, { ...R.land, ...land, ...pre, population: R.population }).capacity);
  out.push([z, 'short settings', run(S), run(S)].join(',')); out.push([z, 'long settings', run(L), run(L)].join(','));
  for (const k of KEYS) { if (S[k] === L[k]) continue; out.push([z, `${k} (${S[k]} to ${L[k]})`, run({ ...S, [k]: L[k] }), run({ ...L, [k]: S[k] })].join(',')); }
  const T = R.land.cropping + R.land.pasture + R.land.nonAg + R.land.infrastr1 + R.land.nature1, deficit = Math.max(0, L.nature2 * T - R.land.nature1), sh = R.land.cropping / (R.land.cropping + R.land.pasture);
  out.push([z, 'reserve deficit km2 (30% target less existing)', Math.round(deficit), ''].join(','));
  out.push([z, 'long settings with the reserve deficit taken from pasture and cropping pro rata', run(L, { cropping: R.land.cropping - deficit * sh, pasture: R.land.pasture - deficit * (1 - sh), nonAg: R.land.nonAg + deficit }), ''].join(','));
}
fs.writeFileSync(process.argv[2], out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'rows');
// Australia, long-term settings: liquid fuel per person against the biofuel share of it, and the resilience (climate variability) setting
{
  const R = D[1], run = pre => ev.evaluate(R, { ...R.land, ...R.presets.long, ...pre, population: R.population }).capacity;
  const g = ['fuel_litres,biofuel_share,capacity'];
  for (const f of [253, 500, 860, 1500]) for (const b of [1, 0.5, 0.3, 0.1]) g.push([f, b, Math.round(run({ fuel: f, biofuel: b }))].join(','));
  fs.writeFileSync(process.argv[2].replace('levers.csv', 'fuel_grid.csv'), g.join('\n') + '\n');
  const r = ['resilience_years,capacity'];
  for (const y of [1, 5, 10, 20, 50, 100, 150]) r.push([y, Math.round(run({ resilience: y }))].join(','));
  fs.writeFileSync(process.argv[2].replace('levers.csv', 'resilience_curve.csv'), r.join('\n') + '\n');
}
