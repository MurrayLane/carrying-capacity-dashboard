// Contiguous regionalisation of Australia that maximises the sum of regional capacities (national yield vector, so land mix alone decides).
//   cd web && node ../analysis/regionalise_2025/regionalise.mjs RELEASE PRESET K [AREA_MAX_KM2] [AREA_MIN_FRACTION]     (needs built data and data/sa2/adjacency.csv)
// Method: start from the 2,450 SA2s; (1) while a region has less land than AREA_MIN (default a tenth of the mean land of K regions) merge it with the neighbour that gives the largest capacity gain that keeps it under AREA_MAX;
// (2) merge the adjacent pair with the largest gain until K regions remain; (3) improve by moving boundary SA2s to a neighbouring region while the sum of capacities rises. Constraints: contiguity, a region's land at
// most AREA_MAX (default 650,000 km2, about the largest NRM zone, but never below the largest single SA2) and at least AREA_MIN. A population floor was tried and dropped: in the outback it forces regions beyond any area cap. Writes data/regions/ideal_<release>_<preset>_K<K>.csv (sa2_code, region).
import fs from 'node:fs'; import path from 'node:path';
import { root } from '../../web/scripts/releases.mjs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir } from '../../web/scripts/results-lib.mjs';
const [rel, preset, Karg, amaxArg, aminArg] = process.argv.slice(2); const K = +Karg;
const csv = f => { const [h, ...rows] = fs.readFileSync(path.join(root, f), 'utf8').trim().split('\n').map(l => l.replace(/\r$/, '').split(',')); return rows.map(r => Object.fromEntries(h.map((k, i) => [k, r[i]]))); };
const KEYS = ['cropping', 'pasture', 'nonAg', 'infrastr1', 'nature1'];
const model = JSON.parse(fs.readFileSync(path.join(dataDir(rel), 'model.json'))), regionsJ = JSON.parse(fs.readFileSync(path.join(dataDir(rel), 'regions.json'))).regions, ev = new Evaluator(model), N = regionsJ[1];
const cache = new Map(); const cap = v => { const key = KEYS.map(k => Math.round(v[k] * 10)).join(','); let c = cache.get(key); if (c === undefined) { const o = ev.evaluate(N, { ...N.presets[preset], ...Object.fromEntries(KEYS.map(k => [k, v[k]])), population: 1 }).capacity; c = Number.isFinite(o) ? o : 0; cache.set(key, c); } return c; };
const meth = csv('data/sa2/land_2011_method_by_sa2.csv'), pops = Object.fromEntries(csv('data/sa2/population_erp.csv').map(r => [r.sa2_code, +r['2025'] || 0]));
const sa = meth.map(r => ({ code: r.sa2_code, name: r.sa2_name, v: { cropping: +r.cropping_km2, pasture: +r.pasture_km2, nonAg: +r.nonAgricultural_km2, infrastr1: +r.infrastructure_km2, nature1: +r.reserve_km2 }, pop: pops[r.sa2_code] ?? 0 }));
const idx = Object.fromEntries(sa.map((u, i) => [u.code, i])); const nbr = sa.map(() => new Set());
for (const r of csv('data/sa2/adjacency.csv')) { const a = idx[r.sa2_a], b = idx[r.sa2_b]; if (a !== undefined && b !== undefined && a !== b) { nbr[a].add(b); nbr[b].add(a); } }
const area = v => KEYS.reduce((a, k) => a + v[k], 0), add = (a, b) => Object.fromEntries(KEYS.map(k => [k, a[k] + b[k]]));
const AMAX = Math.max(+(amaxArg ?? 650000), ...sa.map(u => KEYS.reduce((a, k) => a + u.v[k], 0)));
const natV = sa.reduce((a, u) => add(a, u.v), Object.fromEntries(KEYS.map(k => [k, 0]))), natCap = cap(natV), totalPop = sa.reduce((a, u) => a + u.pop, 0), AMIN = (aminArg ? +aminArg : 0.1) * KEYS.reduce((a, k) => a + natV[k], 0) / K, POPMIN = 0;
// regions
let regs = new Map(sa.map((u, i) => [i, { id: i, members: new Set([i]), v: { ...u.v }, pop: u.pop, nbrs: new Set(nbr[i]), cap: cap(u.v), ver: 0 }]));
const gain = (a, b) => cap(add(a.v, b.v)) - a.cap - b.cap, feasible = (a, b) => area(a.v) + area(b.v) <= AMAX;
function merge(a, b) { for (const m of b.members) a.members.add(m); a.v = add(a.v, b.v); a.pop += b.pop; a.cap = cap(a.v); for (const n of b.nbrs) { if (n === a.id) continue; const r = regs.get(n); r.nbrs.delete(b.id); r.nbrs.add(a.id); a.nbrs.add(n); } a.nbrs.delete(b.id); a.nbrs.delete(a.id); regs.delete(b.id); a.ver++; }
// phase 1: land floor (merge small regions into the neighbour that gives the largest gain under the area cap)
let guard = 0;
while (guard++ < 100000) { const small = [...regs.values()].filter(r => area(r.v) < AMIN && r.nbrs.size); if (!small.length || regs.size <= K) break; let best = null;
  for (const r of small) for (const n of r.nbrs) { const o = regs.get(n); if (!feasible(r, o)) continue; const g = gain(r, o); if (!best || g > best.g) best = { g, a: r, b: o }; }
  if (!best) break; const keep = area(best.a.v) >= area(best.b.v) ? best.a : best.b; merge(keep, keep === best.a ? best.b : best.a); }
const n1 = regs.size; console.log(`${rel} ${preset} K=${K}: land cap ${Math.round(AMAX).toLocaleString()} km2, floor ${Math.round(AMIN).toLocaleString()} km2; after the land floor ${n1} regions`);
// phase 2: merge by largest gain with a lazy heap
const heap = []; const push = e => { heap.push(e); let i = heap.length - 1; while (i) { const p = (i - 1) >> 1; if (heap[p].g >= heap[i].g) break; [heap[p], heap[i]] = [heap[i], heap[p]]; i = p; } };
const pop = () => { const t = heap[0], l = heap.pop(); if (heap.length) { heap[0] = l; let i = 0; for (;;) { let m = i; const a = 2 * i + 1, b = a + 1; if (a < heap.length && heap[a].g > heap[m].g) m = a; if (b < heap.length && heap[b].g > heap[m].g) m = b; if (m === i) break; [heap[m], heap[i]] = [heap[i], heap[m]]; i = m; } } return t; };
const pushEdges = a => { for (const n of a.nbrs) { const b = regs.get(n); if (b && feasible(a, b)) push({ g: gain(a, b), a: a.id, b: n, va: a.ver, vb: b.ver }); } };
for (const a of regs.values()) for (const n of a.nbrs) if (a.id < n) { const b = regs.get(n); if (feasible(a, b)) push({ g: gain(a, b), a: a.id, b: n, va: a.ver, vb: b.ver }); }
while (regs.size > K && heap.length) { const e = pop(), a = regs.get(e.a), b = regs.get(e.b); if (!a || !b || a.ver !== e.va || b.ver !== e.vb) continue; merge(a, b); pushEdges(a); }
console.log(`after merging: ${regs.size} regions, sum of capacities ${(([...regs.values()].reduce((s, r) => s + r.cap, 0)) / natCap * 100).toFixed(1)}% of national`);
// phase 3: boundary moves
const regionOf = new Array(sa.length); const reindex = () => { for (const r of regs.values()) for (const m of r.members) regionOf[m] = r.id; }; reindex();
const connectedWithout = (r, m) => { const left = [...r.members].filter(x => x !== m); if (left.length <= 1) return left.length === 1 || false; const set = new Set(left), seen = new Set([left[0]]), st = [left[0]]; while (st.length) { const x = st.pop(); for (const y of nbr[x]) if (set.has(y) && !seen.has(y)) { seen.add(y); st.push(y); } } return seen.size === set.size; };
const sub = (a, b) => Object.fromEntries(KEYS.map(k => [k, a[k] - b[k]]));
for (let pass = 1; pass <= 20; pass++) { let moved = 0;
  for (let m = 0; m < sa.length; m++) { const from = regs.get(regionOf[m]); if (from.members.size < 2) continue; const cands = new Set([...nbr[m]].map(x => regionOf[x]).filter(x => x !== from.id)); if (!cands.size) continue;
    let best = null; for (const t of cands) { const to = regs.get(t); const newFrom = sub(from.v, sa[m].v), newTo = add(to.v, sa[m].v); if (area(newTo) > AMAX || from.pop - sa[m].pop < POPMIN) continue; const d = cap(newFrom) + cap(newTo) - from.cap - to.cap; if (d > 1 && (!best || d > best.d)) best = { d, to, newFrom, newTo }; }
    if (best && connectedWithout(from, m)) { from.members.delete(m); from.v = best.newFrom; from.pop -= sa[m].pop; from.cap = cap(from.v); best.to.members.add(m); best.to.v = best.newTo; best.to.pop += sa[m].pop; best.to.cap = cap(best.to.v); regionOf[m] = best.to.id; moved++; } }
  for (const r of regs.values()) { r.nbrs = new Set(); for (const m of r.members) for (const y of nbr[m]) if (regionOf[y] !== r.id) r.nbrs.add(regionOf[y]); }
  const tot = [...regs.values()].reduce((s, r) => s + r.cap, 0); console.log(`move pass ${pass}: ${moved} SA2s moved, sum ${(tot / natCap * 100).toFixed(1)}%`); if (!moved) break; }
const list = [...regs.values()].sort((a, b) => b.pop - a.pop), total = list.reduce((s, r) => s + r.cap, 0);
console.log(`\nFINAL ${list.length} regions: sum of capacities ${(total / natCap * 100).toFixed(1)}% of the national capacity (NRM zones 33%, SA4 54% on this basis)`);
console.log('population (thousand) range', Math.round(Math.min(...list.map(r => r.pop)) / 1e3), 'to', Math.round(Math.max(...list.map(r => r.pop)) / 1e3), '| land km2 range', Math.round(Math.min(...list.map(r => area(r.v)))), 'to', Math.round(Math.max(...list.map(r => area(r.v)))));
console.log('largest-capacity regions: ' + [...list].sort((a, b) => b.cap - a.cap).slice(0, 6).map(r => `${(r.cap / 1e3).toFixed(0)}k (pop ${(r.pop / 1e3).toFixed(0)}k, ${Math.round(r.v.cropping)} cropping, ${Math.round(r.v.pasture)} pasture km2)`).join('; '));
fs.mkdirSync(path.join(root, 'data/regions'), { recursive: true });
fs.writeFileSync(path.join(root, `data/regions/ideal_${rel}_${preset}_K${K}_cap${Math.round(AMAX / 1000)}k.csv`), 'sa2_code,region\n' + sa.map((u, i) => `${u.code},${regionOf[i]}`).join('\n') + '\n');
// summary line for analysis/regionalise_2025/summary.csv
const sm = path.join(root, 'analysis/regionalise_2025/summary.csv'); if (!fs.existsSync(sm)) fs.writeFileSync(sm, 'release,preset,K,area_max_km2,area_min_km2,sum_capacity_share_of_national,regions,regions_under_floor,pop_min,pop_max,area_min_region,area_max_region\n');
fs.appendFileSync(sm, [rel, preset, K, Math.round(AMAX), Math.round(AMIN), (total / natCap).toFixed(3), list.length, list.filter(r => area(r.v) < AMIN).length, Math.round(Math.min(...list.map(r => r.pop))), Math.round(Math.max(...list.map(r => r.pop))), Math.round(Math.min(...list.map(r => area(r.v)))), Math.round(Math.max(...list.map(r => area(r.v))))].join(',') + '\n');
