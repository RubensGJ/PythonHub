def exibir_menu_unidades():
    print("\n=== MENU CONVERSOR DE UNIDADES ===")
    print("1 - Converter Unidades")
    print("0 - Voltar ao Menu Principal")
    opcao = input("Digite sua opção: ").strip()
    return opcao

def converter_unidade(valor, unidade_origem, unidade_destino):
    conversoes = {
        "km": {"m": 1000, "cm": 100000, "mm": 1000000},
        "m": {"km": 0.001, "cm": 100, "mm": 1000},
        "cm": {"m": 0.01, "km": 0.00001, "mm": 10},
        "mm": {"m": 0.001, "km": 0.000001, "cm": 0.1},
    }

    if unidade_origem not in conversoes or unidade_destino not in conversoes[unidade_origem]:
        raise ValueError("Unidade de origem ou destino inválida.")

    fator_conversao = conversoes[unidade_origem][unidade_destino]
    return valor * fator_conversao

def conversor_unidade():
    while True:
        opcao = exibir_menu_unidades()
        if opcao == "1":
            try:
                valor = float(input("Digite o valor a ser convertido: "))
                unidade_origem = input("Digite a unidade de origem (m, km, cm, mm): ").strip()
                unidade_destino = input("Digite a unidade de destino (m, km, cm, mm): ").strip()

                resultado = converter_unidade(valor, unidade_origem, unidade_destino)
                print(f"{valor} {unidade_origem} equivalem a {resultado} {unidade_destino}.")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "0":
            print("Voltando ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    conversor_unidade()