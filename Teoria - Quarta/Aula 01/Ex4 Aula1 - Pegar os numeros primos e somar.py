#EXER 4
ndiv = 0
quant = 0
soma = 0

while quant<=0:
    n=int(input("Digite a quantidade de numeros:"))
    while n>0:
        n = -1
        while n<=0:
            n=int(input("Digite um numero:"))
            for cont in range(1,n+1,1):
                if n%cont == 0:
                    ndiv = ndiv + 1
        if ndiv == 2:
            soma = soma + n
        quant = quant - 1

print("A soma dos numeros primos é igual a",soma)
