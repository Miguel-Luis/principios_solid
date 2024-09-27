from abc import ABC, abstractmethod

class DescuentoBase(ABC):
    @abstractmethod
    def calcular(self, total_compra):
        pass
