from animal import *

class Perro(Animal):
    def __init__(self, nombre, raza, color, peso, altura):
        super().__init__(nombre, raza, color, peso, altura)

    def marcar_territorio(self):
        print(f"{self.nombre} está marcando territorio")
    
    def saludar_con_la_cola(self):
        print(f"{self.nombre} está saludando con la cola")