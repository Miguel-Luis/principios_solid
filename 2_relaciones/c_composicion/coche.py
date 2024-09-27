from motor import Motor

class Coche:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.__motor = Motor(tipo_motor)  # Composición: el motor es parte integral del coche

    def arrancar(self):
        print(f"Arrancando el {self.marca} {self.modelo}.")
        self.__motor.encender()

    def detener(self):
        print(f"Deteniendo el {self.marca} {self.modelo}.")
        self.__motor.apagar()
