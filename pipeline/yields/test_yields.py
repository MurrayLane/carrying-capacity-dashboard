"""Tests that need no archive: the method's arithmetic on small invented cubes.   python3 -m unittest discover -s pipeline/yields"""
import unittest
from yields import crop_year, norm
from average import five_year_average
from fill import model_yield, major_factor, MAJOR_ROWS
from livestock import livestock_year, P


def cube(**rows): return {norm(k.replace('_', ' ')): v for k, v in rows.items()}


class Crops(unittest.TestCase):
    def test_seed_is_deducted(self):                       # Border Rivers-Gwydir wheat 2008-09 in the archive: 2.1226 t/ha
        c = cube(Wheat__ha=[None, 640909.0], Wheat__t=[None, 1403001.0])
        self.assertAlmostEqual(crop_year(c, 'Wheat')[1], 1403001 / 640909 - 0.0665, places=9)

    def test_vegetable_area_is_scaled_up(self):
        c = cube(Carrots__ha=[None, 1000.0], Carrots__t=[None, 40000.0])
        self.assertAlmostEqual(crop_year(c, 'Carrots')[1], 40000 / (1000 * 1.020431688779), places=6)

    def test_trees_become_hectares(self):
        c = cube(Oranges_trees__n=[None, 278730.7328868287], Oranges__t=[None, 15000.0])
        self.assertAlmostEqual(crop_year(c, 'Oranges')[1], 15000 / 1000.0, places=5)

    def test_deleted_cells_and_missing_figures_give_none(self):
        c = cube(Wheat__ha=[None, 100.0, 0.0], Wheat__t=[None, 200.0, 50.0])
        self.assertIsNone(crop_year(c, 'Wheat', deleted={(norm('Wheat (ha)'), 1)})[1])
        self.assertIsNone(crop_year(c, 'Wheat')[2])


class AverageAndFill(unittest.TestCase):
    def test_zero_year_counts_and_missing_year_does_not(self):
        got = five_year_average([[None, 0.0], [None, 4.0], [None, None], [None, 2.0], [None, 2.0]])
        self.assertAlmostEqual(got[1], 2.0)

    def test_all_zero_is_empty(self):
        self.assertIsNone(five_year_average([[None, 0.0], [None, 0.0]])[1])

    def test_fill_uses_national_times_major_factor_then_irrigation(self):
        avg = {r: [None] + [10.0, 5.0] + [None] * 58 for r in MAJOR_ROWS}      # zone 2 is half the national yield in every major crop
        avg[20] = [None, 8.0] + [None] * 59                                     # a commodity zone 2 does not report
        irr = {z: 0.0 for z in range(1, 61)}; irr[2] = 0.1
        self.assertAlmostEqual(major_factor(avg, 2), 0.5)
        out = model_yield(avg, irr, fill_mask={(20, 2)})
        self.assertAlmostEqual(out[20][2], 8.0 * 0.5 / 1.055 * 100)             # g/m2
        self.assertIsNone(model_yield(avg, irr, fill_mask=set())[20][2])        # unmarked pairs stay empty
        self.assertAlmostEqual(out[1][1], 100.0 * 10.0)                         # present averages are only converted

    def test_default_irrigation_setting_returns_the_observed_average(self):        # the model multiplies back by 1 + 0.55 x irrigation
        avg = {r: [None, 10.0] + [7.0] + [None] * 58 for r in MAJOR_ROWS}; irr = {z: 0.048 for z in range(1, 61)}
        self.assertAlmostEqual(model_yield(avg, irr, set())[1][2] / 100 * (1 + 0.55 * 0.048), 7.0)


class Livestock(unittest.TestCase):
    def inputs(self):
        zero = {k: 0.0 for k in ('grazingHa', 'hayHa', 'sheepLambs', 'sheepEwesToLamb', 'sheepEwesNotInLamb', 'sheepRams', 'sheepFeedlot', 'dairyCows', 'dairyHeiferCalves',
               'dairyHeifers1to2', 'dairyHeifersOver2', 'dairyBulls', 'milkTonnes', 'beefBulls', 'beefCows', 'beefCalves', 'beefBalance', 'cattleFeedlot',
               'buffaloes', 'deer', 'goats', 'horsesStud', 'horsesOther', 'otherLivestock')}
        regions = {str(z): dict(zero) for z in range(1, 61)}
        regions['1'].update(grazingHa=1e9, beefCows=1e6, milkTonnes=1e5, dairyCows=1e5); regions['2'].update(grazingHa=5e8, beefCows=5e5, dairyCows=1e5, milkTonnes=5e4)
        nat = dict(sheepFeedlotGrainT=0.0, sheepMeatT=0.0, woolT=0.0, cattleFeedlotGrainT=0.0, cattleMeatT=1e5)
        return {'national': nat, 'regions': regions}

    def test_poultry_follows_grain_yield_over_feed_conversion(self):
        crops = {n: [None] + [3.0] * 60 for n in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans')}
        out = livestock_year(self.inputs(), crops)
        self.assertAlmostEqual(out['Chicken meat'][5], 3.0 / P['fcrChickenMeat'])
        self.assertAlmostEqual(out['Pig meat'][5], 3.0 / P['fcrPigMeat'])

    def test_a_region_with_a_third_of_the_cattle_dse_gets_a_third_of_the_meat_on_its_share_of_land(self):
        crops = {n: [None] + [3.0] * 60 for n in ('Wheat', 'Oats', 'Barley', 'Sorghum', 'Maize', 'Canola', 'Soybeans')}
        out = livestock_year(self.inputs(), crops)
        self.assertGreater(out['Cattle meat'][2], out['Cattle meat'][1])       # same herd density, so yield per hectare of its land is the national figure x its share ratio
        self.assertEqual(out['Cattle meat'][7], 0.0)                           # a region with no animals


if __name__ == '__main__':
    unittest.main()
