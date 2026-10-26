// Records the SHA-256 of every input file in a release's release.json.
// Usage: node scripts/lock-release.mjs <id>          refuses to change hashes that are already recorded
//        node scripts/lock-release.mjs <id> --force  only for a release that has never been published
import fs from 'node:fs';
import path from 'node:path';
import { root, sha, rawRelease, resolveRelease, inputFiles } from './releases.mjs';
const [id, flag] = process.argv.slice(2); if (!id) throw new Error('usage: lock-release.mjs <id> [--force]');
const raw = rawRelease(id), rel = resolveRelease(id);
const inputs = Object.fromEntries(inputFiles(rel).map(f => [f, sha(f)]));
if (raw.inputs && JSON.stringify(raw.inputs) !== JSON.stringify(inputs) && flag !== '--force') {
  console.error(`release ${id} is already locked and its inputs have changed:`); for (const f of Object.keys(inputs)) if (raw.inputs[f] !== inputs[f]) console.error('  ' + f);
  console.error('A published release is never edited. Create a new release instead.'); process.exit(1);
}
const file = path.join(root, 'releases', id, 'release.json');
const text = JSON.stringify({ ...raw, inputs }, null, 2) + '\n';
fs.writeFileSync(file, text); console.log(`locked ${id}: ${Object.keys(inputs).length} inputs`);
