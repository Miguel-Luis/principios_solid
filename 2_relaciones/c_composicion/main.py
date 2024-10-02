from coche import Coche

def main():
    # Crear una instancia de Coche
    mi_coche = Coche("Toyota", "Corolla", "Gasolina")

    # Utilizar métodos del Coche
    mi_coche.arrancar()
    mi_coche.detener()

    # Intentar acceder al motor de forma independiente (no permitido)
    try:
        mi_coche.__motor.encender()
    except AttributeError as e:
        print(f"Error: {e}")

    # Eliminar el coche y verificar que el motor también deja de existir
    del mi_coche
    try:
        mi_coche.arrancar()
    except NameError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


"""
! Conceptos Clave

* Composición:
- Es una relación fuerte donde el todo (coche) es responsable de la existencia de las partes (motor).
- Si el coche es destruido, el motor también lo es.
- Las partes no pueden existir independientemente del todo.

? Encapsulamiento:
- Al declarar __motor como atributo privado, evitamos que sea accedido o manipulado desde fuera de la clase Coche.

TODO: Ciclo de Vida Compartido:
- El motor es creado y destruido junto con el coche.
"""