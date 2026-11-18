// B137 item 5 (helper of resilience_variants.py): short-term capacity of 2025-fixed, Australia, at a given drought factor, under the model's rule (every yield times the factor) and with the factor on crop output only.
//   node analysis/resilience_2025/drought_factor_variants_eval.mjs FACTORS.csv OUT.csv      (repository root; FACTORS.csv has a header and one factor per line in its first column; needs the built data)
// The two rules are those of drought_bounds.mjs (same row groups; the 'both' result at the 1-in-10 factor of the model's own table is checked equal to the model run at that return period).
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [inFile, outFile] = process.argv.slice(2), REL = '2025-fixed';
const dir = new URL(`../../web/public/data/${REL}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(dir + 'model.json')), data = JSON.parse(fs.readFileSync(dir + 'regions.json')), ev = new Evaluator(model);
const R = data.regions[1], rows = data.yieldRows;
const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
const PLANT = new Set([...range(4, 94), ...range(106, 133)]), GRAINFED = new Set(range(99, 103));
const cap = yields => Math.round(ev.evaluate({ ...R, yield: yields }, { ...R.land, ...R.presets.short, resilience: 1, population: R.population }).capacity);
const scaled = (f, keep) => R.yield.map((y, i) => keep(rows[i]) ? y * f : y);
const res = model.sheets.resilience.cells;
const check = cap(R.yield) === Math.round(ev.evaluate(R, { ...R.land, ...R.presets.short, resilience: 1, population: R.population }).capacity);
const f10 = res['2:11'], modelAt10 = Math.round(ev.evaluate(R, { ...R.land, ...R.presets.short, resilience: 10, population: R.population }).capacity);
if (cap(scaled(f10, () => true)) !== modelAt10) throw new Error('the all-output rule does not reproduce the model at 1 in 10');
const lines = fs.readFileSync(inFile, 'utf8').trim().split(/\r?\n/).slice(1).map(Number);
const out = ['factor,capacity_all_output,capacity_crop_only'];
for (const f of lines) out.push([f, cap(scaled(f, () => true)), cap(scaled(f, r => PLANT.has(r) || GRAINFED.has(r)))].join(','));
fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', lines.length, 'factors; mean-year capacity', cap(R.yield), '; all-output rule reproduces the model at 1 in 10:', modelAt10);
