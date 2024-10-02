from libro import Libro
from biblioteca import Biblioteca

def main():
    # Crear instancias de libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")

    # Crear instancia de Biblioteca
    biblioteca = Biblioteca("Biblioteca Central")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Mostrar el catálogo de la biblioteca
    biblioteca.mostrar_catalogo()

    # Demostrar que los libros existen independientemente de la biblioteca
    print("\nInformación de los libros fuera de la biblioteca:")
    libro1.mostrar_info()
    libro3.mostrar_info()

if __name__ == "__main__":
    main()

"""
! Análisis de la Relación de Agregación

* Agregación entre Biblioteca y Libro:

- La clase Biblioteca tiene una lista de objetos Libro en su atributo catalogo.
- Los Libros pueden existir independientemente de la Biblioteca.
    -- En el ejemplo, libro3 no es agregado a ninguna biblioteca pero sigue existiendo y podemos acceder a su información.
- La biblioteca es un contenedor de libros, pero los libros no dependen de la biblioteca para existir.

? Diferencia con Asociación Simple:

- En una asociación simple, una clase conoce a otra pero no necesariamente la contiene.
- En la agregación, una clase contiene instancias de otra clase como parte de su estado interno, pero las instancias contenidas pueden existir sin la contenedora.

TODO: Diferencia con Composición:

- En la composición, las partes no pueden existir sin el todo.
- Si la Biblioteca fuera eliminada y los Libros también, estaríamos ante una composición.
- En este ejemplo, si eliminamos la instancia de Biblioteca, los libros siguen existiendo.
"""