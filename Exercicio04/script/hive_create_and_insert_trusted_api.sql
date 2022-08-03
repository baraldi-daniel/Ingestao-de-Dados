CREATE TABLE api_dados_trusted AS SELECT CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,CodigoServico,DataVigencia,Periodicidade,Servico,TipoValor,Unidade,ValorMaximo FROM default.api_dados_raw WHERE CNPJ!='';

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/raw/api/'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM api_dados_trusted;