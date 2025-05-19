dec = int(input("Digite um número decimal: "))

def decimal_pra_hexadecimal(numero):
    digitos_hex = "0123456789ABCDEF"
    restos = []
    n = numero
    while n > 0:
        resto = n % 16
        restos.append(digitos_hex[resto])
        n = n // 16
    restos.reverse()
    return ''.join(restos)

print(decimal_pra_hexadecimal(dec))
