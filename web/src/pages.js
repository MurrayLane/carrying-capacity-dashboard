// Text pages: methods, what has changed since 2011, and about.
import { h } from './lib.js';
import { PARAMS, GROUPS, LAND } from './params.js';
import { REPO } from './layout.js';
import help from './data/help.json';

const THESIS = 'https://eprints.qut.edu.au/67485/';
const trustedLinks = el => { el.querySelectorAll('a[href^="http"]').forEach(a => { a.target = '_blank'; a.rel = 'noopener noreferrer'; }); return el; };
const page = (...kids) => h('div', { class: 'page' }, ...kids);

export function mountMethods(root) {
  const params = GROUPS.map(g => {
    const gh = help.groups[g.id];
    return h('section', {}, h('h2', {}, gh.title.trim().charAt(0) + gh.title.trim().slice(1).toLowerCase()),
      gh.html ? trustedLinks(h('div', { class: 'help-html', html: gh.html })) : null,
      g.params.map(k => { const p = PARAMS[k], ph = help.params[p.help];
        return h('details', {}, h('summary', {}, p.caption, h('span', { class: 'param-desc' }, '  ', p.desc)), ph ? trustedLinks(h('div', { class: 'help-html', html: ph })) : h('p', { class: 'scope-note' }, `Range ${p.min} to ${p.max}${p.unit}. See the group description above.`)); }));
  });
  root.replaceChildren(page(
    h('h1', {}, 'Methods'),
    h('p', {}, 'The dashboard estimates how many people a landscape could support from its own land, if the population produced everything it consumed within the boundary. It is a land budget for food, textiles, timber and liquid fuel. It does not model water, electricity, shelter beyond land area, trade or environmental damage, so its answers are limits on land rather than forecasts.'),
    h('div', { class: 'callout' }, 'Everything here is described in full in ', h('a', { href: THESIS }, 'the thesis'), ', chapter 8. The model itself is an Excel workbook in the ', h('a', { href: REPO }, 'repository'), '; the website evaluates that workbook in your browser.'),
    h('h2', {}, 'How an estimate is made'),
    h('ol', {}, [
      'Choose a zone. Each zone has default areas of five land types (cropping, pasture, non-agricultural, infrastructure, nature reserve) and a current population.',
      'The diet is built from about 750 foods, each broken into raw commodities such as wheat or canola. Serving sizes and amounts follow national dietary modelling and change with activity level and the share of meat, eggs and dairy.',
      'Losses are applied at six stages, from inedible portions and cooking to consumer, retail, processing and farm. Only consumer, retail and farm-to-retail waste are treated as avoidable, and the waste slider changes those.',
      'Each commodity’s demand is divided by its yield for the zone. Yields are five-year ABS averages, adjusted for organic and irrigation choices and for the climate time frame you pick. The result is land per person.',
      'Biofuel, textiles and timber add land per person in the same way. Infrastructure and nature reserve are set directly.',
      'Land is not interchangeable. Cropping land can do any job, pasture all but cropping, and the rest only forestry and infrastructure. The model re-allocates land by that rule to give the largest population that every demand can be met for.',
      'Land left over is excess land. A zone is over capacity when its current population exceeds the estimate.']
      .map(t => h('li', {}, t))),
    h('h2', {}, 'The scale effect'),
    h('p', {}, 'A zone treated as one unit usually supports more people than the sum of its regions each treated as self-sufficient, because a surplus of pasture in one region cannot fill a shortage of cropping land in another. The dashboard shows both figures under Scale. The thesis (section 9.4) reports 40 million for Australia as one unit and 23 million as the sum of its regions.'),
    h('h2', {}, 'Land and population'),
    LAND.concat([{ key: 'p', label: 'Current population', field: 'inputPopulation' }]).map(l => { const t = help.areas[l.field]; return t ? h('details', {}, h('summary', {}, l.label), trustedLinks(h('div', { class: 'help-html', html: t.html }))) : null; }),
    h('h2', {}, 'Parameters'),
    h('p', {}, 'The text below is carried over unchanged from the 2011 page, so figures such as “average Australian estimate” refer to 2011 conditions.'),
    params,
    h('h2', {}, 'Data used'),
    h('table', { class: 'data' }, h('thead', {}, h('tr', {}, ['Input', 'Source', 'Period'].map(x => h('th', { scope: 'col' }, x)))), h('tbody', {}, [
      ['Crop yields and land use by region', 'Australian Bureau of Statistics, agricultural commodities by NRM region', '2005-06 to 2009-10, five-year average'],
      ['Nature reserve and infrastructure land', 'ABARES land use of Australia; thesis estimates', '2005-06'],
      ['Population', 'ABS for Australia and states; NRM bodies and published papers for regions', 'Around 2010'],
      ['Diet and serving sizes', 'NHMRC food guidance modelling; ABS national nutrition survey', '1995 and 2011'],
      ['Climate variability', 'ABS historical yields of wheat, oats and barley by state', '1861 to 2010']].map(r => h('tr', {}, r.map(c => h('td', {}, c)))))),
    h('h2', {}, 'Known limits'),
    h('ul', {}, [
      'Pasture is treated as equally productive across a zone, yet red meat takes most of the land for food, so this assumption drives much of the answer.',
      'Irrigation has no water limit. The slider is irrigated share of all farmland, and a flat 55 percent yield uplift applies to every crop.',
      'The climate variability series ends in 2010 and assumes the future resembles the past.',
      'Regional state and national populations in the 2011 data set do not add up exactly, which affects state-level over and under capacity but not capacity itself.'].map(t => h('li', {}, t)),),
    h('p', {}, 'These and other findings from auditing the model are written up in the ', h('a', { href: `${REPO}/tree/main/analysis` }, 'analysis folder'), ' of the repository.')));
}

export function mountChanges(root) {
  const versions = h('div', {}, h('p', {}, 'Loading...'));
  root.replaceChildren(page(
    h('h1', {}, 'Since 2011'),
    h('p', {}, 'This site currently runs the 2011 data set: the zones, land areas, populations and yields used in the thesis. A refreshed data set, using current sources, is being prepared.'),
    h('div', { class: 'callout' }, 'Once the refresh is complete, this page will compare each zone then and now: carrying capacity, population, whether the zone has moved between under and over capacity, and how much of the change comes from population, land use and yields.'),
    h('h2', {}, 'What is already fixed'),
    h('p', {}, 'The complete output of the original 2011 program for all 60 zones and both default settings is saved in the repository, along with the script that produced it. This site reproduces every one of those 120 results: it is the test the rebuild had to pass.'),
    h('ul', {}, [h('li', {}, h('a', { href: `${REPO}/blob/main/baseline/baseline_2011.csv` }, 'The 2011 results as a table')), h('li', {}, h('a', { href: `${REPO}/blob/main/SCOPE.md` }, 'The plan for the refresh')), h('li', {}, h('a', { href: `${REPO}/blob/main/PUBLICATIONS.md` }, 'How the comparison will be reported'))]),
    h('h2', { id: 'versions' }, 'Versions'),
    versions));
  fillVersions(versions);
}

// Every version of the data and method is kept. A version that has been published is never edited; a correction or a
// refresh becomes a new version, so an old link or a citation always reproduces what it showed.
async function fillVersions(box) {
  try {
    const base = new URL(import.meta.env.BASE_URL, location.href).href;
    const m = await (await fetch(base + 'data/releases.json')).json();
    box.replaceChildren(
      h('p', {}, 'Each version fixes the zones, the data and the method together. A published version is never edited: a correction or a refresh becomes a new version, so a saved link or a citation always shows what it showed when it was made. Versions differ only as described here, so the effect of each change can be told apart.'),
      ...m.releases.map(r => h('section', { class: 'card', style: 'margin-bottom:12px' },
        h('div', { class: 'card-h' }, h('h3', {}, r.label), h('span', { class: 'step' }, r.id === m.default ? 'default' : r.status)),
        h('p', {}, r.description),
        r.patches.length ? h('ul', {}, r.patches.map(p => h('li', {}, `${p.preset === 'long' ? 'Long-term' : 'Short-term'} ${p.field === 'fibre' ? 'textiles (kg per person)' : p.field} default set to ${p.value}. ${p.reason}`))) : null,
        r.errata.length ? h('div', {}, h('b', {}, 'Known issues'), h('ul', {}, r.errata.map(e => h('li', {}, e)))) : null,
        h('p', {}, h('a', { href: `index.html#r=${r.id}` }, 'Open this version')))));
  } catch (e) { box.replaceChildren(h('p', { class: 'err' }, `The version list could not be loaded: ${e.message}`)); }
}

export function mountAbout(root) {
  root.replaceChildren(page(
    h('h1', {}, 'About'),
    h('p', {}, 'The Carrying Capacity Dashboard was created by Murray Lane as part of doctoral research at the Queensland University of Technology, with supervisors Les Dawes and Peter Grace. It was first released online in 2012. This version was rebuilt in 2026 so that it can be maintained, updated and checked.'),
    h('h2', {}, 'How to cite'),
    h('p', {}, 'Lane, M. (2014). ', h('i', {}, 'The development of a carrying capacity assessment model for the Australian socio-environmental context'), '. PhD thesis, Queensland University of Technology. ', h('a', { href: THESIS }, THESIS)),
    h('p', {}, 'Lane, M., Dawes, L. and Grace, P. (2014). The essential parameters of a resource-based carrying capacity assessment model: an Australian case study. ', h('i', {}, 'Ecological Modelling'), ' 272, 220-231.'),
    h('p', {}, 'Lane, M., Dawes, L. and Grace, P. (2015). Scalar considerations in carrying capacity assessment: an Australian example. ', h('i', {}, 'Population and Environment'), ' 36(3), 356-371.'),
    h('h2', {}, 'Open code and data'),
    h('p', {}, 'The code is under the MIT licence. The workbook, data layers and results are under Creative Commons Attribution 4.0. Everything is in the ', h('a', { href: REPO }, 'repository'), ', including the plan, the audit of the model and the saved 2011 results.'),
    h('h2', {}, 'Questions and corrections'),
    h('p', {}, 'Please raise them as an ', h('a', { href: `${REPO}/issues` }, 'issue on the repository'), '. A contact address will be added here.'),
    h('h2', {}, 'Acknowledgements'),
    h('p', {}, 'The original dashboard was built at the QUT Institute for Future Environments. Data come from the Australian Bureau of Statistics, ABARES, the National Health and Medical Research Council and the other sources listed under Methods.'),
    h('h2', {}, 'Disclaimer'),
    h('p', {}, 'This is a research prototype. While every effort has been made to ensure its accuracy, the developers accept no liability for any results generated.')));
}
