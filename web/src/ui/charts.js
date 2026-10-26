// Charts as plain SVG, built to the dataviz method: thin marks, a 2px surface gap between touching fills, hairline axes,
// a legend for two or more series, selective direct labels, a tooltip on hover and keyboard focus, and a table twin.
// Colours come from CSS custom properties (see styles.css), so light and dark swap in one place.
import { h, fmt0, fmt1 } from '../lib.js';

const SVGNS = 'http://www.w3.org/2000/svg';
const s = (tag, attrs = {}, ...kids) => {
  const el = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v == null) continue;
    if (k === 'fill' && (tag === 'text' || String(v).startsWith('var('))) el.style.fill = v;   // style beats the stylesheet; custom properties need it
    else el.setAttribute(k, v);
  }
  for (const k of kids.flat()) if (k != null) el.append(k.nodeType ? k : document.createTextNode(String(k)));
  return el;
};

// ---- tooltip: one shared element; values lead, names follow; text only, never markup --------------------------------
let tip;
function ensureTip() {
  if (!tip) { tip = h('div', { class: 'tt', role: 'tooltip', hidden: true }); document.body.append(tip); }
  return tip;
}
function showTip(x, y, rows) {
  const t = ensureTip(); t.replaceChildren(...rows.map(r => h('div', { class: 'tt-row' }, r.color ? h('i', { style: `background:${r.color}` }) : null, h('strong', {}, r.value), h('span', {}, r.name))));
  t.hidden = false;
  const w = t.offsetWidth, hgt = t.offsetHeight; const pad = 12;
  t.style.left = `${Math.min(Math.max(8, x + pad), window.innerWidth - w - 8)}px`;
  t.style.top = `${Math.min(Math.max(8, y - hgt - pad), window.innerHeight - hgt - 8)}px`;
}
const hideTip = () => { if (tip) tip.hidden = true; };
function bindTip(el, rows) {
  el.addEventListener('pointermove', e => showTip(e.clientX, e.clientY, rows()));
  el.addEventListener('pointerleave', hideTip);
  el.addEventListener('focus', () => { const r = el.getBoundingClientRect(); showTip(r.left + r.width / 2, r.top, rows()); });
  el.addEventListener('blur', hideTip);
}

// ---- table twin ------------------------------------------------------------------------------------------------------
export function table(headers, rows, caption) {
  return h('table', { class: 'data' }, caption ? h('caption', { class: 'sr' }, caption) : null,
    h('thead', {}, h('tr', {}, headers.map((x, i) => h('th', { scope: 'col', class: i ? 'num' : '' }, x)))),
    h('tbody', {}, rows.map(r => h('tr', {}, r.map((c, i) => (i ? h('td', { class: 'num' }, c) : h('th', { scope: 'row' }, c)))))));
}
/** A figure with a title, the chart, and a "table" toggle that swaps in the same numbers as a table. */
export function figure({ title, note, chart, tableEl, wide }) {
  const tbtn = h('button', { type: 'button', class: 'link', 'aria-pressed': 'false' }, 'Table');
  const box = h('div', { class: 'fig-body' }, chart);
  tbtn.addEventListener('click', () => {
    const on = tbtn.getAttribute('aria-pressed') !== 'true'; tbtn.setAttribute('aria-pressed', on);
    tbtn.textContent = on ? 'Chart' : 'Table'; box.replaceChildren(on ? tableEl : chart);
  });
  return h('figure', { class: 'fig' + (wide ? ' wide' : '') }, h('figcaption', {}, h('span', { class: 'fig-title' }, title), tbtn), note ? h('p', { class: 'fig-note' }, note) : null, box);
}
export function legend(items) {
  return h('ul', { class: 'legend' }, items.map(i => h('li', {}, h('i', { style: `background:${i.color}` }), h('span', {}, i.label), i.value ? h('b', {}, i.value) : null)));
}

// ---- stacked bar: part to whole, up to about six parts ---------------------------------------------------------------
export function stackedBar({ segments, total, unit = '' }) {
  const W = 640, H = 40, gap = 2, rows = segments.filter(x => x.value > 0);
  const sum = rows.reduce((a, x) => a + x.value, 0) || 1;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'svg', role: 'img', 'aria-label': 'Land use as shares of all land' });
  let x = 0;
  rows.forEach((seg, i) => {
    const w = Math.max(0, seg.value / sum * W - (i < rows.length - 1 ? gap : 0));
    const share = seg.value / sum * 100;
    const g = s('g', { tabindex: 0, class: 'mark', 'aria-label': `${seg.label}: ${fmt0(seg.value)} ${unit}, ${fmt1(share)} percent` },
      s('rect', { x, y: 4, width: w, height: 32, rx: 4, fill: seg.color }),
      // a label goes inside only when it fits with room either side; otherwise legend and tooltip carry it
      w > 54 ? s('text', { x: x + w / 2, y: 24, 'text-anchor': 'middle', class: 'in-bar', fill: seg.ink || '#ffffff' }, `${fmt0(share)}%`) : null);
    bindTip(g, () => [{ value: `${fmt1(share)}%`, name: `${seg.label}, ${fmt0(seg.value)} ${unit}`, color: seg.color }]);
    svg.append(g); x += w + gap;
  });
  return h('div', {}, svg, legend(rows.map(sg => ({ color: sg.color, label: sg.label, value: `${fmt1(sg.value / sum * 100)}%` }))));
}

// ---- horizontal bars: one series; the title names it, so there is no legend box -------------------------------------
export function hBars({ rows, format = fmt0, max, color = 'var(--series-1)', labelWidth = 150, ref, labelWhich }) {
  const W = 640, rowH = 28, barH = 16, top = 4, bottom = ref ? 22 : 6, left = labelWidth;
  const H = top + rows.length * rowH + bottom; const m = max ?? Math.max(...rows.map(r => r.value), 1);
  const plotW = W - left - 100; const xOf = v => left + Math.min(v, m) / m * plotW;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'svg', role: 'img' });
  svg.append(s('line', { x1: left, x2: left, y1: top, y2: top + rows.length * rowH, class: 'axis' }));
  if (ref) svg.append(s('line', { x1: xOf(ref.value), x2: xOf(ref.value), y1: top, y2: top + rows.length * rowH, class: 'refline' }), s('text', { x: xOf(ref.value), y: H - 6, 'text-anchor': 'middle', class: 'muted' }, ref.label));
  rows.forEach((r, i) => {
    const y = top + i * rowH, w = Math.max(r.value > 0 ? 2 : 0, xOf(r.value) - left);
    const show = labelWhich ? labelWhich(r, i) : true;
    const g = s('g', { tabindex: 0, class: 'mark', 'aria-label': `${r.label}: ${r.text ?? format(r.value)}` },
      s('rect', { x: 0, y, width: W, height: rowH, fill: 'transparent' }),                       // a hit area bigger than the bar
      s('text', { x: left - 8, y: y + rowH / 2 + 4, 'text-anchor': 'end', class: r.emphasis ? 'row-label strong' : 'row-label' }, r.label),
      s('rect', { x: left, y: y + (rowH - barH) / 2, width: w, height: barH, rx: 4, fill: r.color || color, opacity: r.dim ? 0.55 : 1 }),
      show ? s('text', { x: left + w + 6, y: y + rowH / 2 + 4, class: 'tip-label' }, r.text ?? format(r.value)) : null);
    bindTip(g, () => [{ value: r.text ?? format(r.value), name: r.label, color: r.color || color }, ...(r.extra ? [{ value: r.extra, name: '' }] : [])]);
    if (r.onSelect) { g.style.cursor = 'pointer'; g.addEventListener('click', r.onSelect); g.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); r.onSelect(); } }); }
    svg.append(g);
  });
  return svg;
}

// ---- paired bars: two series per row (existing land, land used at capacity) ------------------------------------------
export function pairedBars({ rows, aName, bName, aColor, bColor, format = fmt0 }) {
  const W = 640, rowH = 40, barH = 12, top = 4, left = 130; const H = top + rows.length * rowH + 4;
  const m = Math.max(...rows.flatMap(r => [r.a, r.b]), 1); const plotW = W - left - 100; const xOf = v => left + v / m * plotW;
  const svg = s('svg', { viewBox: `0 0 ${W} ${H}`, class: 'svg', role: 'img' });
  svg.append(s('line', { x1: left, x2: left, y1: top, y2: top + rows.length * rowH, class: 'axis' }));
  rows.forEach((r, i) => {
    const y = top + i * rowH;
    const g = s('g', { tabindex: 0, class: 'mark', 'aria-label': `${r.label}: ${aName} ${format(r.a)}, ${bName} ${format(r.b)}` },
      s('rect', { x: 0, y, width: W, height: rowH, fill: 'transparent' }),
      s('text', { x: left - 8, y: y + rowH / 2 + 4, 'text-anchor': 'end', class: 'row-label' }, r.label),
      s('rect', { x: left, y: y + 6, width: Math.max(r.a > 0 ? 2 : 0, xOf(r.a) - left), height: barH, rx: 4, fill: aColor }),
      s('rect', { x: left, y: y + 6 + barH + 2, width: Math.max(r.b > 0 ? 2 : 0, xOf(r.b) - left), height: barH, rx: 4, fill: bColor }),
      s('text', { x: xOf(r.b) + 6, y: y + 6 + barH + 2 + barH - 2, class: 'tip-label' }, format(r.b)));
    bindTip(g, () => [{ value: format(r.a), name: `${r.label}, ${aName}`, color: aColor }, { value: format(r.b), name: `${r.label}, ${bName}`, color: bColor }]);
    svg.append(g);
  });
  return h('div', {}, svg, legend([{ color: aColor, label: aName }, { color: bColor, label: bName }]));
}
