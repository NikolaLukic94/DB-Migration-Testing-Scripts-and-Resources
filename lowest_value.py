import mysql.connector
from mysql.connector import Error  

db1_name = input("1st db name: ")
db1_table_name = input("1st db table name: ")
db1_column_name = input("1st db column name: ")

db2_name = input("2nd db name: ")
db2_table_name = input("2nd db table name: ")
db2_column_name = input("2nd db column name: ")

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT MIN(id) from orders") # select the table
        records1 = cursor.fetchall()
        print("Highest value in this column is", records1)

    connection2 = mysql.connector.connect(host='localhost',
                                         database='python_db_1',
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT MIN(id) from orders") # select the table
        records2 = cursor.fetchall()
        print("Highest value in this column is", records2)

    if(connection1 != connection2):
        print("We have a missmatch")
    else:
        print("Lowest values are matching")


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
