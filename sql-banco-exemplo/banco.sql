-- Criação da tabela de clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

-- Criação da tabela de pedidos
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(100),
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Inserção de dados na tabela de clientes
INSERT INTO clientes (id, nome, email) VALUES (1, 'Ana', 'ana@email.com');
INSERT INTO clientes (id, nome, email) VALUES (2, 'Bruno', 'bruno@email.com');

-- Inserção de dados na tabela de pedidos
INSERT INTO pedidos (id, cliente_id, produto, valor) VALUES (1, 1, 'Notebook', 3500.00);
INSERT INTO pedidos (id, cliente_id, produto, valor) VALUES (2, 2, 'Mouse', 99.90);
INSERT INTO pedidos (id, cliente_id, produto, valor) VALUES (3, 1, 'Teclado', 150.00);

-- Consulta simples: todos os clientes
SELECT * FROM clientes;

-- Consulta simples: todos os pedidos
SELECT * FROM pedidos;

-- Consulta com JOIN: nomes dos clientes e os produtos que compraram
SELECT 
    c.nome AS cliente, 
    p.produto, 
    p.valor
FROM 
    clientes c
JOIN 
    pedidos p ON c.id = p.cliente_id;
