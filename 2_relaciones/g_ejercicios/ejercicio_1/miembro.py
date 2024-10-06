class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros.append(libro)
            print(f"{self.nombre} prestó el libro {libro.titulo}")
        else:
            print(F"{libro.titulo} no está disponible")

    def devolver(self, libro):
        if libro in self.libros:
            libro.devolver()
            self.libros.remove(libro)
            print(f"{self.nombre} devolvió el libro {libro.titulo}")
        else:
            print(f"{self.nombre} no prestó el libro {libro.titulo}")

    