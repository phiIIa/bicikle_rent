
class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__bicycle = None

    def rent_bicycle(self, bicycle):
        if self.__bicycle is not None:
            return False

        self.__bicycle = bicycle
        return True

    def pay(self, bicycle, amount):
        if self.__bicycle is not bicycle:
            return False

        if self.__balance >= amount:
            self.__balance -= amount
            self.__bicycle = None
            return True

        return False

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_bicycle(self):
        return self.__bicycle
