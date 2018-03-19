contador = 1
lista=[]

print("-"*5,"Menu","-"*5)
print("Digite (1) para cadastras um amigo no final da lista")
print("Digite (2) para Mostrar os nomes da lista")
print("Sair do programa")

while contador==1:
    menu=int(input("Digite o numero de queseja do menu: "))
    if menu == 1:
        nome=input("Digite um nome que deseja ser inserido: ")
        lista.append(nome)
        print(lista)
    elif menu == 2:
        print(lista)
    elif menu == 8:
        print("Fechando a lista!!")
        print(lista)
        contador -=1
    
