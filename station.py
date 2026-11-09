import defaulte_bicikle, electro_bicikle, user, admin

class Station:
    __total_profit = 0

    def __init__(self, number,):
        self.__number = number
        self.__bicikles = []

    def get_bicikles(self):
        return self.__bicikles

    def add_bicikle(self, bicikle):
        self.__bicikles.append(bicikle)

    def rent_bicikle(self, bicikle, client):
        if bicikle in self.__bicikles:
            if client.get_is_owning()[0] == False:
                client.set_is_owning(True, bicikle.get_number())
                self.__bicikles.remove(bicikle)
            else:
                raise ValueError("User already rented another bicikle")
        else:
            raise ValueError("bicikle not exist in this station")

    def receive_bicikle(self, bicikle, client, minutes):
        if client.get_is_owning()[0] == True:
            if client.get_is_owning()[1] == bicikle.get_number():
                if not client.pay(bicikle.get_price() * minutes):
                    raise ValueError("not enough money to pay for the ride")
                client.set_is_owning(False)
                Station.__total_profit += bicikle.get_price() * minutes
                self.__bicikles.append(bicikle)
            else:
                raise ValueError("user dont rented this bicikle")
        else:
            raise ValueError("user didnt rent any bicikle")

    def get_total_profit(self, client):
        if isinstance(client, admin.Admin):
            return self.__total_profit
        else:
            raise ValueError("client is not Admin")