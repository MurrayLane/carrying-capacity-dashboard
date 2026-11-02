// How good could a split be? On the national yield vector (one basis for every unit): (1) is capacity proportional to land? (2) the sum of capacities for random groupings of the SA2s into K groups
// (no geography), for the NRM zones and the SA4s on the same basis, and for the SA2s themselves.   cd web && node ../analysis/scale_curve_2025/ideal_split_test.mjs [RELEASE] [short|long]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = process.argv[3] ?? 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), N = regions[1];
const cap = u => { const o = ev.evaluate(N, { ...N.presets[preset], ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
const sa = meth.map(r => ({ sa4: hier[r.sa2_code]?.sa4_code, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }));
const agg = us => Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)]));
const nat = agg(sa), natCap = cap(nat);
console.log(`${id} ${preset}, national yield vector: national capacity ${(natCap / 1e6).toFixed(1)} M`);
for (const f of [0.5, 0.1, 0.01]) console.log(`  capacity of ${f} x the national land: ${(cap(Object.fromEntries(KEYS.map(k => [k, nat[k] * f]))) / natCap / f * 100).toFixed(1)}% of ${f} x the national capacity`);
let seed = 12345; const rnd = () => (seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296;
const groupsOf = (key) => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()]; };
const share = gs => gs.reduce((a, us) => a + cap(agg(us)), 0) / natCap * 100;
console.log(`SA4 (${groupsOf('sa4').length} units): ${share(groupsOf('sa4')).toFixed(0)}%   SA2s: ${share(sa.map(u => [u])).toFixed(0)}%`);
for (const K of [7, 53, 89, 336]) { const out = []; for (let rep = 0; rep < 5; rep++) { const gs = Array.from({ length: K }, () => []); for (const u of sa) gs[Math.floor(rnd() * K)].push(u); out.push(share(gs.filter(g => g.length))); } console.log(`random groups of SA2s, K=${K}: ${out.map(x => x.toFixed(0)).join(', ')}%`); }
// the real partitions on the same (national-yield) basis: the NRM zones as built, the states, the SA3s
const nrm = Object.values(regions).filter(z => z.kind === 'region' || z.id === 60).map(z => Object.fromEntries(KEYS.map(k => [k, z.land[k]])));
console.log(`NRM zones (${nrm.length} units): ${(nrm.reduce((a, u) => a + cap(u), 0) / natCap * 100).toFixed(0)}%`);
const sa3 = (() => { const m = new Map(); meth.forEach((r, i) => { const k = hier[r.sa2_code]?.sa3_code; (m.get(k) ?? m.set(k, []).get(k)).push(sa[i]); }); return [...m.values()]; })();
console.log(`SA3 (${sa3.length} units): ${share(sa3).toFixed(0)}%`);
