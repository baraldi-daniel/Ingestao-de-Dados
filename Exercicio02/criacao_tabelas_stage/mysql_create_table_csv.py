#import sqlite3 
import mysql.connector 
  
#conn = sqlite3.connect('stage_database.db')  



conx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)
  
mycursor = conx.cursor()

  
mycursor.execute('''CREATE TABLE IF NOT EXISTS csv (
       Ano VARCHAR(255),
       Trimestre VARCHAR(255),
       Categoria VARCHAR(255),
       Tipo VARCHAR(255),
       CNPJ VARCHAR(255),
       InstituicaoFinanceira VARCHAR(255),
       Indice VARCHAR(255),
       QuantidadeReclamacoesReguladasProcedentes VARCHAR(255),
       QuantidadeReclamacoesReguladasOutras VARCHAR(255),
       QuantidadeReclamacoesNaoReguladas VARCHAR(255),
       QuantidadeTotalReclamacoes VARCHAR(255),
       QuantidadeTotalClientesCCSSCR VARCHAR(255),
       QuantidadeClientesCCS VARCHAR(255),
       QuantidadeClientesSCR VARCHAR(255));''')  

conx.close()


