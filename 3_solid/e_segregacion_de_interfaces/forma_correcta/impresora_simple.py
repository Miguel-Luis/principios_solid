from impresora import IImpresora

class ImpresoraSimple(IImpresora):
    def imprimir(self, documento):
        print(f"Imprimiendo documento: {documento}")
