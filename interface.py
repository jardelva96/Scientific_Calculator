import tkinter as tk
from tkinter import messagebox, ttk, font
from math import sin, cos, tan, log, sqrt, pi, e, factorial, asin, acos, atan
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class CalculadoraCientifica:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora Científica Completa - Avançada")
        self.janela.geometry("800x700")
        self.janela.configure(bg="#2c3e50")
        
        # Variáveis
        self.modo_grafico = False
        self.historico = []
        
        # Criar interface
        self.criar_interface()
    
    def criar_interface(self):
        # Frame superior para o display
        frame_display = tk.Frame(self.janela, bg="#2c3e50")
        frame_display.pack(pady=10, padx=10, fill=tk.X)
        
        # Display principal com bordas arredondadas
        self.entrada = tk.Entry(frame_display, font=("Arial", 24, "bold"), 
                               borderwidth=3, relief="solid", 
                               bg="#ecf0f1", fg="#2c3e50",
                               justify='right')
        self.entrada.pack(fill=tk.X, ipady=20, padx=5)
        
        # Label para mostrar histórico/modo
        self.label_info = tk.Label(frame_display, text="Modo: Calculadora", 
                                   font=("Arial", 10), bg="#2c3e50", fg="#ecf0f1")
        self.label_info.pack(pady=5)
        
        # Frame para os botões
        frame_botoes = tk.Frame(self.janela, bg="#2c3e50")
        frame_botoes.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Definição dos botões com cores
        botoes_config = [
            # Linha 1 - Funções especiais
            [('C', 'danger', self.limpar_entrada), ('⌫', 'warning', self.apagar_ultimo),
             ('(', 'secondary', lambda: self.inserir_valor('(')), 
             (')', 'secondary', lambda: self.inserir_valor(')')),
             ('√', 'info', lambda: self.inserir_valor('sqrt('))],
            
            # Linha 2 - Funções trigonométricas
            [('sin', 'info', lambda: self.inserir_valor('sin(')),
             ('cos', 'info', lambda: self.inserir_valor('cos(')),
             ('tan', 'info', lambda: self.inserir_valor('tan(')),
             ('π', 'success', lambda: self.inserir_valor('pi')),
             ('e', 'success', lambda: self.inserir_valor('e'))],
            
            # Linha 3 - Números e operações
            [('7', 'primary', lambda: self.inserir_valor('7')),
             ('8', 'primary', lambda: self.inserir_valor('8')),
             ('9', 'primary', lambda: self.inserir_valor('9')),
             ('÷', 'operator', lambda: self.inserir_valor('/')),
             ('^', 'operator', lambda: self.inserir_valor('**'))],
            
            # Linha 4
            [('4', 'primary', lambda: self.inserir_valor('4')),
             ('5', 'primary', lambda: self.inserir_valor('5')),
             ('6', 'primary', lambda: self.inserir_valor('6')),
             ('×', 'operator', lambda: self.inserir_valor('*')),
             ('!', 'info', lambda: self.inserir_valor('factorial('))],
            
            # Linha 5
            [('1', 'primary', lambda: self.inserir_valor('1')),
             ('2', 'primary', lambda: self.inserir_valor('2')),
             ('3', 'primary', lambda: self.inserir_valor('3')),
             ('-', 'operator', lambda: self.inserir_valor('-')),
             ('log', 'info', lambda: self.inserir_valor('log('))],
            
            # Linha 6
            [('0', 'primary', lambda: self.inserir_valor('0')),
             ('.', 'primary', lambda: self.inserir_valor('.')),
             ('=', 'success', self.calcular),
             ('+', 'operator', lambda: self.inserir_valor('+')),
             ('exp', 'info', lambda: self.inserir_valor('e**('))],
        ]
        
        # Cores para cada tipo de botão
        cores = {
            'primary': ('#3498db', '#2980b9', 'white'),      # Azul
            'success': ('#27ae60', '#229954', 'white'),       # Verde
            'danger': ('#e74c3c', '#c0392b', 'white'),        # Vermelho
            'warning': ('#f39c12', '#d68910', 'white'),       # Laranja
            'info': ('#16a085', '#138d75', 'white'),          # Turquesa
            'secondary': ('#95a5a6', '#7f8c8d', 'white'),     # Cinza
            'operator': ('#34495e', '#2c3e50', 'white')       # Cinza escuro
        }
        
        # Criar botões
        for i, linha in enumerate(botoes_config):
            for j, (texto, tipo, comando) in enumerate(linha):
                bg_color, hover_color, fg_color = cores[tipo]
                btn = tk.Button(frame_botoes, text=texto, 
                              font=("Arial", 16, "bold"),
                              bg=bg_color, fg=fg_color,
                              activebackground=hover_color,
                              borderwidth=0, relief="flat",
                              command=comando, cursor="hand2")
                btn.grid(row=i, column=j, sticky="nsew", padx=3, pady=3)
                
                # Efeito hover
                btn.bind('<Enter>', lambda e, b=btn, h=hover_color: b.configure(bg=h))
                btn.bind('<Leave>', lambda e, b=btn, c=bg_color: b.configure(bg=c))
        
        # Frame para botões de gráficos
        frame_graficos = tk.Frame(self.janela, bg="#2c3e50")
        frame_graficos.pack(pady=5, padx=10, fill=tk.X)
        
        btn_plot2d = tk.Button(frame_graficos, text="📊 Gráfico 2D", 
                              font=("Arial", 12, "bold"),
                              bg="#8e44ad", fg="white",
                              activebackground="#7d3c98",
                              borderwidth=0, relief="flat",
                              command=self.plotar_funcao_2d,
                              cursor="hand2", height=2)
        btn_plot2d.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        btn_plot3d = tk.Button(frame_graficos, text="📈 Gráfico 3D", 
                              font=("Arial", 12, "bold"),
                              bg="#e67e22", fg="white",
                              activebackground="#d35400",
                              borderwidth=0, relief="flat",
                              command=self.plotar_funcao_3d,
                              cursor="hand2", height=2)
        btn_plot3d.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        btn_historico = tk.Button(frame_graficos, text="📜 Histórico", 
                                 font=("Arial", 12, "bold"),
                                 bg="#16a085", fg="white",
                                 activebackground="#138d75",
                                 borderwidth=0, relief="flat",
                                 command=self.mostrar_historico,
                                 cursor="hand2", height=2)
        btn_historico.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        # Configurar grid para expandir
        for i in range(len(botoes_config)):
            frame_botoes.grid_rowconfigure(i, weight=1)
        for j in range(5):
            frame_botoes.grid_columnconfigure(j, weight=1)
    
    def inserir_valor(self, valor):
        self.entrada.insert(tk.END, valor)
    
    def limpar_entrada(self):
        self.entrada.delete(0, tk.END)
    
    def apagar_ultimo(self):
        conteudo_atual = self.entrada.get()
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, conteudo_atual[:-1])
    
    def calcular(self):
        try:
            expressao = self.entrada.get()
            resultado = eval(expressao, {"__builtins__": None}, 
                           {"sin": sin, "cos": cos, "tan": tan, 
                            "asin": asin, "acos": acos, "atan": atan,
                            "log": log, "sqrt": sqrt, "pi": pi, "e": e, 
                            "factorial": factorial, "abs": abs})
            
            # Adicionar ao histórico
            self.historico.append(f"{expressao} = {resultado}")
            if len(self.historico) > 10:
                self.historico.pop(0)
            
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na expressão: {str(e)}")
    
    def plotar_funcao_2d(self):
        try:
            expressao = self.entrada.get()
            
            # Criar nova janela para o gráfico
            janela_grafico = tk.Toplevel(self.janela)
            janela_grafico.title("Gráfico 2D")
            janela_grafico.geometry("800x600")
            janela_grafico.configure(bg="#2c3e50")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            x = np.linspace(-10, 10, 1000)
            
            # Avaliar a função
            y = eval(expressao, {"__builtins__": None}, 
                    {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                     "log": np.log, "sqrt": np.sqrt, "pi": np.pi, "e": np.e,
                     "exp": np.exp, "abs": np.abs, "np": np})
            
            ax.plot(x, y, linewidth=2.5, color='#3498db')
            ax.set_title(f'Gráfico: y = {expressao}', fontsize=16, fontweight='bold')
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.grid(True, alpha=0.3, linestyle='--')
            ax.axhline(y=0, color='k', linewidth=0.8)
            ax.axvline(x=0, color='k', linewidth=0.8)
            
            canvas = FigureCanvasTkAgg(fig, master=janela_grafico)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao plotar gráfico 2D: {str(e)}")
    
    def plotar_funcao_3d(self):
        try:
            expressao = self.entrada.get()
            
            # Criar nova janela para o gráfico
            janela_grafico = tk.Toplevel(self.janela)
            janela_grafico.title("Gráfico 3D")
            janela_grafico.geometry("900x700")
            janela_grafico.configure(bg="#2c3e50")
            
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            x = np.linspace(-10, 10, 100)
            y = np.linspace(-10, 10, 100)
            X, Y = np.meshgrid(x, y)
            
            # Avaliar a função
            Z = eval(expressao, {"__builtins__": None},
                    {"x": X, "y": Y, "np": np, "sin": np.sin, "cos": np.cos,
                     "tan": np.tan, "sqrt": np.sqrt, "exp": np.exp,
                     "log": np.log, "pi": np.pi, "e": np.e})
            
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            ax.set_xlabel('X', fontsize=12)
            ax.set_ylabel('Y', fontsize=12)
            ax.set_zlabel('Z', fontsize=12)
            ax.set_title(f'Gráfico 3D: z = {expressao}', fontsize=16, fontweight='bold')
            fig.colorbar(surf, shrink=0.5, aspect=5)
            
            canvas = FigureCanvasTkAgg(fig, master=janela_grafico)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao plotar gráfico 3D: {str(e)}\nUse variáveis x e y na expressão.")
    
    def mostrar_historico(self):
        janela_hist = tk.Toplevel(self.janela)
        janela_hist.title("Histórico de Cálculos")
        janela_hist.geometry("500x400")
        janela_hist.configure(bg="#2c3e50")
        
        label = tk.Label(janela_hist, text="Histórico de Cálculos", 
                        font=("Arial", 16, "bold"),
                        bg="#2c3e50", fg="#ecf0f1")
        label.pack(pady=10)
        
        frame_lista = tk.Frame(janela_hist, bg="#2c3e50")
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(frame_lista, font=("Courier", 11),
                            bg="#ecf0f1", fg="#2c3e50",
                            yscrollcommand=scrollbar.set)
        listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        if self.historico:
            for item in self.historico:
                listbox.insert(tk.END, item)
        else:
            listbox.insert(tk.END, "Nenhum cálculo no histórico")

def exibir_resultado(resultado):
    messagebox.showinfo("Resultado", f"O resultado é: {resultado}")

def plotar_grafico_na_janela(janela, funcao, intervalo=(-10, 10)):
    fig, ax = plt.subplots(figsize=(5, 4))
    x = np.linspace(intervalo[0], intervalo[1], 1000)
    y = funcao(x)
    ax.plot(x, y, linewidth=2.5)
    ax.set_title(f'Gráfico da função: {funcao.__name__}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)

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
    """Função legada para compatibilidade"""
    janela = tk.Tk()
    app = CalculadoraCientifica(janela)
    janela.mainloop()

if __name__ == "__main__":
    criar_janela()
