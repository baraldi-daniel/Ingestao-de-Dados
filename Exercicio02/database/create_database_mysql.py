import mysql.connector

conx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01"
)

mycursor = conx.cursor()

mycursor.execute("CREATE DATABASE engenhariadados;")