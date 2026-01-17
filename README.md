# <span style="font-size:20pt"><b>Portfólio de Projetos de Banco de Dados</b></span>

## Projetos Incluídos

1. **Fundamentos de SQL**  
2. **Jurisconsulto**  

---

# <span style="font-size:20pt"><b>Projeto: Fundamentos de SQL</b></span>

## Sobre o Projeto

Este projeto foi desenvolvido para demonstrar conhecimentos fundamentais de **SQL** aplicados em um cenário real de **gestão escolar**. O objetivo foi criar um banco de dados completo com tabelas de alunos, professores, disciplinas, turmas, matrículas e avaliações, utilizando **BigQuery** como ambiente de execução.  

O projeto foi dividido em cinco partes principais, cada uma representando uma categoria de comandos SQL:  

---

## **1. DDL (Data Definition Language)**

- Criação de **dataset** e **tabelas**.  
- Alterações em colunas e adição de descrições.  
- Comandos utilizados: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`.  

---

## **2. DML (Data Manipulation Language)**

- Inserção de registros com `INSERT`.  
- Modificação de dados com `UPDATE`.  
- Remoção de dados com `DELETE` e `TRUNCATE`.  

---

## **3. DQL (Data Query Language)**

- Consultas simples e filtradas (`SELECT`, `WHERE`).  
- Agregações e condições (`GROUP BY`, `HAVING`).  
- Ordenações (`ORDER BY`).  
- Relacionamento entre tabelas com `JOIN`.  

---

## **4. DCL (Data Control Language)**

- Controle de permissões e segurança (`GRANT`, `REVOKE`).  
- Controle em nível de **dataset** e **tabela**.  

---

## **5. DTL (Data Transaction Language)**

- Controle de transações (`BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`).  
- Garantia de **integridade e consistência** em múltiplas operações DML.  

---

## **Tecnologias Utilizadas**

- **SQL**: Linguagem para manipulação, definição, consulta e controle de dados.  
- **BigQuery**: Ambiente de execução em nuvem para armazenamento e análise de dados.  
- **Google Cloud Platform (GCP)**: Gerenciamento de datasets e exportação de resultados.  

---

# <span style="font-size:20pt"><b>Projeto: Jurisconsulto</b></span>

## Sobre o Projeto

**Jurisconsulto** é um projeto que trabalha com **modelagem, inserção e consulta de dados estruturados**, além da criação de um **Sistema de Gerenciamento de Clientes** para um escritório de advocacia.  

O objetivo foi organizar informações de clientes, endereços, processos e réus, permitindo consultas rápidas e geração automática de qualificações de petições iniciais.

---

## **Resumo do Projeto**

### O Problema

- Organizar informações pessoais, endereços, processos e réus.  
- Obter dados sobre ações mais comuns, clientes e processos:  
  - Clientes que ajuizaram ações de cobrança e indenização.  
  - Número de processos por estado.  
  - Processos ativos para análise de dados por estagiários.  
- Reduzir tempo gasto pelos advogados na **qualificação de partes** ao redigir Petições Iniciais.  

### Execução do Projeto

1. Criação do banco de dados `cadastro_clientes` e quatro tabelas: **clientes, enderecos, processos, reus** (`Tables.sql`).  
2. Inserção de dados nas tabelas (`data_insert.sql`).  
3. Consultas e geração de relatórios (`data_visualization.sql`) com `SELECT` e `JOIN`, exportados em **CSV**.  
4. Criação de um **Diagrama de Entidade-Relacionamento (ERD)**.  
5. Desenvolvimento de **Jurisconsulto.py**, aplicação de linha de comando em Python, integrando-se ao MySQL:  
   - Inserção de dados via terminal.  
   - Consulta de clientes digitando apenas o nome.  
   - Exibição organizada em tabela (`tabulate`).  
6. Função para **geração automática de qualificações de petições iniciais**, exportando arquivos `.txt`.  

---

## **Tecnologias Utilizadas**

- **MySQL**: Sistema de gerenciamento de banco de dados.  
- **SQL**: Criação e manipulação do banco de dados.  
- **Python**: Linguagem principal para a aplicação.  
- **mysql-connector-python**: Conexão Python com MySQL.  
- **tabulate**: Exibição de dados em tabela no terminal.  

---

## **Estrutura do Projeto**

### Banco de Dados

- **/Scripts**  
  - `Tables.sql`: Criação das tabelas (**clientes, enderecos, processos, reus**).  
  - `data_insert.sql`: Inserção de dados de exemplo.  
  - `data_visualization.sql`: Consultas SQL para relatórios e análises.  
- **/Docs**  
  - `CSV results`: Arquivos CSV dos resultados das consultas.  
- **/ERD**  
  - `ERD.PNG`: Diagrama de Entidade-Relacionamento.  

### Aplicação em Python

- **/Jurisconsulto_app**  
  - `Jurisconsulto.py`: Linha de comando para gestão de clientes e processos.  

---

## **Instruções da Aplicação Jurisconsulto.py**

### Funcionalidades

- Cadastro completo de clientes, endereços, processos e réus.  
- Consultas rápidas de clientes pelo nome.  
- Geração automática de qualificações de petições iniciais (`.txt`).  
- Visualização de dados: relatórios por estado ou tipo de ação mais comum.  

### Configuração e Instalação

1. Certifique-se de ter **Python** e **MySQL** instalados.  
2. Execute `Tables.sql` para criar o banco e tabelas.  
3. (Opcional) Execute `data_insert.sql` para popular as tabelas.  
4. Instale bibliotecas Python:  
   ```bash
   pip install mysql-connector-python
   pip install tabulate
5. Configure a conexão com o MySQL no arquivo `Jurisconsulto.py`, definindo:  

```python
host = "seu_host"
user = "seu_usuario"
password = "sua_senha"
database = "cadastro_clientes"
## Como Usar

Execute o arquivo principal `Jurisconsulto.py` no terminal. O menu exibirá as seguintes opções:

1. **Cadastrar cliente**: Inicia o cadastro completo de clientes, endereços, processos e réus.  
2. **Consultar cadastro do cliente**: Busca e exibe os dados de um cliente de forma organizada.  
3. **Criar qualificação de petição inicial**: Gera automaticamente um documento `.txt` com a qualificação para petição.  
0. **Sair**: Encerra a aplicação.  

---

## Desenvolvedor do Projeto

**João Henrique Pereira da Penha**  
- Email: jhppenha@gmail.com  
- GitHub: [https://github.com/joaohppenha]
(https://github.com/joaohppenha)
