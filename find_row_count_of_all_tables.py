import mysql.connector
from mysql.connector import Error  

try: 
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'python_db'") 
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

