**Projeto Jurisconsulto**

Jurisconsulto é um projeto que trabalha com modelagem, inserção, consulta de dados estruturados e a criação de um Sistema de gerenciamento de clientes de um escritíório de advocacia.

**Resumo do Projeto**

**O Problema**

⦁Um escritório de advocacia tinha uma série de dados de seus clientes e precisava organizar informações pessoais, endereços, dos processos e dos réus. Além disso precisava obter dados sobre ações mais comuns, cliente e processo, os que ajuizaram ações de cobrança e de indenização, o número por estado e processos ativos para entregar para o estagiário fazer a visualização de dados. Outra questão era que os advogados perdiam muito tempo qualificando as partes quando redigiam suas Petições Iniciais.

**Execução do Projeto**

⦁A solução cabia em um projeto de dados

⦁O Primeiro passo foi a utilização da ferramenta MYSQL. Um primeiro script Tables.sql foi criado com um banco de dados chamado cadastro\_clientes e quatro tabelas foram : clientes, enderecos, processos e reus, fazendo a modelagem dos dados;

⦁Depois, um segundo script data\_insert.sql, no qual foram inseridos os dados dos clientes nas quatro tabelas, organizando as informações;

⦁Com as informações organizadas, era possível obter as aquelas requeridas ao estagiário a partir da consulta de dados. Para isso, um terceiro script data\_visualization.sql utilizando as variações dos comandos SELECT e JOIN. Todos os resultados foram exportados no formato .CSV e entregues ao estagiário;

⦁Para Entender melhor o Banco, foi criado um Um Diagrama de Entidade-Relacionamento do banco de dados;

⦁Para facilitar e manter os dados organizados, foi criado uma aplicação de linha de comando em Python Jurisconsulto.py integrado ao MYSQL utilizando o mysql-connector-python que permite a inserção de dados direto do terminal para o banco de dados cadastro\_clientes. Também é possível a consulta de todos os dados do Cliente apenas digitando o seu nome em formato de tabela, utilizando o tabulate;

⦁Para resolver o problema da Qualificação das Partes na Petição Inicial, foi criada uma função dentro do Jurisconsulto.py que permite a criação automática e que exporta um documento no formato .txt.

**Tecnologias Utilizadas**

⦁**MySQL**: Sistema de gerenciamento de banco de dados.

⦁**SQL**: Linguagem para a criação e manipulação do banco de dados.

⦁**Python**: Linguagem de programação principal.

⦁**mysql-connector-python:** Biblioteca Python para conexão com o MySQL.

⦁**tabulate**: Biblioteca Python para exibir dados em formato de tabela.

**Estrutura do Projeto**

**1 - Banco de Dados Estruturados SQL**

⦁**/Scripts**: scripts em SQL com dados

⦁**Tables.sql**: Script SQL para a criação das tabelas no banco de dados (clientes, enderecos, processos, reus).

⦁**data\_Insert.sql**: Script SQL que insere os dados de exemplo para popular as tabelas.

⦁**data\_visualization.sql**: Script SQL Consultas SQL de para gerar relatórios e análises sobre os dados, como o número de clientes por estado ou o tipo de ação mais comum.

⦁**/Docs**: outros documentos

⦁**CSV results**: Pasta com arquivos CSV dos resultados das consultas feitas no script data\_visualization.sql

⦁**/ERD**:

⦁**ERD.PNG**: arquivo de imagem com um Um Diagrama de Entidade-Relacionamento do banco de dados

**2 - Aplicação em Python**

⦁**/Jurisconsulto\_ap**p:

⦁j**urisconsulto.py**: é uma aplicação de linha de comando desenvolvida em Python para auxiliar advogados e escritórios de advocacia na gestão de seus clientes e processos

**Instruções da aplicação Jurisconsulto.py**

**Funcionalidades**

⦁Cadastro Completo: Insere dados de clientes, seus endereços, processos e réus.

⦁Consultas Rápidas: Permite buscar clientes pelo nome e visualizar seus dados de forma organizada.

⦁Geração Automática de Documentos: Cria qualificações de petições iniciais com base nos dados cadastrados, agilizando o trabalho.

⦁Visualização de Dados: Inclui scripts SQL para gerar relatórios e análises, como a quantidade de clientes por estado ou o tipo de ação mais comum.

**Configuração e Instalação**

Para rodar o projeto em seu ambiente local, siga estes passos.

**1\. Pré-requisitos**

Certifique-se de ter o Python e o MySQL instalados em sua máquina.

**2\. Configuração do Banco de Dados**

⦁Acesse seu servidor MySQL.

⦁Execute o script Tables.sql para criar o banco de dados cadastro\_clientes e todas as tabelas necessárias:

⦁(Opcional) Para popular as tabelas com dados de exemplo, execute o script data\_Insert.sql:

**3\. Configuração do Ambiente Python**

⦁Baixe os arquivos do projeto.

⦁Instale as bibliotecas Python necessárias com pip:

pip install mysql-connector-python

pip install tabulate

⦁No arquivo Juriconsulto.py, configure os dados de conexão com seu banco de dados (host, usuário, senha, etc.).

**Como Usar**

Execute o arquivo principal Jurisconsulto.py no terminal para iniciar a aplicação:\]

**O menu principal será exibido com as seguintes opções:**

**1 - Cadastrar cliente: Inicia o processo de cadastro completo.**

**2 - Consultar cadastro do cliente: Busca e exibe os dados de um cliente.**

**3 - Criar qualificação de petição inicial: Gera um texto de qualificação para petição.**

**0 - Sair: Encerra o programa.**

**Desenvolvedor do projeto:**

João Henrique Pereira da Penha

jhppenha@gmail.com

https://github.com/joaohppenha
