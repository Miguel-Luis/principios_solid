class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"El motor {self.tipo} está encendido.")

    def apagar(self):
        print(f"El motor {self.tipo} está apagado.")
