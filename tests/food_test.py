import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Chips and gravy", 3.50, 100)


    def test_food_has_name(self):
        self.assertEqual("Chips and gravy", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(3.50, self.food.price)
    
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(100, self.food.rejuvenation_level)