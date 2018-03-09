'''def pot():
    base=int(input("Digite a da base: "))
    expoente=int(input("Digite a do expoente: "))
    resultado=base**expoente
    print(resultado)

    
pot()'''



def pot(base, expoente):
    res = base
    if expoente == 0:
        return 1
    return base * pot(base, expoente-1)

base = int(input("Num: "))
expoente = int(input("Pontencia: "))
print(pot(base, expoente))
