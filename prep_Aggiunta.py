import mysql.connector
from flask import Flask, jsonify
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/mammiferi', methods=['GET'])
def get_mammiferi():
    # Esegui la query per ottenere tutti i dati dalla tabella "Mammiferi"
    mycursor.execute("SELECT * FROM Mammiferi")
    rows = mycursor.fetchall()

    # Ottieni i nomi delle colonne
    columns = [desc[0] for desc in mycursor.description]

    # Converti ogni riga in un dizionario, con le colonne come chiavi
    mammiferi_list = [dict(zip(columns, row)) for row in rows]

    # Restituisci i dati in formato JSON
    return jsonify(mammiferi_list)

# Esegui l'app Flask
if __name__ == '__main__':
    app.run(debug=True)