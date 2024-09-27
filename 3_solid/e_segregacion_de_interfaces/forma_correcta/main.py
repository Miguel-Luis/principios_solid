from impresora_simple import ImpresoraSimple
from impresora_avanzada import ImpresoraAvanzada

def main():
    documento = "Contrato.pdf"

    impresora_simple = ImpresoraSimple()
    impresora_avanzada = ImpresoraAvanzada()

    # Uso de Impresora Simple
    impresora_simple.imprimir(documento)
    # impresora_simple.escanear(documento)  # Ahora, este método no existe en ImpresoraSimple

    # Uso de Impresora Avanzada
    impresora_avanzada.imprimir(documento)
    impresora_avanzada.escanear(documento)
    impresora_avanzada.enviar_fax(documento)

if __name__ == "__main__":
    main()
