print('-'*5,'Desafio 6','-'*5)
print("")

def soma_(lista, cont):
    global soma
    if cont>=0:
        soma = soma + lista[cont]
        cont = cont - 1
        return soma_(lista, cont)
    else:
        return soma
    
soma = 0
lista = []
n = None
while n!=0:
        n = int(input("Digite um número: "))
        lista.append(n)
        
cont = len(lista) - 1
print(soma_(lista, cont))
