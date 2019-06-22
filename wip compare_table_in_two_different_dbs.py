import mysql.connector
from mysql.connector import Error  

try:
    connection1 = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection1.is_connected():
        cursor = connection1.cursor()
        cursor.execute("SELECT IF(COUNT(1)>0,'Differences','No Differences') Comparison FROM ( SELECT column_name,ordinal_position, data_type,column_type,COUNT(1) rowcount FROM information_schema.columns  WHERE  (  (table_schema='python_db' AND table_name='orders') OR  (table_schema='python_db_1' AND table_name='orders') AND table_name IN ('orders')  GROUP BY column_name,ordinal_position, data_type,column_type HAVING COUNT(1)=1) A;") # select the table
        records1 = cursor.fetchall()
        print("Type & lenght:", records1)

    if(connection1 == connection2):
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
