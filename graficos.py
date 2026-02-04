import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

def plotar_funcao(funcao, intervalo=(-10, 10), titulo=None):
    """
    Plota uma função 2D.
    
    Args:
        funcao: Função a ser plotada
        intervalo: Tupla com (min, max) do eixo x
        titulo: Título do gráfico
    """
    x = np.linspace(intervalo[0], intervalo[1], 1000)
    y = [funcao(val) for val in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=2, color='blue')
    plt.title(titulo or f'Gráfico da função: {funcao.__name__}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()

def plotar_multiplas_funcoes(funcoes, intervalo=(-10, 10), labels=None):
    """
    Plota múltiplas funções no mesmo gráfico.
    
    Args:
        funcoes: Lista de funções a serem plotadas
        intervalo: Tupla com (min, max) do eixo x
        labels: Lista de labels para cada função
    """
    plt.figure(figsize=(12, 8))
    x = np.linspace(intervalo[0], intervalo[1], 1000)
    
    cores = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    
    for i, funcao in enumerate(funcoes):
        y = [funcao(val) for val in x]
        label = labels[i] if labels and i < len(labels) else f'Função {i+1}'
        cor = cores[i % len(cores)]
        plt.plot(x, y, linewidth=2, color=cor, label=label)
    
    plt.title('Comparação de Funções')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.legend()
    plt.show()

def plotar_funcao_3d(funcao_str, intervalo=(-10, 10)):
    """
    Plota uma função 3D da forma z = f(x, y).
    
    Args:
        funcao_str: String da expressão (ex: 'x**2 + y**2')
        intervalo: Tupla com (min, max) para os eixos x e y
    """
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(intervalo[0], intervalo[1], 100)
    y = np.linspace(intervalo[0], intervalo[1], 100)
    X, Y = np.meshgrid(x, y)
    
    try:
        # Validação de segurança básica
        caracteres_proibidos = ['import', 'exec', 'eval', '__', 'open', 'file', 'input', 'compile']
        if any(palavra in funcao_str.lower() for palavra in caracteres_proibidos):
            print("Erro: Expressão contém elementos proibidos!")
            return
        
        # Namespace seguro
        safe_dict = {
            "__builtins__": {},
            "x": X, "y": Y, "np": np,
            "sin": np.sin, "cos": np.cos, "tan": np.tan,
            "sqrt": np.sqrt, "exp": np.exp, "log": np.log,
            "pi": np.pi, "e": np.e, "abs": np.abs
        }
        
        Z = eval(funcao_str, {"__builtins__": {}}, safe_dict)
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Gráfico 3D: z = {funcao_str}')
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
    except Exception as e:
        print(f"Erro ao plotar função 3D: {e}")

def plotar_grafico_polar(funcao, titulo='Gráfico Polar'):
    """
    Plota uma função em coordenadas polares.
    
    Args:
        funcao: Função r = f(theta)
        titulo: Título do gráfico
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = [funcao(t) for t in theta]
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))
    ax.plot(theta, r, linewidth=2)
    ax.set_title(titulo)
    ax.grid(True)
    plt.show()

def plotar_histograma(dados, bins=30, titulo='Histograma'):
    """
    Plota um histograma dos dados fornecidos.
    
    Args:
        dados: Lista ou array de dados
        bins: Número de intervalos
        titulo: Título do gráfico
    """
    plt.figure(figsize=(10, 6))
    plt.hist(dados, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title(titulo)
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.grid(True, alpha=0.3)
    plt.show()

def plotar_scatter(x_dados, y_dados, titulo='Gráfico de Dispersão'):
    """
    Plota um gráfico de dispersão.
    
    Args:
        x_dados: Dados do eixo x
        y_dados: Dados do eixo y
        titulo: Título do gráfico
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(x_dados, y_dados, c='blue', alpha=0.6, edgecolors='black')
    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, alpha=0.3)
    plt.show()

def plotar_grafico_barras(categorias, valores, titulo='Gráfico de Barras'):
    """
    Plota um gráfico de barras.
    
    Args:
        categorias: Lista de categorias
        valores: Lista de valores
        titulo: Título do gráfico
    """
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, valores, color='steelblue', edgecolor='black')
    plt.title(titulo)
    plt.xlabel('Categorias')
    plt.ylabel('Valores')
    plt.grid(True, alpha=0.3, axis='y')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
