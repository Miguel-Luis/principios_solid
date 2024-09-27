from cliente import Cliente
from calculadora_descuentos import CalculadoraDescuentos

def main():
    cliente = Cliente("Juan", "estudiante", 100)
    calculadora = CalculadoraDescuentos()
    total_con_descuento = calculadora.calcular_descuento(cliente)
    print(f"Total a pagar por {cliente.nombre}: ${total_con_descuento}")

if __name__ == "__main__":
    main()
