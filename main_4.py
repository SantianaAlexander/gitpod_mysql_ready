import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Santianamydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Film")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)