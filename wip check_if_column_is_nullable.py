import mysql.connector
from mysql.connector import Error  

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select c.table_schema as database_name, c.table_name, c.column_name, case c.is_nullable when 'NO' then 'not nullable' when 'YES' then 'is nullable' end as nullable from information_schema.columns c join information_schema.tables t on c.table_schema = t.table_schema and c.table_name = t.table_name where c.table_schema not in ('mysql', 'sys', 'information_schema','performance_schema') and t.table_type = 'BASE TABLE' -- and t.table_schema = 'python_db' -- put your database name here order by t.table_schema,  t.customers, c.id;") 
        records = cursor.fetchall()
        print(records)

except Error as e:

    print ("Unable to count", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



