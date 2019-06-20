import MySQLdb

dbconnect = MySQLdb.connect("localhost", "pythonuser", "pythonpwd123", "pythondb")

cursor = dbconnect.cursor()

query = 'insert into movie(id, name, year, director, genre) values (1, "Bruce Almighty", 2003, "Tom Shaydac", "Comedy")'
try:  
   cursor.execute(query)
   dbconnect.commit()
except:  
   dbconnect.rollback()
finally:  
   dbconnect.close()