# Importar os dois modelos ajustados na pasta Utils
from Model.previsao_consumo import executar_previsao_consumo
from Model.classificacao_submercado import executar_classificacao_submercado

def main():
    while True:
        print("\n=== Menu de Modelos ===")
        print("1. Previsão de Consumo (Random Forest Regressor)")
        print("2. Classificação de Submercados (Random Forest Classifier)")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("\nExecutando modelo de Previsão de Consumo...\n")
            executar_previsao_consumo()
        elif escolha == '2':
            print("\nExecutando modelo de Classificação de Submercados...\n")
            executar_classificacao_submercado()
        elif escolha == '3':
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()
