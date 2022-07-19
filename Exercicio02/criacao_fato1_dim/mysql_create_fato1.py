import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE fato1 (CHAVEPERIODO VARCHAR(255),CNPJ INT, QTDPROBLEMASREGULADOSPROCEDENTES INT);")

