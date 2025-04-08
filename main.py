from conversores.conversor_moeda import converter_moeda

def exibir_menu():
    print("\n=== MENU DE OPCOES ===")
    print("1 - Conversor de Moedas")
    print("0 - Sair")
    opcao = input("Digite sua opção: ")
    return opcao

def main():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            converter_moeda()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
