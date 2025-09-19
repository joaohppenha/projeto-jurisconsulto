CREATE DATABASE cadastro_clientes;

USE cadastro_clientes;

-- DADOS DOS CLIENTES

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_cadastro DATE
);

-- ENDEREÇO DOS CLIENTES

CREATE TABLE IF NOT EXISTS enderecos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    estado CHAR(2),
    cep VARCHAR(10),
    tipo ENUM('Residencial', 'Comercial', 'Outros') DEFAULT 'Residencial',
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- DADOS DO PREOCESSO

CREATE TABLE IF NOT EXISTS processos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    numero_processo VARCHAR(50) UNIQUE,
    tipo_processo VARCHAR(100),
    tipo_acao VARCHAR(100), -- Nova coluna adicionada aqui
    descricao TEXT,
    data_inicio DATE DEFAULT (CURRENT_DATE),
    status ENUM('Ativo', 'Encerrado', 'Arquivado') DEFAULT 'Ativo',
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);
CREATE TABLE reus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    CONSTRAINT fk_reus_clientes 
        FOREIGN KEY (cliente_id) 
        REFERENCES clientes(id)
);




