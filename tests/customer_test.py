import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Harrison", 15, 30.00)

    def test_customer_has_name(self):
        self.assertEqual("Harrison", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(30.00, self.customer.wallet)

    def test_reduce_wallet(self):
        drink = Drink("Wine", 9.75)
        self.customer.reduce_wallet(drink)
        self.assertEqual(20.25, self.customer.wallet)