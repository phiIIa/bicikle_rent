
class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
