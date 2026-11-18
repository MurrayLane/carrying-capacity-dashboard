// B134 (decision 141): the crop-only drought bound for every weather figure Paper B prints, national, short term at 1 in 5, 10, 20, 50 and 100, long term at 1 in 100,
// on release 2025-fixed (Paper B's corrected method) and 2025-improved (the improved method Paper B quotes beside it).
//   node analysis/resilience_2025/drought_bounds_paper_B.mjs [analysis/resilience_2025/drought_bounds_paper_B.csv]     (repository root; needs the built data: cd web && node scripts/build-data.mjs)
//   node analysis/resilience_2025/drought_bounds_paper_B.mjs --wrong-value-demo      shows the check failing on a planted wrong value (writes nothing)
// Same rule as B112 (drought_bounds.mjs, unchanged, its csv kept): the factor of the zone's resilience row at the return period multiplies
//   both applied   every yield row (the model's own rule; must equal the model run at that return period, the first check)
//   crop only      plant rows 4 to 94 and 106 to 133 plus the grain-fed animal rows 99 to 103; pasture-fed rows (95 to 98, 135, 136), fish, honey, timber held at the mean year
//   plant rows only  as crop only with the grain-fed animal rows also held (the strict reading)
// 2025-improved: the row-scaling rule does not reproduce that release's own drought run exactly (0.1 to 0.4% low, cause not identified), so its rows are an approximate bound, flagged in both_check and outside the pass test.
// The 2025-fixed rows for T = 10, 20, 100 short and 100 long must equal drought_bounds.csv (the second check). Added here: T = 5 and 50 (the failure curve's run points) and 2025-improved.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const args = process.argv.slice(2), DEMO = args.includes('--wrong-value-demo'), out = args.find(a => !a.startsWith('--')) ?? 'analysis/resilience_2025/drought_bounds_paper_B.csv';
const root = new URL('../../', import.meta.url).pathname;
const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
const PLANT = new Set([...range(4, 94), ...range(106, 133)]), GRAINFED = new Set(range(99, 103));
const PASTURE = new Set([95, 96, 97, 98, 135, 136]), OTHER = new Set([104, 105, 134, 137, 138]);
const lines = ['release,preset,return_period,factor,mean_year_capacity,both_applied,crop_only,plant_rows_only,model_at_return_period,both_check,population,both_pct_below_mean,crop_only_pct_below_mean,mean_over_both,mean_over_crop_only,crop_only_over_both'];
const table = {};
let ok = true;
for (const REL of ['2025-fixed', '2025-improved']) {
  const dir = `${root}web/public/data/${REL}/`;
  const model = JSON.parse(fs.readFileSync(dir + 'model.json')), data = JSON.parse(fs.readFileSync(dir + 'regions.json')), ev = new Evaluator(model);
  const R = data.regions[1], rows = data.yieldRows;
  for (const r of rows) if ([PLANT, GRAINFED, PASTURE, OTHER].filter(s => s.has(r)).length !== 1) throw new Error(`yield row ${r} is not in exactly one group`);
  const res = model.sheets.resilience.cells, factor = T => res[`2:${T + 1}`];
  const cap = (yields, preset, T) => Math.round(ev.evaluate({ ...R, yield: yields }, { ...R.land, ...R.presets[preset], resilience: T, population: R.population }).capacity);
  const scaled = (f, keep) => R.yield.map((y, i) => keep(rows[i]) ? y * f : y);
  for (const [preset, Ts] of [['short', [5, 10, 20, 50, 100]], ['long', [100]]]) {
    const mean = cap(R.yield, preset, 1);
    for (const T of Ts) {
      const f = factor(T), both = cap(scaled(f, () => true), preset, 1), crop = cap(scaled(f, r => PLANT.has(r) || GRAINFED.has(r)), preset, 1);
      const plant = cap(scaled(f, r => PLANT.has(r)), preset, 1), modelT = cap(R.yield, preset, T);
      const shown = DEMO && REL === '2025-fixed' && preset === 'short' && T === 100 ? both + 1000000 : both;   // EXAMPLE wrong value in demo mode only
      const same = Math.abs(shown - modelT) <= 1; if (REL === '2025-fixed') ok &&= same;
      table[`${REL}|${preset}|${T}`] = { both, crop, mean };
      lines.push([REL, preset, T, f.toFixed(6), mean, shown, crop, plant, modelT, same ? 'equal' : REL === '2025-fixed' ? `DIFFERS by ${shown - modelT}` : `rule differs from the release's own run by ${shown - modelT} (approximate bound)`, R.population,
        (100 * (1 - shown / mean)).toFixed(1), (100 * (1 - crop / mean)).toFixed(1), (mean / shown).toFixed(3), (mean / crop).toFixed(3), (crop / shown).toFixed(3)].join(','));
    }
  }
}
// Second check: the 2025-fixed rows against B112's csv.
const b112 = fs.readFileSync(root + 'analysis/resilience_2025/drought_bounds.csv', 'utf8').trim().split('\n').slice(1).map(l => l.split(','));
for (const r of b112) {
  const t = table[`${r[0]}|${r[2]}|${r[3]}`];
  if (!t || t.both !== +r[7] || t.crop !== +r[8] || t.mean !== +r[6]) { ok = false; console.error('DIFFERS from drought_bounds.csv:', r.slice(0, 4).join(' ')); }
}
console.log(lines.join('\n'));
console.log(ok ? 'checks: PASS (2025-fixed: both-applied equals the model at every return period; 2025-fixed rows equal drought_bounds.csv)' : 'checks: FAIL');
if (DEMO) { console.log('EXAMPLE (deliberate wrong value): 2025-fixed short 1 in 100 both-applied planted 1,000,000 high; nothing written'); process.exit(ok ? 1 : 0); }
if (!ok) process.exit(1);
fs.writeFileSync(out, lines.join('\n') + '\n');
