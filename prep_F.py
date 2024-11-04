#PREPARAZIONE ALLA VERIFICA F
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

risposta = ""
numAnimali = 0

rispOpz = int(input("""1) Inserisci nuovo mammifero 
2) Controlla la tabella """))

if (rispOpz == 1):
  risposta = input("Vuoi inserire un nuovo animale? y/n ")
  if (risposta.lower() == 'y'):
    numAnimali = int(input("Quanti animali vuoi inserire "))
    for i in range(numAnimali):
        mycursor.execute("USE Animali")
        Nome = input("Inserisci il nome: ")
        Razza = input("Inserisci la razza: ")
        Peso = int(input("Inserisci il peso: "))
        Eta = int(input("Inserisci l'età: "))
        sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s,%s,%s)"
        val = (Nome, Razza, Peso, Eta)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        rispNum = input("Vuoi continuare? y/n ")
        if (rispNum.lower() == 'n'):
            break

elif (rispOpz == 2):
  mycursor.execute("USE Animali")
  mycursor.execute("SELECT * FROM Mammiferi")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)





