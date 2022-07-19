# script para leitura dos dados da API
import mysql.connector
from email import header
import sqlite3
import csv
import os

path_csv_arqs = r'C:\Users\baral\OneDrive\Documents\Engenharia de Dados - USP\Ingestão de Dados\Exercicio02\CSV'
files = os.listdir(path_csv_arqs)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados",
  autocommit=True
)

mycursor = mydb.cursor()


for arq in files:
    with open(path_csv_arqs + r'\\' + arq, encoding='iso-8859-1') as csv_file:
        csv_reader =  csv.reader(csv_file, delimiter=';',skipinitialspace= True)
        line_count = 0
        next(csv_reader)
        for row in csv_reader:
            print(row)
            query = f'INSERT INTO csv (' \
                    f'Ano, Trimestre, Categoria, Tipo, CNPJ,' \
                    f'InstituicaoFinanceira,' \
                    f'Indice,' \
                    f'QuantidadeReclamacoesReguladasProcedentes,' \
                    f'QuantidadeReclamacoesReguladasOutras,' \
                    f'QuantidadeReclamacoesNaoReguladas,' \
                    f'QuantidadeTotalReclamacoes,' \
                    f'QuantidadeTotalClientesCCSSCR,' \
                    f'QuantidadeClientesCCS,' \
                    f'QuantidadeClientesSCR) ' \
                    f'VALUES (' \
                    f'\'{row[0]}\',' \
                    f'\'{row[1]}\',' \
                    f'\'{row[2]}\',' \
                    f'\'{row[3]}\',' \
                    f'\'{row[4]}\',' \
                    f'\'{row[5]}\',' \
                    f'\'{row[6]}\',' \
                    f'\'{row[7]}\',' \
                    f'\'{row[8]}\',' \
                    f'\'{row[9]}\',' \
                    f'\'{row[10]}\',' \
                    f'\'{row[11]}\',' \
                    f'\'{row[12]}\',' \
                    f'\'{row[13]}\'' \
                    f');'

            mycursor.execute(query)


mydb.commit()  

mydb.close()


    

    

  