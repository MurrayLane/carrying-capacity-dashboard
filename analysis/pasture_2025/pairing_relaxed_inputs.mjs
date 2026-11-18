// B114 (decision 107), step 1 of 2: what the corrected model needs per person, food group by food group, so that the pairing of pasture-fed food with crops can be relaxed
// outside the evaluator. The evaluator and the workbook are not changed: this script only sets inputs and reads cells. Australia, release 2025-fixed, presets short and long.
// Writes two files beside this script:
//   pairing_relaxed_inputs_2025-fixed.csv    per preset and food group: cropland and pasture m2 a person a year (Settings!C33:D40, C45:D46), energy kJ and protein g a person a day
//                                            (Base columns AF and AG of the diet rows of the group), plus the non-food needs and the land the model allocates
//   pairing_relaxed_meatscan_2025-fixed.csv  variant 2: the model's own diet family at every meat-and-egg share on its 0.5% grid (Settings!B10), run through the evaluator
// Run from the repository root:  node analysis/pasture_2025/pairing_relaxed_inputs.mjs [RELEASE]     then  python3 analysis/pasture_2025/pairing_relaxed.py
import fs from 'node:fs';
import { Evaluator } from '../../web/src/model/evaluator.js';
const id = process.argv[2] ?? '2025-fixed', here = new URL('./', import.meta.url).pathname, d = new URL(`../../web/public/data/${id}/`, import.meta.url).pathname;
const model = JSON.parse(fs.readFileSync(d + 'model.json')), regions = JSON.parse(fs.readFileSync(d + 'regions.json')).regions, R = regions[1];
const ev = new Evaluator(model), S = model.sheets.Settings.cells;
// Guard: the cells read below must still hold the formulas this script was written against (0-based keys row:col).
const expect = { '32:2': 'AC6:Base!AC89', '33:3': 'AC90:Base!AC143', '36:2': 'AC178', '36:3': 'AC175:Base!AC177', '75:1': '=B62', '61:2': 'C61/C53', '59:3': '=1-(SUM(E60:H60,C60))' };
for (const [k, v] of Object.entries(expect)) if (!String(S[k]).includes(v)) throw new Error(`Settings ${k} changed: ${S[k]}`);
// Food groups: Settings row (1-based) whose columns C (cropland) and D (pasture) carry the group's land, and the Base rows (1-based) whose diet columns carry its nutrients.
// Red meat is split: beef, lamb and veal are pasture-fed (Settings!D37 = Base!AC175:AC177); pork is crop-fed (Settings!C37 = Base!AC178 plus recycled feed).
const GROUPS = [
  ['cereals', 33, 'C', [[6, 89]]], ['dairy', 34, 'D', [[90, 143]]], ['fruit', 35, 'C', [[144, 165]]], ['legumes', 36, 'C', [[166, 173], [187, 194], [301, 305]]],
  ['red_meat_pasture_fed', 37, 'D', [[175, 177]]], ['red_meat_crop_fed', 37, 'C', [[178, 178]]], ['white_meat_eggs', 38, 'C', [[180, 186], [320, 320]]],
  ['nuts_seeds', 39, 'C', [[196, 210], [306, 319]]], ['vegetables', 40, 'C', [[211, 264]]], ['oils', 45, 'C', [[266, 282]]], ['sweeteners', 46, 'C', [[283, 296]]]];
const COL = { C: 2, D: 3 }, s = (r1, c) => ev.s(r1 - 1, c);                    // 1-based Settings row, 0-based column
const groupOf = r1 => GROUPS.find(g => g[3].some(([a, b]) => r1 >= a && r1 <= b));
const fmt = (x, n = 10) => Number.isFinite(x) ? +x.toPrecision(n) : x;
const inputs = [['release', 'preset', 'item', 'cropland_m2_pp', 'pasture_m2_pp', 'other_m2_pp', 'energy_kj_pd', 'protein_g_pd', 'note']];
const scan = [['release', 'preset', 'meategg', 'capacity', 'cropland_m2_pp', 'pasture_m2_pp', 'cropland_used_km2', 'energy_kj_pd', 'protein_g_pd', 'binding']];
for (const preset of ['short', 'long']) {
  const P = R.presets[preset], base = ev.evaluate(R, { ...R.land, ...P, population: R.population });
  const E = {}, Pr = {};
  for (const r of model.meta.dietRows) { const g = groupOf(r + 1); if (!g) continue; const e = ev.num(ev.bid, r, 31), q = ev.num(ev.bid, r, 32);
    E[g[0]] = (E[g[0]] ?? 0) + (Number.isFinite(e) ? e / 7 : 0); Pr[g[0]] = (Pr[g[0]] ?? 0) + (Number.isFinite(q) ? q / 7 : 0); }
  const sumE = Object.values(E).reduce((a, b) => a + b, 0), sumP = Object.values(Pr).reduce((a, b) => a + b, 0);
  if (Math.abs(sumE - base.diet.energy) > 1e-6 * base.diet.energy || Math.abs(sumP - base.diet.protein) > 1e-6 * base.diet.protein) throw new Error('group nutrients do not add to the diet');
  for (const [name, row, c] of GROUPS) {
    const land = s(row, COL[c]), crop = c === 'C' ? land : 0, past = c === 'D' ? land : 0;
    inputs.push([id, preset, name, fmt(crop), fmt(past), 0, fmt(E[name]), fmt(Pr[name]), `Settings!${c}${row}`]);
  }
  // Non-food needs a person: biofuel (row 47), textiles (row 48: crop fibre in C, wool in D), timber (row 49, non-agricultural), infrastructure (row 50).
  inputs.push([id, preset, 'nonfood_biofuel', fmt(s(47, 2)), 0, 0, 0, 0, 'Settings!C47']);
  inputs.push([id, preset, 'nonfood_textiles', fmt(s(48, 2)), fmt(s(48, 3)), 0, 0, 0, 'Settings!C48:D48 (D is wool)']);
  inputs.push([id, preset, 'nonfood_timber_infrastructure', 0, 0, fmt(s(49, 4) + s(50, 5)), 0, 0, 'Settings!E49 + F50']);
  // Totals as the model computes them, for the check that the closed form reproduces the evaluator.
  inputs.push([id, preset, 'model_total_need', fmt(s(52, 2)), fmt(s(52, 3)), fmt(s(52, 4) + s(52, 5)), fmt(base.diet.energy), fmt(base.diet.protein), 'Settings!C52:F52; diet from the evaluator']);
  const L = R.land, total = L.cropping + L.pasture + L.nonAg + L.infrastr1 + L.nature1;
  inputs.push([id, preset, 'land_km2', L.cropping, L.pasture, fmt(total * (1 - P.nature2) - L.cropping - L.pasture), 0, 0, 'cropland; pasture; other = total less reserve share less cropland and pasture']);
  inputs.push([id, preset, 'model_capacity', fmt(base.capacity, 10), fmt(s(61, 2), 10), fmt(s(61, 3), 10), 0, 0, 'Settings!B75; C61 and D61 = cropland and pasture the model allocates, km2']);
  inputs.push([id, preset, 'preset_meategg', P.meategg, 0, 0, 0, 0, 'Settings!B10']);
  // Variant 2: the model's own diet at every meat-and-egg share of its 0.5% grid, from zero to the preset's own share.
  for (let k = 0; k <= Math.round(P.meategg / 0.005); k++) {
    const mg = +(k * 0.005).toFixed(3), o = ev.evaluate(R, { ...R.land, ...P, meategg: mg, population: R.population });
    const used = s(61, 2), bind = used < L.cropping * (1 - 1e-9) ? 'pasture' : 'cropland';
    scan.push([id, preset, mg, fmt(o.capacity, 10), fmt(s(53, 2) * 1e6), fmt(s(53, 3) * 1e6), fmt(used, 10), fmt(o.diet.energy), fmt(o.diet.protein), bind]);
  }
}
fs.writeFileSync(here + `pairing_relaxed_inputs_${id}.csv`, inputs.map(r => r.join(',')).join('\n') + '\n');
fs.writeFileSync(here + `pairing_relaxed_meatscan_${id}.csv`, scan.map(r => r.join(',')).join('\n') + '\n');
console.log(`wrote pairing_relaxed_inputs_${id}.csv (${inputs.length - 1} rows) and pairing_relaxed_meatscan_${id}.csv (${scan.length - 1} rows)`);
