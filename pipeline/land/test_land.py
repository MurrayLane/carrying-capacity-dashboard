"""Tests on the committed SA2 land and population tables.   python3 -m unittest discover -s pipeline/land"""
import csv, json, os, unittest
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
rows = lambda f: list(csv.DictReader(open(os.path.join(REPO, 'data/sa2', f))))


class Land(unittest.TestCase):
    def test_total_area_matches_the_2011_models_total_land(self):
        total = sum(float(r['total_km2']) for r in rows('land_types_by_sa2.csv'))
        self.assertAlmostEqual(total, 7687574, delta=7687574 * 0.001)

    def test_types_sum_to_the_total_in_every_sa2(self):
        for r in rows('land_types_by_sa2.csv'):
            parts = sum(float(r[k]) for k in r if k.endswith('_km2') and k != 'total_km2')
            self.assertAlmostEqual(parts, float(r['total_km2']), delta=0.01)

    def test_every_raster_class_maps_to_exactly_one_type(self):
        import re
        m = json.load(open(os.path.join(REPO, 'pipeline/land/land_types.json')))['types']
        for r in rows('clum_classes.csv'):
            first = re.split(r';\s*', re.match(r'[\d.]+(?:;\s*[\d.]+)*', r['TERTV8']).group(0))[0].rstrip('.')
            hits = [t for t, ps in m.items() for p in ps if first == p or first.startswith(p + '.')]
            self.assertEqual(len(hits), 1, r['TERTV8'])

    def test_population_is_there_for_the_land_sa2s_and_totals_are_plausible(self):
        pop = {r['sa2_code']: r for r in rows('population_erp.csv')}
        land = [r['sa2_code'] for r in rows('land_types_by_sa2.csv')]
        self.assertEqual([c for c in land if c not in pop], [])
        self.assertAlmostEqual(sum(float(r['2011']) for r in pop.values()), 22.3e6, delta=0.1e6)      # the 2011 model's national population is 22,326,388


if __name__ == '__main__': unittest.main()
