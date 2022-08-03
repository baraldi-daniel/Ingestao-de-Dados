CREATE EXTERNAL TABLE IF NOT EXISTS api_dados_raw (
       CNPJ VARCHAR(255),
       CodigoServico VARCHAR(255),
       DataVigencia DATE,
       Periodicidade VARCHAR(255),
       Servico VARCHAR(255),
       TipoValor VARCHAR(255),
       Unidade VARCHAR(255),
       ValorMaximo INT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';'
STORED AS TEXTFILE
LOCATION 's3://exercicio04/raw/api/'
tblproperties("skip.header.line.count"="1",'serialization.encoding'='ISO-8859-1');