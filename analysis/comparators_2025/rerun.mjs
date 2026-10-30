// The model re-run under the definitions other estimates use (candidate paper 5, analysis/comparators_2025/COMPARATORS.md).
//   node analysis/comparators_2025/rerun.mjs OUT.csv      (repository root; needs the built data)
// R1 a drought allowance: the model's resilience setting is the return period (years) of the worst year the population must survive; 1 = an average year, the model's short-term default.
// R2 cropland doubled (the CSIRO submission to the 1975 National Population Inquiry assumed twice the cropped area, everything eaten at home): the cropland is doubled out of non-agricultural land.
// R3 no allowance for waste (the energy and subsistence calculations count none): the avoidable waste setting at 0.
// All Australia, today's (short-term) diet and settings, unless stated; releases are the three 2025 cells and the three 2011 cells.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2], base = new URL('../../web/public/data/', import.meta.url).pathname;
const CELLS = ['2011-corrected', '2011-fixed', '2011-improved', '2025-mirror', '2025-fixed', '2025-improved'], rows = ['release,variant,setting,capacity_million'];
for (const id of CELLS) {
  const model = JSON.parse(fs.readFileSync(`${base}${id}/model.json`)), R = JSON.parse(fs.readFileSync(`${base}${id}/regions.json`)).regions[1], ev = new Evaluator(model);
  const run = (over = {}, land = R.land) => ev.evaluate(R, { ...land, ...R.presets.short, ...over, population: R.population }).capacity / 1e6;
  for (const y of [1, 5, 10, 20, 50, 100]) rows.push([id, 'R1 drought allowance (return period, years)', y, run({ resilience: y }).toFixed(2)].join(','));
  const l2 = { ...R.land, cropping: R.land.cropping * 2, nonAg: Math.max(R.land.nonAg - R.land.cropping, 0) };
  rows.push([id, 'R2 cropland doubled (from non-agricultural land)', 'average year', run({}, l2).toFixed(2)].join(','));
  rows.push([id, 'R2 cropland doubled (from non-agricultural land)', '10-year', run({ resilience: 10 }, l2).toFixed(2)].join(','));
  rows.push([id, 'R3 no avoidable waste', 'average year', run({ losses: 0 }).toFixed(2)].join(','));
  rows.push([id, 'R3 no avoidable waste', '10-year', run({ losses: 0, resilience: 10 }).toFixed(2)].join(','));
}
fs.writeFileSync(out, rows.join('\n') + '\n'); console.log(rows.filter(r => /^2025-(fixed|improved)|^2011-fixed/.test(r)).join('\n'));
