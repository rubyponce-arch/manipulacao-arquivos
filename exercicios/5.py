def contar_caracteres():
    with open("texto.txt", "r") as arquivo:
        conteudo = arquivo.read()

    quantidade = len(conteudo)

    print(f"Quantidade de caracteres: {quantidade}")


contar_caracteres()