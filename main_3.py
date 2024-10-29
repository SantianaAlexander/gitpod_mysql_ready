import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Santianamydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Film (Nome, Regista) VALUES (%s, %s)"
val = ('La', 'Isao')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
