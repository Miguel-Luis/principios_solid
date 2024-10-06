from profesor import Profesor
from deparmento import Departamento

def main():
    departamento_1 = Departamento('Ingeniería')
    departamento_2 = Departamento('Ciencias exactas y naturales')

    profesor_1 = Profesor('Luis Miguel González')
    profesor_2 = Profesor('Luis David Ortiz')

    departamento_1.agregar_profesor(profesor_1)
    departamento_1.quitar_profesor(profesor_2)

    departamento_2.agregar_profesor(profesor_2)
    departamento_2.quitar_profesor(profesor_2)

if __name__ == '__main__':
    main()