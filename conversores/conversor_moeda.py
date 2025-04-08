from currency_converter import CurrencyConverter

def exibir_menu_inicial():
    print("\n=== MENU CONVERSOR DE MOEDAS ===")
    print("1 - Começar Conversão")
    print("2 - Ver Moedas Disponíveis")
    print("0 - Voltar ao Menu Principal")
    opcao = input("Digite sua opção: ").strip()
    return opcao

def listar_moedas_disponiveis(c):
    print("\n=== MOEDAS DISPONÍVEIS ===")
    for moeda in sorted(c.currencies):
        print(moeda)
    print()

def validar_moeda(c, moeda):
    if moeda not in c.currencies:
        print(f"Moeda '{moeda}' inválida. Por favor, escolha uma moeda válida.")
        return False
    return True

def converter_moeda():
    c = CurrencyConverter()

    while True:
        opcao = exibir_menu_inicial()
        if opcao == "1":
            moeda_origem = input("Digite a moeda que você possui (ex: USD, EUR, BRL): ").strip().upper()
            if not validar_moeda(c, moeda_origem):
                continue

            valor_str = input("Digite a quantia que você tem: ").strip()
            try:
                valor = float(valor_str)
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")
                continue

            moeda_destino = input("Digite a moeda para a qual deseja converter (ex: USD, EUR, BRL): ").strip().upper()
            if not validar_moeda(c, moeda_destino):
                continue

            try:
                valor_convertido = c.convert(valor, moeda_origem, moeda_destino)
                print(f"{valor} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}")
            except Exception as e:
                print("Erro na conversão:", e)
        elif opcao == "2":
            listar_moedas_disponiveis(c)
        elif opcao == "0":
            print("Voltando ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    converter_moeda()