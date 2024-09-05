G = 5.80
E = 4.90

combustivel = input("Qual tipo de combustivel utilizado? G- gasolina E- etanol")
if combustivel != 'E' and combustivel != 'G':
    print("Combustível inválido!")

else:
    print("Combustível válido")
    if combustivel == 'G':
        litros = float(input("Quantos litros foram comprados?"))

        valortotal = litros * 5.80
        print(f"O valor a ser pago é R${valortotal}")

    else:
        combustivel == 'E'
        litros = float(input("Quantos litros foram comprados?"))

        valortotal = litros * 4.90
        print(f"O valor a ser pago é R${valortotal}")