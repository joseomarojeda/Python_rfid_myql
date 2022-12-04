from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='omarojeda', password='2602',
                                 host='127.168.100.7',
                                 database='codigoIoT')
cnx.close()