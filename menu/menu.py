# menu.py
from dados import carregar_dados, dividir_dados
from func import rede_neural, perceptron, arvore_decisao
from collections import Counter

def mostrar_menu():
    print("\nEscolha uma técnica de aprendizado:")
    print("1. Rede Neural")
    print("2. Perceptron")
    print("3. Árvore de Decisão")
    print("4. Sair")

def menu():
    caminho_arquivo = "default of credit card clients.xls"
    X, y = carregar_dados(caminho_arquivo)
    X_train, X_test, y_train, y_test = dividir_dados(X, y)

    print("\nDistribuição das classes no conjunto de dados original:")
    print(Counter(y_train))

    while True:
        mostrar_menu()
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            rede_neural(X_train, y_train, X_test, y_test)
        elif escolha == '2':
            perceptron(X_train, y_train, X_test, y_test)
        elif escolha == '3':
            arvore_decisao(X_train, y_train, X_test, y_test)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
