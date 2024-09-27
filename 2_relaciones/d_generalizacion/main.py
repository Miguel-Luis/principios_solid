from gerente import Gerente
from programador import Programador

def main():
    # Crear instancia de Gerente
    gerente = Gerente("Ana", 5000, "Ventas")
    # Crear instancia de Programador
    programador = Programador("Luis", 3000, "Python")

    # Mostrar información y acciones del gerente
    print("Información del Gerente:")
    gerente.mostrar_informacion()
    gerente.trabajar()    # Método heredado de Empleado
    gerente.gestionar()   # Método específico de Gerente

    print("\nInformación del Programador:")
    # Mostrar información y acciones del programador
    programador.mostrar_informacion()
    programador.trabajar()   # Método heredado de Empleado
    programador.programar()  # Método específico de Programador

if __name__ == "__main__":
    main()
