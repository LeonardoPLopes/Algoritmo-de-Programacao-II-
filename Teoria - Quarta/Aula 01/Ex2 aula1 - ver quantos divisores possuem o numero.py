n=-1
while n <=0:
    n=int(input("Digite um inteiro e positivo: "))

ndiv=0
contador=1
for i in range(contador,n+1):
    resto = (n%i)
    if resto == 0:
        ndiv=ndiv+1

print("%d tem %d divisores" %(n,ndiv))
