from pato import Pato
from avestruz import Avestruz

def main():
    pato = Pato()
    avestruz = Avestruz()

    # Lista de aves voladoras
    aves_voladoras = [pato]

    # Hacer volar a las aves voladoras
    for ave in aves_voladoras:
        ave.volar()

    # Mostrar comportamiento de la avestruz
    avestruz.caminar()
    avestruz.correr()

if __name__ == "__main__":
    main()
