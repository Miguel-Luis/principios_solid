from persona import Persona
from mascota import Mascota

def main():
    # Crear instancia de Persona
    persona1 = Persona("Luis", 30)

    # Crear instancias de Mascota
    mascota1 = Mascota("Laika", "Perro")
    mascota2 = Mascota("Schrödinger", "Gato")

    # Asociar mascotas a la persona
    persona1.adoptar_mascota(mascota1)
    persona1.adoptar_mascota(mascota2)

    # Mostrar las mascotas de la persona
    persona1.mostrar_mascotas()

    # Interactuar con las mascotas
    mascota1.hacer_sonido()
    mascota2.hacer_sonido()

if __name__ == "__main__":
    main()
