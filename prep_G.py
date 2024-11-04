#PREPARAZIONE ALLA VERIFICA G
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

risposta = ""

rispOpz = int(input("""Premi 1 per inserire un nuovo animale 
Premi 2 per visualizzare tutti gli animali
Premi 3 per eliminare un animale
Premi 4 per modificare un animale """))

if (rispOpz == 1):
  risposta = input("Vuoi inserire un nuovo animale? y/n ")
  if (risposta.lower() == 'y'):
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
elif (rispOpz == 2):
  mycursor.execute("USE Animali")
  mycursor.execute("SELECT * FROM Mammiferi")
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
elif (rispOpz == 3):
    mycursor.execute("USE Animali")
    rispId = input("Inserisci l'ID dell'animale che vuoi eliminare ")
    delete_query = "DELETE FROM Mammiferi WHERE id = %s"
    mycursor.execute(delete_query, (rispId,))
    mydb.commit()
elif (rispOpz == 4):
    mycursor.execute("USE Animali")
    rispId = input("Inserisci l'ID dell'animale che vuoi modificare ")
    nuovo_nome = input("Inserisci il nuovo nome: ")
    nuova_razza = input("Inserisci la nuova razza: ")
    nuovo_peso = int(input("Inserisci il nuovo peso: "))
    nuova_eta = int(input("Inserisci la nuova età: "))
    
    update_query = """
        UPDATE Mammiferi 
        SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s 
        WHERE id = %s
    """
    valori = (nuovo_nome, nuova_razza, nuovo_peso, nuova_eta, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()



