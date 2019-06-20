import mysql.connector
from mysql.connector import Error

try: 
#connect to the 1st db
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')

    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema = 'python_db'") 
        records1 = cursor.fetchall()
#connect to the 2nd db
    connection2 = mysql.connector.connect(host='localhost',
                                         database='python_db_1',
                                         user='root',
                                         password='')    

    if connection2.is_connected():
        cursor = connection2.cursor()
        cursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema = 'python_db_1'") 
        records2 = cursor.fetchall()

    if(records1 == records2):
        print("completely matching :)")
    else:
        print("disrepancies found :(")           

except Error as e:
    print ("Unable to finish", e)


finally:
    if (connection1.is_connected()):
        cursor.close()
        connection1.close()
        print("MySQL connection is closed")

