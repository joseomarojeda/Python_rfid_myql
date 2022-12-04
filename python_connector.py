# Bibliotecas
import mysql.connector

# Programa
print ("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='omaro',
                              password='1234',
                              host='192.168.100.7',
                              database='codigoIoT')
print ("Conexion realizada")
print (cnx)

print ("Cerrar conexión")
cnx.close()
print ("Conexión cerrada")