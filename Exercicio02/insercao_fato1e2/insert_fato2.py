import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute(f"INSERT INTO fato2 (CNPJ, CodigoServico) SELECT CNPJ,CodigoServico FROM apidadoscoletados WHERE CNPJ!='' ;")

mydb.commit()

mydb.close()