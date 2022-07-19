import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute(f"INSERT INTO fato1 (CHAVEPERIODO,CNPJ, QTDPROBLEMASREGULADOSPROCEDENTES) SELECT CONCAT(Ano,Trimestre),CNPJ,QuantidadeReclamacoesReguladasProcedentes FROM csv WHERE CNPJ!='';")

mydb.commit()

mydb.close()