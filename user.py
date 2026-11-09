class Client:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__is_owning = (False, None)

    def pay(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_is_owning(self):
        return self.__is_owning

    def set_is_owning(self, is_owning, bicikle_number=None):
        self.__is_owning = (is_owning, bicikle_number)