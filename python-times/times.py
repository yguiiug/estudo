import tkinter as tk
from tkinter import messagebox
import random

def organizar_times():
    # Pegando os nomes da caixa de texto
    nomes = entrada_nomes.get("1.0", tk.END).strip()
    
    if not nomes:
        messagebox.showwarning("Atenção", "Digite pelo menos 10 nomes.")
        return

    # Separando os nomes por linha ou vírgula
    lista_nomes = [nome.strip() for nome in nomes.replace(',', '\n').splitlines() if nome.strip()]

    if len(lista_nomes) < 10:
        messagebox.showwarning("Atenção", "Digite no mínimo 10 nomes.")
        return

    random.shuffle(lista_nomes)  # Embaralha os nomes

    time1 = lista_nomes[:5]
    time2 = lista_nomes[5:10]
    substitutos = lista_nomes[10:]

    # Mostrando o resultado
    resultado = f"🏆 Time 1:\n" + "\n".join(time1) + "\n\n"
    resultado += f"🔥 Time 2:\n" + "\n".join(time2) + "\n\n"
    if substitutos:
        resultado += f"🔄 Substitutos:\n" + "\n".join(substitutos)

    output_resultado.config(state='normal')
    output_resultado.delete("1.0", tk.END)
    output_resultado.insert(tk.END, resultado)
    output_resultado.config(state='disabled')


# Criando janela
janela = tk.Tk()
janela.title("Organizador de Times")
janela.geometry("500x600")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Organizador de Times", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Instruções
instrucoes = tk.Label(janela, text="Digite os nomes (um por linha ou separados por vírgula):", font=("Arial", 12))
instrucoes.pack()

# Caixa de texto para nomes
entrada_nomes = tk.Text(janela, height=10, width=50, font=("Arial", 12))
entrada_nomes.pack(pady=10)

# Botão para organizar os times
botao_organizar = tk.Button(janela, text="Organizar Times", command=organizar_times, font=("Arial", 14), bg="#4CAF50", fg="white")
botao_organizar.pack(pady=10)

# Caixa de texto para mostrar o resultado
output_resultado = tk.Text(janela, height=15, width=50, font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_resultado.pack(pady=10)

# Rodando a janela
janela.mainloop()
