// Murray 2026-11-03: if people were forced into smaller self-sufficiency, more cropping land might be found at small scale (back yards). A sensitivity on the scale curve: a share F of each unit's
// infrastructure land (the urban land of the 2011 method: houses, gardens, roads) is turned into cropping land at the yields of the unit's state; short term, default diet and a 2.5% meat-and-egg diet.
// What is measured: the people the urban SA4s could feed from their own land, against their population. Not a claim about how much garden there is: F is varied from 0 to 0.5.
//   cd web && node ../analysis/scale_curve_2025/urban_gardens_test.mjs [RELEASE]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r])), erp = Object.fromEntries(csv('data/sa2/population_erp.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), N = regions[1];
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 2 };   // 8 ACT and 9 Jervis Bay belong to the NSW-ACT zone; the NT zone (60) is its own state
const sa = meth.map(r => ({ sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2, pop: +erp[r.sa2_code]?.['2025'] || 0 }));
const agg = us => Object.fromEntries(KEYS.concat('pop').map(k => [k, us.reduce((a, u) => a + u[k], 0)]));
const cap = (u, state, over, F) => { const z = regions[STATE_ZONE[state] ?? 1], v = { ...u, cropping: u.cropping + F * u.infrastr1, infrastr1: u.infrastr1 * (1 - F) }; return ev.evaluate(z, { ...N.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...over, ...Object.fromEntries(KEYS.map(k => [k, v[k]])), population: 1 }).capacity || 0; };
const m = new Map(); for (const u of sa) (m.get(u.sa4) ?? m.set(u.sa4, []).get(u.sa4)).push(u);
const sa4 = [...m.values()].map(us => ({ ...agg(us), state: us[0].state, dens: agg(us).pop / Math.max(1, KEYS.reduce((a, k) => a + agg(us)[k], 0)) }));
const urban = sa4.filter(u => u.dens > 300 && u.pop > 50000);               // people a km2: the metropolitan SA4s
console.log(`${id} ${preset}: ${urban.length} urban SA4s (more than 300 people a km2), population ${(urban.reduce((a, u) => a + u.pop, 0) / 1e6).toFixed(1)} M of ${(sa4.reduce((a, u) => a + u.pop, 0) / 1e6).toFixed(1)} M; their infrastructure land ${(urban.reduce((a, u) => a + u.infrastr1, 0)).toFixed(0)} km2 of ${agg(sa).infrastr1.toFixed(0)} km2 nationally, cropping ${urban.reduce((a, u) => a + u.cropping, 0).toFixed(0)} km2`);
for (const [label, over] of [['default diet', {}], ['2.5% meat and eggs', { meategg: 0.025 }]]) for (const F of [0, 0.1, 0.25, 0.5]) {
  const c = urban.reduce((a, u) => a + cap(u, u.state, over, F), 0), natF = cap(agg(sa), 0, over, F), nat0 = cap(agg(sa), 0, over, 0), allSa4 = sa4.reduce((a, u) => a + cap(u, u.state, over, F), 0);
  console.log(`${label.padEnd(20)} garden share ${String(F).padEnd(4)} | urban SA4s feed ${(c / 1e3).toFixed(0).padStart(6)} thousand (${(c / urban.reduce((a, u) => a + u.pop, 0) * 100).toFixed(1)}% of their population) | all SA4s ${(allSa4 / 1e6).toFixed(1)} M | nation ${(natF / 1e6).toFixed(1)} M (${((natF / nat0 - 1) * 100).toFixed(1)}% over no gardens)`); }

// the scale curve with adaptation: small units switch to a 2.5% meat-and-egg diet and turn half their infrastructure land to crops, against the national capacity on today's diet (41.5 M)
{ const natToday = cap(agg(sa), 0, {}, 0); console.log(`\nscale curve with adaptation (state yields; share of the national capacity on today's diet, ${(natToday / 1e6).toFixed(1)} M):`);
  const groupsBy = key => { const mm = new Map(); for (const u of sa) (mm.get(u[key]) ?? mm.set(u[key], []).get(u[key])).push(u); return [...mm.values()].map(us => ({ ...agg(us), state: us[0].state })); };
  const sa3 = (() => { const mm = new Map(); meth.forEach((r, i) => { const k = hier[r.sa2_code]?.sa3_code; (mm.get(k) ?? mm.set(k, []).get(k)).push(sa[i]); }); return [...mm.values()].map(us => ({ ...agg(us), state: us[0].state })); })();
  const levels = [['State', (() => { const mm = new Map(); for (const u of sa) { const k = u.state === 8 || u.state === 9 ? 1 : u.state; (mm.get(k) ?? mm.set(k, []).get(k)).push(u); } return [...mm.values()].map(us => ({ ...agg(us), state: us[0].state })); })()], ['SA4', groupsBy('sa4')], ['SA3', sa3], ['SA2', sa.map(u => ({ ...u }))]];
  for (const [name, units] of levels) { const row = [['today', {}, 0], ['low-meat diet', { meategg: 0.025 }, 0], ['low-meat diet and gardens (half the urban land)', { meategg: 0.025 }, 0.5]].map(([l, over, F]) => `${l}: ${(units.reduce((a, u) => a + cap(u, u.state, over, F), 0) / natToday * 100).toFixed(0)}%`); console.log(name.padEnd(6), row.join(' | ')); } }
