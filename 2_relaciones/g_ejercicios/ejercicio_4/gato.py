from animal import *

class Gato(Animal):
    def __init__(self, nombre, raza, color, peso, altura):
        super().__init__(nombre, raza, color, peso, altura)

    def escalar(self):
        print(f"{self.nombre} está escalando")

    def ronronear(self):
        print(f"{self.nombre} está ronroneando")