from ave import Ave
from pato import Pato
from avestruz import Avestruz

def hacer_volar(ave):
    ave.volar()

def main():
    ave = Ave()
    pato = Pato()
    avestruz = Avestruz()

    hacer_volar(ave)       # Funciona correctamente
    hacer_volar(pato)      # Funciona correctamente
    hacer_volar(avestruz)  # Genera una excepción

if __name__ == "__main__":
    main()
