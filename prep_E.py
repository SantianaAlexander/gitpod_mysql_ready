#PREPARAZIONE ALLA VERIFICA B
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s,%s,%s)"
val = [('Nala', 'Gatto Persiano', 5, 1), ('Fufy', 'Labrador ', 30, 5), ('Oliver', 'Bulldog', 28, 4), ('Charlie', 'Gatto Europeo', 5, 2), ('Giucas', 'Shih Tzu', 6, 1)]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
