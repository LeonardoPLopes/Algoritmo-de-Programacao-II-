n=-1
while n<=0:
    n=int(input("Digite"))

ndiv=0
cont=1
while cont <=n:
    resto = n%cont
    if resto==0:
        ndiv=ndiv+1
    cont=cont+1

print("%d tem %d divisores" %(n,ndiv))
