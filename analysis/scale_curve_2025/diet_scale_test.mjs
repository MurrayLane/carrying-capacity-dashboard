// To what extent can diet recover the capacity lost at smaller scales? Short term, state yield basis (as results/scale_curve.csv): at each level (nation, state, SA4, SA3, SA2) the sum of capacities with
// the meat-and-egg share fixed at 0, 2.5, 5, 7.5% and today's 12%, and with every unit choosing its best diet from a grid (meat and eggs 0 to 15%, red meat 0 to 100% of the meat). Shares are of the
// national capacity on today's diet. Writes analysis/scale_curve_2025/diet_scale.csv.   cd web && node ../analysis/scale_curve_2025/diet_scale_test.mjs [RELEASE]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), N = regions[1];
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 2 };   // 8 ACT and 9 Jervis Bay belong to the NSW-ACT zone; the NT zone (60) is its own state
const sa = meth.map(r => ({ sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }));
const agg = us => ({ ...Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)])), state: us[0].state });
const cap = (u, over) => { const z = regions[STATE_ZONE[u.state] ?? 1]; const o = ev.evaluate(z, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const grp = key => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()].map(agg); };
const natU = { ...agg(sa), state: 0 }; const levels = [['Australia', [natU]], ['State', (() => { const m = new Map(); for (const u of sa) { const k = u.state === 8 || u.state === 9 ? 1 : u.state; (m.get(k) ?? m.set(k, []).get(k)).push(u); } return [...m.values()].map(agg); })()], ['SA4', grp('sa4')], ['SA3', grp('sa3')], ['SA2', sa.map(u => ({ ...u }))]];
const natToday = cap(natU, {});
const grid = []; for (const m of [0, 0.025, 0.05, 0.075, 0.1, 0.12, 0.15]) for (const r of [0, 0.25, 0.578, 1]) grid.push({ meategg: m, redmeat: r });
const rows = [['level', 'units', 'diet', 'sum_capacity_million', 'share_of_national_today', 'share_of_same_diet_national']]; const natBy = {};
for (const [name, units] of levels) {
  const res = [];
  for (const m of [0, 0.025, 0.05, 0.075, 0.12]) res.push([`${(m * 100).toFixed(1).replace('.0', '')}% meat and eggs`, units.reduce((a, u) => a + cap(u, { meategg: m }), 0)]);
  res.push(['each unit its best diet', units.reduce((a, u) => a + Math.max(...grid.map(d => cap(u, d))), 0)]);
  for (const [d, c] of res) { if (name === 'Australia') natBy[d] = c; rows.push([name, units.length, d, (c / 1e6).toFixed(1), (c / natToday * 100).toFixed(0), (c / natBy[d] * 100).toFixed(0)]); }
  console.log(name.padEnd(10), String(units.length).padStart(5), res.map(([d, c]) => `${d.replace(' meat and eggs', '')}: ${(c / natToday * 100).toFixed(0)}%`).join(' | ')); }
fs.writeFileSync(path.join(root, 'analysis/scale_curve_2025/diet_scale.csv'), rows.map(r => r.join(',')).join('\n') + '\n');
