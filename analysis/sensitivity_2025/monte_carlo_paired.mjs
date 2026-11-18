// B133 (decision 135): paired draws for the change between 2011 and 2025. National, short and long term.
//   node analysis/sensitivity_2025/monte_carlo_paired.mjs                    (repository root; needs the built data and analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv)
//   writes analysis/sensitivity_2025/monte_carlo_draws_paired_2011-2025.csv and results/paired_change_2011-2025.csv
//   node analysis/sensitivity_2025/monte_carlo_paired.mjs --base-check       evaluates both releases at their base settings through this script's own path and compares them with the release (no files written)
//
// What is paired. The 2,000 draws are block A of monte_carlo_draws_2025-fixed_wide.csv (B115: 19 choices, seed 20261027, Latin hypercube). Each row is one set of choices. The 2025 capacity is the one that file
// holds for the row. The 2011 capacity (release 2011-fixed-3, the corrected 2011 release) is evaluated here with the choices both years share, taken from the same row (common random numbers); the 2025-only choices
// are left at the 2011 release's own values. SHARED (7 of the 19, the same uncertainty in both years):
//   energy    energy requirement per person (food amount, short term)  the same multiplier on each year's food amount
//   waste     avoidable waste (short term)                              the same rate (the 2011 release's 12% is the 2025 base too)
//   lossaus   retail and consumer loss factors                          the same weight between the US and the Australian factors (the 2011 and 2025 releases hold the same US factors; checked below)
//   orgfac    default organic yield factor                              the same value in the workbook's default organic cells (the two releases hold the same default; checked below)
//   meategg   meat and egg share of the diet                            a relative move: the 2011 release's 0.13 times the draw over the 2025 proxy 0.12 (a diet-share range is a range about a year's own share)
//   redmeat   red meat share of meat                                    a relative move: 0.64 times the draw over the 2025 proxy 0.578
//   restable  resilience table (long term only)                         the leave-one-out table moves every cell of the release's table by the same ratio in 2025; the same ratios are applied to the 2011 (thesis) table
// 2025-ONLY (the other 12 of the 19, listed here; each has no 2011 analogue, or the 2011 value is a measured input and not a proxy):
//   sf, sh        group factors of field crops and of vegetables, fruit and nuts: the error of the rule that carries the 2016-21 yields to 2022-25 (2011's yields are the thesis's own, not carried forward)
//   meat          window of herd and meat data: 2011 uses the archive years 2006 to 2010, a window that is not drawn
//   meatcal       calibration of the ABS meat tables to the archive's 2010 level: 2011 is the archive
//   trendwin      window of the field-crop group trend: the trend is a 2025 device
//   land          ABS holdings or the ABARES land-use raster: no 2011 raster is held, so the draw cannot be paired (the subset land = 0 is the like-for-like comparison)
//   fuel, biofuel, timber   the proxy value to the 2011 value: 2011 is the thesis value itself, the end of the 2025 range
//   orgshare      organic share of land: the 2011 release's 2% is the thesis's measured share; the range is the 2025 proxy's
//   lfuel         long-term liquid fuel: 156 to 253 about the re-derived 210; 2011 uses its own 253 (the thesis value)
//   lbench        feeding benchmark of the recycling-stage module: not present in either release (constant), listed for the 19
// (All 19 columns are kept in the draws file. Draw values are the file's five-decimal figures; the 2025 capacity is the one the widened draws file holds, computed from the unrounded values.)
// Besides the brief's columns the file carries cap2025_shared_only: 2025 with the shared choices drawn and every 2025-only choice at the release's value (from the release itself, no yield matrices needed),
// so the change can also be tested against the settings the years share alone.
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { methodModule } from '../../web/scripts/releases.mjs';
const root = new URL('../../', import.meta.url).pathname, dataDir = root + 'web/public/data/';
const SRC = root + 'analysis/sensitivity_2025/monte_carlo_draws_2025-fixed_wide.csv';
const OUT = root + 'analysis/sensitivity_2025/monte_carlo_draws_paired_2011-2025.csv', SUM = root + 'results/paired_change_2011-2025.csv';
const BASECHECK = process.argv.includes('--base-check');
const decode = a => { const m = a.match(/^([A-Z]+)(\d+)$/); let c = 0; for (const ch of m[1]) c = c * 26 + ch.charCodeAt(0) - 64; return { row: +m[2] - 1, col: c - 1 }; };
const load = id => ({ id, model: JSON.parse(fs.readFileSync(`${dataDir}${id}/model.json`)), data: JSON.parse(fs.readFileSync(`${dataDir}${id}/regions.json`)) });
const R25 = load('2025-fixed'), R11 = load('2011-fixed-3');
// the default organic cells: the Yield!G cells at the workbook default 0.8083 (the 119 cells monte_carlo.mjs draws, from variants.json org_def_lo); the same cells in both releases
const cellOf = (m, a) => { const { row, col } = decode(a); return m.sheets.Yield.cells[`${row}:${col}`]; };
const ORG = Object.keys(m25org()), BASEF = cellOf(R25.model, 'G7');
function m25org() { const o = {}; for (const [k, v] of Object.entries(R25.model.sheets.Yield.cells)) { const [r, c] = k.split(':').map(Number); if (c === 6 && Math.abs(v - 0.8083406058241784) < 1e-12) o['G' + (r + 1)] = v; } return o; }
if (ORG.length !== 119) { console.error(`expected 119 default organic cells, found ${ORG.length}`); process.exit(1); }
for (const R of [R11, R25]) if (ORG.some(a => Math.abs(cellOf(R.model, a) - BASEF) > 1e-12)) { console.error(`${R.id}: the default organic cells differ from ${BASEF}`); process.exit(1); }
// loss-factor cells, from the module monte_carlo.mjs uses; the US value is each release's own and must be the same
const LOSSC = Object.entries(methodModule('loss-factors-australia').cellOverrides.Base).map(([a, au]) => { const { row, col } = decode(a); return { row, col, au, us25: R25.model.sheets.Base.cells[`${row}:${col}`], us11: R11.model.sheets.Base.cells[`${row}:${col}`] }; });
if (LOSSC.some(c => typeof c.us25 !== 'number' || c.us25 !== c.us11 || typeof c.au !== 'number')) { console.error('the 2011 and 2025 releases do not hold the same US loss factors in the module cells'); process.exit(1); }
// the leave-one-out table against the release's: the ratio cell by cell (2025-fixed to 2025-resilience-loo)
const loo = JSON.parse(fs.readFileSync(`${dataDir}2025-resilience-loo/model.json`)).sheets.resilience.cells, t25 = R25.model.sheets.resilience.cells, t11 = R11.model.sheets.resilience.cells;
const TAB = Object.keys(loo).filter(k => loo[k] !== t25[k]).map(k => { const [r, c] = k.split(':').map(Number); return { row: r, col: c, k, ratio: typeof t25[k] === 'number' && t25[k] !== 0 ? loo[k] / t25[k] : null }; });
if (TAB.some(c => c.ratio === null)) { console.error('a changed table cell is not a number'); process.exit(1); }
if (TAB.some(c => typeof t11[c.k] !== 'number')) { console.error('the 2011 table lacks a cell the leave-one-out table changes'); process.exit(1); }

function makeEval(R) {
  const ev = new Evaluator(R.model), region = R.data.regions[1], rid = ev.hf.getSheetId('resilience'), us = R.id === '2011-fixed-3';
  const tab0 = R.model.sheets.resilience.cells; let lossState = 0, tabState = 0;
  const base = k => region.presets[k];
  // p: { energy, waste, lossaus, orgfac, dmeategg, dredmeat (the draw over the 2025 proxy), restable }, any missing one at the release's own value
  const evaluate = (p = {}) => {
    const q = { energy: 1, lossaus: 0, orgfac: BASEF, dmeategg: 1, dredmeat: 1, restable: 0, ...p };
    if (q.lossaus !== lossState) { ev.hf.batch(() => { for (const c of LOSSC) ev.hf.setCellContents({ sheet: ev.bid, row: c.row, col: c.col }, [[c.us25 + q.lossaus * (c.au - c.us25)]]); }); lossState = q.lossaus; }
    if (q.restable !== tabState) { ev.hf.batch(() => { for (const c of TAB) ev.hf.setCellContents({ sheet: rid, row: c.row, col: c.col }, [[q.restable ? tab0[c.k] * c.ratio : tab0[c.k]]]); }); tabState = q.restable; }
    for (const a of ORG) { const { row, col } = decode(a); ev.hf.setCellContents({ sheet: ev.yid, row, col }, [[q.orgfac]]); }
    const out = {};
    for (const k of ['short', 'long']) {
      const pre = { ...base(k) };
      if (k === 'short') Object.assign(pre, { losses: q.waste ?? pre.losses, food: pre.food * q.energy, meategg: pre.meategg * q.dmeategg, redmeat: pre.redmeat * q.dredmeat });
      out[k] = Math.round(ev.evaluate(region, { ...region.land, ...pre, population: region.population }).capacity);
    }
    return out;
  };
  return { evaluate, region };
}
const E11 = makeEval(R11), E25 = makeEval(R25);

// the 2011 and 2025 values when every shared choice is at its release value: must equal the release evaluated directly
const direct = (R, ev0 = new Evaluator(R.model)) => { const g = R.data.regions[1]; return Object.fromEntries(['short', 'long'].map(k => [k, Math.round(ev0.evaluate(g, { ...g.land, ...g.presets[k], population: g.population }).capacity)])); };
const b11 = E11.evaluate(), b25 = E25.evaluate(), d11 = direct(R11), d25 = direct(R25);
console.error(`base check: 2011 short ${b11.short} (release ${d11.short}), long ${b11.long} (${d11.long}); 2025 short ${b25.short} (${d25.short}), long ${b25.long} (${d25.long})`);
for (const [a, b, n] of [[b11, d11, '2011'], [b25, d25, '2025']]) for (const k of ['short', 'long']) if (a[k] !== b[k]) { console.error(`base check failed: ${n} ${k}`); process.exit(1); }
if (BASECHECK) {
  // --base-check JSON: the 2025 evaluation of these shared values (monte_carlo.mjs names: meategg and redmeat as shares), to compare with `monte_carlo.mjs WORK OUT fixed JSON` on 2025-fixed
  const i = process.argv.indexOf('--base-check'), j = process.argv[i + 1]; if (j) { const q = JSON.parse(j); const r = E25.evaluate({ ...q, dmeategg: (q.meategg ?? 0.12) / 0.12, dredmeat: (q.redmeat ?? 0.578) / 0.578 }); console.log(r.short, r.long); }
  process.exit(0);
}

// ---- the draws -------------------------------------------------------------------------------------------------------------------------------
const L = fs.readFileSync(SRC, 'utf8').trim().split(/\r?\n/), H = L[0].split(',');
const rowsA = L.slice(1).map(l => l.split(',')).filter(c => c[0] === 'A');
if (rowsA.length !== 2000) { console.error(`expected 2000 block A draws, found ${rowsA.length}`); process.exit(1); }
const CH = H.slice(H.indexOf('sf'), H.indexOf('trendwin') + 1);                     // the 19 choices in the file's order
if (CH.length !== 19) { console.error(`expected 19 choice columns, found ${CH.length}`); process.exit(1); }
const ix = n => H.indexOf(n), SHARED = ['energy', 'waste', 'lossaus', 'orgfac', 'meategg', 'redmeat', 'restable'];
const out = [['draw', ...CH, 'meategg_2011', 'redmeat_2011', 'cap2011_short', 'cap2025_short', 'diff_short', 'cap2011_long', 'cap2025_long', 'diff_long', 'cap2025_shared_only_short', 'cap2025_shared_only_long'].join(',')];
const D = [];
rowsA.forEach((c, i) => {
  const v = n => +c[ix(n)];
  if (+c[1] !== i) { console.error(`block A is not in draw order at row ${i}`); process.exit(1); }
  const p11 = { energy: v('energy'), waste: v('waste'), lossaus: v('lossaus'), orgfac: v('orgfac'), dmeategg: v('meategg') / 0.12, dredmeat: v('redmeat') / 0.578, restable: v('restable') };
  const a = E11.evaluate(p11), s = E25.evaluate({ ...p11, waste: v('waste') });
  const c25 = { short: +c[ix('1_short')], long: +c[ix('1_long')] };
  D.push({ i, land: v('land'), a, c25, s });
  out.push([i, ...CH.map(n => c[ix(n)]), (0.13 * p11.dmeategg).toFixed(5), (0.64 * p11.dredmeat).toFixed(5), a.short, c25.short, c25.short - a.short, a.long, c25.long, c25.long - a.long, s.short, s.long].join(','));
  if ((i + 1) % 250 === 0) console.error(`${i + 1}/2000`);
});
fs.writeFileSync(OUT, out.join('\n') + '\n');

// ---- the distribution of the change ----------------------------------------------------------------------------------------------------------
const pct = (v, q) => { const s = [...v].sort((a, b) => a - b), i = q * (s.length - 1), lo = Math.floor(i), hi = Math.min(lo + 1, s.length - 1); return s[lo] + (s[hi] - s[lo]) * (i - lo); };
const f3 = x => x.toFixed(3), share = (a, n) => (a / n).toFixed(4);
const HEAD = 'preset,basis,n_draws,release_2011_at_base,release_2025_at_base,diff_p5,diff_p50,diff_p95,ratio_p5,ratio_p50,ratio_p95,draws_with_a_fall,share_draws_with_a_fall,unpaired_share_2025_below_2011_at_base,unpaired_share_shifted_pairing,cap2011_p5,cap2011_p50,cap2011_p95,cap2025_p5,cap2025_p50,cap2025_p95,basis_description';
const rows = [HEAD];
const BASES = [
  ['all_draws', 'the 2,000 draws: 2025 with all 19 choices drawn, 2011 with the 7 shared choices drawn on the same rows (the 2025-only choices are 2025 data uncertainty)', () => true, d => d.c25],
  ['holdings_land_only', 'the draws with land = 0 (ABS holdings, as in 2011); the like-for-like land source', d => d.land === 0, d => d.c25],
  ['shared_choices_only', 'both years with the 7 shared choices drawn on the same rows and every 2025-only choice at the release value', () => true, d => d.s]];
for (const k of ['short', 'long']) for (const [id, desc, keep, side] of BASES) {
  const S = D.filter(keep), n = S.length, y11 = S.map(d => d.a[k]), y25 = S.map(d => side(d)[k]), df = y25.map((x, i) => x - y11[i]), rt = y25.map((x, i) => x / y11[i]);
  const fall = df.filter(x => x < 0).length;
  const unBase = y25.filter(x => x < b11[k]).length;                                         // R05a's reading: the 2025 draws against the 2011 value at its base settings
  const un = S.map((d, j) => side(S[(j + Math.floor(n / 2)) % n])[k] < d.a[k]).filter(Boolean).length;      // 2011's draw j against the 2025 draw half a hypercube away (no common random numbers)
  rows.push([k, id, n, b11[k], b25[k], ...[.05, .5, .95].map(q => Math.round(pct(df, q))), ...[.05, .5, .95].map(q => f3(pct(rt, q))), fall, share(fall, n), share(unBase, n), share(un, n),
    ...[.05, .5, .95].map(q => Math.round(pct(y11, q))), ...[.05, .5, .95].map(q => Math.round(pct(y25, q))), JSON.stringify(desc)].join(','));
}
fs.writeFileSync(SUM, rows.join('\n') + '\n');
for (const r of rows.slice(1)) console.log(r.split(',').slice(0, 15).join(','));
