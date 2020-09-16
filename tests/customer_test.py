import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Harrison", 30.00)

    def customer_has_name(self):
        self.assertEqual("Harrison", self.customer.name)

    def customer_has_wallet(self):
        self.assertEqual(30.00, self.customer.wallet)