#PREPARAZIONE ALLA VERIFICA A
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("USE Animali")
mycursor.execute("CREATE TABLE Mammiferi (id INT PRIMARY KEY AUTO_INCREMENT , nome_Proprio VARCHAR(255), razza VARCHAR(255), peso INT, eta INT)")

