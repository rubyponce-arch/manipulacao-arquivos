def criar_arquivo():
    with open('numeros.txt', "w", encoding="utf-8") as arquivo:
        arquivo.write("10")
        arquivo.write("15")
        arquivo.write("22")
        arquivo.write("40")
        arquivo.write("55")
        arquivo.write("68")
        arquivo.write("73")
        arquivo.write("80")
        arquivo.write("91")

criar_arquivo()