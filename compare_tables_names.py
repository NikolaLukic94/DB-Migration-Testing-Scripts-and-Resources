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
        cursor.execute("SHOW TABLES in {}".format(db1_name,)) # select the table
        records1 = cursor.fetchall()
        records2 = sorted(records1)

    connection2 = mysql.connector.connect(host='localhost',
                                         database=db2_name,
                                         user='root',
                                         password='')

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SHOW TABLES in {}".format(db2_name,)) # select the table
        records1 = cursor.fetchall()
        records2 = sorted(records1)


    if(connection1 == connection2):
        print("Tables are matching")
    else:
        print("Tables are not matching")


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
