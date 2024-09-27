from abc import ABC, abstractmethod

class ConexionDB(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def ejecutar_consulta(self, consulta):
        pass
