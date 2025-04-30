# Banco de Dados Simples em SQL

Este projeto implementa um **banco de dados simples** com duas tabelas e operações básicas de **inserção**, **atualização** e **consulta** de dados. O objetivo é fornecer um exemplo prático de manipulação de dados utilizando SQL.

## Estrutura do Banco de Dados

O banco de dados é composto por duas tabelas principais:

1. **clientes**: Armazena informações sobre clientes.
2. **pedidos**: Armazena informações sobre pedidos feitos pelos clientes.

### Tabela: `clientes`

A tabela `clientes` contém os seguintes campos:

- **id** (INT, chave primária): Identificador único do cliente.
- **nome** (VARCHAR(100)): Nome do cliente.
- **email** (VARCHAR(100)): E-mail do cliente.

### Tabela: `pedidos`

A tabela `pedidos` contém os seguintes campos:

- **id** (INT, chave primária): Identificador único do pedido.
- **cliente_id** (INT, chave estrangeira): ID do cliente que fez o pedido (referencia a tabela `clientes`).
- **produto** (VARCHAR(100)): Nome do produto do pedido.
- **quantidade** (INT): Quantidade do produto no pedido.