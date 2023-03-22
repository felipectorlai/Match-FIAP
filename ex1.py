print("1 caneta , 1.20")

print("2 lapis , 0.80")

print("3 caderno , 4.50")

print("4 borracha , 1.00")

print("5 regua , 1.50")

num = int(input("Digite a opcao desejada (1-4): "))

match num:

    case 1:

        print("Voçe escolheu caneta e custa 1.20")

    case 2:

        print("Voçe escolheu lapiz custa 0.80")

    case 3:

        print("Voçe escolheu caderno e custa 4.50")

    case 4:

        print("Voçe escolheu borracha e custa 1.00")

    case 5:

        print("Voçe escolheu a regua e custa 1.50")

    case _:

        print("O produto nao esta cadastrado!")