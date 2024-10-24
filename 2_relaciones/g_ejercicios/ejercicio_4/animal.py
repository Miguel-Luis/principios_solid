class Animal:
    def __init__(self, nombre, raza, color, peso, altura):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.peso = peso
        self.altura = altura

    def caminar(self):
        print(f"{self.nombre} está caminando")

    def correr(self):
        print(f"{self.nombre} está corriendo")

    def comer(self):
        print(f"{self.nombre} está comiendo")





        