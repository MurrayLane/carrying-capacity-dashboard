"""Tests on the committed ABS cubes (data/abs-2016-21) and the commodity map.   python3 -m unittest discover -s pipeline/yields/abs_current"""
import json, os, unittest
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
YEARS = ('2016-17', '2017-18', '2018-19', '2019-20', '2020-21')
cube = lambda y: json.load(open(os.path.join(REPO, 'data/abs-2016-21', f'cube_{y}.json')))
cmap = json.load(open(os.path.join(HERE, 'commodity_map.json')))['crops']


class Mapping(unittest.TestCase):
    def test_every_model_crop_has_exactly_one_entry(self):
        model = json.load(open(os.path.join(HERE, 'model_crops.json')))['crops']
        self.assertEqual([c['crop'] for c in cmap], model); self.assertEqual(len(model), 91)

    def test_a_mapped_crop_names_area_or_trees_and_tonnes(self):
        for c in cmap:
            if c['status'] == 'absent': self.assertFalse(c['area'] or c['trees'] or c['tonnes'], c['crop'])
            else: self.assertTrue((c['area'] or c['trees']) and c['tonnes'], c['crop'])

    def test_regions(self):
        r = json.load(open(os.path.join(REPO, 'data/abs-2016-21/regions.json')))['regions']
        self.assertEqual(len(r), 64); self.assertEqual((r[0]['column'], r[0]['label']), (1, 'Australia'))
        self.assertEqual(sum(x['kind'] == 'state' for x in r), 8)


class Cubes(unittest.TestCase):
    def test_national_yields_are_plausible_in_every_year(self):
        for y in YEARS:
            rows = cube(y)['rows']
            for crop, lo, hi in (('Wheat', 0.8, 3.5), ('Barley', 1.0, 3.5), ('Sugar cane', 60, 100), ('Potatoes', 25, 55)):
                a, t = rows[f'{crop} (ha)'][1], rows[f'{crop} (t)'][1]; self.assertTrue(lo < t / a < hi, (y, crop, t / a))

    def test_units_were_converted(self):                    # mushrooms are published in m2 and kg; fruit production in kg in the early years
        for y in YEARS:
            rows = cube(y)['rows']; self.assertTrue(1e3 < rows['Mushrooms (ha)'][1] < 1e4 or rows['Mushrooms (ha)'][1] < 1e3, y)
            self.assertTrue(1e4 < rows['Apples (t)'][1] < 1e6, (y, rows['Apples (t)'][1]))

    def test_unreliable_cells_refer_to_rows_that_exist(self):
        for y in YEARS:
            d = cube(y)
            for label, col in d['unreliable']: self.assertIn(label, d['rows']); self.assertTrue(1 <= col <= 64)

    def test_2020_21_has_the_minimum_size_rule_applied(self):
        d = cube('2020-21'); flagged = {(l, c) for l, c in d['unreliable']}
        for c in range(1, 65):
            a = d['rows']['Wheat (ha)'][c]
            if a is not None and a < 10: self.assertIn(('Wheat (ha)', c), flagged)


if __name__ == '__main__': unittest.main()
