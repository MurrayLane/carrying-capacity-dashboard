// Evaluates release 2025-fixed with the diet inputs of each FAO window (B138 item 5). Called by diet_window.py:  cd web && node ../analysis/diet_2025/diet_window_eval.mjs W.json OUT.csv
// For each window: the three diet inputs (meat-and-egg share, red-meat share, red-meat split Base!V175:V178) set in the evaluator, as rounded by the release and unrounded, for Australia and the seven states,
// short term and long term (the long term takes meategg and redmeat from the time frame, so only the red-meat split moves it). Effect = capacity minus capacity with the 2011 values of the three inputs.
import fs from 'node:fs'; import path from 'node:path';
import { Evaluator } from '../../web/src/model/evaluator.js';
import { dataDir, PRESETS } from '../../web/scripts/results-lib.mjs';
const [wf, out] = process.argv.slice(2), W = JSON.parse(fs.readFileSync(wf)), id = '2025-fixed';
const model = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'model.json'))), regions = JSON.parse(fs.readFileSync(path.join(dataDir(id), 'regions.json'))).regions, ev = new Evaluator(model);
const ROW = { 175: 174, 176: 175, 177: 176, 178: 177 }, COL = 21;      // Base!V175:V178 (zero-based row, column V)
for (const r of [175, 176, 177, 178]) if (Math.abs(model.sheets.Base.cells[`${ROW[r]}:${COL}`] - { 175: 0.595284, 176: 0.231357, 177: 0.01714, 178: 0.156219 }[r]) > 1e-9) throw new Error('Base!V' + r + ' is not the 2025-diet value');
const setMix = mix => { for (const r of [175, 176, 177, 178]) ev.hf.setCellContents({ sheet: ev.bid, row: ROW[r], col: COL }, [[mix[r]]]); };
const zones = Object.values(regions).filter(z => z.kind === 'nation' || z.kind === 'state').sort((a, b) => a.id - b.id);
const cap = (z, p, me, rm) => { const s = z.presets[p]; return ev.evaluate(z, { ...z.land, ...s, ...(p === 'short' ? { meategg: me, redmeat: rm } : {}), population: z.population }).capacity; };
const run = (me, rm, mix) => { setMix(mix); const o = {}; for (const p of PRESETS) for (const z of zones) o[p + '|' + z.id] = cap(z, p, me, rm); return o; };
const off = run(W.off.meategg, W.off.redmeat, W.off.mix);
const released = run(0.12, 0.578, { 175: 0.595284, 176: 0.231357, 177: 0.01714, 178: 0.156219 });
const rows = [['window', 'kind', 'first_year', 'last_year', 'rounding', 'preset', 'zone', 'name', 'meat_eggs_share_of_food', 'red_meat_share_of_meat', 'beef_share_of_red_meat', 'capacity', 'capacity_with_2011_diet_inputs', 'layer_effect', 'effect_relative_to_released_effect', 'capacity_ratio_to_released_2025_fixed',
  'fao_ratio_meat_eggs_share', 'fao_ratio_red_share', 'fao_ratio_beef_kg', 'fao_beef_kg_per_person', 'fao_poultry_kg_per_person']];
const emit = (name, kind, y0, y1, rounding, me, rm, mix, inp) => { const c = run(me, rm, mix);
  for (const p of PRESETS) for (const z of zones) { const k = p + '|' + z.id, eff = c[k] - off[k], effRel = released[k] - off[k];
    rows.push([name, kind, y0, y1, rounding, p, z.id, z.name, me, rm, mix[175].toFixed(4), Math.round(c[k]), Math.round(off[k]), Math.round(eff), effRel ? (eff / effRel).toFixed(4) : '', (c[k] / released[k]).toFixed(4),
      inp.me_ratio.toFixed(4), inp.red_ratio.toFixed(4), inp.beef_ratio.toFixed(4), inp.beef_kg.toFixed(2), inp.poultry_kg.toFixed(2)]); } };
for (const w of W.windows) { emit(w.name, w.kind, w.years[0], w.years[1], 'release rounding', w.inputs.meategg, w.inputs.redmeat, w.inputs.mix, w.inputs);
  emit(w.name, w.kind, w.years[0], w.years[1], 'unrounded', +w.inputs.meategg_raw.toFixed(6), +w.inputs.redmeat_raw.toFixed(6), w.inputs.mix_raw, w.inputs); }
const q = v => /[",]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : v;
fs.writeFileSync(out, rows.map(r => r.map(q).join(',')).join('\n') + '\n'); console.log('wrote', out, rows.length - 1, 'rows');
