class Departamento:
    def __init__(self, nombre_departamento):
        self.nombre_departamento = nombre_departamento
        self.profesores = []

    def agregar_profesor(self, profesor):
        if profesor.agregar_a_departamento():
            self.profesores.append(profesor)
            print(f"{profesor.nombre} se ha agregado al departamento {self.nombre_departamento}")
        else:
            print(f"{profesor.nombre} ya se encuentra en el departamento {self.nombre_departamento}")


    def quitar_profesor(self, profesor):
        if profesor in self.profesores:
            self.profesores.remove(profesor)
            profesor.salir_de_departamento()
            print(f"{profesor.nombre} se ha eliminado del departamento {self.nombre_departamento}")
        else:
            print(f"{profesor.nombre} no se encuentra en el departamento {self.nombre_departamento}")