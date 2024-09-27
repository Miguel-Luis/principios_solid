from multifuncion_dispositivo import IMultiFunctionDevice

class ImpresoraSimple(IMultiFunctionDevice):
    def imprimir(self, documento):
        print(f"Imprimiendo documento: {documento}")

    def escanear(self, documento):
        raise NotImplementedError("Escaneo no soportado.")

    def enviar_fax(self, documento):
        raise NotImplementedError("Fax no soportado.")
