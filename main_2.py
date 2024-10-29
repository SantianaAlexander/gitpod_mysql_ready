#ESERCIZIO 2 - CREAZIONE DI UNA TABELLA
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Santianamydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Film (Nome VARCHAR(255), Regista VARCHAR(255))")
