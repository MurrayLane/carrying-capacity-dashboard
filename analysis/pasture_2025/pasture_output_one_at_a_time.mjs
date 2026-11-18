// B134 (decision 141), step 1 of 2: national pasture output plus and minus 20% one at a time, everything else at base, through the evaluator (the full model).
//   node analysis/pasture_2025/pasture_output_one_at_a_time.mjs [OUT.csv]      (repository root; needs the built data)   then  python3 analysis/pasture_2025/pasture_output_one_at_a_time.py
// Pasture output = the yield per hectare of the pasture-fed rows (sheep meat 95, wool 96, dairy milk 97, cattle meat 98, goat and sheep milk 135, 136), the same set drought_bounds.mjs holds at the mean.
// The last column is Settings!C45 (cropland a person for oils and fats) as the evaluator holds it after the run: it moves with pasture output (animal fats), which the closed form needs as an input.
// Release 2025-fixed, Australia (zone 1), short and long presets. Which land binds is read in the closed form (the python step).
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2] ?? 'analysis/pasture_2025/pasture_output_one_at_a_time_2025-fixed.csv', REL = '2025-fixed';
const dir = new URL(`../../web/public/data/${REL}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(dir + 'model.json')), data = JSON.parse(fs.readFileSync(dir + 'regions.json')), ev = new Evaluator(model);
const R = data.regions[1], rows = data.yieldRows, PASTURE = new Set([95, 96, 97, 98, 135, 136]);
const run = (f, preset) => ev.evaluate({ ...R, yield: R.yield.map((y, i) => PASTURE.has(rows[i]) ? y * f : y) }, { ...R.land, ...R.presets[preset], population: R.population });
const lines = ['release,preset,pasture_output_factor,capacity,change_from_base,change_pct,oils_cropland_m2_pp'];
for (const preset of ['short', 'long']) {
  const base = run(1, preset).capacity;
  for (const f of [0.8, 1, 1.2]) {
    const r = run(f, preset);
    lines.push([REL, preset, f, r.capacity, r.capacity - base, (100 * (r.capacity / base - 1)).toFixed(2), ev.s(44, 2)].join(','));
  }
}
fs.writeFileSync(out, lines.join('\n') + '\n'); console.log(lines.join('\n'));
