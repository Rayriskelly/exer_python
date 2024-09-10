                                   # Outra forma de resolução com uso do (case)


mes = int(input("Digite o número do mês:"))

match mes:

    case 1:
        print("Janeiro")

    case 2:
        print("Fevereiro")

    case 3:
        print("Março")

    case _:
        print("Mês inválido")