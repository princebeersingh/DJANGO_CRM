import mysql.connector
dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'database2'
)
cursorObject = dataBase.cursor()
# email = hello@gmail.com

cursorObject.execute("create database dj")

print("all done")