Este é um sistema simples para cadastro de usuários com nome e senha. O sistema utiliza SQLite para armazenar os dados e foi implementado em Python.

Funcionalidades
Cadastro de Usuário: O sistema permite cadastrar um novo usuário. Durante o cadastro, o usuário precisa confirmar a senha.
Login: O sistema permite que o usuário realize login utilizando o nome e senha cadastrados.

Como usar
Pré-requisitos
Python 3.x
Biblioteca SQLite (já inclusa no Python)

Passo 1: Criar o banco de dados
Execute o script criar_db.py para criar o banco de dados e a tabela usuarios no SQLite.
python criar_db.py

Passo 2: Rodar o sistema
Execute o script principal para interagir com o sistema de cadastro e login.
python sistema.py

Funcionalidades disponíveis
1: Cadastrar novo usuário

2: Fazer login com um usuário já cadastrado

3: Sair do sistema

Observações
O sistema realiza a verificação se o usuário já existe no banco de dados durante o cadastro.

As senhas devem ser digitadas corretamente para serem confirmadas.

Como funciona o código
Banco de dados
O banco de dados usuarios.db é um arquivo SQLite que armazena a tabela usuarios, com as colunas:

id: Identificador único do usuário (autoincremento)

nome: Nome do usuário

senha: Senha do usuário

Arquivos principais
criar_db.py: Cria o banco de dados e a tabela de usuários.

sistema.py: Implementa o menu e as funcionalidades de cadastro e login.

Contribuições
Este é um projeto simples e aberto para melhorias. Você pode contribuir:

Adicionando criptografia de senha para aumentar a segurança.

Implementando suporte a outros bancos de dados, como MySQL ou PostgreSQL.

Melhorando a interface de interação (pode ser uma interface gráfica com Tkinter, por exemplo).

Licença
Este projeto está sob a licença MIT.