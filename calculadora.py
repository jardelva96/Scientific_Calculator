import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não permitida"

def potencia(base, expoente):
    return math.pow(base, expoente)

def raiz_quadrada(n):
    if n >= 0:
        return math.sqrt(n)
    else:
        return "Número negativo não tem raiz real"
