class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self._tiene_departamento = False

    def agregar_a_departamento(self):
        if not self._tiene_departamento:
            self._tiene_departamento = True
            return True
        return False
    
    def salir_de_departamento(self):
        self._tiene_departamento = False