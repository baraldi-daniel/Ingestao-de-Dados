import sqlite3  
import mysql.connector
  
conx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)
  
mycursor = conx.cursor()
  
mycursor.execute(
    '''CREATE TABLE IF NOT EXISTS apidadoscoletados (
       CNPJ VARCHAR(255),
       CodigoServico VARCHAR(255),
       Servico VARCHAR(255),
       Unidade VARCHAR(255),
       DataVigencia VARCHAR(255),
       ValorMaximo VARCHAR(255),
       TipoValor VARCHAR(255),
       Periodicidade VARCHAR(255));''')  

conx.close()
 