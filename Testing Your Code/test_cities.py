#Testing our function in city_functions.py

import unittest
from city_functions import city_and_country

class TestCityCountry(unittest.TestCase):
    '''Tests for 'city_functions.py'''
    
    def test_city_country(self):
        '''Does 'Atlanta, United States' work?'''
        atl = city_and_country('atlanta','united states')
        self.assertEqual(atl, 'Atlanta, United States')
        
    def test_city_country_population(self):
        '''Does 'Atlanta, United States - 500' work?'''
        atl = city_and_country('atlanta', 'united states', 500)
        self.assertEqual(atl, 'Atlanta, United States - 500')
        

if __name__ == '__main__':
    unittest.main()
    
