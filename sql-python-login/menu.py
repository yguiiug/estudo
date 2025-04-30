import sqlite3
import os
from usuarios import cadastrar_usuario, login

# Função para criar a tabela no banco de dados
def criar_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do menu de opções
def menu():
    criar_db()  # Cria o banco de dados e a tabela (caso não existam)
    
    while True:
        limpar_tela()
        print("\n1 - Cadastrar novo usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_usuario()
            input("Pressione ENTER para continuar...")  # Aguardar entrada do usuário

        elif escolha == '2':
            login()
            input("Pressione ENTER para continuar...")  # Aguardar entrada do usuário
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Rodar o menu quando o script for executado
if __name__ == "__main__":
    menu()