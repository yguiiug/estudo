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

    # Mostrando os times nos campos separados
    preencher_output(output_time1, time1)
    preencher_output(output_time2, time2)
    preencher_output(output_substitutos, substitutos if substitutos else ["Nenhum"])

def preencher_output(caixa, lista):
    caixa.config(state='normal')
    caixa.delete("1.0", tk.END)
    caixa.insert(tk.END, "\n".join(lista))
    caixa.config(state='disabled')

def limpar():
    entrada_nomes.delete("1.0", tk.END)
    for caixa in [output_time1, output_time2, output_substitutos]:
        caixa.config(state='normal')
        caixa.delete("1.0", tk.END)
        caixa.config(state='disabled')

# Criando janela
janela = tk.Tk()
janela.title("Organizador de Times")
janela.geometry("600x700")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Organizador de Times", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Instruções
instrucoes = tk.Label(janela, text="Digite os nomes (um por linha ou separados por vírgula):", font=("Arial", 12))
instrucoes.pack()

# Caixa de texto para nomes
entrada_nomes = tk.Text(janela, height=8, width=60, font=("Arial", 12))
entrada_nomes.pack(pady=10)

# Botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_organizar = tk.Button(frame_botoes, text="Organizar Times", command=organizar_times, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_organizar.grid(row=0, column=0, padx=10)

botao_limpar = tk.Button(frame_botoes, text="Limpar Nomes", command=limpar, font=("Arial", 12), bg="#f44336", fg="white")
botao_limpar.grid(row=0, column=1, padx=10)

# Área dos Times e Substitutos
frame_resultados = tk.Frame(janela)
frame_resultados.pack(pady=10)

# Time 1
label_time1 = tk.Label(frame_resultados, text="🏆 Time 1", font=("Arial", 14, "bold"))
label_time1.grid(row=0, column=0, padx=20, pady=5)

output_time1 = tk.Text(frame_resultados, height=10, width=25, font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_time1.grid(row=1, column=0, padx=20)

# Time 2
label_time2 = tk.Label(frame_resultados, text="🔥 Time 2", font=("Arial", 14, "bold"))
label_time2.grid(row=0, column=1, padx=20, pady=5)

output_time2 = tk.Text(frame_resultados, height=10, width=25, font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_time2.grid(row=1, column=1, padx=20)

# Substitutos
label_substitutos = tk.Label(frame_resultados, text="🔄 Substitutos", font=("Arial", 14, "bold"))
label_substitutos.grid(row=2, column=0, columnspan=2, pady=5)

output_substitutos = tk.Text(frame_resultados, height=5, width=60, font=("Arial", 12), state='disabled', bg="#f0f0f0")
output_substitutos.grid(row=3, column=0, columnspan=2, pady=5)

# Rodando a janela
janela.mainloop()
