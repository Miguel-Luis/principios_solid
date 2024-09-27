class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []  # Lista para almacenar los libros agregados

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Se ha agregado el libro '{libro.titulo}' a la biblioteca '{self.nombre}'.")

    def mostrar_catalogo(self):
        if self.catalogo:
            print(f"Catálogo de la biblioteca '{self.nombre}':")
            for libro in self.catalogo:
                libro.mostrar_info()
        else:
            print(f"La biblioteca '{self.nombre}' no tiene libros en su catálogo.")
