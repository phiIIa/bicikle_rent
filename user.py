
class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def pay(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name
