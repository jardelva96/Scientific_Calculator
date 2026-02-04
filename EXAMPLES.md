# Exemplos de Uso - Calculadora Científica

Este arquivo contém exemplos práticos de como usar todas as funcionalidades da calculadora científica.

## 📋 Índice
1. [Operações Básicas](#operações-básicas)
2. [Funções Trigonométricas](#funções-trigonométricas)
3. [Funções Logarítmicas e Exponenciais](#funções-logarítmicas-e-exponenciais)
4. [Gráficos 2D](#gráficos-2d)
5. [Gráficos 3D](#gráficos-3d)
6. [Interface Gráfica](#interface-gráfica)

---

## Operações Básicas

### Soma
```python
from calculadora import soma
resultado = soma(15, 27)
print(resultado)  # 42
```

### Subtração
```python
from calculadora import subtracao
resultado = subtracao(50, 23)
print(resultado)  # 27
```

### Multiplicação
```python
from calculadora import multiplicacao
resultado = multiplicacao(7, 8)
print(resultado)  # 56
```

### Divisão
```python
from calculadora import divisao
resultado = divisao(100, 4)
print(resultado)  # 25.0
```

### Potenciação
```python
from calculadora import potencia
resultado = potencia(2, 10)
print(resultado)  # 1024.0
```

### Raiz Quadrada
```python
from calculadora import raiz_quadrada
resultado = raiz_quadrada(144)
print(resultado)  # 12.0
```

### Raiz N-ésima
```python
from calculadora import raiz_n
resultado = raiz_n(27, 3)  # Raiz cúbica de 27
print(resultado)  # 3.0
```

---

## Funções Trigonométricas

### Seno (em graus)
```python
from calculadora import seno
resultado = seno(30)
print(resultado)  # 0.5
```

### Cosseno (em graus)
```python
from calculadora import cosseno
resultado = cosseno(60)
print(resultado)  # 0.5
```

### Tangente (em graus)
```python
from calculadora import tangente
resultado = tangente(45)
print(resultado)  # 1.0
```

---

## Funções Logarítmicas e Exponenciais

### Logaritmo Natural
```python
from calculadora import logaritmo
import math
resultado = logaritmo(math.e, math.e)
print(resultado)  # 1.0
```

### Logaritmo Base 10
```python
from calculadora import logaritmo
resultado = logaritmo(1000, 10)
print(resultado)  # 3.0
```

### Exponencial (e^x)
```python
from calculadora import exponencial
resultado = exponencial(1)
print(resultado)  # 2.718281828459045 (aproximadamente e)
```

### Fatorial
```python
from calculadora import fatorial
resultado = fatorial(5)
print(resultado)  # 120
```

---

## Gráficos 2D

### Plotar Função Simples
```python
from graficos import plotar_funcao
import numpy as np

# Definir uma função
def minha_funcao(x):
    return x**2

# Plotar
plotar_funcao(minha_funcao, intervalo=(-10, 10), titulo='Parábola: y = x²')
```

### Plotar Função Trigonométrica
```python
from graficos import plotar_funcao
import numpy as np

# Função seno
funcao_seno = lambda x: np.sin(x)
plotar_funcao(funcao_seno, intervalo=(-2*np.pi, 2*np.pi), titulo='Função Seno')
```

### Plotar Múltiplas Funções
```python
from graficos import plotar_multiplas_funcoes
import numpy as np

# Definir várias funções
funcao1 = lambda x: x**2
funcao2 = lambda x: x**3
funcao3 = lambda x: np.sin(x)

funcoes = [funcao1, funcao2, funcao3]
labels = ['x²', 'x³', 'sin(x)']

plotar_multiplas_funcoes(funcoes, intervalo=(-3, 3), labels=labels)
```

### Função Exponencial Decrescente
```python
from graficos import plotar_funcao
import numpy as np

# Decaimento exponencial
decaimento = lambda x: np.exp(-x/5)
plotar_funcao(decaimento, intervalo=(0, 20), titulo='Decaimento: e^(-x/5)')
```

---

## Gráficos 3D

### Paraboloide
```python
from graficos import plotar_funcao_3d

expressao = "x**2 + y**2"
plotar_funcao_3d(expressao, intervalo=(-10, 10))
```

### Sela (Saddle)
```python
from graficos import plotar_funcao_3d

expressao = "x**2 - y**2"
plotar_funcao_3d(expressao, intervalo=(-10, 10))
```

### Onda Circular
```python
from graficos import plotar_funcao_3d

expressao = "np.sin(np.sqrt(x**2 + y**2))"
plotar_funcao_3d(expressao, intervalo=(-10, 10))
```

### Superfície Complexa
```python
from graficos import plotar_funcao_3d

expressao = "np.sin(x) * np.cos(y)"
plotar_funcao_3d(expressao, intervalo=(-10, 10))
```

---

## Gráficos Polares

### Rosa de 3 Pétalas
```python
from graficos import plotar_grafico_polar
import numpy as np

funcao_rosa = lambda theta: 5 * np.cos(3 * theta)
plotar_grafico_polar(funcao_rosa, titulo='Rosa de 3 Pétalas')
```

### Espiral de Arquimedes
```python
from graficos import plotar_grafico_polar
import numpy as np

espiral = lambda theta: theta
plotar_grafico_polar(espiral, titulo='Espiral de Arquimedes')
```

### Cardioide
```python
from graficos import plotar_grafico_polar
import numpy as np

cardioide = lambda theta: 1 + np.cos(theta)
plotar_grafico_polar(cardioide, titulo='Cardioide')
```

---

## Interface Gráfica

### Abrir a Interface
```python
from interface import criar_janela

# Abre a calculadora gráfica
criar_janela()
```

### Usar a Calculadora Gráfica
1. Digite expressões matemáticas diretamente no display
2. Use os botões para inserir números e operações
3. Exemplos de expressões:
   - `2*sin(pi/6)` → Calcula 2 × seno(π/6)
   - `sqrt(16) + 3**2` → Calcula √16 + 3²
   - `log(100)` → Calcula log₁₀(100)
   - `e**(2)` → Calcula e²

### Plotar Gráficos na Interface
1. **Gráfico 2D**: Digite uma expressão em termos de `x`
   - Exemplo: `sin(x)`, `x**2`, `exp(-x/10)*sin(x)`
   - Clique em "📊 Gráfico 2D"

2. **Gráfico 3D**: Digite uma expressão em termos de `x` e `y`
   - Exemplo: `x**2 + y**2`, `sin(x)*cos(y)`
   - Clique em "📈 Gráfico 3D"

3. **Ver Histórico**: Clique em "📜 Histórico" para ver seus últimos 10 cálculos

---

## Dicas e Truques

### 1. Usar Constantes
```python
# Na interface ou no código
pi  # 3.141592653589793
e   # 2.718281828459045
```

### 2. Funções Compostas
```python
# Você pode compor funções complexas
sin(cos(tan(pi/4)))
sqrt(log(e**2))
```

### 3. Operações em Cadeia
```python
# Calcule expressões longas
(5 + 3) * (10 - 2) / 4
```

### 4. Precisão de Cálculo
```python
# Python mantém alta precisão
from calculadora import exponencial
resultado = exponencial(10)
print(f"{resultado:.10f}")  # 10 casas decimais
```

---

## Exemplos Práticos

### Exemplo 1: Calcular Área de um Círculo
```python
from calculadora import multiplicacao, potencia
import math

raio = 5
area = multiplicacao(math.pi, potencia(raio, 2))
print(f"Área do círculo: {area:.2f}")  # 78.54
```

### Exemplo 2: Calcular Hipotenusa
```python
from calculadora import soma, potencia, raiz_quadrada

cateto_a = 3
cateto_b = 4
hipotenusa = raiz_quadrada(soma(potencia(cateto_a, 2), potencia(cateto_b, 2)))
print(f"Hipotenusa: {hipotenusa}")  # 5.0
```

### Exemplo 3: Converter Temperatura
```python
# Celsius para Fahrenheit: F = C * 9/5 + 32
from calculadora import multiplicacao, divisao, soma

celsius = 25
fahrenheit = soma(multiplicacao(celsius, divisao(9, 5)), 32)
print(f"{celsius}°C = {fahrenheit}°F")  # 25°C = 77.0°F
```

### Exemplo 4: Juros Compostos
```python
from calculadora import potencia, multiplicacao

capital_inicial = 1000
taxa_juros = 0.05  # 5% ao ano
anos = 10

montante = multiplicacao(capital_inicial, potencia(1 + taxa_juros, anos))
print(f"Montante após {anos} anos: R$ {montante:.2f}")
```

---

## Solução de Problemas

### Erro: "Divisão por zero não permitida"
```python
# ❌ Evite divisões por zero
divisao(10, 0)

# ✓ Verifique o denominador antes
b = 0
if b != 0:
    resultado = divisao(10, b)
else:
    print("Erro: divisor não pode ser zero")
```

### Erro: "Número negativo não tem raiz real"
```python
# ❌ Raiz quadrada de número negativo
raiz_quadrada(-16)

# ✓ Use valor absoluto ou raiz complexa
from calculadora import valor_absoluto, raiz_quadrada
resultado = raiz_quadrada(valor_absoluto(-16))
```

---

## Recursos Avançados

### Plotagem Personalizada
```python
import matplotlib.pyplot as plt
import numpy as np

# Criar gráfico customizado
fig, ax = plt.subplots(figsize=(12, 8))
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
ax.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
ax.fill_between(x, y1, y2, alpha=0.3)
ax.set_title('Área entre Seno e Cosseno', fontsize=16)
ax.legend()
ax.grid(True)
plt.show()
```

### Análise Numérica
```python
import numpy as np
from graficos import plotar_histograma

# Gerar dados aleatórios com distribuição normal
dados = np.random.normal(100, 15, 1000)
plotar_histograma(dados, bins=30, titulo='Distribuição Normal')
```

---

Para mais exemplos e informações, consulte a documentação completa no README.md
