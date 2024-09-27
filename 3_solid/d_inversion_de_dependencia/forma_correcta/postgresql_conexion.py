from conexion_db import ConexionDB

class PostgreSQLConexion(ConexionDB):
    def conectar(self):
        print("Conectando a la base de datos PostgreSQL...")

    def ejecutar_consulta(self, consulta):
        print(f"Ejecutando consulta en PostgreSQL: {consulta}")
