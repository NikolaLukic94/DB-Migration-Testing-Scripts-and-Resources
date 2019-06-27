import mysql.connector
from mysql.connector import Error  

db_name = input("db name: ")

try: 
    connection = mysql.connector.connect(host='localhost',
                                         database=db_name,
                                         user='root',
                                         password='')

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = %s",(db_name,)) 
        records = cursor.fetchall() 
        print(records)
        #TABLE_ROWS column is only an estimated value used in SQL optimization
except Error as e:

    print ("Unable to count", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

