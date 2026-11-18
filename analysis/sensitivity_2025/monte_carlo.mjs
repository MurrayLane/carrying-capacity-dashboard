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
//
// Options added by B115 (decision 108). Every one is off unless its environment variable or argument is given, and with none of them the script's
// output is byte for byte what it was before (checked in README.md, section "The widened Monte Carlo"):
//   MC_ZONES=national   Australia only (zone 1); MC_ZONES=all and the default eight zones are unchanged
//   MC_WIDE=1           six more choices, drawn after the existing ones (the first columns of the Latin hypercube are therefore unchanged):
//     waste     avoidable waste, short term                       uniform 0.12 to 0.14 (analysis/waste_2025/README.md: the Australian measurement, FIAL 2021, allows about 12 to 14%)
//     lossaus   retail and consumer loss factors                  uniform 0 to 1: 0 the thesis's US factors (Buzby 2010, Muth 2011), 1 the Australian factors of methods/loss-factors-australia
//                                                                 (FIAL 2021 Table 5, Burnside bin audit 2022); each Base!G and Base!I cell of the module is set to US + lossaus x (Australian - US)
//     land      source of cropping and pasture areas              0 or 1, equal chances: 0 the ABS holdings (the release), 1 the ABARES land-use raster (variant land_raster of build_variants.py)
//     meatcal   calibration of the ABS meat tables                uniform 0 to 1: 0 the ABS tables as published (variant meat_nocal), 1 the archive's 2010 level (cattle x1.086, sheep x1.155, the release);
//                                                                 a zone's sheep and cattle meat yields are proportional to the calibration, so they are scaled by the ratio of meat_nocal to the base (after the meat window)
//     energy    energy requirement per person, short term         uniform 1 to 1.8/1.4: Settings!B9 (food amount) times the sedentary NHMRC diet; PAL 1.4 (sedentary, the release) to 1.8
//                                                                 (moderate activity), NHMRC Nutrient Reference Values, dietary energy, Tables 3 and 4
//     trendwin  window of the field-crop group trend              uniform 0 to 1: 0 the 2022-25 factor (1.356, the release), 1 the 2016-21 factor (1.289) (data/abs-2022-25/group_trend.json, variant gt_field_2016)
//                                                                 The long-term waste (0), food amount and activity (high) are the long-term scenario's own and are not drawn.
//   sobol N [PART NPARTS]  as the third and later arguments: the design of Saltelli (2010) for first-order and total-order indices: two Latin hypercubes A and B of N rows
//                          (A is the hypercube the plain draws give for N), B drawn after it with the same generator, and for each choice the matrix A with that choice's
//                          column from B; N x (k + 2) runs, written as rows block,i,choices,results; PART of NPARTS (0-based) runs draws i with i % NPARTS = PART.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [work, outFile, arg3, arg4, arg5, arg6] = process.argv.slice(2);
const dataDir = new URL('../../web/public/data/', import.meta.url).pathname, root = new URL('../../', import.meta.url).pathname;
const REL = process.env.MC_RELEASE ?? '2025-organic';                      // the release the draws are made on (2025-organic by default; 2025-mirror and 2025-improved are the tip cells)
const model = JSON.parse(fs.readFileSync(dataDir + REL + '/model.json')), data = JSON.parse(fs.readFileSync(dataDir + REL + '/regions.json'));
const ZONES = process.env.MC_ZONES === 'all' ? Object.keys(data.regions).map(Number).sort((a, b) => a - b) : process.env.MC_ZONES === 'national' ? [1] : [1, 2, 15, 26, 40, 49, 56, 60];     // MC_ZONES=all: every zone (120 evaluations a run)
const LONG = process.env.MC_LONG === '1', WIDE = process.env.MC_WIDE === '1';                                  // MC_LONG=1 adds three long-term choices: the resilience table, the long-term fuel and the feeding benchmark
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
// MC_WIDE=1 (B115): the six added choices, with checks that their inputs sit on the release.
const ENMAX = 1.8 / 1.4;                                                    // NHMRC NRV: PAL 1.4 (sedentary) to 1.8 (moderate activity)
let LOSS = [], RASTER = {}, lossState = 0;
// B130: a release that already applies loss-factors-australia (2025-improved) has no US-to-Australian weight to draw: the choice has no meaning there and is left out (18 choices), not set to a base value.
const NOLOSS = WIDE && (resolveRelease(REL).methods ?? []).includes('loss-factors-australia');
if (WIDE) {
  if (NOLOSS) console.error(`MC_WIDE: ${REL} already applies loss-factors-australia; the loss-factor choice (lossaus) is left out and 18 choices are drawn`);
  else LOSS = Object.entries(methodModule('loss-factors-australia').cellOverrides.Base).map(([a, au]) => { const { row, col } = decode(a), us = model.sheets.Base.cells[`${row}:${col}`];
    if (typeof us !== 'number' || typeof au !== 'number') { console.error(`MC_WIDE: Base!${a} is not a number in ${REL} or in the module`); process.exit(1); } return { row, col, us, au }; });
  const lr = JSON.parse(fs.readFileSync(`${work}/variants.json`)).find(v => v.id === 'land_raster'), bad = [];
  for (const z of ZONES) { const a = lr.land[z], b = data.regions[z].land, pz = lr.zonePresets[z];
    if (a.infrastr1 !== b.infrastr1 || a.nature1 !== b.nature1 || Math.abs(a.cropping + a.pasture + a.nonAg - b.cropping - b.pasture - b.nonAg) > 2) bad.push(`zone ${z} land`);
    if (pz.short.nature2 !== data.regions[z].presets.short.nature2 || pz.long.nature2 !== data.regions[z].presets.long.nature2) bad.push(`zone ${z} reserve share`);
    RASTER[z] = { cropping: a.cropping, pasture: a.pasture, nonAg: a.nonAg }; }
  if (bad.length) { console.error(`MC_WIDE: the land_raster variant of ${work} was not built on the land of ${REL}: ${bad.slice(0, 5).join('; ')}`); process.exit(1); }
  D.nocal = diff('meat_nocal'); D.trend = diff('gt_field_2016');
  const rowsOf = d => { const r = new Set(); for (const z of ZONES) d[z].forEach((x, i) => { if (x) r.add(data.yieldRows[i]); }); return r; };
  const field = new Set([...rowsOf(D.fieldLo), ...rowsOf(D.fieldHi)]), nocalRows = [...rowsOf(D.nocal)], trendRows = [...rowsOf(D.trend)];
  if (nocalRows.some(r => r !== 95 && r !== 98)) { console.error(`MC_WIDE: meat_nocal changes rows other than sheep meat (95) and cattle meat (98): ${nocalRows.join(' ')}`); process.exit(1); }
  if (trendRows.some(r => !field.has(r))) { console.error(`MC_WIDE: gt_field_2016 changes rows the field-crop factor does not: ${trendRows.filter(r => !field.has(r)).join(' ')}`); process.exit(1); }
  console.error(`MC_WIDE: ${LOSS.length} loss-factor cells; meat_nocal changes rows ${nocalRows.join(' ')}; gt_field_2016 changes ${trendRows.length} rows, all of them field-crop rows`);
}

function evaluate(p) {
  if (LONG) {
    if ((p.restable ?? 0) !== tableState) { ev.hf.batch(() => { for (const d of tabDiff) ev.hf.setCellContents({ sheet: resid(ev), row: d.row, col: d.col }, [[p.restable ? d.loo : d.base]]); }); tableState = p.restable ?? 0; }
    if (hasBench) for (const a of BENCH) { const { row, col } = decode(a); ev.hf.setCellContents({ sheet: ev.sid, row, col }, [[p.lbench]]); }
  }
  if (WIDE && (p.lossaus ?? 0) !== lossState) { ev.hf.batch(() => { for (const c of LOSS) ev.hf.setCellContents({ sheet: ev.bid, row: c.row, col: c.col }, [[c.us + p.lossaus * (c.au - c.us)]]); }); lossState = p.lossaus ?? 0; }
  for (const a of orgRows) setCell(a, p.orgfac);
  setCell('E2', `=Settings!B15-${p.orgshare}`);
  const row = {};
  for (const z of ZONES) {
    const y = baseMat[z].slice(), add = (d, s, lo, hi) => { const w = s >= 0 ? hi[z] : lo[z]; for (let i = 0; i < y.length; i++) if (w[i]) y[i] += Math.abs(s) * w[i]; };
    add(null, p.sf, D.fieldLo, D.fieldHi); add(null, p.sh, D.hortLo, D.hortHi);
    if (p.meat) for (let i = 0; i < y.length; i++) if (D.meat[p.meat][z][i]) y[i] += D.meat[p.meat][z][i];
    if (WIDE) for (let i = 0; i < y.length; i++) { if (D.nocal[z][i]) y[i] *= 1 + (1 - p.meatcal) * D.nocal[z][i] / baseMat[z][i]; if (D.trend[z][i]) y[i] += p.trendwin * D.trend[z][i]; }
    const region = WIDE && p.land ? { ...data.regions[z], yield: y, land: { ...data.regions[z].land, ...RASTER[z] } } : { ...data.regions[z], yield: y };
    for (const k of ['short', 'long']) {
      const pre = { ...data.regions[z].presets[k] }; if (k === 'long' && LONG) pre.fuel = p.lfuel; if (k === 'short') Object.assign(pre, { meategg: p.meategg, redmeat: p.redmeat, fuel: p.fuel, biofuel: p.biofuel, timber: p.timber, organic: p.orgshare });
      if (WIDE && k === 'short') Object.assign(pre, { losses: p.waste, food: pre.food * p.energy });
      row[`${z}_${k}`] = Math.round(ev.evaluate(region, { ...region.land, ...pre, population: region.population }).capacity);
    }
  }
  return row;
}
const LFUEL = data.regions[1].presets.long.fuel, LBENCH = hasBench ? model.sheets.Settings.cells[(() => { const { row, col } = decode('BQ4'); return `${row}:${col}`; })()] : 0.4;
const BASEP = { sf: 0, sh: 0, meat: 0, meategg: 0.12, redmeat: 0.578, fuel: 2360, biofuel: 0.0023, timber: 0.8, orgfac: BASEF, orgshare: 0.07, restable: 0, lfuel: LFUEL, lbench: LBENCH };
if (WIDE) Object.assign(BASEP, { waste: data.regions[1].presets.short.losses, ...(NOLOSS ? {} : { lossaus: 0 }), land: 0, meatcal: 1, energy: 1, trendwin: 0 });

if (arg3 === 'fixed') {
  const r = evaluate({ ...BASEP, ...JSON.parse(arg4 ?? '{}') });
  fs.writeFileSync(outFile, Object.keys(r).join(',') + '\n' + Object.values(r).join(',') + '\n'); console.log(r['1_short'], r['1_long']); process.exit(0);
}

if (arg3 === 'oat') {                    // one choice at a time over its range (the other nine at their base values): the responses for the quick range of rss_check.py
  const PTS = { sf: [-1, 0, 1], sh: [-1, 0, 1], meat: Array.from({ length: NMEAT }, (_, i) => i), meategg: [0.115, 0.12, 0.13], redmeat: [0.528, 0.578, 0.64], fuel: [2360, 2520], biofuel: [0.0023, 0.005],
                timber: [0.8, 1.0], orgfac: [0.771, BASEF, 0.845], orgshare: [0.02, 0.07, 0.12] };
  if (LONG) { PTS.restable = [0, 1]; PTS.lfuel = [156, LFUEL, 253]; if (hasBench) PTS.lbench = [0.30, LBENCH, 0.525]; }
  if (WIDE) Object.assign(PTS, { waste: [0.12, 0.13, 0.14], ...(NOLOSS ? {} : { lossaus: [0, 0.5, 1] }), land: [0, 1], meatcal: [0, 0.5, 1], energy: [1, (1 + ENMAX) / 2, ENMAX], trendwin: [0, 0.5, 1] });
  const lines = []; let head;
  const base = evaluate({ ...BASEP }); head = ['input', 'value', ...Object.keys(base)]; lines.push(['base', '', ...Object.values(base)].join(','));
  for (const [k, vals] of Object.entries(PTS)) for (const v of vals) lines.push([k, v, ...Object.values(evaluate({ ...BASEP, [k]: v }))].join(','));
  fs.writeFileSync(outFile, head.join(',') + '\n' + lines.join('\n') + '\n'); console.log('wrote', lines.length, 'runs'); process.exit(0);
}

// ---- Latin hypercube -------------------------------------------------------------------------------------------------------------------------
const SOBOL = arg3 === 'sobol', N = SOBOL ? +arg4 : +(arg3 ?? 1000);
let seed = 20261027; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const NAMES = ['sf', 'sh', 'meat', 'meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'orgfac', 'orgshare', ...(LONG ? ['restable', 'lfuel', 'lbench'] : []), ...(WIDE ? ['waste', ...(NOLOSS ? [] : ['lossaus']), 'land', 'meatcal', 'energy', 'trendwin'] : [])];
const makeLhs = () => NAMES.map(() => { const idx = Array.from({ length: N }, (_, i) => i); for (let i = N - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } return idx.map(i => (i + rnd()) / N); });
const lhs = makeLhs();
const tri = (u, a, c, b) => { const f = (c - a) / (b - a); return u < f ? a + Math.sqrt(u * (b - a) * (c - a)) : b - Math.sqrt((1 - u) * (b - a) * (b - c)); };
const lerp = (u, a, b) => a + u * (b - a);
const drawU = u => ({
  sf: lerp(u('sf'), -1, 1), sh: lerp(u('sh'), -1, 1), meat: Math.min(NMEAT - 1, Math.floor(u('meat') * NMEAT)),
  meategg: tri(u('meategg'), 0.115, 0.12, 0.13), redmeat: tri(u('redmeat'), 0.528, 0.578, 0.64),
  fuel: lerp(u('fuel'), 2360, 2520), biofuel: lerp(u('biofuel'), 0.0023, 0.005), timber: lerp(u('timber'), 0.8, 1.0),
  orgfac: lerp(u('orgfac'), 0.771, 0.845), orgshare: tri(u('orgshare'), 0.02, 0.07, 0.12),
  ...(LONG ? { restable: u('restable') < 0.5 ? 0 : 1, lfuel: tri(u('lfuel'), 156, LFUEL, 253), lbench: hasBench ? tri(u('lbench'), 0.30, LBENCH, 0.525) : LBENCH } : {}),
  ...(WIDE ? { waste: lerp(u('waste'), 0.12, 0.14), ...(NOLOSS ? {} : { lossaus: u('lossaus') }), land: u('land') < 0.5 ? 0 : 1, meatcal: u('meatcal'), energy: lerp(u('energy'), 1, ENMAX), trendwin: u('trendwin') } : {}) });
const draw = i => drawU(k => lhs[NAMES.indexOf(k)][i]);
if (SOBOL) {                             // Saltelli (2010) design: A, B and A with column j from B, for each draw i of this part
  const lhsB = makeLhs(), PART = +(arg5 ?? 0), NPARTS = +(arg6 ?? 1), lines = []; let head;
  for (let i = PART; i < N; i += NPARTS) {
    const uA = k => lhs[NAMES.indexOf(k)][i], uB = k => lhsB[NAMES.indexOf(k)][i];
    const runs = [['A', drawU(uA)], ['B', drawU(uB)], ...NAMES.map(n => [`AB_${n}`, drawU(k => k === n ? uB(k) : uA(k))])];
    for (const [blk, p] of runs) { const r = evaluate(p); if (!head) head = ['block', 'i', ...NAMES, ...Object.keys(r)]; lines.push([blk, i, ...NAMES.map(k => +p[k].toFixed(5)), ...Object.values(r)].join(',')); }
    if ((i - PART) / NPARTS % 50 === 49) console.error(`part ${PART}: ${(i - PART) / NPARTS + 1} of ${Math.ceil((N - PART) / NPARTS)} draws`);
  }
  fs.writeFileSync(outFile, head.join(',') + '\n' + lines.join('\n') + '\n'); console.log('wrote', lines.length, 'runs'); process.exit(0);
}
const out = []; let header;
for (let i = 0; i < N; i++) {
  const p = draw(i), r = evaluate(p); if (!header) header = [...NAMES, ...Object.keys(r)];
  out.push([...NAMES.map(k => +p[k].toFixed(5)), ...Object.values(r)].join(','));
  if ((i + 1) % 100 === 0) console.error(`${i + 1}/${N}`);
}
fs.writeFileSync(outFile, header.join(',') + '\n' + out.join('\n') + '\n'); console.log('wrote', N, 'draws');
