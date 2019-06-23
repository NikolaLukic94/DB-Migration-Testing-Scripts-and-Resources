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
                                         database=db1_name,
                                         user='root',
                                         password='')

    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT is_nullable FROM information_schema.columns  where table_name   = %s  AND column_name = %s;",(db1_table_name, db1_column_name)) 
        records1 = cursor.fetchall()
        print("Nullable:", records1)

    connection2 = mysql.connector.connect(host='localhost',
                                         database=db2_name,
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT is_nullable FROM information_schema.columns  where table_name   = %s  AND column_name = %s;",(db2_table_name, db2_column_name)) 
        records2 = cursor.fetchall()
        print("Nullable:", records2)

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