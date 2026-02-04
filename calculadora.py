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

def seno(angulo):
    """Calcula o seno de um ângulo em graus."""
    return math.sin(math.radians(angulo))

def cosseno(angulo):
    """Calcula o cosseno de um ângulo em graus."""
    return math.cos(math.radians(angulo))

def tangente(angulo):
    """Calcula a tangente de um ângulo em graus."""
    return math.tan(math.radians(angulo))

def logaritmo(numero, base=10):
    """Calcula o logaritmo de um número em uma base especificada."""
    if numero > 0:
        if base == math.e:
            return math.log(numero)
        return math.log(numero, base)
    else:
        return "Logaritmo não definido para números não-positivos"

def fatorial(n):
    """Calcula o fatorial de um número."""
    if n < 0:
        return "Fatorial não definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return math.factorial(int(n))

def raiz_n(numero, indice):
    """Calcula a raiz de índice n de um número."""
    if indice == 0:
        return "Índice da raiz não pode ser zero"
    if numero < 0 and indice % 2 == 0:
        return "Raiz par de número negativo não é real"
    if numero < 0:
        return -math.pow(-numero, 1/indice)
    return math.pow(numero, 1/indice)

def exponencial(n):
    """Calcula e^n."""
    return math.exp(n)

def modulo(a, b):
    """Calcula o módulo (resto da divisão) de a por b."""
    if b != 0:
        return a % b
    else:
        return "Módulo por zero não permitido"

def valor_absoluto(n):
    """Retorna o valor absoluto de um número."""
    return abs(n)
