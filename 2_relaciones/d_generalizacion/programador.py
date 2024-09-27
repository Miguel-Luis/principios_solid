from empleado import Empleado

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje de programación: {self.lenguaje}")

    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")
