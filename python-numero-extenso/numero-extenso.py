import re

# Dicionários de palavras para números
UNIDADES = {
    "um": 1, "uma": 1, "dois": 2, "duas": 2, "três": 3, "quatro": 4,
    "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9
}

DEZENAS = {
    "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14, "catorze": 14,
    "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19,
    "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60,
    "setenta": 70, "oitenta": 80, "noventa": 90
}

CENTENAS = {
    "cem": 100, "cento": 100, "duzentos": 200, "trezentos": 300,
    "quatrocentos": 400, "quinhentos": 500, "seiscentos": 600,
    "setecentos": 700, "oitocentos": 800, "novecentos": 900
}

MULTIPLICADORES = {
    "mil": 1000,
    "milhão": 1000000, "milhões": 1000000,
    "bilhão": 1000000000, "bilhões": 1000000000
}

def palavras_para_numero(texto):
    texto = texto.lower()
    texto = re.sub(r" e ", " ", texto)
    palavras = texto.split()
    
    total = 0
    parcial = 0

    for palavra in palavras:
        if palavra in UNIDADES:
            parcial += UNIDADES[palavra]
        elif palavra in DEZENAS:
            parcial += DEZENAS[palavra]
        elif palavra in CENTENAS:
            parcial += CENTENAS[palavra]
        elif palavra in MULTIPLICADORES:
            multiplicador = MULTIPLICADORES[palavra]
            if parcial == 0:
                parcial = 1
            total += parcial * multiplicador
            parcial = 0

    total += parcial
    return total

# Parte interativa
if __name__ == "__main__":
    entrada = input("Digite um número por extenso (ex: 'quatrocentos mil e vinte'): ")
    resultado = palavras_para_numero(entrada)
    print(f"Resultado: {resultado}")
