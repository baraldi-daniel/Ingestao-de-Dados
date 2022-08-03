CREATE EXTERNAL TABLE IF NOT EXISTS csv (
       Ano VARCHAR(255),
       Trimestre VARCHAR(255),
       Categoria VARCHAR(255),
       Tipo VARCHAR(255),
       CNPJ VARCHAR(255),
       InstituicaoFinanceira VARCHAR(255),
       Indice VARCHAR(255),
       QuantidadeReclamacoesReguladasProcedentes INT,
       QuantidadeReclamacoesReguladasOutras VARCHAR(255),
       QuantidadeReclamacoesNaoReguladas VARCHAR(255),
       QuantidadeTotalReclamacoes VARCHAR(255),
       QuantidadeTotalClientesCCSSCR VARCHAR(255),
       QuantidadeClientesCCS VARCHAR(255),
       QuantidadeClientesSCR VARCHAR(255))
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';'
STORED AS TEXTFILE
LOCATION 's3://exercicio04/output/trusted/'
tblproperties("skip.header.line.count"="1",'serialization.encoding'='ISO-8859-1');