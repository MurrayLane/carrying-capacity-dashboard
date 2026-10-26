// The dashboard: where (zone and land), what if (the 17 parameters), so what (results).
import { h, fmt0, fmt1, compact, debounce } from './lib.js';
import { PARAMS, GROUPS, LAND, LAND_KEYS } from './params.js';
import { decodeState, encodeState, inputsFor, releaseFromHash } from './state.js';
import { ModelClient } from './model/client.js';
import * as ch from './ui/charts.js';
import help from './data/help.json';

const FOODS = ['Red meat', 'White meat and eggs', 'Dairy', 'Cereals', 'Vegetables', 'Fruit', 'Legumes', 'Nuts and seeds', 'Oils', 'Sweeteners'];
const LAND_TYPES = ['Cropping', 'Pasture', 'Non-agricultural', 'Infrastructure', 'Nature reserve'];
const eq = (a, b) => Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(a), Math.abs(b));
const clean = v => Number(v.toPrecision(10));
const shown = (key, v) => Number((v * PARAMS[key].ratio).toFixed(3));

export async function mountDashboard(root) {
  const base = new URL(import.meta.env.BASE_URL, location.href).href;
  const manifest = await (await fetch(base + 'data/releases.json')).json();
  const releaseId = releaseFromHash(location.hash, manifest);
  const release = manifest.releases.find(r => r.id === releaseId);
  const data = await (await fetch(`${base}data/${releaseId}/regions.json`)).json();
  const regions = data.regions; const ids = Object.keys(regions).map(Number);
  const client = new ModelClient(base, releaseId);
  let st = decodeState(location.hash, ids, releaseId);
  history.replaceState(null, '', `#${encodeState(st)}`);      // pin the version into the link
  let runId = 0, compareMode = 'near', last = null;

  // ---- skeleton ----------------------------------------------------------------------------------------------------
  const el = {
    zone: h('select', { id: 'zone', 'aria-describedby': 'zone-note' }),
    release: h('select', { id: 'release', 'aria-describedby': 'release-note' }),
    releaseNote: h('p', { id: 'release-note', class: 'scope-note' }),
    note: h('p', { id: 'zone-note', class: 'scope-note' }),
    landBox: h('div'), presets: h('div', { class: 'presets' }),
    groups: h('div'), hero: h('div', { class: 'card hero', 'aria-live': 'polite' }), details: h('div'),
  };
  const dialog = h('dialog', { class: 'help-dialog' });
  dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close(); });
  function openHelp(title, html) {
    dialog.replaceChildren(h('div', { class: 'dlg-h' }, h('h2', {}, title), h('button', { class: 'btn', type: 'button', onclick: () => dialog.close() }, 'Close')), h('div', { class: 'dlg-b', html }));
    dialog.querySelectorAll('a').forEach(a => { a.target = '_blank'; a.rel = 'noopener noreferrer'; });
    dialog.showModal();
  }
  const helpBtn = (title, html) => html ? h('button', { class: 'help', type: 'button', 'aria-label': `About ${title}`, onclick: () => openHelp(title, html) }, '?') : null;

  // ---- zone select ---------------------------------------------------------------------------------------------------
  const opt = (id, text) => h('option', { value: id }, text);
  el.zone.append(opt(1, regions[1].name));
  for (const sid of regions[1].children) {
    const s = regions[sid];
    if (!s.children.length) el.zone.append(opt(sid, s.name));
    else el.zone.append(h('optgroup', { label: s.name }, opt(sid, `${s.name}, whole state`), s.children.map(c => opt(c, regions[c].name))));
  }
  for (const r of manifest.releases) el.release.append(h('option', { value: r.id, selected: r.id === releaseId }, r.label));
  el.releaseNote.append(release.status === 'frozen' ? 'A fixed version: its results never change. ' : 'The current version. ', h('a', { href: 'changes.html#versions' }, 'What the versions are'), '.');
  el.release.addEventListener('change', () => {
    const q = new URLSearchParams(location.hash.replace(/^#/, '')); q.set('r', el.release.value);
    history.pushState(null, '', `#${q}`); location.reload();      // zones, data and method all belong to the version, so start it afresh
  });
  el.zone.addEventListener('change', () => { st.zone = Number(el.zone.value); st.land = {}; st.population = null; commit(true); });

  // ---- land and population -------------------------------------------------------------------------------------------
  const landInputs = {};
  const landRow = (key, label, field, unit, readonly) => {
    const input = h('input', { type: 'text', id: `land-${key}`, inputmode: 'numeric', autocomplete: 'off', readonly });
    input.addEventListener('focus', () => { input.value = input.value.replace(/[^\d.]/g, ''); input.select(); });
    input.addEventListener('blur', () => syncInputs());
    landInputs[key] = input;
    if (!readonly) input.addEventListener('change', () => {
      const v = Number(input.value.replace(/[^\d.]/g, ''));
      if (!Number.isFinite(v) || input.value.replace(/[^\d.]/g, '') === '') { syncInputs(); return; }
      if (key === 'population') st.population = v; else st.land[key] = v;
      commit(false);
    });
    return h('div', { class: 'land-row' }, h('label', { for: `land-${key}` }, label, ' ', helpBtn(label, field && (help.areas[field] || {}).html)), input, h('span', { class: 'unit', html: unit }));
  };
  el.landBox.append(...LAND.map(l => landRow(l.key, l.label, l.field, 'km<sup>2</sup>')), landRow('total', 'Total land', null, 'km<sup>2</sup>', true), landRow('population', 'Current population', 'inputPopulation', ''));

  const btn = (text, fn, cls = 'btn') => h('button', { type: 'button', class: cls, onclick: fn }, text);
  el.presets.append(
    btn('Short-term defaults', () => { st.preset = 'short'; st.overrides = {}; st.land = {}; st.population = null; commit(true); }),
    btn('Long-term defaults', () => { st.preset = 'long'; st.overrides = {}; st.land = {}; st.population = null; commit(true); }),
    btn('Reset to zone defaults', () => { st.overrides = {}; st.land = {}; st.population = null; commit(true); }));

  // ---- parameters ----------------------------------------------------------------------------------------------------
  const controls = {};
  function makeParam(key) {
    const p = PARAMS[key]; const lo = p.min, hi = p.max; const pos = v => ((v - lo) / (hi - lo)) * 100;
    const range = h('input', { type: 'range', id: `r-${key}`, min: lo, max: hi, step: p.step, 'aria-label': `${p.caption}, ${p.desc}` });
    const num = h('input', { type: 'number', id: `n-${key}`, min: lo, max: hi, step: 'any', 'aria-label': `${p.caption} value` });
    const rail = h('div', { class: 'rail', 'aria-hidden': 'true' }, p.rules.map(([v]) => h('i', { style: `left:${pos(v)}%` })));
    const defMark = h('i', { class: 'def' }); rail.append(defMark);
    const err = h('div', { class: 'err', role: 'alert' });
    const foot = h('span'); const reset = h('button', { type: 'button', class: 'link', hidden: true }, 'Reset');
    const setValue = disp => { const v = clean(disp / p.ratio); const def = currentDefaults()[key]; if (eq(v, def)) delete st.overrides[key]; else st.overrides[key] = v; commit(false); };
    range.addEventListener('input', () => setValue(Number(range.value)));
    num.addEventListener('change', () => {
      const v = Number(num.value);
      if (num.value === '' || !Number.isFinite(v) || v < lo || v > hi) { err.textContent = `Enter a value from ${lo} to ${hi}.`; syncInputs(); return; }
      err.textContent = ''; setValue(v);
    });
    reset.addEventListener('click', () => { delete st.overrides[key]; commit(false); });
    const chips = h('div', { class: 'chips' }, p.rules.filter(r => r[1]).map(([v, label]) => h('button', { type: 'button', class: 'chip', title: `Set to ${v}${p.unit}`, onclick: () => setValue(v) }, `${label} ${v}${p.unit}`)));
    const gh = help.params[p.help];
    controls[key] = { range, num, defMark, foot, reset, pos, err };
    return h('div', { class: 'param', dataset: { key } },
      h('div', { class: 'param-head' }, h('label', { class: 'param-cap', for: `n-${key}` }, p.caption), helpBtn(p.caption, gh), h('span', { class: 'param-desc' }, p.desc)),
      h('div', { class: 'param-ctl' }, range, h('span', { class: 'numwrap' }, num, h('span', { class: 'unit' }, p.unit.trim()))),
      rail, chips, err, h('div', { class: 'param-foot' }, foot, reset));
  }
  const groupSummaries = {};
  GROUPS.forEach((g, i) => {
    const gh = help.groups[g.id]; const title = (gh.title || g.id).replace(/\s+$/, '');
    const count = h('span', { class: 'changed' });
    groupSummaries[g.id] = { count, params: g.params };
    el.groups.append(h('details', { class: 'group', open: i < 2 }, h('summary', {}, h('span', {}, title.charAt(0) + title.slice(1).toLowerCase(), ' ', count), helpBtn(title, gh.html)), g.params.map(makeParam)));
  });
  // a help button inside <summary> must not toggle the group
  el.groups.querySelectorAll('summary .help').forEach(b => b.addEventListener('click', e => e.stopPropagation()));

  // ---- state helpers --------------------------------------------------------------------------------------------------
  const region = () => regions[st.zone];
  const currentDefaults = () => region().presets[st.preset];
  function syncInputs() {
    const reg = region(), def = currentDefaults(); el.zone.value = String(st.zone);
    const parentName = reg.parent ? regions[reg.parent].name : null;
    el.note.textContent = reg.kind === 'nation' ? 'Australia as one unit. Choose a state or an NRM region for a smaller scale.' : reg.kind === 'state' ? `Whole of ${reg.name}${reg.children.length ? `, treated as one unit. It contains ${reg.children.length} regions.` : '.'}` : `${reg.name}, an NRM region of ${parentName}.`;
    for (const k of Object.keys(PARAMS)) {
      const c = controls[k], p = PARAMS[k]; const v = st.overrides[k] ?? def[k]; const d = shown(k, v), dd = shown(k, def[k]);
      c.range.value = d; if (document.activeElement !== c.num) c.num.value = d;
      c.defMark.style.left = `${c.pos(Math.min(Math.max(dd, p.min), p.max))}%`;
      const changed = k in st.overrides;
      c.foot.textContent = `Zone default ${dd}${p.unit.trim()}`;
      c.reset.hidden = !changed;
    }
    for (const g of Object.values(groupSummaries)) { const n = g.params.filter(k => k in st.overrides).length; g.count.textContent = n ? `${n} changed` : ''; }
    for (const k of LAND_KEYS) { if (document.activeElement !== landInputs[k]) landInputs[k].value = fmt0(st.land[k] ?? reg.land[k]); landInputs[k].classList.toggle('changed', k in st.land); }
    landInputs.total.value = fmt0(LAND_KEYS.reduce((a, k) => a + (st.land[k] ?? reg.land[k]), 0));
    if (document.activeElement !== landInputs.population) landInputs.population.value = fmt0(st.population ?? reg.population); landInputs.population.classList.toggle('changed', st.population != null);
  }
  function writeUrl(push) { const url = `#${encodeState(st)}`; if (push) history.pushState(null, '', url); else history.replaceState(null, '', url); }
  const run = debounce(() => evaluate(), 60);
  function commit(push) { writeUrl(push); syncInputs(); run(); }
  const resync = () => {
    let rid; try { rid = releaseFromHash(location.hash, manifest); } catch { rid = null; }
    if (rid !== releaseId) { location.reload(); return; }       // Back or a pasted link moved to another version
    st = decodeState(location.hash, ids, releaseId); syncInputs(); run();
  };
  addEventListener('popstate', resync); addEventListener('hashchange', resync);

  // ---- evaluation ------------------------------------------------------------------------------------------------------
  async function evaluate() {
    const my = ++runId; const reg = region(); const sel = inputsFor(reg, st, true);
    const landTyped = Object.keys(st.land).length > 0 || st.population != null;
    const parts = reg.parts.length && !landTyped ? reg.parts : [];
    el.details.classList.add('busy');
    const fail = e => { if (my === runId) el.hero.replaceChildren(h('p', { class: 'err' }, `The model could not run: ${e.message}`)); };
    // the selected zone first, so the headline answer never waits on the comparison charts
    let res;
    try { res = await client.evaluate([{ zone: st.zone, inputs: sel }], my); } catch (e) { fail(e); return; }
    if (my !== runId || !res) return;
    last = { reg, sel, main: res[0], parts: null, partsPending: parts.length > 0, landTyped };
    renderHero(); renderDetails(); el.details.classList.remove('busy');
    if (parts.length) {
      let pr; try { pr = await client.evaluate(parts.map(id => ({ zone: id, inputs: inputsFor(regions[id], st, false) })), my); } catch (e) { fail(e); return; }
      if (my !== runId || !pr) return;
      last.parts = pr.map((r, i) => ({ id: parts[i], r })); last.partsPending = false; renderDetails();
    }
    renderCompare(my);
  }

  function renderHero() {
    const { main, sel, reg } = last; const cap = main.capacity, pop = sel.population;
    const pct = cap > 0 ? pop / cap * 100 : Infinity; const over = pop > cap, at = Math.abs(pop - cap) < 0.5;
    el.hero.replaceChildren(
      h('div', { class: 'card-h' }, h('span', { class: 'step' }, `So what, ${reg.name}`), helpBtn('Population carrying capacity', help.sections.projections)),
      h('div', { class: 'hero-label' }, 'Population carrying capacity'),
      h('div', { class: 'hero-num' }, fmt0(cap)),
      h('div', { class: 'hero-line' }, `Current population ${fmt0(pop)} is `, h('b', {}, Number.isFinite(pct) ? `${fmt1(pct)}%` : 'unbounded'), ' of capacity. ',
        h('span', { class: `badge ${at ? '' : over ? 'over' : 'under'}` }, at ? 'At capacity' : over ? 'Over capacity' : 'Under capacity')),
      h('div', { class: 'hero-extra' }, h('div', { class: 'meter', role: 'img', 'aria-label': `Current population is ${Number.isFinite(pct) ? fmt1(pct) : 'more than 200'} percent of capacity` }, h('b', { style: `width:${Math.min(pct, 200) / 2}%` }), h('i')),
      h('div', { class: 'meter-scale' }, h('span', {}, '0%'), h('span', {}, '100%, capacity'), h('span', {}, '200%')),
      h('p', { class: 'vintage' }, 'Estimated from land for food, textiles, timber and liquid fuel. Version: ', release.label, '.')));
  }

  function renderDetails() {
    const { main: r, reg, parts, sel } = last; const kids = [];
    // scale: the zone as one unit against the sum of its regions, each self-sufficient (thesis 9.4)
    if (reg.parts.length) {
      if (parts) {
        const sum = parts.reduce((a, x) => a + x.r.capacity, 0); const ratio = r.capacity > 0 ? sum / r.capacity * 100 : 0;
        kids.push(h('section', { class: 'card' }, h('div', { class: 'card-h' }, h('h2', {}, 'Scale'), h('span', { class: 'step' }, 'Region alone or in parts')),
          h('div', { class: 'scale-tiles' }, h('div', { class: 'tile' }, h('div', { class: 'k' }, `${reg.name} as one unit`), h('div', { class: 'v' }, fmt0(r.capacity))),
            h('div', { class: 'tile' }, h('div', { class: 'k' }, `Sum of its ${parts.length} regions`), h('div', { class: 'v' }, fmt0(sum)))),
          h('p', { class: 'fig-note' }, `If each region had to be self-sufficient on its own, the total capacity would be ${fmt0(ratio)}% of the single-unit figure. Land that is spare in one region cannot make up a shortfall in another.`)));
      } else if (last.partsPending) kids.push(h('section', { class: 'card' }, h('div', { class: 'card-h' }, h('h2', {}, 'Scale')), h('p', { class: 'scope-note' }, 'Calculating the regions...')));
      else kids.push(h('section', { class: 'card' }, h('div', { class: 'card-h' }, h('h2', {}, 'Scale')), h('p', { class: 'scope-note' }, 'The comparison of one unit against its parts uses each region\'s own land and population, so it is hidden while land areas or population are edited.')));
    }
    // land use
    const seg = (label, value, color, ink) => ({ label, value, color, ink });
    const useSeg = [seg('Food', r.requirements[10][1], 'var(--series-1)'), seg('Fuel, textiles and timber', r.requirements[11][1] + r.requirements[12][1] + r.requirements[13][1], 'var(--series-2)'),
      seg('Infrastructure', r.requirements[14][1], 'var(--series-3)'), seg('Nature reserve', r.requirements[15][1], 'var(--series-4)', 'var(--seg-ink-4, #0b0b0b)'), seg('Excess land', r.excess[5][0], 'var(--other)')];
    const totalUse = useSeg.reduce((a, x) => a + x.value, 0);
    kids.push(h('section', { class: 'card' }, ch.figure({ title: 'Land requirements, by use', note: 'Share of all land in the zone at its carrying capacity. Excess land is land the chosen way of life does not need.',
      chart: ch.stackedBar({ segments: useSeg, unit: 'km²' }),
      tableEl: ch.table(['Use', 'km²', '% of land'], useSeg.map(x => [x.label, fmt0(x.value), fmt1(x.value / totalUse * 100)]), 'Land requirements by use') })));
    // reallocation
    const re = LAND_TYPES.map((label, i) => ({ label, a: r.existing[i], b: r.used[i] }));
    kids.push(h('section', { class: 'card' }, ch.figure({ title: 'Land by type: existing and used', note: 'Better land can do the work of poorer land, so some land changes use at capacity. Cropping land is the usual limit.',
      chart: ch.pairedBars({ rows: re, aName: 'Existing land', bName: 'Used at carrying capacity', aColor: 'var(--other)', bColor: 'var(--series-1)', format: v => `${fmt0(v)} km²` }),
      tableEl: ch.table(['Land type', 'Existing km²', 'Used km²'], re.map(x => [x.label, fmt0(x.a), fmt0(x.b)]), 'Existing and used land by type') })));
    // food mix
    const food = FOODS.map((label, i) => ({ label, value: r.requirements[i][1], extra: `${fmt1(r.requirements[i][3])}% of food land` })).sort((a, b) => b.value - a.value);
    const foodTotal = r.requirements[10][1];
    kids.push(h('section', { class: 'card' }, ch.figure({ title: 'Land for food, by food type', note: help.sections.foodUsage ? undefined : undefined,
      chart: ch.hBars({ rows: food, format: v => `${fmt0(v)} km²`, labelWhich: (_, i) => i < 3, labelWidth: 140 }),
      tableEl: ch.table(['Food type', 'km²', '% of food land'], food.map(x => [x.label, fmt0(x.value), fmt1(foodTotal ? x.value / foodTotal * 100 : 0)]), 'Land for food by type') })));
    // diet
    const d = r.diet;
    kids.push(h('section', { class: 'card' }, h('details', {}, h('summary', {}, h('b', {}, 'The diet behind this, per person per day')),
      ch.table(['Measure', 'Per person per day'], [['Energy', `${fmt0(d.energy)} kJ`], ['Protein', `${fmt0(d.protein)} g`], ['Fat', `${fmt0(d.fat)} g`], ['Carbohydrate', `${fmt0(d.carbs)} g`], ['of which sugar', `${fmt0(d.sugar)} g`], ['Dietary fibre', `${fmt0(d.fibre)} g`]], 'Diet components'),
      h('p', { class: 'fig-note' }, 'Computed from about 750 foods broken into raw commodities. The sedentary level gives about 7,400 kJ a day; moderate and high activity give more.'))));
    // compare container, actions, notes
    el.compare = h('section', { class: 'card' }); kids.push(el.compare);
    kids.push(h('section', { class: 'card' }, h('div', { class: 'actions' }, btn('Copy link to this scenario', copyLink), btn('Download results (CSV)', downloadCsv)),
      h('p', { class: 'vintage', style: 'margin-top:10px' }, `This is the "${release.label}" version: land use, population and yields from ABS sources for 2006 to 2010, with the model workbook as published with the thesis. A refreshed data set is planned; see `, h('a', { href: 'changes.html' }, 'Since 2011'), '.')));
    el.details.replaceChildren(...kids);
  }

  // ---- compare zones: every zone's own land, population and defaults, with the user's changed parameters ------------
  function compareSet() {
    const reg = region(); const stateOf = reg.kind === 'region' ? regions[reg.parent] : reg;
    if (compareMode === 'states') return { title: 'Australia and its states', ids: [1, ...regions[1].children] };
    if (compareMode === 'all') return { title: 'All regions', ids: ids.filter(i => regions[i].kind === 'region' || i === 60) };
    if (stateOf.kind === 'state' && stateOf.children.length) return { title: `Regions of ${stateOf.name}`, ids: stateOf.children };
    return { title: 'Australia and its states', ids: [1, ...regions[1].children] };
  }
  async function renderCompare(my) {
    if (!el.compare) return; const { title, ids: list } = compareSet();
    let res; try { res = await client.evaluate(list.map(id => ({ zone: id, inputs: inputsFor(regions[id], st, id === st.zone) })), my); } catch { return; }
    if (my !== runId || !res) return;
    const rows = list.map((id, i) => ({ id, name: regions[id].name, cap: res[i].capacity, pop: inputsFor(regions[id], st, id === st.zone).population }))
      .map(x => ({ ...x, pct: x.cap > 0 ? x.pop / x.cap * 100 : 300 })).sort((a, b) => b.pct - a.pct);
    const sel = (value, text) => h('option', { value }, text);
    const picker = h('select', { 'aria-label': 'Zones to compare' }, sel('near', 'Regions of this state'), sel('states', 'Australia and states'), sel('all', 'All regions'));
    picker.value = compareMode; picker.addEventListener('change', () => { compareMode = picker.value; renderCompare(runId); });
    const inList = rows.some(x => x.id === st.zone);
    const bars = rows.map((x, i) => ({ label: x.name, value: Math.min(x.pct, 300), text: `${fmt0(x.pct)}%`, emphasis: x.id === st.zone, dim: inList && x.id !== st.zone, color: 'var(--series-1)',
      extra: `${x.pct > 100 ? 'Over' : 'Under'} capacity: population ${fmt0(x.pop)}, capacity ${fmt0(x.cap)}`, onSelect: () => { st.zone = x.id; st.land = {}; st.population = null; commit(true); } }));
    const labelled = new Set([0, 1, 2, rows.length - 1, rows.findIndex(x => x.id === st.zone)]);
    el.compare.replaceChildren(ch.figure({ title: `Compare zones: ${title}`, note: 'Current population as a percentage of carrying capacity. Above 100% is over capacity. Each zone uses its own land, population and defaults, with the parameters you have changed. Select a bar to open that zone.',
      chart: h('div', {}, h('div', { class: 'compare-ctl' }, h('label', {}, 'Show '), picker),
        ch.hBars({ rows: bars, format: v => `${fmt0(v)}%`, max: 300, ref: { value: 100, label: 'Capacity' }, labelWidth: 150, labelWhich: (_, i) => labelled.has(i) })),
      tableEl: ch.table(['Zone', 'Capacity', 'Population', '% of capacity'], rows.map(x => [x.name, fmt0(x.cap), fmt0(x.pop), fmt1(x.pct)]), 'Zones compared'), wide: true }));
  }

  // ---- actions ----------------------------------------------------------------------------------------------------------
  function toast(msg) { const t = h('div', { class: 'toast', role: 'status' }, msg); document.body.append(t); setTimeout(() => t.remove(), 2200); }
  async function copyLink() { try { await navigator.clipboard.writeText(location.href); toast('Link copied'); } catch { prompt('Copy this link', location.href); } }
  function downloadCsv() {
    if (!last) return; const { reg, sel, main: r } = last; const q = v => `"${String(v).replaceAll('"', '""')}"`;
    const lines = [['# Carrying Capacity Dashboard'], [`# Version: ${release.label} (${releaseId}); ${data.layer}; land use, population and yields from ABS sources, 2006 to 2010`], [`# Scenario link: ${location.href}`], ['# Percent parameters are fractions in the model; shown here as displayed on the page'], [], ['item', 'value', 'unit']];
    lines.push(['zone', reg.name, ''], ['preset', st.preset, '']);
    LAND.forEach(l => lines.push([l.label, Math.round(sel[l.key]), 'km2'])); lines.push(['Current population', Math.round(sel.population), 'people']);
    Object.keys(PARAMS).forEach(k => lines.push([PARAMS[k].caption, shown(k, sel[k]), PARAMS[k].unit.trim() || 'level']));
    lines.push([], ['Carrying capacity population', Math.round(r.capacity), 'people'], ['Current as % of capacity', fmt1(sel.population / r.capacity * 100), '%']);
    ['Cropping', 'Pasture', 'Non-agricultural', 'Infrastructure', 'Nature reserve'].forEach((n, i) => lines.push([`${n}: existing`, Math.round(r.existing[i]), 'km2'], [`${n}: used at capacity`, Math.round(r.used[i]), 'km2']));
    lines.push(['Excess land', Math.round(r.excess[5][0]), 'km2']); FOODS.forEach((n, i) => lines.push([`Land for ${n.toLowerCase()}`, Math.round(r.requirements[i][1]), 'km2']));
    const blob = new Blob([lines.map(l => l.map(q).join(',')).join('\n')], { type: 'text/csv' });
    const a = h('a', { href: URL.createObjectURL(blob), download: `carrying-capacity-${reg.name.replace(/[^A-Za-z0-9]+/g, '-')}.csv` }); document.body.append(a); a.click(); a.remove();
  }

  // ---- assemble ----------------------------------------------------------------------------------------------------------
  root.replaceChildren(h('div', { class: 'layout' },
    h('section', { class: 'card col-where', 'aria-labelledby': 'where-h' }, h('div', { class: 'card-h' }, h('h2', { id: 'where-h' }, 'Where'), h('span', { class: 'step' }, 'Step 1')),
      h('label', { class: 'field' }, h('span', {}, 'Zone'), el.zone), el.note,
        h('label', { class: 'field' }, h('span', {}, 'Version'), el.release), el.releaseNote, h('h3', { style: 'margin:14px 0 8px' }, 'Land and people ', helpBtn('Land areas', help.sections.landAreas)), el.landBox, el.presets),
    h('section', { class: 'card col-whatif', 'aria-labelledby': 'what-h' }, h('div', { class: 'card-h' }, h('h2', { id: 'what-h' }, 'What if'), h('span', { class: 'step' }, 'Step 2')),
      h('p', { class: 'scope-note' }, 'Change how the population lives. The blue mark on each slider is the zone\'s default.'), el.groups),
    h('div', { class: 'col-right' }, h('div', { class: 'col-hero' }, el.hero), h('div', { class: 'col-details' }, el.details)), dialog));
  syncInputs(); writeUrl(false); evaluate();
}
