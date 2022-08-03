CREATE TABLE fato1 AS SELECT CONCAT(Ano,Trimestre) AS CHAVEPERIODO,CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,QuantidadeReclamacoesReguladasProcedentes FROM default.csv WHERE CNPJ!='';

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato1/fato1'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM fato1;


CREATE TABLE dimcategoria AS SELECT CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,COLLECT_SET(Categoria)[0] AS Categoria FROM default.csv WHERE CNPJ!='' GROUP BY CNPJ;

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato1/dimcategoria'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM dimcategoria;


CREATE TABLE diminstituicao AS SELECT CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,COLLECT_SET(InstituicaoFinanceira)[0] AS InstituicaoFinanceira FROM default.csv WHERE CNPJ!='' GROUP BY CNPJ ORDER BY InstituicaoFinanceira;

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato1/diminstituicao'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM diminstituicao;

CREATE TABLE dimperiodo AS SELECT CONCAT(Ano,Trimestre) AS CHAVEPERIODO,Ano,Trimestre FROM default.csv;

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato1/dimperiodo'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM dimperiodo;


CREATE TABLE dimtipo AS SELECT CONCAT(LPAD(CNPJ,8,'0')) AS CNPJ,COLLECT_SET(Tipo)[0] AS Tipo FROM default.csv WHERE CNPJ!='' GROUP BY CNPJ;

INSERT OVERWRITE DIRECTORY 's3://exercicio04/output/analytics/fato1/dimtipo'
ROW FORMAT DELIMITED FIELDS TERMINATED BY ';'
SELECT * FROM dimtipo;