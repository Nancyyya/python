import unittest
from user import city_country
"""
def city_country(city,country):
    cstr = city.title() + ',' + country.title()
    return cstr
"""

class CityTestCase(unittest.TestCase):
    """测试city country"""
    def test_city_country(self):
        cstr = city_country('santiago','chile')
        self.assertEqual(cstr,'Santiago,Chile')
unittest.main()
