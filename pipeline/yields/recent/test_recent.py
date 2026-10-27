import json, os, unittest
from group_trend import factors, absent_yield

G = {'Wheat': 'field crops', 'Oats': 'field crops', 'Barley': 'field crops', 'Carrots': 'vegetables', 'Apples': 'fruit', 'Almonds': 'nuts'}


class GroupTrend(unittest.TestCase):
    def test_median_of_the_reported_crops_in_the_group(self):
        f = factors({'Wheat': 1.5, 'Oats': 1.1, 'Barley': 1.3, 'Carrots': 0.9}, G)
        self.assertAlmostEqual(f['field crops']['factor'], 1.3); self.assertEqual(f['field crops']['crops'], 3)

    def test_group_without_a_reported_crop_carries_the_earlier_factor(self):
        f = factors({'Wheat': 1.2, 'Oats': 1.1, 'Barley': 1.3}, G, earlier={'vegetables': 1.06, 'fruit': 1.03})
        self.assertTrue(f['vegetables']['carried']); self.assertAlmostEqual(f['vegetables']['factor'], 1.06)
        self.assertFalse(f['field crops']['carried'])

    def test_no_earlier_factor_means_no_change_and_is_marked_carried(self):
        f = factors({}, G)
        self.assertEqual(f['nuts'], {'factor': 1.0, 'crops': 0, 'carried': True})

    def test_fewer_than_three_crops_is_not_enough_for_a_factor(self):
        g = {'A': 'fruit', 'B': 'fruit', 'C': 'fruit'}
        self.assertTrue(factors({'A': 2.0, 'B': 3.0}, g, earlier={'fruit': 1.1})['fruit']['carried'])
        self.assertFalse(factors({'A': 2.0, 'B': 3.0, 'C': 1.0}, g)['fruit']['carried'])

    def test_absent_yield_keeps_the_regional_pattern(self):
        old = [None, 100.0, 50.0, None]
        self.assertEqual(absent_yield(old, 1.2), [None, 120.0, 60.0, None])

    def test_zero_or_missing_ratios_are_ignored(self):
        f = factors({'Wheat': 0, 'Oats': 1.2, 'Barley': None}, G)
        self.assertEqual(f['field crops']['crops'], 1); self.assertTrue(f['field crops']['carried'])


REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
cube = lambda y: json.load(open(os.path.join(REPO, 'data/abs-2022-25', f'cube_{y}.json')))


class CommittedCubes(unittest.TestCase):
    def test_national_totals_match_the_published_state_tables(self):
        # AABDC_Winter_202425.xlsx, Table 1: wheat total crop area and levied production, Australia
        for year, ha, t in (('2022-23', 12925286, 41199486), ('2023-24', 10506997, 28028429), ('2024-25', 12726755, 34779179)):
            r = cube(year)['rows']
            self.assertAlmostEqual(r['Wheat (ha)'][1], ha, delta=5); self.assertAlmostEqual(r['Wheat (t)'][1], t, delta=10)

    def test_sa2_cells_sum_to_the_states(self):
        for year in ('2022-23', '2024-25'):
            for label in ('Wheat (ha)', 'Canola (t)'):
                v = cube(year)['rows'][label]
                self.assertAlmostEqual(sum(x for x in v[11:] if x), sum(x for x in v[2:11] if x), delta=50)

    def test_every_year_has_the_same_columns(self):
        self.assertEqual({len(r) for y in ('2022-23', '2023-24', '2024-25') for r in cube(y)['rows'].values()}, {len(json.load(open(os.path.join(REPO, 'data/abs-2022-25/regions.json')))['regions']) + 1})


if __name__ == '__main__': unittest.main()
