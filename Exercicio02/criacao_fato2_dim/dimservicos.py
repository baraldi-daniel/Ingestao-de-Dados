import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE dimservicos AS (SELECT CodigoServico,Servico FROM apidadoscoletados GROUP BY CodigoServico);")