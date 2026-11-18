// B112 (decision 103): the drought factor applied to crop output only, against the model's rule of applying it to every yield. National, release 2025-fixed.
//   node analysis/resilience_2025/drought_bounds.mjs analysis/resilience_2025/drought_bounds.csv      (repository root; needs the built data: cd web && node scripts/build-data.mjs)
// The model scales every yield of a zone by one factor, Yield!C2, which reads the zone's row of the resilience sheet at the return period of Settings!B8
// (Australia: resilience!B3, the row C3:EV3 indexed by the return period). Every yield is Yield!C2 x the irrigation and organic adjustments x the zone yield
// in Yield column F, so scaling a row of column F by the factor is the same as the factor acting on that row alone. The bounds:
//   both applied   every yield row times the factor (the model's rule); checked equal to the model run at that return period
//   crop only      the plant rows (field crops, vegetables, fruit, nuts, fodder: rows 4 to 94 and 106 to 133) and the grain-fed animal rows (chicken, duck, turkey,
//                  eggs, pig meat: rows 99 to 103, whose yield per hectare is a grain yield over a feed conversion ratio) times the factor; the pasture-fed rows
//                  (sheep meat, wool, dairy milk, cattle meat, goat and sheep milk: rows 95 to 98, 135, 136) and the rest (fish, seafood, honey, wild fish,
//                  timber: rows 104, 105, 134, 137, 138) held at the mean
//   plant rows only  as crop only, with the grain-fed animal rows also held at the mean (the strict reading of "crop output only")
// Short-term settings at 1 in 10, 1 in 20 and 1 in 100; long-term settings at 1 in 100 (the long-term setting is defined at 100 years).
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2] ?? 'analysis/resilience_2025/drought_bounds.csv', REL = '2025-fixed';
const dir = new URL(`../../web/public/data/${REL}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(dir + 'model.json')), data = JSON.parse(fs.readFileSync(dir + 'regions.json')), ev = new Evaluator(model);
const R = data.regions[1], rows = data.yieldRows;
const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
const PLANT = new Set([...range(4, 94), ...range(106, 133)]), GRAINFED = new Set(range(99, 103));
const PASTURE = new Set([95, 96, 97, 98, 135, 136]), OTHER = new Set([104, 105, 134, 137, 138]);
for (const r of rows) if ([PLANT, GRAINFED, PASTURE, OTHER].filter(s => s.has(r)).length !== 1) throw new Error(`yield row ${r} is not in exactly one group`);
const col = c => { let s = ''; for (c += 1; c > 0; c = Math.floor((c - 1) / 26)) s = String.fromCharCode(65 + (c - 1) % 26) + s; return s; };
const res = model.sheets.resilience.cells;                       // row 2 (sheet row 3) is Australia; column c (0-based) holds return period c - 1
const factor = T => res[`2:${T + 1}`];
const cap = (yields, preset, T) => Math.round(ev.evaluate({ ...R, yield: yields }, { ...R.land, ...R.presets[preset], resilience: T, population: R.population }).capacity);
const scaled = (f, keep) => R.yield.map((y, i) => keep(rows[i]) ? y * f : y);
const lines = ['release,zone,preset,return_period,factor,factor_cell,mean_year_capacity,both_applied,crop_only,plant_rows_only,model_at_return_period,both_check,population,both_over_population,crop_only_over_population,population_over_both,population_over_crop_only,crop_only_over_both'];
for (const [preset, Ts] of [['short', [10, 20, 100]], ['long', [100]]]) {
  const mean = cap(R.yield, preset, 1);
  for (const T of Ts) {
    const f = factor(T), both = cap(scaled(f, () => true), preset, 1), crop = cap(scaled(f, r => PLANT.has(r) || GRAINFED.has(r)), preset, 1);
    const plant = cap(scaled(f, r => PLANT.has(r)), preset, 1), model_T = cap(R.yield, preset, T);
    const ok = Math.abs(both - model_T) <= 1 ? 'equal' : `DIFFERS by ${both - model_T}`;
    lines.push([REL, 1, preset, T, f.toFixed(6), `resilience!${col(T + 1)}3`, mean, both, crop, plant, model_T, ok, R.population, (both / R.population).toFixed(3), (crop / R.population).toFixed(3), (R.population / both).toFixed(3), (R.population / crop).toFixed(3), (crop / both).toFixed(3)].join(','));
  }
}
fs.writeFileSync(out, lines.join('\n') + '\n'); console.log(lines.join('\n'));
