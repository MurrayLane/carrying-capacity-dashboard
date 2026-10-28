// Which of the model's own diets feeds the most people in each zone? (SCOPE.md E16, first step)
//   node analysis/diet_templates/best_diet.mjs RELEASE OUT.csv      (repository root; needs the built data: cd web && node scripts/build-data.mjs)
// The model's diet is the NHMRC food-modelling diet for an activity level and a meat and egg share (Diet sheet: 15 food groups, nutritionally adequate at every meat share from 0 to 15%), with the
// share of red meat in the meat chosen separately. This tries a grid of the two shares in every zone, everything else at the release's defaults, and records the capacity of each, the best, and the
// capacity at the release's own diet. It changes nothing in the model: it shows how much the choice of diet within the model's diets is worth zone by zone, and where it points.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, outFile] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const ev = new Evaluator(JSON.parse(fs.readFileSync(d + 'model.json'))), D = JSON.parse(fs.readFileSync(d + 'regions.json')).regions;
const MEAT = [0, 0.025, 0.05, 0.075, 0.10, 0.12, 0.13, 0.15], RED = [0, 0.25, 0.5, 0.75, 1.0];
const out = ['release,zone,name,kind,preset,population,capacity_default,default_meat,default_red,best_meat,best_red,capacity_best,gain,capacity_vegan,capacity_no_red,capacity_all_red_13'];
for (const R of Object.values(D).sort((a, b) => a.id - b.id)) for (const preset of ['short', 'long']) {
  const p = R.presets[preset], cap = (m, r) => ev.evaluate(R, { ...R.land, ...p, meategg: m, redmeat: r, population: R.population }).capacity;
  const base = cap(p.meategg, p.redmeat); let best = { c: -1 };
  for (const m of MEAT) for (const r of m === 0 ? [0.578] : RED) { const c = cap(m, r); if (c > best.c) best = { c, m, r }; }
  out.push([rel, R.id, `"${R.name}"`, R.kind, preset, R.population, Math.round(base), p.meategg, p.redmeat, best.m, best.r, Math.round(best.c), (best.c / base).toFixed(3), Math.round(cap(0, 0.578)), Math.round(cap(0.13, 0)), Math.round(cap(0.13, 1))].join(','));
}
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'rows');
