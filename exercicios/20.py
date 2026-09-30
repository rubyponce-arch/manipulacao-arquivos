def sistema_alunos():
    alunos = []

    # Carregar alunos do arquivo
    with open("alunos.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            aluno = {
                "id": int(dados[0]),
                "nome": dados[1],
                "idade": int(dados[2]),
                "curso": dados[3]
            }

            alunos.append(aluno)

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        # Listar alunos
        if opcao == "1":
            print("\nALUNOS:")

            for aluno in alunos:
                print(
                    f"{aluno['id']} - "
                    f"{aluno['nome']} - "
                    f"{aluno['idade']} anos"
                )

        # Buscar aluno
        elif opcao == "2":
            id_pesquisa = int(input("Digite o ID: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_pesquisa:
                    print("\nAluno encontrado:")
                    print(aluno["nome"])
                    print(f"{aluno['idade']} anos")
                    print(aluno["curso"])

                    encontrado = True
                    break

            if not encontrado:
                print("Aluno não encontrado!")

        # Cadastrar aluno
        elif opcao == "3":
            novo_id = int(input("ID: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            novo_aluno = {
                "id": novo_id,
                "nome": nome,
                "idade": idade,
                "curso": curso
            }

            alunos.append(novo_aluno)

            with open("alunos.txt", "w") as arquivo:
                for aluno in alunos:
                    arquivo.write(
                        f"{aluno['id']};"
                        f"{aluno['nome']};"
                        f"{aluno['idade']};"
                        f"{aluno['curso']}\n"
                    )

            print("Aluno cadastrado com sucesso!")

        # Remover aluno
        elif opcao == "4":
            id_remover = int(input("Digite o ID do aluno que deseja remover: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_remover:
                    alunos.remove(aluno)
                    encontrado = True
                    break

            if encontrado:
                with open("alunos.txt", "w") as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};"
                            f"{aluno['nome']};"
                            f"{aluno['idade']};"
                            f"{aluno['curso']}\n"
                        )

                print("Aluno removido com sucesso!")
            else:
                print("Aluno não encontrado!")

        # Alterar aluno
        elif opcao == "5":
            id_alterar = int(input("Digite o ID do aluno que deseja alterar: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_alterar:
                    print("\nDigite os novos dados:")

                    aluno["nome"] = input("Nome: ")
                    aluno["idade"] = int(input("Idade: "))
                    aluno["curso"] = input("Curso: ")

                    encontrado = True
                    break

            if encontrado:
                with open("alunos.txt", "w") as arquivo:
                    for aluno in alunos:
                        arquivo.write(
                            f"{aluno['id']};"
                            f"{aluno['nome']};"
                            f"{aluno['idade']};"
                            f"{aluno['curso']}\n"
                        )

                print("Aluno alterado com sucesso!")
            else:
                print("Aluno não encontrado!")

        # Sair
        elif opcao == "6":
            print("Programa encerrado.")
            break

        # Opção inválida
        else:
            print("Opção inválida!")


sistema_alunos()