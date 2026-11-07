// E8: Monte Carlo ranges for the 2025-organic result (env MC_RELEASE=<id> to draw on another release of the 2025 chain, for example 2025-mirror or 2025-improved).
//   node monte_carlo.mjs WORK_DIR OUT.csv [N]            random draws (Latin hypercube, seed 20261027); WORK_DIR is the folder of build_variants.py
//     WORK_DIR must be built on the current data/2025 matrices: the script stops if the group-factor matrices are not centred on the base matrix (defect X054)
//   node monte_carlo.mjs WORK_DIR OUT.csv fixed '{"sf":1,"meat":1}'     one evaluation at fixed parameter values (to check the additive shortcut)
// Needs the built data: cd web && node scripts/build-data.mjs
//
// Uncertain choices and the ranges drawn (the ranges are the defensible ones of README.md, not confidence intervals):
//   sf      field-crop group factor            uniform, -1 to +1 = 14% below to 14% above the factor (the measured error of the rule)
//   sh      vegetable, fruit and nut factors   uniform, -1 to +1 = 20% below to 20% above
//   meat    window of herd and meat data       one of: 2020-21 to 2024-25 (base), 2020-21 to 2022-23, 2022-23 to 2024-25, equal chances
//   meategg meat and egg share of the diet     triangular 0.115, 0.12 (proxy), 0.13 (2011)
//   redmeat red meat share                     triangular 0.528, 0.578 (proxy), 0.64 (2011)
//   fuel, biofuel, timber                      uniform between the proxy value and the 2011 value
//   orgfac  default organic factor             uniform 0.771 to 0.845 (Ponisio et al. 2015 range)
//   orgshare organic share of land (default and baseline together)   triangular 0.02, 0.07, 0.12
// The group factors and the meat window act on the yield matrix as differences from the base matrix, taken from the matrices that build_variants.py
// wrote (a linear shortcut: yields are linear in a group factor; combining a factor with a meat window is checked in README.md).
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [work, outFile, arg3, arg4] = process.argv.slice(2);
const dataDir = new URL('../../web/public/data/', import.meta.url).pathname, root = new URL('../../', import.meta.url).pathname;
const REL = process.env.MC_RELEASE ?? '2025-organic';                      // the release the draws are made on (2025-organic by default; 2025-mirror and 2025-improved are the tip cells)
const model = JSON.parse(fs.readFileSync(dataDir + REL + '/model.json')), data = JSON.parse(fs.readFileSync(dataDir + REL + '/regions.json'));
const ZONES = process.env.MC_ZONES === 'all' ? Object.keys(data.regions).map(Number).sort((a, b) => a - b) : [1, 2, 15, 26, 40, 49, 56, 60];     // MC_ZONES=all: every zone (120 evaluations a run)
const LONG = process.env.MC_LONG === '1';                                  // MC_LONG=1 adds three long-term choices: the resilience table, the long-term fuel and the feeding benchmark
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return { row: +m[2] - 1, col: c - 1 }; };

function readMatrix(file) {
  const lines = fs.readFileSync(file, 'utf8').trim().split(/\r?\n/), head = lines[0].split(',').slice(1).map(Number), out = {};
  for (const l of lines.slice(1)) { const c = l.split(','); out[+c[0]] = head.map((row, i) => [data.yieldRows.indexOf(row), +c[i + 1]]); }
  return out;
}
const baseY = {};                                                           // zone -> yield vector of the release
for (const z of ZONES) baseY[z] = data.regions[z].yield.slice();
import { resolveRelease, methodModule } from '../../web/scripts/releases.mjs';
const FACTORS = (resolveRelease(REL).methods ?? []).flatMap(id => methodModule(id).yieldFactors ?? []);      // regional yield factors of the release's method modules (the matrices below hold the unscaled yields)
const asVec = m => { const v = {}; for (const z of ZONES) { v[z] = baseY[z].slice(); for (const [i, x] of m[z]) v[z][i] = x; for (const f of FACTORS) v[z][data.yieldRows.indexOf(f.row)] *= f.zones[z] ?? 1; } return v; };
const baseMat = asVec(readMatrix(root + 'data/2025/yield_matrix_livestock.csv'));
// Locked rows (2026-11-04): rows whose yield the release sets by a module other than a yield factor (the dairy-good-land module sets the dairy milk row from observed farm yields, row 97) are not the matrix value.
// The matrix would overwrite them and the 2025-improved base would fall from 53.6 to 21.2 million. A locked row keeps the release value and takes no group-factor or meat-window difference.
const LOCK = {}; for (const z of ZONES) { LOCK[z] = new Set(); baseMat[z].forEach((x, i) => { if (Math.abs((baseY[z][i] ?? 0) - (x ?? 0)) > 1e-6 * Math.max(1, Math.abs(x ?? 0))) LOCK[z].add(i); }); }
const lockedRows = new Set(); for (const z of ZONES) for (const i of LOCK[z]) lockedRows.add(data.yieldRows[i]); if (lockedRows.size) console.error('locked yield rows (kept at the release value):', [...lockedRows].join(' '));
// The matrix rows that no yield factor or module changes were checked equal to the release above; a locked row is one the release changes after the matrix.
for (const z of ZONES) for (const i of LOCK[z]) baseMat[z][i] = baseY[z][i];
const diff = (id, dir = work) => { const m = asVec(readMatrix(`${dir}/${id}/yield_matrix_livestock.csv`)), d = {}; for (const z of ZONES) d[z] = m[z].map((x, i) => LOCK[z].has(i) ? 0 : (x ?? 0) - (baseMat[z][i] ?? 0)); return d; };
const D = { fieldLo: diff('gt_field_lo'), fieldHi: diff('gt_field_hi'), hortLo: diff('gt_hort_lo'), hortHi: diff('gt_hort_hi'), meat: [null, diff('meat_early'), diff('meat_3y')] };
// Check of the work folder (defect X054): the yields are linear in a group factor and lo and hi are 14% (20%) either side of it, so the mean of the lo and hi matrices must equal the base matrix.
// A work folder built before a change to the base (in X054, livestock_zone.py of 2026-10-29: wool, dairy milk and cattle meat rows) fails this, and its offset would be added at both ends of the factor.
// The meat windows of the same folder come from the same livestock_zone.py, so a folder that passes for the group factors has meat windows on the current base too. Rebuild a failing folder with build_variants.py.
{ const bad = [];
  for (const [name, lo, hi] of [['field crops', D.fieldLo, D.fieldHi], ['vegetables, fruit and nuts', D.hortLo, D.hortHi]])
    for (const z of ZONES) lo[z].forEach((a, i) => { const off = (a + hi[z][i]) / 2, b = baseMat[z][i] ?? 0; if (Math.abs(off) > 1e-5 + 1e-6 * Math.abs(b)) bad.push(`${name}: zone ${z} row ${data.yieldRows[i]} offset ${(100 * off / (b || 1)).toFixed(2)}%`); });
  if (bad.length) { console.error(`work folder ${work} was not built on the current base matrix (${bad.length} offsets, for example ${bad.slice(0, 3).join('; ')}); rebuild it with build_variants.py`); process.exit(1); } }
// MC_WIN_DIR=<folder with meat_8y, meat_10y, meat_15y, meat_20y, made as in README.md> draws the meat window from the base window and those four full-cycle windows instead
// (herds and meat of 2017-18 to 2024-25, 2015-16 to 2024-25, 2010-11 to 2024-25 and 2005-06 to 2024-25), five equal chances.
// Check of the MC_WIN_DIR folder (defect X069, the X054 offset in the full-cycle windows): a window changes only the animal rows that depend on the years of herd and meat data
// (rows 95 to 103: sheep meat, wool, dairy milk, cattle meat, chicken, duck, turkey, eggs, pig meat); every other row must equal the base matrix. The folder must also hold
// base_window, the base years (2020-21 to 2024-25) built in the same run, and it must equal the base matrix in every row: a folder built on another base (in X069, livestock_zone.py
// with the placeholders for wool, feedlot grain and milk) fails this, and its offset would be added to every drawn window. Rebuild a failing folder as README.md describes.
if (process.env.MC_WIN_DIR) {
  const W = process.env.MC_WIN_DIR, WINROWS = new Set(['95', '96', '97', '98', '99', '100', '101', '102', '103']);
  const raw = f => { const l = fs.readFileSync(f, 'utf8').trim().split(/\r?\n/), out = {}; for (const x of l.slice(1)) { const c = x.split(','); out[c[0]] = c.slice(1).map(Number); } return { head: l[0].split(',').slice(1), rows: out }; };
  const B0 = raw(root + 'data/2025/yield_matrix_livestock.csv'), bad = {};
  const check = (id, allowed) => {
    const f = `${W}/${id}/yield_matrix_livestock.csv`; if (!fs.existsSync(f)) { bad[`${id}: no matrix (${f})`] = null; return; }
    const m = raw(f); if (m.head.join() !== B0.head.join()) { bad[`${id}: rows differ from the base matrix's`] = null; return; }
    for (const z of Object.keys(B0.rows)) B0.rows[z].forEach((b, i) => { const r = B0.head[i], x = m.rows[z]?.[i];
      if (allowed.has(r) || (x !== undefined && Math.abs(x - b) <= 1e-6 * Math.max(1, Math.abs(b)))) return;
      const k = `${id} row ${r}`, e = bad[k] ?? (bad[k] = { n: 0, max: 0 }); e.n++; e.max = Math.max(e.max, x === undefined ? Infinity : Math.abs(x - b) / (Math.abs(b) || 1)); });
  };
  check('base_window', new Set()); for (const id of ['meat_8y', 'meat_10y', 'meat_15y', 'meat_20y']) check(id, WINROWS);
  const keys = Object.keys(bad);
  if (keys.length) { console.error(`MC_WIN_DIR ${W} was not built on the current base matrix (${keys.length} faults: ${keys.map(k => bad[k] ? `${k} differs in ${bad[k].n} zones, up to ${(100 * bad[k].max).toFixed(1)}%` : k).join('; ')}); rebuild it as README.md describes`); process.exit(1); }
  console.error(`MC_WIN_DIR ${W}: base_window equals the base matrix and the four windows differ from it only in rows 95 to 103`);
}
if (process.env.MC_WIN_DIR) D.meat = [null, ...['meat_8y', 'meat_10y', 'meat_15y', 'meat_20y'].map(id => diff(id, process.env.MC_WIN_DIR))];
const NMEAT = process.env.MC_WIN_DIR ? 5 : 3;
const orgRowsAll = Object.keys(JSON.parse(fs.readFileSync(`${work}/variants.json`)).find(v => v.id === 'org_def_lo').modelCells);
// 2026-11-04: only the cells still at the workbook default are drawn. A release can set some of them itself (the organic-ruminant-factor module sets sheep meat, sheep wool and cattle meat to 0.9);
// the draws would overwrite that with 0.808 and the 2025-improved long term would fall from 18.5 to 16.9 million at the base.
let orgRows = orgRowsAll;

const ev = new Evaluator(model);
const setCell = (a, v) => { const { row, col } = decode(a); ev.hf.setCellContents({ sheet: ev.yid, row, col }, [[v]]); };
// long-term choices (MC_LONG=1): the resilience table (this release's, or the leave-one-out table of 2025-resilience-loo), the long-term liquid fuel (litres a person: 156 with light vehicles electrified,
// 210 re-derived, 253 the thesis) and the feeding benchmark of the recycling-stage module (0.30 to 0.525 of each stage that may be fed: South Korea 42.5%, Japan 35.9%, Japan without households 52.5%, lower for Australia)
// The law (current or adapted), the grain store and the time frame are scenario switches, not uncertain inputs, and are not drawn.
const looCells = JSON.parse(fs.readFileSync(dataDir + '2025-resilience-loo/model.json')).sheets.resilience.cells, tabCells = model.sheets.resilience.cells;
const tabDiff = Object.keys(looCells).filter(k => looCells[k] !== tabCells[k]).map(k => { const [r, c] = k.split(':').map(Number); return { row: r, col: c, base: tabCells[k], loo: looCells[k] }; });
const resid = ev0 => ev0.hf.getSheetId('resilience');
const BENCH = ['BQ4', 'BQ5', 'BQ6', 'BQ7'], hasBench = BENCH.every(a => { const { row, col } = decode(a); return model.sheets.Settings.cells[`${row}:${col}`] !== undefined; });
let tableState = 0;
const BASEF = (() => { const { row, col } = decode(orgRows[0]); return model.sheets.Yield.cells[`${row}:${col}`]; })();       // the default organic factor of the workbook (0.8083)
const cellVal = a => { const { row, col } = decode(a); return model.sheets.Yield.cells[`${row}:${col}`]; };
orgRows = orgRowsAll.filter(a => Math.abs(cellVal(a) - BASEF) < 1e-9);
if (orgRows.length !== orgRowsAll.length) console.error('organic cells set by the release and left alone:', orgRowsAll.filter(a => !orgRows.includes(a)).join(' '));

function evaluate(p) {
  if (LONG) {
    if ((p.restable ?? 0) !== tableState) { ev.hf.batch(() => { for (const d of tabDiff) ev.hf.setCellContents({ sheet: resid(ev), row: d.row, col: d.col }, [[p.restable ? d.loo : d.base]]); }); tableState = p.restable ?? 0; }
    if (hasBench) for (const a of BENCH) { const { row, col } = decode(a); ev.hf.setCellContents({ sheet: ev.sid, row, col }, [[p.lbench]]); }
  }
  for (const a of orgRows) setCell(a, p.orgfac);
  setCell('E2', `=Settings!B15-${p.orgshare}`);
  const row = {};
  for (const z of ZONES) {
    const y = baseMat[z].slice(), add = (d, s, lo, hi) => { const w = s >= 0 ? hi[z] : lo[z]; for (let i = 0; i < y.length; i++) if (w[i]) y[i] += Math.abs(s) * w[i]; };
    add(null, p.sf, D.fieldLo, D.fieldHi); add(null, p.sh, D.hortLo, D.hortHi);
    if (p.meat) for (let i = 0; i < y.length; i++) if (D.meat[p.meat][z][i]) y[i] += D.meat[p.meat][z][i];
    const region = { ...data.regions[z], yield: y };
    for (const k of ['short', 'long']) {
      const pre = { ...data.regions[z].presets[k] }; if (k === 'long' && LONG) pre.fuel = p.lfuel; if (k === 'short') Object.assign(pre, { meategg: p.meategg, redmeat: p.redmeat, fuel: p.fuel, biofuel: p.biofuel, timber: p.timber, organic: p.orgshare });
      row[`${z}_${k}`] = Math.round(ev.evaluate(region, { ...region.land, ...pre, population: region.population }).capacity);
    }
  }
  return row;
}
const LFUEL = data.regions[1].presets.long.fuel, LBENCH = hasBench ? model.sheets.Settings.cells[(() => { const { row, col } = decode('BQ4'); return `${row}:${col}`; })()] : 0.4;
const BASEP = { sf: 0, sh: 0, meat: 0, meategg: 0.12, redmeat: 0.578, fuel: 2360, biofuel: 0.0023, timber: 0.8, orgfac: BASEF, orgshare: 0.07, restable: 0, lfuel: LFUEL, lbench: LBENCH };

if (arg3 === 'fixed') {
  const r = evaluate({ ...BASEP, ...JSON.parse(arg4 ?? '{}') });
  fs.writeFileSync(outFile, Object.keys(r).join(',') + '\n' + Object.values(r).join(',') + '\n'); console.log(r['1_short'], r['1_long']); process.exit(0);
}

if (arg3 === 'oat') {                    // one choice at a time over its range (the other nine at their base values): the responses for the quick range of rss_check.py
  const PTS = { sf: [-1, 0, 1], sh: [-1, 0, 1], meat: Array.from({ length: NMEAT }, (_, i) => i), meategg: [0.115, 0.12, 0.13], redmeat: [0.528, 0.578, 0.64], fuel: [2360, 2520], biofuel: [0.0023, 0.005],
                timber: [0.8, 1.0], orgfac: [0.771, BASEF, 0.845], orgshare: [0.02, 0.07, 0.12] };
  if (LONG) { PTS.restable = [0, 1]; PTS.lfuel = [156, LFUEL, 253]; if (hasBench) PTS.lbench = [0.30, LBENCH, 0.525]; }
  const lines = []; let head;
  const base = evaluate({ ...BASEP }); head = ['input', 'value', ...Object.keys(base)]; lines.push(['base', '', ...Object.values(base)].join(','));
  for (const [k, vals] of Object.entries(PTS)) for (const v of vals) lines.push([k, v, ...Object.values(evaluate({ ...BASEP, [k]: v }))].join(','));
  fs.writeFileSync(outFile, head.join(',') + '\n' + lines.join('\n') + '\n'); console.log('wrote', lines.length, 'runs'); process.exit(0);
}

// ---- Latin hypercube -------------------------------------------------------------------------------------------------------------------------
const N = +(arg3 ?? 1000);
let seed = 20261027; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const NAMES = ['sf', 'sh', 'meat', 'meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'orgfac', 'orgshare', ...(LONG ? ['restable', 'lfuel', 'lbench'] : [])];
const lhs = NAMES.map(() => { const idx = Array.from({ length: N }, (_, i) => i); for (let i = N - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } return idx.map(i => (i + rnd()) / N); });
const tri = (u, a, c, b) => { const f = (c - a) / (b - a); return u < f ? a + Math.sqrt(u * (b - a) * (c - a)) : b - Math.sqrt((1 - u) * (b - a) * (b - c)); };
const lerp = (u, a, b) => a + u * (b - a);
const draw = i => { const u = k => lhs[NAMES.indexOf(k)][i]; return {
  sf: lerp(u('sf'), -1, 1), sh: lerp(u('sh'), -1, 1), meat: Math.min(NMEAT - 1, Math.floor(u('meat') * NMEAT)),
  meategg: tri(u('meategg'), 0.115, 0.12, 0.13), redmeat: tri(u('redmeat'), 0.528, 0.578, 0.64),
  fuel: lerp(u('fuel'), 2360, 2520), biofuel: lerp(u('biofuel'), 0.0023, 0.005), timber: lerp(u('timber'), 0.8, 1.0),
  orgfac: lerp(u('orgfac'), 0.771, 0.845), orgshare: tri(u('orgshare'), 0.02, 0.07, 0.12),
  ...(LONG ? { restable: u('restable') < 0.5 ? 0 : 1, lfuel: tri(u('lfuel'), 156, LFUEL, 253), lbench: hasBench ? tri(u('lbench'), 0.30, LBENCH, 0.525) : LBENCH } : {}) }; };
const out = []; let header;
for (let i = 0; i < N; i++) {
  const p = draw(i), r = evaluate(p); if (!header) header = [...NAMES, ...Object.keys(r)];
  out.push([...NAMES.map(k => +p[k].toFixed(5)), ...Object.values(r)].join(','));
  if ((i + 1) % 100 === 0) console.error(`${i + 1}/${N}`);
}
fs.writeFileSync(outFile, header.join(',') + '\n' + out.join('\n') + '\n'); console.log('wrote', N, 'draws');
