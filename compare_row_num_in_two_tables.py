import mysql.connector
from mysql.connector import Error  

db1_name = input("1st db name: ")
db1_table_name = input("1st db table name: ")
db2_name = input("2nd db name: ")
db2_table_name = input("2nd db table name: ")

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database=db1_name,
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT * FROM {}".format(db1_table_name,))
        cursor.fetchall()
        result1 = cursor.rowcount

    connection2 = mysql.connector.connect(host='localhost',
                                         database=db2_name,
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT * FROM {}".format(db2_table_name,))
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
