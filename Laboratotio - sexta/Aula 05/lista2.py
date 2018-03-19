contador = 1
lista=[]

print("-"*5,"Menu","-"*5)
print("Digite (1) para cadastras um amigo no final da lista")
print("Digite (2) para Mostrar os nomes da lista")
print("Digite (3) para cadastrar um amigo no inicio da lista")
print("Digite (4) Remover um nome")
print("Digite (5) Substituir um nome")
print("Digite (6) para Mostrar os nomes da lista")
print("Digite (7) para Mostrar os nomes da lista")
print("Digite (8) para Sair do programa")

while contador==1:
    menu=int(input("Digite o numero de queseja do menu: "))
    if menu == 1:
        nome=input("Digite um nome que deseja ser inserido: ")
        lista.append(nome)
        print(lista)
        print("")
    elif menu == 2:
        print(lista)
        print("")

    elif menu == 3:
        nom=input("Digite um nome que deseja colocar primeiro: ")
        lista.insert(0,nom)
        print(lista)
        print("")

    elif menu == 4:
        local=int(input("Digite a posição(começando por 0) que deseja deletar o nome: "))
        del lista[local]
        print(lista)
        print("")

    elif menu == 5:
        sub=input("Digite o nome que deseja substituir: ")
        nu=int(input("Digite a posição que deseja substituir: ")) 
        lista[nu]=sub
        print(lista)
        print("")

    elif menu == 6:
        print(len(lista))
        print("")

    elif menu == 7:
        print(sorted(lista))
        print("")
    
    elif menu == 8:
        print("Fechando a lista!!")
        print(lista)
        contador -=1

    else:
        print("")
    
