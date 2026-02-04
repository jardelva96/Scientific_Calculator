from calculadora import *
from graficos import *
import numpy as np

def menu():
    print("\n" + "="*50)
    print("  CALCULADORA CIENTÍFICA COMPLETA")
    print("="*50)
    print("1.  Soma")
    print("2.  Subtração")
    print("3.  Multiplicação")
    print("4.  Divisão")
    print("5.  Potência")
    print("6.  Raiz Quadrada")
    print("7.  Raiz N-ésima")
    print("8.  Seno (graus)")
    print("9.  Cosseno (graus)")
    print("10. Tangente (graus)")
    print("11. Logaritmo")
    print("12. Fatorial")
    print("13. Exponencial (e^x)")
    print("14. Plotar Gráfico 2D")
    print("15. Plotar Múltiplas Funções")
    print("16. Plotar Gráfico 3D")
    print("17. Plotar Gráfico Polar")
    print("18. Abrir Interface Gráfica")
    print("0.  Sair")
    print("="*50)

def main():
    print("\n🎓 Bem-vindo à Calculadora Científica Completa!")
    print("Desenvolvida com Python, NumPy e Matplotlib\n")
    
    while True:
        menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == '0':
            print("\n👋 Obrigado por usar a Calculadora Científica!")
            break
            
        elif escolha in ['1', '2', '3', '4', '5', '7', '11']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print(f"\n✓ Resultado: {soma(a, b)}")
            elif escolha == '2':
                print(f"\n✓ Resultado: {subtracao(a, b)}")
            elif escolha == '3':
                print(f"\n✓ Resultado: {multiplicacao(a, b)}")
            elif escolha == '4':
                print(f"\n✓ Resultado: {divisao(a, b)}")
            elif escolha == '5':
                print(f"\n✓ Resultado: {potencia(a, b)}")
            elif escolha == '7':
                print(f"\n✓ Resultado: {raiz_n(a, b)}")
            elif escolha == '11':
                print(f"\n✓ Resultado: {logaritmo(a, b)}")
                
        elif escolha in ['6', '8', '9', '10', '12', '13']:
            n = float(input("Digite um número: "))
            
            if escolha == '6':
                print(f"\n✓ Resultado: {raiz_quadrada(n)}")
            elif escolha == '8':
                print(f"\n✓ Resultado: {seno(n)}")
            elif escolha == '9':
                print(f"\n✓ Resultado: {cosseno(n)}")
            elif escolha == '10':
                print(f"\n✓ Resultado: {tangente(n)}")
            elif escolha == '12':
                print(f"\n✓ Resultado: {fatorial(n)}")
            elif escolha == '13':
                print(f"\n✓ Resultado: {exponencial(n)}")
                
        elif escolha == '14':
            print("\nExemplos de funções:")
            print("- Quadrática: x**2")
            print("- Seno: np.sin(x)")
            print("- Exponencial: np.exp(x)")
            expressao = input("Digite a expressão da função em termos de x: ")
            try:
                funcao = lambda x: eval(expressao, {"__builtins__": None}, 
                                       {"x": x, "np": np})
                plotar_funcao(funcao, titulo=f"y = {expressao}")
            except Exception as e:
                print(f"\n✗ Erro ao plotar: {e}")
                
        elif escolha == '15':
            print("\nPlotagem de múltiplas funções")
            num_funcoes = int(input("Quantas funções deseja plotar? "))
            funcoes = []
            labels = []
            
            for i in range(num_funcoes):
                expr = input(f"Digite a expressão da função {i+1}: ")
                label = input(f"Digite o rótulo da função {i+1}: ")
                try:
                    funcao = lambda x, e=expr: eval(e, {"__builtins__": None}, 
                                                    {"x": x, "np": np})
                    funcoes.append(funcao)
                    labels.append(label)
                except Exception as e:
                    print(f"\n✗ Erro na função {i+1}: {e}")
            
            if funcoes:
                plotar_multiplas_funcoes(funcoes, labels=labels)
                
        elif escolha == '16':
            print("\nExemplos de funções 3D:")
            print("- Paraboloide: x**2 + y**2")
            print("- Sela: x**2 - y**2")
            print("- Onda: np.sin(np.sqrt(x**2 + y**2))")
            expressao = input("Digite a expressão da função em termos de x e y: ")
            try:
                plotar_funcao_3d(expressao)
            except Exception as e:
                print(f"\n✗ Erro ao plotar: {e}")
                
        elif escolha == '17':
            print("\nExemplos de funções polares:")
            print("- Rosa: 5*np.cos(3*theta)")
            print("- Espiral: theta")
            print("- Cardioide: 1 + np.cos(theta)")
            expressao = input("Digite a expressão r = f(theta): ")
            try:
                funcao = lambda theta: eval(expressao, {"__builtins__": None},
                                           {"theta": theta, "np": np})
                plotar_grafico_polar(funcao)
            except Exception as e:
                print(f"\n✗ Erro ao plotar: {e}")
                
        elif escolha == '18':
            print("\n🚀 Abrindo interface gráfica...")
            from interface import criar_janela
            criar_janela()
            
        else:
            print("\n✗ Opção inválida. Tente novamente.")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
