class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"the profit:{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        self.money_received = 0
        for k, v in self.COIN_VALUES.items():
            coin = float(input(f"enter count of coin {k}:\n"))
            self.money_received += coin * v
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        if cost >= self.money_received:
            self.profit += cost
            return True
        return False
