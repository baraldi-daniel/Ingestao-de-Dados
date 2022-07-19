import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute(f"CREATE TABLE fato2 (CNPJ INT, CodigoServico VARCHAR(255));")

