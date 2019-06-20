import MySQLdb

dbconnect = MySQLdb.connect("localhost", "pythonuser", "pythonpwd123", "pythondb")

cursor = dbconnect.cursor()

query = "SELECT * FROM movie"  
try:  
   cursor.execute(query)
   resultList = cursor.fetchall()
   for row in resultList:
      print ("Movie ID =", row[0])
      print ("Name =", row[1])
      print ("Year =", row[2])
      print ("Director = ", row[3])
      print ('Genre = ', row[4])
except:  
   print ("Encountered error while retrieving data from database")
finally:  
   dbconnect.close()