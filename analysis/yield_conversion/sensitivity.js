// How much does the irrigation uplift matter at default settings?
// Capacity at each zone's default irrigation share, against capacity with the irrigation parameter set to zero.
// Setting it to zero removes the uplift that the thesis rule says restores the ABS average yield.
// If instead the stored yields already included irrigation, the uplift would be a double count of the same size.
const XLSX = require('xlsx'); const { HyperFormula } = require('hyperformula'); const fs = require('fs');
const S = process.argv[2], R = process.argv[3];
const wb = XLSX.readFile(S, { cellFormula: true });
const horizontal = rng => { const m = rng.match(/\$?[A-Z]+\$?(\d+):\$?[A-Z]+\$?(\d+)/); return m && m[1] === m[2]; };
const rewrite = f => f.replace(/LOOKUP\(([^,()]+),([^,()]+),([^,()]+)\)/g, (m, x, k, v) => horizontal(v) ? `INDEX(${v},1,MATCH(${x},${k},1))` : `INDEX(${v},MATCH(${x},${k},1),1)`);
const sheets = {};
for (const name of wb.SheetNames) { const ws = wb.Sheets[name]; const rg = XLSX.utils.decode_range(ws['!ref']); const rows = [];
  for (let r = 0; r <= rg.e.r; r++) { const row = []; for (let c = 0; c <= rg.e.c; c++) { const cell = ws[XLSX.utils.encode_cell({ r, c })];
    row.push(!cell ? null : cell.f ? '=' + rewrite(cell.f) : (cell.t === 'n' || cell.t === 's' || cell.t === 'b') ? cell.v : null); } rows.push(row); } sheets[name] = rows; }
const hf = HyperFormula.buildFromSheets(sheets, { licenseKey: 'gpl-v3' }); const sid = hf.getSheetId('Settings');
const order = ['regionId','cropping','pasture','nonAg','infrastr1','nature1','resilience','food','meategg','redmeat','activity','recycling','losses','organic','irrigation','fuel','biofuel','fibre','fibreNat','fibreWool','timber','infrastr2','nature2','population'];
const parse = f => { const L = fs.readFileSync(R + f, 'utf8').trim().split(/\r?\n/); const h = L[0].split(','); return L.slice(1).map(l => { const c = l.split(','); const o = {}; h.forEach((k, i) => o[k] = isNaN(+c[i]) ? c[i] : +c[i]); return o; }); };
const run = d => { hf.batch(() => order.forEach((k, i) => hf.setCellContents({ sheet: sid, row: i + 1, col: 1 }, [[d[k]]]))); const v = hf.getCellValue({ sheet: sid, row: 75, col: 1 }); return typeof v === 'number' ? v : NaN; };
const out = [['preset', 'region_id', 'region', 'irrigation_share', 'capacity_default', 'capacity_irrigation_zero', 'change_pct']];
for (const [file, label] of [['default-inputs-short-term.csv', 'short'], ['default-inputs-long-term.csv', 'long']]) for (const d of parse(file)) {
  const a = run(d), b = run({ ...d, irrigation: 0 }); out.push([label, d.regionId, d.regionName, d.irrigation, a.toFixed(0), b.toFixed(0), ((b - a) / a * 100).toFixed(2)]); }
fs.writeFileSync(process.argv[4], out.map(r => r.join(',')).join('\n') + '\n'); console.log('wrote', out.length - 1, 'cases');
