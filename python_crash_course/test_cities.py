from city_functions import city_country
import unittest

class CityTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do Ouput like this 'Lisboa, Portugal' work?"""
        full_name = city_country('lisboa', 'portugal')
        self.assertEqual(full_name, 'Lisboa, Portugal')
    
    def test_city_country_population(self):
        """Do output like this 'Lisboa, Portugal - population 10000000' work?"""
        full_name = city_country('lisboa', 'portugal', '10000000')
        self.assertEqual(full_name, 'Lisboa, Portugal - Population 10000000')

if __name__ == '__main__':
    unittest.main()