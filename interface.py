import tkinter as tk
from tkinter import messagebox
from math import sin, cos, tan, log, sqrt, pi, e, factorial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def exibir_resultado(resultado):
    messagebox.showinfo("Resultado", f"O resultado é: {resultado}")

def plotar_grafico_na_janela(janela, funcao, intervalo=(-10, 10)):
    fig, ax = plt.subplots(figsize=(5, 4))
    x = np.linspace(intervalo[0], intervalo[1], 1000)
    y = funcao(x)
    ax.plot(x, y)
    ax.set_title(f'Gráfico da função: {funcao.__name__}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=5, rowspan=4, padx=5, pady=5)

def plotar_grafico_3d_na_janela(janela, funcao):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    try:
        # Avaliar a função de forma segura, passando x e y como variáveis
        Z = np.array([[eval(funcao, {"x": xi, "y": yi, "np": np}) for xi, yi in zip(row_x, row_y)] for row_x, row_y in zip(X, Y)])
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title('Gráfico 3D')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        canvas = FigureCanvasTkAgg(fig, master=janela)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=5, rowspan=4, padx=5, pady=5)
    except SyntaxError:
        messagebox.showerror("Erro", "Erro de sintaxe na expressão. Verifique a entrada.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao plotar gráfico 3D: {e}")

def criar_janela():
    janela = tk.Tk()
    janela.title("Calculadora Científica Completa")
    janela.geometry("600x600")
    janela.configure(bg="#f0f0f0")

    entrada = tk.Entry(janela, font=("Helvetica", 20), borderwidth=5, relief="ridge")
    entrada.grid(row=0, column=0, columnspan=5, pady=10, ipadx=5, ipady=15)

    def inserir_valor(valor):
        entrada.insert(tk.END, valor)

    def limpar_entrada():
        entrada.delete(0, tk.END)

    def calcular():
        try:
            resultado = eval(entrada.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "log": log, "sqrt": sqrt, "pi": pi, "e": e, "factorial": factorial})
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na expressão: {e}")

    def plotar_funcao_2d():
        try:
            expressao = entrada.get()
            funcao = lambda x: eval(expressao, {"__builtins__": None}, {"x": x, "sin": sin, "cos": cos, "tan": tan, "log": log, "sqrt": sqrt, "pi": pi, "e": e, "np": np})
            plotar_grafico_na_janela(janela, funcao)
        except SyntaxError:
            messagebox.showerror("Erro", "Erro de sintaxe na expressão. Verifique a entrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao plotar gráfico: {e}")

    def plotar_funcao_3d():
        try:
            expressao = entrada.get()
            funcao = expressao
            plotar_grafico_3d_na_janela(janela, funcao)
        except SyntaxError:
            messagebox.showerror("Erro", "Erro de sintaxe na expressão. Verifique a entrada.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao plotar gráfico 3D: {e}")

    botoes = [
        ('C', 5, 0, limpar_entrada), ('π', 5, 1, lambda: inserir_valor('pi')),
        ('e', 5, 2, lambda: inserir_valor('e')), ('(', 5, 3, lambda: inserir_valor('(')),
        (')', 5, 4, lambda: inserir_valor(')')),
        ('7', 6, 0, lambda: inserir_valor('7')), ('8', 6, 1, lambda: inserir_valor('8')),
        ('9', 6, 2, lambda: inserir_valor('9')), ('/', 6, 3, lambda: inserir_valor('/')),
        ('*', 6, 4, lambda: inserir_valor('*')),
        ('4', 7, 0, lambda: inserir_valor('4')), ('5', 7, 1, lambda: inserir_valor('5')),
        ('6', 7, 2, lambda: inserir_valor('6')), ('-', 7, 3, lambda: inserir_valor('-')),
        ('+', 7, 4, lambda: inserir_valor('+')),
        ('1', 8, 0, lambda: inserir_valor('1')), ('2', 8, 1, lambda: inserir_valor('2')),
        ('3', 8, 2, lambda: inserir_valor('3')), ('log', 8, 3, lambda: inserir_valor('log(')),
        ('^', 8, 4, lambda: inserir_valor('**')),
        ('0', 9, 0, lambda: inserir_valor('0')), ('.', 9, 1, lambda: inserir_valor('.')),
        ('=', 9, 2, calcular), ('√', 9, 3, lambda: inserir_valor('sqrt(')),
        ('!', 9, 4, lambda: inserir_valor('factorial(')),
        ('sin', 10, 0, lambda: inserir_valor('sin(')), ('cos', 10, 1, lambda: inserir_valor('cos(')),
        ('tan', 10, 2, lambda: inserir_valor('tan(')), ('exp', 10, 3, lambda: inserir_valor('e**')),
        ('Plot 2D', 10, 4, plotar_funcao_2d),
        ('Plot 3D', 11, 4, plotar_funcao_3d)
    ]

    for (texto, linha, coluna, comando) in botoes:
        tk.Button(janela, text=texto, width=5, height=2, font=("Helvetica", 14),
                  command=comando).grid(row=linha, column=coluna, padx=5, pady=5)

    janela.mainloop()

if __name__ == "__main__":
    criar_janela()
