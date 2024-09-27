from conexion_db import ConexionDB

class OrdenProcesador:
    def __init__(self, conexion_db: ConexionDB):
        self.conexion = conexion_db

    def procesar_orden(self, orden_id):
        self.conexion.conectar()
        self.conexion.ejecutar_consulta(f"SELECT * FROM ordenes WHERE id = {orden_id}")
        print(f"Procesando la orden {orden_id}")
