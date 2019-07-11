import mysql.connector
from mysql.connector import Error  

db1_name = input("1st db name: ")
db1_table_name = input("1st db table name: ")
db1_col_name = input("1st db column name: ")

db2_name = input("2nd db name: ")
db2_table_name = input("2nd db table name: ")
db2_col_name = input("1st db column name: ")


try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database=db1_name,
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        val_first = cursor.execute("SELECT * from information_schema.columns where table_name = '{}' and column_name = '{}' ORDER BY LENGTH('{}') DESC LIMIT 1".format(db1_table_name,db1_col_name,db1_col_name)) # select the table
        cursor.fetchall()
        print(val_first)

    connection2 = mysql.connector.connect(host='localhost',
                                         database=db2_name,
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        val_second = cursor.execute("SELECT * from information_schema.columns where table_name = '{}' and column_name = '{}' ORDER BY LENGTH('{}') DESC LIMIT 1".format(db2_table_name,db2_col_name,db2_col_name)) # select the table
        cursor.fetchall()
        print(val_second)

    if(val_first == val_second):
        print("Matching!")
    else:
        print("")
        print("Max: {}".format(val_first))
        print("Max: {}".format(val_second))


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
