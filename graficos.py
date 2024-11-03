import matplotlib.pyplot as plt
import numpy as np

def plotar_funcao(funcao, intervalo=(-10, 10)):
    x = np.linspace(intervalo[0], intervalo[1], 1000)
    y = [funcao(val) for val in x]

    plt.plot(x, y)
    plt.title(f'Gráfico da função: {funcao.__name__}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
