from mysql_conexion import MySQLConexion

class OrdenProcesador:
    def __init__(self):
        self.conexion = MySQLConexion()

    def procesar_orden(self, orden_id):
        self.conexion.conectar()
        self.conexion.ejecutar_consulta(f"SELECT * FROM ordenes WHERE id = {orden_id}")
        print(f"Procesando la orden {orden_id}")
