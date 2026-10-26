// Writes baseline/release_2011-corrected.csv: the capacity of every default case, so later changes to the evaluator
// or the build cannot move this release's results unnoticed. Run only when the release is first locked.
import fs from 'node:fs';
import path from 'node:path';
import { root } from './releases.mjs';
import { Evaluator } from '../src/model/evaluator.js';
const id = '2011-corrected', dir = path.join(root, 'web/public/data', id);
const model = JSON.parse(fs.readFileSync(path.join(dir, 'model.json'))), { regions } = JSON.parse(fs.readFileSync(path.join(dir, 'regions.json')));
const ev = new Evaluator(model); const out = ['preset,regionId,capacity'];
for (const preset of ['short', 'long']) for (const r of Object.values(regions)) out.push(`${preset},${r.id},${ev.evaluate(r, { ...r.land, ...r.presets[preset], population: r.population }).capacity}`);
fs.writeFileSync(path.join(root, 'baseline', 'release_2011-corrected.csv'), out.join('\n') + '\n'); console.log('wrote', out.length - 1, 'cases');
