import unicodedata
import string
import os

os.system('cls' if os.name == 'nt' else 'clear')

entrada = input("Digite uma frase: ")
frase = entrada.lower()

frase = unicodedata.normalize("NFD", frase)
frase = "".join([letra for letra in frase if unicodedata.category(letra) != "Mn"])

vogais = 0
consoantes = 0
outros = 0

for caractere in frase:
    if caractere in "aeiou":
        vogais += 1
    elif caractere in string.ascii_lowercase:
        consoantes += 1
    else:
        outros += 1

print(f"\nVogais: {vogais}")
print(f"Consoantes: {consoantes}")
print(f"Outros: {outros}")
