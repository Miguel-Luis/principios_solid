from conexion_db import ConexionDB

class MySQLConexion(ConexionDB):
    def conectar(self):
        print("Conectando a la base de datos MySQL...")

    def ejecutar_consulta(self, consulta):
        print(f"Ejecutando consulta en MySQL: {consulta}")
