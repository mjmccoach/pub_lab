import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.drink = Drink("Highland Park 18yr", 6.95, 8)
        self.drink2 = Drink("Rum", 5.50, 4)
        self.drink3 = Drink("Beer", 3.20, 2)

        self.food = Food("Chips and gravy", 3.50, 100)
        
        self.customer1 = Customer("Malcolm", 33, 25.00)
        self.customer2 = Customer("Harrison", 15, 30.00)
        self.customer3 = Customer("Dave", 21, 50.00)

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(self.drink3)
        self.assertEqual(103.20, self.pub.till)

    def test_sell_drink_to_customer_over_18_and_not_drunk(self):
    
        self.pub.sell_drink_to_customer(self.drink, self.customer1)
        self.assertEqual(106.95, self.pub.till)
        self.assertEqual(18.05, self.customer1.wallet)


    def test_sell_drink_to_customer_under_18(self):

        self.pub.sell_drink_to_customer(self.drink, self.customer2)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(30.00, self.customer2.wallet)


    def test_sell_drink_to_customer_drunk(self):
        self.customer3.drunkenness = 20

        self.pub.sell_drink_to_customer(self.drink, self.customer3)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(50.00, self.customer3.wallet)
        self.assertEqual(20, self.customer3.drunkenness)

    def test_sell_food_to_customer(self):

        self.pub.sell_food_to_customer(self.food, self.customer3)
        self.assertEqual(103.50, self.pub.till)
        self.assertEqual(46.50, self.customer3.wallet)
        self.assertEqual(-100, self.customer3.drunkenness)