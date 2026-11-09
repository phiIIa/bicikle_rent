class Bicikle:

    def __init__(self, number, bicikle_type, price_per_minute):
        self.__number = number
        self.__bike_type = bicikle_type
        self.__price_per_minute = price_per_minute
        self.__available = True

    def get_number(self):
        return self.__number

    def get_bike_type(self):
        return self.__bike_type

    def is_available(self):
        return self.__available

    def manage_available(self, value):
        self.__available = value

    def get_price(self):
        return self.__price_per_minute