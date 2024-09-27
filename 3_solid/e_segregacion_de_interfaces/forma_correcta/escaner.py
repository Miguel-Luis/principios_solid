from abc import ABC, abstractmethod

class IEscaner(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass
