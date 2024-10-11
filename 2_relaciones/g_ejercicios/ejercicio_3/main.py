from lago import Lago

def main():
    tipos_peces = ['bagre', 'bocachico', 'trucha']
    lago = Lago('Cristal', tipos_peces)

    ###---Utilizar metodos del lago
    lago.alimentar()

    ###---Intentar alimentar los peces 
    try:
        lago._peces[0].comer()
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