import bicikle

class Electro_bicikle(bicikle.Bicikle):
    def __init__(self, number):
        super().__init__(number, "electro_bicikle", 5)