import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        drink = Drink("Beer", 3.20)
        self.pub.increase_till(drink)
        self.assertEqual(103.20, self.pub.till)

    # def test_sell_drink_to_customer():
    #     Pub.drinks = []    