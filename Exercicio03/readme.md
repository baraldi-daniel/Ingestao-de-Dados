# Exercício 03

## AWS EC2 e MySQL

### EC2 (Amazon Linux) com Airflow e DBT instalados e configurados

![image](https://user-images.githubusercontent.com/108779870/180909961-bafb362c-6623-4998-a684-027001b6ae02.png)
![image](https://user-images.githubusercontent.com/108779870/180910586-df5da75d-416d-4c27-9384-8930c1885d7d.png)
![image](https://user-images.githubusercontent.com/108779870/180910634-3b19d5b0-6b70-49f0-b394-a6cc834feb22.png)

### MySQL na AWS

![image](https://user-images.githubusercontent.com/108779870/180911045-aee37ed3-45aa-452c-aed0-83fc5d221132.png)

### Acesso ao MySQL na AWS usando DBeaver

![image](https://user-images.githubusercontent.com/108779870/180913090-4911df66-c9b2-4299-b840-fd1860e2cc0a.png)

OBS: É necessário realizar uma configuração para acesso ao MySQL e para conexão entre EC2 e MySQL usando as inbound rules e adicionando o IP privado da instância EC2

![image](https://user-images.githubusercontent.com/108779870/180917635-5b5d2e30-85b9-4f81-a20e-8eea8b0b7a81.png)


## Scripts em Python e DBT

### Scripts em Python para manipulação dos dados e criação das tabelas para Stage:

![image](https://user-images.githubusercontent.com/108779870/180912127-4986e918-b3c6-4d78-8158-ca4d0a99d53d.png)
![image](https://user-images.githubusercontent.com/108779870/180912276-cb0ef301-adad-41c0-82df-eff3f2cb12bf.png)
![image](https://user-images.githubusercontent.com/108779870/180912341-c301e944-b5e9-4f7c-99b9-b6ea2d6109e4.png)
![image](https://user-images.githubusercontent.com/108779870/180912399-aa173d62-0855-491f-9e6d-bee40381e155.png)
![image](https://user-images.githubusercontent.com/108779870/180912490-52d27dfe-83f9-46ac-b128-364bca31fc93.png)
![image](https://user-images.githubusercontent.com/108779870/180912524-b837a5af-f15d-4b7e-8027-d25c2e5c9cc7.png)


### Uso do DBT para modelagem star schema:

![image](https://user-images.githubusercontent.com/108779870/180912600-0dadc393-bc3f-418b-b9b0-7d6d1f61305f.png)
![image](https://user-images.githubusercontent.com/108779870/180912619-fc48b4a3-00f8-43d4-891e-25549a7dbba9.png)
![image](https://user-images.githubusercontent.com/108779870/180912649-d207505e-5987-4d32-808f-65d1ae763aa6.png)
![image](https://user-images.githubusercontent.com/108779870/180912673-1e1506d9-1027-456d-9e0d-025471152fc8.png)
![image](https://user-images.githubusercontent.com/108779870/180912695-4bf1cbe7-e247-424f-9884-2500d02892a0.png)
![image](https://user-images.githubusercontent.com/108779870/180912709-779a1203-f64e-4657-b09b-aeb30287d390.png)
![image](https://user-images.githubusercontent.com/108779870/180912750-8d96902c-5109-4d38-a183-71c4b88bf3bf.png)

## Airflow para Workflow

### Executando o Airflow:

![image](https://user-images.githubusercontent.com/108779870/180914381-5e68462d-b6c1-4415-9d83-f0282fcc4044.png)
![image](https://user-images.githubusercontent.com/108779870/180914394-a069b0c4-2db5-4074-9e19-fcb5c508369e.png)
![image](https://user-images.githubusercontent.com/108779870/180914483-b55cc2db-f8bf-43df-9399-624c905ffe1a.png)
![image](https://user-images.githubusercontent.com/108779870/180914569-b0d7ddea-fa8b-4110-b22d-daacccae7614.png)
![image](https://user-images.githubusercontent.com/108779870/180914603-dffd6478-9465-44ae-bff1-d0e403961e6a.png)
![image](https://user-images.githubusercontent.com/108779870/180914643-17bbe64f-be9f-4f4e-95ff-758832fb8153.png)
![image](https://user-images.githubusercontent.com/108779870/180914672-683ec267-25eb-4b37-9d9c-3966a9b7c4cd.png)
![image](https://user-images.githubusercontent.com/108779870/180915107-6e24e456-55db-403d-bc6f-dba1616e8883.png)
![image](https://user-images.githubusercontent.com/108779870/180915747-77d2a6af-cbc5-4ab8-8e9d-386da2b4d2b2.png)

### Verificação da criação das tabelas pelo DBeaver:

![image](https://user-images.githubusercontent.com/108779870/180915272-7e0198fa-f629-468a-852f-93b80d9a5301.png)

## Exibição dos Dados no Tableau

### Configuração no Tableau e relacionamento entre tabelas:

![image](https://user-images.githubusercontent.com/108779870/180915353-67fdc4b0-c448-44ac-8309-41bb81e6ac39.png)

### Visualização no Tableau:

![image](https://user-images.githubusercontent.com/108779870/180915396-f316a65c-85f6-4e5b-b074-845937cd63eb.png)
![image](https://user-images.githubusercontent.com/108779870/180915414-2a17131d-988f-465f-9a0e-7d26dbe66b90.png)
![image](https://user-images.githubusercontent.com/108779870/180915429-cc9cdb33-1c2e-4211-ac00-5de3df879a0c.png)

## Referências:

  https://towardsdatascience.com/creating-an-environment-with-airflow-and-dbt-on-aws-part-1-ca13bc95f479
  https://towardsdatascience.com/creating-an-environment-with-airflow-and-dbt-on-aws-part-2-a23617d56eeb
  https://towardsdatascience.com/creating-an-environment-with-airflow-and-dbt-on-aws-part-3-2789f35adb5d
