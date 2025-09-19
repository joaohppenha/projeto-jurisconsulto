USE cadastro_clientes;

-- Alimentando dados da Tabela clientes

INSERT INTO clientes (nome, cpf_cnpj, email, telefone) VALUES
('Ana Beatriz Silva',        '12345678900', 'ana.silva@email.com',      '(11) 91234-5678'),
('Bruno Carvalho',           '98765432100', 'bruno.carvalho@email.com', '(21) 97654-3210'),
('Carla Mendes',             '32165498700', 'carla.mendes@email.com',   '(31) 99887-7766'),
('Daniel Souza',             '45612378900', 'daniel.souza@email.com',   '(41) 91212-3434'),
('Eduarda Lima',             '78912345600', 'edu.lima@email.com',       '(51) 93456-7890'),
('Felipe Torres',            '23456789100', 'felipe.torres@email.com',  '(61) 95678-1234'),
('Giovana Rocha',            '65478912300', 'giovana.rocha@email.com',  '(71) 97890-4567'),
('Henrique Vasconcelos',     '15975348600', 'henrique.vas@email.com',   '(81) 91111-2222'),
('Isabela Martins',          '75315985200', 'isa.martins@email.com',    '(91) 92222-3333'),
('João Pedro Almeida',       '85245696300', 'joao.pedro@email.com',     '(31) 93333-4444');

-- Alimentando dados da Tabela enderecos

INSERT INTO enderecos (cliente_id, logradouro, numero, bairro, cidade, estado, cep, tipo) VALUES
(1, 'Rua das Flores', '123', 'Jardim Primavera', 'São Paulo', 'SP', '01001-000', 'Residencial'),
(1, 'Av. Brasil', '456', 'Centro', 'São Paulo', 'SP', '01002-000', 'Comercial'),
(2, 'Rua do Sol', '789', 'Bela Vista', 'Rio de Janeiro', 'RJ', '20001-000', 'Residencial'),
(3, 'Alameda Santos', '321', 'Jardins', 'São Paulo', 'SP', '01419-000', 'Residencial'),
(4, 'Rua das Acácias', '654', 'Centro', 'Curitiba', 'PR', '80010-000', 'Residencial'),
(5, 'Rua das Palmeiras', '987', 'Boa Vista', 'Porto Alegre', 'RS', '90020-000', 'Residencial'),
(6, 'Av. Paulista', '1000', 'Bela Vista', 'São Paulo', 'SP', '01310-000', 'Comercial'),
(7, 'Rua das Orquídeas', '234', 'Centro', 'Salvador', 'BA', '40010-000', 'Residencial'),
(8, 'Rua das Laranjeiras', '567', 'Centro', 'Recife', 'PE', '50010-000', 'Residencial'),
(9, 'Rua do Comércio', '890', 'Boa Vista', 'Fortaleza', 'CE', '60020-000', 'Comercial');

-- Alimentando dados da Tabela processos

INSERT INTO processos (cliente_id, numero_processo, tipo_processo, tipo_acao, descricao, data_inicio, status) VALUES
(1, '0001234-56.2023.8.26.0000', 'Cível', 'Ação de Cobrança', 'Cobrança de dívida referente a contrato.', '2023-01-10', 'Ativo'),
(2, '0001235-56.2023.8.26.0000', 'Trabalhista', 'Ação Trabalhista', 'Reclamação trabalhista por horas extras.', '2023-02-15', 'Ativo'),
(3, '0001236-56.2023.8.26.0000', 'Cível', 'Ação de Indenização', 'Indenização por acidente de trânsito.', '2023-03-20', 'Ativo'),
(4, '0001237-56.2023.8.26.0000', 'Penal', 'Ação Penal', 'Defesa em processo penal.', '2023-04-05', 'Ativo'),
(5, '0001238-56.2023.8.26.0000', 'Cível', 'Habeas Corpus', 'Pedido de habeas corpus em favor do cliente.', '2023-05-12', 'Ativo'),
(6, '0001239-56.2023.8.26.0000', 'Cível', 'Mandado de Segurança', 'Mandado de segurança contra ato administrativo.', '2023-06-18', 'Ativo'),
(7, '0001240-56.2023.8.26.0000', 'Cível', 'Ação Declaratória', 'Ação declaratória de inexistência de débito.', '2023-07-22', 'Ativo'),
(8, '0001241-56.2023.8.26.0000', 'Trabalhista', 'Ação Trabalhista', 'Reclamação por verbas rescisórias.', '2023-08-30', 'Ativo'),
(9, '0001242-56.2023.8.26.0000', 'Cível', 'Ação de Cobrança', 'Cobrança referente a serviços prestados.', '2023-09-10', 'Ativo'),
(10, '0001243-56.2023.8.26.0000', 'Cível', 'Ação de Indenização', 'Indenização por danos morais.', '2023-09-25', 'Ativo');

-- Alimentando dodos dos reus


INSERT INTO reus (cliente_id, nome, cpf_cnpj, email, telefone, endereco) VALUES
(1, 'Empresa Alfa Ltda',       '12345678000199', 'contato@alfa.com',          '(11) 3000-1000', 'Rua Industrial, 100 - São Paulo/SP'),
(1, 'Carlos Pereira',           '98765432111',    'carlos.pereira@email.com',  '(11) 98888-7777', 'Av. Central, 55 - São Paulo/SP'),
(2, 'Construtora Beta S/A',     '11222333000188', 'juridico@betasa.com',       '(21) 3999-2000', 'Av. das Américas, 500 - Rio de Janeiro/RJ'),
(3, 'Loja Gama ME',              '22334455000177', 'financeiro@gamame.com',     '(31) 3555-9090', 'Rua do Comércio, 77 - Belo Horizonte/MG'),
(4, 'João Ribeiro',              '11122233344',    'joao.ribeiro@email.com',    '(41) 97777-1111', 'Rua XV de Novembro, 200 - Curitiba/PR'),
(4, 'Clínica Vida Plena',        '33445566000155', 'contato@vidaplena.com',     '(41) 3222-3344', 'Av. Batel, 400 - Curitiba/PR'),
(5, 'Maria Fernanda Rocha',      '99988877766',    'maria.fr@email.com',        '(51) 96666-5555', 'Rua da Praia, 12 - Porto Alegre/RS'),
(6, 'Tech Solutions Ltda',       '55667788000144', 'suporte@techsolutions.com', '(61) 3111-4455', 'SCS Quadra 2, Bloco A - Brasília/DF'),
(7, 'Cooperativa Rural Sol',     '66778899000133', 'cooperativa@ruralsol.com',  '(71) 3888-9988', 'Estrada do Coco, km 12 - Lauro de Freitas/BA'),
(7, 'Pedro Henrique Oliveira',   '22233344455',    'pedro.henrique@email.com',  '(71) 95555-3333', 'Rua das Bromélias, 45 - Salvador/BA'),
(8, 'Hospital Santa Luzia',      '77889900000122', 'contato@santaluzia.com',    '(81) 3222-7788', 'Av. Boa Viagem, 999 - Recife/PE'),
(9, 'Translog Transportes',      '88990011000111', 'logistica@translog.com',    '(85) 3777-2222', 'Rod. BR-116, km 10 - Fortaleza/CE'),
(10, 'Editora Nova Era',          '99001122000100', 'contato@novaera.com',       '(31) 3888-4444', 'Av. Afonso Pena, 1200 - Belo Horizonte/MG'),
(10, 'Lucas Andrade',              '33322211100',   'lucas.andrade@email.com',   '(31) 96666-0000', 'Rua dos Pinheiros, 89 - Belo Horizonte/MG');

