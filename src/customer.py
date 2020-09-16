class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def reduce_wallet(self, drink):
        self.wallet -= drink.price