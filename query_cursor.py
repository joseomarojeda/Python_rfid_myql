# Bibliotecas
import mysql.connector

# Conexion
cnx = mysql.connector.connect(user='omarojeda', 
                              password='2602', 
                              host='192.168.100.7',
                              database='codigoIoT')

# Cursor
cursor = cnx.cursor()

# Query
query = ("SELECT * FROM rfid WHERE id=16;")

# Ejecutar cursor
cursor.execute (query)

res = cursor.fetchall ()

for x in res:
    print (x)

# Cerrar todo
cursor.close()
cnx.close()