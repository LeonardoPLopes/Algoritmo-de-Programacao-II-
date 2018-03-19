contador = 1
lista=[]

def append():
     nome=input("Digite um nome que deseja ser inserido: ")
     lista.append(nome)
     print(lista)
     print("")

def mostrar():
     print(lista)
     print("")

def inserir():
     nom=input("Digite um nome que deseja colocar primeiro: ")
     lista.insert(0,nom)
     print(lista)
     print("")

def deletar():
     local=int(input("Digite a posição(começando por 0) que deseja deletar o nome: "))
     del lista[local]
     print(lista)
     print("")

def substituir():
     sub=input("Digite o nome que deseja substituir: ")
     nu=int(input("Digite a posição que deseja substituir: ")) 
     lista[nu]=sub
     print(lista)
     print("")

def Mostrar_Numero():
     print(len(lista))
     print("")

def sort():
     print(sorted(lista))
     print("")

def saida():
     print("Fechando a lista!!")
     print(lista)
     contador -=1

def nada():
     print("")


while contador==1:
     print("-"*5,"Menu","-"*5)
     print("Digite (1) para cadastras um amigo no final da lista")
     print("Digite (2) para Mostrar os nomes da lista")
     print("Digite (3) para cadastrar um amigo no inicio da lista")
     print("Digite (4) Remover um nome")
     print("Digite (5) Substituir um nome")
     print("Digite (6) para Mostrar os nomes da lista")
     print("Digite (7) para Mostrar os nomes da lista")
     print("Digite (8) para Sair do programa")
     menu=int(input("Digite o numero de queseja do menu: "))
     if menu == 1:
          append()
     elif menu == 2:
          mostrar()

     elif menu == 3:
          inserir()

     elif menu == 4:
          deletar()

     elif menu == 5:
          substituir()

     elif menu == 6:
          Mostrar_Numero()

     elif menu == 7:
          sort()
    
     elif menu == 8:
          saida()

     else:
          nada()
    
