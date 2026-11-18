// B137 item 3 (R05a issue 3 (b)): the part of the land-and-livestock rise that a change in what counts as grazing area could account for, as an upper bound.
//   node analysis/paper_a/definitional_residue.mjs analysis/paper_a/definitional_residue.csv      (repository root; needs the built data: cd web && node scripts/build-data.mjs)
// Reasoning: the livestock yields divide output by the grazing area, so a change of area definition cancels where pasture binds, EXCEPT for the idle cropland ceded to pasture, which the model credits at the pasture yield per square metre.
// Test: take release 2025-fixed, Australia, and give it the 2011 grazing area (pasture x k, k = 2011 pasture / 2025 pasture; the added area comes out of non-agricultural land so the total is unchanged) with OUTPUT and DIET held fixed:
// every pasture-fed yield row (sheep meat, wool, milk, cattle meat, goat and sheep milk: rows 95 to 98, 135, 136) is divided by k. The fall in capacity is the most the whole 2011-to-2025 fall in grazing area could have contributed if ALL of it were a change of definition.
// Rows 95, 96 and 98 carry feedlot grain land in their denominator, so dividing the whole row by k slightly overstates the area effect: the bound is an upper bound.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2] ?? 'analysis/paper_a/definitional_residue.csv';
const load = id => { const d = new URL(`../../web/public/data/${id}/`, import.meta.url).pathname; return { model: JSON.parse(fs.readFileSync(d + 'model.json')), data: JSON.parse(fs.readFileSync(d + 'regions.json')) }; };
const A = load('2025-fixed'), B = load('2011-fixed-3'), ev = new Evaluator(A.model);
const R = A.data.regions[1], rows = A.data.yieldRows, PASTURE = new Set([95, 96, 97, 98, 135, 136]);
const k = B.data.regions[1].land.pasture / R.land.pasture;
const cap = (R2, land, preset) => ev.evaluate(R2, { ...land, ...R.presets[preset], population: R.population }).capacity;
const lines = ['preset,k_2011_over_2025_pasture,capacity_2025_fixed,capacity_with_2011_grazing_area_output_fixed,fall_people,fall_percent,combined_layer_short_term_people,share_of_combined_layer_percent'];
const COMB = { short: 2456649, long: -598893 };           // land and livestock as one layer, eight-layer average (capacity_by_cause_corrected_orders.csv)
for (const preset of ['short', 'long']) {
  const base = cap(R, R.land, preset);
  const land = { ...R.land, pasture: R.land.pasture * k, nonAg: R.land.nonAg - R.land.pasture * (k - 1) };
  if (land.nonAg < 0) throw new Error('not enough non-agricultural land');
  const y = R.yield.map((v, i) => PASTURE.has(rows[i]) ? v / k : v);
  const alt = cap({ ...R, yield: y }, land, preset);
  lines.push([preset, k.toFixed(5), Math.round(base), Math.round(alt), Math.round(base - alt), (100 * (base - alt) / base).toFixed(2), COMB[preset], preset === 'short' ? (100 * (base - alt) / COMB[preset]).toFixed(1) : ''].join(','));
}
fs.writeFileSync(out, lines.join('\n') + '\n'); console.log(lines.join('\n'));
