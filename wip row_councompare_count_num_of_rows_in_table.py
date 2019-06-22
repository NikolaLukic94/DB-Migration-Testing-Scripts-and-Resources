import mysql.connector
from mysql.connector import Error  

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("describe customers name") # select the table
        records1 = cursor.fetchall()
        print("Num of rows:", records1)

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