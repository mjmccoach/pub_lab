from src.customer import Customer
from src.drink import Drink

class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, drink):
        self.till += drink.price
    
    def sell_drink_to_customer(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness <= 15:
            customer.reduce_wallet(drink)
            self.increase_till(drink)
            customer.chug_drink(drink)

    def sell_food_to_customer(self, food, customer):
        customer.reduce_wallet(food)
        self.increase_till(drink)
        customer.rejuvenate(food)
# could add return if wanted
        

