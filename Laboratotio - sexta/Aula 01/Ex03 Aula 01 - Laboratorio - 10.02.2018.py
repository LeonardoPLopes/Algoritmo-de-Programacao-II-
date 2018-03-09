digito=int(input("Digite até onde quer que vá o termo de fibonacci: "))
numero1=0
numero2=1
print(numero1)
print(numero2)

cont=3

for i in range(cont,digito+1,1):
    numero3=numero1+numero2
    print(numero3)
    numero1=numero2
    numero2=numero3

print("Sequencia Realizada")
    
