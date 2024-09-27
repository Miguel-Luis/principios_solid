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
