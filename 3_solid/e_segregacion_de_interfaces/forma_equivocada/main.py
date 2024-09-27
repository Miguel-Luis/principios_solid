from impresora_simple import ImpresoraSimple
from impresora_avanzada import ImpresoraAvanzada

def main():
    documento = "Contrato.pdf"

    impresora_avanzada = ImpresoraAvanzada()
    impresora_simple = ImpresoraSimple()

    # Uso de Impresora Avanzada
    impresora_avanzada.imprimir(documento)
    impresora_avanzada.escanear(documento)
    impresora_avanzada.enviar_fax(documento)

    # Uso de Impresora Simple
    impresora_simple.imprimir(documento)
    impresora_simple.escanear(documento)  # Esto generará NotImplementedError
    impresora_simple.enviar_fax(documento) # Esto generará NotImplementedError

if __name__ == "__main__":
    main()
