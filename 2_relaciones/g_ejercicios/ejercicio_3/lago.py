from pez import Pez

class Lago:
    def __init__(self, nombre_lago, tipo_peces):
        self.nombre = nombre_lago
        self._peces = []
        self._agregar_peces(tipo_peces)

    def _agregar_peces(self, tipo_peces):
        if tipo_peces:
            for tipo_pez in tipo_peces:
                self._peces.append(Pez(tipo_pez))

    def alimentar(self):
        if self._peces:
            print(f"Alimentando peces en el lago {self.nombre}")
            for pez in self._peces:
                pez.comer()
        else:
            print(f"No hay peces que alimentar en el lago {self.nombre}")

