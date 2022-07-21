import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE dimcategoria AS (SELECT CNPJ,Categoria FROM csv WHERE CNPJ!='' GROUP BY CNPJ);")

#mycursor.execute("ALTER TABLE dimcategoria MODIFY COLUMN CNPJ INT;")

mydb.commit()
mydb.close()