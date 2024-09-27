from abc import ABC, abstractmethod

class IMultiFunctionDevice(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass

    @abstractmethod
    def escanear(self, documento):
        pass

    @abstractmethod
    def enviar_fax(self, documento):
        pass
