from currency_converter import CurrencyConverter

def converter_moeda():
    c = CurrencyConverter()

    moeda_origem = input("Digite a moeda que você possui (ex: USD, EUR, BRL): ").strip().upper()

    valor_str = input("Digite a quantia que você tem: ").strip()
    try:
        valor = float(valor_str)
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        return

    moeda_destino = input("Digite a moeda para a qual deseja converter (ex: USD, EUR, BRL): ").strip().upper()

    try:
        valor_convertido = c.convert(valor, moeda_origem, moeda_destino)
        print(f"{valor} {moeda_origem} equivalem a {valor_convertido:.2f} {moeda_destino}")
    except Exception as e:
        print("Erro na conversão:", e)

if __name__ == "__main__":
    converter_moeda()