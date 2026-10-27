// Build the data files the site loads, one folder per release (releases/<id>/release.json):
//   public/data/releases.json          the list of releases and the default
//   public/data/<id>/model.json        the workbook (the method), with any cell overrides of that release
//   public/data/<id>/regions.json      the zones: land, population, defaults for both presets, yield vectors (the workbook's block, or a release's yieldMatrix)
// Sources: model/model.xls and the CSV files each release names.
//
// The workbook keeps one column of yields per region (Yield!H:BO) and looks the chosen region up by number
// (Yield!F). That caps the model at 60 regions. Here the lookup column becomes plain cells that the evaluator
// fills from regions.json, so any region, however defined, can be evaluated. Nothing else in the workbook refers
// to the regional block, which the acceptance test against the 2011 baseline confirms.
import XLSX from 'xlsx';
import fs from 'node:fs';
import path from 'node:path';
import { root, sha, index, resolveRelease, inputFiles, lockDrift } from './releases.mjs';

const outRoot = path.resolve(root, 'web', 'public', 'data');
fs.rmSync(outRoot, { recursive: true, force: true });
fs.mkdirSync(outRoot, { recursive: true });

// ---- the workbook, parsed once per file --------------------------------------------------------------------------
const horizontal = r => { const m = r.match(/\$?[A-Z]+\$?(\d+):\$?[A-Z]+\$?(\d+)/); return m && m[1] === m[2]; };
// HyperFormula has no vector LOOKUP: the workbook's LOOKUP(x, keys, values) becomes INDEX/MATCH
const rewrite = f => f.replace(/LOOKUP\(([^,()]+),([^,()]+),([^,()]+)\)/g, (m, x, k, v) =>
  horizontal(v) ? `INDEX(${v},1,MATCH(${x},${k},1))` : `INDEX(${v},MATCH(${x},${k},1),1)`);
const YIELD_FIRST_REGION_COL = 7, YIELD_LAST_REGION_COL = 66;          // H..BO, zero-based
const YIELD_LOOKUP_COL = 5;                                            // F
const workbooks = new Map();
function loadWorkbook(file) {
  if (workbooks.has(file)) return workbooks.get(file);
  const wb = XLSX.readFile(path.join(root, file), { cellFormula: true });
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
  const entry = { wb, sheets, yieldRows, dietRows }; workbooks.set(file, entry); return entry;
}

// ---- the 2011 zone hierarchy (thesis Table 2): Australia, seven state groups, 52 NRM regions ------------------------
const parseCsv = file => { const L = fs.readFileSync(path.join(root, file), 'utf8').trim().split(/\r?\n/); const h = L[0].split(',');
  return L.slice(1).map(l => { const c = l.split(','); const o = {}; h.forEach((k, i) => o[k] = isNaN(+c[i]) || c[i] === '' ? c[i] : +c[i]); return o; }); };
const PARAMS = ['resilience', 'food', 'meategg', 'redmeat', 'activity', 'recycling', 'losses', 'organic', 'irrigation', 'fuel', 'biofuel', 'fibre', 'fibreNat', 'fibreWool', 'timber', 'infrastr2', 'nature2'];
const STATE_IDS = [2, 15, 26, 40, 49, 56, 60];
function range(a, b) { return Array.from({ length: b - a + 1 }, (_, i) => a + i); }
const CHILDREN = { 1: STATE_IDS, 2: range(3, 14), 15: range(16, 25), 26: range(27, 39), 40: range(41, 48), 49: range(50, 55), 56: range(57, 59), 60: [] };
const parentOf = id => id === 1 ? null : STATE_IDS.includes(id) ? 1 : STATE_IDS.filter(s => s < id).pop();
const leaves = id => CHILDREN[id]?.length ? CHILDREN[id].flatMap(leaves) : [id];

function buildRegions(rel, { wb, yieldRows }) {
  const shortCsv = parseCsv(rel.defaults.short), longCsv = parseCsv(rel.defaults.long);
  const yws = wb.Sheets['Yield']; const regions = {};
  for (const d of shortCsv) {
    const id = d.regionId; const lg = longCsv.find(x => x.regionId === id);
    if (d.population !== lg.population || d.cropping !== lg.cropping) throw new Error(`${rel.id}: short and long defaults disagree on land or population for region ${id}`);
    const yieldVec = yieldRows.map(r => { const c = yws[XLSX.utils.encode_cell({ r: r - 1, c: YIELD_FIRST_REGION_COL + id - 1 })]; return c && typeof c.v === 'number' ? c.v : 0; });
    regions[id] = {
      id, name: d.regionName, parent: parentOf(id), kind: id === 1 ? 'nation' : STATE_IDS.includes(id) ? 'state' : 'region',
      children: CHILDREN[id] ?? [], climateZone: id,
      land: { cropping: d.cropping, pasture: d.pasture, nonAg: d.nonAg, infrastr1: d.infrastr1, nature1: d.nature1 }, population: d.population,
      presets: { short: Object.fromEntries(PARAMS.map(k => [k, d[k]])), long: Object.fromEntries(PARAMS.map(k => [k, lg[k]])) },
      yield: yieldVec,
    };
  }
  for (const id of Object.keys(regions)) { const l = leaves(+id); regions[id].parts = l.length > 1 || l[0] !== +id ? l : []; }
  // the release's own changes to the defaults and to the yield vectors
  for (const p of rel.patches ?? []) for (const r of Object.values(regions)) {
    if (!(p.field in r.presets[p.preset])) throw new Error(`${rel.id}: patch names unknown field ${p.field}`);
    r.presets[p.preset][p.field] = p.value;
  }
  // a whole matrix of yields (one column per row of the Yield sheet, one line per zone), replacing the workbook's regional block for those rows
  if (rel.yieldMatrix) {
    const lines = parseCsv(rel.yieldMatrix.file);
    for (const x of lines) for (const [h, v] of Object.entries(x)) {
      if (h === 'regionId') continue;
      const k = yieldRows.indexOf(+h); if (k < 0) throw new Error(`${rel.id}: yield matrix column ${h} is not an injected row`);
      if (!regions[x.regionId]) throw new Error(`${rel.id}: yield matrix names unknown zone ${x.regionId}`);
      regions[x.regionId].yield[k] = v;
    }
  }
  for (const o of rel.yieldOverrides ?? []) {
    const k = yieldRows.indexOf(o.row); if (k < 0) throw new Error(`${rel.id}: yield override row ${o.row} is not an injected row`);
    for (const x of parseCsv(o.file)) regions[x.regionId].yield[k] = x[o.column];
  }
  return regions;
}

// ---- one folder per release ----------------------------------------------------------------------------------------
const idx = index(); const listing = [];
for (const id of idx.order) {
  const rel = resolveRelease(id);
  if (rel.status === 'frozen') { const bad = lockDrift(id); if (bad.length) throw new Error(`release ${id} is frozen but its inputs changed: ${bad.join(', ')}. Create a new release instead of editing this one.`); }
  const wbk = loadWorkbook(rel.model.file);
  const sheets = JSON.parse(JSON.stringify(wbk.sheets));
  for (const [sheet, cellsToSet] of Object.entries(rel.model.cellOverrides ?? {})) for (const [addr, v] of Object.entries(cellsToSet)) {
    const { r, c } = XLSX.utils.decode_cell(addr); sheets[sheet].cells[`${r}:${c}`] = v;
  }
  const dir = path.join(outRoot, id); fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'model.json'), JSON.stringify({
    version: 1, release: id, source: { file: rel.model.file, sha256: sha(rel.model.file), cellOverrides: rel.model.cellOverrides ?? null },
    meta: { yieldRows: wbk.yieldRows, dietRows: wbk.dietRows }, sheets,
  }));
  const regions = buildRegions(rel, wbk);
  fs.writeFileSync(path.join(dir, 'regions.json'), JSON.stringify({
    version: 1, release: id, label: rel.label, vintage: rel.vintage, layer: rel.layer,
    source: { files: inputFiles(rel), sha256: inputFiles(rel).map(sha) }, yieldRows: wbk.yieldRows, regions,
  }));
  listing.push({ id, label: rel.label, status: rel.status, parent: rel.parent ?? null, description: rel.description, layer: rel.layer, vintage: rel.vintage,
    patches: (rel.patches ?? []).map(({ preset, field, value, reason }) => ({ preset, field, value, reason })), errata: rel.errata ?? [] });
  console.log(`${id}: model.json ${(fs.statSync(path.join(dir, 'model.json')).size / 1024).toFixed(0)} KB, regions.json ${(fs.statSync(path.join(dir, 'regions.json')).size / 1024).toFixed(0)} KB, ${Object.keys(regions).length} zones, ${wbk.yieldRows.length} injected yield rows`);
}
fs.writeFileSync(path.join(outRoot, 'releases.json'), JSON.stringify({ default: idx.default, releases: listing }));
