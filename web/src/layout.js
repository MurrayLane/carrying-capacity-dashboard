// Header, navigation, theme toggle and footer shared by every page.
import './styles.css';
import { h, store } from './lib.js';

export const REPO = 'https://github.com/MurrayLane/carrying-capacity-dashboard';
const PAGES = [['index.html', 'Dashboard'], ['methods.html', 'Methods'], ['changes.html', 'Since 2011'], ['about.html', 'About']];

function applyTheme(t) { if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t); else document.documentElement.removeAttribute('data-theme'); }
const isDark = () => { const t = document.documentElement.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; };

export function mountChrome(current) {
  applyTheme(store('ccd-theme'));
  const toggle = h('button', { class: 'btn', type: 'button' }, '');
  const label = () => { toggle.textContent = isDark() ? 'Light theme' : 'Dark theme'; };
  toggle.addEventListener('click', () => { const next = isDark() ? 'light' : 'dark'; applyTheme(next); store('ccd-theme', next); label(); });
  label();
  document.getElementById('site-header').replaceChildren(h('div', { class: 'bar' },
    h('a', { class: 'brand', href: 'index.html' }, h('b', {}, 'Carrying Capacity Dashboard'), h('span', {}, 'A resource-based indicator of regional self-sufficiency')),
    h('nav', { class: 'nav', 'aria-label': 'Main' }, PAGES.map(([href, text]) => h('a', { href, 'aria-current': href === current ? 'page' : null }, text)), toggle)));
  document.getElementById('site-footer').replaceChildren(
    h('p', { class: 'notice' }, h('b', {}, 'Prototype. '), 'While every effort has been made to ensure its accuracy, the developers accept no liability for any results generated. Estimates cover land for food, textiles, timber and liquid fuel only, and say nothing about environmental impact.'),
    h('p', {}, 'Model by Murray Lane (', h('a', { href: 'https://eprints.qut.edu.au/67485/' }, 'thesis'), '). Code and data are open: ', h('a', { href: REPO }, 'source repository'), '.'));
}
