CREATE TABLE fato2 AS SELECT CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,CodigoServico FROM default.api_dados_trusted WHERE CNPJ!='' GROUP BY CNPJ, CodigoServico;
INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato2/fato2'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM fato2;

CREATE TABLE dimservicos AS SELECT CodigoServico,COLLECT_SET(Servico)[0] AS Servico FROM default.api_dados_trusted GROUP BY CodigoServico;
INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato2/dimservicos'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM dimservicos;