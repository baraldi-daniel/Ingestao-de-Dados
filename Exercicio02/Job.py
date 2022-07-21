#Job executar arquivos .py

#Importar arquivo para criação do database
import database.create_database_mysql

#Importar arquivos para criação das tabelas stage
import criacao_tabelas_stage.mysql_create_table_csv
import criacao_tabelas_stage.mysql_create_table_api

#Importar arquivos para insercao nas tabelas stage
import insercao_tabelas_stage.read_csv_file_mysql
import insercao_tabelas_stage.read_api_data_mysql

#Importar arquivos para criacao de tabelas fato1 e dim
import criacao_fato1_dim.mysql_create_fato1
import criacao_fato1_dim.dimcategoria
import criacao_fato1_dim.diminstituicao
import criacao_fato1_dim.dimperiodo
import criacao_fato1_dim.dimtipo

#Importar arquivos para criacao de tabelas fato2 e dim
import criacao_fato2_dim.mysql_create_fato2
import criacao_fato2_dim.dimservicos

#Importar arquivos para insercao nas tabelas fato1 e fato2
import insercao_fato1e2.insert_fato1
import insercao_fato1e2.insert_fato2


#-----------------------------------------------------------------

#1) Criacao do database
database.create_database_mysql


#2) Criar tabelas stage
criacao_tabelas_stage.mysql_create_table_csv
criacao_tabelas_stage.mysql_create_table_api

#3) Insercao tabelas stage
insercao_tabelas_stage.read_csv_file_mysql
insercao_tabelas_stage.read_api_data_mysql

#4) Criacao fato1 e dim
criacao_fato1_dim.mysql_create_fato1
criacao_fato1_dim.dimcategoria
criacao_fato1_dim.diminstituicao
criacao_fato1_dim.dimperiodo
criacao_fato1_dim.dimtipo

#5) Criacao fato2 e dim
criacao_fato2_dim.mysql_create_fato2
criacao_fato2_dim.dimservicos

#6) Insercao dados fato1 e fato2
insercao_fato1e2.insert_fato1
insercao_fato1e2.insert_fato2