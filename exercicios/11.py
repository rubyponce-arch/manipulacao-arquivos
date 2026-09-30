def listar_aprovados():
    print("Alunos aprovados:")

    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = float(dados[1])

            if nota >= 6:
                print(f"{nome} - {nota}")


listar_aprovados()