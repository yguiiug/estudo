import math

def menu():
    print("\n=== MENU DE OPÇÕES ===")
    print("1. Calcular área do triângulo")
    print("2. Calcular área do círculo")
    print("3. Calcular área do quadrado")
    print("4. Raiz quadrada")
    print("5. Fatorial")
    print("6. Verificar número primo")
    print("0. Sair")

def deseja_continuar():
    resposta = input("Deseja continuar? (s/n): ").strip().lower()
    return resposta == 's'

def area_triangulo():
    base = float(input("Digite a base: "))
    altura = float(input("Digite a altura: "))
    return (base * altura) / 2

def area_circulo():
    raio = float(input("Digite o raio: "))
    return math.pi * raio ** 2

def area_quadrado():
    lado = float(input("Digite o lado: "))
    return lado * lado

def raiz_quadrada():
    numero = float(input("Digite o número: "))
    return math.sqrt(numero)

def fatorial():
    numero = int(input("Digite um número inteiro: "))
    return math.factorial(numero)

def eh_primo():
    numero = int(input("Digite um número inteiro: "))
    if numero <= 1:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True
