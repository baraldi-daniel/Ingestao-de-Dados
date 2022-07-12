# Ingestao-de-Dados
## Exercício 1:

### O Exercício tem o objetivo de usar ferramentas de ETL, um banco de dados relacional e uma ferramenta de visualização para usar e tratar dados de duas bases (um CSV e a resposta de uma chamada de API).
### As ferramentas usada para esse caso foram, respectivamente, Talend (ETL), MySQL (Base de Dados relacional) e Grafana (Dashboard).

### Com isso, os Jobs utilizados no TALEND foram os seguintes:

Job Geral:
![image](https://user-images.githubusercontent.com/108779870/178613333-867c57dc-e98c-4e15-805d-9f59d6701e22.png)

Job Consolidação CSV:
![image](https://user-images.githubusercontent.com/108779870/178613388-1deca0e7-2e86-4c3b-b144-b7afdbe44b85.png)

Job Consolidação API e Transferência para DB:
![image](https://user-images.githubusercontent.com/108779870/178613514-ea37b430-71aa-49df-a666-b4ecb332f76e.png)

   - Job API Call:
   ![image](https://user-images.githubusercontent.com/108779870/178613556-9fa236fb-1c66-4f8a-bf91-46e82ed65aca.png)

   - Job Consolidação Dados API:
   ![image](https://user-images.githubusercontent.com/108779870/178613708-f1cf1b7e-f123-4f04-aa20-5d52a8c9650d.png)

Job Transferência Dados API Consolidados para DB:
![image](https://user-images.githubusercontent.com/108779870/178613750-0b0834d0-a873-4aef-be9c-70f99fee0945.png)

Job Junção de Bases e Transferência para DB:
![image](https://user-images.githubusercontent.com/108779870/178613791-fce2dfda-fc29-4bdd-b2dc-e5307b0b7321.png)

### Esses Jobs realizam registros locais como estágios de checagem salvando arquivos localmente.

### Os dados são registrados em um Database MySQL, com três tabelas distintas (csv, apidadoscoletados, csvapidadoscoletados), conforme abaixo:

### csv:
![image](https://user-images.githubusercontent.com/108779870/178614990-bb2e257c-aa34-4344-a5a7-cede6fabe17b.png)

### apidadoscoletados:
![image](https://user-images.githubusercontent.com/108779870/178615046-64a03d29-347d-42e3-a677-5e842f9cc03f.png)

### csvapidadoscoletados:
![image](https://user-images.githubusercontent.com/108779870/178615099-4804be80-6944-4925-89a1-cf53eef08507.png)

### Os arquivos de exemplo estão nas pastas dentro das pasta Exercício 01.

### Para a visualização dos dados, foi utilizado o Grafana, conforme abaixo, com três gráficos (um com a base csv consolidada, outro com a base de dados da API consolidada e um terceiro com a junção das duas bases): 

Grafana antes da execução dos Jobs:
![image](https://user-images.githubusercontent.com/108779870/178615583-90c17980-1a57-4afc-a84c-3b8e510fabb6.png)

Grafana após a execução dos Jobs:
![image](https://user-images.githubusercontent.com/108779870/178617324-b938eec3-fc93-40fd-a0e0-d71f0c06e419.png)
![image](https://user-images.githubusercontent.com/108779870/178617358-b3e708f8-cfc7-45b5-8716-143b9ff87a7a.png)
![image](https://user-images.githubusercontent.com/108779870/178617393-af79cc8f-96ea-4d60-ad26-fdb69550ec23.png)

