def ler_arquivo():
    with open("mensagem.txt", "r") as arquivo:
        conteudo = arquivo.read()

    print(conteudo)


ler_arquivo()