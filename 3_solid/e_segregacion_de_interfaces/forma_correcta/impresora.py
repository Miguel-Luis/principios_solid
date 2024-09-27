from abc import ABC, abstractmethod

class IImpresora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
