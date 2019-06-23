import mysql.connector
from mysql.connector import Error  

db1_name = input("1st db name: ")

db2_name = input("2nd db name: ")


try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database=db1_name,
                                         user='root',
                                         password='')

    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT MAX(id) from orders") # select the table
        records1 = cursor.fetchall()
        print("Highest value in this column is", records1)

    connection2 = mysql.connector.connect(host='localhost',
                                         database=db2_name,
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT MAX(id) from orders") # select the table
        records2 = cursor.fetchall()
        print("Highest value in this column is", records2)

    if(records1 == records2):
        print("Everything is matching")
    else:
        print("We have a missmatch")


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