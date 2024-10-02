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

"""
! Conceptos Clave

* Generalización (Herencia):
- La clase base Empleado define atributos y métodos comunes.
- Las clases derivadas Gerente y Programador heredan estos atributos y métodos, y pueden añadir sus propios atributos y métodos o sobrescribir los existentes.

? Uso de super():
- Permite llamar a métodos de la clase base desde la clase derivada.
- Facilita la extensión de métodos heredados.
"""