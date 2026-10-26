// The 17 parameters, in the 2011 page's groups. Ticks ("rules") and descriptions are carried over from dashboard.js.
// `ratio` converts the model's value to the displayed one (fractions to percent). `help` keys into data/help.json.
export const PARAMS = {
  food:      { caption: 'Total food', desc: '% of food to be produced', min: 0, max: 500, step: 1, unit: '%', ratio: 100, help: 'pFoodRatio',
               rules: [[0, ''], [100, ''], [200, ''], [300, ''], [400, ''], [500, '']] },
  meategg:   { caption: 'Meat and eggs', desc: '% of diet', min: 0, max: 15, step: 0.5, unit: '%', ratio: 100, help: 'pMeateggRatio',
               rules: [[0, 'Vegan'], [1.5, 'Vegetarian (inc. eggs)'], [2.5, 'Vegetarian (inc. eggs and dairy)'], [7.5, 'Healthy level'], [13, '2011 level'], [15, '']] },
  redmeat:   { caption: 'Red meat', desc: '% of all meat (if meat diet)', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: 'pRedmeatRatio',
               rules: [[0, '100% white meat'], [50, ''], [64, '2011 level'], [100, '0% white meat']] },
  activity:  { caption: 'Activity level', desc: 'Average for population', min: 1, max: 3, step: 1, unit: '', ratio: 1, help: 'pActivityLevel',
               rules: [[1, 'Sedentary'], [2, 'Moderate'], [3, 'High']] },
  losses:    { caption: 'Avoidable waste', desc: '% of all food produced', min: 0, max: 20, step: 1, unit: '%', ratio: 100, help: 'pLossesRatio',
               rules: [[0, ''], [10, ''], [12, '2011 level'], [20, '']] },
  recycling: { caption: 'Recycling', desc: '% of food wastage fed to farm animals', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: 'pRecyclingRatio',
               rules: [[0, '2011 level'], [50, ''], [100, '']] },
  resilience:{ caption: 'Time frame', desc: 'Continuous years', min: 1, max: 150, step: 1, unit: ' yr', ratio: 1, help: 'pResilience',
               rules: [[1, ''], [50, ''], [100, ''], [150, '']] },
  organic:   { caption: 'Organic farming', desc: '% of all agricultural land', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: 'pOrganicRatio',
               rules: [[0, '100% conventional'], [50, ''], [100, '0% conventional']] },
  irrigation:{ caption: 'Irrigation', desc: '% of all irrigated land', min: 0, max: 100, step: 0.1, unit: '%', ratio: 100, help: 'pIrrigationRatio',
               rules: [[0, ''], [50, ''], [100, '']] },
  fibre:     { caption: 'All textiles', desc: 'kg per person per year', min: 0, max: 30, step: 0.5, unit: ' kg', ratio: 1, help: 'pFibreTotal',
               rules: [[0, ''], [10, ''], [23, '2011 level'], [30, '']] },
  fibreNat:  { caption: 'Natural fibre', desc: '% of all natural fibre', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: 'pFibreNaturalRatio',
               rules: [[0, '100% synthetic'], [50, '2011 level'], [100, '0% synthetic']] },
  fibreWool: { caption: 'Wool fibre', desc: '% of all wool fibre', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: 'pFibreWoolRatio',
               rules: [[0, '100% cotton'], [12, '2011 level'], [50, ''], [100, '0% cotton']] },
  fuel:      { caption: 'All liquid fuel', desc: 'Litres per person per year', min: 0, max: 3000, step: 10, unit: ' L', ratio: 1, help: 'pFuelTotal',
               rules: [[0, ''], [1000, ''], [2000, ''], [2600, '2011 level'], [3000, '']] },
  biofuel:   { caption: 'Biofuel', desc: '% of all liquid fuel', min: 0, max: 100, step: 0.5, unit: '%', ratio: 100, help: 'pBiofuelRatio',
               rules: [[0, ''], [50, ''], [100, '']] },
  timber:    { caption: 'Timber', desc: 'All uses, m³ per person per year', min: 0, max: 10, step: 0.1, unit: ' m³', ratio: 1, help: null, group: 'pgTimber',
               rules: [[0, ''], [5, ''], [10, '']] },
  infrastr2: { caption: 'Infrastructure', desc: 'Buildings, roads and so on, m² per person', min: 0, max: 2000, step: 10, unit: ' m²', ratio: 1, help: null, group: 'pgInfrastructure',
               rules: [[0, ''], [730, '2011 level (excluding private green space)'], [1000, ''], [1600, '2011 level (including private green space)'], [2000, '']] },
  nature2:   { caption: 'Nature reserve', desc: '% of all land', min: 0, max: 100, step: 1, unit: '%', ratio: 100, help: null, group: 'pgEcosystem',
               rules: [[0, ''], [23, '2011 level'], [50, ''], [100, '']] },
};
export const GROUPS = [
  { id: 'pgFood', params: ['food', 'meategg', 'redmeat', 'activity', 'losses', 'recycling'] },
  { id: 'pgResilience', params: ['resilience'] },
  { id: 'pgAgriculture', params: ['organic', 'irrigation'] },
  { id: 'pgTextiles', params: ['fibre', 'fibreNat', 'fibreWool'] },
  { id: 'pgLiquidFuel', params: ['fuel', 'biofuel'] },
  { id: 'pgTimber', params: ['timber'] },
  { id: 'pgInfrastructure', params: ['infrastr2'] },
  { id: 'pgEcosystem', params: ['nature2'] },
];
export const PARAM_KEYS = Object.keys(PARAMS);
// land areas (km2) and population, with the form field names the help text is keyed by
export const LAND = [
  { key: 'cropping', label: 'Cropping', field: 'inputAreasCropping' },
  { key: 'pasture', label: 'Pasture', field: 'inputAreasPasture' },
  { key: 'nonAg', label: 'Non-agricultural', field: 'inputAreasNonAg' },
  { key: 'infrastr1', label: 'Infrastructure', field: 'inputAreasBuilt' },
  { key: 'nature1', label: 'Nature reserve', field: 'inputAreasNature' },
];
export const LAND_KEYS = LAND.map(l => l.key);
