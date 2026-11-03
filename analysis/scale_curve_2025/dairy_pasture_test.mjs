// Murray 2026-11-03: pasture quality. The model has one pasture land type; each animal product has a regional yield (g per m2 of pasture) found by dividing the region's total grazing land among its animals by
// Dry Sheep Equivalent (thesis step 10), so dairy is credited with an average share of all the pasture, not with the good (improved, irrigated) pasture it really uses. Sensitivity: the dairy milk yield (Yield!97) times
// 1, 3 and 5 in every unit (a stand-in for dairy on better land), at the national level and summed over the SA4s and SA2s, today's diet and 2.5% meat and eggs, short term, state yields.
//   cd web && node ../analysis/scale_curve_2025/dairy_pasture_test.mjs [RELEASE]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const RJ = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))); const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = RJ.regions, ev = new Evaluator(model), N = regions[1];
const DAIRY = RJ.yieldRows.indexOf(97); console.log('dairy milk Yield row index', DAIRY, '| national value (g/m2):', N.yield[DAIRY]);
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };
const sa = meth.map(r => ({ sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }));
const agg = us => ({ ...Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)])), state: us[0].state });
const cap = (u, over, f) => { const z = regions[STATE_ZONE[u.state] ?? 1], y = z.yield.slice(); y[DAIRY] *= f; return ev.evaluate({ ...N, yield: y }, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity || 0; };
const m4 = new Map(); for (const u of sa) (m4.get(u.sa4) ?? m4.set(u.sa4, []).get(u.sa4)).push(u);
const levels = [['Australia', [{ ...agg(sa), state: 9 }]], ['SA4', [...m4.values()].map(agg)], ['SA2', sa]];
const base = cap({ ...agg(sa), state: 9 }, {}, 1);
console.log(`share of the national capacity on today's diet (${(base / 1e6).toFixed(1)} M); dairy milk yield multiplied by 1 / 3 / 5`);
for (const [name, units] of levels) for (const [dl, over] of [['today\'s diet', {}], ['2.5% meat and eggs', { meategg: 0.025 }]]) console.log(name.padEnd(10), dl.padEnd(20), [1, 3, 5].map(f => `${(units.reduce((a, u) => a + cap(u, over, f), 0) / base * 100).toFixed(0)}%`).join(' / '));
