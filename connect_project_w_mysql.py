import mysql.connector
from mysql.connector import Error  # mysql connector Error object is used to show us an error when we failed to connect Databases or if any other database error occurred while working with the database.

try:  # Using this function we can connect the MySQL Database,
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    # verify if our python application is connected to MySQL
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        # This method returns a cursor object. Using a cursor object, we can execute SQL queries.
        cursor = connection.cursor()
        cursor.execute("select database();")

        record = cursor.fetchone()
        print ("Your connected to - ", record)

except Error as e:

    print ("Error while connecting to MySQL", e)

finally:
    # closing database connection.
    if (connection.is_connected()):
        # Using cursor’s close method we can close the cursor object. Once we close the cursor object, we can not execute any SQL statement.
        cursor.close()
        connection.close()
        print("MySQL connection is closed")