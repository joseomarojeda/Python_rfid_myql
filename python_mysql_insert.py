# Bibliotecas
import mysql.connector

# Conexión
cnx = mysql.connector.connect(user='omarojeda', password='2602', host='192.168.100.7', database='codigoIoT')

# Cursor
cursor = cnx.cursor()

query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Omar Ojeda','Test Python 8',865485648652);"
# query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Omar Ojeda','" + text + "'," + str(id) + ");"

# Ejecutar cursor
cursor.execute (query_insert)

# Asegurarse de realizar la operacion en BD
cnx.commit()
print ("Query Ok")

# Cerrar
cursor.close()
cnx.close()