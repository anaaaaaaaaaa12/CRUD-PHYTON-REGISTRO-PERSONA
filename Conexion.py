import mysql.connector

class CConexion:
   
    def ConexionBaseDeDatos():
        print("Paso 1: Iniciando conexión a la base de datos...")  
        try:
            print("Paso 2: Intentando conectar...")  
            conexion = mysql.connector.MySQLConnection(  
                user='root',
                password='@ana1234',
                host='127.0.0.1',
                database='clientesdb',
                port=3306
            )
            print("Paso 3: Conexión correcta")  
            return conexion  # No cierres la conexión aquí

        except mysql.connector.Error as error:
            print(f"Error al conectarse: {error}")  
            return None

# Probar conexión
if __name__ == "__main__":
    conexion = CConexion.ConexionBaseDeDatos()
    if conexion:
        print("Paso 4: Se logró conectar a la base de datos.")
    else:
        print("Paso 4: No se pudo conectar a la base de datos.")
