from abc import ABC, abstractmethod

class IFax(ABC):
    @abstractmethod
    def enviar_fax(self, documento):
        pass
