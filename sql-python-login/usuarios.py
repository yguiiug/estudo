import sqlite3

# Função para conectar ao banco de dados
def conectar_db():
    return sqlite3.connect('usuarios.db')

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    confirmar = input("Confirme a senha: ")

    if senha != confirmar:
        print("As senhas não coincidem. Tente novamente.")
        return

    conn = conectar_db()
    cursor = conn.cursor()

    # Verificar se o usuário já existe
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
    if cursor.fetchone():
        print("Usuário já existe.")
        conn.close()
        return

    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()
    print("Usuário cadastrado com sucesso!")

# Função para fazer login
def login():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    if cursor.fetchone():
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

    conn.close()
