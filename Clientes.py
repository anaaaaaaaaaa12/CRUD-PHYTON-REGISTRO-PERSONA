import sys
sys.dont_write_bytecode = True  # Evita que se genere __pycache__



from Conexion import *


import mysql.connector  # Importa el módulo para utilizar mysql.connector

class Clientes:
    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mostrar datos: {}".format(error))

    
    
    def ingresarClientes(nombres, apellidos, sexo):
        try:
            # Llamar al método para establecer la conexión
            cone = CConexion.ConexionBaseDeDatos()
            # Crear el cursor para ejecutar la consulta
            cursor = cone.cursor()
            # La consulta de inserción (ajusté la sintaxis a un formato SQL común es de usuarios no de clientes esto tambien tiene que ver en el codigo)
            query = "INSERT INTO usuarios (nombres, apellidos, sexo) VALUES (%s, %s, %s)"

            # Definimos los valores como tupla
            valores = (nombres, apellidos, sexo)
            # Ejecutamos la consulta con los valores
            cursor.execute(query, valores)
            # Guardamos los cambios
            cone.commit()
            print(cursor.rowcount, "Cliente agregado correctamente.")
            # Cerramos la conexión
            cone.close()
        except mysql.connector.Error as error:
            print("Error de ingreso de datos: {}".format(error))

    def modificarClientes(idUsuario,nombres, apellidos, sexo):
        try:
            # Llamar al método para establecer la conexión
            cone = CConexion.ConexionBaseDeDatos()
            # Crear el cursor para ejecutar la consulta
            cursor = cone.cursor()
            # La consulta de inserción (ajusté la sintaxis a un formato SQL común es de usuarios no de clientes esto tambien tiene que ver en el codigo)
            query = "UPDATE usuarios SET usuarios.nombres =%s, usuarios.apellidos =%s, usuarios.sexo = %s where  usuarios.id = %s"

            # Respetarel orden de la consulta query
            valores = (nombres, apellidos, sexo, idUsuario)
            # Ejecutamos la consulta con los valores
            cursor.execute(query, valores)
            # Guardamos los cambios
            cone.commit()
            print(cursor.rowcount, "Registro actualizado.")
            # Cerramos la conexión
            cone.close()
        except mysql.connector.Error as error:
            print("Error de actualización: {}".format(error))

    def eliminarClientes(idUsuario):
        try:
            # Llamar al método para establecer la conexión
            cone = CConexion.ConexionBaseDeDatos()
            # Crear el cursor para ejecutar la consulta
            cursor = cone.cursor()
            # La consulta de inserción (ajusté la sintaxis a un formato SQL común es de usuarios no de clientes esto tambien tiene que ver en el codigo)
            query = "delete from usuarios where usuarios.id= %s ;"

            # aqui o me lo queria elminar porque suponia que era un tupla
            valores = (idUsuario,)
            # Ejecutamos la consulta con los valores
            cursor.execute(query, valores)
            # Guardamos los cambios
            cone.commit()
            print(cursor.rowcount, "Registro eliminado.")
            # Cerramos la conexión
            cone.close()
        except mysql.connector.Error as error:
            print("Error de eliminacion: {}".format(error))


        
