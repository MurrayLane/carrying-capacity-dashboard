// E8: Monte Carlo ranges for the 2025-organic result (env MC_RELEASE=<id> to draw on another release of the 2025 chain, for example 2025-mirror or 2025-improved).
//   node monte_carlo.mjs WORK_DIR OUT.csv [N]            random draws (Latin hypercube, seed 20261027); WORK_DIR is the folder of build_variants.py
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
const ZONES = [1, 2, 15, 26, 40, 49, 56, 60];
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return { row: +m[2] - 1, col: c - 1 }; };

function readMatrix(file) {
  const lines = fs.readFileSync(file, 'utf8').trim().split(/\r?\n/), head = lines[0].split(',').slice(1).map(Number), out = {};
  for (const l of lines.slice(1)) { const c = l.split(','); out[+c[0]] = head.map((row, i) => [data.yieldRows.indexOf(row), +c[i + 1]]); }
  return out;
}
const baseY = {};                                                           // zone -> yield vector of the release
for (const z of ZONES) baseY[z] = data.regions[z].yield.slice();
const asVec = m => { const v = {}; for (const z of ZONES) { v[z] = baseY[z].slice(); for (const [i, x] of m[z]) v[z][i] = x; } return v; };
const baseMat = asVec(readMatrix(root + 'data/2025/yield_matrix_livestock.csv'));
const diff = (id, dir = work) => { const m = asVec(readMatrix(`${dir}/${id}/yield_matrix_livestock.csv`)), d = {}; for (const z of ZONES) d[z] = m[z].map((x, i) => (x ?? 0) - (baseMat[z][i] ?? 0)); return d; };
const D = { fieldLo: diff('gt_field_lo'), fieldHi: diff('gt_field_hi'), hortLo: diff('gt_hort_lo'), hortHi: diff('gt_hort_hi'), meat: [null, diff('meat_early'), diff('meat_3y')] };
// MC_WIN_DIR=<folder with meat_8y, meat_10y, meat_15y, meat_20y, made as in README.md> draws the meat window from the base window and those four full-cycle windows instead
// (herds and meat of 2018-19 to 2024-25 and so on back to 2006-07 and 2024-25), five equal chances.
if (process.env.MC_WIN_DIR) D.meat = [null, ...['meat_8y', 'meat_10y', 'meat_15y', 'meat_20y'].map(id => diff(id, process.env.MC_WIN_DIR))];
const NMEAT = process.env.MC_WIN_DIR ? 5 : 3;
const orgRows = Object.keys(JSON.parse(fs.readFileSync(`${work}/variants.json`)).find(v => v.id === 'org_def_lo').modelCells);

const ev = new Evaluator(model);
const setCell = (a, v) => { const { row, col } = decode(a); ev.hf.setCellContents({ sheet: ev.yid, row, col }, [[v]]); };
const BASEF = (() => { const { row, col } = decode(orgRows[0]); return model.sheets.Yield.cells[`${row}:${col}`]; })();       // the default organic factor of the workbook (0.8083)

function evaluate(p) {
  for (const a of orgRows) setCell(a, p.orgfac);
  setCell('E2', `=Settings!B15-${p.orgshare}`);
  const row = {};
  for (const z of ZONES) {
    const y = baseMat[z].slice(), add = (d, s, lo, hi) => { const w = s >= 0 ? hi[z] : lo[z]; for (let i = 0; i < y.length; i++) if (w[i]) y[i] += Math.abs(s) * w[i]; };
    add(null, p.sf, D.fieldLo, D.fieldHi); add(null, p.sh, D.hortLo, D.hortHi);
    if (p.meat) for (let i = 0; i < y.length; i++) if (D.meat[p.meat][z][i]) y[i] += D.meat[p.meat][z][i];
    const region = { ...data.regions[z], yield: y };
    for (const k of ['short', 'long']) {
      const pre = { ...data.regions[z].presets[k] }; if (k === 'short') Object.assign(pre, { meategg: p.meategg, redmeat: p.redmeat, fuel: p.fuel, biofuel: p.biofuel, timber: p.timber, organic: p.orgshare });
      row[`${z}_${k}`] = Math.round(ev.evaluate(region, { ...region.land, ...pre, population: region.population }).capacity);
    }
  }
  return row;
}
const BASEP = { sf: 0, sh: 0, meat: 0, meategg: 0.12, redmeat: 0.578, fuel: 2360, biofuel: 0.0023, timber: 0.8, orgfac: BASEF, orgshare: 0.07 };

if (arg3 === 'fixed') {
  const r = evaluate({ ...BASEP, ...JSON.parse(arg4 ?? '{}') });
  fs.writeFileSync(outFile, Object.keys(r).join(',') + '\n' + Object.values(r).join(',') + '\n'); console.log(r['1_short'], r['1_long']); process.exit(0);
}

if (arg3 === 'oat') {                    // one choice at a time over its range (the other nine at their base values): the responses for the quick range of rss_check.py
  const PTS = { sf: [-1, 0, 1], sh: [-1, 0, 1], meat: Array.from({ length: NMEAT }, (_, i) => i), meategg: [0.115, 0.12, 0.13], redmeat: [0.528, 0.578, 0.64], fuel: [2360, 2520], biofuel: [0.0023, 0.005],
                timber: [0.8, 1.0], orgfac: [0.771, BASEF, 0.845], orgshare: [0.02, 0.07, 0.12] };
  const lines = []; let head;
  const base = evaluate({ ...BASEP }); head = ['input', 'value', ...Object.keys(base)]; lines.push(['base', '', ...Object.values(base)].join(','));
  for (const [k, vals] of Object.entries(PTS)) for (const v of vals) lines.push([k, v, ...Object.values(evaluate({ ...BASEP, [k]: v }))].join(','));
  fs.writeFileSync(outFile, head.join(',') + '\n' + lines.join('\n') + '\n'); console.log('wrote', lines.length, 'runs'); process.exit(0);
}

// ---- Latin hypercube -------------------------------------------------------------------------------------------------------------------------
const N = +(arg3 ?? 1000);
let seed = 20261027; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const NAMES = ['sf', 'sh', 'meat', 'meategg', 'redmeat', 'fuel', 'biofuel', 'timber', 'orgfac', 'orgshare'];
const lhs = NAMES.map(() => { const idx = Array.from({ length: N }, (_, i) => i); for (let i = N - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } return idx.map(i => (i + rnd()) / N); });
const tri = (u, a, c, b) => { const f = (c - a) / (b - a); return u < f ? a + Math.sqrt(u * (b - a) * (c - a)) : b - Math.sqrt((1 - u) * (b - a) * (b - c)); };
const lerp = (u, a, b) => a + u * (b - a);
const draw = i => { const u = k => lhs[NAMES.indexOf(k)][i]; return {
  sf: lerp(u('sf'), -1, 1), sh: lerp(u('sh'), -1, 1), meat: Math.min(NMEAT - 1, Math.floor(u('meat') * NMEAT)),
  meategg: tri(u('meategg'), 0.115, 0.12, 0.13), redmeat: tri(u('redmeat'), 0.528, 0.578, 0.64),
  fuel: lerp(u('fuel'), 2360, 2520), biofuel: lerp(u('biofuel'), 0.0023, 0.005), timber: lerp(u('timber'), 0.8, 1.0),
  orgfac: lerp(u('orgfac'), 0.771, 0.845), orgshare: tri(u('orgshare'), 0.02, 0.07, 0.12) }; };
const out = []; let header;
for (let i = 0; i < N; i++) {
  const p = draw(i), r = evaluate(p); if (!header) header = [...NAMES, ...Object.keys(r)];
  out.push([...NAMES.map(k => +p[k].toFixed(5)), ...Object.values(r)].join(','));
  if ((i + 1) % 100 === 0) console.error(`${i + 1}/${N}`);
}
fs.writeFileSync(outFile, header.join(',') + '\n' + out.join('\n') + '\n'); console.log('wrote', N, 'draws');
