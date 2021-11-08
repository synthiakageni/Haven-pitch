import unittest
from models import Categories

class CategoriesTest(unittest.TestCase):
    
    def setUp(self):
        self.new_category=Categories(category = 'Spiritual')
        
    def test_cat(self):
        self.assertTrue(self.new_category is not None)    