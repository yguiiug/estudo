import os

os.system('cls' if os.name == 'nt' else 'clear')
entrada = input("Digite uma sequência de números (sem espaços): ")
lista_original = [int(digito) for digito in entrada]
lista_ordenada = sorted(lista_original)

if lista_original == lista_ordenada:
    print(f"Lista: {lista_original}")
    print("A lista já está ordenada!")
else:
    print(f"Lista Original: {lista_original}")
    print(f"Lista Ordenada: {lista_ordenada}")
