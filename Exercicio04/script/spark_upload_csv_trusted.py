import argparse

from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def upload_csv_raw(data_source, output_uri):

    with SparkSession.builder.appName("Upload CSV").getOrCreate() as spark:
        # Load CSV data
        # if data_source is not None:
        df = spark.read.option("header", "true").option("sep",";").csv(data_source)
        

        df2=df.withColumn("CNPJ IF", when( (length(df["CNPJ IF"]) <8) & (df["CNPJ IF"]>1), (lpad(col('CNPJ IF'), 8, '0')) ).otherwise(df["CNPJ IF"]))


        for row_iterator in df2.collect():
            print(row_iterator["CNPJ IF"])



        # Create an in-memory DataFrame to query
        df.createOrReplaceTempView("upload_csv")



       
        csv_data = spark.sql("""SELECT * FROM upload_csv WHERE `CNPJ IF` IS NOT NULL AND `CNPJ IF` != '' AND `CNPJ IF` != ' '""")
        #csv_data = spark.sql("""SELECT cnpj FROM upload_csv""")

        #print(csv_data.show())

        # Write the results to the specified output URI
        csv_data.write.option("sep",";").option("header", "true").mode("overwrite").csv(output_uri)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_source', help="s3://exercicio04/raw/CSV/")    
    parser.add_argument(
        '--output_uri', help="s3://exercicio04/output/trusted/csv")
    args = parser.parse_args()

    upload_csv_raw(args.data_source, args.output_uri)
			