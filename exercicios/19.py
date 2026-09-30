def gerar_relatorio():
    vendas = []

    with open("vendas.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            venda = {
                "vendedor": dados[0],
                "produto": dados[1],
                "valor": float(dados[2])
            }

            vendas.append(venda)

    total_vendas = 0
    quantidade_vendas = {}
    valor_por_vendedor = {}

    print("VENDAS:")

    for venda in vendas:
        print(
            f"{venda['vendedor']} - "
            f"{venda['produto']} - "
            f"R$ {venda['valor']:.2f}"
        )

        total_vendas += venda["valor"]

        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

        if vendedor in valor_por_vendedor:
            valor_por_vendedor[vendedor] += venda["valor"]
        else:
            valor_por_vendedor[vendedor] = venda["valor"]

    print(f"\nTOTAL DE VENDAS: R$ {total_vendas:.2f}")

    print("\nQuantidade de vendas:")

    for vendedor in quantidade_vendas:
        print(f"{vendedor}: {quantidade_vendas[vendedor]}")

    maior_vendedor = ""
    maior_valor = 0

    for vendedor in valor_por_vendedor:
        if valor_por_vendedor[vendedor] > maior_valor:
            maior_valor = valor_por_vendedor[vendedor]
            maior_vendedor = vendedor

    print(
        f"\nMaior valor total em vendas: "
        f"{maior_vendedor} - R$ {maior_valor:.2f}"
    )


gerar_relatorio()