def numero():
    a=int(input("Digite um numero inteiro: "))
    return a

def soma_digitos(a):
    adc = 0
    while a > 0:
        resto = a % 10
        a = (a - resto) / 10
        adc = adc + resto
    return adc

#programa
adc = numero()
print(soma_digitos(adc))
