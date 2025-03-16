def pagamento():
    metodo = input("Escolha o método de pagamento (cartao/dinheiro): ").strip().lower()
    valor = float(input("Informe o valor da compra: "))

    if metodo == "cartao":
        saldo = float(input("Informe o saldo disponível: "))
        print("Pagamento aprovado!" if saldo >= valor else "Saldo insuficiente!")

    elif metodo == "dinheiro":
        recebido = float(input("Informe o valor entregue: "))
        print(f"Pagamento aprovado! Troco: R$ {recebido - valor:.2f}" if recebido >= valor else "Valor insuficiente!")

    else:
        print("Método inválido!")

pagamento()
