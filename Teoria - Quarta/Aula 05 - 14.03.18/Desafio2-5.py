print('-'*5,'Desafio 2','-'*5)
print("1")
print("")
print('-'*5,'Desafio 3','-'*5)
print("3")
print("")
print('-'*5,'Desafio 4','-'*5)
print("""0-35
1-15
2-50
3-45
4-28""")
print("")
print('-'*5,'Desafio 5','-'*5)
lista=[]
soma=0

n=None

while n != 0:
    n=int(input("Digite um numero inteiro: "))
    if n!=0:
        lista.append(n)
        soma = soma + n
        
print('Sua lista é: {}'.format(lista))
print('Sua Soma é: {}'.format(soma))

