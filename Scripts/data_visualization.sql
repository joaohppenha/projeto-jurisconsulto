USE cadastro_clientes;

-- Consulta de número de clientes por estado

SELECT estado, COUNT(DISTINCT cliente_id) AS qtd_clientes
FROM enderecos
GROUP BY estado;

-- Quantidade de Processos ativos por cliente

SELECT c.nome, COUNT(p.id) AS processos_ativos
FROM clientes c
LEFT JOIN processos p ON c.id = p.cliente_id AND p.status = 'Ativo'
GROUP BY c.id;

-- Número de Clientes com Processos

SELECT c.nome, p.numero_processo, p.tipo_acao
FROM clientes c
INNER JOIN processos p ON c.id = p.cliente_id;

-- Tipo de Ação mais comum

SELECT tipo_acao, COUNT(*) AS total
FROM processos
GROUP BY tipo_acao
ORDER BY total DESC
LIMIT 1;

-- Informações sobre Cliente e Processo

SELECT 
  p.numero_processo,
  p.tipo_acao,
  p.status,
  c.nome AS cliente_nome
FROM clientes c
RIGHT JOIN processos p ON c.id = p.cliente_id
ORDER BY p.numero_processo;

-- Clientes com Ação de Cobrança e de Indenização

SELECT c.nome, p.tipo_acao
FROM clientes c
JOIN processos p ON c.id = p.cliente_id
WHERE p.tipo_acao = 'Ação de Cobrança'
UNION
SELECT c.nome, p.tipo_acao
FROM clientes c
JOIN processos p ON c.id = p.cliente_id
WHERE p.tipo_acao = 'Ação de Indenização';




