from perro import *
from gato import *

def main():
    perro = Perro('Gaia', 'criollo', 'blanco y negro', '20 Kg', '40 cm')
    gato = Gato('Mona', 'criolla', 'blanca', '5 Kg', '20 cm')

    perro.correr()
    perro.saludar_con_la_cola()
    perro.caminar()
    perro.marcar_territorio()
    perro.comer()

    print("|-------------------------------|")

    gato.caminar()
    gato.escalar()
    gato.ronronear()
    gato.comer()
    gato.correr()

if __name__ == '__main__':
    main()