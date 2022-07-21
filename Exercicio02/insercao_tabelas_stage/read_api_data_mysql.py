# script para leitura dos dados da API
import requests
import sqlite3
import mysql.connector

#conn = sqlite3.connect('stage_database.db')  
  
#data = conn.execute("select CNPJ from csv"); 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MinhaSenha01",
  database="engenhariadados"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT CNPJ from csv")

dados=mycursor.fetchall()

#PessoaFisicaouJuridica = ['F','J']

for cnpj in dados:
    if(str(cnpj[0]) != ''):
        
        url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifasPorInstituicaoFinanceira/versao/v1/odata/" \
            f"ListaTarifasPorInstituicaoFinanceira(PessoaFisicaOuJuridica=@PessoaFisicaOuJuridica,CNPJ=@CNPJ)?@PessoaFisicaOuJuridica='F'" \
            f"&@CNPJ='{cnpj[0]}'&$format=json"

        r = requests.get(url = url, verify=False ,timeout=300)

        response = r.json()['value']

        for i in range(0,len(response)):
            CodigoServico = response[i]['CodigoServico']
            Servico = response[i]['Servico']
            Unidade =  response[i]['Unidade']
            DataVigencia = response[i]['DataVigencia']
            ValorMaximo = response[i]['ValorMaximo']
            TipoValor = response[i]['TipoValor']
            Periodicidade = response[i]['Periodicidade']

            query = f'INSERT INTO apidadoscoletados (' \
            f'CNPJ, CodigoServico, Servico, Unidade, DataVigencia,' \
            f'ValorMaximo, TipoValor, Periodicidade)' \
            f' VALUES (' \
            f'\'{cnpj[0]}\',' \
            f'\'{CodigoServico}\',' \
            f'\'{Servico}\',' \
            f'\'{Unidade}\',' \
            f'\'{DataVigencia}\',' \
            f'\'{ValorMaximo}\',' \
            f'\'{TipoValor}\',' \
            f'\'{Periodicidade}\'' \
            f');' 

            mycursor.execute(query);  

mydb.commit()  
mydb.close()
