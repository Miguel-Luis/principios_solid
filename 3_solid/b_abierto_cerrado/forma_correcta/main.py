from cliente import Cliente
from calculadora_descuentos import CalculadoraDescuentos

def main():
    clientes = [
        Cliente("Juan", "estudiante", 100),
        Cliente("María", "jubilado", 200),
        Cliente("Pedro", "empleado", 150),
        Cliente("Ana", "veterano", 120),
        Cliente("Luis", "regular", 80)
    ]

    calculadora = CalculadoraDescuentos()

    for cliente in clientes:
        total_con_descuento = calculadora.calcular_descuento(cliente)
        print(f"Total a pagar por {cliente.nombre} ({cliente.tipo}): ${total_con_descuento}")

if __name__ == "__main__":
    main()
