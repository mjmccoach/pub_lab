class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = 0

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def chug_drink(self, drink):
        self.drunkenness += drink.alcohol_units

    def rejuvenate(self, food):
        self.drunkenness -= food.rejuvenation_level