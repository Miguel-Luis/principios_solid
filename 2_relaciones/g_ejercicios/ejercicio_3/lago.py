from pez import Pez

class Lago:
    def __init__(self, nombre_lago, tipo_peces):
        self.nombre_lago = nombre_lago
        self.__tipo_peces = Pez(tipo_peces)

    def alimentar(self):
        print(f"Alimentando peces en el lago {self.nombre_lago}")
        self.__tipo_peces.comer()

