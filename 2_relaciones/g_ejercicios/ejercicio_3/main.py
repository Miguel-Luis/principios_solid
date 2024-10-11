from lago import Lago

def main():
    lago = Lago('Cristal', 'Bagre')

    ###---Utilizar metodos del lago
    lago.alimentar()

    ###---Intentar alimentar los peces 
    try:
        lago.__tipo_peces.comer()
    except Exception as e:
        print(f"Error {e}")

    ###---Intentar alimentar peces despues de eliminar el lago
    del lago

    try:
        lago.alimentar()
    except Exception as e:
        print(f"Error {e}")


if __name__ == '__main__':
    main()