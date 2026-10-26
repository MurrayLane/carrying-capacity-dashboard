// Build the data files the site loads, from the editable sources:
//   ../model/model.xls          the workbook (the method)
//   ../data/2011/*.csv          the 2011 zone defaults (land, population, both presets)
// Writes public/data/model.json and public/data/regions.json.
//
// The workbook keeps one column of yields per region (Yield!H:BO) and looks the chosen region up by number
// (Yield!F). That caps the model at 60 regions. Here the lookup column becomes plain cells that the evaluator
// fills from regions.json, so any region, however defined, can be evaluated. Nothing else in the workbook refers
// to the regional block, which the acceptance test against the 2011 baseline confirms.
import XLSX from 'xlsx';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..', '..');
const outDir = path.resolve(here, '..', 'public', 'data');
fs.mkdirSync(outDir, { recursive: true });
const sha = f => crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');

// ---- model.json -------------------------------------------------------------------------------------------------
const modelPath = path.join(root, 'model', 'model.xls');
const wb = XLSX.readFile(modelPath, { cellFormula: true });
const horizontal = r => { const m = r.match(/\$?[A-Z]+\$?(\d+):\$?[A-Z]+\$?(\d+)/); return m && m[1] === m[2]; };
// HyperFormula has no vector LOOKUP: the workbook's LOOKUP(x, keys, values) becomes INDEX/MATCH
const rewrite = f => f.replace(/LOOKUP\(([^,()]+),([^,()]+),([^,()]+)\)/g, (m, x, k, v) =>
  horizontal(v) ? `INDEX(${v},1,MATCH(${x},${k},1))` : `INDEX(${v},MATCH(${x},${k},1),1)`);

const YIELD_FIRST_REGION_COL = 7, YIELD_LAST_REGION_COL = 66;          // H..BO, zero-based
const YIELD_LOOKUP_COL = 5;                                            // F
const sheets = {}; const yieldRows = [];
for (const name of wb.SheetNames) {
  if (name === 'log') continue;
  const ws = wb.Sheets[name]; const rg = XLSX.utils.decode_range(ws['!ref']); const cells = {};
  for (const addr of Object.keys(ws)) {
    if (addr[0] === '!') continue;
    const { r, c } = XLSX.utils.decode_cell(addr); const cell = ws[addr];
    if (name === 'Yield' && c >= YIELD_FIRST_REGION_COL && c <= YIELD_LAST_REGION_COL) continue;     // regional block leaves the workbook
    let v;
    if (cell.f) {
      v = '=' + rewrite(cell.f);
      if (name === 'Yield' && c === YIELD_LOOKUP_COL && /LOOKUP\(F\$2,H\$2:BO\$2/.test(cell.f)) { v = r === 0 ? '' : 0; if (r >= 3) yieldRows.push(r + 1); }
    } else if (cell.t === 'n' || cell.t === 's' || cell.t === 'b') v = cell.v; else continue;
    cells[`${r}:${c}`] = v;
  }
  sheets[name] = { rows: rg.e.r + 1, cols: rg.e.c + 1, cells };
}
// rows of Base that carry per-diet nutrient totals, summed for the diet panel
const base = wb.Sheets['Base']; const dietRows = [];
for (let r = 5; r < 349; r++) { const a = base[XLSX.utils.encode_cell({ r, c: 29 })]; if (a && a.f) dietRows.push(r); }
fs.writeFileSync(path.join(outDir, 'model.json'), JSON.stringify({
  version: 1, source: { file: 'model/model.xls', sha256: sha(modelPath) },
  meta: { yieldRows, dietRows }, sheets,
}));

// ---- regions.json -----------------------------------------------------------------------------------------------
const parseCsv = file => { const L = fs.readFileSync(file, 'utf8').trim().split(/\r?\n/); const h = L[0].split(',');
  return L.slice(1).map(l => { const c = l.split(','); const o = {}; h.forEach((k, i) => o[k] = isNaN(+c[i]) || c[i] === '' ? c[i] : +c[i]); return o; }); };
const shortCsv = parseCsv(path.join(root, 'data/2011/default-inputs-short-term.csv'));
const longCsv = parseCsv(path.join(root, 'data/2011/default-inputs-long-term.csv'));
const PARAMS = ['resilience', 'food', 'meategg', 'redmeat', 'activity', 'recycling', 'losses', 'organic', 'irrigation', 'fuel', 'biofuel', 'fibre', 'fibreNat', 'fibreWool', 'timber', 'infrastr2', 'nature2'];
// the 2011 zone hierarchy (thesis Table 2): Australia, seven state groups, 52 NRM regions
const STATE_IDS = [2, 15, 26, 40, 49, 56, 60];
const CHILDREN = { 1: STATE_IDS, 2: range(3, 14), 15: range(16, 25), 26: range(27, 39), 40: range(41, 48), 49: range(50, 55), 56: range(57, 59), 60: [] };
function range(a, b) { return Array.from({ length: b - a + 1 }, (_, i) => a + i); }
const parentOf = id => id === 1 ? null : STATE_IDS.includes(id) ? 1 : STATE_IDS.filter(s => s < id).pop();
const yws = wb.Sheets['Yield'];
const regions = {};
for (const d of shortCsv) {
  const id = d.regionId; const lg = longCsv.find(x => x.regionId === id);
  if (d.population !== lg.population || d.cropping !== lg.cropping) throw new Error(`short and long defaults disagree on land or population for region ${id}`);
  const yieldVec = yieldRows.map(r => { const c = yws[XLSX.utils.encode_cell({ r: r - 1, c: YIELD_FIRST_REGION_COL + id - 1 })]; return c && typeof c.v === 'number' ? c.v : 0; });
  regions[id] = {
    id, name: d.regionName, parent: parentOf(id), kind: id === 1 ? 'nation' : STATE_IDS.includes(id) ? 'state' : 'region',
    children: CHILDREN[id] ?? [], climateZone: id,
    land: { cropping: d.cropping, pasture: d.pasture, nonAg: d.nonAg, infrastr1: d.infrastr1, nature1: d.nature1 }, population: d.population,
    presets: { short: Object.fromEntries(PARAMS.map(k => [k, d[k]])), long: Object.fromEntries(PARAMS.map(k => [k, lg[k]])) },
    yield: yieldVec,
  };
}
// "the region as the sum of its parts": the leaf regions under each zone (NT is both a state and a region)
const leaves = id => CHILDREN[id]?.length ? CHILDREN[id].flatMap(leaves) : [id];
for (const id of Object.keys(regions)) { const l = leaves(+id); regions[id].parts = l.length > 1 || l[0] !== +id ? l : []; }
fs.writeFileSync(path.join(outDir, 'regions.json'), JSON.stringify({
  version: 1, vintage: '2011', layer: '2011 zones',
  source: { files: ['data/2011/default-inputs-short-term.csv', 'data/2011/default-inputs-long-term.csv'], sha256: [sha(path.join(root, 'data/2011/default-inputs-short-term.csv')), sha(path.join(root, 'data/2011/default-inputs-long-term.csv'))] },
  yieldRows, regions,
}));
console.log(`model.json: ${(fs.statSync(path.join(outDir, 'model.json')).size / 1024).toFixed(0)} KB, ${Object.keys(sheets).length} sheets, ${yieldRows.length} injected yield rows, ${dietRows.length} diet rows`);
console.log(`regions.json: ${(fs.statSync(path.join(outDir, 'regions.json')).size / 1024).toFixed(0)} KB, ${Object.keys(regions).length} zones`);
