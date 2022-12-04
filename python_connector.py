# Bibliotecas
import mysql.connector

# Programa
print ("Conectandose a la base de datos")
cnx = mysql.connector.connect(user='omarojeda',password='2602',host='192.168.100.7',database='codigoIoT')
print ("Conexion realizada")
print (cnx)

print ("Cerrar conexión")
cnx.close()
print ("Conexión cerrada")