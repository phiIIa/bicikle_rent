import user
class Admin(user.Client):
    def __init__(self, name, balance):
        super().__init__(name, balance)