class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # Por ejemplo: perro, gato, etc.

    def hacer_sonido(self):
        if self.tipo.lower() == 'perro':
            print(f"{self.nombre} dice: ¡Guau!")
        elif self.tipo.lower() == 'gato':
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido desconocido.")
