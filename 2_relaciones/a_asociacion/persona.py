class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mascotas = []  # Lista para almacenar mascotas asociadas

    def adoptar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"{self.nombre} ha adoptado a {mascota.nombre}.")

    def mostrar_mascotas(self):
        if self.mascotas:
            print(f"{self.nombre} tiene las siguientes mascotas:")
            for mascota in self.mascotas:
                print(f"- {mascota.nombre} ({mascota.tipo})")
        else:
            print(f"{self.nombre} no tiene mascotas.")
