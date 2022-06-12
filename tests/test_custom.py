# pylint: skip-file
"""
Comproveu que la funció 2a(find_max_col) dóna el resultat correcte quan cols_to_return conté, com a mínim, dues columnes (per exemple, short_name i potential).
- Comproveu que la funció 2a(find_max_col)  dóna el resultat correcte si el resultat inclou més d'una fila.
- Comproveu que la funció calculate_BMI dóna el resultat correcte quan gender = ‘F’
- Comproveu que la funció clean_up_players_dict dóna el resultat correcte si la query conté
l'operació “one”.
"""

import unittest
from testing_imports import *
from HTMLTestRunner import HTMLTestRunner



class CustomTests_1_2(unittest.TestCase):
    @classmethod
    def setUp(cls):
        #cls.data = join_datasets_year("data", [2016])
        #cls.data = join_datasets_year(self.path_to_data, [2016])
        cls.data = join_datasets_year("data", [2016])


    def test_custom_1(self):
        # find_max_col function works properly using 2 columns in cols_to_return
        max_potential = find_max_col(df = self.data, filter_col='potential', cols_to_return=['potential', 'short_name'])
        self.assertEqual(max_potential.iloc[0,0],95) # First column
        self.assertEqual(max_potential.iloc[0, 1], 'L. Messi') # Second column

    def test_custom_2(self):
        # Check if find_max_col works properly with multiple row outputs.
        multi_row = find_max_col(df=self.data, filter_col='weak_foot', cols_to_return=['weak_foot', 'short_name'])
        self.assertEqual(multi_row.shape[0], 170)


class CustomTests_3(unittest.TestCase):
    # Comproveu que la funció calculate_BMI dóna el resultat correcte quan gender = ‘F’
    @classmethod
    def setUp(cls):
        # Create some fake data
        cls.data = pd.DataFrame({"short_name": ["L. Messi", "A. Putellas", "A. Hegerberg"],
                                 "gender": ["M", "F", "F"],
                                 "year": [2021, 2021, 2022],
                                 "height_cm": [169, 171, 177],
                                 "weight_kg": [67, 66, 70]})

    def test_custom_3(self):
        female_bmi = calculate_bmi(self.data, "F", 2021, ["short_name"])
        self.assertEqual(female_bmi["short_name"].iloc[0], "A. Putellas")
        self.assertEqual(female_bmi["BMI"].iloc[0], 66/(1.71*1.71))



class CustomTests_4(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.data = join_datasets_year("data", [2016, 2017, 2018])

    def test_custom_4(self):
        # Check if the function clean_up_players_dict reduces the content of a field to one.
        ids = [176580, 168542]
        columns_of_interest = ["short_name", "dob"]
        data_dict = players_dict(self.data, ids, columns_of_interest)
        data_dict = clean_up_players_dict(data_dict, [("dob", "one")])
        # Check a couple of values
        self.assertCountEqual(data_dict[176580]["dob"], ['1987-01-24'])
        self.assertCountEqual(data_dict[168542]["dob"], ['1986-01-08'])




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CustomTests_1_2))
    suite.addTest(unittest.makeSuite(CustomTests_3))
    suite.addTest(unittest.makeSuite(CustomTests_4))

    runner = HTMLTestRunner(log=True, verbosity=2, output='reports',
                            title='PAC4', description='PAC4 custom tests',
                            report_name='custom tests')
    runner.run(suite)
