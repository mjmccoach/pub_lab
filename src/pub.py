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
        if customer.age >= 18:
            customer.reduce_wallet(drink)
            self.increase_till(drink)
# could add return if wanted

    
    # def sell_drink_to_customer(self, customer, drink):
    #     customer = Customer.name
    #     drink = Drink.name
    #     self.till += Drink.price
    #     Customer.wallet -= Drink.price
        

