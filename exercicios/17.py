def calcular_estoque():
    produtos = []
    valor_total = 0

    with open("produtos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            produto = {
                "nome": dados[0],
                "preco": float(dados[1]),
                "quantidade": int(dados[2])
            }

            produtos.append(produto)

    for produto in produtos:
        valor = produto["preco"] * produto["quantidade"]
        valor_total += valor

    print(f"Valor total do estoque: R$ {valor_total:.2f}")


calcular_estoque()