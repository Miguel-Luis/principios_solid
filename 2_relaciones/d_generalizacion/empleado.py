class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario: ${self.salario}")

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")
