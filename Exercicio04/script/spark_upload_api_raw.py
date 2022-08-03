import argparse
import requests
import json

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

def upload_api_raw(data_source,output_uri):

    with SparkSession.builder.appName("Upload API").getOrCreate() as spark:
        ##Load CSV data
        
        df = spark.read.option("header", "false").option("sep", "\t").csv(data_source)
        df=df.toDF('CNPJ')

        print(df.show())


        data = spark.sparkContext.emptyRDD()

        columns = StructType([StructField('CNPJ', StringType(), True),
                            StructField('CodigoServico', StringType(), True),
                            StructField('DataVigencia', StringType(), True),
                            StructField('Periodicidade', StringType(), True),
                            StructField('Servico', StringType(), True),
                            StructField('TipoValor', StringType(), True),
                            StructField('Unidade', StringType(), True),
                            StructField('ValorMaximo', StringType(), True)
                            ])

        df3 = spark.createDataFrame(data=data,
                                    schema=columns)


        for row_iterator in df.collect():

            print(row_iterator["CNPJ"])

            #cnpj=row_iterator["CNPJ"]
            if(str(row_iterator["CNPJ"]) != ''):
                
                url = f"https://olinda.bcb.gov.br/olinda/servico/Informes_ListaTarifasPorInstituicaoFinanceira/versao/v1/odata/ListaTarifasPorInstituicaoFinanceira(PessoaFisicaOuJuridica=@PessoaFisicaOuJuridica,CNPJ=@CNPJ)?@PessoaFisicaOuJuridica='F'&@CNPJ='{row_iterator['CNPJ']}'&$format=json"

                r = requests.get(url = url, verify=False ,timeout=300)
                print(url)       
                print(r.content)
                print(r.json()['value'])
                if len(r.json()['value'])!=0:
                    df=spark.createDataFrame((r.json()['value']))
                    print(df.show())
                    df2=df.withColumn("CNPJ",lit(row_iterator["CNPJ"]))
                    
                    df2 = df2.select('CNPJ','CodigoServico','DataVigencia','Periodicidade','Servico','TipoValor','Unidade','ValorMaximo')
                    print(df2.show())
                    df2.createOrReplaceTempView("df_final")

            api_data = spark.sql("""SELECT * FROM df_final""")
            df3=df3.union(api_data)
            print(df3.show())
                

        # # # Create an in-memory DataFrame to query
        df3.createOrReplaceTempView("upload_api")



        # # Create var with data
        csv_data = spark.sql("""SELECT * FROM upload_api""")
        #csv_data = spark.sql("""SELECT * FROM upload_csv""")

        print(csv_data)

        

        # # Write the results to the specified output URI
        csv_data.write.option("sep",";").option("header", "true").mode("overwrite").csv(output_uri)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_source', help="s3://exercicio04/output/cnpjs/")    
    parser.add_argument(
        '--output_uri', help="s3://exercicio04/raw/api")
    args = parser.parse_args()

    upload_api_raw(args.data_source,args.output_uri)
