// Scale as a partition effect (B138 item 4; R05a issue 10; R04a 3.8 and question 9; R04b 4 and question 2). One yield basis throughout: the STATE basis of the paper (every unit takes the yields,
// climate zone and irrigation and nature-reserve settings of one state's zone, as web/scripts/make-scale-curve.mjs does). Short and long term; 2025-fixed and 2011-fixed-3.
//   (a) 200 random groupings of the 53 regions (52 NRM regions and the Northern Territory) into 7 groups (the state count), two ways: (u) every region to a uniformly random group (a re-draw if
//       a group is empty); (s) a random permutation cut into groups of the same sizes as the real states' region counts. A group takes the yields of the state holding most of its cropland (total area where it has none).
//       The share is the sum of the groups' capacities over the national capacity (zone 1, the release's own national zone), as in results/scale_curve.csv. The real 7-state and 53-region partitions are on the same rows.
//       The same groups are also evaluated on the national yield vector as a reference row set (variants ending _national_yield_reference), because on the state basis a group that mixes states takes one
//       state's yields, which can lift the sum above the national capacity (the yield-assignment effect of analysis/scale_curve_2025/README.md); the national vector isolates the land-mix effect.
//   (b) the arable-share relaxation (2025-fixed, SA2 land of the 2011 method, data/sa2/land_2011_method_by_sa2.csv): the rule of the model is that pasture never grows crops. Here the GAEZ arable share of each SA2
//       (data/sa2/arable_share_gaez_by_sa2.csv, temperate crops; the broad any-field-crop set; and half the temperate share) of its pasture is moved to cropping, at the unit's own crop yields: an upper bound on what
//       letting arable grazing land carry crops can do, not a measurement of what farmers do. Levels: Australia, State, SA4, SA3, SA2, each as a share of the UNRELAXED national capacity and of its OWN national capacity.
//   (c) the dairy relaxation held (analysis/pasture_2025/two_pool.csv, B-job of 2026-11-03) is copied in with its source named, not rerun.
// Usage: cd web && node ../analysis/scale_curve_2025/scale_partition.mjs        Writes scale_partition.csv (rows) and scale_partition_summary.csv (distribution of the random groupings) beside this file.
// Deterministic: seeded generator (seed 138). Needs the built data (npm run build:data).
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const HERE = path.dirname(new URL(import.meta.url).pathname);
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'], DRAWS = 200, K = 7;
let seed = 138; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const q = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
const rows = [['release', 'preset', 'section', 'variant', 'draw', 'groups', 'sum_capacity', 'share_of_national_unrelaxed', 'share_of_own_national', 'note']];
const summary = [['release', 'preset', 'grouping', 'draws', 'groups', 'min', 'p5', 'p25', 'median', 'p75', 'p95', 'max', 'mean', 'sd', 'real_state_partition', 'real_state_share_rank_among_draws', 'real_nrm_partition_53_units']];
const pct = (a, p) => { const s = [...a].sort((x, y) => x - y), i = (s.length - 1) * p, lo = Math.floor(i), hi = Math.ceil(i); return s[lo] + (s[hi] - s[lo]) * (i - lo); };

// ---------- (a) random groupings of the 53 regions ----------
for (const id of ['2025-fixed', '2011-fixed-3']) {
  const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), R = regions[1];
  const states = Object.values(regions).filter(z => z.kind === 'state'), units = Object.values(regions).filter(z => z.kind === 'region' || z.id === 60);
  if (states.length !== K || units.length !== 53) throw new Error('expected 7 states and 53 regions');
  const stateOfUnit = z => z.kind === 'region' ? z.parent : z.id;
  const capOf = (land, st, preset) => { const o = ev.evaluate(regions[st], { ...R.presets[preset], irrigation: regions[st].presets[preset].irrigation, nature2: regions[st].presets[preset].nature2, ...land, population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
  const sumLand = us => Object.fromEntries(KEYS.map(k => [k, us.reduce((a, z) => a + z.land[k], 0)]));
  const domState = us => { const w = {}; for (const z of us) { const s = stateOfUnit(z); w[s] = (w[s] ?? 0) + (z.land.cropping > 0 ? z.land.cropping : 1e-6 * KEYS.reduce((a, k) => a + z.land[k], 0)); } return +Object.entries(w).sort((a, b) => b[1] - a[1] || a[0] - b[0])[0][0]; };
  const groupCap = (us, preset) => capOf(sumLand(us), domState(us), preset);
  for (const preset of ['short', 'long']) {
    const nat = ev.evaluate(R, { ...R.presets[preset], ...R.land, population: 1 }).capacity;
    const natYieldCapLand = land => { const o = ev.evaluate(R, { ...R.presets[preset], ...land, population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
    const realStates = states.reduce((a, z) => a + capOf(z.land, z.id, preset), 0) / nat;                       // state basis: the state's own yields
    const realNrm = units.reduce((a, z) => a + capOf(z.land, stateOfUnit(z), preset), 0) / nat;                // NRM regions on their parent state's yields
    rows.push([id, preset, 'real_partition', 'states', '', K, Math.round(realStates * nat), (realStates).toFixed(4), (realStates).toFixed(4), 'the release 7 state zones, state basis']);
    rows.push([id, preset, 'real_partition', 'nrm_regions', '', 53, Math.round(realNrm * nat), (realNrm).toFixed(4), (realNrm).toFixed(4), '52 NRM regions and the Northern Territory, parent state basis']);
    const realStatesNat = states.reduce((a, z) => a + natYieldCapLand(z.land), 0) / nat, realNrmNat = units.reduce((a, z) => a + natYieldCapLand(z.land), 0) / nat;
    rows.push([id, preset, 'real_partition', 'states_national_yield_reference', '', K, Math.round(realStatesNat * nat), realStatesNat.toFixed(4), realStatesNat.toFixed(4), 'the 7 state zones evaluated on the national yield vector (reference basis)']);
    rows.push([id, preset, 'real_partition', 'nrm_regions_national_yield_reference', '', 53, Math.round(realNrmNat * nat), realNrmNat.toFixed(4), realNrmNat.toFixed(4), 'the 53 regions evaluated on the national yield vector (reference basis)']);
    const sizes = states.map(s => units.filter(z => stateOfUnit(z) === s.id).length);
    const natYieldCap = us => { const o = ev.evaluate(R, { ...R.presets[preset], ...sumLand(us), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
    for (const variant of ['uniform', 'size_matched']) {
      const draws = [];
      for (let d = 1; d <= DRAWS; d++) {
        let groups;
        if (variant === 'uniform') { do { groups = Array.from({ length: K }, () => []); for (const z of units) groups[Math.floor(rnd() * K)].push(z); } while (groups.some(g => !g.length)); }
        else { const idx = units.map((_, i) => i); for (let i = idx.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } groups = []; let p = 0; for (const n of sizes) { groups.push(idx.slice(p, p + n).map(i => units[i])); p += n; } }
        draws.push(groups);
      }
      const note = variant === 'uniform' ? 'each region to a uniformly random group of 7' : `random permutation cut into groups of ${sizes.join(',')} regions (the real states' counts)`;
      // main basis: the state basis (a group takes the yields of the state holding most of its cropland); reference basis: the national yield vector, which has no yield-assignment effect (a group's yield cannot beat the nation's)
      for (const [basis, tag, capFn, ref] of [['state', variant, groupCap, 'state basis (main)'], ['national', variant + '_national_yield_reference', natYieldCap, 'national yield vector (reference: removes the yield-assignment effect)']]) {
        const shares = draws.map((g, i) => { const tot = g.reduce((a, us) => a + (basis === 'state' ? capFn(us, preset) : capFn(us)), 0); rows.push([id, preset, 'random_grouping', tag, i + 1, K, Math.round(tot), (tot / nat).toFixed(4), (tot / nat).toFixed(4), `${note}; ${ref}`]); return tot / nat; });
        const mean = shares.reduce((a, b) => a + b, 0) / DRAWS, sd = Math.sqrt(shares.reduce((a, b) => a + (b - mean) ** 2, 0) / (DRAWS - 1)), realS = basis === 'state' ? realStates : realStatesNat, realN = basis === 'state' ? realNrm : realNrmNat, below = shares.filter(x => x < realS).length;
        summary.push([id, preset, tag, DRAWS, K, ...[Math.min(...shares), pct(shares, .05), pct(shares, .25), pct(shares, .5), pct(shares, .75), pct(shares, .95), Math.max(...shares), mean, sd].map(x => x.toFixed(4)), realS.toFixed(4), `${below} of ${DRAWS} draws are below the real states (same basis)`, realN.toFixed(4)]);
      }
    }
    console.log(id, preset, 'national', Math.round(nat), 'real states', realStates.toFixed(3), 'real NRM (state basis)', realNrm.toFixed(3), summary.slice(-4).map(r => r.slice(2, 3).concat(r.slice(5, 13)).join(' ')).join(' | '));
  }
}

// ---------- (b) the arable-share relaxation on SA2 land, 2025-fixed, state basis ----------
{
  const id = '2025-fixed', model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model), R = regions[1];
  const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), hier = Object.fromEntries(csv('data/sa2/land_types_by_sa2.csv').map(r => [r.sa2_code, r]));
  const temperate = Object.fromEntries(csv('data/sa2/arable_share_gaez_by_sa2.csv').map(r => [r.sa2_code, +r.arable_share_gaez])), broad = Object.fromEntries(csv('data/sa2/arable_share_gaez_broad_by_sa2.csv').map(r => [r.sa2_code, +r.arable_share_gaez]));
  const STATE_ZONE = { 1: 2, 2: 15, 3: 26, 4: 40, 5: 49, 6: 56, 7: 60, 8: 2, 9: 1 };       // as analysis/pasture_2025/two_pool_test.mjs: 8 ACT with NSW; 9 Jervis Bay on the national zone
  const sa = meth.map(r => ({ code: r.sa2_code, sa3: hier[r.sa2_code]?.sa3_code, sa4: hier[r.sa2_code]?.sa4_code, state: +hier[r.sa2_code]?.state, cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }));
  const relax = (u, share) => { const s = Math.min(1, Math.max(0, share[u.code] ?? 0)), mv = s * u.pasture; return { ...u, cropping: u.cropping + mv, pasture: u.pasture - mv }; };
  const agg = us => ({ ...Object.fromEntries(KEYS.map(k => [k, us.reduce((a, u) => a + u[k], 0)])), state: us[0].state });
  const groupBy = (list, key) => { const m = new Map(); for (const u of list) { const k = typeof key === 'function' ? key(u) : u[key]; (m.get(k) ?? m.set(k, []).get(k)).push(u); } return [...m.values()].map(agg); };
  for (const preset of ['short', 'long']) {
    const cap = u => { const zid = STATE_ZONE[u.state] ?? 1, z = regions[zid]; const o = ev.evaluate(z, { ...R.presets[preset], irrigation: z.presets[preset].irrigation, nature2: z.presets[preset].nature2, ...Object.fromEntries(KEYS.map(k => [k, u[k]])), population: 1 }).capacity; return Number.isFinite(o) ? o : 0; };
    const variants = [['unrelaxed', null, 0], ['arable_temperate_full', temperate, 1], ['arable_temperate_half', temperate, 0.5], ['arable_broad_full', broad, 1]];
    let natBase = null; const natUnit = sa => ({ ...agg(sa), state: 9 });
    for (const [name, share, f] of variants) {
      const list = share ? sa.map(u => relax(u, Object.fromEntries(Object.entries(share).map(([k, v]) => [k, v * f])))) : sa;
      const levels = [['Australia', [natUnit(list)]], ['State', groupBy(list, u => u.state === 8 ? 1 : u.state)], ['SA4', groupBy(list, 'sa4')], ['SA3', groupBy(list, 'sa3')], ['SA2', list]];
      const caps = levels.map(([n, us]) => [n, us.length, us.reduce((a, u) => a + cap(u), 0)]);
      if (name === 'unrelaxed') natBase = caps[0][2]; const natOwn = caps[0][2];
      for (const [n, units, c] of caps) rows.push([id, preset, 'arable_relaxation', name, '', units, Math.round(c), (c / natBase).toFixed(4), (c / natOwn).toFixed(4), `pasture of each SA2 moved to cropping by ${f} x its GAEZ arable share; state basis; SA2 land of the 2011 method; ${n}`]);
      console.log(preset, name.padEnd(24), caps.map(([n, , c]) => `${n} ${(c / natBase * 100).toFixed(1)}%/${(c / natOwn * 100).toFixed(1)}%`).join('  '));
    }
  }
}

// ---------- (c) the dairy relaxation held, copied with its source ----------
for (const r of csv('analysis/pasture_2025/two_pool.csv')) rows.push(['2025-fixed', 'short', 'dairy_relaxation_held', r.diet, '', r.units, '', (+r.dairy_on_cropland / 100).toFixed(4), '', `copied from analysis/pasture_2025/two_pool.csv: ${r.level}; unchanged model ${r.unchanged_model}% ; dairy on cropland ${r.dairy_on_cropland}% ; dairy yield halved ${r.dairy_on_cropland_yield_halved}% (shares of the unchanged national capacity); own-national share ${(100 * r.dairy_on_cropland / csv('analysis/pasture_2025/two_pool.csv').find(x => x.diet === r.diet && x.level === 'Australia').dairy_on_cropland).toFixed(1)}%`]);
fs.writeFileSync(path.join(HERE, 'scale_partition.csv'), rows.map(r => r.map(q).join(',')).join('\n') + '\n');
fs.writeFileSync(path.join(HERE, 'scale_partition_summary.csv'), summary.map(r => r.map(q).join(',')).join('\n') + '\n');
console.log('wrote scale_partition.csv', rows.length - 1, 'rows and scale_partition_summary.csv');
