def criar_arquivo():
    frase = input("Digite uma frase: ")

    with open("frase.txt", "w") as arquivo:
        arquivo.write(frase)

    print("Arquivo criado com sucesso!")


criar_arquivo()