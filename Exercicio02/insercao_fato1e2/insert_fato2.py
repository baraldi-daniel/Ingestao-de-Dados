import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO fato2 (CNPJ, CodigoServico) SELECT CNPJ,CodigoServico FROM apidadoscoletados WHERE CNPJ!='' GROUP BY CNPJ, CodigoServico;")

#mycursor.execute("UPDATE fato2 SET QuantidadeServicos = 1;")

mydb.commit()

mydb.close()