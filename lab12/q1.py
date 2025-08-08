class Ship:
    
    def __init__(self, name, year):
        self.__name = name 
        self.__year = year 


    def print (self):
        print("Name : ", self.__name)
        print("Name : ", self.__year)

class CruiseShip(Ship):

    def __init__(self, name, year, maxPass):
        super().__init__(name, year)
        self.__maxPass = maxPass

    def print(self):
        super().print()
        print("Max passenger", self.__maxPass)


class CargoShip(Ship):

    def __init__(self, name, year, capacity):
        super().__init__(name, year)
        self.__capacity = capacity

    def print(self):
        super().print()
        print("Maximum capacity : ", self.__capacity)




ships = [ 
    Ship("Titanic", 1912),
    CruiseShip("Symphony", 2012, 2000),
    CargoShip("hugeShip", 2024, 1500)
]


for ship in ships:
    ship.print()






