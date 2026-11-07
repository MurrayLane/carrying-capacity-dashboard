// Why do the 53 NRM regions sum to about the capacity of the 336 SA3s and well below the 89 SA4s (results/scale_curve.csv, state yield basis)? Diagnosis on 2025-fixed, short term:
// by state, the sum of the NRM zones, of the SA4s and of the state itself; the NRM partition rebuilt from whole SA2s; and the unused land (excess) each partition leaves.
//   cd web && node ../analysis/scale_curve_2025/nrm_vs_sa_diagnosis.mjs [RELEASE] [short|long]
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const id = process.argv[2] ?? '2025-fixed', preset = process.argv[3] ?? 'short';
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), N = regions[1];
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 2 };   // 8 ACT and 9 Jervis Bay belong to the NSW-ACT zone
const run = (u, zoneId) => { const Y = regions[zoneId]; const o = ev.evaluate(Y, {   // the zone's own region record: its yields and its climate zone
   ...N.presets[preset], irrigation: Y.presets[preset].irrigation, nature2: Y.presets[preset].nature2, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }); return { cap: Number.isFinite(o.capacity) ? o.capacity : 0, excess: o.excess?.[5]?.[0] ?? 0, o }; };
const classes = Object.fromEntries(csv('data/sa2/clum_classes.csv').map(r => [r.Value, r.TERTV8.split(' ')[0].replace(/\.$/, '')])), CROP = ['3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6'], isCrop = c => CROP.some(p => c === p || c.startsWith(p + '.'));
const ZONE_OF = {}; for (const [z, codes] of Object.entries(JSON.parse(fs.readFileSync(path.join(root, 'pipeline/land/zone_to_nrm2011.json'))).zones)) for (const c of codes) ZONE_OF[c] = +z;
const piece = new Map(); for (const r of csv('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv')) { const n = +r.nrmr_code_2011; if (!(n in ZONE_OF)) continue; const k = r.zone_name + '|' + ZONE_OF[n], p = piece.get(k) ?? { sa2: r.zone_name, zone: ZONE_OF[n], total: 0, cropland: 0 }; p.total += +r.km2; if (isCrop(classes[r.class_code] ?? '')) p.cropland += +r.km2; piece.set(k, p); }
const bySa2 = {}; for (const p of piece.values()) (bySa2[p.sa2] ??= []).push(p);
const domZone = {}; for (const [s, ps] of Object.entries(bySa2)) { const key = ps.some(p => p.cropland > 0) ? 'cropland' : 'total'; domZone[s] = ps.sort((a, b) => b[key] - a[key])[0].zone; }
const sa = meth.map(r => ({ sa2: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, nrm: domZone[r.sa2_code] ?? 1, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }));
const agg = us => Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)]));
const natCap = run(agg(sa), 1).cap;
const sumBy = (key, zoneFn) => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); let cap = 0, ex = 0; for (const us of m.values()) { const r = run(agg(us), zoneFn(us[0])); cap += r.cap; ex += r.excess; } return { cap, ex, n: m.size }; };
const stZone = u => STATE_ZONE[u.state] ?? 1;
console.log(`${id} ${preset}: national ${(natCap / 1e6).toFixed(1)} M, excess land ${(run(agg(sa), 1).excess / 1e6).toFixed(2)} Mkm2 (units km2 x1e6 as in results)`);
const nrmReal = Object.values(regions).filter(z => z.kind === 'region' || z.id === 60);
let capR = 0, exR = 0; for (const z of nrmReal) { const r = run({ ...Object.fromEntries(KEYS.map(k => [k, z.land[k]])) }, z.kind === 'region' ? z.parent : z.id); capR += r.cap; exR += r.excess; }
const s4 = sumBy('sa4', stZone), sd = sumBy('nrm', u => STATE_ZONE[u.state] ?? 1);   // NRM rebuilt from whole SA2s: the state zone is that of the first SA2 (approximate)
console.log(`NRM zones as built (53): ${(capR / natCap * 100).toFixed(0)}% | excess ${exR.toFixed(0)}`);
console.log(`NRM rebuilt from whole SA2s (${sd.n}): ${(sd.cap / natCap * 100).toFixed(0)}% | excess ${sd.ex.toFixed(0)}`);
console.log(`SA4 (${s4.n}): ${(s4.cap / natCap * 100).toFixed(0)}% | excess ${s4.ex.toFixed(0)}`);
// by state: NRM zones, SA4s, state
console.log('\\nby state (share of national capacity): state itself | its NRM zones | its SA4s | land share cropping, pasture');
for (const [code, name, zone] of [[1, 'NSW', 2], [2, 'VIC', 15], [3, 'QLD', 26], [4, 'SA', 40], [5, 'WA', 49], [6, 'TAS', 56], [7, 'NT', 60]]) {
  const us = sa.filter(u => u.state === code || (code === 1 && u.state === 8)), st = run(agg(us), zone).cap;
  const nz = nrmReal.filter(z => (z.kind === 'region' ? z.parent : z.id) === zone), nrmCap = nz.reduce((a, z) => a + run(Object.fromEntries(KEYS.map(k => [k, z.land[k]])), zone).cap, 0);
  const m = new Map(); for (const u of us) (m.get(u.sa4) ?? m.set(u.sa4, []).get(u.sa4)).push(u); const sa4Cap = [...m.values()].reduce((a, g) => a + run(agg(g), zone).cap, 0);
  console.log(name.padEnd(4), (st / natCap * 100).toFixed(1).padStart(5) + '% |', (nrmCap / natCap * 100).toFixed(1).padStart(5) + '% (' + nz.length + ' zones) |', (sa4Cap / natCap * 100).toFixed(1).padStart(5) + '% (' + m.size + ' SA4s) | land', (agg(us).cropping / 316499 * 100).toFixed(0) + '% of cropping,', (agg(us).pasture / 3318689 * 100).toFixed(0) + '% of pasture');
}

// detail for chosen states: each NRM zone and each SA4 with its land mix and capacity (thousands of people), so the mismatch of crop and pasture land is visible
if (process.argv[4]) for (const [code, zone] of process.argv[4].split(',').map(s => s.split(':').map(Number))) {
  const us = sa.filter(u => u.state === code || (code === 1 && u.state === 8)), nameOfZone = z => regions[z.id]?.name ?? z.id;
  console.log(`\\nstate ${code}: NRM zones (cropping km2, pasture km2, capacity thousand, crop:pasture ratio)`);
  for (const z of nrmReal.filter(z => (z.kind === 'region' ? z.parent : z.id) === zone)) { const u = Object.fromEntries(KEYS.map(k => [k, z.land[k]])), r = run(u, zone); console.log('  ', z.name.slice(0, 32).padEnd(33), String(Math.round(u.cropping)).padStart(7), String(Math.round(u.pasture)).padStart(8), String(Math.round(r.cap / 1e3)).padStart(7), (u.cropping / Math.max(u.pasture, 1)).toFixed(2)); }
  const m = new Map(); for (const u of us) (m.get(u.sa4) ?? m.set(u.sa4, []).get(u.sa4)).push(u);
  console.log(`state ${code}: SA4s`);
  for (const [k, g] of [...m.entries()].sort((a, b) => agg(b[1]).cropping - agg(a[1]).cropping)) { const u = agg(g), r = run(u, zone); console.log('  ', ('SA4 ' + k + ' ' + (meth.find(x => hier[x.sa2_code]?.sa4_code === k)?.sa2_name ?? '')).slice(0, 32).padEnd(33), String(Math.round(u.cropping)).padStart(7), String(Math.round(u.pasture)).padStart(8), String(Math.round(r.cap / 1e3)).padStart(7), (u.cropping / Math.max(u.pasture, 1)).toFixed(2)); }
}

// stranded pasture: the share of the nation's pasture lying in units whose cropping land is under 2% of their pasture (rangelands with no crops to pair with), and what those units contribute
{ const part = (label, groups) => { let strandedPasture = 0, strandedCap = 0, stranded = 0, totalCap = 0; for (const [u, zone] of groups) { const r = run(u, zone); totalCap += r.cap; if (u.cropping < 0.02 * u.pasture && u.pasture > 1000) { strandedPasture += u.pasture; strandedCap += r.cap; stranded++; } }
    console.log(label.padEnd(34), 'pasture-only units:', String(stranded).padStart(3), '| their pasture', (strandedPasture / 3318689 * 100).toFixed(0).padStart(3) + '% of the nation\'s | their capacity', (strandedCap / natCap * 100).toFixed(1) + '% of national | all units', (totalCap / natCap * 100).toFixed(0) + '%'); };
  console.log('\\nstranded pasture by partition (short term):');
  part('NRM zones as built', nrmReal.map(z => [Object.fromEntries(KEYS.map(k => [k, z.land[k]])), z.kind === 'region' ? z.parent : z.id]));
  const grp = key => { const m = new Map(); for (const u of sa) (m.get(u[key]) ?? m.set(u[key], []).get(u[key])).push(u); return [...m.values()].map(g => [agg(g), STATE_ZONE[g[0].state] ?? 1]); };
  part('SA4 (89)', grp('sa4')); part('SA3 (336)', grp('sa3')); part('SA2 (2,450)', sa.map(u => [u, STATE_ZONE[u.state] ?? 1])); }
