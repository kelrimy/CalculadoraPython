print(f"{'-' * 30}\n{'CALCULADORA':^30}\n{'-' * 30}")

while True:
    a = int(input("Digite um número inteiro para ser calculado: "))
    b = int(input("Digite outro número inteiro para ser calculado: "))
    resultado = 0

    operacao = input("Qual operação deseja realizar?\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n ").strip()

    while operacao not in "1234":
        print("Escolha uma das operações sugeridas")
        operacao = input("Qual operação deseja realizar?\n1 - Adição\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n ").strip()

    if operacao == "1":
        resultado = a + b
        operacao = "adição"
    elif operacao == "2":
        resultado = a - b
        operacao = "subtração"
    elif operacao == "3":
        resultado = a / b
        operacao = "divisão"
    elif operacao == "4":
        resultado = a * b
        operacao = "multiplicação"

    print(f"O resultado da operação {operacao} foi {resultado}")
    print()

    continua = input("Deseja continuar com mais uma operação? [S/N] ").strip().lower()
    while continua not in "sn":
        print("Digite somente S ou N.")
        continua = input("Deseja continuar com mais uma operação? [S/N] ").strip().lower()

    if continua == "n":
        print("Obrigado e volte sempre!")
        break
