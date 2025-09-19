import mysql.connector
from tabulate import tabulate
import getpass

#  Conexão com o Banco de Dados cadastro_clientes que armazena as informações sobre os clientes

def conectar_banco(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Vamos alimentar o banco de dados e suas 4 tabelas: 'clientes', que vai conter os dados pessoais do Cliente
# "endereço", o seu domicílio ou sede, 'processo' que vai conter os dados sobre a ação do cliente
# 'Reus", se possível, o cadastro sobre contra quem a ação será ajuizada

# Funções de Input Para colocar os dados do Cliente e alimentar a tabela 'clientes'
def input_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ").strip()
    cpf_cnpj = input("CPF/CNPJ: ").strip()
    email = input("Email: ").strip()
    telefone = input("Telefone: ").strip()
    return {"nome": nome, "cpf_cnpj": cpf_cnpj, "email": email, "telefone": telefone}

# Funções de Input Para colocar os dados do Cliente e alimentar a tabela 'endereco'

def input_endereco():
    print("\n--- Cadastro de Endereço ---")
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado (UF): ").strip()
    cep = input("CEP: ").strip()
    tipo = input("Tipo (Residencial, Comercial, Outros): ").strip()
    if tipo.lower() not in ['residencial', 'comercial', 'outros']:
        tipo = 'Residencial'
    return {
        "logradouro": logradouro,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado.upper(),
        "cep": cep,
        "tipo": tipo.capitalize()
    }

# Funções de Input Para colocar os dados do Cliente e alimentar a tabela 'processo'

def input_processo():
    print("\n--- Cadastro de Processo ---")
    numero_processo = input("Número do Processo: ").strip()
    tipo_acao = input("Tipo de Ação: ").strip().upper()  # Convertido para maiúsculas
    return {"numero_processo": numero_processo, "tipo_acao": tipo_acao}

# Funções de Input Para colocar os dados do Cliente e alimentar a tabela 'reus'

def input_reus():
    reus = []
    while True:
        print("\n--- Cadastro de Réu ---")
        nome = input("Nome: ").strip()
        cpf_cnpj = input("CPF/CNPJ: ").strip()
        email = input("Email: ").strip()
        telefone = input("Telefone: ").strip()
        endereco = input("Endereço: ").strip()
        reus.append({
            "nome": nome,
            "cpf_cnpj": cpf_cnpj,
            "email": email,
            "telefone": telefone,
            "endereco": endereco
        })
        if input("Deseja cadastrar outro réu? (S/N): ").strip().lower() != 's':
            break
    return reus

# Função para mostrar os dados adicionados

def revisar_dados(titulo, dados):
    print(f"\n--- Revisão dos dados: {titulo} ---")
    if isinstance(dados, list):
        for i, item in enumerate(dados, start=1):
            print(f"\nRéu {i}:")
            for k, v in item.items():
                print(f"{k.capitalize()}: {v}")
    else:
        for k, v in dados.items():
            print(f"{k.capitalize()}: {v}")
    print("-----------------------------")

#  Funções de  integração com MYSQL para inserir o cadastro no banco de dados

def cadastrar_cliente(conn, cliente):
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nome, cpf_cnpj, email, telefone) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (cliente["nome"], cliente["cpf_cnpj"], cliente["email"], cliente["telefone"]))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar cliente: {err}")
        return None
    finally:
        cursor.close()

def cadastrar_endereco(conn, cliente_id, endereco):
    cursor = conn.cursor()
    sql = """
    INSERT INTO enderecos (cliente_id, logradouro, numero, bairro, cidade, estado, cep, tipo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (cliente_id, endereco["logradouro"], endereco["numero"], endereco["bairro"],
                             endereco["cidade"], endereco["estado"], endereco["cep"], endereco["tipo"]))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar endereço: {err}")
    finally:
        cursor.close()

def cadastrar_processo(conn, cliente_id, processo):
    cursor = conn.cursor()
    sql = "INSERT INTO processos (cliente_id, numero_processo, tipo_acao) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (cliente_id, processo["numero_processo"], processo["tipo_acao"]))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar processo: {err}")
    finally:
        cursor.close()

def cadastrar_reus(conn, cliente_id, reus):
    cursor = conn.cursor()
    sql = "INSERT INTO reus (cliente_id, nome, cpf_cnpj, email, telefone, endereco) VALUES (%s, %s, %s, %s, %s, %s)"
    try:
        for r in reus:
            cursor.execute(sql, (cliente_id, r["nome"], r["cpf_cnpj"], r["email"], r["telefone"], r["endereco"]))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar réus: {err}")
    finally:
        cursor.close()

#  Consulta: 
#  Segunda Função do menu principal, permite consultar em forma de tabela, 
# todos os dados cadastrados do cliente
# integração com o tabulate 

def consultar_cliente(conn, nome):
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT c.id, c.nome, c.cpf_cnpj, c.email, c.telefone,
           e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep
    FROM clientes c
    LEFT JOIN enderecos e ON c.id = e.cliente_id
    WHERE c.nome LIKE %s
    """
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def exibir_tabela(resultados):
    if not resultados:
        print("Nenhum cliente encontrado.")
        return
    print(tabulate(resultados, headers="keys", tablefmt="grid", showindex=True))

# Funções para Qualificação 
# Terceira opção do Menu Principal ajuda a criar a qualificação das partes, adicionando dados do banco

def buscar_processos(conn, cliente_id):
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT tipo_acao FROM processos WHERE cliente_id = %s"
    cursor.execute(sql, (cliente_id,))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def buscar_reus(conn, cliente_id):
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT nome, cpf_cnpj, endereco FROM reus WHERE cliente_id = %s"
    cursor.execute(sql, (cliente_id,))
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def criar_qualificacao_completa(conn, nome_cliente):
    cursor = conn.cursor(dictionary=True)
    sql_cliente = """
    SELECT c.id, c.nome, c.cpf_cnpj, c.email, c.telefone,
           e.logradouro, e.numero, e.bairro, e.cidade, e.estado, e.cep
    FROM clientes c
    LEFT JOIN enderecos e ON c.id = e.cliente_id
    WHERE c.nome LIKE %s
    """
    cursor.execute(sql_cliente, (f"%{nome_cliente}%",))
    cliente = cursor.fetchone()
    cursor.close()

    if not cliente:
        print("Cliente não encontrado.")
        return

    cliente_id = cliente['id']
    processos = buscar_processos(conn, cliente_id)
    tipos_acao = ", ".join([p['tipo_acao'].upper() for p in processos]) if processos else "NÃO HÁ PROCESSOS CADASTRADOS"

    reus = buscar_reus(conn, cliente_id)
    if reus:
        reus_texto = ", ".join([f"{r['nome']} (CPF/CNPJ: {r['cpf_cnpj']}), endereço: {r['endereco']}" for r in reus])
    else:
        reus_texto = "Não há réus cadastrados."
    endereco_str = f"{cliente.get('logradouro', '')}, {cliente.get('numero', '')}, {cliente.get('bairro', '')}, {cliente.get('cidade', '')} - {cliente.get('estado', '')}, CEP {cliente.get('cep', '')}"

    # Gera o Texto de qualificação das partes 
    texto = (
        f"{cliente['nome']}, portador(a) do CPF/CNPJ {cliente['cpf_cnpj']}, "
        f"residente em {endereco_str}, por intermédio de seu advogado, propõe a presente {tipos_acao}, "
        f"em face de {reus_texto}, pelos motivos de fato e de direito a seguir."
    )

    print("\n--- Qualificação da Petição Inicial ---")
    print(texto)
    print("-----------------------------\n")

    # Exporta o Texto de qualificação das partes em TXT

    salvar = input("Deseja salvar esta qualificação em um arquivo TXT? (S/N): ").strip().lower()
    if salvar == "s":
        nome_arquivo = f"Qualificacao_{cliente['nome'].replace(' ', '_')}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"Qualificação salva em: {nome_arquivo}")

#  Menu Principal - Exibe a primeira tela, primeiro pede a conexão com o banco de dados e depois as 3 opções
# 1 - Cadastra os dados do cliente e alimenta o banco de dados diretamente pelo terminal
# 2 - Consulta todos os dados cadastrados do Cliente
# 3 - Cria um texto e automatiza a qualificação das Partes para a Petição Inicial


def main():
    host = input("Host: ").strip()
    user = input("Usuário: ").strip()
    password = getpass.getpass("Senha: ").strip()  # senha escondida
    database = input("Banco de dados: ").strip()

    try:
        conn = conectar_banco(host, user, password, database)
    except mysql.connector.Error as err:
        print(f"Erro na conexão: {err}")
        return

    while True:
        print ("\n---BEM-VINDO ao Jurisconsulto! - o seu assistente jurídico digital ---")
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Cadastrar cliente")
        print("2 - Consultar cadastro do cliente")
        print("3 - Criar qualificação de petição inicial")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cliente = input_cliente()
            revisar_dados("Cliente", cliente)
            if input("Confirmar cadastro? (S/N): ").strip().lower() != "s":
                continue
            cliente_id = cadastrar_cliente(conn, cliente)
            if cliente_id:
                endereco = input_endereco()
                cadastrar_endereco(conn, cliente_id, endereco)
                processo = input_processo()
                cadastrar_processo(conn, cliente_id, processo)
                reus = input_reus()
                cadastrar_reus(conn, cliente_id, reus)

        elif opcao == "2":
            nome = input("Digite o nome do cliente para consultar: ").strip()
            resultados = consultar_cliente(conn, nome)
            exibir_tabela(resultados)

        elif opcao == "3":
            nome = input("Digite o nome do cliente para gerar qualificação: ").strip()
            criar_qualificacao_completa(conn, nome)

        elif opcao == "0":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

    if conn.is_connected():
        conn.close()

if __name__ == "__main__":
    main()
