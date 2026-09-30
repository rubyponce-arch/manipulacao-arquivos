def contar_linhas():
    quantidade = 0

    with open("nomes.txt", "r") as arquivo:
        for linha in arquivo:
            quantidade += 1

    print(f"O arquivo possui {quantidade} linhas.")


contar_linhas()