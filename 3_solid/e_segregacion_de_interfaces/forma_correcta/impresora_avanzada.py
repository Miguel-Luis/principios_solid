from impresora import IImpresora
from escaner import IEscaner
from fax import IFax

class ImpresoraAvanzada(IImpresora, IEscaner, IFax):
    def imprimir(self, documento):
        print(f"Imprimiendo documento: {documento}")

    def escanear(self, documento):
        print(f"Escaneando documento: {documento}")

    def enviar_fax(self, documento):
        print(f"Enviando fax del documento: {documento}")
