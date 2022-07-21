import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE diminstituicao AS (SELECT CNPJ,InstituicaoFinanceira FROM csv WHERE CNPJ!='' GROUP BY CNPJ ORDER BY InstituicaoFinanceira);")


#mycursor.execute("ALTER TABLE diminstituicao MODIFY COLUMN CNPJ INT;")

mydb.commit()
mydb.close()