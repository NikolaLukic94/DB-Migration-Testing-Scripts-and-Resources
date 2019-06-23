
import mysql.connector
from mysql.connector import Error  

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        query = "SELECT * FROM customers"
        cursor.execute(query)
        cursor.fetchall()
        result1 = cursor.rowcount

    connection2 = mysql.connector.connect(host='localhost',
                                         database='python_db_1',
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        query = "SELECT * FROM customers"
        cursor.execute(query)
        cursor.fetchall()
        result2 = cursor.rowcount

    if(connection1 == connection2):
        print("Nums of rows is the same")
    else:
        print("Num of rows is not the same")


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
