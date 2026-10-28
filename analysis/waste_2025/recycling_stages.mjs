// Line 2 (improved method): recycling split by stage, by origin and by dry matter.
//   node analysis/waste_2025/recycling_stages.mjs stages  OUT.csv     where the recyclable losses arise: stage x origin, Australia, release 2025-fuel (needs: cd web && node scripts/build-data.mjs)
//   node analysis/waste_2025/recycling_stages.mjs ladder  OUT.csv     capacity of Australia and four states as each correction is added, short and long term
//   node analysis/waste_2025/recycling_stages.mjs pool    OUT.csv     the fed pool by stage after the corrections, and the uptake observed in 2018-19 (FIAL 2021 Table 3)
//   node analysis/waste_2025/recycling_stages.mjs release             writes releases/2025-recycling-stage/release.json (cell overrides of the full method) and adds it to releases/index.json
//
// The thesis workbook (Base!P) credits a recycled share of ALL losses 1 - E*H*J*M (inedible part E, consumer H, retail J, primary-to-retail M; processing K only for foods where it is below 1), in wet
// grams, against an animal feed conversion ratio (Recycle!E) that is a mass of dry feed. Here the pool is split exactly as the workbook's own chain does it:
//   primary to retail  Y (1 - M)            retail  Y M (1 - J)            consumer avoidable  Y M J (1 - H)            inedible  Y M J H (1 - E)            processing  Y (O - (1 - E H J M))
// and each part is multiplied by (a) the share of it that can be fed (Settings!BL4:BM8, plant and animal origin), (b) for processing, the feed-grade share of the by-product class (Settings!BL12:BL17),
// (c) its dry matter, relative to the dry matter of feed (Settings!BL40). Settings!B13 (recycling) stays the overall uptake, as in the thesis.
import fs from 'node:fs';
import path from 'node:path';
import { Evaluator } from '../../web/src/model/evaluator.js';
const ROOT = new URL('../../', import.meta.url).pathname, dir = ROOT + 'web/public/data/2025-fuel/';
const [mode, outFile] = process.argv.slice(2);

// ---- the classification -------------------------------------------------------------------------------------------------------------------------
const ANIMAL = new Set(['milk (cow)', 'milk (sheep)', 'milk (goat)', 'egg', 'egg (chicken)', 'beef (dressed)', 'lamb (dressed)', 'veal (dressed)', 'pork (dressed)', 'fish (whole, farmed)', 'chicken (dressed)', 'duck (dressed)', 'turkey (dressed)', 'seafood']);
const CEREAL = new Set(['wheat (whole)', 'spelt (whole)', 'maize (whole)', 'rye (whole)', 'oats (whole)', 'rice (whole)', 'barley (whole)', 'oat (whole)', 'buckwheat (whole)', 'quinoa (whole)', 'oats', 'wheat', 'maize', 'rice', 'barley', 'rye']);
const OILSEED = new Set(['canola seed', 'soy bean', 'soy bean (whole)', 'sunflower seed', 'linseed', 'sesame seed', 'sesame', 'sunflower']);
const TUBER = new Set(['potato', 'sweetcorn (whole)', 'cassava', 'tapioca', 'sweet potato', 'sweet potato orange']);
// by-product classes: [name, feed-grade share, dry matter]
const PROC = [['whey and skim milk (cheese, butter, yoghurt)', 1, 0.07], ['bran, germ and offal (milling, rice, oats)', 1, 0.88], ['oilseed meal (canola, soy, sunflower)', 1, 0.90], ['potato and corn residues', 1, 0.20],
              ['shells, hulls, bagasse, pomace, grounds (not fed)', 0, 0.50], ['animal by-products (rendered, not fed)', 0, 0.30]];
const procClass = (prim) => ANIMAL.has(prim) ? (prim.startsWith('milk') ? 0 : 5) : CEREAL.has(prim) ? 1 : OILSEED.has(prim) ? 2 : TUBER.has(prim) ? 3 : 4;
// dry matter of the food as it is wasted (medians of AUSNUT 2007 raw foods for fruit, vegetables and nuts, dried legumes and grain, cow's milk 87% moisture; archive prelim models/ausnut07full.xls; judgement for the rest)
const DM = { 'Cereal whole': 0.88, 'Cereal ref': 0.88, 'Legume': 0.90, 'Nut & seed': 0.97, 'Fruit': 0.15, 'Vege green': 0.09, 'Vege orange': 0.15, 'Vege other': 0.08, 'Vege starch': 0.22, 'Fat & oil': 0.98, 'Other': 0.50,
             'Dairy High': 0.13, 'Dairy Med': 0.13, 'Dairy Low': 0.13, 'Meat red': 0.30, 'Meat white': 0.25, 'Lacto-ovo': 0.25 };
const FEED_DM = 0.88;
const STAGES = ['primary to retail (culls, transport, packing)', 'retail', 'consumer avoidable waste (households, food service)', 'inedible parts (peel, core, bones, shells)', 'processing by-products'];
const col = a => { let c = 0; for (const ch of a) c = c * 26 + ch.charCodeAt(0) - 64; return c - 1; };
const colName = n => { let t = ''; n++; while (n > 0) { const r = (n - 1) % 26; t = String.fromCharCode(65 + r) + t; n = Math.floor((n - 1) / 26); } return t; };

const model0 = JSON.parse(fs.readFileSync(dir + 'model.json')), regions = JSON.parse(fs.readFileSync(dir + 'regions.json')).regions;
const base = model0.sheets.Base.cells, bv = (r, c) => base[`${r - 1}:${c - 1}`];
const rowsInfo = [];                                    // every Base row that has a recyclable-loss formula
for (let r = 6; r <= 321; r++) { const o = bv(r, 15); if (o === undefined) continue; rowsInfo.push({ r, cat: bv(r, 1), prim: bv(r, 4), animal: ANIMAL.has(bv(r, 4)) }); }

// ---- Settings block and Base!P formulas for one parameter set ---------------------------------------------------------------------------------------
// shares[stage] = [plant, animal under current law, animal under adapted law]; procShare[class] = feed-grade share; dm on/off.
// The law in force follows the time frame (Settings!B8, years): from lawYears on, the adapted-law column applies (the short term is 1 year, the long term 100).
// intra = 1 lets the waste of a species be fed to the same species (Japan and South Korea allow it; the EU does not).
function overrides({ shares, procShare, dm, lawYears = 20, intra = 0 }) {
  const S = {}, put = (a, v) => { S[a] = v; };
  put('BK1', 'Recycling split by stage (line 2): share of each part of the recyclable losses that can be fed to animals');
  put('BK3', 'Stage'); put('BL3', 'Plant origin'); put('BM3', 'Animal origin, law in force'); put('BN3', 'Animal origin, current law'); put('BO3', 'Animal origin, law adapted');
  STAGES.forEach((s, i) => { put(`BK${4 + i}`, s); put(`BL${4 + i}`, shares[i][0]); put(`BM${4 + i}`, `=IF($B$8>=$BL$9,BO${4 + i},BN${4 + i})`); put(`BN${4 + i}`, shares[i][1]); put(`BO${4 + i}`, shares[i][2]); });
  put('BK9', 'The law is adapted from a time frame of this many years (Settings!B8)'); put('BL9', lawYears);
  put('BK10', 'Waste of a species may be fed to the same species (1 yes, 0 no)'); put('BL10', intra);
  put('BK11', 'Processing by-product class'); put('BL11', 'Feed-grade share'); put('BM11', 'Dry matter');
  PROC.forEach((p, i) => { put(`BK${12 + i}`, p[0]); put(`BL${12 + i}`, procShare[i]); put(`BM${12 + i}`, dm ? p[2] : 1); });
  put('BK19', 'Dry matter of the food as wasted (by diet category)');
  const cats = Object.keys(DM); for (const x of rowsInfo) if (!cats.includes(x.cat)) throw new Error('no dry matter for ' + x.cat + ' (row ' + x.r + ')'); cats.forEach((c, i) => { put(`BK${20 + i}`, c); put(`BL${20 + i}`, dm ? DM[c] : 1); });
  put('BK40', 'Dry matter of feed (the basis of the feed conversion ratios, Recycle!E)'); put('BL40', dm ? FEED_DM : 1);
  const B = {};
  for (const x of rowsInfo) {
    const o = x.animal ? 'BM' : 'BL', st = i => `Settings!$${o}$${4 + i}`, d = `Settings!$BL$${20 + cats.indexOf(x.cat)}`, pc = procClass(x.prim), r = x.r;
    const chain = `(1-E${r}*H${r}*J${r}*M${r})`;
    B[`P${r}`] = `=P$5*Y${r}*((1-M${r})*${st(0)}+M${r}*(1-J${r})*${st(1)}+M${r}*J${r}*(1-H${r})*${st(2)}+M${r}*J${r}*H${r}*(1-E${r})*${st(3)})*${d}/Settings!$BL$40`
         + `+P$5*Y${r}*MAX(0,O${r}-${chain})*${st(4)}*Settings!$BL$${12 + pc}*Settings!$BM$${12 + pc}/Settings!$BL$40`;
  }
  // Recycle!F2:F8 shares the fed pool among the animals in proportion to what is eaten (thesis); the waste of a species is taken out of the pool offered to its own kind (pigs; poultry and eggs; farmed fish and seafood)
  const own = { 2: 'Base!P178', 3: 'Base!P180+Base!P320+Base!P182+Base!P183+Base!P184', 7: 'Base!P181+Base!P186' }, R = {};
  for (let r = 2; r <= 8; r++) R[`F${r}`] = `=$D${r}*(F$9-(1-Settings!$BL$10)*(${own[r === 2 ? 2 : r <= 6 ? 3 : 7]}))`;
  return { Settings: S, Base: B, Recycle: R };
}
const ALL = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], ONE = PROC.map(() => 1);
const LAW = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]];                       // current law: animal-origin waste is not fed,                       // factory by-product streams are
const ADAPT = [[1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]];                     // law adapted (Japan and South Korea): heat-treated animal-origin waste may be fed to pigs, poultry and fish, never to ruminants
const FEED = PROC.map(p => p[1]);                                          // only feed-grade by-products
const STEPS = [['thesis (as published)', null], ['dry matter of the waste counted', { shares: ALL, procShare: ONE, dm: true, intra: 1 }], ['animal-origin waste not fed', { shares: LAW, procShare: ONE, dm: true, intra: 1 }],
               ['only feed-grade by-products (the improved method)', { shares: LAW, procShare: FEED, dm: true }],
               ['law adapted in the long term (the Japan and South Korea model)', { shares: ADAPT, procShare: FEED, dm: true }]];

function evaluatorFor(ov) {
  const m = JSON.parse(JSON.stringify(model0));
  if (ov) for (const [sheet, cells] of Object.entries(ov)) for (const [a, v] of Object.entries(cells)) { const mm = a.match(/^([A-Z]+)(\d+)$/); m.sheets[sheet].cells[`${+mm[2] - 1}:${col(mm[1])}`] = v; }
  return new Evaluator(m);
}
const run = (ev, z, k, rec) => { const R = regions[z]; return ev.evaluate(R, { ...R.land, ...R.presets[k], recycling: rec, population: R.population }); };

// share of each stage's feed-grade pool that was fed in 2018-19 (FIAL 2021, Table 3; analysis/waste_2025/fial_destinations.csv). Primary production is not in the table (unmeasured, taken as 0);
// households, food service and public procurement send nothing to feed; retail 68 of 629 thousand tonnes (waste 526, feed 68, other recovery 35); manufacturing 6,253 of 11,131 (waste 1,276, feed 6,253, other recovery 3,602)
const OBSERVED = [0, 68 / 629, 0, 0, 6253 / 11131];
function pool(k) {                                                     // fed pool of the improved method by stage (dry-matter feed grams a week at 100% uptake), Australia
  const FEEDG = PROC.map(p => p[1]), out = [];
  for (let s = 0; s < 5; s++) { const shares = [0, 1, 2, 3, 4].map(i => i === s ? [1, s === 4 ? 1 : 0, 1] : [0, 0, 0]), ev = evaluatorFor(overrides({ shares, procShare: FEEDG, dm: true }));
    run(ev, 1, k, 1); const sid = ev.hf.getSheetId('Recycle'); out.push(ev.hf.getCellValue({ sheet: sid, row: 8, col: 5 })); }
  return out;
}
const effectiveUptake = k => { const p = pool(k); return p.reduce((a, g, i) => a + g * OBSERVED[i], 0) / p.reduce((a, g) => a + g, 0); };

if (mode === 'pool') {
  const out = ['setting,stage,fed_pool_g_per_week,share_of_pool,uptake_2018_19'];
  for (const k of ['short', 'long']) { const p = pool(k), t = p.reduce((a, g) => a + g, 0); p.forEach((g, i) => out.push([k, `"${STAGES[i]}"`, Math.round(g), (g / t).toFixed(3), OBSERVED[i].toFixed(3)].join(','))); out.push([k, 'all stages', Math.round(t), 1, effectiveUptake(k).toFixed(3)].join(',')); }
  fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log(out.join('\n'));
} else if (mode === 'stages') {
  const ev = new Evaluator(model0), sid = ev.hf.getSheetId('Base'), val = (r, c) => ev.hf.getCellValue({ sheet: sid, row: r - 1, col: c - 1 });
  const out = ['setting,stage,origin,g_per_week,share_of_pool'];
  for (const k of ['short', 'long']) {
    run(ev, 1, k, 1); const T = {}; let tot = 0;
    for (const x of rowsInfo) { const r = x.r, [E, H, J, M, Y, P] = [5, 8, 10, 13, 25, 16].map(c => val(r, c)); if (![E, H, J, M, Y, P].every(v => typeof v === 'number')) continue;
      const parts = [Y * (1 - M), Y * M * (1 - J), Y * M * J * (1 - H), Y * M * J * H * (1 - E), P - Y * (1 - E * H * J * M)];
      parts.forEach((g, i) => { const key = `${i}|${x.animal ? 'animal' : 'plant'}`; T[key] = (T[key] ?? 0) + g; }); tot += P; }
    for (let i = 0; i < 5; i++) for (const o of ['plant', 'animal']) { const g = T[`${i}|${o}`] ?? 0; out.push([k, `"${STAGES[i]}"`, o, Math.round(g), (g / tot).toFixed(4)].join(',')); }
  }
  fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log(out.join('\n'));
} else if (mode === 'ladder') {
  const out = ['setting,zone,step,recycling,capacity'];
  for (const [name, p] of STEPS) { const ev = evaluatorFor(p && overrides(p));
    for (const k of ['short', 'long']) for (const z of [1, 2, 15, 26, 49]) for (const rec of [0, 0.25, 0.4, 0.5, 0.75, 1]) out.push([k, z, name, rec, Math.round(run(ev, z, k, rec).capacity)].join(',')); }
  fs.writeFileSync(outFile, out.join('\n') + '\n'); console.log('wrote', out.length - 1);
} else if (mode === 'release') {
  const ov = overrides(STEPS[4][1]), parent = JSON.parse(fs.readFileSync(ROOT + 'releases/2025-resilience/release.json'));
  const rel = {
    id: '2025-recycling-stage', label: 'Alternate: recycling split by stage, origin, dry matter and the law in force', status: 'current', extends: '2025-fuel',
    description: 'An alternate to 2025-fuel, not a later layer, and a change to the method (line 2 of the two lines of enquiry: the thesis method is kept in 2025-fuel). The thesis credits a share of ALL losses as animal feed, in wet grams, and at 100% feeds the whole pig, poultry, egg and farmed-fish industry on waste. Here the recyclable losses are split as the workbook\'s own loss chain gives them (primary to retail, retail, consumer avoidable, inedible parts, processing); only feed-grade processing by-products count (whey, bran, oilseed meal, potato and corn residues; not shells, bagasse, pomace or grounds); every gram is counted at its dry matter against a feed conversion ratio measured on dry feed; and the law decides what may be fed: with a time frame under 20 years (the short term) animal-origin food waste is not fed, as the swill rules now require, and from 20 years on (the long term) it may be fed to pigs, poultry and fish after heat treatment, never to ruminants, as Japan and South Korea allow, with the waste of a species kept from its own kind. The recycling setting is the uptake of what may be fed: 16% in the short term (2018-19 practice) and 40% in the long term (Japan and South Korea achieve 36 to 43% of all food waste as feed). The tables are in Settings!BK1:BO40 and can be edited.',
    layer: parent.layer, vintage: parent.vintage,
    patches: [{ preset: 'short', field: 'recycling', value: Math.round(effectiveUptake('short') * 100) / 100, reason: 'Short-term uptake of the feed pool that the method counts: the share of each stage\'s feed-grade pool that was fed in 2018-19, weighted by the size of the pool (FIAL 2021 Table 3; analysis/waste_2025/pool.csv). Retail 11%, manufacturing 56%, households, food service and procurement none; primary production is not measured and counted as none. The thesis short-term setting was 0%.' },
              { preset: 'long', field: 'recycling', value: 0.4, reason: 'Long-term uptake of the feed pool: 40% of what may be fed, the national rates achieved with a heat-treated food waste feed system: Japan 35.9% and South Korea 42.5% of all food waste recycled as animal feed in 2006-07 (their mean, 39.2%, is also the figure used by zu Ermgassen et al. 2016 for the EU). Even South Korea, which bans landfill of food waste and recycles 98% by all routes, feeds less than half. The thesis long-term setting was 100%.' }],
    model: { file: parent.model.file, cellOverrides: { ...parent.model.cellOverrides, Settings: { ...(parent.model.cellOverrides.Settings ?? {}), ...ov.Settings }, Base: ov.Base, Recycle: ov.Recycle } },
    errata: ['Dry matters are medians of raw foods by diet category (AUSNUT 2007), not item by item; the feed-grade shares of by-products are judgements listed in Settings!BL12:BL17.',
             'The long-term law is an assumption (the setting that the law is adapted from a time frame of 20 years is Settings!BL9): Australia bans feeding food waste containing meat or dairy to pigs and ruminants, and its biosecurity case rests on foot-and-mouth disease and African swine fever; Japan and South Korea feed heat-treated waste (70 degrees for 30 minutes, 80 degrees for 3 minutes in Japan; 80 degrees for 30 minutes in South Korea) and have recorded no outbreak traced to it. The argument that local supply chains lower the disease risk is not tested by the model.',
             'Processing by-products such as whey, bran and oilseed meal are already fed to animals today (food manufacturing sends 6.25 million tonnes a year to animal feed, FIAL 2021); the model prices all feed as primary crops, so the credit is not double counted, but the thesis short-term setting of 0% understates current practice.',
             'The Japan and South Korea rates are shares of all food waste, including the parts that cannot be fed, and are applied here to the part that may be fed, which is conservative; Japan excluding households reached 52.5%.',
             'The shares of consumer-level and primary-to-retail plant waste that can actually be collected and fed are not measured in Australia.'] };
  fs.mkdirSync(ROOT + 'releases/2025-recycling-stage', { recursive: true });
  fs.writeFileSync(ROOT + 'releases/2025-recycling-stage/release.json', JSON.stringify(rel, null, 2));
  const idx = JSON.parse(fs.readFileSync(ROOT + 'releases/index.json')); if (!idx.order.includes(rel.id)) { idx.order.splice(idx.order.indexOf('2025-fuel-ev') + 1, 0, rel.id); fs.writeFileSync(ROOT + 'releases/index.json', JSON.stringify(idx, null, 2)); }
  console.log('wrote releases/2025-recycling-stage/release.json;', Object.keys(ov.Base).length, 'Base formulas');
} else { console.error('mode: pool | stages | ladder | release'); process.exit(1); }
