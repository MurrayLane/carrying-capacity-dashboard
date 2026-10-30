// A line-protocol server around the model for the nutrition-constrained optimisation (SCOPE.md E11): it knows the model's accounting units and evaluates a diet given as grams of each unit.
//   node analysis/nutrition_lp_2025/server.mjs RELEASE ZONE PRESET        (repository root; needs the built data); reads JSON lines on stdin, answers JSON lines on stdout
// Commands: {"cmd":"units"}  -> the units, their groups, serves ranges and nutrient floors;   {"cmd":"eval","grams":{row: grams per week}}  -> capacity and the land used by type.
// An accounting unit is a row of the Base sheet that carries the land of a food (column AC); its grams are Q x R x X (serve size, serves a week, share of the group), and its nutrients are read from columns AF to AK where the workbook has them (cheeses and some composites have none): a composite food's TOTAL row (breads, poultry, ...) or a single-ingredient row. The
// model's diet is a serves-a-week figure for each of 17 food groups (Base column R of the group's TOTAL row, from the Diet sheet) and the shares of the group's serves among its units (column V, normalised in X);
// a diet in grams of each unit is set by writing exactly those cells, so every other formula of the model (losses, ingredient mix, yields, land, recycling, the allocation of land types) is the model's own.
import fs from 'node:fs';
import readline from 'node:readline';
import { Evaluator } from '../../web/src/model/evaluator.js';
const [rel, zoneId, preset] = process.argv.slice(2), d = new URL(`../../web/public/data/${rel}/`, import.meta.url).pathname;
const RJ = JSON.parse(fs.readFileSync(d + 'regions.json')), model = JSON.parse(fs.readFileSync(d + 'model.json')), R = RJ.regions[zoneId];
for (const f of (process.env.YIELD_SCALE ?? '').split(',').filter(Boolean)) { const [row, x] = f.split(':').map(Number); R.yield[RJ.yieldRows.indexOf(row)] *= x; }      // YIELD_SCALE=131:0.54 scales Yield-sheet rows of this zone (sensitivity tests, e.g. the GAEZ cassava ratio)
const ev = new Evaluator(model), hf = ev.hf, bid = ev.bid, did = hf.getSheetId('Diet');
const B = model.sheets.Base.cells, cell = (r, c) => B[`${r - 1}:${c}`];
const num = (r, c) => ev.num(bid, r - 1, c);
const set = (r, c, v) => hf.setCellContents({ sheet: bid, row: r - 1, col: c }, [[v]]);
const inputs = { ...R.land, ...R.presets[preset], population: R.population };
const run = () => ev.evaluate(R, inputs);
// ---- units and groups -----------------------------------------------------------------------------------------------------------------------------------------------------
const FOODCATS = new Set(['Cereal whole', 'Cereal ref', 'Dairy High', 'Dairy Med', 'Dairy Low', 'Fruit', 'Legume', 'Meat red', 'Meat white', 'Nut & seed', 'Vege green', 'Vege orange', 'Vege other', 'Vege starch', 'Fat & oil', 'Other', 'Lacto-ovo']);
const DIETROW = { 'Cereal whole': 3, 'Cereal ref': 4, 'Dairy High': 5, 'Dairy Med': 6, 'Dairy Low': 7, 'Fruit': 8, 'Legume': 9, 'Meat red': 10, 'Meat white': 11, 'Nut & seed': 12, 'Vege green': 13, 'Vege orange': 14, 'Vege other': 15, 'Vege starch': 16, 'Fat & oil': 17, 'Other': 18, 'Lacto-ovo': 19 };
const PASTURE = r => (r >= 90 && r <= 143) || (r >= 175 && r <= 177);                  // the Settings formulas: dairy and beef, lamb, veal are pasture-fed, the rest is cropping
// the unit rows: land (AC, col 28) and grams (AD, col 29) defined, a food category, and a serves cell (col 17) that refers to a group total
const units = [];
for (let r = 6; r <= 346; r++) {
  const cat = cell(r, 0), land = cell(r, 28), Rf = cell(r, 17); if (!FOODCATS.has(cat) || land === undefined || typeof Rf !== 'string') continue;
  const m = /R\$?(\d+)/.exec(Rf); if (!m) continue; units.push({ row: r, cat, sub: cell(r, 1), name: cell(r, 2) === 'TOTAL' ? `${cell(r, 1)}` : `${cell(r, 1)} ${cell(r, 3)}`, groupRow: +m[1], Q: cell(r, 16), type: PASTURE(r) ? 'pasture' : 'crop' });
}
const groups = {}; for (const u of units) (groups[u.groupRow] ??= { row: u.groupRow, cat: u.cat, diet: DIETROW[u.cat], units: [] }).units.push(u.row);
const original = { R: {}, V: {} }; for (const g of Object.values(groups)) original.R[g.row] = cell(g.row, 17); for (const u of units) original.V[u.row] = cell(u.row, 21);
// ---- probe: every group at 7 serves a week, every unit at equal preference, to read the per-gram coefficients ----------------------------------------------------------------
const apply = (serves, prefs) => { for (const [gr, s] of Object.entries(serves)) set(+gr, 17, s); for (const [ur, v] of Object.entries(prefs)) set(+ur, 21, v); };
apply(Object.fromEntries(Object.keys(groups).map(g => [g, 7])), Object.fromEntries(units.map(u => [u.row, 1])));
let out = run();
const coef = units.map(u => { const g = num(u.row, 16) * num(u.row, 17) * num(u.row, 23); return { ...u, grams: g, land: num(u.row, 28), kJ: num(u.row, 31), protein: num(u.row, 32), fat: num(u.row, 33), carb: num(u.row, 34), sugar: num(u.row, 35), fibre: num(u.row, 36) }; });
for (const u of coef) { u.ok = u.grams > 0 && u.land >= 0 && Number.isFinite(u.land); }
// ---- the diet family of the Diet sheet: serves ranges per group and nutrient floors over the sedentary diets ----------------------------------------------------------------
const D = model.sheets.Diet.cells; const range = {};
for (const g of Object.values(groups)) { const vals = []; for (let c = 4; c <= 34; c++) { const v = D[`${g.diet - 1}:${c}`]; if (typeof v === 'number') vals.push(v); } range[g.row] = [Math.min(...vals), Math.max(...vals)]; }
const family = [];
for (let k = 0; k <= 30; k++) { const m = k * 0.005; apply(Object.fromEntries(Object.keys(groups).map(g => [g, original.R[g]])), original.V); const o = ev.evaluate(R, { ...inputs, meategg: m, redmeat: 0.578, activity: 1 }); family.push({ meat: m, ...o.diet }); }
apply(original.R, original.V);
const cuts = (key) => Math.min(...family.map(f => f[key]));
// ---- evaluation --------------------------------------------------------------------------------------------------------------------------------------------------------------
function evaluate(grams, opts = {}) {                                                   // grams: unit row -> grams a week eaten; groups with no unit eaten get 0 serves
  const serves = {}, prefs = {};
  for (const g of Object.values(groups)) { let s = 0; for (const ur of g.units) { const u = coef.find(x => x.row === ur); const q = (grams[ur] ?? 0) / u.Q; s += q; prefs[ur] = Math.max(q, 0); } serves[g.row] = s; }
  for (const g of Object.values(groups)) if (serves[g.row] === 0) for (const ur of g.units) prefs[ur] = 1;
  apply(serves, prefs); const o = ev.evaluate(R, { ...inputs, ...(opts.inputs ?? {}) });
  return { capacity: o.capacity, existing: o.existing, used: o.used, diet: o.diet };
}
const rl = readline.createInterface({ input: process.stdin });
rl.on('line', line => {
  const q = JSON.parse(line);
  if (q.cmd === 'units') console.log(JSON.stringify({ units: coef.map(({ row, cat, sub, name, groupRow, Q, type, ok, grams, land, kJ, protein, fat, carb, sugar, fibre }) => ({ row, cat, sub, name, groupRow, Q, type, ok, perGram: ok ? { land: land / grams, kJ: kJ / grams, protein: protein / grams, fat: fat / grams, carb: carb / grams, sugar: sugar / grams, fibre: fibre / grams } : null })),
    groups: Object.values(groups).map(g => ({ ...g, serves: range[g.row] })), floors: { kJ: cuts('energy'), protein: cuts('protein'), fibre: cuts('fibre') }, family, defaultServes: original.R }));
  else if (q.cmd === 'eval') console.log(JSON.stringify(evaluate(q.grams, q)));
  else if (q.cmd === 'familygrams') {                                                    // the grams of every unit in each of the family's 31 sedentary diets (meat and egg share 0 to 15%)
    apply(original.R, original.V); const fam = [];
    for (let k = 0; k <= 30; k++) { ev.evaluate(R, { ...inputs, meategg: k * 0.005, redmeat: 0.578, activity: 1 }); fam.push({ meat: k * 0.005, grams: Object.fromEntries(coef.map(u => [u.row, num(u.row, 16) * num(u.row, 17) * num(u.row, 23)])) }); }
    apply(original.R, original.V); ev.evaluate(R, inputs); console.log(JSON.stringify(fam)); }
  else if (q.cmd === 'defaultgrams') { apply(original.R, original.V); const o = ev.evaluate(R, inputs); console.log(JSON.stringify({ capacity: o.capacity, grams: Object.fromEntries(coef.map(u => [u.row, num(u.row, 16) * num(u.row, 17) * num(u.row, 23)])), serves: Object.fromEntries(Object.values(groups).map(g => [g.row, num(g.row, 17)])), shares: Object.fromEntries(coef.map(u => [u.row, num(u.row, 23)])) })); }
  else if (q.cmd === 'default') { apply(original.R, original.V); const o = ev.evaluate(R, inputs); console.log(JSON.stringify({ capacity: o.capacity, existing: o.existing, used: o.used, diet: o.diet })); }
});
