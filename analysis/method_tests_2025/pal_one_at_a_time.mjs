// B134 (decision 141): the energy requirement one at a time, everything else at base. The model's energy requirement is the food amount (Settings!B9, preset field `food`, 1 at base)
// times the sedentary NHMRC diet, PAL 1.4 (8.0 MJ a day as eaten at base); so PAL p is food = p / 1.4 (the same scale analysis/sensitivity_2025/monte_carlo.mjs draws, 1 to 1.8/1.4 = 1.286).
//   node analysis/method_tests_2025/pal_one_at_a_time.mjs [OUT.csv]      (repository root; needs the built data)
//   node analysis/method_tests_2025/pal_one_at_a_time.mjs --wrong-value-demo      shows the check failing on a planted wrong value (writes nothing)
// PAL 1.2 and 2.2 are the ends of the NHMRC range; 1.4 to 1.8 is the drawn window. Short and long presets, releases 2025-fixed and 2025-improved. The Monte Carlo draws the requirement in the short term only.
// Check: PAL 1.4 (food = 1) must equal the base capacity of results/<release>.csv, and capacity must fall as PAL rises.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const args = process.argv.slice(2), DEMO = args.includes('--wrong-value-demo'), out = args.find(a => !a.startsWith('--')) ?? 'analysis/method_tests_2025/pal_one_at_a_time_2025.csv';
const root = new URL('../../', import.meta.url).pathname;
const lines = ['release,preset,pal,food_amount,energy_mj_per_day,capacity,change_from_base,change_pct,capacity_times_pal_over_base'];
let ok = true;
for (const REL of ['2025-fixed', '2025-improved']) {
  const dir = `${root}web/public/data/${REL}/`, model = JSON.parse(fs.readFileSync(dir + 'model.json')), R = JSON.parse(fs.readFileSync(dir + 'regions.json')).regions[1], ev = new Evaluator(model);
  const pub = fs.readFileSync(`${root}results/${REL}.csv`, 'utf8').trim().split('\n').map(l => l.split(','));
  const h = pub[0], zi = h.indexOf('zone'), pi = h.indexOf('preset'), ci = h.indexOf('capacity');
  for (const preset of ['short', 'long']) {
    const P = R.presets[preset], run = pal => ev.evaluate(R, { ...R.land, ...P, food: P.food * pal / 1.4, population: R.population });
    const base = run(1.4), ref = +pub.slice(1).find(r => r[zi] === '1' && r[pi] === preset)[ci];
    const shown = DEMO && REL === '2025-fixed' && preset === 'short' ? base.capacity + 1e6 : base.capacity;   // EXAMPLE wrong value in demo mode only
    const same = Math.abs(shown - ref) <= 1e-6 * ref; ok &&= same;
    console.log(`check ${REL} ${preset}: PAL 1.4 capacity ${shown} vs results csv ${ref}: ${same ? 'PASS' : 'FAIL'}`);
    let prev = Infinity;
    for (const pal of [1.2, 1.4, 1.8, 2.2]) {
      const r = run(pal); ok &&= r.capacity < prev; prev = r.capacity;
      lines.push([REL, preset, pal, (P.food * pal / 1.4).toFixed(4), (8.0 * pal / 1.4).toFixed(2), r.capacity, r.capacity - base.capacity, (100 * (r.capacity / base.capacity - 1)).toFixed(1), (r.capacity * pal / 1.4 / base.capacity).toFixed(3)].join(','));
    }
  }
}
console.log(lines.join('\n'));
if (DEMO) { console.log('EXAMPLE (deliberate wrong value): the 2025-fixed short PAL 1.4 capacity planted 1 million high; nothing written'); process.exit(ok ? 1 : 0); }
if (!ok) { console.error('a check failed'); process.exit(1); }
fs.writeFileSync(out, lines.join('\n') + '\n');
