senha = "123456"
rept = 1
#tentativa = 3

nome = input("Digite seu nome:")
print(f'Olá {nome}, seja bem vindo(a)!')

banco = input("Digite sua senha:")

'''while senha == banco:
    print("Senha correta!")

else:
    print("Senha incorreta")'''

#rept = rept - 4
if banco != senha:
    while rept <=3 and banco != senha:
        #print(input("Gostaria de tentar novamente?"))
        rept = rept + 1

        if rept <=3:
            print("Senha incorreta!")
            banco = input("Digite sua senha:")


        else:
            print("Sistema finalizado!")

        if banco == senha:
            print("Senha correta!")

else:
    print("Senha correta!")