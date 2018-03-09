def inteiro():
    num=0
    if num <1 :
        num=int(input("Digite um numero: "))
    return num


def fatorial():
    soma = 1
    for i in range(numero,0,-1):
        soma = soma *i
    return soma

numero = inteiro()
resultado = fatorial()

print(resultado)
