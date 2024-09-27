from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

    def gestionar(self):
        print(f"{self.nombre} está gestionando el departamento de {self.departamento}.")
