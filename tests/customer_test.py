import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Harrison", 15, 30.00)
        self.drink4 = Drink("Wine", 9.75, 12)
        self.food = Food("Chips and gravy", 3.50, 100)

    def test_customer_has_name(self):
        self.assertEqual("Harrison", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(30.00, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink4)
        self.assertEqual(20.25, self.customer.wallet)

    def test_customer_has_drunkenness(self):
        self.assertEqual(0, self.customer.drunkenness)


    def test_chug_drink(self):
        self.customer.chug_drink(self.drink4)
        self.assertEqual(12, self.customer.drunkenness)

    def test_rejuvenate(self):
        self.customer.rejuvenate(self.food)
        self.assertEqual(-100, self.customer.drunkenness)