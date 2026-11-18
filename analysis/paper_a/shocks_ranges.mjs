// B112 (decision 102): ranges on the shocked figures of Paper A section 8 and Table 6. Release 2025-fixed (the corrected release), short-term settings,
// return periods 1 (average year, for reference), 10 and 20, for Australia, the states and the 52 regions (all 60 zones of the Monte Carlo).
//   node analysis/paper_a/shocks_ranges.mjs analysis/paper_a/shocks_ranges.csv      (repository root; needs the built data)
// Method. The model scales every yield of a zone by one factor (Yield!C2), the zone's row of the resilience sheet at the return period (Australia resilience!B3,
// New South Wales B4, Victoria B5, Queensland B6, South Australia B7, Western Australia B8, Tasmania B9, Northern Territory B10, by the zone number as in Yield!C2).
// Capacity is linear in the yields, so a draw's shocked capacity is its average-year capacity times that factor. Each Monte Carlo draw of
// analysis/sensitivity_2025/monte_carlo_draws_<set>.csv is multiplied by its zone's factor and the 5th, 50th and 95th percentiles are taken (the percentile
// rule of summarise_mc.py). central is the release itself evaluated at the return period. Check, written to the console (the script stops above 0.5%): in every zone
// the release's capacity at 10 and 20 years equals its average-year capacity times the factor; it does to under 0.001% in 59 zones, and to 0.24% and 0.39% in Northern and
// Yorke (zone 45), the one zone where the scaling is not exact. The draws were checked the same way in B112 (report).
// B123 (decision 115): `node analysis/paper_a/shocks_ranges.mjs analysis/paper_a/shocks_ranges_wide.csv --wide` reads the widened draws instead (19 choices, 2,000 draws, the headline range of decision 115;
// analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv, which is monte_carlo.mjs with MC_WIDE=1 MC_LONG=1 and its default eight zones, Australia and the seven states, 2,000 draws:
// the national column is the block A of monte_carlo_draws_2025-fixed_wide.csv to the person, checked below) and writes the same columns plus share_draws_below_population, the share of the draws whose
// shocked capacity is under the zone's own population. The drought factor is the release table's, applied to every draw, as in B112: the widened draws carry the choice `restable` (0 the release table of all
// years, 1 the leave-one-out table, 1,000 draws each), which acts on the long term only (short-term resilience is 1 in every draw), so it does not change a short-term draw. A second file, <out>_own_table.csv
// (same columns), applies the factor of a draw's own table to its shocked figure (the leave-one-out row of 2025-resilience-loo for restable = 1): the alternative V38 raised for B112.
// Draw sets: the published 1,000 draws (three meat windows) and, where present, the B112 herd-cycle draws (four full-cycle windows) and the base-plus-four set.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const out = process.argv[2] ?? 'analysis/paper_a/shocks_ranges.csv', REL = '2025-fixed';
const root = new URL('../../', import.meta.url).pathname, dir = `${root}web/public/data/${REL}/`;
const model = JSON.parse(fs.readFileSync(dir + 'model.json')), data = JSON.parse(fs.readFileSync(dir + 'regions.json')), ev = new Evaluator(model);
const res = model.sheets.resilience.cells;
const resRow = z => z === 1 ? 2 : z < 15 ? 3 : z < 26 ? 4 : z < 40 ? 5 : z < 49 ? 6 : z < 56 ? 7 : z < 60 ? 8 : 9;      // Yield!C2: zone number -> resilience!B3..B10 (0-based row 2..9)
const col = c => { let s = ''; for (c += 1; c > 0; c = Math.floor((c - 1) / 26)) s = String.fromCharCode(65 + (c - 1) % 26) + s; return s; };
const factor = (z, T) => res[`${resRow(z)}:${T + 1}`];
const WIDE = process.argv.includes('--wide');
const SETS = WIDE ? [['2025-fixed_wide_states', 'widened range: 19 choices, 2,000 draws (B115, decision 115), Australia and the seven states (B123)', `${root}analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide_states.csv`]] : [['2025-fixed_all', 'three meat windows (published range, results/ranges_2025-fixed.csv)'],
              ['2025-fixed_herdcycle_all', 'four full-cycle meat windows (B112, results/ranges_2025-fixed_herdcycle.csv)'],
              ['2025-fixed_herdcycle5_all', 'base window and four full-cycle meat windows (B112 variant, results/ranges_2025-fixed_herdcycle5.csv)']]
  .map(([id, label]) => [id, label, `${root}analysis/sensitivity_2025/monte_carlo_draws_${id}.csv`]).filter(s => fs.existsSync(s[2]));
if (WIDE && !SETS.every(s => fs.existsSync(s[2]))) { console.error('the widened draws file is missing'); process.exit(1); }
const pct = (v, q) => { const s = [...v].sort((a, b) => a - b), i = q * (s.length - 1), lo = Math.floor(i), hi = Math.min(lo + 1, s.length - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo); };
const zones = Object.keys(data.regions).map(Number).sort((a, b) => a - b);
const central = {}; let worst = 0;
for (const z of zones) { const R = data.regions[z];
  for (const T of [1, 10, 20]) { central[`${z}_${T}`] = ev.evaluate(R, { ...R.land, ...R.presets.short, resilience: T, population: R.population }).capacity;
    if (T > 1 && central[`${z}_1`] > 0) worst = Math.max(worst, Math.abs(central[`${z}_${T}`] / (central[`${z}_1`] * factor(z, T)) - 1)); } }
console.error(`check: release capacity at 10 and 20 years over (average year x factor), largest deviation over ${zones.length} zones: ${(100 * worst).toFixed(4)}%`);
if (worst > 5e-3) { console.error('the shocked capacity is not the average-year capacity times the factor; stop'); process.exit(1); }
const r3 = x => x.toFixed(3);
const HEAD = 'release,draws,draws_description,n_draws,preset,return_period,zone,name,kind,population,factor,factor_cell,central,p5,p50,p95,population_over_capacity_central,population_over_capacity_at_p5,population_over_capacity_at_p95,capacity_over_population_central,capacity_over_population_p5,capacity_over_population_p95,population_inside_p5_p95';
const lines = [HEAD + (WIDE ? ',share_draws_below_population' : '')], own = [HEAD + ',share_draws_below_population'];
// the leave-one-out resilience table (release 2025-resilience-loo), which the widened draws' restable = 1 stands for; read only for the own-table file
const looRes = WIDE ? JSON.parse(fs.readFileSync(`${root}web/public/data/2025-resilience-loo/model.json`)).sheets.resilience.cells : null;
for (const [id, label, file] of SETS) {
  const L = fs.readFileSync(file, 'utf8').trim().split(/\r?\n/), H = L[0].split(','), D = L.slice(1).map(l => l.split(',').map(Number)), rt = H.indexOf('restable');
  for (const T of [1, 10, 20]) for (const z of zones) {
    const R = data.regions[z], c = H.indexOf(`${z}_short`); if (c < 0) continue;
    const f = factor(z, T), v = D.map(r => r[c] * f), [p5, p50, p95] = [0.05, 0.5, 0.95].map(q => pct(v, q)), C = central[`${z}_${T}`], P = R.population;
    const row = (p5, p50, p95, fcol, fcell, share) => [REL, id, JSON.stringify(label), D.length, 'short', T, z, JSON.stringify(R.name), R.kind, P, fcol, fcell,
      Math.round(C), Math.round(p5), Math.round(p50), Math.round(p95), r3(P / C), r3(P / p5), r3(P / p95), r3(C / P), r3(p5 / P), r3(p95 / P), P >= p5 && P <= p95 ? 'yes' : (P < p5 ? 'no: population below the range' : 'no: population above the range'),
      ...(share === null ? [] : [share])].join(',');
    lines.push(row(p5, p50, p95, f.toFixed(6), `resilience!${col(T + 1)}${resRow(z) + 1}`, WIDE ? (v.filter(x => x < P).length / v.length).toFixed(4) : null));
    if (WIDE) {
      const fl = looRes[`${resRow(z)}:${T + 1}`], w = D.map((r, i) => r[c] * (r[rt] === 1 ? fl : f)), [q5, q50, q95] = [0.05, 0.5, 0.95].map(q => pct(w, q));
      own.push(row(q5, q50, q95, `${f.toFixed(6)} (restable 0); ${fl.toFixed(6)} (restable 1)`, `resilience!${col(T + 1)}${resRow(z) + 1} of this release and of 2025-resilience-loo`, (w.filter(x => x < P).length / w.length).toFixed(4)));
    }
  }
}
fs.writeFileSync(out, lines.join('\n') + '\n');
if (WIDE) fs.writeFileSync(out.replace(/\.csv$/, '_own_table.csv'), own.join('\n') + '\n');
for (const l of lines) if (/,1,"Australia",/.test(l)) console.log(l);
