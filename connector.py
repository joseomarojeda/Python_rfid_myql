from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='omaro', password='1234',
                                 host='127.1668.100.7',
                                 database='codigoIoT')
cnx.close()