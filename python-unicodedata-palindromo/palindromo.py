import unicodedata
import string

palavra = input("Digite uma frase: ")

frase = palavra.lower()
frase = unicodedata.normalize("NFD", frase)
frase = "".join([letra for letra in frase if unicodedata.category(letra) != "Mn"])
frase = "".join([letra for letra in frase if letra in string.ascii_lowercase])

cont = frase[::-1]

if cont == frase:
    print(f"{palavra} É um palíndromo")
else:
    print(f"{palavra} Não é um palíndromo")
