from impresora import Impresora
from documento import Documento

def main():
    documento = Documento("Este es el contenido del documento.")
    impresora = Impresora()
    impresora.imprimir(documento)

if __name__ == "__main__":
    main()

"""
Explicación:
- La clase Impresora depende de la clase Documento porque utiliza su instancia en el método imprimir.
- Sin embargo, Impresora no posee ni mantiene una referencia permanente a Documento.
- Es una relación temporal y de uso.
"""