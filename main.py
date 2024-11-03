from calculadora import soma, subtracao, multiplicacao, divisao, potencia, raiz_quadrada
from graficos import plotar_funcao

def menu():
    print("Calculadora Científica")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Plotar Gráfico")
    print("0. Sair")

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            break
        elif escolha in ['1', '2', '3', '4', '5']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            if escolha == '1':
                print("Resultado:", soma(a, b))
            elif escolha == '2':
                print("Resultado:", subtracao(a, b))
            elif escolha == '3':
                print("Resultado:", multiplicacao(a, b))
            elif escolha == '4':
                print("Resultado:", divisao(a, b))
            elif escolha == '5':
                print("Resultado:", potencia(a, b))
        elif escolha == '6':
            n = float(input("Digite um número: "))
            print("Resultado:", raiz_quadrada(n))
        elif escolha == '7':
            funcao = lambda x: x**2  # Exemplo: gráfico de x²
            plotar_funcao(funcao)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
