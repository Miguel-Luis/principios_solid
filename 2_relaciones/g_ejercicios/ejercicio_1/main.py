from miembro import Miembro
from libro import Libro

def main():
    libro_1 = Libro('¡Que viva la música!')
    libro_2 = Libro('El mundo y sus demonios')

    miembro_1 = Miembro('Luis Miguel González')
    miembro_2 = Miembro('Luis David Ortiz')

    miembro_1.prestar_libro(libro_1)
    miembro_1.devolver(libro_1)

    miembro_2.prestar_libro(libro_2)
    miembro_2.devolver(libro_1)


if __name__ == '__main__':
    main()