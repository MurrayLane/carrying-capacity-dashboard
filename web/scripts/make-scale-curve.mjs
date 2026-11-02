// results/scale_curve.csv: how capacity falls as the unit of self-sufficiency shrinks (the scale effect of Lane, Dawes and Grace 2015, extended to SA2), for the six cells of the comparison grid.
// The sum of capacities of a level is the people its units could feed if each had to feed itself from its own land. Each unit is evaluated with ITS OWN yields and its own irrigation and nature-reserve
// settings (the other settings are the national zone's), as the zones are in the release:
//   Australia, State (7 zones), NRM region (the 52 regions plus the Northern Territory): the release's own zones, land and population (land basis "release")
//   SA4, SA3, SA2: land by the 2011 method on 2020-21 data (data/sa2/land_2011_method_by_sa2.csv) and the ERP of the release's vintage year (land basis "2020-21 land"). An SA2's yields and its irrigation and nature-reserve settings are those of the
//   NRM zone that holds most of its cropland (the allocation `pipeline/yields/recent/zone_yields.py` uses); a coarser unit takes the zone holding most of its cropland (area where it has none). Averaging yield vectors was tried and
//   rejected: it inflates the yields of crops grown in a few zones (the Australia unit then reaches 77 million, not 33).
//   The Australia row of the SA group is its own reference. The 2011 cells' SA shares are against the 2020-21 land national and are not exactly comparable with their zone levels (the 2011 land by SA2 does not exist).
// Two yield bases (column yield_basis): "local" = each unit takes the yields of its own (zone levels) or dominant (SA levels) NRM zone, which overstates the yields of units larger than a zone (SA4) and mixes bases across levels;
// "state" = each unit takes the yields and settings of its parent state's zone (zone levels: the state's own), one consistent basis, which is monotone and conservative (it ignores yield differences within a state).
// Usage: cd web && npm run build:data && node scripts/make-scale-curve.mjs
import fs from 'node:fs';
import path from 'node:path';
import { root } from './releases.mjs';
import { Evaluator } from '../src/model/evaluator.js';
import { dataDir, PRESETS } from './results-lib.mjs';

const CELLS = ['2011-corrected', '2011-fixed', '2011-improved', '2025-mirror', '2025-fixed', '2025-improved'];
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r])), erp = Object.fromEntries(csv('data/sa2/population_erp.csv').map(r => [r.sa2_code, r]));
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
// SA2 to zone shares (cropland where the SA2 has any, else total area), as pipeline/yields/recent/zone_yields.py
const classes = Object.fromEntries(csv('data/sa2/clum_classes.csv').map(r => [r.Value, r.TERTV8.split(' ')[0].replace(/\.$/, '')]));
const CROPLAND = ['3.3', '3.4', '3.5', '3.6', '4.3', '4.4', '4.5', '4.6'], isCrop = c => CROPLAND.some(p => c === p || c.startsWith(p + '.'));
const ZONE_OF = {}; for (const [z, codes] of Object.entries(JSON.parse(fs.readFileSync(path.join(root, 'pipeline/land/zone_to_nrm2011.json'))).zones)) for (const c of codes) ZONE_OF[c] = +z;
const piece = new Map();
for (const r of csv('data/nrm2011/land_use_by_sa2_nrm2011_piece.csv')) { const n = +r.nrmr_code_2011; if (!(n in ZONE_OF)) continue; const key = r.zone_name + '|' + ZONE_OF[n], p = piece.get(key) ?? { sa2: r.zone_name, zone: ZONE_OF[n], total: 0, cropland: 0 }; p.total += +r.km2; if (isCrop(classes[r.class_code] ?? '')) p.cropland += +r.km2; piece.set(key, p); }
const share = {}; { const bySa2 = {}; for (const p of piece.values()) (bySa2[p.sa2] ??= []).push(p);
  for (const [s, ps] of Object.entries(bySa2)) { const key = ps.some(p => p.cropland > 0) ? 'cropland' : 'total', tot = ps.reduce((a, p) => a + p[key], 0); share[s] = {}; for (const p of ps) share[s][p.zone] = (share[s][p.zone] ?? 0) + p[key] / tot; } }
const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };
const wmean = (vecs, ws) => { const n = vecs[0].length, out = new Array(n).fill(0); for (let i = 0; i < n; i++) { let w = 0, v = 0; vecs.forEach((x, j) => { if (x[i] > 0) { w += ws[j]; v += ws[j] * x[i]; } }); out[i] = w > 0 ? v / w : 0; } return out; };
const rows = [['release', 'vintage', 'preset', 'level', 'land_basis', 'units', 'sum_capacity', 'population', 'share_of_national', 'units_over_capacity', 'yield_basis']];
for (const id of CELLS) {
  const vintage = id.startsWith('2011') ? '2011' : '2025', year = vintage;
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), R = regions[1];
  const zones = Object.values(regions);
  const unitOf = (z, preset) => ({ ...Object.fromEntries(KEYS.map(k => [k, z.land[k]])), pop: z.population, yield: z.yield, irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2 });
  const cap = (u, preset) => { const o = ev.evaluate({ ...R, yield: u.yield }, { ...R.presets[preset], irrigation: u.irrigation, nature2: u.nature2, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: Math.max(u.pop, 1) }).capacity; return Number.isFinite(o) ? o : 0; };
  // SA2 units for this release: each takes the yields and settings of its dominant zone
  const dom = sh => Object.entries(sh).filter(([z]) => regions[z]).sort((x, y) => y[1] - x[1])[0]?.[0] ?? '1';
  const sa = meth.map(r => { const sh = share[r.sa2_code] ?? { 1: 1 };
    return { sa2: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2, pop: +erp[r.sa2_code]?.[year] || 0, sh, zone: dom(sh) }; });
  const withZone = (u, z, preset) => ({ ...u, yield: regions[z].yield, irrigation: regions[z].presets[preset].irrigation, nature2: regions[z].presets[preset].nature2 });
  const group = (key, preset) => { const m = new Map(); for (const u of sa) { const g = key ? u[key] : 'all'; (m.get(g) ?? m.set(g, []).get(g)).push(u); }
    return [...m.values()].map(us => { const a = Object.fromEntries(KEYS.concat('pop').map(k => [k, us.reduce((x, u) => x + u[k], 0)])), zs = {};
      for (const u of us) for (const [z, v] of Object.entries(u.sh)) zs[z] = (zs[z] ?? 0) + v * (u.cropping > 0 ? u.cropping : 1e-6 * (u.cropping + u.pasture + u.nonAg + u.nature1 + 1e-9));
      return withZone(a, key ? dom(zs) : '1', preset); }); };
  const stateOf = u => String(STATE_ZONE[+hier[u.sa2]?.state] ?? 1);
  for (const preset of PRESETS) for (const basis of ['local', 'state']) {
    const zoneUnits = (zs) => zs.map(z => basis === 'local' ? unitOf(z, preset) : { ...unitOf(z, preset), yield: regions[z.parent ?? z.id].yield, irrigation: regions[z.parent ?? z.id].presets[preset].irrigation, nature2: regions[z.parent ?? z.id].presets[preset].nature2 });
    const saZone = (us, key) => basis === 'state' ? stateOf(us[0]) : null;
    const saUnits = (key) => { if (key === 'sa2') return sa.map(u => withZone(u, basis === 'state' ? stateOf(u) : u.zone, preset)); const m = new Map(); for (const u of sa) { const g = u[key]; (m.get(g) ?? m.set(g, []).get(g)).push(u); }
      return [...m.values()].map(us => { const a = Object.fromEntries(KEYS.concat('pop').map(k => [k, us.reduce((x, u) => x + u[k], 0)])), zs = {};
        for (const u of us) for (const [z, v] of Object.entries(u.sh)) zs[z] = (zs[z] ?? 0) + v * (u.cropping > 0 ? u.cropping : 1e-6 * (u.cropping + u.pasture + u.nonAg + u.nature1 + 1e-9));
        return withZone(a, basis === 'state' ? stateOf(us[0]) : dom(zs), preset); }); };
    const natUnit = (() => { const a = Object.fromEntries(KEYS.concat('pop').map(k => [k, sa.reduce((x, u) => x + u[k], 0)])); return withZone(a, '1', preset); })();
    const sets = [['Australia', 'release', [unitOf(R, preset)]], ['State', 'release', zones.filter(z => z.kind === 'state').map(z => unitOf(z, preset))], ['NRM region', 'release', zoneUnits(zones.filter(z => z.kind === 'region' || z.id === 60))],
      ['Australia (SA land)', '2020-21 land', [natUnit]], ['SA4', '2020-21 land', saUnits('sa4')], ['SA3', '2020-21 land', saUnits('sa3')], ['SA2', '2020-21 land', saUnits('sa2')]];
    const nat = {};
    for (const [level, basisLand, units] of sets) {
      const caps = units.map(u => cap(u, preset)), total = caps.reduce((a, b) => a + b, 0), popTotal = units.reduce((a, u) => a + u.pop, 0);
      if (level === 'Australia' || level === 'Australia (SA land)') nat[basisLand] = total;
      rows.push([id, vintage, preset, level, basisLand, units.length, Math.round(total), Math.round(popTotal), (total / nat[basisLand]).toFixed(3), units.filter((u, i) => u.pop > caps[i]).length, basis]);
    }
  }
  console.log(id, 'done');
}
fs.writeFileSync(path.join(root, 'results', 'scale_curve.csv'), rows.map(r => r.join(',')).join('\n') + '\n');
console.log(rows.filter(r => r[0] === '2025-fixed').filter(r => r[2] === 'short').map(r => r.join(' | ')).join('\n'));
