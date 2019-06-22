import mysql.connector
from mysql.connector import Error  

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'python_db'") 
        records1 = cursor.fetchall()
        print("Tables:", records1)

    connection2 = mysql.connector.connect(host='localhost',
                                         database='python_db_1',
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'python_db_1'") 
        records2 = cursor.fetchall()
        print("Tables:", records2)

    if(connection1 != connection2):
        print("We have a missmatch")
    else:
        print("Everything is matching")


except Error as e:

    print ("Unable to finish", e)

finally:
    if (connection1.is_connected()):
        cursor.close()
        connection1.close()
        print("MySQL connection is closed")
    if (connection2.is_connected()):
        cursor.close()
        connection1.close()
        print("MySQL connection is closed")
