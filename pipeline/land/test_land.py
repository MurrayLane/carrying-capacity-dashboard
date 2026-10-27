"""Tests on the committed SA2 land and population tables.   python3 -m unittest discover -s pipeline/land"""
import csv, json, os, unittest
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
rows = lambda f: list(csv.DictReader(open(os.path.join(REPO, 'data/sa2', f))))
rows_nrm = lambda f: list(csv.DictReader(open(os.path.join(REPO, 'data/nrm2011', f))))


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


class Zones2011(unittest.TestCase):
    def test_zone_table_totals_and_state_rows(self):
        z = {int(r['zone']): r for r in rows_nrm('land_2011_method_zones.csv')}
        self.assertEqual(len(z), 60)
        self.assertAlmostEqual(float(z[1]['total']), 7687574, delta=7687574 * 0.001)
        for k in ('cropping', 'pasture', 'reserve', 'total'):
            self.assertAlmostEqual(sum(float(z[s][k]) for s in (2, 15, 26, 40, 49, 56, 60)), float(z[1][k]), delta=1)

    def test_cropping_and_grazing_sum_to_the_abs_national_figures(self):
        z = {int(r['zone']): r for r in rows_nrm('land_2011_method_zones.csv')}
        self.assertAlmostEqual(float(z[1]['cropping']), 316500, delta=300)           # ABS 2020-21: 31.650 Mha
        self.assertAlmostEqual(float(z[1]['pasture']), 3318690, delta=3000)          # ABS 2020-21: 331.869 Mha

    def test_zone_mapping_covers_the_regions_once(self):
        m = json.load(open(os.path.join(REPO, 'pipeline/land/zone_to_nrm2011.json')))['zones']
        codes = [c for v in m.values() for c in v]
        self.assertEqual(len(codes), len(set(codes)))


if __name__ == '__main__': unittest.main()
