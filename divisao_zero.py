#receber dois numeros dividir por

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo numero:"))

while n2 == 0:
    n2 = int(input("número inválidp digite novamente"))


res = n1/n2
print(res)
