numero = []

n=None

while n != 0:
    n = int(input("Digite um numero: "))
    if n!=0:
        numero.append(n)

print(numero)

num=len(numero)
soma=0

while num>0:
    soma = soma + numero[num-1]
    num-=1

print(soma)


