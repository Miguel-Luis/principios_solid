from orden_procesador import OrdenProcesador
from mysql_conexion import MySQLConexion
# from postgresql_conexion import PostgreSQLConexion  # Para usar PostgreSQL

def main():
    conexion_db = MySQLConexion()
    # conexion_db = PostgreSQLConexion()  # Cambiar a PostgreSQL si se desea

    procesador = OrdenProcesador(conexion_db)
    procesador.procesar_orden(123)

if __name__ == "__main__":
    main()
