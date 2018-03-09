n=int(input("Digite um numero inteiro e positivo: "))

contadordiv=0
contador=1
ndiv=0
for i in range(contador,n+1):
    resto = (n%i)
    if resto == 0:
        ndiv=ndiv+1
if ndiv>2:
    print("Não é um numero primo")
else:
    print("O numero é primo")

print("%d tem %d divisores" %(n,ndiv))
