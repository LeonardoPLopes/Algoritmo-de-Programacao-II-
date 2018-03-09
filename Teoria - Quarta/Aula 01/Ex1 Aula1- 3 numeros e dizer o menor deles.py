numero1=int(input("Digite o primeiro numero: "))
numero2=int(input("Digite o segundo numero: "))
numero3=int(input("Digite o terceiro numero: "))

if (numero1 < numero2) and (numero1 < numero3):
    print("O primeiro numero que é",numero1,"é o menor")

elif (numero2 < numero1) and (numero2 < numero3):
    print("O segundo numero que é",numero2,"é o menor")

else:
    print("O terceiro numero que é",numero3,"é o menor")
    
    
