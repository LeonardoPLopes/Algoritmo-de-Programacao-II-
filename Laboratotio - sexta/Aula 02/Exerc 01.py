def eprimo(n):
    contadordiv=0
    contador=1
    ndiv=0
    for i in range(contador,n+1):
        resto = (n%i)
        if resto == 0:
            ndiv=ndiv+1
    if ndiv>2:
        return False
    else:
        return True


a=int(input("Digite o valor: "))
print(eprimo(a))
